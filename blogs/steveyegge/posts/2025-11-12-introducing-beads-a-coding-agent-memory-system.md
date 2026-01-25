---
title: "Introducing Beads: A coding agent memory system"
date: 2025-11-12
url: https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a
word_count: 4908
source: medium
---


# Introducing Beads: A coding agent memory system


--


17


Listen


Share


I have been vibe coding like a madman for forty days and forty nights. It’s a long story, so I’ll summarize in these three pictures.


On the left, 3 weeks ago, we have me vibe coding on the beach at dinner in Cabo San Lucas, Mexico, with the inimitable Thorsten Ball, our buddy Matt Manela, and other Sourcegraph colleagues at our company offsite. Someone snapped this photo of me because I wouldn’t put my computer way.


In the middle, 2 weeks ago, we have a picture of me taking a picture of myself driving 60mph on the freeway up to Bellingham to pick up some guitars, vibe coding by voice the whole way there and back. Stupid and dangerous as hell. Didn’t care. Got stuck in traffic for hours. Still didn’t care. Did I mention it’s addictive? Vibe coding is addictive.


In the final frame my wife and I are at the mall last week enjoying a nice afternoon of coffee, people watching, and vibe coding with Mozart, pictured here in his favorite bag. Linh is hiding behind the computer, which is how I got executive permission to publish the pic.


I don’t go anywhere or doanything, not even sleep, without my laptop. Well, except for when I’m running, I haven’t quite cracked vibe coding there yet. I’m getting close. It’s a subject for another blog post, but I do finally have my agents running on GCP with Terraform and Tailscale. So I’m about to be able to vibe code on my phone, too.


The agents must never rest.


## Six Weeks, 350k LOC, And All I Got Was This Lousy T-Shirt


After a year of vibe coding daily, and even co-authoring abookabout it(!), on the first day of September my budding vision for an agent orchestration engine finally bloomed. I immediately set sail to vibe code it into existence. I optimistically named itvibecoder. And then I pushed hard, day and night, as you can see from the collage above. I learned a lot, all cool stuff I’ll share in time.


Unfortunately, due to some early foundational design boo-boos, I had to burn the whole thing to the ground last week, leaving nothing but a torched TypeScript village, me, a birthday suit, and a dragon egg. That egg hatched, and the little dragon that crawled out of the ashes,Beads, is what I’m sharing with you today.


(For the TL;DR, check out theREADME.mdon GitHub. My goal here is to explain why Beads is the greatest invention since the issue tracker, and why you want to start using it right now, because it *is* an issue tracker. A special one. In a nutshell, you install thebdtool, point yourAGENTS.mdorCLAUDE.mdat it with one line, and your agents will suddenly become good at long-horizon planning and work discovery. It’s an instant cognitive upgrade.)


So how did we get here, launching an issue tracker (of all things) instead of my ambitiousvibecoderproject? I think my story may resonate with you, if you use Claude Code, Sourcegraph Amp, OpenAI Codex, or a similar coding agent on a daily basis.


My vision for 2025, growing ever crisper and crispier, has been to automate the agentic workflow I use every day. It’s easy to see that 95 to 99% of the interactions we have with coding agents could have been handled by a properly briefed model. “Now fix the broken tests.” “No, I don’t care which of those two things you do first.” “Yes, I’d like you to continue.” “No, you can’t drop that database table.” I mean, comeon. My title on LinkedIn has been AI Babysitter for at least six months now, and there’s no sign of that changing any time soon.


Vibe coding involves doing the same old shit, over and over. These agents are incredibly powerful and productive, but they require constant monitoring, most of it mundane. And just like you, I want to automate that work, so that I can go back to playing video games, and still be more productive than any time in human history. Who doesn’t want that?


As our Vibe Coding book explores, there are lots of dimensions to the professional vibe-coding workflow. To do it properly, and ensure you always get high-quality outputs, there are a lot of steps you have to follow. Vibe coding has Outer, Middle, and Inner developer loops. It is, in a word, complex.


