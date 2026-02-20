---
title: "Appointment Reminder at 6 Months"
date: 2011-04-14
url: https://www.kalzumeus.com/2011/04/15/appointment-reminder-update/
slug: appointment-reminder-update
word_count: 2648
---


****


**** The guys at [AppSumo](http://www.appsumo.com) approached me and said “Hey, we’d like to do a video of you talking strategy with Andrew Warner.  You guys script it, we’ll edit it and sell it.”  Ordinarily I don’t really do e-books and whatnot but that pitch had me at “Andrew”, because [Mixergy](http://www.mixergy.com) is one of the best sources of consistently actionable advice I’ve seen, and I want to help him succeed in whatever little way I can.


The topic of the video is Scalable Content Generation.  It’s the same SEO strategy that I’ve talked about on my blog for years (see Greatest Hits section)  Take my word for it: that is the highest single expected ROI of anything I’ve ever talked about on this blog.  However, those posts are stream-of-consciousness notes from a strategy which evolved organically over years.  Many people tell me that the idea is wonderful, *very few* actually end up implementing it.


The video is scripted, professionally edited, and organized so that hopefully people will actually implement it this time.  Andrew and I walk you through exactly what I did to turn $3,000 of freelancer writing into $30,000 of sales last year, and discuss how to apply that to an arbitrary online business.


Here was my pitch to AppSumo for why they should have me talk on Scalable Content Generation:

1. It lets small businesses achieve top rankings for relevant search terms on Google for minimal costs.
2. It lets small businesses develop an asset which continues to grow in value over time, rather than leasing traffic via e.g. AdWords ads, where you have to continue paying or the spigot turns off.
3. It allows you to provide huge amounts of actual value to customers without spending a huge amount of time on it.


The video is for sale [over here](http://www.appsumo.com/hacking-content-creation/).  Apparently there is an option for getting it free for the next 24 hours (on Friday April15th, 2011 US time) — after that it will be somewhere south of $100.  They’re also throwing in an hour of consultation with me for somebody who writes a review.


Ask me about my thoughts on e-books and info marketing some other time, but suffice it to say a) I am doing this for free, b) I would not have done it but for Andrew’s involvement, and c) I believe the video has value to online businesses or I wouldn’t be associated with it.


**</Plug>**


## Appointment Reminder Update


