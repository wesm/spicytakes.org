---
title: "Rituals for Engineering Teams"
date: 2022-08-15
url: https://charity.wtf/2022/08/15/rituals-for-engineering-teams/
word_count: 1600
---


Last weekend I happened to pick up a book called “[Rituals For Work: 50 Ways To Create Engagement, Shared Purpose, And A Culture That Can Adapt To Change](https://www.amazon.com/Rituals-Work-Engagement-Bottom-Up-Innovation/dp/1119530784/ref=asc_df_1119530784/).” It’s a super quick read, more comic book than textbook, but I liked it.


It got me thinking about the many rituals I have initiated and/or participated in over the course of my career. Of course, I never thought of them as such — I thought of them as “having fun at work” 🙃 — but now I realize these rituals disproportionately contribute to my favorite moments and the most precious memories of my career.


> Rituals (a definition): Actions that a person or group does repeatedly, following a similar pattern or script, in which they’ve imbued symbolism and meaning.


I think it is extremely worth reading the first 27 pages of the book — the Introduction and Part One. To briefly sum up the first couple chapters: the power of creative rituals comes from their ability to link the physical with the psychological and emotional, all with the benefit of “regulation” and intentionality. Physically going through the process of a ritual helps people feel satisfied and in control, with better emotional regulation and the ability to act in a steadier and more focused way. Rituals also powerfully increase people’s sense of belonging, giving them a stable feeling of social connection. (p. 5-6)


The thing that grabbed me here is that **rituals create a sense of belonging**. You show that you belong to the group by participating in the ritual. You *feel* like you belong to the group by participating in the ritual. This is powerful shit!


It seems especially relevant these days when so many of us are atomized and physically separated from our teammates. That ineffable sense of *belonging* can make all the difference between a job that you do and a role that feeds your soul. Rituals are a way to create that sense of belonging. Hot damn.


So I thought I’d write up some of the rituals for engineering teams I remember from jobs past. I would love to hear about your favorite rituals, or your experience with them (good or bad). Tell me your stories at [@mipsytipsy](http://twitter.com/mipsytipsy). 🙃


## Rituals at Linden Lab


### Feature Fish Freeze


At [Linden Lab](http://lindenlab.com), in the ancient era of SVN, we had something called the “Feature Fish”. It was a rubber fish that we kept in the freezer, frozen in a block of ice. We would periodically cut a branch for testing and deployment and call a feature freeze. Merging code into the branch was painful and time consuming, so If you wanted to get a feature in after the code freeze, you had to first take the fish out of the freezer and unfreeze it.


This took a while, so you would have to sit there and consider your sins as it slowly thawed. Subtext: Do you *really* need to break code freeze?


### Stuffy the Code Reviewer


You were supposed to pair with another engineer for code review. In your commit message, you had to include the name of your reviewer or your merge would be rejected. But the template would also accept the name “Stuffy”, to confess that your only reviewer had been…Stuffy, the stuffed animal.


However if your review partner was Stuffy, you would have to narrate the full explanation of Stuffy’s code review (i.e., what questions Stuffy asked, what changes he suggested and what he thought of your code) at the next engineering meeting. Out loud.


### Shrek Ears


We had a matted green felt headband with ogre ears on it, called the Shrek Ears. The first time an engineer broke production, they would put on the Ears for a day. This might sound unpleasant, like a dunce cap, but no — it was a rite of passage. It was a badge of honor! *Everyone* breaks production eventually, if they’re working on something meaningful.


If you were wearing the Shrek Ears, people would stop you throughout the day and excitedly ask what happened, and reminisce about the first time *they* broke production. It became a way for 1) new engineers to meet lots of their teammates, 2) to socialize lots of production wisdom and risk factors, and 3) to normalize the fact that yes, things break sometimes, and* it’s okay* — nobody is going to yell at you. ☺️


This is probably the number one ritual that *everybody* remembers about Linden Lab. “Congratulations on breaking production — you’re really one of us now!”


### Vorpal Bunny


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2022/08/vorpal.jpeg?resize=281%2C300&ssl=1)

*vorpal bunny*


We had a stuffed Vorpal Bunny, duct taped to a 3″ high speaker stand, and the operations engineer on call would put the bunny on their desk so people knew who it was safe to interrupt with questions or problems.


