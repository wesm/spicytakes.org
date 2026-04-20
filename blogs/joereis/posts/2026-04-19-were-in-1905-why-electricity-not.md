---
title: "We're in 1905: Why Electricity (Not Dot-Com) Is the Right AI Analogy"
subtitle: "The Weekend Windup #29 - Cool reads, events, links, and more"
date: 2026-04-19T19:31:11+00:00
url: https://joereis.substack.com/p/were-in-1905-why-electricity-not
slug: were-in-1905-why-electricity-not
word_count: 2054
---


![](https://substackcdn.com/image/fetch/$s_!LVMe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9221669-9add-4004-b198-e6428426894b_1266x921.jpeg)

*A 1920’s era speculation on electrifying the farm. Source:Paleofuture.*


Everyone loves comparing AI to the dot-com bubble. It’s the most recent tech revolution we can point to, and the parallels are obvious: insane valuations, companies raising money by slapping “AI” on their pitch deck, the general pandemonium and silliness of it all. I was around during the dot-com era, and it was f*cking bananas. Money made from thin air…and also vanishing into thin air. Much like today.


But I think it’s the wrong analogy for where we are with AI today. And the right one is alotmore unsettling.


Paul David, the late Stanford economist, laid out the framework in his landmark 1990 paper “The Dynamo and the Computer.” Electric power showed up in factories in the 1880s. Labor productivity didn’t meaningfully accelerate until the 1920s. David’s later research with fellow Stanford economic historian Gavin Wright quantified the discontinuity: trend productivity growth jumped from 1.5% per year during 1899–1914 to 5.1% during 1919–1929. Same technology across both periods. Radically different results. So what changed?


The motors worked fine by the 1890s. The problem was that factory owners swapped their steam engines for electric motors and kept the same factory layout. Think of multi-story buildings, a central power shaft, and belt-and-pulley systems distributing energy to every floor. They bolted the new technology onto the old architecture. The real gains came only when factories were torn down and rebuilt: single-story layouts, individual motors per machine (”unit drive”), and workflows redesigned around electric power rather than steam constraints.


The architecture had to change, not just the energy source (in this case, steam to electric motors1).


## The Data Industry Has Been Swapping Motors for Decades


The data industry has been repeating this exact move for decades. For some reason, we have a hard time reimagining the possibilities of new modalities. Think of lifting and shifting an on-prem warehouse to a cloud warehouse. We’ll often keep the same data models, same batch ETL, same BI team bottleneck. I’ve seen teams try to run the cloud data warehouses the same as their on-prem ones, often with costly mistakes and cost overruns. We get faster motors, but the same old factory and habits stick around.


Along comes Hadoop, where we bolted asecondmotor onto the factory. Two centralized power systems, and even more belt-and-pulley complexity. We even added a data engineering team to maintain the second motor. But the broader enterprise decision-making patterns didn’t change.


The modern data stack is maybe the most egregious swap. Here, we swapped ETL for ELT, monoliths for a spawl of dozens of modular pay-as-you-go systems, and open-source. The architecture diagram looks different, but the organizational reality is identical: a centralized team, a centralized pipeline, and centralized consumption. Shinier equipment, but still the same factory layout from decades before.


And now AI. I see many companies simply bolting LLMs onto corporate files and folders (CoPilot on SharePoint, or similar), slapping a chatbot on the warehouse, and similar machinations. Maybe there are agents running around. But this isn’t that interesting and doesn’t fundamentally change the underlying architecture. And more importantly, the org design hasn’t changed. This matters a ton because of Conway’s Law.


Here’s something I hear a lot in enterprises, big ones especially. The executives buy Copilot subscriptions (sort of like pizza for the breakroom). Nobody uses them. The mandate comes down: use it, or you’re fired. Suddenly, everyone’s “using AI.” That’s the 2026 equivalent of bolting an electric motor onto your steam engine and declaring you’ve electrified the factory.


Even the more sophisticated moves can be traps. Companies using AI to accelerate code migrations. To be fair, rewriting COBOL to Java and moving legacy ETL to modern tooling (among other things) are getting real efficiency gains from AI. But zooming out, code migration isn’t fundamentally that interesting. We’re using the electric motor to rebuild the belt-and-pulley system faster. The code is newer and the architecture is identical. You’ve simply automated the construction of the old factory layout. It’s the most dangerous version of the motor swap because it genuinely feels like progress. You can point to measurable wins while encoding every assumption of the old architecture into the new codebase. You’ve paved the cow path with better asphalt. But it’s still a cow path.


## We Need to Rethink Today’s “Factories”


The old factory had a single central power shaft with belts distributing energy to every floor. Every machine was physically tethered. You couldn’t rearrange the floor because everything was constrained by the belt system.


We need to rethink our “factories.” For example, centralized BI operates similarly. One data team. One warehouse. A pipeline distributing insights through a belt system of dashboards and reports. Every downstream consumer depends on the central team’s throughput.


The analytics request queueisthe central shaft bottleneck. Same constraint, different medium, same problems. And we’ve been running this pattern since the 1990s. It’s clear that the improved tooling makes life tolerable, but it hasn’t solved the core challenges. We’re still wondering whether the data is high-quality, believable, and usable for decision-making, and so on.


In electrification, unit drive (giving each machine its own motor) unlocked the redesign. The factory could finally be organized around workflow instead of power distribution. For data, the equivalent means decision-making moves to where data is generated, operational systems become analytically aware, and AI gets embedded in business processes rather than accessed through a BI portal. It means the request queue disappears entirely, or is at least reshaped into something better.


That’s bigger than any technology purchase. And it’s why the MIT NANDA report’s finding, that roughly 95% of enterprise GenAI pilots fail to deliver measurable P&L impact, isn’t evidence that AI doesn’t work. It’s evidence that most enterprises are still bolting motors onto the old layout. The technology works. The architecture and traditional org layouts likely won’t. And that’s what we need to solve. AI can help us get there, but we need to fundamentally rethink how we approach incorporating it into our organizations.


## How Long Does This Actually Take?


David’s 40-year lag was partly physical. You had to demolish multi-story brick factories. Software and org charts are hard to change, but they’re not “tear down a building” hard. We also know about the pattern now. David’s paper exists, and Carlota Perez’s work on techno-economic paradigm shifts is widely read. We can see the trap even as we step into it.


But David’s key insight was that the bottleneck was never the technology. It was organizational design, incentive structures, workforce skills, and institutional inertia. That’s still slow. And here’s the part that doesn’t get enough attention: the factory owners who finally redesigned in the 1920s were often new entrants or next-generation managers who’d never internalized the old layout as normal. Today’s data leaders grew up in the warehouse paradigm. It’s the water they swim in, and we all know the old trope about asking a fish to describe water.


My rough estimate for the change is 10–20 years ofrealtransformation, not 40. But definitely not 3–5. A CoPilot subscription doesn’t magically transform you into an AI company. On the plus side, it seems every organization is adopting AI to varying degrees. But adopting isn’t the same as total integration into an organization’s fabric. And given the track record of how many organizations move with various replatforming efforts (internet, mobile, cloud, etc), they move slowly. How many companies are still in the midst of digital transformation, something that became popular a few decades ago? Replatforming and transformation are totally different things, and both take a long time.


We’re in 1905. The electric motor works, and everyone’s bought one. Almost nobody has redesigned the factory to fully optimize the motor’s potential.


## Is It the Tech, or Is It Us?


The companies that win the AI era won’t be the ones with the best tools. They’ll be the ones who tear down the factory or build a factory from scratch. History says most incumbents won’t do it. They’ll get replaced by new entrants who build the single-story factory from scratch. The ones who survive will be the ones who recognized early that the motor was never the point. The layout, ways of working, and org structure were what mattered. I suspect the same will happen with AI. Big companies will get eaten alive by hundreds or thousands of smaller competitors whoerode the edgesuntil there’s nothing left of the big company.


At some point, you’ve got to look in the mirror and ask: Is it the tech, or is it us? I think it’s us. It’s always been us.


Have a great weekend,


Joe


---


Here’s the YouTube/travel vlog version of this, live from Tokyo Japan.


Here’s this week’s Freestyle Friday podcast. Available on Spotify, Apple, and wherever else you get your podcasts.Please support the show with a review.It means a lot.


---


![Ellie.ai - Enterprise Data Modeling Powered by AI](https://substackcdn.com/image/fetch/$s_!YB3V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F085929fe-223b-4838-94f4-4678db81d663_626x200.svg)


Modern data modelers need to live at the intersection of business and tech.Ellie.aiallows you to collaborate effectively with business while maintaining credibility with the Tech team. Get contextual support from AI, reverse engineer anything building a repository of sources with synthetic AI generated contextual metadata while delivering insights via an MCP Server and integrating anything with full blown API support.


The full stack data modeling future is here today!


Thanks toEllie.aifor partnering on this newsletter.


---


# Awesome Upcoming Events


Here are a couple of things I’m up to. Much more to come, so stay tuned.


---


## Agentic Analytics Summit 2026


![](https://substackcdn.com/image/fetch/$s_!qwIM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5223ebea-a546-4f45-bb0d-0b54ec97d6da_1920x1080.jpeg)


A LOT is happening right now with AI + analytics + agents. The Agentic Analytics Summit will have lots of great speakers and the latest updates on this fast-moving space.Definitely register for the event. It’s free and will be awesome!


When: Wednesday, April 29. Starts at 9am PTWhere: Virtual


Register here


---


## Data Innovation Summit 2026 - Nordics


![](https://substackcdn.com/image/fetch/$s_!jtH1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0127c585-1f6e-42d3-881f-39e7d1e71c55_1920x1280.png)


🇸🇪 Sweden! See you at the Data Innovation Summit in Stockholm.


I’m doing a keynoteandworkshop on Mixed Model Arts: Data Modeling in the Age of AI.

- May 7 - keynote
- May 8 - workshop


Here’s 10% off: SD10OFF (good for the event. Workshop is not included)Register here


---


# Cool Videos and Reads


In this episode, I sit down with Bob Seiner, a true pioneer who has been working in data governance since before it was even called governance. We dive into why he calls BS on the trendy term "data enablement" and how his trademarked approach, Non-Invasive Data Governance, formalizes what organizations are already doing without beating employees over the head.We also unpack his latest concept, The Data Catalyst Cubed, and get into a fascinating discussion about the precarious state of data security in the age of LLMs and autonomous AI agents like OpenClaw.Plus, Bob shares some great war stories about building the T-DAN newsletter using Microsoft FrontPage back in 1997 and drops his best advice for standing out and building a personal brand in the noisy data industry.


---


### Here are some things I read this week that you might enjoy.


Do mega passes leave skiers and snowboarders better or worse off? | KSL.com


I Trained for the Paris Marathon Using ChatGPTThe Cheese in the Fridge


Trump’s White House Was ‘Awash in Speed’ — and Xanax


Robots captured Russian army positions for first time in history, Zelenskyy says – POLITICO


“This Wasn’t Just a Job; It Was a Trap”: A Former Infowars Staffer Tells All (Exclusive Excerpt)


US tech firms successfully lobbied EU to keep datacentre emissions secret | Microsoft | The Guardian


# Find My Other Content Here


📺YouTube- Interviews, tutorials, product reviews, rants, and more.


🎙️Podcasts- Listen on Spotify or wherever you get your podcasts


📝Practical Data Modeling- This is where I’m writing my upcoming book, Mixed Model Arts, mostly in public. Free and paid content.


# The Practical Data Community


The Practical Data Community is a place for candid, vendor-free conversations about all things tech, data, and AI. We host regular events such as book clubs, lunch-and-learns, Data Therapy, and more.


🤖Join on Discord


Thanks for reading! Subscribe for free to receive new posts and support my work.

[1](#footnote-anchor-1)

This is also where arguments about oil being a stronger analogy fall flat. Fuel is different from the machine the fuel uses. But that’s a rant for another post.
