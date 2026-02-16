---
title: "DevOps vs SRE: delayed coverage of the dumbest war"
date: 2016-06-30
url: https://charity.wtf/2016/06/30/devops-vs-sre-delayed-coverage-of-the-dumbest-war/
word_count: 1997
---


Last week was the [West Coast Velocity](http://conferences.oreilly.com/velocity/devops-web-performance-ca) conference.  I had a terrific time — I think it’s the

best Velocity I’ve been to yet.  I also slipped in quite late, the evening before last, to catch Gareth’s session on DevOps vs SRE.


I *had *to catch it, because [Gareth Rushgrove](http://www.morethanseven.net/) (of [DevOps Weekly](http://www.devopsweekly.com/) glory) was taunting [@lusis](http://twitter.com/lusis) and me about it on the Internet.


my plan for this @velocityconf talk is increasingly to make [@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) and [@lusis](https://twitter.com/lusis?ref_src=twsrc%5Etfw) blush— Gareth Rushgrove (@garethr) [June 16, 2016](https://twitter.com/garethr/status/743402475340849152?ref_src=twsrc%5Etfw)


And it was worth it!   Holy crap, this was such a fun barnburner of a talk, with Gareth schizophrenically arguing both for and against the key premise of the talk, which was about “[Google Infrastructure for Everyone Else (GIFEE)](http://conferences.oreilly.com/velocity/devops-web-performance-ca/public/schedule/detail/49945)” and whether SRE is a) the highest, noblest goal that we should all aspire towards, or b) mostly irrelevant to anyone outside the Google confines.


Which Gareth won?  Check out the slides and judge for yourself.  🙃


At some point in his talk, though, Gareth tossed out something like “Charity probably already has a blog post on this drafted up somewhere.”  And I suddenly remembered **“Fuck!  I DO!”**  it’s been sitting in my Drafts for months god dammit.


So this is actually a thing I dashed off back in April, after [CraftConf](http://craft-conf.com/).  Somebody asked me for my opinion on the internet — always a dangerous proposition — and I went off on a bit of a rant about the differences and similarities between DevOps and SRE, as philosophies and practices.


Time passed and I forgot about it, and then decided it was too stale.  I mean who really wants to read a rehash of someone’s tweetstorm from two months ago?


Well Gareth, apparently.


Anyway: enjoy.


---


### SRE vs DevOps: TWO PHILOSOPHIES ENTER, BOTH ARE PHENOMENALLY SUCCESSFUL AND MUTUALLY DUBIOUS OF ONE ANOTHER


---


So in case you haven’t noticed, [Google](http://google.com) recently published a book about [Site Reliability Engineering: How Google Runs Production Systems](https://www.amazon.com/Site-Reliability-Engineering-Production-Systems/dp/149192912X).  It contains some really terrific wisdom on how to scale both systems and orgs.  It contains chapters written by dear friends of mine.  It’s a great book, and you should buy it and read it!


It also has some really fucking obnoxious blurbs.  Things like about how “ONLY GOOGLE COULD HAVE DONE THIS”, and an whiff of snobbery throughout the book as though they actually believe this (which is far worse if true).


You can’t really blame the poor blurb’ers, but you can certainly look askance at a massive systems engineering org when it seems as though they’ve never heard of DevOps, or considered how it relates to SRE practices, and may even be completely unaware of what the rest of the industry has been up to for the past 10-plus years.  It’s just a little weird.


So here, for the record, is what I said about it.


1) a lot of the philosophical volleying between devops / SRE comes down to a failure to recognize the overwhelming power of context.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726755945523609600?ref_src=twsrc%5Etfw)


[Google](http://google.com) is a great company with lots of terrific engineers, but you can only say they are THE


The Google SRE Bible


BEST at what they do if you’re defining what they do tautologically, i.e. “they are the best at making Google run.”  Etsyans are THE BEST at running [Etsy](http://etsy.com), Chefs are THE BEST at building [Chef](http://chef.io), because … that’s what they do with their lives.


Context is everything here.  People who are THE BEST at Googling often flail and flame out in early startups, and vice versa.  People who are THE BEST at early-stage startup engineering are rarely as happy or impactful at large, lumbering, more bureaucratic companies like Google.  People who can operate equally well and be equally happy at startups and behemoths are fairly rare.


And large companies tend to get snobby and forget this.  They stop hiring for unique strengths and start hiring for lack of weaknesses or “Excellence in Whiteboard Coding Techniques,” and congratulate themselves alot about being The Best.  This becomes harmful when it translates into to less innovation, abysmal diversity numbers, and a slow but inexorable drift into dinosaurdom.


2) operations engineering is a specialized skill set *at large scale* or *on hard ops problems*.  many -- most? companies don't have those.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756018605162497?ref_src=twsrc%5Etfw)


Everybody thinks their problems are hard, but to a seasoned engineer, most startup problems are not technically all that hard.  They’re tedious, and they are infinite, but anyone can figure this shit out.  The hard stuff is the rest of it: feverish pace, the need to reevaluate and reprioritize and reorient constantly, the total responsibility, the terror and uncertainty of trying to find product/market fit and perform ten jobs at once and personally deliver to your promises to your customers.


At a large company, most of **the hardest problems are bureaucratic**.  You have to come to terms with being a very tiny cog in a very large wheel where the org has a huge vested interest in literally making you as replicable and replaceable as possible.  The pace is excruciatingly slow if you’re used to a startup.  The autonony is … well, did I mention the politics?  If you want autonomy, you have to master the politics.


3) the outcomes associated with operations (reliability, scalability, operability) are the responsibility of *everyone* from support to CEO.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756107516055552?ref_src=twsrc%5Etfw)


Everyone.  **Operational excellence is *everyone’s* job**.  Dude, if you have a candidate come in and they’re a jerk to your office manager or your cleaning person, don’t fucking hire that person because having jerks on  your team is an operational risk (not to mention, you know, like moral issues and stuff).


But the more engineering-focused your role is, the more direct your impact will be on operational outcomes.


4) therefore, the more literate you are with operational skills, the more effective and powerful you can be -- esp as a software engineer.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756270619897856?ref_src=twsrc%5Etfw)


As a software engineer, developing strong ops chops makes you powerful.  It makes you better at debugging and instrumentation, building resiliency and observability into your own systems and interdependent systems, and building systems that other people can come along and understand and maintain long after you’re gone.


As an operations engineer, those skills are already your bread and butter.  You can increase your power in other ways, like by leveling up at software engineering skills like test coverage and automation, or DBA stuff like query optimization and storage engine internals, or by helping the other teams around you level up on *their* skills (**communication and persuasion are chronically underrecognized** as core operations engineering skills).


5) specialization is not a bad thing. specialization is how we scale and do capitalism! the problem is when this becomes compartmentalizing.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756568772042752?ref_src=twsrc%5Etfw)


