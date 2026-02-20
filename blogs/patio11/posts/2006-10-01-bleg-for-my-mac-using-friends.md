---
title: "Bleg for my Mac using friends"
date: 2006-10-01
url: https://www.kalzumeus.com/2006/10/01/bleg-for-my-mac-using-friends/
slug: bleg-for-my-mac-using-friends
word_count: 267
---


I recently released Bingo Card Creator on Versiontracker.com, a Mac software site that is apparently pretty popular.  And by recently I mean less than 12 hours ago.  I’ve already got multiple sales (!) and also multiple bug reports that it doesn’t work on various versions of Mac OS X.  I know it works on at least some Mac machines because I have happy, satisifed customers from the other download sites and I can see successful requests for the check-for-updates page in my HTTP logs which identify themselves as coming from the Mac version.


Two users reporting problems are using Mac OS X 3.9 and 10.4.7.  These numbers might as well be Greek to me since I have no experience using Macs.  The symptom they describe is that the application dies on startup due to Java being unable to find the main class.  This is behavior I am unfortunately distressingly familiar with on Windows, and it is generally the result of a faulty manifest file.  To my knowledge the Mac doesn’t actually read the manifest file (which is in order) but rather uses a special Mac-only pinfo.list file to specify the main class.  However, I have checked and rechecked and the special Mac file which points to the class which is to be executed *appears* to be in proper order.


Thus the request: if you’ve got a Mac OS X lying around, could you please download the software (www.bingocardcreator.com) and tell me exactly what, if any, error message it produces on your particular version of Mac OS X?  I’d be indebted if you had any suggestions as well.
