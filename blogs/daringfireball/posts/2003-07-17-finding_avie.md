---
title: "Finding Avie"
date: 2003-07-17
url: https://daringfireball.net/2003/07/finding_avie
slug: finding_avie
word_count: 1303
---


A handful of readers emailed to complain about Monday’s [mixed review of Avie Tevanian’s legacy](https://daringfireball.net/2003/07/the_good_the_bad_and_the_avie.html) as Apple’s vice president of software engineering. In particular, this concluding sentence:


> In short, many of Tevanian’s design decisions have not been made
> 	with the best interests of Mac users in mind.


The gist of the griping can be summarized thusly: *What you describe as “bad” under Tevanian doesn’t seem all that bad. An unpopular technote that was eventually withdrawn? So what? I don’t care about developer documentation. How did that have any effect on real users?*


But that’s just it — Technical Note #2034 was not merely a web page of developer documentation. It was a description of de facto policies governing Apple’s own software development, certain of which policies clearly were not in users’ interests, and but which Avie Tevanian wanted all other Mac developers to adopt. While the technote itself was rescinded, the policies, as applied to Apple’s own software, were not.


Take, for example, Tevanian’s inexplicably fanatical antipathy toward HFS file type and creator metadata.


One of the nicest new features in Jaguar (Mac OS X 10.2) was that the Finder was finally able to, well, *find*. To understand why this was such a welcome change, we need to recall a bit of Finder history. The name “Finder” notwithstanding, up through and including System 6, the Finder had no Find command. You couldn’t use the Finder to search.


In System 7.0, Apple added a very rudimentary file search feature to the Finder. So rudimentary that it bordered on being useless. You could enter a search string, but rather than display a list of all resulting matches, the Finder would simply open the containing folder for the first match and select the file. If that wasn’t the one you were looking for, you needed to Find Again, repeating until you got to the file you were looking for. This was frustrating for searches that matched more than a few files; it was downright infuriating for searches that matched dozens or hundreds of files. In System 7.5, Apple removed the lame Find feature from the Finder itself, and replaced it with a much more useful standalone utility called Find File. In Mac OS 8.5, Apple renamed Find File “Sherlock”, and added Internet searching capabilities.


Sherlock made the move to Mac OS X, and its Internet-related search features grew in scope. But it moved further away from its original purpose: providing a simple but effective way to search for files on your computer. And so the split in Jaguar was welcome indeed — Sherlock was refocused purely on Internet-related searching (infamously [taking ideas from Karelia Software’s Watson](http://www.karelia.com/watson/watsonFAQ.html)), and file searching was moved back into the Finder, where it should have been all along.


The Jaguar Finder’s file search feature is very good indeed. It has an intuitive UI for adding and removing multiple search criteria. In a welcome change from the old Sherlock and Find File, the Jaguar Finder allows you to specify multiple criteria based on the same attribute. E.g. you can search for files whose names start with “a” and end with “z”, whereas Sherlock and Find File only allowed a single criterion based on the name.


But Jaguar’s file searching is marred by a glaring omission: the ability to search for file type and creator code attributes, a feature that was present all the way back to Find File in System 7.5. Instead, the Jaguar Finder allows you to search for a new attribute, “Extension”. But of course this isn’t new at all — by definition, a filename extension is part of the filename. Searching for files whose extension is “app” generates the *exact same results* as searching for files whose name ends with “.app”.


Something useful (type and creator searching) was replaced by something utterly and obviously redundant (“extension” searching).


There are so many reasons this is wrong. For one thing, type and creator searching cannot by replaced by filename extension searching — even if you make the (bad) assumption that all files have accurate extensions. Here’s a reasonable hypothetical. Let’s say I’m searching for an HTML file that I created, the name of which I cannot remember. But I’m fairly certain I’ll recognize it when I see it. I also know that I created the file with BBEdit.


I have a spare iMac running a close-to-stock installation of Jaguar. Searching the iMac’s startup disk for files with names ending with “.html” produces a list of over 18,000 results (mostly help files and developer documentation). That doesn’t help me at all. After rebooting into Mac OS 9, a search for files whose names end with “.html” and whose creator is “R*ch” (BBEdit’s creator code) produces a list of 60 files — which I can easily scroll through looking for my target. (Note that neither Find File nor Sherlock forced you to remember type and creator codes — both allowed drag-and-drop to be used to specify an example file.)


Searching for type and creator codes is very fast. Contrary to widespread misconception, file type and creator metadata is *not* stored in a file’s resource fork. They have nothing to do with resource forks whatsoever — rather than being stored as part of either fork of a file, they are stored in the HFS directory entry for the file, alongside the filename (which technically qualifies as metadata also, albeit a form of metadata supported on all file systems).


From a programming perspective, adding support for file type and creator code searching is a cinch. The Carbon APIs provide routines that do all the work — the same group of routines the Finder is already using for the other attributes it allows you to search for.


So (1) type and creator searching is useful; (2) it’s been around since System 7.5; (3) it’s fast; and (4) it’s easy to implement. So why doesn’t the Jaguar Finder support it?


Spite.


I can think of no other reasonable explanation. It certainly can’t be justified by claiming that type and creator codes have been deprecated. For the sake of argument, even if we concede that filename extensions will and should serve as a replacement for genuine type and creator metadata (a huge concession, mind you), it still doesn’t justify not including the ability to search for them in the Finder.


Deprecating only implies moving away from something as you go forward — not pretending that it never existed. HTML 3 has been deprecated for years, but brand new web browsers (like Safari) still render it. Unicode is the future of text encoding — and on Mac OS X, it’s the present — but you can still open and edit single-byte encoded text files.


There are several million Macs running Jaguar, most of which contain hundreds of thousands of files with type and creator codes. That amounts to hundreds of billions of files with type and creator codes that can’t be searched for. How could this limitation possibly be in the interests of regular users?


(The good news is that in the [Panther](http://www.apple.com/macosx/panther/) (10.3) seed released at WWDC, type and creator code searching is back in the Finder. That’s a good sign — but it doesn’t excuse its exclusion from Jaguar.)


Is type/creator searching a huge deal? No. But it’s emblematic of how Avie Tevanian earned the enmity of so many long-time Mac developers. The filename-extension vs. type/creator argument is a political one, and all too often Tevanian has put technical politics ahead of usability. It’s as though it isn’t enough that Mac OS X has been deemed a success — but that the old NeXT system must be proven to have been superior all along.



| **Previous:** | [The Good, the Bad, and the Avie](https://daringfireball.net/2003/07/the_good_the_bad_and_the_avie) |
| **Next:** | [‘Grab HTML’ Script for BBEdit, Redux](https://daringfireball.net/2003/07/grab_html_script_for_bbedit_redux) |


PreviousNext