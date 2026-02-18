---
title: "Writing a Wayland Compositor, Part 1: Hello wlroots"
date: 2018-02-17
url: https://drewdevault.com/2018/02/17/Writing-a-Wayland-compositor-1.html
slug: Writing-a-Wayland-compositor-1
word_count: 2027
---

This is the first in a series of  *many*  articles I’m writing on the subject of
building a functional Wayland compositor from scratch. As you may know, I am the
lead maintainer of  [sway](https://github.com/swaywm/sway) , a reasonably popular
Wayland compositor. Along with many other talented developers, we’ve been
working on  [wlroots](https://github.com/swaywm/wlroots)  over the past few
months. This is a powerful tool for creating new Wayland compositors, but it is
very dense and difficult to understand. Do not despair! The intention of these
articles is to make you understand and feel comfortable using it.

Before we dive in, a quick note: the wlroots team is starting a crowdfunding
campaign today to fund travel for each of our core contributors to meet in
person and work for two weeks on a hackathon. Please consider contributing to
 [the campaign](https://www.indiegogo.com/projects/sway-hackathon-software/x/1059863) !

You  **must**  read and comprehend my earlier article,  [An introduction to
Wayland](/2017/06/10/Introduction-to-Wayland.html) , before attempting to
understand this series of blog posts, as I will be relying on concepts and
terminology introduced there to speed things up. Some background in OpenGL is
helpful, but not required. A good understanding of C is mandatory. If you have
any questions about any of the articles in this series, please reach out to me
directly via  [sir@cmpwn.com](mailto:sir@cmpwn.com)  or to the wlroots team at
 [#sway-devel on irc.freenode.net](http://webchat.freenode.net/?channels=sway-devel&uio=d4) .

During this series of articles, the compositor we’re building will live on
GitHub:  [Wayland McWayface](https://github.com/SirCmpwn/mcwayface) . Each article
in this series will be presented as a breakdown of a single commit between zero
and a fully functional Wayland compositor. The commit for this article is
 [f89092e](https://github.com/SirCmpwn/mcwayland/commit/f89092e) .
I’m only going to explain the important parts - I suggest you review
the entire commit separately.

Let’s get started. First, I’m going to define a struct for holding our
compositor’s state:

```
+struct mcw_server {
+       struct wl_display *wl_display;
+       struct wl_event_loop *wl_event_loop;
+};
```

Note: mcw is short for McWayface. We’ll be using this acronym throughout the
article series. We’ll set one of these aside and initialize the Wayland display
for it 1 :

```
 int main(int argc, char **argv) {
+       struct mcw_server server;
+
+       server.wl_display = wl_display_create();
+       assert(server.wl_display);
+       server.wl_event_loop = wl_display_get_event_loop(server.wl_display);
+       assert(server.wl_event_loop);
        return 0;
 }
```

The Wayland display gives us a number of things, but for now all we care about
is the event loop. This event loop is deeply integrated into wlroots, and is
used for things like dispatching signals across the application, being notified
when data is available on various file descriptors, and so on.

Next, we need to create the backend:

```
 struct mcw_server {
        struct wl_display *wl_display;
        struct wl_event_loop *wl_event_loop;
 
+       struct wlr_backend *backend;
 };
```

The  **backend**  is our first wlroots concept. The backend is responsible for
abstracting the low level  *input*  and  *output*  implementations from you. Each
backend can generate zero or more input devices (such as mice, keyboards, etc)
and zero or more output devices (such as monitors on your desk). Backends have
nothing to do with Wayland - their purpose is to help you with the  *other*  APIs
you need to use as a Wayland compositor. There are various backends with various
purposes:

* The  **drm**  backend utilizes the Linux DRM subsystem to render directly to
your physical displays.
* The  **libinput**  backend utilizes libinput to enumerate and control physical
input devices.
* The  **wayland**  backend creates “outputs” as windows on another running
Wayland compositors, allowing you to nest compositors. Useful for debugging.
* The  **x11**  backend is similar to the Wayland backend, but opens an x11 window
on an x11 server rather than a Wayland window on a Wayland server.

Another important backend is the  **multi**  backend, which allows you to
initialize several backends at once and aggregate their input and output
devices. This is necessary, for example, to utilize both drm and libinput
simultaneously.

wlroots provides a helper function for automatically choosing the most
appropriate backend based on the user’s environment:

```
        server.wl_event_loop = wl_display_get_event_loop(server.wl_display);
        assert(server.wl_event_loop);
 
+       server.backend = wlr_backend_autocreate(server.wl_display);
+       assert(server.backend);
        return 0;
 }
```

I would generally suggest using either the Wayland or X11 backends during
development, especially before we have a way of exiting the compositor. If you
call  `wlr_backend_autocreate`  from a running Wayland or X11 session, the
respective backends will be automatically chosen.

We can now start the backend and enter the Wayland event loop:

```
+       if (!wlr_backend_start(server.backend)) {
+               fprintf(stderr, "Failed to start backend\n");
+               wl_display_destroy(server.wl_display);
+               return 1;
+       }
+
+       wl_display_run(server.wl_display);
+       wl_display_destroy(server.wl_display);
        return 0;
```

If you run your compositor at this point, you should see the backend start up
and… do nothing. It’ll open a window if you run from a running Wayland or X11
server. If you run it on DRM, it’ll probably do very little and you won’t even
be able to switch to another TTY to kill it.

In order to render something, we need to know about the outputs we can render
on. The backend provides a  **wl_signal**  that notifies us when it gets a new
output. This will happen on startup and as any outputs are hotplugged at
runtime.

Let’s add this to our server struct:

```
 struct mcw_server {
        struct wl_display *wl_display;
        struct wl_event_loop *wl_event_loop;
 
        struct wlr_backend *backend;
+
+       struct wl_listener new_output;
+
+       struct wl_list outputs; // mcw_output::link
 };
```

This adds a  `wl_listeners`  which is signalled when new outputs are added. We
also add a  `wl_list`  (which is just a linked list provided by libwayland-server)
which we’ll later store some state in. To be notified, we must use
 `wl_signal_add` :

```
        assert(server.backend);
 
+       wl_list_init(&server.outputs);
+
+       server.new_output.notify = new_output_notify;
+       wl_signal_add(&server.backend->events.new_output, &server.new_output);
 
        if (!wlr_backend_start(server.backend)) {
```

We specify here the function to be notified,  `new_output_notify` :

```
+static void new_output_notify(struct wl_listener *listener, void *data) {
+       struct mcw_server *server = wl_container_of(
+                       listener, server, new_output);
+       struct wlr_output *wlr_output = data;
+
+       if (!wl_list_empty(&wlr_output->modes)) {
+               struct wlr_output_mode *mode =
+                       wl_container_of(wlr_output->modes.prev, mode, link);
+               wlr_output_set_mode(wlr_output, mode);
+       }
+
+       struct mcw_output *output = calloc(1, sizeof(struct mcw_output));
+       clock_gettime(CLOCK_MONOTONIC, &output->last_frame);
+       output->server = server;
+       output->wlr_output = wlr_output;
+       wl_list_insert(&server->outputs, &output->link);
+}
```

This is a little bit complicated! This function has several roles when dealing
with the incoming  `wlr_output` . When the signal is raised, a pointer to the
listener that was signaled is passed in, as well as the  `wlr_output`  which was
created.  `wl_container_of`  uses some  `offsetof` -based magic to get the
 `mcw_server`  reference from the listener pointer, and we cast  `data`  to the
actual type,  `wlr_output` .

The next thing we have to do is set the  **output mode** . Some backends (notably
x11 and Wayland) do not support modes, but they are necessary for DRM. Output
modes specify a size and refresh rate supported by the output, such as
 `1920x1080@60Hz` . The body of this if statement just chooses the last one (which
is usually the highest resolution and refresh rate) and applies it to the output
with  `wlr_output_set_mode` . We  *must*  set the output mode in order to render to
it.

Then, we set up some state for us to keep track of this output with in our
compositor. I added this struct definition at the top of the file:

```
+struct mcw_output {
+       struct wlr_output *wlr_output;
+       struct mcw_server *server;
+       struct timespec last_frame;
+
+       struct wl_list link;
+};
```

This will be the structure we use to store any state we have for this output
that is specific to our compositor’s needs. We include a reference to the
 `wlr_output` , a reference to the  `mcw_server`  that owns this output, and the
time of the last frame, which will be useful later. We also set aside a
 `wl_list` , which is used by libwayland for linked lists.

Finally, we add this output to the server’s list of outputs.

We could use this now, but it would leak memory. We also need to handle output
 *removal* , with a signal provided by wlr_output. We add the listener to the
mcw_output struct:

```
 struct mcw_output {
        struct wlr_output *wlr_output;
        struct mcw_server *server;
        struct timespec last_frame;
+
+       struct wl_listener destroy;
 
        struct wl_list link;
 };
```

Then we hook it up when the output is added:

```
         wl_list_insert(&server->outputs, &output->link);

+        output->destroy.notify = output_destroy_notify;
+        wl_signal_add(&wlr_output->events.destroy, &output->destroy);
 }
```

This will call our output_destroy_notify function to handle cleanup when the
output is unplugged or otherwise removed from wlroots. Our handler looks like
this:

```
+static void output_destroy_notify(struct wl_listener *listener, void *data) {
+        struct mcw_output *output = wl_container_of(listener, output, destroy);
+        wl_list_remove(&output->link);
+        wl_list_remove(&output->destroy.link);
+        wl_list_remove(&output->frame.link);
+        free(output);
+}
```

This one should be pretty self-explanatory.

So, we now have a reference to the output. However, we are still not rendering
anything - if you run the compositor again you’ll notice the same behavior. In
order to render things, we have to listen for the  **frame signal** . Depending on
the selected mode, the output can only receive new frames at a certain rate. We
keep track of this for you in wlroots, and emit the frame signal when it’s time
to draw a new frame.

Let’s add a listener to the  `mcw_output`  struct for this purpose:

```
 struct mcw_output {
        struct wlr_output *wlr_output;
        struct mcw_server *server;
 
        struct wl_listener destroy;
+       struct wl_listener frame;
 
        struct wl_list link;
 };
```

We can then extend  `new_output_notify`  to register the listener to the frame
signal:

```
        output->destroy.notify = output_destroy_notify;
        wl_signal_add(&wlr_output->events.destroy, &output->destroy);
+       output->frame.notify = output_frame_notify;
+       wl_signal_add(&wlr_output->events.frame, &output->frame);
 }
```

Now, whenever an output is ready for a new frame,  `output_frame_notify`  will be
called. We still need to write this function, though. Let’s start with the
basics:

```
+static void output_frame_notify(struct wl_listener *listener, void *data) {
+       struct mcw_output *output = wl_container_of(listener, output, frame);
+       struct wlr_output *wlr_output = data;
+}
```

In order to render anything here, we need to first obtain a wlr_renderer 2 .
We can obtain one from the backend:

```
 static void output_frame_notify(struct wl_listener *listener, void *data) {
        struct mcw_output *output = wl_container_of(listener, output, frame);
        struct wlr_output *wlr_output = data;
+       struct wlr_renderer *renderer = wlr_backend_get_renderer(
+                       wlr_output->backend);
}
```

We can now take advantage of this renderer to draw something on the output.

```
 static void output_frame_notify(struct wl_listener *listener, void *data) {
        struct mcw_output *output = wl_container_of(listener, output, frame);
        struct wlr_output *wlr_output = data;
        struct wlr_renderer *renderer = wlr_backend_get_renderer(
                        wlr_output->backend);
+
+       wlr_output_make_current(wlr_output, NULL);
+       wlr_renderer_begin(renderer, wlr_output);
+
+       float color[4] = {1.0, 0, 0, 1.0};
+       wlr_renderer_clear(renderer, color);
+
+       wlr_output_swap_buffers(wlr_output, NULL, NULL);
+       wlr_renderer_end(renderer);
 }
```

Calling  `wlr_output_make_current`  makes the output’s OpenGL context “current”,
and from here you can use OpenGL calls to render to the output’s buffer. We call
 `wlr_renderer_begin`  to configure some sane OpenGL defaults for us 3 .

At this point we can start rendering. We’ll expand more on what you can
do with  `wlr_renderer`  later, but for now we’ll be satisified with clearing the
output to a solid red color.

When we’re done rendering, we call  `wlr_output_swap_buffers`  to swap the
output’s front and back buffers, committing what we’ve rendered to the actual
screen. We call  `wlr_renderer_end`  to clean up the OpenGL context and we’re
done. Running our compositor now should show you a solid red screen!

This concludes today’s article. If you take a look at  [the
commit](https://github.com/SirCmpwn/mcwayland/commit/f89092e)  that this article
describes, you’ll see that I took it a little further with some code that clears
the display to a different color every frame. Feel free to experiment with
similar changes!

Over the next two articles, we’ll finish wiring up the Wayland server and render
a Wayland client on screen. Please look forward to it!

Next —
     [
        Part 2: Rigging up the server
    ](/2018/02/22/Writing-a-wayland-compositor-part-2.html)

1. It’s entirely possible to utilize a wlroots backend to make applications which are not Wayland compositors. However, we require a wayland display anyway because the event loop is necessary for a lot of wlroots internals. ↩︎
2. wlr_renderer is optional. When you call wlr_output_make_current, the OpenGL context is made current and from here you can use any approach you prefer. wlr_renderer is provided to help compositors with simple rendering requirements. ↩︎
3. Namely: the viewport and blend mode. ↩︎
