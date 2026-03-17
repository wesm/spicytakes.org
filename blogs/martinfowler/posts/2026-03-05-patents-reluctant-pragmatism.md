---
title: "Ideological Resistance to Patents, Followed by Reluctant Pragmatism"
description: "This article reflects on an ideological discomfort with software patents, a direct experience of patent         aggression in the software industry, and the practical constraints faced by startups. It"
date: 2026-03-05T00:00:00
tags: ["internet culture", "legal"]
url: https://martinfowler.com/articles/patents-reluctant-pragmatism.html
slug: patents-reluctant-pragmatism
word_count: 1145
---


I have always been uncomfortable with patents.


Ideologically, I subscribe to Richard Stallman's school of thought that ideas should move freely,
            innovation should compound in the open, and progress should not be fenced off by legal constructs. Over
            time, this led me to develop a strong discomfort with patents, and I genuinely believed they cause more harm
            than good.


Software patents are mostly used as roadblocks to innovation


That belief was no longer theoretical when I was confronted with a very real situation where patents were
            weaponized. I still remember working at [Hike Messenger](https://en.wikipedia.org/wiki/Hike_Messenger) in 2016 and being pulled
            into the boardroom for an emergency meeting after we received a legal notice from a large messaging
            platform alleging IP violation.


Patents such as [US10051104B2](https://patents.google.com/patent/US10051104B2) and its published cousin [US20130305164A1
        ](https://patents.google.com/patent/US20130305164A1) describe delivery and read receipts for messaging apps. These are seemingly simple, intuitive UX
            elements, such as message delivery and read indicators.


What surprised me was not the existence of such patents, but the realization that features users
            instinctively expect in an app were being held hostage by IP claims. The industry had reached a point
            where even basic UX primitives could be turned into legal leverage, shaping who could innovate freely
            and who could not.


Martin Fowler clearly articulated these concerns in post on [software
            patents](https://martinfowler.com/bliki/SoftwarePatent.html). He explains why software patents are fundamentally broken: too few of them have any true
            novelty, too many have vague and overly broad claims. Consequently, they have shifted from incentivizing
            invention to reinforcing existing power structures.


Based on my experience, I agree with his diagnosis.


## Our reluctant journey to defensive patents


What follows is not a rebuttal of that position, but an account of what it means to innovate inside that
                reality. When patents become weapons rather than signals of innovation, the question is not why the
                system is broken, but what startups are supposed to do inside it.


While building [Specmatic](https://specmatic.io), whose core is open sourced, we had to ensure we
                could protect our innovation. Reluctantly, we decided to file a couple of patents: not to monetize it,
                not to block others, but purely as defense, so that we would not be locked out of our own work again.


Filing a Patent Is an Unexpected Act of Clarity


Patent filing is not a feel-good exercise. You do not get to hide behind vision decks, buzzwords, piles
                of code, or vague claims of innovation. It forces uncomfortable questions:

- What is actually unique here?
- What problem are we solving that others have not?
- Where does prior art end and our idea begin?
- If everything else is stripped away, what is the irreducible core of our innovation?


Answering these took real effort. It forced discipline to precisely articulate ideas that previously
                existed only as architecture baked into the code of our product. In many ways, it felt less like legal
                paperwork and more like the most rigorous design review we had ever done, one conducted against the
                backdrop of the entire industry's history.


Prior Art Searches Are Humbling and Surprisingly Energizing


The prior art search was equally enlightening. Seeing how others had tackled similar problems, sometimes
                decades earlier, was humbling. It showed us where we were building on existing work, where the industry
                had stalled, and where there were genuinely unexplored areas ripe for innovation.


In several cases, it sparked new ideas. In others, it helped us simplify what we were building.
                Ironically, the process made our thinking more open, not more defensive.


I still believe the patent system is deeply flawed. That has not changed.


I Still Don't Like Patents, but I Understand Their Defensive Necessity


What has changed is my understanding of power asymmetry. Large players can treat patents as a tool to
                extract royalties and fend off competition, while startups often have no choice but to patent execution
                paths to protect their work from appropriation or exclusion. When legal leverage outweighs originality
                or execution, ideology alone does not protect you. Used
                thoughtfully, patents can act as a shield, not a weapon.


This insight is highly relevant for startups building foundational infrastructure in spaces dominated by
                large companies with better lawyers than engineers.


In many ways, the fact that startups like us feel compelled to file defensive patents proves Martin's
                argument. When a system is designed to reward legal capacity instead of novelty or technical merit, even
                those who believe deeply in openness are forced to engage with it, not out of conviction, but out of
                necessity.


## The imperfect alternatives to patents


Before concluding that defensive patents were the only option, it is worth examining alternatives that
                aim to preserve openness without resorting to patenting.


Joining patent non-aggression communities like [Open Invention Network (OIN)](https://www.openinventionnetwork.com/) help
                encode intent and reduce harm. They help reduce patent risk within defined open-source ecosystems,
                particularly around the Linux System.


They are valuable, but they do not eliminate the underlying asymmetry. They do not prevent third parties
                from patenting your ideas, nor do they guarantee protection if those patents are asserted outside the
                scope of the Linux System, where Specmatic falls outside core coverage. Builders still have to navigate
                a system where legal protection and legal capacity are unevenly distributed.


Open-source licenses are about copyright, they do not protect from patent attacks


No open-source license directly prevents patenting. Some licenses, such as Apache 2.0 and GPLv3,
                discourage patent aggression through explicit clauses, but other like MIT License, are intentionally
                silent on patents.


It is also important to understand that patent law and copyright law are separate systems:
                Open-source licenses operate under *copyright*.

                Copyright does not protect the underlying idea, concept, or method. Another developer can
                independently write different code with the same functionality without infringing copyright.

                Patents, in contrast, operate under *patent law*.

                Patent law protects methods, systems, and technical inventions. Patents allow the holder to exclude
                others from practicing that invention, regardless of the specific code they use.


Note: Specmatic's core is released under the MIT License. That choice was intentional. We
                wanted the core to be genuinely open, easy to adopt, and usable without friction, while still allowing
                us to build commercial products on top. MIT optimizes for reach and composability, not control.


The trade-off is that MIT provides no structural protection against patent aggression. There is no patent
                retaliation clause and no implicit non-aggression pact. Openness maximizes adoption, but it does not
                neutralize power. Defensive measures therefore sit alongside permissive licensing, not in opposition to
                it.


Hold on to your ideals, but pair them with clear-eyed realism. If you are building something genuinely
                novel, particularly infrastructure, tooling, or platforms, leaving your innovation unprotected can make
                you vulnerable, sometimes even to the point of being excluded from the very work you created.


The system is imperfect. Holding on to principles is important, but I have learned that principles alone
                do not shield us from reality.


---
