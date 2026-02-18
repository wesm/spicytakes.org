---
title: "Wayland misconceptions debunked"
date: 2019-02-10
url: https://drewdevault.com/2019/02/10/Wayland-misconceptions-debunked.html
slug: Wayland-misconceptions-debunked
word_count: 1851
---

This article has been on my backburner for a while, but it seems Wayland FUD is
making the news again recently, so I’ve bumped up the priority a bit. For those
new to my blog, I am the maintainer of
 [wlroots](https://github.com/swaywm/wlroots) , a library which implements much of
the functionality required of a Wayland compositor and is arguably the single
most influential project in Wayland right now; and  [sway](https://swaywm.org) , a
popular Wayland compositor which is nearing version 1.0. Let’s go over some of
the common misconceptions I hear about Wayland and why they’re wrong. Feel free
to pick and choose the misconceptions you believe to read and disregard the
rest.

The art of hating Wayland has become a cult affair. We don’t need to put
ourselves into camps at war. Please try not to read this article through the
lens of anger.

### Wayland isn’t more secure, look at this keylogger!

There is an  [unfortunate GitHub
project](https://github.com/Aishou/wayland-keylogger)  called “Wayland keylogger”
whose mode of operation is using  `LD_PRELOAD`  to intercept calls to the
libwayland shared library and record keypresses from it. The problem with this
“critique” is stated in the  `README.md`  file, though most don’t read past the
title of the repository. Wayland is only  *one part*  of an otherwise secure
system. Using  `LD_PRELOAD`  is effectively equivalent to rewriting client
programs to log keys themselves, and any program which is in a position to do
this has already won. If I rephrased this as “Wayland can be keylogged, assuming
the attacker can sneak some evil code into your .bashrc”, the obviousness of
this truth should become immediately apparent.

Some people have also told me that they can log keys by opening  `/dev/input/*` 
files and reading input events. They’re right! Try it yourself:  `sudo libinput debug-events` . The catch should also be immediately obvious: ask
yourself why this needs to be run with  `sudo` .

### Wayland doesn’t support screenshots/capture!

The  [core Wayland protocol](https://github.com/wayland-project/wayland/blob/master/protocol/wayland.xml)  does not define a mechanism for taking
screenshots. Here’s another thing it doesn’t define: how to open application
windows, like gedit and Firefox. The Wayland protocol is very conservative and
general purpose, and is built with use-cases other than desktop systems in mind.
To this end it only implements the lowest common denominator, and leaves the
rest to protocol extensions. There is a process for defining, implementing,
maturing, and standardizing these extensions, though the last part is in need of
improvements - which are under discussion.

There are two protocols for the purpose of screenshots and screen recording,
which are developed by wlroots and supported by a strong majority of Wayland
compositors:  [screencopy](https://github.com/swaywm/wlroots/blob/master/protocol/wlr-screencopy-unstable-v1.xml)  and
 [dmabuf-export](https://github.com/swaywm/wlroots/blob/master/protocol/wlr-export-dmabuf-unstable-v1.xml) , respectively for copying pixels (best for
screenshots) and exporting DMA buffers (best for real-time video capture).

There are two approaches to this endorsed by different camps in Wayland: these
Wayland protocols, and a dbus protocol based on Pipewire. Progress is being made
on making these approaches talk to each other via  [xdg-desktop-portal](https://github.com/emersion/xdg-desktop-portal-wlr) ,
which will make just about every client and compositor work together.

### Wayland doesn’t have a secondary clipboard!

Secondary clipboard support (aka primary selection) was first implemented as
 [gtk-primary-selection](https://github.com/swaywm/wlroots/blob/master/protocol/gtk-primary-selection.xml)  and was recently standardized as
 [wp-primary-selection](https://github.com/wayland-project/wayland-protocols/blob/master/unstable/primary-selection/primary-selection-unstable-v1.xml) . It is supported by nearly all Wayland
compositors and clients.

### Wayland doesn’t support clipboard managers!

See  [wl-clipboard](https://github.com/bugaevc/wl-clipboard)

### Wayland isn’t suitable for embedded devices!

Some people argue that Wayland isn’t supported on embedded devices or require
proprietary blobs to work. This is  *very*  untrue. Firstly, Wayland is a
protocol: the  *implementations*  are the ones that need support from drivers, and
a Wayland implementation could be written for basically any driver. You could
implement Wayland by writing Wayland protocol messages on pieces of paper,
passing them to your friend in class, and having them draw your window on their
notebook with a pencil.

That being said, this is also untrue of the implementations. wlroots, which
contains the most popular Wayland rendering backend, implements KMS+DRM+GBM,
which is supported by all open source graphics drivers, and uses GLESv2, which
is the most broadly supported graphics implementation, including on embedded
(which is what the “E” stands for) and most older hardware. For ancient
hardware, writing an fbdev backend is totally possible and I’d merge it in
wlroots if someone put in the time. Writing a more modern KMS+DRM+GBM
implementation for that hardware is equally possible.

### Wayland doesn’t have network transparency!

This is actually true! But it’s not as bad as it’s made out to be. Here’s why:
X11 forwarding works on Wayland.

Wait, what? Yep: all mainstream desktop Wayland compositors have support for
 **Xwayland** , which is an implementation of the X11 server which translates X11
to Wayland, for backwards compatibility. X11 forwarding works with it! So if you
use X11 forwarding on Xorg today, your workflow will work on Wayland unchanged.

However, Wayland itself is not network transparent. The reason for this is that
some protocols rely on file descriptors for transferring information quickly or
in bulk. One example is GPU buffers, so that the Wayland compositor can render
clients without copying data on the GPU - which improves performance
dramatically. However, little about Wayland is inherently network  *opaque* .
Things like sending pixel buffers to the compositor are already abstracted on
Wayland and a network-backed implementation could be easily made. The problem is
that no one seems to really care: all of the people who want network
transparency drank the anti-Wayland kool-aid instead of showing up to put the
work in. If you want to implement this, though, we’re here and ready to support
you! Drop by the wlroots  [IRC channel](https://webchat.freenode.net/?channels=sway-devel)  and we’re prepared to help
you implement this.

### Wayland doesn’t support remote desktop!

This one is also true, but work is ongoing. Several of the pieces are in place:
screen capture and keyboard simulation are there. If an interested developer
wants to add pointer device simulation and tie it all together with librdesktop,
that would be a great boon to the Wayland ecosystem.  [We’re waiting to
help!](https://webchat.freenode.net/?channels=sway-devel)

### Wayland requires client side decorations!

This was actually true for a long time, but there was deep contention in the
Wayland ecosystem over this matter. We fought long and hard over this and we now
have a protocol for negotiating client- vs server-side decorations, which is now
fairly broadly supported, including among some of its opponents. You’re welcome.

### Wayland doesn’t support hotkey daemons!

This is a feature, not a bug, but you’re free to disagree once you hear the
rationale. There are lots of problems with the idea of hotkey daemons as it
exists on X. What if there’s a conflict between several clients who want the
same hotkey? What if the user wants to pick a different hotkey? On top of this,
designing a protocol carefully to avoid keylogging concerns makes it more
difficult still.

To this end, I’ve been encouraging client developers who want hotkeys to instead
use some kind of IPC mechanism and a control binary. For example,  `mako` , a
notification daemon, allows you to dismiss notifications by running the  `makoctl dismiss`  command. Users are then encouraged to use the compositor’s own
keybinding facilities to execute this command. This is more flexible even
outside of keybinding - the user might want to execute this behavior through a
script, too.

Still, if you  *really*  want hotkeys, you should start the discussion for
standardizing a protocol. It will be an uphill battle but I believe that a
protocol which addresses everyone’s concerns is theoretically possible.  *You* 
have to step up, though: no one working on Wayland today seems to care. We are
mostly volunteers working for free in our spare time.

### Wayland doesn’t support Nvidia!

Actually, Nvidia doesn’t support us. There are three standard APIs which are
implemented by all graphics drivers in the Linux kernel: DRM (display resource
management), KMS (kernel mode setting), and GBM (generic buffer management). All
three are necessary for most Wayland compositors. Only the first two are
implemented by the Nvidia proprietary driver. In order to support Nvidia,
Wayland compositors need to add code resembling this:

```
if (nvidia proprietary driver) {
    /* several thousand lines of code */
} else {
    /* several thousand lines of code */
}
```

That’s terrible! On top of that, we cannot debug the proprietary driver, we
cannot send fixes upstream, and we cannot read the code to understand its
behavior. The mesa code (where much of the important code for many drivers
lives) is a frequent object of study among Wayland compositor developers. We
cannot do this with the proprietary drivers, and it doesn’t even implement the
APIs it needs to. They claim to be working on a replacement for GBM which they
hope will satisfy everyone’s concerns, but 52 commits in 3 years with over a
year of inactivity isn’t a great sign.

To boot, Nvidia is a bad actor on Linux. Compare the talks at FOSDEM 2018
from the  [nouveau developers](https://archive.fosdem.org/2018/schedule/event/nouveau/)  (the open source Nvidia driver) and the
 [AMDGPU developers](https://archive.fosdem.org/2018/schedule/event/amd_graphics/)  (the  *only* 1  AMD driver - also open source). The
Nouveau developers discuss all of the ways that Nvidia makes their lives
difficult, up to and including  *signed firmwares* . AMDGPU instead talks about
the process of upstreaming their driver, discuss their new open source Vulkan
driver, and how the community can contribute - and this was presented by paid
AMD staff. I met Intel employees at XDC who were working on a continuous
integration system wherein Intel offers a massive Intel GPU farm to Mesa
developers free-of-charge for working on the open source driver. Nvidia is
clearly a force for bad on the Linux scene and for open source in general, and
the users who reward this by spending oodles of cash on their graphics cards are
not exactly in my good graces.

So in short, people asking for Nvidia proprietary driver support are asking the
wrong people to spend hundreds of hours working for free to write and maintain
an implementation for  *one*  driver which represents a harmful force on the Linux
ecosystem and a headache for developers trying to work with it. With respect, my
answer is no.

### Wayland doesn’t support gaming!

First-person shooters, among other kinds of games, require “locking” the pointer
to their window. This requires  [a protocol](https://github.com/wayland-project/wayland-protocols/blob/master/unstable/pointer-constraints/pointer-constraints-unstable-v1.xml) , which was
standardized in 2015. Adoption has been slower, but it landed in wlroots several
months ago and support was added to sway a few weeks ago.

### In conclusion

At some point, some of these things have been true. Some have never been true.
It takes time to replace a 30-year incumbent. To be fair, some of these points
are true on GNOME and KDE, but none are inherently problems with the Wayland
protocol. wlroots is a dominating force in the Wayland ecosystem and the tide is
clearly moving our way.

Another thing I want to note is that Xorg still works. If you find your needs
aren’t met by Wayland, just keep using X! We won’t be offended. I’m not trying
to force you to use it. Why you heff to be mad?

1. *actively maintained ↩︎
