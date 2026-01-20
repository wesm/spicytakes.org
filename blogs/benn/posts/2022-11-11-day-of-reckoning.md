---
title: "Data’s day of reckoning"
subtitle: "They’ve got data marts like gold, and ours are a little more like stone."
date: 2022-11-11T17:44:30+00:00
url: https://benn.substack.com/p/day-of-reckoning
slug: day-of-reckoning
word_count: 2051
---


![Peat takes millennia to generate, and bogs store 10 times more carbon than  forests — using it in gardening is madness - Country Life](https://substackcdn.com/image/fetch/$s_!ODhJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F48b9ddc4-4211-4910-8f1d-1ef0a62a0121_2560x1707.jpeg)


Tools are out; people and processes are in.1


After two years of excited debate about data startups and technologies, and hype about the modern data stack, the zeitgeist—andcollapsing SaaS valuations—wants usto move onto the more pragmatic stuff: How to build teams, how to find and solve meaningful problems, how to collaborate, how to “do the work.” All the technology in the world hasn’t saved us fromarguing about mismatched dashboards; better data teams and cultures,modeled after those inside the best companies in the world, might.


Fair; I’m all for those conversations.2But underneath this pivot is an unnerving worry that I can’t quite shake. Even if we have the tools that companies likeNetflix,Google,Airbnb, and others have, and even if we copy their cultures and hire their employees, we’re still missing the third leg of their gold-plated analytical stool: Their data. And without that—and without similar business problems to apply it to—I’m not sure how much all of the data industry’s recent sound and fury is really worth.


# It’s not a data lake, it’s a peat bog


True or not, and with no disrespect to the pioneers inoperations researchanddecision support,most people see Silicon Valley3as the birthplace of today’s modern data practices. Iconic tech companies’ data teamswere the field’s first superstars, coining thetermsand creating thetechnologiesthat define the industry today. These teams were also huge profit centers for their employers, optimizing products, ad markets, and business operations to the tune of billions of dollars in revenue. It was these companies, and their staggering fortunes, that inspired the analogy thatdata is the new oil.


When we ask how they were so successful, we typically credit their teams and their talent. They were great, we say, because they were so good.


The converse, however, is just as plausible. Facebook and Google, for example, can clearly make a lot of money by using their data to serve better ads. Netflix can clearly improve its business by using viewership logs to better promote the content that they offer. Uber can clearly make their service better by shortening wait times. And all of these companies operate at such an extraordinary scale that seemingly trivial improvements are amplified into meaningful financial gains. In these contexts, data has tremendous leverage—leverage that, even if used clumsily, could still produce impressive results.


In other words, rather than being exemplars of good data practices because they were so good, it’s possible that they’re exemplars becausethey didn’t have to be that good.


In that light, when the rest of us struggle to keep up, it’s not because we don’t have their tools or cultures; it’s because we don’t have their data. The data of a mid-sized B2B SaaS product simply doesn’t have the potential energy of Google’s search histories, or of an Amazon’s browsing logs.4If the latter examples are the new oil, the former is a new peat bog. No matter how good the tools are that clean and analyze it, how skilled the engineers are who are working on it, or how mature the culture is around it, it’ll never burn ashot or as bright.


This is why I think, if you wanted to put forward case for how the entire modern data stack fails, themost tilted argumentmaking that claim—that today’s tools let people build inefficient infrastructure that encourages companies to solve problems with expensive brute-force computing—is looking in the right direction, but makes the wrong point.


Consider cloud computing. Companies spend massive amounts of money on AWS, GCP, and Azure—multiples more than they do on data tooling. Moreover, a lot of this spend is probably unnecessary: Services are over-provisioned; they run inefficient code; problems that could be solved with better engineering are solved with more EC2 instances. And yet, save theoccasional skeptical look, we’ve generally accepted that this is the cost of doing business in 2022. The value that most customers get out of their cloud provider—even with mediocre development teams and lazy deployments—is so plainly high that companies are willing to absorb those inefficiencies. Even with extraneous spend, there’s plenty ofconsumer surplus.


For companies like Netflix and Airbnb—the ones whose data is high-grade oil—the margins on data investments5are similarly high. Inefficiencies don’t drown out the benefit. But companies that are harvesting peat, for whom data has fewer clear applications, don’t have those margins. For them, emulating the practices of high-margin businesses—i.e., those that can afford inefficiencies in their data initiatives—is a trap. Peat suppliers can’t copy the refinement methods and cost structures of oil producers and still expect to come out ahead; small SaaS businesses can’t operate as though their data has anywhere near the same value as Uber’s or Airbnb’s. And yet, that’s what most of us do—we assume that there are diamonds buried in our rough data, if only we clean it properly, analyze it effectively, or stuff it through the right YC startup's new tool.6


But what if there aren’t? Or what if they’re buried so deep that they’re impractical to extract?7What if some data, no matter how clean and complete it is, just isn’t valuable to the business that owns it?


# Gas over SaaS


To illustrate this point, suppose that you’re banished (or raptured away, you choose) to some west coast exurb. You decide to embrace the analog life, and buy a gas station just off the interstate. For a while, you run it like I’d imagine most gas stations are run.8You price your gas based on how much it costs to buy, adding or subtracting a few cents to stay competitive with the Citgo a half-mile up the road. You tried staying open 24/7, but you didn’t get many customers late at night, so now you close at 11 p.m. You replace expensive gas lines and pumps only when they break. You take all major credit cards.


One morning, a traveling salesman shows up with a magical offer: For a moderate fee, they can give you, in perfectly clean and queryable form, a dataset of every interaction your customers have ever had with your gas station. It’s the holy grail of corporate data—what your customers bought, when they bought it, how much it cost, how long they were at your pump, if they were on their phone when they were.9The data also captures every demographic detail about the customer, and includes exact information about who they are, what they do, and the car they drove. It even tells you what was happening inside of their heads, from what brought them to your gas station to what they thought of it when they left.


At first glance, it’s a gold mine of incalculable worth—every question answered; every curiosity satisfied. But upon a bit more reflection, that value starts to fade. Your costs are largely fixed by external markets; no analysis will get you cheaper gas. You can adjust your prices, but those are anchored to your costs and to what your competitors are charging up the street. You already know, from checking tank levels every week, that customers prefer regular gas over the higher octane varietals.10The dataset might reveal that you get a lot of Toyota Siennas at your station because you’re close to an elementary school, but you aren’t going to run Facebook ads targeting van owners or young parents. Even if you find out that customers think your pumps are slower than most, it’s not affordable to replace them unless you need to. Maybe you decide to stop taking American Express, and save dozens of dollars a month.


Put differently, as enticing as the salesman’s offer is, his data wouldn’t materially change how you manage your business. Looking at monthly spreadsheets and periodically talking to customers is guidance enough. The omniscient dataset isn’t worth the cost.


# WAGMI


Obviously, most companies aren’t gas stations. But most aren’t Square or Stitch Fix either. They probably sit somewhere in the middle, with moderately valuable datasets that can inspire moderate business improvements. That’s not bad, but it’s the promise that a lot of companies seem to think they’re buying.


If there’s a reckoning in the data industry, it’ll come from our expectations of data coming back to earth. It’ll come from companies who saw what a handful of trendy high-flyers were able to do with data, and thought that they should do the same without questioning if they actually could. It’ll come from business leaders believing that beingdata-driven wins, and not recognizing the importance of the data that’s doing the driving.11It’ll come from people realizing that, no matter what tools they buy or who they poach from Google, data will never be to them what it is to Google.


To avoid this kind of meltdown (and it’s been abigweekformeltdowns), I think we have to be more targeted in our ambitions, as both data teams and as data vendors. Focus on proven tooling and use cases—reporting, dare I say decision support—over moonshots. Focus on identifying which few datasets have real value, rather than assuming it’s all of them. And perhaps most of all, rather than trying to copy the companies whose oil fields made them rich, focus on the learning from the businesses that are build on peat bogs.


---


# Bonus: Survey results!


Four months ago, I askedpeople how they would rankthe value of five types of competitive edges in a startup: Experience, speed, operational excellence, data savvy, and talent.


Surprisingly to me, experience won. Twenty-nine percent of the 171 respondents voted for that as their top choice. Data savvy was the second most-popular top choice, with 21 percent of the votes. And nobody cared about operational excellence.


![](https://substackcdn.com/image/fetch/$s_!0G5l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6183e2a1-6ec8-4e37-af39-24f8bc8d39d7_994x348.png)


Experience, however, was somewhat more polarizing. The net approval rating of experience—the percentage of respondents who put experience in their top two choices minus the percentage who put it in their bottom two—was only 9 percent, compared to an approval rating of 16 percent for data.


Furthermore, data was preferred by more than half of all respondents in every head-to-head comparison.


![](https://substackcdn.com/image/fetch/$s_!0b9i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd334215b-d129-41cb-8c44-88976df1c51f_1102x330.png)


Still, the differences between all five characteristics are relatively small. So the main conclusion may be that, even among what’s likely a biased audience—the benn.substack.angellist.com syndicate is probably, for better or for worse, more embedded in the data world than most—a lot of investing comes down to personal opinions.

[1](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-1-83946516)

pwned.

[2](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-2-83946516)

Does that mean fewer posts about tooling and startups here? Probably not. We can have both, and I think those conversations are useful too. More importantly, though, I don’t write this blog to be useful in that way, but to rubberneck at the tech industry. And if a mindless bloggertypes outenough blog posts to eventuallyfind a worthwhile nut, that’sgravy.

[3](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-3-83946516)

If we can’t trust the Enterprise Big Data Framework® for this sort of information, who can we trust?

[4](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-4-83946516)

Speaking of datasets with a lot of potential energy, I will never understand how Pinterest isn’t the most valuable company in the world. Facebook is one of the most successful businesses in history, in large part because it can, through immensely complicated demographic profiling and behavior tracking, figure out what products you might want to buy. The entire business is built around serving you more and more relevant ads. On Pinterest, you just…tell it what you want, no inference or fancy math required. I mean, the whole product is justasking people to pick relevant ads for themselves.How is that not worth more money???

[5](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-5-83946516)

By margins, I mean how much value a company can generate by putting a dollar into their data organization (to, for example, serve better ads, make better decisions, or operate more efficiently), not the overall operating margin of the business.

[6](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-6-83946516)

A worthless datasetisn’t a true Scotsman.

[7](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-7-83946516)

Is aplanet-sized diamondworth anything if it’s forty light years from earth?

[8](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-8-83946516)

If you actually own a gas station, I have questions.Email me,DM me,connect with me on LinkedIn.

[9](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-9-83946516)

If they put the gas in the car, oron each other.

[10](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-10-83946516)

Regular is floral, light-bodied, with hints of grapefruit and tangerine.V-Poweris fuller, more tannic, and has bits of cherry and rubber cement on the nose.

[11](https://benn.substack.com/p/day-of-reckoning#footnote-anchor-11-83946516)

And for the love of god, I do not mean how clean the data is. Messy data being worthless doesn’t imply clean data is valuable.
