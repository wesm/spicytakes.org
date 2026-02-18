---
title: "Writing a Wayland compositor with wlroots: shells"
date: 2018-07-29
url: https://drewdevault.com/2018/07/29/Wayland-shells.html
slug: Wayland-shells
word_count: 2247
---

I apologise for not writing about wlroots more frequently. I don’t really enjoy
working on the McWayface codebase this series of blog posts was originally
about, so we’re just going to dismiss that and talk about the various pieces of
a Wayland compositor in a more free-form style. I hope you still find it useful!

Today, we’re going to talk about shells. But to make sure we’re on the same page
first, a quick refresher on surfaces. A basic primitive of the Wayland protocol
is the concept of a “surface”. A surface is a rectangular box of pixels sent
from the client to the compositor to display on-screen. A surface can source
its pixels from a number of places, including raw pixel data in memory, or
opaque handles to GPU resources that can be rendered without copying pixels on
the CPU. These surfaces can also evolve over time, using “damage” to indicate
which parts have changed to reduce the workload of the compositor when
re-rendering them. However, making a surface and filling it with pixels is not
enough to get the compositor to show them.

Shells are how surfaces in Wayland are given meaning. Consider that there are
several kinds of surfaces you’ll encounter on your desktop. There are
application windows, sure, but there are also tooltips, right-click menus and
menubars, desktop panels, wallpapers, lock screens, on-screen keyboards, and so
on. Each of these has different semantics - your wallpaper cannot be minimized
or dragged around and resized, but your application windows can be.  Likewise,
your application windows cannot cover the entire screen and soak up all input
like your lock screen can. Each of these use cases is fulfilled with a  *shell* ,
which generally takes a surface resource, assigns it a role (e.g.  application
window), and returns a handle with shell-specific interfaces for manipulating
it.

## Shells in wlroots

I want to first discuss features common to shells as implemented by wlroots.
Each shell has a shell-specific interface that sits on top of the surface. Each
time a client connects and creates one of these, the shell raises a  `wl_signal` ,
 `events.new_surface` , and passes to it a pointer to a shell-specific structure
which encapsulates that shell surface’s state.

Many shells require some configuration between the creation of the shell surface
and displaying it on screen. For example, during this period application windows
will typically set the window title so that the compositor never has to show an
empty title. All Wayland interfaces aim for atomicity, so that all changes are
applied in a single fell swoop and we never display an invalid frame. This is
why Wayland is known for addressing vsync problems X suffers from, but is
pervasive across the ecosystem. Even things like setting the window title are
done atomically.

So, once the client is done communiciating the new shell surface’s desired
traits to the compositor, it will commit the surface to atomically apply the
changes. The first time this happens, the client is ready to be shown, and the
shell-specific wlroots shell surface interface will communicate this to you with
the surface’s  `events.map`  signal. The reverse is sometimes communicated with
 `events.unmap` , when the shell surface should be hidden.

## xdg-shell

