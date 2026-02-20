---
title: "Programming Productivity Up By 10%… Yowza"
date: 2007-06-07
url: https://www.kalzumeus.com/2007/06/07/programming-productivity-up-by-10-yowza/
slug: programming-productivity-up-by-10-yowza
word_count: 661
---


I have tried [expressing my love](http://microisvjournal.wordpress.com/2006/08/05/a-love-note-to-my-favorite-productivity-app-ever/) for [Direct Access](http://www.nagarsoft.com/) before.  Really, its hard to describe until you’ve tried it.  However, Andrea was smart enough to include an automatic logging feature in the newest version, which demonstrates exactly how much time it saves you.  (Memo to self: scrape user accounts for Kalzumeus, generate similar ROI-proving eyecandy, and put at the top of the Upgrade Your Account screen.  Its brilliantly simple salesmanship.)  For me, that number is scary.  Lets focus on yesterday, shall we.  Here is a shot of Direct Access on my home computer, which was on yesterday from 7 PM when I got home to 2 AM.  Of that, 3 solid hours was programming time, after doing battle with SVN fruitlessly for far, far too long.


During programming time, I’m typically opening folders and programs left, right, and center.  Copy this to there, grab the backup of that, nuke those sources, where the heck was my Rails API reference, need to open Thunderbird to retrieve my SVN password, that sort of thing.  Apparently I do this more commonly than I had thought:


I generally estimate 20 seconds to accomplish any random opening from staring at my IDE window.  For example, to get to the Rails API, that would generally be Start -> Internet Explorer  -> Google (my home page) -> Rails API -> I’m Feeling Lucky.  (Why type as opposed to using my bookmark?  Faster, less requirement for right hand, gets autocomplete.)  Given the need to take my hands off the keyboard and the lingering pain in my right hand, thats a good twenty seconds.


Well, thats a bit shorter, isn’t it.


**rrrTAB** (used to be **railsTAB**, but I found myself typing it a lot) gets me a command shell opened to my Rails application directory.  **sshTAB** gets me a Putty window set to automatically log into the server I’m most frequently using.  All the power of the command line and autocompletion… from anywhere.  Bwahaha.  You can keep your OS X, vim, and bash, I’m puttering around in a deliciously iconoclastic Windows XP… at Unix sysop speeds.


I also love the autotext for hammering out boilerplate code… that turns out to be a heck of a lot less useful in Ruby than it was in Java, though, since a) I write less boilerplate and b) I’m not sufficiently well versed in the boilerplate to have prepared it as a macro yet.  In Java, on the other hand,  I *know* I will have to do **intconvertTAB** again, writing out a try-catch block to surround a very prosaic String to int conversion.


> try {
> replaceMe = Integer.parseInt(cursorStartsHereAfterIHitTab);
> } catch (NumberFormatException e) {
> // Handle if string was passed by user, safe to ignore if string came internally.
> }


The third time I type the same freaking snippet out it goes in Direct Access with a memorable abbreviation.   I have twenty of them for Java now, and a few for Rails, mostly for migrations and to act as quick references for syntax.


You wouldn’t think shaving a few seconds here and a few seconds there would really matter that much, but the stats don’t lie.  A 165 minute programming session was a 180 minute session purely thanks to Direct Access.  Not bad.  I really wish they hadn’t forced me to uninstall my copy at work — “Well, Patrick, you see, we have a new security policy…”  Suit yourself, boss.  I get paid regardless of whether I’m being productive or not at the day job.  When *I’m* the boss, heck, time spent clicking is time spent not doing more important things.


If you don’t have something like this… get it.  Really.  Its a no brainer.


As usual, product placements on this blog are 100% uncompensated.  I like it, I use it, it saves me time and money, I blog about it.  I do not solicit, accept, or envision folks giving me money for anything other than the products I sell.
