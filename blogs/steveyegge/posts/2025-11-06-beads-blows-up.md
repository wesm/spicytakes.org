---
title: "Beads Blows Up"
date: 2025-11-06
url: https://steve-yegge.medium.com/beads-blows-up-a0a61bb889b4
word_count: 3822
source: medium
---

Beads Blows Up
Steve Yegge
Follow
15 min read
·
Nov 6, 2025

9

I’m overdue for a Beads update. I’ve been so busy building that I’ve been too busy for blogging!

In the past week, I’ve had so many people telling me they’re using Beads and that they love it. Even in person. I was at the super-awesome AI Tinkerers events in Seattle this week and last week, and both times there were several Beads users at the 100+ person turnouts.

So from that incredibly rigorous statistical sample, fully 3% of the world’s developers are using Beads!

Seriously, though, it is spreading. And people are indeed coming up to me to tell me they love it. The conversation always goes like this:

Them: Hey Steve, I just wanted to say, I love Beads!

Me: That’s awesome! Me too!

Both: <Awkwardly beam at each other>

Because there’s nothing else to say! Beads is so easy and natural to use that it’s like saying, “I love shoes!”

Well me too, buddy, I love shoes too. I can’t believe we didn’t have ’em before.

24 Days of Critical Bugs

So there’s good news and there’s bad news.

The good news is, 3 weeks in, Beads is shaping up to be the Right Thing. It works well for the 2025 coding agent form factor, whether you’re using Q-developer, or Gemini CLI, or Amp Free with Ads, or Claude Code, or Codex, or Cursor Agent, or Cline CLI, or any other agentic coding assistant.

All of them use markdown files for their TODOs and planning. It’s like walking long distances in socks. Beads is like putting on shoes. It’s a drop-in replacement that solves that whole footache. Beads uses lightweight, git-backed issue tracking instead of markdown files. It even puts markdown inside the issues, so it’s like wearing socks with your shoes.

And it works the way AIs like to work. If you ask them, they will talk your ear off about how much better it is.

I think I made the right choices with Beads. Not the little ones, they were all terrible. God I’m an awful designer. Beads has needed a lot of iteration to get into decent shape since I launched it. But the big decisions, the foundational architecture and assumptions I put in place early on, have been heroes.

In particular, we use Git and JSONL (one line per issue), with a SQLite database, acting as a fast queryable cache layer, which hydrates on demand from the JSONL. That has been the Beads architecture from Day One. It hasn’t had to change, and at this point it does not look like it will need to. It’s practical magic. Beads feels like there is a central managed server, but there isn’t one. It’s just Git with some hooks and auto-syncing logic.

That core design, folks, makes up for a lot of Beads implementation deficiencies. The AI agents can fix stuff whenever it breaks, because (a) it’s easy to query stuff with the database, and (b) it’s easy to repair stuff with git. So it’s very rare to lose work in Beads, about as rare as losing code in Git.

As a result, Beads is moving really, really fast. That’s what happens when you find the Right Thing. People pounce on it and start helping make it better. And boyo, is it getting better fast. People submit high-quality PRs every day, and high-quality bug reports as well. We’ve had twenty-seven people merge PRs into Beads so far, which is also how many days old it is.

Beads is developing a raft of features while managing to keep its vision and mission tiny. As just one example, the command palette for the agents is growing rich, allowing them to sling Beads around like lightning bolts as they work. In the early days (a week ago) they had to do a lot of manual grubbing through issue records with jquery and SQL. But now they do it all with Beads commands via MCP.

So that’s the good news. I got the core design right, my contributors have helped me get the implementation and next-level design right, and it’s all growing so quickly that I can barely stay on top of it even with three full-time agents allocated.

The bad news is, Beads has remained very, very buggy. Like, I am appalled and embarrassed, and I work 10 hours a day on keeping up with the reports (thankfully most of which I encounter first.) I’ve probably fixed half a dozen major, heart-attack, show-stopper, oh-god-are-users-seeing-this type bugs every single day for the past 3 weeks. No exaggeration; it’s all there in the changelog for everyone to laugh at.

Most of the bugs spring from the design — yeah, the design I just claimed was good. It is, but it’s also fiddly. It’s not a centralized database, but it tries to act like one transparently, using git hooks, daemons, and intelligent multidirectional syncing between the database, the JSONL file, and the git repo. That has led to a lot of broken edge cases, such as issues getting resurrected after deletion, or even issues getting deleted or overwritten. Ouch!

Fortunately, on the heels of the bad news comes more good news, which is that your issues really are all in Git–even if you delete them from Beads–and the AI can always repair things when they go south.

