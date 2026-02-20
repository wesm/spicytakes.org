---
title: "Mac Version Doing Fairly Well"
date: 2006-09-13
url: https://www.kalzumeus.com/2006/09/14/mac-version-doing-fairly-well/
slug: mac-version-doing-fairly-well
word_count: 293
---


As an afterthought, while programming v1.04 I had it append a variable saying what OS it was running on to all queries it makes to my website.  This lets me track the relative popularity of the OS X version versus the Windows version.  Now, as stated previously, I give customers the option of not telling me anything so these two numbers are fractions of what the true values are, but in the last seven days I’ve had 66 requests-for-updates from the Windows version and 6 from the Mac version (those are unique counts), not counting requests from folks with the registered version.


That would put my Mac popularity at about 10% of my windows one, which is pretty phenomenal given that a) my Mac version isn’t on the major download sites yet (still working on getting it on Download.com and versiontracker.com) b) I make it almost painfully difficult to get the Mac version and c) 2% of my visitors use Macs.


I think I might have to revisit that whole “make getting the Mac version painfully difficult” thing.  Here’s what happens: I’ve got exactly one button to initiate a trial download, and at the moment it opens up a web page which starts a download of the Windows .exe installer.  There is a note in bold telling Mac users “Sorry guys, that download is useless to you, click here”.  Why do it this way?  I figure my users are not exactly savvy and having multiple download buttons confuses more users than the Mac downloads are worth.  While I still think that, inconviniencing 10% of my user base doesn’t sit well with me, so I’m going to add a bit of Javascript to that download page and redirect Mac users to the correct package.
