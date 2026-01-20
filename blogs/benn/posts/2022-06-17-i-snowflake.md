---
title: "iSnowflake"
subtitle: "It’s not the App Store. It’s the iPhone."
date: 2022-06-17T16:45:47+00:00
url: https://benn.substack.com/p/i-snowflake
slug: i-snowflake
word_count: 2258
---


![](https://substackcdn.com/image/fetch/$s_!N2zy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6c6cfe20-d4ab-4130-8d13-682f8fcd665a_640x356.png)

*The apps areinthe computer.*


The trip to Las Vegas—forSnowflake Summit, the first data Megaconference1since 2019—got off to an inauspicious start. My Uber to the airport cost a fortune, and the driver spent most of the trip complaining about, as he put it, “the flu.” When we took off, the Nasdaq was down 3.2 percent. When we landed—after five hours of searching for smooth air, rumbling over the Great Lakes like a Greyhound hydroplaning across a gravel road—theNasdaq was down 4.7 percent. The taxi driver from the airport said no tourists were in town because gas prices are so high.


On the opening night of the conference, I made a couple of slow laps around the vendor hall atCaesar’s Forum.2The room was full of glittering booths, eager salespeople, escalating lures for attention—swag, then a magician, then a raffle for a trip to Europe, then aski simulator—and, if we’re honest about it, dozens of nowmassively overvalueddata startups. Though entirely incidental, I couldn’t help but think that hosting such an extravagant celebration of the data industry,this weekof all weeks, at the conference center of a hotel that’s agiant replica of Romefelt a little on the nose. Like Las Vegas itself, the event felt like was an excuse to forget about what was happening around us, and to pretend we were somewhere else.


The content of the conference, I assumed, wouldn’t change this impression. Snowflake execs in blazers, jeans, and sneakers would announce a predictable set of database improvements. They’d tell us Snowflake is now bigger, faster, cheaper, and more secure. They’d demo new integrations, new partnerships, and new features. They’d tell us how excited they were to be here; how hard their teams have been working; how this was all for us, the customer. They’d trot out a few of those customers, who would also tell us how excited they were. One would win an award for customer of the year. We would learn best practices.


It would be boring—though in fairness,boring makes money—but we’d all pretend to be excited anyway. We’d mingle in clubs while wearing lanyards with our names on them. And then we’d go home, forgetting most of what we learned and who we met. What was going to happen in Vegas, I figured, would stay in Vegas.3


It didn’t quite happen this way.


To be sure, we made plenty of the scheduled stops. We had lots ofsponsoredfun. Save one passing remark about how Snowflake isn’t lowering its hiring targets, the collapsing tech market was roundly ignored. Snowflake announced that it’s nowbigger,faster, morecost-conscious, and moresecure. And the keynote closed with a nifty “one more thing.”


But amid the predictable spectacle, something genuinely big happened too—something with parallels to Apple that go beyond mimicking the Jobsian reveal. It was largely missed by the audience, though, because Snowflake whiffed on the announcement.4


# The anatomy of a data app


What’s a data app?


As best I can tell, the most common definition is a dashboard with interactive widgets. A sales forecasting report that lets you tweak assumptions about sales cycles and win rates is a data app; a tabbed set of charts and tables that shows how a customer has recently interacted with a product is a data app; an A/B testing dashboard that computes all of the relevant results of a chosen experiment is a data app.


In all of these cases—and in the example galleries of data app providers likeStreamlitandHex—data apps are overwhelmingly tools for consumption. If we were to draw diagrams of where apps are in the data stack, they’d sit squarely on top of the warehouse. In this way, they aren’t fundamentally different from classic BI tools; they just present data in more narrow, purpose-built ways.


This rough architecture has become implicit in the way we talk about data apps. Over the last eighteen months, a number of people have gotten excited about their potential, and, intentionally or not, we’ve all described them in this way:


Bucky Moore, on thefuture of cloud data services: “The logical next step is to use this foundation to build full-featured applications that both read and write to the warehouse.”


Patrick Chase, on thedata warehouse becoming the new backend: “It makes sense for apps to read and write to their customer’s data warehouse instead of their own database.”


Martin Casado, on thefuture of the data industry: “All apps are just going to be reimplemented on top of the data layer.”


You can imagine the technical diagram underneath all of these predictions: The data warehouse sits at the back, data apps at the front, and there’s an arrow representing a few nice APIs in between.


I had this same picture in mind after Snowflake acquired Streamlit, a tool for creating this type of data app, earlier this year.The deal made sense, I thought, because, with a few tweaks, Streamlit could become “a framework for interacting with Snowflake” to build data apps. With a few more tweaks, it could also be “a marketplace for apps that Snowflake stands behind.”


This week, Snowflake announced thatthey’re building exactly this. According to the announcement, they’re launching a “native application framework” for developing apps, and a marketplace for selling and distributing them.


Snowflake’s announcements framed these apps in the same way that Bucky, Patrick, Martin, and I did: They’re tools that sit on top of the warehouse.The launch post5shows a diagram of apps, on top of a database, with arrows in between them. The same post lists a few examples of data apps, and most of them, like “cost analytics for cloud platforms” and “financial transaction analytics,” sound little different than a dashboard. And in the keynote announcing the app framework and marketplace, Snowflake leaned heavily on Streamlit, suggesting that data apps are synonymous with Streamlit apps.


I think this is wrong. I don’t think Snowflake is building what this implies they’re building. Data apps are actually much more than blinged-out dashboards that sit on top of a warehouse. They’re also programs that runina data warehouse.


# Inthe computer


Later during the conference, I was talking with a couple of Mode folks6about a data privacy and protection product that automatically masks personally identifiable information in Snowflake. They asked if Mode, which runs queries against Snowflake, could ever integrate with this tool. Could we connect Mode to it, so that email addresses would be hidden in query results in Mode?


My initial thought was, sure, maybe. If the privacy product sat between Mode and Snowflake, it could intercept queries from Mode, do whatever magic it does, and send back masked results. Or we could connect to the tool via an API, and it’d give us some special query to run that would return concealed data.


But then it occurred to me—what if the privacy tool was a data app that raninsideSnowflake? What if Mode doesn’t even need to know that the tool exists, and we just send normal queries, as we always do? When they get to Snowflake, they’re executed according to logic defined by Snowflake’s native primitivesandthe custom apps that people have installed in Snowflake. What if apps aren’t simple widgets for consumption, but are foundational programs that fundamentally change how Snowflake operates?


This framing opens up a tremendous amount of potential for what data apps could do. ML tools likeContinual? A suite of Python-based stored procedures that run directly in Snowflake. A custom logging framework, like Segment or Snowplow, for how people are using your warehouse? A package that gets installed in Snowflake, and creates log tables directly. dbt packages, dbt metrics, native Jinja, a dbt scheduler, the entirety of dbt itself? All apps.


And like dbt, these apps could “just work” with everything else in Snowflake. One of the keys to dbt’s success is that it silently slid under every other tool in the stack. Nobody had to build an integration to dbt; you got it for free, via the tables it created in the warehouse.


The same would be true for the apps that run inside of Snowflake. A SQL-based ML package would be accessible via every BI tool or within dbt, with no work from either. A governance management service would apply its rules to every query run in Snowflake. A load-balancing app could automatically distribute jobs to the right warehouses to maximize speed at the lowest cost.


In this telling, Streamlit doesn’t become a framework for building apps; it becomes a platform-focused language likeSwift.7And to extend the analogy, Snowflake isn’t just an app store for buying widgets; it’s the entire iPhone. App developers don’t play in a limited sandbox; they can write custom programs that can take full advantage of the system’s hardware and native software.


Moreover, like an iPhone, Snowflake could automatically manage things like app permissions. A reverse ETL app would be granted permission to send data outside of Snowflake; an ML app might keep data inside Snowflake, but be allowed to send metadata back to a SaaS service so that people could configure it; a logging app could be prevented from communicating with anything outside of Snowflake itself.


In addition to giving customers more control, this would dramatically alter the economics of data app development. If buyers can find apps in a store, and security teams can simply decide what permissions they’re comfortable granting without doing formal diligence, small teams could profitably develop and distribute apps. Installing a data app would be like downloading a mobile app: Put in a credit card, check a few permission boxes, and you’re ready to go.


Of course, even if Snowflake built all this, lots of things could go wrong. They could struggle to attract app developers—but Snowflake’s customer base is definitely big enough to entice some initial entrants, especially if development costs are reasonably low. The mobile app analogy could be flawed, because there are two mobile operating systems and dozens of databases—but given its growth rate, I suspect Snowflake is rapidly gaining market share. And Snowflake’s app store could become yet another graveyard of marginally useful widgets, like those that exist in everything fromSharepointtoSlack8—but if you can run apps inside Snowflake rather than just on top of it, it can be a platform for building anything you want to do with your data. This offers a far wider range of valuable possibilities than app stores that are essentially extension libraries for SaaS products.9


However high the risk is for Snowflake, I believe the reward is even higher. Running apps inside of a database could redefine what a database is as much as iPhones redefined what cell phones were. If momentum builds in the ecosystem, and what you can do with Snowflake expands at the pace of what the community can develop, other database vendors will have no choice but to chase it. As the first mover on a premier product, Snowflake will be the industry’s iOS—the platform every developer wants to build for first.


# Cambrian explosion, part III


At the start of the conference, one of Snowflake’s executives said that this moment didn’t represent the end of Snowflake’s journey, but the end of the beginning. My initial reaction was to roll my eyes, wonder what cliché someone would drop next,10and think that, if this conference marks the end of anything, it’s the passing of the market’s bull run and the reversal of the industry’s“Cambrian explosion” of new data tools and startups. Snowflake Summit wasn’t a graduation; it was the last party in Rome.


After hearing more about what Snowflake is going to build—or, more accurately, what I think they’re going to build, even if they haven’t quite said it themselves—I’m changing my mind. Snowflake could be on the cusp of changing what a database is, what data apps are, how they get built and sold, and what we can do with both of them. They could be building a platform that stokes the industry once more, and leads to another explosion of ideas and products. Rome isn’t falling; it’s simply evolving.


What happens in Vegas, it turns out, can also be meaningful.

[1](https://benn.substack.com/p/i-snowflake#footnote-anchor-1-59911367)

It’s like amegachurch: The preachers are paid salesmen, and the congregation is thinking about lunch.

[2](https://benn.substack.com/p/i-snowflake#footnote-anchor-2-59911367)

And you had to walk slow, lest you stumble on the alarmingly squishy carpet.

[3](https://benn.substack.com/p/i-snowflake#footnote-anchor-3-59911367)

Speaking of things happening in Vegas, according to Snowflake, about ten thousand people attended the conference. These are tech people, so many of them are rich. Some, I suspect, like to gamble. Of those who did, some people made money, and some lost money. Of all the people who lost money gambling,somebody lost the most money.How much do we think this person lost?

[4](https://benn.substack.com/p/i-snowflake#footnote-anchor-4-59911367)

Or, they just didn’t want to talk about it yet. I should probably give the company making a billion dollars and growing at 100 percent a year the benefit of the doubt.

[5](https://benn.substack.com/p/i-snowflake#footnote-anchor-5-59911367)

I’m not saying that it’s suspicious that this annoucement links to theexact momentin Martin’s talk atFuture DatathatI linked toin the post about Streamlit, but I’m notnotsaying that.

[6](https://benn.substack.com/p/i-snowflake#footnote-anchor-6-59911367)

In case it’s not obvious,I am a Mode folk.

[7](https://benn.substack.com/p/i-snowflake#footnote-anchor-7-59911367)

Admittedly, I have no idea if this is technically possible for Snowflake to build.

[8](https://benn.substack.com/p/i-snowflake#footnote-anchor-8-59911367)

You could argue that Slack apps are a key part of Slack, and I wouldn’t disagree. However, I don’t know many companies of any reasonable size whose primary product is a Slack app.

[9](https://benn.substack.com/p/i-snowflake#footnote-anchor-9-59911367)

In other words, apps in SaaS services can only be as valuable as the service. Apps on a data platform are far more open-ended, and have a much higher ceiling.

[10](https://benn.substack.com/p/i-snowflake#footnote-anchor-10-59911367)

“I know it’s hot here, but it’s a dry heat.”
