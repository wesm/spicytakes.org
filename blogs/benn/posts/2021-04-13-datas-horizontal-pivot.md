---
title: "Data’s horizontal pivot"
subtitle: "An industry turns sideways."
date: 2021-04-13T16:24:18+00:00
url: https://benn.substack.com/p/datas-horizontal-pivot
slug: datas-horizontal-pivot
word_count: 1522
---


![Some pivots succeed, some pivots fail, and some get stuck on the stairs. ](https://substackcdn.com/image/fetch/$s_!9viO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0b3bd96a-3337-4ffc-8413-daa07837e8b2_900x474.jpeg)

*PIVOT!*


In economics,vertical integrationis a method of production in which companies own the entire supply chain and distribution network for a product. A vertically integrated beer producer, for example, owns the farm that grows hops, owns the brewery where beer is made, owns trucks to ship the beer, and potentially owns the stores and pubs where the beer is sold.


Horizontal integrationturns this structure on its side. In horizontally integrated industries, each link in the supply chain is owned by a different company. Companies grow not by expanding into other parts of that chain, but by controlling a larger share of their link. In a horizontally integrated beer industry, one company would own a bunch of farms, another company would buy their hops and brew beer, a third company would manage shipping and distribution, and fourth would run the retail stores that sell the beer.


Each structure has its own advantages and disadvantages. Because vertically integrated companies control their supply chain, they aren’t dependent on other suppliers to build their products. These companies also avoid paying the markups charged by external suppliers (e.g., the hops farmer who needs to make their own margin), so they can often charge lower prices to consumers.


In vertically integrated industries, however, technological improvements diffuse slowly because every company has to integrate the change on its own. If one brewer develops a more efficient method for brewing beer, other brewers have to upgrade their breweries to support it. In a horizontal industry, every producer can take advantage of improvements in one layer of production simply by purchasing from that more efficient supplier.


For this reason, in particularly large and dynamic supply chains, horizontal integration can have clear benefits. It’s difficult enough, for instance, for one company to maintain farms for growing crops, breweries for producing beer, logistics networks for distributing it, and stores for selling it—and it’s only made more difficult if new technologies are constantly disrupting each layer. A horizontal industry of companies specializing in each stage of production would be more capable of quickly integrating new technologies and, ultimately, producing higher quality goods.


---


A decade ago, as “big data” and “data scientist” were entering (and quickly saturating) the lexicon, analytics products were vertically integrated. The most popular data tools were responsible for every aspect of the data “supply chain”—collection, storage, analysis, and visualization. If you wanted to analyze a particular type of data, there was a tool specific for that data or business domain.

- For product teams, Google Analytics and Mixpanel include their own agents for tracking user activity. They log this data, and store it in their own databases. That data is made available through the Google Analytics and Mixpanel apps, and has to be analyzed using their visualization tools.
- For sales teams, data is entered directly into Salesforce. Salesforce maintains the definitive copy of that data, and it can be explored through Salesforce’s native reporting tools.
- For marketing teams, Hubspot sends emails, tracks how people interact with campaigns, stores performance metrics, and surfaces them in dashboards in the Hubspot interface.
- For finance teams, Stripe manages and records user transactions directly. Stripe then provides reporting tools for people to build reports on their invoices.


Though not specific to an operational domain, BI tools traced a similar outline, integrating ETL, warehousing, transformation, and visualization capabilities in a single tool. Qlik and Tableau, prominent BI tools founded in the 1990s and early 2000s, built connectors that plug directly into lots of sources and ingest data into their infrastructure. Analysts can then configure datasets and data models, which are only accessible through Qlik’s or Tableau’s exploratory tools. This architecture doesn’t shut out other tools—you can still bring your own warehouse or data modeling application if you want—but it didn’t require them either.


As is the case for any vertically integrated producer, that independence is one of the primary benefits of this structure. If you want to track how people are using your website, you can do that, soup to nuts, through Google Analytics. If you want to build a great BI practice, you can get everything you need from Qlik.


Or at least, you could in 2010. Over the last decade, two major shifts have put a lot of pressure on this industry orientation.


First, the data ecosystem hasexploded. To paraphrase data presentations’ most overused opening statistic—“we’vecreatedmoredataoverthelasttwoyearsthantheprevioustwothousand”—we’ve probably created more data companies over the last two years than the previous two thousand. While not all of these vendors will produce something valuable, they introduce a lot of technological disruption, making it difficult for end-to-end vendors to keep pace.


Second, as companies become operationally dependent on data, vertically integrated data products create another problem: Data is segregated by tool and function. Product reporting lives in one place; sales in another; marketing in another. Like being able to go to BevMo (!) (Jeb!) and buy any beer you want, it’s nice to go to one place for all the data you need. And unlike beer at BevMo, data’s often best consumed when blended with other data (with apologies toblack and tanfans).


In this context, all-in-one data products have less benefit. While it doesn’t make sense to buy a separate horizontal tools for each layer of the data stack if you’re a lone analyst building campaign tracking reports for the marketing team, that calculus changes if you need to build reporting for every department—and doubly so if you want all of that reporting to built on the same technical and logical foundation.


In response to these changes, companies are turning their stacks sideways. One tool is responsible for each layer—each stage of the data supply chain—across the entire business. A single tool handles ingestion, another one is responsible for storage, a third for consumption, and so on. This not only makes it easier to introduce new technologies, but it also ensures that updates to one layer—for example, an update to the logic defined in the transformation tool—automatically propagate to every other layer.


![](https://substackcdn.com/image/fetch/$s_!CgZE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F01738560-6d2b-4d55-8d88-30e472ebcba5_1116x594.jpeg)

*Every pivot needs asketch*


In recent years, this architecture has become more and more common. Rather than relying on native reporting in tools like Salesforce, lots of companies are now writing their Salesforce data into a central warehouse and analyzing it there. Responding to this trend, product analytics tools like Google Analytics now let you export your data directly into a database. And dbt is encouraging companies to pull apart data transformation and consumption, which traditional BI tools often combine.


For folks familiar with the now-buzzwordy Modern Data Stack™, none of this is controversial. But it has a few interesting implications.


First, building across horizontal boundaries is going to be really hard, for both vendors and for the companies using them. For vendors, it’s tempting to expand into other layers of the stack, given their obvious value and complementary nature. But, with dedicated vendors at each layer, it’ll be difficult to offer competitive crossovers. And more importantly, multi-layered tools force data teams—the customers of these products—to muddy theoptimal application boundariesof their data stacks (RIP Robert Mundell). Data teams are better off not trying to cut against the grain of this emerging architectural outline, and vendors are better off not encouraging them to do so.


Horizontally integrated companies, however, can’t operate in a vacuum; for this orientation to work, these companies have to work well with the rest of the supply chain. This makes inter-layer integration particularly important. To this point, we haven’t really figured out how to do this, at least not directly. Lots of tools “integrate” via the data warehouse (Segment, Fivetran, dbt, and Mode all talk through the warehouse); over time, there need to be more direct links to make sure the system moves together.


This could happen via a bunch of bilateral integrations, over some agreed upon standards, or through a dedicated middleman that’s designed for exactly that purpose. My suspicion is we’ll start with the first option and end with the third, whileunsuccessfully flirtingwith the second the whole time.


There’s also a final elephant (or three) in the room: Could one company do it all? Or more pointedly, will Amazon, Google, or Microsoft build the whole thing?


For most companies, the surface area of the data stack is becoming too complex, and pulling in too many directions, to build an all-in-one solution. But, if Amazon can operate awind farm, agrocery store, and amovie studio, I imagine they can build a handful of data tools—and it’s probably inevitable that they do.


When they do, however, it won’t be a single product. Instead, they, along with Google, Microsoft, and potentially Salesforce, are likely to offer a suite of services that play nicely together, similar to the cloud computing services offered by AWS, GCP, and Azure. These offerings would operate less as a centralized product—you could still mix-and-match the services you want—and more as a centralized billing plan. And like their independent counterparts, tools that cut across these layers—including Looker, in my view—will eventually get pulled apart to align with the horizontal grooves the industry is carving.