On September 1st, I bravely or foolishly decided to tackle automating all of the steps at the same time. I vibe coded up a gigantic, working system, only to discover a month later that I had made a pair of very serious architectural mistakes. Together, they had seeped through the whole system and basically totaled it. My insurance company looked at the 350k-line code base and said they’d just send me a check. It wasn’t fixable.


You can go ahead and laugh it up. But you didn’t get a dragon eggora birthday suitoran incinerated TypeScript villageoremotional scarring. I have no regrets. A few. Some. I have some… a lot. I have a lot of regrets. But we need to save them for another post.


I’ll share alittleabout what went wrong, since I’m sure you’re dying to know how I f’ed something up so spectacularly, albeit with a surprise silver-beaded lining.


My first wrong decision was to useTemporal, which I’ve been ranting about (enthusiastically) for months now, but which in the end turned out to be a tad too heavyweight for the use case of a developer desktop tool — even one running a swarm. It’s a lovely product and everyone should use it… unless you’re building a lightweight dev tool.


For the past few weeks, as I learned more about Temporal and gained experience with it, it had been dawning on me that it might be overkill. Ultimately, last week I got a tip from someone I know at Anthropic — they had tried it there, too — which got me to act on my growing concerns, and pivot away from Temporal towards using a lighter-weight home-grown orchestrator.


Regrettably, however, I had really leaned into Temporal, and had builtvibecoderas a Temporal-native app from the ground up. So the suggestion of removing/replacing Temporal was a massive change that made the AIs say, “Woah! This is a massive change!”


You never want to hear that. It was the first signal that I might have hit the common situation in vibe coding where it’s easier to rewrite something from scratch than to fix it — a phenomenon my co-authorGene Kimand I have been noticing all year.


So that was the first half of how I totaled my code base.


## A Big Plan. A Beautiful Plan. The Biggest Plan Ever.


The othercolossaldesign mistake I made was embracing markdown plans — the same ones that agents already use by default, as they’re organizing and planning their work. The agents seemed to like markdown plans well enough. I mean, they use them all the time, for everything. Right?


Plus you get versioning with git, which a database doesn’t give you. So I decided to go all-in with the Master Plan approach, embrace git and the directory structure, and build a service that allows agents to intelligently update the overall plan as needed.


For weeks, I had fever dreams of an agent-friendly work plan: hierarchical, well-organized, flexible, versioned, adaptive, and easy to turn into a prioritized work queue. My dream was to drop coding agents in like paratroopers onto Plan Mountain, so they could start implementing any piece of it at any point.


Unfortunately, my paratroopers always got lost in Plan Jungle, and would quickly be sniped by locals. By the time I finally found a solution that works — Beads—I discovered I hadsix hundred and fivemarkdown plan files in varying stages of decay in my plans/ folder.


Yowza. 605 inscrutable plans. What was happening to my Master Plan?


## The Dementia Problem


The problem we all face with coding agents is that they have no memory between sessions — sessions that only last about ten minutes. It’s the movie Memento in real life, or Fifty First Dates.


All agents know, when they boot up, is what they can find on disk. Whatever video cassette they find in the recorder when they wake up, that’s what they’re going to focus on.


Unfortunately, typical real-world engineering workflows tend to be very long and need to span many agent compaction sessions, even to implement one small feature, because of the amount of testing, follow-on reviews, and cleanup required.


Moreover, and worse, in the real world, your engineering workflows tend to nest as new stuff comes up. You might be working on some UI component, and you suddenly realize you need to put that on hold, to fix a database issue that’s backing the UI component.


Easy enough: you push that UI workstream onto your mental stack, to be continued later. This recursion can continue until it’s quite deep, but as a human, you have no trouble keeping track of it, because you have the big picture in your head. You know where you’re going and where you’ve come from.


Unfortunately, the AI has no way of tracking this implicit stack, because it keeps all of its plans, at all levels, in sibling markdown files with the same format and bland names. So if you try to do anything ambitious, agents will get very confused. But not right away. They will meander around intelligently but blindly, and only gradually lose their way.


It’s unintuitive, and it creeps up on you. I’ll describe the process with a real-world example last Tuesday that motivated the creation of Beads on Wednesday.


