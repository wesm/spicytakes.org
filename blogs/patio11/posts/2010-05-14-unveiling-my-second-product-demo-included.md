---
title: "Unveiling My Second Product (Demo Included)"
date: 2010-05-14
url: https://www.kalzumeus.com/2010/05/14/unveiling-my-second-product-demo-included/
slug: unveiling-my-second-product-demo-included
word_count: 2612
---


Earlier this week, I went to a small massage parlor which is located at the mall next to my house.  There are three attendants on duty at any given time.  I was a “walk-in” (no appointment) and ordinarily would not have been able to see someone quickly, but luckily for me two clients had failed to make their appointments.  That was rather unlucky for the firm, though: two clients not at their appointments means two massage therapists not seeing anyone, and that costs them $2 *a minute* in direct economic losses.


What that business needs is some way to reduce the number of no-shows and get earlier warning when no-shows happen, so that they can rearrange the schedul, actively solicit walk-in customers, or invite one of their regular customers to have her weekly massage early.  That would minimize the lost revenue from missed appointments.  For example, they could call every client the day before their appointment.


But calling customers is an expensive proposition, when you think of it: three staff members times an average of 10 clients each per day means they’d need to make 30 phone calls a day.  That is thirty opportunities to hit the answering machine, thirty voicemails to leave, thirty “We’re sorry, our customer is not in the service area” messages to hear.  And, since there is no dedicated receptionist at the store, that is time that has to come from an expensive therapist — and when their hands are on a receiver, they aren’t working the knots out of someone’s shoulders for $1 a minute.


There are many, many businesses like my local massage parlor: massage therapists, hair salons, auto mechanics, private tutors, and large segments of the healthcare industry.  They all have an appointment problem…  and it is about to get a bit better.


## Introducing Appointment Reminder


