---
title: "My AdWords Are Turned Off [Edit: Resolved]"
date: 2009-08-01
url: https://www.kalzumeus.com/2009/08/01/my-adwords-are-turned-off-scary-stuff/
slug: my-adwords-are-turned-off-scary-stuff
word_count: 1682
---


**[Edited to add**: My campaign returned to mostly normal on August 4th or thereabouts.  I still don’t know what the heck happened, but I’m happy things are normal.  I sent Google a second support request, but that may or may not have had anything to do with the fixing: it was not responded to.  I also added two additional ads (which both triggered a human review), upped my bids, and in general tried to flag the system to say “Hey system, new stuff here!”, so that may or may not have had something to do with it.  My current feelings about Google, on a 1 to 10 scale: performance of platform: 8, superiority over competing ad options: 10, support responsiveness: 3.  That 3 is generous, based on my *completely* *unevidenced thought* that it is possible someone inside Google actually saw the problem and intervened.  At the moment, though, **I have as convincing evidence for the existence of Google technical support as I have evidence for the existence of Santa Claus** — luckily for Google, in my heart of hearts, I still believe in Santa Claus.]


High on the list of things to do today was try my hand at making my [first landing page](http://www.bingocardcreator.com/lp/try_online).  I have recently started selling my product as an online web application in addition to downloadable software, and wanted to see if focusing pages on one or the other would improve my conversion rates.


Naturally, I had to log into AdWords to create the alternate ads to test this landing page against my usual ads, which just dump people at [my homepage](http://www.bingocardcreator.com).  Since AdWords is very fire and forget for me (yay, [Conversion Optimizer](http://www.google.com/adwords/conversionoptimizer/bingocard.htmlhttps://www.kalzumeus.com/2007/11/10/conversion-optimizer-adwords-done-right/)) I don’t log in more than once a month.  Thus, I hadn’t known that since July 23rd they’ve been ratcheted down from “most schoolteachers are out for summer so you’re only getting 10k impressions a day” to “almost turned off so you’re getting 20 impressions per day”.  Since AdWords account for a large portion of my sales this is, to be blunt, **absolutely terrifying**.


## Delving Deep Into Black Magic


AdWords includes a variety of automated means to diagnose why your ads aren’t showing.  They provided the very useful advice “It is because you haven’t input a valid means of payment yet.”  Google, the charge for $200 yesterday went through as swimmingly as the last $12,000 have gone.  **You have my freaking credit card on file**.


This left me with another alternative, contacting AdWords support.  Google really buries the email us button (behind useful automated diagnostics like the above, and equally helpful FAQ entries) because *Google hates dealing with customers*.  We’re little annoying things that don’t scale well when we can’t be handled perfectly algorithmically like all the world’s information (TM).  Stories about how their support is incompetent and outright hostile to speaking to customers [are](http://www.slash7.com/articles/2009/3/26/google-is-evil-worse-than-paypal-don-t-use-google-checkout-for-your-business) [legion](http://www.slash7.com/articles/2009/3/28/google-checkout-still-unfit-for-business-i-got-my-money-but-would-you).


I say this as someone who is a fan of Google.  Full disclosure: I am a case study about AdWords’ effectiveness.  [*Literally*](http://www.google.com/adwords/conversionoptimizer/bingocard.html).  When the system is operational it rocks my socks off, but when it goes off the rails you are screwed.


They’ve improved response times since the last time I used them.  It took me less than an hour to get a response.  (Aside: Last time it took almost two days to hear from them when I wrote in to complain about one of my ads being disapproved.  That time I got copy/pasted a portion from their TOS implying that [St. Patrick’s Day bingo cards](http://www.bingocardcreator.com/bingo-cards/holidays/st-patrick%27s-day) were gambling paraphenelia.  It took three back-and-forth emails before I convinced them that I am, in fact, not in the gambling business and if they read that *cough* Google case study *cough* they would see that.  But the ad missed St. Patrick’s Day, which rather sharply limited its commercial utility to me.)


## AdWords Support: Like Talking To A Markov Chain


My email (which was limited to 512 characters, because Google apparently after indexing the entire freaking Internet Google didn’t have enough hard disk space in BigTable to save bug reports of a useful length) explained who I was, what behavior I had seen (ad impressions down by a factor of a thousand), what behavior I had expected (ad impressions *not* down by a factor of a thousand), what factors I had already ruled out (disapproved ads, sudden CTR decrease, sudden conversion rate decrease, payments issues, quality score issues, etc, etc), and what resolution I wanted (a fix or cause that I could fix myself).


Here’s what the Googleplex Markov chain spit back:


```
It looks like you have some questions about your ad rank.
```


**Translation**: I did not even pretend to read your email, or else am unaware that the Content Network has no concept of ad rank per se.


```
In the future, you may find that the quickest way to find the answer to your question is
 through the Help Center at https://adwords.google.com/support/?hl=en_US?utm_id=hc. Or, try the
 AdWords Help Forum at http://www.google.com/support/forum/p/AdWords?hl=en?utm_id=aut, where you
 can share information and exchange ideas with other advertisers.
```


**Translation**: We really hate when you email us.  Please don’t.


```
Please note that it's possible your account may be under review. As you
may be aware, we periodically perform these reviews to ensure the highest
quality ads, verify billing information, and maintain general account
security. Per our Terms and Conditions
(https://adwords.google.com/select/tsandcsfinder), ads can undergo review
at any time. If your account is under review, we will get back to you
shortly.
```


**Translation**: You may be evil.  We don’t do evil, hence, we don’t do you.  You may not be evil — that would be a good thing, but we still hate talking to you.  If you’re evil, we kind of have to talk to you.  If not, whee, we don’t have to talk to you, so don’t be evil.


```
For your convenience, we've listed some relevant information below:
```


**Translation**: Here are twenty random links from our knowledge base.  Despite our expertise at ordering the world’s information, they are neither relevant nor even plausibly related to your inquiry, and most are an insult to your intelligence.    They won’t resolve your problem, but possibly they’ll stop you from trying to email Google again, which is our ultimate goal.


The uselessness of some of their suggestions beggars belief.  *“Why do the same ads show on different pages?”* Well, I didn’t click, but I’m going to guess that the reason the same ads show on different pages is because I paid $10,000 to have Google put my ads on their Content Network.  If my ads were not showing on different pages, that would be a problem.  **Oh, guess what — they aren’t!**


```
Sincerely,
The Google AdWords Team
```


**Translation**: You weren’t even worth enough of our time to have one of our $6 an hour Indian callcenter employees sign her name to this.


## What I Think Went Wrong


While waiting for the (as expected) useless reply from Google, I played forensic investigator with my stats from this year and last year.  Everything looked nominal — in particular, Conversion Optimizer is sensitive to conversion rates so if your website suddenly stops converting, you’ll find your ads turned off in short order.  (That is what you’re paying them for, after all.) I verified that my trial download was still converting as expected.  Yep, code present in pages, yep, code evaluating, yep, conversions reported in AdWords so Google must be getting the data.


Then I tried it for the online version.  The online version scores a conversion any time someone signs up for the trial and logs in successfully (that should be automatic on signup, but you never know, particularly with bots).  To prevent the same person from getting scored as a conversion every time they log in (which would cost me gratuitous amounts of money), I have Rails set up so that only on their first login after signup they get sent to a welcome action.  The welcome action, in addition to doing a bit of housekeeping, is supposed to set the @welcome instance variable so that the post-sign-in page knows to display the conversion tracking Javascript.


This is a Rails idiom that runs the dashboard method and then renders the dashboard action, so that the welcome-specific code gets executed and then the shared template gets called.  Did you spot the bug?  Yep, that @welcome really needs to be initialized to true.  I’m not quite sure how this got by testing but it would be easy to miss — the page will display fine and all the functionality works perfectly, it is just that Google fails to get a wee little ping to credit my account with a conversion.  Which I didn’t notice since my download page continued to ping as usual.


**I’m not even sure this was the problem**.  Even with the online trial siphoning off conversions that should have been credited, my conversion rate for July was close to historical norms (the online trial was largely adding conversions, not replacing them).  The issue with conversion siphoning in Conversion Optimizer is if you don’t score conversions then your apparent Cost Per Action goes up, and if that routinely exceeds your maximum desired CPA then they won’t bid for you anymore.  However, my CPA stayed at the usual level for the 3 weeks where a portion of conversions weren’t scored, prior to my ads not showing.


## What Next


Well, since I fixed the bug, I’m sort of in a wait-and-see mode.  If their algorithms auto-correct me back to my previous status, then life is peaches and cream again.  I also went ahead and scheduled a few new ads with my new landing page, which should start with very little “history”, positive or negative, so they’ll largely not be effected by this.  I know Google heavily biases their historical computations to consider recent history rather than overall account history, so I’m a little worried about making a full recovery.


And I’m blogging about this, obviously, because I want anybody else in the same situation to have some support which is not a Markov Chain.
