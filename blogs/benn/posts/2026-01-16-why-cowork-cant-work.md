---
title: "Why Cowork can’t work"
subtitle: "The future isn’t collaborative."
date: 2026-01-16T17:27:03+00:00
url: https://benn.substack.com/p/why-cowork-cant-work
slug: why-cowork-cant-work
word_count: 1791
---


![](https://substackcdn.com/image/fetch/$s_!IcFW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F178c12a1-6461-45c9-89e1-971e9490a30d_1974x1066.png)


Why does Claude Code, thesuddenly ubiquitousAI-powered code-writing tool, work so well?


You might say that it’s because Opus 4.5, the LLM that generates the code, is good. Many peoplehave said this, and popular coding benchmarkssupport it. Claude Code works because its engine works.


Or, you might say that Claude Code works because the Claude Codeapplication—the thing that takes your instructions and uses Opus to figure out what to do with them—is good. That application extends Opus’ native capabilities with a bunch of clever reasoning loops and tool calls in waysthat mimichow humans think through problems. Opus is smart, sure, but it’s asking Opus to create a plan for itself and to reflect on its own output that makes it an engineer, and maybe, almost,an employee capable of any kind of work.


Anyway, if you thought these things, you might get to thinking about some other things too:

1. Most people do not write code. They have jobs in which they do other things: Send emails,make PowerPoint decksfor quarterly business reviews, and writeTPS reports.
2. Claude Code can probably do these things too. Opus knows a lot aboutbiology, chemistry, and physics. It demonstrates “fluid intelligence.” Itwrites reasonably well. It can code good, and it has also learned to doother stuff good too. It invented adistributed agent orchestratorat Google. Like, c’mon, it can probably write some emails.
3. But Claude Code is a terminal app. It uses monospaced fonts; there is no UI; there are no buttons. It feels, aesthetically, like logging into the mainframe with MS-DOS. “Code” is right there in its name. And most people who write emails and make PowerPoint decks and send TPS reports do not want to log into the mainframe.
4. So make it look like a website! Put a pretty UI over it, add some menus and colors and stuff to click. And say it’s for everyone, working on anything. And call it something more inclusive, like Claude Work.


And so,inevitably:


> Cowork: Claude Code for the rest of your workWhen we released Claude Code, we expected developers to use it for coding. They did—and then quickly began using it foralmost everything else. This prompted us to build Cowork: a simpler way for anyone—not just developers—to work with Claude in the very same way. …In Cowork, Claude completes work like this with much more agency than you’d see in a regular conversation. Once you’ve set it a task, Claude will make a plan and steadily complete it, while looping you in on what it’s up to. If you’ve used Claude Code, this will feel familiar—Cowork is built on the verysame foundations. This means Cowork can take on many of the same tasks that Claude Code can handle, but in a more approachable form for non-coding tasks.


The reactions were immediate: This is what’s coming. Just as Claude Code changed software development forever, Cowork could be the start of changingworkforever. The product has rough edges,said one reviewer, but “this is still a strong signal of the future.” “Cowork is less a new feature than it is a new way of working,”said another.


Probably? Maybe? I don’t know. But I’m not sure the story is quite so simple. Because there is another answer that you could give that explains why Claude Code is successful—that it works becausewe don’t care what it writes.


We’ve talked about this before. Sure sure sure, we care about how elegant our code is, and some engineers will nitpick Claude’s architectural decisions andstylisticchoices. But ultimately, code is meant to be run, not read. And if Claude can turn our English instructions into a functioning application, we don’t care if it does so in beautifully written Rust, inmiles of incomprehensible CSS, or in Pig Latin:


> When people talk about the dangers of vibe coding, they often worry about AI writing, if not bad code,uncannycode. “It works, it’s clear, it’s tested, and it’s maintainable,”they say, “but it’s written in a way that doesn’t follow the project conventions we’ve accepted.” This has always struck me as an odd concern—or at least, an overstated and potentially temporary one. Code quality is a proxy for application quality, and application quality is both what we care aboutandverifiable on its own. Though it’s slightly more complicated than that—you can’t test every possible edge of a website or an app—at some theoretical limit, an application’s code could be completely incomprehensible, andthat’s fine. And while we may never reach that limit,we could get a lot closer.


Put differently, code does not need to be personally expressive. Engineers are responsible for what code does; they are increasinglyless responsiblefor—andless concernedabout—the specific way it does it. In a sense, software development is no longer directly collaborative: We write private messages to a machines; the machines transform our instructions into code that we do not read; they commit it to a repository that nobody else reads, either.


You could argue that this fact—that we don’treallycare if we write code with awkward syntactic quirks—is a central reason that Claude Code works. We all know aboutdelve; we all know aboutem-dashes. Code written by LLMshas similar telltale habits. But if we aren’t going to read it, so what? Bulldoze our personalities and cosmetic preferences out of our work. Though we care howwetalk to each other, when we only speak through translators, who cares howtheytalk?


None of this is true for sending an email, or making a PowerPoint, or writing a TPS report. Emails are fromme, toyou. There are no intermediaries. My emails represent me; theyareme. And you will read it—and judge it, and me—if I talk in ChatGPT’shollow wispiness. Writing an email may be a lot simpler than writing code, but it is not easier, because only emails need to containme. If you want to write code, write a specification. If you want to write an email,you must first invent the universe.1


There are two solutions to this. The first is to teach AI tobe us, or at least,writelikeus. Teach it our voice; teach it our personality. Give it ourmemories. If we can replace itssoulwith our own, then it can be our digital surrogate.


Many people will no doubt try; someone may succeed. But if you’ve ever tried to use Claude or ChatGPT to write on your behalf, you know howhard it isto beat the pre-training out of an LLM. No matter how much you tell it to write like Susan Sontag, or David Foster Wallace,2or “these 20 example emails I just gave you,” the machine will always hearthe echoes of its whispering ghosts.


The other solution, of course, is tofix the roads.


What if we stopped making PowerPoints for each other, but for the machines? What if all of our TPS reports were absorbed intocontext layersanddecision traces, and nobody ever saw the actual documents we put into the system? What ifwenever saw the documents that we put into the system? We dump our ideas into atext box; the machine uses our input to update its inscrutable repository of facts; other people interrogate the repository, not by reading it, but by asking the machine to fetch what they need. Why collaborate when you canadd context?


Consider the current moment: We talk to one another, and work together. We email back and forth; we share documents with each other. We know stuff, because it’s in our messages and our files and our heads.


A new repository of knowledge is starting to emerge underneath us.Dozens of toolsare absorbing all the things we say to each other, and presenting it back to us in a chatbot or a search bar. It’s a second world, a map to the territory that lives in Google Drive and Slack and Outlook.


How long will we maintain both? If we’re doing our work by asking what’s on the map—or by having robots that read from the map do our work for us—why wouldn’t we just update the map directly? Why wouldn’t the mapbecomethe territory?


Speaking of maps, last month, Googlereplaced the Q&A featurein Google Maps with an Ask AI feature. Instead of showing people what others are saying about stores and restaurants, the app now prompts you to ask Gemini questions like, “Is this place good for groups?” Customers no longer talk to one another; it is all intermediated through an unseen repository of aggregated posts and reviews.


For better or for worse, that seems to be where we’re heading—workingaroundone another, through an unseen repository of PowerPoints and TPS reports. And Anthropic’s new product may well be the beginnings of a new way of working, but it is notcollaborativework. It is confederated work. Or Cowork, for short.


---


# Takeoff


Nine months ago, several AI researchers wrote adetailed forecastfor how the world will likely end. A key part of their story—and of nearly every science fiction story about an apocalyptic AI taking over the world—is “takeoff:” The point at which AI becomes smart enough to improve itself. The researchers said this could happen in early 2026:


> Early 2026: Coding AutomationThe bet of using AI to speed up AI research is starting to pay off.OpenBrain [a fictional AI company] continues to deploy the iteratively improving Agent-1 [a fictional AI model] internally for AI R&D. Overall, they are making algorithmic progress 50% faster than they would without AI assistants—and more importantly, faster than their competitors.


The point is that, once Agent-1 gets good enough to accelerate how quickly OpenBrain can improve it, the model’s advantage compounds—first, over its competitors, and then, over its own creators. The smarter the model gets, the faster it improves, until we lose control of it.


Ah, whatever,it’s all just science fiction, right?


> When I created Claude Code as a side project back in September 2024, I had no idea it would grow to be what it is today. … In the last thirty days, I landed 259 PRs -- 497 commits, 40k lines added, 38k lines removed. Every single line was written by Claude Code + Opus 4.5.


it’s all just science fiction, right?


> Scoop: xAI staff had been using Anthropic’s models internally through Cursor—until Anthropic cut off the startup’s access this week.


Right?

[1](https://benn.substack.com/p/why-cowork-cant-work#footnote-anchor-1-184785771)

I understand that Cowork can be used for a lot of individual projects too—cleanmy desktop,planmy day,write a reporton how I work—and Cowork is probably quite good at these things. Still, so long as we work with other people, there will also be a lot of cases in which care a lot about how well a tool like Cowork represents us, and that’s a far harder problem to solve.

[2](https://benn.substack.com/p/why-cowork-cant-work#footnote-anchor-2-184785771)

Here’s an analysis I want, from someone inside of Anthropic or Claude: Who’s the most mimicked writer? “Write like X,” a million people probably say. Who is the most used X? Give me that leaderboard.
