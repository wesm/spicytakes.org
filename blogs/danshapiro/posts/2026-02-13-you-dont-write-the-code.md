---
title: "You Don’t Write the Code. You Don’t Read the Code Either."
date: 2026-02-13
url: https://www.danshapiro.com/blog/2026/02/you-dont-write-the-code/
word_count: 1188
---


A few months ago, I walked into Justin McCarthy’s office at StrongDM and noticed something wrong with his colleague Jay’s monitor.


He had a Google Spreadsheet open. Columns, rows, formatting – it looked exactly like Sheets. Except the URL bar said localhost.


That could not be so.


Gsuite was not alone. Slack was there, Jira, Okta… all running locally? A digital twin of the entire enterprise SaaS universe, there on that desktop, faithful enough that the Python client libraries couldn’t tell the difference. Jay confirmed that it was in fact what it looked like; he built it himself. It took a couple of weeks. He used their [Dark Factory](https://simonwillison.net/2026/Feb/7/software-factory/).


The essence of what I learned from them could fit on a notecard.


---


## Standing on One Foot


I’ve been having quiet conversations with Justin McCarthy, CTO of StrongDM, for months now. I wrote about the first one – a dinner at Piccino where he told me about [slot machine development](https://www.danshapiro.com/blog/2025/10/slot-machine-development/), and I walked away patting myself on the back thinking I understood a little bit of the future now. Since then, every few weeks he’d tell me something new, and every few weeks I’d nod politely while privately thinking he was… let’s say optimistic. Exaggerating would be rude. Nobody’s actually doing that.


This week he got on stage and showed it to the world. I was in the room. He was not exaggerating.


The essence of what Justin’s team learned fits on an index card.


**First**, you recognize that, if you want to move quickly, you’re not the person best qualified to be writing code anymore. The AI writes the code.


**Second,** you recognize that if you’re not writing the code, and you’re still reviewing every pull request, *you* are the bottleneck. So you have to stop reading the code, too.


**Third**, you realize this creates an enormous pile of terrifying problems. If nobody’s writing code, who understands it? If nobody’s reading the code, how do you know it works? How do you know it’s getting better instead of worse?


**Finally** – and this is the part that takes a minute to land – you realize that solving those problems is your actual job now.


That’s it. That’s the whole thing. That’s how you build a software factory. Everything else is commentary. You can stop reading and go figure it out.


---


## You Can’t Look Inside


So you don’t read the code. You built something, it’s inside a sealed box, and you have no idea what’s going on in there.


It seems strange, but we’ve been here before.


When I was 10 years old, [my dad](https://en.wikipedia.org/wiki/Leonard_Shapiro), a professor of computer science, explained this while carving a roasted chicken at the dinner table.


“You see, everyone used to write the code by hand. But now there are these ‘high level languages’. People say it’s cheating to use them. But getting things done is *so much faster*.”


People would complain that you had to hand-optimize the assembler. They would be horrified that you’d ship assembly code you’ve never read.


History rhymes.


---


## Monday, Then Tuesday


The Monday before their release, they built CXDB. It’s a special-purpose observability layer that watches every interaction in their system.


On Tuesday, they built Healer.


Healer watches CXDB, develops opinions about whether agent behaviors look right, and clusters similar problems into diagnoses. Those diagnoses become investigations – and the investigations are themselves agents. An agent wakes up, looks at the cluster of bad behavior, finds the relevant code and prompts and data, and writes a prescription. The prescription gets applied. The bug gets fixed.


No human filed the bug report. No human triaged it. No human wrote the fix.


This is what I found most interesting about their building process. Last year, “let’s spend our time on the tools before we start the product” was foolish. This year, it’s more like the quote attributed to Abraham Lincoln: “Give me six hours to chop down a tree, and I will spend the first four sharpening my axe.”


---


## The Digital Twin Universe


Back to GSheets on localhost.


StrongDM is an enterprise security company. They build access management for complex enterprises. In their world, ‘security issue’ is a euphemism for ‘lawsuit’.


Once you’ve realized you don’t write the code, and you don’t read the code, the biggest problem is quality. And the best solution to quality is testing – in the most realistic environment you can.


You see where this is going.


As Justin put it: “A year ago, if an eager new hire had walked into my office and suggested ‘let’s just clone GSuite and Salesforce and Okta and every SaaS application our product integrates with,’ I would have said: your enthusiasm is really welcome. Get back to work. Project not approved.”


“And I would have been wrong. Jay built the whole suite in a couple of weeks. The replicas are faithful enough for every externally observable behavior the agents need – not a full reimplementation of Google Sheets, but close enough that the agents can’t tell the difference.”


---


## Why Am I Doing This?


Justin’s team has a mantra. Whenever anyone finds themselves doing something manually – reviewing logs, checking output, validating behavior – they stop and ask one question:


*Why am I doing this?*


If you’re looking at a log file and something doesn’t look right, and you can articulate *why* it doesn’t look right, you’ve just described a validation rule. And if you can describe it, you can automate it. So stop looking at log files. Get yourself out of the job of looking.


This is the discipline that separates a team that uses AI from a software factory. It’s relentless, almost uncomfortable. But it’s also the most concrete thing you can take away from Justin’s work: the next time you find yourself doing something, ask how you can stop.


---


## What Next?


Justin’s team is three people. A CTO, a senior software engineering manager, and a new hire less than a year out of school. That team built it all – the factory, the features, the digital twin universe. Now Navan, the new guy, is leading bootcamps where dozens of StrongDM senior developers learn the new way software is built.


StrongDM’s experience is what happens when building software becomes a means instead of an end. A compiler – not one that turns BASIC into machine code, but one that turns problems into solutions. Our job is to keep the ideas flowing, and the factory running.


It happened to software first. I don’t think it’s going to stop there.


If you’d like to build something with a dark factory yourself, you should. There are a few options. You can read more of the team’s work at [https://factory.strongdm.ai/](https://factory.strongdm.ai/). You can try out a real implementation of their software factory at [https://github.com/danshapiro/kilroy](https://github.com/danshapiro/kilroy). Or – meat for another blog post – you can take a trip to the incredible, Mad-Max infused magic of [Steve Yegge’s Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).


Time to sharpen our axes.

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
