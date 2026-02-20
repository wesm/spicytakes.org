---
title: "Dropbox is saving my bacon"
date: 2009-05-11
url: https://www.kalzumeus.com/2009/05/11/dropbox-is-saving-my-bacon/
slug: dropbox-is-saving-my-bacon
word_count: 490
---


About a month and change ago a Japanese coworker asked me “Hey, Patrick, have you ever heard of [Dropbox](https://www.getdropbox.com/home)?”  All I knew is that they were some vaguely storage-in-the-clooooooooooooooooooooooud startup, but not really the specifics.  But since he and another coworker were interested in it I did some checking to tell them what they would need to press to sign up & etc.  And, yep, storage in the cloud, painless backup, blah blah.  So I grabbed an account for the heck of it and decided I would get around to backing up my files one of these days.


*Sigh*.  You think we would know by now, right?  “I’m going to start a backup any day now” ranks right up there with “Hmm, well, we haven’t heard from that freaky serial killer in a while.  I think I’ll stay in the house.”


This is despite [Benji](http://benjismith.net/index.php/2009/01/13/calamity/) and [Andy Brice](http://successfulsoftware.net/2008/02/04/your-harddrive-will-fail-its-just-a-question-of-when/) both having recent hard drive failures.  (Andy’s, which was a year ago so I suppose not so recent, even came with the title “Your harddrive *will* fail”.  Yeah yeah, sure, and I bet you think there is a machete-wielding maniac over in the next room.  Bah, I think I’ll take a bath.)


Thankfully I was sufficiently moved by their advice to start keeping backups of my servers at Slicehost, which has the added benefit of protecting my source code (since I have my repositories on those servers).  Most of my critical business data is already off of my laptop — its at a Google server farm, or chilling on a Slicehost server, or over at Paypal, but there is still quite a bit of sentimental value in my photos and nuisance in having to reconfigure, e.g., Eclipse to match my personal setup again when I reinstall it.


Anyhow, today the inevitable happened: my Vista-using laptop decided to start the sputter and die deathspiral.  Thankfully, after an hour of fruitless restarts, I was able to boot into safe mode, where I am right now.  I think the hard disk covering some of the code loaded by all the bells&whistles that autoload when the machine boots is toast.  Luckily untoasted is my ability to read the rest of the disk and run Dropbox.


Which is currently streaming my last few folders of Really Don’t Want To Lose That to safer pastures.  Here’s $100, Dropbox — thanks a million.


Fun tip for Vista users: mklink /D name-of-your-symlink C:\Users\blahblah\Documents\whatever will create a symlink between two places on a Vista OS.  If you have a symlink pointing out of your Dropbox folder, dropbox will perceive the stuff outside (say, a full Cygwin installation) as being inside of the Dropbox, and automatically sync it for you.  I really appreciate that trick, as it meant I didn’t have to copy/paste the files I need to update and risk more harddrive activity at the moment.


2 hours until the last of the files are off the disk.  Go Dropbox, go!
