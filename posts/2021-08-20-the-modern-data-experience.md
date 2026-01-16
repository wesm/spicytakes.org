---
title: "The Modern Data Experience"
subtitle: "How a revolution comes together. Or doesn’t."
date: 2021-08-20T15:45:08+00:00
url: https://benn.substack.com/p/the-modern-data-experience
slug: the-modern-data-experience
word_count: 2785
---


![](https://substackcdn.com/image/fetch/$s_!4HeV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3e6157f-9c2e-4c5f-89a1-ae36cd255523_1200x630.jpeg)


What is the modern data stack?1


To analytics engineers, it’s a transformational shift intechnologyandcompany organization. To startup founders, it’s arevolution in how companies work. To VCs, it’s a$100 billion opportunity. To engineers, it’s adynamic architectural roadmap. To Gartner, it’s thefoundation of a new data and analytics strategy. To thought leaders, it’s adata mesh. To an analyst with an indulgent blog on the internet, it’s anew orientation, anew nomenclature, andabunchofotheresotericanalogiesthat only someone living deep within their own navel would care about.


It’s easy to see why we’re all so excited. Our new technology is impressive, and lots of things that used to be hard, time-consuming, and expensive are now easy, fast, and cheap. In 2013, I worked on a data team that paid seven figures for a database that went down regularly, hired a full-time engineer to build and maintain a daily job to copy data from Salesforce into that warehouse, and employed an entire team of developers to build an internal tool for analysts to write and share SQL queries in a browser. Today, you can do all of thatin 30 minutes, for free.2


But to the everyday analyst and “business user,” the modern data stack is decidedly less fantastical.


To most people—pleasant, social people, the kind who can make it through a party withoutarguing about SQL formatting—the modern data stack isn’t an architecture diagram or a gratuitous think piece on Substack or a fight on Twitter. It’s an experience—and often, it’s not a great one. It’s trying to figure out why growth is slowing before tomorrow’s board meeting; it’s getting everyone to agree to the quarterly revenue numbers when different tools and dashboards say different things; it’s sharing product usage data with a customer and them telling you their active user list somehow includes people who left the company six months ago; it’s an angry Slack message from the CEO saying their daily progress report is broken again.


Toborrow an analogyfrom Erik Bernhardsson, if the modern data stack is a restaurant, these frustrations are how it feels to eat there. As the chefs, we’ve made some amazing optimizations in the kitchen. But our customers (which includes ourselves as analysts) are here for a good meal, provided by an attentive staff, in a pleasant environment. Until we can serve them that, our technology, no matter how revolutionary, is academic.


Our first reaction to this problem is to create more technology. We draw maps of what we’ve built, and look for small spaces in our diagrams to wedge new products and companies. Though each tool serves its niche better than what was there before,fracturing the market into smaller and smaller piecesdoesn’t solve the larger problem. As Erik said, hyperspecialization makes us great at chopping onions and baking apple tarts, but it’s a bad way to manage a restaurant.


Our other scapegoat is “culture,” loosely defined as some combination of the skills we have (ordon’t have), theorganizational structuresof our teams, and squishy terms likedata literacy. Though I’m sympathetic to these points, as are our Davos-bound aristocracyinterviewed by the Harvard Business Review, data cultures don’t materialize out of employee handbooks or internal seminars. The structures of our technologies and organizations till the land from which they grow. If people aren’t excited about the future we’re promising them or are put off by work required to be “data driven,” we can’t just ask them toplease get on board. We have to earn their enthusiasm.


To do that, the modern data stack isn't enough. We have to create a modern dataexperience.


# The other modern data stacks


Over the last several months,catalyzed by a postby Emilie Schario and Taylor Murphy, it’s become popular to say that data teams should think of everything they create as a product, and the rest of their colleagues as their customers. To build on this idea, what should that product be? What should it feel like to go from question, through technology and tools, through collaboration and conversation, to an answer?


Our current solution, though full of pieces that are individually great, is a disjointed one. Some responsibilities, like metric governance, are shared across multiple tools; others, like tracking what happens after a question is answered,are mostly ignored. Even seemingly basic questions, like "where do I first go to ask a question?," don't have clear answers.


It doesn't have to be this way—and that's not just hope. Airbnb, Uber, and Netflix built entire integrated stacks, from analytics tools, reporting applications, metrics repositories, data catalogs, and ML platforms. Unlike vendors in these categories, tools in internal platforms support a goal bigger than themselves. The results are impressive.


At Uber, employees cansearch for a metric, visualizeit across different dimensions, and move from code-free exploration directly into writing queries, all while an AI ensures that work doesn’t get repeated.3Airbnb built a similar platform, connecting a data catalog and a metrics repository with a data exploration tool and a SQL IDE. AndNetflix designed an entire workflowfor creating, sharing, deploying, scheduling, and discovering notebook applications that support everything from dashboards to production models.


Undoubtedly, these tools aren’t perfect.4But they offer a window into the bigger questions we should be asking: How should it feel to use modern data stack? What can the system add up to? What’s the best way for people to answer an unfolding series of questions, to trust those answers, and to decide what to do next? What can we create for people who care about how well the modern data stack works, regardless of where the lines are drawn between products and services? What are we building for the people who are at our restaurant to enjoy their dinner, and don’t care who prepared the onions or how they did it?


# Trading ideas


I’m under no illusion that the market can or should agree to a singular vision, at least not today.5Regardless of your preferred definition of the modern data stack, nearly everyone, myself included, agrees that it should bedecentralized.


This isn’t a call to create a council to dictate a roadmap from on high, or for a company to build some integration umbrella under which we can all live.6It’s also not an ask for more conversations about the philosophical underpinnings—cloud-first, modular over monolithic, version control and peer review—inspiring what we build. Instead, it’s an acknowledgement that decentralization comes at a cost: Our architecture becomes our user experience. Fault lines between products become fault lines in how it feels to use the modern data stack—and for most people, that’s what matters most.7


This is, bluntly, not an easy problem. How does a multitude of sovereign, often competitive entities come together to build something cohesive?


One potential guide comes from a much,muchmessier market: international trade. Prior to World War I, most multinational trade agreements—treaties on tariffs and trade restrictions—werebilateral agreements between two countries. As countries in Europe industrialized, “a network of bilateral trade agreements” emerged, centered around and often dictated by key trading partners—in the European case, Britain and France.


In 1947, after an interlude for a world war, a Great Depression, aprotectionism fad, and another world war, twenty-three of the world’s major trading partners signed the General Agreement on Tariffs and Trade, orGATT. Because of the importance of the GATT’s original members, over the next half-century, the agreement attracted more signatories. It was eventually succeeded by the World Trade Organization in 1995; today, the WTOhas 164 members, accounting for 98 percent of international trade. Though many countries still negotiate bilateral or regional trade agreements, world trade is generally governed by global WTO treaties rather than a complex web of thousands of bilateral agreements.


The data ecosystem is tracing the same path. Today’s stack currently operates as hundreds of member states, orbiting around major platforms like Snowflake, Fivetran, dbt, and a few others. To the extent that we concern ourselves with how vendors relate to one another, we do so through bilateral integrations, mostly to caulk over gaps betweenone productandthe next.


In the ballooning ecosystems of both global trade and data tools, bilateral integrations won’t scale. A messy patchwork of agreements will—and did—come apart under stress. The GATT and WTO are an admission of that. Built outward from the world’s largest economies, these agreements created a shared vision for trade policy that, even if it wasn’t always legally binding, helped tilt the world in a common direction.8If we want to makethismarket work, we need a similar set of guiding principles.


# The Modern Data Experience


If the modern data stack provides an architectural roadmap, these principles should provide an experiential one. They represent the aspirational standard for how our new tools work together, and what they can collectively become.


In thespirit of dying on some hills, these are the ambitions I believe we should have. To me, the modern data experience…


...enables everyone to do their job rather than asking them to be an analyst.Data democratization was a trendy catchphrase with worthy goals: Make the value of data available to everyone, and free up data teams to work on strategic projects. But it became a prescription—make everyone an analyst with code-free tools—that largelyfailed us. In a modern data experience, we don’t hand people data and ask them to analyze it; weincorporate it into the operational systemswhere they already live. Data shouldhelp people do their jobs, rather than add a new job for them to do.


...merges BI and data science.We often think that analysts work in technical tools, and everyone else lives in BI apps.That’s wrong.Drag-and-drop tools can be valuable to senior data scientists, and anyone can be a consumer of advanced analysis. As Bobby Pinero put it recently, “analysts are becoming positionless.” In the modern data experience, people should transition seamlessly between viewing a key metric sourced from a well-vetted data catalog, to exploring that metric with groupings and filters, to incorporating it in deep technical analyses. Those consuming data should never have to fully leave one system and start over in another.


...makes status and trust explicit.“Can I trust this?” is one of the most frustrating—and common—questions people ask of data. Today, our answer to that question mostly depends on implicit signals: Who built it? Did it change recently? Does itlookright? This leads us down endless multi-tool chases to confirm our results. Indicators of trust need to be explicit: Every data asset should show if upstream processes are operating abnormally, out-of-date, or in some state of development or disrepair. Our goal should be to spend more time debating what to do because of a number on a dashboard than we spend verifying if that number’s right.


...remembers what we’ve learned.Discoveries in BI tools are ephemeral, lost when a dashboard updates or its configuration changes. Ad hoc analysis is haphazardly recorded among a sea of scratch work. Conversations about both, where decisions are made and knowledge actually accumulates, are washed away by the Slack firehose. To make sure our time is spent exploring new territory rather than retracing old steps, a modern data experience should remember and catalog what we learnandwhat we say about it.


…governs business logic globally.Historically, business logic—instructions for transforming data and computing metrics—is governed locally, within individual BI tools and one-off analyses, with little coordination. In a decentralized, modular stack, this creates a patchwork of duplicative and often contradictory calculations. A modern data experience should centralize this logic such that it’s accessible anywhere data is consumed, whether that’s a BI dashboard, a Python notebook, or an operational ML pipeline.


...doesn’t communicate in only tables.Steep yourself in data long enough, and all you see are relational structures: tables, rows, columns, join keys. Most data tools reflect this view, and present datathis way.This is lazy packaging.To analysts, data comes in this form; to everyone else, data is protean. Sometimes, it’s a metric on a time series; sometimes, it’s anabstract representationof a complex business domain; sometimes, it’s a document ofexplanatory narratives. People should be able to search for, ask questions of, and explore data in these terms, not just as tables and columns.


...builds a bridge between the past (read: Excel) and future.It’s tempting to treat the modern data stack as a discontinuity, a leap from the past into a better future. It’s not. It’s a transition, and some uncomfortable anchors are coming with us. Most notably, Excel isn’t going away. A modern data experience has to negotiate with it, not treat it as an outdated pariah.


...is elastic.Analysis isn’t a predictable, linear process that can be anticipated. It starts as one question, and opens into other questions. Similarly, data infrastructures evolve as the businesses underneath them change, data sources and structures change, and the analysis built on top of them uncovers new problems to track or opportunities to organize around. A modern data experience should be emergent in this way, able to start small and grow into new, unforeseen territory. Rigid experiences and systems are debt that will quickly come due.


...is a melting pot.Data stacks have a history of building walls to throw things over: data engineers throw pipelines at analysts; BI developers throw reports at their stakeholders; analysts throw results at anyone who will listen. Modularity can’t tempt us to build more walls. Just as dbt broke down the first wall, a modern data experience needs to break down the others by encouraging collaboration and conversation between business, data, and engineering teams. In other words, in the shorthand of the moment, the modern data experience ispurple.


There’s plenty more to say about each of these topics, and a lot more conversation to be had about how to refine this list. But it’s a conversation we need to have. Without it—without thinking about the experience that pairs with the stack—we can build the tools, and the things we’ve promised—a technological revolution, a transformation shift in how industries function, $100 billion!—won’t come.


---


# The data mesh postscript


Last week, Analytics Twitter melted down over The Data Mesh™ and what, exactly, it is. As best I can tell, there are now two definitions. Theoriginal definitionis a fairly complex set of architectural requirements. Its pillars are technical, and, as data mesh creatorZhamak Dehghani made clear, quite specific. The second definition—thedescriptivistone thecommunityisgravitatingtowards—is more vague, essentially claiming that any decentralized architecture in which teams are responsible for their own “data products” is a data mesh.


I have mixed opinions on the content of both definitions. However, I don’t have mixed opinions, and am decidedly opposed to, theformof the first definition.


According to its creators, the data mesh ismeant to addressthe failures of today’s data stack: It leads to “disconnected source teams, frustrated consumers fighting for a spot on top of the data platform team backlog and an over stretched data platform team.” In other words, the modern data stack needs a better modern data experience. However, rather than making that central to the data mesh, the original definition is a funhouse of specific technologies and buzzwords. I think we would be better served by talking directly about the experience we want to create, without running the conversation through a briar patch of technical diagrams. In many ways, that’s the point of this whole post: To talk about the goals of the data mesh, which are worthy ends, without getting mired in obscure details that, I believe, aren’t necessary for achieving those goals.

[1](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-1-40271466)

Pardon me while I pander to Google’s SEO gods.

[2](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-2-40271466)

Pardon me while I pander to Mode’s marketing team.

[3](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-3-40271466)

A fun bit of circular history: In 2009, the data team atPlaydombuilt an internal tool for running and sharing SQL queries. That tool inspired a similar tool at Yammer (my former employer), which then inspired the original idea behind Mode. Another member of Yammer’s data team left for Uber, and built the first version ofUber’s query tool, which is now inspiring all of us.

[4](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-4-40271466)

“I know they aren’t perfect but I've never felt this way for no one.”

[5](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-5-40271466)

We can’t even agree on how to buildbasic templatesfor the reports that everybody wants.

[6](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-6-40271466)

That said, my suspicion is that GCP, AWS, Azure, and perhaps Salesforce will attempt to do exactly this. I think all four will create data stacks that are similar to their cloud infrastructure stacks: Tightly integrated tools surrounded by a low wall that encourages, but doesn’t require, people to use other tools within the stack.

[7](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-7-40271466)

Consider this a particularly strong application ofConway’s Law, one of Silicon Valley’s favorite pop proverbs: The design of the modern data stack will reflect the org chart of those who build it—and, worryingly for us, those org charts span across many companies.

[8](https://benn.substack.com/p/the-modern-data-experience#footnote-anchor-8-40271466)

Reasonable people can disagree on whether or not that direction was a good one. My point is that this approach succeeded in creating a common framework at all.
