---
title: "Discussions: Flat or Threaded?"
date: 2006-11-24
url: https://blog.codinghorror.com/discussions-flat-or-threaded/
slug: discussions-flat-or-threaded
word_count: 520
---

Clay Shirky’s [classic articles on social software](https://blog.codinghorror.com/a-group-is-its-own-worst-enemy/) should be required reading for all software developers working on web applications. As near as I can tell, that’s pretty much every developer these days.


But I somehow missed Joel Spolsky’s related 2003 article on social software, [Building Communities With Software](http://www.joelonsoftware.com/articles/BuildingCommunitieswithSo.html).* It’s an excellent, albeit somewhat long-winded, explanation of the way Joel runs his [community forums](https://web.archive.org/web/20061205205738/http://discuss.joelonsoftware.com:80/?joel). Although I recently accused [Joel of jumping the shark](https://blog.codinghorror.com/has-joel-spolsky-jumped-the-shark/), his scathing criticism of Usenet, Slashdot, and IRC is right on the money. All three are deeply flawed social software models, incapable of sustaining civilized discussion.


Joel advocates policies on his discussion boards that seem unworkable, even borderline *anarchic*:

- No registration
- No user moderation
- No email notifications for new posts
- No posted rules
- No support for quoting or reply shortcuts
- No unread post shortcuts
- Arbitrary deletion of off-topic posts


Reads like a recipe for disaster, doesn’t it? But with one minor exception,** I’m in complete agreement. **When it comes to writing social software, Joel’s curmudgeonly advice may very well be the right approach.** Read the rest of Joel’s post to understand why.


In particular, I share Joel’s intense dislike of threaded conversations:


> *Q. OK, but can’t you at least have branching? If someone gets off on a tangent, that should be its own branch which you can follow or go back to the main branch.*
> A. Branching is very logical to a programmer’s mind but it doesn’t correspond to the way conversations take place in the real world. Branched discussions are disjointed to follow and distracting. [. . .] Branching makes discussions get off track, and reading a thread that is branched is discombobulating and unnatural. Better to force people to start a new topic if they want to get off topic.

kg-card-begin: html


| Threaded |  | Flat |
|  |  |  |


kg-card-end: html

Two of the oldest and most popular discussion boards on the web, [phpBB](http://www.phpbb.com/) and [vBulletin](http://www.vbulletin.com/), avoid threaded views. The phpBB developers [won’t add threading](http://www.phpbb.com/phpBB/viewtopic.php?t=256707). vBulletin offers threaded views, but they are off by default – and often disabled completely by administrators.


Personally, **I have yet find any threaded discussion format I like**. Aside from the philosophical objections Joel raises, threaded discussions are painful to use. You’re forced to click through to see the responses, and once you do, there’s far too much pogo-ing up and down the hierarchy of the threaded discussions. It’s all so... *unnecessary*.


Flat discussion views have their limitations, too. But they’re minor compared to the train wreck that is threaded discussions. Until we can come up with a new discussion model that *doesn’t* add a slew of new problems, let’s take Joel’s advice and **stick with simple, flat discussion views**.


*Thanks to [Phil](http://haacked.com/) for pointing this article out to me.


**Quoted snippets are helpful if used in moderation. Unlike Joel, I don’t have total recall of the last five posts I just read; judicious use of a few contextual quotes helps me keep the rest of the conversation in my brain.

[community moderation](https://blog.codinghorror.com/tag/community-moderation/)
[discussion forums](https://blog.codinghorror.com/tag/discussion-forums/)
[social software](https://blog.codinghorror.com/tag/social-software/)
[online communities](https://blog.codinghorror.com/tag/online-communities/)