xdg-shell is currently the only shell whose protocol is considered stable, and
it is the shell which describes application windows. You can read the xdg-shell
protocol specification (XML)
 [here](https://cgit.freedesktop.org/wayland/wayland-protocols/tree/stable/xdg-shell/xdg-shell.xml) 
(you are strongly encouraged to read through the XML for all protocols mentioned
in this article).

The xdg-shell is quite complicated, as it attempts to encapsulate every feature
of a typical graphical desktop session in a single protocol. An xdg-shell
surface is a  `wl_surface`  wrapped twice - once in a  `xdg_surface`  and then again
in a  `xdg_toplevel`  or  `xdg_popup` , depending on what kind of window it is. The
wlroots  `wlr_xdg_surface`  type (the one emitted by
 `xdg_shell.events.new_surface` ) contains tagged union of  `wlr_xdg_toplevel`  and
 `wlr_xdg_popup` , selected from the  `role`  field. You can wire up the xdg-shell
with  `wlr_xdg_shell_create` .

Most application windows you see are called toplevels. These windows are the
root node of a tree of surfaces which may include arbitrarily nested popups, for
example, as you navigate through a deep menu. These windows can have titles;
parent surfaces; app IDs (e.g. “gnome-calculator”); minimum and maximum sizes;
and maximized, minimized, and fullscreen states. They also often 1  draw their
own window decorations and drop shadows, and tell the compositor when you click
and drag on the titlebar to move or resize the window.  Unfortunately, if the
client is not responding or misbehaving, the user cannot use these controls to
move, resize, or minimize the window 2 .

The compositor can tell the window to adopt a specific size, though the client
can choose to ignore this. The compositor also lets the client know when it’s
“activated”, which is used by GTK+, for example, to start rendering the caret
and render a different set of client-side decorations. It can also toggle the
fullscreen, minimized, maximized, and other states.

Each of the various state transitions involved are expressed through
the  `wlr_xdg_toplevel.events`  signals. The most recent atomically agreed-upon
state is stored in  `wlr_xdg_toplevel.current` . When each of the signals in
 `events`  are emitted, the state change will have been applied to
 `client_pending` . However, you must consent to these changes by calling a
corresponding function on the xdg_toplevel (e.g.
 `wlr_xdg_toplevel_set_fullscreen` ), which will apply the change to
 `server_pending` . You shouldn’t consider these changes atomically set until the
 `wlr_surface.events.commit`  signal has been raised. At that point, you can start
showing the window in fullscreen or whatever. There’s also some
configure/ack-configure stuff going on here which may eventually become relevant
to you 3 , but wlroots takes care it for the most part.

The popup interface is used to show a “popup” window, which can be used for a
variety of purposes. These include context menus (or “right click” menus),
tooltips, some confirmation modals 4 , etc. The lifecycle of a popup resource
is managed similarly to that of a toplevel resource, of course with different
states that can be atomically updated. Arguably, the most fundamental of these
states is the relative X and Y position of the popup with respect to its parent
toplevel surface.

The position of the popup can be influenced by an extraordinarily complicated
interface called  `xdg_positioner` , also provided by xdg-shell. Since these
articles focus on the compositor side of things, and they focus on using
wlroots, I can thankfully save you from understanding most of the specifics of
this interface. The purpose of this interface is to adjust the position and size
of  `xdg_popup`  surfaces with respect to the display they live on - for example,
to prevent them from being partially off-screen. The rub is that if you’re using
wlroots, when the popup is created you can just call
 `wlr_xdg_popup_unconstrain_from_box`  to deal with everything, passing it a box
which represents the available space surrounding the parent toplevel for the
popup to be placed in.

Popups are also able to take “grabs”, which indicate that they should keep
focus without respect to any of the other goings-on of the seat. This is used so
that you can, for example, use the keyboard to pick items from a context menu.
Grabs are automatically handled for you with  `wlr_seat`  for you. If you want to
deny or cancel grabs, you can do so through the appropriate  `wlr_seat` 
interfaces.

One last note: xdg-shell only recently became stable, so client support for the
stable version is hit and miss. The last unstable protocol, xdg-shell v6, is
also supported by wlroots. It mostly behaves in the same way. Eventually it
will be removed from wlroots.

## layer-shell

Under the umbrella of wlroots, 8 Wayland compositors have been collaborating on
the design of a new shell for desktop shell components. The result is  [layer
shell
(XML)](https://github.com/swaywm/wlr-protocols/blob/master/unstable/wlr-layer-shell-unstable-v1.xml) .
The purpose of this shell is to provide an interface for desktop components like
panels, lock screens, wallpapers, on-screen keyboards, notifications, and so on,
to display on your compositor.

The layer-shell is organized into four discrete layers: background, bottom, top,
and overlay, which are rendered in that order. Between bottom and top,
application windows are displayed. A wallpaper client might choose to go in the
bottom layer, while a notification could show on the top layer, and a panel on
the bottom layer.

The compositor’s job is to decide where to place each surface and how large the
surface can be. The client can specify either or both of its dimensions (width
and height) for the compositor to specify, then provide some hints for the
compositor to do so. The client can, for example, choose to be anchored to edges
of the screen. A notification might be anchored to  `TOP | RIGHT` , and a panel
might be anchored to  `LEFT | BOTTOM | RIGHT` . A layer surface anchored to an
edge, like our panel, can also request an exclusive zone, which is a number of
pixels from the edge that should not be occluded by other layer surfaces or
application windows. This is used, for example, when maximizing application
windows to prevent them from occluding the panel (or in sway’s case, when
arranging tiled windows).

Layer surfaces also have special keyboard input semantics. Some layer surfaces
want to receive keyboard input, such as an application launcher overlay. Others
might prefer that application windows continue to receive keyboard events, such
as a notification. To this end, a layer surface can toggle a boolean indicating
its “keyboard interactivity”. For layers beneath application windows, layer
surfaces participate in keyboard focus normally, usually meaning they need to be
clicked to receive keyboard focus. Above application windows, the top-most layer
always has keyboard focus if it requests it.

In wlroots, you can wire up a layer shell to the display with
 `wlr_layer_shell_create` . From there it behaves similarly to xdg-shell with
respect to the creation of new surfaces and the handling of atomic state. The
main concern of yours is that, when the surface is committed, you need to
arrange the surfaces in the affected layer and communicate the final dimensions
of the layer surface to the client with  `wlr_layer_surface_configure` . You can
implement the arrangement however you want, but you may find the  [sway
implementation](https://github.com/swaywm/sway/blob/master/sway/desktop/layer_shell.c#L18-L215)  to be a useful reference. Also check out the
wlroots  [example client](https://github.com/swaywm/wlroots/blob/master/examples/layer-shell.c)  to test out your implementation.

Layer surfaces can also have popups, for example when right-clicking on a
taskbar. This borrows xdg-shell’s xdg_popup interface, except the parent is set
to the layer surface (this is explicitly allowed for through the xdg_popup spec,
and you may see future shells doing something similar). Most of your code for
xdg_popups can be reused with layer surfaces.

## Xwayland

Some Wayland developers turn up their nose when I refer to Xwayland as a shell,
and perhaps with good reason. However, wlroots treats Xwayland like a shell, so
the API remains consistent. For that reason, we’ll treat it as one in this
article as well.

We figured that you might be writing a Wayland compositor so that you  *don’t* 
have to write an X11 window manager, too. So we wrote one for you, and it’s
called  `wlr_xwayland` . This interface provides an abstraction over Xwayland
which makes it behave similarly to our other shells. It still lets you dig your
heels into it in any degree so that you can adjust the behavior of your
compositor to suit X-specific needs as necessary.

The resulting wlr_xwayland API is similar to the other shells we’ve described.
We have a series of events for configuring Xwayland surfaces, a map and unmap
event, and we expose a whole bunch of info about Xwayland surfaces so you can
make the judgement call about how much or how little to obey their requests (X11
windows make more unreasonable requests than other shells, since X11 was the
wild wild west and a lot of clients took advantage of that).

This should be enough to get you started, and if you have questions ask on IRC
for the time being. I could go into more detail, but I think Xwayland deserves
its own article, and probably not written by me.

## Other shells

There are three other shells of note. Two are not very interesting:

* wl_shell, the now-deprecated original desktop shell of Wayland
* ivi-shell, used for “in-vehicle infotainment” systems running Wayland

wlroots supports neither (though I guess we’d accept a patch adding IVI-shell
support, maybe if the vehicle industry was open to improving that protocol…),
and neither is interesting for desktops, phones, etc. You probably don’t need to
worry about them.

The other is the fullscreen-shell, which is used for optimizing the rendering of
fullscreen appliations. I don’t know much about how it works, and it’s not
supported by wlroots yet; it’s not required of a functional Wayland compositor.
Maybe someday!

1. [But not always](https://cgit.freedesktop.org/wayland/wayland-protocols/tree/unstable/xdg-decoration/xdg-decoration-unstable-v1.xml). You’re welcome. ↩︎ ↩︎
2. Which is one of the reasons we made the protocol mentioned in footnote1. ↩︎
3. For example, this is relevant for sway, which needs to reach deeper into our shell implementations to atomically syncronize the resizing of several clients at once when rearranging the layout. ↩︎
4. Some popup windows, the GTK+ file chooser for example, prefer to make a new xdg_toplevel and assign its parent to the application window. This is useful if you want your window to show up in taskbars, be able to be minimized and maximized separately, etc. ↩︎
