---
title: "Beads Best Practices"
date: 2025-11-27
url: https://steve-yegge.medium.com/beads-best-practices-2db636b9760c
word_count: 2107
source: medium
---


# Beads Best Practices


--


Listen


Share


Beads continues to grow momentum. When my old friends start stumbling across it independently, I know it’s going viral.


Beads sits in an utterly unique space. Everyone is focused on making planning tools, and Beads is an execution tool. It’s like putting your coding agent on waxed skis. Maybe a better name would have beenAgents on Rails. But “Beads” does a nice job of capturing the idea that it’s focused on just the tracking, and nothing else: a small name for a small system.


Beads is now far, far more stable, nearly 6 weeks into its journey. It’s been a wild ride, with sometimes 50k lines of code changing per day. And none of us contributors look at any of it. It is 100% vibe coded, currently at 130k lines of Go code total, roughly half tests. And tens of thousands of people are using it in their daily workflows. People tell me they love it so much they use it for their personal TODO lists. And people are wiring it into larger orchestrators left and right. It’s also an amazing building block.


We have kept the scope small. With the community’s input, I reject anything that shouldn’t be part of the Beads core. So Beads doesn’t have a UI, but it has lots of example UIs that people have built as passion projects. We have at least four or five now. My buddy and co-authorGene Kimeven built his own Beads UI in Java Swing! He was so excited to show it to me. And it was indeed very cool.


So no UI, and Beads also doesn’t have a planning system. That’s not what it’s for. But it integrates well with any old planning system — just make your plan, then tell the agent to file Beads epics and issues for the work. After the epics are done, you can throw any number of agents at them to grind through them.


The last big category people keep trying to wedge into Beads is orchestration. We know orchestration is coming. And it’s tempting to make Beads more active; today it’s fairly passive and expects the Agent to use it as a tool. But people want more. And I get it. However, that stuff doesn’t belong in Beads.


## Beads + Agent Mail = Agent Village


The most compelling case to come along so far for direct integration with an orchestrator was MCP Agent Mail, written by a gentleman named Jeffrey Emanuel. We hadn’t met, but he had implemented an email-inspired system for agent-to-agent messaging, and a couple weeks ago he pinged me on LinkedIn, excited to tell me that it works super well with Beads.


He said that Beads gives the agents shared memory, and MCP Agent Mail gives them messaging… and that’s all they need. The surprising thing, he says, is that it doesn’t require massive setup or coordination. You just give them a task and tell them to go sort it out amongst themselves. There’s no ego, so they quickly decide on a leader and just split things up.


Jeffrey’s personal multi-agent workflow isverydifferent from mine, and to me it resembles how I worked back as a contractor at Accenture in the late 1990s. Their version control system was so crappy that only one developer could have a file locked at a time, and nobody else could work on it. We called it sneakernet — you had to run over to someone’s cube to get them to unlock a file for you. Once a guy came by and asked, “how long will you have that file?” and I was like, “about a month?” and he turned ghost white. So we negotiated.


That’s not how I like to work anymore, but it’s how Jeffrey likes his agents to work, all in the same repo clone (folder). So MCP Agent Mail comes with a file reservation system much like our old sneakernet VCS at Accenture. And although it seemscrazyto work that way, he assures me that the agents just figure it out. They’re quite resilient.


This, amusingly, is exactly my attitude towards Beads. It’s a crummy architecture (by pre-AI standards) thatrequiresAI in order to work around all its edge cases where it breaks. But AI canalwaysget it working (usually without too much effort). So AI “hydrates” the crummy architecture and makes it uncrummy. Well, less crummy.


I’m working on setting up my own git worktree-based agent village, also using Beads and MCP Agent Mail. Jeffrey was kind enough to modify it to support the worktree model, which doesn’t need the file reservation system; it uses git branches. I am testing it out now, with an Emacs frontend (soon to be powered by Efrit) so I can easily switch between 30+ agent workers in different vterm buffers. No more colored terminal windows sprawling across my screen! And Mail will give them swarm capabilities. This is going to 3x–5x my productivity, I’m certain. I’ll find out this week.


## A Tale of Two Bloggers


This is where the story of MCP Agent Mail gets more interesting. Jeffrey lives in NYC, and 2 weeks ago offered to have coffee, should I ever be in the area. Luckily this week I was there for Swyx’s excellent AIE conference, so on Thursday, he and I met up in the rain in Manhattan and walked around for about 2 hours trying to find my hotel. We were so caught up in conversation that we’d walk aggressively the wrong way for 20 minutes, and we did this two or three times, before we finally found the hotel and had a nice hot lunch.


The author of MCP Agent Mail turned out to be one of the most insanely over-the-top brilliant people I have ever met in my life. I do not use those words lightly. He wound up doing most of the talking, since frankly I had little to add, but I was enthralled, all the while being amused that he still wanted his agents grubbing around in a single folder like raccoons in a dumpster. Dev preferences are so unpredictable.


Anyhoo. He turned out to be the guy who wiped 2 trillion dollars off the global stock market in January, with his post, “The Short Case for Nvidia Stock.” I found out 3 hours in, during lunch at the hotel. Surprise!