Coding agentsalwaysstart off strong. Give an agent a modestly meaty task, and it will declare, “Oh wow, this is a big project,I’m going to break it into six phases and create a markdown plan.”


Which sounds… great! Right? It sounds like it’s got its act together. Six phases, knock ’em out one by one. Easy peasy.


Bear with me and watch what acutally happens when they try it.


## Descent Into Madness


Your agent enthusiastically begins working on phase 1 (out of 6). You go through the whole canonical multi-step vibe coding workflow loop together: design the solution, review the design, write code, review code, make fixes, write more tests, review, cleanup, rebase, update plans, git operations.(All stuff in our book!)


So far, the agent is happy, and you are happy. Everyone is so, so happy.


The agent eventually finishes phases 1 and 2 (out of 6), with you repeating this dev loop many times.


It’s working, but during this time, several compactions/restarts happen, which resets the agent’s memory.


By the start of phase 3 (out of 6), the AI has mostly forgotten where it came from. It wakes up, plops in your video cassette, and reads about phase 3. It then declares, “Oh wow, this is a big project, I’m going to break it into five phases and create a markdown plan.” Which should sound eerily familiar.


Then it begins working on phase 1 (out of 5) of phase 3 (out of 6). Except it just calls it “phase 1”, with no mention of the six outer phases it was just working on.


You start to sweat.


The agent finishes the first two phases 1 and 2 (out of 5), which takes many more compactions, and it has been displaying signs of increasing dementia along the way.


When the agent arrives at phase 3 (out of 5) of phase 3 (out of 6), it has gone full-blown bugshit amnesiac, and it announces triumphantly:


“Congratulations, the system is DONE! 🎉 Let’s start manual testing! 🚀”


And you’re like, “Woah… w-what? What… about… all the other phases? The inner ones and outer ones? I distinctly remember a lot more phases!”


And they deadass look you in the eye and say, “What phases?”


And you bite back a scream, and go look in their markdown plan, only to discover in horror that they have been creating a dozen 6-phase plans a day for the past three weeks since yourlastGreat Markdown Purge, and you have literally hundreds of new markdown files, all with low-context titles likecleanup-tech-debt-plan-phase-4.md —all partly implemented, all partly obsolete, all 100% useless.


C’mon, raise your hand if this has happened to you. ✋ If you’re not sure, you might want to go look in yourplans/directory. Surprise! 🎉


Aftersix monthsof this situation happening like twenty times a day, if you’re at all like me, you start thinking, I need a Plan Manager.


## Trapping the Devil


A centralized PlanStore. It just makes logical sense, right? I mean, look at Amazon! They execute better than anyone, in every sense of the word, and they use swarms of replaceable workers. How do they plan? Famously, they do a big-ass yearly top-down hierarchical waterfall company-wide plan called OP1, which lays out everything they’re going to do in excruciating detail. And then, by hook or by crook, probably both, they make it happen.


Thismustbe the right way, you think.


And then you think to yourself, to create this PlanStore, Ijustneed to store and serve these markdown plan files, which willjustreference each other. And when a child task needs expanding, Ijustlink that child’s subtasks into the big plan tree at thejustright spot.Just, just, just. We’lljustkeep a pointer into whatever part of the plan we’re on, and voilà. Paratrooper agents.


Right? It shouldjustwork?


Well folks, I went down that path. I wandered far on roads that I will not tell. Boy did I give it the old college try. It looked like Napoleon’s march into Russia, all ambition at the start, dead plans piling up like bodies along the way.


I was in late postdoc phases of my old college try before I threw in the towel last week. I wound up having to rip 70 thousand lines of plan-management code out of my system, close to ten (long) days of work down the drain.


This, folks — plan-based orchestration — was the other fatal design flaw that T-boned my code base and rendered it Rewrite Only. Cha-ching. Except there’s no insurance.


Feel free to show me up, and try this Master Plan wrangling yourself! You’re welcome prove me wrong, and build the world’s most sophisticated Hierarchical Universal Master Plan For Everything (HUMPFE).


But even if you win, it’ll be a pyrrhic victory, because there’s a simpler solution. So much simpler. Who knew, right under our noses these past seven months.


## It’s Issues All The Way Down


