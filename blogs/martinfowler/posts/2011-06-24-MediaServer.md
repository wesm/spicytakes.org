---
title: "Media Server"
description: "I recently decided to upgrade my homeMediaServerand   got anHP N36L. So far I'm happy   with it."
date: 2011-06-24T00:00:00
tags: ["gadgets"]
url: https://martinfowler.com/bliki/MediaServer.html
slug: MediaServer
word_count: 529
---


I recently decided to upgrade our home server setup. I posted
  some thoughts about what I was planning to do here, and now I've
  updated this page with what I did.


Before the upgrade I had a home server machine running Debian
  that provided:

- some samba shares, which are only used occasionally
- backups with rsync
- music streaming with [Squeezebox](https://martinfowler.com/bliki/Squeezebox.html)
- dhcp server, so I can pin the IP addresses of regular devices


It's not much, but it's useful stuff. The box that ran it was
  rather old (I got it in 2005) and I wanted to reduce its
  power consumption. I also wanted to increase its hard drive storage,
  since it used IDE drives, which are now rather passé.


At the same time, I wanted to do something about video. Netflix
  streaming is increasingly useful, and there other online video
  sources I could make use of.


In the end I went for an [HP_N36L](https://martinfowler.com/bliki/HP_N36L.html) for the new home server and a
  [WD TV](https://www.amazon.com/gp/product/B003MVZ60I/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B003MVZ60I&linkCode=as2&tag=martinfowlerc-20) for video.


## Discarded Options


The first suggestion I got for this was a Mac Mini. There's
    some good software for running it through the video system, and I
    can feed VGA into the TV. Its power draw is low and it could
    replace the server. But the more I looked into it, the less I
    liked it:

- it's expensive ($700)
- I'm more familiar with Debian based servers
- I'd need to use external drives to get the storage I'd like


Jeff Atwood [built a low power media server](http://www.codinghorror.com/blog/2011/03/revisiting-the-home-theater-pc.html)that could also handle both
  things together. I ended up not fancying having it all in a single
  machine - preferring the ability to upgrade them independently. I
  was also less keen on a Windows solution as I'm more familiar with
  Unix servers.


Several people suggested using NAS (Network Attached
  Storage). There are some very flexible NAS units out there, which
  support hot-swapping of hard drives and automatic RAID
  mirroring. I don't really see the need for hot-swapping as it's rare
  for me to change a hard drive and I don't mind bouncing the server
  when I do it. I also see little point in RAID mirroring. It does
  protect you from a hard drive failure - but that's not the only
  thing that can go wrong. RAID won't protect you from `rm
  important_file`. So my preference is regular, automated,
  backups. This also allows the backup hard drive to be well away from
  the server box.


NAS would allow file sharing, but wouldn't support the other
  options. Some NASs are hackable, but I decided I'd rather have a
  bare server that I can put a stock distribution on and go from
  there.


Another possible video option was [Boxee](http://www.boxee.tv/). This would be very flexible, but
  also more pricey and complex than the WDTV. I felt the WDTV would do
  for now and I could always change later should I need to. There's
  actually a lot of options for video but the need for Netflix and
  analog outputs constrained my decision.


## Other thoughts


Some other bloggers I read had similar things to think
    about

- [Tim
    Bray](http://www.tbray.org/ongoing/When/201x/2011/03/06/Music-Bitch) (read the excellent comments).
- [Jeff Atwood](http://www.codinghorror.com/blog/2011/03/revisiting-the-home-theater-pc.html)