Early in December I launched my second software business, [Appointment Reminder](http://www.appointmentreminder.org).  I can’t be as open with it as I am with [Bingo Card Creator](http://www.bingocardcreator.com) (you can literally see my [sales stats](http://www.bingocardcreator.com/stats) for that one) , but I hope to keep folks informed about how things are going.  Long story short: egads, I had forgotten how long it takes to get these things off the ground.


One would assume that, after leaving the 70 ~ 90 hours day job, I would be able to devote 100% of my concentration to the new business.   That turned out to be grossly over-optimistic: a combination of burnout, reacquainting myself with human life, and distractions from consulting meant that I accomplished almost nothing on AR between May and late October of last year.  Similarly, after launching I took the month off for Christmas, and when I got back in January I immediately started applying myself to marketing AR floundered around for quite a bit.  There was a consulting engagement, a few side projects (Achievement Unlocked: Published in Academic Journal), an earthquake, and now we’re almost to Easter and I’m wondering where 2011 has gone.


So that’s the bad news.  The good news:


## Got Customers.


AR has had about fifty people sign up for the trial, either by doing it themselves on the website or by me giving them an account manually.  That’s much, much, much slower than BCC — these days, BCC routinely gets [250 signups a day](http://www.bingocardcreator.com/stats/signups-per-day).  The saving grace is that their conversion rates are high: keeping in mind that customers have a 30 day free trial and that many are still within it, about 10 of them have already paid me money and about 10 more look likely to.  The revenue run rate is still inconsequential (south of $500 a month), but AR is cash flow positive (pays for server, calls, credit card processing, etc), and the unit economics for those customers turned out better than expected.


For example, my most popular plan currently is the Professional one, at $29 a month.  This entitles the customer to up to 100 appointments a month.  The worse case scenario for cost to service that customer is about $20 a month paid to [Twilio](http://www.twilio.com).  My hypothesis was that the actual cost to service the customer would be lower than $5 or so, which makes the economics attractive.  It turns out that most customers on that plan are below $3 apiece.  This means that, if I could just scale customer acquisition, I would be in a very happy place.


## They Love It.


My customers have sent over a thousand reminders regarding 800 or so appointments.  It is anecdotally making a big impact for their businesses: my biggest fan has seen his no-show rate decline to virtually nothing, which singlehandedly “pays for the mortgage.”  Many other customers report that they didn’t previously have a problem with no-shows, but that making reminder calls was a source of frustration for them, and that AR removes the frustration and makes it much more likely that any given client actually gets contacted.


Somewhat surprisingly to me, my customers’ customers love Appointment Reminder, too.  My favorite: “I wish all my [service providers] used this.”  The context for me hearing that was that customer relaying his customers’ opinions to tell me why he wouldn’t stop using Appointment Reminder after getting bitten by a real doozy of a bug.


## Bugs Suck


I very carefully avoided doing anything “Mission Critical” when I was an employee, because I didn’t feel like I could offer the requisite level of service.  BCC going down can inconvenience a teacher, but nobody is going to have their day totally ruined by it.


Appointment Reminder is more than capable of totally ruining somebody’s day.  If it *just* broke, that would be annoying but survivable: clients do not *expect* to get automated reminders yet from my customers, and most will come in for their appointments regardless of whether they get a reminder or not.  However, “failure to deliver reminders in a timely fashion” is not nearly the worst possible failure case.


An example: during my apartment move in February, due to an ill-considered code push the night before the move, the DelayedJob queue which handles (among other things) outgoing reminders fell over.  Thanks to the magic of [Scout](http://www.scoutapp.com), I heard about this essentially instantly.  Well, my cell phone did, at any rate.  My cell phone was packed up with my laptop and other essential computer stuff for transport by hand.  I didn’t hear about the queue falling over until after the move was mostly complete, by which time it was already 8 PM for many of my customers (in the US).


I panicked.  Mistake #3.  I was worried about many customers not getting their reminders for appointments tomorrow, so instead of doing the smart thing and purging the outgoing queue, turning on my In Case Shit Happens button (which prevents any outgoing reminders without my explicit approval), and manually restarting then verifying that the system was stable, I decided to improvise.  Mistake #4.


I visually inspected the queue, which was 1,000+ jobs ranging from outgoing reminders to low-priority requests to external analytics APIs.  I saw one type of queued item that would be annoying to try again — demo calls, which have to occur when a user is still on the website rather than hours later — and purged them.  Then I just restarted the queue workers and watched the queue go from 1,000 jobs down to 0.  Mission accomplished, right?


That night, for some reason I couldn’t sleep, so I turn on my iPad and check email.  I had several very irate emails from customers, who had just had their morning appointments come in and complain about getting contacted by Appointment Reminder.  Repeatedly.  See, for the several hours that the queued workers were down, a cron job kept saying “Who has an appointment tomorrow?  Millie Smith?  Have we called Millie Smith yet?  OK then, queuing a call for Millie Smith and ignoring her for 5 minutes while that call takes place.”  There are an awful lot of 5 minute intervals in several hours, and the queue was not idempotent, so Millie Smith got many, many calls queued for her.


As soon as I hit “go”, the backed up queue workers blasted through 600 calls, 400 SMSes, and 200 emails, and my website and Twilio received an impromptu stress test.  We passed with flying colors.  Millie Smith’s phone, on the other hand, did not.  The worst affected user got 40 calls, back to back, essentially DDOSing their phone line for 15 minutes straight.


I didn’t have Internet at my new apartment yet, so I picked up my laptop and walked 45 minutes across town at 3 AM to my old apartment to perform damage control.  First I hit the In Case Shit Happens button like I should have hours ago — it stayed on for the next several days.  Then I started making phone calls.  This was, unquestionably, the low point of my entrepreneurial career: picture me in a freezing, pitch black apartment at 4 AM in the morning crying in between calls to apoplectic customers of customers.


Things looked much better in the morning.  Surprisingly to me, I only lost two customers in the debacle, and one of them resubscribed after seeing how I handled it.


## High Touch Sales Processes Are Not My Cup of Tea


I’m fairly decent at marketing software on the Internet with low-touch sales: you click on my AdWords ad or SEO’d piece of content, the website convinces you to take a spin, you like the software, and a sale happens without ever speaking to me.  This is born of necessity: I simply couldn’t routinely talk to people when I had a day job.  Happily, there exist at least a few people who will buy AR on this model.


Also happily, for a different kind of happy, there is a channel for AR that I wasn’t aware existed: white label sellers.  Picture a technology consultant or web development shop which has a relationship with a few dozen small businesses in their area.  Many of them sell hours-for-dollars but they would really love to have recurring revenue sources.  Their clients have business models which involve appointments.  They would like to sell AR to their clients as if it were their own software — it lets them have all of the upside of SaaS businesses (recurring revenue, low support, etc) without actually having to write SaaS.  This also has obvious benefits for me: they have boots on the ground to sell AR to their clients, and I don’t.


I had had this in the back of my mind as an option, but it was on the backburner until somebody came to me with a dream client.  Suffice it to say they were just about ready to sign on the dotted line, and it would have involved enough Small Business ($80 / month) accounts to singlehandedly make AR a smashing success.  I immediately dropped what I was doing and built up the infrastructure to actually offer white label accounts and let the white label customers customize their off-brand AR sites.  (You can see one for a fictitious Ocean Waves Spa [here](https://example.appointmentremindersystem.com).)  All hosting and software gets taken care of by me.


Then that sale fell through.  It was nobody’s fault, really, the contact’s client just happened to decide to exit the line of business which used appointments.  Oof.  This sort of thing happens quite a bit in sales.  One would think I would be used to it, since it isn’t unknown in consulting either, but it still snuck up on me.


Similarly, actually riding herd on white label accounts has been more difficult than I would have expected.  I have had a dozen leads to folks very interested in offering it and then they just dry out, largely because I am not aggressive enough on pushing the deals forward.  My typical customer support workflow is responding to all email and then thinking that I am done.  It is a new experience when a) people are not trying to tell me about problems and b) this means I have work to do.  For example, many folks need marketing support (brochures, questions answered, and whatnot) to make the sale to their clients, and since they have the relationship but know nothing about AR, I need to figure out a way to get them that support in a timely and proactive manner without interrupting everything else I need to do.


Another niggle I had not expected: some B2B customers are unqualified and it is to your advantage to figure that out early and stop pursuing them.  I had a long exchange of emails with a prospect who does professional development for a particular type of business.  Think salon, but crucially, at a much lower price point than salons operate at.  We were 15 emails and thousands of words into discussing possibilities when she indicated that the $9 a month plan would simultaneously a) too costly and b) too limited for most of her customers.


“Ah, I don’t believe that my business is the right fit for your needs.  Best of luck in your search for an alternative.”


A business is defined both by what it does and what it does not do.  I don’t want to spend time marketing the service to customers who think $9 is an appreciable amount of money.  (For that and related reasons, I’ll be killing the $9 account tier for new customers as soon as I get the pricing page redesigned.)


## What’s Next?


Same old same old!  I’m continuing to develop AR in response to observed customer needs and requests.  The product is very stable these days — I was able to virtually ignore it during a client engagement with no harm done.  Although I don’t know if I would have agreed with it at the time, I’m glad to have taken my licks when I had five customers as opposed to when I have five thousand — that would have made for a *very* long night of apologies.


I started implementing Scalable Content Generation (see above plug section) for AR.  Currently, I’m at the “experiment by hand” stage.  The site does not have sufficient link equity to rank for much yet, and I’m not totally wowed with my first concept for the content, so I’m going to try something else towards the end of April.  I also have a project or two in the queue along the lines of A/Bingo: produce something of value to people who are not my customers, put in on the website, collect links, use to bootstrap rankings for commercially valuable keywords.


I’m still tentatively targeting 200 paying accounts by the end of this year.  It will take a bit of acceleration to happen, but after May (going back to the US for family and a bit of the consulting/conference circuit), I’ll have most of summer to concentrate on scaling the [marketing plan](http://www.marketingplan.net/). I am strongly considering various options for taking things to the next level if I can get things that far.  It will depend on a few factors, some business and some personal, but it looks highly likely that there is a viable micro-ISV in AR and quite likely that there is a bigger business there if I want to go after it.


Any questions?
