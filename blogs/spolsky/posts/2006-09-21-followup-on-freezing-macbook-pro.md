---
title: "Followup on freezing MacBook Pro"
date: 2006-09-21
url: https://www.joelonsoftware.com/2006/09/21/followup-on-freezing-macbook-pro/
word_count: 263
---


Remember when I [complained](https://www.joelonsoftware.com/items/2006/09/11.html) that my Mac kept freezing with bouncing beach balls?


A lot of people suggested it might be a hardware problem, but the diagnostics on the setup disks didn’t find anything.


Well, Daniel Jalkut over at [Red Sweater Software](http://www.red-sweater.com/products/index.html) suggested that I look in the console app to see what was going wrong, and lo and behold, there were lots and lots of messages that said:


**Sep 19 22:56:39 joel-spolskys-computer lookupd[711]: NetInfo connection failed for server 127.0.0.1/local**


This totally corresponded to what I was seeing… suddenly any app that tried to do a DNS lookup of any sort would go into permanent beachball mode and never recover.


Some Googling around led me to a page by John Bafford that [said](http://www.dshadow.com/software/unlockupd/) “Lookupd has a bug (rdar://3632865) in its cache cleanup code that causes it to randomly crash. CrashReporter, the system crash log agent, does not properly handle lookupd crashes, and as a result, when lookupd crashes, the process is not terminated. Since lookupd has not terminated, mach_init does not respawn lookupd. From this point, any application that attempts to access lookupd, either directly or indirectly, will hang.”


Hmmph. Kindly, John provides [Unlockupd](http://www.dshadow.com/software/unlockupd/), a daemon that watches lookupd and restarts it if it gets jammed up.


I’ll try this for a while and see if it helps. In the meantime, if it’s true, it’s odd that Apple hasn’t fixed this bug in over two years. If somebody inside Apple wants to peek into [that bug](rdar://3632865) (link only works inside Apple) and let me know what they see there, I’ll update this article!