I think this is why Beads has continued to spread even though it hasn’t really been ready for prime-time. Vibe coders are already used to things going wonky every 5 minutes and asking the agent to fix them up. To experienced vibe coders, Beads is just more of the same.

Abusing Beads

Beads was designed to be small, but people are pushing it hard. I can tell that any day now, I’m going to get a GitHub Discussion issue filed that says:

Dear Sir or Madam,

I am the CTO/Cofounder of TeleRoboCall International, responsible for millions of live AI customer service calls around the world. After a rigorous evaluation and bidding process, we have selected Beads as our regional data storage layer and content distribution network cache.

We are encountering some scaling issues in production and would earnestly request to schedule a call with you at your earliest convenience.

Right? I mean, I’m almost shocked at how people skimmed my post, in which I clearly stated that I had pooped out Beads in four or five days of feverish coding and then launched it without so much as half a day of testing. And then they tossed my post right in the garbage can and wired Beads straight up to multi-agent workflows and multi-person teams. Yikes!

Fortunately, as of v0.22.0, today, we have much better support overall for both multi-human and multi-agent workflows. Like, you can now keep your Beads issues in a separate repo, so you can protect your branches and still let the planning flow freely. We also have support for local-only contributor workflows with their own private beads, with the ability to promote issues for consideration by the maintainers. And we (I and our growing team of contributors) have fixed a ton of bugs in syncing between workers.

So, long story short, it’s probably OK to try with your multi-worker workflows now, as long as you’re not abusing it too hard.

Highlights and Lowlights

We’ve come pretty far in the past three weeks!

Beads works in Copilot CodeSpaces now, I tested it myself
Beads works really super well in Amp Free with Ads, which you should seriously try
It’s installable as an npm package (@beads)
You can brew install Beads on Mac
The beads-mcp server is on PyPI and can be used anywhere
It works on most operating systems and distros, and with any agent
Beads works in Claude Code for Web and Claude Code Marketplace
People have it running on a lot of bespoke setups, including Windows

One of my favorite highlights has been how far Beads has reached— it’s safe to say that you can use it in almost every situation where you can use a coding agent.

I’m not sure if it’s a highlight or a lowlight, but — not only have I never once looked at the Beads code base, I don’t even look at the code while I’m generating it. I would not recognize Beads code if it bit me in the ass. Beads itself bites me in the ass so much I have to code standing up, but I do recognize it as it’s biting me. I’m like, hey Beads, ouch, ouch.

Beads code, though? Never seen it before. Whose code is that biting my ass?

Beads is 100% vibe coded. This is of course why I have had to fix half a dozen critical bugs per day for 3 solid weeks. But it’s also how Beads went from a rough back-of-envelope idea, to what seems to be viral adoption, in under a month. Beads simply would not have existed without vibe coding.

Go vs. TypeScript: AI Showdown

Ah, just I thought of another highlight: The Go language.

I don’t know Go and have never done anything in it before. I sure do like it now, though! Wow. Compared to other languages I’ve seen agents using, Go is almost brutally simple. It’s so easy to see what’s going on, what the agent is doing. You can just glance at it. I love it. I don’t have to think.

With TypeScript, the agents will make sixteen slightly different copies of the same interface, re-export the symbols from five different files through a barrel export, and then call some monstrous Partial<Omit<AsyncCallback<T>>> wrapper factory to massage the type into submission without offending the compiler.

In Go, you just loop, and call functions, and print stuff, and make if/else decisions. Maybe spin off a goroutine now and then. It’s so nice.

Oddly, my Go code is also accreting at a much slower pace than TypeScript did during my September experiment. I would have thought it would be the exact opposite. I have no theories whatsoever. But in my experience so far, Go has the surprising property of being malleable. You can, more often than not, make big changes to the system with small changes to the code.

It honestly doesn’t look super malleable to me, though all I’ve done is the Go tutorials online and read a couple books. It doesn’t jump out as a language where can achieve sub-linear code base growth with linear feature growth, as you can in some dynamic languages, and most famously Lisp.

Despite appearances, my Go code base is growing far more slowly than the TS code bases I’ve been working on, which grow like weeds. (I’m working on another one now, a React app, same deal, it grows too fast.) The only thing that grows like weeds in Go is test code. It’s undoubtedly awkward. Go really isn’t expressive enough here, and TypeScript makes testing an order of magnitude easier.

Get Steve Yegge’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

