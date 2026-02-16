---
title: "Questionable Advice: “People Used To Take Me Seriously. Then I Became A Software Vendor”"
date: 2023-03-29
url: https://charity.wtf/2023/03/29/questionable-advice-people-used-to-take-me-seriously-then-i-became-a-software-vendor/
word_count: 2626
---


I recently got a plaintive text message from my magnificent friend [Abby Bangser](http://twitter.com/a_bangser), asking about a conversation we had several years ago:


> “Hey, I’ve got a question for you. A long time ago I remember you talking about what an adjustment it was becoming a vendor, how all of a sudden people would just discard your opinion and your expertise without even listening. And that it was SUPER ANNOYING.
> I’m now experiencing something similar. Did you ever find any good reading/listening/watching to help you adjust to being on the vendor side without being either a terrible human or constantly disregarded?”


Oh my.. This brings back memories. ☺️🙈


Like Abby, I’ve spent most of my career as an engineer in the trenches. I have also spent a *lot* of time cheerfully talking smack about software. I’ve never really had anyone question my experience[1] or my authority as an expert, hardened as I was in the flames of a thousand tire fires.


Then I started a software company. And all of a sudden this bullshit starts popping up. Someone brushing me off because I was “selling something”, or dismissing my work like I was fatally compromised. I shrugged it off, but if I stopped to think, it really bothered me. Sometimes I felt like yelling “HEY FUCKERS, I am one of your kind! I’m trying to HELP YOU. Stop making this so hard!” 😡 (And sometimes I actually did yell, lol.)


That’s what I remember complaining to Abby about, five or six years ago. It was all very fresh and raw at the time.


We’ll get to that. First let’s dial the clock back a few *more* years, so you can fully appreciate the rich irony of my situation. (Or skip the story and jump straight to “Five easy ways to make yourself a vendor worth listening to“.)


## The first time I encountered “software for sale”


My earliest interaction with software vendors was at [Linden Lab](http://secondlife.com). Like most infrastructure teams, most of the software we used was open source. But somewhere around 2009? 2010? Linden’s data engineering team began auditioning vendors like Splunk, Greenplum, Vertica[2], etc for our data warehouse solution, and I tagged along as the sysinfra/ops delegate.


For two full days we sat around this enormous table as vendor after vendor came by to demo and plump their wares, then opened the floor for questions.


One of the very first sales guys did something that pissed me off me. I don’t remember exactly what happened — maybe he was ignoring my questions or talking down to me. (I’m certain I didn’t come across like a seasoned engineering professional; in my mid twenties, face buried in my laptop, probably wearing pajamas and/or pigtails.) But I do remember becoming very irritated, then settling in to a stance of, shall we say, oppositional defiance.


I peppered every sales team *aggressively* with questions about the operational burden of running their software, their architectural decisions, and how canned or cherry-picked their demos were. Any time they let slip a sign of weakness or betrayed uncertainty, I bore down harder and twisted the knife. I was a ✨royal asshole✨. My coworkers on the data team found this extremely entertaining, which only egged me on.


What the fuck?? 🫢😧🫠 I’m not usually an asshole to strangers.. where did that *come from*?


## What open source culture taught me about sales


I came from open source, where contempt for software vendors was apparently *de rigueur*. (is it *still* this way?? seems like it *might* have gotten better? 😦) It is fascinating now to look back and realize how much attitude I soaked up before coming face to face with my first software vendor. According to my worldview at the time,

1. Vendors are liars
2. They will say *anything* to get you to buy
3. Open source software is always the safest and best code
4. Software written for profit is inherently inferior, and will ultimately be replaced by the inevitable rise of better, faster, more democratic open source solutions
5. Sales exists to create needs that ought never to have existed, then take you to the cleaners
6. Engineers who go work for software vendors have either sold out, or they aren’t good enough to hack it writing *real *(consumer facing) software.


I’m remembering Richard Stallman trailing around behind me, up and down the rows of vendor booths at USENIX in his St IGNUcious robes, silver disk platter halo atop his head, offering (begging?) to lay his hands on my laptop and bless it, to “free it from the demons of proprietary software.” Huh. ([Remember THIS song?](https://www.youtube.com/watch?v=AdmHNaFaD08) 🎶 😱)


Given all that, it’s not hugely surprising that my first encounter with software vendors devolved into hostile questioning.


(It’s fun to speculate on the origin of some of these beliefs. Like, I bet 3) and 4) came from working on databases, particularly Oracle and MySQL/Postgres. As for 5) that sounds an awful lot like the beauty industry and other products sold to women. 🤭)


## Behind every software vendor lies a recovering open source zealot(???)


I’ve had many, many experiences since then that slowly helped me dismantle this worldview, brick by brick. Working at Facebook made me realize that open source successes like Apache, Haproxy, Nginx etc are exceptions, not the norm; that this model is only viable for certain types of general-purpose infrastructure software; that governance and roadmaps are a huge issue for open source projects too; and that if steady progress is being made, at the end of the day, somewhere *somebody* is probably paying those developers.


I learned that the overwhelming majority of production-caliber code is written by **somebody** **who was paid to write it** — not by volunteers. I learned about coordination costs and overhead, how expensive it is to organize an army of volunteers, and the pains of decentralized quality control. I learned that you really *really* want the person who wrote the code to stick around and own it for a long time, and not just on alternate weekends when they don’t have the kids (and/or they happen to feel like it).


I learned about game theory, and I learned that **sales is about relationships**. Yes, there are unscrupulous sellers out there, just like there are shady developers, but good sales people don’t *want* you to walk away feeling tricked or disappointed any more than you want to *be* tricked or disappointed. They want to exceed your expectations and deliver more value than expected, so you’ll keep coming back. In game theory terms, it’s a “repeated game”.


I learned SO MUCH from interviewing sales candidates at Honeycomb.[3] Early on, when nobody knew who we were, I began to notice how much our sales candidates were **obsessed with value**. They were constantly trying to puzzle out out how much value Honeycomb actually brought to the companies we were selling to. I was not used to talking or thinking about software in terms of “value”, and initially I found this* incredibly offputting* (can you believe it?? 😳).


## Sell unto others as you would have them sell unto you


Ultimately, this was the biggest (if dumbest) lesson of all: I learned that **good software has tremendous value**. It unlocks value and creates value, it pays enormous ongoing dividends in dollars and productivity, and the people who build it, support it, and bring it to market fully deserve to recoup a slice of the value they created for others.


There was a time when I would have bristled indignantly and said, “**we didn’t start honeycomb to make money!**” I would have said that the reason we built honeycomb because we knew as engineers what a radical shift it had wrought in how we built and understood software, and we didn’t want to live without it, ever again.


But that’s not quite true. Right from the start, Christine and I were intent on building not just great software, but [a great software *business*](https://charity.wtf/2022/01/20/how-engineering-driven-leads-to-engineering-supremacy/). It wasn’t personal wealth we were chasing, it was independence and autonomy — the freedom to build and run a company the way we thought it should be run, building software to radically empower other engineers like ourselves.


Guess what you have to do if you care about freedom and autonomy?


Make money. 🙄☺️


I also realized, belatedly, that most people who start software companies do so for the same damn reasons Christine and I did… to solve hard problems, share solutions, and help other engineers like ourselves. If all you want to do is get rich, this is actually a pretty stupid way to do that. **Over 90% of startups fail**, and even the so-called “success stories” aren’t as predictably lucrative as RSUs. And then there’s the wear and tear on relationships, the loss of social life, the vicissitudes of the financial system, the ever-looming spectre of failure … 👻☠️🪦 Startups are brutal, my friend.


## Karma is a bitch


None of these are particularly novel insights, but there was a time when they were definitely news to *me*. ☺️ It was a pretty big shock to my system when I first became a software vendor and found myself sitting on the other side of the table, the freshly minted target of hostile questioning.


These days I am far less likely to be cited as an objective expert than I used to be. I see people on Hacker News dismissing me with the same scornful wave of the hand as I used to dismiss other vendors. Karma’s a bitch, as they say. What goes around comes around. 🥰


I used to get very bent out of shape by this. “You act like I only care because I’m trying to sell you something,” I would hotly protest, “but it’s exactly the opposite. I *built something* *because* *I cared*.” That may be true, but it doesn’t change the fact that vested interests can create blind spots, ones I might not even be aware of.


And that’s ok! My arguments/my solutions should be sturdy enough to withstand any disclosure of personal interest. ☺️


Some people are jerks; I can’t control that. But there are a few things I *can* do to acknowledge my biases up front, play fair, and just generally be the kind of vendor that I personally would be happy to work with.


## Five easy ways to make yourself a vendor worth listening to


So I gave Abby a short list of a few things I do to try and signal that I am a trustworthy voice, a vendor worth listening to. (What do you think, did I miss anything?)


**🌸 Lead with your bias.🌸

**I always try to disclose my own vested interest up front, and sometimes I exaggerate for effect: “As a vendor, I’m contractually obligated to say this”, or “Take it for what you will, obviously I have religious convictions here”. Everyone has biases; I prefer to talk to people who are aware of theirs.


**🌸 Avoid cheap shots.🌸 **

Try to engage with the most powerful arguments for your competitors’ solutions. Don’t waste your time against straw men or slam dunks; go up against whatever ideal scenarios or “steel man” arguments they would muster in their own favor. Comparing your strengths vs  their strengths results in a way more interesting, relevant and USEFUL discussion for all involved.


**🌸 Be your own biggest critic.🌸 **

Be forthcoming about the flaws of your own solution. People *love it* when you are unafraid to list your own product’s shortcomings or where the competition shines, or describe the scenarios where other tools are genuinely superior or more cost-effective. It makes you look strong and confident, not weak.


What would you say about your own product *as an engineer*, or a customer? Say that.


**🌸 You can still talk shit about software, just not your competitors‘ software. 🌸 **

I try not to gratuitously snipe at our competitors. It’s fine to speak at length about technical problems, differentiation and tradeoffs, and to address how specifically your product compares with theirs. But confine your shit talking to categories of software where you *don’t* have a personal conflict of interest.


Like, I’m not going to get on twitter and take a swipe at a monitoring vendor (anymore 😇), but I *might* say rude things about a language, a framework, or a database I have no stake in, if I’m feeling punchy. ☺️ (This particular gem of advice comes by way of [Adam Jacob](http://twitter.com/adamhjk).)


**🌸 Be generous with your expertise.🌸**

If you have spent years going deep on one gnarly problem, you might very well know that problem and its solution space more thoroughly than almost anyone else in the world. Do you know how many people you can *help* with that kind of mastery?! A few minutes from you could potentially spare someone days or weeks of floundering. This is a gift few can give.


It feels good, and it’s a nice break from battering your head against unsolvable problems. **Don’t restrict your help to paying customers,** and, obviously, don’t give self-serving advice. Maybe they can’t buy/don’t need your solution today, but maybe someday they will.


## In conclusion


There’s a time and place for being oppositional. Sometimes a vendor gets all high on their own supply, or starts making claims that aren’t just an “optimistic” spin on the facts but are provably untrue. If any vendor is operating in poor faith they deserve to to be corrected.


But it’s a shitty, self-limiting stance to take as a default. We are all here to *build things, *not tear things down. No one builds software alone. The code you write that defines your business is just the wee tippy top of a colossal iceberg of code written by other people — device drivers, libraries, databases, graphics cards, routers, emacs. All of this value was created by other people, yet we collectively benefit.


Think of how many gazillion lines of code are required for you to run just one AWS Lambda function! Think of how much cooperation and trust that represents. And think of all the deals that brokered that trust and established that value, compensating the makers and allowing them to keep building and improving the software we all rely on.


We build software together. Vendors exist to help you. We do what we do best, so you can spend your engineering cycles doing what *you* do best, working on your core product. Good sales deals don’t leave anyone feeling robbed or cheated, they leave *both* sides feeling happy and excited to collaborate.[4]


🐝💜Charity.


[1] Yes, I know this experience is far from universal; LOTS of people in tech have not felt like their voices are heard or their expertise acknowledged. This happens disproportionately to women and other under-represented groups, but it also happens to plenty of members of the dominant groups. It’s just a really common thing! However that has not really been my experience — or if it has, I haven’t noticed — nor Abby’s, as far as I’m aware.


[2] My first brush with [columnar storage systems](https://www.honeycomb.io/blog/why-observability-requires-distributed-column-store)! Which is what makes [Honeycomb](http://honeycomb.io) possible today.


[3] I have learned SO MUCH from watching the world class sales professionals we have at Honeycomb. Sales is a tough gig, and doing it well involves many disciplines — empathy, creativity, business acumen, technical expertise, and so much more. Selling to software engineers in particular means you are often dealing with cocky little shits who think they could do your job with a few lines of code. On behalf of my fellow little shits engineers, I am sorry. 🙈


[4] Like our sales team says: “Never do a deal unless you’d do both sides of the deal.” I fucking love that.
