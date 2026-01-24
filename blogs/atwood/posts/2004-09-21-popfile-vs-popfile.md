---
title: "POPFile vs. POPFile"
date: 2004-09-21
url: https://blog.codinghorror.com/popfile-vs-popfile/
slug: popfile-vs-popfile
word_count: 369
---

In my previous blog entry on [some plan(s) for spam](https://blog.codinghorror.com/some-plans-for-spam/), I mentioned that I didn’t care for challenge/response “human-only” whitelists. I couldn’t put my finger on exactly why I felt that way... until I happened upon this [John Graham-Cumming PowerPoint presentation](http://www.jgc.org/SpamConference011604.pps):


> *I don’t “do” Challenge/Response. If I mail you and you challenge me I hit delete, because, as Dan Quinlan put it: **“Challenge/Response is the ultimate email diss. By using it you are saying, ‘my time is more important than yours.’”***


That about sums it up for me.


John Graham-Cumming is the author of [POPFile](http://popfile.sourceforge.net), so naturally his presentation goes on to... describe ways to defeat POPFile? It’s actually titled, [How to beat an Adaptive Spam Filter](http://www.jgc.org/SpamConference011604.pps). A fascinating read, with a disturbing conclusion: when pitting “evil” POPFile against good POPFile, the good guys lose. In other words, spammers can use Bayesian filters to defeat Bayesian filters – **if they get feedback about what mails are getting through!**


This makes me very, very happy that Windows XP Service Pack 2 turned off [HTML rendering in Outlook Express](https://web.archive.org/web/20040824014840/http://www.microsoft.com/windowsxp/sp2/ieoeoverview.mspx) by default:


> *Pictures and images embedded in HTML e-mail messages can be adapted to secretly send a message back to the sender. These are often referred to as Web beacons. Spammers rely on information returned by these images to confirm active e-mail addresses. Some spam messages contain Web beacon images so small that they are invisible to the human eye – but not to Outlook Express.
> An improved defense against Web beacons is to stop pictures from downloading until you’ve had a chance to review the message. Outlook Express in Windows XP SP2 will now block images automatically in messages from people who are not in your address book. This goes a long way in preventing the verification of your e-mail address for spammers. It makes your e-mail name less useful to spammers and may result in your getting less spam over time.*


Putting images in HTML seems innocent enough, but retrieving *any *image results in a direct request from your computer to the spammer’s webserver. With this tiny bit of feedback, they could conceivably defeat any anti-spam technology. Scary stuff!

[spam filtering](https://blog.codinghorror.com/tag/spam-filtering/)
[email](https://blog.codinghorror.com/tag/email/)
[popfile](https://blog.codinghorror.com/tag/popfile/)
[bayesian filters](https://blog.codinghorror.com/tag/bayesian-filters/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
