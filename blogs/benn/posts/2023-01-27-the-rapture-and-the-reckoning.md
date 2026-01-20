---
title: "The rapture and the reckoning"
subtitle: "I'm a believer—AI will change everything about data too."
date: 2023-01-27T17:55:04+00:00
url: https://benn.substack.com/p/the-rapture-and-the-reckoning
slug: the-rapture-and-the-reckoning
word_count: 2274
---


![the end is nigh | The End is Nigh sandwich board near the en… | Flickr](https://substackcdn.com/image/fetch/$s_!NAFf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b4b0b56-4c54-4017-86dc-b034c8799142_1024x687.jpeg)

*The mess-AI-ah is coming.*


Give me a Bible and a bullhorn; the end is near.


All the work we’ve put in to building the modern data stack is on the cusp of being undone. Hard-won theologies will be proven wrong;the day of judgmentwill come for our mighty Babylon. That great city will be thrown down; it will be cast into the sea, and dozens of promising SaaS toolsshall be found no more at all.


Theprophetswere right. AI will change everything.


Admittedly, I didn’t believe them at first. Yes, large language models like ChatGPT are impressive, and image generation software likeStable Diffusionis breathtaking, but I never saw how this technology would meaningfully change the data industry. Most early converts would just point to ChatGPT, make a comment about how it can pass the bar exam, and handwave past how, exactly, this would change the day-to-day job of a data team.


So far, its real applications have been either trivial or underwhelming. AI might help us identify defects in our data or anomalies in our metrics. Neat, I guess, but hardly transformational. It mightmake us more creative analysts. Again, an improvement in degree, not in kind.


What aboutreplacing analysts with a chatbot?Thatwould be a revolution—but we’re not anywhere close to it being possible. On the surface, early efforts like these to generateSQL with ChatGPThave been extraordinary. With shockingly little input and tuning, it can turn English questions into working queries. Though it’s only right about half the time—which isn’t close to good enough1—that also means, when asked to perform a task that a tiny fraction of adults could do, it’sright half the time.


But these impressive demos are just that: Impressive demos. Though they aren’t exactly scripted, they’re run in tidy sandboxes that don’t resemble anything close to real data environments. The chatbot, for example, was built against a databasewith three tablesand 32 columns. Everything was simply and sensibly named, mostly using words that can be looked up in a dictionary. The test questions were basic, unambiguous, and could be answered by an experienced analyst in a handful of lines of SQL.2


The distance between this and companies’ actual data ecosystems is staggering.In a webinar earlier this week, Tristan Handy, the CEO of dbt Labs’, said that a meaningful percentage of their customers are using dbt to create more than 5,000 tables. These tables are often named with unintuitive and idiosyncratic idioms and abbreviations, and are littered with ambiguous words, like accounts and transactions, that mean different things in different contexts.3There are no simple questions—answering “How many new European accounts did we add last week?” requires defining an account, what new means, where Europe is, when a week starts,in what time zone it should be calculated in, and if “add” means net or gross. And there aren’t often simple answers—the average query in Mode is 75 lines and 2,700 characters long.


If ChatGPT is already unacceptably bad inimpossibly agreeable environments, it would be abysmal in the real world. To borrow again from Tristan in the same webinar, the early attempts to use AI to write SQL queries (to answer questions or to generate dbt models) are akin to our efforts to build self-driving cars. Practically overnight, both went from it being the stuff of science fiction to appearing tantalizing possible. But theprogress bar is a mirage. The edge cases—the construction sites, the unexpected traffic patterns, the school zones; the messy schemas, the bespoke metric definitions, the complex questions—are far,farharder than highways and dummy databases we got excited about. And I would guess that this is particularly true for using large language models to write company-specific queries. It’s hard enough to build a self-driving car that can navigate complicated neighborhoods; it’s quite another if every single one of those neighborhoods has its own traffic laws, follows different traditions, and has never bothered to write any of it down.4


The inevitable revolution in data, it seems,  would arrive at the same time as ourautonomous cars:5Tomorrow.Alwaystomorrow.


# Where we're going, we don't need roads


But maybe our problem is easier. Contemplating the problem of self-driving cars, Balaji Srinivasan—who may well be a chatbot himself, trained exclusively on backwater crypto subreddits, the University of Austin’s “curriculum,” andFuture, Andreessen Horowitz’s techno-optimism content marketing program6—proposed a solution:Rebuild the roads.


Balaji’s tweet was ratioed into oblivion.7Putting aside the fact we already have these roads—they're called train tracks—at our current pace of improvingtwo milesof road everysix years, we’d be able to replace allfour million miles of roadsin the United States by the year 12,002,023.8


Still, Balaji’s tweet highlights a useful trick. To solve a problem, we can solve it outright—or we can change the problem. Rather than asking self-driving cars to navigate hopelessly complex terrain, we could bulldoze the terrain into something more manageable.


The same principle applies when we ask an AI to analyze today’s sprawling and labyrinthine data structures. We could demand it figure them out, or we could refactor them into something more consistent. And unlike our roads, these models are just code—they could be rebuilt, not inmeggannums, but in days and weeks.


# Back to the future


Two decades ago, the data industry’s holy wars weren’t about meshes or contracts, butwarehouse schema design. Should tables be wide or narrow? Should multiple tablescontain redundant informationto make queries faster by avoiding joins? How shoulddata martsbe used? These questions mattered because databases were much slower and more expensive back then. But an organized warehouse was a faster warehouse, so IT teams that rigorously chose and stuck to a consistent set of governing principles could squeeze out better performance. The only way to cook efficiently in a small kitchen isby putting everything in its place; the only way to work with an old database is to be disciplined about how you structure your tables.


As warehouses have gotten faster, we’ve backed away from these principles. Part of that is intentional—ideas that were canon fifteen years agoare now outdated. Part of it is also probably necessary—the average Fivetran customer, for example, is extracting data from about 25 different services;9it’s very difficult to apply a single design pattern across such a diverse range of sources. But most of our slow abandonment of old design principles feels like intellectual drift. Without yesterday’s performance constraints, we can lazily relax our standards. And more importantly, the accessibility of the modern data stack and tools like dbt make it possible for anyilliterate clownto cosplay as a DBA.


The results are predictably chaotic. Like most otherKids These Days,10I don’t design our databases based on the actual teaching of Ralph Kimball or Bill Inman, butin accordance with what I think their wishes might well have been. Fact and dimension tables aren’t oriented around tight star schemas; they’re instead just a naming convention forseparating tables of events from tables of objects. Most schemas aren’t intelligently designed; they’re emergent, the result of an evolving web of new models that are continually added to the dbt DAG. There is no law governing how the database should be organized; there’s convention and a bunch of halfway-educated best guesses.


Amid this chaos, there have been some calls todefine schema design standardsfor the modern data stack. Of course, we shouldn’t try to go back to the same patterns we used a decade ago; we need new ones, for the people, data, and technology we have today.


But why stop there? As messy as the current world is for us, it’s kryptonite for an AI. What if instead of building new patterns for people, we built them for our AI gods?


A few years ago,Narrator, a product inspired by tools inside of WeWork, proposed a design pattern that they called theactivity schema. If nothing else, I give it points for audacity: The entire blueprint is one giant event table. It’s as if you took a star schema, joined every dimension table onto its corresponding fact table, and then unioned all of those fact tables together into one bottomless list of events.


Assuming this approach doesn’t have structural limitations (i.e., there aren’t questions that it can’t answer that other schemas could), its biggest problem might be usability. For analysts who are accustomed to thinking about relational models, working witha single event stream and a bunch of self-joinsfeels pretty unnatural.


For ChatGPT, however, this could be trivially easy—far easier than stepping through a convoluted series of joins. Moreover, because the activity schema is heavily standardized, an LLM doesn’t need to be deeply aware of the individual idioms within each company that wants to use it. Train a general model with a bit more detail about activity schemas, prompt your version of it with the basic documentation of the events contained in your stream—in other words, put the car on the traffic-free interstate and tell it the traffic laws—and see how farthat'llgo.11


# Judgment day


To be clear, Narrator’s activity schema is meant to be illustrative, not prescriptive. I haven’t used it in meaningful ways, and I have no idea how ChatGPT would actually interact with it. The point, though, is that it seems unlikely that the schema design patterns that we created for people are optimized for LLMs. As theskeptics of the chatbot analyst correctly pointed out, it’s the relational nuances that confuse AI models. But we could flip that. If AI-powered analytical tools have enough potential—which, seeing what ChatGPT can do, it seems like they do—would it not make sense to favor schema design patterns that enable the big-brained computers more than they enable us feeble-brained apes?


If something like this works, it’s a bomb that blows up half of the data industry. For data consumption, it would be like replacingAOL channelswith search. Instead of leafing through a sitemap of existing reports, people could ask for what they need directly. Analysts would either become less relevant, or would finally be freed up to work onmore interesting things.12


Analytics engineering would be recast as well. Today, analytics engineers have to translatecomplicated technical schemasinto semantically useful ones that have to make sense to the people who use them. That’s an architectural job, it’s a creative job, andit’s hard. Schema models designed for LLMs, by contrast, would probably come with a spec. Because the model wouldn’t need to be semantically expressive—LLMs find patterns, not meaning—that spec would likely also be relatively simple and consistent. Our transformation layers wouldn’t be inventive kitchens, figuring how to design bespoke dishes for individual customers. They’d instead become factories, stamping out the same standardized and machine-readable perforations that everyone else does.


This would also make our data more reliable. Not only is something like the activity schema easier to produce than a complex logical mesh of tables and metrics; it would also be much easier to monitor and debug. Observability tools wouldn’t need to be anything more than an QA tester on an event stream assembly line.


The implications of this would be profound. For decades, we’ve thought about building data tools and processes for people. They’ve been our best analysts, our best query writers, and our best decision makers.


But I’m not so convinced that’s true anymore—and the only thing that’s keeping us on top is we’ve rigged the game in our favor. If that changes, if we design our worlds for AIs,if we give our power and strength unto the beast, we might be able to go much  further than we can today. A new heaven and a new earth will come, and thefirst heaven and the first earth will pass away.

[1](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-1-99275606)

Nobody’s going to use a tool that is randomly and confidently incorrect half the time, or even ten percent of the time. No CEO will send a financial statement to the board that misstates one in ten metrics wrong; no operations team will manage their inventory based on order volume reports that have a ten percent chance of being wrong.Spectacularly bombing a mathematical riddleis one thing; invisibly issuing a bad SEC filing is quite another.

[2](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-2-99275606)

None of this is meant to be critical of either blog post, neither of which claim to be anything more than experiments.

[3](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-3-99275606)

Are accounts…customers? People who signed up for a product? Shared workspaces for collections of users? TheSalesforce account object? TheStripe account object? And transactions—are they customer orders? Credit card payments? Web events? TheSalesforce transaction object? TheStripe transaction object?

[4](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-4-99275606)

Some people drive on the right side of the road, some on the left, and lunaticsdrive down the middle.

[5](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-5-99275606)

And our free beer.

[6](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-6-99275606)

I mean,read thisand tell me it’s not at leastpossible.

[7](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-7-99275606)

Balaji’s 9.1 quote-tweet-to-retweet ratio was higherthan the 7.9 Matt Yglesias put up whenwell ackshually’ed the Uvalde shooting, but far lower than the 51.3masterpiecethat Nate Silver dropped when he compared Covid school closures to the invasion of Iraq.

[8](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-8-99275606)

True longtermism isn’t worried about our great-grandchildren, but about the world 400,000 generations hence, when the only surviving life is a few mountain lichens, a handful ofhorseshoe crabs, andPeter Thiel’s immortal husk.

[9](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-9-99275606)

In 2022, Fivetran said they were syncing data from100,000 connectorsfor4,000 customers.

[10](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-10-99275606)

Ok, somehow Lenovo Tiktokisn’tbad.

[11](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-11-99275606)

Are there already two decades of history behind this idea?Probably.But what is a data Substack if not a place to rebrandold ideaswithnew names?

[12](https://benn.substack.com/p/the-rapture-and-the-reckoning#footnote-anchor-12-99275606)

Yes, there are already tools like Thoughtspot that sorta do this. The difference is that these tools either require a semantic model to work, or are tripped up by the same problems that confound today’s ChatGPT bots. The point here is to back up a step: Can we structure our data such that these tools work on complex questions without predefined semantic configurations?
