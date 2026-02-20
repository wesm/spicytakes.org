---
title: "Perl Makes Me Feel Dirty"
date: 2007-01-16
url: https://www.kalzumeus.com/2007/01/16/perl-makes-me-feel-dirty/
slug: perl-makes-me-feel-dirty
word_count: 188
---


I had to code Perl at my day job today… and was productive… and *enjoyed* it.  Ewwwww.  The task was munging 15,000 mails from a variety of mailing list archives into our email system to test the new spam filter.  Previously, I would have used gawk for that, and spent a good half my morning writing out clever ways to extract the “next” mail from the archive’s web page.  That task took a single regular expression — that whole “matching the stuff in parentheses” is really magic.


Then I got home and had to add a bit of Javascript to all of my webpages to get the new e-junkie cart working.  So I decided “Hey, this will only take a minute in Perl”.  And it actually only did take a minute.  It was sort of *fun*, too.


Someone please pass me a flail, I need to be beaten before all my code looks like newspaper characters cussing.  (No lie.  That one minute program included the line $_=~s/blahblah/blah/.  Experienced Perl hackers will immediately notice the problem with this line — its four characters longer than it needs to be.
