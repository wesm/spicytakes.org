---
title: "Open Source vs. uISVs — Some Myths That Need To Die"
date: 2006-08-22
url: https://www.kalzumeus.com/2006/08/23/open-source-vs-uisvs-some-myths-that-need-to-die/
slug: open-source-vs-uisvs-some-myths-that-need-to-die
word_count: 1710
---


Oddly enough right before I went on vacation I [ended up on Slashdot](http://developers.slashdot.org/article.pl?sid=06/08/17/1332241) for my recent musing on [crippling trial versions](http://microisvjournal.wordpress.com/2006/08/16/to-limit-or-not-to-limit/). It being Slashdot, many people were shocked and amazed that someone would have the gumption to actually sell a program of the complexity of Bingo Card Creator. There was also, shall we say, a weeeee bit of animosity. Similarly, if you go to the [Business of Software forums](http://discuss.joelonsoftware.com/default.asp?biz), every time the subject of OSS (open source software — to sidestep a debate which is essentially religious, OSS can be most easily understood as “software which you can use and modify for free”) comes up some folks have a weeeeee bit of animosity towards it. And when I say a weeeeee bit of animosity, its like saying that Israelis and Arabs don’t quite see eye-to-eye on that little land dispute they’ve had running for a few years.


Now, personally, I don’t understand quite why this is. Open source coexists quite readily with uISVs (micro independent software vendors = people, like me, who sell software without the backing of a “really big company”) and will continue to do so indefinitely. I say this as someone who both has contributed to OSS software (namely, I did bugfixing and optimizations for the best online version of the [classic Battletech boardgame](http://megamek.sf.net) in existence), use OSS constantly in both my day job and my uISV, and sell [proprietary software.](http://www.bingocardcreator.com) So when I hear myths like the following I get a good chuckle.


**OSS backers are crazy Commies**. Most people who have installed Firefox are, in fact, not Communists. Most of the folks who, for lack of a better term, find themselves politically or spiritually fulfilled by the OSS movement (as opposed to a particular piece of OSS software), are in fact not Communists. Many of them do have irrational takes on the actual economics of software (c.f. Richard Stallman’s [GNU Manifesto](http://www.gnu.org/gnu/manifesto.html), which suggests at one point that all computer users be taxed to fund software development, an idea which would lead to overpriced computers, a crushing undersupply of new software, and a gigantic transnational boondoggle of a government agency to administer the tax, and thats just for starters). However, the movement is too fractured, too corporatized (see below), and too lacking in bullets-in-the-back-of-the-head-for-all-who-oppose-us to be fairly called Communist. Of course, its entirely possible that some OSS developers are honest-to-badness Commies, but thats far from universal.


**OSS software is written by tiny developers working in their spare time out of the goodness of their hearts**. This is every bit as much a lie as the Commie bit. Here’s a dirty little secret: most big-name OSS projects (including Linux, Firefox, Eclipse, take your pick) are produced primarily by programmers at large corporations working at the direction of their bosses in exchange for cash money. “Anyone can contribute to Linux!” is, if not a lie, a gross misstatement of the facts: getting a patch into the Linux kernel requires getting it past a series of gatekeepers who are getting paid for their time. And thats probably a good thing. Why IBM et al spend billions of dollars (in money and donated labor) on funding the Apache Software Foundation, Mozilla, et al are outside the scope of this post, but they do. And they’re hardly alone — [more than half](http://www.osdn.com/bcg) of the developers working on Sourceforge at the behest of the people signing their paychecks.


**OSS will reach every niche in the software world and there will be no space for proprietary software**. O rly? Allow me to give a +5 insightful to guy on Slashdot who said “If that was true, why hasn’t OSS produced something of quality comparable to Bingo Card Creator?” Oh, there are a lot of answers to that one.


Have you ever noticed that programmers seem to be able to find almost anything they need on Sourceforge and that everybody else really has to hunt for it? This is a reflection of the most fundamental truth of software development: you can’t program if you’re not a programmer. Programmers are very good at producing software for their own needs… and a lot less good at producing software for other’s needs. But the rest of the world keeps needing software to run their [chimney sweep](http://www.chimsoft.com/) operations, [make bingo cards](http://www.bingocardcreator.com), [plan their weddings](http://www.perfecttableplan.com), and [write their aquisition forms](http://office.microsoft.com) for a new laptop to replace the one that just exploded. And so there is a market for software development expertise, where people who don’t have it pay people who do money so that they can get back to doing the things they do best. Like sweeping chimneys, teaching children, looking at overly expensive wedding dresses, and blogging.


**Open source means all bugs are get fixed and all features get implemented**… in some dreamworld where all open source projects are under active development. Back in the real world, the overwhelming majority of open source projects are inactive. Development has ceased, the original maintainer (and the only person who knows how the code works) cannot be contacted, and mails/forum posts go unanswered. Take a look at the closest OSS competitor to my program, [bingo-cards](http://sourceforge.net/projects/bingo-cards): it hasn’t seen a patch since 2004. (And its more active than 75% of the projects on SourceForge.) This is despite some minor usability niggles such as the fact that if you try to install it on a Windows PC it will crash.


Here’s another myth held by many in the uISV community: **OSS developers will instantly clone any successful application because they’re crazy zealots**. I’m sure any competent C developer could take the bingo-cards codebase and make it the equal of Bingo Card Creator in less than a man-week. I’m equally sure that they won’t. Sure, lots of the folks on Slashdot said variations of “Oh, I’d clone your program just to spite you”, but I have the strong suspicion that, as the Texas saying has it, they have a lot of hat but no cattle. And most uISVs produce programs with vastly higher barriers to entry than Bingo Card Creator — I shudder to think at how much I’d have to learn about chimney sweeping to outdo ChimneySoft, and there’s probably an order of magnitude more code to write there.


IBM is no more interested in bankrolling bingo-cards than they are interested in rolling out their own Proprietary Bingo Solution (TM) because the niche is just too tiny. Most teachers are incapable of coding and don’t have a week to spend doing it at any rate. Most one-man OSS teams don’t exactly have their intrinsic motivation fire lit by doing the unchallenging, boring coding tasks like making sure that bingo cards are printed correctly. Enter the uISV, who has the skills and the motivation ($$$) to solve this task, and everyone profits. Little kids learn to read, teachers spend more time teaching and less time preparing, I earn money to fund my cocoa habit, OSS developers write software they’ll actually enjoy writing.


Oh, while we’re at it, here’s another myth both OSS backers and many uISVs suffer under: **Most of the work done in producing a quality piece of software happens in an IDE**. If a tree falls in a forest, does it make any sound? If the perfect solution to the problem facing you can’t be found on a Google search, does it matter that it exists? Most successful uISVs have long since learned the lesson that writing the program is about 10% of the battle: you’ve then got to get it in front of prospective users, write documentation, help them with their problems, market market and market some more, etc. These take time and money, and most OSS developers hate them. With a burning passion. Intrinsic motivation only takes the typical OSS developer as far as closing the IDE.


bingo-cards, for example, gets about 5% of my downloads primarily because I spent time making a website which attracts teachers who have a problem like “I need to play sight word bingo with my first graders tomorrow but don’t want to spend hours making cards” and gives me the opportunity to tell them “Yep, install my software and you’ll be done in five minutes”. One way of several is I just got charged $90 by Goooogle for clicks on contextual advertising. Probably 99.9999% of OSS has an advertising budget of nothing. The developers also don’t typically take even rudimentary, free steps such as writing a description of their software which explains to real, honest-to-God users what their program actually allows them to accomplish. Not to pick on bingo-cards, but let me quote [literally the entirety](http://sourceforge.net/projects/bingo-cards) of what you can learn about their software without downloading it:


> GPL bingo card printing program (numeric, letter bingo and picture bingo). Also prints a calling sequence (equivalent to the output from a barrel full of balls). XML output for later linking to multimedia engine.


Thats full of scary acronyms, irrelevant information, and about three words which are actually of use to an elementary school teacher. You can’t tell from that description that bingo-cards will even allow you to print Dolch sight word bingo cards (it will, incidentally, although you’ll have to supply the list yourself).


Compare this to a random three sentence snippet from a page on my website about [Dolch sight word bingo](http://www.bingocardcreator.com/dolch-sight-words-bingo.htm):


> This is a page of **free resources for teaching how to read Dolch sight words** which we put together as a resource to educators. You’ll probably want to have a set of sight words bingo cards ready to go to use these activities. If you don’t have one, you can make one in under five minutes if you [download the free trial of Bingo Card Creator](http://www.bingocardcreator.com/thanks_for_downloading.htm), which comes complete with all five Dolch sight word lists (pre-primer, primer, first grade, second grade, and third grade).


Only one of these two pages is responsive to the needs of our busy first grade teacher, and only one of them gets hit by Google searchers about 200 times per week.


[Edit: “Boondoggle” is a very hard word to spell.  I have no clue where “misunderstatement” came from, but I do love the charming Dubyaesque quality of that coinage.  Sadly, I was forced to rectify it to avoid enraging my readers who are English teachers.]
