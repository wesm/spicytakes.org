---
title: "How Snowflake fails"
subtitle: "Climate change comes for us all."
date: 2022-09-02T16:05:21+00:00
url: https://benn.substack.com/p/how-snowflake-fails
slug: how-snowflake-fails
word_count: 2610
---


![](https://substackcdn.com/image/fetch/$s_!D0aD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52c10657-c9c7-42bd-a841-d9e0befdf5dc_540x360.png)


If we had to mark the moment when our hubris peaked, sometime around 1 p.m. on March 24, 2022 is as good a point as any.


Like much of the tech industry, data companies came roaring out of the pandemic. Snowflake’srecord IPOin September of 2020 kicked off a gold rush for data startups, which accelerated through 2021 and peaked in early 2022. The default Series A term sheet was a $20 million raise on a working prototype and a $100 million valuation. Series B and C rounds were often priced at more than half a billion dollars, with founders taking more money out in secondary than their companies had ever booked in revenue.


The fever pitch came to a head in late March at Data Council, a long-standing community conference on data engineering. The event,full of vendors and VCs pitching to one another, felt less like a technology conference and more like a celebration of an industry that suddenly couldn't miss. At an afternoon panel on the 24th, an investor was asked if he was worried about the amount of traffic in the market. When a lot of companies chase the same problem, he was asked, how many can actually be successful?


"A fuckton," he said. “Go build a $100 million business. It’s all possible for everyone in this room.” The audience applauded.


We went full Ponzi scheme after that. In one reaction to the conference, a commentator speculated that as more data practitioners leave their jobs to found startups, other companies will have a harder time staffing their data engineering teams. They’ll need to buy data products because nobody will be able to build them, the argument went, creating an "almost a self-fulfilling prophecy that many of these data companies will be successful."


Icarus, may I introduce you to the sun?


Our fall was swift. The climate changed almost overnight. In early April, the stock market started atwo-month plunge, with the Nasdaq bottoming 25 percent below its value in March. Fundraising markets dried up. Venture capitalists sent outapocalyptic warnings. Companies started hoarding cash. The paved downhill road to success turned into an overgrown trail up a mountain.


Still, a few companies have proven well-suited for the climb. As we're often reminded by VCs in their corporate pep talks,the hottest fires can forge the most enduring companies. This downturn appears no different—and three companies, each representing the emerging default for theirrespective pillarsof the modern data stack, now seem poised to become the inevitable winners.


Snowflake, every analytics engineer’s favorite database, keeps piling upremarkable financial results. dbt is still the unchallenged hub of data transformation.1And Fivetran has consolidated its lead in ELT née ETL, building and acquiring its way into a position that its (biased, yes)board members have called “unassailable.”


I, and nearly everyone I talk to, subscribes to this consensus—so much so that I know more than one person who’s contemplating putting as much as half of their savings in Snowflake stock. But, just two years ago,we all marveledat Zoom’s financial performance. Since then, Zoom shares have fallen 85 percent. Slack, once hyped withbreathless coverageabout how it’s transforming the way we work, now makes$900 million a year—an impressive number, to be sure, but barely twice theestimated revenue of Edible Arrangements.2Do we all work in WeWork offices? WeDon’t. And I still don’t knowwhat happened to Magic Leap.


Sure things, in other words, aren’t always dominant.


In the spirit of beingthe tenth man, what if we’re also wrong about Snowflake, dbt, or Fivetran? What if we had to assume, five years from now, that each company fell from grace? What if it’s no longer the Silicon Valley darling, but the disappointment, the cautionary tale, the missed opportunity, the tragic has-been and once-was? What if they’ve been replaced by the new new thing, disrupted by a more exciting newcomer, and left behind by the community? If we have to take this outcome as a given—a future that is clearly possible, if unlikely—how would it happen?3How do these companies lose?


Let's start with Snowflake.4


Editor’s note: I was going to do this for all three companies in this post. But, I spent 700 words on frivolous preamble, and ran out of space. Fivetran and dbt, your dark timelines are coming later.


# It’s expensive, part I


We were always going to spend a lot on Snowflake. Data is often a one-way ratchet: We areconstantly collecting more of it, and trying to do more with it. Any company that meters that usage inevitably creates a pricing elevator thatpeople will complain about.


The data zeitgeist is slowly souring on Snowflake for this—though I don’t think it represents a real risk for Snowflake. Yes, if buyers become more cost-conscious, their bills probably won’t go up by the current average of71 percent a year. But it’s a fallacy to assume that high prices that arecreated by rising demandwill drive people away from Snowflake.


If you workaround economic policy, you sometimes hear arguments like this: If prices for a product rise, fewer people will be able to buy it. That will lead to less demand for it, so producers will sell less stuff and make less money than they would if prices were at their original levels. But this confuses natural prices increase set by the market with artificial prices increases set by sellers. In the former case, demand affects price. In the latter case, price affects demand.


The rising Snowflake costs that people complain about, which are driven by product adoption, are analogous to the first case. Price increases of this sort don’t “go too high;” they are simply what the market dictates them to be.


More succinctly, demand for Snowflake won’t go down because demand for Snowflake went up. And there’s a different between something being “expensive” and people buying a lot of it.


That said, it’s conceivable that the Snowflake’s ability to close large deals (and the natural need to chase bigger enterprise contracts) causes Snowflake to ignore the lower end of the market. This could create space for new players to undercut them, just asAmplitude did to Mixpanel. Though this dynamic is pretty common, it typically happens to well-established, dominant incumbents. Given that Snowflake is still a fraction of the size of Microsoft, Google, andOracle, Snowflake is still more disruptor than disrupted, and seems unlikely to cede control of the bottom of the market any time soon.


# It’s expensive, part II


Even if cost isn’t a weakness for Snowflake, however, it might be an opportunity for someone else. For better or for worse, Snowflake (and other warehouses like BigQuery and Databricks) have become the engine of the modern data stack. Most other data products lazily use Snowflake (et al) for their compute services, hiding the total cost of using them inside Snowflake bills.


Nobody has that much incentive to change this. Snowflake takes the pricing heat, so vendors aren’t as motivated to make their services as efficient as they would be if they had to justify the compute bill as part of their offering. And Snowflake probably doesn’t mind these services being inefficient; no gas station will complain too much if you buy anExcursion.


On one hand, the database provider can only do so much here. If you hammer Snowflake with queries, they can try to make those queries cheaper to process. But at some point, if you use it a ton, they’ll bill you a ton.


On the other hand, the warehouse could be smarter about which queries it processes and how. A database could come with abuilt-in battery saverthat’s less focused on pure technical performance, and more focused on optimizing how other data tools interact with it. Given how muchextraneous or redundant computetoday’s tools probably push through Snowflake,5I suspect you could squeeze considerably more savings out of streamlining how databases are used than you could by trying to outrun Moore’s Law. A database that figures this out could compete with Snowflake on price—not on the performance of each unit of compute, but on how useful each unit is.


# A modern data warehouse


This principle—be the warehouse for the modern data stack—could be extended to more fundamental characteristics of the database. To a user, the first versions of Snowflake were just a database, but big, fast, and stable. Yes, there was magic under the hood, but you’d never know that using it. If you’d given me an unlabeled connection to Snowflake in 2016, I would’ve thought it was Postgres on steroids.


As I’ve said before, I thinkthis was the right pitch—but it might not be the right foundation for the future. We’re starting to ask databases to do lots of things that Postgres can’t do. We want them to be transactional and analytical; we want them to power machine learning infrastructure; we want them to be semantically aware of their contents; we want to build operational systems on top of them; we want them to power advanced analysis in Python and R; we want them to support interactive data exploration; we want them to host their own applications; and we want all of it to happen in real time.


Though Snowflake clearly wants to do all of these things too, they could be awkward fits. Snowflake’s bones weren’t (I don’t think?) built for polyglot querying like Databricks, to support native APIs like BigQuery, to embed semantic models likeRelationalAI, for streaming data likeMaterialize, or for interactive analytical queries likeFirebolt; they were built in a time when databases were, well, databases. In ten years, that could prove to be outdated, and Snowflake’s new features could be—like an on-premise provider stumbling their way into a clumsy cloud offering—a facade on an aging foundation.


# The retro data warehouse


Or, the opposite could happen. The effort to redefine the database as something between acloud provider and an operating systemmight break down under its own weight. This sort of offering could become too confusing, too complicated, and too hard to manage. Longing for simpler times, the pendulum swings back the other way—towards big, dumb, basic databases that just store data and run queries. Liketouch screens in cars, just because we can build a database with lots of technical bells and flashy whistles doesn’t mean weshould.


As an aside, if I were in charge of Redshift, this is the bet I’d be making. The war for the “data cloud” is lost. But does every business need such a heavy solution? No—some might want a simple warehouse that’s fast, reliable, and predictably priced. Make it easy to spin up; make it easy to buy; make it easy to load a CSV into. Don’t chase the glittering lure of technology. Take us to the time we ache to go again; be the analog, stick shift database.Sell us nostalgia.6


# Picking the wrong fight


If we do prefer our newfangled all-in-one digital databases—if we want a data platform and not a data warehouse—Snowflake would likely expand aggressively into new markets and product lines. This could open a lot of fronts of competition, and Snowflake might not have the resources to win them all.


You can already see this happening. During the keynote at Snowflake Summit, Snowflake said they were committed to their technology partners—while simultaneously announcing new features that directly compete with a number of those partners. If this expands further, and Snowflake fully embraces its ambitions as a “data cloud,” they could also start competing more directly with cloud providers too.


In that war, all bets are off. They might alienate the ecosystem. They might find themselves at war withGoogle's tech,Microsoft's money, andAmazon’s market share. They might isolate themselves as an oversized database vendor and an undersized cloud provider. Under these conditions, in a war of attrition against a bigger opponent,even the invincible become vulnerable.


# A margin squeeze


Ok, this one’s a bit weird for a company withsixty percent margins, but hear me out.


Last fall,Erik Bernhardsson made the casethat AWS and other cloud providers might be happy to sell core compute services like EC2, and let other vendors—Snowflake, for example—do the hard work of building, marketing, and distributing applications on top of it.7Some businesses will build rich applications on top of these services, and sell them at a huge premium over cost. Others, however, will end up mostly repackaging compute and storage at a huge scale.


Snowflake has clearly built a lot of technology on top of AWS, GCP, and Azure. But, if this ends up as mostly extraneous—i.e., if we mostly just want a database to store and query data—Snowflake could slowly drift towards being a lower-margin reseller of cloud compute. This could encourage Snowflake to build its own cloud, opening, again, a dangerous and expensive front against the current cloud providers. Wall Street would start scrutinizing Snowflake’s expenses, just as their margins start to tighten. And that combination can turn around a business’s momentum in a hurry.


# Karma


Snowflake’s original sin—the hideous decision touse capital letters everywhere—finally comes home to roost. Elon Musk loses his lawsuit against Twitter, buys the company, and immediately reinstates Donald Trump’s account. Trump blasts out his first tweet in all caps—“END THE LIBERAL SNOWFLAKE!!!”—and Elon Musk retweets it. Republicans, assuming that Trump is talking about the data company, boycott Snowflake in favor of the database they believe was made for them: Redshift (#turnSnowflakeRed). Democrats, assuming that Elon Musk’s retweet means that Elon Musk will try to buy Snowflake, boycott it in favor the preferred database of Elon Musk’s mortal enemy Jeff Bezos: Redshift (#theEnemyOfMyEnemyIsMyFriend). Within months, Redshift is everywhere, Snowflake is a pariah, andEVERY ANALYST IS A LITTLE BIT CALMER.


---


Will any of these things happen? I have no idea. Though I have no money in Snowflake (either long or short), I’mstill bullish. The most likely path is probably gradually slowing growth, followed by twenty years of dominance, followed by twenty years of slow disruption. But, as inevitable as Snowflake’s success seems, how many paths could it end up down thataren'tthat consensus forecast?


Afuckton.

[1](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-1-71510341)

Are there any other examples of companies that have created a big market while also remaining largely unchallenged in that market? Typically, when someone finds a vacuum, new competitors and copycats rush to fill it. dbt found an opening and…nobody else even tried to compete.

[2](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-2-71510341)

Is this source reputable? Probably not. But don’t youwantto live in a world where Edible Arrangements is a bigger business than most blue chip Silicon Valley startups?

[3](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-3-71510341)

People who’ve had the misfortune to work with me know that I ask this question a lot. The“pre-mortem”is one of the analytical shortcuts I’ve stolen from other people, along with things like “reverse the timeline,” and “invert the success metric,” and “what else would happen?” A blog post for another day, maybe.

[4](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-4-71510341)

There's a Wall Street version of this post that requires reading financial statements and doing actual math. I'll leave that effort tomore talented financial analysts. All of my money is in the S&P 500. I applied to many jobs at banks, and never got an offer. I sold all myMicrosoft sharesat $32, a mere 91 percent off its eventual $343 high. I'm anaNgEl InVeStOr.

[5](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-5-71510341)

If a dashboard or pipeline updates in a forest and nobody is around to look at it, does it still make a sound? If that sound is Snowflake’s cash register, then you better believe it does.

[6](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-6-71510341)

Millennials are executives of analytics now. They don’t want futuristic corporate databases; they want retro 80skidcorearcade databases.

[7](https://benn.substack.com/p/how-snowflake-fails#footnote-anchor-7-71510341)

People in the tech world like to use "commodity" as a pejorative, but…commodities are a pretty good business? Data isn’t the new oil; cloud compute is. Both are commodified, sold by an oligopoly, and incomprehensibly rich.
