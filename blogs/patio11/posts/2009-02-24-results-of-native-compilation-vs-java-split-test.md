---
title: "Results of Native Compilation vs. Java Split Test"
date: 2009-02-24
url: https://www.kalzumeus.com/2009/02/24/results-of-native-compilation-vs-java-split-test/
slug: results-of-native-compilation-vs-java-split-test
word_count: 727
---


For the last month I’ve been testing a version of Bingo Card Creator compiled with [Excelsior JET](http://www.excelsior-usa.com/) versus the standard Java one.  Half of all Windows downloaders have gotten one, half got the other.  I then have tallied when they confirm an installation (i.e. access my website through the application — for example by checking for updates or looking at the purchase page) and purchase the software.


This is accomplished via a really simple expedient — Bingo Card Creator has a properties file in it, which contains all the strings for the interface like you would expect.  It also contains strings for the version number and site the trial was downloaded from, which I repurposed for the purpose of this split test (since I only track bingocardcreator.com versus “all the download sites” at present anyhow).


So if you click “Purchase now” from version 2.51 of the Java version of the program after getting hit with the print quota limit, you end up accessing


http://www.bingocardcreator.com/purchasing.htm?source=trial&version=2.51&site=bingocardcreator&button=printquota


At which point Google Analytics springs into action, uses some very simple logic to parse the query string, and cookies you up with that information.  If you purchase within the next 30 days, the cookie is passed in when you hit the order acknowledgement page and scored as a conversion.  There is a custom segment in Google Analytics devoted to both the JET-compiled and native versions of BCC 2.51.


Anyhow: in the last 30 days I have had 118 sales of Bingo Card Creator.  (Wow, that number shocks me.)  Google Analytics has racked up 116 conversions, meaning they caught the access of the confirmation page on almost all transactions.  Of these 116 conversions, 75 of them were cookied up with a cookie indicating they were positively part of this split test.  (You could easily have participated without getting cookied — for example, if you decided to buy the software and then opened up a browser and Googled [Bingo Card Creator], I would have no way of knowing which executable you had downloaded.)


Of the 75 purchases, 44 were for the JET version and 31 were for the native Java compiled version.  So what’s that mean?  OK, back to Stats 102: if we assume hypothetically that it doesn’t matter which version you were using, we would expect that 50% of the total number of conversions would turn out each way.  However, just like flipping a coin twice doesn’t automatically mean you get one head and one tail, it won’t necessarily be exactly 37.5 sales of each version.  (One would hope not, right?  I’d hate to support the half-and-half.)


The probability of each possible outcome on the 0 purchases for JET through 75 purchases through JET continuum is given by the binomial distribution.  There is this notion of cumulative probability — given the assumption of 50/50 fairness between the two versions, the probability that any particular result is like to be random is equal to the sum of the probability of that result and all results less extreme than it.


Plugging and chugging with a binomial probability calculator, we arrive at the result that, if the versions were fair, in only 8% of all samples of 75 sales would we find 44 or more sales for JET.  Accordingly, we conclude that JET is helping sales, by some amount which the binomial probability test is not quite sensitive enough to determine.


Which is good enough for me.  One niggle: I discovered that for reasons beyond my ken, the JET version cannot save to the program directory on Vista, whereas the Java version can.  I probably should have listened to the advice a year and change ago when people said I should revisit the choice of home directories.  (Vista prevents programs from writing to subdirectories of Program Files to prevent bad behavior.  However, it emulates writing to Program Files to avoid breaking legacy software, and that emulation is sufficient for BCC Java but apparently not good enough for BCC JET).  Ah, we live and we learn.


After I patch that little issue, the JET compiled version of BCC is going to become the default version for all Windows users, and I will keep the Java version around only for support purposes, and to upgrade folks who already have one installed.


Much thanks to Dmitry at Excelsior, who donated a copy of JET to make this experiment possible.
