---
title: "RaptorCS's redemption: the POWER9 machine works"
date: 2019-10-10
url: https://drewdevault.com/2019/10/10/RaptorCS-redemption.html
slug: RaptorCS-redemption
word_count: 917
---

This is a follow-up to my earlier article, “ [RaptorCS POWER9 Blackbird PC: An
expensive mistake](https://drewdevault.com/2019/09/23/RaptorCS-Blackbird-a-horror-story.html) ”. Since I published that article, I’ve been in
touch with Raptor and they’ve been much more communicative and helpful. I now
have a working machine!

Update Feb. 2024: Seems the improvements I asked for may not have stuck.  [Buyer
beware](https://posixcafe.org/blogs/2024/02/26/0/) .

After I published my article, Raptor reached out and apologised for my
experience. They offered a full refund, but I agreed to work on further
diagnosis now that we had opened a dialogue 1 . They identified that my CPU was
defective and sent me a replacement, then we found the mainboard to be
defective, too, and the whole thing was shipped back and replaced. I installed
the new hardware into the datacenter today and it was quite pleasant to get up
and running. Raptor assures me that my nightmares with the old board are
atypical, and if the new board is representative of the usual user experience, I
would have to agree. The installation was completely painless. 2

However, I refuse to give any company credit for waking up their support team
only when a scathing article about them frontpages on Hacker News. I told them I
wouldn’t publish a positive follow-up unless they also convinced me that the
support experience had been fixed for the typical user as well. To this end,
Raptor has made a number of substantive changes. To quote their support staff:

> After investigation, we are implementing new mechanisms to avoid support
> issues like the one you experienced. We now have a
> [self-serve RMA generation system](https://twitter.com/RaptorCompSys/status/1176432946670186498)
> which would have significantly reduced your wait time, and are taking measures
> to ensure that tickets are no longer able to be ignored by front line support
> staff. We believe we have addressed the known failure modes at this time, and
> management will be keeping a close eye on the operation of the support system
> to ensure that new failure modes are handled rapidly.

They’ve tweeted this about their new self-service RMA system as well:

> We’ve made it easy to submit RMA requests for defective products on our Web
> site. Simply go to your account, select the “Submit RMA Request” link, and
> fill out the form.  Your product will be warranty checked and, if valid, you
> will receive an RMA number and shipping address!

— @RaptorCompSys via  [Twitter](https://twitter.com/RaptorCompSys/status/1176432946670186498)

They’re also working on other improvements to make the end-user experience
better, including  [more content on the
wiki](https://wiki.raptorcs.com/wiki/Main_Page) , such as a  [flowchart for
dealing with common
problems](https://wiki.raptorcs.com/wiki/Troubleshooting/Support_Request_Checklist) .

Thanks to Raptor for taking the problem seriously, quickly fixing the problems
with my board, and for addressing the systemic problems which led to the
failure of their support system.

On the subject of the working machine, I am quite impressed with it so far.
Installation was a breeze, it compiles the kernel on 32 threads from spinning
rust in 4m15s, and I was able to get KVM working without much effort. I have
christened it “flandre” 3 , which I think is fitting. I plan on bringing it up
as a build slave for builds.sr.ht in the coming weeks/months, and offering
ppc64le builds on Sourcehut in the near future. I have another board which was
generously donated by another Raptor customer 4 , which arrived last week and
that I hope to bring up and use for testing Wayland before introducing it to the
Sourcehut fleet.

P.S. For those interested in more details of the actual failures:

This machine is so badly broken that it would actually be hilarious if the
manufacturer had been more present in the troubleshooting process. I think the
best way to sum it up is “FUBAR”. Among problems I encountered were:

* The CPU experiences a “ZCAL failure” (???)
* The BMC (responsible for bringing up the main CPU(s)) had broken ethernet,
making login over SSH impossible
* The BMC’s getty would boot loop, making login over serial impossible
* The BMC’s u-Boot would boot loop if the TX pin on the serial cable was plugged
in, making diagnosing issues from that stage impossible
* petitboot’s ncurses output was being piped into a shell and executed (what the fuck?)

In the immortal words of James Mickens, “I HAVE NO TOOLS BECAUSE I HAVE
DESTROYED MY TOOLS WITH MY TOOLS.” A staff member at Raptor tells me:
“Your box ended up on my desk […] This is easily the most broken board I’ve
seen, ever, and that includes prototypes. This will help educate us for a while
to come due to the unique nature of some of the faults.”

Not sure what can cause such an impressive cacophony of failures, but it’s so
catastrophic that I can easily believe that this is far from typical. The
hardware is back in Raptor’s hands now, and I would be interested to hear about
their insights after further diagnosis.

1. They did refund the RAM which was unfulfilled from my original order. ↩︎
2. They did give me a little heart attack, however, by sending the replacement CPU to me in the same box I had returned the faulty CPU back to them with - a box which I had labelled “BAD CPU”. ↩︎
3. Sourcehut virtual machines are named after their purpose, but our physical servers are named after [Touhou](https://en.wikipedia.org/wiki/Touhou_Project) characters. ↩︎
4. This happened prior to any of the problems with the first machine. ↩︎
