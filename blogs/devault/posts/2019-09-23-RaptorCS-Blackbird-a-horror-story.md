---
title: "RaptorCS POWER9 Blackbird PC review"
date: 2019-09-23
url: https://drewdevault.com/2019/09/23/RaptorCS-Blackbird-a-horror-story.html
slug: RaptorCS-Blackbird-a-horror-story
word_count: 1161
---

**November 2018** : Ordered  [Basic Blackbird
Bundle](https://www.raptorcs.com/content/BK1B01/intro.html)  w/32 GB RAM:
$1,935.64

**Update 2019-12-23** : This article was originally titled “RaptorCS POWER9
Blackbird PC: An expensive mistake”. Please read the follow-up article,
published 2019-10-10:
 [RaptorCS’s redemption: the POWER9 machine works](https://drewdevault.com/2019/10/10/RaptorCS-redemption.html)

**June 2019**

Order ships, and arrives without RAM. It had been long enough that I didn’t
realize the order had only been partially fulfilled, so I order some RAM from
the  [list of recommended chips](https://wiki.raptorcs.com/wiki/POWER9_Hardware_Compatibility_List/Memory)  ($338.40), along with the other necessities
that I didn’t purchase from Raptor: a case ($97.99) and a PSU ($68.49), and grab
some hard drives I have lying around. Total cost: about $2,440. Worth it to get
POWER9 builds working on builds.sr.ht!

I carefully put everything together, consulting the manual at each step, plug in
a display, and turn it on. Lights come on, things start whizzing, and the screen
comes to life - and promptly starts boot looping.

**June 27th**

Support ticket created. What’s going on with my board?

**June 28th**

Support gets back to me the next day with a suggestion which is unrelated to the
problem, but no matter - I spoke with volunteers in the IRC channel a few hours
earlier and we found out that - whoops! - I hadn’t connected the CPU power to
the motherboard. This is the end of the PEBKAC errors, but not the end of the
problems. The machine gets further ahead in the boot - almost to “petitboot”,
and then the display dies and the machine reveals no further secrets.

I sent an update to the support team.

**July 1st**

> We have normally only seen this type of failure when there is a RAM-related
> fault, or if the PSU is underpowered enough that bringing the CPUs online at
> full power causes a power fault and immediate safety power off. 
>  Can you watch the internal lights while the system is booting, and see if the
> power LED cluster immediately changes from green to orange as the system stops
> responding over SSH?

The IRC channel suspects this is not related to the problem. Regardless, I reply
a few hours later with two videos showing the boot up process from power-out to
display death, with the internal LEDs and the display output clearly visible.

**July 4th**

“Any progress on this issue?”, I ask.

**July 15th**

“Hi guys, I’m still experiencing this problem. If you’re unsure of the issue I
would like to send the board back to you for diagnosis or a refund.”

**July 25th**

> Sorry for the delay. Having senior support check out the videos. 
>  Thanks for writing back. We should have something for you by tomorrow during
> the day.

**July 31st**

> Hi Drew. 
>  The videos are being reviewed this week. Thank you for sending them. 
>  Please stay tuned.

**September 15th**

No reply from support. I have since bought a little more hardware for
self-diagnosis, namely the necessary pieces to connect to the two (or is it 3?)
serial ports. I manage to get a log, which points to several failures, but none
of them seem to be related to the problem at hand (they do indicate some network
failures, which would explain why I can’t log into the BMC over SSH for further
diagnosis). And the getty is looping, so I can’t log in on the serial console to
explore any further.

That was a week ago. Radio silence since.

So, 10 months after I placed an order for a POWER9 machine, 3 months after I
received it (without the RAM I purchased, no less), and over $2,500 invested…
it’s clear that buying the Blackbird was an expensive mistake. Maybe someday
I’ll get it working. If I do, I doubt the “support” team will have been
involved. Currently my best bet seems to be waiting for some apparent staff
member (the only apparent staff member) who idles in the IRC channel on Freenode
and allegedly comes online from time to time.

I’m not alone in these problems. Here are some (anonymized) quotes I’ve heard
from others while trying to troubleshoot this on IRC.

On support:

> ugh, ddevault, yeah. [Blackbird ownership] has not been a smooth experience
> for me, either.

> my personal theory is that they have really bad ticket software that ’loses'
> tickets somehow

On reliability:

> I’ve found openbmc’s networking to be… a bit unreliable… maybe 20% of the
> time it does not responed[sic]/does not respond fast enough to networking
> requests.

> yeah the vga handoff failing doesn’t surprise me (other people here have
> reported it). but the BMC not getting a DHCP lease is odd. (well maybe not
> that odd if you look at the crumminess of the OpenBMC software stack…)

So, yeah, don’t buy from Raptor Computer Systems. It’s too large and unwieldly
to be an effective paper weight, either!

**Erratta**

*2019-09-24 @ 00:19 UTC* : Raptor has reached out and apologized for my support
experience. We are discussing these problems in more detail now. They have also
issued a refund for the unshipped RAM.

*2019-09-24 @ 00:51 UTC* : Raptor believes the CPU to be faulty and is shipping a
replacement. They attribute the delay to having to reach out to IBM about the
problem, but don’t have a satisfactory answer to why the support process failed.
I understand it’s being discussed internally.

*2019-09-24 @ 13:08 UTC* :

> After investigation, we are implementing new mechanisms to avoid support
> issues like the one you experienced. We now have a self-serve RMA generation
> system which would have significantly reduced your wait time, and are taking
> measures to ensure that tickets are no longer able to be ignored by front line
> support staff. We believe we have addressed the known failure modes at this
> time, and management will be keeping a close eye on the operation of the
> support system to ensure that new failure modes are handled rapidly.

They’ve tweeted this about their new self-service RMA system as well:

> We’ve made it easy to submit RMA requests for defective products on our Web
> site. Simply go to your account, select the “Submit RMA Request” link, and
> fill out the form.  Your product will be warranty checked and, if valid, you
> will receive an RMA number and shipping address!

— @RaptorCompSys via  [Twitter](https://twitter.com/RaptorCompSys/status/1176432946670186498)

I agree that this shows positive improvements and a willingness to continue
making improvements in their support experience. Thanks to Raptor for taking
these concerns seriously. I hope to have a working Blackbird system soon, and
will publish a follow-up review when the time comes.

*2019-10-08 @ 22:30 UTC*  A source quoted anonymously in this article asked me to
remove their quote, after a change of heart. They feel that the attention this
article has received has made their statement reach beyond the level of
dissatisfaction they had with Raptor at the time.
