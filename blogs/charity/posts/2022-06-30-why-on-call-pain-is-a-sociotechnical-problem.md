---
title: "Why On-Call Pain Is A Sociotechnical Problem"
date: 2022-06-30
url: https://charity.wtf/2022/06/30/why-on-call-pain-is-a-sociotechnical-problem/
word_count: 1951
---


[*Cross-posted from leaddev.com*](https://leaddev.com/call/why-call-pain-sociotechnical-problem)


Most people hate being on call, because most on-call rotations are terrible.


Pager bombs, flappy alerts, false positives going off night and day, sleepless nights… Who can blame them? Small wonder that so many people develop a Pavlovian response to the sound of their Pagerduty ringtone. Alert goes off; adrenaline soars.


Conventional wisdom tells us that being on call means you put your whole life on hold, then spend all week lurching between firefighting and false alarms as you get progressively more sleep-deprived. It sucks, but that’s just what you get when you own your code in production. Right?


Noooooo. Wrong wrongy wrong wrong. Being on call should not be a constant cycle of things breaking down and firefighting, or alerts going off at all hours. This is not ‘normal.’ These are telltale signs of a fragile system and lack of alert discipline.


If on-call pain is a constant source of pain at your organization, that is a PROBLEM. It’s a five-alarm fire. You should drop what you’re doing and *fix it* with urgency.


An eternally miserable on-call rotation is a violation of the pact we make to support these systems:

1. It is engineering’s job to own their code in production.
2. It is management’s job to make sure it doesn’t suck.


This is a two-way handshake. If management isn’t holding up their end, if they don’t allocate enough time to fix the underlying problems – if they run a feature factory that never stops to refactor or invest in reliability work – then on-call will never get better, and *you should leave*.


### On-call rotations are sociotechnical systems


On-call rotations are a classic example of a [sociotechnical problem](https://en.wikipedia.org/wiki/Sociotechnology#:~:text=Technology%20is%20the%20sum%20of,construction%20and%20insight%2C%20is%20sociotechnology.). A sociotechnical system consists of three elements: in this case that’s your production system, the people who operate it, and the tools they use to enact change on it.


You cannot solve sociotechnical problems with purely people solutions or with purely technical solutions. You need to use both.


The technical problems are usually easier to diagnose. You need to automate failovers, instrument your code, build and test repairing code, audit your indexes, etc. The social problems can be trickier to spot, but here’s a tip: they usually manifest as organizational problems.


Some engineers spend their entire career actively avoiding roles where they would have to be on call. Other engineers cling to the safety buffer of ops teams on call for their code, so that only manual escalations reach them.


### Responsibility for your code is increasingly non-optional


This is becoming a harder line to hold, as the consensus has shifted decisively towards engineers owning their own code in production. Our systems are becoming exponentially more complex, and feedback loops are tightening. The people best equipped to own software in production are the people who built it. And in order to own it effectively, they need to close the loop by receiving the signal when something breaks.


But the point is not to invite software engineers into the same circle of hell that ops engineers have traditionally inhabited. This isn’t an act of vengeance. The point is that tightening these feedback loops is how we make systems *better*. Being on call shouldn’t have to destroy your social life or your sleep schedule.


Yes, engineering owns their software. But ensuring that engineering’s time is respected and their rest time valued is on management. It’s management’s job to make sure time is allocated to fixing recurring or known issues – and that they don’t kick the proverbial can down the road to later turn into tech debt. If reliability or productivity is suffering, managers need to reassign engineering cycles away from feature work. Managers’ performance should be evaluated by the four DORA metrics, as well as a fifth; how often is their team alerted outside of working hours?


It’s reasonable to be woken up two to three times a year when on call. But more than that is not okay. It’s management’s responsibility to ensure enough resources are dedicated to maintaining system stability, and *they* should be held accountable – *not* the on-call engineers.


### Humans doing human things


We all have lives outside of work – families, doctor appointments, dentist visits, and so on. Instead of being surprised when things come up, we can predict the ways people’s lives will conflict with on-call duty and come up with ways to ease the burden.

- **Kids.** I would never ask a new parent to be on call. Being woken up by ONE instrument of chaos is all anyone should ever have to cope with at any given time.
- **Sleepy brain. **People are never going to be at their best when they are woken up in the middle of the night. We should make sure alert text, documentation, and steps are all clear, simple, and otherwise tuned for 2 a.m. brain fog.
- **Getting sleep.** Sometimes people struggle getting back to sleep, or they were up all night dealing with something. Establish that 1) no one is EVER to be on call two nights in a row after a bad night, and 2) they are entitled to sleep in, come in late, leave early – whatever works best to help them catch up on their sleep.
- **Anxiety.** I’ve managed people before who had high anxiety about being on call. They were perfectly willing, but it didn’t matter how quiet the pager was – their anxiety knowing it was on made it impossible to sleep. We tried it for a while, and it wasn’t getting better, so we ultimately found other ways for them to pull their weight.


