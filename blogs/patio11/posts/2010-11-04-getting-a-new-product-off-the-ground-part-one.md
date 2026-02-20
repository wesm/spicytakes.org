---
title: "Getting A New Product Off The Ground: Part One"
date: 2010-11-04
url: https://www.kalzumeus.com/2010/11/04/getting-a-new-product-off-the-ground-part-one/
slug: getting-a-new-product-off-the-ground-part-one
word_count: 2096
---


There was overwhelming enthusiasm from people when I offered to blog about the development of [Appointment Reminder](http://www.appointmentreminder.org), so I will be doing it during the month of November, prior to my planned release.  (Tentatively planned for the end of the month, if it is ready in time.)


## Achieving Activation Energy


Appointment Reminder has, theoretically speaking, been on my plate since April 1st, which was my first day of self-improvement.  I released the MVP — basically, a functioning demo of the core interaction between service provider and customers — halfway through May.  And then I sat on my hands for about six months.


Oh, stuff happened, don’t get me wrong.  I went travelling internationally, twice.  I kicked butt and took names for some consulting clients, got (and turned down) about a dozen job offers, won an award for best presentation at the Business of Software conference, started writing an article for the ACM, met a young lady, and broke my old bingo card sales record.  But while my life is firing on all cylinders, happiness does not write jQuery or Rails code.


My last client project wrapped up in mid-October, I told clients I would be mostly unavailable for the next few months, and I picked the end of November as an arbitrary deadline to finally get Appointment Reminder out the door.  Deadlines tend to coerce me into doing my best work.  Specifically, deadlines with subgoals that have small units of measurable accomplishment work best for me.  It must be the WoW player in me, I swear.  So I broke the month or so of work up into a series of mini-quests which take about half a day to accomplish, and then logged the first dozen or so in [EpicWin](http://www.rexbox.co.uk/epicwin/) (productivity management for recovering WoW players — my other quests include going to the gym, doing the dishes, and calling each of my younger brothers).  I have been polishing them off more or less according to plan.


## Technology Choices


When I start a greenfield project (and AR is still new enough to be mostly greenfield), one of the first things I write down in the project notebook is what technology stacks I’m good with and which make a fit for the product.  Given that my options for web development are Big Freaking Enterprise Java and Rails, Rails was the clear winner.  I am literally an order of magnitude more productive in Rails than I am with Java, and I lack the experience with Java architecture astronomy to build an application from the ground up (which I have done successfully in Rails before).


I sometimes also use the opportunity of new projects as an excuse to broaden my horizons.  For example, I’ve wanted to get into jQuery for a while since the world seems to be moving that way (away from Prototype, my old Javascript framework of choice), so I decided to take the minor productivity hit with starting a new framework and moved to jQuery.


My other professional growth goal with AR was to get a little more serious about interface design.  Thomas Ptacek has been raving to me about how much better SASS/Compass made the experience of getting CSS to work right, so I decided to move to SASS/HAML from my previous CSS/ERB standbys.  This delivered huge, huge wins within two days of starting exploratory coding with the project.  I can’t recommend [SASS](http://sass-lang.com/) enough.  This also led to a bonus: the lack of markup going into my views means that I can develop against a cheapo CSS template and then swap to a professional design later, without having to have the design be on the critical path for November.


## Design on Paper


I generally keep all notes for a project in a $1 notebook.  However, my first Appointment Reminder notebook is nowhere to be found.  Drats.  I probably left it in a hotel room in America.  So I bought a new notebook and started sketching out database tables, screens, features I would like to include, etc etc.  Then I started cutting, ruthlessly.


For example: Users need to be able to manage clients.  OK.  Hypothetically, they may have hundreds or thousands of them, so they’ll need a search interface… but will they have hundreds or thousands on launch day?  No?  *Search is out of scope*.  Next!


Users need to be able to give custom reminders to clients.  This requires recording their voice.  Uploading files is a pain in the keister — *out of scope*!  I’ll make do by having them just narrate the reminder over the phone to Twilio, which would obviate the need for me to do any file encoding or management myself.


And so it continued.  By the end of my first working lunch, the feature list that was in scope ended up looking something like this (broken down roughly along controller/model lines):


**Accounts**


Account creation


User management


User permissions (Enterprise-y feature, enterprises aren’t going to adopt in first two weeks: out of scope.)


User preferences


Login / Logout / Forgot Password


**Clients**


CRUD app for users to add clients


Track phone numbers and email


Communication preferences


Opt out of reminders in case of abuse (Barely avoided being out of scope: it is important but doesn’t sell software.)


**Schedules** (one schedule manages one resource — a room, service provider, etc)


Default schedule (most users will have only one)


CRUD app for schedules


Change hours of business day, days of business week.  Eventually that might change on week-to-week basis, for now, simplest thing that works.


**Appointments**


Appointment calendar — starred several times because this is going to be the hardest part of the app


CRUD for appointments, based on calendar


Status tracking for appointments


Reports for number of appointments missed, etc Can’t be used on day one, out of scope.


cron job to send reminders about appointments


**Reminders**


Spawned automatically from appointments


State machine (see below)


Twilio integration


**Twilio**


Inbound calls


“Who the heck are you and why did you call me?” auto-response


Reset trial (already implemented)


Record custom reminder


Get schedule for day dictated over phone great feature, out of scope for now


Voice-assisted tour only in scope if I have two days left over


Outbound calls


Reminders


If answered live, capture user input and update Appointment state accordingly (coming, canceled, needs call, etc)


If answered by machine, leave message, update Appointment state as notified.


Reminders with custom recordings


Text messages


Email


Thank you for signing up, blah blah blah


Password reset


Appointment reminders


User notifications on appointment confirmation, cancellation, etc out of scope


**Billing**


Get paid (oh heck yes, in scope)


Assorted Stuff


Account deletion out of scope


Admin interface God gave us console for a reason


Custom analytics Nobody to track on first day


A/B tests (would be out of scope, but hey, free since I have [A/Bingo](http://www.bingocardcreator.com/abingo/))


Whitelabel version


HIPPA compliant version


Change tracking (e.g. audit trail for deletion, etc)


## Exploratory Coding Begins


After playing around with the signup screen for a little while, mostly to get a feel for SASS/Haml, I started working on the first feature of the app that would provide user value and be mostly self-contained.  Ideally, I would start with the first thing I want them to do (schedule an appointment), but that requires adding a first client anyhow, so I started with the client administration screens first.


I don’t use Rails scaffolding, although since I got publicly told off [invited to try improvements](http://news.ycombinator.com/item?id=1398957) by DHH for having insufficiently RESTful routes I thought I’d give that a try.  (Turns out it actually does save enough pain to matter, although I still think publicly visible RESTful routes are a mistake.  For internal features of a CRUD app, though, they make a lot of sense.)


What I generally do is start with the index action, verify that I can display records added to the database directly (via the console or a seed script), then start on the show action.  This results in me getting *frequent incremental visual progress* that the program is, in fact, getting better.  Anything which can’t be used yet gets stubbed out with lorem ipsum.  When I feel myself reaching the stopping point for a day, I go to the next action on my list and get the view working, even if it is as simple as displaying a screen which says “This action does not really exist yet but if it did it would show #{@client.name}”.  That gives me a place to pick up again in the morning (or, ahem, afternoon, given my frequent work/sleep habits).


Anyhow, after getting show done, I work on the edit/save loop, which requires building out the model a bit, adding validations, and writing some less trivial controller logic.  Here I frequently discover something like “Hmm, it would be handy to have a way to display messages out of the flash” and start working up a helper to do it in a minimalistic way.  You can see it behind the example of me operating the new (error-enabled) edit window.


Working with jQuery slowed me down a bit when creating some of these screens.  I used [jRails](https://github.com/aaronchi/jrails) to ease the transition (it lets you use all the old Rails-esque Javascript helpers like link_to_remote), but it does not play well with jQuery 1.4 out of the box.  It turns out that the issue I was having was mostly that jQuery executes any Javascript it grabs from the server prior to updating the DOM with the rest of the data it got back, which borks the Prototype-esque habit of sending back both HTML and then Javascript which relies on that HTML being in the DOM to function.  I got around this by simply returning only Javascript — e.g. for the “pop a window to put in a new client” action I return:


This is hacky as heck, and obviates some of the reason of using jRails in the first place, but it works. I can always DRY up the helpers a little more later.


After getting the validations and whatnot working for Clients, and doing some light testing to make sure things worked to my satisfaction, I did similar work for Schedules. I got the basic CRUD functions working in record time, mostly by copy/pasting everything I had done for clients and then just changing the parts of the model and view that were different. The controllers are mostly identical, at least until I actually create the ability to render a schedule.


I’ve finished the CRUD logic for my first two parts of the problem domain, and am impressively ahead of schedule. To celebrate, I spent a day upgrading jQuery to the latest stable version (not quite so fun), upgraded the jQuery week calendar widget I was using to a fork that is being actively maintained, and wrote code to render the minimum calendar possible without actually having any appointment data available.


And that is about it for today. Tomorrow: hooking up the ability to add appointments to the schedule, then CRUD logic for them, then the ability to create an appointment and client at the same time. That will complete the first take on the core interface logic for the application, leaving me next week to tackle integration with [Twilio](http://www.twilio.com).  (I had originally planned on that taking at least two weeks, but I remember it being much easier than I expected back when doing the MVP, and I seem to be progressing faster on this project than I typically do.)


Plans after that are roughly:

- Turn on user account creation, log in/log out, etc
- Create staging server, taking care to document my setup process on a computer this time (darn missing notebook)
- Add integration with [Spreedly](http://www.spreedly.com)/Paypal for billing
- Polish as much as possible.
- Test as much as possible.
- Ship at or near end of November.


## After Shipping


After shipping, of course, comes the 90% of the remaining work needed to turn an application into a business.  (Of course, I have been doing some of it all along: speaking with customers, gathering requirements, thinking about marketing angles, etc.)  In particular, I’m starting to devote my free cycles at lunch into thinking about scalable content generation strategies for organic SEO, which is the form of marketing that I’ve had the best results with in the past.


But it is highly likely that, immediately after launch, I’ll have a bare handful of customers and a fairly relaxing December with answering customer support queries (and pre-sales inquiries), mapping out future development, starting the marketing engine, and enjoying Christmas with my family.  Then, on to January.
