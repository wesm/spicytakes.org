---
title: "Remembering the Dynabook"
date: 2008-11-04
url: https://blog.codinghorror.com/remembering-the-dynabook/
slug: remembering-the-dynabook
word_count: 1178
---

My [recent post on netbooks](https://blog.codinghorror.com/the-web-browser-is-the-new-laptop/) reminded me of [Alan Kay’s](http://en.wikipedia.org/wiki/Alan_Kay) original 1972 [Dynabook concept](http://www.mprove.de/diplom/gui/Kay72a.pdf) (pdf).

kg-card-begin: html

> We now have some reasons for wanting the DynaBook to exist. Can it be fabricated from currently invented technology in quantities large enough to
> bring a selling (or renting) price within reach of millions of potential users? The set of considerations which pertain to the more practical aspects of the device (such as size, cost, capability, etc.) are just as important as the more abstruse philosophy which prompted us in the first place. The next few pages discuss some of the tradeoffs involved, and will attempt to convince the reader that a target price of $500 is not totally outrageous. The current cost trends and size of the various components do offer considerable hope that the target can be reached. The analogy to color TVs which can be sold for under S500 is also important to keep in mind.
> Now, what should the DynaBook be?
> The size should be no larger than a notebook; weight less than 4 pounds. The visual display should be able to present at least 4000 printing quality characters with contrast ratios approaching that of a book. Dynamic graphics of reasonable quality should be possible; there should be removable local file storage of at
> least one million characters (about 500 ordinary book pages) traded off against several hours of audio (voice/music) files.
> The active interface should be a language which uses linguistic concepts not far removed from the owner of the device. The owner will be able to maintain and edit his own files of text and programs when and where he chooses. He can use his DynaBook as a terminal when at work (or as a connection to the library system when in school).
> When he is done perusing and has discovered information that he wishes to abstract and take with him, it can rapidly be transferred to his local file storage. The umbilical connection will supply not only information but also extra power for any motors the device might have, allowing high bandwidth transmission of about 300K bits/sec to the file storage, or one 500-page-book in 1/2 minute. The batteries will also be automatically recharging during this connection.

kg-card-end: html

A netbook with a 3G wireless/wifi internet connection is almost eerily close to Kay’s original [Dynabook](http://en.wikipedia.org/wiki/Dynabook) concept. **It only took, what, thirty-six years?**


Most netbooks have coalesced around these rough specs, as documented on the excellent [netbook-centric website Liliputing](http://www.liliputing.com/):

- 1.6GHz Intel Atom CPU
- 9 or 10 inch, 1024 x 600 pixel display
- high capacity hard drive or relatively small (and cheap/slow) solid state disk
- 802.11 b/g wireless
- 2.5 hour battery life with standard size battery
- 2 to 3 pounds
- approximately $350 - $399


Do netbooks meet the criteria outlined in Kay’s original 1972 Dynabook paper? To my eye, yes. They’re far cheaper once you factor in inflation relative to his original $500 price point in 1972 dollars. I referred to netbooks as [portable web browsers](https://blog.codinghorror.com/the-web-browser-is-the-new-laptop/) and I still believe that is in fact what they are – inexpensive, ubiquitous, (mostly) full featured portals into the larger internet.


But Kay, in a recent [interview with Wired](https://web.archive.org/web/20081107122226/http://blog.wired.com/gadgets/2008/11/museum-celebrat.html), isn’t so sure this is a good thing:


> **Wired.com:** What do you think of netbooks? They’re lightweight and small – pretty close to two pounds. Do they still need work before they can meet your definition of a Dynabook?
> **Kay:** I’d like to think that they are finding a form factor and weight that fits human beings better, but I’m presuming that it is because many people use only a small part of what they could do on their larger machines, and much of what they do use computers for can be done through a browser or a few simple apps. So this would be somewhat similar to the limited uses of computing that fit into other even smaller devices such as phones and PDAs. If so, then this is more disappointing than something to be cheered about.
> **I cringe every time I use a browser for many reasons.** The browser people had a chance to make a more integrated UI and functionality, but really did pretty much the opposite in almost all respects. But, because of the attraction, and even some real value of stuff on the internet, there is more pressure to do better. I would expect to see some real alternatives to the typical “bad de facto standard” browsers we’ve had to put up with.
> There is much to be done here, and to even get back to a number of important integration and workflow ideas that were part of the PARC UI.


Apparently Kay doesn’t think much of the current status quo, where you define the status quo as OS X, Windows, or Linux. I suspect much of Kay’s objection to the web browser interface is the general passivity of browsing the web; bear in mind that Kay is an educator and originally intended Dynabooks as tools for children to create and explore with [something like Logo](https://blog.codinghorror.com/modern-logo/).


Personally, my only objection to current netbook platforms is the stupidly huge power draw of the creaky old Intel 945 motherboard chipset they are [typically built on](https://web.archive.org/web/20081207192350/http://techreport.com/articles.x/15204/9).


> Looking at these results, one can’t help but think that **the Atom could be an astoundingly power-efficient processor when coupled with a chipset and platform with a lower power use floor.** Intel, of course, has such things in the works for other markets.


This is why most *current* netbooks have mediocre 2 to 2.5 hour battery life – unless you pick up the mongo extra-large extended batteries, which of course increase size and weight.


I hooked up my [trusty old kill-a-watt](https://blog.codinghorror.com/why-estimate-when-you-can-measure/) to my wife’s netbook and measured almost no difference at all in power consumption between idle and full Prime 95 load. [Intel’s Atom CPU](http://www.anandtech.com/cpuchipsets/showdoc.aspx?i=3276) is truly astonishingly efficient – a feat all the more impressive when you realize that on most laptops the CPU is, by far, the number one [consumer of power](https://blog.codinghorror.com/revisiting-how-much-power-does-my-laptop-really-use/). On our netbook, **only 1 or 2 watts** of the total ~25 watt idle power draw is attributable to the CPU, a tiny fraction of the overall power consumption. I tried turning off wireless and dimming the screen, but I couldn’t get the power draw floor below 18 watts – that’s all attributable to the chipset.


Intel did a fantastic job on the Atom CPU, but they completely phoned it in on the chipset. The next generation of netbooks with more power efficient chipsets should *easily* double battery life. No question.


**I think netbooks will be as revolutionary as Kay originally predicted with his DynaBook concept**. Though we have only seen the beginning of this trend, I’m not sure the big players really understand how much these early netbooks have [*already* changed the game](https://web.archive.org/web/20081104004438/http://blog.wired.com/gadgets/2008/09/netbooks-evolvi.html). It’ll probably take several more years for the rest of the market to catch on.

[conceptual design](https://blog.codinghorror.com/tag/conceptual-design/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[portable devices](https://blog.codinghorror.com/tag/portable-devices/)
[computing history](https://blog.codinghorror.com/tag/computing-history/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