This doesn’t mean that everyone can or should be able to do *everything*.  (I can’t even SAY the words “full stack engineer” without rolling my eyes.)  Generalists are awesome!  But past a certain inflection point, specialization is the only way an org can scale.


It’s the only way you make room for those engineering archetypes who only want to dive deep, or who really really love refactoring, or who will save the world then disappear for weeks.  Those engineers can be incredibly valuable as part of a team … but they are most valuable in a large org where you have enough generalists to keep the oars rowing along in the meantime.


6) so: Google SRE has an incredibly powerful set of best practices, that enable them to run the largest site in the world incredibly well.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756663831744512?ref_src=twsrc%5Etfw)


So, back to Google.  They’ve done, ahem, rather  well for themselves.  Made shitbuckets of money, pushed the boundaries of tech, service hardly ever goes down.  They have operational demands that most of us never have seen and never will, and their engineers are definitely to be applauded for doing a lot of hard technical and cultural labor to get there.


So why did this SRE book ruffle a few [feathers](http://blog.lusis.org/blog/2016/04/17/review-site-reliability-engineering/)?


7) we can learn a lot of things from google SRE.  but if you just blindly apply them to your org you will fuck your org up, because context.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756762074910720?ref_src=twsrc%5Etfw)


Mostly because it comes off a little tone deaf in places.  I’m not *personally* pissed off by

