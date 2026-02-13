---
title: "Set Your Priorities"
date: 2005-10-12
url: https://www.joelonsoftware.com/2005/10/12/set-your-priorities/
word_count: 2678
---


It was getting time to stop futzing around with FogBugz 4.0 and start working on 5.0. We just shipped a big service pack, fixing a zillion tiny little bugs that nobody would ever come across (and introducing a couple of new tiny little bugs that nobody will ever come across) and it was time to start adding some gen-yoo-ine new features.


By the time we were ready to start development, we had enough ideas for improvement to occupy 1700 programmers for a few decades. Unfortunately, all we have is three programmers, and we wanted to be shipping next fall, so there had to be some prioritization.


Before I tell you how we prioritized our list of features, let me tell you two ways *not* to do it.


Number one. If you ever find yourself implementing a feature simply because it has been promised to one customer, RED DANGER LIGHTS should be going off in your head. If you’re doing things for one customer, you’ve either got a loose cannon sales person, or you’re slipping dangerously down the slope towards consultingware. And there’s nothing wrong with consultingware; it’s a very comfortable slope to slip down, but it’s just not as profitable as shrinkwrap software.


Shrinkwrap is the take-it-or-leave it model of software development. You develop software, wrap it in plastic, and customers either buy it, or they don’t. They don’t offer to buy it if you implement just one more feature. They don’t call you up and negotiate features. You can’t call up Microsoft and tell them, “Hey, I love that BAHTTEXT function you have in Excel for spelling out numbers in Thai, but I could really use an equivalent function for English. I’ll buy Excel if you implement that function.” Because if you did call up Microsoft here is what they would say to you:


“Thank you for calling Microsoft. If you are calling with a designated 4-digit advertisement code, press 1. For technical support on all Microsoft products, press 2. For Microsoft presales product licensing or program information, press 3. If you know the person at Microsoft you wish to speak to, press 4. To repeat, press Star.”


Notice? None of the choices was, “To negotiate what features need to be added to our products before you’ll buy them, press 5.”


Custom development is that murky world where a customer tells you what to build, and you say, “are you sure?” and they say yes, and you make an absolutely beautiful spec, and say, “is this what you want?” and they say yes, and you make them sign the spec in indelible ink, nay, *blood*, and they do, and then you build that thing they signed off on, promptly, precisely and exactly, and they see it and they are horrified and shocked, and you spend the rest of the week reading up on whether your E&O insurance is going to cover the legal fees for the lawsuit you’ve gotten yourself into or merely the settlement cost. Or, if you’re really lucky, the customer will smile wanly and put your code in a drawer and never use it again and never call you back.


Somewhere in the middle is consultingware, where you pretend to be doing shrinkwrap while really doing custom development. Here’s how consultingware works:

1. You’re working as a wage-slave writing code for a shoe company, and
2. the company needs shoe-shining software, so
3. you develop shoe-shining software in VB 3.0 using bits and pieces of JavaScript, Franz Lisp, and a FileMaker database running on an old Mac connected over the network using AppleScript, then
4. everyone thinks it’s the cat’s whiskers, so, always having dreamed of starting your own software company and maybe being Bill Gates or perhaps even just Larry Ellison
5. you buy the rights to ShoeShiner 1.0 from your old company and get VC to start your own company, ShoeShiner LLC, marketing shoe-shining software, but
6. none of your beta testers can get it to work because of the obscure dependencies on AppleScript and the hardcoded IP addresses in the source code, so it takes a month to install at each client site, and
7. you have trouble getting clients, because your product is so expensive because of all the installation costs, including the vintage Macintosh IIci running System 7 which they have to buy on ebay from computer museums, so your VCs start to get really nervous,
8. putting pressure on the sales guys,
9. who find out that one of your potential customers doesn’t need a shoe-shining thing but he could really use trousers-pressing software, and
10. the sales guy, being a sales guy, sells him $100K worth of trousers-pressing software,
11. and now you spend 6 months writing a one-off “trousers-pressing module” for this client, which
12. no other client will ever need, thus, effectively,
13. for all intents and purposes you’ve just spent a year raising VC so that you could work as a wage-slave writing code for a trouser company; GOTO 1.


