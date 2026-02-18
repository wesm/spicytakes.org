---
title: "Input handling in wlroots"
date: 2018-07-17
url: https://drewdevault.com/2018/07/17/Input-handling-in-wlroots.html
slug: Input-handling-in-wlroots
word_count: 2116
---

I’ve said before that wlroots is a “batteries not included” kind of library, and
one of the places where that is most apparent is with our approach to input
handling. We implemented a very hands-off design for input, in order to support
many use-cases: desktop input, phones with and without USB-OTG HIDs plugged in,
multiple mice bound to a single cursor, multiple keyboards per seat, simulated
input from fake input devices, on-screen keyboards, input which is processed by
the compositor but not sent to clients… we support all of these use-cases and
even more. However, the drawback of our powerful design is that it’s confusing.
Very confusing.

Let’s begin by forgetting about the Wayland part entirely. After all, wlroots is
flexible enough that you can use it without writing a Wayland compositor at all!
It can be used in a similar fashion to tools like GLFW and SDL, to abstract
low-level input (via e.g. libinput) and graphical output (via e.g. DRM). Let’s
start here, simply getting input events from wlroots in the first place.

One of the fundamental building blocks of wlroots is the  `wlr_backend` ,
which is a resource that abstracts the underlying hardware and exposes a
consistent API for outputs and input devices. Outputs have been discussed
elsewhere, so let’s focus just on input devices. Each backend provides an
event:  [`wlr_backend.events.new_input`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/backend.h#L17) . The signal is called with a
reference to a  [`wlr_input_device`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_input_device.h)  each time a new input
device appears on the backend - for example, when you plug a mouse into your
computer when using the libinput backend.

The input device can be one of five types, appropriately identified by the
 `type`  field. The types are:

* `WLR_INPUT_DEVICE_KEYBOARD`
* `WLR_INPUT_DEVICE_POINTER`
* `WLR_INPUT_DEVICE_TOUCH`
* `WLR_INPUT_DEVICE_TABLET_TOOL`
* `WLR_INPUT_DEVICE_TABLET_PAD`

The type indicates which member of the anonymous union is valid. If
 `wlr_input_device->type == WLR_INPUT_DEVICE_KEYBOARD` , then
 `wlr_input_device->keyboard`  is a valid pointer to a
 [`wlr_keyboard`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_keyboard.h) .

Let’s examine the wlr keyboard more closely now. The keyboard struct also
provides its own events, like  `key`  and  `keymap` . If you want to process input
from this keyboard, you need to set up an  [xkbcommon](https://xkbcommon.org/doc/current/)  context for
ingesting the raw scancodes emitted by the  `key`  event and converting them to
Unicode and keysyms (e.g. “Up”) with an XKB keymap. Most of the wlroots examples
 [implement this](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/examples/simple.c#L114)  if you’re looking for a simple reference.

When these events are sent, we just let you process them as you please. They do
not automatically get propagated to any Wayland clients. Communicating these
events to the clients is your responsibility, though we provide you tools to
help - we’ll get into that shortly. You don’t even have to source the input you
give to Wayland clients from a  `wlr_input_device` , you can just as easily make
them up or get them from the network or anywhere else.

Before we get into details on how to send events to clients, let’s examine the
other components in your compositor’s input code. First, let’s talk about the
cursor.

We provide the  [`wlr_pointer`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_pointer.h)  abstraction for getting events from
a “pointer” device, like a mouse. However, because batteries are not included,
you will find that we only tell you what the pointer device is doing - we don’t
act on it. If you want to, for example, display a cursor image   
on screen which moves around when the mouse does, you need to wire this up
yourself. We have tools which can help.

First, let’s talk about getting the cursor image to show. You can source the
image from anywhere you want, but you will probably want to leverage
 [`wlr_xcursor`](https://github.com/swaywm/wlroots/blob/master/include/wlr/xcursor.h) . This is a small wlroots module (forked from the
 `wayland-cursor`  library used by Wayland clients) which can read Xcursor themes,
the kind your user will already have installed on their system. Loading up a
cursor theme and getting the pixels from it is pretty straightforward. But what
should you do with those pixels?

Well, now we have to introduce hardware cursors. Many backends support
“hardware” cursors, which is a feature provided by your low-level graphics stack
(e.g. GPU drivers) for rendering a cursor on the screen. Hardware cursors are
composited by the GPU, which means you can move the cursor around without
re-drawing the things underneath it. This is the most energy- and CPU-efficient
way of drawing your cursor, and you can do it with
 [`wlr_output_cursor_set_image`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_output.h#L179-L190) , specifying which  `wlr_output` 
you want it to appear on and at what coordinates. Not all configurations support
hardware cursors, but  `wlr_output`  automatically falls back to software cursors
if need be.

Now you have all of the pieces to show a cursor on screen that moves with the
mouse. You can store some X and Y coordinates somewhere, grab an image from an
Xcursor theme, and throw it at your  `wlr_output` , then process input events and
move it around. Then… you need to consider multiple outputs. And you need to
make sure that it can’t be moved outside of an output. And you need to let the
user move it around with a drawing tablet or touch screen as well. And… well,
it’s about to get complicated. That’s where our next tool comes in!

[`wlr_cursor`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_cursor.h)  is how wlroots saves you from some of this work. It
can display a cursor image on-screen, tie it to multiple input devices,
constrain it to your outputs and move it across multiple displays. It can also
map input from certain devices to certain outputs or regions of the output
layout, change the geometry of inputs from a drawing tablet, and more.

To use  `wlr_cursor` , you should create one ( `wlr_cursor_create` ) and as the
backend emits  `new_input`  events, bind them to the cursor with
 `wlr_cursor_attach_input_device` .  `wlr_cursor`  then raises aggregated events
from all of its devices, which you can catch and handle accordingly - usually
calling a function like  `wlr_cursor_move`  and propagating the event to Wayland
clients. You also need to attach a  [`wlr_output_layout`](https://github.com/swaywm/wlroots/blob/master/include/wlr/types/wlr_output_layout.h)  to
the cursor, so it knows how to constrain the cursor movement and can handle
hardware cursors for you.

Aside: the  `wlr_output_layout`  module allows you to configure an arrangement of
 `wlr_output` s in physical space. Its function is fairly straightforward and
largely unrelated to our topic - I suggest reading through the header and asking
questions if you need help. Once you make one of these and hand it to a
 `wlr_cursor` , you have a cursor on-screen which moves around when you provide
input and correctly moves throughout a multi-display setup. 1   2

Okay, now that we have all of those pieces in place, we can finally start talking
about sending input events to Wayland clients! Before we get into how  *wlroots* 
does it, let’s talk about how  *Wayland*  does it in general.

The top-level resource which manages input for a Wayland client is the
 `wl_seat` . One seat, in rough terms, maps to a single set of input devices used
by a user (a user who is presumably sitting at a seat in front of their
computer). A seat can have up to one keyboard, pointer, touch device, or drawing
tablet each. Each of these devices can then  *enter*  or  *leave*  any of the
client’s surfaces at the compositor’s orders.

When you bind to a  `wl_seat` ’s  `wl_keyboard`  and  `wl_keyboard.enter`  is raised
on a surface, it means your surface has keyboard focus. The compositor will
follow-up with (or will have already sent) a  `wl_keyboard.keymap`  signal to let
you know the layout of this keyboard (e.g.  `us-intl` ,  `de` ,  `ru` , etc) in the
form of an xkbcommon keymap (the same format we were using with  `wlr_keyboard` 
earlier - hint hint). Some number of  `key`  and  `modifier`  events will likely
follow as the user taps away.

When you bind to a  `wl_seat` ’s  `wl_pointer`  and  `wl_pointer.enter`  is raised, it
means a pointer has moved over one of your surfaces. Note that this can be an
entirely separate occasion from receiving keyboard focus. The client is then
expected to provide a cursor image to display (at the moment, Wayland  *requires* 
client side cursors. They have to do the whole Xcursor dance we did on the
wlroots side earlier, too. We have some plans to correct this…). Some number
of  `motion`  and  `button`  events will likely follow as the user wiggles their
mouse and clicks your windows.

So, how does a wlroots-based compositor facilitate these interactions? With
 [`wlr_seat`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_seat.h) , our abstraction on top of  `wl_seat` . This implements the
whole  `wl_seat`  state machine, but again leaves it to you to tweak the knobs as
you wish. You need to decide how your compositor is going to deal with focus -
KDE, Sway, the Librem5 phone UI, an in-vehicle infotainment system; all of these
will have a different approach to focus.

wlroots doesn’t render client surfaces for you, and doesn’t know where you put
them. Once you figure out where they go, you need to notice when the
 `wlr_cursor`  is moved over it and call  `wlr_seat_pointer_notify_enter`  with the
pointer’s coordinates relative to the surface it entered, along with any
appropriate  `motion`  or  `button`  events through the relevant  `wlr_seat` 
functions. The client will also likely send you a cursor image to display - this
is done with the  `wlr_seat.events.request_set_cursor`  event.

When you decide that a surface should receive keyboard focus, call
 `wlr_seat_keyboard_notify_enter` .  `wlr_seat`  will automatically handle removing
focus from whatever had it last, and will also grab the keymap and send it to
the client for you, assuming you configured it with  `wlr_keyboard_set_keymap` …
you did, right?  `wlr_seat`  also semi-transparently deals with grabs, the sort of
situation where a client wants to keep keyboard focus for longer than it
normally would, to deal with a context menu or something.

Touch events are similar and should be self-explanatory when you read the
header. Drawing tablet events are a bit different - they’re not actually
specified by the core Wayland protocol. Instead, we rig these up with the
 [tablet](https://cgit.freedesktop.org/wayland/wayland-protocols/tree/unstable/tablet/tablet-unstable-v2.xml)  protocol extension and  [wlr_tablet](https://github.com/swaywm/wlroots/blob/7f20ab644347b11fd8242beaf7a6fe42c910d014/include/wlr/types/wlr_tablet_v2.h) . It
works in much the same way, but you have to explicitly configure it for a
 `wlr_seat`  by calling  `wlr_tablet_create`  yourself.

So, in short, if you wiggle your mouse, here’s what happens:

1. Before you wiggled your mouse, the  `libinput`  backend noticed it was plugged
in and raised a  `new_input`  event.
2. Your compositor attached the resulting  `wlr_pointer`  to its  `wlr_cursor` ,
which it had prepared earlier by looking up an appropriate cursor theme and
letting it know about the display layout.
3. The  `wlr_pointer`  bubbled up a  `motion`  event, which was caught by
 `wlr_cursor`  and bubbled up to your compositor.
4. Your compositor called  `wlr_cursor_move`  to apply the resulting motion,
constrained by the output layout, which in turn caused the cursor image on
your display to move.
5. Your compositor then looked around to see if the pointer had moved over any
new surfaces. Since wlroots doesn’t handle rendering or know where anything
is displayed, this was a rather introspective question.
6. You  *did*  wiggle it over a new surface, so the compositor called
 `wlr_seat_notify_pointer_enter`  after translating the pointer coordinates to
surface-local space. It sent a  `wlr_seat_notify_pointer_motion`  for good
measure.
7. The client noticed the pointer entered it and sent back a cursor image to
show. The compositor was informed of this via
 `wlr_seat.events.request_set_cursor` .
8. The compositor handled the client’s cursor image to  `wlr_cursor` , throwing
away all of that hard work loading up a cursor theme just for a client-side
cursor to come in and ruin it.

And there you have it, that’s how input works in wlroots. It’s really fucking
complicated, isn’t it? I think this article puts on display both the incredible
advantages and serious drawbacks of wlroots. Because you have to plug all of
these pieces together yourself, you are afforded an  *enormous*  amount of
flexibility. However, you have to do a lot of work and understand a whole lot of
different pieces to get there. Libraries like
 [wlc](https://github.com/Cloudef/wlc)  are much easier to use in this respect,
but if you want to change even a small detail of this process with wlc you are
unable to.

If you have any questions about this article, please reach out to the developers
hanging out in  [#sway-devel on irc.freenode.net](http://webchat.freenode.net/?channels=sway-devel&uio=d4) . We know this is
confusing, and we’re happy to help.

1. One more quick note: for multi-DPI setups, you need to provide the `wlr_cursor` with different cursor images, one for each scale present on the output layout. We have another tool for sourcing Xcursor images at multiple scale factors, check out [`wlr_xcursor_manager`](https://github.com/swaywm/wlroots/blob/4984ea49eeaa292d66be9e535d93a4d8185f3e18/include/wlr/types/wlr_xcursor_manager.h). ↩︎
2. Another thing `wlr_output_layout` is useful for, if you were wondering, is figuring out where to render windows in a multi-output arrangement, where some windows might span multiple outputs. Read the header! ↩︎