the google SRE book, actually, just a little bemused at how legitimately unaware they seem to be about … anything else that the industry has been doing over the past 10 years, in terms of cultural transformation, turning sysadmins into better engineers, sharing on-call rotations, developing processes around empathy and cross-functionality, engineering best practices, etc.


DevOps for the rest of us


**If you try and just apply Google SRE principles to your own org** according to their prescriptive model, you’re gonna be in for a really, really bad time.


However, it happens that [Jen Davis](http://twitter.com/sigje) and [Katherine Daniels](http://twitter.com/beerops) just published a book called [Effective DevOps](https://www.amazon.com/Effective-DevOps-Building-Collaboration-Affinity/dp/1491926309), which covers a lot of the same ground with a much more varied and inclusive approach.  And one of the things they return to over and over again is the power of context, and how one-size-fits-all solutions simply don’t exist, just like unisex OSFA t-shirts are a dirty fucking lie.


Google insularity is … a thing.  On the one hand it’s great that they’re opening up a bit! On the other hand it’s a little bit like when somebody barges onto a mailing list and starts spouting without skimming any of the archives.  And don’t even get me started on what happens when you hire long, longterm ex-Googlers back into to the real world.


So, *so* many of us have had this experience of hiring ex-Googlers who automatically assume that **the way Google does a thing is CORRECT, **not just contextually appropriate**.**   Not just right for Google, but right for everyone, always.  Which is just obviously untrue.  But the reassimilation process can be quite long and exhausting when the Kool-Aid is so strong.


8) DevOps as a philosophy is much more sensitive to context than SRE philosophy, because it grew from a broader collaborative base.— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726756998201663489?ref_src=twsrc%5Etfw)


Because yeah, this is a conversation and a transformation that the industry has been having for a long time now.  **Compared with the SRE manifesto, the DevOps philosophy is much more crowd-sourced, more flexible, and adaptable** to organizations of all stages of developments, with all different requirements and key business differentiators, because it’s benefited from loud, mouthy contributors who aren’t all working in the same bubble all along.


And it’s like Google isn’t even aware this was happening, which is weird.


9) that's it, basically all i'm saying is "all blanket statements are false" including probably this one 🙂 [#devops](https://twitter.com/hashtag/devops?src=hash&ref_src=twsrc%5Etfw) [#sre](https://twitter.com/hashtag/sre?src=hash&ref_src=twsrc%5Etfw)— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726757245661356032?ref_src=twsrc%5Etfw)


Orrrrrr, maybe I’m just a wee bit annoyed that I’ve been drawn into this position of having to defend “DevOps”, after many excellent years spent being grumpy about the word and the 10000010101 ways it is used and abused.


(Tell me again about your “DevOps Engineering Team”, I dare you.)


(^^ thanks to [@kellan](https://twitter.com/kellan?ref_src=twsrc%5Etfw) and others who particularly influenced/clarified my thinking around #8, the crowdsourcing of devops)— Charity Majors (@mipsytipsy) [May 1, 2016](https://twitter.com/mipsytipsy/status/726759770955354112?ref_src=twsrc%5Etfw)


P.S. I highly encourage you to go read the epic hours-long rant by [@matthiasr](http://twitter.com/matthiasr) that kicked off the whole thing.  some of which I definitely endorse and some of which not, but I think we could go drink whiskey and yell about this for a week or two easy breezy  <3


[https://twitter.com/matthiasr/status/726703064799961088](https://twitter.com/matthiasr/status/726703064799961088)


Anyway what the fuck do I know, I’ve never worked in the Google lair, so maybe I am just under-equipped to grasp the true glory, majesty and superiority of their achievements over us all.


Or maybe they should go read Katherine and Jen’s book and interact with the “UnGoogled” once in a while.  ☺️
