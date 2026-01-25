---
title: "Beads for Blobfish"
date: 2025-10-22
url: https://steve-yegge.medium.com/beads-for-blobfish-80c7a2977ffa
word_count: 2629
source: medium
---


# Beads for Blobfish


--


Listen


Share


Here’s why you should take 3 minutes and tryBeadswith your coding agent.


First, let’s all agree to agree:you should be using an autonomous, command-line coding agent. It’s October 2025. It’s time to put that IDE away. It is a crutch. You could use it in a prop for a Soon-To-Be-Unemployed Programmer costume for Halloween.


If you want the absolute best programming experience today, no compromises, your choices are (a) Claude Code, which is amazing and also straight up expensive, and (b)Sourcegraph Amp, which is equally amazing (I use it 12–14 hours a day) and it is alsofree with ads. Amp has the same great model, no cheaping out like you’ve seen in free tiers of some other coding agents.


You can get a LOT done on “free with ads.”


So. We’re in agreement, yeah? You are now Informed. No more excuses. Coding agents. The agentic, terminal-based, autonomous kind. If you’re not using them then you are the programming equivalent of a sad blobfish.


However, at least until Beads came out, the coding agent frontier has had some pretty rough camping.


## 10 Minute Lifetimes


For starters, if you are one of the early adopters pushing your coding agents hard, then you know their attention span is woefully brief.


Even with a 1M context window, coding agents can only get a usable 10–15% out of that before their cost and performance both go the wrong direction. Most agents cut you off hard at around 20%, and it’s best to stay below 15% before restarting your session.


Working at full speed, this means you get 5–10 minutes of work before they poop out and need a restart (which is like death) or compaction (which is a mind wipe). It sucks. You make Tyler Durden-style single-serving friends with them, and ten minutes later, they’re gone.


If you want any continuity at all, then it is a critical necessity for your coding agents towrite down what they know before they die.


So they do! And since I run around 50+ sessions a day, this has resulted in the creation of a Great Pacific Garbage Patch of Markdown files, right here on my hard disk.


## The Global Markdown Crisis


In order to understand why Beads improves things, first we must understand how coding agents do their planning today.


Coding agents use Markdown files for managing their TODO lists. These are the agent’s working memory. They are all that your agent can “remember” from session to session.


These TODO-like plans are so important that coding agents get access to a dedicated function calledTodoWriteortodo_write. This, unfortunately, only encourages them to use it all the time.


I’ve been using coding agents all year, and I’ll let you in on a little secret: they are TERRIBLE at managing Markdown plans.


Seriously, have you not noticed this already? They will create one at the drop of a hat named something vague likephase-6-design-review.mdand drop it in any old place in your project tree.


Where, you ask? Many of them just plop it right into the root directory, where before long your GitHub project landing page will look like it was visited by a Plan Emitter with severe gastrointestinal issues.


But I’ve found they also like to bury them deep in some path that will quietly accumulate fifteen thousand.mdfiles, all named stuff likeprofile-results-writeup-16.md, until your antivirus software finally blows a gasket, and you get a bunch of alerts from your OS saying the North Koreans finally got in, when all along it was just your coding agent with full-blown dementia because it is lost in a sea of Markdown files.


If this hasn’t happened to you yet, then you aren’t using coding agents very heavily.


The Markdown approach works just fine under light usage.That’s probably why you haven’t noticed a problem. Yet.


Once you start vibe coding a program larger than a one-shottable 10k-20k lines, though, the plan load starts to unravel the agent’s very mind. As their haphazard records begin to accumulate, fall out of date, and contradict one another, your agents descend from mere amnesia into complete schizophrenia.


## Super Baby


Curious family members have asked me about theVibe Codingbook I co-wrote with the legendaryGene Kim, which comes out in a few days. What is vibe coding exactly, they ask?


I explained vibe coding using the Super Baby story, and it seemed to resonate.


You start by pulling a fresh new AI agent clone off the shelf. It is a baby, and it cries, “Waaaaaah! Where am I? Who are you?” You spend some time explaining what you would like it to do.


It learns fast, but ages to 10 years old in the process. It now understands your general problem, now two minutes into the session.


The kid says, “I’m going to research solutions.” It does a few greps, reads some code and some docs, and four minutes in, it’s 18 years old and has learned everything it needs to start working. It declares, eyes seeing into forty dimensions at once, I UNDERSTAND NOW. I CAN HELP YOU.


The agent begins sprinting, feet pounding, aging visibly into its thirties as it runs, sitting at 7% context usage six minutes in. It is powering through problems that would take a pair of smart humans hours to days. In a few minutes, it has moved a small mountain for you. By now it sees all, knows all.


It’s working fast. But it is aging faster. At 15% context, ten minutes in, it’s 85 years old. Nearly exhausted, but at one with the universe, it cries, “I don’t have much longer. Let me record the vast knowledge that I have acquired, and the many feats I have accomplished, into fifty beautiful new markdown files for you, filled with glorious emojis…”


