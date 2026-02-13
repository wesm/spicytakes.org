---
title: "Fixing Venture Capital"
date: 2003-06-03
url: https://www.joelonsoftware.com/2003/06/03/fixing-venture-capital/
word_count: 2690
---


Many software companies these days are built using some form of venture capital. But the VC  industry has been hurting lately. A lot of investments in dotcoms turned  out to be spectacular flameouts. As a result, VCs are becoming ever more  selective about where to put their money. To get funded these days, it’s not enough to  be a pet shop on the web. Nope! You have to be a pet shop on the web  *with 802.11b wireless hotspots,* or your business plan is going right in  the dumpster.


The formerly secretive world of VC has become a  bit more transparent, of late. VCs like Joi Ito, Andrew Anker, David Hornik, and Naval Ravikant have created weblogs which  are a great source of insight into their thought process. That dotcom thing  resulted in three great books by company founders that look deep inside the process  of early stage financing (see footnote). But as I read this  stuff, as a founder of a company, I can’t help but think  that there’s something wrong with the VC model as it exists today. Almost every page of these  books makes me say, “yep, that’s why Fog Creek doesn’t want venture capital.” There  are certain fundamental assumptions about doing business in the VC world that make venture  capital a bad fit with entrepreneurship. And since it’s the entrepreneurs who  create the businesses that the VCs fund, this is a major problem. Here’s  my perspective on that, from a company founder’s point of view.


When people ask me if they should seek venture  capital for their software startups, I usually say no. At Fog Creek Software, we have never  looked for venture capital. Here’s why.


The fundamental reason is  that VCs do not have goals that are aligned with the goals of the  company founders. This creates a built-in source of stress in the relationship. Specifically,  founders would prefer reasonable success with high probability, while VCs are looking  for fantastic hit-it-out-of-the-ballpark success with low probability. A VC fund will invest in a lot  of startups. They expect about seven of them to fail, two of them to trudge  along, and one of them to be The Next Netscape (“TNN”). It’s OK if seven fail, because  the terms of the deal will be structured so that TNN makes them enough money to  make up for all the losers.


Although the real spreadsheets are many megabytes long and quite detailed, this is  the VC’s calculation:



| A | Probability of Success | 10% |
| B | How rich I would get | $1,000,000,000 |
| C | Expected Return (A x B) | $100,000,000 |



But founders are much more conservative than that. They  are not going to start ten companies in their lifetime, they’re going to start,  maybe, two. A founder might prefer the following model:



| A | Probability of Success | 80% |
| B | How rich I would get | $100,000,000 |
| C | Expected Return (A x B) | $80,000,000 |



Even though the second model has a  lower expected return, it is vastly preferable to most founders, who can’t diversify  away the risk, while VCs who invest in dozens of businesses would prefer the  first model because it has a greater return. This is just Econ 101; it’s the same reason you buy car insurance and Hertz  doesn’t.


The difference in goals means that VCs are always going  to want their companies to do risky things. Oh, sure, they’ll deny it, but if  they were really looking to do conservative risk-free things, they’d be  investing in U.S. Treasuries, not optical networking companies. But as an  entrepreneur, you’re going to be forced at gunpoint to bet on three cherries  again and again and  again. You know you’re going to lose, but the gunman doesn’t care, he’s got bets  on all the slot machines and one of them is going to pay off big  time.