At some point we lost the bunny (and added more offices), but it lingered on in company lore since the engineers kept on changing their IRC nick to “$name-bunny” when they went on call.


There was also a monstrous, 4-foot-long stuffed rainbow trout that was the source of endless IRC bot humor… I am just now noticing what a large number of Linden memories involve stuffed animals. Perhaps not surprising, given how many [furries](https://www.gizmodo.com.au/2021/04/abc-island-second-life-run-by-furries-was-a-misunderstood-oasis/) were on our platform ☺️


## Rituals at Parse


### The Tiara of Technical Debt


Whenever an engineer really took one for the team and dove headfirst into a spaghetti mess of tech debt, we would award them the “Tiara of Technical Debt” at the weekly all  hands. (It was a very sparkly rhinestone wedding tiara, and every engineer looked simply gorgeous in it.)


Examples included refactoring our golang rewrite code to support injection, converting our entire jenkins fleet from AWS instances to containers, and writing a new log parser for the gnarliest logs anyone had ever seen (for the MongoDB pluggable storage engine update).


### Bonfire of the Unicorns


We spent nearly 2.5 years rewriting our entire ruby/rails API codebase to golang. Then there was an extremely long tail of getting rid of everything that used the ruby unicorn HTTP server, endpoint by endpoint, site by site, service by service.


When we finally spun down the last unicorn workers, I brought in a bunch of rainbow unicorn paper sculptures and a jug of lighter fluid, and we ceremonially set fire to them in the Facebook courtyard, while many of the engineers in attendance gave their own (short but profane) eulogies.


### Mission Accomplished


This one requires a bit of backstory.


For two solid years after the acquisiton, Facebook leadership kept pressuring us to move off of AWS and on to FB infra. We kept saying “no, this is a bad idea; you have a flat network, and we allow developers all over the world to upload and execute random snippets of javascript,” and “no, this isn’t cost effective, because we run large multi-terabyte MongoDB replica sets by RAIDing together multiple EBS volumes, and you only have 2.5TB FusionIO (for extremely high-perf mysql/RocksDB) and 40 TB spinning rust volumes (for Hadoop), and also it’s impossible to shrink or slice up replsets”, and so forth. But they were adamant. “You don’t understand. We’re* Facebook*. We can do anything.” (Literal quote)


Finally we caved and got on board. We were excited! I announced the migration and started providing biweekly updates to the infra leadership groups. Four months later, when the  migration was half done, I get a ping from the same exact members of Facebook leadership:


“What are you doing?!?”

“Migrating!”

“You can’t do that, there are security issues!”

“No it’s fine, we have a fix for it.”

“There are hardware issues!”

“No it’s cool, we got it.”

“*You can’t do this!*!!”


ANYWAY. To make an EXTREMELY long and infuriating story short, they pulled the plug and canned the whole project. So I printed up a ten foot long “Mission Accomplished” banner (courtesy of George W Bush on the aircraft carrier), used Zuck’s credit card to buy $800 of top-shelf whiskey delivered straight to my desk (and cupcakes), and we threw an angry, ranty party until we all got it out of our systems.


### Blue Hair


I honestly don’t remember what this one was about, but I have extensive photographic evidence to   prove that I shaved the heads of and/or dyed the hair blue of at least seven members of engineering. I wish I could remember why! but all I remember is that it was *fucking hilarious*.


## In Conclusion


Coincidentally (or not), I have no memories of participating in any rituals at the jobs I didn’t like, only the jobs I loved. Huh.


One thing that stands out in my mind is that all the fun rituals tend to come bottoms-up. A ritual that comes from your VP can run the risk of feeling like forced fun, in a way it doesn’t if it’s coming from your peer or even your manager. I actually had the MOST fun with this shit as a line manager, because 1) I had budget and 2) it was my job to care about teaminess.


There are other rituals that it does make sense for executives to create, but they are less about hilarious fun and more about reinforcing values. Like [Amazon’s infamous door desks](https://www.aboutamazon.com/news/workplace/how-a-door-became-a-desk-and-a-symbol-of-amazon) are basically just a ritual to remind people to be frugal.


Rituals tend to accrue mutations and layers of meaning as time goes on. Great rituals often make no sense to anybody who isn’t in the know — that’s part of the magic of belonging. 🥰


[Now, go tell me about yours!](http://twitter.com/mipsytipsy)


charity
