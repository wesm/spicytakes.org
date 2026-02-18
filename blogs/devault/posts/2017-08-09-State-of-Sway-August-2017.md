---
title: "State of Sway August 2017"
date: 2017-08-09
url: https://drewdevault.com/2017/08/09/State-of-Sway-August-2017.html
slug: State-of-Sway-August-2017
word_count: 431
---

Is it already time to write another one of these? Phew, time flies. Sway marches
ever forward. Sway 0.14.0 was recently released, adding much asked-after support
for tray icons and fixing some long-standing bugs. As usual, we already have
some exciting features slated for 0.15.0 as well, notably some cool improvements
to clipboard support. Look forward to it!

Today Sway has 24,123 lines of C (and 4,489 lines of header files) written by 94
authors across 2,345 commits. These were written through 689 pull requests and
624 issues. Sway packages are available today in the repos of almost every Linux
distribution.

For those who are new to the project,  [Sway](http://swaywm.org)  is an
i3-compatible Wayland compositor. That is, your existing  [i3](http://i3wm.org/) 
configuration file will work as-is on Sway, and your keybindings and colors and
fonts and for_window rules and so on will all be the same. It’s i3, but for
Wayland, plus it’s got some bonus features. Here’s a quick rundown of what’s
new since the  [previous state of Sway](/2017/04/29/State-of-sway-April-2017.html) :

* Initial support for tray icons
* X11/Wayland clipboard synchronization
* nvidia proprietary driver support*
* i3’s marks
* i3’s mouse button bindings
* Lots of i3 compatibility improvements
* Lots of documentation improvements
* Lots of bugfixes

If this seems like a shorter list than usual, it’s because we’ve also been
making great progress on wlroots too - no doubt thanks to the help of the many
contributors doing amazing work in there. For those unaware, wlroots is our
project to replace wlc with a new set of libraries for Wayland compositor
underpinnings (it fills a similar niche as libweston). We now have a working DRM
backend (including output rotation and hardware cursors) and libinput backend
(including touchscreen and drawing tablet support), and we’re making headway now
on drawing Wayland clients on screen.  I’m very excited about our pace and
direction - keep an eye on it
 [here](https://github.com/SirCmpwn/wlroots/issues/9) . I have also taken over for
Cloudef as the maintainer of  [wlc](https://github.com/Cloudef/wlc)  during the
transition.

In other news, our bounty program continues to go strong. Our  [current
pot](https://github.com/SirCmpwn/sway/issues/986)  is $1200 and we’ve paid out
$80 so far (and a $280 payout is on the horizon for tray icons). I’ve also
started a  [Patreon page](https://www.patreon.com/sircmpwn) , where 26 patrons are
generously supporting my work as maintainer of Sway and other projects. Many
thanks to everyone who has contributed financially to Sway’s success!

That wraps up today’s post. Thanks for using Sway!

* I hate this crappy driver. It works, but don’t
expect to receive much support for it. [Linus said it
best](https://www.youtube.com/watch?v=iYWzMvlj2RQ).
