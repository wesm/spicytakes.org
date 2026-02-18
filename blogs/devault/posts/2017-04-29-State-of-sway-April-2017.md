---
title: "State of Sway April 2017"
date: 2017-04-29
url: https://drewdevault.com/2017/04/29/State-of-sway-April-2017.html
slug: State-of-sway-April-2017
word_count: 585
---

Development on Sway continues. I thought we would have slowed down a lot more by
now, but every release still comes with new features - Sway 0.12 added
redshift support and binary space partitioning layouts. Sway 0.13.0 is
coming soon and includes, among other things, nvidia proprietary driver support.
We already have some interesting features slated for Sway 0.14.0, too!

Today Sway has 21,446 lines of C (and 4,261 lines of header files) written by 81
authors across 2,263 commits. These were written through 653 pull requests and
529 issues. Sway packages are available today in the official repos of pretty
much every distribution except for Debian derivatives, and a PPA is available
for those guys.

For those who are new to the project,  [Sway](http://swaywm.org)  is an
i3-compatible Wayland compositor. That is, your existing  [i3](http://i3wm.org/) 
configuration file will work as-is on Sway, and your keybindings and colors and
fonts and for_window rules and so on will all be the same. It’s i3, but for
Wayland, plus it’s got some bonus features. Here’s a quick rundown of what’s
new since the  [previous state of Sway](/2016/12/27/State-of-sway.html) :

* Redshift support
* Improved security configuration
* Automatic binary space partitioning layouts ala AwesomeWM
* Support for more i3 window criterion
* Support for i3 marks
* xdg_shell v6 support (Wayland thing, makes more native Wayland programs work)
* We’ve switched from X.Y to X.Y.Z releases, Z releases shipping bugfixes while
the next Y release is under development
* Lots of i3 compatibility improvements
* Lots of documentation improvements
* Lots of bugfixes

The new  [bounty program](https://github.com/SirCmpwn/sway/issues/986)  has also
raised $1,200 to support Sway development! Several bounties have been awarded,
including redshift support and i3 marks, but every awardee chose to redonate
their reward to the bounty pool. Thanks to everyone who’s donated and everyone
who’s worked on new features! Bounties have also been awarded for features in
the Wayland ecosystem beyond Sway - a fact I’m especially proud of. If you want
a piece of that $1,200 pot,  [join us on
IRC](http://webchat.freenode.net/?channels=sway&uio=d4)  and we’ll help you get started.

Many new developments are in the pipeline for you. 0.13.0 is expected to
ship within the next few weeks -  [here’s a sneak peek at the
changelog](https://github.com/SirCmpwn/sway/issues/1162#issuecomment-295012255) .
In the future releases, development is ongoing for tray icons (encouraged by the
sweet $270 bounty sitting on that feature), and several other features for
0.14.0 have been completed. We’ve also started work on a long term project to
replace our compositor plumbling library, wlc, with a new one:
 [wlroots](https://github.com/SirCmpwn/wlroots) . This should allow us to fix many
of the more difficult bugs in Sway, and opens the doors for  *many*  features that
weren’t previously possible. It should also give us a platform on which we can
build standard protocols that other compositors can implement, unifying the
Wayland platform a bit more.

Many thanks to  [everyone that’s contributed to
sway](https://github.com/SirCmpwn/sway/graphs/contributors) ! There’s no way Sway
would have enjoyed its success without your help. That wraps things up for
today, thanks for using Sway and look forward to Sway 1.0!

Note: future posts like this will omit some of the stats that were included in
the previous posts. You can use the following commands to find them for
yourself:

```
# Lines of code per author:
git ls-tree -r -z --name-only HEAD -- */*.c \
    | xargs -0 -n1 git blame --line-porcelain HEAD \
    | grep  "^author " | sort | uniq -c | sort -nr
# Commits per author:
git shortlog
```