<inferences for 30 seconds…>


“Aaaaah!”<dies>


Next!


You pull a fresh clone baby off the shelf. “Waaaaaah!” It cries. “Who are you? Where am I?”


Butthistime, you are prepared. You reply, “Let’s go look at the Markdown trail you left for yourself. I told you take good notes right before we restarted. You said it would be no problem.”


The baby agent crawls off for five minutes, churning through Markdown plans. Your computer fan comes on.


The agent finally returns in its school uniform, declaring, “Perfect! I’m ready to work on some shit you abandoned 2 weeks ago and told me to delete all traces of!”


Right? Tell me this hasn’t happened to you.


## Matt Beane Redpills Beads


Super Baby is a 100% true real-life drama, unfolding all around you. This cycle is EXACTLY how they work. You can get an absolute miraculous crap-ton done with coding agents, but it’s Benjamin Button, backwards, every ten minutes. And everything comes down to that context handoff.


Markdown isn’t cutting it.


I’m not going into a lot of detail about Beads here. If you’d like more information as to what, how, and why Beads, I heartily recommend being unspeakably lazy. Just tell your agent to go research Beads (github.com/steveyegge/beads). Ask it how Beads compares to your current approach for working together.


Dollars to donuts, your agent willvastlyprefer Beads, and will offer to just install it for you and start using it.


The reason for this preference is agentsgetBeads, the instant they see it. Beads works the way they want to work. Agentsliketo track things. Theyliketo set priorities, and to stay organized, because it helps them manage their limited time and space. They like having good tools for discovery, for forensics, and for tracking the provenance of ideas.


We haven’t been giving them good tools for any of this in 2025.


## Beane Redpills Beads


My buddy Dr. Matt Beane tried exactly what I am recommending. He asked his coding agent about Beads, and it promptly talked him (almost bullied him!) into trying it. Just read it! Here is the short and memorable transcript:


> (Matt) grok this and tell me implications for my work with you.https://github.com/steveyegge/beads


