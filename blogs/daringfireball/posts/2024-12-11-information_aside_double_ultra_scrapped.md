---
title: "The Information Suggests, in an Aside, That Apple Scrapped Work on a Quad-Max/Double-Ultra M-Series Chip"
date: 2024-12-11
url: https://daringfireball.net/2024/12/information_aside_double_ultra_scrapped
slug: information_aside_double_ultra_scrapped
word_count: 1521
---


Wayne Ma and Qianer Liu, in a piece today for The Information (paywalled up the wazoo, sadly), “[Apple Is Working on AI Chip With Broadcom](https://www.theinformation.com/articles/apple-is-working-on-ai-chip-with-broadcom)”:


> Apple is developing its first server chip specially designed for
> artificial intelligence, according to three people with direct
> knowledge of the project, as the iPhone maker prepares to deal
> with the intense computing demands of its new AI features. Apple
> is working with Broadcom on the chip’s networking technology,
> which is crucial for AI processing, according to one of the
> people. If Apple succeeds with the AI chip — internally
> code-named Baltra and expected to be ready for mass production by
> 2026 — it would mark a significant milestone for the company’s
> silicon team. [...]
> Broadcom typically doesn’t license its intellectual property,
> choosing instead to sell chips directly to customers. In its
> [arrangement with Google](https://www.theinformation.com/articles/to-reduce-ai-costs-google-wants-to-ditch-broadcom-as-its-tpu-server-chip-supplier), for instance, Broadcom translates
> Google’s AI chip blueprints into designs that can be manufactured,
> oversees its production with TSMC and sells the finished chips to
> Google at a markup.
> But Broadcom appears to be taking a different tack with Apple.
> Broadcom is providing a more limited scope of design services to
> Apple while still providing the iPhone maker with its networking
> technology, one of the people said. Apple is still managing the
> chip’s production, which TSMC will handle, another person said.
> Additional details of the business arrangement couldn’t be learned 
> [*sic*]1


I’ll go out on a limb and say that it’s Apple choosing to take a different tack with Broadcom than Google did, rather than a choice in any way driven by Broadcom. The Information’s own “arrangement with Google” link above points to [this year-ago report](https://www.theinformation.com/articles/to-reduce-ai-costs-google-wants-to-ditch-broadcom-as-its-tpu-server-chip-supplier) that opens: “Google executives have extensively discussed dropping Broadcom as a supplier of artificial intelligence chips as early as 2027, according to a person with direct knowledge of the effort. In that scenario, Google would fully design the chips, known as tensor processing units, in-house, the person said. The move could help Google save billions of dollars in costs annually as it invests heavily in AI development, which is especially pricey compared to other types of computing.” Why would Apple ever agree to an arrangement like that?


The hint of obsequiousness to Broadcom suggests to me, pretty clearly, that it’s sources from Broadcom who provided the leaks for this story.


Anyway, what *really* caught my eye in this report wasn’t the AI server chips, but rather the following (emphasis to key paragraph added), included seemingly only as an aside even though I thought it was the most interesting nugget in the report (vague shades of Fermat’s Last Theorem):


> Apple’s silicon design team in Israel is leading development of
> the AI chip, according to two of the people. That team was
> instrumental in designing the processors Apple introduced in 2020
> to replace Intel chips in Macs.
> *Apple this past summer canceled the development of a
> high-performance chip for Macs — consisting of four smaller chips
> stitched together — to free up some of its engineers in Israel to
> work on the AI chip, one of the people said, highlighting the
> company’s shifting priorities.*
> To make the chip, Apple is planning to use one of TSMC’s most
> advanced manufacturing processes, known as N3P, said three
> people with direct knowledge. That would be an improvement over
> the manufacturing process used for Apple’s latest computer
> processor, the M4.


What they’re talking about regarding a cancelled high-end Mac chip would be a hypothetical M-series chip with (effectively) double the specs of an Ultra, which I presume would only be available in a future Mac Pro, and, just pulling adjectives from Apple’s marketing dictionary, I’d bet would be called the “M# Extreme” (where “#” is the M-series generation number). The M1 and M2 Ultra chips are, effectively, two M1/M2 Max chips fused together with something called a silicon interposer that offers extremely high-speed I/O between the fused chips. Performance doesn’t exactly double, [but it comes close](https://arstechnica.com/gadgets/2023/06/m2-ultra-mac-studio-review-who-needs-a-mac-pro-anyway/). A hypothetical quad-Max “Extreme” would effectively double the performance of the same-generation Ultra chips. Such a chip, available exclusively in the Mac Pro, would give the Mac Pro a much more obvious reason to exist alongside the Mac Studio (which, to date, has offered Max and Ultra chip configurations).


But if Apple’s work on that quad-interposed M-series chip was cancelled only “this past summer”, and was for a generation of chips using TSMC’s next-generation N3P process, that would mean it was slated for the M5 or M6 generation, not the M4.2 The M4 generation is fabbed using TSMC’s N3E process, and any additional variants beyond the M4 Max, slated for updated Mac Studios and Mac Pros next year, were designed long before this past summer.


I feel like it’s a lock that there will be an M4 Ultra chip next year, with the performance of two M4 Max chips fused together. Or, perhaps the M4 Ultra will be a standalone design, not two Max chips fused. The M-series Max chips have always been their own designs — not two Pro chips fused together. The same could be true for Ultra chips, starting next year, or some generation further into the future.


But I’ve had my fingers crossed that we’ll also see an “M4 Extreme” — or whatever Apple would decide to call a tier above “Ultra” — sooner rather than later. If The Information’s reporting is correct, however, either we’ll see a quad-Max M4 chip next year, and then it will skip a generation because the engineering team was redirected to work on these AI server chips, or, those engineers were working on the *first* quad-Max M-series chips, and now the first such M-series chips have been punted even further into the future, if ever. Today’s report has me thinking, sadly, that could be a few years off, at the soonest.


---

1. That *sic* is for the missing sentence-ending period. I expect better copy editing from [a $400/year subscription](https://www.theinformation.com/subscribe) (soon going to $500) that keeps badgering me, every time I visit the site, to upgrade to a $1,000/year “Pro” subscription tier. But while I’m slagging on The Information for this sentence, the missing period is the least of its problems. “Additional details of the business arrangement couldn’t be learned” is some passive voice bullshit. What they mean is that Wayne Ma and Qianer Liu were unable to learn any additional details, not that additional details of the business arrangement between Apple and Broadcom are some sort of unknowable information — you know, like the answer to why I continue paying so much money to subscribe to a publication that annoys me. ↩︎
2. Or even the M7 generation. The lead times on chip designs are measured in years, plural. Back in July 2023, just after the release of the M2-generation Mac Studio models (offering the M2 Max and M2 Ultra) and the first — and so far only — Apple silicon Mac Pro (M2 Ultra), Jason Snell and Myke Hurley got the following tidbit from an anonymous listener of their podcast Upgrade ([episode 468](https://www.relay.fm/upgrade/468); [transcript](http://podsearch.david-smith.org/episodes/7329)). Hurley read it on air, right up front around the 4:00 mark:

I am an Apple engineer working on the GPU team.
It pains me to say that Jason’s speculation is correct. The quad
chip has been canned with no plans to return. For context, we are
actively developing what will presumably be the M5 chip. And the
quad chip was only ever specced for the M1 and removed late in the
project. There are no plans to create a quad chip through at least
the M7 generation. My understanding is that the quad required too
much effort for too small of a market. Something interesting that
may come in the M8 and future generations is called multi-die
packaging. This allows the CPU and GPU parts of the chip to be
fabricated on different dies and packaged together much like how
two max chips make an ultra. With this design, it is conceivable
that we could have three, four, or five or more GPU dies with one
or two CPU for a graphics powerhouse or vice versa for a CPU
workstation that doesn’t need as much GPU grunt. However, as far
as I know, no such plans exist yet.

Take that with however many grains of salt you think necessary to season a comment from an anonymous person, but it doesn’t hit a single false note to my ears. And if this little Upgrade birdie was legit, that would suggest that the Israeli chip engineers reassigned from an advanced 4× Mac chip this past summer to work on a new AI server chip would have been working on the M6 generation of Apple silicon, for products launching in 2026–2027. ↩︎︎



| **Previous:** | [Don’t Throw the Baby Out With the Generative AI Bullshit Bathwater](https://daringfireball.net/2024/12/dont_throw_the_baby_out_with_the_generative_ai_bullshit_bathwater) |
| **Next:** | [Federico Viticci on Apple Intelligence, With ChatGPT, as a Breakthrough Automation Tool](https://daringfireball.net/2024/12/viticci_apple_intelligence_chatgpt_automation) |


PreviousNext