---
title: "The (Trial Downloads) Numbers Game"
date: 2006-08-07
url: https://www.kalzumeus.com/2006/08/07/the-trial-downloads-numbers-game/
slug: the-trial-downloads-numbers-game
word_count: 712
---


I passed a milestone some time in the last week — over 1,000 trial downloads of some version of Bingo Card Creator.  Its actually a little higher than that as reported by my server logs but I’m discounting that a bit to account for download site update spiders and pirates.


But its really, really hard to tell exactly how many people are using Bingo Card Creator today.  This is obviously a number of profound interest to me.  In the last week, for example, Google Analytics reports that 95 people have hit my thanks-for-downloading page, which starts automagically downloading a trial demo.  On the other hand, only 18 people have used the update feature in Bingo Card Creator (17 of them with version 1.02, 1 with version 1.03).  So my lowball estimate for number of people using the software is 18ish at the moment, plus an unknown number of folks who are stuck with version 1.0 which doesn’t have update checking.  That number is unfortunately *growing* because getting a new version onto Download.com takes two weeks if you’re not willing to pay through the nose, and I’m not (need sales to cover August advertising still).


I’ve got a couple of worries for the discrepency between downloads as reported by Analytics and confirmed downloads as reported by update checking.  They could be due to any of the following:


1)  Analytics records the download but no download actually took place.  This could easily happen on, for example, IE.  Microsoft’s late-in-the-day embrace of security makes it impossible for my meta-refresh to the .exe to work properly on most computers, so I have to rely on the customers actually reading the first line of text on the page and right-clicking the download link.  This is obviously the worst sort of failure — its a failure I’ll never know about and can’t recover from.


2)  People download the demo and then fail to install it, after forgetting about it or what have you.


3)  People download the demo, install it, run it, and then are told they don’t have a sufficient IDE.  Despite the fact that launch4j, the Java wrapper of my dreams, will offer to launch the Java download page, I obviously can’t sit on folks shoulders and make them press the 6 buttons it will take to get the 18MB JRE installed.


4)  Folks might download the demo, run it successfully, and then opt-out of the checking for updates.  After all, the thinking goes, why would I need to check for updates if I’ve just downloaded it 2 minutes ago.  I might get an update request from them in 15 days when Bingo Card Creator expires their previous cancel (and then I won’t know whether its a user continuing to use my product or a new downloader… grr…).  It would be the simplest thing in the world for me to ping my server regardless of whether they want to check for updates or not, but its not honest.


Anyhow, I’m thinking of sweetening the pot a little bit to encourage people to check for updates.  At the moment my software comes with about a dozen unique word lists, and as time goes on that number is going to increase.  (I should really sit down and write some more, actually — they’re “new features” from the perspective of my users and only take ~10 minutes to compile each.)  I think I’ll reserve, say, 5 of these lists as a Bonus Pack.  And then, if folks don’t have the bonus pack installed, when I ask them for an update I’ll say “You’re missing the Bonus Pack of free word lists.  Would you like to download the Bonus Pack and check for other updates now?”  Since the Bonus Pack would be downloaded exactly once per customer, that would give me a more accurate count of total installations.


I could even, theoretically, just put the Bonus Pack in the installer and only *enable* it if folks choose “Check for Updates” (and/or automagically download a decryption key and decrypt it, whatever).  That, however, leaves a bit of a bad taste in my mouth.  Its the same “tell me you exist and I’ll give you additional benefits” transaction as the download-the-bonus-pack option is, but it seems to be based on a deception.
