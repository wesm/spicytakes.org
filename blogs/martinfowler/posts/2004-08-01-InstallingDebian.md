---
title: "Installing Debian"
description: "In recent months I've gone on a major binge of installingDebianLinux. In the last few months have seen a lot of new environments appear in my setup. I've acquired a new desktop machine which I install"
date: 2004-08-01T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/InstallingDebian.html
slug: InstallingDebian
word_count: 975
---


In recent months I've gone on a major binge of installing [Debian](http://www.debian.org/) Linux. In the last few months
have seen a lot of new environments appear in my setup. I've acquired
a new desktop machine which I installed Windows XP on, a Powerbook
laptop with MacOS X, and a new work laptop with windows XP. All of
these involve various amounts of work, even my work laptop, which came
with a Thoughtworks configured Windows XP already on it, needed work
to install the various applications that I use in my work.


The Debian part of the this saga is twofold. Firstly switching my
Linux basement server from RedHat to Debian, and secondly adding a
Debian desktop to my primary desktop machine.


The server part always is the most tense, because I really do
like servers to just work. It's an old box (I got it about six years
ago) but works well primarily a file server (smb and cvs) and a music
server ([Slimp3](https://martinfowler.com/bliki/Slimp3.html)). The OS on the server was old (RedHat 7.2)
basically because upgrading is such a pain that I didn't do it. I
picked Debian because they don't upgrade very often and have a
reputation for being very conservative with their stable
distribution.


Of course the install process for Debian is famously awful, but
the good thing about a server is that you don't have to deal with X,
which does a great deal to remove the pain of the process. It still
turned out to be rather involved. Although Debian installed fine on
the machine, it didn't properly recognize the shiny new 250G hard
drive I decided to stick in it. To do that needed a new version of the
kernel, one that was just a rev higher than what was available as a
package. I thus had the joy of a kernel recompile. I'd not done this
before, so this wasn't likely to decrease my stress level, but thanks
to [this](http://www.osnews.com/story.php?news_id=2949) and
[this](http://newbiedoc.sourceforge.net/system/kernel-pkg.html),

I coped.


Once things were installed, I busied myself with getting things
that were working under RedHat working under Debian. The bottom line
is that if the application is properly supported under Debian's
package management system (apt-get), everything is so easy it feels
like cheating. The complications arise when either the packages aren't
available with apt-get (Java), or the apt-get packages aren't quite up
to date (rexml). Even then it's no worse than any other unix, it's
just that it feels so much worse because it isn't done with
apt-get.


The desktop system was rather less fraught, but still involved a
fair bit of trial and error. I'd actually been using a Debian desktop
system for a couple months on my old desktop machine. Once I got my
new laptop I felt it was time to configure Debian as an alternative
boot on my primary (and much faster) desktop machine. My number one
tip for playing with Debian desktop systems is don't use the official
installer - not even the [brand new one](http://www.debian.org/devel/debian-installer/)
developed for Debian Sarge. The Sarge installer is good as far as it
goes, but it doesn't go far enough to include configuring X - and
configuring X is a horror which involves the installer asking you a
bevy of questions that I don't even understand, let alone answer. The
contrast between setting up Windows on a new desktop and getting X to
go can't get more stark.


Fortunately you can dodge this pain by using [Knoppix](http://www.knoppix.org/), or one of its [customizations](http://www.knoppix.net/docs/index.php/KnoppixCustomizations).

My previous experimental desktop had used [Morphix Lite GUI](http://www.morphix.org/modules/news/), a
Knoppix customization with a lightweight UI that runs better on older
machines. For my new machine I wanted something more powerful, KDE or
Gnome. As it turned out this was rather messier than I hoped. While
the installs went without incident, three times the system was hosed
during the apt-get upgrade. On two of those the boot record was
broken and I had to reboot and reinstall from the live CD. I
eventually managed to get a working and up to date KDE desktop, but
without google and some educated guessing I would have been
stuck.


All in all I can say that while the Knoppix-like installs help,
it still was not a straightforward process.  I haven't had the time
yet to work with KDE to see if I like it. Other distributions are
probably much easier, certainly the RedHat 9 install was easier, but
still caught me out on the upgrades.


## Update - August 2004


All of what I said above is still valid, but there's a bit more
story to tell. Although the Morphix based install on my desktop was
mostly fine, it has a couple of minor irritations. The biggest of
these was on the UI. The X setup for some reason had about a 1/4â on
the left and right of screen that was beyond the monitor. So if a
window or icon moved right to the sides of the screen, I couldn't see
them on the screen. I could live with this, but it was still a pain.
Again X Windows setup looks so crummy next to windows where setting up
the GUI has always been easy.


Trying to fix this took far too much time. I experimented again
with the latest version of the new sarge installer, but it's X
configuration stuff was still as hopeless as before. The way I finally
solved it was to install RedHat 9 on a bit of spare disk and then copy
the XF86Config file over to my debian installation. I needed to add in
the font path entries from the debian file, but after that I can
finally don't have any hidden edges. So the good news is that it's
working, but the bad news is that this is a horribly baroque way to
sort out a GUI.