But on the balance, I feel like the winner for vibe coding is Go. AIs cannot seem to stop themselves from writing dodgy TypeScript, whereas it doesn’t seem possible to write bad Go code. The worst it ever gets is mediocre.

I still think TypeScript is an incredibly elegant achievement and I don’t mean to be dismissive of it. I have fond memories of liking it. But after my AIs pooped out 350,000 lines of TypeScript in 30 days, I found that, like snow when I had to live in Idaho for a year, I just don’t like that much of it.

As for lowlights, honestly, the whole last three weeks of madly chasing stability, 1500 commits in, with probably seven major rearchitectures completed — the whole implementation has been a lowlight. I have just wanted it to work, and I have been holding off this blog post until I felt it was stable enough.

But I think we’ve reached a good spot. All of the critical flaws people have identified have been addressed now, as of v0.22.0. We have bug fixes, new features, and/or workarounds for all of them. I’m hopeful that the nature of the bugs will start changing now, from architectural problems (like having to change our issue ID scheme) to minor implementation issues. We’ll see!

Sure, there will still be bugs every day, and likely releases every day for a while too. But I am now satisfied that our architectural puzzle is complete, with all the pieces in place. From here out, the bugs should just be bugs.

Can I Use Beads Yet?

I know a lot of you have had your eye on Beads, and have wisely chosen not to be early adopters. So when is the time to try it?

Answer: Do you vibe code with agents every day? Have you stopped writing code by hand? Then yes! You should try Beads.

If your answer to either question above was No, then my advice is: stop writing code by hand, vibe code with agents every day, and then try Beads.

I’d say it’s still early adopter territory, though. Alpha quality. If you want to wait until it’s truly stable, wait for the 1.0.0 release. It could be weeks away or months away, hard to say, but until the bug rate slows down, it could be a while.

Last, I should mention that although Beads is a drop-in memory bank, it is not an invisible drop-in. It changes the way you work, a little bit. You now have issue numbers like bd-7cz to refer to every single bit of work you ever want the LLM to do. Which is amazing. But you do have to use them.

Beads is a leaky abstraction, and it will remain that way. What I mean by that is, you have to know you’re using Beads. You don’t normally use Beads yourself, mind you — you ask your agent to use it. But you still have to talk about it during your agent conversations, telling it which issue to work on.

It would be great if the frontier models were trained on Beads, and the agents were all prompted to use it instead of TodoWrite. But they don’t, and they aren’t, so it’s on you to fill the gap.

Here are a few examples of where you have to incorporate Beads into your workflow consciously:

After creating a design doc, you must ask the agent to file Beads epics and issues for it. (But then you can start every session for those epics with, “What’s next?”)
While the agent is working, you will sometimes need to nudge it to file issues it discovers. (Often it does it automatically, but not always.)
At the end of every session there is hygiene to perform; I call it Landing the Plane.

The latter example is a new technique I came up with today, and I’m over the moon about it. This is a generally applicable technique even if you don’t use Beads.

Landing the Plane

Agents often misrepresent the current state of affairs when they’re getting ready to finish up, especially when they’re low on context and they don’t want to explore much. They will tell you that the steak dinner’s ready for your guests, when there’s still a dead cow in the living room.

When you use Beads, there is an extra hygiene step required at the end of every agent session. It’s supposed to be automatic, but Beads has been so buggy that a gnat farting in your neighbor’s attic is enough to make the imports or exports fail. You have to take some of your time, to tell the agent to spend some of its time, to sync Beads issues from other workers.

As it happens, when you’re vibe coding, there are lots of other hygiene steps involved at the end of a session. These have nothing to do with Beads. Off the top of my head, here are a few I ask for almost every time, and specific projects have their own custom session-cleanup steps as well:

Make sure tests and other quality gates pass
Remove debugging code and temp artifacts
Check for leftover git stashes
Check for unmerged git branches
Update and close GH and Beads
Update documentation
Perform git operations
Deal with untracked files and edge cases
Choose work and create a prompt for next session

Gene Kim and I cover this kind of hygiene in our book, Vibe Coding, which is out now and available on Amazon. We talk about it extensively in our coverage in Part 3 of the developer Inner, Middle and Outer loops.

Anyway, I got so tired of typing all this hygiene stuff out every session that I told an agent, “I want to be able to tell you, ‘land the plane’, and have all this stuff happen.” It generated detailed instructions in my AGENTS.md, and now, when I’m ready to shut an agent down and push its work, I just tell it to land the plane.

