---
title: "The new philosophers"
subtitle: "How the modern data stack falls out of fashion."
date: 2023-04-07T16:27:37+00:00
url: https://benn.substack.com/p/the-new-philosophers
slug: the-new-philosophers
word_count: 2026
---


![](https://substackcdn.com/image/fetch/$s_!MJaj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec0e828a-a8f9-457f-81f5-4da5dfb655e7_840x360.png)

*Plato, aka the modern data stack, left of center. Aristotle, aka the next new thing, right of center. Socrates, aka Hadoop, not pictured.*


> What’s the Hadoop of today’s data ecosystem?


Shortly after I started working in tech in 2012, I attended my first data conference:Strata + Hadoop World. Held at the San Jose Conference Center, the same venue that hosted Apple’s and Facebook’s developer conventions, it was a confident coronation of the next big thing. Data vendors launched new products to packed auditoriums; customers, in scripted fireside chats, told us how digitally transformed they were; venture capitalists assured us this was just the beginning. The event’s premier sponsors—Cloudera, Hortonworks, and MapR—had raised hundreds of millions of dollars, pitched their software out of huge pavilions in the vendor hall, and were on the fast track to IPOs. Everything was ascendent: The startups, the ecosystem, and, most of all, therevolutionary promise of Big Data.


It didn’t go so well after that.


Hortonworks’ sharesfell by more than seventy percentin the two years after its IPO. When Clouderawent public in 2017, it was worth half its private market valuation. MapRblew up, and Hewlett Packard Enterprisebought its “business assets”for an undisclosed sum.1Strata rebranded toStrata Data & AI, and thengot canceled. Hadoop eventually became a one-liner: AtGartner’s data conferencethis year, our fling with Hadoop was the punchline of a lot of self-deprecating jokes, like anembarrassing high school ex that was never good for us.


Of course, we didn’t discard data entirely; instead, we moved on to a new thing. Hadoop-based or -inspired data systems likeHive,Pig, andImpalagot replaced by cloud data warehouses, which looked like ordinary relational databases, but very big, very fast, and relatively cheap. These products became platforms fordozens of new categoriesof data tools and hundreds of new companies.


Colloquially, we’ve come to call this collection of products the modern data stack. But that term represents more than just a set of tools; it represents the epochal sequel2to the era of Big Data. MapReduce was hard to write; Hadoop was hard to maintain; the data science initiatives that these tools were supposed to unlock were plagued by unusable data and brittle pipelines. The modern data stack was the reactionary counter-movement to these problems.3That movement includes toolsandphilosophical beliefs—SQL-first, cloud-first, decision support over fancy data science, modular over monolithic—that emerged organically, and were eventuallycanonized by dbt Labs. Their viewpoint became the industry viewpoint, something somethingZIRP, and the “modern data stack”—as an ecosystem of tools and as The Way make data valuable—went vertical.


But every movement, especially one as hyped and frothy as this one, will inevitably get some ideas wrong. Surely, something we’re excited about won’t pan out; surely, something will be our Hadoop.


Over the last eighteen months, I’ve asked a number of people what they think that might be. I’ve gotten a range of answers: ELT, streaming, the centralized warehouse, data catalogs, observability, theever-impressive, long-contained, often-imitated, but never duplicateddata mesh. Worthy candidates, all, but I can’t help but wonder if the answer is the entirety of the modern data stack. Just as the era of Big Data gave way to the modern data stack, it’s starting to feel like the era of the modern data stack is on the verge of being overtaken by the next counter-movement.


# 99 problems, 15 standards, 1 landscape


Like every startup pitch deck, every data talk has a few mandatory slides in its preamble. For years, one of the mainstays was a chart showing howdata volumes double every two years. The talk track was always the same: “Businesses aredrowning in digital papers, and we’re building MetaQuery.io to help.”


No longer. We’ve stopped talking about how data volumes are doubling, and started talking about datatoolsaredoubling.4Every presentation now opens with a screenshot ofMatt Turck’s MAD landscape from 2012—”This is what customers used to have to choose from.” Then, with a dramatic slide change—“Today, it’sthis”—they showMatt’s 2023 landscape. “And we’re buildingMetaQuery.aito help.”


The punchline is the entire modern data stack. It’s the now-widespread acknowledgement that there are too many tools, that we’ve created too many thin categories, and that what was meant to be a usable rewrite to Hadoop is now an unnavigable labyrinthine of tools and intertwined costs. If a Big Data platform was too hard to set up, deploying the modern data stack has been, if anything, tooeasy.


These frustrations have shown up in a number of ways. People complain about tools being disconnected and hard to manage.Meta-vendorslaunch productsthat manage other vendors for you.5There are constant rumblings about how much metered data warehouses cost. Some consulting firms market themselves around helping companies clean up and organize their dbt projects. Data quality is an ever-present problem. And new concepts likedata contracts,active metadata management, anddata control planesare direct efforts to control—and make a market from—the chaos that the modern data stack can often create. We had 99 problems, so we used the modern data stack—andnow we have 100 problems.


In fairness, none of these issues are necessarily fatal, or even unexpected.Progress isn’t linear. We experimented; we found some things that work and some that don’t; we’re experimenting again. The best problem any new technology can have is thatpeople want to use it too much.


Moreover, most of these new ideas aren’t rejections of the modern data stack’s foundational tenets, but iterations on top of them. Thoughattention-seekinghecklerscriticize the modern data stack’s edges because there are likes and subscribers to be had by starting fights,6most of us still agree with the modern data stack’sgospel. We complain, but rarely offer an alternative philosophy.7


Six months ago, I thought this was a steady equilibrium—two steps forward, one cynical blog post back, and messy progress for years to come. But in the last few months, I’ve changed my mind. I now believe we’re in the liminal8space between two eras. In a few years, we’ll see this time as when we faded away from the modern data stack, and moved towards intelligent infrastructures.


# The next discontinuity


I have a theory that technological cycles are like the stages ofSquid Game: Each one is almost entirely disconnected from the last, and you never know what the next game is going to be until you’re in the arena.


For example, some new technology, like the automobile, the internet, or mobile computing, gets introduced. We first try to fit it into the world as it currently exists: The car is a mechanical horse; the mobile internet is the desktop internet on a smaller screen. But we very quickly figure out that this new technology enables some completely new way of living. The geography of lives can be completely different; we can design an internet that is exclusively built for our phones. Before the technology arrived, we wanted improvements on what we had, like the proverbial faster horse. After, we invent things that were unimaginable before—how would you explain everything about TikTok to someone from the eighties? Each new breakthrough is a discontinuity, andteleports us to a new world—and, for companies,into a new competitive game—that would’ve been nearly impossible to anticipate from our current world.


Artificial intelligence, it seems, will be the next discontinuity. That means it won’t tack itself onto our lives as they are today, and tweak them around the edges; it will yank us towards something that is entirely different and unfamiliar.


AI will have the same effect on the data ecosystem. We'll initially try to insert LLMs into the game we're currently playing, by using them to help us write SQL, create documentation, find old dashboards, or summarize queries.


But these changes will be short-lived. Over time, we'll find novel things to do with AI, just as we did with the cloud and cloud data warehouses. Our data models won’t be augmented by LLMs; they’ll bebuilt for LLMs. We won't glue natural language inputs on top of our existing interfaces; natural language will become thedefault way we interact with computers. If a bot can write data documentation on demand for us,what’s the point of writing it down at all? And we're finally going to deliver on the promise of self-serve BI in ways that are profoundly different than what we've tried in the past.9


As these changes—and dozens of others that we can’t anticipate—start to come into focus, a new set of philosophical beliefs will likely coalesce around them. We’ll figure outnew ways to structureAI-powered technology stacks and AI-enabled data teams; at some point, as the good ideas separate from the bad, someone willpin a new set of thesesto the modern data stack’s door.


If this happens, the tenets of the intelligent infrastructure could quickly outpace those of the modern data stack as the next new thing. AI technologies are advancing at a breakneck pace, and they've already captured the imagination of the enterprise data ecosystem in ways the modern data stack still hasn't. For the Fortune 500 buyers at the recent Gartner conference, the modern data stack is an up-and-coming flirtation. LLMs, by contrast, were already everywhere, with vendors and CIOs scrambling to adopt it.


# Evolve, or die


The week after Gartner's conference, I attendedData Councilin Austin. At one point, I found myself in a conversation with a newly-minted founder who told me they were excited about their company's potential because it could ride the momentum of generative AI and of the modern data stack.


On AI, yes, of course. ChatGPT proved to be the only thing that could replace Elon Musk as the permanent main character on Twitter;10weeknight AI meetups in San Francisco are now better attended than major data conferences. For better or for worse, there’s no shortage of momentum in AI.


But the founder’s comment about the modern data stack struck me as something between anachronistic and contradictory. Though I don't believe the tools that make up the modern data stack will fail, the modern data stackas a movementseems incompatible with the rise of AI. It's a philosophy that was designed for a world in which reasoning through a data problem with a robot was a fantasy. That philosophy may be no more suitable for the world run on LLMs than MapReduce is for a world run on Snowflake.11


That’s is the reality that data teams and data vendors both have to reckon with. Our world is changing; the future we’ve been fighting to create may soon become the past that we have to fight to escape. For the modern data stack,this is it.

[1](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-1-113305279)

And for a $69.99 negotiation fee,GoDaddy will help you negotiateto buy the domain mapr.com.

[2](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-2-113305279)

Get it???

[3](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-3-113305279)

I’vejoked beforethat the best definition of the modern data stack is data tools that launched on Product Hunt. It’s not an entirely accurate definition—Snowflake was never on Product Hunt, for example—but it gets at the right idea for me: That the modern data stack isn’t an actual stack, but the era when data tools become cloud-first, bottoms-up, and community-oriented. This definition also excludes tools like Oracle’s Autonomous Data Warehouse and PowerBI, which I suspect most people would sayaren’tclear members of the modern data stack.

[4](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-4-113305279)

YC’s Law: The number of data companies in YCdoubles every two years.

[5](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-5-113305279)

I’m apersonal investorin both 5x and Mozart Data.

[6](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-6-113305279)

Get rekt,@bennstancil.

[7](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-7-113305279)

You could potentially argue that the data mesh isan alternative ideology. I don’t think I’d quite agree with that; to me, it feels more like a recommendation on how to make the modern data stack scale within very large companies. But some people may see that differently.

[8](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-8-113305279)

I swear, I went thirty-some odd years without knowing that this word existed, and now it’severywhere.

[9](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-9-113305279)

Given that my day job is to build aBI tool, I’ve thought way too much about this one. A longer post for a different day.

[10](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-10-113305279)

It’s unclear who will destroy humanity first.

[11](https://benn.substack.com/p/the-new-philosophers#footnote-anchor-11-113305279)

Of course, it’s also possible that AI is a flash in the pan; that the modern data stack is the tortoise that’s still going to win the race; and that now is the perfect time to build boring analog products when all the competition is distracted by something else. During a gold rush, sell pickaxes—or stay in Ohio, and be the only carpenter in town.
