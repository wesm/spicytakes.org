---
title: "Writing a Wayland Compositor, Part 2: Rigging up the server"
date: 2018-02-22
url: https://drewdevault.com/2018/02/22/Writing-a-wayland-compositor-part-2.html
slug: Writing-a-wayland-compositor-part-2
word_count: 790
---

This is the second in a series of articles on the subject of writing a Wayland
compositor from scratch using  [wlroots](https://github.com/swaywm/wlroots) .
Check out  [the first article](/2018/02/17/Writing-a-Wayland-compositor-1.html) 
if you haven’t already. Last time, we ended up with an application which fired
up a wlroots backend, enumerated output devices, and drew some pretty colors on
the screen. Today, we’re going to start accepting Wayland client connections,
though we aren’t going to be doing much with them yet.

The commit that this article dissects is
 [b45c651](https://github.com/SirCmpwn/mcwayland/commit/b45c651) .

A quick aside on the nature of these blog posts: it’s going to take  *a lot*  of
these articles to flesh out our compositor. I’m going to be publishing these
more frequently than usual, probably 1-2 per week, and continue posting my usual
articles at the typical rate. Okay? Cool.

So we’ve started up the backend and we’re rendering something interesting, but
we still aren’t running a Wayland server – Wayland clients aren’t connecting to
our application. Adding this is actually quite easy:

```
@@ -113,12 +113,18 @@ int main(int argc, char **argv) {
        server.new_output.notify = new_output_notify;
        wl_signal_add(&server.backend->events.new_output, &server.new_output);
 
+       const char *socket = wl_display_add_socket_auto(server.wl_display);
+       assert(socket);
+
        if (!wlr_backend_start(server.backend)) {
                fprintf(stderr, "Failed to start backend\n");
                wl_display_destroy(server.wl_display);
                return 1;
        }
 
+       printf("Running compositor on wayland display '%s'\n", socket);
+       setenv("WAYLAND_DISPLAY", socket, true);
+
        wl_display_run(server.wl_display);
        wl_display_destroy(server.wl_display);
        return 0;
```

That’s it! If you run McWayface again, it’ll print something like this:

```
Running compositor on wayland display 'wayland-1'
```

[Weston](https://cgit.freedesktop.org/wayland/weston/) , the Wayland reference
compositor, includes a number of simple reference clients. We can use
 `weston-info`  to connect to our server and list the  **globals** :

```
$ WAYLAND_DISPLAY=wayland-1 weston-info
interface: 'wl_drm', version: 2, name: 1
```

If you recall from my  [Introduction to
Wayland](/2017/06/10/Introduction-to-Wayland.html) , the Wayland server exports a
list of  **globals**  to clients via the Wayland registry. These globals provide
interfaces the client can utilize to interact with the server. We get  `wl_drm` 
for free with wlroots, but we have not actually wired up anything useful yet.
Wlroots provides many “types”, of which the majority are implementations of
Wayland global interfaces like this.

Some of the wlroots implementations require some rigging from you, but several
of them just take care of themselves. Rigging these up is easy:

```
        printf("Running compositor on wayland display '%s'\n", socket);
        setenv("WAYLAND_DISPLAY", socket, true);
+
+       wl_display_init_shm(server.wl_display);
+       wlr_gamma_control_manager_create(server.wl_display);
+       wlr_screenshooter_create(server.wl_display);
+       wlr_primary_selection_device_manager_create(server.wl_display);
+       wlr_idle_create(server.wl_display);
 
        wl_display_run(server.wl_display);
        wl_display_destroy(server.wl_display);
```

Note that some of these interfaces are not necessarily ones that you typically
would want to expose to all Wayland clients - screenshooter, for example, is
something that should be secured. We’ll get to security in a later article. For
now, if we run  `weston-info`  again, we’ll see a few more globals have appeared:

```
$ WAYLAND_DISPLAY=wayland-1 weston-info
interface: 'wl_shm', version: 1, name: 3
	formats: XRGB8888 ARGB8888
interface: 'wl_drm', version: 2, name: 1
interface: 'gamma_control_manager', version: 1, name: 2
interface: 'orbital_screenshooter', version: 1, name: 3
interface: 'gtk_primary_selection_device_manager', version: 1, name: 4
interface: 'org_kde_kwin_idle', version: 1, name: 5
```

You’ll find that wlroots implements a variety of protocols from a variety of
sources - here we see protocols from Orbital, GTK, and KDE represented. Wlroots
includes an example client for the orbital screenshooter - we can use it now to
take a screenshot of our compositor:

```
$ WAYLAND_DISPLAY=wayland-1 ./examples/screenshot
cannot set buffer size
```

Ah, this is a problem - you may have noticed that we don’t have any wl_output
globals, which the screenshooter client relies on to figure out the resolution
of the screenshot buffer. We can add these, too:

```
@@ -95,6 +99,8 @@ static void new_output_notify(struct wl_listener *listener, void *data) {
        wl_signal_add(&wlr_output->events.destroy, &output->destroy);
        output->frame.notify = output_frame_notify;
        wl_signal_add(&wlr_output->events.frame, &output->frame);
+
+       wlr_output_create_global(wlr_output);
 }
```

Running  `weston-info`  again will give us some info about our outputs now:

```
$ WAYLAND_DISPLAY=wayland-1 weston-info
interface: 'wl_drm', version: 2, name: 1
interface: 'wl_output', version: 3, name: 2
	x: 0, y: 0, scale: 1,
	physical_width: 0 mm, physical_height: 0 mm,
	make: 'wayland', model: 'wayland',
	subpixel_orientation: unknown, output_transform: normal,
	mode:
		width: 952 px, height: 521 px, refresh: 0.000 Hz,
		flags: current
interface: 'wl_shm', version: 1, name: 3
	formats: XRGB8888 ARGB8888
interface: 'gamma_control_manager', version: 1, name: 4
interface: 'orbital_screenshooter', version: 1, name: 5
interface: 'gtk_primary_selection_device_manager', version: 1, name: 6
interface: 'org_kde_kwin_idle', version: 1, name: 7
```

Now we can take that screenshot! Give it a shot (heh)!

We’re getting close to the good stuff now. The next article is going to
introduce the concept of  **surfaces** , and we will use them to render our first
window. If you had any trouble with this article, please reach out to me at
 [sir@cmpwn.com](mailto:sir@cmpwn.com)  or to the wlroots team at
 [#sway-devel](http://webchat.freenode.net/?channels=sway-devel&uio=d4) .

Next —
     [
        Part 3: Rendering a window
    ](/2018/02/28/Writing-a-wayland-compositor-part-3.html)

Previous —
     [
        Part 1: Hello wlroots
    ](/2018/02/17/Writing-a-Wayland-compositor-1.html)
