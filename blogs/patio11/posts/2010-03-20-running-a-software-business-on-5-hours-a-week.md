---
title: "Running A Software Business On 5 Hours A Week"
date: 2010-03-20
url: https://www.kalzumeus.com/2010/03/20/running-a-software-business-on-5-hours-a-week/
slug: running-a-software-business-on-5-hours-a-week
word_count: 5287
---


Some four years ago, I started [Bingo Card Creator](http://www.bingocardcreator.com), a business which sells software to teachers.  At the time, my big goal for the future was eventually making perhaps $200 a month, so that I could buy more video games without feeling guilty about it.  The business has been successful beyond my wildest expectations and has made it possible to quit my day job at the end of this month.  The amount of time I’ve spent on it has fluctuated: the peak was the week I launched (50 hours in 8 days), a very busy week in the last few years spiked up to as many as 20 hours, and the average over the period is (to my best estimate) about 5 hours.


During the majority of the time I’ve had the business, I’ve also been a Japanese salaryman at a company in Nagoya.  For those of you who are not acquainted with the salaryman lifestyle, I leave the office at 7:30 PM on a *very good day*, and have an hour and a half of commute both ways.  In our periodic bouts of crunch time, such as the last three months, I end up sleeping at a hotel next to the office (about 25 times this calendar year).


I’m not saying this to brag about my intestinal fortitude — this schedule is heck on your body and life, and absolutely no one should aspire to it.  That said, I snort in the general direction of anyone saying a nine-to-five job is impossible to juggle with a business because “businesses require 100% concentration”.


Here are practical, battle-tested ways for you to improve the efficiency of your business and deal with some of the niggles of partial self-employment.  They’ll hopefully be of use whether you intend to try running it in your spare time or just want to squeeze more results out of the time you’re already spending.  Many of these suggestions are specific to the contours of running a software business on the Internet, which has a lot to recommend it as far as part-time businesses go — take care before trying these willy-nilly with an unrelated industry.  (Part-time pacemaker research is probably not the best idea in the world.)


## Time as Asset; Time as Debt


The key resource if you’re running a business by yourself is your time.  Other businesses might worry about money — however, you’ve probably got all your needs and then some covered by your day job salary, and capital expenditures in our business are so low as to be insulting.  (I started my business with $60.  Literally.)  And the key insight about time is that software lets us take the old saying about how “Everyone gets the same 24 hours per day” and break it open like a pinata.


**Time *can* be stored**.  One of the great features about currency is that it functions as a store of value: you create some sort of value for someone via your labor, trade that value for currency, and then the currency will retain value even after the physical effect of the labor has faded.  For example, a pumpkin farmer might not be able to conveniently store pumpkins, but if he sells them the currency will (under normal circumstances) not rot.


Most people think, intuitively, time *always* rots.  You get 24 hours today.  Use them or lose them.  The foundation of most time management advice is about squeezing more and more out of your allotted 24 hours, which has sharply diminishing returns.  Other self-help books exhort you to spend more and more of your 24 hours on the business, which has severely negative effects on the rest of your life (trust the Japanese salaryman!)


Instead of doing either of these, **build time assets**: things which will save you time in the future.  Code that actually does something useful is a very simple time asset for programmers to understand: you write it once today, then you can execute it tomorrow and every other day, saving you the effort of doing manually whatever it was the code does.  Code is far from the only time asset, though: systems and processes for doing your work more efficiently, marketing which scales disproportionate to your time, documentation which answers customers’ questions before they ask you, all of these things are assets.


The inverse of time assets is **time debt**.  Most programmers are familiar with technical debt, where poor technical decisions made earlier cause an eventual reckoning where forward progress on the program becomes impossible until the code is rearchitectured.  Technical debt is one programmer-specific form of time debt.  Basically, time debt is anything that you do which will **commit you to doing unavoidable work** in the future.


Releasing shoddy software, for example, commits you to having to deal with customer complaints about it later.  So don’t do that.  Better yet, rather than a useless bromide like “don’t release bad software”, spend time creating systems and processes which raise the quality of your software — for example, write unit tests so that regressions don’t cause bugs for customers.


However, **not all time debt comes from intrinsically negative activities**: there are many things that successful businesses do which cause time debt and *you probably do not have the luxury of engaging in them*.  For example, high touch sales processes incur time debt almost as soon as you put out your shingle: you’re committed to spending many, many hours wining and dining clients, often on a schedule that you cannot conveniently control.  That is generally a poor state of affairs to be in for a part-time entrepreneur, even though there are many wonderful businesses, small and large, created in high-touch industries.


## Code Is About 10% Of Your Business.  Maybe Less.


Are you considering starting up a business because you wish to work on wonderfully interesting technical problems all of the time?  **Stop now —** Google is hiring, go get a job with them.  90% of the results of your business, and somewhere around 90% of the effort, are caused by non-coding activities: dealing with pre-sales inquiries, marketing, SEO, marketing, customer support, marketing, website copywriting, marketing, etc.


Bingo Card Creator has been memorably described as “Hello World attached to a random number generator.”  If anything, that probably overstates its complexity.  Customers do not care, though — they have problems and seek solutions, regardless of whether the solution required thousands of man years of talented engineers (Excel) or one guy working part-time for a week.  (You’ll note that you can make bingo cards in Excel, too.  Well, you could.  Many people can’t.  If I sell to them, I don’t necessarily have to sell to you.)


## Relentlessly Cut Scope


37Signals had many good ideas in their book [Getting Real](http://gettingreal.37signals.com/), but probably the best one is to “Build Less”.  **Every line of code you write is time debt**: it is another line that has to be debugged, another line that has to be supported, another line that may require a rewrite later, another line that might cause an interaction with a later feature, another line to write documentation for.


Cutting your feature set to the bone is the single best advice I can give you which will get you to actually launching.  Many developers, including myself, nurse visions of eventually releasing an application… but always shelve projects before they reach completion.  First, understand that software is a work in progress at almost every stage of maturity.  There is no magic “completion” day on an engineer’s schedule: “complete” is 100% a marketing decision that the software as it exists is Good Enough.  If you have to cut scope by 50% to get the software out the door, you’re not launching with a 50% product: you’re launching with 100% of the feature set that is implemented, with 100% of (hopefully decent) ideas for expansion in the future.


## Pick Your Problem Well


Long before you sit down to write code, you should know what your strengths are and what your constraints are.  If you can only afford to spend 10 hours a week and your schedule is inflexible, then anything which requires calling customers in the middle of the day is out.  Scratch B2B sales for you.  If you have the graphical skills of a molerat, like myself, you probably should not develop for iPhones.  (Minor heresy: while Mac developers are very graphically intensive people who will buy software just to lick it if the UI is good enough, many Mac users are just regular people.  My Mac version has a conversion rate fully twice that of the Window version, and it is not noticeably pretty.)


Some people profess difficulty at finding applications to write.  I have never understood this: *talk to people*.  People have problems — lots of problems, more than you could enumerate in a hundred lifetimes.  Talk to a carpenter, ask him what about carpentry sucks.  Talk to the receptionist at your dentist’s office — ask her what about her job sucks.  Talk to a teacher — ask her what she spends time that she thinks adds the least value to her day.  (I’ll bet you the answer is “Prep!” or “Paperwork!”)


After you’ve heard problems, find one which is amenable to resolution by software and that people will pay money for solving.  One quick test is to see whether they pay money for solving the problem currently: if people are spending hundreds of thousands of dollars on inefficient, semi-manual ways to do something that you could do with Hello World and a random number generator, you may be on to something.  (For example, if you knew *nothing* about the educational market, you can infer that there are at least several hundred thousand dollars sold of reading vocabulary bingo cards every year, just by seeing those cards stocked in educational stores across the country and doing some quick retail math.  So clearly people are spending money on reading vocabulary bingo.  It isn’t *that* much a reach to assume they might pay money for software.)


Other things you would look for in your idea are anything you see yourself using in your Benefits section of the website to entice people to buy it.  (Benefits, *not* Features.  People don’t buy software because of what it does, they buy it for the positive change it will make in the life.)  If you think “People should buy this because it will make them money, save them time, and get them back to their kids faster”, then you probably have a viable idea.


Another thing I’d look for prior to committing to building anything is a marketing hook — something you can take advantage of to market your product in a time-effective way.  For bingo cards, I knew there were more activities possible than any one company could ever publish, and that gave me hope that I could eventually out-niche the rest of the market.  (This is core idea still drives most of my marketing, four years later.)  Maybe your idea has built-in virality (nice if you can get it — I really envy the Facebook crowd sometimes, although I suppose they probably envy having a customer base which pays money for software), a built-in hook for getting links, or something similar.  If you can’t come up with anything, fix that before you build it.


This should go without saying, but talk to your customers prior to building anything.  People *love* talking about their problems to anyone who will listen to them.  Often they won’t have the first clue about what a solution looks like, but at the very least repeated similar emotional reactions from many people in a market should tell you that the problem is there and real.  After that, it is “just” a matter of marketing.


One note about business longevity: you will likely be involved in this business until you decide to quit.  That means planning for the long term.  Markets which change quickly or where products rot, such as applications for the iPhone (which have a sales window measured in weeks for all but the most popular apps) or games (which have constantly increasing asset quality expectations and strong fad-seeking in mechanics/themes/etc) interact very poorly with the constraints you are under.  I would advise going into those markets only with the utmost caution.


## Get Your Day Job Onboard


Don’t do work on your business at your day job.  DO NOT do work on your business at your day job.  Do NOT do work on your business at your day job.  It is morally and professionally inappropriate, it exposes you to legal liability (particularly if your business ends up successful), and it just causes headaches for all concerned.


As long as you follow that one iron law of doing a part time business, all other obstacles are tractable.  Many engineers these days code outside the clock — for example, contributing to OSS projects.  Tell your boss that you have a hobby which involves programming, that it will not affect your performance at work, and that you want to avoid any misunderstandings about who owns the IP.  You can do something culturally appropriate to actually effect that: it might involve a contract, a memorandum of understanding, or even just a promise that there is no problem.


(Aside: I know many Americans consider the last option shockingly irresponsible.  My ability to prevail over my employer — a major multinational — in a lawsuit is effectively nil.  A contract is just a formalization of a promise.  In Japan, the ongoing relationship with my bosses is the part of the agreement that provides security, not the piece of paper.)


One sweetener you can offer any employer: providing you with discretion to continue with your hobby costs the employer nothing, but it will result in you getting practical experience in technologies and techniques you wouldn’t normally get at the day job, and they can then make use of that expertise without having to send you to expensive training or seminars.  I generated conservatively six figures in business for my day job as a result of things I learned from my “wee little hobby.”  Feel free to promise them the moon on that score — all they have to do in return is not object to your hobby.


Speaking of day jobs: if you know entrepreneurship is in your future, you might pick a job which dovetails nicely with it.  Prior to becoming a salaryman I was employed by a local government agency which had stable salaries and a work-day which ended at 4:30 PM.  Hindsight is 20/20, but that would have been perfect for nuturing a small business on the side.  (What did I do with my free time back when I had so much of it?  I played World of Warcraft.  *sigh* Youth, wasted on the young…)


## Avoid Setting Publicly Visible Deadlines


One thing I did not know four years ago was how dangerous it is to promise things to customers.  For example, suppose a customer asks for a feature which is on the release roadmap.  I might, stupidly, commit to the customer that “Yes, this will be available in the next release, which I hope to have ready on next Monday.”  If the day job then has me spend the rest of the week at the hotel, or I have a family emergency, I will miss that deadline and have one ticked-off customer to deal with.  That is 100% avoidable if you simply *don’t commit to schedules*.  (Also note that committing to a schedule is time debt, by definition.  If you ever say “Yes, I will implement that”, you’ve lost the ability to decide not to implement it if your priorities change.)


One of the most useful things I learned in college was a line from my software engineering professor.  “The only acceptable response to a feature request is: ‘Thank you for your feedback.  I will take it under advisement and consider it for inclusion in a later version of the software.’”  That line actually works.  (There are industries and relationships in which it won’t work — for example, if you’re in a regulated industry and the regulations change, you can’t fob the regulatory authority off with that.  *Don’t be in a regulated industry*.)


Release schedules are not the only type of deadline out there.  Ongoing relationships with freelancers will occasionally have deadline-like characteristics, too.  For example, if you have a pipeline where you generate requests for work and then the freelancer fills it, if you unexpectedly are unable to do your part, the freelancer will be idle.  Thus, you want a bit of scheduling flexibility with them, a store of To Be Done On A Rainy Day requests queued up, or a rethink of your relationship such that *your* brain is not required for them to be able to do *their* job.


## Cultivate Relationships With Effective Freelancers


Dealing with outside talent is one of the most important skills of being a part-time entrepreneur.  It lets you work more hours than you have personally available, it lets you use skills that you don’t possess, and especially [when combined with software you’ve written](https://www.kalzumeus.com/2009/12/31/engineering-your-way-to-marketing-success/) you can do truly tremendous things with with a little bit of elbow grease.  Many folks get started with freelancing from posting to sites like Rentacoder (awesome article about which [here](http://maxkle.in/the-subtleties-in-outsourcing-using-rentacode/)) or Craigslist.  That is fine — everyone has to start somewhere.  However, you’ll quickly find that there is literally a world of people out there who are willing to work for $1.50 an hour… and would be terrifically overpaid at that price.


My suggestion is that, when you find a freelancer who you click with, hold onto them for dear life.  Pay them whatever it takes to keep them happy.  Additionally, since most clients are just as incompetent as most freelancers, don’t be one of the flakes.

- Pay freelancers as agreed, promptly.  I jokingly refer to my payment terms as Net 30 (Minutes), and that ends up being true 90% of the time.
- Provide sufficient direction to complete the task without being overbearing.  (Freelancers with a bit of personal initiative are worth their weight in gold.)
- Don’t schedule things such that freelancers are ever blocking on you or that you are ever blocking on freelancers.  You have all the time in the world if you get things done well in advance of need.  For example, I just got my St. Patrick’s Day wordpress theme done — for *next* year.  If I was getting the [Easter bingo](http://www.easterbingocards.com) site cranked out now, any hiccup would mean it missed my window.  (Technically speaking it would already be too late for SEO purposes, but that is a long discussion.)
- Recurring tasks are a great thing to systemize and outsource.  You can write software to do the painful or boring bits, greatly increasing productivity, and as your freelancers get more experienced at the task you take on less time debt for explanation and review of their work.


Speaking of which, the most successful freelancing relationships are ones where you correct the labor market’s estimation of someone’s value.  (That is the positive way to say “You spend much less on them than you’d pay someone else for the same work *and* they’re happy to get it because you’re the highest paying offer.”)  Much ink has been spilled about how the globalization of labor makes it possible to get work done by folks in low-wage countries.  To the extent that you identify skilled, reliable workers, this is certainly one way to do things, but it is not the only way.  The current economic malaise has left many folks in high-wage countries either unemployed or underemployed.  In addition, the labor markets have huge structural impediments to correctly valuing the expertise of stay-at-home mothers, retirees, and college students.  All of those are potentially good resources for you.


## Understand the Two Types of Time


There are two types of time involved in business: wall clock time and calendar time.


**Wall clock time**: minutes/hours which you spend actually working.


**Calendar time**: days/weeks/months/years where time passes so that something can happen.


We expect the world to be very, very fast, because the Internet is very, very fast, but when dealing with non-Internet processes we are frequently reminded of how slow things are.


Paul Graham [mentions this](http://www.paulgraham.com/really.html) as one of the hard things to learn about startups.  I really like his metaphor for how to deal with it: fork a process to deal with it, then get back to whatever you were doing.  For example, while Google rebuilds its index in a matter of minutes these days (this blog post will be indexed within fifteen minutes of me hitting the post button, guaranteed), getting a new site to decent rankings still takes months of calendar time.  That doesn’t mean you stand around waiting for months — you get your site out and aging as fast as humanly possible, and then start working on other things.  **Get good at task switching** — you’ll be doing it a lot.  (I literally just alt-tabbed to Gmail and squashed a support inquiry.)


You can incorporate calendar time into your planning, too, and since it is essentially free to you (you’re planning on being here in a week, right?) it is often advantageous to do it.  For example, A/B testing requires lots of calendar time but very little wall-clock time: you spend 15 minutes coding up the test and then have to wait a week or two for results.  That works very, very well in a part-time business.  Often, you can get into a rhythm for feedback loops like that.  Do whatever works for you: for me, Saturday typically sees me end my old tests and start new ones.


## Avoid Events, Plan For Processes


There is a temptation to see business as series of disconnected events, but that should probably be avoided.  For example, you might see a dozen emails as a dozen emails, but it is probably just as true that it is six of Email A, 3 of Email B, and three emails with fairly unique issues.  You should probably turn your response to Email A and Email B into some sort of process — address the underlying issue, write your web page copy better, add it to your FAQ, create an auto-text to answer the problem, etc etc.


Similarly, spending your time on things which help your business once is almost always less effective than making improvements which you can keep.  For example, running a sale may boost sales in the short term, but eventually the sale will end and then you cease getting additional advantage from it.  There is a time overhead assorted with running the sale: you have to promote it, create the graphics, code the logic, support customers who missed the sale by 30 minutes but want the price (give it to them, of course), etc etc.  Spend your time on building processes and assets which you get to keep.


Another example: attempting to woo a large blog to post about you may require quite a bit of time in return for one fleeting exposure to a fickle audience.  Instead, spend the time creating a repeatable process for contacting smaller blogs, for example something along the lines of [Balsamiq’s very impressive approach]( https://balsamiq.com/company/how-we-run-our-business/marketing/startup-marketing-advice/).  (Other examples: repeatable piece of linkbait such as the [OKCupid’s series on dating](http://blog.okcupid.com/index.php/2009/10/05/your-race-affects-whether-people-write-you-back/) also works, or a repeatable method of building linkable content, or a repeatable way of convincing customers to tell their friends about you.)


You can also avoid spending hours on incident response if you spend minutes planning your testing and QA procedures to avoid it.  When they fail — and they [will fail](https://www.kalzumeus.com/2010/02/21/i-had-downtime-today-heres-what-im-doing-about-it/) — fix the process which permitted the failure to happen, in addition to just responding to the failure.


## Document.  Everything.


I’m indebted to my day job for teaching me the importance of proper internal documentation.  As weeks stretch into months stretch into years, no matter how good of a memory you have, you will eventually have things fall through the cracks.  Your business is going to produce:

- Commit notes.  Thousands of them.
- Bug reports.
- Feature requests.
- Pre-sales inquiries
- Strategic decisions
- Statistical analyses


… etc, etc.  The exact method for recording these doesn’t matter — what matters is that you will be able to quickly recall necessary information when you need it.


I tend to have short-term storage and long-term storage.  Short term things, like “What do I need to do this week?”, get written down in a notebook that I carry with me at all times.  (I lock it in the drawer when I get to work, but feel no compunction about sketching things on my train ride.)  Things that actually need to get preserved for later reference go into something with a search box.  This blog actually serves as a major portion of my memory, particularly for strategic direction, but I also have SVN logs (with obsessive-compulsive commit notes… often referencing bugs or A/B tests by number), email archives, and the like.  (One habit I picked up at the day job is sending an email when I make a major decision outlining it and asking for feedback.  Note this works just as well even if you’re the only person you send it to — at least you’ll force yourself to verbalize your rationalizations and you can compare your expectations with the results later.)


There are a million-and-one pieces of software that will assist in doing this.  My day job uses Trac, which has nice SVN integration.  I have heard good things about 37Signals’ stuff for project planning/management and also about Fogbugz for bug tracking.  Use whatever works for you.


Note that quality documentation of processes both prevents operator error and makes it possible for you to delegate the process to someone else.  Also, if you have eventual designs on selling this business, comprehensible and comprehensive documentation is going to be a pre-requisite.


## Dealing With The Government


I’ve been pleasantly surprised how little pain I’ve suffered in dealing with the government.  Part of this is because software is such a new industry that we often slide by on regulation — if I ran an actual Italian restaurant instead of the software analogue, I would have to keep health inspectors happy on a regular basis, but there is (thankfully) no one auditing my code quality.  Speak with competent legal advice if you’re not sure, but for the most part the only thing Japan and America want from me is that I pay my taxes on time.


Paying taxes is weeks of hard work really freaking easy.  The typical Italian restaurant has to do lots of bookkeeping involving thousands of sales, most of them involving cash, juggle record-keeping demands for half-dozen employees, and has expenditures ranging from rent to wages to capital improvements to food with a thousand rules about depreciation, etc, to worry about.  By comparison, the typical software business gets half of bookkeeping *for free* (if you can’t tell me to a penny how much your software business has sold this year with a single SQL query… well, I don’t know whether to deride your intelligence or congratulate you on your evident success), we have absurdly high margins so if you forget to expense a few things it won’t kill you, the number of suppliers we deal with is typically much lower, and the vast majority of what we do is amenable to simple cash accounting.


Additionally, your local government almost certainly has a bureau devoted to promoting small businesses.  They are happy to give you pamphlets explaining your legal responsibilities — in fact, sometimes it seems the only thing they do is create ten thousand varieties of pamphlets.  Your local tax office will also fall over backwards telling you how quick and easy it is to pay them more money.


Incorporation?  Incorporate when you have a good reason to.  (I still don’t, but I might do it after I go full-time, largely for purposes of dealing with Immigration.)  If you’re selling B2C software, your number one defense against getting sued is promptly refunding any customer who complains, and that pretty decisively moots the LLC’s (oft-exaggerated) ability to limit your personal liability.  You’ll be personally liable for debts from the business, but since the business is fundable out of your personal petty cash that isn’t the worst thing in the world.  If sales collapsed tomorrow I’d be on the hook for my credit card bill, which runs about $1,200 a month — not a financial catastrophe for an employed professional, particularly when the business generates far more than that in profits well in advance of the bill being due.  Sole proprietorship — i.e. merely declaring “I have a business” — is the most common form of business organization, by far.


## Ask Someone Else About Health Insurance


I’m only putting this here to mention I have no useful information, because I live in a country with national insurance.   That isn’t a veiled political statement — I am not really emotionally attached to either model, I just don’t have useful experience here.  (My impression is that young single businessmen around my age are probably well-served with getting cheap catastrophic coverage.)


## Keep A Routine, When Appropriate


Through sickness, health, and mind-numbing tedium, I’ve woken up every day for the last four years, checked email, gone through the day, checked email, and gone to sleep.  This is the single best guarantee that I would deliver on the promised level of service to customers — almost all questions answered within 24 hours.  There have been many, many weeks where this is literally all I’ve done for the business.


I try to keep creative work — such as writing, coding, or thinking up new tacts for marketing — to a bit of a routine, too, with flexibility to account for days where I’m not mentally capable of pushing forward.  For example, generally I do planning for the week at dinner on Monday and have four hour block to the business on Saturday.  If on Saturday it turns out that I can’t make forward progress on the business, I clock out and go enjoy life.


Routines aren’t limited to the business, either.  They help me incorporate my other priorities — family, friends, church, gym, hobbies — into a schedule that would otherwise descend into total anarchy.  (If you want to see what happens to the things that I don’t prioritize when the day job starts knocking, well, suffice it to say that I was cleaning today and removed 13 pizza boxes from my kitchen table.  I hope to put both cleaning and cooking back in the rotation after separating from the day job.)


## Seek The Advice Of Folks You Trust.  Disregard Some Of It.


One of the major things which pushed me to (a small measure) of success these last four years has been advice from the communities at the [Business of Software](http://discuss.joelonsoftware.com/?biz) boards and [Hacker News](http://news.ycombinator.com) and the writings of folks like Joel Spolsky, Paul Graham, and the 37Signals team.  Much of the advice I received has been invaluable.  I disagree quite strongly with some of it.  When reading advice from me or anyone else, keep in mind that it is a product of particular circumstances and may not be appropriate for your business.  And always, always, always trust the data over me if the data says I’m wrong.  (That’s the easy part.  The hard part is trusting the data when it is overruling *you*.)


I’m thinking of making this first in a series.  If you have topics you’d like me to cover in more detail, please, let me know in the comments.