With this strategy, the agent grinds away through all the steps in your protocol, often for minutes. It will be far more thorough than usual, even if it’s low on context. It gets everything spotless, pushes, and then searches your project’s Beads for the next thing to work on. It finishes by creating a tailored prompt for you to hand off to the next agent. And then you can add in custom plane-landing steps for each individual project.

This simple prompting exercise, combined with Beads, turns vibe coding into an experience so addictive that you will literally pee yourself, like a Vegas regular at the blackjack tables.

The Dark Side of Beads

Let me offer one small consideration as to why you might not want to use Beads: It can cause you to lose control of your bodily functions.

I’ve been playing guitar for forty years, pretty decent at it actually, and I’ve noticed a new quirk lately. I’ll be practicing a super tough piece of music, and really hitting everything right, and start thinking to myself, “Wow, I’ve finally nailed it! This is incredible!” And then, right at the musical climax, when I’m completely lost in the zone, an enormous blob of spittle falls out of my mouth and splashes all over my guitar and my lap, bluuuuuhhh. This is why I am not famous like Taylor Swift.

Gene and I have written plenty about how addictive vibe coding is. It’s like being a dog and sticking your head out the car window. All the smells from coding, good and bad, come flying by incredibly fast. It’s already a blast.

Well, Beads makes it stupidly addictive. The problem is that Beads eliminates nearly all the friction in the handoff between sessions. So your agents work for longer, and you tend to fire up more of them. It’s easier to keep more agents in the air with Beads, because it keeps them on track. It’s like adderall for them. And it’s like crack for you.

Look, don’t get me wrong. Working with coding agents is incredibly frustrating at times. Not a day goes by where I’m not ranting at one of them, about to have a heart attack.

I’ll say, “No, no, NO, for the last time, it’s 91 issues, not 318, I swear this conversation sucks so hard I feel like I’m talking to a jet engine.” And then I’ll think, “Gosh, who says LLMs stifle creativity? My insults have been on point lately.” And then I think, “Remember in The Terminator (1984) when SkyNet read all my Claude logs and sent a robot back to kill me?”

You’ve all been there, I’m sure.

But being able to sit down and say, “What’s next up?” to your agent, and never have it forget or disclaim any work — that’s paradise. It drags you inexorably towards juggling as many agents as you can without peeing yourself.

Sometimes it might just be a couple of agents, or even one. Sometimes it might be four or five or more. But no matter what you’re doing, you’ll start more agents up, until you reach a point where there is always one waiting to give you some dopamine or adrenaline. And then you’re stuck.

You’ll be standing there in front of your ultrawide monitor, slinging agents like Tom Cruise in Minority Report, and you’ll be thinking, “I’m in the zone!” You’ll be at the top of your game, focused like never before, having the time of your life. And right then, a huge glop of drool will land in your lap. I’m just sayin’, it’s a real risk.

Press enter or click to view image in full size
ChatGPT refused to make this vibe coder wet his pants

So be careful, folks. Using Beads can really mess with those glands and smooth muscles. Wear a bib!

Time to Try Beads

I’m super pleased that Beads has been gaining popularity, and making people more productive. I’m also overjoyed about the emerging contributor community. They all get the vision deeply and they have been incredibly thoughtful in helping it mature.

Special recognition to Ryan Newton for a ton of contributions, to Dan Shapiro for native Windows support, and to 
Artyom Kazak
 for a beautiful semantic beads-merge module that elegantly solved the tombstoning issue. I am deeply grateful to everyone who has submitted PRs, as well as thoughtful discussion issues and bug reports. A few people have even asked innocent questions that wound up triggering large architectural changes!

I’m excited that Beads is being ported to so many different environments and workflows. It’s proving itself to be pretty flexible. Scalable? Probably not very… but then, it’s not meant to be Jira. Beads is meant to be the working memory for your active agents. Nothing more nor less.

Finished issues and future issues don’t really belong in Beads — it’s best to keep them in a separate store. I find GH Issues is good for the Future stuff. And for Finished — just deleting old closed issues periodically keeps your beads database sprightly and tractable. They’ll stay in Git forever.

I’ve been accumulating a big list of Beads Best Practices and I’ll post it soon, probably on the GH Discussions. In the meantime, try Beads out and let me know what you think!

If you want to know more about vibe coding–especially if you haven’t ever tried it, or maybe you haven’t even coded for years–then I heartily recommend our book, Vibe Coding, which I co-wrote with bestselling author and researcher, my buddy 
Gene Kim
. Our book will help you get the most out of your coding agents, and I’m pretty proud of it. Take a look!

Press enter or click to view image in full size
Vibe Coding, by Gene Kim and Steve Yegge
