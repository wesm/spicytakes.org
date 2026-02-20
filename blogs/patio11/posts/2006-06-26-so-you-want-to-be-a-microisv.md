---
title: "So you want to be a microISV"
date: 2006-06-26
url: https://www.kalzumeus.com/2006/06/27/so-you-want-to-be-a-microisv/
slug: so-you-want-to-be-a-microisv
word_count: 1498
---


Recently I’ve been investigating the possibility of starting a micro independent software vendor (mISV, apparently). This involves a heck of a lot of work which is not strictly related to getting your software finished and bug free. Assuming you can pass that hurdle, here’s some other stuff you might want to get a handle on:


Web site: You absolutely, positively need a web site to promote your software. It will probably also be your number one sales channel. Even if you have additional channels (for example, if you manage to hammer out a distribution detail with a portal) the fact that you’ll get so much more money from sales at your own website makes it well worth your trouble to spend some time and money setting up the site.


Web hosting is a commodity business nowadays. After a little poking around the Internet, it seems [www.godaddy.com](http://www.godaddy.com) is about as good a choice as anyone. You get your domain name for about $2 with a hosting contract (2 month minimum) and their cheapest hosting plan gets you 250 GB of transfer for $4 a month. If you need CGI, for example for customer tracking or to implement your own web store, you’ll want to upgrade to their next higher hosting plan for a whopping $7 a month. Warning: When it comes to support and dispute resolution you probably get what you pay for here. If your venture takes off you might want to move to a web host where you’d actually rate enough importance to get a live representative if you call in… but lets not get ahead of ourselves, shall we?


Web site development: “Hey, I can do this by myself on notepad!” Well, I suppose you could… if this were 1996. In 2006, having a nice professional looking website is a) not very expensive and b) worth its weight in gold when you’re trying to convince someone to hand over their credit card number to you. I have no particular recommendation on a web designer, but get somebody who can build you a nice extensible site with CSS so you can add additional pages in the same style yourself. I suppose you could cut corners and use one of the default templates that comes with, say, OSS blogging software… but would YOU purchase something from a page like that? Budget $100 as the bare minimum and likely a bit of a multiple of that.


Marketing: So you’ve got a web site hosted somewhere on the Internet. Thats great. What are you missing? Customers. With no userbase to start out with you’re cut out of the most important marketing tool: word of mouth. Thus, to get the ball rolling, you’re going to be relying on the world’s largest marketing firm: [www.google.com](http://utility.kalzumeus.com//www.google.com) . First, you need to optimize your site so that its maximally search-engine friendly. There’s gigabytes of good advice and sheer voodoo written about how to do this on the Internet. I’ll give you the five second summary: make sure everything on your site is tagged in machine-readable format (alts on your images, etc), never miss a chance to provide natural language information (filenames and URLs should be human readable and descriptive of content, your TITLE tag should include your keywords in addition to your company name), and have the keywords that your users will be searching for in your site (if, for example, your users are non-technical then make sure the non-technical gloss of what your software does appears somewhere in, say, a FAQ page).


Then your other, likely more productive option, is [Google AdWords](https://adwords.google.com/select/main?cmd=Login&sourceid=AWO&subid=US-ET-ADS&hl=en_US). Here’s how it works: you come up with a text ad which points at your site, and you hand it to Google along with a list of keywords which you want that ad to appear with. If someone searches a combination of your keywords, Google will hold an automated auction between you and the other people aiming for that keyword, and show adds for the folks offering the most money. You pay per click (or per thousand impressions if you target a particular site — more on that later). For a keyword with vanishingly little competition, AdWords is *dirt cheap* — a penny per click. For keywords with lots of competition and/or high value keywords (“online casino”), they’re much more expensive (I hear some are in the $10+ dollar range, mostly for legal services). If you’ve choosen your software niche well, you’ll be going up against moderate competition with your main phrases and, this is key, *no competition* on phrases folks search but haven’t thought to market to yet. Let me give you an example. Say you make software which, to continue my example from below, teaches Japanese. Yay for you. “Japanese software” has lots of bidders. “Teach yourself Japanese” has exactly one ad displayed for it. “Japanese language game”, “Teach yourself kanji”, “Kanji game”, “Japanese edutainment”, “Japanese practice”, etc, have NO ads displayed for them. This means you can pick up these searches for a song (a penny per click). Then your ad takes them right to your sales presentation, which has in big bold type your two actions you want them to take: downloading the demo and purchasing the software.


Software deployment: I originally thought of spending a couple of hundred dollars on [Installshield](http://www.installshield.com/), which is an industry-standard installer program. Here’s the rub: why spend a couple hundred dollars when you can get something functionally identical and very professional looking for free. And legally, too! Take a gander at the Nullsoft Scriptable Install System, a GPLed piece of software (don’t worry, you can wrap commercial software with it without any license issues). Wouldn’t you want your installer to look something like one of [these](http://http://nsis.sourceforge.net/Screenshots)? Yeah, thought so.


Incidentally, I’m a Java developer. Java development can be risky for an mISV, because you can’t be sure that folks will have the JRE that you need installed, and folks might not understand the whole “click on this jar” concept. You can make this a much simpler concept for them by adding a native executable to wrap your JAR. Ideally, this executable would detect if they had no JRE or if their JRE were insufficient (if, for example, you are addicted to Java 1.5 and can’t write two lines of code without creating a HashTable) and then take them straight to Sun’s site to fix the problem. Haha, such a program also exists, and its free! Try out [Launch4j](http://launch4j.sourceforge.net/), and watch your conversion rate soar as you take the hassle out of the critical “launching the bloody program” step. There are some other nice features, such as being able to display a native splash screen while loading the JRE (nice for those of us mildly concerned that Java, while being a quite responsive language during runtime, can be a bit… slow… when loading), and builds nicely from an ant task.


Payment processing: OK, so you’ve got folks to your website, they’ve downloaded your demo, and they’re ready to hand you money! Thats great. How can they get you the money?


Well, option #1 is you get yourself a credit card merchant account. This can be a bit on the expensive side for startup costs, you’ll have to pay a monthly maintenance fee, and you’ll need some web facing and backend software to handle billing. All in all, not a whole lot of fun. On the plus side, this is absolutely the cheapest option in terms of the rake the payment processor will take (figure on ~$.50 + 2%).


Your other option is working with a payment processor. I’ve been able to locate three, which have very little functional differentiation from my perspective (since I’m just looking for the very simple “process my payments and mail out serial numbers, I’ll handle the rest myself” service rather than any of their overpriced shopping cart/DRM/etc offerings). Here’s the links and prices:


```
www.shareit.com : $2.95 + 5% *or* min(2.50, 14.9%). No setup fee.
```


```
www.esellerate.com : 10% "trial" offer, scales to $15k yearly sales.
Then 15% and declining based on sales
```


```
www.regsoft.com: min($3.00, 8.9%).  $10 setup fee.
```


You can do the math on which is cheapest at your price point and expected level of sales. I personally will be launching something within the next few weeks at $15, and www.esellerate.com wins at that level by a significant amount, but if you’re planning on doing significant levels of business (say, in the $30k per year range) on more expensive program (say, $40) their 15% fee is going to lose to either of the other options.


Note there is a bit of vendor lockin here: while you won’t strictly speaking be contractually obligated to only use their service transferring your serial numbers, customer data, and registration schemes to another system after having used one of them for a while will burn up a LOT of your time. The creator of Lux, a rather successful Risk clone, has some great words about this [here](http://randomdude.com/blog/threads/1199-Internet-payment-services-and-associated-ramblings).
