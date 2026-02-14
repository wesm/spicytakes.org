---
title: "The hardware we need for our cloud exit has arrived"
date: 2023-04-06
url: https://world.hey.com/dhh/the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966
slug: the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966
word_count: 778
---

It's been a long time since I last saw a physical piece of hardware used to run our services at
[37signals](https://37signals.com/)
. I vaguely remember doing a tour of our Chicago data center over a decade ago, but somewhere along the line, I just lost interest in the iron itself. Now the interest is back, because
[hardware is fun again](https://world.hey.com/dhh/hardware-is-fun-again-b819d0b4)
, so let me share my excitement with you!

![server-pallets.jpg](https://world.hey.com/dhh/99d66966/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTE3Njk2MDY4NiwicHVyIjoiYmxvYl9pZCJ9fQ--dadb9431b789b211b9d78250f2b72c8ec62a79eac690eedb5d801f51756803fd/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--b3779d742b3242a2a5284869a45b2a113e0c177f0450c29f0baca1ee780f6604/server-pallets.jpg)

These are the two pallets that showed up in our Chicago data center recently. The same day that an identical set arrived in Ashburn, Virginia for our second data center. In total, we received twenty R7625 Dell servers that'll power the bulk of our cloud exit. It's a staggering amount of computing power in a shockingly small footprint.
Here's a diagram of our four cabinets in Chicago (we have another four in Ashburn). As you can tell, there's still a bunch of older hardware dedicated to Basecamp in particular. A good chunk of that will actually get retired, once we're done setting things up. But all the 2U servers marked "kvm" at the bottom of the cabinets are the new ones:

![cabinets.png](https://world.hey.com/dhh/99d66966/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTE3Njk4ODQxMywicHVyIjoiYmxvYl9pZCJ9fQ--0b7a41e3f02ee3db12b8014c17a2230db66db6ef9ca0820d72a71c111b090bf3/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/cabinets.png)

You can spot the new R7625s at the bottom of the actual racks here, next to the older gear:

![IE106_Front.jpg](https://world.hey.com/dhh/99d66966/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTE3Njk3MjU4MywicHVyIjoiYmxvYl9pZCJ9fQ--24390dc8f1032955f45dc0f80d32229c8afd75f81c2d5d7179ef43c2271b61c3/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fbGltaXQiOlsxNjAwLDEyMDBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--5064b479ada3ee025b93adf2e61206b234743c66d57c07df4b23f2fdbbf13ba5/IE106_Front.jpg)


![IH106_Front.jpg](https://world.hey.com/dhh/99d66966/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTE3Njk3Mjk0MSwicHVyIjoiYmxvYl9pZCJ9fQ--0e6bd05f7219dba352a477283c5ad3f594047378d5c939f17ba003fee8d6adc9/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fbGltaXQiOlsxNjAwLDEyMDBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--5064b479ada3ee025b93adf2e61206b234743c66d57c07df4b23f2fdbbf13ba5/IH106_Front.jpg)

Each of these R7625s contain two AMD EPYC 9454 CPUs running at 2.75GHz with 48 cores / 96 threads. That means we're adding almost 4,000 vCPUs to our on-premise fleet! And a ridiculous 7,680 GB of RAM! And 384TB of Gen 4 NVMe storage! Serious horsepower and headroom for years to come. In addition to this, we have another ~six database servers showing up between now and this summer, and then we'll be set.
The contrast to the origin of Basecamp is funny. We launched Basecamp on a single-core Celeron server with just 256MB of RAM back in 2004. Spinning rust at 7,200 RPM. And that was good enough to get the business from part-time to full-time in about a year.
Almost twenty years later, we now have a long lineage of legacy applications (because we promise to keep applications customers depend on running
[until the end of the internet](https://37signals.com/policies/until-the-end-of-the-internet/)
!), some massive flagship services in
[Basecamp](https://basecamp.com/)
and
[HEY](https://www.hey.com/)
, and a mission to get it all running on hardware we own ourselves again.
It's kinda wild to think that it's been less than three months since we decided to scrap Kubernetes and pursue a simpler solution for the cloud exit with
[Kamal](https://kamal-deploy.org)
. And that we've already moved half of the cloud applications that need to come home!
Over the next month or so, we plan to bring home both Basecamp Classic (still a multi-million dollar business, even if it hasn't been updated in about 13 years – that SaaS magic!), as well as the grand prize of the cloud exit: HEY! That'll leave us with just Highrise and a small auxiliary service called Portfolio left in the cloud as we start the month of May.
I thought we were already being optimistic when we
[planned a total cloud exit](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa)
by the end of summer, but now it seems we'll basically be done by the end of spring instead. Truly a remarkable achievement by the team working on this effort.
The reality of our accelerated timeline has made me even more bullish on cloud exits in general. I imagined getting out of the cloud was going to be as hard as getting in. But that just hasn't proven to be the case. Though perhaps it's helped that we've had that nuts number of
[$38,000/week in cloud spend](https://37signals.com/podcast/leaving-the-cloud-part-2/)
as a motivating carrot to get it done quickly!
I seriously hope that other SaaS entrepreneurs looking at their daunting cloud bills are paying attention. Once you've gone cloud, it might seem impossible to contemplate getting out again, but don't believe that for a second.
Modern server hardware is incredible. We've taken huge leaps forward in performance, density, and cost over the last few years. If you haven't run the numbers since cloud became the default in the past decade, you really ought to do so now. The numbers might just shock you as much as they did us.
So the end is now clearly in sight. We've solved all the key technical challenges we needed to address to make the cloud exit happen. We've been running production apps on Kamal for a while now. The path is clear, and I can't wait for those mammoth cloud bills evaporate. I think we're going to find that the napkin math I did for
[our public calculation of savings](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa)
will be highly conservative. But we'll see and we'll share.
