---
title: "My (hypothetical) SRECon26 keynote (xpost)"
date: 2026-03-03
url: https://charity.wtf/2026/03/03/my-hypothetical-srecon26-keynote-xpost/
word_count: 1508
---


# My (hypothetical) SRECon26 keynote


*One year ago, Fred Hebert and I delivered the closing keynote at SRECon25. Looking back on it now, I can hardly connect with how I felt then. Here’s what I’d say one year later.*


[Crossposted from here. ](https://charitydotwtf.substack.com/p/my-hypothetical-srecon26-keynote)


Hey, it’s almost time for [SRECon 2026](http://usenix.org/conference/srecon26americas)! (I can’t go, but YOU really should!)


Which means it was almost a year ago that [Fred Hebert](http://ferd.ca/) and I were up on stage, delivering the [closing keynote](https://www.usenix.org/conference/srecon25americas/presentation/majors)[1](https://charitydotwtf.substack.com/p/my-hypothetical-srecon26-keynote#footnote-1-189584921) at SRECon25.


We argued that SREs should get involved and skill up on generative AI tools and techniques, instead of being naysayers and peanut gallerians. You can get a feel for the overall vibe from the description:


> It’s easy to be cynical when there’s this much hype and easy money flying around, but generative AI is not a fad; it’s here to stay.
> Which means that even operators and cynics — no, especially operators and cynics — need to get off the sidelines and engage with it. How should responsible, forward-looking SREs evaluate the truth claims being made in the market without being reflexively antagonistic?


Yep, that was our big pitch. Don’t be *reflexively* antagonistic. You should learn AI *so that* your critiques will land with credibility.


That is not the message I would give today, if I were keynoting SRECon26.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%216A3s%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb8458b4-f5fe-4e53-a5a7-94cbe057e946_467x374.jpeg?w=375&ssl=1)


## I came out of a hole, and the world had changed


I’ve been in a bit of a hole for the past few months, trying to get the [second edition](https://charitydotwtf.substack.com/p/observability-engineering-a-book?r=j8fxh) of “[Observability Engineering](https://charitydotwtf.substack.com/p/first-i-wrote-the-wrong-book-then?r=j8fxh)” written and shipped.


Maybe the hole is why this feels so abrupt and discontinuous to me. Or maybe it’s just having such a clear artifact of my views one year ago. I don’t know.


What I do know is that one year ago, I still thought of generative AI as one more really big integration or use case we had to support, whether we liked it or not. Like AI was a slop-happy toddler gone mad in our codebase, and our sworn duty as SREs was to corral and control it, while trying not be a *total* dick about it.


Today, it’s very clear to me that the center of gravity has shifted from cloud/automation workflows to AI/generation workflows, and that the agentic revolution has only just begun. That toddler is heading off to school. With a loaded gun.


## When the facts change, I change my mind


I don’t know when exactly that bit flipped in my head, I only know that it did. And as soon as it did, I felt like the last person on earth to catch on. I can barely connect with my own views from eleven months ago.


Were my views *unreasonably *pessimistic? Was I willfully ignoring credible evidence in early 2025?


Hmm, perhaps. But Silicon Valley hype trains have not exactly covered themselves in glory in recent years. VR/AR, crypto/web3/NFTs, wearable tech, the Metaverse, 3D printing, the sharing economy…this is not an illustrious string of wins.[2](https://charitydotwtf.substack.com/p/my-hypothetical-srecon26-keynote#footnote-2-189584921)


Cloud computing, on the other hand: genuinely huge. So was the Internet. Sometimes the hype train brings you internets, sometimes the hype train brings you tulips.


So no, I don’t think it was obvious in early 2025 that AI generated code would soon grow out of its slop phase. Skepticism was reasonable for a time, and then it was not. I know *a lot* of technologists who flipped the same bit at some point in 2025.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21HW5-%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38d6a745-2502-4250-92c0-fe57e14d6b01_560x682.jpeg?w=230&ssl=1)


## The keynote I would give today


If I was giving the keynote at SRECon 2026, I would ditch the begrudging stance. I would start by acknowledging that AI is radically changing the way we build software. It’s here, it’s happening, and it is coming for us all.


#### 1 — This is happening


It is very, very hard to adjust to change that is being forced on you. So please don’t wait for it to be forced on you. **Swim out to meet it**. Find your way in, find something to get excited about.


As Adam Jacob recently advised,


> “If you’re an engineer or an operations person, there is only one move. You have to start working in this new way as much as you can. If you can’t do it at work, do it at home. You want to be on the frontier of this change, because the career risk to being a laggard is incredibly high.” — [Adam Jacob](https://www.linkedin.com/posts/adamjacob_if-youre-thinking-to-yourself-this-10x-activity-7431057194520936448-ZTFL?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAEP-B4Bn1IFS4Br7okfkI7z81XqQEOEKro)


This AI shit is *not hard*. The early days of any technology are the simplest, and this technology more than most. Conquer the brain weasels in your head by learning the truth of this for yourself.


#### 2 — Know thyself


At a time of elevated uncertainty and anxiety, our natural human tendency to drift into confirmation bias and disconfirmation bias is higher than ever. Whatever proof you instinctively seek out, you are guaranteed to find.


The best advice I can give anyone is: **know your nature, **and** lean against it**.

- If you are a reflexive naysayer or a pessimist, *know that, *and force yourself to find a way in to wonder, surprise and delight.
- If you are an optimist who gets very excited and tends to assume that everything will improve: *know that*, and force yourself to mind real cautionary tales.


Try to keep your aperture wide, and remain open to possibilities you find uncomfortable. Curate the ocean you swim in. Puncture your bubble.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21pGnW%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe78b88bf-51a5-4382-b9be-37a99af4dc4e_588x616.jpeg?w=288&ssl=1)


#### 3 — Don’t panic


Don’t panic, and don’t give in to despair. The future isn’t written yet, and nobody knows what’s going to happen. I sure as hell don’t. Neither do you.


The fact that AI has radically changed the way we develop software in very a short time, and seems poised to change it much more in the next year or two, is real and undeniable.


This does not mean that everything else predicted by AI optimists will come to pass.


Extraordinary claims still require extraordinary evidence. AGI is, at present, an elaborate thought experiment, one that contradicts all the evidence we currently have about how technological breakthroughs typically yield enormous change in the early days, and then plateau.


## We are all technologists now


Here’s another Adam quote I really like:


> The bright side is that it’s a technology shift, not a manufacturing shift – meaning you still have to have technologists to do it.


I’ve written a number of blog posts over the years where I have advised people to go into the second half of their career thinking of themselves not as “engineers” or as “managers”, but as “technologists”. [3](https://charitydotwtf.substack.com/p/my-hypothetical-srecon26-keynote#footnote-3-189584921)


Every great technologist needs an arsenal of skills on top of their technical expertise. They need to understand how to navigate an organization, how to translate between the language of technology and the language of the business; how to wield influence and drive results across team, company, even industry lines.


These remain durable skills, in an era where good code can be generated practically for free.


## This is the moment for pragmatists


Many people who love the art and craft of software are struggling in this moment, as the value of that craft is diminishing.


People who take a much more…functional…approach to software seem to be thriving in the present chaos. “Functional” describes most of the SREs I know, including myself.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21Q-p1%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc420de1-1487-423c-8bf3-0d446803b7a1_1418x1696.jpeg?w=270&ssl=1)


After all, SREs have always been judged by outcomes — uptime, reliability, whether the thing kept running. An [outcome orientation](http://o16g.com/) turns out to be excellent preparation for a world where the “how” of software is becoming less important than the what and the whether, across the board.


So maybe the advice we gave at SRECon wasn’t so bad after all. Especially this part:


> Which means that even operators and cynics — no, especially operators and cynics — need to get off the sidelines and engage with it.


Who can build better guardrails for AI, than SREs and operators who have spent their entire careers building guardrails for software engineers and customers?


The industry needs us. But not begrudgingly, eyerollingly, pretending to get on board in order to slow things down from the inside. The industry needs our skills to help engineering teams go fast forever.


Don’t sit back and wait for change to reach you. Run towards the waves. It’s nice out here.


1 — Our talk was called “[AIOps: Prove it! An Open Letter to Vendors Selling AI for SREs](https://www.usenix.org/conference/srecon25americas/presentation/majors)”. In retrospect, this was a terrible title. It was not an open letter to vendors at all; if anything, it was an open letter to SREs. It started out as one topic, but by the time the event rolled around, it had morphed into something entirely different. Ah well.


2 — I am not even listing the kooky religious shit like effective accelerationism, transhumanism, AI “alignment” or the Singularity, all of which has seeped into the water table around these parts.


3 — Omg, I have *so many* unwritten posts wriggling around in my brain right now on this topic.