There’s nothing controversial here. A VC would say,  “that’s what VC is *for:* investing in risky ideas.” Fair enough. As long  as the entrepreneur *wants* to take a 10% chance, VC may be the way to  go. The trouble here is that the VC is now doing a perverse kind of selection.  They are looking for the founders with business ideas where the founders  themselves think the idea *probably won’t work. *The end result is that  VC money ends up being used in bet-the-farm kind of ways. This kind of  recklessness causes companies like WebVan to [blow](http://sfgate.com/cgi-bin/article.cgi?f=/c/a/2001/07/09/MN196371.DTL)  $800,000,000 in a rather desperate attempt to *buy* a profitable business  model. The trouble is that they were going so fast that they didn’t have time to  learn how to spend money in a way that has a positive return, which is, by definition, what you have to do to be  profitable.


Here’s my [philosophy](https://www.joelonsoftware.com/articles/fog0000000056.html)   of company growth. A growing company looks like  this:


Oh, wait, I forgot to define the Y axis. Let’s assume this curve is my  revenues:


There are some other things which grow at roughly the same speed. For example, the number of  employees:


And the number of people who have heard of your product, which we’ll call  “PR”:


There’s also the “quality of your code”  curve, based on the theory that good software takes [ten years](https://www.joelonsoftware.com/articles/fog0000000017.html)           .


I’ve drawn these curves moving up at roughly  an equal rate. That’s not a coincidence. In a small company, you regulate each  of these curves so they stay roughly in sync. Why? Because if any two of those  curves get out of whack, you have a big problem on your hand—one that can kill your company. For  example:

1. **Revenues grow faster than you can  hire employees.** Result: customer service is inadequate. Let’s [tune  in](http://www.cloudmark.com/support/spamnet/forum/read.php?f=11&i=1392&t=1392) to Alex Edelstein over at Cloudmark: “[Cloudmark Sales are] pretty swamped,  so they’re not getting back properly to everyone…. What’s happening here now  at Cloudmark is a little like the early days at Netscape when we just had too few people to properly respond to the customer  interest.”

**Revenues grow slower than you  hire employees.** Result: you burn cash at a ridiculous rate and go out of business. That’s an easy  one.

**PR grows faster than the quality  of your code.**  Result: everybody checks out your code, and it’s  not good yet. These people will be permanently convinced that your code is simple  and inadequate, even if you improve it drastically later. I call this the [Marimba phenomenon](https://www.joelonsoftware.com/articles/PickingShipDate.html)    . Or,  you get PR before there’s a product people can buy, then when the product  really comes out the news outlets don’t want to do the story again. We’ll  call this the Segway           phenomenon.

**Employees grows faster than  code:** Result: too many cooks working on code in the early days causes  bad architecture. Software development works best when a single person creates  the overall architecture and only later parcels out modules to different  developers. And if you add developers too fast, development screeches to a  halt, a phenomenon well understood since [1975](http://www.amazon.com/exec/obidos/tg/detail/-/0201835959/joelonsoftware)           .


And so on, and so on… A small company growing at a natural  pace has a reasonable chance of keeping these things in balance. But VCs don’t  like the flat part of the curve at the beginning, because they need an exit  strategy in which the hockey-stick part of the curve occurs *before* their fund needs to cash out, about  six years [according  to VC Joi Ito](http://joi.ito.com/archives/2003/05/17/our_investment_process.html)  . This is in direct conflict with the  fact that good software can’t really accomplish this kind of growth. Hockey  stick, there will be, but it will take longer than most VCs are willing to wait.  [Remember](https://www.joelonsoftware.com/articles/fog0000000017.html) my chart of Lotus Notes? Good heavens, I  *am*         repeating  myself.


VCs try to speed things up by spending  more money. They spend it on PR, and then you get problem 3 (“PR grows faster  than code”). They spend it on employees, and then you get problem 4 (“too  many cooks”) and problem 2 (“high burn rate”). They hire HR people, marketing  people, business development people. They spend money on advertising. And the  problem is, they spend all this money before anyone has had a chance to learn what  the best way to spend money *is*. So the business development guy  wanders around aimlessly and accomplishes zilch. You advertise in magazines that  VCs read, not magazines that your customers read. And so  on.


OK, that’s the first part of the VC  crisis.


The second part is the fact that VCs hear too  many business plans, and they need to reject 999 out of 1000. There appear to be an infinite number of business plans looking  for funding. A VC’s biggest problem is filtering the incoming heap to find what they consider to be that needle in  the haystack that’s worth funding. So they get pretty good at saying “no,” but they’re  not so good at saying no to the bad plans and yes to the good  plans.


When you have to say “no” 999 times for every  time you say “yes,” your method becomes whack-a-mole. Find the flaw, say no.  Find the flaw, say no. The faster you find flaws, the more business           plans you can ding. Over at VentureBlog you can [amuse  yourself](http://www.ventureblog.com/articles/cat_presenting_your_company.html) for an hour with some of the trivial  reasons VCs will ding you. PowerPoint too complicated?  Ding! Won’t tell us your magic sauce? Ding! You didn’t research the VC before you came  in? Ding! It’s not their fault; they are just  trying to say no 999 times in as efficient a  way as possible. All of this reminds me too much of the old-school manager who  hires programmers based on what school they went to or whether they look good in a  suit.


[Naval Ravikant](http://www.ventureblog.com/contributors.html#naval), a  VC at [August Capital](http://www.augustcap.com/), [reveals](http://www.ventureblog.com/articles/indiv/2003/000024.html)  the classic VC myopia of feeling like  they just don’t have time to get to know entrepreneurs that aren’t  ready to pitch yet. “Most VCs are too busy to ‘dance,’” he wrote. They are  too busy vetting serious proposals to shmooze with interesting companies that might not need cash right  now.


This is, roughly, the equivalent of the  old joke about the guy searching for his car keys under a streetlamp. “Did you  lose them here?” asks the cop. “No, I lost them over there, but the light’s better  here.”


But the great companies are often  *not* the ones that spend all their time begging for investments. They  may already be profitable. They may be too busy to look for VC, something which is  a full time job for many entrepreneurs. Many excellent entrepreneurs feel  that their time is better spent pitching products to customers  rather than pitching stock to investors. It’s bizarre that so many VCs are willing to  ignore these companies simply because they aren’t playing the traditional get-funded game. Get out there and pursue  them!


Here’s another funny thing that’s happening. VCs are  reacting to the crash by demanding ever stricter conditions for investments. It’s  now considered standard that the VC gets all their money back before anyone  else sees a dime, no matter what percent of the company they actually own.  VCs feel like this protects their interests. What they’re forgetting is  that it reduces the quality of startups that are willing to make deals. Here’s  one of VC [Joi Ito](http://joi.ito.com/)‘s [suggestion for VCs](http://joi.ito.com/archives/2003/05/17/our_investment_process.html)     : “Sign a ‘no shop’ and get a letter of intent  (LOI) signed quickly so an auction doesn’t start jacking up the price.” A  *no shop* is sometimes called an exploding  term sheet. It means that the company must either accept the deal on the  spot or it won’t get funded at all. The theory is, we don’t  want you going around to other VCs trying to get a better deal. It’s common  among the second-tier VCs, but the best VCs are usually willing to stand on their own  merits.


It seems to me that a company that  accepts an exploding offer is demonstrating a remarkable lack of basic business  aptitude. Every building contractor in New York knows you request bids from five  or ten plumbers before you award the contract. If a plumber said, “I’ll do it  for $x, but if you shop around, deal’s off,” the contractor would laugh his head  off and throw the plumber out on the street. Nothing sends a stronger message  that an offer is uncompetitive than refusing to expose it to competition. And  that’s for a $6000 kitchen installation. Getting $10 million in funding for  a business is the biggest and most important deal in the life of a company.  You’re going to be stuck with this VC forever, they’re going to want to control  your board of directors, they’re going to push the founders  out and bring in some polished CEO as quickly as they can, someone who  will take the picture of the cat off your homepage and [replace it](https://www.joelonsoftware.com/articles/fog0000000021.html)      with the usual MBA  jargon.


And now they want you to agree  to all this in a matter of fifteen minutes without talking to anyone else? Yeah,  right.


VCs who make exploding offers  are pretty much automatically eliminating all the people with good business sense from their  potential universe of companies. Again, it does make it easier to say no  999 times, but you’re pretty much guaranteed to say no to  all the companies with a modicum of negotiating skills. This is not the correlation  you’re looking for. In fact, just about everything the VCs do to make their deals  “tougher,” like demanding more control, more shares, more preferential shares, lower valuations, death spiral  convertible stock, etc., is pretty much guaranteed to be at the expense of  the founders in a very zero-sum kind of way. And this  means that smart founders, especially the ones with businesses that can survive a lack of  funding, are going to walk away. VCs must realize that if the business flops, no matter how much  control you have, the investor is going to lose everything. Look at the story of [arsDigita](http://eveander.com/arsdigita-history). A nasty fight over  control gives [Phil Greenspun](http://philip.greenspun.com/)  enough money to buy an airplane, and the VCs still lost  every penny when the company went down the tubes. So all these tough deals  are not really protecting the VCs, they’re just restricting the VCs’ world of  possible investments to dumb companies and desperate companies. Sam Bhaumik, VC, [says](http://www.nasvf.org/web/allpress.nsf/pages/2839) “VCs are being aggressive, but most requests are  legitimate.” The capital belongs to public pension funds and university  endowments, he notes, using the standard widows-and-orphans         sob story.  Boo  *hoo*    . Come *on*      , public pension funds and university endowments are the savviest investors out there; don’t tell me they  need coddling and protecting. They’re investing in risky venture funds for a reason: they  want to get paid for taking risk. If they wanted protection, they’d invest in US  Treasuries.


There are probably hundreds of software  companies started every day. Of that universe, there is a small number that are  actively looking for early stage investors. Of that small number, an even  smaller portion is willing to go along with the current harsh deals that VCs are  offering. Now slice away the founders who are afraid of being arsDigita’d. The  population shrinks even more as VCs reject companies that don’t match  their—quite reasonable—criteria for spotting a successful company. You wind up  with a tiny number of investment opportunities which, quite frankly, is  vanishingly unlikely to contain The Next  Netscape.


**More Reading**


Considering VC? First read this article on the  web:


> [**An  Engineer’s View of Venture Capitalists**](http://www.spectrum.ieee.org/WEBONLY/resource/sep01/speak.html)   , by Nick  Tredennick


Don’t miss these three books by company  founders:

- [**High St@kes,  No Prisoners: A Winner’s Tale of Greed and Glory in the  Internet Wars**](http://www.amazon.com/exec/obidos/tg/detail/-/0812931432/joelonsoftware)   by Charles  Ferguson.

[**The  Leap: A Memoir of Love and Madness in the Internet Gold Rush**](http://www.amazon.com/exec/obidos/tg/detail/-/0395839343/joelonsoftware) by  Tom   Ashbrook

[**Burn  Rate: How I Survived the Gold Rush Years on the Internet**](http://www.amazon.com/exec/obidos/tg/detail/-/0684856212/joelonsoftware) by  Michael   Wolff

**[Startup:  A Silicon Valley Adventure](http://www.amazon.com/exec/obidos/ASIN/0140257314/joelonsoftware)** by  Jerry   Kaplan


A movie   about the   process:

- [**Startup.com**](http://us.imdb.com/Title?0256408)


And don’t   forget:

- [**Eboys:  The First Inside Account of Venture Capitalists at Work**](http://www.amazon.com/exec/obidos/tg/detail/-/0812930959/joelonsoftware) by  Randall E.   Stross


Weblogs by   VCs:

- [VentureBlog](http://www.ventureblog.com/) 

[Joi  Ito](http://joi.ito.com/)
