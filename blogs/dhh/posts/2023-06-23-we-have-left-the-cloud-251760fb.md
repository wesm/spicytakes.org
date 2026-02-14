---
title: "We have left the cloud"
date: 2023-06-23
url: https://world.hey.com/dhh/we-have-left-the-cloud-251760fb
slug: we-have-left-the-cloud-251760fb
word_count: 976
---

Since it took us years to get into the cloud in the first place, I originally imagined it would take us years
[to get out](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
as well. But all that work to containerize our applications and prepare them for the cloud actually turned out to make it relatively easy to exit. And now, after six months of effort, it's done. We're out. The last application was brought home to our own hardware on Wednesday. Hallelujah!
In those six months, we brought home six heritage services that we're no longer selling, but have committed to support for existing customers and users
[until the end of the internet](https://basecamp.com/about/policies/until-the-end-of-the-internet)
. Basecamp Classic, Highrise, Writeboard, Campfire, Backpack, and Ta-da List are all over a decade old, but continue to serve tens of thousands of people, and
[generate millions of dollars in revenue](https://world.hey.com/dhh/until-the-end-of-the-internet-439ccfce)
. But now we'll be spending far less to operate them, and as a bonus to those users, provide a
[considerably faster experience](https://world.hey.com/dhh/cloud-exit-pays-off-in-performance-too-4c53b697)
due to the powerful new hardware.
But the big move was
[HEY](https://www.hey.com/)
. This is an application that was born in the cloud. We'd never run it on our own hardware before, and as a
[full-featured email service](https://www.hey.com/features/)
, it had a lot of moving parts. But the team pulled this off without a hitch by doing the move in several stages, with different databases, cache servers, mail services, and app instances moving independently over the course of a few weeks.
Our stack for bringing home all these applications is entirely open source. We use KVM to slice our new monster 192-thread Dell R7625s into isolated VMs, then Docker to run the containerized applications, and finally
[Kamal](https://kamal-deploy.org)
to do zero-downtime app deploys and rollbacks. This setup helped us dodge the complexity of Kubernetes, and
[avoid any sort of enterprisey service contract entanglements](https://world.hey.com/dhh/the-only-thing-worse-than-cloud-pricing-is-the-enterprisey-alternatives-854e98f3)
.
The back of the napkin math is that
[we'll save at least $1.5 million per year](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa)
by owning our own hardware rather than renting it from Amazon. And crucially, we've been able to do this without changing the size of the operations team at all. Running our applications in the cloud just never provided the promised productivity gains to do with any smaller of a team anyway.
This is possible because the way we operate our own hardware actually isn't too dissimilar from how people use rental clouds like AWS. We buy new hardware from
[Dell](https://www.dell.com/)
, have it shipped directly to the two data centers we use, and ask the white-glove service hands at
[Deft](https://deft.com)
to rack the new machines. Then we see the new IP addresses pop online, and can immediately put them to work with KVM/Docker/Kamal.
The main difference here is the lag time between needing new servers and seeing them online. It truly is incredible that you can spin up 100 powerful machines in the cloud in just a few minutes, but you also pay dearly for the privilege. And we just don't have such an unpredictable business as to warrant this premium. Given how much money we're saving owning our own hardware, we can afford to dramatically over-provision our server needs, and then when we need more, it still only takes a couple of weeks to show up.
Look at it this way. We spent about half a million dollars buying two pallets of servers from Dell, which added a combined
[4,000 vCPUs with 7,680 GB of RAM and 384TB of NVMe storage](https://world.hey.com/dhh/the-hardware-we-need-for-our-cloud-exit-has-arrived-99d66966)
to our server capacity. This hardware was more than adequate to run all the heritage services we brought home, together with HEY, and give our other Basecamp operations a hardware refresh. And it was
*less than a third the cost*
of what we predict we'll be saving EVERY YEAR! This is hardware we'll be amortizing over five years.
No wonder that sharing our experience with this cloud exit has made a lot of companies think twice about the insane cloud rental bills they're incurring every month. Our
[collective cloud budget](https://dev.37signals.com/our-cloud-spend-in-2022/)
last year was $3.2m, and this was incredibly optimized, with long service commitments, scrupulous right-sizing and monitoring. There are lots of companies paying many times what we did for even less benefit. The potential savings are as large as the AWS quarterly results are staggering.
[AWS generated over $5 billion in profits for Amazon just in 2022 Q4](https://www.cnbc.com/2023/02/02/amazon-aws-earnings-q4-2022.html)
!
As I've mentioned before, I still think the cloud has a place for companies early enough in their lifecycle that the spend is either immaterial or the risk that they won't be around in 24 months is high. Just be careful that you don't look at those lavish cloud credits as a gift! It's a hook. And if you tie yourself too much to their proprietary managed services or serverless offerings, you'll find it very difficult to escape, once the bills start going to the moon.
I also think that there are probably some companies that have such high variance in their loads that renting makes sense. If you only need a plough thrice a year, it doesn't make much sense keeping it in the barn unused for the remaining 363 days.
But most established companies that can amortize capital investments over a few years should seriously reconsider the cloud craze. The benefits have been vastly overstated. The cloud is often just as complicated as running things yourself, and it's usually ridiculously more expensive.
So if the money matters –
[and when does it not?](https://world.hey.com/dhh/cut-cloud-before-payroll-a4530ebd)
– I urge you to do your own math. Consider whether you have a service that really benefits from constantly scaling the capacity up and down. Then have a serious look at what
[your own cloud exit](https://world.hey.com/dhh/five-values-guiding-our-cloud-exit-638add47)
could look like. We pulled out seven applications in six months. You can do that too. The tools are there. They're free. So don't just stay in the cloud because of the hype.
