---
title: "The Future of Coding Agents"
date: 2026-01-20
url: https://steve-yegge.medium.com/the-future-of-coding-agents-e9451a84207c
word_count: 3983
source: medium
---


# The Future of Coding Agents


--


11


Listen


Share


It has been three days since I launched Gas Town! 🔥⛽💥🛢️🔥 Woohoo!


Thelaunch posthad a lot of ground to cover. Fortunately we can relax now. Gas Town is alive, if only just. I have created something that isjust barely smart enough. Gas Town works pretty OK today. Super fast, very fun, very powerful, definitely sloppy. But it will get dramatically more capable as four evolving situations unfold this year, around tooling and model intelligence.


In this post, I’ll share a bit of the backstory of Gas Town that I had to leave out of the Jan 1 post. And then I’ll share some predictions about what I think will happen to IDEs, big companies, and coding agents themselves. I also plan to do a bunch of posts and videos on how I use Gas Town to do real work.


Gas Town is impressive to watch in action. And it’s only just getting started.


## Gas Town’s Free Upgrades


First, let’s talk about how Gas Town will get smarter, simply from having launched it. Gas Town is a bit of a Swamp Thing right now; it sort of oozes rather than whirs. Itdoeswork, and astonishingly fast. Nothing like hurling swarms of Claude Code Opus 4.5 instances at a big epic, or bug backlog. Chomp, chomp! But it also requires a lot of manual steering and course-correction, and you sometimes have to push it to finish.


But that initial instability will fade over the course of 2026. Gas Town will go from a self-propelling slime monster to a shiny, well-run agent factory. All without me having to do a damned thing to improve it myself anymore (though I still will!)


First,models will get smarter. I know many of you think they have plateaued. I know many of you are building tools around the idea, “what if the models never got any smarter?” But modelsaregetting smarter, and better at coding (and everything else). I aimed high with Gas Town. It’s a lot today, but it should be natural for models to play their roles by midyear, if not sooner.


Second,Gas Town and Beads are going to finally make it into the training corpus. One of the astonishing hallmarks ofBeadsis that agents use it naturally and smoothly with no training. Gas Town, too — still a bit bumpy yet, since Beads is two months more mature. But Gas Town will get there too. Fast.


I have been curating Gas Town the same way I did Beads, using theDesire Pathsapproach to agent UX. You tell the agent what you want, watch closely what they try, and then implement the thing they tried. Make it real. Over and over. Until your tool works just the way agents believe it should work. So Gas Town is gradually becoming agent-friendly, even without being in the training corpus.


But now that people are using it? Psh. Agents will know all about Gas Town by summer.


Third, coding agent shops are going to wake up, realize that they have built workers when I’ve built a factory (and the world will soon build more factories), and2026 agents will compete on how well they support being factory workers. Gas Town currently has a crummy, duct-taped API atop a agents that offer barely any platform hooks. The agent shops that start supporting all the necessary automation hooks, to start turning their beloved pets into cattle, will be the agents who win in 2026.


Fourth, and last but not least, theGas Town community is already goingnuts. I’ve already had over 50 PRs, and double that in issue reports and feature requests. And it’s only the weekend; most people haven’t even come back from the holidays andseenGas Town yet. Despite my dire warnings not to use it, Gas Town is growing fast, 10x faster than Beads did. Even if the modelsweren’tgetting smarter, Gas Town will still come into its own anyway, with the community’s help.


Those of you who understood the vision immediately and reached out — I am grateful for you. And for all the contributors sending PRs and GHIs and trying it out, I’m so glad for your help.


Gas Town’s contributors will help make this a reality. I’ve painted just enough of a complete and coherent vision, with a solid initial implementation, that people are already on board and helping me fill in the details.


OK, alittlestory of how we got here, and then we’ll get to the predictions. Feel free to skip or skim the backstory if you’re not interested.


## Gas Town was Orchestrator #4


