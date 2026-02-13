---
title: "Why eBay Bought Skype"
date: 2005-10-25
url: https://www.joelonsoftware.com/2005/10/25/why-ebay-bought-skype/
word_count: 505
---


What caused me to fly off the handle about architecture astronauts was, indeed, [this conference](http://usv.jot.com/WikiHome/PublicWiki/Sessions), organized by Union Square Ventures, a local VC. You can try to [read the transcript online](http://usv.jot.com/WikiHome/PublicWiki/Sessions/Sessions1Fulltranscript/usvsessions1_fulltranscript_ref.doc/!converted/index.html) and see why I was so agitated, or just read the post-mortem, including my ungracious comment, on [USV’s blog-site](http://www.unionsquareventures.com/2005/10/we_dont_get_it.html).


I had to install [Lisp in a Box](http://common-lisp.net/project/lispbox/) and start working through [Seibel’s new book on Common Lisp](http://www.amazon.com/exec/obidos/ASIN/1590592395/ref=nosim/joelonsoftware) until my brain started functioning again.


**eBay and Skype**


Here’s my highly irresponsible, off-the-cuff theory of why [eBay bought Skype](http://news.com.com/eBay+to+buy+Skype+for+2.6+billion+in+cash,+stock/2100-1030_3-5860055.html), because none of us believes that nonsense about how this would “allow people to talk to each other during auctions.” (Hint: eBay didn’t need to buy Skype just to allow people to talk to each other during auctions. Skype worked fine for that purpose without being owned by eBay. So that couldn’t possibly be the reason).


My theory goes like this.


EBay generates a lot of profit, which gives them a lot of cash, which they have to reinvest somehow or else give it back to the shareholders. If they give it back to the shareholders, the executives at eBay won’t be able to justify their ginormous salaries. So that leaves reinvestment.


A lot of big, profitable tech companies — Amazon, Microsoft, and Google — especially Google — hired carefully and have very good software development organizations. Especially Google. When they have extra money, they try to build something new. Whether it’s A9, .Net, or Gmail, it’s designed and built in-house in hopes of getting into a new business.


But eBay somehow got taken over by a swarm of MBAs way too soon and became an organization that was basically incapable of developing software. The evidence for this is the whole BillPoint/PayPal fiasco, in which eBay tried to create their own payment system, BillPoint, but found themselves so constitutionally incompetent at creating software by themselves that a scrappy team of outsiders at PayPal made a system that eBay users preferred 2 to 1, despite the fact that eBay repeatedly tried to force auctioneers into using BillPoint instead. (Eric Jackson wrote a very good book about it, [The PayPal Wars](http://www.amazon.com/exec/obidos/ASIN/0974670103/ref=nosim/joelonsoftware).)


Full credit to eBay for recognizing their weakness, though. Since eBay realized they couldn’t build things, they have to use their cash to buy things instead. This is what MBAs like to do anyway. They don’t completely understand how to make companies but they do enjoy buying and selling them.


Good for eBay. The only problem is that this kind of acquisition, especially combined with Google’s blockbuster IPO, is leading people to think there’s a new bubble underway somehow, which is causing investors to try and figure out if del.icio.us (say) might be the next Skype because they’re both “Peer Production” or something. Hint: Skype has nothing to do with del.icio.us. Nothing. I don’t care if you manage to come up some architectural abstraction with that seems to include both. It’s not going to make del.icio.us worth $2.6b, because del.icio.us, *architecturally*, doesn’t have that “free phone call” feature.
