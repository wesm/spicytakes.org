---
title: "Productizing Twilio Applications"
date: 2011-12-19
url: https://www.kalzumeus.com/2011/12/19/productizing-twilio-applications/
slug: productizing-twilio-applications
word_count: 3529
---


**This post includes video, slides, and a full-text writeup.** I recommend bookmarking it if you’re on an iPhone right now.


I make extensive use of [Twilio](http://www.twilio.com) (a platform company that lets you do telephony with an API) in running [Appointment Reminder](http://www.appointmentreminder.org), my core product focus at the moment.  (Wait around a day or two and I’ll tell you a bit about how it is doing in my annual end-of-the-year wrapup.)


Twilio has a very passionate developer community and fairly good documentation on their website, but I’ve sometimes been frustrated at it, because it teaches you the bare minimum to get phones ringing.  That is truly a wonderful thing and a necessary step to building a telephony application.  However, if you *continue* developing your application in the way that the Quick Start guides suggest, you will routinely run into problems regarding testing your code, maintaining it, securing it, and generally providing the best possible experience to your customers and the people they are calling.


I have a wee bit more than a year of practical experience with a Twilio application in production, so I went to [TwilioConf](http://www.twilio.com/conference/) and did a presentation about how to “productize” Twilio applications: to take them past the [“cool weekend hack”](https://www.kalzumeus.com/2010/01/15/deploying-sinatra-on-ubuntu-in-which-i-employ-a-secretary/) stage and make them production-ready.  Twilio has graciously released [videos](http://www.twilio.com/conference/speakers) of many of the presentations at TwilioConf, so I thought I’d write up my presentation for the benefit of folks who were not at the conference.


## The Video (~30 Minutes)


[Twilio Conference 2011: Patrick McKenzie – Productizing Twilio Apps](http://vimeo.com/32877616) from [Twilio](http://vimeo.com/twilio) on [Vimeo](http://vimeo.com).


## The Presentation (40 Slides)

**[Productizing Twilio Applications](http://www.slideshare.net/patio11/productizing-twilio-applications)**
</p>

## The Writeup


### Why I Think Twilio Will Take Over The World


(This was not actually in the presentation, because I didn’t have enough time for it, but I sincerely believe it and want to publish it somewhere.)


I think Twilio is, far and away, the most exciting technology I’ve ever worked with.  The world needs cat photos, local coupons, and mobifotosocial games, too, but it needs good telephony systems a lot more, as evidenced by companies paying billions of dollars for them.


Additionally, Twilio is the nascent, embryonic form of the first Internet that a billion people are going to have access to, because **Twilio turns every phone into a smartphone**.  The end-game for Zynga’s take-over-the-world vision is the human race slaved to artificial dopamine treadmills.  The endgame for Twilio’s vision is that every $2 handset in Africa is the moral equivalent of an iPhone.  I know which future I want to support.


Smartphones aren’t smart because of anything on the phones themselves, they’re smart because they speak HTTP and thus get always-on access to a universe of applications which are improving constantly.  Twilio radically reduces the amount of hardware support a phone needs to speak HTTP — it *retroactively* upgrades every phone in the world to do so.  After that, all you need is the application logic.  And what application logic there is — because the applications live on web servers, they have access to all the wonderful infrastructure built to run the Internet, from APIs that let you get Highly Consequential Data like e.g. weather reports or stock prices or whatever, to easy integration with systems which were never built to have a phone operating as part of them.


You can’t swing a stick in a business without hitting a problem which a phone application makes great sense for.  I filled up three pages of a notebook with them in just a week after being exposed to Twilio for the first time.  Order status checking for phone/fax/mail orders.  Integrated CRMs for phone customer service representatives.  Flight information.  Bank balances.  Server monitoring.  Appointment reminders.  Restaurant reservations.  Local search.  Loyalty programs.  Time card systems.  Retail/service employee support systems.  Shift management.  The list goes on and on and on.


Seriously, **start writing Twilio apps**.


### What This Presentation Will Actually Cover


I’m tremendously optimistic about the futures of Twilio and the eventual futures of companies which make Twilio applications, but I’m pessimistic about your immediate future as an engineer writing a Twilio app, because it is going to be filled with pain.  You’re probably going to make some choices which will cause you and your customers intense amounts of suffering.  I’ve already done several of them, so use me as the inoculatory cowpox and avoid dying.


### Crying In A Cold, Dark Room


Back in February 2011, I moved from my previous apartment to my current house.  I unwisely decided to push a trivial code change prior to boxing things up.  This trivial code change did not immediately take down the server, but did cause one component (queue worker processes) to fail some hours later.  The most immediate consequence of this was that outgoing appointment reminder phone calls / SMSes / emails failed to go out.  Since I was busy moving, I did not notice the automated messages about this failure.


When I discovered the failure (8 hours into customer-visible downtime), I panicked.  Rather than reasoning through what had happened, I reverted the code change and pushed reset on the queue worker processes.  This worked, and the queue quickly went from 2,000 pending jobs to 0 pending jobs.  I then went to bed.


At roughly 3 AM, I woke up with a vague feeling of unease about how I had handled the situation, and checked my email.  My customers (small businesses using AR to talk to their clients) had left several incensed messages about how their client had reported receiving dozens of unceasing calls on the behalf of their business, in a row, at 7:30 PM the night before (right after I had restarted the queue workers).


Here was the error: my application assumed that the queue would always be almost clear, because queue workers operate continuously.  A cron job was checking the DB every 5 minutes to see whether a particular client had been contacted about her appointment yet.  If she hadn’t, the cron job pushed another job to the queue to make the phone call / SMS / email.  When the queue came back up, each client received approximately ~100 queued events simultaneously.  These did not themselves check, at the start of the job, whether the job was still valid, because the application assumed that the cron job would only schedule valid reminder requests and not execute 100 times in between queue clearings.


This resulted in approximately 15 people receiving a total of 600 phone calls, 400 SMSes, and 200 emails, in approximately a 5 minute period of time.


There are a variety of ways I could have avoided causing this problem for my customers:

1. Don’t make code changes prior to planned unavailability, even if they look trivial.
2. Don’t ever leave your phone that gets emergency messages out of your pocket.
3. Switch to idempotent queues, so that adding the same job multiple times does not result in multiple copies of the job.
4. Add per-client rate limits, so that application logic errors don’t cause runaway contact attempts.
5. Add failsafes for historically unprecedented levels of activity, shutting down the system until I could manually check it for correctness.


### Testing Twilio Applications


Unit testing and integration testing are virtually required to produce production-quality Twilio applications, and will make it much less likely for you to create catastrophically bad bugs in production.  Unfortunately, testing Twilio applications is much harder than testing traditional CRUD web applications, because of how TWIML is different than HTML (in terms of how minor syntax errors actually cause business problems), how it is not easy to replicate telephone operation in integration testing, and because Twilio sometimes has poor separation of concerns between the MVC of a web application, the Twilio helper library, and the Twilio service itself.


Twilio testing is **inherently dangerous,** because non-production environments (testing, staging, development, etc) could conceivably generate actual, real-world phone calls to phone numbers which were in your database but not actually under your control.  The first and most important tip I have for Twilio testing is to make it explicitly impossible to contact anyone not on a whitelist from code when you’re not in production.  I have a quick snippet that I put in a Rails initializer which monkeypatches my Twilio library to force it to only make phone calls or SMSes to whitelisted numbers.  (I don’t suggest actually re-using this code, particularly as you may not be using Rails or the same Twilio library that I am using, but you can reuse the idea of enforcing safety in non-production environments.)


A lot of Twilio testing will, unfortunately, require manual button-pressing (or scripts which simulate button-pressing on a telephone).  This is easier to accomplish if you can expose your local development machine to the actual Internet.  There are strong security reasons why you don’t want to do this but, if you’re comfortable with doing it, [LocalTunnel](http://progrium.com/localtunnel/) is a great way to actually accomplish it.


Also see the section below on Modeling Phone Calls, because it will make Twilio phone trees and call logic much more tractable to unit testing.


### You Should Have A Staging Server


A staging server is just a copy of the entire production system minus the actual customers.  (You probably shouldn’t put production data on it, because staging systems are designed to break and as a result they may leak data through e.g. SQL injections.  This is an easy way to lose your DB.)  You should use firewalls and/or server rules to make the staging server inaccessible to the world (aside from Twilio and any other APIs which need to access your site for it to work), but assume you will botch this.


Staging servers are virtually mandatory for Twilio applications, because Twilio apps can fail in ways which will not be detected until they are actually accessed over the Internet.  For example, even with unit and integration testing, failing to properly deploy all audio assets (MP3 files, etc) will cause Twilio to throw hard, customer-visible errors in production.  I have automated systems which check for this now, but since that isn’t an exhaustive list of things that can go wrong in production, part of my workflow for deploying all changes on Twilio is to push them to the staging server first, and then having automated scripts exercise the core functionality of the application and ensure that it continues to work.


### How To Model Phone Calls


Twilio Quick Start guides generally don’t suggest modeling phone calls explicitly, instead relying on just taking user input and doing if/then or switch statements on it.  This is ineffective for non-trivial use cases, because as the application logic gets more complicated, it will tend to accumulate lots of technical debt, be hard to visually verify for correctness, and be extremely difficult to automatically test.  Instead, you should model Twilio calls as state machines.  I am a big fan of [state_machine](https://github.com/pluginaweek/state_machine) in the Ruby world.


I’ll skip the CS201 description of what a state machine actually is.  If you didn’t take that course, Google is your friend.


You should model calls such that they start in a predictable state and user input moves the call between states, causing side effects of a) running any business logic required and b) outputting Twiml to Twilio, to continue driving the call.  This lets you replace case statements with a lot of parallel structure with well-defined transition tables within the call models.  Those models are then trivial to unit test.  Additionally, adopting coding conventions such as “the Twiml to be executed at a given state is always state_name.xml and any audio assets go in /foo/bar/state_name/*.mp3 “allows you to write trivial code which will test for their presence, which will save you from having to manually go through the entire phone tree every time on the staging server to verify that refactoring didn’t break anything.


Additionally, state machines are much easier to reason over than masses of spaghetti code which case statements tend to produce.  For example, consider the following code, which attempts to implement the phone prompt “Press 1 to confirm your appointment, press 2 to cancel your appointment, press 3 to ask for us to contact you about your appointment.”  Spot the bug.


There are actually **over six bugs** in that code, above the trivial ones you probably saw with numbers not lining up to action names:

- The Twilio API will pass this code params[:Digits] not params[:digits], which will cause an error that won’t be caught until you physically pick up the phone.
- The comparisons of params[:digits] with integers will fail, because it includes string representations of numbers.
- There are several mistakes in mapping numbers to actions.
- One of the action names is spelled improperly.


These are very easy to miss because **our brains get lulled into a false sense of security by parallel structure**.  Instead, the model should be taking care  of that mapping between user input and state transitions.  This would radically simplify the code and make the controller virtually failure-free, while letting the model exhaustively unit-test possible user input, expected transitions, and business logic side effects.


State machines might seem like an unnecessary complication when you only have three branches in your code, but **production Twilio applications can get very, very complicated**.  Here is a state diagram from Appointment Reminder.  You do ***not*** want to have to test these transitions manually!


Dealing With Answering Machines
  

    Dealing with the case where the phone calls is answered by an answering machine or voicemail system has been the hardest application design problem for me in doing outgoing phone calls in Twilio.  The [documentation](http://www.twilio.com/docs/api/rest/making_calls) suggests using an IfMachine feature, which will cause Twilio to listen to a few seconds of the phone call prior to executing your code.  They do some opaque AI magic to determine whether the entity speaking (or not speaking) in that interval is a machine or not, and tell your application whether it is talking to a machine or a human.  In my experience, this has error rates in the 20% region, and many customers intensely dislike the gap of dead air at the start of their phone calls.  Also, if the heuristic improperly detects the beep, your message will start playing early, causing the recording to be cut off in the middle.
  

    There are several ways you could attempt to deal with this:
  


      Ignore the issue and treat both machines and humans the same.  This will produce the optimal result for humans, but your system will be virtually unusable when it gets a machine.  (This happens *very frequently* in my use case.)
    

      Force a keypress (“1″) prior to playing your message, then give all users the same message.  This will force most machines to start recording immediately, stopping the cut-off-in-the-middle problem but annoying some clients.
    

      Play instructions such as “This is an automated message from $COMPANY.  To hear it, press 1.”  Assume that anyone who doesn’t press 1 in 5 seconds is a machine and play the machine message.  If they interact with the call, play the human message.  This is my preferred solution (although not actually implemented in AR publicly yet, because customers don’t really grok this issue until it bites them personally).
    


    There is one particular problem with recording messages on answering machines: if you give a user instructions such as “Press 1 to confirm your message” and they follow that instruction when listening to their voicemail, that keypress will not be caught by your application, it will be caught by their voicemail system, with unpredictable results (such as deleting the message) and an absolute certainty of not doing what your keypress would normally do.  ***Users do not understand why this happens***.  They expect your instructions to them to work.
  

    Securing Twilio Applications
  

    Twilio applications have a superset of the security issues of web applications.  In addition to the usual SQL injections / XSS issues / etc, use of the telephone has unique security issues associated with it.
  

    One issue is that confidential information is only confidential **until** you repeat it into a telephone.  Even assuming that the phone call isn’t intercepted (which is, ahem, problematic), there are very common user errors and use cases which will cause that information to be disclosed to third parties.  For example:
  


      User error in inputting telephone numbers causes the message to go to the wrong party.
    

      The message goes to corporate voicemail, where it will routinely be accessible to third parties.
    

      The message is played over a speakerphone / cell phone / etc within earshot of third parties.
    

      The message is saved on a physical device which can predictably leave the physical control of authorized parties.
    

      etc, etc
    


    Don’t ever put confidential information into an outgoing message, unless you have an automated way to authenticate who you are speaking with.
  

    For incoming phone calls, **Caller ID is not sufficient authentication**.  It can be trivially spoofed, indeed, your phone company will probably sell you a product whose sole aim is to spoof Caller ID.  Instead, you should use a circumstance where the user is already authenticated and authorized, such as a face-to-face meeting or using a username / password pair in a web application, and then give them one-time PINs to do whatever they need to do on your system.  Alternatively, you can implement an entire password system for your incoming phone calls, but users tend to hate them, so I try to keep to the one-time PIN metaphor.  (When a user does something on the AR site which requires calling the system, such as setting up a recording for a reminder, I tell them “Call 555-555-5555 and put in your Task Code 1234″, which (since it is time-sensitive) both helps me look up what they were doing on a multi-user system and also conclusively demonstrates that they were able to read a web page which already verified their identity.
  

    Not in the presentation because the slide got deleted for some reason: the 4chan rule.  **Even if your free trial is discovered by 4chan, the world should not become a darker, more evil place**.  There exists tremendous possibilities for abuse of free-form input/output to people’s telephones.  I gate access to my trial by requiring a valid credit card, and demonstration calls and the like have strict rate limits which prevent them from being used to spam someone’s phone to death.  (I should also make it impossible to send demo calls outside of standard work hours.  This is easy to say but a little tricky to implement across multiple time zones while still encouraging legitimate use of demo calls, which is why I haven’t done it yet.)
  

    Twilio Scales Impressively
  

    Twilio and modern web technologies scale impressively well by the standards of traditional businesses.  However, you should probably continue to rate-limit your systems, even though you could theoretically do substantially more volume.  For example, many customers who ask about scaling issues *do not sufficiently understand* that your application scales several orders of magnitude better than their business processes.  For example, a prospective client asked if my system could handle 10,000 phone calls a month.  I told them that I could handle that in under an hour.  They were quite excited about that, but as we continued to speak about their needs, it developed that actually doing that would have crushed their business.  They would have made 10,000 phone calls in an hour, received over 1,000 callbacks, and their two full-time telephone operators would have been overwhelmed by incoming demand for their time.
  

    Grab Bag of Random Advice
  


      Never contact Twilio, or any external API, inside the HTTP request/response cycle.  Doing so imposes an unacceptable delay in performance and slaves your reliability to that of the worst performing API you use.  (Twilio has never had user-visible downtime, but some APIs I rely on have.) Queue the request and tell the browser that you’ve done so.  You can drizzle AJAX magic on your website to make this feel responsive for your users.
    

      The Twilio Say verb will have a robot read your message.  This is adequate for development, but for production, people prefer listening to people.  [Fiverr.com](http://www.fiverr.com) is great for finding voice actresses for $5.
    

      You can’t record too much information about Twilio requests, responses, and errors.  I stuff everything in Redis these days.  I strongly wish I had started doing this earlier, rather than writing “An error happened” to a log file and being unable to determine exactly what the error was or easily figured out whose account it actually affected.
    

      When in doubt, don’t make that phone call.  Design your system to fail closed.  This is a continuous discipline, but it will drastically cut down on catastrophic problems.
    


    Wrapup
  

    That’s it for the presentation contents.  I remain very interested in Twilio apps, and am happy to talk to you about them whenever. My contact details are trivially discoverable.
  

    I’m going to attempt to write a more comprehensive guide to developing Twilio applications, eventually. We’ll see what form that takes — I would really like to provide people an (even) easier way to get started, but at the same time I can’t justify dropping two months of my schedule to write a traditional book on it.