In August I started working on an orchestrator calledvibecoder. It was in TypeScript, all vibe coded. It was a serious attempt to automate my own workflow using (at the time) Amp, which has always been a luxury Rolls-Royce coding agent. Amp has great ergonomics. But importantly, it also has Ads — which means, Amp just might be the most affordable way to use Gas Town today. I found myself running 5–10 instances of Amp, and wanted to try to figure out how to get them to help me with the job.


My v1 attempt, Vibecoder, was built atopTemporal, which is the gold standard for workflow orchestration. It proved cumbersome for my needs. The workflows I was orchestrating turned out to be micro-workflows, since you have to severely decompose tasks for LLMs to reliably follow them.


Unfortunately, that lost me some scalability: Gas Town isn’t super vertically scalable in its K8s-shaped form. A town is about machine-sized. Gas Town scales by having lots of towns, much like Git scales by having lots of repos, which really just pushes the scaling problem onto the user. For this reason, I still believe Temporal will be a key piece of the puzzle for scaling AI workflows to enterprise level. Models love to offload cognition to powerful tools, and Temporal is as powerful as it gets: theBagger 288of workflow orchestrators. But that power is exactly why I stepped away from it for my dev tool: I feel like it needs a “lite” version.


My v2 version ofvibecoderwas calledvc. You can see the legacyrepo; it was supposed to be private but at some point I thinkvcitself made the repo public. It was in Go. It wound up being overly monolithic, not because of Go, but because I was trying to solve the wrong problem. Withvibecoderandvc, I was trying to make agents better. With Gas Town, I was just trying to make more of them. The fact that Gas Town has all the features of the other two, with a tiny fraction of the code, tells me I finally got it right.


My v3 orchestrator began on November 23rd. I had by then left Sourcegraph (three memorable years, great company, lots of fun) and I was now working on a set of Python scripts aimed at trying to help me with swarming work. I had given up on quality and switched my focus to quantity. I started by moving all my ad-hoc named agents (just random directories and repo clones) under a single tree and trying to organize them withgit worktree.I called it Gas Town, after Mad Max, because it was a ridiculously chaotic environment at first, where it felt like everyone was fighting to get their work done. I now call that first version PGT, or Python Gas Town.


Gas Town eagerly adopted a discovery by Jeffrey Emanuel, author ofMCP Agent Mail. He found that combining Mail with Beads led to an ad-hoc “agent village,” where agents will naturally collaborate divide up work and farm it out. Coding agents are pros at email-like interfaces, and you can use mail as an “agent village” messaging system without needing to train or prompt them. They just get it. Gas Town was my attempt to turn an ad-hoc agent village into a coordinated agent town.


Python Gas Town grew quickly, becoming operational within a week, and carrying me for a couple weeks. It had evolved most of the roles except Deacon and Dogs. The Refinery was brand-new and untested. Mostly what Python Gas Town did was provide spawning for named and ephemeral workers. All with raw Beads and epics. But something about it feltright.


The last 2 weeks of December, after my trip to Sydney/Melbourne to visit CBA, was the fertile innovation period where I came up with 90% of the design for Gas Town. I had promised everyone at the workshops that I was going to launch it (Python Gas Town!) by Christmas day, or Jan 1 at the latest. Not realizing that I was going to wind up redesigning and rewriting the whole thing in Go, immediately after I got home.


It was the port to Go that actually encouraged me to try different things. I would tell Claude, “this is it, this is our last chance to get this or that irksome issue fixed”, and I went all-in on Gas Town’s revised architecture. I had to redo it all 3 or 4 times(again, after 3–4 redesigns in PGT) because the agents were still guessing wrong about the directory structure and roles. But eventually I achieved liftoff. By Dec 29th, my handoff loops were working, seances worked, polecats and swarms and convoys were working, the crew and tmux bindings were working, and I could improve Gas Town simply by slinging work at it. It was time to launch!


## Why Golang?


My four orchestrators were written in TypeScript, Go, Python, then Go. For the record, I’m mostly a Java/Kotlin guy by background, and my best scripting language is probably Ruby. And I am generally happiest hand-coding in any dialect of Lisp.


