---
title: "Limited \"generics\" in C without macros or UB"
date: 2017-06-05
url: https://drewdevault.com/2017/06/05/Limited-generics-in-C.html
slug: Limited-generics-in-C
word_count: 382
---

I should start this post off by clarifying that what I have to show you today is
not, in fact, generics. However, it’s useful in some situations to solve the
same problems that generics might. This is a pattern I’ve started using to
reduce the number of  `void*`  pointers floating around in my code: multiple
definitions of a struct.

**Errata** : we rolled this approach back in wlroots because it causes problems
with LTO. I no longer recommend it.

Let’s take a look at a specific example. In
 [wlroots](https://github.com/SirCmpwn/wlroots) ,  `wlr_output`  is a generic type
that can be implemented by any number of backends, like DRM (direct rendering
manager), wayland windows, X11 windows, RDP outputs, etc. The  `wlr/types.h` 
header includes this structure:

```
struct wlr_output_impl;
struct wlr_output_state;

struct wlr_output {
    const struct wlr_output_impl *impl;
    struct wlr_output_state *state;
    // [...]
};

void wlr_output_enable(struct wlr_output *output, bool enable);
bool wlr_output_set_mode(struct wlr_output *output,
    struct wlr_output_mode *mode);
void wlr_output_destroy(struct wlr_output *output);
```

`wlr_output_impl`  is defined elsewhere:

```
struct wlr_output_impl {
    void (*enable)(struct wlr_output_state *state, bool enable);
    bool (*set_mode)(struct wlr_output_state *state,
        struct wlr_output_mode *mode);
    void (*destroy)(struct wlr_output_state *state);
};

struct wlr_output *wlr_output_create(struct wlr_output_impl *impl,
        struct wlr_output_state *state);
void wlr_output_free(struct wlr_output *output);
```

Nowhere, however, is  `wlr_output_state`  defined. It’s left an incomplete type
throughout all of the common  `wlr_output`  code. The “generic” part is that each
output implementation, in its own private headers, defines the
 `wlr_output_state`  struct for itself, like the DRM backend:

```
struct wlr_output_state {
    uint32_t connector;
    char name[16];
    uint32_t crtc;
    drmModeCrtc *old_crtc;
    struct wlr_drm_renderer *renderer;
    struct gbm_surface *gbm;
    EGLSurface *egl;
    bool pageflip_pending;
    enum wlr_drm_output_state state;
    // [...]
};
```

This allows implementations of the  `enable` ,  `set_mode` , and  `destroy`  functions
to avoid casting a  `void*`  to the appropriate type:

```
static struct wlr_output_impl output_impl = {
    .enable = wlr_drm_output_enable,
    // [...]
};

static void wlr_drm_output_enable(struct wlr_output_state *output,
        bool enable) {
    struct wlr_backend_state *state =
        wl_container_of(output->renderer, state, renderer);
    if (output->state != DRM_OUTPUT_CONNECTED) {
        return;
    }
    if (enable) {
        drmModeConnectorSetProperty(state->fd,
            output->connector,
            output->props.dpms,
            DRM_MODE_DPMS_ON);
        // [...]
    } else {
        drmModeConnectorSetProperty(state->fd,
            output->connector,
            output->props.dpms,
            DRM_MODE_DPMS_STANDBY);
    }
}

// [...]
struct wlr_output output = wlr_output_create(&output_impl, output);
```

The limitations of this approach are apparent: you cannot work with multiple
definitions of  `wlr_output_state`  in the same file. However, you get improved
type safety, have to write less code, and improve readability.
