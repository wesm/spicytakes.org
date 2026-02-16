---
title: "Questionable Advice: “How can I drive change and influence teams…without power?”"
date: 2023-06-05
url: https://charity.wtf/2023/06/05/drive-change-and-influence-teams-without-power/
word_count: 2285
---


Last month I got to attend GOTO Chicago and give a talk about continuous deployment and high-performing teams. Honestly I did a terrible job, and I’m not being modest. I had just rolled off a delayed redeye flight; I realized partway through that I had the *wrong slides loaded*, and my laptop screen was flashing throughout the talk, which was *horribly* distracting and means I couldn’t read the speaker notes or see which slide was next. 😵 Argh!


Anyway, shit happens. BUT! I got to meet some longstanding online friends and acquaintances (hi JJ, Avdi, Matt!) and got to eat some of Hillel Wayne’s homemade chocolates, and the Q&A session afterwards was actually super fun.


My talk was about what high performing teams look like and why it’s so important to be on one (spoiler: because this is the #1 way to become a radically better engineer!!). Most of the Q&A topics therefore came down to some version of “okay, so how can I help my team get there?” These are GREAT questions, so I thought I’d capture a few of them for posterity.


But first… just a reminder that the actual best way to persuade people to listen to you is to **make good decisions** and **display good judgment**. Each of us has an implicit reputation score, which formal power can only overcome to an extent. Even the most junior engineer can work up a respectable reputation over time, and even principal engineers can fritter theirs away by shooting off at the mouth. 🥰


## “how can I drive change when I have no power or influence?”


This first question came from someone who had just landed their first real software engineering job (congrats!!!):


> “This is my first real job as a software engineer. One other junior person and myself just formed a new team with one super-senior guy who has been there forever. He built the system from scratch and knows everything about it. We keep trying to suggest ideas like the things you talked about in your talk, but he always shoots us down. How can we convince him to give it a shot?”


Well, you probably can’t. ☺️ Which isn’t the end of the world.


If you’re just starting to write software every day, you are facing a healthy learning curve for the next 3-5 years. Your one and only job is to learn and practice as much you possibly can. Pour your heart and soul into basic skills acquisition, because there really are no shortcuts. (Please don’t get hooked on chatGPT!!)


I know that I came down hard in my talk on the idea that **great engineers are made by great teams**, and that the best thing most people can do for their career is to join a high-performing, fast-moving team. There will come a time where this is true for you too, but by then you will have skills and experience, and it will be much easier for you to find a new job, one with a better culture of learning.


It is *hard* to land your first job as a software engineer. Few can afford to be picky. But as long as you are a) writing code every day, b) debugging code every day, and c) getting good feedback via code reviews, this job will get you where you need to go. When you’re fluent and starting to mentor others, or getting into higher level architecture work, or when you’re starting to get bored … then it’s time to start looking for roles with better teachers and a more collaborative team, so your growth doesn’t stall. (Please don’t fall into [the Trap of the Premature Senior](https://charity.wtf/2020/11/01/questionable-advice-the-trap-of-the-premature-senior/).)


**This is an apprenticeship industry**. You’re like a med student right now, who is just starting to do rounds under the supervision of an attending physician (your super-senior engineer). You can kinda understand why he isn’t inclined to listen to your opinions on his choice of stethoscope or how he fills out a patient chart. A better teacher would take time to listen and explain, but you already know he isn’t one. 🤷


I only have one piece of advice. If there’s something you want to try, and it involves doing engineering work, consider tinkering around and building it after hours. It’s **real hard to say no **to someone who cares enough to invest their own time into something.


## “how can I drive change when I am a tech lead on a new team?”


> “I have the same question! — except I’m a tech lead, so in theory I DO have some power and influence. But I just joined a new team, and I’m wondering what the best way is to introduce changes or roll them out, given that there are soooo many changes I’d like to make.”


(I wrote a somewhat scattered post a few years ago on [engineers and influence](https://charity.wtf/2018/08/17/on-engineers-and-influence/), or influence without authority, which covers some related territory.)


As a tech lead who is new to a team, busting at the seams with changes I want to make, here’s where I’d start:

1. **Understand why things are the way they are** and get to know the personalities on your team a bit before you start pitching changes. (UNLESS they are coming to you with arms outstretched, pleading desperately for changes ~fast~ because everything is on fire and they know they need help. *This does happen*!)
2. **Spend some time working with the old systems,** even if you think you already understand. It’s not enough for *you* to know; you need to take the team on this journey with you. If you expect your changes to be at all controversial, you need to show that you respect their work and are giving it a chance.
3. **Change one thing at a time**, and go for the developer experience wins first. Address things that will visibly pay off for your team in terms of shipping faster, saving time, less frustration. You have no credibility in the beginning, so you want to start racking up wins before you take on the really hard stuff.
4. **Roll up your sleeves**. Nothing buys a leader more goodwill than being willing to do the scut work. Got a flaky test suite that everybody has been dreading trying to fix? I smell opportunity…
5. **Pitch it as an experiment**. If people aren’t sold on your idea for e.g. code review SLAs, ask if they’d be willing to try it out for three weeks just as an experiment.
6. **Strategically shop it around** to the rest of the team, if you sense there will be resistance…


At this point in my answer 👆 I outlined a technique for persuading a team and building support for a plan or an idea, especially when you already know it’s gonna be an uphill battle. [Hillel Wayne](http://twitter.com/hillelogram) said I should write it up in a blog post, so here it is! (I’ll do anything for free chocolate 😍)


## “How can I get people on board with my controversial plan?”


So you have a great idea, and you’re eager to get started. Awesome!!! You believe it’s going to make people’s lives better, even though you know you are going to have to fight tooth and nail to make it happen.


#### What NOT to do:


Walk into the team meeting and drop your bomb idea on everyone cold:


> “Hey, I think we should stop shipping product changes until we fix our build pipeline to the point where we can auto-deploy each merge set to production, one at a time, in under an hour.” ~ (for example)


…. then spend the rest of the hour grappling with everybody’s thoughts, feelings, and intense emotional reactions, before getting discouraged and slinking away, vowing to *never have another idea, *ever again.


#### What to do instead:


Suss out your audience. Who will be there? How are they likely to react? Are any of them likely to feel especially invested in the existing solution, maybe because they built it? Are any of them known for their strong opinions or being combative?


Great!!! Your first move is to **have a conversation with each of them**. Approach them in the spirit of curiosity, and ask what they think of your idea. Talking with them will also help you hash out the details and figure out if it is *actually* a good idea or not.


Your goal is to make the rounds, ask for advice, identify any allies, and talk your idea through with anybody who is likely to oppose you…*before* the meeting where you intend to unveil your plan. So that when that happens, you have:

1. given people the chance to process their reactions and ask questions in private
2. ensured that key people will not feel surprised, threatened, or out of the loop
3. already heard and discussed any objections
4. ideally, you have earned their support!


Even if you didn’t manage to convince every person, this was still a valuable exercise. By approaching people in advance, you are signaling that you respect them and **their voice matters**. You are always going to get people’s absolute worst reactions when you spring something on them in a group setting; any anxiety or dismay will be amplified tenfold. By letting them reflect and ask questions in private, you’re giving time for their better selves to emerge.


#### What to do instead…if you’re a manager:


As an engineer or a tech lead, you sometimes end up out front and visible as the owner of a change you are trying to drive. This is normal. But as a manager, there are far more times when you need to influence the group but *not* be the leader of the change, or when you need to be wary of sounding like you are telling people what to do. These are just a few of the many reasons it can be highly effective to have **other people arguing on your behalf**.


In the ideal scenario, particularly on technical topics, *you* don’t have to push for anything. All you do is pose the question, then sit back and listen as vigorous debate ensues, with key stakeholders and influential engineers arguing for your intended outcome. That’s a good sign that not only are they convinced, they feel ownership over the decision and its execution. This is the goal! 🌈


It’s not just about persuading people to agree with you, either. Instead of having a shitty dynamic where engineers are attached to the old way of doing things and you are “dragging them” into the newer ways against their will, you are inviting them to partner with you. You are offering them the opportunity to **lead the team** into the brave new world, by getting on board early.


(It probably goes without saying, but always start with the smallest relevant group of stakeholders, and not, say, all of engineering, or a group that has no ownership over the given area. 🙃 And … even this strategy will stop working rather quickly, if your controversial ideas all turn out to be disastrous. 😉)


## “How do I know where to even start?!? 😱”


Before I wrap up, I want to circle back to the question from the tech lead about how to drive change on a team when you do have some influence or power. He went on to say (or maybe this was from a third questioner?*):


> “There is SO MUCH I’d like to do or change with our culture and our tech stack. Where can I even start??”


Yeah, it can be pretty overwhelming. And there are no universal answers… as you know perfectly well, the answer is always “it depends.” ☺️ But in most cases you can reduce the solution space substantially to one of the two following starting points.


#### 1. Can you understand what’s going on in your systems? If not, start with observability.


It doesn’t have to be elegant or beautiful; grepping through shitty text logs is fine, if it does the trick. But do any of the following make you shudder in recognition?:

- If I get paged, I might lose the rest of the afternoon trying to figure out what happened
- Our biggest problem is performance and we don’t know where the time is going
- We have a lot of flaky, flappy alerts, and unexplained outages that simply resolve themselves without our ever truly understanding what happened.


If you can’t understand what’s going on in your system, you have to start with instrumentation and observability. It’s just too deadly, and too risky, not to. You’re going to waste a ton of time stabbing around in the dark trying to do anything else without visibility. Put your glasses on before you start driving down the freeway, please.


#### 2. Can you build, test and deploy software in under an hour? If not, start with your deploy pipeline.


Specifically, the interval of time between when the code is written and when it’s being used in production. Make it shorter, less flaky, more reliable, more automated. This is the feedback loop at the heart of software engineering, which means that it’s upstream from a whole pile of pathologies and bullshit that creep in as a consequence of long, painful, batched-up deploys.


Here’s a talk I’ve given a few times on why this matters so much:


You pretty much can’t fail with one of those two; your lives will materially improve as you make progress. And the iterative process of doing them will uncover a great deal of shit you should probably know about.


Cheers! 🥂


charity.


** My apologies if I remembered anyone’s question inaccurately!*
