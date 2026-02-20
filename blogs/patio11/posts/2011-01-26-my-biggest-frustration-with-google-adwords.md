---
title: "My Biggest Frustration With Google AdWords"
date: 2011-01-26
url: https://www.kalzumeus.com/2011/01/26/my-biggest-frustration-with-google-adwords/
slug: my-biggest-frustration-with-google-adwords
word_count: 1606
---


Last week, I had an opportunity to talk with Andy Brice, who sells software for [wedding seating plans](http://www.perfectableplan.com) and the like.  He is an absolute genius with AdWords, and gave me some ideas on ways to improve my performance.  I immediately started to implement them, full with the excitement of a new project and wondering why I don’t spend more time optimizing AdWords.


Oh, **right**.


There were another 15 ads which I added last Friday-ish and are still Under Review.  Under Review is Google-speak for “We aren’t sure that this ad complies with our policies yet.”  While an ad is Under Review, it doesn’t show anywhere, and you aren’t learning anything by having it.


## Dealing With Shades of Grey


Google has a variety of businesses which it does not want to or legally cannot do business with.  To prevent them from using AdWords, they exercise prior restraint on AdWords copy, not letting their ads run until a human at Google has approved them.


One of the businesses that Google doesn’t want advertising (in the US, at any rate) is gambling.  Bingo is a form of gambling.  [Bingo Card Creator](http://www.bingocardcreator.com) is not a form of gambling — it is a form of software which helps elementary schoolkids learn to read.  This makes it rather hard to write focused, relevant advertisements responsive to customer queries like [how do I make a US presidents bingo card] which sell Bingo Card Creator without using the word “bingo” anywhere.


Google is, to all appearances, just using a keyword-based blacklist.  I guess all the eats-Bayesian-classifiers-for-lunch PhDs work in search and Gmail spam filtering, where they’ve clearly got an aptitude for understanding that words can have multiple meanings.  OK, fine, but at least the remaining boffins can do a blacklist correctly?


Well, not so much.

- Using Google’s Copy Ad feature to copy an ad, word for word, between ad groups will cause the new copy to go back into review purgatory.  This is despite that theoretically being a content-neutral action and a **core task for advertisers**, because many flavors of AdWords optimization rely on keywords being partitioned correctly into focused ad groups.
- Changing so much as a character of the ad, including landing page URLs, will cause the ad to get flagged again.  This only affects good advertisers.  Bad advertisers can presumably figure out how to serve whatever content they want on http://example.com/approved .  Pulling a bait-and-switch is absolutely trivial, since you have full control over what your own server serves to users.  This rule only inconveniences compliant advertisers, who get thrown into review purgatory every time they e.g. try to add another tracking parameter to their landing pages, switch from http:// to https://, etc etc.  I get the feeling I’m supposed to create five copies of each ad, pointing to /lp1 … /lp5 with identical content, and then if I need to do any testing I should get crafty with redirects or what have you later.  **That’s insane** - it is extra work that is directly against the spirit of the rules and unlike actual compliance **it works**.


## Scalable Communication Methods


According to Google:


We review all ads in the order they’re received, and we work to review all ads in our program as quickly as possible, usually within 1 to 2 business days or sooner.


If there were only 48 hours of lag time inserted every time I touched an AdWords ad, this would be annoying but tractable.  It would lengthen my time through the idea creation/validation loop (Lean Startup  fans know why that is a Very Bad Thing), but I could still get work done by batching all my edits together and then twiddling my thumbs for 48 hours.


Sadly, Google routinely falls short of their announced level of service.  And when I say “Falls short”, I mean “Ads can sit **for weeks** ‘Under Review’ and never be approved.”


This leads you to have to contact Google Customer Service to be able to get Google to give permission to give Google money.


## Google Customer Service: Welcome to Kafka


The first rule of Google Customer Service is that Google does not have Customer Service.  They prefer what Chief Engineer Matt Cutts describes as “scalable communication methods”: there are like a bazillion of you, there are only a few tens of thousands of us, instead of actually speaking to a human being you should read a blog post or watch a video or talk to a machine.  It is a wonderful, scalable model… when things work.


Anything which introduces a mandatory customer service interaction with Google is a process designed for failure.  AdWords approvals requires a customer service interaction.  Catch-22, to mix literary metaphors.


The “scalable communication methods” like AdWords Help have this to say about contacting customer service with regards to ad approvals:


Our Support team won’t be able to help you expedite this process.


That is not actually a true statement (which, incidentally, describes much of AdWords Help).  Length of time from ad submission to approval is, in my experiences, unbounded (literally, weeks can go by without approval).  Length of time from complaining to Support to approval: a day or two.  The most helpful Google employee I’ve ever Internet-met (name withheld to protect him from whatever dire punishments await someone who attempts to help customers) told me that my workflow should literally be 1) Submit ad 2) Submit ticket to get ad looked at, if I persistently fell into Under Review.


