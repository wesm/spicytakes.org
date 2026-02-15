---
title: "Go crazy, folks, go crazy"
subtitle: "I’m not saying it’s right. I’m just saying it might work."
date: 2026-02-13T19:02:46+00:00
url: https://benn.substack.com/p/go-crazy-folks-go-crazy
slug: go-crazy-folks-go-crazy
word_count: 2008
---


![Ozzie Smith](https://substackcdn.com/image/fetch/$s_!0y7j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F377eb840-784a-4c90-be76-f4268c5dfbaf_1040x1602.jpeg)

*The three soundtracks to my life:This,this, andthis.*


Right now, millions of engineers are using AI to do their job. “Top engineers at Anthropic, OpenAI say AI now writes 100% of their code,”says Fortune. Claude is now effectively writing itself,says the personbuilding Claude.1“When AI writes almost all code, what happens to software engineering?,”asks a software engineer. This is all a very well known phenomenon at this point.2


By contrast, data analysts, who also write a lot of code, arenotusing AI to do their jobs. Though most use chat applications like ChatGPT, a 2025 survey from dbt Labs found thatless than a thirdare using dedicated development tools. Things may have changed since that survey—it’s fromearly2025, which was years agothese days—but by most accounts, AI seems to be upending analysts’ lives much less than it’s upending engineers’.


You could have two theories about this:

1. Analysts do a job that is uniquely hard for AI. We’vetalkedaboutthistheory a lot. Software projects are relatively contained—there is a codebase; there are users who give feedback on what that codebase does; there can be specifications for how you want to update that codebase to improve it; all of these things can be written down. Software is also relatively testable—change the code; push the new button; does it work? Data analysis is neither of these things. To solve an analytical problem, you have to know about a codebase, but alsoa business, a market,the thoughts inside of people’s heads, and the location ofnearby electrical substations. Youcannotwrite all of this down. Moreover, analysis isn’t testable. You find out ifyour recommendationwas good after the recommendationplays itself out.
2. Or, analysts are cowards.


I mean, no, not exactly. But here is a history of popular generative AI products, and there is a pattern:

1. Google inventedtransformers, which were foundational to the development of large language models. Putting a chatbot on top of transformers was a fairly obvious idea, but Google was cautious about releasing a product like ChatGPT, because, in part,they were“too scared” that “chatbots say dumb things.” So, they didn’t, OpenAI eventually did—not because they knew it was going to work, but because,eh, why not?—and practically overnight, ChatGPT became one of the most used products in the world and OpenAI became one of the most valuable companies in the world.
2. Then, people quickly realized that AI is good at writing code. Initially, most AI-powered coding products, likeGithub Copilotor Cursor, were fundamentally aboutasking for permission: They proposed changes in code editors, and engineers were asked if they wanted to accept or reject the updates. Simply accepting all of the model’s edits was a fairly obvious idea, butthat made people nervous. So most tools didn’t encourage it, until Anthropic said,eh, why not?,3and released a fully autonomous coding app. Practically overnight, Claude Code became one of the mostinfluential products in the world, and Anthropic became one of themost valuable companiesin the world.
3. At its core, Claude Code is a bunch of looped requests to Claude. A user says “add a button to my website;” that is turned into a prompt to Claude; Claude’s response is fed back into another Claude; and again; and again; and so on. But why stop there, many people wondered. Could you have a managerClaude tell the first Claude to add a button to the website? Could you have adirectorClaude tell the manager Claude what problem it needs to solve, and have the manager Claude decide to add a button on its own? Could you have a CEO Claude tell the director Claude to hit their quarterly targets? Could you have a board of Claude tell the CEO Claude tosharpen their pencil?4Which is all to say,Gas Town—i.e., an army of Claudes, telling each other what to do—was a fairly obvious idea. Still, most people didn’t try to build it—not in its unhinged, explosive form, anyway—because it sounds dangerous and expensive. But then, someone did, and it got a bunch of attention,becauseit was unhinged and explosive.
4. Of course, if a bunch of Claudes are good at managing our software projects, maybe they’d be good at managing our personal lives? Our lives aren’t that complicated; they’re just scattered. They’re in our personal emails, and our work emails, and texts, and  calendars, and in our documents, and our bank statements, and our forgotten Banana Republic Rewards Credit Card accounts. Giving Claude access to all of these things and telling it to be a personal assistant is a fairly obvious idea, but it’s a horrifying one. So, most companies that tried to build personal AI assistants did so “responsibly,” by carefully gating what the assistant could see and do. And then an engineer said,eh, why not?, andyippee-ki-yayyedtogether Clawdbot, an AI assistant with access to absolutely everything. It became,in amonth, the world’ssixth-most popularopen source software project.5


Look, this is a responsible blog that believes in doing responsible things. It believes that it iscorrectfor AI data products to focus ondelivering“trusted insights on your enterprise data.” It believes that, “as AI agents evolve from experimental sidekicks to productive team members,”ofcourse“enterprise leaders must design systems that are not only powerful but trusted, governed, and simple to use.” It believes that if the world were right and just,the product“that helps data teams deploy analytics agents they can trust” would be the product that earns everyone’s business. We should be rigorous. We should measure twice and cut once. We should bedata stewards, andmaster data managers. We shouldnotpursue the fairly obvious—and obviously irresponsible—idea of giving an AI agent unfettered access to our databases, our documents, our emails, our Slack messages, our Zoom calls, our meeting notes, and our customer support messages, and telling it, “Go find me something useful, and don’t come back until you do.” We shouldnotlaunch a hundred Claude Code sessions and instruct them all to chase whatever hunches they have about how we could make more money. We shouldnothave Codex test a new hypothesisevery three seconds, until one finds a billion-dollar needle in a haystack.


Butsomeonewill. Someone will make a product that does that. And given this environment—and our recent history—which product are you betting on? The slow and steady one that carefully audits its structured context stores and tells users it doesn’t have enough information to answer their question? Or the one that cranks the AI dial to 12? Will it be the product that worries itself with governance and keeping inference costs low, or the one that believes that a dollar spent on Opus is probably a lot more productive than dollar spent on an analyst, andtriesto ignite a data center on fire on your behalf?6Is it the AI agent that’s optimized to oh-so-preciselyanswer mundane questions like, “How many shirts did we sell last week?” over and over again via a Slack integration? Or is a battalion of Codexes and Claudes that are all told to relentlessly and recklessly find ways to make more money?


Yes yes yes, I know, I know. That product is wrong. It doesn’t always work. It makes stuff up. It’s not reliable. It’s not secure. It’sdangerous.


Tell that to Google. Tell that to Copilot. Tell that a graveyard of AI personal assistant startups that stood on the same righteous soapbox.


When you’re on the inside, you forget that most people don’t care about the details that you do. You spent your life carefully researching AI safety inside of a cleanroom at Google; how could the public ever want to use a chatbot that doesn’t meet your exacting standards? Your entire job is double-checking the numbers; how could anyone ever trust an AI that isn’t writing queries through a version-controlled semantic layer? Up close, we can’t just do it; we have do itright.7


But outside of your particular domain, how many terms of service do you blindly accept? How many defaults do you change? How often do you YOLO your way through the warnings and fine print?  How regularly do you say, “this is too long,I ain’t reading all that, just show me something good already?”


It’s a form of theGell-Mann amnesia effect: Within our area of expertise, the more we worry about the details, and the more we forget that other people don’t. But outside of it, we’re like everyone else—we just want to see something cool.


---


These days, people spend a lot of time talking about the future of software. From an earlier post, here’sone way you could think about it:


> Before we all had computers and phones and Instagram, making art was hard. You had to have a fancy camera, or painting skills, or the ability to stitch together film strips into a video. Because art was expensive and somewhat scarce, we valued the art itself.Then it became easy to make. You can create great art in seconds, sometimeswithout even meaning to. And as the cost of making it fell, the value and notoriety of each individual piece of art fell too.So we started to care more about thecreatorsthan their specific creations. Like: Name that one great Kai Cenat stream. What’s your favorite Mr. Beast video? What’s Charli D’Amelio’s masterpiece? Some things might be more memorable than others, but there is no opus. Very little stands on its own. Popularity comes from a personality and an amorphous body of work.Now, the cost of creating software is also going to zero,as they say. So would we not expect to see the same patterns here? While that doesn’t mean big software businesses will go away—there will always be workhorse products that do accounting and manage warehouses and fly airplanes, just as there are still big-budget Hollywood movies—could there not also be an ecosystem of influencers who make software that is popular because they made it? …AreNikita Bier’s appsproducts or content? Is he an entrepreneur or an influencer? Issignull, an anonymous tech commentator,creating a product studioor a hype house?Is there even a difference?


There is another parallel, perhaps. When we are drowning in content, the only way to get people’s attention is bybeing crazy. Software may not be so different. Software must be disciplined, many people will say. It must be made bywell-trained teams of thoughtful professionals, because that is the right way to do it.


Sure, maybe. But the right way and winning way aren’t necessarily the same thing. And maybe the future of software is stuff that’s made byone personwho was willing to try somethingcrazy.

[1](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-1-187885232)

Overseeing Claude? Observing Claude?

[2](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-2-187885232)

Even if you aren’t aware of it,your retirement account is.

[3](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-3-187885232)

“Our goal with Claude Codeis to better understand how developers use Claude for coding to inform future model improvements.”

[4](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-4-187885232)

Could you have the manager Claude tell the board Claude that they’re lowering their growth targets this quarter, but they’llmake it up in the back half of the year?

[5](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-5-187885232)

Twenty projects have more stars on Github than OpenClaw. Fifteen are lists of engineering resources. The other five are React, Python, Linux, Vue, and TensorFlow.

[6](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-6-187885232)

I once asked peoplehow often in their careers they found a truly meaningful “insight” in their data. The average answer was once every two years—or, if measured by an analyst’s salary, once every few hundred thousand dollars. How many Gas Towns of Claudes could you run with that? How many different moonshots could it explore? How many useful things would it find? Do you think it would be less thanone?

[7](https://benn.substack.com/p/go-crazy-folks-go-crazy#footnote-anchor-7-187885232)

When we launched Mode, we had to build a way for it to connect to customers’ databases. A lot of people used cloud databases, which we could connect to directly, if people gave us their passwords. But nobody would ever do that, we thought; you can’t expect people to just paste important passwords into a form on a random startup’s website. So we spent several months building a tiny application that people could install on their own servers, which made it possible for them to use Mode without ever sharing their passwords with us.


Almost immediately, everyone complained. “I have a password,” they said, “can’t you just use that?” “Here it is,” some said, in a support ticket, “please get me connected.”
