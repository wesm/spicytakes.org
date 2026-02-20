---
title: "Kalzumeus — The What, The Why, and a bit of The When"
date: 2007-06-17
url: https://www.kalzumeus.com/2007/06/17/kalzumeus-the-what-the-why-and-a-bit-of-the-when/
slug: kalzumeus-the-what-the-why-and-a-bit-of-the-when
word_count: 2415
---


Picture this: you’re a young doctor, 32, recently married to your med school sweetheart.  Life is pretty hectic, what with being constantly tied to a beeper, carrying a cellphone so you and your wife can murmur sweet nothings in each others ears when not on call, and you having all the distractions of normal every day life.  Also, earlier this year you purchased a nice little house in the city to rent out to folks for some passive income, with eventual designs of using it to build up a little equity and maybe give something to the child you expect to be having one of these years, and then it hits you:


Being a landlord *sucks*.


Every first of the month you get to have even more thrown at your plate, and it is by and large busywork.  You have to check your mail to see if your renter sent you the check.  If they didn’t send you the check, you have to contact them fairly quickly to request that they send you the check, assess a late fee, field the phone call whining about the late fee, explain to the renter that just because their back door is a wee bit off its hinges that doesn’t mean they get to live rent-free, try to remember to call the handyman to fix that blasted door this week, get the check a few days late, drive to the bank, and wonder why on earth you took out a $200,000 mortgage to buy yourself a minimum wage job.


There has to be a better way, you think.  Why can’t this be as easy as your wife’s hobby selling those Beanie Babies on eBay?  Deal with any questions or disputes by email, get an email from Paypal when the money arrives, no checks in the mail, no runs to the bank, no forgetting to mail the Beanie because there is a big announcement on your eBay dashboard on your computer saying “Hey, you haven’t mailed the Beanie yet”.


Kalzumeus makes being a landlord as easy as selling Beanies on eBay.


(Note: Kalzumeus is a codename and will eventually be the name of my LLC.  The actual product name is quite boring, was chosen mostly for SEO, and will be announced later when that website has some content on it and, ideally, a functioning demo.)


One of the nice things about Kalzumeus being a web app is that features can be added to it fairly easily.  At release Kalzumeus will support:

- Landlords and renters logging into their accounts.
- Landlords adding properties, residences, and renters to the system.
- Landlords billing renters, with automatic repetition, in a very flexible fashion.
- Billings for rent, parking fees, what have you.
- Renters paying their bills online through Paypal.  All the landlord needs is a Paypal account, the computer handles the rest.  No messing with buttons.
- Email notifications of rent due.
- Automatic bill payment for *most* renters.  (My systems are more flexible for automatic rebillings than Paypal’s are.  I can, for example, bill someone on the 1st Monday and 3rd Thursday of every month.  I don’t know why you’d want to do that, but “1st and 3rd Friday”, for example, is a typical paycheck schedule and landlords like being able to bill people immediately after they get their paychecks.)
- Roommates.  (This was a low priority feature, but it was free with an architectural decision, so it made it into the first release.)


What I eventually want to add:

- More payment options for landlords to choose from.
- Automatic paper dunning letters.
- Expense/work order tracking.
- Reports.
- “Click this button to print out the stuff your accountant wants from you.”  (Depreciation calculation and all that jazz.)
- Export to Quickbooks, CSV, etc.


**Is this a big market?**


There are fifteen million landlords in the United States, according to Intuit.  The most common number of properties owned is one.  (Cue the “If I could get 1% of that market…” song.  Now all I need is a venture capitalist and I’ll have all the ingridients for a funding round.)


**Who are the competitors?**


