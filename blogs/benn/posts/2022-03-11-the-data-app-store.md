---
title: "A very big deal"
subtitle: "Snowflake goes shopping, and buys the store."
date: 2022-03-11T17:16:08+00:00
url: https://benn.substack.com/p/the-data-app-store
slug: the-data-app-store
word_count: 2272
---


![](https://substackcdn.com/image/fetch/$s_!8fN9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F53c344b3-e1e0-43e6-b79d-483efd7658e7_1280x720.jpeg)


Tech acquisitions are like marriages: They mean a lot to the people involved, but the rest of us would be forgiven for not noticing that much is different. After blustery announcements about synergy, shared visions, and obligatory corporate excitement for the next step in the journey, most acquisitions fade from relevance. The rough edges of innovation get sanded down. A few fonts and brand colors get updated. Product roadmaps are gutted to make space for backend infrastructure integrations and strategic repricing initiatives. Acquisitions don’t create revolutions; they capture those that have already happened, and repackage them into a limited enterprise offering.


Last week was an exception. We may not have felt it then, we may not feel it tomorrow, and we may not even feel it in twelve months, but five years from now, we’ll look back and see it—Snowflake’s acquisition of Streamlitstarted an avalanche, and the data landscape will be forever changed because of it.1


On the surface, the acquisition of Streamlit, an open-source framework for creating data apps, is both underwhelming and a bit confusing. In the fundraising fever dream between a fading pandemic and an impending nuclear winter, a purchase price of $800 million wasn’t an uncommon sum for a data company. Industry observers, accustomed to seeingmuchbiggertotals, reacted to the announcement with a collective shrug: Tech publicationsquotedfrom press releases, peoplequipped about the name, and Wall Streettook an axto Snowflake’s stock price, either for lowering their growth forecasts or for existing a global economy that could, at any moment, be annihilated by a humiliated madman who misses his stolen yacht.


Assuming we aren’t all nuked into oblivion, the acquisition is still somewhat perplexing. Financially, it definitely doesn't make sense. While Snowflake, which is still worth $60 billion after its stock market swan dive, can easily afford it, it’s paying a huge premium for a company thatreportedlymakes less than $100,000 in revenue. Even by last year’s fundraising standards, an 8,000x revenue multiple is steep.


Streamlit is also a peculiar strategic fit. The company hosts a platform that helps data scientists build data apps with a few lines of Python. These apps aren’t exactly traditional BI tools, but they exist squarely in the consumption layer of the data stack.


Compare this acquisition with the other notable announcement in the industry last week:Google laid offLooker’s entire U.S. support staff. Though layoffs happen for all sorts of reasons, the tea leaves of this one are easy enough to read. BigQuery, as many have long suspected, is the gravitational center of Google’s data stack. While Lookermakes real money, Google's balance sheet only registers line items that make preposterous money.High-volume computing services—i.e, BigQuery—can do that in the way that SaaS applications can't. For Google, Looker is too big to fail, but too expensive to scale. The future of the cloud data warehouse business is, in other words, the cloud data warehouse.


Why, then, would Snowflake, BigQuery’s most direct competitor, invest more in the top of the stack, just as Google is backing away from it? Why would Snowflake look at the same market and move in the opposite direction?


Because that's not what they are doing.2Streamlit will never step foot in Gartner's data apps magic quadrant, or, I suspect, ever even attempt to bring a traditional product to market. It will instead become something more fundamental: the platform—in a true sense, thecapital-P platform—on which every other commercial data app is built and sold.


# The promise and peril of data apps


Last fall, a16z's Martin Casado predicted that we’re going toremake all of today’s SaaS apps on top of the data layer. Soon, according to Martinand others, we’ll all be running our businesses through “data apps,” which, not yet having an agreed-upon definition, I’m defining as a product that solves a non-data problem where removing data ruins the product.3It’s a compelling future, where data is more than a "Insights" tab glued onto a recruiting tool or a task management app. It's a future in which data isembedded in operational experiences directly, just as reviews are inextricably interwoven into Yelp.


But, as I’ve argued before, there are a few obstacles that make this vision impractical today. First, it’s technically incomplete. The “data layer” isn’t yeta coherent platform; it’s just a database. Early data apps likeEppo,Supergrain,4Vero, andNarratorsimply connect to analytical warehouses directly, and “integrate” with the data layer through a JDBC driver and some SQL queries.


Though that architecture is potentially powerful, it’s not an easy sandbox to develop in. SQL is a clumsy language for application development, and most databases don’t provide true APIs, much less software development kits, or SDKs. Without these tools, building data apps today is akin to building web applications before frameworks likeRails—every application has to solve low-level problems like, “How do I interact with a database?” and "How do I translate this user action into performant DDL?" It's possible, but it's not easy.


This creates the second challenge to Martin’s vision: Data apps are expensive to build. Dealing with these technical complexities requires engineers, and hiring engineers requires money.


Moreover, data apps are also expensive to sell. Enterprise IT teams generally prefer that people don’t install random apps from the internet on corporate computers, and they’ll hunt you down if you connect those apps to tightly governed data warehouses. As a result, in addition to engineering teams, data app vendors also need go-to-market teams to pitch, sell, and support their products.


Thisratchets up the economicsof the data app market. The cost of selling a data app requires vendors to charge a high price for that app; to command high prices, app providers are incentivized to expand the surface areas of their products; this makes hard-to-create products even mores expensive to build and maintain, amplifying the pressure to sell them at a high price.


For all the talk about the value of modularity in the data stack, these dynamics push the data app market towards monolithic consolidation. Just as there are no boutique car manufacturers, so long as building and distributing data apps requires significant capital, we won't have a thriving ecosystem of specialized data apps either. Instead, we'll have a bunch of startups chasing the only things that make them economically viable businesses:Significant venture funding, big visions, and the soft monopoly of category creation.


Streamlit and Snowflake could change all this.


# The framework


Today, Streamlit is primarily focused on manipulating and presenting data within the Streamlit application. There areutilities for connecting to databases, but they’re mostly light wrappers around Python SQL clients like psycopg2. Streamlit’smethodsandcomponentslibraries, which provide ways to “visualize, mutate, and share data,” are far more expansive.


Over time, I expect this balance to flip. A package for wrapping yet another abstraction layer around Python visualization libraries is cool; a framework for interacting with Snowflake as though it’s a transactional database—as a kind ofactive recordfor Snowflake, if you will—is transformative.


For instance, a Streamlit app’s configuration files could define which tables in an underlying Snowflake database areentities. From within the app, developers could then interact with those tables, via Pythonic syntax, with Streamlit facilitating the handshake between the app and the database. Rather than translating application logic into strings of SQL queries and back again, developers could simply call something more native:


```
Customer.filter(plan_type=”business”).values(“name”)
```


Not only does this shortcut otherwise difficult operations, but it could also solvemuch bigger problemsthat most data apps punt on today. Take access controls—as anyone who’s ever built a data app knows, trying to translateapplication-levelpermissions intodatabase-levelpermissions is an immensely complicated problem. Streamlit could handle this directly: By being aware of both the application user and the underlying database grants, the query generated by the code snippet above could automatically change depending on who that user is. It’s this sort of magic, much more so than filter widgets and gauge charts, that transform data apps from neat toys into markable products.


# The marketplace


Notably, a framework like the one above would make Streamlit more complicated. Rather than helping data scientists build simple apps in minutes, it would help developers build complicated apps in days.


But that’s not a step backwards; it’s a huge step forward. The impact of Rails and Django, which are used by engineers to create rich web applications that can be fully commercialized, has been unfathomably greater than the impact of low-code website builders like Squarespace. Streamlit could offer the same promise. To get there, though, it has to be willing to sacrifice the lower end of the market for the top end, and invest in frameworks over components.


But if they do that, Streamlit could also catalyze the second tectonic shift in the data landscape: The introduction of a Snowflake app store.


With support for more complex apps, Streamlit and Snowflake could host a marketplace of commercial apps, similar to those like Eppo, Supergrain, Vero, and Narrator. Before listing the apps, Snowflake would review them, and pre-approve each as as meeting (or not meeting) various security and compliance standards like HIPAA and SOC 2. In return for this, and for making vendors’ products available in a single click, Snowflake would take a cut of each sale. To jumpstart the ecosystem and give vendors an incentive to create and list their apps, Snowflake could also pass a portion of the compute costs generated by the apps back to them as a form of royalties.


The combination of these two things—a framework for data app development, and a marketplace for apps that Snowflake stands behind—closes nearly all the gaps in Martin’s vision. It provides the technical layer on which apps can be built. It makes developing apps cheaper, and makes selling apps easier. And if apps are built on top of an entity-like framework, it makes them fast to deploy as well. To get started, all customers would need to do is point the apps to the tables required to back them, like an event stream formatted like Narrator’sCustomer 360.


Imagine, for example, what it would take to bring a customer success app to market in this new world. Rather than integrating with Salesforce and other CRMs, the product could simply require a customer entity with a predefined schema. Customer usage data, which is notoriously hard to reliably load into marketing and sales tools, could be ingested though a few user and event entities.5With direct access to this data, the app could then create renewal forecasts, automatically suggest customer interventions, and write customer health scores back to the database. And all of this could be built by a small team, distributed directly through an app store, and sold for a fraction of the cost of a comparable SaaS app today.


# The store next door


This isn’t, of course, a magic bullet. Most obviously, it's restricted to Snowflake. For most apps, that’s probably not as limiting as it seems at first glance. App developers can still make plenty of money selling only to iPhone users; as long as development costs are reasonably low, data app providers could still make good money only selling to Snowflake’s 6,000 customers.6


A Snowflake app store also starts to collide with the other nascent “app platforms” in the space, likedbt’sandLooker’sunified semantic layers. In Google’s case, their offering is likely to become directly competitive at some point, the Android Play Store to Snowflake’s iOS App Store. That’s ok though; the two would likely share structural similarities, and would expand the market to Google customers as well.


dbt is in a more interesting position. Down one path, they could embed themselvesbehindapp development frameworks, providing additional logical governance for entities and metrics. Or they could expand upwards, and offer an open, database-agnostic development environment, whereUsers.filter(...)gets translated into the SQL dialect of your choosing.7


Regardless, Snowflake has set the avalanche in motion. The release has been triggered, a data app development framework is coming, and an app store is close behind. It won’t completely reshape the data landscape—avalanches level trees, not mountains—because we’ll still needcore categorieslike centralized warehouses, ETL pipelines, and robust analytics tools. But it will blanket thousands of enterprise experiences, from how we hire to how we send prospects’ swag, with a cascade of small data apps that do very little, but do it very well.


That’s how Apple and Android devices injected software into every corner of our personal lives. And it’s how the modern data stack will inject data into every operational nook of professional lives.

[1](https://benn.substack.com/p/the-data-app-store#footnote-anchor-1-50157390)

Sooner or later, Frank Slootman comes for us all.

[2](https://benn.substack.com/p/the-data-app-store#footnote-anchor-2-50157390)

One assumes. I have no idea what they’re actually doing.Nobody tells me nothing; I’m just out here taking swings.

[3](https://benn.substack.com/p/the-data-app-store#footnote-anchor-3-50157390)

Mint? Data app, because you use it to manage your personal finances, but if you remove the data about your spending patterns, it no longer works. Salesforce? Not a data app, because you can take the reports out of Salesforce and still have a reasonably functional CRM. TheNew York Times’COVID dashboard? Not a data app, because it’s not a product meant to solve a problem; it’s just an interface for exposing data.

[4](https://benn.substack.com/p/the-data-app-store#footnote-anchor-4-50157390)

I’m apersonal investorin Supergrain.

[5](https://benn.substack.com/p/the-data-app-store#footnote-anchor-5-50157390)

While reverse ETL tools could also do this, that means the ETL tool has to build the integrationandthe customer has to buy the reverse ETL tool. If the goal is make the app marketplace more dynamic, adding in a bunch of extra costs and product dependencies probably doesn’t get us very far.

[6](https://benn.substack.com/p/the-data-app-store#footnote-anchor-6-50157390)

This doesn’t apply to some types of products. For example, analytics and BI tools, almost by definition, need access to a wide range of data sources.

[7](https://benn.substack.com/p/the-data-app-store#footnote-anchor-7-50157390)

“I’ll take door number 3, Monty: This is all nonsense, these are all terrible ideas, and we’ll be ignoring the whole thing.”
