---
title: "State of Sway - December 2015"
date: 2015-12-20
url: https://drewdevault.com/2015/12/20/State-of-sway-December-2015.html
slug: State-of-sway-December-2015
word_count: 490
---

I wrote sway’s  [initial commit](https://github.com/SirCmpwn/sway/commit/6a33e1e3cddac31b762e4376e29c03ccf8f92107) 
4 months ago, on August 4th. At the time of writing, there are now 1,070 commits
from 29 different authors, totalling 10,682 lines of C (and 1,176 lines of
header files). This has been done over the course of 256 pull requests and 118
issues. Of the 73  [i3 features we’re
tracking](https://github.com/SirCmpwn/sway/issues/2) , 51 are now supported, and
I’ve been using sway as my daily driver for a while now. Today, sway looks like
this:

For those who are new to the project,  [sway](https://github.com/SirCmpwn/sway) 
is an i3-compatible Wayland compositor. That is, your existing
 [i3](http://i3wm.org/)  configuration file will work as-is on sway, and your
keybindings will be the same and the colors and font configuration will be the
same, and so on. It’s i3, but on Wayland.

Sway initially made the rounds on  [/r/linux](https://redd.it/3he5hn)  and
 [/r/i3wm](https://redd.it/3he48j)  and
 [Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=Wayland-i3-Sway-Tiling) 
on August 17th, 13 days after the initial commit. I was already dogfooding it by
then, but now I’m actually using it 100% of the time, and I hear others have
started to as well. What’s happened since then? Well:

* Floating windows
* Multihead support
* XDG compliant config
* Fullscreen windows
* gaps
* IPC
* Window criteria
* 58 i3 commands and 1 command unique to sway
* Wallpaper support
* Resizing/moving tiled windows with the mouse
* swaymsg, swaylock,  **swaybar**  as in i3-msg, i3lock, i3bar
* Hundreds of bug fixes and small improvements

Work on sway has also driven improvements in our dependencies, such as
 [wlc](https://github.com/Cloudef/wlc) , which now has improved xwayland support,
support for Wayland protocol extensions (which makes swaybg and swaylock and
swaybar possible), and various bugfixes and small features added at the bequest
of sway. Special thanks to Cloudef for helping us out with so many things!

All of this is only possible thanks to the hard work of dozens of contributors.
Here’s the breakdown of  **lines of code per author**  for the top ten authors:

And here’s the total  **number of commits per author**  for each of the top 10
committers:

As the maintainer of sway,  *a lot*  of what I do is reviewing and merging
contributions from others. So these statistics change a bit if we use  **number
of commits per author, excluding merge commits** :

These stats only cover the top ten in each, but there are more - check out the
 [full list](https://github.com/SirCmpwn/sway/graphs/contributors) .

So, what does this all mean for sway? Well, it’s going very well. If you’d like
to live on the edge, you can use sway right now and have a productive workflow.
The important features that are missing include stacking and tabbed layouts,
window borders, and some features on the bar. I’m looking at starting up a beta
when these features are finished. Come try out sway! Test it with us, open
GitHub issues with your gripes and desires, and  [chat
with us on IRC](http://webchat.freenode.net/?channels=sway&uio=d4) .

*This blog post was composed from sway.*
