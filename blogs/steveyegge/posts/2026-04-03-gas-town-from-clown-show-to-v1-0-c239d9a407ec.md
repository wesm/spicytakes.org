---
title: "Gas Town: from Clown Show to v1.0"
date: 2026-04-03
url: https://steve-yegge.medium.com/gas-town-from-clown-show-to-v1-0-c239d9a407ec?source=rss-c1ec701babb7------2
source: medium
word_count: 3135
---


TL;DR: Gas Town and Beads have both released version 1.0.0 today. Enjoy!


![](https://cdn-images-1.medium.com/max/1024/1*lahvtXYL-5ebP3gOf8ovpA.jpeg)

*Gas Town and Beads hit v1.0.0*


It has been a wild 3-month ride since I [launched](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) Gas Town.


First there was the part where I was like nooo don’t use it, and everyone was like, hold my beer. I am so glad some of you ignored me so hard. It’s just what I’d hoped for. You early adopters helped pave the way for everyone else.


And we went through some chaotic times early on. There were the serial killer sprees, viciously taking out random workers mid-job. *(It’s always the Deacon, the modern-day Butler in the Gas Town murder mysteries.)* There was the 22-nose Clown Show, where the Mayor scored a new clown nose every time it had massive data loss, which went on for weeks. And more. We’ve had our share of trying times, honking alert noses, piles of worker corpses. All long past us now.


![](https://cdn-images-1.medium.com/max/1024/1*HqGMDjS1AjIPckGknFXFew.jpeg)

*The Gas Town Serial Murders and Clown Show*


Despite the early bumps, we’ve continued to enjoy absolutely massive community engagement. Even though Gas Town “only” has 13k stars (at 3 months!), it has hundreds of enthusiastic committers, and bugs get noticed and fixed fast.


It’s safe to say that Gas Town has largely been in maintenance mode since the Dolt migration finished up, and that was well over a month ago. I’ve continued to allow a few nice features here and there, but for the most part we are now directing people’s creative efforts to the successor, Gas City, which is in alpha testing and on track for a fast GA.


And maintenance mode is a good thing! It means it’s not thrashing. Gas Town “just works.” It does its job, it has tons of integration points, and it has been stable for many weeks. People are using it to build real stuff.


As one example, Gene Kim and I were chatting with a very cool midsize company, who are making a company-wide move to adopt agentic AI. A person in their Communications department, who is a Comms major four years out of school, shared with us (to our lasting astonishment) that she has been using Gas Town since “a few weeks after it came out.” She decided to build replacement for a niche but pricey SaaS product their company has been paying for. She’s working with another non-technologist on it, and it’s so good the company is getting ready to switch over to it. Amazing!


![](https://cdn-images-1.medium.com/max/1024/1*OkRXf1gc3ao2PpJ18H2yMg.jpeg)

*Anyone can build software with Gas Town — and people are!*


Non-technologists using Gas town to build software! It sounds crazy but I’m seeing it all over. People in academia, non-technical knowledge workers, even just people curious about vibe coding; all are figuring it out.


So as far as I’m concerned, Gas Town is ready. That’s why I feel it merits a 1.0.0 release.


To get started, you just have your coding agent install it, and talk to the Mayor. More on that below. The Mayor is cool. You’ll like the Mayor.


Importantly, we are also rolling Beads to version 1.0.0 today. Beads is the secret sauce that makes Gas Town and Gas City both possible and best-of-class. I’ll spend some time talking about Beads before we get back to Gas Town.


**Beads: The Memory Revolution**


Last year I noticed that agents were struggling with basic stuff: working memory, and simple task tracking. They had zero attention span and developed progressive dementia. That led me to create [Beads](https://github.com/gastownhall/beads), which is a drop-in, generic, unopinionated memory system and knowledge graph for coding agents. Beads gives your coding agent sudden clarity and long-horizon planning capability.


Beads [started life](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) back in October as a lightweight issue tracker with version control. But it quickly became clear that it was like Adderall for your agent. It is an instant cognitive upgrade for any coding agent, even replacing their built-in memory and task tracking systems with a system that’s more powerful, more portable, and every bit as transparent and easy to use. You don’t need to know Beads in order to use it; your agent handles it all.


Over time, it became clear that Beads was a sort of universal discovery, a gift that keeps giving. It’s way more than an issue tracker, and is evolving gradually into something more like a universal ledger for all knowledge work. One that agents happen to really, really like.


It was a high-level insight from Chris Sells, an old friend of mine and (with Julian Knutsen) the co-creator of Gas City, that helped crystallize for me why Beads seems to solve so many problems at once: Beads is the Why.


**Beads is the Missing Why**


In Beads, every work item becomes a bead. A bead is just a structure with some fields: a lightweight bug/issue report, with a title, description, status, etc. Beads are stored and versioned in Git, linked together as a multi-graph, and they are queryable with SQL like a database. Best of all worlds.


Versioning your Beads is critical: you get a complete historical log of every change to any Bead, trivial to query. So in multi-agent environments, everyone using Beads can tell what everyone else using Beads did, and why.


Your project’s Git commit history has always been your permanent ledger that contains the What, Where, Who, and How of what happened to your code. But as Chris Sells astutely observed a few months back, Beads is the Why — the missing piece in your commit history. It completes the data-warehousing picture of your project needed (by agents) for forensics, recovery, onboarding, design, and more. Having this information handy is invaluable for agents when they are trying to reconstruct how we got where we are.


![](https://cdn-images-1.medium.com/max/1024/1*pjAfmZ3VF22ZcY5Him2PvQ.jpeg)

*Beads: The Missing Why for your projects*


Individual beads capture and record all your work on the Git ledger, through its entire lifecycle, from planning/design, through implementation, and then they form the audit trail after the work is closed. This isn’t limited to development work, either; you can use it anything. Someone once told me they use Beads for their grocery shopping (which they do with an agent.)


A key insight was that you can use Beads for defining and tracking orchestration work, which is how Gas Town and Gas City operate. Beads string together into “molecules” that have deterministic steps to follow, for patrols, releases, etc. Every step an agent takes in a Beads-based workflow is recorded on a ledger. This acts like a save-game that you can roll back to, or at least use to see how you got where you are.


**Beads is for Literally Everyone, and Everything**


Beads is completely unaware of Gas Town (though Gas Town uses Beads as a dependency.) You can use Beads by itself and get a vastly improved agentic experience, no matter which coding agent you’re using. Unlike Gas Town, which only works with a handful of agents today, Beads works with anything and everything, as long as it’s roughly as smart as Claude Sonnet 3.5 was.


People who switch to Beads soon realize they can build their own workflows and orchestration using nothing but Beads. It’s an incredibly powerful and versatile data plane. Once you start storing stuff in Beads, you kind of want everything there. It doesn’t *solve* the memory problem by itself, but it certainly gives you a solid foundation for solving it your own way.


Beads crossed 20k stars on GitHub this week, a bit over 5 months since launch. I have not been much of a GitHub user for most of my career, so I didn’t appreciate how unusual 20k stars is until this week. Chris, Julian and I all guessed that roughly 10k-20k repos would be that popular. But we were way off. You can browse them all with a [query](https://github.com/search?q=stars%3A%3E20000&type=Repositories&ref=advsearch&l=&l=). There are currently 1988 with more than 20k stars.


So Beads is already in roughly the top 2000 GitHub repos, out of some 300 million. That’s pretty rarified air. But it makes sense. I mean, it just works. It’s soooo easy. You start using Beads, everything becomes a bead, and life with agents just starts getting easier.


![](https://cdn-images-1.medium.com/max/1024/1*zK0kOxfc7Rc26_JwvVdeEQ.jpeg)

*Beads enters the stratosphere with 20k stars*


**Beads: Ready for v1**


I held out on a v1.0.0 release for Beads for months because I had a feeling it would become clear when it’s ready for prime time. With the recent completion of [Beads with Embedded Dolt](https://www.linkedin.com/posts/dolthubinc_steve-yegges-beads-a-memory-system-for-activity-7445535824894640129-Qxod?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAt1ukBgAKCy5S6X8q0kzSeibgywocofK4) by the amazing Dolt team, Beads is finally back to its Day Zero experience. We have managed to land on an architecture and implementation that serve all the key audiences:

- Solo, single-player users with just a coding agent or a chat session. Great experience out of the box, simple setup, syncs to GitHub automatically.
- Multi-agent power users who might be working on multiple projects or workflows.
- Gas Town users doing high-velocity orchestration on heavy-duty project work.
- Gas City users doing multiple projects and enterprise-level orchestration setups.
- Wasteland and other federation users, who want the power of Dolt, Git, and Beads as a work federation protocol.
- Anyone building their own orchestrator.


Many of these audiences were poorly served by the original, janky Beads architecture of SQLite + JSONL + awkward syncing and tons of merge conflicts. When it did work, it was often last-write wins semantics with SQLite just taking “whatever” happened to win. Not exactly enterprise-grade building material.


All that jank is gone. Torn out of the code base entirely. Beads is now backed with the power of [Dolt](https://github.com/dolthub/dolt), which itself sports an impressive 22k GH stars. The inherent fragility of the v0.x Beads architecture, with its bidirectional sync, 3-way merge, two sources of truth, race conditions, and tombstone hell — that’s all gone now. Dolt was designed to handle all this stuff gracefully. We got incredibly lucky that it exists at all.


Now that Beads is stable on Dolt, with both embedded and server-mode fully supported, v1.0.0 is the right call. I’ve moved the Beads repo into the [gastownhall](https://github.com/gastownhall/) org (soon to be gascityhall), where we will continue to support Beads as a first-class standalone product for non-GT/GC users.


![](https://cdn-images-1.medium.com/max/1024/1*ImuIDsWhZsp89beFpbyAcQ.jpeg)

*Dolt: Migration complete!*


**Gas Town: It’s That Dang Mayor**


I want to chat a little more about what we’ve learned about Gas Town before we wrap.


One of the reasons that people like Gas Town is that they don’t have to read as much, or even pay attention as closely. It’s more like DM’ing with a friend.


Claude Code makes you read. A lot. It doesn’t matter if you don’t like reading, or if this isn’t your native tongue, or if you’re busy, or tired. With coding agents, you’re gonna do some reading. Read read read read. It’s like a stevey post gone wild, running rampage, in every session. But make sure you don’t miss anything important!


I read just fine, and even I didn’t like doing all that reading. Most of it clearly could have been read by a model, saving me the trouble. I wanted something else, some other interface, but wasn’t sure what. I just didn’t want to have to read so much unnecessary cruft.


I spent a bunch of time building orchestrators last year, trying to get Claude to run Claude. At first, I was trying to achieve the elusive “visibility without reading” by chasing classic Observability. I was initially thinking that I wanted dashboards or activity feeds or some other visualization of my town’s workers. And some people still do like those, and they can be handy.


But after a while I realized I just wanted someone to talk to, while the system was working. And perhaps, as occasion might demand, someone to yell at.


The Mayor abstraction turned out to be perfect. Mayors are *there* to get yelled at. A Mayor isn’t so distant, like some higher-level governor or executive, to whom yelling seems like it will go unheard. A city mayor is ostensibly someone who has your local interests at heart, so the mayor is who you yell at first. It’s a social custom going back centuries. As one famous and rather wise U.S. mayor put it a week ago, if your constituents aren’t yelling at you, it’s because they aren’t around at all, and you don’t want that.


![](https://cdn-images-1.medium.com/max/1024/1*THeSv1unbpZv-rK9pR_mZA.jpeg)

*Programming in 2026 will become talking to a face*


With the Gas Town Mayor, you feel like you’re operating at a special level, a VIP, above all the workers. You are talking to someone important: the mayor of a factory the size of a town. You have access to someone with resources, someone who gets you, someone who appreciates how busy you are.


Working with regular coding agents just doesn’t give you that special feeling. I’m not making this up; this is a pretty consistent report I get from the field, from people around the world, particularly nontechnical people. I truly think it comes down to the Mayor giving you less stuff to read.


Claude Code only has one way to tell you what’s going on, which is to tell you what’s going on. It babbles while it works. “Now I will run this awk script s@(*fj$&h(*!&*.* Now I will print 8 pages of recaps. Now I’m deleting your database. Now I’m printing more recaps, and running another script here is the code #$AWESR@#$.”


Claude Code is a wall of scrolling text. The harder it works, the scrollier it gets. Now imagine having 10 standard coding agents running. Any agent, could be Codex, whatever. Ten of them puking out text. And you have to sort through all their output to find the nuggets of actually interesting stuff you need to know about, like the part where they’re deleting the database.


This is why people love Gas Town. The Mayor reads all that crap that the workers are printing. The Mayor knows your context, your hopes and dreams. The Mayor has an army of polecats it can whip up when it needs to. The Mayor has all these cool-sounding resources, like the Crew and Convoys and Dog patrols, that it can bring to bear on your problem. Just say the word, the Mayor’s on it for you.


Claude Code and some other agents are trying to turn themselves into dark factories, by running subagents, and providing their own task management, memory systems, etc. But so far, they’re all trying to do it with a product lens, no platform to speak of — a monolith. I’ve read some interesting [blog posts](https://gist.github.com/chitchcock/1281611) about that approach, but safe to say I’m not a fan.


Gas Town at least lets you talk to your agents as first class citizens, with externally visible identities; Gas City takes it further and decomposes the entire stack into a modular platform architecture.


In short, what’s behind the Mayor also matters, and as soon as people start getting curious, today’s coding agents immediately disappoint. And believe you me, people are getting curious. And they’re finding their way to Gas Town.


![](https://cdn-images-1.medium.com/max/1024/1*W9ieOK7cL5EH4nbGlL6P3A.jpeg)

*The Mayor does your reading for you, so you can supervise*


Ultimately the Mayor is doing way more than just saving you a bunch of reading. It is your personal concierge. If Claude Code is an Executive Assistant, then the Gas Town Mayor is more like your Chief of Staff, who manages a full team of capable EAs, all working for you behind the scenes.


I’ve been saying since last year that by the end of 2026, people will be mostly programming by talking to a face. There’s absolutely NO reason to type with the Mayor. You should be able to chat with them like a person. You’ll have a cartoon fox there onscreen, in costume, building and managing your production software, and showing you pretty status updates whenever you ask for one. This is the end state for IDEs.


**On to Gas City**


As I mentioned in my long-overdue [Vibe Maintainer](https://steve-yegge.medium.com/vibe-maintainer-a2273a841040) post, we’re going to start gently nudging everyone towards [Gas City](https://github.com/gastownhall/gascity). You literally just install it, import your Gas Town configuration, and then you’re using that instead of Gas Town. It’s functionally identical, when used as a dev IDE.


Except with Gas City, you can now build your own orchestrators using all the Gas Town primitives: identity, roles, messaging, mail, sessions, cost tracking, multi-model dispatch, skills, prompting and priming, hooks, GUPP, NDI, formulas, molecules, beads, epics, convoys, orders, patrols, plugins, tmux, seances, and more more more. It’s all there. You can mix and match to create arbitrarily simple or fancy orchestrators, with all their work logged to a beautiful set of git ledgers.


There will be nothing like it. You *are* going to want to use Gas City. We will have some imitators, but I’m not worried. Ask your agent to dig into Dolt federation and have a look at our Wasteland, and you’ll quickly see why this is a superior way to do work.


I can’t begin to express my excitement about Gas City. It is all MIT-licensed, supported by a growing team of enthusiasts, and it is already starting to have legit hosting options for people who want to build orchestration in the cloud. I will have a detailed post about it when we get closer to GA, when it’s late beta and ready for wider adoption.


But no need to wait. At a high level, Gas City is the answer to all your problems. Ha! At least, for certain classes of problem, such as, “How can I bring AI into my company and pass an audit trail,” “How can I rid myself of gougy niche SaaS by in-sourcing it all to AI,” and similar. I know you’re all thinking about it!


Stay tuned. I have another blog post hot on this one’s heels. I’m giving some talks next week, one in NYC and one in San Jose, and I figured, why not just spill all my talk secrets in a public blog so that I have nothing interesting or new to add during my talks!


Anyway, that’s a wrap! Congrats to the Beads community for riding the wave to the 1.0 release and 20k stars, and for finally getting a solid embedded-Dolt experience. Thanks to the Dolt team and Dustin Brown for that! And congrats to everyone who has used Gas Town to do something cool. I couldn’t be happier!


Finally, a huge thank you to the core team who have all worked incredibly hard to bring you Gas Town, Gas City, the Wasteland, and much more to come. From left to right, skipping me the panda, there’s Matt Beane, Chris Sells, Julian Knutsen, Tim Sehn, and Brendan Hopper. We’ve got so much more in store for this ecosystem. Come join our Discord at [gastownhall.ai!](https://gastownhall.ai/)


![](https://cdn-images-1.medium.com/max/1024/1*GeVxwM147GYS0mngSGP6tg.jpeg)

*Gas Town Ecosystem Generals: Matt, Chris, Steve, Julian, Tim, Brendan*


![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=c239d9a407ec)
