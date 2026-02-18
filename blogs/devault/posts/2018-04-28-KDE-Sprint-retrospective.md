---
title: "Sway reporting in from KDE's Berlin development sprint"
date: 2018-04-28
url: https://drewdevault.com/2018/04/28/KDE-Sprint-retrospective.html
slug: KDE-Sprint-retrospective
word_count: 689
---

I’m writing to you from an airplane on my way back to Philadelphia, after
spending a week in Berlin working with the KDE team. It was great to meet those
folks and work with them for a while. It’ll take me some time to get the taste
of C++ out of my mouth, though! In all seriousness, it was a very productive
week and I feel like we have learned a lot about each other’s projects and have
a strengthened interest in collaborating more in the future.

The main purpose of my trip was to find opportunities for
 [sway](http://swaywm.org)  and  [KDE](http://kde.org)  to work together on
improving the Linux desktop. Naturally, the main topic of discussion was
interopability of software written for each of our projects. I brought the
wlroots layer-shell protocol to the table seeking their feedback on it, as well
as reviewing how their desktop shell works today. From our discussions we found
a lot of common ground in our designs and needs, as well as room for improvement
in both of our approaches.

The KDE approach to their desktop shell is similar to the original sway
approach. Today, their Plasma shell uses a number of proprietary protocols which
are hacks on top of the xdg-shell protocol (for those not in the know, the
xdg-shell protocol is used to render normal desktop windows and is not designed
for use with e.g. panels) that incorporate several of the concepts they were
comfortable using on X11 in an almost 1:1 fashion. Sway never had any X11
concepts to get comfortable with, but some may not know that sway’s panel,
wallpaper, and lock screen programs on the 0.x releases are also hacks on top of
xdg-shell that are not portable between compositors.

In the wlroots project (which is overseen by sway), we’ve been developing a
new protocol designed for desktop shell components like these. In theory, it is
a more generally applicable approach to building desktop shells on Wayland than
the approach we were using before. I sat down with the KDE folks and went over
this protocol in great detail, and learned about how Plasma shell works today,
and we were happy to discover that the wlroots approach (with some minor tweaks)
should be excellently suited to Plasma shell. In addition to the layer-shell, we
reviewed several other protocols Plasma uses to build its desktop experience,
and identified more places where it makes sense for us to unify our approach.
Other subjects discussed included virtual desktops, external window management,
screen capture and pipewire, and more.

The upshot of this is that we believe it’s possible to integrate the Plasma
shell with sway. Users of KDE on X11 were able to replace kwin with i3 and still
utilize the Plasma shell - a feature which was lost in the transition to
Wayland. As we continue to work together, this use-case may well be captured
again. Even KDE users who are uninterested in sway stand to benefit from this.
The hacks Plasma uses today are temporary and unmaintainable, and the
improvements to Plasma’s codebase will make it easier to work with. Should kwin
grow stable layer-shell support, clients designed for sway will work on KDE as
well. Replacing sway’s own similar hacks will have similar benefits for our
codebase and open the door to 3rd-party panels, lockscreens, rofi, etc.

I spent my time in their care working on actual code to this end. I wrote up a
C++ library that extends Qt with layer-shell support called
 [qtlayershell](https://github.com/SirCmpwn/qtlayershell) , and extended the
popular  Latte Dock  KDE extension to support it. Though this work is not
complete, it works - as I write this blog post, Latte is running on my sway
session! This is good progress, but I must return my focus to wlroots soon. If
you are interested in this work, please help me complete it!

A big thanks goes to KDE for putting on this event and covering my travel costs
to attend. I hope they found it as productive as I did, and I’m very excited
about working more with them in the future. The future of Wayland is bright!
