---
title: "Why did we replace wlc?"
date: 2018-05-27
url: https://drewdevault.com/2018/05/27/Why-rewrite-wlc.html
slug: Why-rewrite-wlc
word_count: 928
---

For a little over a year, I’ve been working with a bunch of talented C
developers to build a replacement for the  [wlc](https://github.com/Cloudef/wlc) 
library. The result is  [wlroots](https://github.com/swaywm/wlroots) , and we’re
still working on completing it and updating our software to use it. The
 [conventional
wisdom](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) 
suggests that rewriting your code from scratch is almost never the right idea.
So why did we do it, and how is it working out? I have spoken a little about
this in the past, but we’ll answer this question in detail today.

Sway will have been around for 3 years as of this August. When I started the
project, I wanted to skip some of the hard parts and get directly to
implementing i3 features. To this end, I was browsing around for libraries which
provided some of the low-level plumbing for me - stuff like DRM (Display
Resource Management) and KMS (Kernel Mode Setting), EGL and GLES wires, libinput
support, and so on. I was more interested in whatever tool could get me up to
speed and writing sway-specific code quickly. My options at this point came down
to wlc and  [swc](https://github.com/michaelforney/swc) .

swc’s design is a little bit better in retrospect, but I ended up choosing wlc
for the simple reason that it had an X11 backend I could use for easier
debugging. If I had used swc, I would have been forced to work without a display
server and test everything under the DRM backend - which would have been pretty
annoying. So I chose wlc and go to work.

Designwise, wlc is basically a Wayland compositor with a plugin API, except you
get to write  `main`  yourself and the plugin API communicates entirely
in-process. wlc has its own renderer (which you cannot control) and its own
desktop with its own view abstraction (which you cannot control). You have some
events that it bubbles up for you and you can make some choices like where to
arrange windows.  However, if you just wire up some basics and run  `wlc_init` ,
wlc will do all of the rest of the work and immediately start accepting clients,
rendering windows, and dispatching input.

Over time we were able to make some small improvements to wlc, but sway 0.x
still works with these basic principles today. Though this worked well at first,
over time more and more of sway’s bugs and limitations were reflections of
problems with wlc. A lengthy discussion on IRC and  [on
GitHub](https://github.com/swaywm/sway/issues/1076)  ensued and we debated for
several weeks on how we should proceed. I was originally planning on building a
new compositor entirely in-house (similar to GNOME’s mutter and KDE’s kwin), and
I wanted to abstract the i3-specific functionality of sway into some kind of
plugin. Then, more “frontends” could be written on top of sway to add
functionality like AwesomeWM, bspwm, Xmonad, etc.

After some discussion among the sway team and with other Wayland compositor
projects  [facing similar
problems](https://github.com/way-cooler/way-cooler/issues/248)  with wlc, I
decided that we would start developing a standalone library to replace wlc
instead, and with it allow a more diverse Wayland ecosystem to flourish.
Contrary to wlc’s design - a Wayland compositor with some knobs - wlroots is a
set of modular tools with which you build the Wayland compositor yourself. This
design allows it to be suited to a huge variety of projects, and as a result
it’s now being used for many different Wayland compositors, each with their own
needs and their own approach to leveraging wlroots.

When we started working on this, I wasn’t sure if it was going to be successful.
Work began slowly and I knew we had a monumental task ahead of us. We spent a
lot of time and a few large refactorings getting a feel for how we wanted the
library to take shape. Different parts matured at different paces, sometimes
with changes in one area causing us to rethink design decisions that affected
the whole project. Eventually, we fell into our stride and found an approach
that we’re very happy with today.

I think that the main difference with the approach that wlroots takes comes from
experience. Each of the people working on sway, wlc, way cooler, and so on were
writing Wayland compositors for the first time. I’d say the problems that arose
as a result can also be seen throughout other projects, including Weston, KWin,
and so on. The problem is that when we all set out, we didn’t fully understand
the opportunities afforded by Wayland’s design, nor did we see how best to
approach tying together the rather complicated Linux desktop stack into a
cohesive project.

We could have continued to maintain wlc, fixed bugs, refactored parts of it, and
maybe eventually arrived at a place where sway more or less worked. But we’d
simply be carrying on the X11 tradition we’ve been trying to escape this whole
time. wlc was a kludge and replacing it was well worth the effort - it simply
could not have scaled to the places where wlroots is going. Today, wlroots is
the driving force behind 6 Wayland compositors and is targeting desktops,
tablets, and phones. Novel features never seen on any desktop - even beyond
Linux - are possible with this work. Now we can think about not only replacing
X11, but innovating in ways it never could have.

Our new approach is the way that Wayland compositors should be made. wlroots is
the realization of Wayland’s potential. I am hopeful that our design decisions
will have a lasting positive impact on the Wayland ecosystem.
