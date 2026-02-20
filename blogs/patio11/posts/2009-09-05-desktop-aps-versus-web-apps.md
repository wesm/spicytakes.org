---
title: "Why I’m Done Making Desktop Applications"
date: 2009-09-05
url: https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/
slug: desktop-aps-versus-web-apps
word_count: 2782
---


Breaking up has always been difficult for me.  I tend to fall in love with being in love, and continue a relationship well past the point of futility.  And so it is with my oldest love, writing desktop software.


I’m sorry, desktop apps.  We just don’t have a future together anymore.  Its not you, its me.


A bit of background: for the last three years I’ve sold [Bingo Card Creator](http://www.bingocardcreator.com), a desktop app which pretty much does what it says on the tin.  It has gone from being a passing fancy to a rather lucrative hobby to, well, a bit more than that over the years.  As I gradually became more invested in the business of writing desktop software, I got more and more snippy about the periodic desktop versus webapp flamewars, and defended the ascendancy of desktop software.


## What Changed My Mind


Over roughly the same period my day job has changed and transitioned me from writing thick clients in Swing to big freaking enterprise web apps.  I’ve learned SQL, Rails, etc and used them to fairly decent effect in selling Bingo Card Creator, which is a Swing app (if all you have is a hammer…).  This summer, I decided to try stepping my web programming skills up a notch, and released a web version of Bingo Card Creator.  It has **exceeded all my expectations**: in ease of writing, in features, in sales, in support burden, in marketability, etc.  In game theory terms, it *strictly dominates* the desktop version, when seen from the eyes of the developer at any rate.


If I were starting out today, I would, without a shadow of a doubt, write a web app instead of a desktop app, for these reasons:


## The Shareware Funnel Is Lethal


I have never used the word “shareware” to describe Bingo Card Creator, because I think that it is an anacronism that my customers do not understand, but among fellow technically inclined people it describes the business model succinctly.  Someone visits your website, downloads your trial, and hopefully purchases your program.  That process is called a funnel, and if you break it down into concrete steps, the shareware funnel is **long and arduous** for the consumer:

1. Start your web session on Google, like everyone does these days.
2. Google your pain point.
3. Click on the search result to the shareware site.
4. Read a little, realize they have software that solves your problem.
5. Mentally evaluate whether the software works on your system.
6. Click on the download button.
7. Wait while it downloads.
8. Close your browser.
9. Try to find the file on your hard disk.
10. Execute the installer.
11. Click through six screens that no one in the history of man has ever read.
12. Execute the program.
13. Get dumped at the main screen.
14. Play around, fall in love.
15. *Potentially weeks pass*.
16. Find your way back to the shareware site.  Check out price.
17. Type in your credit card details.  Hit Checkout.


I could go into more detail if I wanted, but that is **seventeen different opportunities for the shareware developer to fail**.  If you don’t catch the download in the 30 seconds people give your website, *no sale*.  If your customer can’t find the file after they download it, *no sale*.  If it requires a JRE upgrade and after restarting their computer they’ve forgotten what they were working on, *no sale*.  If they play around with it, close it, and can’t remember how to open it again, *no sale*.  If they get to the sales page and can’t operate your shopping cart, *no sale*.


Is it any wonder why shareware has typical conversion ratios of [1% or less](http://successfulsoftware.net/2009/04/23/the-truth-about-conversion-ratios-for-software/)?


## Web Applications Convert Better


A web application doesn’t have to be downloaded or installed, never requires a restart, and never requires a contextual change just to open up a purchasing page.  As a result, the conversion ratio is higher.  *Much* higher.  Here are the actual stats from Bingo Card Creator.  I’m looking at conversions from my best performing AdWords campaign only, because that minimizes sources of variation like, e.g., the different types of traffic I’ve gotten in the last 2 months (while the webapp was available) versus in the last three years.


Visitor to Free Trial:

- Downloaded: 18 ~ 22%
- Web App: 22% ~ 26%


Trial to Purchase:

- Downloaded: 1.35%
- Web App: 2.32%


This is **essentially the same application**.  If anything, the online version has *less* features, and it has 2 months of development whereas the downloadable application has had 3 years of improvements made to it.  Yet **the online version outsells my desktop application almost two to one**.


## Your AdWords Strategy Is Very Sensitive To Conversion Rates


A portion the numerical disparity is because I have started to react to, e.g., the difference in conversion rates of advertising and promote accordingly.  A sale of either nets me the same amount of money, about $28.  However, if you break out the math on how much AdWords costs per sale (cost per click divided by conversion rate to trial divided by conversion rate to purchase):

- Downloadable version: $20 AdWords CPA
- Web App: $9 AdWords CPA


(You’re welcome, Google.)


This doesn’t just save me money, it **helps me trounce my competitors**.  For example, if my competitors are selling downloadable software, and they are equally as skilled as I am about writing AdWords ads and optimizing their websites, then it should also cost them about $20 a sale to advertise on AdWords.  (This explains why I never see ads for the competitors who try to gain volume by undercutting my price — if you’re going to price at $23.95, you’d better be a crackerjack SEO because you simply cannot afford to outbid me in AdWords.)


Decreasing my cost of customer acquisition by over half lets me bid more for my AdWords to gain additional volume.  For example, for the longest time my AdWords strategy was more or less monetizing traffic other people couldn’t be bothered with, while larger brands producing e.g. printed bingo supplies went after the head terms like [bingo cards].  With vastly improved conversion rates, I might be able to advertise profitably on those terms, increasing my volume and making me very, very happy.  As it is, I have walked up bids a bit and am getting 25% more inventory than I usually do.


## Web Applications Are Easier To Support


Many desktop developers hate customer support with a burning passion in their soul.  I actually enjoy it, but I enjoy making it unnecessary even more, as **there is no customer support experience so good as avoiding the problem in the first place**.


Support requests from last 50 customers:

- Desktop Application: 15
- Web Application: 3


I’ve had three years to streamline the website, purchasing process, and application for my desktop app, and that has helped me greatly reduce the number of inquiries I get.  Even after all that work, the main culprits are pretty much the same as ever: installation issues, lost registration keys, and bugs present in old versions of the software that are still floating around download sites.


Web apps, by comparison:

- Have no installation issues, because there is no installation.
- Do not require registration keys.  (Technically, because I allow users to use both the desktop and web application, I issue them one — but it is immediately applied to their account via creative abuse of [e-junkie ](http://www.e-junkie.com)and cookies.  Most customers get to use their software immediately without actually reading the bit in the email sent to them — or failing to read it, as happens quite often.)
- Never have an accessible version of the software older than the most recent one.  By comparison, if you were to Google [[bingo card creator version 1.04](http://www.google.com/#hl=en&q=bingo+card+creator+version+1.04)] (which hasn’t been distributed in, hmm, two years or so), you’d find it on hundreds of download sites.


## The Age Of The Pirates Is Coming An End, Jack


I’m famously lackadaisical about software piracy, preferring to concentrate on [satisfying paying customers](https://www.kalzumeus.com/2006/09/05/everything-you-need-to-know-about-registration-systems/) rather than harming their experience with anti-piracy methods.  However, the existence of pirates is a stitch in my craw, particularly when any schoolmarm typing the name of my software into Google is prompted to try stealing it instead:


You want to take a quick stab at how many pirates have circumvented the copy protection on the online version?  **Bwa.  Hah.  Hah**.


I once [remarked to Paul Graham](http://news.ycombinator.com/item?id=503959) that the future of software was with pervasive integration with the server simply because that means that downloading the client doesn’t let you pirate the software any more than downloading Firefox lets you pirate Basecamp.  (Ironically, I made that point in a defense of desktop software as a business model.  Mea maxima culpa!  **Theoretical utility of desktop software is one thing, but I can’t ignore what my numbers are telling me.**)


## Phone Home vs. Google Analytics


One of the curious traits among software developers is that, speaking as a group, we feel something like “I own what happens on my machine and nothing should happen without my say-so”.  This generally leads to a severe reluctance to “phone home” from the application to the developer’s server — even reports on very innocuous data like “Did I steal this software or not?” is often tarred with the label spyware.


On the Internet, privacy expectations have evolved a bit in the last few years.  The overwhelming majority of the public has been told that they’re being tracked via cookies and **could not care less**.  If you write a privacy policy, they won’t even bother reading it.  Which means that you can disclose in your privacy policy that you track non-personally identifying information, which is *very* valuable as a software developer.

- What features of your software are being used?
- What features of your software are being ignored?
- What features are used by people who go on to pay?
- What combination of settings is most common?
- What separates the power users from the one-try-and-quit users?


Tracking all of these is very possible with modern analytics software like, e.g., [Mixpanel](http://www.mixpanel.com).  You can even wrestle the information out of Google Analytics if you’re prepared to do some extra work.  You can do it in a way which respects your users’ privacy while still maximizing your ability to give them what they want.


Some people may be under the impression that users will *tell* you what they want.  Nope — most of them will assume you are like every other business they have ever dealt with, where their opinion doesn’t matter, and the software is offered take-it-or-leave-it.  And they just left it!


Things I learned about Bingo Card Creator customers which I never knew before I had an online app:

- The most common word used in bingo cards is — ready for it — “baby”.  I completely underestimated the demand for [Baby Shower bingo cards](http://www.bingocardcreator.com/bingo-cards/parties-and-events/baby-shower), and avoided making an official set for *years*.  As soon as I had the top ten word list (which was *all* baby shower words) I fixed that.
- The more features I add to the software, [the worse it sells](http://www.bingocardcreator.com/articles/tracking-with-mixpanel.htm#results).  (This is, needless to say, *highly unintuitive* to most software developers.)
- Most customers purchase *within two hours of signup*, so it is absolutely imperative that their first use of the software exceed all their expectations.


## Web Apps Can Be Customized Per User


Downloadable software pretty much has to treat every user identically by default.  There are very limited ways to segment users, and no way to report the results of experiments.  For web apps, however, if you have a halfway decent A/B testing library (like, say, [the free one I wrote for Rails developers](http://www.bingocardcreator.com/abingo/)), you can experiment with having multiple versions of the application available concurrently, and see which one performs best.


The data collected by A/B testing has helped me:

- simplify my options screens to avoid confusing users
- improve the first-run experience
- write instructions such that they’re easier to follow


In addition to changing program behavior randomly, you can segment your users.  I have only scratched the surface of how powerful this is, and it is already producing solid results for me:


**Don’t treat your newbies like you treat your power-users.** You have a database.  It records all their actions since the dawn of time.  *Use it*.  I have a couple very simple heuristics for “is probably still getting used to the software” and, if you are, the software treats you with kid gloves.  For example, it hides complex, seldom used options by default.  It gives you instructions to a degree that a power-user might find insulting.  (I don’t have the artistic skills to draw a little animated paperclip but I would if I could!  *It looks like you’re trying to make a bingo card.  Need help?*)


**Give your customers a “credit” score**.  I have a particular heuristic which segments users into four buckets.  It isn’t exactly FICO, but it does successfully predict conversion rates: they range from 10% in bucket A to 0.01% in bucket D.  Bucket C is interesting, though — they convert some of the time, but don’t seem to be getting quite the value out of Bingo Card Creator that Bucket A does.


I wonder if Bucket C would feel differently if they got a $5 coupon in the email.


Meanwhile, it looks like Bucket D isn’t very interested in paying me money under any circumstances, but if I had a scratch-my-back-to-get-it-free option, I could place it prominently on their dashboards.


## Long Cycles Mean Low Innovation.  Short Cycles Mean Fast Innovation.


This sort of thing is very difficult to do with desktop apps, because you can’t reliably collect data on what approaches work, and you have the build/test/deploy/distribute cycle to worry about.  It takes months for a new version of the desktop application to hit more than half of my users, and I give out upgrades for free.


By comparison, I can *literally* have an A/B test coded, tested, and deployed globally in under a minute, for ones which are fairly low impact.  Relocating a button, for example, requires two lines of code, a SVN commit, and a quick server restart.  I start getting data *immediately*.  By comparison, doing that on my desktop app would require 15 minutes of building, then waiting weeks while the new trials percolated from my website to the various download sites, and probably unforseen issues on Mac OS X 10.4 because apparently in a past life I must have stepped on Pharaoh Jobs’ cat.


Recently, a desktop developer’s mailing list that I’m on commented that a release weekly development cycle is unsustainable, bordering on suicide.  As a desktop developer, I agree, it would break me.  As a web application developer — I have released 67 updates to Bingo Card Creator in the past 7 weeks, and *this isn’t even my day job*.  A button here, some textual edits there, seven A/B tests, etc etc, and pretty soon you’re looking at the magic of compounding 1% improvements.


## Speaking of Magic


I *love* desktop applications.  I prefer them to web apps almost any chance I get. You can keep your Google Docs, Excel is superior in almost every way.


As a developer, I love getting permanent presence right in front of the user (on their desktop, naturally).


My customers love desktop applications.  They love the “physicality”.  They love the perceived security (the number of people who purchased backup CDs and then proceeded to only use the webapp is *downright distressing* to me).  They love that the application has first-class OS support, feels native, copies and pastes right, works with double clicking files, etc etc.


But at the end of the day, I’m an engineer.  I follow the numbers where they lead me.  The numbers say that [sales in this August were 60% over those of last August](http://www.bingocardcreator.com/stats/sales-by-month), despite a major blowup with Google that should have cost me dearly.  All of my attempts to distill wisdom from the statistics have lead to one conclusion: the cumulative advantages of the web application, in my advertising, in my on-site experience, within the application, within my development process, and within my purchase funnel are just stupendously superior to the desktop app.


I’m sorry, desktop apps.  We had good times together, but we’re through.


[Edit to add: I’m going to continue supporting all customers of Bingo Card Creator, regardless of how they choose to get it. The next major release will almost certainly be its last. The webapp, and my future webapps, seem to be much better investments.]
