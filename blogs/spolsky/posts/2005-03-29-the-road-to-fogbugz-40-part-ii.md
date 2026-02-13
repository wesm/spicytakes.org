---
title: "The Road to FogBugz 4.0: Part II"
date: 2005-03-29
url: https://www.joelonsoftware.com/2005/03/29/the-road-to-fogbugz-40-part-ii/
word_count: 1445
---


A long time ago I wrote an article called [What is the Work of Dogs in this Country?](https://www.joelonsoftware.com/articles/fog0000000012.html) about the benefits of eating your own dogfood, a quaint expression in the software industry that means “using your own product.”


We’re totally devoted to the idea of using our own software as much as possible… all my writing is done inside [CityDesk](http://www.fogcreek.com/CityDesk) (a very unstable developer build, at that, which drives everyone completely crazy), all our development is planned and tracked in [FogBugz](http://www.fogcreek.com/FogBugz), of course, and even our customer service operation is entirely supported and tracked with FogBugz, which is why when you email us you always get a reply.


Well, almost always.


About a year ago, I noticed that people were emailing us, sometimes, and not getting responses.


This was not good.


I dug up their messages in FogBugz.


RESOLVED: SPAM, it said. Someone handling the customer service queue had decided that the email was spam and closed it without responding.


When I looked closer, it was usually because the subject line sounded kinda spammy or was blank, but sometimes it was just the proverbial Operator Error.


In the meantime I had been using [SpamBayes](http://spambayes.sourceforge.net/) for my own personal email. This is probably the best implementation of what is probably the best spam filtering algorithm out there: Bayesian filtering, invented by [Paul Graham](http://www.paulgraham.com/) and first published in August 2002 in his seminal article [A Plan for Spam](http://www.paulgraham.com/spam.html). Bayesian filtering learns from experience. When it makes a mistake trying to classify an email as spam or non-spam, you correct it, and it looks for clues in that message so it can do a better job at classification in the future.


And I thought, gosh, here I am paying a* college graduate* to go through email and decide whether or not it’s spam, and he’s flagging 1% of email incorrectly, when there’s this algorithm called Bayesian filtering which in my experience has far fewer false positives (something like 0.01% false positives). So while everybody is worried about how spam filters might inadvertently delete the proverbial *crucial email from a customer,* in practice, in the presence of lots of spam, human beings are far more likely to delete a real email than a well-implemented Bayesian filter.


The other thing about the Bayesian algorithm, by the way, is that it has to be implemented in the email *client*, not the server, because it needs to be taught about what one particular person’s legitimate email looks like. For example when we get email at Fog Creek, the word “FogBugz” in the body of the email is strong evidence that the email is not spam while the word “mortgage” in the body of the email is strong evidence that the email *is* spam. However if you’re a real estate agent or bank, the word mortgage probably occurs all the time in legitimate email. So basically Bayesian filtering is not going to work unless it knows what messages you deleted as spam and which suspicious messages you recovered. The Ipswitch guys who make a mail server tried to implement Bayesian filtering on the server, because that’s what they have, and frankly that system just doesn’t work.


Since spam filtering needs to be done on the client, and FogBugz is an email client, we decided that spam filtering needs to be done in FogBugz.


Now, all that probability stuff is too hard for me, so we asked Summer Intern Ben Kamens to figure it out. In a matter of weeks he had a beautiful, speedy implementation of Bayesian filtering up and running in FogBugz.


Bayesian filtering is really just a specialization of a long established AI algorithm for sorting documents based on training, and we thought, gosh, why not generalize the algorithm so that in addition to sorting incoming email into “spam,” “suspect,” and “ham,” it also sorted all the ham into piles, for example, “sales,” “tech support,” and “job applications”?


Ben spent a few more weeks studying this and came up with the idea of using a tournament algorithm. He’s a college athlete. They think of the world in terms of tournaments. It worked quite well. With 24 hours of training I had it sorting my own inbox into personal email, Fog Creek email, *Joel on Software* email, Joel on Software translator coordination email, Subversion checkin comments, bug notifications, and sales reports. Frankly it did an astonishingly good job with 100% accuracy on the obvious emails, like the checkin comments that all had the same structure, and well over 90% accuracy on the hard ones, like telling personal email from *Joel on Software* reader mail.


I was tempted to try and get it to sort email into messages from Republicans vs. messages from Democrats, but that was pushing my luck.


By the way, the paper Ben wrote at the end of the summer describing his algorithm is [here](http://www.fogcreek.com/FogBugz/Downloads/KamensPaper.pdf) (PDF). This paper is the ultimate rebuttal to those grumpy people who email me, barely able to conceal their disgust, saying, “why do you need to hire such smart people to work on *bug tracking software*?”


The cool thing about the implementation in FogBugz is that if the sorter makes a mistake, it’s OK. You just correct it and get on with your life, and it learns from its mistake. But in the meantime it saves you 95% of the work directing incoming email to the right people.


**Snippets**


We got one other good idea for FogBugz 4.0 from dogfooding it.


As long as FogBugz has had the ability to receive mail, all customer service email sent to Fog Creek goes into our own FogBugz database where anyone can answer it.


Over time I’ve come to notice the occasional customer who thought we were being rude to him in an email message. On closer examination, we weren’t being rude, but the email we sent *seemed* rude, and it was usually because it was incredibly terse and to-the-point. We decided that instead of sending emails like:


> Yep, this is fixed in the latest version.


… we should be sending emails like:


> Hi! Thanks for writing to us. I think I know what you’re talking about, and it’s definitely a bug in our product. The good news is: it’s fixed! You can download the latest version by logging onto our online store at [https://shop.fogcreek.com](https://shop.fogcreek.com/) with your order ID number and email address, and that should solve this problem once and for all. If you don’t have your order ID number just let me know and I’ll be happy to look it up for you, or call us here at the Fog Creek office at 866-FOG-CREEK.
> Please let me know if there’s any other way I can be of assistance!
> All the best,
> (signature of a real human being)


It’s sort of like translating from English to Japanese. I have never been to Japan but my father, a linguist, once told me the story of the train station in Tokyo, where the announcements were made in Japanese and English. You would hear four or five minutes of nonstop Japanese and then the English translation would be “The train to Osaka is on platform 4.” It seems that in Japanese there is simply no way to say something that simple without cosseting it heavily in a bunch of formal etiquette-stuff. And it turns out the same thing applies to email messages, even in English. The moral of the story is that given two email messages with the same semantic content, the terse one is more likely to come across sounding rude. But given the amount of email correspondence we have to deal with here, we don’t have time to be Emerson on every customer support email.


Thus was born the idea of snippets: canned bits ‘n’ pieces of email that you could insert into an outgoing reply with a few keystrokes. The theory is that you define a snippet like “Please let me know if there’s any other way I can be of assistance” and then assign it to a short code like “2”. Now while your composing your reply, you just hit 2 and then press the backquote key ` and (ding!) it is instantly replaced with the long text it represents right in front of your eyes. It’s really cool and it saves a ton of time and allows us to produce the verbose email replies that are less likely to be misinterpreted. We have built up an extensive library of snippets for all kinds of “faqs” and common parts of email messages.


In tomorrow’s installment of The Road to FogBugz, a look at Thistle, our proprietary ASP to PHP compiler/translator.