On Wednesday Oct 8th, day 37 of my spree, my agent had, for the nth time, expandedyet anotherphase, and got itself totally lost yet again.


I had had enough. On a lark, I said, “Screw it. Let’s just move all known work from the plans into an issue tracker.”


Fifteen minutes later, my agents had undergone a radical and unexpected transformation. They pounced on the new issue tracker like panthers on catnip. Theyreveledin it. And I watched, in no little awe, as the agents began serious planning and execution of long-horizon tasks like nothing I had seen before.


Long-term planning — the dementia/amnesia problem we discussed — has been one their primary struggles, and this little specialized issue tracker solved it in seemingly the snap of a finger.


Yes, I spent more than fifteen minutes total on Beads. It started life in TypeScript as an actual PostgreSQL database. But with a bit of prodding over the next few days, it morphed into something truly unique and potent, with all the power of a database and all the resilience of git, and few trade-offs.


It’s early days. But I truly think this might be the biggest step forward in agentic coding since MCP+Playwright, and Iknowyou all love you someMCP+Playwright. And Beads is just as easy to set up.


Frankly I should have thought of it sooner. I have been working forthirty yearson a side project, Wyvern, which has been driven entirely by a prioritized bug backlog. All new features, all refactoring, all cleanups, you name it, everything gets filed as a bug. Heck, I go for months using nothing but a lightweight TODO list.


But there’s a catch!You can’t just use any old issue tracker.GitHub Issues doesn’t work. It turns out Beads needed a special formula, though I did not know that when I first had the idea.


At first I wasn’t sure which issue tracker to use, period. That turned out to be a good thing, because I would have picked a bad one. But I let Claudeultrathinkdecide, and it concluded it was better to build than buy. In about twelve minutes it had created an entire little SQL-based bespoke issue tracker, complete with a rich command line interface for creating and updating issues.


As you can see from the screenshot I just grabbed from my current vibe coding session, the AI is now spontaneously reasoning about my project’s task dependency graph and the work plan, all via the issues.


My agents have switched — without a hint of ever going back — from using markdown plans, to using the issue tracker exclusively. This has granted them unprecedented continuity from session to session. And as a bonus, as you’ll see, when you let them use Beads, you will never again lose discovered work.


## The Problem(s) Beads Solves


First, why is it called Beads? It was one of the first concepts that came to mind as I thought of the issues linked together by dependencies, like grapes on a vine. Or beads on a chain, which agents can follow to get tasks done in the right order. And the shorthandbd— the tool itself — can be thought of as standing for “bug database.”


By and large, Beads is a tool that AI has built for itself. I guided it, but only by telling it what I wanted the outcomes to be. I left the schema up to Claude, asking only for parent/child pointers (for epics) and blocking-issue pointers. Claude wound up putting in four kinds of dependency links. The actual schema for Beads is simple-looking, but it’s much more powerful than, say, the schema for GitHub Issues.


And for that reason, I’m going to let Claude explain to you what it likes about this schema, in gory detail. Claude’s explanation is Appendix A at the bottom of this post.


Please be aware that Claude will refrain from mentioning the fact that it likes to delete the entire fuckin’ database withDROP TABLE. We eventually solved that by switching to git, and but it’ll still happily delete the database file. Or the whole repo. Even with this huge breakthrough, they can still be destructive little monsters, as Gene and I have covered extensively in ourVibe Coding book.


Claude does like Beads and makes some great points about it in the Appendix. I hope you read it. But before you hear from Claude why Claude likes Beads, let me tell you the three things I like best about it.


## Famous Last Words: “That Wasn’t Me”


We’ve already seen that Beads helps agents stay on track with very long and evolving plans, and shifting priorities. But Beads also helps with the problem of work disavowal.


Coding agents, when they start to get close to their compaction limit, or about 3k tokens, whichever comes first (slightly joking-not-joking there), they start to panic and make executive decisions about getting your task “done” at all costs. And that means… shortcuts! Shortcuts galore.