Sparky, I’m gonna have to strongly recommend clinging as strongly as possible to the shrinkwrap side of the equation. That’s because shrinkwrap has no marginal costs for each additional customer, so you can essentially sell the same thing over and over again and make a lot more profit. Not only that, but you can lower the price, because you can spread your development costs out over a lot more customers, and lowering the price *gets you more customers* because more people will suddenly find your now-cheaper software worthwhile, and life is good and all is sweet.


Thus. If you ever find yourself implementing a feature simply because it has been promised to a customer, you’re drifting over to the land of consultingware and custom development, which is a fine world to operate in if that’s what you like, but it just doesn’t have the profit potential of off-the-shelf commercial software.


Now, I’m not saying you shouldn’t listen to your customers. I for one think that it’s about time Microsoft actually implemented a version of the BAHTTEXT function for those of us who haven’t yet joined the global economy and learned Thai and who still write checks using other currencies. And in fact if you want to tell yourself that the best way to allocate your development resources is effectively to let your biggest customers “bid” on features, well, you can do that too, although you’ll soon find that the kind of features that big, rich customers want are not the same as the kind of features that the mass market wants, and that feature you put in to handle Baht currency is not really helping you sell Excel to health spas in Scottsdale, Arizona, and in fact what you’re really doing is letting your sales force pimp out your developers with the sole goal of maximizing their personal commissions.


The path to being Bill Gates, this is not.


Now, let me tell you the second way *not* to decide what features to implement. Don’t do things just because they’re inevitable. Inevitability is not a high enough bar. Let me explain.


Some time during the first year of Fog Creek’s operations, I was filing away some papers, and realized that I was all out of blue folders.


Now, I have a system. Blue folders are for clients. Manila folders are for employees. Red folders are receipts. Everything else is yellow. I needed a blue folder and had run out.


So I said to myself, “What the heck, I’m going to need a blue folder eventually anyway, I might as well go to Staples and buy some now.”


Which was, of course, a waste of time.


In fact when I thought about this later, I realized that for a long time, I had been doing dumb shit (that’s a technical term) simply because I figured that eventually it would have to get done, so I might as well do it now.


I used this excuse to weed the garden, patch holes in the walls, sort out MSDN disks (by color, language, and number), etc., etc., when I should have been writing code or selling code, the only two things a startup really needs to do.


In other words, I found myself pretending that all non-optional tasks were equally important, and therefore, since they were inevitable anyway, they could be done in any order! Tada!


But to be honest, I was just procrastinating.


What should I have done? Well, for starters, I could get over my fetish for having file folders all be the right color. It just doesn’t make any difference. You don’t have to color-code your files.


Oh, and those MSDN CD-ROMs? Toss them in a big box. PER-fect.


More importantly, I should have realized that “important” is not a binary thing, it’s an analog thing. There are all kinds of different shades of important, and if you try to do everything, you’ll never get anything done.


So if you want to get things done, you positively have to understand at any given point in time what is the most important thing to get done *right now* and if you’re not doing it, you’re not making progress at the fastest possible rate.


Slowly, I’m weaning myself off of my tendency to procrastinate. I’m doing this by letting less-important things go undone. There’s some nice lady from the insurance company who has been pestering me for two months to get some data she needs to renew our policy, and I didn’t actually get her the data until she asked about the fiftieth time, along with a stern warning that our insurance is going to expire in three days. And this is a good thing, I think. I’ve grown to think that keeping your desk clean is actually probably a sign that you’re not being effective.


How’s *that *for a mortifying thought!


So. Don’t do features based on what the sales force has inadvertently promised a single customer, and don’t do unimportant-slash-fun features first because “you’re going to have to do them eventually anyway.”


Anyway, back on the topic of choosing features for FogBugz 5.0. Here’s how we got our initial prioritization.


First, I took a stack of 5×8 cards, and wrote a feature on each one. Then I called the team together. In my experience this works with up to about twenty people, and it’s a good idea to get as many different perspectives in the room: programmers, designers, people who talk to customers, sales, management, documentation writers and testers, even (!) customers.


