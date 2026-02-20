---
title: "Engineering Your Way To Marketing Success"
date: 2009-12-31
url: https://www.kalzumeus.com/2009/12/31/engineering-your-way-to-marketing-success/
slug: engineering-your-way-to-marketing-success
word_count: 3136
---


//


I visited Thomas Ptacek and the gang at Matasano (who are developing a [firewall management](http://runplaybook.com/) product) over Christmas break and had a very productive discussion about marketing.  One of the things Thomas mentioned was that I should probably blog out how you can use engineering resources to improve your marketing.


## In Which I Have A Revelation


Have you ever been talking to someone and had them crystallize an idea you’ve been fumbling around about but never seem to put into words?  That was what I felt like when Thomas mentioned the engineering-to-marketing conversion: the lightbulb went off.  This is what I’ve been doing so much of the last few years, with automated scalable approaches to SEO, A/B testing the living daylights out of my site, optimizing user interactions, tracking tracking tracking, implementing Mailchimp APIs, etc etc.  It is all engineering means to marketing ends: make your customers happy, get your name out there, sell more stuff.


And really, we don’t do nearly enough of it in our industry.  We’re sitting on top of more software and programmer brain juice than Saudi Arabia has oil, and when we deploy it to maximize our sales… we build **marginal features** that *nobody has asked for* and that *nobody will see*.


I am as guilty of that as anybody else: version 3.0 of the desktop [Bingo Card Creator](http://www.bingocardcreator.com) included a prodigious amount of time spent on integrating a bit of a client/server application into it.  I thought, hey, customers empirically ask me all the time how to get access to the same cards on their home and school computers, so allowing them to save it to the server (wait, I have to be buzzword-compliant) **cloud** would solve a problem for them.


It turns out that those customers with the problem had already either figured out how to email files to themselves or were part of the mass exodus to the web version of my program.  The client/server features of BCC got terrifically underused: exactly 22 of my customers have used them.  That works out to be about 1% of the customers I’ve added in the last year.  By way of comparison, adding color to my bingo cards scratched off one of my Top 3 user feature requests, took me a tenth the time, and gets used by about 8.5% of customers.


As if that weren’t painful enough, not a single customer was enticed by the client/server features being pay-only to purchase BCC to get them.  (If you’re wondering “Hmm that sounds like a curiously specific claim for someone who is not telepathic” tie a mental string around your finger to read the forthcoming part about analytics carefully.)


## Features Do Not Sell Your Software


For the last three years and change I’ve been hanging out on the Business of Software discussion boards and have advised more programmers on websites than I have friends.  You can tell when someone is on version 1.0 of their website: they have The Traditional Shareware Website with six pages listed in the horizontal navigation, featuring Trial, Purchase, Features, Screenshots, Support, and About Us, and the main content on their front page and the Features page is a list of features.


The first advice we always give them is strike Features and replace with Benefits because **benefits, not features, sell software**.  (I have heard that this is not true in some markets comprising of very technical experts who are looking for exactly the tool to fit their problem and, if you sell to these people, hat’s off to you and please don’t ever take my advice *on anything*.  Well, OK, one little thing: you may not actually be selling to that customer, regardless of what you think, so go get some data.)


A quick sidenote for people who have not repeated the benefits-not-features mantra on every sunrise for the last several years: features are things that your software does.  Objectively speaking, Microsoft Powerpoint reads PPT files and lets you animate bullet points.  Benefits are the perceived improvements in the user’s life that will result from purchasing your software.  Subjectively speaking, customers of Microsoft Powerpoint buy it because it will let them close the deal, please their bosses, and get promoted.


Closing the deal has nothing to do with the internal structures of PPT files.  It answers a human need for the customer.  You could sell Powerpoint to a tribe of cavemen of spear-hunting lions on the savanna.

- Ogg see lion.
- Ogg poke lion with sharp pointy bits.
- Tribe eat lion.
- Ogg get to synergize with Ogga.


## Marketers Get It.  Engineers Don’t.


I have a bit of the tribal programmers’ disdain for marketing, but marketers *get* this concept.  You’ll very rarely (God willing) have people in Marketing obsessing about features because they understand that benefits bring home the bacon.  Sadly, engineers typically work on features, features, features, and more features, when we could do so much more productive things with our time.


For example, when Marketing says “This software should really make the user feel like they just killed an effing lion!”, they’ll typically have, well, no clue whether it actually does or not.  Nobody in the organization does, which is when the problem gets kicked to Management, and we all know that is where interesting questions go to die and, if they were wicked in life, get reborn as meetings.


Your mission as an engineer is to stop thinking the job is building features and start thinking that the job is building systems to answer interesting questions like that.  For example, you could pretty trivially put an item on the sidebar of the software saying “Do you feel like you just killed an effing lion?  (Thumbs up)  (Thumbs down)”, and very quickly you’d have actual data on whether the software is delivering on the promise of visceral feline slaughtering action.


## Measuring Vicarious Lion Slaying As A Process


Of course, engineers are expensive and building a bunch of one-off “Do you feel like you just killed a lion?” quizzes is unlikely to result in you covering your desired hourly salary.  Instead, you should be thinking of *building tools and processes* — give people the resources they need to ask questions like “Do you feel like you just killed a lion?” and make it so brain-dead easy and so ingrained in the culture that if somebody asked “I wonder if users prefer gazelles to lions” didn’t immediately start designing an experiment it would result in chatter about them at the water cooler.


This notion of tools and processes to use engineering as a force multiplier for everything else you do is the key to decoupling productivity from hours worked.  This is a handy feature to have for startups and small businesses.


For example, I’m a one-man shop with occasional help from freelancers, and virtually by definition I’m the most qualified man alive to write content for my website.  However, writing content for my website is a poor use of my time. While it is quite profitable for me, it is much more efficient to build a system to let somebody else do it.  This frees me up to build more force multipliers rather than grind out 757 bingo activities with 28,761 words of content about them.  (That is, incidentally, about as many as a young-adult novel.  The chief difference is that I pay more.)


## Enough With The Lions.  Give Me Actual Things I Could Build Today.


## **A/B testing that anybody can use**.  I hate to harp on A/B testing so much since it is just one arrow in the quiver and I would hate if it blinded anybody (including myself) to other productive uses of their time.  That being said, in terms of dollars gained per hour invested, it is really, really hard to beat.  You need to make it brain-dead easy to that whoever does your website and, ideally, whoever is developing the application can quickly iterate through text, button designs, and workflows to find what works for you.  Feel free to crib design points from [A/Bingo](http://www.bingocardcreator.com/abingo), my OSS Rails testing library.


## **Scalable content generation**.  SEO is sort of my first love in marketing, probably because of the obvious potential for automating it.  Essentially nobody hand writes every page on their website these days, which is A Good Thing because your CMS of choice will make it much less painful and greatly improve the quality of the output.


## If you take that to the next step and figure out how to inject content into the CMS without having you personally type it into the HTML form area, you can fluff up your website and collect an awful lot of long-tail search traffic without overly distracting you from the business of running your business.  For example, Demand Media has creating vast oceans of garbage [down to a science](http://www.wired.com/magazine/2009/10/ff_demandmedia/).  With a bit of creativity, you can use similar techniques (freelancers available as a utility, algorithmic discovery of topics to write about, and automating the quality control) and combine them with existing data sources to actually create value in your niche.


For example, a quick script I wrote up in five minutes to dump the most commonly used words on bingo cards that are not used by a bingo card I have available reported that more than 50 people in December independently typed these into their cards: Star of China, darjeeling, genmaicha, jasmine.  This taught me something I had no clue of: there is a group of people in the world who really want to play Tea Bingo.  With a little more packaging my ad hoc Ruby script can be incorporated directly into the interface for my freelancers.  Then, they could just take a gander at the list of words at the top and use them for inspiration for new writing assignments.


**Automated Error Detection/Correction**. I was so amused by the popularity of Tea Bingo I checked to see if I already had a tea-related activity and discovered, much to my surprise, that [I did](http://www.bingocardcreator.com/bingo-cards/health-foods/types-of-tea).  A handful of boring technical problems resulted in it not getting spidered properly by Google.  (Typically large numbers of customers typing the same activity into the program, rather than starting from one I’ve provided for them, indicates that I don’t have anything responsive to their needs or that they can’t find it.)  I’ve since fixed those problems, and am now contemplating how I can have the computer check this for me in an automated manner so that I never have to expend effort on it again.


There are probably bugs in your own marketing/advertising/etc systems which are leaking a percent here and a percent there of prospects.  Since improvements in many things we do are multiplicative, a percent here and a percent there is worth *real money* if you can recover them.  Consider automating the process of detecting and addressing these things, so it isn’t merely an ad hoc task you do when it is brought to your attention.  (Or, more often, that you don’t do, because it is boring.  I’m *quite* guilty of that.)


**Write your own CMS**.  I would have totally disagreed with this advice up until last week or so, but Thomas convinced me: writing a single-purpose CMS is pretty much the new Hello World for modern web frameworks (heck, it *is* the official Rails demo), and with a man-week or two you can make something much more productive for your purposes than using, e.g., WordPress.  (Though if you can do whatever functionality you need as a WordPress plugin, I’d still be inclined to suggest that.  No need to reinvent the wheel for basic CRUD operations on textual content, or HTML parsing.)


**Lifecycle customer contact**.  One of my big realizations in 2009 was that I was avoiding sending customers emails mostly because I hate receiving emails, and since I am not a forty-something schoolmarm with two kids, my opinion does not count.  So I signed up with [MailChimp](http://www.mailchimp.com), spent three hours incorporating their API into my site, and started sending customers what I call “lifecycle” emails: thanks for signing up, wait a day, you signed up yesterday here’s some stuff you can do, wait a week, hey remember us by the way here’s advanced features.


This is *stupidly* cost effective relative to finding new prospects.  (It costs me a penny to send an existing trial user an email but about a quarter to recruit a new trial user via AdWords.)  Since 97.6% or so of trial users aren’t buying, scraping back a mere fraction of the waste generates great returns for me, and it is incredibly scalable.  (I write the API integration once and test variations on the emails periodically, they get sent to thousands of people without my intervention, money hats all around.)


That is, incidentally, a pretty brain-dead way to do things: with a little more work, I could e.g. send emails only to customers who weren’t active on the site, or vary the email contents with respect to how active or how sophisticated a user appeared to be, etc.  These are both things I intend to try out in 2010.


Similarly, you can create scalable systems to have your users do retention-improving activities for you.  By far the most brilliant implementation I’ve ever seen of this is on Facebook.  If you look to the top right of your main Facebook page right now, you’ll see “Suggestions” where Facebook tells you to add somebody as a friend or reconnect with someone on Facebook.  I will bet you a dollar that anyone who they suggest adding has few friends and anyone they suggest reconnecting with has not logged in recently.  Go check right now, I’ll wait.


Pretty amazing, right?  That is a few hours of engineer time, but it is going to get ***amazing*** increases in retention for Facebook (a key marketing goal) because it leverages the spontaneous-looking social pressure of a person’s own friends to keep them in the service.  And no Facebook engineer or marketer has to touch that system again, except trivially to test improvements to the textual calls to action.  *You could have done this,* or something which is similar for your niche or service.


**Automatically generating advertising creatives.** If you can create content for your website in a scalable fashion, why do you still have highly paid artisans fashioning exquisite one-off works of art for your landing pages again?  Generate a couple hundred, throw traffic at them, see what works and iterate.  If your analytics are sophisticated enough to track conversions back to whatever creative someone saw prior to signup (hint: this isn’t really all that hard but it also isn’t out-of-the-box behavior), you can quickly identify what works and what doesn’t.  Better yet, you can have a computer quickly identify what works and what doesn’t, so that you don’t have to worry about it.


I did this by repurposing the same content I use for my website and slotting it into a landing page template, which gives me about 750 distinct landing pages to work with.  If I took it to the next level and made variations on that template, I’d have thousands available for very little extra cost.  After that you just design a strategy for splitting traffic coming to them and Bob’s your uncle.


Don’t do what I do, but I just split half of my incoming traffic into a the best landing page I’ve handwritten and half into the landing page my system thinks is best.  (Check out how complicated the logic is: “Send people to the landing page corresponding to the most popular content on the site this week.”  This tends to select for holiday bingo in the runup to holidays and my most popular generic activity — currently baby shower bingo — in dull times.)


This should be the point where I tell you “My system beats the stuffing out of me, here are the numbers to prove it” but I actually don’t have the numbers handy, because I apparently had more important things to do with an hour of my time back in September than making a few thousand dollars.  Oh, that’s right, I was busy implementing the client/server feature.  Anyhow, forensic evaluation of my conversion rates for all my AdWords suggests that the 50/50 handwritten/algorithmic mix converts better than my previous 100% handwritten mix for the same landing page, so I’m betting that the system does indeed trounce my intuitions, but that is itself an intuition only marginally supported with data.  Let me get back to you on that in a few months.


**Remove friction in your processes**.  Another hat tip to Thomas for this idea.  One of the key insights to increasing productivity is changing things you do from disconnected tasks to processes.


This one idea explains a huge amount of why Toyota ran roughshod over Detroit, and has been discussed so often in the business literature I’d forgive you if you thought it was false.  Stopped clocks are right twice a day, and the hype about Toyota management you’ll find in your Business Books section is based on reality.


One of the corollaries to this notion is that processes which include steps that are boring, annoying, or tedious tend to fail to get performed.  For example, if anything you do for your business includes boring manual processing of data which you (consciously or otherwise) consider an insult to your intelligence, you probably will fail to do it despite the process being designed to be executed, e.g., weekly.  This is an example of *friction* in the process, and computers are really good at eliminating it.  You can either automate the boring bits or automate their assignment to someone more qualified than you to do them (i.e. freelancers), then automate the quality control, and then automate the notification to you that the raw data has been massaged and you can now continue with the work that actually matters.


There are literally infinite opportunities for this in your business.  Eliminate the friction in content creation by creating your own CMS or re-using existing data sources, as suggested above.  Eliminate the friction in testing by writing automatically executable tests.  Eliminate the friction in bookkeeping by having the computer do it for you.  Eliminate the friction in using your APIs by redesigning or wrapping them such that the common cases take no work at all.  etc, etc.


## Try It.  You’ll Like It.


Hopefully the above list got the juices flowing on how you can do a bit of programming to improve the marketing in your business.  I’m also going to be exploring the topic quite a bit in the New Year, so stay tuned to the blog if you’re interested in it.


**Credits**: The beautiful lightbulb was lightly edited from a Creative Commons licensed work available through [Flickr](http://www.flickr.com/photos/johnmarchan/3877166306/).
