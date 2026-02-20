---
title: "Doubling SaaS Revenue By Changing The Pricing Model"
date: 2012-08-13
url: https://www.kalzumeus.com/2012/08/13/doubling-saas-revenue/
slug: doubling-saas-revenue
word_count: 2538
---


Most technical founders abominably misprice their SaaS offerings to start out.  I’m as guilty of this as anyone, so I wrote up my observations about un-borking this as The Black Arts of SaaS pricing a few months ago.  (It went out to my mailing list — [sign up](https://training.kalzumeus.com) and you’ll get it tomorrow.)  A few companies implemented advice in there to positive effect, and one actually let me write about it, so here we go:


## Aligning Price With Customer Value


[Server Density](http://www.serverdensity.com) does server monitoring to a) give you peace of mind when all is well and b) alert you really darn quickly when all isn’t.  (Sidenote: If you run a software business, you absolutely need some form of server monitoring, because the application being down costs you money and trust.  I personally use [Scout](http://www.scoutapp.com) because of great Ruby integration options.  They woke me up today, as a matter of fact — apparently I had misconfigured a cronjob last night.)


Anyhow, Server Density previously used a pricing system much beloved by technical founders: highly configurable pricing.


Why do geeks love this sort of pricing?  Well, on the surface it appears to align price with customer success (bigger customers pay more money), it gives you the excuse to have really fun widgets on your pricing page, and it seems to offer low-cost entry options which then scale to the moon.


I hate, hate, **hate** this pricing scheme.  Let me try to explain the pricing in words so that you can understand why:

- It costs $11 per server plus $2 per website.
- Except if you have more than 10 servers it costs $8 per server plus $2 per website.
- Except if you have more than 50 servers it costs $7 per server plus $2 per website.


**This is very complicated and does not align pricing with customer success.  **Why not?


## Pricing Scaling Linearly When Customer Value Scales Exponentially Is A Poor Decision


Dave at Server Density explained to me that their core, sweet-spot customer has approximately 7 servers, but that the per-server pricing [was chosen](http://blog.serverdensity.com/choosing-a-price-for-your-webapp-or-startup-using-multivariate-testing/) to be cheap to brand-new single-server customers.  They were very concerned with competing with free.


Regardless of whether this wins additional $13 accounts, it clearly under-values the service for 7 server accounts, because their mission-critical server monitoring software in charge of paging the $10,000 a month on-call sysadmin to stop thousands of dollars of losses per minute *only costs $79*.  You don’t get 7x the value from server monitoring if you increase your server fleet by 7x, you get (at least) 50x the value.  After you get past hobby project you quickly get into the realms of a) serious revenue being directly dependent on the website, b) serious hard costs like fully-loaded developer salaries for doing suboptimal “cobble it together ourselves from monit scripts” solutions, and c) serious career/business reputational risks if things break.


Let’s talk about those $13 accounts for a moment.  Are $13 accounts for server monitoring likely to be experienced sysadmins doing meaningful work for businesses who will solve their own problems and pay without complaint every month?  No, they’re going to be the worst possible [pathological customers](http://www.hnsearch.com/search#request/all&q=patio11+pathological+customers&sortby=points+desc).  They’ll be hobbyists.  Their servers are going to break all the time.  They’re going to misconfigure Server Density and then blame it for their server breaking all the time.  **They’ll complain that Server Density** **costs infinity percent more than OSS, **because they value their own time at zero, not having to e.g. pay salaries or account for a budget or anything.


My advice to Dave was that Server Density switch to a SaaS pricing model with 3~4 tiers segmented loosely by usage, and break with the linear charging.  The advantages:

- **Trivial to buy** for non-technical stakeholders: name the plans correctly and they won’t even need to count servers to do things correctly.  (“We’re an enterprise!  Of course we need the Enterprise plan!”)
- **Predictable pricing**.  You know that no matter what the sysadmins do this month, you’re likely to end up paying the same amount.
- **Less decisions.  **Rather than needing to do capacity planning, gather data internally, and then use a custom-built web application to determine your pricing, you can just read the grid and make a decision in 30 seconds.
- **More alignment with business goals.  **Unless you own a hosting company, “number of servers owned” is not a metric your CEO cares about.  It only tends to weakly proxy revenue.  Yes, in general, a company with 10 servers tends to have more commercial success than a company with 1 server, but there are plenty of single-server companies with 8 figures of revenue.


(Speaking of custom-built web applications to determine pricing, the best product with the worse pricing strategy is [Heroku](http://www.heroku.com/pricing#0-0).  Enormously successful, but I’m pretty sure they could do better, and have been [saying so for years](http://news.ycombinator.com/item?id=577622).  All Heroku would have to do is come up with four tiers of service, attach reasonable dynos/workers/databases to them, and make that the core offering for 90% of new accounts.  You could even keep the actual billing model entirely intact: make the plans an abstraction over sensible defaults picked for the old billing model, and have the Spreadsheet Samurai page somewhere where power users and the sales team can find it.)


## Ditching Linear Scaling In Favor Of A Plan Model


After thinking on my advice, Server Density came up with this redesign:


**I love this.**

- The minimum buy-in for the service is now $99 a month, which will segment away customers who are less serious about their server uptime.
- You now only need to make one decision, rather than needing to know two numbers (which you might not have access to at many of their customers).
- The segmentation on users immediately triples the price for serious businesses using the service, irrespective of the size of their server fleet.  This is good because **serious businesses generate a lot of money no matter how many servers they have**.
- Phone support will be an absolute requirement at many companies, and immediately pushes them into the $500 a month bucket.


My minor quibbles:

- I still think it is underpriced at the top end.  Then again I say that about everything.
- Did you notice the *real* Enterprise pricing?  (Bottom right corner, titled “More than 100?”) Like many SaaS services, Server Density will quote you a custom plan if you have higher needs.  Given that these customers are extraordinarily valuable to the business both for direct sales and for social proof, I might make this one a little more prominent.


## Results From Testing: 100% Increase In Revenue


Server Density implemented an A/B test of the two pricing strategies using [VWO](https://vwo.com).


At this point, there’s someone in the audience saying “That’s illegal!”  That person is just plain wrong.  There is no carbon in a water molecule, and price testing is not illegal.


What if the fact of the price testing were discovered?  **Not really that problematic**: you can always offer to switch someone to the most advantageous pricing model for them.  Since most existing customers would pay less under variable pricing than they would under the above pricing grid, simply grandfathering them in on it removes any problem from people who have an actual stake in the business.  For new customers who get the new pricing grid but really, really feel that they should be a $13 a month account, you can always say “Oh, yep, we were testing.  I’ll give you the $13 pricing if you want it.”  (David from Server Density says that this is in fact what they did, three times, and had no lasting complaints.)


Most customers will not react like this because **most customers do not care about price**.  (Those that do are disproportionately terrible customers.  To quote David from Server Density, “We had the occasional complaint that pricing was too high but this was from users with either just a single server or very low cost VPSs where the cost of monitoring (even at $10/m) was more than the cost of the server.”)


Anyhow, where were we?  Oh yeah, making Server Density piles of money.  They requested that I not disclose the interval the test was conducted over, to avoid anyone reasoning back to their e.g. top-line revenues, but were OK with publishing exact stats otherwise.


**Variable pricing**: 150 free trial signups / 2161 visitors


**Pricing plans**: 113 free trial signups / 2153 visitors


At this point, variable pricing is **clobbering** the pricing plans (they get 25% less signups and pricing plans being inferior at maximizing trials has a confidence over 99%)… but let’s wait until this cohort reaches the end of the trial period, shall we?


Server Density does not make credit card capture mandatory.  (I might suggest revising that decision as another test.)


**Variable pricing**: 23 credit cards added / 2161 visitors


**Pricing plans**: 18 credit cards added / 2153 visitors


That’s a fairly similar attachment rate for credit cards.  But collecting credit cards doesn’t actually keep the lights on — the important thing is how much you successfully charge them, and that is highly sensitive to the prices.


**Variable pricing**: $420 monthly revenue added / 2161 visitors   (~$0.19 a visitor)


**Pricing plans**: $876 monthly revenue added / 2153 visitors  (~$0.41 a visitor)


**+100% revenue** (and revenue-per-visitor) for that cohort.  Pretty cool.


(P.S. Mathematically inclined readers might get puzzled at the exact revenue numbers — how do you get $876 from summing $99, $299, and $499?  Long story short: Server Density is a UK company and there are conversion issues from GBP to USD and back again.  They distort the exact revenue numbers a wee bit, but it comes out in the wash statistically.)


## We Doubled Revenue?!  Can We Trust That Result?


Visual Website Optimizer displays on the dashboard that it is 93% confident that there was indeed a difference between the two.  (The reported confidence intervals are $0.19 +/- 0.08 and $0.41 +/- $0.16.  How to read that?  Well, draw your bell curves and do some shading, but for a qualitative description, “Our best guess is that we doubled performance, but there’s some room for error in these approximations.  What would those errors look like?  Well, calculus happens, here we go: it is more likely that the true performance improvement is more than ~3x than it is that there was, in fact, no increase in performance.”)


Truth be told, I don’t know if I trust that confidence in improvement or not, because I don’t understand the stats behind it.  I understand the reported confidence intervals and what they purport to measure, I just don’t know of a defensible way to get the data to that point.  The ways I’m aware of for generating confidence intervals for averages/aggregates of a particular statistic (like, say, “Average monthly revenue per visitor of all visitors who would ever sign up under the pricing plan”) all have to assume something about the population distribution.  One popular assumption is “Assume normality”, but that’s known to be clearly wrong — no plausible arrangement of numbers makes X% $99, Y% 299, Z% $499 into a normal distribution.  **Even in absence of a rigorous test for statistical confidence**, though, there’s additional information that can’t be put in this public writeup which causes me to put this experiment in the “highly probable win” column.  (If my Stats 102 is failing me and there’s a simple test I am neglecting, feel free to send me an email or drop a mention in the comments.)


Note that since this is a SaaS business that is **monthly revenue added**.  Increasing your monthly revenue from a particular cohort by $450 increases your predicted revenue over the next year by in excess of $4,000.  (The calculation is dependent on your churn rate.  I’m just making a wild guess for Server Density’s, biased to be conservative and against their interests.)


Now, in the real world, SaaS customers’ value can change over time via plan upgrades and downgrades, and one would ideally collect many months of cohort analyses to see how things shook out.  Unfortunately, in the equally real world which we actually live in, sometimes we have to reason from incomplete data.  If you saw a win this dramatic in your business and were wondering whether you could “take your winnings” now by adopting the new pricing across all new accounts, I would suggest informing that decision with what you previously know about customer behavior vis-a-vis number of servers over time.  My naive guess is that once a server goes into service it gets taken out of service *quite rarely indeed* and, as a consequence, most Server Density accounts probably have roughly static value and the few that change overwhelmingly go up.


And what about the support load?  Well, true to expectations, it has largely been from paid experts at larger companies, rather than from hobbyists complaining that they don’t get the moon and stars for their $13 a month.  Dave was particularly impressed how many were happy to hop on a phone call to talk about requirements (which helps learn about the customer segments and develop the future development and marketing roadmaps) — meanwhile, the variable pricing customers largely a) don’t want to talk about things and b) need a password reset *right now* WTF is taking so long.


Server Density expects that their plan customers will be much less aggravating to deal with in the future, but it is still early days yet and they don’t have firm numbers to back up that impression.


## Testing Pricing Can Really Move The Needle For Your Business


Virtually no one gets pricing right on the first try.


(When I wrote the [pricing grid](http://www.appointmentreminder.org/pricing/) for Appointment Reminder I snuck a $9 plan in there, against my own better judgment, and paid for that decision for a year.  I recently nixed it and added a $199 plan instead.  Both of those decisions changes been nothing but win.)


Since you probably don’t have optimum pricing, strongly consider some sort of price testing.  If I can make one concrete recommendation, consider more radical “packaging” restructurings rather than e.g. keeping the same plan structure and playing around with the plan prices +/- $10.  (This means that, in addition to tweaking numbers, you find some sort of differentiation in features or the consolidated offering that you can use to segment a particular group of customers into a higher plan than they would otherwise be at numerically.)


For more recommendations, again, you probably want to be [on my mailing list](https://training.kalzumeus.com).  You’ll get an email today with a link to a 45 minute video about improving your app’s first run experience, the email about SaaS pricing tomorrow, and then an email about weekly or biweekly about topics you’ll find interesting.  Server Density is not the only company telling me that those emails have really been worth people’s time, but if they don’t appeal to your taste, feel free to unsubscribe (or drop me an email to tell me what you’d rather read) at any time.


*Disclosure*: Server Density is not a client, which is very convenient for me, because I’m not ordinarily at liberty to talk about doubling a client’s revenue.