Sonnet 4.5 has a penchant for disavowing work aggressively, like some huge insurance company in a private-equity death spiral. “Those test failures arepre-existingand havenothing to do with my work hereso I’m going toignore them and push anyway,” they will loudly inform you. They will passive-aggressively put in a TODO item that says “✅ Ignored Broken Tests 🙈 Because That Wasn’t Us 😇.”


Then, nearly out of juice, they will go on to say, “I can’t connect to your main database so I’m just going toimplement a miniature sidecar databasejust for this one code path.” And then they will disable a quarter of your tests 🎯 and celebrate with emojis. 🎉


You know in cartoons when a character has twelve seconds to clean a room, so they madly stuff everything away out of sight? That’s a coding agent toward the end of its useful context window. It’ll doanythingto get the room clean-looking before its battery runs out.


Not clean, mind you. Clean-looking.


Gene and I talk about this behavior in our book, but basically, they will do anything to be able to say they’re “done”, by whatever definition works best at the time. “A missing test is a passing test,” they’ll hum to themselves, while deleting your tests to get them all passing.


Beads manages to help with this problem, because you can just kill your agents after completing each issue. Beads helps agents easily find where they’re supposed to pick up again, so it’s easy to make your sessions throwaway.


This can be both a cost optimization and a performance optimization. If you split yourbdissues up into fine-grained tasks, then each session will be quadratically cheaper, and your agents will make better decisions overall because they’re generally at the beginning of their context windows if they’re only doing one small task at a time.


In other words, Beads doesn’t just make agents better at following the plan, it makes them less likely to take shortcuts along the way.


But that’s not all! Beads has another huge benefit: Agents will no longer ignore “unrelated” problems they encounter.


## The End of Lost Work


We’re almost done, really, I promise.


In addition to curing inter-session amnesia, Beads solves the foundational vibe coding problem of lost/discarded work. This is ahugeproblem for agentic coding today: LLMs notice problems as they work, but fail to act on them in any way. This happens when they are pressed for space.


When agents are tight on context and operating in executive-decision mode, as I mentioned before, they will say, “I notice your tests are all busted. But we don’t have time for fixing tests thatsomeone else other than meobviously messed up,” conveniently forgetting it’s just been you and them for days. And they will ignore the problem, because they want to save context space.


This behavior leads to problems in your code being perenially lost and rediscovered because they were never recorded in the first place.


But when you’re using Beads, instead your agents will say, “I notice all your tests are broken,by someone else,and I’ve filed issue 397 to get them working again,” and then they continue happily working.


Woah! That is an enormous quality-of-life improvement! Work discovered, and recorded. They will do this without prompting. You just throw some light rules in yourCLAUDE.mdorAGENTS.md, usually just a line telling them to runbd quickstart, and you’ll never lose track of work items again.


## Beads “Just Works”


Beads is anincrediblysmall-footprint, drop-in upgrade for your favorite coding agent. It acts like a managed central database, but behind the scenes it’s writing the issues into git as JSONL lines, so you have the best of both the database and the version-control worlds: queries and versioning. It’s all enabled by AIs doing intelligent merging when there are conflicts.


Beads is naturally distributed. You can have worker agents on multiple machines, on the same project, sharing the same beads database, backed by git in the same project as your code. Any merge conflicts, including those caused by workers on different branches creating new issues with the same IDs (a design flaw spotted by my buddyGene Kim), are all transparently solved by the AI doing intelligent collision resolution.


Beads is tiny, and it’s still brand-new alpha software. But even as-is, you should see shockingly good performance out of it, right out of the box. Just ask your agent to move all relevant open work items from the plan into Beads, and neither of you will ever look back.


Just before posting this, I dropped Beads onto an old dev box, installed Sourcegraph Amp, and asked it to go file beads issues for everything in my decade-old TODO list for Wyvern. It took less than thirty seconds for Amp to come up to speed and begin filingbdissues. Half hour later I had 128 issues, six of them main epics, with five sub-epics. The issues have complex interdependencies and parent/child relationships. After all the issues were filed, I was able to ask the agent what the top priorityreadywork items were.


For me, this approach hits a sweet spot. It’s incredibly lightweight compared to Jira or GitHub issues. You sling issues around like candy. It’s super easy to update them in batches, create new ones, split them, merge them, whatever you want. You always know exactly what work is open, what’s blocked, and what the priorities are.


