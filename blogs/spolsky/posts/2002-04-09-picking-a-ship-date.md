---
title: "Picking a Ship Date"
date: 2002-04-09
url: https://www.joelonsoftware.com/2002/04/09/picking-a-ship-date/
word_count: 2076
---


One of the best reasons to make a detailed [schedule](https://www.joelonsoftware.com/articles/fog0000000245.html) is because it gives you an excuse to cut features. If there’s no way to make the ship date *and* implement Bob’s Singalong MP3 Chat feature, it’s easy to cut that feature without making Bob feel bad.


So my basic rule for software release cycles is:

1. Set a ship date, which might as well be arbitrary
Make a list of features and sort them out by priority
Cut low-priority features every time you slip so as to make the date.


If you do this well, you’ll soon discover that you don’t regret the features that you cut. They’re usually kind of dumb. If they were so important, you can do them next time. It’s like editing. If you ever want to write a brilliant 750 word essay, start by writing a 1500 word essay and then edit.


One way to screw this up, by the way, is forgetting to do features *in order of priority*. If you aren’t careful, your programmers are going to do features in order of fun, and you won’t be able to ship *or* cut features because all the programmers were busy writing Karaoke Recalc before they even got the menus to work, and now here it is, six months after the day you wanted to ship, and you have one *hell* of an [easter egg](http://www.eeggs.com/items/672.html) but no functionality.


So the obvious question is: how do you pick a ship date?


It’s conceivable that you have outside constraints. The stock market is switching from fractions to decimals on such-and-such a date, and if you haven’t got the new software ready, your firm will be forced out of business and you personally will be taken out behind the loading docks and shot in the head. Or maybe a new version of the Linux kernel is coming out soon with yet *another* all-new system to implement packet filtering; all your customers are getting it; and your existing application won’t run on it. OK, for those people, your ship date is easy to figure out. You can stop reading this article now. Go cook a nice dinner for your loved ones.


Bye, now!


But how should the rest of us pick a ship date?


There are three approaches you could take.

1. **Frequent Small Releases.** This is the Extreme Programming approach, and is most appropriate for small-team projects with a small number of customers, such as in-house IT development.
**Every 12 to 18 months.** This is typical of shrinkwrapped software products, desktop applications, etc., where you have larger teams and thousands or millions of customers.
**Every 3-5 years.** This is typical of huge software systems and platforms that are worlds unto themselves. Operating systems, .Net, Oracle, and for some reason Mozilla fall into this category. They often have thousands of developers (VS.Net had 50 people on the *installer* team) and enormously complex interactions to other shipping software which can’t be allowed to break.


Here are some of the things you need to think about when deciding how often to release software.


Short releases get customer feedback fast. Sometimes the best way to work with a customer is to show them code, let them try it out, and immediately incorporate their feedback into a build which you give them the very next day. You won’t waste a year developing a complicated system with lots of features that nobody uses, because you’ll be so busy doing things that customers are requesting right now. **If you have a small number of customers, prefer frequent small releases. **The size of each release should be the minimum chunk that does something useful.


Several years ago I was assigned to develop a web content management system for MTV. The requirements called for a database-backed system with templates, and a complete workflow system that allowed unpaid MTV stringers at colleges across the country to input information about clubs, record stores, radio stations, and concerts. “How are you building the site now?” I asked.


“Oh, we just do it all manually with BBEdit,” they told me. “Sure, there are thousands of pages, but BBEdit has a really good global-find-and-replace function…”


I figured the whole system would take six months to deliver. “But let me suggest something else. Let’s get the templating stuff working first. I can get you that in 3 months and it will save tons of manual work right away. Once that’s working we’ll start in on the workflow component; in the meantime you can continue to do workflow with email.”


They agreed. It sounded like a great idea. Guess what? Once I delivered the templating feature, they realized that they didn’t really need workflow that much. And the templating turned out to be useful for lots of other web sites which didn’t need workflow, either. So we never built workflow, saving three months which I used to enhance the templating feature which turned out to be more useful.


Some types of customers don’t appreciate being “guinea pigs” in this fashion. Generally, people who buy off-the-shelf software don’t want to be part of a Grand Development Experiment; they want something that *anticipates* their needs. As a customer, the only thing better than getting feature requests done quickly is getting them *instantaneously* because they’re already in the product, because it was designed thoughtfully and extensively usability- and beta-tested before being inflicted on the world. **If you have (or want) a large number of paying customers, prefer less frequent releases**.


If you ship an anemic commercial program just to get something out the door so you can “start listening to customers,” what you’ll hear those customers saying is “it doesn’t do very much,” which you might think is OK. Hey, it’s 1.0. But then if you release 2.0 four months later, everybody’s going to think, “*That* feeble program? What am I, supposed to keep evaluating it every four months just to see if it’s gotten better yet?!” And in fact five years down the line, people will still remember their first impression of 1.0, and it will be almost impossible to get them to reevaluate. Think about what happened to poor Marimba. They launched their company with infinite VC in the days of hyper-Java-hype, having lured the key developers from the Java team at Sun. They had a CEO, Kim Polese, who was *brilliant *at public relations; when she was marketing Java she had Danny Hillis making speeches about how Java was *the next step in human evolution; *George Gilder wrote these breathless articles about how Java was going to completely upturn the very *nature *of human civilization. Compared to Java, we were to believe, monotheism, for example, was just a *wee blip*. Polese is *that good*. So when Marimba Castanet launched it probably had more unearned hype than any product in history, but the developers had only been working on it for a total of … four months. We all downloaded it and discovered that — tada! — it was a list box that downloaded software. (What do you expect from four months of development?) Big whoop. The disappointment was so thick you could cut it with butter. And here it is, six years later, ask anybody what Castanet is and they’ll tell you it’s a list box that downloads software. Hardly anyone bothered to reevaluate it, and Marimba has had six *years* to write code; I’m sure it’s just the coolest thing now but, honestly, who has time to find out? Let me tell you a little secret: our strategy for [CityDesk](http://www.fogcreek.com/CityDesk) is to avoid massive PR until 2.0 is out. *That’s* the version that we want everybody on earth to get their first impressions from. In the meantime we’ll do quiet [guerilla marketing](http://www.fogcreek.com/Affiliates.html), and anybody who finds it will discover that it’s a completely spiffy program that solves a lot of problems, but [Arnold Toynbee](http://www.amazon.com/exec/obidos/ASIN/0195050800/joelonsoftware) won’t have to rewrite anything.


With most commercial software, you’ll discover that the process of designing, prototyping, integrating, fixing bugs, running a full alpha and beta cycles, creating documentation, and so forth takes 6-9 months. In fact if you try to do a full release every year, you only have time for about 3 months worth of new code development. Software that is upgraded annually usually doesn’t feel like it has enough new features to justify the upgrade. (Corel PhotoPaint and Intuit Quickbooks are particularly egregious examples of this; they have a new “major” version every year which is rarely worth buying). As a result many people have learned by now to skip every other release. You don’t want your customers getting in that habit. If you stretch out your schedule to 15 or 18 months between releases, you get 6 months of new features instead of 3 months worth, which makes your upgrade a lot more compelling.


OK, if 15 months is so good, wouldn’t 24 months be better? Maybe. Some companies can get away with it, if they are major leaders in their category. PhotoShop seems to get away with it. But as soon as an application starts to feel old, people stop buying it because they are expecting that new version Any Day Now. This can cause serious cash flow problems for a software business. And of course you may have competitors nipping at your heels.


For large platform software — operating systems, compilers, web browsers, DBMSs — the hardest part of the development process is maintaining compatibility with thousands or millions of existing applications or hardware. When a new version of Windows comes out, you very rarely hear about backwards compatibility problems. The only way they can achieve this is with insane amounts of testing that make the construction of the Panama Canal seem like a weekend do-it-yourself project. Given the typical 3 year cycle between major Windows releases, almost all of that time is spent in the boring integration and testing phase, not writing new features. Releasing new versions any more often than that is just not realistic. And it would drive people crazy. Third party software and hardware developers would simply revolt if they had to test against lots of little incremental releases of an operating system. **For Systems With Millions of Customers and Millions of Integration Points, Prefer Rare Releases**. You can do it like Apache: one release at the beginning of the Internet Bubble, and one release at the end. Perfect.


If you have a lot of validation and unit tests, and if you write your software carefully, you may get to the point where any daily build is *almost *high enough quality to ship. This is certainly something to strive for. Even if you’re planning the next release for three years from now, the competitive landscape may suddenly change and there may be a good reason to do a quick interim release to react to a competitor. When your wife is about to give birth, it’s not really a good idea to take apart your car’s engine. Instead build a new one on the side and don’t hook it up until it’s perfect.


But don’t overestimate what you can accomplish by keeping high quality daily builds. Even if you are permanently at zero bugs, if your software has to run In The Wild, you’re never going to find all the compatibility bugs and Windows 95 bugs and It-Doesn’t-Work-With-Large-Fonts-Turned-On bugs until you do a few betas, and there is no realistic way to do a beta cycle in less than 8 weeks.


One final thought. If your software is delivered as a service over the web, like ebay or PayPal, theoretically there’s nothing to stop you from frequent small releases, but this might not be the best thing to do. Remember the [cardinal rule of usability](https://www.joelonsoftware.com/uibook/chapters/fog0000000057.html): an application is usable if it behaves the way that the user *expected* it to behave. If you keep changing things around every week, it won’t be so predictable, so it won’t be so usable. (And don’t think you can get around this by having one of those annoying screens with a paragraph of text saying Warning! The UI has changed! [Nobody reads those](https://www.joelonsoftware.com/uibook/chapters/fog0000000062.html).) From a usability perspective a better approach would probably be less frequent releases that include a bunch of changes all at once, where you make an effort to change the visuals of the whole site so that it all looks weird and users intuit that things have changed a lot and they have to be careful.
