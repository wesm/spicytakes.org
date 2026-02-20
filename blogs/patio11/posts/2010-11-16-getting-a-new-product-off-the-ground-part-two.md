---
title: "Getting A New Product Off The Ground: Part Two"
date: 2010-11-16
url: https://www.kalzumeus.com/2010/11/16/getting-a-new-product-off-the-ground-part-two/
slug: getting-a-new-product-off-the-ground-part-two
word_count: 2498
---


Along with some other users from Hacker News, I’m doing my darndest to get [Appointment Reminder](http://www.appointmentreminder.org) into the hands of customers by the end of November.  It looks like it is going to happen, too.  (There was an early blog post about this [here](https://www.kalzumeus.com/2010/11/04/getting-a-new-product-off-the-ground-part-one/).)


## Rails Deployment Options


Somebody asked me to talk about this subject, so I will cover it briefly.  Rails deployment has historically been very painful.  These days it is a little better.  The big options are:

- Run a Rails stack on a server or VPS under your control
- Use Heroku
- Run a Rails stack on Amazon EC2


I have used Heroku for a client project before.  It is a wonderful service, don’t get me wrong, but I have almost five years of managing production Rails applications on a VPS and less than five weeks of managing production Rails applications on Heroku.  I know from experience that I will try to do things during development where Heroku’s limitations (like the read only filesystem) will trip me up, and tripping myself up doesn’t get things in the hands of my customers any quicker.


Additionally, my anticipated traffic for Appointment Reminder is way, waaaaay within the capacity of single largish Slicehost slice to handle.  If I manage to bring my Slice to its knees, it will be because my revenue has hit several million dollars a month.  That will give me many attractive scalability options, such as hiring someone to care about scalability while I sip chilled juices on the beach of a tropical island.


I built a staging server, from scratch, and obsessively documented the process.  (I strongly recommend that you do this for building servers, since you will have a burning need for that documentation if something ever goes wrong.)  It relied heavily on the [Deprec gem](https://github.com/mbailey/deprec), which is far and away the easiest way to get a Rails stack running on a bare Ubuntu install.   I still spent almost 4 hours filing down sharp edges, though.  (Sample: I wanted to run Rails 2.3.10 rather than upgrade to Rails 3, there were issues with compiling Mongrel on Ubuntu that had to be resolved via manually grabbing packages, etc etc.) I only really recommend this if you know what you’re doing with Rails system administration.


In terms of software choices for my deployment stack:

- Ruby 1.8.7 via the Matz Ruby interpreter.  It isn’t the fastest, but speed is hardly of the essence to this application and it is the least likely to die horribly when using a gem or library, since everybody tests against it.
- Rails 2.3.10.  I don’t want to learn Rails 3 at the moment.  Maybe next year
- Mongrel cluster: I have experience managing it.
- Nginx: The best web server I’ve ever had the pleasure of working with.  Also plays well with PHP, which I need on the box to handle the marketing portion of the website outside of the application.  (The marketing site is in WordPress.)
- God process monitoring: I have experience using it.
- DelayedJob job queuing: I have experience using it.


I will probably eventually put WordPress on a physically separate server (hey, it’s WordPress), but that doesn’t strike me as the biggest priority at launch.  I did go to a wee bit of trouble to secure it:

- Access to the admin directory is denied at the server level for requests not from my private network.
- WordPress has its own database and database user, and can’t touch anything elsewhere.
- The WordPress directories are only writable by root, not by the web server user.  If I want to install plugins, I get to SCP them to my account on the server then SSH in and start sudoing to actually copy them in.  Ditto for uploading files.  Facilities to upload and immediately execute PHP code are, ahem, a persistent source of vulnerabilities.


## Code Is About 70% Complete


I have sustained pretty close to my lifetime peak productivity at programming (say that five times fast) for the last two weeks, averaging 4 to 6 hours per weekday.  Appointment Reminder has most core functionality implemented on the staging server, for a single single-user account.  [Twilio](http://www.twilio.com) has been an absolute joy to work with — I really can’t express how much of the pain they take out of running a telephony company.


What’s done:

- Client creation/management: 100%
- Appointment creation/management: 90% (still need to associate scripts with appointments)
- SMS reminder loop: 100% implemented.  (web app -> Twilio -> user’s phone -> web app)
- Phone reminder loop: 100% implemented (web app -> Twilio -> user’s phone -> web app)
- Dashboard: 90% implemented.  (Needs to be a wee bit more configurable, particularly for multi-user environments.)


Things are looking fairly slick thanks to jQuery UI and a lot of AJAX, but it has been a bit of a handful to test.  If you have suggestions for doing so, I’d love to hear about them in the comments.  Mostly I have been doing unit testing for models which are likely to have failures, and then doing manual testing to verify that the UI works how I expect it to.


I am currently using an absolute riot of colors on the dashboard to convey status information.  That probably should get reduced.  SASS has been very, very helpful in keeping me from having to handwrite CSS to manage all of these.


What still needs work:

- Email reminder loop: 0%, should take ~4 hours for simplest thing that will work
- Script creation/management: 0%, should take 1~2 days (this requires hooking up another phone system)
- User/account management: 0%, should take ~2 days
- Reports: 0%, should take ~1 day for simplest thing that will work
- Feedback to user on appointment status changing: 0%, 2~4 hours depending on how full-featured I want to launch with
- Charging people money (using [Spreedly](http://www.spreedly.com) — shouldn’t take more than a day)


## Outsourcing Up A Storm


I have had a lot of luck using [Fiverr](http://www.fiverr.com) for getting recordings done cheaply.  Try the [Appointment Reminder demo](http://www.appointmentreminder.org/a/calendar) to hear one of the voiceover artists in action.  My plan is to launch with about four different sets of voices to give customers some variety: I expect that most will actually record their own reminder scripts, but anything which decreases the amount of work it takes before they get a phone call from the system is a win for me.


I also plan on eventually using reminder scripts as a cheap way of marketing.  There are virtually infinite marketing angles once you have the ability to make a phone ring, since it is so ridiculously compelling.  (I mean, people paid how many *billions of dollars* for ringtones?)  For example, I have an absolutely unhealthy interest in the [Old Spice Man](http://www.youtube.com/watch?v=owGykVbfgUE).  Getting a script inspired by the character is easy, remarkable, and is both a win for my customers (“That phone call you gave me earlier was hilarious!  Thanks!”) and lets my customers market AR inside their organizations (“Cindy, you have to hear this.  Quick, what is your phone number?”)


There are virtually infinite variations on that: you could imagine getting a phone call from a Humphrey Bogart impersonator, etc etc.


Speaking of outsourcing, I recently started using a Virtual Assistant, something I have been meaning to try since reading about them in Rob Walling’s [book](http://www.startupbook.net).  I found mine through an agency called [Pepper](http://www.peppervirtualassistant.com/) (that name is a bit of an easter egg for comic book geeks in the audience).  For about $300 a month, I get twenty hours of time from one particular lady who works at their office.  She does, within reason, anything I tell her to do.  This has been a huge win for me in cleaning boring, time-sucking tasks off my plate so that I can concentrate on development and marketing.


For example, up until quite recently I was ten months behind on bookkeeping.  That’s a long story: I do expenses bookkeeping via a home grown application so that I can display [nice graphs](http://www.bingocardcreator.com/expenses/profitability-pie-chart?year=2010) on my website, and that application got broken by an unrelated update back in February.  (Bookkeeping of revenue is totally automated, and didn’t break.)  Since customers don’t pay me to do bookkeeping, fixing it went on the back burner.  I eventually got it working again sometime in summer… and then had six months of credit card statements to process.  Well, that sure sounds like *work*, so I procrastinated… until there were ten months of statements to process.  Crikey.  It kept getting worse, it kept weighing on me that it wasn’t done, and I didn’t want to spend a day or two just going through 20 PDF files and typing some 300 transactions into the computer.


Enter my Virtual Assistant.  I spent ten minutes typing up my decision tree for classifying transactions (the credit card statements have mixed business and personal charges — whoops, got to fix that one next year), instructions for operating the bookkeeping interface, and the like.  Then I created an account for her in the system, zipped up the 20 statements, sent them over, and answered an email or two from her over the course of the next week.  Managing her and reviewing her output took perhaps 30 minutes in total, instead of somewhere on the order of three to six hours to do the data entry myself — plus, it didn’t totally wreck me for other productive work that day.


I’m now almost caught up with bookkeeping (got another statement delivered by my bank in the interim), and now that there is a process in place for it keeping caught up is simplicity itself: download statement, shoot it to my VA, go on to do things that actually matter.


This was **astoundingly** beneficial for me.  I have a nagging worry taken off my plate and a process to make sure it never comes up again.  I got to invest several extra hours in things which matter to the business, instead of doing data entry.  That covers the first week of the month: if I never got another stitch of work done, I’d consider my $300 well spent, but I’m guessing that I can almost certainly find other stuff for her to do.


When I get some time to breathe this month, I’m going to figure out other tasks I can assign to her: perhaps drawing up lists of keywords or blog post topics.  I mean, I could spend a day coming up with every possible permutation of a professional service plus every possible synonym for “scheduling software”, but that doesn’t require my personal attention.  (Why I would want a list of hundreds of keywords about my software is fairly straightforward if you’ve followed my bingo card creation endeavors: implement system to create content at scale, farm out content creation to freelancers, cover the organic search longtail for the topic, sell thousands of accounts to organic searchers).


## Speaking To Customers


Dharmesh Shah, I think, said that there are phone people and email people, and that most engineers are email people.  I am definitely an email person.  I hated speaking on the phone even before I started using the Internet.  But I’ve been chitchatting with prospects (at Ungodly O’Clock AM) for the last couple of weeks to hear about their needs, and have both learned stuff I didn’t know about my market, confirmed some stuff I did know, and — importantly — gotten some promises to pay me money **immediately** when the software is ready.


Here is my mental model of the typical customer for Appointment Reminder: Martha owns a massage therapy practice.  If Cindy, her client, doesn’t make her 4:00 PM massage, then Martha loses $60 of revenue immediately and will likely be unable to rebook the slot, since she’ll find out about the gap at about 4:05 PM.  Appointment Reminder either gets Cindy in on time or gets Martha 24 hours of notice, so she can book the slot.  Martha happily buys the service.


Note the embedded assumption there: Appointments are something you *go to*.  I never even realized I was assuming that.  It turns out that I was, and that there is a broader market than I expected, for appointments where the service provider comes to you.


Why does this distinction matter?  Because Martha is greatly annoyed when her customers don’t come in, but she has not literally lost money out of her pocket.


Consider Earnest the Exterminator.  He has a team of three guys and a van filled with lots of dangerous chemicals.  When Earnest makes an appointment, he finds out that you’ve forgotten **after he drives 25 miles to your house**.  Not only did Earnest just lose out on the revenue from killing your bugs, he just burned up **three hours of salary** at skilled labor rates because you forgot that today was, indeed, Tuesday.  Martha is greatly inconvenienced by her no-show problem.  Earnest is **sputtering with rage** about his now-show problem.  I now know this because I’ve gotten on the phone with three different Earnests now and just *shut up* while they talked about their problems.


I’m going to make changes to my marketing posture to reflect this (the Marthas of the world are overwhelmingly female, but there are an awful lot of guys in the Earnest category along with some ladies), and I’ve also started to create some features for supporting Earnest and his team.  Some of my Earnests have been surprisingly tech savvy (“Oh, my programming team wants to know about your API.”  “You have a programming team?!?”  “Bleep yes I do, you think I’m going to run the systems myself?”), and the knowledge that the user of the software could very possibly be mobile rather than at her place of business really rejiggers my development priorities for e.g. checking your schedule via a phone call.


Plus, as you can probably guess, somebody who has a programming team and a very good idea for how many tens of thousands of dollars they lost last year to no-shows is, shall we say, quite willing and able to pay any price I want to charge.


## Next Steps


More of the same, really.  I just got confirmation from one of my freelancers that she is working on the MP3 files for phone calls.  Tomorrow I build out the script interface to allow people to pick or record the telephone/SMS/email scripts that they use.  After that is done, I think I’ll do the email integration, which is the last bit of actual functionality for the site.  After that, user management (if worse comes to worse, all I really need is to have users have separate settings, and I can do all creation of secondary users by waiting for emails from customers and then doing it via the Rails console rather than with a slick UI on top of it).


If you have anything in particular you’d like me to cover in the next installment, say the word.