So my instinct was spot-on; he actuallyISone of the brutally smartest people on Earth. He is a top-tier engineer, mathematician, AI researcher, and hedge-fund financier, equally rarified-air at all of them, and he seems more driven than any human I’ve ever met. Here’s his project list:jeffreyemanuel.com/projects


I left our conversation believing that Jeffrey Emanuel may well beat frontier-lab researchers to finding the next-gen LLM architecture. He’s got a shot at it, anyway. Time will tell.


So yeah. Beads. He likes Beads. Good endorsement. And you know who else likes Beads?


The models. Just ask ‘em.


With that, let’s get to the current best-known best practices.


## Best Practices for Solo Development


I don’t have much experience sharing Beads with other human teammates, so I’d love it if those of you with experience would chime in on best practices for teams. I can update this post with any especially juicy ones.


For my own development, here are some tips I’ve found helpful.


## Runbd doctorRegularly


Beads has a greatbd doctorcommand that will diagnose and automatically fix a wide range of issues. It also handles migrations and metadata updates for various features, including git hooks and other configuration.


You should get into the habit of runningbd doctorevery day on your repos.


## Keep Your Database Small


I runbd cleanupevery few days on every project. Whenever I get more than about 200 issues I start thinking about cleaning up, and I rarely let it go beyond 500.


bd cleanupdeletes any issues that are older than N days. I set it to 2 days because I'm cranking through so much work that I have to be aggressive. You can runbd syncafterwards to sync the database and push everything to git.


Doing this never hurts anything. The issues are always in git history, even after deleting them, because Beads is a git-native issue tracker. So you can always easily examine them and resurrect them if necessary.


Keeping your working issue set small is a performance optimization that you will come to appreciate. For instance, often agents will just use jQuery to search in theissues.jsonlfile directly. This fails if your file is larger than 25k tokens, the current limit for reading whole files, which is maybe 500-ish Beads issues, ballpark.


## Upgrade Regularly and Do Daily Hygiene


Beads gets a lot of bug fixes and its quality is improving fast. Make sure you stay on top of releases, and upgrade at least every week or two.


You can nowbd upgradeto upgrade. Runbd doctor [--fix]periodically.


Beads is a pretty complex system and conflicts often happen during merges. It is much better every week, as we fix more edge cases, but you’ll still often need to ask the agent to clean up Beads messes — broken rebases, conflicts that need manual resolution, etc.


## Plan Outside Beads, Then Import


Use your favorite planning tool, something maybe like OpenSpec, to create your plan. Once it has been revised a few times by the model, you’re ready to translate it into Beads.


My advice for a larger plan is to do the following:


First, ask your agent to file a set of detailed Beads epics and issues to track all the work from the plan, focusing carefully on dependencies, detailed designs, and potential parallelization.


Second, once the agent finishes grinding through filing all the beads, ask it to do a thorough review, proofreading, refining, and polishing, to ensure the workers have as smooth a time as possible when implementing the epics.


You can ask it to iterate and improve on your plan up to 5 times, and ask it again to iterate and refine the Beads epics up to 5 times, before it will say, “I don’t think we can do much better than this.”


## Restart Agents Frequently


Agents should tackle one task at a time. Once it’s done, kill the process and start a new agent. Beads acts as the working memory between sessions. By starting new sessions often, you save money and get better performance from the models.


## Ask the AI to File Lots of Issues


You should ask the AI to file beads to track any work that will take it longer than about 2 minutes to finish.


When you ask for a code review, tell it to file beads as it goes. This will result in much more actionable results from your code reviews.


The models will often choose to file Beads issues spontaneously, but nudging it occasionally will help as well.


## Use a Short Issue Prefix


My project prefixes so far arebd-,vc-,wy-,ef-, andgt-.


It just makes the whole world more readable if you cut down on your issue tracker ID sizes by using short prefixes.


Beads supports changing your issue prefix, so if you set it tomy-long-project-then you can ask your agent to use Beads commands to change it to e.g.mlp-.


## File Beads Bug Reports and Feature Requests


Head over to GitHub and file bugs as GitHub Issues. You can also ask for features in the Discussions section, or just post general questions or comments.


I have managed to stay on top of the feature requests so far, so don’t be shy.


## Tell Others About Beads


If you like Beads, share the love on social media. It’s such a great way to use coding agents, we should encourage people to try it out. Especially now that it is getting a bit more stable.


## Beads is Booming


Beads has been a pleasant surprise. It’s growing fast and proving that it’s solving a real developer pain point in the world of agentic coding. Yes, we’re still ironing out a lot of edge cases. It’s early days. But every release gets us closer to a rock-solid, stable system for sharing issue tracking across multiple workers.


I will do another post in a week or so, after I’ve played with Mail + Beads in an “agent village.” We’ll see how it goes!


In the meantime, my book with Gene Kim about Vibe Coding has sold through its entire first run of 10k copies and is now selling like mad through its second run. People are telling us they’re enjoying it and finding value. If you’re getting ready to start coding with coding agents, this is required reading for you!