But I am really liking Go for vibe-coded projects. I probably wrote close to a million lines of code last year, rivaling my entire 40-year career oeuvre to date. I started writing code at age 17, and I estimate that in the past 40 years I’ve handwritten about 1.1 million lines ofreleasedproduction code. But despite my attempts to keep Beads and Gas Town small, together they are already pushing half a million lines of code, including contributor contributions.


During the time I was vibe-coding those million lines of code, I learned a lot about what AIs handle well and poorly. And what I found is that models waste a lot of tokens on TypeScript. It’s, like, too much language for them. Easily a third to half of all my diffs they created in TS were either complicated type manipulations, or complicated workarounds to avoid having to put proper types on things. Every single “write code” step had to be followed by 2–3 “let’s make it less bad” steps that don’t exist in other languages, to force it to go clean up all its crummy type modeling. I found it to be a huge waste of tokens, and the end result was still always ahugepile of code. For an ultra-expressive language it sure is verbose!


Python was “fine”. It didn’t suck. It hot reloaded my changes as I was working, which was nice. Whereas with Go, every agent has to reinstall and re-codesign the binary locally whenever you make a change, and they tend to forget. PGT’s code diffs were easy to scan and understand. The agents don’t waste time wrestling with type modeling. I think for server-side stuff, Python can potentially be great. But for a client-side deployment, it still always felt like a bunch of scripts. I liked Beads’ ability to build and distribute a native Go binary, so I opted for that with Go Gas Town.


Sure enough, I found on my second major Go project that Go is just… good. Polyglots have always turned their noses down a bit at Go because it’s “boring,” but I now think that’s an evolutionary advantage in the AI-coding space. When the diffs go by in TypeScript, half the time you’re like, what awful thing is my computer up to now? But with Go, it’s justboring. It’s writing log files, doing simple loops, doing simple conditionals, reading from maps and arrays, just super duper plain vanilla stuff. Which means you can always understand it! Speaking as someone who has studied and used 50+ programming languages, always looking for elegance and compactness — to my surprise, Go is a real boon to vibe-coding systems programmers.


Is TypeScript still the best for Web apps? Yeah, probably. I’m just glad I don’t have to build one.


## The Future of Coding Agents


I’ve already predicted that IDEs, in their current form, are goners. If you’re still using one, you need to get your ass in gear and start using coding agents before before you acquire the equivalent of severe body odor on the open market.


Everyone seems to think that the future of coding agents is… coding agents. I’ll reiterate what my friend Brendan Hopper said about them, which is that when work needs to be done, nature prefers colonies. Nature builds ant colonies, Brendan says, while Claude Code is “the world’s biggest fuckin’ ant.” It will bite you in half and take all your resources. Everyone is focused on making their ant run longer, perform more, and do bigger things. Making the super-worker. The super-ant. It’s like all the black and white 1950s horror movies I watched as a kid in the 1970s.


And it’s great, because a colony of huge ants is going to really kick ass. Nothing wrong with big ants, yeah? I don’t mind at all that coding agents are getting better. I appreciate it, and in fact, Icounton it. Gas Town really needs another model upgrade or two before it’s firing on all cylinders. I saw itappreciablyimprove when Opus 4.5 came out. I already had Python Gas Town and it was a struggle, but Opus 4.5 made it super smooth, overnight. So I know it’s just gonna keep getting smoother as the ants get bigger.


But colonies are going to win. Factories are going to win. Automation is going to win. Of course they’re gonna fucking win. Anyone who thinks otherwise is, well, not a big fan of history, I guess.


So my prediction here is that coding agents are very soon going to shift focus to be bettercolony workers. They need to have direct, built-in support for the emerging “Orchestrator API Surface”, which is a score or more or interaction points where I had to create some shitty hack because the agents have almost no platform APIs. Why? Because none of the 30+ coding-agent vendors are thinking of their precious baby coding agent as a colony worker. They’re thinking of it as a human pair programmer. Gas Town is going to change that over the course of 2026. The focus will shift to coordinating agents.


