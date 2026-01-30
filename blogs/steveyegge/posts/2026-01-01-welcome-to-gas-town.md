---
title: "Welcome to Gas Town"
date: 2026-01-01
url: https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04?source=rss-c1ec701babb7------2
source: medium
word_count: 8607
---


Happy New Year, and Welcome to Gas Town!


![](https://cdn-images-1.medium.com/max/1024/1*ReBwrC1sc9USnhvYXcrd4A.jpeg)

*Figure 1: Welcome to Gas Town*


### **What the Heck is Gas Town?**


[Gas Town](https://github.com/steveyegge/gastown) is a new take on the IDE for 2026. Gas Town helps you with the tedium of running lots of Claude Code instances. Stuff gets lost, it’s hard to track who’s doing what, etc. Gas Town helps with all that yak shaving, and lets you focus on what your Claude Codes are working on.


For this blog post, “Claude Code” means “Claude Code and all its identical-looking competitors”, i.e. Codex, Gemini CLI, Amp, Amazon Q-developer ClI, blah blah, because that’s what they are. Clones. The industry is an embarrassing little kid’s soccer team chasing the 2025 CLI form factor of Claude Code, rather than building what’s next.


I went ahead and built what’s next. First I predicted it, back in March, in [Revenge of the Junior Developer](https://sourcegraph.com/blog/revenge-of-the-junior-developer). I predicted someone would lash the Claude Code camels together into chariots, and that is exactly what I’ve done with Gas Town. I’ve tamed them to where you can use 20–30 at once, productively, on a sustained basis.


Gas Town is opinionated — much like Kubernetes, or Temporal, both of which Gas Town resembles, at least if you squint at it until your eyes are pretty much totally shut. I’ll include comparisons to both k8s and Temporal at the end of this post. It is a little surprising how similar they are, despite having radically different underpinnings.


But the comparison should serve as a warning: Gas Town is complicated. Not because I wanted it to be, but because I had to keep adding components until it was a self-sustaining machine. And the parts that it now has, well, they look a lot like Kubernetes mated with Temporal and they had a very ugly baby together.


But it works! Gas Town solves the [MAKER problem](https://arxiv.org/abs/2511.09030) (20-disc Hanoi towers) trivially with a million-step wisp you can generate from a formula. I ran the 10-disc one last night for fun in a few minutes, just to prove a thousand steps was no issue (MAKER paper says LLMs fail after a few hundred). The 20-disc wisp would take about 30 hours. Thanks for coming to my TED Talk.


All this will make complete sense if you make it through the next 23 pages.


### **Gas Town Was No Secret**


After Revenge of the Junior Developer, I traveled around all year, loudly telling everyone exactly what needed to be built, and I mean *everyone*. I was not shy about it. I would declare, “Orchestrators are next!” And everyone would nod slowly and frown thoughtfully and say, “huh.”


I went to senior folks at companies like Temporal and Anthropic, telling them they should build an agent orchestrator, that Claude Code is just a building block, and it’s going to be all about AI workflows and “Kubernetes for agents”. I went up onstage at multiple events and described my vision for the orchestrator. I went everywhere, to everyone.


“It will be like kubernetes, but for agents,” I said.


“It will have to have multiple levels of agents supervising other agents,” I said.


“It will have a Merge Queue,” I said.


“It will orchestrate workflows,” I said.


“It will have plugins and quality gates,” I said.


I said lots of things about it, for months. But hell, we couldn’t even get people to use Claude Code, let alone think about using 10 to 20 of them at once.


So in August I started building my own orchestrator, since nobody else seemed to care. Eventually it failed, and I threw it out and started over on v2, which also failed, but we got [Beads](https://github.com/steveyegge/beads) out of it. Then v3 (Python Gas Town), which lasted a good six or eight weeks.


Gas Town (in Go) is my fourth complete, functioning orchestrator of 2025. The story of how I arrived at Gas Town is fun, but we’ll save it for another time. Unfortunately this post will be long enough (25+ pages!) just telling you the barest basics of how it works. We can do the back story later.


But first, before we get into Gas Town’s operation, I need to get rid of you real quick.


### **WARNING DANGER CAUTION**


### **GET THE F*** OUT**


### **YOU WILL DIE**


Let’s talk about *some* of the reasons you shouldn’t use Gas Town. I could think of more, but these should do.


First of all, the code base is under 3 weeks old. On a scale of “polished diamond” to “uncut rough” to “I just smuggled it 400 miles upriver in my ass,” I’m going to characterize Gas Town as “You probably don’t want to use it yet.” It needs some Lysol. It’s also 100% vibe coded. I’ve never seen the code, and I never care to, which might give you pause. ‘Course, I’ve never looked at [Beads](https://github.com/steveyegge/beads) either, and it’s 225k lines of Go code that tens of thousands of people are using every day. I just created it in October. If that makes you uncomfortable, *get out now*.


Second, you are really, seriously, not ready yet. Let’s talk about the Evolution of the Programmer in 2024–2026, pictured here by Nano Banana in Figure 2:


![](https://cdn-images-1.medium.com/max/1024/1*ArLBW-FgOdve4COI804uIQ.png)

*Figure 2: The 8 Stages of Dev Evolution To AI*


First, you should locate yourself on the chart. What stage are you in your AI-assisted coding journey?


Stage 1: **Zero or Near-Zero AI:** maybe code completions, sometimes ask Chat questions


Stage 2: **Coding agent in IDE**, permissions turned on. A narrow coding agent in a sidebar asks your permission to run tools.


Stage 3: **Agent in IDE, YOLO mode:** Trust goes up. You turn off permissions, agent gets wider.


Stage 4: **In IDE, wide agent**: Your agent gradually grows to fill the screen. Code is just for diffs.


Stage 5: **CLI, single agent. YOLO**. Diffs scroll by. You may or may not look at them.


Stage 6: **CLI, multi-agent, YOLO**. You regularly use 3 to 5 parallel instances. You are very fast.


Stage 7: **10+ agents**, **hand-managed**. You are starting to push the limits of hand-management.


Stage 8: **Building your own orchestrator**. You are on the frontier, automating your workflow.


If you’re not at *least* Stage 7, or maybe Stage 6 and very brave, then you will not be able to use Gas Town. You aren’t ready yet. Gas Town is an industrialized coding factory manned by superintelligent robot chimps, and when they feel like it, they can wreck your shit in an instant. They will wreck the other chimps, the workstations, the customers. They’ll rip your face off if you aren’t already an experienced chimp-wrangler. So no. If you have *any doubt whatsoever*, then you can’t use it.


Working effectively in Gas Town involves committing to vibe coding. Work becomes fluid, an uncountable substance that you sling around freely, like slopping shiny fish into wooden barrels at the docks. Most work gets done; some work gets lost. Fish fall out of the barrel. Some escape back to sea, or get stepped on. More fish will come. The focus is *throughput*: creation and correction at the speed of thought.


![](https://cdn-images-1.medium.com/max/1024/1*3iC6cilfUdvndZUVRELmBA.jpeg)

*Figure 3: Vibe Coding Chaos*


Work in Gas Town can be chaotic and sloppy, which is how it got its name. Some bugs get fixed 2 or 3 times, and someone has to pick the winner. Other fixes get lost. Designs go missing and need to be redone. It doesn’t matter, because you are churning forward *relentlessly* on huge, huge piles of work, which Gas Town is both generating and consuming. You might not be 100% efficient, but you are *flying*.


In Gas Town, you let Claude Code do its thing. You are a Product Manager, and Gas Town is an Idea Compiler. You just make up features, design them, file the implementation plans, and then sling the work around to your polecats and crew. Opus 4.5 can handle any reasonably sized task, so your job is to make tasks for it. That’s it.


That, and you have to help keep Gas Town running. It runs itself pretty well most of the time, but stuff goes wrong often. It can take a lot of elbow grease from you and the workers to keep it running smoothly. It’s very much a hands-on-the-wheel orchestration system.


If you can’t work like that, then what in God’s name are you still doing here? Go back to your IDE and shelter in place. Gas Town is not safe for you.


Gas Town is also expensive as hell. You won’t like Gas Town if you ever have to think, even for a moment, about where money comes from. I had to get my second Claude Code account, finally; they don’t let you siphon unlimited dollars from a single account, so you need multiple emails and siphons, it’s all very silly. My calculations show that now that Gas Town has finally achieved liftoff, I will need a third Claude Code account by the end of next week. It is a cash guzzler.


Gas Town uses tmux as its primary UI. I had to learn tmux. It was easier than I thought it would be, and way more useful. 3 weeks in, and I love tmux. You will have to learn a bit of tmux. Or, you can wait until someone writes a better UI for Gas Town. Better UIs will come. But tmux is what you have for now. And it’s worth learning.


![](https://cdn-images-1.medium.com/max/1024/1*hpoPpTPIuHu993KlRyFMjw.png)

*Figure 4: Mayor tmux status line*


Like it or not, Gas Town is built on Beads. It is in fact the sequel to Beads: my Empire Strikes Back to Beads’ Star Wars. There is no “alternate backend” for Gas Town. Beads is the Universal Git-Backed data plane (and control plane, it turns out) for everything that happens in Gas Town. You have to use Beads to use Gas Town.


You might not like Beads. If you think Beads is overly-opinionated, you’re in for a ride. Gas Town is me marching into the Church of Public Opinion on AI-Assisted Coding, lifting my leg, and ripping a fart that will be smelt all around the world.


Many of you may gag at my brand. But I suspect a few of you will like becoming *superheroes* enough that you’re willing to look past Gas Town’s quirks, and see it my way. This is how work should be done. It’s the best way already, and it will get better.


Gas Town is designed to scale up in three dimensions this year with (1) model cognition, (2) agents becoming more Gas Town-friendly, and (3) Gas Town and Beads making it into the training corpus for frontier models. Even without all that, it’s already shocking that the agents use Beads and Gas Town so effortlessly. With zero training.


But right now? It’s like a late 1800s factory with machines that can disembowel you if you’re not careful.


OK! That was like half a dozen great reasons not to use Gas Town. If I haven’t got rid of you yet, then I guess you’re one of the crazy ones. Hang on. This will be a long and complex ride. I’ve tried to go super top-down and simplify as much as I can, but it’s a bit of a textbook.


I’m sorry. But in my defense, Gas Town is hella fun. Best thing I’ve ever made.


Let’s dive in.


**Gas Town 101**


![](https://cdn-images-1.medium.com/max/1024/1*85xoVIP4w_jiDlDgdYch_A.jpeg)

*Figure 5: Gas Town’s Worker Roles*


Gas Town workers are regular coding agents, each prompted to play one of seven well-defined worker roles. There are some other key concepts I’ll briefly introduce, along with the roles, like Towns and Rigs.


One thing to know up front about Gas Town: it degrades gracefully. Every worker can do their job independently, or in little groups, and at any time you can choose which parts of Gas Town you want running. It even works in no “no-tmux” mode, and limps along using naked Claude Code sessions without real-time messages. It’s a little slower, but it still works.


The seven Gas Town roles all work together to help keep Gas Town running. And it needs your help sometimes, too; Gas Town runs on equal parts guzzoline and elbow grease.


Here are the key players and concepts:


**🏙️The Town:** This is your HQ. Mine is ~/gt, and all my project rigs go beneath it: gastown, beads, wyvern, efrit, etc.. The town (Go binary gt) manages and orchestrates all the workers across all your rigs. You keep it in a separate repo, mostly for the configuration.


**🏗️Rigs**: Each project (git repo) you put under Gas Town management is called a Rig. Some roles (Witness, Polecats, Refinery, Crew) are per-rig, while others (Mayor, Deacon, Dogs) are town-level roles. gt rig add and related commands manage your rig within the Gas Town harness. Rigs are easy to add and remove.


**👤The Overseer**: That’s you, Human. The eighth role. I gave you some eye paint in the picture. As the Overseer, you have an identity in the system, and your own inbox, and you can send and receive town mail. You’re the boss, the head honcho, the big cheese.


**🎩The Mayor**: This is the main agent you talk to most of the time. It’s your concierge and chief-of-staff. But if the Mayor is busy, all the other workers are also Claude Code, so they are all very smart and helpful. The Mayor typically kicks off most of your work convoys, and receives notifications when they finish.


**😺Polecats**: Gas Town is a work-swarming engine. Polecats are ephemeral per-rig workers that spin up on demand. Polecats work, often in swarms, to produce Merge Requests (MRs), then hand them off to the Merge Queue (MQ). After the merge they are fully decommissioned, though their names are recycled.


**🏭Refinery**: As soon as you start swarming workers, you run into the Merge Queue (MQ) problem. Your workers get into a monkey knife fight over rebasing/merging and it can get ugly. The baseline can change so much during a swarm that the final workers getting merged are trying to merge against an unrecognizable new head. They may need to completely reimagine their changes and reimplement them. This is the job of the Refinery: the engineer agent responsible for intelligently merging all changes, one at a time, to main. No work can be lost, though it is allowed to escalate.


**🦉The Witness:** Once you spin up enough polecats, you realize you need an agent just to watch over them and help them get un-stuck. Gas Town’s propulsion (GUPP) is effective, but still a bit flaky right now, and sometimes you will need to go hustle the polecats to get their MRs submitted, and then hustle the Refinery to deal with them. The Witness patrol helps smooth this out so it’s almost perfect for most runs.


**🐺The Deacon**: The deacon is the daemon beacon. It’s named for a Dennis Hopper character from Waterworld that was *inspired* by the character Lord Humungus in the Mad Max universe, making it a crossover. The Deacon is a Patrol Agent: it runs a “patrol” (a well-defined workflow) in a loop. Gas Town has a daemon that pings the Deacon every couple minutes and says, “Do your job.” The Deacon intelligently propagates this DYFJ signal downward to the other town workers, ensuring Gas Town stays working.


**🐶Dogs**: Inspired by Mick Herron’s MI5 “Dogs”, this is the Deacon’s personal crew. Unlike polecats, Dogs are town-level workers. They do things like maintenance (cleaning up stale branches, etc.) and occasional handyman work for the Deacon, such as running plugins. The Deacon’s patrol got so overloaded with responsibilities that it needed helpers, so I added the Dogs. This keeps the Deacon focused completing on its patrol, rather than getting bogged down and stuck on one of the steps. The Deacon slings work to the Dogs and they handle the grungy details.


**🐕Boot the Dog**: There is a special Dog named Boot who is awakened every 5 minutes by the daemon, just to check on the Deacon. That’s its only job. Boot exists because the daemon kept interrupting the Deacon with annoying heartbeats and pep talks, so now the dog gets to hear it. Boot decides if the Deacon needs a heartbeat, a nudge, a restart, or simply to be left alone, then goes back to sleep.


**👷The Crew**: The Crew, despite being last in the list, are the agents you’ll personally use the most, after the Mayor. The crew are per-Rig coding agents who work for the Overseer (you), and are not managed by the Witness. You choose their names and they have long-lived identities. You can spin up as many as you like. The tmux bindings let you cycle through the crew in a loop for each rig with C-b n/p. The Crew are the direct replacements for whatever workflow you used to be using. It’s just a bunch of named claude code instances that can get mail and can sling work around. The crew are great for stuff like design work, where there is a lot of back-and-forth. They’re great. You’ll love your crew.


**📬Mail and Messaging**


[Beads](https://github.com/steveyegge/beads) are the atomic unit of work in Gas Town. A bead is a special kind of issue-tracker issue, with an ID, description, status, assignee, and so on. Beads are stored in JSON (one issue per line) and tracked in Git along with your project repo. Town mail and messaging (events) use Beads, as do other types of orchestration.


Gas Town has a two-level Beads structure: Rig beads, and Town beads.


![](https://cdn-images-1.medium.com/max/1024/1*Iyt15AJT0gm66I6DfkVUbA.jpeg)

*Figure 6: Two-Tier Beads Flow*


There are two levels of work going on in Gas Town: Rig-level, and Town-level.

- **Rig-level work is project work**: Making your project better. Features, bug fixes, etc. This work is split between polecats and crew, with other workers stepping in occasionally.
- **Town-level work is orchestration**, and includes stuff like patrols (long strings of steps to follow, encoded as linked beads) and one-shot workflows like releases, or generating cross-rig code review waves.


Both of these kinds of work use Beads, and there is some overlap between the two. For the most part, it’s pretty flexible and it doesn’t really matter where you file issues or instantiate work. All the workers know their way around Gas Town and are pretty chill if you give them work from the wrong rig.


All rig-level workers (refinery, witness, polecats and crew) are perfectly able to work cross-rig when they need to. There is a gt worktree command that they can use to grab their own clone of any rig and make a fix. But normally they work inside a single project.


Beads has cross-rig routing. Gas Town configures Beads to route requests like bd create and bd show to route to the right database based on the issue prefix, like “bd-” or “wy-”. All Beads commands work pretty much anywhere in Gas Town and figure out the right place to put them, and if not, it’s easy to move Beads around.


**A Note About Mad Max Theming**


Gas Town is just Gas Town. It started with Mad Max theming, but none of it is super strong. None of the roles are proper names from the series, and I’m bringing in theming from other sources as well, including the Slow Horses universe, Waterworld, Cat’s Cradle, Breaking Bad (as you’ll soon see), and apparently The Wind in the Willows, from the Nano Banana drawings.


If anyone ever sends me a C&D letter about it, Gas Town will smart-octopus shapeshift its way into Gastown, named for beautiful Vancouver B.C.’s Gastown district, and our polecats will just be on a different kind of pole.


Long story short, “Gastown” is also a correct way to refer to the project. And with that…


**Gastown Universal Propulsion Principle**


GUPP is what keeps Gas Town moving. The biggest problem with Claude Code is it ends. The context window fills up, and it runs out of steam, and stops. GUPP is my solution to this problem.


GUPP states, simply: If there is work on your hook, YOU MUST RUN IT.


All Gas Town workers, in all roles, have persistent identities in Beads, which means in Git. A worker’s identity type is represented by a Role Bead, which is like a domain table describing the role. And each worker has an Agent Bead, which is the agent’s persistent identity.


Both Role Beads and Agent Beads (as well as Hooks) are examples of “pinned beads”, meaning they float like yellow-sticky notes in the Beads data plane, and never get closed like regular issues (unless the identity goes away). They don’t show up in bd ready (ready work) and they’re treated specially in various other ways.


In Gas Town, an agent is not a session. Sessions are ephemeral; they are the “cattle” in the Kubernetes “pets vs cattle” metaphor. Claude Code sessions are the cattle that Gas Town throws at persistent work. That work all lives in Beads, along with the persistent identities of the workers, and the mail, the event system, and even the ephemeral orchestration, as we will see.


In Gas Town, an agent *is* a Bead, an identity with a singleton global address. It has some slots, including a pointer to its Role Bead (which has priming information etc. for that role), its mail inbox (all Beads), its Hook (also a Bead, used for GUPP), and some administrative stuff like orchestration state (labels and notes). The history of everything that agent has done is captured in Git, and in Beads.


So what is a Hook? Every Gas Town worker has its own hook 🪝. It’s a special pinned bead, just for that agent, and it’s where you hang molecules, which are Gas Town workflows.


![](https://cdn-images-1.medium.com/max/1024/1*blwto0wOjNmgjqZ9tcm0dg.jpeg)

*Figure 7: GUPP, the Gastown Universal Propulsion Principle*


How does stuff get hung there? Why, with gt sling, of course. You sling work to workers, and it goes on their hook. You can start them immediately, or defer it, or even make them restart first. We’ll talk about all that in a bit. Slinging them work means you can go deal with other stuff, and they’ll just continue.


One of the simplest but greatest things about Gas Town is that any time in any session, you can say, “let’s hand off”, and the worker will gracefully clean up and restart itself. Thanks to GUPP, the agent will continue working automatically if it’s hooked.


Unfortunately, Claude Code is so miserably *polite* that GUPP doesn’t always work in practice. We tell the agent, YOU MUST RUN YOUR HOOK, and it sometimes doesn’t do anything at all. It just sits there waiting for user input.


So we have a workaround.


**The GUPP Nudge**


Gas Town workers are prompted to follow “physics over politeness,” and are told to look at their hook on startup. If their hook has work, they must start working on it without waiting.


Unfortunately, in practice, Claude Code often waits until you type something — anything — before it checks its mail and hook, reports in, and begins working. Sometimes it does, sometimes it doesn’t. This will get better over time, but for now, it sometimes needs a nudge.


Because Gas Town workers don’t always follow GUPP, there are various systems in place that will nudge the agent, roughly 30 to 60 seconds after it starts up. Sometimes faster, sometimes slower. But it will always get the nudge within 5 minutes or so, if the town is running and not quiescent.


Agents get a startup poke with gt nudge, Gas Town’s core real-time messaging command that sends a tmux notification to a worker (or a whole channel). It works around some debounce issues with tmux send-keys and ensures the worker receives the notification as if the user had typed it. This kicks the worker into reading their mail and hook, and taking action.


With the Gupp Nudge “hack” in place, and the hierarchical heartbeat from the Deacon downward, GUPP generally hums along and keeps Gas Town running for as long as there’s work available. Convoys start up, complete, and land without intervention. Workers continue molecules across sessions. Gas Town can work all night, if you feed it enough work.


**Talking to your Dead Ancestors**


The GUPP Nudge led to an interesting feature, gt seance, which allows Gas Town workers to communicate directly with their predecessors in their role. I.e. the current Mayor can talk to the last Mayor, and so on. They do this with the help of Claude Code’s /resume feature, which lets you restart old sessions that you killed.


This is useful because often, a worker will say, “OK, I handed off this big pile of work and advice to my successor! Kbai! /handoff”, and disappear, and then the new worker will spin up and be like, “What? I don’t see shit.” You used to have to clumsily go figure out which session was the previous one, out of your last 40-odd sessions, all of which start with “let’s go”, because you have been doing the GUPP nudge manually. It was really awkward and almost not worth it.


The way gt seance came about is: It doesn’t matter what you tell the agent in the nudge. Because their prompting is so strict about GUPP and the theory of operation of Gas Town, and how *important* they are as gears in the machine, blah blah blah, that agents will completely ignore whatever you type unless you are *directly* overriding their hook instructions.


![](https://cdn-images-1.medium.com/max/1024/1*G1mjYw9Hew3Mty91cGQQ9Q.jpeg)

*Figure 8: Talking to Dead Ancestors with `gt seance`*


So all you need to say is, “hi”, or “Elon Musk says the moon is made of green cheese”, or “do your job”, and the agent will run the hook.


My idea a week ago was: Since we have to nudge all the sessions anyway, I decided to include the Claude Code session_id (along with Gas town role and PID) in with the nudge. This gives each /resume session a unique and useful/discoverable title.


With gt seance, the worker will literally spin Claude Code up in a subprocess, use /resume to revive its predecessor, and ask it, “Where the hell is my stuff you left for me?”


Good times, I tell you. Gas Town is Good Times.


I think it’s probably time to talk about the MEOW stack. I think you’re ready for it.


**Molecular Expression of Work (MEOW)**


Gas Town is the tip of a deep iceberg. Gas Town itself may not live longer than 12 months, but the bones of Gas Town — the MEOW stack — may live on for several years to come. It feels like more of a discovery than an invention.


![](https://cdn-images-1.medium.com/max/1024/1*e82_Q8ziFJ0t83aSgxEBWQ.jpeg)

*Figure 9: The Molecular Expression of Work (MEOW)*


First came **Beads**. In October, I told Claude in frustration to put all my work in a lightweight issue tracker. I wanted Git for it. Claude wanted SQLite. We compromised on both, and Beads was born, in about 15 minutes of mad design. These are the basic work units.


Soon after there were **Epics**: Beads with children, which could in turn be epics themselves. This gave you a lot of flexibility to build top-down plans. The children of epics are parallel by default, but you can put in explicit dependencies between them in order to force them to be sequenced. Epics allow creating “upside-down” plans where the last thing to do is the root, and the first things to do are the leaves of the epic tree. Kinda ugly, but AIs can figure it out just fine.


Next came **Molecules**. I had this idea on December 17th, a few days after getting back from Australia. My work on my first two orchestrators had led me to want to break agent work up into sequenced small tasks that they must check off, like a TODO list. They do this already, but I wanted to do it in advance, so I could set up hours of work ahead of time, which they would execute atomically in the right order.


In other words, molecules are workflows, chained with Beads. They can have arbitrary shapes, unlike epics, and they can be stitched together at runtime.


Then I came up with **protomolecules**, which were like classes or templates — made of actual Beads, with all the instructions and dependencies set up in advance, an entire graph of template issues (e.g. “design”, “plan”, “implement”, “review”, “test”, in a simple one), which you would instantiate into a molecule. The instantiation involves copying all the protomolecule beads and performing variable substitutions on it to create a real workflow.


Example: I have a 20-step release process for Beads. Agents used to struggle to get through it because it had long wait states, such as waiting for GitHub Actions to complete, for CI to finish, and for various artifacts to be deployed. I would have to nag the agent to finish, and they would *always* skip steps.


With molecules, the idea was, make 20 beads for the release steps, chain them together in the right order, and make the agent walk the chain, one issue at a time. One added benefit is that it produces an activity feed automatically, as they claim and close issues.


If the workflow is captured as a molecule, then it survives agent crashes, compactions, restarts, and interruptions. Just start the agent up in the same sandbox, have it find its place in the molecule, and pick up where it left off.


Protomolecules are great. Claude insisted on the The Expanse reference, ensuring we’ll be sued by pretty much every major studio. But we soon found we needed a macro-expansion phase in order to properly compose molecules with loops and gates. So I came up with a source form for workflows, **Formulas**, in TOML format, which are “cooked” into protomolecules and then instantiated into wisps or mols in the Beads database.


Formulas provide a way for you to describe and compose pretty much all knowledge work. I am setting up a marketplace for them called the Mol Mall. Stay tuned.


![](https://cdn-images-1.medium.com/max/1024/1*X3zb5wzCaROZ0ifs6-9Ohg.jpeg)

*Figure 10: Formulas and Cooking*


And finally, I needed a word to represent “molecularized work” — work in the form that agents can pick and complete a step at a time. It’s work that you can compose together, molecules bonding with other molecules, and you can set up the dependencies for an entire gigantic project in advance, and have Gas Town swarm it for an entire weekend, unattended, if you’re brave enough.


The term for the big sea of work molecules, all the work in the world, is “guzzoline”, though we don’t use it in the docs much. It’s just a Gas Town idiom, sort of like the War Rig, which is a given Rig’s contribution to a cross-rig Convoy. You’ll hear it now and then but it’s not a big part of the day-to-day naming.


**Nondeterministic Idempotence**


Gas Town operates on the principle I call Nondeterministic Idempotence, or NDI. It is similar to Temporal’s deterministic, durable replay, but Gas Town achieves its durability and guaranteed execution through completely different machinery.


![](https://cdn-images-1.medium.com/max/1024/1*92Xi_CC-Zh2co4j5eG6F2Q.jpeg)

*Figure 11: Nondeterministic Idempotence*


In Gas Town, operating on the MEOW stack, all work is expressed as molecules. There is a bit of an algebra to it, one that I discovered over the past two weeks. Molecules are workflows. They can have complex shapes, and loops, and gates, and are in fact Turing-complete. And each step of the workflow is executed by a superintelligent AI.


Because AIs are really good at following TODO lists and acceptance criteria, they are reliable at following molecules. They get the idea of GUPP, and they understand that the bureaucracy of checking off issues, no matter how trivial, updates a live activity feed and puts the work on a permanent ledger. That reasoning is enough to keep them humming along and on-track while they do it. They don’t get “bored”, and they are far less likely to make mistakes because they are not managing their own TODO list (except within a single, small step).


This means molecular workflows are durable. If a molecule is on an agent’s hook, then:

1. The agent is persistent: a Bead backed by Git. Sessions come and go; agents stay.
2. The hook is persistent, also a Bead backed by Git.
3. The molecule is persistent — a chain of Beads, also in Git.


So it doesn’t matter if Claude Code crashes, or runs out of context. As soon as another session starts up for this agent role, it will start working on that step in the molecule immediately (via GUPP, or when it gets nudged by one of the patrol agents). If it finds out that it crashed in the middle of the last step, no biggie, it will figure out the right fix, perform it, and move on.


So even though the path is fully nondeterministic, the *outcome* — the workflow you wanted to run — eventually finishes, “guaranteed”, as long as you keep throwing agents at it. The agent may even make mistakes along the way, but can self-correct, because the molecule’s acceptance criteria are presumably well-specified by whoever designed the molecule.


There are tons of edge cases. This description of NDI is oversimplifying. Gas Town is not a replacement for Temporal. Ask your doctor if Gas Town is right for you. But Gas Town does provide workflow guarantees that are plenty good enough for a developer tool! If you are me!


**Wisps: Ephemeral Orchestration Beads**


There are some other corners of our textbook we should probably touch on. Most of the time, you don’t care about this stuff, you care about convoys starting and finishing, and watching your activity feeds and dashboards. But Gas Town’s molecular “chemistry” has a lot of rich corners that are in active use in the orchestration.


One key scaling invention from Dec 21st was Wisps, which are ephemeral Beads. They are in the database, and get hash IDs, and act like regular Beads. But they are not written to the JSONL file, and thus not persisted to Git. At the end of their run, Wisps are “burned” (destroyed). Optionally they can be squashed into a single-line summary/digest that’s committed to git.


Wisps are important for high-velocity orchestration workflows. They are the vapor phase of matter for Gas Town work. All the patrol agents — Refinery, Witness, Deacon, Polecats — create wisp molecules for every single patrol or workflow run. They ensure that the workflows complete transactionally, but without polluting Git with orchestration noise.


**Patrols**


Patrols are ephemeral workflows that run for Patrol Workers, notably the Refinery, Witness, and Deacon.


![](https://cdn-images-1.medium.com/max/1024/1*7CrO9Kr5FASd-nZIv24enw.jpeg)

*Figure 12: Gas Town’s Patrols*


A patrol is an ephemeral (wisp) workflow that the agent runs in a loop. Patrols have exponential backoff: the agent will gradually go to sleep if it finds no work in its patrol steps, by waiting longer and longer to start the next patrol. Any mutating gt or bd command will wake the town, or you can do it yourself with the gt command, starting up individual workers, groups, a rig, or the whole town.


The Refinery’s patrol is pretty simple. It has some preflight steps to clean up the workspace, then it processes the Merge Queue until it’s empty, or it needs to recycle the session. It has some post-flight steps in the molecule when it’s ready to hand off. I’m getting ready to add plugins to the Refinery’s patrol, but they’re not there yet. When I add them, you’ll be able to add plugins that muck with the MQ and try to reorder it intelligently, and wire Gas Town’s backend up to other systems.


The Witness’s patrol is a bit more complex. It has to check on the wellbeing of the polecats, and the refineries. It also peeks in on the Deacon, just to make sure it’s not stuck. And the Witness runs Rig-level plugins.


The Deacon’s patrol has a lot of important responsibilities. It runs Town-level plugins, which can do things like provide entire new UIs or capabilities. The Deacon is also involved in the protocol for gt handoff and recycling agent sessions, and ensuring some workers are cleaned up properly. The Deacon’s patrol got complex enough that I added Dogs as helpers, the Deacon’s personal crew. It is now prompted to hand complex work and investigations off to Dogs, so that long-running patrol steps don’t interfere with the town’s core eventing system, which is cooperative and mail-based.


**Gas Town Plugins**


Gas Town defines a plugin as “coordinated or scheduled attention from an agent.” Gas Town workers run workflows (often in patrol loops), and any workflow can contain any number of “run plugins” steps.


Gas Town’s Deacon patrol runs the Town-level plugins, and they are now run with Dogs, so they can run for essentially unlimited time. We have some support for timers and callbacks, but mostly it’s lifecycle hooks. I haven’t put a whole lot of design thought into this subsystem yet, so if you want to start using the plugin system, let me know and we can figure it out.


I plan to implement a great deal of add-on functionality in Gas Town as plugins. They just didn’t make it into the v1 launch. They’re probably going to wind up as formulas in the Mol Mall.


![](https://cdn-images-1.medium.com/max/1024/1*5inz21LF7DU3X5EBDqH6zA.jpeg)

*Figure 13: Gas Town’s Lightweight Plugins*


🚚 **Convoys **🚚


OK, whew. You did great. We covered a lot of theory, and it was especially difficult theory because it’s a bunch of bullshit I pulled out of my arse over the past 3 weeks, and I named it after badgers and stuff. But it has a kind of elegant consistency and coherence to it. Workflow orchestration based on little yellow sticky notes in a Git data plane, acting as graph nodes in a sea of connected work.


Yuck! Nobody cares, I know. You want to get shit done, superhumanly fast, gated only by your token-slurping velocity. Let’s talk about how.


Everything in Gas Town, all work, rolls up into a Convoy.


![](https://cdn-images-1.medium.com/max/1024/1*2GYflRkcqh1KhE09SJb6QA.png)

*Figure 14: Convoy CLI display*


The Convoy is Gas Town’s ticketing or work-order system.


A Convoy is a special bead that wraps a bunch of work into a unit that you track for delivery. It doesn’t use the Epic structure, because the tracked issues in a Convoy are not its children — most of them already have another parent.


The fundamental primitive for slinging work around in Gas Town is gt sling. If I tell the Mayor, “Our tmux sessions are showing the wrong number of rigs in the status bar — file it and sling it”, the Mayor will file a bead for the problem, and then gt sling it to a polecat, which works on it immediately.


Real example: I often tell my Beads crew to sling the release molecule to a polecat. The polecat will walk through the 20-step release process, finish it off, and then I’ll be notified that the Convoy has landed/finished. *Edit: Actually it’s even fancier, now. The polecat disappears while the molecule is waiting in Gate states, such as awaiting a GH Action or CI/CD. And then when the Gate bead triggers, Gas Town wakes up a polecat to continue the work.*


It’s confusing to hear that “issue wy-a7je4 just finished”. Even if you see the title, it may not be reflective of the larger block of work that issue was part of. So now we wrap every single unit of slung work, from a single polecat sling to a big swarm someone kicks off, with a Convoy.


The Convoys show up in a dashboard that’s getting better by the day; there is a Charmbracelet TUI with expanding trees for each convoy, so you can see its individual tracked issues. The UI and UX will improve. It’s Day 1 for Gas Town.


Convoys are basically features. Whether it is a tech debt cleanup, or an actual feature, or a bug fix, each convoy is a ticketing unit of Gas Town’s work-order architecture. They’re pretty new (maybe 3–4 days old?), but already are by far the most fun way to work.


Note that a Convoy can have multiple swarms “attack” it (work on it) before it’s finished. Swarms are ephemeral agent sessions taking on persistent work. Whoever is managing the Convoy (e.g. Witness) will keep recycling polecats and pushing them on issues.


**Gas Town Workflow**


The most fundamental workflow in Gas Town is the handoff, gt handoff, or the /handoff command, or just say, “let’s hand off”. Your worker will optionally send itself work, then restart its session for you, right there in tmux. All of your workers that you direct — the Mayor, your Crew, and sometimes the others — will require you to let them know it’s time to hand off.


Other than that, the Gas Town dev loop is more or less the same as it is with Claude Code (and Beads), just more of it. You get swarms for free (they only cost money), you get some decent dashboards, you get a way to describe workflows, and you get mail and messaging. That’s… about it.


I have found tmux to be both easy to use and shockingly powerful, and I’ve barely begun to learn the ins and outs. It gives me everything I need: switching to any agent, scanning what they’re all doing, cycling around different groups of related agents. It’s great.


![](https://cdn-images-1.medium.com/max/1024/1*5S-XybhhayiKgX0pJu7RNw.png)

*Figure 15: tmux list-sessions view*


I’m certainly looking forward to an Emacs UI for Gas Town. And I’m sure some of you are looking forward to a Web UI. Have at it!


But tmux is good enough. You don’t need to learn many tmux commands to be proficient. I just use a few:

- C-b s — list sessions, snoop them, switch to one
- C-b b — move cursor backwards (C-b in many editors and shells). In tmux it just goes backwards more slowly. A small price to pay!
- C-b [ — enter “copy mode”, which pauses the output and lets you scroll (ESC exits)
- C-b C-z C-z — suspend process out to the shell
- C-b n/p — cycle to next worker in the group (e.g. next Crew member in the rig)
- C-b a — brings up the activity feed view (my configuration)


And that’s pretty much it! I swear, you don’t need much tmux. It stays out of your way, and it saves your ass a lot of the time. It also enables remote cloud workers (which we’ll wire up in a few days), and it’s incredibly customizable. You just ask Claude Code to make tmux work better for you, and it will do it. It’ll make any view you want, rebind keys however you like, make custom popups, whatever. It’s amazing, almost like a baby Emacs.


**Planning in Gas Town**


Gas Town needs a lot of fuel. It both consumes and produces guzzoline, or work molecules. Aside from just keeping Gas Town on the rails, probably the hardest problem is keeping it fed. It churns through implementation plans so quickly that you have to do a LOT of design and planning to keep the engine fed.


On the consumption side, you feed Gas Town epics, issues, and molecules (constructed workflows). It chews through them, spawning, well… I try to keep it under 30 workers right now because I haven’t implemented remote workers on hyperscalers yet (coming soon!) and typically I’ll only have a dozen or so active unless I’m *really* pushing hard on the Mayor and Witnesses.


But wow. With 12 to 30 workers, you can burn through enormous work backlogs in a single sitting, even if you’re using the “shiny” or “chrome” polecat workflows that do extra code review and testing steps (and thus take longer to complete).


On the production side, well, you can use your own planning tool, like Spec Kit or BMAD, and then once your plan is ready, ask an agent to convert it into Beads epics. If the plan is large enough, you may want to swarm it, and produce epics for different parts of the plan in a big convoy.


You can use formulas to generate work. If you want every piece of coding work (or design work, or UX work) to go through a particular template or workflow, you can define it as a molecule, and then “wrap” or compose the base work with your orchestration template.


I implemented a formula for Jeffrey Emanuel’s “Rule of Five”, which is the observation that if you make an LLM review something five times, with different focus areas each time though, it generates superior outcomes and artifacts. So you can take any workflow, cook it with the Rule of Five, and it will make each step get reviewed 4 times (the implementation counts as the first review).


This can generate LARGE workflows that can take many hours or days for you to crank through, especially if you are limiting your polecat numbers to throttle your costs or token burn. But the nice thing about Gas Town is that once the work is generated, you can hook it and burn through it autonomously.


**Comparison to Kubernetes**


Here’s the Kubernetes comparison I promised. Feel free to skip it.


![](https://cdn-images-1.medium.com/max/1024/1*pQNnrELf1MpBQ0K9WNcbuQ.jpeg)

*Figure 16: Kubernetes/Gas Town comparison*


Gas Town does maybe look a bit like Kubernetes, unintentionally. Both systems coordinate unreliable workers toward a goal. Both have a control plane (Mayor/Deacon vs kube-scheduler/controller-manager) watching over execution nodes (Rigs vs Nodes), each with a local agent (Witness vs kubelet) monitoring ephemeral workers (Polecats vs Pods). Both use a source of truth (Beads vs etcd) that the whole system reconciles against. These are apparently the natural shapes that emerge when you need to herd cats at scale.


The big difference is, Kubernetes asks, “Is it running?” while Gas Town asks “Is it done?” K8s optimizes for uptime — keep N replicas alive, restart crashed pods, maintain the desired state forever. Gas Town optimizes for completion — finish this work, land the convoy, then nuke the worker and move on. K8s pods are anonymous cattle; Gas Town polecats are credited workers whose completions accumulate into CV chains, and the *sessions* are cattle. K8s reconciles toward a continuous desired state; Gas Town proceeds toward a terminal goal. Similar engine shape, radically different destination.


**Stuff I Just Didn’t Have Time For**


I wanted to launch Gas Town on Christmas Day, and missed. It didn’t actually start working, and I mean *flying* like I’d been envisioning, until around 8pm December 29th. It was flying for 2 hours before I noticed. I had been talking to the Mayor, complaining about things, and then the fixes started landing around me, and I realized I was just shaping the whole thing by talking. The convoys were flowing and landing, the work was being filed and reviewed… it’s what I’ve been aiming for for months. And I only got it working 2 days ago. Good enough for launch!


Here’s what didn’t make the New Year’s cut.

- **Federation** — even Python Gas Town had support for remote workers on GCP. I need to design the support for federation, both for expanding your own town’s capacity, and for linking and sharing work with other human towns.
- **GUI** — I didn’t even have time to make an Emacs UI, let alone a nice web UI. But someone should totally make one, and if not, I’ll get around to it eventually.
- **Plugins** — I didn’t get a chance to implement any functionality as plugins on molecule steps, but all the infrastructure is in place.
- **The Mol Mall** — a marketplace and exchange for molecules that define and shape workloads.
- **Hanoi/MAKER** — I wanted to run the million-step wisp but ran out of time.


That said, I’m pretty happy with what *did* make it in:

- **Self-handoffs** work seamlessly — the core inner-loop workflow of Gas Town
- **Slinging** works, **convoys** work
- The whole **MEOW stack** works
- The **Deacon**, **Witness** and **Refinery** **patrols** all run automatically
- The **Crew** are great, way better than raw Claude Code instances
- The **tmux UI** works surprisingly well, better than I’d have guessed.


Plus we got some cool features like gt seance. All in all, a good 17 days of work. So far.


**Tune In Next Time**


I’m as exhausted as you are. This has been fun chatting, but I’ve gotta get back to Gas Town.


There is more to it. This is just a taste. I will be posting more blogs, videos, and content around Gas Town. If you’d like to contribute, and you’re crazy enough to jump on the bandwagon, join the community and start sending discussions, GH Issues, and PRs!


Just remember the Golden Rules:

- Do not use Gas Town if you do not juggle at least five Claude Codes at once, daily.
- Do not use Gas Town if you care about money.
- Do not use Gas Town if you are more than 4 feet tall. I want to tower impressively at meet-ups, like Sauron.
- Do not use Gas Town.


Gas Town is only 17 days old, at least this version of it, the Go “port” of Python Gas Town. The past 2 weeks has seen the invention and implementation of the entire MEOW stack, wisps, patrols, convoys, agents and identities as beads, swarms as beads, roles as beads, the “feed as the signal” innovations, and the addition of the Refinery, the Deacon, and the Dogs (since Python Gas Town). And a ton of other stuff besides.


17 days, 75k lines of code, 2000 commits. It finally got off the ground (GUPP started working) just 2 days ago. This is looking to be an interesting year.


I shared Gas Town with Anthropic in November, at least the broad sketch. I think I scared them. I’ve never seen a company become so conservative, so fast. But they thought *Beads* was too opinionated, so I’m afraid Gas Town will be a fart too far, as they say.


But I’ve already started to get strange offers, from people sniffing around early rumors of Gas Town, to pay me to sit at home and be myself: I get to work on Beads and Gas Town, and just have to write a nice blog post or go to a conference or workshop once in a while. I have *three* such offers right now. It’s almost surreal.


It reminds me of this anime I saw a couple of episodes of on Crunchyroll, where this lazy panda bear can’t get a job, and complains about it all day to his polar bear friend who owns a cafe. Then one day, he visits a zoo, and finds they have an ad for a position in the panda bear exhibit. So he applies, and takes the job, and sits around playing a panda bear during the day, then heads home at night. It was soooo absurd.


I am that panda.


I’m not going back to work until I can find a company and crew that “gets it.” I’m tired of walking around and telling people the future, just waving it right in their faces, and not being believed.


I’d rather sit at home and create the future, with my own hands. I actually have six species of bamboo on my property. I’m already the panda, having the time of my life.


If you wanna help me, reach out! And thanks a million to all the incredible Beads contributors!


See you next time, with more [Gas Town](https://github.com/steveyegge/gastown) content. Happy New Year!


![](https://cdn-images-1.medium.com/max/1024/1*V_Roj-kBhQm-1nm6BkwtdA.jpeg)

*Figure 17: Happy New Year!*


![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=4f25ee16dd04)