If someone is absolutely unable to participate in on-call rotations, well, it happens. If it’s a temporary situation, you might want to let it go. But if it’s a permanent thing, like in the ‘anxiety’ example above, the team should address this by finding other ways for that person to do their share of maintenance work.


For example, they could be in charge of failed builds or maintain the dev environment. What matters is that 1) the team as a whole feels like it’s a fair distribution of labor, and 2) there are enough people left in the on-call rotation that no one is overly burdened.


### Technical stumbling blocks

- **Un-owned code**. Everything you support, and every alert that can fire, should have a team that owns it.
- Conversely, you may have **architectural issues** that make it impossible to isolate and alert only the owners. If you have ten different on-call rotations for various areas of the code base, but any time the database gets slow all ten of you get paged, this is a bad situation.
- **SLOs.** As you scale up, there will come a point where you can no longer alert on individual services or symptoms. They will simply drown you. At this point, you need to migrate your alerts over to Service Level Objectives. SLOs align your engineering pain directly with user pain.
- **Paging too early**. Ah, this always sounds like such a great idea. ‘Wouldn’t it be great if we could catch it and alert someone before the users are impacted?’ But it’s not. It’s a recipe for flappy alerts and aggravation. Alert when users are impacted, not before.
- **Two lanes**. You need two types of alerts: ‘WAKE ME UP’ and ‘Deal with this later.’ No more, no less. Keep the list of ‘wake me up’ alerts as short, crisp, and carefully curated. Put everything that needs to be dealt with ‘soon’ in the second lane, and have your on-call engineer sweep through it at the start of the day and the end of the day. *If it doesn’t need to be acted upon in the next day, it probably shouldn’t be an alert.*


### On-call problems are often organizational problems


Sometimes people don’t want to be on call, and it’s not due to life events. This is a bit trickier to address because they are actually the result of organizational problems that present themselves as on-call problems. For example:

- **Tribal knowledge, or the ‘[bus factor](https://en.wikipedia.org/wiki/Bus_factor).’ **You’re the debugger of last resort because you’ve been responsible for a mission-critical component of the system from the very beginning. The team tried training new people, but you still get called every time something goes wrong, and it’s not clear if the issue would be fixed if you weren’t available (or how long it would take them if they did).
- **Individual ownership vs. team ownership**. Software is owned by teams, not by individuals. In an ideal world, this means everyone on the team is capable of debugging and maintaining all the systems they collectively own. In the real world, this means everything is at least understood by more than one engineer.
- **Too little – or too much – coverage. **If you have three to four people on call, that’s too much of your life spent lugging around a laptop. Tossing all 20-30 engineers into a single rotation is also the wrong way to go; engineers won’t be on call often enough to stay familiar with the systems. The ideal on-call rotation has seven to eight people; five people is a bare minimum. With eight people, you are on call for a highly sustainable one week out of every two months.
- **Lower the barriers to asking for help,** swapping times, covering for each other, etc. When someone asks for help with their on-call shift, thank them for asking. If the on-call shift isn’t that arduous, it’s really no big deal to back someone up for the duration of a movie.
- **Appointing primary/secondary on-call engineers **can be really helpful here. Only the primary needs to get alerted and lug their laptop around, but they have a designated point person to tag if they need to run to the grocery store, drive through the boonies, or otherwise go offline for a while.
- **Put managers on call. **I’m not generally a fan of putting managers in the rotation, but they really are the ideal backup situation. *Especially* when it comes to picking up the pager the day after someone has had a rough night. This serves multiple purposes: it helps keep the manager fresh, it exposes them to the reality of what on-call is currently like, and their time doesn’t have to be swapped for someone else’s.


The next time someone doesn’t want to be on call, it may be time to take a closer look at your organization as a whole to see whether the problem really is resource allocation, risk mitigation, or something else.


### Making on-call costs tangible


On the topic of paying people more to be on call: there are loads of opinions here – it’s a very fraught topic. I generally come down on the side of ‘no, it’s part of the job,’ just like it is [for doctors](https://work.chron.com/doctors-paid-overtime-4382.html). With one big exception.


If you’re having a hard time getting upper management to understand the value of spending engineering cycles on the infrastructure and reliability work that needs to be done, instead of just cranking features… by all means, pay people for being on call.


Pay them for every event they have to respond to.


Pay them well.


Pay them so goddamn well the finance team starts squawking about the need to pay down that reliability debt.


If that’s the only way you can make it real for them, well, use the tools you’ve got. Engineers should never have to quietly suffer the pain of flaky software and unhappy users alone. Give management pain too until they take their jobs seriously enough to see that reliability issues get fixed.