On the one hand, we have property management companies, which charge a figure anywhere between 6 and 10% to stand in for you in all or most interactions with tenants.  There are also services which will do ACH (Automated Clearing House) deductions for landlords, which are a way to automatically withdraw set amounts of money from someone’s bank account, for approximately $10-15 a month plus $2 per renter.  Some of these services also provide online reports, although the functionality is fairly limited.  Finally, there are many, many companies which offer “property management software”, which is basically integrated accounting packages set up for landlords.  One I have a lot of respect for is [LandlordMax](http://www.landlordmax.com/), run by a fellow uISV.  (Before anyone asks, I don’t see him and I as really being in the same niche.)


**Why go into a market that crowded?**


Because the vast majority of my competitors sell chainsaws and there are a lot of landlords who really need butter knives.  Much of the property management software is geared at professional property managers, including folks who have strong accounting backgrounds and are managing hundreds or thousands of units simultaneously.  I think there is a whole lot of overkill going on for folks who are at the “I’m not so much a landlord as I am a teacher who happens to own a house which I rent to people”  side of the market.  Additionally, the pricing models for many of the existing solutions totally ignore the needs of small landlords, probably because they are not nearly as lucrative as large landlords.


**Pricing Model**


I am thinking of doing one month of free trial and then billing folks $X per month.  I have not decided on a final X yet, but am thinking $10 or $15 puts it in line with many of the successful small business web applications.  If folks want to prepay for a year I’ll give them two months free.  The wild card is Paypal costs, which for many of my customers are going to run at essentially 2.9% of their monthly rents.  That is a lot of money for just processing payments (comparable with running credit cards yourself, a heck of a lot more than using an ACH service).  At a $650 average rent in the US, that works out to about $19 in Paypal charges on top of whatever I charge.  I am cautiously optimistic that if I make it easy to use I can justify a price premium from some landlords over ACH payments, which are not exactly easy to set up (contracts need to be signed, faxed, etc), and am extraordinarily confident that for folks who are looking to accept credit cards I can do a bang-up job.


I am also thinking, eventually, of offering a separate $99 a month account type targetted at professionals (management companies and the like).  They’ll be able to create logins for the property owners, who can check the website at any time and see “Ooh, yay, I’m making money”.  That will require a bit of rearchitecturing so it is slightly down the road.


**The Shoestring Factor**


I have already booked most or all of the prelaunch costs.  While I don’t have my tab in front of me at the moment, they came to a little less than $250 last time I checked.  That includes a year worth of hosting with Textdrive prepayed.  (Just over $10 a month, even counting the setup fee.)  If my hosting plan is inadequate for keeping a Rails application running, which I have been hearing conflicting reports about, I’ll get one of their [medium accelerators](http://www.joyent.com/accelerator/pricing) (basically, a slice of a server) for about $65 a month.  Currently, my break even number of customers is one.  If I end up buying the accelerator, that will put the break even number at between 5 and 7.  (Bingo Card Creator, by comparison, is profitable from the first customer every month to the last.)


Where is the end-game for this?  I don’t know.  My goal for the intermediate term is 300 (paying) customers, and I’m hoping to have say 80 to 100 by the end of the year.   (I generally like to set small and achievable goals and scale up from there.  My first goal for Bingo Card Creator was $200 a month in sales.  Hit that and kept going…  working on $1,000 a month now.)  As scary as this is to say, 300 paying customers would be enough for me to quit my dayjob.  (I love being a uISV.  If you’re doing some sort of advertising funded social networking site, you can have hundreds of thousands of users and still be losing money every month to your massive hosting and infrastructure costs.)


**Marketing**


Blog, SEO, and AdWords to start out, more as time permits.  I’ve been looking at the market for a couple of months and while “property management software” is an absolute bloodbath I am fairly confident that I can SEO very well for other queries, like “pay rent with credit cards”, “online rent collection”, and the like.  I don’t need or want to compete with the largest players on their own turf — for the moment I’ll be quite happily picking and choosing crumbs dropped from the table.


**Demo / Ease of Use**


I’m working at having a mostly full featured online demo for the software, part of my usual quest to get folks to the shiny bits as quickly as possible.  I also have no-hassle, no download, no credit card, “Give your email address and get started” account creation.  There are plenty of examples you can find of Web 2.0 companies who do [Actual](http://www.blinksale.com/home) [Business](http://www.crazyegg.com) [Processes](http://www.sproutit.com/mailroom) without requiring 30 minutes of forms to get started.  I am practicing the most sincere form of flattery with regards to the design of my own signup process.


In my timer tests (something I often did with Bingo Card Creator — time how long it takes from hitting the download free trial button to when the cards come off the printer), I can sign up and have automatic billing working for a renter in 90 seconds.  We’ll see if I can’t shave some more off of that when the interface is more complete and AJAXified.  For example, I want you to be able to do the most common types of rent (monthly on the 1st, monthly on the 1st and 15th, etc) with about two to three clicks while adding a renter.


**Legal**


I am not decided on whether I will have a lawyer draft the terms of use or not.  I’m leaning towards “not” — the application can’t kill anybody, and a quick glance around the world at my various competitors shows that companies with Serious Money On The Line are quite happy to just have generic “If you bill your renter for a gazillion dollars and get taken to court, that is Your Problem” disclaimers.  The privacy policy is already drawn up, and looks very similar to the Bingo Card Creator one: we use cookies to track X Y and Z, we don’t sell your information, we won’t spam you, any questions feel happy to ask.


**So when will this be publicly released?**


I will happily show this as soon as I can without embarassing myself.  Since it is currently black text on a white background with the default Rails stylesheets for errors and much navigation is still accomplished by manually keying in the proper URLs, the app is not quite ready yet.


At the moment, the business logic for the first shipping version is about 80% complete.  The billing system still has yet to be implemented, and I have yet to write the systems for sending reminder emails, etc.  The interface, on the other hand, is only about 15% complete — things link to the right pages most of the time, but I will have to redo most of the views so that they look nice and pretty in [Multiflex-3](http://www.oswd.org/design/preview/id/3626).  I also want to hand-edit the [Multiflex-3 WordPress theme](webgazette.co.uk/web-design/wordpress-themes/wp-multiflex-3/) so that clicking from the product blog to the product site is a totally seemless experience, which by necessity involves a bit of headache since WordPress is PHP, the product site is flat HTML, and the application is Ruby on Rails.  Yay for getting to tweak the same template three times.  (I might eventually make the static pages served by Rails, but for the time being I know that new Rails apps can be a bit tempermental and if I should cause the app to die I would like people to be able to access the front page and send me a letter about it.)


Of course, since I’m currently winding down my employment contract with the day job and actively searching for a new one, the schedule could get changed at any time.  That is another reason why I don’t want to have a site in front of potential customers until I can have reasonable assurances that I have time to act on things that potential customers tell me.


**My Capsule Impressions of Ruby on Rails**


How am I finding Rails?  Elegant, but not easy.  I will need to do a refactor or three over the codebase to standardize the way I do some things before I release.  The amount of existing code which can be leveraged for my project is pretty low but when it does exist its amazing.  (You should see the graph libraries.  Wow.)  On the other hand, the community is growing rapidly and as a result the average level of skill in the community (and hence on forums, etc) is not quite so high yet.


Test driven development has proven to be a lot like going to the gym — I didn’t enjoy starting it but the results are easily visible at the annual physical.


Since my interface is not in anywhere close to its final form yet I haven’t been AJAXing everything in sight, but I have identified a few places where there are major, major wins for user experience using it.  I was also able to replace graphs generated on the server with graphs generated on the client (using a clever bit of Javascript whose name eludes me at the moment), which moves the performance of the application from “fast relative to my projected needs” to “stupidly fast relative to my projected needs”.
