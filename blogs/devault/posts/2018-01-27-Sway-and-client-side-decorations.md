---
title: "Sway and client side decorations"
date: 2018-01-27
url: https://drewdevault.com/2018/01/27/Sway-and-client-side-decorations.html
slug: Sway-and-client-side-decorations
word_count: 313
---

You may have recently seen an article from GNOME on the subject of client side
decorations (CSD) titled  [Introducing the CSD
Initiative](https://blogs.gnome.org/tbernard/2018/01/26/csd-initiative/) . It
states some invalid assumptions which I want to clarify, and I want to tell you
 [Sway](https://github.com/swaywm/sway) ’s
stance on the subject. I also speak for the rest of the projects involved in
 [wlroots](https://github.com/swaywm/wlroots)  on this matter, including  [Way
Cooler](https://github.com/way-cooler/way-cooler) ,
 [waymonad](https://github.com/Ongy/waymonad) , and
 [bspwc](https://github.com/Bl4ckb0ne/bspwc) .

The subject of which party is responsible for window decorations on Wayland (the
client or the server) has been a subject of much debate. I want to clarify that
though GNOME may imply that a consensus has been reached, this is not the case.
CSD have real problems that have long been waved away by its supporters:

* No consistent look and feel between clients and GUI toolkits
* Misbehaving clients cannot be moved, closed, minimized, etc
* No opportunity for compositors to customize behavior (e.g. tabbed windows on
Sway)

We are willing to cooperate on a compromise, but GNOME does not want to
entertain the discussion and would rather push disingenuous propaganda for their
cause. The topic of the #wayland channel on Freenode includes the statement
“Please do not argue about server-side vs. client-side decorations. It’s settled
and won’t change.” I have been banned from this channel for over a year because
I persistently called for compromise.

GNOME’s statement that “[server-side decorations] do not (and will never) work
on Wayland” is false. KDE and Sway have long agreed on the importance of these
problems and have worked together on a solution. We have developed and
implemented a Wayland protocol extension which allows the compositor and client
to negotiate what kind of decorations each wishes to use. KDE, Sway, Way Cooler,
waymonad, and bspwc are all committed to supporting server-side decorations on
our compositors.

See also:  [Martin Flöser of KDE responds to GNOME’s
article](https://blog.martin-graesslin.com/blog/2018/01/server-side-decorations-and-wayland/)
