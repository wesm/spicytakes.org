---
title: "Software Businesses In 5 Hours A Week: Microconf 2011 Presentation (1 hour)"
date: 2011-06-17
url: https://www.kalzumeus.com/2011/06/17/software-businesses-in-5-hours-a-week-microconf-2010-presentation-1-hour/
slug: software-businesses-in-5-hours-a-week-microconf-2010-presentation-1-hour
word_count: 3188
---


Rob Walling (who wrote a [book on starting software businesses](http://www.startupbook.net) that I enjoyed) and [Mike Taber](http://www.singlefounder.com) produced [Microconf](http://www.microconf.com), a conference for small solo software entrepreneurs.  That sounded right up my alley, and I was extraordinarily happy when asked to speak at it.  The organizers have generously given me permission to post the slides and video of my talk.  (Sidenote: editing videos is going on my Never Doing This Again list.  I should have just thrown a few hundred dollars at someone and saved six hours.  It probably would have ended up better, too.)


If you have an hour free, I recommend the video.  I am told that it was funny, though the genre of humor was very different than my [Business of Software presentation](http://www.businessofsoftware.org/video_10_pmckenzie.aspx).  If you can’t take an hour to watch it, though, you can certainly just read the slides and my commentary below.

**[Software Businesses On 5 Hours A Week](http://www.slideshare.net/patio11/software-businesses-on-5-hours-a-week)**
View more
[presentations](http://www.slideshare.net/)
from
[Patrick McKenzie](http://www.slideshare.net/patio11)
</p>

## How I Ended Up In Central Japan


I have long wrestled with fairly severe self-confidence issues.  (The psychology of entrepreneurship is the major theme of an upcoming post, inspired by a talk I had with [Ramit Sethi](http://www.iwillteachyoutoberich.com), who also spoke at Microconf.)  When I was in college, I knew I wanted to be a software engineer, but I was worried about my job prospects competing with 100,000 engineers graduating every year in China and India.  My family was very big on me getting a nice stable job at a megacorp, and I didn’t think I had the chops for it.  So I played the Venn Diagram game: if I could do one very hard thing plus engineering, the intersection of those two would be only a half dozen people, and I’d be set for life.


Learning languages is very hard, so I went down the list that my university offered, and Japanese jumped out at me.  The US and Japan trade billions upon billions of dollars of high-tech stuff every year.  Virtually no Americans speak Japanese.  Practically no Japanese people are fluent in business-level English.  Bingo, if I spoke Japanese and can do engineering, I thought Microsoft (my favored employer at the time) would have to put me in a nice safe job in the Office group for the rest of my life.  So I doubled majored in the two.


Quick tangent: A major multinational advertising firm with an anomalously high number of PhDs on the payroll recently approached me about being a Product Manager in Japan, so this strategy really does work.  It’s funny, three years ago that would have been my dream job and now it was totally untempting.


Anyhow, after graduating college, I was still not confident in my business Japanese, so I decided to go to Japan, work in a Japanese office, and firm it up.  Did I think I could actually call the VP of the multinational who gave me his card and said “Call for a job when you graduate?”  No, confidence issues.  So instead I applied to an international exchange program, which places mostly English teachers and, crucially, some translators at Japanese governmental and quasi-governmental institutions.  One of them was the prefectural technology incubator in Gifu.  (I’m not comfortable telling you which one, but suffice it to say that *really* narrows it down.)  They took me on as a technical translator, in the expectation that their quickly-growing incubated companies would need technical translation to close big deals with foreign companies and governments.


Gifu is the Kansas of Japan, with more rice and less white people.  I’ve lived here for the last seven years and love Ogaki, my adopted home town, to pieces.  Being a technical translator, however, was not very professionally fulfilling.  Professional ethics require you to translate everything exactly, without elaboration.  I like to think I have something to add to the conversation, so when my contract elapsed in 2007 I switched to being an engineer at a Japanese megacorp.  Prior to doing that, though, I launched Bingo Card Creator.


## From Humblest Beginnings


BCC was originally the hobbiest of hobby projects.  One of my assorted job duties as a heavily-underused technical translator was to help out the prefecture’s 200-strong mailing list of (foreign) English teachers, who didn’t speak Japanese and as a result often had issues with coworkers, landlords, government, and the like to muddle through.  Someone asked the mailing list how to make bingo cards for an activity she had planned for later in the week.  I told her to Google it.  She told me that she had and that Google was showing her solutions which were grossly inadequate to her needs.  So I got permission from my boss and spent the rest of the day putting together what might today be called the Minimum Viable Bingo Card Creator.


It was *terrible:* a Java swing app, distributed as a .jar file, which would accept words in one text-box and, when you hit Print, dump a directory of card0.html … card29.html and ask you to print them from IE because I didn’t know how to actually do that in Java at the time.  But it did actually create bingo cards, and they were of sufficient quality to give to a 7 year old Japanese kid without feeling embarrassed, so I sent it to the mailing list, and went home for the day.  I thought that was the end of it.


The next day, I had 60 emails in my inbox when I got into work.  They were split 50/50 between “THANK YOU!  BEST SOFTWARE EVER!” and “THIS SUCKS!  IT DOESN’T WORK ON MY MACHINE! FIX IT BECAUSE I NEED IT NOW!”


So later in June 2006, when I decided to create a business on the side to try my hand at the SEO/AdWords/etc stuff I had been reading about, bingo jumped out at me as a good topic for software.  I mean, if I could find 60 people who wanted it *in Gifu*, surely there must have been a market back in the US.  So I budgeted $60 (one video game) and one week to rewriting and productizing it (outside the day job this time, naturally), and set myself a goal: some day, after months of work, I wanted to make $200 in sales a month.


Since I had been inspired by other tales of success on the Internet, I started blogging (you’re reading the result, 5 years later) and publishing [my statistics](http://www.bingocardcreator.com/stats/), including [sales](http://www.bingocardcreator.com/stats/sales-by-month).  You can see annotated graphs in the slides, so I won’t put them in this post.


## Early Days: Filling A Hole In The Internet


BCC exceeded $200 in sales in its second month, largely on the strength of two pages I wrote about [Dolch sight words bingo](http://www.bingocardcreator.com/dolch-sight-words-bingo.htm).  (Not an English teacher?  No problem.  Dolch was an English pedagogist who compiled lists of the 220 or so words early English learners need to know on sight.  Teachers know they should teach these but often don’t know which words are on the lists for what year.  I put lists of them online and monetized them with self-ads for the strongly-related bingo activity, on the assumption that almost any teacher wanting to teach them would want a review activity, too.)


This was a good thing, since I had no budget at the time for AdWords.  The success of the content marketing also clued me into one of the core features of the software: writing pre-made word lists that shipped with it, so that teachers didn’t have to type up their own.  So I spent the next year or so in very part-time fashion improving the software, launching new versions, polishing the site, and generally learning more about running a business.  (“Schedule C?  What is that?  Ooooh.”)


## Got Google AdWords To Work


In 2007, I started trying my hand at AdWords.  It was a fistful of fail — I could not seem to get either positive ROI or meaningful volumes for the life of me. A [buddy of mine](http://www.declan-software.com/) from the Business of Software forums advised me to try the Content Network (i.e. ads on sites other than Google.com).  I had turned this off, as prevailing sentiment on the Internet was that the Content Network was a hive of scum and villainy, filled with spammers and MFA (Made For AdSense) sites which sent traffic that did not convert.  But my buddy was sufficiently credible that I trusted him…


… and that ruined my summer.  (His advice ended up turbocharging my business, so I’m retroactively happy for it, but try telling that to me at the time.)  See, every day after coming home from work I would check into AdWords, and every day I would have a new list of spam sites to have to manually ban.  They sent non-converting traffic and I didn’t want to subsidize them.


Towards the end of summer, Google came out with [Conversion Optimizer](http://www.google.com/adwords/conversionoptimizer/).  In brief, it automatically increased your bid on sites/keywords which sent traffic that converted and decreased it on sites/keywords which didn’t.  This meant that non-converting traffic from spam sites essentially got optimized away without me having to manually ban it.  I loved that, and became an early adopter, writing a [pair](https://www.kalzumeus.com/2007/09/25/new-adwords-feature/) of [blog posts](https://www.kalzumeus.com/2007/11/10/conversion-optimizer-adwords-done-right/) on it.


Concurrently with adopting Conversion Optimizer, October rolled around.  Halloween happens at the end of October, and **hundreds of thousands** of teachers look for a Halloween activity to play with class.  (Why Halloween, over every other holiday?  Because it is kid-focused, because kids are in school for it, and because as a largely secular holiday it can’t get public school teachers in trouble.)  This meant that sites with content responsive to Halloween bingo, like about.com (which was a content farm before content farming was cool), suddenly had hundreds of thousands of page views to sell AdSense against.  And who was in the front row of the auction for halloween bingo ad impressions?  Me, because Conversion Optimizer figured out that I was making out like a bandit and aggressively moved to spend my money.


Sentiment on the Internet towards Conversion Optimizer had been primarily negative, but I was killing it with it.  My blog post also ranked #3 for Conversion Optimizer right below two posts on google.com… above much of the official documentation.  I think that was probably what clued the Product Manager into talking to me.  Anyhow, to my total surprise, Google asked to do a [white paper](http://www.google.com/adwords/conversionoptimizer/bingocard.html) about my experience with the product.  That was my proudest professional accomplishment for a while, actually.


## Content Marketing Seems To Be Working Out… Let’s Scale It


So I was doing well for Halloween bingo in spite of not having any page about it (remember — AdWords ads only), and had done even better for Dolch sight words.  If only I could make a page about Halloween bingo, and Thanksgiving bingo, and addition bingo, and any kind of bingo a teacher could possibly want to play.  Then instead of paying Google to lease the traffic, I would get it for free myself, forever.


This struck me as an unachievably huge amount of work while full-time employed, so I decided to partially automate and partially outsource it.  I taught myself Rails and rewrote the website as a Rails application (rather than 100% HTML-written-in-Notepad), then wrote a script that would populate the Cards table by reading in text files.  Each card got its own page on the website, complete with image of the card, downloadable PDF of 8 randomly created cards, and copious oppotunities to download the free trial of my software.


Creating the GIF and PDF was originally very difficult: you had to use BCC, print to a virtual PDF-ing print driver, open the PDF, screencapture it, crop the capture manually, and then send me the words you used, the resulting GIF, and the PDF.  Repeat thirty times over.  My freelancers understandably got bored, so I had someone write a script which would use a particular Windows macroing utility to drive my laptop’s mouse and do the work.  This took about an hour to get through 30 cards, and required my presence if the script broke in the middle (which was “often”), but it still cut production time down by 90%.


This ended up working out scandalously well for me.  See Scalable Content Creation under [Greatest Hits](https://www.kalzumeus.com/greatest-hits/) if you want the story in detail.  (I also did a [video with Andrew Warner and AppSumo](http://www.appsumo.com/hacking-content-creation/) on the topic, if you want it described in a more organized fashion than my blog’s usual stream-of-consciousness approach.)  Eventually, after optimizing the process, I had nearly a thousand pages like this created.


I also have a variety of micro-sites written on exact match domain names, like my favorite, [Halloween bingo cards](http://www.halloweenbingocards.net).  Honestly, they’re not that material to my strategy anymore, but if you want to hear more about them [see the blog](https://www.kalzumeus.com/2008/11/24/christmas-bingo-boards/) from a few years back.


## On Being A Salaryman


Around this time my contract elapsed at the cushy translation job, where I left at 4:00 most days, and I got a job as an engineer at a megacorporation in Nagoya.  No, not that one… not technically, at any rate.  Somewhat to my surprise, the job they offered was as *seishain*,  which means full-time company employee.  The more commonly known coinage for this status is *salaryman*, because the job is designed to take over your life.  And take over my life it did.


I rush to point out that I have no ill-will against my old employers: they treated me fairly, by the standards of Japanese corporations, and I learned a lot at that job.  I had my eyes wide open going into it, too — I just didn’t realize how bad 70 ~ 90 hour work weeks would actually be.


This was intended more as a tangent for the speech, but I did more than a bit of venting in the video, much of it humorous.  See that for the full version.


## Web Applications Are The Bomb


By 2009, I had advanced sufficiently in my Rails and web programming skills that I could re-release BCC as a web application.  That decision roughly doubled sales, largely due to increased conversion rates both to the trial and from trial to purchase.  I strongly, strongly, strongly suggest developers build web applications in preference to desktop apps, for reasons [I have gone into before](https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/).  Or, alternately, see this bingo card:


Web apps: do ‘em.


## Quitting The Day Job


The combination of these and a hundred other smaller improvements ([A/B tests](http://www.bingocardcreator.com/abingo/), etc) eventually got my sales to the point in late 2009 where I could seriously consider quitting the day job.  I went home for Christmas, talked it over with my family, then came back and told my bosses that I was through.  They let me go with a mere four months notice.  (Theoretically, the law only requires two weeks in Japan.  In practice, well, see the video.)


Also at Christmas I had a conversation with Thomas Ptacek at [Matasano](http://www.matasano.com) (conveniently in Chicago, close to my family), who opened my eyes regarding consulting.  I owe Thomas a lot for that, because consulting turned quitting from a dicey proposition (a dip in sales could have imperiled my ability to fly home or expand the business, to say nothing of making rent) into a total no-brainer.  Last year I made a bit more from BCC than consulting.  This year I’ll make quite a bit more from consulting than BCC.  The goal is still building a software product business (my current focus on that score is [Appointment Reminder](http://www.appointmentreminder.org)), but as of late the caliber of clients, work, and paychecks for consulting has been so attractive that I have been unable to say no.


## Tactical Advice


The last half of the presentation was tactical advice on running a small business in one’s spare time — over the first 4 years of doing BCC, I averaged about 5 hours a week on it.  (This last year, even less: it is in maintenance mode.  I send out customer support emails and that is about it.)


The five quick hits:


### Charge more money.


Most engineers severely undercharge for their products.  This is particularly true for products which are aimed at businesses — almost all SaaS firms find that they make huge portions of their revenue from the topmost plan which is bought by people spending other people’s money, but instead of optimizing for this we optimize for charging “fair” prices as determined by other software developers who won’t pay for the service anyway.  This is borked.  Charge more.


### Make it a web app.


Covered above.


### Put more of your iceberg above the water line.


Businesses create value with almost everything they do.  The lion’s share of the value is, like an iceberg, below the waterline: it cannot be seen from anywhere outside the business.  Create more value than you capture, certainly, but **get the credit** for doing so, both from Google and from everybody else.  This means biasing your business to producing value in a public manner.  Did you write software not core to  your line of business?  Great, OSS it.  **Get the credit**.  Have you learned something novel about your customers or industry?  Write about it.  **Get the credit**.  Are your business’ processes worthy of emulation?  Spread what you know.  **Get the credit**.


37Signals is amazing at this.  You can do it, too.


### Get good at SEO.


I talk about this extensively on my blog.  In a nutshell:

1. You need more links.  Create ways to justify people who aren’t in a commercial relationship with you linking to you anyway.  My favorite way for doing this is getting the credit for things you do, as described above.
2. Create quality content at scale which solves problems for people in your niche.  See earlier discussion on Scalable Content Creation.


### Optimize Everything


I’ve blogged extensively on A/B testing and funnel optimization (see [Greatest Hits](https://www.kalzumeus.com/greatest-hits/)).  The big take away is, as [Steve Pavlina said](http://www.sodaware.net/dev/articles/shareware-amateurs-vs-shareware-professionals.htm), all factors in the success of a software business are multiplicative.  If you increase conversions to the trial by 10% and conversions to sale by 10%, your sales go up by 21%, because 1.1 * 1.1 = 1.21.  This is awesomely powerful, particularly for businesses which don’t require hockey-stick trajectories.  You can hill-climb your way to very, very nice places in life for a one-man shop or small company.  (I mean, what real company offers 70% raises per year just for doing an A/B test every week and collecting a +5% improvement on one out of every four?)


## Outsource / Automate / Eliminate To Actually Do It In 5 Hours A Week


I have previously written about Outsource / Automate / Eliminate extensively on my blog, so see [here](https://www.kalzumeus.com/2009/10/04/work-smarter-not-harder/) and [here](https://www.kalzumeus.com/2010/03/20/running-a-software-business-on-5-hours-a-week/).


## Comments?


I’d love hearing what you thought of the presentation.  I sincerely enjoy talking to people about this and other topics, so if there is a topic you’d like to hear more (or less!) on in the future, tell me and I’ll try to work it in to future presentations.  I never deliver the same one twice.
