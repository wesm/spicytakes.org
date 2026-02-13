---
title: "The Road to FogBugz 4.0: Part I"
date: 2005-03-28
url: https://www.joelonsoftware.com/2005/03/28/the-road-to-fogbugz-40-part-i/
word_count: 1135
---


It started with a phone call from a customer, back in the old office.


Most of our customers, thankfully, understand that the idea here at Fog Creek is to make shrinkwrapped, off-the-shelf software that you buy for a low price and it already does what you need, and if it doesn’t, well, we’d like to hear about that, but for $99 you’re not getting a customized version of the software, sorry.


Some of our customers still think we’re one of those big enterprise software companies where you call them up, negotiate with a salesperson for three months, and, on the last day of the fiscal quarter, force the salesperson to promise a long list of new features in exchange for a half-million dollar contract.


That’s nice, but we don’t have salespeople and we’re not one of those vendors. Our customers are happy that our price point is low but not all of them quite understand the implications. They ask us to fly out to their headquarters to give a demo of the software to their development team. They send us long spreadsheets with lists of features and ask us to check off the features we support. They even send us RFPs (shudder). RFP stands for “Request for Proposal.” It’s a request by a large company for a custom proposal from a small company. The small company works on the 200 page laser-printed proposal like mad for three weeks and Fedexes it in great expense and at the last minute, where it gets put in the trash because the large company has their favorite vendor who takes them on a helicopter to Atlantic City on junkets involving blackjack and strippers, and who is going to get the contract no matter what, but someone in purchasing *for some unexplained reason, maybe he’s bucking for a promotion *is insisting that the proposal be opened up to “competitive bidding” and the small company has been chosen as a victim to write up a proposal that has no chance of being accepted just to make the process look a little bit less corrupt, and if you’re a small company, I would recommend that you don’t fall for it and don’t spend any time responding to RFPs unless it’s already understood that you’re going to get the contract.


ANYHOO.


The good thing about such customers is that they give us useful feedback about what features we should be adding to FogBugz. One of our [mantras](http://discuss.fogcreek.com/newyork/default.asp?cmd=show&ixPost=3245&ixReplies=15) here at Fog Creek is “Listen to your customers, not your competitors.” So when we get calls from potential big customers we listen.


Back then, early in the planning stages of FogBugz 4.0, the call was from a large not-for-profit organization. They were considering using so many copies of FogBugz that they needed a way for department managers to see their own departments’ cases in one place, even when each department managed multiple projects.


The short term solution would have been for us to add a table of departments and make a report based on departments. But we’re an off-the-shelf company, and when we do something, we want to do it in a general way that’s useful to a lot of customers. So we took a little bit more time and designed a more general feature and solved a large class of customer problems with one feature. In addition to customers who wanted things sorted out by department, we had customers who were typical consulting shops and wanted to sort things out by client. Most of these customers wanted privacy features so their clients could access FogBugz without seeing any *other* clients’ bugs. And many of our customers were small shops with ten or twenty users who couldn’t care less about departments, clients, or privacy features, so whatever we did needed to be implemented in a way that would have zero impact on customers who didn’t care. The last thing we need is for FogBugz to become big and unwieldy because it has a lot of features and fields you don’t care about.


So, OK, it took a little bit of time to deliver this feature to this particular customer. From that phone call to the time we delivered an alpha release to the customer with the new feature about twelve months elapsed. That’s more because we’re still oriented around big major releases every year and a half. I justified the reason for this schedule in the article [Picking a Ship Date](https://www.joelonsoftware.com/articles/PickingShipDate.html).


Many of the other features in FogBugz 4.0, which we finally shipped on February 22, were based on customer feedback, too. We kept hearing customers asking how to attach screenshots to a bug. “Oh, it’s easy,” we said. “Alt+Print Screen, run paintbrush, paste, save as a file somewhere, run your browser, go to the FogBugz homepage, hit “New Case,” describe the case, click the file browse button, and find the file you just created.” What could be easier?


Maybe it could be a *bit* easier.


Finally I thought “how hard could it be to make a little taskbar lint icon thingy that grabs a screenshot and makes a bug out of it?” Not so hard.


I got the Windows version done in The Proverbial Weekend (defined as one weekend to get it working, two weeks to fix bugs, another week to rewrite it to workaround new bugs introduced by a patch to Internet Explorer). [Daniel Berlinger](http://archipelago.phrasewise.com/) knocked out the Macintosh version in [REALbasic](http://www.realsoftware.com/) in a couple of weeks. And now entering a bug that you see on screen is a matter of two clicks.


It’s great.


I’ve found that about 30% of the bugs I enter can be completely described with a screenshot. Here’s a complete bug report I entered on Monday:


The red rectangle comes from a highlight tool built into the screenshot program. The “wha?” I typed was probably overkill. If I had been willing to live with an untitled bug this entire bug report could have been entered with four clicks and a drag (that sounds like a good name for a band: “Four Clicks and a Drag.” Or the Fog Creek development team, now that I think of it.)


The thing is, as far as I know, not that I pay close attention, *none* of our competitors has this feature.


If one of our competitors think this is cool, they can copy us, but it’ll take them a while, especially if they read my site and bought my line about only shipping every 18 months.


No amount of listening to our competitors would have motivated us to do a screenshot feature. Our customers didn’t think to ask for it, but we did notice that they kept asking for ways to attach screenshots, so that’s what we did.


Come back tomorrow for Part II, in which I talk about dog food.
