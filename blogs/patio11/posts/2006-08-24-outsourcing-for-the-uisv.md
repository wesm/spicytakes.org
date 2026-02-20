---
title: "Outsourcing for the uISV"
date: 2006-08-24
url: https://www.kalzumeus.com/2006/08/25/outsourcing-for-the-uisv/
slug: outsourcing-for-the-uisv
word_count: 995
---


Recently, on the Business of Software board (an excellent resource, by the way), there was a [discussion about using stock icons](discuss.joelonsoftware.com%2Fdefault.asp%3Fbiz.5.379877) for your application.  Some folks turned up their noses at paying $29.95 for stock icons when you could do them yourself for free.  And I suppose you could.


My question is what you’d have to be smoking to want to.  Your time as an ISV is severely limited and there are several demands on it: programming the next version of your software, marketing marketing marketing, optimizing your AdWords campaign, rewriting your website, answering customer inquiries, and doing all the things in your life that don’t happen in front of a computer screen.  Presumably you’re good at all of these things or you wouldn’t have decided to go into this business.  For things you are less good at, outsource them.  Now.


Here’s a couple of things that strongly suggest to me “Yep, I should let somebody else do that”.


**No customer will be able to tell the difference**.  I would never outsource support or customer service for the simple reason that people hate, hate, hate that.  Doing it all myself lets me brag on my website that people can get an answer “straight from the top” and I think the personal connection (or potential for one) is one of the primary advantages of this form of business.  Similarly, I wouldn’t outsource programming the key features of my program (e.g. the logic which controls printing).  But everything else is fair game.


**The cost of outsourcing is lower than the cost to even consider whether you’re capable of insourcing**.  I pay e-junkie $5 a month for them to handle [Paypal IPN notifications](http://www.e-junkie.com) for me (receive notice from Paypal that someone has paid me, send out an email to the customer with their serial number).  I’m not a web programming guru but I’m pretty certain I could whip up a Perl script to do this… but, crickeys, **$5 a month**.  I know it will take me hours of researching the IPN spec, brushing up on my perl syntax, looking at code snippets, etc etc, before I even start coding my version.  And e-junkie is already there… for ***$5*** a month.  This is a no-brainer.


**The outsourcing would result in higher quality than insourcing**.  This is why I spent $29.95 on the [Roma icon set](http://www.icons-icons.com) yesterday (price good to the end of August, incidentally — you might consider taking advantage of it).  I’m not an artist — the one thing in my life I have ever successfully drawn is a goomba (little mushroom monster from Mario which requires about 5 pencil strokes, for those people who have lived under a rock for the past twenty years).  Meanwhile, the stock icons look professionally done (because they are, naturally), they stand out vibrantly when compared to the (free) stock Java icons I had been using previously, and they’ll make my screenshots leap off the page.  I remember how much of an impact the graphical design of Direct Access had on me — it was stylish and professional looking, and I think bringing that flavor to Bingo Card Creator will generate at least two marginal sales over the next 10,000 downloads, which would pay off the investment handily.


Speaking of stock icons, somebody cooked up this resource: [stock icons review](http://www.iconsreview.com/).  Its probably the only example of a socially beneficial AdSense site I’ve seen: it aggregates information which is of genuine use to someone looking for stock icons, such as a list of a few dozen players, their prices and formats, and a save-you-hours-of-looking estimation of their quality.  And in return it has AdSense ads (for stock icons, naturally) and affiliate relationships with a lot of the icon producers (check for the links which point to tinyurl).  I hope the site makes the author a mint, to encourage folks to actually create value with AdSense rather than just spamming the entire Internet with, e.g., automatic scrapings from blogs.


**You wouldn’t pay yourself $5/hr to do the work**.  Are you tempted to code a minor component yourself instead of just buying something which will do it for $19.95?  Try this little experiment: put a cookie jar next to your computer.  Now, take $5 out of your pocket every hour on the hour and put it into the cookie jar.  The point of this excercize is essentially to demean and annoy you: first, you’re really worth a lot more than $5 an hour (and should return to the tasks where you’ll make more than that), second, $5 is an inconvinient denomination which will have you constantly trying to make change.  Have you ever noticed that computer programmers can’t tolerate 15 seconds of nuisance an hour but will happily spend man-weeks reinventing the wheel?  This way, you get to internalize that annoyance and do what you should do, which is abandon the trivial task to the person who already solved it and get back to what makes your business special.


I did the cookie jar trick (although I used a plastic cup, since I don’t own a cookie jar) for my newest feature: implementing a font chooser.  I was pretty sure I could do it myself rather than just adapting pre-existing code (which was available for an attractive license: give me credit in the documentation and its yours).  After 1000 yen was in the cup (in 100 yen coins, five an hour) I surrendered and just downloaded [this guy’s solution](http://www.java2s.com/Code/Java/Tiny-Application/Afontselectiondialog.htm).  I ended up extending that code a bit (I finished off his todo list, added in sane default choices for the font, and improved the time complexity of initialization) but I estimate I probably saved six hours even counting the two I wasted due to stubbornness.  And its time saved writing Java GUI code, which on the scale of “tasks which I relish” falls right between taking out the trash and cleaning the bathroom.


Incidentally, the 1,000 yen stupidity tax is lunch today.  I’m thinking chicken.
