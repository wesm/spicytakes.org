---
title: "How A Half-Broken Halloween Promotion Smashed Revenue Records"
date: 2010-11-01
url: https://www.kalzumeus.com/2010/11/01/how-a-half-broken-halloween-promotion-smashed-revenue-records/
slug: how-a-half-broken-halloween-promotion-smashed-revenue-records
word_count: 2491
---


Happy Halloween!  Everyone’s favorite secular American holiday where kids are in school is invariably the best month of the year for [Bingo Card Creator](http://www.bingocardcreator.com).  This year, it ended up being a very happy Halloween indeed.  I ended up selling $6,024.45 worth of software after returns, beating my previous record (set last Halloween) by about 30%.  Bingo Card Creator has now sold **over $100,000 worth of software** (now *that* is spooky) and is on target to hit $45,000 in sales in 2010.


I did a bit of extra work getting the Halloween promotion to work this year, and also automating/systemizing so that I’ll be able to exploit similar opportunities without needing to take time off to do custom coding.  Some parts of the strategy worked very, very well.  Other parts lagged expectations.  And, naturally, I managed to make a critical CSS error and cost myself a few thousand dollars in sales… [again](https://www.kalzumeus.com/2009/10/23/the-ie-css-bug-which-cost-me-a-months-salary/).


## Timing A Seasonal Promotion


The best time to start preparing for Halloween is in September… preferably, a September *many years ago*.  This is because there is a huge, huge surge of Halloween-related queries on Google starting at about October 15th or so, and if you wait you won’t have your site ranking in time to ride the tidal wave.


[Halloween costumes], [Halloween parties], [Halloween ideas], etc etc, all follow almost the same distribution.  Most importantly for my business, so does [Halloween bingo cards].


A brief digression to understand why this is important: teachers want to play a game on Halloween because t is a children-centered holiday.  Halloween is a much more festive occasion in American schools than many other holidays, because kids are not given any time off for it and it is secular.  To make a long story short, there is a wide cultural rift in US education about the proper place of religion in public schools, and that makes celebrating e.g. Easter with a rousing game of bingo not exactly a career-enhancing move.  Despite Halloween being theoretically based on All Hallow’s Eve, in standard American practice it is totally secular in character.


Anyhow, to make a long story short, upwards of a hundred thousand people will go to the Googles and search for [Halloween bingo cards] and a passel of related terms in October.  For the last few years I’ve really wanted to be #1 for that.  This year, I was — my mini-site, established in September 2008 or so, finally hit the big time.


Halloween Bingo Cards is what SEOs call a mini-site.  It has one mission in life: for two weeks out of the year, it is supposed to be the best, most focused site on the Internet for, well, Halloween bingo cards.  Between on-page optimization, a handful of inlinks, the exact match domain bonus (it is a .net, which along with .com and .org receives a huge bonus to rankings if the domain name exact matches the query), and a bit of age, it finally edged out the competition.  The extra traffic I got was, well, **a little underwhelming**.


Why was I underwhelmed by 27,000 visits?  Well, the site was designed to generate trial signups of Bingo Card Creator, and most of the obvious candidates for action on the site linked people directly to a trial signup form.  Conversion rates were unspectacular, in part due to a technical failure describe later and and in part because a combination of design issues and just overall low traffic quality meant fairly few people clicked off Halloween Bingo Cards in the first place.


So:

- 27,000 people saw the Halloween mini-site
- 3,500 (**only about 13%**) clicked to the main site (and the signup form)
- 1,300 (**37%**) signed up for the free trial (that is actually extraordinarily good — normally I top out at about 28 ~ 30% for scalable traffic sources)


So of those 1,300 people, how many do you think actually signed up for BCC?  Well, since I finally have end-to-end analytics running (through a combination of KissMetrics/Mixpanel and a bit of glue code I wrote myself), I can get away from half-accurate Google Analytics reports and give concrete numbers on this.  So I know, with certainty, that that answer is 15 sales **directly attributable** to this page.  At about 1.2% conversion that isn’t that much to write home about — for the right audiences, BCC gets about 2%+.  (It should be noted that Halloween traffic is almost always going to be the wrong audience, because most *searchers* are parents but most of my *customers* are teachers: parents have their needs 100% met by the free trial.)


## So What Worked Better Then?


Email.  Holy cow, email.  This has been a blindspot of mine for years since I used to be an anti-spam researcher, do not really send or read mail that regularly outside of doing customer support, and hate newsletters with a passion.  **Big mistake**: my customers empirically do not feel the same way.


Halfway through last year I signed up for [MailChimp](http://www.mailchimp.com) with the intention of doing great things with it, but I struggled to get it to work out right.  I would lose interest for several months at a time and not send email to the list, which causes people to forget who you are and then get very peevish when they receive mail from you.  About the only thing that worked very well for me was my auto-responder, which automatically mails people 1 and 6 days after they sign up for it with hints and tricks, to basically remind them that I am still here.  (A huge percentage of BCC users never sign in after their first day, and anything I can do to remind them of my existence is worth serious money.)


Sadly, I got an automated notice from MailChimp several months ago about excessive unsubscribes from my autoresponder — about 1% (they’re **serious** about list quality at MailChimp), and paused it while editing to make it obvious who I was and why they were getting email from me.  (The phrase “because you went out of your way, *twice*, to ask for it” may have been in an initial draft.)  And then I left the autoresponder paused for several months.  *sigh* So I wrote a new alert for my dashboard about that, since I’m serious about making mistakes only once.


Anyhow: [Rob Walling](http://www.softwarebyrob.com) had an amazing [presentation](http://www.softwarebyrob.com/2010/10/12/the-1-goal-of-your-website-slides-from-my-business-of-software-talk/) at the Business of Software conference about using email to sell more software, and I was so inspired I decided to get serious about it this year.

- I used MailChimp filters to go down from the 8,000 or so people on my list to only the 800 signing up since June, figuring they would still remember me.  (In hindsight, I should have cut further, and I will make a point about absolutely, positively keeping the list “fresh” from here on out.)
- I tweaked my from address from “Bingo Card Creator” to be “Patrick McKenzie (Bingo Card Creator)”, at Rob’s suggestion.
- I mulled over reasons why teachers might open the mail, and settled on “A Halloween Activity (And Discount) From Your Friends at Bingo Card Creator”


The time-limited discount was repeatedly stressed in Rob’s presentation and in his [book about selling software](http://www.startupbook.net).  (He gave me a free copy.  You should buy it just for the email chapter.)  So I spent a few hours tweaking my shopping cart so it could use discounts, and then polished until the experience of receiving them was totally transparent to the user — they never have to fumble for a code, all they have to do is click a link in their email and they’re in.


This discount was extraordinarily effective at motivating sales, relative to many things I have tried.

- 775 mails sent.
- 170 (23%) opened
- Of those, 6 people bought.


At a little less than 1% conversion from an *email* to a sale, I’m absolutely giddy about the future potential for email marketing.  I got perhaps excessively giddy and sent another email two weeks later to people who didn’t open the first one.  At least, that was my intention: I actually hit the button for sending it to people who didn’t open last year’s Halloween newsletter (i.e. essentially everyone who had just been mailed two weeks prior).  *Doh*.


One person did not appreciate getting two newsletters in one month after not getting them for several months.  I got a handful of spam complaints for that (four from the first send, one from the second).  Since MailChimp is hypersensitive to spam complaints and I likewise care about my reputation, I’m going to be more careful in the future.  I anticipate the best thing to do to keep them down is to just email people early and often to keep myself in their mind, which is almost the opposite of my natural inclination.


Anyhow, the two campaigns together:

- 1,600 emails (total cost: $32 of MailChimp credits)
- 60 reactivated accounts
- 15 sales (~ $370 in revenue)


Very little I have done has **scalable 1,000% ROIs** on marketing spends.  You can bet I will be doing more of this in the future.  (Granted, this doesn’t count approximately 3 hours of effort upgrading my shopping cart and site to do discounts, but I can amortize that over every time I use them from here on out.  The newsletter was the 2009 Halloween newsletter with about 5 minutes of editing.)


## Speaking Of Discounts


So after having huge results early in the month with the emailed discount offer, I thought “Hey, why not extend that to everybody?  I’m getting crazy 10% conversion rates on reactivated accounts — if I got 10% conversion rates on new accounts I would be making hats out of money.”  Out of an abundance of caution, I A/B tested that for the last two weeks.  Surprisingly, **discounts failed to make a dent in sales numbers** in the general (non-email) population.  Roughly 2.08% of people seeing the discount converted, and 1.87% converted without seeing the discount.  That is despite prominent notices on the first screen after you log in, plus the pricing page, and the exploding nature of the discount (act now or you won’t get it).  Not only is that difference below the floor of statistical significance, when you factor in the fact that I make $5 less for every discounted copy, the full-price version did better for me.


Things to try next time:

- Only give the discount to people who I’m reactivating — their accounts are writeoffs if they don’t sign back in, after all.
- Pick the cutoff date for the discount better.  I gave people to November 1st, because Halloween is the 31st and I wanted to be generous.  However, that diminishes the perceived urgency of the sale — on Thursday night, they still have “3 days left!”  **That was stupid of me** because I know, from doing this for several years, that my window of opportunity for Halloween sales closes as soon as she goes to sleep on Thursday.  I should have had the Halloween sale go until Thursday night, which makes it a pretty cruddy “Halloween” sale but would almost certainly have goosed sales.


That said, that was a pretty good day for me — Wednesday before Halloween was my best day ever, right until Thursday smashed that record.  Last Halloween I was beginning to pull weeks upon weeks of crunch, and I think I probably made less in a 70 hour workweek than I did in those two days… while sleeping.  I love self-employment.


## Google Enjoyed Halloween, Too


While I was #1 on Google for [Halloween bingo cards], [Halloween bingo] and a thousand words on the long tail also receive significant traffic, and many of them are sewn up by about.com, eHow, etc etc.  Luckily, most of the content mills run AdSense ads, and the guy at the front of the auction screaming “Pick me pick me!” was yours truly. I spent $1,764.84 on AdWords ads in October.  Sadly, much of it got wasted.


Why?  Well, I made one extraordinarily poor decision and followed it up with a mistake: when FireSheep (the sniff-your-credentials Firefox plugin) was announced, I immediately bumped SSL support from “something I’d eventually like Bingo Card Creator to have” to “must be done today”.  If I had had any sense, I would have let that wait until November.  Enabling SSL took about a day, but I missed some edge cases which came back to cut me: in particular, I had the registration form throwing SSL errors for about 6 hours (painful, particularly since it was during an email delivery window) and, even more painfully, I had the AdWords landing page throwing errors for 48 hours (not fun when you’re spending $150 *a day* driving people to it).


But the worst thing was keeping the freaking AdWords conversion code on HTTP, which caused some browsers to not load it from an SSL page, and cut my conversion rate in half.  Since I use Conversion Optimizer, this caused Google’s algorithms to think “Hmm, Patrick must really not want this flood of traffic we’re sending him since it apparently converts like crap.  Oh well.  I guess we’ll just send it somewhere else instead.”  Between money that I essentially set fire to, an AdWords campaign thrown into disarray (I still haven’t recovered my previous conversion rates, since the bots are in a bit of confusion and haven’t replaced me on my best performing sites yet), and missed opportunities, that mistake probably cost me a few thousand dollars.  Ouch.


Still, I generally try to see things as half-full rather than half-empty, and my jack o’lantern is overflowing at the moment: previous sales records smashed, a new scalable marketing tactic which actually works, infrastructure ready to go for Thanksgiving, Christmas, and Valentine’s Day (and a few hundred more email addresses to send to), and the SSL issues now *mostly* under control.  (I still am not transitioned to 100% SSL, which ironically means that the effective increase in security was minimal.  *sigh*)


## Mini-update on Appointment Reminder


I was very busy with ongoing improvements to Bingo Card Creator, consulting, travel, and non-business life for the first six months of being self-employed.  Since midway through October I’ve refocused to get Appointment Reminder out the door (really — most of the Halloween campaign was taking advantage of things which already existed), and since previous experience has taught me that artificial deadlines really work for me, I have joined up with a bunch of Hacker Newsies to make November the Get Your Startup Accomplished month.  After some fumbling around with jQuery and other infrastructural issues, I feel like I really hit my stride today, and if I keep it up I should launch right around the end of the month.


If you’d be interested in hearing about this on a regular basis, leave me a comment — if folks care, I will post regular updates to the blog.