I’m not saying we’re going to give up on curating the human/agent loop — weneedto continue improving that. But the real progress comes from colonies. The agents who get that, and embrace it, will win.


## The Future of Big Companies


I think big companies are going to be screwed. Really screwed. The form factor is starting to be wrong. It’s too many people to accomplish too little work. Have you noticed how every fuckin’ person on LinkedIn is a CEO or cofounder now? The entire world is going toexplodeinto tiny companies, which will then aggregate and re-form into larger ones… but not until we go through at least a year of churn, where small shops dramatically outperform large ones, to a degree we’ve never seen in all history.


Here’s a case study for you. I had lunch the other day with a couple ex-Amazon buddies, neither of whom I’d seen in 20 years — Ryan Snodgrass and Ajit Banerjee, who are doing a startup together in the devops/automation space. They are big Beads fans and wanted to grab lunch and chat about it. We ate at Cactus in Kirkland, always good food there. And we had a hell of a chat! Thanks for the lunch, guys!


These guys are level 8s on my developer-evolution chart from the Gas Townlaunch post. They’re pushing coding agents as hard as anyone on the planet. And they’re observing some phenomena that I didn’t see coming. This is because they are doing something that I am not:they are working as a team, whereas all my orchestrated vibe coding has been done alone.


The stories they told me… it’s all still buzzing around in my head. They are both vibe coding with agents (Claude Code and maybe a couple others), and they both lean hard into Beads, which is a workflow accelerator. It doesn’t actually matter what your agentic coding workflow is: Beads will accelerate it. They both have unlimited tokens; Ryan’s burning $60k/year or thereabouts, but is quickly pushing up into dev-salary territory. So they have been achieving the maximum speeds you can get with coding agents.


Their stories flew by, but the theme was the same: They are going so fast that other teammates can’t keep up. They have a contributor in Munich who works in PST (our timezone), and he’ll say, “I did X!” And they’ll get mad and say, “Why did you do X, where did you get that information from?” And he’ll be like, it was from 2 hours ago. And they’ll say, “2 hours ago!? That’s ancient!” It might as well have been 2 weeks ago.


Ajit and Ryan go so fast that they have these new rules emerging, like, everything you do has to be 100% transparent and announced, all the time, or else you might as well be working in a sealed concrete chamber a mile underground. Everyone has to see your work or nobody will see it. Stuff is moving by too fast.


How do you scale this up to a big company? Crikey, when Ajit & Ryan get fully spun up with Gas Town, they’re going to be at many multiples of today’s productivity. They don’tneedto scale it to a big company. Heck, theycan’tscale it to a big company. At least, nobody knows how today.


Gene Kim and I are seeing this everywhere; we talked to one big company who was getting so wrecked by the merge problem that they decided the solution was “one engineer per repo”(!) They basically gave up and punted on coordination, ceding the floor to raw single-dev velocity.


This is crazy, right? And factory coding farms like Gas Town will only accelerate and accentuate this problem. Solo unicorn? They’llallbe solo, soon. At this rate I’ll be more impressed if a 100-person startup can make a billion dollars in 2027. Genuinely impressed. How will they even communicate, with that many people doing AI work at once? I can’t wait to find out.


I’m sure we’ll solve all these problems eventually, but as of this moment, we’re at the beginning of a massive shift that’s going to plow through the industry like a tornado, flipping companies like houses.


OK, we’ve done the backstory, we’ve done the predictions. Let’s land the plane.


## Like and Subscribe and F*** Off


Ha! Just kidding, I already told you all to f*** off in the launch post, several times, so if you’re still here, you’re definitely one of the crazy ones and welcome aboard!


Plus, I don’t even think Medium has that like/subscribe stuff. Do they?