Google apparently knows it, too, since they have special-cased out the CS interaction for dealing with Ad approvals:


After filling in everything, I hit Submit expecting to be taken to a page which had an “OK, now actually tell us what the problem” comment box was.  No need — it has been optimized away!  Google doesn’t even want that much interaction.  (The last time I went through this — sometime last year — I recall there being a freeform field, limited to 512 characters or so.  I always use it to explain that I am not a gambling operation and if they want confirmation they can read the [AdWords case study](http://www.google.com/adwords/conversionoptimizer/bingocard.html) about my business.)


Google’s computers then weighed my support request and found it wanting:


Dear Advertiser,


Thank you for your e-mail. We understand you’d like us to review your ad.
 When you submit new ads or make changes to existing ads, they’re
 automatically submitted for review.


We work to review all ads in our program as quickly as possible. You
 should receive an email notification stating the approval status of your
 ads pending review within the next 3 business days. You can view the
 status of your ad any time in your account. The “Status” column in the
 “Ads” tab displays information on the current state of an individual ad
 variation.


For a list of Ad Approval Statuses, visit
 [http://adwords.google.com/support/aw/bin/answer.py?hl=en&answer=138186](http://adwords.google.com/support/aw/bin/answer.py?hl=en&answer=138186)


We are working as quickly as possible to get everyone up and running and
 should get to yours soon! If you have a different question, which doesn’t
 refer to pending ad approval, please get back to us via the ‘Contact Us’
 link in the Help Center at [https://adwords.google.com/support/aw/?hl=en](https://adwords.google.com/support/aw/?hl=en).
 Be sure to choose the category that is most relevant to your question.


Sincerely,


The Google AdWords Team


Well, at least the templating engine correctly replaced $BRUSHOFF_LETTER, but in terms of customer communication:

- You asked me to put in my name… you might want to think about using it.
- As much as I appreciate your False! Enthusiasm! if the next line of your letter is going  to be Eff Off And Die then maybe you should take out the exclamation points and give them to a Ruby programmer.  (We can always use more.)
- If the original timeline was 1-2 business days and the timeline three days later is “within 3 business days”, can we update them so that they quote it consistently?  Or maybe put something like “We get to 98.2% of approvals within 3 business days.”  (Or 2.89% of approvals within 3 business days, as the case may be.)


## Google’s Isolation From Market / Customer Pressure


Google theoretically values my business — I pay them $10,000 a year and would love to pay more.  Indeed, they can find my email address and have a human contact it when they want to do ad sales.  (I got an offer recently to set up a call with one of their AdWords Strategists to discuss optimization of my account… which is great, but previous experience leads me to believe he would use the same reports I have access to, make decisions with little understanding of my business, and then leave it to me to actually schedule the new ads/keywords and run headlong into Pending Review purgatory.)  But they are not doing very well lately at convincing me they actually care.  And they’ll still make a bazillion dollars without that, so no harm done.


In normal markets, I would be strongly tempted to take my business to vibrant competitive offerings.  Sadly, Google is pretty much the only game in town for viable CPC advertising: even if Microsoft/Yahoo exorcized the abominations haunting their UIs, they would not have enough inventory to matter for me in my niche (I’ve tried before).


Which leaves me with only one option: trying out my own scalable communication methods, and hoping someone in the Googleplex reads this and takes action to unbork this process (ideally, for a large class of advertisers).  It is the Internet equivalent of putting a message in a bottle and then throwing it into the ocean, but that is still an improvement on the normal channels.
