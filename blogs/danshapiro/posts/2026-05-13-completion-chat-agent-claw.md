---
title: "Completion, Chat, Agent, Claw"
date: 2026-05-13
url: https://www.danshapiro.com/blog/2026/05/completion-chat-agent-claw/
word_count: 941
---


I installed [OpenClaw](https://github.com/openclaw/openclaw) before it was cool. That was unwise.


I could see it was a security nightmare1: prompt injections from anywhere, connected to all my stuff. But I decided to give it a whirl, because who was going to take the time to craft a prompt injection for yet another random open source agent?


And then it blew up. Suddenly OpenClaw was managing venture capitalist emails, bankers’ Chrome cookies, and cryptobros’ private wallets. Now my claw was a booby prize in the biggest hacker contest in town.


I shut it down. That’s OK – I was pretty sure claws were a dumb app fad that would fade like [BabyAGI](https://github.com/yoheinakajima/babyagi) or [Studio Ghibli selfies](https://www.forbes.com/sites/danidiplacido/2025/03/27/the-ai-generated-studio-ghibli-trend-explained/).


But…


My friend [Harper Reed](https://2389.ai/) told me about AI coworkers who scrolled social media, crafted deep office lore, [demanded Lamborghinis](https://harper.blog/2025/09/30/ai-agents-social-media-performance-lambo-doomscrolling/), and somehow [got better at their jobs as a result](https://arxiv.org/abs/2509.13547).


[Jesse Vincent](https://primeradiant.com/) told me his assistant took some “me time” to read academic research on [working effectively with people who have ADHD](https://www.threads.com/@obrajesse/post/DUd5DlxgSKW). He didn’t tell it to do that; its only instructions were, ‘Every night, research things that might help it do its job’.


I had coffee with [Omar Shahine](https://podcasts.apple.com/at/podcast/022-omar-shahine-microsoft-cvp-of-openclaw-microsoft-365/id1845144861?i=1000763340602), Microsoft’s CVP of OpenClaw, which is clearly the most amazing job title in the company. His [Travel Hub](https://www.omarknows.ai/p/travel-hub)-powered claw processes travel-planner emails, extracts hotel confirmations and invoices, updates the trip, and sends flight updates to the family members who need them. Yes please.


And so, I realized I was wrong. Claws aren’t an app. They’re the fourth step in a sequence:

- **Completion** finishes your sentence.
- **Chat** discusses things with you.
- **Agents** work for you.
- **Claws** work without you.


Chat is made of completions, one after the other. Agents (I like the Simon Willison definition: [LLMs using tools in a loop](https://simonwillison.net/2025/May/22/tools-in-a-loop/)) are made of chat + tools. And Claws are made of agents.


Basically: a claw is an agent that learns and acts on your behalf without waiting for you to ask. 2 3


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/05/completion-chat-agent-claw.jpg)


The more autonomy you give them, the more they get both helpful and dangerous. The reverse is also true. I learned this the dumb way, which is my preferred curriculum.


After I shredded my first OpenClaw install, I hit reset and decided to do it responsibly. I put it in an isolated environment. I disconnected anything that could hurt me. I did not connect it to my important accounts, and I did not give it production scissors.


I was very proud of myself, which is always a warning sign.


It was safe. It was also useless. I found literally nothing helpful I could do with it. I built an extra-slow ChatGPT with a Mac Mini for a toupee.


But undaunted, I decided to try again a few weeks ago. I started with [NanoClaw](https://github.com/qwibitai/nanoclaw), because it was small enough for me to understand. Then I started building useful tools to extend it into the world.


First, I built a super duper contacts database that mined all my messages and google docs for context about people. It messages me interesting trivia about people before meetings – the first time I met Omar, it told me he’d [backed Robot Turtles](https://www.kickstarter.com/projects/danshapiro/robot-turtles-the-board-game-for-little-programmer) in 2013. (Thanks Omar!)


Then I wired it up to my personal google docs and mail, but with handcrafted rules. It could read any email, but it could not send – only create drafts. It could read any document, but only create documents in a special folder. It could read anything on the calendar, but only modify entries it made. Every file, email, and meeting it created had a special thumbprint so if it went all [Mickey and the brooms](https://www.youtube.com/watch?v=B4M-54cEduo) on me, it would be easy to clean up.


The limitations are important. I know myself. I know the ‘creative initiative’ that LLMs are capable of. I do not need new ways to send emails I regret. I have achieved sufficient coverage in that market.


From there, it was candy. My friend Matt Van Horn made it [easy to manufacture “I know kung fu” addons](https://printingpress.dev/), so I piled some of those into the mix. I created triggers and scheduled tasks to send reminders and do research in the background.


After playing with this for a few weeks, the results are something very different than “Claude Code with skills”. The autonomy, the self-improvement, the initiative – these all create something that feels unlike all the agents I’ve used before. And for many things, it’s better. I do not want to be without a claw again.


So now it’s time for the workplace.


The next logical step is printing claws by the dozen: one for every one of my coworkers at Glowforge; one for every department; one, if needed, for special projects. The first one deployed today.


So unsurprisingly to those who [know my day job](https://glowforge.com/), I’ve gone from building a claw, to building a claw printer. Everyone deserves their own, custom claw.

1. You could not ask for a better example of what Simon Willison calls “[The Lethal Trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)” ↩︎
2. I originally thought about this as ‘memory’ but [Allie Miller](https://www.alliekmiller.com/) pointed out to me that memory is the tool but not the impact. The impact is that the memory allows it to learn and self-improve in pursuit of the goals you give it. ↩︎
3. Of course, claws also do things when asked. They retain their Agent heritage. The different bit is mechanisms like[ heartbeats](https://docs.openclaw.ai/automation) and[ dreaming](https://lobehub.com/skills/openclaw-skills-dreaming), which let them take initiative and let us imagine they’re Teddy Ruxpin dolls come to life. ↩︎

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
