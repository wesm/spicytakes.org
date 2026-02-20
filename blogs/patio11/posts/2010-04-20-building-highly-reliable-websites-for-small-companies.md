---
title: "Building Highly Reliable Websites For Small Companies"
date: 2010-04-20
url: https://www.kalzumeus.com/2010/04/20/building-highly-reliable-websites-for-small-companies/
slug: building-highly-reliable-websites-for-small-companies
word_count: 3991
---


Downtime severely annoys customers.  Downtime annoys sole proprietors even more, because it has a funny way of invariably striking at the worst possible time.  Apache has no respect for date night.  So if you’re a small company without dedicated ops team, you might well be [worried](http://news.ycombinator.com/item?id=1269592) about whether you can reasonably promise customers that you’ll be able to avoid inconveniencing them while still maintaining some semblance of sanity in your own life.


Happily, you can, if you’re savvy about it.  I’ve supported thousands of customers and hundreds of thousands of trial users for four years without causing frequent outages, despite not being particularly skilled at server administration or having a huge money or time budget.


## Setting Expectations


Let’s get this out of the way: are you a small company dependent on technology?  You will have downtime.  You will wear a communication device twenty four hours a day for the next several years, and respond with alacrity if it goes off.  The purpose of the rest of this blog post is to minimize downtime and have that communication device do as little damage to your relationships and sanity as possible.


Specifically, you will want to:

- Anticipate failure ahead of time
- Minimize the inicidence of failure
- Be notified of failures in a timely manner
- Quickly recover from failure
- Learn from failures to prevent reoccurence


Many of these tips are **specific to my personal experiences** as an entrepreneur with a small business.  If you work in a highly regulated industry, have a dedicated ops team, or are Google, you probably should not be reading my blog to solve your technical challenges.


## Identify Risks To Your Service


The key to building reliable systems is first to know where the risks are.  Don’t be suckered into thinking that downtime is generally caused by unpredictable black swan events: that is an easy mistake to make when reading stories about reliability from Google et al.  This is partly because they have large teams of supergeniuses wielding nearly infinite budgets to build reliable systems, and partly because when they do have downtime they typically phrase the report of it in such a way that it sounds like it was a black swan and not systemic failure to follow routine, easily understood policies seven times in a row *plus* the black swan that let the system go down.  (We’ll be returning to the policy theme in a moment.)


No, your risks are quite predictable, and you can jot them on a piece of notebook paper right now.  I’d strongly suggest actually physically doing this, as it helps inform your thinking about what is likely to break and what you’ll need to do to mitigate the risk of that.


Not sure what your risks are?  I’ve worked for the last several years in Nagoya, the Town that Toyota Built, and even though I was never in the automotive industry my professional mentors were heavily influenced by it.  You know what causes 99% of problems with cars?  *Moving parts*.


It is astronomically more likely for something which moves to fail than something which doesn’t: it is subject to friction, wear, foreign particles, and a thousand other sources of failure.  By comparison, all the chassis of the car has to do is not decompose into its constituent atoms, and since it hasn’t done that until now it is a good bet that today will not be the day it picks to do so.


**Software systems are also, overwhelmingly, killed by their moving parts.**


Hard drives, to be very literal, are one of the only things that actually move in your server, and statistically speaking they’ve got the worst failure rate of any device in the box.  Serious engineers treat hard drives as a component that by grace of God has not died yet.  That is why we put them in RAID arrays which abstracts the life and death of particular hard drives away from users of the system.  I’m rationally ignorant of how RAID actually works: if you want to know, read a book; if you want to do something productive with your day, pay your VPS provider or managed hosting company to deal with this for you.  Trust me, you have better things to do than actually touch hard drives.


Side note: This is increasingly becoming true of [just about everything](http://mvdirona.com/jrh/TalksAndPapers/JamesHamilton_SMDB2009.pdf) [PDF link] in computer systems: scales are such that statistically speaking something is broken right now, so we’ll build our systems in the assumption that they’re broken to a degree unpredictable at run-time, and still squeeze some work out of them.  “The Cloud” has not quite brought web-scale computing principles to the smallest software companies yet, but I think it is highly likely we’ll adopt bits and pieces of them eventually.  After all, essentially all of us use RAIDs these days, many without knowing it, while they were a Serious Tool for Serious Businesses only a fairly short while ago.


**Less literally speaking, your system is most vulnerable where it sees dynamism, complexity, and change.**


It is at its most vulnerable when you are working on it and shortly after, because computer systems largely do not rot and once they’ve achieved a steady state tend to stay in it until something exceptional happens.  You are your own worst enemy, and you’ll take steps to mitigate the threat you pose, as described later.


Many web applications these days have easy dividing lines between static and dynamic requests.  The dynamic requests represent generally a small fraction of the overall total but will cause almost all of the failures.  If you have, for example, Nginx proxying to Mongrel, you can be quite confident that Mongrel will fail much, much more often than Nginx will.  (In point of fact, Nginx fails so seldomly you can almost get away with ignoring the possibility of it happening, since something else will almost surely kill either your service or you personally prior to Nginx dying on you.   Carry life insurance and look both ways before you cross the street, but if you have too many things to do and not enough time to do them in, worrying about Nginx failing is something you can probably safely kick down the road.)


Your database is also a high-probability culprit for failing, partially for practical reasons (it is a very sophisticated bit of engineering which by its very nature is highly dynamic) and partially for philosophical ones.  For historical reasons, most databases are made/configured around the assumption that it is better to fail loudly and completely rather than fudge the ACID guarantees silently.  This is a perfectly reasonable engineering tradeoff for a bank’s transactional systems which might not be optimal for the sheepthrowing statistics your app may be tracking.  (The degree of this impedance mismatch is why some folks are very passionate about the whole NoSQL thing when they really just want to drop ACID.)


Then there are a whole host of systems outside of your direct control which can nonetheless bring your system down.  Your hosting provider’s network, for example, can fail at any moment, and typically a failure there is essentially a 100% loss of service for the typical web application.  Their upstream provider could similarly fail.  Any API your application depends on could fail in a hundred ways at any time.


Basically, keep writing on that piece of notebook paper until you run out of obvious sources of failure.


Here’s the abbreviated list of things that could go wrong at my business.

- Operator error
- **Operator error**
- ***Operator error***
- Hardware failures on the server
- Network failures at Slicehost
- Mongrel fails
- MySQL fails
- Memcached fails
- Delayed Job fails
- Scheduled cron tasks fail
- External APIs (e.g. [Mixpanel](http://www.mixpanel.com)) fail
- Embedded Javascript (e.g. Google Analytics) fail


All of these have actually happened at one time or another, but most did not cause downtime for my customers.


## Mitigating Failures Before They Happen


After you have some idea of what is likely to go wrong, you can start taking actions to mitigate it.


One conceptually easy step is **decoupling**: make it so that a failure of a particular component can’t bring down the entire system.  This isn’t always possible in a cost-effective fashion: for example, in a heavily dynamic web application, it is highly likely that the database failing means you’re going down hard.  *That is OK*.  Ideally, your business is not running the power generators at a hospital: you don’t have to eliminate all of the downtime, you just have to minimize it, **so go after the low-hanging fruit** before addressing “what happens if the database dies”.  (Answer: nothing… if you spent a few months of Very Expensive Engineer Time working out a replication/failover strategy.  That is overkill when a) your customers are the sort that will tolerate a bit of downtime once every blue moon and b) you’re much, much more likely to bring the server down because you didn’t spent ten minutes writing a deployment checklist.)


One example of decoupling: **never call an external API from within an HTTP request/response cycle**.  That essentially makes your system 100% dependent on the external API being constantly available.  Their downtime is now *your* downtime.  Their capacity problems are now *your* capacity problems.  Their operator error is now *your* operator error.


Instead, do all communication with external APIs asynchronously.  There are many common patterns for this.  My website calls out to Mixpanel for statistics tracking but the end-user doesn’t care about that, so I just queue up a Delayed Job to do the API call asynchronously and regardless of it eventually succeeding or failing my user never cares.  This means that Mixpanel’s (quite infrequent) downtimes have not caused my users any loss of service.


If your users actually need to see the results of the API call, you can schedule the call asynchronously and then do AJAX-y magic to poll the server asking if it has completed yet.  If it doesn’t complete in a reasonable amount of time, you can either tell the user to do so in a nice, customized error message, or you can fallback to something which you can accomplish locally.  In many applications, for example, instantaneous response to changes in the underlying data is just “nice to have” rather than a genuine requirement — RSS readers, for example, usually won’t kill anybody if they are a few minutes out of date.  If updating an RSS feed fails for whatever reason, you can probably get by with showing the user your most recent cache of it — quite possibly without ever telling the user about the failure at all.  (Engineers often are excessively protective of users.  Personally, in most applications that don’t involve lives or money, I would rather tell the user a white lie than show them a red error message.  This is particularly true when they can’t really do anything to address the error message other than “Try again later [and pray a third party who you don’t even know exists has figured out why they are throwing 501 status codes and addressed it].”)


Similarly, you can decouple bits of your web infrastructure from other bits.  In Rails applications, Mongrel can (and will) fail independently of Nginx.  By default, this will result in Nginx showing a forbidding black and white page with a scary error message on it.  That is a terrible user experience and you can alleviate it in seconds: create a nice-looking page using nothing but static assets, and have Nginx serve it using the error_page directive.  Somewhat contrary to what many engineers might assume, users are often largely mollified by *anything* showing up on their screens, and a well-written error page is sometimes almost as good as a functioning system.


I know the failwhale is a running joke, but that is just because we see so much of it and are accustomed to our computers mostly working.  More typical users have computers eat their documents, freeze, and break all the time for no discernable reason at all, and if you do your job right they may *never* see your system fail twice, so their first and only encounter with your error page might not actually cost you too much customer goodwill.


**Automated recovery** is another smart mitigation step to take.  I use a [process manager called god](http://god.rubyforge.org/) to watch over my Rails programs, and when a Mongrel starts consuming too much memory or failing to respond to “Are you alive?” messages, god forcibly restarts it.  This sounds almost crazy to the Big Freaking Enterprise engineer in me, but practically speaking it eliminates almost all common Rails problems (e.g. poor memory management caused by overly enthusiastic creation of objects and not garbage collecting them efficiently) before they cause a problem for my customers or myself.  The god daemon is, similarly, restarted daily to avoid it having memory leaks.  Yep, it smells strongly of duct tape, but the duct tape *works*.


**Minimizing operator error** is critically important, because **you are the least reliable component of your system**.  Because you rely on software to do most of the actual work, when you touch the system you’re almost by definition performing something novel that isn’t automated.  Novel operations are moving parts and vastly more likely to fail than known-good operations that your system crunches millions of times per day.  Additionally, even if what you want to do is absolutely flawlessly planned out, you’ll often not execute flawlessly on the plan.  This was one of the root causes of my [worst downtime ever](https://www.kalzumeus.com/2010/02/21/i-had-downtime-today-heres-what-im-doing-about-it/).


Happily, the steps to minimize operator error are well understood.  Unhappily, they require swallowing a bit of your ego and actually following them.  They’re well researched, reproducible, and will save you time in the long run: get over yourself.  I had to, too.


**If you have to do it more than once, it should be automated or made into a checklist**.  This includes things like:

- server setup
- sever upgrades
- upgrading code on the staging server
- upgrading code on the production server
- any maintenance task


Checklists are very simple: just a textual description of what the list describes, why you’d want to do it, what the *exact* steps are (i.e. down to what you type into the console), and what the exact steps are for verifying that the procedure was carried out correctly.  This last bit is non-optional: subtle failures in maintenance tasks are a frequent cause of downtime, sometimes weeks or months later.


This is one reason we spend so much time on root cause analysis, to demonstrate to skeptical engineers that checklists are like flossing.  My dentist tells me “If you think flossing is a nuisance, that’s fine: just floss the ones you intend to keep.”  If you think checklists are a nuisance, that is fine: you can feel free to skip checklists for systems where catastrophic failure is no big deal.


I personally keep checklists in text files, because I only have one person to worry about, but in a multi-user organization wikis are fantastic for them.  This goes doubly true for wikis which keep version history, because frequently as the system matures and as you respond to issues the checklist will need modification, and rather than tracking Bob down and asking him what this command is supposed to do, a well-written changelog will tell you “That command is there to prevent you from hosing the DB like we did last August.”


Certain checklists are executed very infrequently.  Of particular note is one checklist that absolutely everyone should have: how to restore a machine (or machines) from the bare metal to a working copy of the production system.  Ideally, you should be capable of doing this in 15 minutes or less, because if you ever have to do it for real it means that disaster has struck and your site is now down.  **Take 15 minutes out of your busy schedule every quarter and actually run that checklist to make sure it still works.** You will frequently find “Oh, effity, we use GraphicsMagick these days rather than ImageMagick but nobody wrote that on here.  Hah, silly me.”  which, if this were an actual emergency, would have you scrambling to correct while the site was still down.  “Scrambling” sounds a whole lot like *moving parts*, right?  Right, you’ll be introducing more errors at the worst possible time to have them, in the middle of an emergency.  Get emergency recover down to a routine, so that when you actually have an emergency (and you will, eventually), dealing with it is a matter of routine.


**Automation is your friend**.  Some organizations get checklist happy and make checklists for procedures which essentially can’t fail and which require no judgement.  Those shouldn’t be checklists — they should be shell scripts.  That way, they save your engineers time and you can be confident that the latest script in version control (it *is* in version control, riiiiiight?) is well-tested (it is tested, riiiiight?) and will actually work.


Of particular note in the Rails world: [deprec](http://deprec.failmode.com/) and [Capistrano](http://www.capify.org/index.php/Capistrano) are wonderful tools which automate server setup (very well suited to deployment to a VPS like Slicehost) and application deployment.  These are absolutely lifesavers and, although I’ve bashed my head against both a few times (typically with integration issues with Windows) they save you from weeks and weeks of script writing.  I also sleep much more easily at night knowing that I’ve set up a staging environment in ~8 minutes using my Capistrano script this month and, if *everything* else went wrong, I could have a server reimaged and loading my database backup almost as soon as I got the phone call.


## Be Notified Of Failures In A Timely Manner


Many failures can be solved or mitigated fairly quickly after you get to a computer, which means that time to recovery is dominated by the time it takes from the time the failure arises to the time it takes for you to be made aware of it.  There are easy, reproducible ways to bring that down to “a few minutes or less.”


**Low-hanging fruit**: The absolute easiest possible solution is to point [Pingdom ](http://www.pingdom.com)or [Mon.itor.us](http://mon.itor.us) at your home page and have them contact you if it doesn’t resolve.  They’re fairly simple: if the server doesn’t respond with HTTP 200 when they try to access it (every 15 minutes or so), you get an email or SMS.  This is the simplest thing that could possibly work, but there are circumstances where it won’t catch failures.  (For example, applications of non-trivial complexity often have parts which can fail without taking the front page down.)


I recommend creating an internal status page which automatically checks all the things you think are crucial, risky, and tractable to resolution if you were to know about them.  (If an external API provider goes down and you already know your response is going to be “I wait until it comes back up”, then no sense disturbing your sleep about it, right?)  For example, mine will fail to return properly if Nginx, Mongrel, the Delayed::Job workers, memcached, or Redis is having a bad day.  You can then have your external monitoring poll that page and, if they don’t get the HTTP 200 all clear, send you an email.


For folks who are feeling adventurous (or excessively stingy), you can rig your own server monitoring terminating with a phone call or SMS with [Twilio](http://www.twilio.com) and about 30 minutes of work.  If you do this, you can escape the time or notification limitations which the notification services use to segment their customers into “hobbyists” and “enterprises who have an awful lot of money to spend to make sure nothing breaks.”  Personally I don’t think it is worth it but, hey, it is an option.  (Note that this introduces another moving part into your system which, if it fails, you will probably find out about only when your main system is down… a couple hours after the fact.  This is a compelling reason to not be a cheapskate.)


I have a very simple solution for going from notification mails to instant awareness of the problem: my cell phone, which is a cheapo Japanese model, can do custom ringtones for individual callers or mail senders.  In the event I get an email from my notification service, it plays [Ride of the Valkyries](http://www.youtube.com/watch?v=V92OBNsQgxU).  As I recall, I’ve heard it twice, once while sound asleep and once on date night.  (The interesting question of whether I would have begged off of date night may not ever be answered, since I was able to successfully reboot before my girlfriend noticed.)


In addition to the phone-in method of server monitoring, you can also use the phone-out method.  I have been using [Scout ](http://www.scoutapp.com)for the last couple of weeks, and it is wonderful.  Basically, a cron job running locally reports a variety of statistics to their server every few minutes, and if the statistics are anomalous or the report fails to happen as scheduled, you get detailed warnings of it.  My sole problem with Scout is that it is one chatty little robot: by default, it sends me emails about things like not-even-close-to-critical demand spikes (you went to 2% CPU utilization for a minute?  *Poor baby!* My business got linked to from Reddit and requests spiked 1,000% without any performance degradation: great, why are you telling me?).  After a few weeks of tuning I’ve mostly shut it up about non-critical notifications.  (One other gripe with Scout is that they reserve SMS notifications for their priciest plan.  It is market segmentation, I know, but in an age of Twilio it is almost petty.  Still, I feel quite satisfied on their $20 a month option.)


## Quickly Recover From Failure


Ideally, you’re either recovering automatically or you’ve been given timely notice of a failure you anticipated and now all you have to do is open your checklist.  Neither of the above?  Well then, this is why you earn the big bucks.  Godspeed.


## Learn From Failures To Prevent Re-occurrence


We’re a big fan locally of Five Whys, which has lately achieved a bit of prominence in US startups due to [Eric Ries](http://www.startuplessonslearned.com/2009/07/how-to-conduct-five-whys-root-cause.html) and the rest of the Lean Startups crowd.  Boiled down to its essence, Five Whys says that no failure ever has one cause.  There might be a single surface-level immediate cause, but the failure is also a symptom of multiple process failures because you had things in place to prevent that failure from happening and they did not trigger or were not effective.


I’m ruthless about doing the corrective action — root cause analysis — in my own business.  You can see an example [here](https://www.kalzumeus.com/2010/02/21/i-had-downtime-today-heres-what-im-doing-about-it/).  I’m more proud of that failure than a lot of my successes, because I learned from it.


Basically, you keep peeling layers of the failure onion until you’re satisfied that you’ve gone deep enough: five layers is a guideline, not a rule.  You then invest proportionate resources into making sure that each of the failures does not happen again.  This could mean updating procedures/checklists, adding features to your autorecovery code or diagnostics, beefing up employee training, etc etc etc.


A note for those with employees: Five Whys will frequently — very, very frequently — implicate human or cultural issues in your organization.  Just trust me on this:  you’re not alone, and you can persevere through the difficulties.  Resolving critical defects was ironically one of the least contentious processes we had at my ex-day job — even in a Japanese megacorp we had internalized that it was too important to coat with the usual amount of corporate horsepuckey.  (It helps that my Japanese megacorp is in Nagoya and that the development practices of a certain large automobile manufacturer are practically state religion here.)  Check the egos, chuck the org chart, and make the fixes you need to make to uphold your responsibilities to your customers.