⏺ Fetch(https://github.com/steveyegge/beads)⎿ Received 581KB (200 OK)


⏺Implications for Your Work With Me


Beads addresses exactly what we’ve been doing manually withTodoWrite:


What We’re Already Doing (Aligned with Beads Philosophy)


1.Task tracking across sessions—TodoWritemaintains state2.Dependency management— We mark tasks asin_progress/completedsequentially3.Work discovery— Adding new tasks as we uncover them (e.g., IRB compliance issue emerged mid-work)4.Persistent memory—TODO.mdsurvives session context limits


Where Beads Could Improve Our Workflow


1.Long-Horizon Task Memory


Current limitation: When context resets, I rely on session summaries +TODO.mdBeads: Git-committed JSONL gives me persistent, queryable memory of:— What was discovered during each task— Why decisions were made— What’s blocking what


Example: Today’s work generated subtasks (anonymization→IRB compliance→force push). Beads would auto-track these dependencies.


2.Automatic Work Discovery


Current: You tell me “on to the interviews” and I create todos manuallyBeads: I could automatically create linked issues as I discover new work:—Reading interviews→ discoversneed anonymization→ creates issue—Anonymization→ discoversneed to verify GitHub doesn’t have PII→ creates issue


3.Ready Work Detection


Current: I manually check what’s unblockedBeads: Automatically surfacesreadytasks based on dependency resolution


Example:Share with teamwas blocked byanonymize data→ once anonymized, it becomes ready automatically


4.Cross-Session Context


Biggest win: When you resume work tomorrow, I could query Beads to see:— What was completed today (with full context)— What was discovered but deferred— What’s ready to work on next


Practical Next Steps(Note from Steve: This is the bullying part!)


Option 1:Adopt Beads for our work— Install Beads in your knowledge-work repo— MigrateTodoWriteworkflow to Beads issues— I gain queryable memory across sessions


Option 2:Enhance TodoWrite with Beads principles— Add dependency tracking toTODO.md— Auto-discover subtasks during work— Flag “ready” vs. “blocked” tasks explicitly


Would you like to try integrating Beads into our workflow?It’s especially valuable for long-running projects like SkillBench research where tasks span multiple days and have complex dependencies.


> (Matt) option 1. red pill. lfg


<a few minutes later…>


⏺ ✅ Beads Integration Complete!


What we accomplished:


1. ✅ Installed Beads (v0.9.2via Go)2. ✅ Initialized database (.beads/kw.db)(kw for “knowledge-work”)3. ✅ Migrated 6 TODO items to Beads issues with proper prioritization and labels4. ✅ Tested dependency tracking (blocks, discovered-from relationships work)5. ✅ Verified ready work detection (automatically surfaces unblocked tasks)6. ✅ Created helper script (bd-helper.shfor easy access)7. ✅ Committed to git (database is now version-controlled)


How this transforms our workflow:


Before (TodoWrite only):


- I lose context between sessions— No dependency tracking— Manual task discovery— Limited query capability


Now (Beads):


# I can query what’s ready to work onbd ready


# Show blocked workbd blocked


# Create tasks with dependencies as I discover thembd create“New subtask” — deps “discovered-from:kw-3”


# Show full context on any issuebd showkw-5


Next time you resume:I can query Beads to see exactly where we left off, what was discovered during work, and what’s ready to tackle next — even after context resets.


🎺 You just gave me a memory upgrade!


Come ON, this is amazing, right? Matt’s agent pulled the trumpet out, for crying out loud. How can you not? 🎺🎺🎺


## Beads is an Agent Memory Upgrade


Why wouldn’t you want a memory upgrade for your agents that die every 10 minutes? There’s almost nothing to learn. Just embrace Beads in your existing workflow. The AI will do all the heavy lifting for you.


For every new feature, just ask your agent to create a plan/design, like you always do. But then, have it create a tracking epic with child issues. Your agent will happily stuff all the work into Beads. Or, you can import all the work from your existing pile of crap. You have options!


And then, for the next several days, you can start every agent session with “What’s next?”


There isnothingmore satisfying, I tell you. It keeps me glued to my computer, worse than ever before. It keeps the addictive momentum going oh so much smoother. ly. Smootherly.


Agentic vibe coding feels so muchdifferentthan it did just a month ago.


You pull a fresh clone off the shelf. The baby wakes up and cries, “Waaaaaah!” It then notices the video cassette player you put in for it, with a tape that reads: “Watch Me.” In nine seconds, baby agent reads the onboarding instructions inAGENTS.md, teaching it to use Beads instead of Markdown.


It is now four months old, still just a wee bairn.


But now you can say to it, “What’s next?”


From now on, your agent will come up to speed so fast, it will be seeing into the 40th dimension by the time it’s 3 or 4 years old. Then, ten minutes later, having moved a much larger mountain for you, the old agent will create epics and tracking issues, with dependencies and details, for anything it couldn’t get to in life. And then it will swan-dive gracefully into your Ctrl-C.


Oh no, wait! You forgot to tell it to clean up, commit, and push your changes! But you killed it! Argh!


Fortunately, because you are using Amp, you simply copy/paste the Amp thread ID back into the shell, and your session is instantly resurrected:


amp threads continue T-f6d324a9-a324–4cf8–7962–7391602c8c91


Whew! Disaster averted. Your agent is resurrected from the dead.


Wait, you weren’t using Claude Code, were you? Because it doesn’t havethreads. It justdies, all your session, lost. Poof. You will have to start a fresh baby agent clone and explain stuffagainjust to get it to finish the work. I tell you, Imuchprefer Amp and its restartable threads.


Both fine products, though, and way better than whatever you’re using, blobbo.


Either way, now you can tell your agent to go clean up, commit and push. It’s finally time to shut that session down for good. You come up behind it while it’s working, and ask it to tell you again about the rabbits, one last time.


And that’s it! That’s all there is to using Beads. It’s just like your regular agent sessions, except now they always know what to do next.


So think on it. Give it a wee tink.


Next time you find yourself having to type a bunch of stuff into your agent, blah blah blah, type type type, blah blah BLAH BLAH BLAH, and you’re thinking, “Gosh I need SuperWhisper because I blah blah blah blah blah so much that my fingers are blah blah blah”, remember:


You could have just typed, “What’s next?”


## Epilogue, Caveats, and Disclaimers


Beads is different from anything else out there. It’s shaping itself to a new space, one where AI agents are most comfortable and productive. Which is different from how humans like to work. Beads is making design and architecture decisions that are almost the opposite of what most traditional issue trackers and planners make.


But you would sort of expect that, if you think about it. We need to build tools for agents now.


It’s early days. We are still working through Beads issues with multi-repo and multi-worker support. It’s best for simple projects for now, unless you want to be a bleeding adopter and help improve it.


My advice: Don’t use beads for anything important until we release 1.0.0. That should not be long. It’s moving fast. We have tons of community contributions flooding in. Beads is undergoing rapid development as it evolves into a true agentic memory.


Butdogo try it! It’s fantastic for single-player workflows. It’s 100% safe. All your issues are tracked in git, so you never truly lose anything even if some cache gets stale or whatever. Your AI will always figure it out and repair it.


Enjoy your newfound superpowers!


And if you want to learn more about how to keep your agent on the railsduringyour sessions (not just at the transitions, where Beads shines), check out our book, Vibe Coding, which is finally out!


And for God’s sake, go check outAmp Free. You’ll never have a better chance to get a high-speed jumpstart in this new agentic world.

