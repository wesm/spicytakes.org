---
title: "Six New Tips for Better Coding With Agents"
date: 2025-12-07
url: https://steve-yegge.medium.com/six-new-tips-for-better-coding-with-agents-d4e9c86e42a9?source=rss-c1ec701babb7------2
source: medium
word_count: 5666
---


I’m hanging out in Sydney with my esteemed co-author and co-conspirator Gene Kim today; we flew in to conduct Vibe Coding workshops and talks this week to the Commonwealth Bank of Australia, some of their partner companies, and the general engineering public. Very cool of CBA to sponsor this training, and Gene and I are super excited for it.


We noticed that we’ve pushed into new territory since our [Vibe Coding](https://www.amazon.com/Vibe-Coding-Building-Production-Grade-Software/dp/1966280025) book was published. The book is all about how to work with coding agents, and all the advice and techniques in it are still incredibly relevant; I use it all daily. But there’s even more to learn, and we continue to uncover new tips and strategies.


I thought I’d share some of the new themes we’ve noticed, in no particular order, hot off the presses. Let’s see which ones resonate with you.


**1. Software is now throwaway — expect < 1 year shelf life**


This is probably the most obvious one. Anthropic has already begun embracing this idea internally, which is how I first heard about it, from friends there.


26 years ago Joel Spolsky wrote one of the most useful pieces of software advice anyone has ever given, in [Things You Should Never Do, Part 1](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/), where he says, in a nutshell, DON’T REWRITE YOUR SOFTWARE!


In this classic essay, well worth a read, Joel gives powerful examples of companies and projects that decided their code base was too old and crufty, so they chose to rewrite it all from scratch. And the results were, predictably, awful. Joel says:


> The idea that new code is better than old is patently absurd. Old code has been *used*. It has been *tested*. Lots of bugs have been found, and they’ve been *fixed*. There’s nothing wrong with it. It doesn’t acquire bugs just by sitting around on your hard drive. Au contraire, baby! Is software supposed to be like an old Dodge Dart, that rusts just sitting in the garage? Is software like a teddy bear that’s kind of gross if it’s not made out of *all new material*?


And he was right! Outstanding essay. But unfortunately, not so timeless as we thought. It proved to have a shelf life of only about a quarter century. We are entering a surprising new phase of software development, in which rewriting things is often easier (and smarter) than trying to fix them.


I first noticed this with unit tests. You’ll use agents to make a giant refactoring to your system, and then all the tests will be broken. The agents inevitably struggle to fix them. So one day I said, screw it, delete all the tests and make me new ones. And it got through that exercise SO much faster. The new tests were great, had great coverage, and importantly, the LLM was able to generate them very quickly, compared to trying to reason through the old system behavior vs the new expected behavior. With new tests, it can focus just on the new behavior, which is a much cleaner cognitive problem.


This generalizes beyond tests: generating almost any code is easier (for AIs) than rewriting it. Hence, recreating software stacks from scratch is starting to become the new normal. We’re seeing it more and more, e.g. companies with mainframes who are concluding that a small team of engineers and biz people could recreate the entire experience with the same API, but with modern architecture and maintainable code, in just a few months. And they’re doing it.


The upshot is that for all the code I write, I now expect to throw it away in about a year, to be replaced by something better. Maybe mine, maybe someone else’s. Doesn’t matter. It’s all just stepping-stones to higher velocity.


This spells trouble for third-party SaaS vendors. Companies are also discovering that they can build bespoke business-automation software so easily that they don’t need to re-up their vendor contracts. SaaS vendors are going to have to work harder to provide value that’s too expensive to recreate. It can be done — [Graphite](https://graphite.com/) is one example; they now have years of learnings into the nuances of AI code review. I don’t think you would necessarily want to retrace those years of steps yourself, on your company dime. Sourcegraph is another example; they have a code search engine with 10 years of enterprise bug fixes, and even with modern agents, you almost certainly wouldn’t want to try to clone that yourself.


But many SaaS vendors who’ve found niches building business automation software are going to be in real trouble. Because businesses are automating their own processes now, with vibe coding!


**2. Agent UX matters at least as much as Human UX**


One of the interesting themes I heard at the AI Engineering Conference in NYC a couple weeks ago was that although many people are building tools for AIs, they are finding it very hard to get the AIs to *use* those tools.


It’s tricky to get AI to use a tool it’s not trained on. They have certain ways of thinking and working, and they tend to reach for familiar tools (e.g. grep instead of a fancier search). I’ve talked with many people who wanted to build a tool for their agents to use, and they’d work with the frontier models to design the *perfect* agent-friendly interface — one the models swore up and down would get them to use it.


And then haha, no, the agents don’t use it. You prompt and prompt, they ignore and ignore. So what do you do? How do you get them to use your tools?


My [Beads](https://github.com/steveyegge/beads) issue tracker for agents has been an interesting case study here. It’s only maybe 2 months old and it already has 250+ forks and 5000+ stars. It’s a successful project. But I’ve never looked at the code. It’s fully vibe-coded by agents. Despite that, Beads managed to capture lightning in a bottle — it’s a tool that AIs use, and not only that, they *like* it. Agents use Beads eagerly and enthusiastically with very little prompting. They make smart decisions, such as filing Beads when they are low on context, instead of doing the work directly. Things you would normally have to prompt them to do, they just do!


I’m no magician. I’ve built plenty of tools that the AIs refused to use; I’ll talk about one of them below. And I’ve built plenty of prompts that the AIs choose to ignore or overlook. It’s not like capturing lightning in a bottle is super reproducible at this point. But I can share some of the things I did with Beads that I think helped.


First, I asked Claude to help me design a new lightweight issue tracker backed by git, with a few other constraints, and then Claude came up with about half of the rest of the design: the SQLite database caching layer, the discovered_by graph link that the models feel is *very* important for gathering context on issues, the hash IDs, deletion tombstoning, etc.


During the Beads design phase, I mostly argued with Claude, telling it I didn’t like certain choices it was making from a Human UX perspective. Eventually we negotiated our way to something we both liked, something that had good agent UX and also good human UX.


For the agent side, once we had the initial structure in place (the issue tracker itself), the primary UX issue became tooling ergonomics. My agents were trying to use Beads, but they kept giving it the wrong arguments. For example, they’d use — body instead of — description when filing an issue, which would fail. Why? Because they were trained on GH Issues, and GHI’s CLI tool uses — body for filing issues. Reaching for the familiar again!


So in that particular case, told it to add — body as an alias for — description, which it did, and that bit of Agent UX friction went away forever. I’ve done this many, many times in Beads. As the agent works, I watch how it’s using the tool, and whenever it encounters an error, I ask it, how did you want it to work there? How can we change it to make the behavior be more easily guessable?


Over the past few months we’ve made dozens of tweaks, adding flags and commands, and the agents now rarely have trouble using Beads fluently.


I can’t claim to have cracked the agent-UX problem, not by a long shot. I think the role of “Agent UX Designer” feels like it’s ready to emerge as a first-class career for humans. As just one example, I’m working on my *third* agent orchestrator this year. And even though the architecture is sound, I haven’t found the magic UX formula yet, to where any agent automatically just figures out what to do, and does the right thing most of the time. I’ll get there! In fact, as soon as I solve this problem with my orchestrator, I’m launching it. I’m aiming for Christmas Day. We’ll see.


Once you do find that secret incantation that makes your tool truly agent-friendly, you should get it out there as fast as you can, because it will grow like crazy.


And if you try to launch a tool that agents don’t *choose* to use of their own volition, with minimal prompting, then you need to go back to the drawing board and fix the agent UX.


The best way to do this is to leverage the Optionality from FAAFO, from our Vibe Coding book. Generate a whole bunch of interfaces, and then experiment with each one, to see which one the agents like best. It’s very much a trial-and-error search problem at this point, until either the agents get better at using new tools, or we get better at learning what they like.


**3. Spend 40% of your time on code health, or else you’ll wind up spending >60%.**


Gene was curious how I could be so confident in Beads if I’ve never looked at the code. My answer to him was one of the easiest I’ve ever given. If you are vibe coding, i.e., having the AI write all your code for you, then you need to spent at *least* 30–40% of your time, queries, and money on code health. That’s how you make sure your code is OK. You have the AI conduct regular code inspections. Tons of them.


It’s pretty easy in principle: Every now and then, you pause your regular work, and tell your agents: go find code smells of all shapes and sizes. Have them file Beads for anything that needs followup. Tell the agent to look for large files that need refactoring, areas with low test coverage, duplicated/redundant systems, legacy code, dead code, poorly-documented code, etc. etc. etc. I don’t have a good prompt for this step yet; would appreciate it if anyone has crafted one. But you can also just ask your agent to help craft it.


You’ll also want to ask your agent to do cleanups during the code-health passes. Have it look for files that are in the wrong place, or have misleading names, or need better homes. Have it clean up debug cruft, ancient plans, build artifacts, old docs, anything you don’t need. This is all part of the regular hygiene and maintenance of a vibe-coded code base.


It helps to be creative, and also to ask the agent to be creative, thinking outside the box. After the first round or two of regular code reviews, start having it look for over-engineered subsystems (YAGNI), opportunities where your code could have used a third-party library, and other broad, system-level concerns.


Basically the agent will *always* find problems, often shocking ones, e.g. where you discover you have two or even three completely redundant systems (databases, logging, telemetry, whatever) that need consolidating. And since agents tend to accrete code without automatic refactoring, your vibe-coded source files will tend to grow to thousands of lines, which makes them harder to agents (and humans) to reason about. So you should tell it regularly to break things up, and then run dedicated sessions to implement the refactoring!


During each code review, have your agent file Beads for everything it discovers. Then have it review the epics and issues (up to 5 times; see below) to ensure the implementation will go smoothly.


Then swarm to fix it all! Do all this at least weekly. For me, I’d estimate I spend about 25–30% of my time and money on code health, and I don’t think it’s enough. As long as I continue to find serious problems with reviews, I need to do more reviews. My current guidance is that you should expect nearly half of your work to be code-health related.


What happens if you don’t follow this rule? You gradually (but rapidly) accumulate invisible technical debt that weighs down your agents in various ways — too much code, conflicting code, obsolete docs, etc. Your agents will begin to work more slowly and you’ll see more bugs in their outputs.


Stay on top of code health, and you’ll keep your vibe-coded code base sprightly.


**4. You might be too early: Some projects are ahead of their time.**


AI cognition takes a hit every time it crosses a boundary in the code. Every RPC, IPC, FFI call, database call, client/server call, every eval, every single time the AI has to reason cognitively across a boundary or threshold… it gets a little dumber.


I noticed this when working on [Efrit](https://github.com/steveyegge/efrit), my native-elisp coding agent, which lives inside Emacs. Over the summer I was trying to get Claude and other models to build it for me, and they struggled. Hard. Efrit lives in Emacs, which is a separate process from your coding agent, so already there’s one boundary.


For that particular IPC boundary, there are multiple channels for the agent to talk to Efrit, all of them quite unsatisfying. There’s emacs — batch, which has limitations, and the emacs-server client/server mode, which is also limited for the kind of heavy reflective introspection the agent needs to do for this kind of code base.


So what did I do? I spent a week working with Claude to build a better agent-Emacs bridge. Claude built me the “Agent-Efrit bridge”, a simple and elegant system which uses a polling file channel as a message queue to and from Efrit. It’s beautiful. A tool made for agents, by agents! When it does work, it’s amazing.


Naturally, Claude never uses our fuckin’ bridge we built together. I’ve given up even asking. This is an example of a tool I tried to build, but the AI just refuses to use it.


With Efrit, after that initial bridge there are still other RPCs — the API call to the frontier model, the parsing of its response, and the eval of the elisp code to execute the response. All of these were piling up to make the models dumber. And ultimately, the August 2025 crop of frontier models couldn’t solve this problem. Or at any rate, the returns became so diminishing that I gave up.


So I paused the project! There was plenty of other work to do. A few months went by, a few model releases happened (notably Sonnet 4 and Sonnet 4.5). Efrit sat idle. And then about 2 weeks ago, someone asked to be an Efrit maintainer, since people wanted to use it. But wait, Efrit was still crap! So I thought, what the heck, let’s have Claude 4.5 peek at it.


Claude 4.5 took one look and said, “great idea, awful execution, but we can modernize this.” It produced an incredibly detailed plan to take Efrit to the next level, and I’ve spent the past 2 weeks letting it grind through this plan (serially, no swarming, since swarming on elisp sounds like a bad idea today.) And now Efrit is getting to be approximately on par with modern coding agents.


All I had to do, in order to crack this nut, was wait 3 months (i.e., 2 model releases). Claude is finding Efrit quite easy now, compared to this summer. I cite this as one of many examples of how the models and tools are indeed getting exponentially better. I have a set of projects they can’t do today. Efrit is (well, was) one of them. If you keep a menagerie of “too hard for AI” projects, then you will be able to watch and measure their cognitive progress increasing month by month.


I often bake this philosophy into my project planning. I will deliberately build something that’s just *slightly* too hard for the agents, knowing that in the next model release, they’re almost certainly going to find it straightforward. I plan for the models to get smarter, by building tools that don’t work that well with today’s models. This is how you get that little bit of extra shelf life out of your software — plan for it to be useful when smarter agents arrive.


If you read this section and concluded, “well, obviously AI isn’t ready to handle *my* project work; I tried it, it was confused, so I’m just going wait for smarter models,” then I wouldn’t blame you. But be careful! You might not need to wait as long as you think. If you’re just using this as an excuse to procrastinate until the models are smarter, then you’re missing out on honing a massive set of skills you need in order to work with models effectively — even as they do get smarter.


In the next section, we’ll talk about a way you can get even more cognition out of today’s models, without needing to wait. You’ll have them solve even harder problems than you thought they were capable of, all because you didn’t give them enough of a chance before. Let’s take a look!


**5. The Rule of Five: When in doubt, have the agent review its own work 5 times.**


[Jeffrey Emanuel](https://www.jeffreyemanuel.com/) discovered this powerful and unintuitive rule. He found that he gets the best designs, the best plans, and the best implementations, all by forcing agents to review their proposals (and then their work) 4–5 times, at which point it “converges”. It typically takes 4 to 5 iterations before the agent declares that it’s as good as it can get.


Jeffrey described a long, complex series of prompts for this process; I’m sure we’d all be appreciative if he publishes them. But the way he described it to me, you first make them do a task, then you do a series of focused reviews. Each review should be slightly broader and more outlandish than the previous one, or you can do it the opposite order. But you need a mixture of in-the-small and in-the-large reviews. You’re having it look for bad code (or designs), but also bad architecture.


To be slightly more concrete, Jeffrey first asks it to do a couple of regular code reviews, which find all the usual stuff. And you’ll notice right away that even on the second review it will often find things it missed in the first review. But I think most of us stop there, if we even ask at all. It definitely feels weird to ask for the 3rd code review, which is the agent’s 4th pass over the code, counting the generation step. But the 3rd review, especially during the Design phase, is where you start asking it existential questions about whether you’re doing the Right Thing throughout the project.


I tried it, and sure enough, it does take 4–5 iterations, just as Jeffrey described, before the agent will say something like, “I think this is about as good as we can make it.” At that point it has converged. And that, folks, is the first point at which you can begin to *moderately* trust the output the agent has produced. If you always take the first thing it generates, with no review at all, you’re bound to be disappointed.


I asked Claude what it thought of this Rule of Five, and Claude was enthusiastically supportive. Claude claims that this process matches their own cognition model, which is breadth-first: they solve each problem first in very broad strokes. And then they almost always need more passes for proofreading, refining, and polishing — much like humans do.


At first you’re going to want to do this purely with prompting. Maybe Jeffrey Emanuel will share some of his fancy review prompts. But over time, you’re going to want to automate it, since you’re applying the Rule of Five at every single step in the process, which at a bare minimum, for any nontrivial hunk of work, would be:


- 5 passes over the design


- 5 passes over the Beads implementation plan (this results in *far* better issues and dependencies, and better execution)


- 5 passes over the implementation (code + 4 reviews)


- 5 passes over the tests


- 5 passes for code health (might as well build it into your dev middle loop)


Yes, this is slower. Yes, this is more expensive (though, probably less so than all the *rework* you’ll be stuck with if you skip these steps.) Yes, it’s awkward to tell an AI to keep reviewing its work that it just reviewed.


But you should make sure you do it. Rule of thumb: demand at least 2–3 passes on small tasks, and 4–5 passes on big tasks. If you’re not super familiar with the language, the stack, or the domain, then you should err on the side of more reviews.


Do this, and it’ll feel like you’re using a model from the future. They will do far better work than they’ve been doing for you. Try it!


**6. Swarm where you can, but beware the Merge Wall**


I’ve been focused on agent swarming the past few weeks, after several months chasing quality and reliability without much success. I’ve got a new (third!) orchestrator in the works, and wow. Swarming. Next year is going to be extraordinary.


I’ll share a quick example of how powerful swarming can be when it’s working right. I had a disaster the other day where 30 Beads issues went missing. It was three or four major epics, each with a bunch of child issues. I had put a ton of work into their design, following the Rule of Five, and they were all ready to implement.


But I couldn’t find them.


I wasn’t panicked, since it’s hard to truly lose issues in Beads (we do have some bugs here and there but they are getting closed fast). Beads is all backed by Git, so it’s almost always possible (for the AI) to reconstruct what really happened from the git history, and fix it.


But I was concerned, because, where the hell did my 30 issues *go*? They weren’t deleted. After a couple minutes of increasingly alarmed searching, I finally figured out where they all went: My swarm had implemented them all! WTF?


There was a minor miscommunication, I guess; I asked my orchestrator to start working on the bug backlog, and it assigned all 30 issues to the eight workers I had already spun up. Some of these were quite complex issues. But while I was busy with other stuff, and not watching, the worker agents implemented and closed all 30 issues.


I was equal parts delighted and flabbergasted when I realized what had happened. I went and checked, and sure enough, they’d done all the work. It was pretty decent work and needed very little touchup — likely because I had used the Rule of Five throughout, and the Beads were in very good shape when it came time to implement.


After my 30 issues were magically implemented, I was *sold*. I would never not swarm again!


And then, of course, I was utterly unable to reproduce that perfect swarm. Subsequent attempts all ran into merge issues and required a ton of hand-holding and infrastructure tweaks. It will be a couple more weeks before I can swarm reliably. But still, I am completely sold.


I’ll know that my swarm orchestrator is ready to launch when I can swarm the web UI, building it from scratch. My system doesn’t have a non-CLI UI yet; well actually it does, in Emacs, but I doubt you want that one, however cool it might be. (It has Efrit inside it, so it’s pretty damn cool.) But I’m going to build a UI with the swarm, and that’s when I’ll know it’s ready for prime time.


The thing you have to be prepared for when swarming, is the Merge Queue problem. It’s like smacking into a wall. To illustrate, let’s say you have a simple swarm of 3 workers. One worker is redoing the logging system, another is changing the database API, and another is changing the client-server protocol. It’s likely that all three of these subsystems have some overlap, and changing one requires changing another. And their work will collide when they try to merge all the work together.


When you swarm a task, a key problem is that the workers all start from the same baseline (e.g. the same starting git commit), and they all do their work off that baseline. But each worker has the ability to change the baseline dramatically. Let’s say workers A, B, and C all complete and merge in their work. The system may now be completely different from the original baseline. When the fourth agent D finishes its work, a rebase may no longer be feasible. The system may have changed so much that D’s work needs to be completely redesigned and reimplemented on the new system baseline, which includes A, B, and C’s changes.


This is why you need the Merge Queue. You need to serialize the rebases, and give each worker enough context, and context-window space, to fully merge their work into the new baseline.


Some work is inherently parallel, and some work is inherently serial — the latter because of irreducible complexity and task overlap. If you think you’re going to be stuck with an awful merge, then you should probably defer some tasks until the earlier ones complete. But it’s not always possible to tell in advance, so sometimes you’ll have tough merges.


I’ve noticed that projects tend to go through a cycle where they are swarmable for a while, but then you’ll suddenly need to pause and serialize all work for a time. This can happen, for instance, if you’re changing the directory layout of your project — e.g., to make it more accessible to AIs who are trying to guess their way around. You might need to experiment with a bunch of different layouts. But each new project source layout changes all your package imports, scripts and other inter-module references, which would totally break any existing workers. So you have to pause all other work while you do the big package restructuring.


You can think of swarming as a MapReduce-type operation. In the mapper phase, you can spin up virtually unlimited workers. But in the reducer phase you need to merge their work all back together. Unfortunately, as Gene observed, this isn’t *really* a MR because most MRs have a very simple reduce phase — the workstreams have a monoidal shape, and you can merge their work by doing things like summing counts or whatever.


But with agent swarming, the reduce phase is a nightmare; it’s the exact opposite, in fact: it can be *arbitrarily* complicated to merge the work of two agents. In the limit, what should we do if Worker A deleted an entire subsystem, and Worker B comes along with a bunch of changes to that (now-deleted) subsystem?


So the swarm merge step is often messy and not entirely automatable. Some cases require either human judgment, or else *really* good context for AIs to make the call.


I don’t know if we’re going to get a tool that hides the mess. I’ve been talking to investors, many of whom are keenly interested in the next generation of developer tools, and there is a prevailing belief that all we need are proper guardrails, and then these kinds of agentic coding and swarming tools will be accessible to “average” developers, which they certainly are NOT today.


And why is that? Well, as Joel Spolsky observed in Things You Should Never Do Part 1, *reading code is by far the hardest part of coding*. This is a well-known finding in the Dev Productivity world; they’ve done study after study. And with vibe coding, reading code is… pretty much all you do all day. It’s hard for most developers. The average dev probably thinks 5 paragraphs is an essay. Coding agents make you read enormous waterfalls of both text and code. This is absolutely draining and beyond the capabilities of most devs today.


However, I don’t see eye-to-eye with the investors on this one. I personally do NOT think we will get useful guardrails. If you try to build something with heavy guardrails, you’re going to wind up with Bolt or Lovable, and nobody will use it. Sorry! That’s just not the right model. Instead, I think we’re going to get orchestration tools that are every bit as powerful, messy, quirky, and frustrating as Claude Code and the current batch of terminal-based coding agents.


And the people who figure out how to use these tools, despite the lack of guardrails, will become super-engineers. I’ve been kicking around the idea of a new blog post, the Rise of the Superengineer. Dunno if it’s worth a whole post, but what’s going to happen in 2026 is that a new class of 100x (or maybe 1000x) engineer will emerge — people who have figured out how to wield coding agent orchestrators effectively, deal with the merge problem, planning, swarming, code health, etc. — all the stuff I’ve talked about here, and more. And they will be able to run 100 coding agents at once, and get meaningful work done with them.


This will make them as productive as a team of 50+ regular engineers.


I think my own orchestrator will usefully peak at around 50–80 agents. Maybe I can get it up to 100. It’s not aimed at massive swarms; it’s aimed at leveling you up from manually managing a dozen ad-hoc agents in ad-hoc repo clones all around your filesystem, to managing swarms of well-behaved agents working 5–10 at a time on focused tasks. It will still require your full attention, your full engineering background, and every bit of design taste you can muster, to use these tools. In some ways it’s even harder and more dangerous than using a single coding agent, even with tooling support.


But some people are doing it already! By hand, to be sure, or by building their own homegrown orchestrators. Mark my words, though: next year, you’re going to have engineers who can build an (and likely maintain) an entire company’s software on their own. You’ll have solo unicorns, sure, but also a marketplace of solo uber-contractors who can build companies things they would have had to pay someone like Accenture tens of millions of dollars for.


There will also be small teams of people who figure out how to maximize their velocity when multiple humans work with agent teams. And these small teams are going to change the world. Gene and I are actively wondering whether company size is going to decrease on average, because you will be able to get so much more done with so many fewer people.


But no matter what, the tools are going to be messy from now on. Working with AIs is a little messy and nondeterministic. And I think that’s here to stay.


**Wrap-Up**


Gene and I went through at least a baker’s dozen ideas this morning, and I’ve chosen the half that seemed the most baked. A few others are becoming clearer, but are still so vague that we don’t really have the right vocabulary to talk about them yet.


Change is coming. Agents are *way* more powerful than they were 3 months ago. I’ve talked with plenty of (good) engineers lately who still believe that agents have plateaued. Ignoring the 30 years of evidence showing that AI is following Moore’s Law, they feel it’s just going to stop getting better today, out of nowhere. And in their opinion, agents are not good enough yet.


But if you’ve been following and using agents since they landed in February, you’ll know just how much more powerful and capable they have become, even since summertime. It’s not plateauing; heck, it’s not even slowing down. And you can prove it using your backlog of projects that are too hard for AI. Every few months, another one will fall, until there are no more left.


If you’re one of the many engineers who still hasn’t made the switch to AI-first coding, now is a good time to try it again. If you haven’t used an agent in a few months, you’re going to be shocked at how smart and capable they have become. They are full concierges now, able to help you with *any* computing-related problem. People tell me they even use Beads for their personal TODO lists!


My orchestrator is right around the corner. I’m excited for it. It’s going to make a splash. Hopefully this Christmas!


But you’ll only be able to use it if you already use coding agents for literally everything. If you want to be a 100x super-engineer next year, you need to start learning vibe coding basics today, and *make* it work for you. Keep in mind all the advice I’ve given here, and read our Vibe Coding book, which just came out on Oct 21st. It’s fresh and relevant, and will help you get into the right mindset with the right techniques and practices.


More to come, soon.


This stuff is so fun!


![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=d4e9c86e42a9)
