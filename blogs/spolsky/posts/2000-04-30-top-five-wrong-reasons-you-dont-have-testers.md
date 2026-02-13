---
title: "Top Five (Wrong) Reasons You Don’t Have Testers"
date: 2000-04-30
url: https://www.joelonsoftware.com/2000/04/30/top-five-wrong-reasons-you-dont-have-testers/
word_count: 2192
---


In 1992, James Gleick was having a lot of problems with buggy software. A new version of Microsoft Word for Windows had come out, which Gleick, a science writer, considered to be *awful*. He wrote a [lengthy article](http://www.around.com/bugs.html) in the Sunday New York Times Magazine which could only be described as a flame, skewering the Word team for being unresponsive to the requests of customers, and delivering an enormously buggy product.


Later, as a customer of a local Internet provider Panix (which also happens to be my Internet provider), he wanted a way to automatically sort and filter his mail. The UNIX tool for doing this is called **procmail**, which is really arcane and has the kind of interface that *even* the most hardcore UNIX groupies will admit is obscure.


Anyway, Mr. Gleick inadvertently made some kind of innocent typo in procmail which deleted all his email. In a rage, he decided that he was going to create his own Internet access company. Hiring Uday Ivatury, a programmer, he created Pipeline, which was really quite a bit ahead of its time: it was the first commercial provider of Internet access with any kind of graphical interface.


Now, Pipeline had its problems, of course. The very first version didn’t use any kind of error correction protocol, so it had a tendency to garble things up or crash. Like all software, it had bugs. I applied for a job at Pipeline in 1993. During the interview, I asked Mr. Gleick about the article he wrote. “Now that you’re on the other side of the fence,” I asked, “do you have a bit more of an appreciation for the difficultly of creating good software?”


Gleick was unrepentant. He denied that Pipeline had any bugs. He denied that it was anything as bad as Word. He told me: “one day, Joel, you too will come to hate Microsoft.” I was a little bit shocked that his year of experience as a software creator, not merely a software user, hadn’t given him a smidgen of appreciation for how hard it is to really get bug-free, easy to use software. So I fled, turning down the job offer.  (Pipeline was bought out, by PSI, the strangest Internet provider on earth, and then unceremoniously taken out and shot.)


Software has bugs. CPUs are outrageously finicky. They absolutely *refuse* to deal with things that they weren’t taught to deal with explicitly, and they tend to refuse in the most *childish* of ways. When my laptop is away from home, it tends to crash a lot because it can’t find the network printer it’s used to finding. What a *baby*. It probably comes down to a single line of code somewhere with a teensy tiny almost insignificant bug in it.


Which is why you positively, absolutely, need to have a QA department. You are going to need 1 tester for every 2 programmers (more if your software needs to work under a lot of complicated configurations or operating systems). Each programmer should work closely with a single tester, throwing them private builds as often as necessary.


The QA department should be independent and powerful, it must not report to the development team, in fact, the head of QA should have veto power over releasing any software that doesn’t meet muster.


My first real software job was at Microsoft; a company that is not exactly *famous* for its high quality code, but which does nonetheless hire a large number of software testers. So I had sort of assumed that every software operation had testers.


Many do. But a surprising number do not have testers. In fact, a lot of software teams don’t even believe in testing.


You would think that after all the Quality mania of the 80s, with all kinds of meaningless international “quality” certifications like ISO-9000 and buzzwords like “six-sigma”, managers today would understand that having high quality products makes good business sense. In fact, they do. Most have managed to get this through their heads. But they still come up with lots of reasons not to have software testers, all of which are wrong.


I hope I can explain to you why these ideas are wrong. If you’re in a hurry, skip the rest of this article, and go out and hire one full-time tester for every two full-time programmers on your team.


Here are the most common boo-hoo excuses I’ve heard for not hiring testers:


### 1. Bugs come from lazy programmers.


> “If we hire testers”, this fantasy goes, “the programmers will get sloppy and write buggy code. By avoiding testers, we can force the programmers to write correct code in the first place.”
> Sheesh. If you think that, you either have never written code, or you are remarkably dishonest about what writing code is like. Bugs, **by definition**, leak out because programmers did *not* see the bug in their own code. A lot of times it just takes a second set of eyes to see a bug.
> When I was writing code at Juno, I tended to exercise my code the same way every time … I used my own habits, relying on the mouse a lot. Our marvelous, vastly overqualified tester had slightly different habits: she did more things with the keyboard (and actually rigorously tested the interface using every possible combination of inputs). This quickly uncovered a whole *slew* of bugs. In fact at times she actually told me that the interface flatly didn’t work, *100% did not work*, even though it always worked for me. When I watched her repro the bug I had one of those whack-your-forehead moments. Alt! You’re holding down the Alt Key! Why didn’t I test that?


### 2. My software is on the web. I can fix bugs in a second.


> Bwa ha ha ha ha! OK, it’s true, web distribution lets you distribute bug fixes much faster than the old days of packaged software. But don’t underestimate the cost of fixing a bug, even on a web site, after the project has already frozen. For one thing, you may introduce even more bugs when you fix the first one. But a worse problem is that if you look around at the process you have in place for rolling out new versions, you’ll realize that it may be quite an expensive proposition to roll out fixes on the web. Besides the bad impression you will make, which leads to:


### 3. My customers will test the software for me.


> Ah, the dreaded “Netscape Defense”. This poor company did an almost supernatural amount of damage to its reputation through their “testing” methodology:
> when the programmers are about halfway done, release the software on the web without any testing.
> when the programmers *say* they are done, release the software on the web without any testing.
> repeat six or seven times.
> call one of those versions the “final version”
> release .01, .02, .03 versions every time an embarrassing bug is mentioned on c|net. 
> This company pioneered the idea of “wide betas”. Literally *millions* of people would download these unfinished, buggy releases. In the first few years, almost everybody using Netscape was using some kind of pre-release or beta version. As a result, most people think that Netscape software is really buggy. Even if the final release was usually reasonably unbuggy, Netscape had so doggone *many *people using buggy versions that the *average *impression that most people have of the software was pretty poor.
> Besides, the whole point of letting “your customers” do the testing is that they find the bugs, and you fix them. Unfortunately, neither Netscape, nor any other company on earth, has the manpower to sift through bug reports from 2,000,000 customers and decide what’s really important. When I reported bugs in Netscape 2.0, the bug reporting website repeatedly crashed and simply did not let me report a bug (which, of course, would have gone into a black hole anyway). But Netscape doesn’t learn. Testers of the current “preview” version, 6.0, have complained in newsgroups that the bug reporting website *still* just doesn’t allow submissions. Years later! Same problem!
> Of those zillions of bug reports, I would bet that almost all of them were about the same set of 5 or 10 really *obvious* bugs, anyway. Buried in that haystack will be one or two interesting, difficult-to-find bugs that somebody has gone to the trouble of submitting, but nobody is looking at all these reports anyway, so it is lost.
> The worst thing about this form of testing is the remarkably bad impression you will make of your company. When Userland released the first Windows version of their flagship Frontier product, I downloaded it and started working through the tutorial. Unfortunately, Frontier crashed several times. I was literally following the instructions exactly as they were printed in the tutorial, and I just could not get more than 2 minutes into the program. I felt like nobody at Userland had even done the *minimum* amount of testing, making sure that the *tutorial* works. The low perceived quality of the product turned me off of Frontier for an awfully long time.


### 4. Anybody qualified to be a good tester doesn’t want to work as a tester.


> This one is painful. It’s very hard to hire good testers. 
> With testers, like programmers, the best ones are *an order of magnitude* better than the average ones. At Juno, we had one tester, Jill McFarlane, who found *three times as many bugs* as *all four other testers, combined*. I’m not exaggerating, I actually measured this. She was more than **twelve times** more productive than the average tester. When she quit, I sent an email to the CEO saying “I’d rather have Jill on Mondays and Tuesdays than the rest of the QA team put together”.
> Unfortunately, most people who are that smart will tend to get bored with day-to-day testing, so the best testers tend to last for about 3 or 4 months and then move on.
> The only thing to do about this problem is to recognize that it exists, and deal with it. Here are some suggestions:
> Use testing as a career move up from technical support. Tedious as testing may be, it sure beats dealing with irate users on the phone, and this may be a way to eliminate some of the churn from the technical support side.
> Allow testers to develop their careers by taking programming classes, and encourage the smarter ones to develop automated test suites using programming tools and scripting languages. This is a heck of a lot more interesting than testing the same dialog again and again and again.
> Recognize that you will have a lot of turnover among your top testers. Hire aggressively to keep a steady inflow of people. Don’t stop hiring just because you temporarily have a full manifest, ’cause da golden age ain’t gonna last.
> Look for “nontraditional” workers: smart teenagers, college kids, and retirees, working part time. You could create a stunningly good testing department with two or three top notch full timers and an army of kids from Bronx Science (a top-ranked high school in New York) working summers in exchange for college money.
> Hire temps. If you hire about 10 temps to come in and bang on your software for a few days, you’ll find a tremendous number of bugs. Two or three of those temps are likely to have good testing skills, in which case it’s worth buying out their contracts to get them full time. Recognize in advance that some of the temps are likely to be worthless as testers; send them home and move on. That’s what temp agencies are for. 
> Here’s one way *not* to deal with it:
> Don’t even think of trying to tell college CS graduates that they can come work for you, but “everyone has to do a stint in QA for a while before moving on to code”. I’ve seen a lot of this. Programmers *do not* make good testers, and you’ll lose a good programmer, who is a lot harder to replace. 
> And finally. The number one stupid reason people don’t hire testers:


### 5. I can’t afford testers!


> This is the stupidest, and it’s the easiest to debunk.
> No matter how hard it is to find testers, they are *still* cheaper than programmers. A lot cheaper.  And if you don’t hire testers, you’re going to have programmers doing testing. And if you think it’s bad when you have testers churning out, just wait till you see how expensive it is to replace that star programmer, at $100,000 a year, who got sick of being told to “spend a few weeks on testing before we release” and moved on to a more professional company. You could hire three testers for a *year* just to cover the recruiter’s fee on the replacement programmer.
> Skimping on testers is such an outrageous false economy that I’m simply blown away that more people don’t recognize it.
