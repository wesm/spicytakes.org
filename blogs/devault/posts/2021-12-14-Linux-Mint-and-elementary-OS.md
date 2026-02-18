---
title: "Impressions of Linux Mint & elementary OS"
date: 2021-12-14
url: https://drewdevault.com/2021/12/14/Linux-Mint-and-elementary-OS.html
slug: Linux-Mint-and-elementary-OS
word_count: 956
---

In a  [recent post](https://drewdevault.com/2021/12/05/What-desktop-Linux-needs.html) , I spoke about some things that Linux distros need to do
better to accommodate end-users. I was reminded that there are some Linux distros
which are, at least to some extent, following my recommended playbook, and have
been re-evaluating two of them over the past couple of weeks:  [Linux Mint](https://linuxmint.com)  and
 [elementary OS](https://elementary.io) . I installed these on one of my laptops and used it as my daily
driver for a day or two each.

Both of these distributions are similar in a few ways. For one, both distros
required  *zero*  printer configuration: it just worked. I was very impressed with
this. Both distros are also based on Ubuntu, though with different levels of
divergence from their base. Ubuntu is a reasonably good choice: it is very
stable and mature, and commercially supported by Canonical.

I started with elementary OS, which does exactly what I proposed in my earlier
article: charge users for the OS. 1  The last time I tried elementary, I was
less than impressed, but they’ve been selling the OS for a while now so I hoped
that with a consistent source of funding and a few years to improve they would
have an opportunity to impress me. However, my overall impressions were mixed,
and maybe even negative.

The biggest, showstopping issue is a problem with their full disk encryption
setup. I was thrilled to see first-class FDE support in the installer, but upon
first boot, I was presented with a blank screen. It took me a while to figure
out that a different TTY had cryptsetup running, waiting for me to enter the
password. This is  *totally*  unacceptable, and no average user would have any
clue what to do when presented with this. This should be a little GUI baked into
the initramfs which prompts for your password on boot, and should be a regularly
tested part of the installer before each elementary release ships.

The elementary store was also disappointing, though I think there’s improvements
on the horizon. The catalogue is  *very*  sparse, and would benefit a lot by
sourcing packages from the underlying Ubuntu repositories as well. I think
they’re planning on a first-class Flatpak integration in a future release, which
should improve this situation. I also found the apps a bit  *too*  elementary,
haha, in that they were lacking in a lot of important but infrequently used
features. In general elementary is quite basic, though it is also very polished.
Also, the default wallpaper depicts a big rock covered in bird shit, which I
thought was kind of funny.

There is a lot to like about elementary, though. The installer is really
pleasant to use, and I really appreciated that it includes important
accessibility features during the install process. The WiFi configuration is
nice and easy, though it prompted me to set up online accounts  *before* 
prompting me to set up WiFi. All of the apps are intuitive, consistently
designed, and beautiful. I also noticed that long-running terminal processes I
had in the background would pop-up a notification upon completion, which is a
nice touch. Overall, it’s promising, but I had hoped for more. My suggestions to
elementary are to consider that completeness is a kind of polish, to work on
software distribution, and to offer first-class options for troubleshooting,
documentation, and support within the OS.

I tried Linux Mint next. Several years ago, I actually used Mint as my daily
driver for about a year — it was the last “normal” distribution I used
before moving to Arch and later Alpine, which is what I use now. Overall, I was
pretty impressed with Mint after a couple of days of use.

Let’s start again with the bad parts. The installer is not quite as nice as
elementary’s, though it did work without any issues. At one point I was asked if
I wanted to “enable multimedia codecs” with no extra context, which would
confuse me if I didn’t understand what they were. I was also pretty pissed to
see the installer advertising nonfree, predatory services like Netflix and
YouTube to me — distributions have no business advertising this kind of
shit. Mint also has encryption options, but it’s based on ecryptfs rather than
LUKS, and I find that this is an inferior approach. Mint should move to
full-disk encryption.

I also was a bit concerned about the organizational structure of Linux Mint.
It’s unclear who is responsible for Linux Mint, how end-users can participate,
or how donations are spent or how other financial concerns are addressed. I
think that Linux Mint needs to be more transparent, and should also consider how
its allegiance with proprietary services like Netflix acts as a long-term
divestment from the FOSS ecosystem it relies on.

That said, the actual experience of using Linux Mint is very good. Unlike
elementary OS, the OS feels much more  *comprehensive* . Most of the things a
typical user would need are there, work reliably, and integrate well with the
rest of the system. Software installation and system upkeep are very easy on
Linux Mint. The aesthetic is very pleasant and feels like a natural series of
improvements to the old Gnome 2 lineage that Cinnamon can be traced back to,
which has generally moved more in the direction that I would have liked Gnome
upstream to. The system is tight, complete, and robust. Nice work.

In conclusion, Linux Mint will be my recommendation for “normal” users going
forward, and I think there is space for elementary OS for some users if they
continue to improve.

1. I downloaded it for free, however, because I did not anticipate that I would continue to use it for more than a couple of days. ↩︎