I asked everyone to bring their own list of feature ideas to the meeting, too. The first part of the meeting was going over each feature very, very quickly and making sure we had a very, very rough common understanding of what the feature was, and that each feature had a card.


At this stage, the idea was not to debate any feature on its merits, or to design the feature, or even to discuss the feature: just to have a vague, rough idea of what it was. Some of the features for FogBugz 5.0 were things like

- Personalizable Home Page
- Painless Software Schedules
- Track Billable Time
- Fork a bug
- (46 others…)


Very vague stuff. Remember we didn’t need to know at this point how each feature would be implemented, or what it involved, because our only goal was getting a rough prioritization that could be used as the basis to start development. This got us a list of about 50 big features.


In part two, we went through all of the features and everybody voted on each feature: just a quick “thumbs up” or “thumbs down.” No discussion, no nothing: just a real quick thumbs up or thumbs down on each feature. This revealed that about 14 of the feature ideas didn’t have much support. I threw out all the features that only got one or two votes, leaving us with 36 potential features.


Next we assigned costs for each of these features, on a scale of 1 to 10, where 1 was a quicky feature and 10 was a big monster feature. Here it’s important to remember that the goal was *not *to schedule the features: just to separate the tiny features from the medium features from the huge features. I just went through each of the features and asked the developers to call out “small,” “medium,” or “large.” Even without knowing how long a feature is going to take, it’s easy to see that forking a bug is a “small” feature while the big, vague “Personalizable Home Page” feature was large. Based on the consensus estimate of costs and my own judgment, we put down prices on all the features:


Once again, it’s really messy, it’s not exact, and it doesn’t matter. You’re not making a schedule today: you’re just prioritizing. The only thing that you have to get approximately right is the vague idea that you could do two medium features or one large feature or ten small features in about the same amount of time. *It doesn’t have to be accurate.*


The next step was making a menu of all thirty proposed features and their “costs”. Everybody on the team got a copy of the menu and was given $50 to play with. They could allocate their money any way they wanted, but they only had $50 to spend. They could buy half-features, if they wanted, or buy double features. Someone who really liked that Track Billable Time feature could spend $10 or $15 on it; someone who liked it a little might only spend $1 and hope that enough other people funded it.


Next, we added up how much everyone spent on each feature:


Finally I divided the amount spent by the cost:


And then sorted by this number to find the most popular features:


Ta da! A list of all the features you might want to do, in rough order of everyone’s best idea of which features are the most important.


And now you can start to refine. For example, you can clump together features that naturally belong together, for example, doing software schedules makes billable time easier, so maybe we should either do both or neither. And sometimes looking down the prioritized list it’s just real obvious that something is messed up. So, you change it! Nothing is carved in stone. You can even change the prioritization as you go through development.


But what surprised me the most is that the final list we produced was really a very good prioritization for FogBugz 5.0, and really did reflect our collective consensus about the relative priorities of various features.


Priority list in hand, we set out to more or less work down the list in order until about March, when we plan to stop adding new features and start the integration and testing phase. We’ll write specs for each (nonobvious) feature right before implementing that feature.


(The nattering scorekeepers of the BDUF/Agile beauty contest are now thoroughly confused. “Was that a vote for BDUF? Or Agile? What does he *want? Can’t he just take *sides *for once?!*“)


The whole planning process took three hours.


If you’re lucky enough to have the ability to release software more frequently than we do, (see [Picking a Ship Date](https://www.joelonsoftware.com/articles/PickingShipDate.html)), you still need to work down the list in order, but you can just stop and do releases more often. The good thing about frequent releases is that you can reprioritize the list regularly based on actual customer feedback, but not every product has this luxury.


Mike Conte taught me this system during the planning of Excel 5, where it only took a couple of hours even with a couple of dozen people in a conference room. The cool thing was that the roughly 50% of the features that we didn’t have time to do were really stupid features, and Excel was better because it didn’t have them.


It’s not perfect, but it’s better than going to Staples to get blue folders, I’ll tell ya that.
