---
title: "Open Source Software, Self Service Software"
date: 2009-01-22
url: https://blog.codinghorror.com/open-source-software-self-service-software/
slug: open-source-software-self-service-software
word_count: 1092
---

Have you ever used those self-service checkout machines at a grocery store or supermarket?


![](https://blog.codinghorror.com/content/images/2025/04/image-284.png)


What fascinates me about self-service checkout devices is that **the store is making you do work they would normally pay their employees to do.** Think about this for a minute. You’re playing the role of the paying customer *and* the cashier employee. Under the watchful eyes of security cameras and at least one human monitor, naturally, but still. We continue to check ourselves out. Not only willingly, but enthusiastically. For that one brief moment, we’re working for the supermarket at the lowest possible pay scale: none.


That’s the paradox of self-checkout. But to me it’s no riddle at all: **nobody else in that store cares about getting Jeff Atwood checked out *nearly* as much as Jeff Atwood does.** I always choose self-service checkout, except in extraordinary cases. The people with the most vested interest in the outcome of the checkout process are the very same people that self-checkout puts in charge: me! How could it not work? It’s the perfect alignment of self-interest.


I don’t mean this as a dig against supermarket employees. They’re (usually) competent and friendly enough. I should know; I worked my way through high school and part of college as a Safeway checker. I tried my level best to be good at my job, and move customers through my line as quickly as possible. I’m sure I could check someone out faster than they could do it themselves. But there’s only one me, and at most a half-dozen other checkers working the store, compared to the multitudes of customers. It doesn’t scale.


If you combine the self-interest angle and the scaling issue, self-service checkout seems obvious, a win for everyone. But self-service is not without issues of its own:

- What if the item you’re scanning isn’t found, or can’t be scanned?
- Some of the self-service machines have fairly elaborate and non-obvious rules in place, to prevent fraud and theft. Also, the user interface can sometimes be less than ideal on the machines.
- How do you handle coupons? Loyalty cards? Buying 20 of the same item? Scanning the wrong item?
- The self-service stations are lightly manned. The ratio between employee monitors and self-checkout machines runs about 1:4 in my experience. If you have a problem, you might end up waiting longer than a traditional manned checkout.
- How do you ring up items like fruit and vegetables which don’t have UPC codes, and have to be weighed?
- What about unusual, awkwardly shaped items or oversize items?
- Customers who have trouble during self-checkout may feel they’re stupid, or that they did something wrong. Guess where they’re going to lay the blame for those feelings?


There are certain rituals to using the self-service checkout machines. And we know that. **We programmers fundamentally grok the hoops that the self-service checkout machines make customers jump through.** They are, after all, devices designed by our fellow programmers. Every item has to be scanned, then carefully and individually placed in the bagging area which doubles as a scale to verify the item was moved there. One at time. In strict sequence. Repeated exactly the same every time. We live this system every day; it’s completely natural for a programmer. But it isn’t natural for average people. I’ve seen plenty of customers in front of me struggle with self-service checkout machines, puzzled by the workings of this mysterious device that seems so painfully *obvious* to a programmer. I get frustrated to the point that I almost want to rush over and help them myself. Which would defeat the purpose of a... self-service device.


I was thinking about this while reading Michael Meeks’ article, [Measuring the true success of OpenOffice.org](https://web.archive.org/web/20090918165158/http://www.gnome.org/~michael/blog/ooo-commit-stats-2008.html). He reaches some depressing conclusions about the current state of [OpenOffice](https://www.openoffice.org), a high profile open source competitor to Microsoft Office:


> Crude as they are, the statistics show a picture of slow disengagement by Sun, combined with a spectacular lack of growth in the developer community. In a healthy project we would expect to see a large number of volunteer developers involved, in addition – we would expect to see a large number of peer companies contributing to the common code pool; we do not see this in OpenOffice.org. Indeed, quite the opposite. We appear to have the lowest number of active developers on OO.o since records began: 24, this contrasts negatively with Linux’s recent low of 160+. Even spun in the most positive way, OpenOffice.org is at best stagnating from a development perspective.


This is troubling, because **open source software development is the ultimate self-service industry**. As Michael notes, the project is sadly undermining itself:


> Kill the ossified, paralyzed and gerrymandered political system in OpenOffice.org. Instead put the developers (all of them), and those actively contributing, into the driving seat. This in turn should help to kill the many horribly demotivating and dysfunctional process steps currently used to stop code from getting included, and should help to attract volunteers. Once they are attracted and active, listen to them without patronizing.


Indeed, once you destroy the twin intrinsic motivators of self-determination and autonomy on an open source project, I’d argue you’re no better off than you were with traditional closed source software. **You’ve created a self-service checkout machine so painful to use, so awkward to operate, that it gives the self-service concept a bad name.** And that’s heartbreaking, because self-service is the soul of open source:


> Why is my bug not fixed? Why is the UI still so unpleasant? Why is performance still poor? Why does it consume more memory than necessary? Why is it getting slower to start? Why? Why? The answer lies with developers: Will you [help us make OpenOffice.org better?](https://contributing.openoffice.org/)


In order for open source software projects to survive, they must ensure that they present as few barriers to self-service software development as possible. And any barriers they do present must be very low – *radically* low. Asking your customers to learn C++ programming to improve their Open Office experience is a pretty far cry indeed from asking them to operate a scanner and touchscreen to improve their checkout experience. And if you can’t convince an audience of programmers, who are inclined to understand and love this stuff, who exactly *are* you expecting to convince?


So, if you’re having difficulty getting software developers to participate in your open source project, I’d say the community isn’t failing your project. *Your project is failing the community*.

[open source software](https://blog.codinghorror.com/tag/open-source-software/)
[self-service software](https://blog.codinghorror.com/tag/self-service-software/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
