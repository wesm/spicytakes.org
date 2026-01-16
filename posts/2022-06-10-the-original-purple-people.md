---
title: "Microsoft, Google, and the original purple people"
subtitle: "And, of course, Pokémon."
date: 2022-06-10T16:40:44+00:00
url: https://benn.substack.com/p/the-original-purple-people
slug: the-original-purple-people
word_count: 2634
---


![](https://substackcdn.com/image/fetch/$s_!VMM5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F52d0a67f-aecd-4e33-afce-9a85697a4bae_1600x705.png)

*Google,whatareyou doing?*


The firstpurple peopleI cared about were the purple Pokémon.


When I was in fifth grade, I had two hobbies: baseball, and Pokémon cards. On Tuesday nights, I'd play Little League; on Saturday mornings, it was Pokémon League.


In the latter case, every weekend, one of my best friends1and I would get driven to a nearby Books-A-Million to play thePokémon card gameagainst a few dozen other regulars. After a couple hours of matches—each game is a one-on-one battle in which the two players use customized decks of collectable cards—we’d report our results to the league organizers, walk across the parking lot, eat all we could eat at an all-you-can-eat CiCi’s Pizza, and get picked up to go home, to drink sodas and watch baseball.


Because good cards were hard to come by, we built our decks with whatever cards we could get. Typically, this meant using your first great card as a centerpiece, and then assembling a complementary cast around it from trades with other kids,2or from lucky draws from packs bought with your allowance. My friend had aCharizard, a fire-themed Pokémon, so he built a fire deck. I got aJapanese Mewin one of the first packs I opened, so I developed a strategy centered around the purple psychic Pokémon.3


Every once in a while, though, you’d run into a kid who had everything. With an unlimited collection of cards to draw from, they’d stuff their deck with a mismatched jumble of the most powerful Pokémon in the game. They hit you with an onslaught of raw force—Ninetales, thenZapdos, thenHitmonlee—but their strategy was somewhere between inscrutable and incoherent.


In the data industry, Google is this kid.


Most data vendors compete like my friend and I: They find their one edge, and do everything they can to exploit it as much as possible. In more concrete terms, companies build features that pair well with their initial strength, integrate with a few important adjacencies, and try to define new product categories—ELT! Data observability! Data activation!—that put their offering at the center. The strategies don’t always work, just as I sometimes ended up with a lineup of feebleGastlysgetting nuked by an army ofElectabuzzes. The game we’re playing, though, is usually clear enough.


Google, by contrast, has built or acquired a very long list of impressive tools and technologies in the space. To name but a few: BigQuery is one of thefastest and most scalabledatabases on the market;Lookeris a leading BI tool, and LookML, if removed from Looker, isthe original metrics layerof the modern data stack. Google Analytics is themost widely usedweb analytics product in the world. Googlebought Dataform, a dbt-inspired transformation tool, andAlooma, an early Fivetran and Stitch competitor. They offerColabfor developing in notebooks;Data Studiofor visualization;Optimizefor A/B testing;Data Catalogfor data cataloging;Dataprepfor data prep; and a whole host ofmodeling,orchestration,AI, andcomputeservices. And none of these hold a candle to their crown jewel: Google Sheets, the only product on the market that can truly threaten Excel’s thirty-year reign as themost dominant data productin the world.4


As far as data technologies go, it’s an embarrassment of riches. But like that of the kid with the Pokémon deck of death, Google’s strategy is much harder to discern.5Though many of its products are popular, Google—and the data community’s chattering class, which isn’t representative of the market, but is perhaps representative of its attention—tends to discuss each of them separately. Webenchmark BigQuery, debate thefuture of Looker, get excitedabout AlloyDB, and complain aboutGoogle Analytics. But, for all its tall trees, there’s little discussed or revealed about the forest.


Which strikes me as a little eerie. Google has the products, technology, and capital to dominate this industry. Why aren’t they? Are they still figuring out how to make all of their pieces fit together? Have they already, and we just haven’t been hit with it yet? Are they a collector hoping to make money on each card, and they’re playing an altogether different game than the rest of us?


Let’s make some guesses.I’m feeling lucky.


# If it ain’t broke…


There are two obvious potential strategies. The first is to build a bunch of tools that make a lot of money on their own. Just as there’s no unifying vision about product synergies inBerkshire Hathaway’s portfolioof Geico, a railway line, Dairy Queen, and theRoanoke Times, there doesn’t have to be some grand plan for howDataflowandSpannerwork together. The story may be much simpler than that: Google wants to use their bottomless bank account and singular technical expertise to build better products, each winning on their own merits, than the rest of us can.6


That seems possible—and almost inevitable, given that organizational challenges at metropolis-sized companies like Google make some degree of product independence necessary. Still, Google's acquisitions, which include smaller strategic startups, clearly represent more than an effort to buy new revenue streams. So I’m skeptical that this explains everything Google is doing.


The second possible strategy is that Google isn’t trying to build a suite of data products; they’re trying to sell lucrative, high-margin compute. To them, all of their data offerings—pipelines, BI tools, catalogs, marketing dashboards, everything—are glossy veneers on top of BigQuery andGoogle Compute Engine. There's no reason to integrate Alooma with Colab because…who cares about selling Colab? Both tools are hooks to drive people into a handful of major infrastructure services. You don’t cross-sell from one loss leader to another.


Last fall, Erik Bernhardssonmade a compelling casefor cloud vendors to take this approach. Major cloud providers may be better off selling commoditized compute services than duking it out in noisy, competitive, and turbulent SaaS and software markets. Most of these SaaS vendors rely on AWS, GCP, and Azure anyway; if you’re one of the cloud providers, collect your tithe and let everyone else do the hard work on top.


Google’s strategy could be similar. Google’s data products may not be meant to win the market, but to seed it. When better BI tools, data pipelines, or data catalogs come along, Google will happily yield to them, so long as they’re spinning the meter on BigQuery.


If Google sales reps are paid to cross-sell other services—which I imagine they are—and if BigQuery is indeed the revenue center of Google’s data offering—which I’m guessing it is—funneling everyone into a couple central services is probably Google’sde factostrategy in the field. So long as reps are hitting sales targets and departments are meeting revenue goals, Alphabet’s shareholders don’t need a grand vision from Google Cloud. Just, as Erik said, don’t rock the boat.


Still, this seems like a local maximum, and I can’t help but think that there’s a bigger prize out there.


# The trillion dollar buyer


A few weeks ago, I wrote that the data industryhas something to learnfrom the success of Microsoft’s bundled products. Many consumers, I said, would prefer to buy neatly packaged tools from a single seller, even if those products aren’t as good as specialized versions you could buy from individual vendors. Modularity, in other words, often isn’t as valuable as convenience.


I stand by this point—the buying experience is the product experience. If we have to buy eight data tools to build a stack, the buying experience is the sum of all eight sales processes; the cumulative annoyances a buyer feels is,at its very best, equal to the worst one. Microsoft demonstrates that these frustrations can be exploited.


As somepeople pointed out, however, the argument is incomplete. Microsoft sells to IT, not data teams or end users of data products. Microsoft isn’t dominant because people value integration and convenience more than a product’s quality and capabilities; it’s dominant because its buyers care aboutpriceandfeature checkboxes.


This reveals a vulnerability for Microsoft—and a huge opportunity for Google. There are roughly five companies that can credibility build and bundle infrastructure and applications into a complete data stack: Microsoft, Google, Amazon, Oracle, and Salesforce. Amazon sells to developers and engineers. Salesforce champions lines of business. Microsoft and Oracle win with IT. Google, it seems, hasn’t established itself yet.


There’s an obvious place for them to focus: Data organizations. These teams aren’t Amazon’s engineers; they aren’t Salesforce’s business units; and they definitely aren’t Microsoft’s and Oracle’s IT teams. They are, as Anna Filippova memorably christened them last summer, thepurple peoplein the middle: “[H]umans with a deep understanding of business context in a particular domain are called red people; [those with] technical expertise are called blue people…Purple people are the people in between—they have a little bit of both that enables them to translate between red and blue.”7


I’d argue that Microsoft’s enterprise business grew to its size in part because it sold to IT, the original purple people. Though IT organizations weren’t huge, their position as a corporate hub gave them enormously outsized budgets. As my prior post’s critics called out, this is now an anachronistic buyer for data products—but the appeal of selling to a centralized service organization, and the budgets they command, remains. Someone just has to offer it to them. Today, Google’s the only company that can.


What would that specifically look like? There are a variety of product updates that Google could make to turn their loose assortment of products into amodern data experience. Pull LookML out as a separate metrics layer, with public APIs for third-party vendors. Scrap Looker’s visualization product and replace it with Data Studio. Embed the same visualizations in Colab. Make Colab an entry point into various ML services. Put Sheets directly on top of BigQuery; make LookML’s metrics accessible in Sheets;8back the whole thing with BI Engine. Dispatch metadata from across the system into Data Catalog. Build a bridge from Google Analytics to Data Studio, to BigQuery’s SQL client, to Colab, and to Sheets. Glue it all together, because in the multifaceted, multimodal, multiplayer world of enterprise data,it’s the glue that matters the most.


More than any product integration, though, Google’s opportunity comes from clearly defining their buyer. Microsoft did in the 1990s and 2000s with IT. Amazon did it in the 2010s with engineers. The 2020s,we’re told, are the decade that data becomes the next trillion dollar market. If I were Google, holding the hand it holds, I’d be awfully tempted to try to take it.9


---


Update, June 12:I messed this piece up. While I stand by the points it makes, I told the wrong story with them. This is an abbreviated version of what I should've said:


# Google is wasting all the good cards


The Pokémon League kid with all the good cards didn't win very often. Even though he had better individual cards than everyone else, his deck was too disorganized to use them. In most games, he lost with a bunch of mismatched energy cards in his hand, and an unevolved Charmeleon on the board.


Google, it seems, sells its data tools in the same way. When we wentdatabase shopping a few years ago, Google’s sales pitch was as simple as Snowflake’s—but in the wrong way. Early in our evaluation, we asked our Google rep why we should choose BigQuery. We were told that it’d be good enough for us because “it’s good enough for Google.”


As a piece of technology, I don’t doubt that’s true, for BigQuery and most of GCP’s other data products. But we weren’t shopping for horsepower, or pure clock speed. We were looking for a product that was easy to use; for a product that would work well with the rest of our stack; for helpful and engaged customer support; for a productexperience.We weren’t going to use BigQuery to process5.6 billion searches a day; we were going to use it for dashboards and a daily pipeline from Marketo. BigQuery’s top-end power would be squandered on us, like the unused Charizard in the kid’s folded hand.


If I had to guess—again, from the outside—this problem has two origins. First, Google’s culture has long emphasized technology over marketing, which encourages a “if we build it, they will come” approach to software distribution. Second, when there’s pressure to grow the business—when execs say that this technology is great, but how do we make money from it?—the easy strategy is, as Erik identified to drive more compute. Google’s roadmap, then, is pulled by engineers building technology “good enough for Google” on one side, and sales people looking to upsell BigQuery and Google Compute Engine compute on the other. Nobody, it seems, is fighting for a cohesive user experience.


And that, I think, is a huge miss. AsGwen Windflower points out, analytics engineering—and, I’d argue, other adjacent roles that Google might sell data products to—is an extremely attractive field for people who want to work with a like-minded community to wire up open source tools and powerful compute platforms. But foranalytics engineering to go mainstream,10it has to start attracting more data “nine-to-fivers:” The types of folks who care as much about supporting their colleagues with good data as today’s analytics engineers, but neither care about how their tools are made nor want to spend their personal lives talking about it on Twitter, in community forums, or on, god forbid, Substack.


For these people, their adoption criteria are different than the current set of early adopters. Running their own open source software is either enough of a headache or outright technical barrier to make them look for a proprietary solution. And buying one package instead of ten tools is both easier to do, and more likely to help them avoid a fight with IT and procurement that isn’t worth having. In the obnoxious parlance of corporate technobabble, the juice of the current modern data stack isn’t worth the squeeze.


That’s Google’s opportunity. Take inspiration from what’s serving today’s data community, and make it accessible, seamless, and easy to buy.  Stop creating a mismatched stack of overpowered cards; design a cohesive deck of integrated ones. Sell the entire deck, ready to play, right out of the box.


Google has the technology to build it, and the capital to buy it. What’s less clear is if they have the vision to imagine it.

[1](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-1-58708482)

Who, it must be said, eventually moved on from Pokémon but not baseball, found something he loved doing, willed his way into the elite echelons of that thing, and now has a job that ismuch cooler than yours, all while remaining one of the very best people in the world.

[2](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-2-58708482)

There were always rumors floating around Books-A-Million about who was buying and who was selling. A Moltres is on the market! Someone is willing to give away the farm for a Blastoise! Forget labor markets or healthcare markets; I want some economists telling me what’s going on inthesemarkets.

[3](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-3-58708482)

And it was a dope strategy. I loaded the deck withMr. MimesandChanseys. I’d slow play the opening turns (usingMewtwo’sBarrierattack to stall if I could), which would buy me enough time to get an evolvedAlakazamon the board. Then, I’d put a bunch of Chanseys on my bench, and attack with Mr. Mime. Mr. Mime’sInvisible Wallpower protected him from taking heavy damage, and Alakazam’sDamage Swappower let me move the little damage he took onto my high-HP Chanseys. This made it nearly impossible to knock Mr. Mime out, creating a slow war of attrition that bled my opponent dry while Mr. Mime’sMeditateattack, which compounds over time, wore them down. Eat your heart out, Napoleon.

[4](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-4-58708482)

Imagine your product being so widely used that its bugs aredocumented on Wikipedia.

[5](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-5-58708482)

From a distance at least; I have no inside knowledge of what goes onin the plex.

[6](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-6-58708482)

Sooner or later,Frank SlootmanThomas Kuriancomes for us all.

[7](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-7-58708482)

I’m slightly misquoting Anna here, because I’m too much of Scrooge to include the emojis. Bah humbug.

[8](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-8-58708482)

Googleteased this onealready.

[9](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-9-58708482)

Or, you know, catch ‘em all.

[10](https://benn.substack.com/p/the-original-purple-people#footnote-anchor-10-58708482)

I’ll leave it to the reader to decide if this is a good or bad thing.
