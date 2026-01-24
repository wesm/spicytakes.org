---
title: "Oh, You Wanted “Awesome” Edition"
date: 2009-07-01
url: https://blog.codinghorror.com/oh-you-wanted-awesome-edition/
slug: oh-you-wanted-awesome-edition
word_count: 1028
---

We recently upgraded our database server to 48 GB of memory – because  [hardware is cheap, and programmers are expensive](https://blog.codinghorror.com/hardware-is-cheap-programmers-are-expensive/).


Imagine our surprise, then, when we rebooted the server and saw only 32 GB of memory available in Windows Server 2008. Did we install the memory wrong? No, the BIOS screen reported the full 48 GB of memory. In fact, the system information applet even reports 48 GB of memory:


![](https://blog.codinghorror.com/content/images/2025/04/image-396.png)


But there’s only 32 GB of *usable* memory in the system, somehow.


![](https://blog.codinghorror.com/content/images/2025/04/image-395.png)


Did you feel that? A great disturbance in the Force, as if 17 billion bytes simultaneously cried out in terror and were suddenly silenced. It’s so profoundly sad.


That’s when I began to suspect the real culprit: **weasels**.


![](https://blog.codinghorror.com/content/images/2025/04/image-394.png)


No. Not the cute weasels. I’m referring to angry, evil ***marketing* weasels**.


![](https://blog.codinghorror.com/content/images/2025/04/image-393.png)


That’s more like it. Those marketing weasels are *vicious*.


We belatedly discovered post-upgrade that we are foolishly using Windows Server 2008 **Standard** edition. Which has been [arbitrarily limited to 32 GB](http://www.sadtrombone.com/) of memory. Why? So the marketing weasels can [segment the market](http://www.joelonsoftware.com/articles/CamelsandRubberDuckies.html).


> It’s sort of like if you were all set to buy that new merino wool sweater, and you *thought* it was going to cost $70, which is well worth it, and when you got to Banana Republic it was on sale for only $50! Now you have an extra $20 in found money that you would have been perfectly happy to give to the Banana Republicans!
> Yipes!
> That bothers good capitalists. Gosh darn it, if you’re *willing to do without it*, well, give it to me! I can put it to good use, buying a SUV or condo or Mooney or yacht one of those other things capitalists buy!
> In economist jargon, capitalists want to capture the [consumer surplus](http://en.wikipedia.org/wiki/Consumer_surplus).
> Let’s do this. Instead of charging $220, **let’s ask each of our customers if they are rich or if they are poor. If they say they’re rich, we’ll charge them $349. If they say they’re poor, we’ll charge them $220.**
> Now how much do we make? Back to Excel. Notice the quantities: we’re still selling the same 233 copies, but the richest 42 customers, who were all willing to spend $349 or more, are being asked to spend $349. And our profits just went up! from $43K to about $48K! NICE!
> Capture me some more of that consumer surplus stuff!


How many versions of Windows Server 2008 are there? I count at least six. They’re capturing some *serious* consumer surplus, over there in Redmond.

- Datacenter Edition
- Enterprise Edition
- Standard Edition
- Foundation
- Web
- HPC


Already, I’m confused. **Which one of these versions allows me to use all 48 GB of my server’s memory?** There are no less than six individual “compare” pages to slice and dice all the different features each version contains. Just try to make sense of it all. I dare you. No, I double dog dare you! Oh, and by the way, there’s *zero* pricing information on any of these pages. So open another browser window and factor that into your decision making, too.


I don’t mean to single out Microsoft here; lots of companies use this segmented pricing trick. Even Web 2.0 darlings [37 Signals](http://www.basecamphq.com/signup).


![](https://blog.codinghorror.com/content/images/2025/04/image-392.png)


Heck, our very *own* product [segments the market](http://stackexchange.com/).


![](https://blog.codinghorror.com/content/images/2025/04/image-391.png)


37signals just does it... prettier, that’s all. They’re still asking you if you’re poor or rich, and charging you more if you’re rich.


Eric Sink also advocates the same “rich customer, poor customer” [software pricing policy](http://www.ericsink.com/bos/Product_Pricing.html):

kg-card-begin: html

> In an ideal world, the price would be different for every customer. The “perfect” pricing scheme would charge every customer a different amount, extracting from each one the maximum amount they are willing to pay.
> The IT guy at Podunk Lutheran College has no money: Gratis. 
> The IT guy at a medium-sized real estate agency has some money: $500. 
> The IT guy at a Fortune 100 company has tons of money: $50,000. 
> You can never make your pricing “perfect,” but you can do much better than simply setting one constant price for all situations. By carefully tuning all these details, you can **find ways to charge more money from the people who are willing to pay more**.

kg-card-end: html

This sort of pricing seems exploitative, but it can also be [an act of public good](https://blog.codinghorror.com/world-zone-pricing/) – remember that the *poorest* customers are paying less; with a one-size-fits-all pricing policy, they might not be able to afford the product at all. Drug companies often follow the same pricing model when selling life-saving drugs to third-world countries. First-world countries end up subsidizing the massive costs of drug development, but the whole world benefits.


What I object to isn’t the money involved, but the mental overhead. The whole thing runs so contrary to the spirit of [Don’t Make Me Think](https://blog.codinghorror.com/dont-make-me-think-second-edition/). Sure, don’t make us customers think. Unless you want us to think about **how much we’d like to pay you**, that is.


And what are we paying for? The privilege of flipping the magic bits in the software that say “I am *blah* edition!” It’s all so... anticlimactic. All that effort, all that poring over complex feature charts and stressing out about pricing plans, and for what? Just to get the one simple, stupid thing I care about – using all the memory in my server.


Perhaps these complaints, then, point to one unsung advantage of open source software:


**Open source software only comes in one edition: *awesome*.**


The money is irrelevant; the expensive resource here is my brain. If I choose open source, I don’t have to think about licensing, feature matrices, or recurring billing. I know, I know, [we don’t use software that costs money here](https://blog.codinghorror.com/we-dont-use-software-that-costs-money-here/), but I’d almost be willing to pay for the privilege of not having to think about that stuff *ever again*.


Now if you’ll excuse me, I’m having trouble deciding between Windows 7 Smoky Bacon Edition and [Windows 7 Kenny Loggins Edition](http://www.penny-arcade.com/comic/2007/02/02/). Bacon is delicious, but I *also* love that [Footloose](http://www.imdb.com/title/tt0087277/) song...

[hardware](https://blog.codinghorror.com/tag/hardware/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[server configuration](https://blog.codinghorror.com/tag/server-configuration/)
[windows server](https://blog.codinghorror.com/tag/windows-server/)
[licensing restrictions](https://blog.codinghorror.com/tag/licensing-restrictions/)
