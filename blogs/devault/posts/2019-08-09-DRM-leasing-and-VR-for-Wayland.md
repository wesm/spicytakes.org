---
title: "DRM leasing: VR for Wayland"
date: 2019-08-09
url: https://drewdevault.com/2019/08/09/DRM-leasing-and-VR-for-Wayland.html
slug: DRM-leasing-and-VR-for-Wayland
word_count: 2425
---

As those who read my  [status updates](/2019/07/15/Status-update-July-2019.html) 
have been aware, recently I’ve been working on bringing VR to Wayland (and vice
versa). The deepest and most technical part of this work is  *DRM leasing* 
(Direct Rendering Manager,  *not*  Digital Restrictions Management), and I think
it’d be good to write in detail about what’s involved in this part of the
effort. This work has been sponsored by  [Status.im](https://status.im/) , as part
of an effort to build a comprehensive Wayland-driven VR workspace. When we got
started, most of the plumbing was missing for VR headsets to be useful on
Wayland, so this has been my focus for a while. The result of this work is
summed up in this crappy handheld video:

Keith Packard, a long time Linux graphics developer,  [wrote several blog posts
documenting his work implementing this feature for
X11](https://keithp.com/blogs/DRM-lease/) . My journey was somewhat similar,
though thanks to his work I was able to save a lot of time. The rub of this idea
is that the Wayland compositor, the DRM (Direct Rendering Manager) master, can
“lease” some of its resources to a client so they can drive your display
directly. DRM is the kernel subsystem we use for enumerating and setting modes,
allocating pixel buffers, and presenting them in sync with the display’s refresh
rate. For a number of reasons, minimizing latency being an important one, VR
applications prefer to do these tasks directly rather than be routed through the
display server like most applications are. The main tasks for implementing this
for Wayland were:

1. Draft a  [protocol extension](https://lists.freedesktop.org/archives/wayland-devel/2019-July/040768.html)  for issuing DRM leases
2. Write implementations for  [wlroots](https://github.com/swaywm/wlroots/pull/1730)  and  [sway](https://github.com/swaywm/sway/pull/4289)
3. Get a  [simple test client](https://git.sr.ht/~sircmpwn/kmscube)  working
4. Draft a Vulkan extension for leasing via Wayland
5. Write an implementation for  [Mesa’s Vulkan WSI implementation](https://gitlab.freedesktop.org/mesa/mesa/merge_requests/1509)
6. Get a more complex  [Vulkan test client](https://git.sr.ht/~sircmpwn/xrgears)  working
7. Add support to  [Xwayland](https://gitlab.freedesktop.org/xorg/xserver/merge_requests/248)

Let’s break down exactly what was necessary for each of these steps.

## Wayland protocol extension

Writing a protocol extension was the first order of business. There was an
 [earlier attempt](https://lists.freedesktop.org/archives/wayland-devel/2018-January/036652.html)  which petered off in January. I started
with this, by cleaning it up based on my prior experience writing protocols,
normalizing much of the terminology and style, and cleaning up the state
management. After some initial rounds of review, there were some questions to
answer. The most important ones were:

* How do we identify the display? Should we send the EDID, which may be
bigger than the maximum size of a Wayland message?
* Are there security concerns? Could malicious clients read from framebuffers
they weren’t given a lease for?

The EDID I ended up sending in a side channel (file descriptor to shared
memory), and the latter was proven to be a non-issue by writing a malicious
client and demonstrating that the kernel rejects its attempts to do evil.

```
<event name="edid">
  <description summary="edid">
    The compositor may send this event once the connector is created to
    provide a file descriptor which may be memory-mapped to read the
    connector's EDID, to assist in selecting the correct connectors
    for lease. The fd must be mapped with MAP_PRIVATE by the recipient.

    Note that not all displays have an EDID, and this event will not be
    sent in such cases.
  </description>
  <arg name="edid" type="fd" summary="EDID file descriptor" />
  <arg name="size" type="uint" summary="EDID size, in bytes"/>
</event> 
```

A few more changes would happen to this protocol in the following weeks, but
this was good enough to move on to…

## wlroots & sway implementation

After a chat with Scott Anderson (the maintainer of DRM support in wlroots) and
thanks to his timely refactoring efforts, the stage was well set for introducing
this feature to wlroots. I had a good idea of how it would take shape.  [Half of
the work](https://github.com/swaywm/wlroots/pull/1730/files#diff-77b17feac8a8af251811a20e5b9bbdd1)  - the state machine which maintains the server-side
view of the protocol - is well trodden ground and was fairly easy to put
together. Despite being a well-understood problem in the wlroots codebase, these
state machines are always a bit tedious to implement correctly, and I was still
to flushing out bugs well into the remainder of this workstream.

The other half of this work was in  [the DRM subsystem](https://github.com/swaywm/wlroots/pull/1730/files#diff-8b05a774317ee8e87d51422170f82d4b) . We
decided that we’d have leased connectors appear “destroyed” to the compositor,
and thus the compositor would have an opportunity to clean it up and stop using
them, similar to the behavior of when an output is hotplugged. Further changes
were necessary to have the DRM internals elegantly carry around some state for
the leased connector and avoid using the connector itself, as well as dealing
with the termination of the lease (either by the client or by the compositor).
With all of this in place, it’s a  [simple matter](https://github.com/swaywm/wlroots/pull/1730/files#diff-8b05a774317ee8e87d51422170f82d4bR1601)  to enumerate
the DRM object IDs for all of the resources we intend to lease and issue the
lease itself.

```
int nobjects = 0;
for (int i = 0; i < nconns; ++i) {
	struct wlr_drm_connector *conn = conns[i];
	assert(conn->state != WLR_DRM_CONN_LEASED);
	nobjects += 0
		+ 1 /* connector */
		+ 1 /* crtc */
		+ 1 /* primary plane */
		+ (conn->crtc->cursor != NULL ? 1 : 0) /* cursor plane */
		+ conn->crtc->num_overlays; /* overlay planes */
}
if (nobjects <= 0) {
	wlr_log(WLR_ERROR, "Attempted DRM lease with <= 0 objects");
	return -1;
}
wlr_log(WLR_DEBUG, "Issuing DRM lease with the %d objects:", nobjects);
uint32_t objects[nobjects + 1];
for (int i = 0, j = 0; i < nconns; ++i) {
	struct wlr_drm_connector *conn = conns[i];
	objects[j++] = conn->id;
	objects[j++] = conn->crtc->id;
	objects[j++] = conn->crtc->primary->id;
	wlr_log(WLR_DEBUG, "connector: %d crtc: %d primary plane: %d",
			conn->id, conn->crtc->id, conn->crtc->primary->id);
	if (conn->crtc->cursor) {
		wlr_log(WLR_DEBUG, "cursor plane: %d", conn->crtc->cursor->id);
		objects[j++] = conn->crtc->cursor->id;
	}
	if (conn->crtc->num_overlays > 0) {
		wlr_log(WLR_DEBUG, "+%zd overlay planes:", conn->crtc->num_overlays);
	}
	for (size_t k = 0; k < conn->crtc->num_overlays; ++k) {
		objects[j++] = conn->crtc->overlays[k];
		wlr_log(WLR_DEBUG, "\toverlay plane: %d", conn->crtc->overlays[k]);
	}
}
int lease_fd = drmModeCreateLease(backend->fd,
		objects, nobjects, 0, lessee_id);
if (lease_fd < 0) {
	return lease_fd;
}
wlr_log(WLR_DEBUG, "Issued DRM lease %d", *lessee_id);
for (int i = 0; i < nconns; ++i) {
	struct wlr_drm_connector *conn = conns[i];
	conn->lessee_id = *lessee_id;
	conn->crtc->lessee_id = *lessee_id;
	conn->state = WLR_DRM_CONN_LEASED;
	conn->lease_terminated_cb = lease_terminated_cb;
	conn->lease_terminated_data = lease_terminated_data;
	wlr_output_destroy(&conn->output);
}
return lease_fd;
```

The  [sway implementation](https://github.com/swaywm/sway/pull/4289)  is very simple. I added a note in wlroots
which exposes whether or not an output is considered “non-desktop” (a property
which is set for most VR headsets), then sway just rigs up the lease manager and
offers all non-desktop outputs for lease.

## kmscube

Testing all of this required the use of a simple test client. During his earlier
work, Keith wrote some patches on top of
 [kmscube](https://gitlab.freedesktop.org/mesa/kmscube/) , a simple Mesa demo
which renders a spinning cube directly via DRM/KMS/GBM. A  [few simple
tweaks](https://git.sr.ht/~sircmpwn/kmscube/commit/60d89ef1d9304427a1289174d9a311ab06e39b44)  was suitable to get this working through my protocol
extension, and for the first time I saw something rendered on my headset through
sway!

## Vulkan

Vulkan has a subsystem called WSI - Window System Integration - which handles
the linkage between Vulkan’s rendering process and the underlying window system,
such as Wayland, X11, or win32. Keith added an extension to this system called
 [VK_EXT_acquire_xlib_display](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/vkspec.html#VK_EXT_acquire_xlib_display) , which lives on top
of  [VK_EXT_direct_mode_display](https://www.khronos.org/registry/vulkan/specs/1.1-extensions/html/vkspec.html#VK_EXT_direct_mode_display) , a system for
driving displays directly with Vulkan. As the name implies, this system is
especially X11-specific, so I’ve drafted my own VK extension for Wayland:
VK_EXT_acquire_wl_display. This is the crux of it:

```
<command successcodes="VK_SUCCESS" errorcodes="VK_ERROR_INITIALIZATION_FAILED">
  <proto><type>VkResult</type> <name>vkAcquireWaylandDisplayEXT</name></proto>
  <param><type>VkPhysicalDevice</type> <name>physicalDevice</name></param>
  <param>struct <type>wl_display</type>* <name>display</name></param>
  <param>struct <type>zwp_drm_lease_manager_v1</type>* <name>manager</name></param>
  <param><type>int</type> <name>nConnectors</name></param>
  <param><type>VkWaylandLeaseConnectorEXT</type>* <name>pConnectors</name></param>
</command>
```

I chose to leave it up to the user to enumerate the leasable connectors from the
Wayland protocol, then populate these structs with references to the connectors
they want to lease:

```
<type category="struct" name="VkWaylandLeaseConnectorEXT">
  <member>struct <type>zwp_drm_lease_connector_v1</type>* <name>pConnectorIn</name></member>
  <member><type>VkDisplayKHR</type> <name>displayOut</name></member>
</type>
```

Again, this was the result of some iteration and design discussions with other
folks knowledgable in these topics. I owe special thanks to Daniel Stone for
sitting down with me (figuratively, on IRC) and going over ideas for how to
design the Vulkan API. Armed with this specification, I now needed a Vulkan
driver which supported it.

## Implementing the VK extension in Mesa

[Mesa](https://www.mesa3d.org/)  is the premier free software graphics suite
powering graphics on Linux and other operating systems. It includes an
implementation of OpenGL and Vulkan for several GPU vendors, and is the home of
the userspace end of AMDGPU, Intel, nouveau, and other graphics drivers. A
specification is nothing without its implementation, so I set out to
implementing this extension for Mesa. In the end, it turned out to be much
simpler than the corresponding X version. This is the complete code for the WSI
part of this feature:

```
static void drm_lease_handle_lease_fd(
      void *data,
      struct zwp_drm_lease_v1 *zwp_drm_lease_v1,
      int32_t leased_fd)
{
   struct wsi_display *wsi = data;
   wsi->fd = leased_fd;
}

static void drm_lease_handle_finished(
      void *data,
      struct zwp_drm_lease_v1 *zwp_drm_lease_v1)
{
   struct wsi_display *wsi = data;
   if (wsi->fd > 0) {
      close(wsi->fd);
      wsi->fd = -1;
   }
}

static const struct zwp_drm_lease_v1_listener drm_lease_listener = {
   drm_lease_handle_lease_fd,
   drm_lease_handle_finished,
};

/* VK_EXT_acquire_wl_display */
VkResult
wsi_acquire_wl_display(VkPhysicalDevice physical_device,
                       struct wsi_device *wsi_device,
                       struct wl_display *display,
                       struct zwp_drm_lease_manager_v1 *manager,
                       int nConnectors,
                       VkWaylandLeaseConnectorEXT *connectors)
{
   struct wsi_display *wsi =
      (struct wsi_display *) wsi_device->wsi[VK_ICD_WSI_PLATFORM_DISPLAY];

   /* XXX no support for mulitple leases yet */
   if (wsi->fd >= 0)
      return VK_ERROR_INITIALIZATION_FAILED;

   /* XXX no support for mulitple connectors yet */
   /* The solution will eventually involve adding a listener to each
    * connector, round tripping, and matching EDIDs once the lease is
    * granted. */
   if (nConnectors > 1)
      return VK_ERROR_INITIALIZATION_FAILED;

   struct zwp_drm_lease_request_v1 *lease_request =
      zwp_drm_lease_manager_v1_create_lease_request(manager);
   for (int i = 0; i < nConnectors; ++i) {
      zwp_drm_lease_request_v1_request_connector(lease_request,
                                                 connectors[i].pConnectorIn);
   }

   struct zwp_drm_lease_v1 *drm_lease =
      zwp_drm_lease_request_v1_submit(lease_request);
   zwp_drm_lease_request_v1_destroy(lease_request);
   zwp_drm_lease_v1_add_listener(drm_lease, &drm_lease_listener, wsi);
   wl_display_roundtrip(display);

   if (wsi->fd < 0)
      return VK_ERROR_INITIALIZATION_FAILED;

   int nconn = 0;
   drmModeResPtr res = drmModeGetResources(wsi->fd);
   drmModeObjectListPtr lease = drmModeGetLease(wsi->fd);
   for (uint32_t i = 0; i < res->count_connectors; ++i) {
      for (uint32_t j = 0; j < lease->count; ++j) {
         if (res->connectors[i] != lease->objects[j]) {
            continue;
         }
         struct wsi_display_connector *connector =
            wsi_display_get_connector(wsi_device, res->connectors[i]);
         /* TODO: Match EDID with requested connector */
         connectors[nconn].displayOut =
            wsi_display_connector_to_handle(connector);
         ++nconn;
      }
   }
   drmModeFreeResources(res);

   return VK_SUCCESS;
}
```

Rigging it up to each driver’s WSI shim is pretty straightforward from this
point. I only did it for radv - AMD’s Vulkan driver (cause that’s the hardware I
was using at the time) - but the rest should be trivial to add. Equipped with a
driver in hand, it’s time to make a Real VR Application work on Wayland.

## xrgears

[xrgears](https://gitlab.com/lubosz/xrgears)  is another simple demo application
like kmscube - but designed to render a VR scene. It leverages Vulkan and
 [OpenHMD](http://www.openhmd.net/)  (Open Head Mounted Display) to display this
scene and stick the camera to your head. With the Vulkan extension implemented,
it was a fairly simple matter to  [rig up a Wayland backend](https://git.sr.ht/~sircmpwn/xrgears/commit/41ef1d1dfe3e56766d1f8b72b335567eb7842d04) . The
result:

## Xwayland

The final step was to integrate this extension with Xwayland, so that X
applications which took advantage of Keith’s work would work via Xwayland. This
ended up being more difficult than I expected for one reason in particular:
modes. Keith’s Vulkan extension is designed in two steps:

1. Convert an RandR output into a VkDisplayKHR
2. Acquire a lease for a set of VkDisplayKHRs

Between these steps, you can query the modes (available resolutions and refresh
rates) of the display. However, the Wayland protocol I designed does not let you
query modes until  *after*  you get the DRM handle, at which point you should
query them through DRM, thus reducing the number of sources of truth and
simplifying things considerably. This is arguably a design misstep in the
original Vulkan extension, but it’s shipped in a lot of software and is beyond
fixing. So how do we deal with it?

One way (which was suggested at one point) would be to change the protocol to
include the relevant mode information, so that Xwayland could populate the RandR
modes from it. I found this distasteful, because it was making the protocol more
complex for the sake of a legacy system. Another option would be to make a
second protocol which includes this extra information especially for Xwayland,
but this also seemed like a compromise that compositors would rather not make.
Yet another option would be to have Xwayland request a lease with zero objects
and scan connectors itself, but zero-object leases are not possible.

The option I ended up going with is to have Xwayland open the DRM device itself
and scan connectors there. This is less palatable because (1) we can’t be sure
which DRM device is correct, and (2) we can’t be sure Xwayland will have
permission to read it. We’re still not sure how best to solve this in the long
term. As it stands, this approach is sufficient to get it working in the common
case. The code looks something like this:

```
static RRModePtr *
xwl_get_rrmodes_from_connector_id(int32_t connector_id, int *nmode, int *npref)
{
    drmDevicePtr devices[1];
    drmModeConnectorPtr conn;
    drmModeModeInfoPtr kmode;
    RRModePtr *rrmodes;
    int drm;
    int pref, i;

    *nmode = *npref = 0;

    /* TODO: replace with zero-object lease once kernel supports them */
    if (drmGetDevices2(DRM_NODE_PRIMARY, devices, 1) < 1
            || !*devices[0]->nodes[0]) {
        ErrorF("Failed to enumerate DRM devices");
        return NULL;
    }
    drm = open(devices[0]->nodes[0], O_RDONLY);
    drmFreeDevices(devices, 1);

    conn = drmModeGetConnector(drm, connector_id);
    if (!conn) {
        close(drm);
        ErrorF("drmModeGetConnector failed");
        return NULL;
    }
    rrmodes = xallocarray(conn->count_modes, sizeof(RRModePtr));
    if (!rrmodes) {
        close(drm);
        ErrorF("Failed to allocate connector modes");
        return NULL;
    }

    /* This spaghetti brought to you courtesey of xf86RandrR12.c
     * It adds preferred modes first, then non-preferred modes */
    for (pref = 1; pref >= 0; pref--) {
        for (i = 0; i < conn->count_modes; ++i) {
            kmode = &conn->modes[i];
            if ((pref != 0) == ((kmode->type & DRM_MODE_TYPE_PREFERRED) != 0)) {
                xRRModeInfo modeInfo;
                RRModePtr rrmode;

                modeInfo.nameLength = strlen(kmode->name);

                modeInfo.width = kmode->hdisplay;
                modeInfo.dotClock = kmode->clock * 1000;
                modeInfo.hSyncStart = kmode->hsync_start;
                modeInfo.hSyncEnd = kmode->hsync_end;
                modeInfo.hTotal = kmode->htotal;
                modeInfo.hSkew = kmode->hskew;

                modeInfo.height = kmode->vdisplay;
                modeInfo.vSyncStart = kmode->vsync_start;
                modeInfo.vSyncEnd = kmode->vsync_end;
                modeInfo.vTotal = kmode->vtotal;
                modeInfo.modeFlags = kmode->flags;

                rrmode = RRModeGet(&modeInfo, kmode->name);
                if (rrmode) {
                    rrmodes[*nmode] = rrmode;
                    *nmode = *nmode + 1;
                    *npref = *npref + pref;
                }
            }
        }
    }

    close(drm);
    return rrmodes;
}
```

A simple update to the Wayland protocol was necessary to add the  `CONNECTOR_ID` 
atom to the RandR output, which is used by Mesa’s Xlib WSI code for acquiring
the display, and was reused here to line up a connector offered by the Wayland
compositor with a connector found in the kernel. The  [rest of the
changes](https://gitlab.freedesktop.org/xorg/xserver/merge_requests/248)  were pretty simple, and the result is that SteamVR works,
capping everything off nicely:
