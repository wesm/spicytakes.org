---
title: "The return of the modern data stack"
subtitle: "An old trend flickers to life. Plus, White Lotus, DOGE, and gold on a plane!"
date: 2025-02-21T17:00:42+00:00
url: https://benn.substack.com/p/the-return-of-the-modern-data-stack
slug: the-return-of-the-modern-data-stack
word_count: 3096
---


![](https://substackcdn.com/image/fetch/$s_!5leT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d9341f2-7bd1-4fb2-94b6-d60a383a78bc_1228x682.png)

*Fads are a flat circle.*


Before getting into the usual nonsense, we’re launching a temporary new feature here at benn.substack.com:TheWhite LotusPower Rankings.1As I’m sure many of you are aware,The White Lotusis an HBO show about terrible people doing terrible things in beautiful places. Someone usually dies; we don’t know who; there are many deserving candidates. You will never find a more wretched hive of scum and villainy than you will inside aWhite Lotushotel,2andyou must be cautious.


That’s the intrigue of the show—it’s part whodunit and part trolley problem, in which we all argue over who, among a basket of deplorables, is the most irredeemable. So, as someone who loves a dumb debate as much asI love a dumb survey, I have to ask: Who’s your champion? If there are twelve Marie Antoinettes tied to twelve different train tracks and you only have one trolley, what do you do?


Vote!


I’ll ask each week, as the atrocities unfold. And whoever first predicts the killer and the victim wins a stay in the Pineapple Suite.3


---


# Databricks


In late 2021, an analytics startup hosted a conference about the “future of data.” During the closing keynote, a notable venture capitalist made a bold forecast: In the coming years, most major enterprise software applications were going to be rebuilt on top of data warehouses like Snowflake and Databricks. Soon, everything, from CRMs and ERPs to CPQs and ATSs,4were going to be “warehouse-native.” It was a trillion-dollar transformation, and the modern data stack—the dizzying explosion of data tools built to connect to the same databases—was just the beginning.


The prediction had a satisfying promise. Back then, in those medieval times, every SaaS application was built on top of its own internal database. If a company used Salesforce, Salesforce kept its own list of who it thought were their customers. If they used Zendesk, it kept a second list. Marketo kept a third, Jira a fourth, Stripe a fifth, all the way until they had112 different lists, flimsily held in sync byshoddy bilateral integrationsandJeff’s Airflow scripts.5


Unfortunately, 112 lists is 111 lists more than most companies want. So, people sunk endless hours into “harmonizing” their lists. They argued about which one was right. They sent marketing emails to customers who were already customers asking them to become customers again; they sent notes to customers who were no longer customers thanking them for being loyal customers. Data teams spent their lives comparing the lists,looking for scary numbersand staring into the static.


Problems of the past,weallthought. Rather than every tool maintaining their own mismatched list,6companies should keeponelist, in a database all their own. If a tool needs that list, they won’t create a new one; they’ll use the existing one. And if a company needs to update the list, they update it once, in one place.


Now,normally, somewhere in the paragraphs above, I’d add a link to the investor’s talk. But I can’t, because the video no longer exists. The conference was hosted by a startup that was partly built on this general idea, and that startup went out of business. So didothers. Themodern data stack microsite, which would’ve made for a fun link from “dizzying explosion of data tools,”is gone. The wholemodern data stack movement is dead, cringe and out of fashion—replaced, obviously, with AI. Snowflake is theAI data cloud. dbt Labs tells us thatgen AI runs on data. And we’ve all quietly quit on our warehouse-native CRMs, and are loudly pivoting intoAI-nativeCRMs.


In hindsight, it’s easy to see why it was so hard to make one list to rule them all. People often buy tools like Salesforce and SAPbecauseof theircomplex features and endless optionsfor customization. If you want to compete with these products, crossing their labyrinthine moat ishard enough on its own; it turns out to be nearly impossible when you hand over control of core elements of your software, like the list of customers in a CRM, to someone else. You can build a trailer on a modular foundation, but you can’t build a mansion, and enterprises like their mansions. So that was the story of our warehouse-native future: Moments of gold and flashes of light, but mostly things we’d never do again.


But fads are loops, and it’s all coming back to us now?Sorta? I think? From software giant SAP, the full transcript ofthe announcement videoabout “one of their biggest launches” in their 53-year history:


> Today, we are actually announcing a breakthrough offering. We're doing one of our biggest launches in SAP's history: Business Data Cloud.Every company has today, big, big data silos, and what we are doing with Business Data Cloud, is, actually, bringing all the data together—SAP and non-SAP data. We are building the industry's leading data platform.Data is the lifeblood sustaining an organization to allow it to pivot in this new digital economy. And the more you can bring it together, and get access to it quickly, the more you can put it in context, you can start to use it, and you can start to navigate your business to the next level.Our customers have to stitch each of the lanes manually and individually for them to make sense of it. And when they do that, they lose context of the data and the semantical7richness. So this completeness of the solution that allows our customers to take advantage of AI is something that is truly unique in the market.And all the agents, from the frontline to supply chain to finance, will work together, and they will be the smartest agents in the industry because they are sitting on high quality data offered by Business Data Cloud.The one thing that's, to me, amongst many, that's really exciting about Business Data Cloud is the partnership with Databricks, because what it is doing is bringing two powerhouses together into a singular offering for our customers, with SAP, with its breadth of business suite and the most mission critical and most important data that these applications create, harmonized in a way which is critical for any AI aspirations and any value.I think for SAP, it's huge, because now the applications that are all tied to this, as well as adding AI to it, will really help an organization transform to the next level, and it's badly needed in the digital economy. And so we are very excited about the offering, really delivering value to our customers.


Tremendous. I too am excited about the offering, and the value, and completeness of the solution that will navigate my business to the next level in this new digital economy. So maybe Databrickswill tell us what it actually is?


> SAP Databricks will be a native component in the SAP Business Data Cloud.SAP Databricks enables customers to bi-directionally share data between SAP Databricks and their enterprise environment while ensuring SAP data retains all of its semantics.…Our new offering, SAP Databricks, is sold by SAP as part of SAP Business Data Cloud on Azure, AWS, and GCP. SAP Databricks provides customers artificial intelligence, data warehousing, and data engineering capabilities, all governed by Unity Catalog. …SAP Databricks will have all the relevant datasets enriched and ready to be used for everything from data warehousing to building AI that can reason on that data. …The real magic of this partnership is that enterprises can easily combine their SAP data with the rest of their enterprise data. SAP Business Data Cloud empowers customers to unlock insights and business value of context-rich SAP data in both SAP Databricks and all existing and new Databricks deployments via Delta Sharing.


I mean. I don’t really know what’s happening here, nor have I ever been able to figure out what SAP does, or even what an ERP is. But here is what I think is going on:

1. SAP builds lots of business applications.8Those applications produce a lot of lists, like lists of customers andcomplaintsandeco-friendly packagesandmilk. People want to analyze those lists, and so SAP built a 283rd product—the SAP Business Data Cloud—that hoovers up all of this data into an SAP-hosted warehouse, ties it all together with a semantic model, andsticks some charts on top.
2. None of this is particularly inventive, and most big software conglomerates do something similar. Oracle hasOracle Analytics; Atlassian hasAtlassian Analytics; Workday hasPrism Analytics; Salesforce hasCRM Analytics. SAP now has their version. It’s not called SAP Analytics, so I guess it is a little bit inventive.
3. But SAP is also doing something else differently. Their product isn’t just SAP; it also comes with a SAP-branded-but-Databricks-powered portal. So, people log into their SAP account, click on “SAP Databricks,” and see the Databricks interface and have access to all of the normal Databricks features, but the logo at the top says SAP, and the database is automatically full of your SAP data. It’s embedded Databricks, preloaded with SAP data.
4. Buthow? How does all this work? My suspicion is that the SAP Business Data Cloud isn’t just built on some SAP-specific database, but also transforms all of SAP’s lists about customers and complaints and packages and milk into theopen-source data formatthat Databricks uses. Though I'm sure there are lots of ergonomic stitches that tie the SAP and Databricks interfaces together, I’d guess that the substance of the integration is through data reformatting, and most of the work to build it was done by SAP trying to figure out how to convert a bunch of esoteric proprietary formats into one preferred by Databricks.9Once they did that, putting Databricks on top was relatively straightforward, because Databricks could read directly from the result.


Which, sure, this is how databases work now. About ten years ago,they got split in half, into a bucket of data on one side, and a compute engine that runs calculations on the other. So long as the buckets are formatted correctly, you can mix and match different buckets with different calculators.


But this SAP product, if it works the way I think it does, extends that idea in a couple of new ways. First, it suggests that applications, like CRMs and ERPs to CPQs and ATSs, could be one of the buckets that databases connect their calculators to. Rather than exporting data out of SAP—which is howpeople have done this for a while, and it clearlyhasn’t gone well—SAP can simply reformat it. Then, people can bring their database—or, since it’s 2025, bring their aGeNtS—directly to the applications themselves.


It could go even further. In their video, SAP said “we are bringing all the data together—SAP and non-SAP data.” That implies that SAP’s analytics product might be able to read from buckets other than their own. Or, more generally, the calculators that read from the open source buckets don’t have to be databases. They could also be anapplication’scalculator.


In other words, the whole warehouse-native idea might’ve been a bad one, but not entirely. If the world gradually coalesces around common data storage frameworks, people might not rebuild applications on top of databases but on top ofdata formats.A BI tool could run a DuckDB engine and connect it directly to SAP’s Iceberg bucket. A marketing tool could read from Stripe’s bucket. The next AI BDR could read from a CRM’s bucket. It’s not quite one customer list to rule them all, but it’s a bit closer.


Now, I’m not sure that any of this works. The architectural crosstalk of an application reading from another application’s backend is almost certainly a more heinous knot than the “warehouse-native” one. But maybe not? You could at least imagine some tight partnerships working this way, where integrations between some CRMs and marketing tools are maintained through this sort of structure.


My favorite definition of the modern data stack is that it’s data toolsthat launched on Product Hunt—they’re the data tools that came out when people cared about Product Hunt, that sold to people who read Product Hunt, and that have a sort of Zillennial marketing aesthetic that Product Hunt embraced. For better or for worse, SAP and Databricks are none of those things. But maybe that’s the point: Trillion-dollar transformations start whizbang brands on Twitter, but end with the SAP Business Technology Platform (SAP BTP).


---


# Data bricks


I periodically wonder how aerospace engineers feel about airplanes. I have a very rough understanding of how flying works—it’s the lift, and Bernoulli's principle, and something about how the wing is shaped like a slug that’s in a hurry—but I mostly have to suspend disbelief, and let physics take the wheel. Planes fly for the same reason that magnets attract: It’s just how things work, andyou’re better off not asking any more questions.


But if you spent a lifetime studying airplanes, do you see it differently? Does it become intuitively obvious that airplanes can fly, no more unnatural than boats floating and cars not dissolving through the road? Or does knowing more about airplanes make the whole thing feel even more tenuous, held together byforgotten boltsand inexplicable science?


I have other questions. When doctors need surgery for themselves, do they breezily dive under the knife, knowing that decades of precise trials and careful training is behind every incision? Or do they just hope to wake up, because they’ve seen doctors ChatGPT their way through the MCATs and Red Bull their way through 40 straight hours of operations? Do iron workers walk into construction sites confident in the engineering standards that are above their heads, or are they terrified by how many shortcuts people take to cheat those standards? Do sushi chefs know that every piece of fish is inspected by an exacting executive chef, or do they know that every kitchen is full of warring cooks who are more worried about revenge than what theyroll upin your sushi?


I wonder about all of this because the more I learned about the world I worked in—data and its related parties—the more it revealed itself to be a horrific Rube Goldberg machine. Leading tech companies aren’t full offuturistic computersthat aggregate their vast surveillance infrastructure into some piercing Eye of Sauron; they are full of people wondering why their lists don’t match.


Case in point: When I worked at Microsoft—one of thebiggestandmost profitablecompanies in the world, the pinnacle of economic success and scientific achievement, the sort of company thatinvents new states of matterand makes the United States the technological envy of the world—we were trying to figure out how many people used O365, the online version of Office. The question was unanswerable. We heard rumors that there was a 6,000 line script that could parse some logs and approximate a guess, but nobody had ever seen it run. If an exec asked about O365 adoption, someone  glued together a bunch of numbers in Excel. We all laugh at FTX for theirterrible balance sheetof one-off math and “hidden, poorly labeled accounts,” but we are all FTX; it’s just a matter of degree.10


Anyway, it seems like one of the new features of 2025 will be theDOGE teamjoyriding their way through government databases andlive-tweeting about it. I have no idea if they’ll find any real fraud or not, but they will definitely find a lot of messy data. We shouldn’t be shocked or offended by that; in fact, it would be much more shocking—and suspicious—if theydidn’thave it.


Which, sure, clean would be better.That’s what America wants; nice, calm data. But to expect that is to expect government agencies to be not like us.


---


# Gold bricks


Speaking of airplanes, last month, I talked about Hugo Chavez’s quest tofly Argentina’s goldback from London. Several people emailed me to ask if he was successful, and if I knew where the gold was today. The answer, it seems, is that it’s beingflown back and forth between London and New York:11


> President Trump’s threatened tariffs on Europe have thrown precious-metal markets into disarray. Gold prices have been driven to record highs, and a yawning gap has opened in the value of the yellow metal in its two trading hubs, New York and London.Gold is, for the moment, worth substantially more in Manhattan than in the U.K. capital, sparking the biggest trans-Atlantic movement of physical bars in years. Traders at major banks are racing to yank gold from vaults deep below London’s medieval streets and from Swiss gold refineries and ferry them across the ocean.The cheapest way to transport such a valuable commodity safely: the cargo hold of commercial planes.


On the internet, your money is everywhere, all at once. That’s convenient, but boring. When your money is a pile of rocks locked in Gringotts—or Fort Knox,maybe—there are so many more opportunities for shenanigans. Yet another way the internet isoptimizing all the fun away.


The wildest part of this story, though, is how people are keeping up with it:


> [Banks could avoid losses by] flying the physical gold they owned in London to New York and delivering it to the futures contracts’ owners instead, said Robert Gottlieb, a retired gold-trading executive whose LinkedIn posts on the disarray have become required reading in the market.


A confirmed case; the virus is out; we have to flatten the curve. LinkedIn hasbroken containment.

[1](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-1-157625068)

The idea is courtesy ofa good friend.

[2](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-2-157625068)

Especially this season, which features two UNC grads and two Duke grads.

[3](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-3-157625068)

No, you don’t want that, the Pineapple Suite breaks people. The prize will be the Palm Suite, which has better views anyway.

[4](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-4-157625068)

“ATSs” is probably the most grammatically loathsome phrase I’ve ever typed on this blog. TheNew Yorkerwould beashamed.

[5](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-5-157625068)

Y’all, I messed up. Jeff is apparently both a25-year old product manager at Ramp, and along-retired IT engineer. Out of respect for Jeff’s many years of service, henceforth, product manager Jeff will beGeoff.

[6](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-6-157625068)

Customer lists in SaaS apps:Long contained, often imitated, but never duplicated.

[7](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-7-157625068)

“Semantical” might be more offensive than “ATSs,” tbh.

[8](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-8-157625068)

282 of them, apparently.

[9](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-9-157625068)

Why did they use Delta Sharing instead ofIceberg? I have no idea. Because it’s an integration with SAP, which means it’s been three years in the making, andTabular barely even existedback then? Because Delta SharingisIceberg?

[10](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-10-157625068)

Why? Because of all the lists, mostly. If you want to figure out how much money you make—an important question that you’d think companies could cleanly answer—you have data from your bank accounts; you have data from payment processors; you have sales agreements full of weird terms. You have failed payments, bounced checks, paid trials, and overdue bills. It’s a mess, and it never adds up.

[11](https://benn.substack.com/p/the-return-of-the-modern-data-stack#footnote-anchor-11-157625068)

Well, actually, most of the gold made it back to Venezuela, though some of it, like all things, isheld up in litigation.