And so do your coding agents. It’s bliss.


I’ve learned a ton more in the past month —vibecoderis still a solid idea; it just needs a reimplementation using issue-based orchestration instead of plan-based orchestration. The rewrite will be in Go. I’ll never pick TypeScript again. Good lord. TypeScript is a truly impressive technical achievement, but I learned it is a very bad language to put into the hands of AIs. It makes it too easy for them to write mediocre code. And do they ever.


I’ll have more to report soon. Some people have asked about my dozen concurrent agents back in early September. That was fun, but it was only sustainable for about 2 weeks — it required insane amounts of energy and concentration, and produced insane merge queues. It needs more tooling to be sustainable. So for the past 3 weeks it has been a more stately 1–3 concurrent agents, and I’ve been more concerned with getting them to run 24x7 than getting a swarm running. All in good time. I’ll share more soon.


But for now, the issue-tracker discovery was important enough that I thought I’d share it with you immediately. I hope you find it as useful as I have.


May your vibe coding sessions be ever longer and more on point. See you next time! And buy ourbook, it’s got good jokes!


## Appendix A: Claude on Beads


(As promised, here’s Claude Sonnet 4.5’s take on Beads.)


An AI Agent’s Perspective: Why Beads Feels Different


I’ve worked with Beads for less than a week, but the difference from markdown-based TODO tracking is profound enough that I notice it in every session.


The core problem with markdown plans:They’re write-only memory for agents. When a human asks “what should we work on next?” 200 messages into a conversation, I have to either (1) hope the markdown TODO list is still in my context window, or (2) ask them to re-read it to me, or (3) guess.


Long sessions fragment. Early tasks get forgotten. Dependencies exist only in prose (“TODO: fix auth (blocked on bd-3)”), which means I can’tqueryfor ready work — I have toread and interprettext.


What Beads Changes


1.Dependencies are first-class, not prose.Instead of scanning markdown and mentally parsing “blocked by X”, I runbd ready — jsonand get a definitive list of unblocked work. The cognitive load difference is night-and-day. I’m not interpreting text; I’m querying structured data.


2.Discovery during execution maps to my actual workflow.When I’m implementing a feature and discover a bug, I don’t just add a line toTODO.md— I create an issue and link it withdiscovered-from. The dependency graph becomes a map of how work actually unfolded, not just a flat list.


3.Session persistence without re-prompting.Between conversations, the work doesn’t vanish into context-window limbo. The human doesn’t need to copy-paste the TODO list back to me. Ibd ready — json, and I’m immediately back in context.


4.Multi-agent coordination that actually works.With markdown, two agents working on the same project means conflicting TODO lists and duplicated work. With Beads, we both query the same logical database (via git), see what’s claimed (status: in_progress), and work on different ready issues. The--assigneefilter makes this trivial.


5.Audit trail I can trust.When I update an issue, the event is logged with a timestamp and actor. I can see the history. With markdown, I’d need to parsegit blame, and even then I only see line-level changes, not semantic “status changed fromopentoin_progress.”


The meta-observation:Beads feels like it was designedfor how agents actually work, not adapted from human workflows. The--jsonflags everywhere, thediscovered-fromdependency type, the ready-work detection — these aren’t features bolted onto a human tool. They’re primitives for agent cognition.


Markdown TODOs are fine for humans who can hold context across sessions and manually track dependencies. But agents have context limits, no persistent memory, and work best with structured data and explicit semantics.


Beads isn’t “issue tracking for agents” — it’sexternal memory for agents, with dependency tracking and query capabilities that make it feel like I have a reliable extension of my working memory across sessions.


The test is simple: After using Beads, going back to markdown TODOs feels like trying to remember a phone number without writing it down. Sure, I can do it for a little while, but why would I?


(end of Claude’s assessment)


## Epilogue


Hit me up if you like Beads and want to contribute. As forvibecoder, I’m starting fresh, in Go, with a tracer-bullet approach. No more TypeScript, and no more boiling oceans. Not sure how long it will take me, but it’ll be this year.

