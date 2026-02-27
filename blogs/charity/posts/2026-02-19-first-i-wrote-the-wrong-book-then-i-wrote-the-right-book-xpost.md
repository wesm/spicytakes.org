---
title: "First I wrote the wrong book, then I wrote the right book (xpost)"
date: 2026-02-19
url: https://charity.wtf/2026/02/19/first-i-wrote-the-wrong-book-then-i-wrote-the-right-book-xpost/
word_count: 2066
---


I’m not sure whether to say “thank you” or “HOW COULD YOU DO THIS TO ME”, but this one goes out to all the people who sent me advice on buying software last fall.


This is the second in a two-part episode. The first part ended on a ✨cliffhanger!!!✨ — so if you missed the first episode, catch up here:


#### [Martin Fowler told me the second edition should be shorter (it’s twice as long)](https://charitydotwtf.substack.com/p/observability-engineering-a-book)

[Charity Majors](https://substack.com/profile/32306597-charity-majors)

## Six long weeks of writer’s block


I was merrily cranking away what I believed to be my last chapter when I asked the internet — YOU guys — for help the first time. “[Are you an experienced software buyer? I could use some help](https://charity.wtf/2025/09/19/are-you-an-experienced-software-buyer-i-could-use-some-help/),” went up on September 19th, 2025.


The response was overwhelming. I heard from software engineers, SREs, observability leads, CTOs, VPs, distinguished engineers, consultants, even the odd CISO. All these emails and responses and lengthy threads kept me busy for a while, but eventually I had to get back to writing. That’s when I discovered, to my unpleasant surprise, that I couldn’t seem to *write* anymore.


“Well,” I reasoned, “maybe I’ll just ask the internet for EVEN MORE advice” — and out popped [Buffy-themed post number two](https://charity.wtf/2025/10/13/got-opinions-on-observability-i-could-use-your-help-once-more-with-feeling/), on October 13th.


Keep in mind, I thought I would be done by then. November was my *stretch* deadline, my *just in case*, *I better leave myself some breathing room* kind of deadline.


As November 1st came and went, my frustration began spiraling out into blind panic. *What the hell is going on and why can I not finish this???*


## In which I finally listen to the advice I asked for


A week before Thanksgiving, I was up late tinkering with Claude. I imported all the emails and advice I had gotten from y’all, and started sorting into themes and picking out key quotes, and that is when it finally hit me: I had written the wrong thing.


No, this deserves a bigger font.


## **✨I wrote the wrong thing.✨**


I wrote the wrong thing, for the wrong people, and none of it was going to move the needle in any meaningful way.


The chapters I had written were full of practical advice for observability engineering teams and platform engineering teams, wrestling with implementation challenges like instrumentation and cost overflows. Practical stuff.


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21IWQT%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c32f200-fecf-4ac9-b3cf-99c913cb083f_276x277.png?resize=276%2C277&ssl=1)

*Yes.*


## The internet was right (this ONE time)


My inbox, on the other hand, was overflowing with stories like these:

- “Many times [competitive research] is faked. One person has their favorite option and then they do just enough ‘competitive analysis’ to convince the sourcing folks that due diligence was done or to nullify the CIO/CTO/whoever is accepting this on to their budget”
- “We [the observability team] spent six months exhaustively trialing three different solutions before we made a decision. The CEO of one of the losing vendors called our CEO, and he **overruled our decision** without even telling us.” (Does your CEO know anything at all about engineering??) “No.”
- “Our SRE teams have vetoed any attempt to modernize our tool stack. ($Vendor) is part of their identity, and since they would have to help roll out and support any changes, **we are stuck living in 2015** apparently forever.” (What does management have to say?) “It’s been twenty years since they touched a line of code.”
- “We’re weird in that most of the company hates technology and really hates that we have to pay for it since they don’t understand the value it brings to the company. **This is intentional ignorance**, we make the value props continually and well, we just haven’t succeeded yet….We’re a little obsessed with trying to get champagne quality at Boone’s prices.”
- “When it comes to dealing with salespeople and the enterprise sales process, the best tip for engineers is to not anthropomorphize sales professionals who are driven by commission. The best ones are like robot lawn mowers dressed in furry unicorn costumes. They may seem cute and nice but they do not care about anything besides closing the next deal….All of the best SaaS companies are full of these **friendly fake unicorn zombies who suck cash** instead of blood.”


Nearly all of the emails I got were either describing a terminally fucked up buying process from the top down, or the long term consequences of those fucked up decisions.


In other words: I was writing tactical advice for teams who were surviving in a strategic vacuum.


So I threw the whole thing out, and started over from scratch. 😭


## Even good teams are struggling right now


As Tolstoy once wrote, “Happy teams are all alike; every fucked up team is fucked up in its own precious way.”


There is an infinity of ways to screw something up. But there is one pattern I see a critical mass of engineering orgs falling into right now, even orgs that are generally quite solid. That is when there is **no shared alignment** or even shared *vocabulary* between engineering and other stakeholders directors, VPs and SVPs, CTO, CIO, principal and distinguished engineers — on some pretty clutch questions. Such as:

- “What is observability?”
- “Who needs it?”
- “What problem are we trying to solve?”


And my favorite: “Is observability still relevant in a post-AI era? Can’t agents do that stuff now?”


Even some generally excellent CTOs[1] have been heard saying things like, “yeah, observability is definitely very important, but all our top priorities are related to AI right now.”


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21XKMm%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1918c101-46be-42ed-9a04-0179dcde8e6f_328x322.png?resize=328%2C322&ssl=1)


Which gets causality *exactly backwards*. Because your ability to get any returns on your investments into AI will be limited by how swiftly you can validate your changes and learn from them. Another word for this is “OBSERVABILITY”.


Enough ranting. Want a peek? I’ll share the new table of contents, and a sentence or two about a couple of my own favorite chapters.


## Part 6: “Observability Governance” (v2)


The new outline is organized to speak to technical decision-makers, starting at the top and loosely descending. What do CTOs need to know? What do VPs and distinguished engineers need to know? and so on. We start off abstract, and become more concrete.


Since every technical term (e.g. high cardinality, high dimensionality, etc) has become overloaded and undifferentiated by too much sales and marketing, we mostly avoid it. Instead, we use the language of systems and feedback loops.


Again, we are trying to help your most senior engineers and execs develop a shared understanding of “What problem are we solving?” and “What is our goal? Technical terms can actually detract and distract from that shared understanding.

1. **An Open Letter to CTOs:** **Why Organizational Learning Speed is Now Your Biggest Constraint**. Organizations used to be limited by the speed of delivery; now they are limited by how swiftly they can validate and understand what they delivered.
2. **Systems Thinking for Software Delivery**. Observability is the signal that connects the dots to make a feedback loop; no observability*,* *no loop*. What happens to amplifying or balancing loops when that signal is lossy, laggy, or missing?
3. **The Observability Landscape Through a Systems Lens**. What feedback loops do developers need, and what feedback loops does ops need? How do these map to the tools on the market?
4. **The Business Case for Observability**. Is your observability a cost center or an investment? How should you quantify your RoI?
5. **Diagnosing Your Observability Investment**
6. **The Organizational Shift**
7. **Build vs Buy (vs Open Source)**
8. **The Art and Science of Vendor Partnerships.** Internal transformations run on trust and credibility; vendor partnerships run on trust and reciprocity. We’ll talk about both of these, as well as how to run a strong POC.
9. **Instrumentation for Observability Teams**
10. **Where to Go From Here**


Hey, I have *a lot* of empathy right now for leaders and execs who feel like they’re behind on everything. I feel it too. Anyone who doesn’t is lying to themselves (or their name is [Simon Willison](http://x.com/simonw)).


But the role observability plays in complex sociotechnical systems is one of those foundational concepts **you need to understand**. You’re not gonna get this right by accident. You’re not going to win by doing the same thing you were doing five years ago. And if you screw up your observability, you screw up everything downstream of it too.


To those of you who do understand this, and are working hard to drive change in your organizations: I see you. It is hard, often thankless work, but it is **work worth doing**. If I can ever be of help: reach out.


## A longer book, but a better book


The last few chapters are heading into tech review on Friday, February 20th. *Finally*. The last 3.5 months have been some of the most panicky and stressful of my life. I….just typed several paragraphs about how terrible this has been, and deleted them, because you do not need to listen to me whine. ☺️


Like I said, [I have never felt especially proud of the first edition](https://charitydotwtf.substack.com/p/observability-engineering-a-book). I am not UN proud, it’s just…eh. I feel differently this time around. I think—I *hope*—it can be helpful to a lot of different people who are wrestling with adapting to our new AI-native reality, from a lot of different angles.[2]


![](https://i0.wp.com/substackcdn.com/image/fetch/%24s_%21OS1m%21%2Cw_1456%2Cc_limit%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7250b64f-137d-415f-92be-6ee06aca3039_475x322.png?resize=475%2C322&ssl=1)

*Thanks, Christine. (Another for the folder marked ”NOW YOU TELL ME”)*


I am incredibly grateful to my co-authors, collaborators, and our editor, Rita Fernando, without whom I never would have made it through.


But there’s one more group that deserves some credit, and it’s…you guys. I asked for help, and help I got. So many people wrote me such long, thought-provoking emails full of stories, advice and hard-earned wisdom. The better the email, the more I peppered you with followup questions, which is a great way to punish a good deed.


## Blame these people


I am a tiny bit torn on whether to say “thank you” or “fuck you”, because my life would have been *much nicer* if I had stuck to the plan and wrapped in October.


But the following list of people were especially instrumental in forcing me to rethink my approach. It made the book much stronger, so if you catch one of them in the wild, please buy them a stiff drink. (Or buy yourself one, and throw it in their face with my sincere compliments.)

- **Abraham Ingersoll**, the aforementioned “odd CISO”, who would be quoted in the book had his advice not been so consistently unprintable by the standards of respectable publications
- **Benjamin Mann** of Delivery Hero, who I would work for in a heartbeat, and not just for the way he wields “NOPE” as a term of art
- **Marty Lindsay**, who has spent more time explaining POCs and tech evals to me than anyone should have to. (If you need an o11y consultant, Marty should be your very first stop).
- **Sam Dwyer**, whose stories seeded my original plan to write a set of chapters for observability engineering teams. (I hope the replacement plan is useful too!)


Many others sent me terrific advice, and endured multiple rounds of questions and more questions and clarifications on said questions. A few of them:


**Matthew Sanabria, Chris Cooney, Glen Mailer, Austin Culbertson, John Scancella, John Doran, Bryan Finster, Hazel Weakly, Chris Ziehr, Thomas Owens, Mike Lee, Jay Gengelbach, Will Hegedus, Natasha Litt, Alonso Suarez, Jason McMunn, Evgeny Rubtsov, George Chamales, Ken Finnegan, Cliff Snyder, Robyn Hirano, Rita Canavarro, Matt Schouten, Shalini Samudri Ananda Rao (Sam)**.


I am definitely forgetting some names; I will try to update the list as I remember them.


But seriously: thank you, from the bottom of my heart. I loved hearing your stories, your complaints, your arguments about how the world should improve. Your DNA is in this book; I hope it does you justice.


~charity

💜💙💚💛🧡❤️💖


[1] It’s ironic (and makes me uncomfortably self-conscious), but some of the worst top-down decision-making processes I have ever seen have come from companies where CEO and CTO are both former engineers. The confidence they have in their own technical acumen may be not *wholly* unfounded, but it is often ten or more years out of date. We gotta update those priors, my friends. Stay humble.


[2] On the other hand, as my co-founder, Christine Yen, informed me last week: “Nobody reads books anymore.”