For the last several weeks, since quitting my day job, I’ve been hard at work on [Appointment Reminder](http://www.appointmentreminder.org).  (You can tell that I haven’t lost the same panache for inspiring, creative names that bought you [Bingo Card Creator](http://www.bingocardcreator.com).)  It is a web application that handles scheduling and automated appointment reminders via phone, SMS, email, and post cards.  The phone and SMS reminders are through the magic of [Twilio](http://www.twilio.com), which lets you make and receive phone calls and SMSes using simple web technology.


My value proposition to my customers is simple:

1. Schedule your appointments in the easy-to-use web interface.  That’s all you have to do.
2. Prior to the appointment, we’ll automatically remind your customer of the date and time of their appointment.
3. The customer will be asked whether they’re coming or not.  If not, we’ll notify you of that immediately, so that you can reschedule them and rescue the emptied slot.
4. This **makes you money**.  Plus, it is another opportunity to touch your customers, hopefully improving your commercial relationship.


## How This Is A Lot Like Bingo Cards


My assumption, which has been borne out a bit in talking to potential customers, is that the market for this sort of thing is overwhelmingly female.  The personal services industry is mostly female, and dedicated receptionists (who I am replacing making more efficient in one facet of their jobs) are almost universally female.  That is one point in common with the market for Bingo Card Creator.


In addition, the competition is similar to the competition for educational bingo cards in 2006:  they’re structurally incapable of addressing huge segments of the market and I am going to go after those segments with a vengeance.  For example, if you look for appointment reminder services online, you’ll find that most of them go after the healthcare market — that is, after all, where the money is.  (My dentist got $770 for 15 minutes of his time and 30 minutes from the dental hygienist — he’s losing a car payment every hour he doesn’t have his hands in a mouth.)


This is mostly sold as enterprise software, with the long sales cycle, non-transparent pricing, and general cruftiness to match.  It almost has to be, because the software has to plug into patient records systems (the typical enterprise morass of dead languages, horrible interfaces, and software which would have fallen to pieces years ago if it hadn’t sold its soul to the devil).  Additionally, healthcare is a very regulated industry, and compliance with [HIPPA](http://www.hhs.gov/ocr/privacy/) and other regulatory requirements inevitably drives costs up.


From my research, the cheapest options available cost about $300 a month as a service (often involving a contract with an actual call center) or ~$1,000 as installable software and hardware.  Those do not strike me as viable options for a hair salon, piano teacher, or small massage parlor.  However, thanks to Twilio incurring the capital expenditures on my behalf, I can afford to offer a superior service for a fraction of that price.


And because my cost structure is absurdly better than my competitors, I don’t need to have a sales force to close the deals.  Instead, I can use the skills I’ve built up over the last several years of selling B2C software, and consummate transactions online on the strength of passive sales techniques like a demo, free trial, and website.  My guess is that the low-friction nature of this is going to help me with the less enterprise-y segment of the market, as they’re least in the mood for “Give us your phone number, address, and financial particulars so we can have a salesman set up a meeting to talk to your office manager about how much this is going to cost you.”


## Demo / Minimum Viable Product


Appointment Reminder is not actually ready yet.  Having been on something of a [Lean Startup](http://www.startuplessonslearned.com) kick recently, I thought that getting the software ready prior to showing it around to customers would put the cart in front of the horse: why spend 2-3 months getting v1.0 of the software ready if it turns out that users are cool on the entire concept.  Instead, I took a bit of inspiration from [Dropbox’s ](http://www.dropbox.com)minimum viable product, which was just a [video](http://dl-web.dropbox.com/u/2/screencast.html) showing how awesome your routine tasks would be if the product actually worked.  (They had a working prototype at the time but not one which would 100% reliably keep people’s data, which is sort of a key consideration if you’re making a backup product.)


The way I figure it, since the demo of my software is what ultimately makes the sale, everything that happens after the demo is essentially irrelevant to getting someone’s credit card number.  So everything that happens after the demo is out of scope for the MVP: **I can demonstrate the sizzle without actually cooking the steak**.  The sizzle for Bingo Card Creator was cards coming off your printer.  The sizzle for Appointment Reminder is demonstrating that I can make a phone ring on command if you type a number into your computer.


I’ve been programming for more than a decade now and very, very rarely get the “kid in a candy store” feel these days from it, but the first time I made my phone ring with an API call, I got all kinds of giddy.  I’m figuring that my customers will likely be the same: this is new and magical territory for them.  And unlike a certain technology company which specializes in new and magical telephone equipment, this will credibly promise to make people money.


You can try the [demo of Appointment Reminder](http://www.appointmentreminder.org/a/calendar) yourself.  Get your cellphone out, you’ll need it.  The flow goes something like:

1. Open the demo page.  (I may eventually capture email addresses here, but folks visiting in the first few weeks are mostly going to be my tech buddies, so I’ll hold off for now rather than collecting a lot of mailinator.com addresses.)
2. Take a look at the simple calendar interface.
3. Type in your phone number and hit Schedule Fake Appointment.
4. Your phone rings and you get a combination sales pitch and product demo in the guise of informing you of your fake appointment.  At the end of the call, you’ll be given an option to confirm or cancel the appointment.
5. As soon as you confirm or cancel the appointment, that is reflected on your computer screen.
6. You’ll be asked for a conversion here.  At the moment, it just asks for your email address.  Once the site is live, I’ll be pushing for the sale right there.


In real life I’d be using a more immediate way to contact the customer than updating their web interface, since they won’t be on Appointment Reminder when *their* customer gets the phone call, but that didn’t make sense for the demo — I’ve already credibly demonstrated my ability to make the phone ring.  Now I just need to credibly demonstrate that I can get information from the phone calls to the computer.


## Pricing


I have some tentative thoughts on [pricing](http://www.appointmentreminder.org/pricing) for the service.  This was mostly a marketing decision — I want to be able to say something similar to “Appointment Reminder will pay for itself the first time it prevents a no-show.”  There is also quite a bit of daylight between the value of an appointment among my various customer groups — for a low-end salon that might only be $10, for a massage therapist $50, and for a lawyer or dentist “quite a bit indeed.”


My plan breakdown is mostly to do price discrimination among those user groups:

- Personal ($9 / month): This is for folks who either want to send reminders to themselves/family or folks who have a part-time business like piano tutoring on the side.  Candidly, I think the value of these customers is going to be minimal, but I wanted to have this plan available for marketing reasons.  (It gives me a shot at appealing to the web worker/productivity/etc blogging folks, for example.)
- Professional ($29 / month): The bread and butter plan.  This is intentionally sized to be decent for a low-intensity full-time business, such as a hair salon or single massage therapist.  Of note, putting the ability to record custom reminders here rather than in the personal plan provides a strong incentive for folks to upgrade.
- Small business ($79 / month): This is where I expect to get the majority of my revenues and profits from (notice how I recommend it?).  It should be sufficient to cover most businesses smaller than a busy dentistry practice.  Speaking of dentistry practices…
- Enterprise ($669 / month): So here’s a trick I’ve learned in Japan: there are a million ways to tell people “no”.  One way to tell people “No, I don’t want your business if you’re in health care” is to make them check a box certifying they are not in healthcare at signup.  That increases friction and demonstrates contempt for potential customers.  Instead, I’ll say yes, I do want their business eventually (after I get the kinks out of my system and have hardened the security and legal representation enough to feel comfortable with soliciting their business), but it won’t be today and it won’t be cheap.


Common among all plans: the first month will be free (capture credit card on day 1, bill on day 30 for month #2, etc etc), and I’ll have my usual 30 day money-back guarantee.  I’d like to offer discounts for multi-month signups, but I think that Paypal may not be too keen about that until I have some history with this business, so I’ll be avoiding it.  (Oh, trivia note: Paypal Website Payments Pro + [Spreedly](http://www.spreedly.com) for subscription billing.)


At these price points, the cost of providing the service (Twilio calls) would cap out at about 30% if customers routinely rode their plans to the limit.  On experience and knowledge of the industry, I think that is highly unlikely, and expect to pay something much closer to 5 ~ 10%.  Obviously, I’m never going to characterize this as a 20x markup on Twilio services to my customers, as my customers don’t care beans about Twilio: they care about making sure their expensive professionals don’t idle for lack of work.


## Early Reception From Potential Customers


Sadly, I’m not in a position to get this localized into Japanese at the moment (Twilio doesn’t quite have first-class Japanese support, and I have severe doubts about my ability to market effectively domestically).  This means that I can’t exactly walk over to the massage parlors around town and ask them to try it out.  However, I’ve been talking to friends from high school who work in service industries to verify that my assumption of what their problems are is indeed accurate, lurking on message boards (the number of posts deleted for excessive vituperation about missed appointments suggests to me that there may indeed be a market need for this service), and have been doing keyword research.  There appear to be healthy volumes in the core keywords, although I wish it had a built-in longtail search strategy like bingo cards did.


This summer I’m going back to America for about a month to visit family, do a bit of consulting, and have something of a vacation.  Over that time, I’m going to be taking the demo (or the product) on my laptop and showing it to as many service providers as I can stomach seeing.  Thankfully, I expect that they’ll indulge my request for an interview — I intend to pay them their normal hourly, so coffee and a discussion of their industry and opinions about the software will work out just as well as offering a haircut/massage/etc would.


## Business Plan


I didn’t write a formal business plan last time and I have no intention to devolve.  That said, I do intend on documenting and revisiting assumptions.  As usual, I’ll be doing most of that on my blog, so you guys are welcome along for the ride.  I’ll also continue my general transparency policy with regards to what works, what doesn’t, and what my statistics are looking like.  That probably won’t rate automatic reporting for a few months yet — no sense building things to track the sales I don’t have.


I’ve essentially got two notes for marketing and intend to be hitting both of them: SEO and AdWords.  AdWords is likely going to be a tough nut to crack in this market due to high spending by companies with very, very high average ticket prices, but most of my competitors do not strike me as extraordinarily web savvy, and I think I can out-think their outsourced SEO/SEM teams.


In terms of reasonably achievable goals, I’d like to have v1.0 of the service open and accepting money by the end of June.  I think that two hundred paying customers is a very achievable target for a year from now, although I’m still not sure yet how being full time affects my skill at marketing, so that might be understating things by a bit.  The last time I made a sales prediction for a new product was when I expressed the wild desire that Bingo Card Creator eventually sell a whole $200 per month.  I hope to be every bit as mistaken.


## A Quick Request


I value your opinions tremendously.  If you have suggestions related to the business or forthcoming feature set, I’d love to hear them.  If you have any particular areas you’d like to hear about in my upcoming blog posts, I’d love to hear that, too.


I’m coming to the market several years behind most of my competitors and will be playing catchup for quite some time.  I would be indebted if you took a few minutes to blog about Appointment Reminder.