I’ve got a LOT of Gas Town content coming. Gas Town is the Big One. I’ll do videos that show you how I work with Gas Town, doing real work with it. I’ll post tips and tricks. I’ll share stuff that other people are doing with Gas Town. I’ll showcase agents that are working to become compatible Gas Town colony workers. And Gene Kim and I will continue to host hands-on workshops throughout 2026, for those of you who want a premium educational experience to jumpstart your enterprise devs in this brave new world.


Remember, you’re probably not ready for Gas Town just yet. I’ll reprise the “Evolution of Coders, 2024–2026,” from thelaunch post, as it’s already making the rounds and sparking a lot of discussion.


The post shows a spectrum of 8 levels of developer, with trust in the agent gradually increasing from zero to where it takes over your IDE, spills into the CLI, and then multiplies from there.


You need to be atleastlevel 6, and have about half of the XP needed to reach level 7, before you’ll appreciate Gas Town. If you are already very experienced with multi-agent agentic coding, outside the IDE, then I think you will immediately find Gas Town a breath of fresh air. You’ll be faster than ever, with the exact same quality output you’ve learned to demand and expect with “naked” Claude Code, or with ad-hoc orchestrators.


Level 7+ users are already reporting that Gas Town is fun. Which it is! Once it gets on a roll for you, and it starts plowing throughgiantpiles of heavily-reviewed, heavily-tested work, day after day, you’ll realize, wow. This is it. There’s no going back. We’ve arrived at factory farming code. And it’shellafun.


I’m ready to write my next two posts about Gas Town, so let’s wrap this one! I’ll throw in some original content here to get you to subscribe. AI did not write this. Trying to get AI to write stuff like this is like getting old people to clap their hands to music.


Your original content: the beginnings of a song about Gas Town.


(To the tune of, well… you know.)


LeFou:Gosh it disturbs me to see you, Gas Town, looking so hard at my jobEvery one here’d love to use you, Gas Town, you’re making our coder hearts throbThere’s no orchestration available todayWe’re wrestling with Claude Code all nightGas Town you’ve shown us the game’s pay to playOh we hope it will turn out all right…


Nooooo…Ooooone…Churns like Gas TownToken-burns like Gas TownNo one’s cloud bill at end-of-month hurts like Gas Town!For there’s no system half as autonomousIt’s got Beads, so it keeps going onYou can ask any coder who’s tried usAnd they will all tell you their savings are gone!


No one codes like Gas TownContext-loads like Gas TownNo one leaves humans out in the cold like Gas Town!(spoken) “I’m especially skillful at orchestrating!”My, what a rig, that Gas Town!


## FAQ


People have been asking some interesting questions about Gas Town already.


Q:Are we entering a pay-to-play era where garage hackers are irrelevant?


A:It’s an understandable question. Gas Town is the beginning of industrialized factory-farming of code, which feels like pay to play. It’s expensive today, and as the models improve, it will become even more expensive to push it at the frontier. However, I think garage vibe-coding is going to be alive and well starting around summer 2026. OSS models lag frontier models by about 7 months, so by summer, OSS models will be as good as October’s crop, which were “good enough” for most startup-type eng work. If you have a GPU or two, you can run them for free all night long.


Q:Does Gas Town obsolete Vibe Coding?


A:Ha! It does not. Gas Town goes the other way, and fully embraces vibe coding. People still don’t understand that we’ve been vibe coding since the Stone Age. Programming hasalwaysbeen a best-effort, we’ll-fix-shit-later endeavor. Wealwaysship with bugs. The question is, how close is it? How good are your tests? How good is your verification suite? Does it meet the customer’s needs? That’s all that matters. Today is no different from how engineering haseverbeen. From a company’s perspective, historically, the engineer has always been the black box. You ask them for stuff; it eventually arrives, broken, and then gradually you work together to fix it. Now the AI is that black box. If you want to learn the art of Vibe Coding so you can be maximally effect with coding agents and Gas Town, check out theVibe Coding bookthat I co-wrote with the legendary Gene Kim!

