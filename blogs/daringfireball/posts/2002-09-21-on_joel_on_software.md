---
title: "On Joel on Software"
date: 2002-09-21
url: https://daringfireball.net/2002/09/on_joel_on_software
slug: on_joel_on_software
word_count: 1175
---


Last week, Joel “[Joel On Software](http://joelonsoftware.com)” Spolsky [wrote an article](http://www.joelonsoftware.com/news/20020910.html) arguing that there’s not much of a business case for developing Mac software. Not surprising, given that [his company](http://www.fogcreek.com) only develops for Windows, and that Mr. Spolsky formerly worked for Microsoft developing Windows software.


His argument boils down to something like this: there are around 25 times more Windows users than Mac users; thus, the only reason you should develop for the Mac is if you think a Mac version of your software will be 25 times more popular on the Mac than Windows. That the Daring Fireball disagrees goes without saying.


Brent Simmons took the bait and [responded](http://inessential.com/?comments=1&postid=2138), politely. Mr. Simmons, of course, is the developer of the red-hot, just-out-of-beta [NetNewsWire Lite](http://ranchero.com/software/netnewswire/). Many of you know exactly what NetNewsWire is, given the number of times it is showing up in Daring Fireball’s referrer logs. For those of you who don’t know, it’s an RSS news reader, which means it allows you to subscribe to web sites that publish RSS feeds.


Notably, NetNewsWire is written using Cocoa, and thus is *only* for Mac OS X. Spolsky only seems to be debating whether professional developers should write for the Mac in addition to Windows; that a serious developer might ignore Windows and write only for the Mac is apparently inconceivable.


Simmons’s defense is insightful, elegant, and passionate; I disagree with but a single sentence: the one in which he writes, “I don’t think Joel is wrong about anything he says.”


In fact, I think Spolsky is wrong about nearly everything in his
article. (Dave Winer [theorizes](http://scriptingnews.userland.com/backissues/2002/09/20#morningCoffeeNotes) that Spolsky is being purposefully
inflammatory, so that suckers like me will link to him. I don’t doubt this, but I still feel the need to refute Spolsky’s argument.) Let’s start with this nugget:


> Developing for the Mac is not a whole lot different than creating
> 	a web site that only works on Netscape. (Given the market share of
> 	Macs (about 3.5%) and the market share of Netscape (about 3.4%),
> 	that is not a silly comparison.)


But it *is* a silly comparison. A terribly silly one. First, making web sites and writing application software are two totally different tasks. Browsers aren’t API’s. Sane web developers don’t target specific browsers, they target [standards](http://webstandards.org), and all browsers which support them.


Second, what is “Netscape”? Netscape 4 and Netscape 7 couldn’t
possibly be more different. They share no code, and have totally different rendering engines. Netscape 4’s renderer is a piece of crap; Netscape 7’s renderer is the Gecko engine from Mozilla, which is one of the best ever written. Spolsky knows this, since he’s [written about it](http://www.joelonsoftware.com/articles/fog0000000069.html) previously, which gives more credence to the charge that he wrote the entire article as flamebait.


Next comes the arithmetic:


> In other words, if your Windows product appeals to 1 in 100 Windows
> 	users, you have to appeal to 25 in 100 Mac users to make the same
> 	amount of money.


Skipping over the argument about the Mac’s overall market share, the bigger problem with this sort of analysis is that it considers all computer users as equal consumers of commercial software. That can’t be. There can be no dispute that most computers in corporate use are running Windows. But how many corporate users do you know who buy or choose their own software? Especially software from small independent developers? Most corporate users I know run all-Microsoft, all the time: Windows, IE, Office. There is often *no* third-party software on a corporate computer.


Windows dominates the home market also. But a large part of home users are complete computer phobics. They don’t buy any software, either, unless there are kids in the house, in which case they probably buy lots of games. More on this later.


Sure, some Macs are used in corporate settings, and some are used at home by the “I just use the web and email” crowd. But Macs are much more likely to be used by computer enthusiasts. You pretty much have to go out of your way to end up with a Mac on your desk (or lap). If you walk into CompUSA and say, “I’d like to buy a computer”, you’re probably going to walk out with a Wintel box. If you do that at Wal-mart, you *definitely* will.


Let’s divide computer users into two groups — people who think
computers are fun, and people who just happen to use a computer. Which
group do you think buys more software (even including all the Linux
nerds in the first group)? Which group do you think most Mac users are in?


Don’t get me wrong, the Windows software market is much larger than the Mac market, and there are millions more Windows nerds than Mac nerds — if you’re trying to sell into big corporations, write for Windows. I’m not even arguing anything silly, like that Mac users, on average, are smarter than their Windows counterparts. (Although I will link to [this](http://www.internetnews.com/stats/article.php/1403581).) All I’m saying is this: amongst computer users who actually buy software, Mac users comprise a significantly larger chunk than 4 percent. Significantly.


> Maybe there’s less competition in your category on the Mac; maybe
> 	you’re in a niche like graphics where it seems like Macs dominate
> 	(they don’t, it just seems that way because the elite graphics people
> 	in big American cities use Macs);


That’s as absurd as claiming this: *Maybe you’re in a niche like games where it seems like Wintel boxes dominate (they don’t, it just seems that way because teenagers all over suburban America use Wintel boxes).*


Denying that Macs dominate the graphics industry is absurd. If you doubt me, do this: (1) call your local professional print shop (hint: Kinko’s is not a professional print shop); (2) ask them what percentage of their customers use Macs; (3) thank them for their time. And, while I’m at it, if the “elite graphics people in big American cities” aren’t an indicator of the industry’s OS preference, who is? Non-elite PowerPoint users in rural areas?


## Amelio Had a Point With His Maglite Analogy


Picking apart Spolsky’s argument bit by bit, while fun, misses the forest for the trees. Windows software ported to the Mac almost always [fails](http://www.corel.com). Mac software ported to Windows very often [succeeds](http://www.adobe.com/products/photoshop/main.html). On the Mac, in any given software category, the best app usually wins. On Windows, in any given software category, Microsoft usually wins.


Given a choice between two otherwise unmarked software packages, one labeled “more features”, the other labeled “better designed interface”, most Mac users will choose the latter. Mac users value attention to detail and intuitive, consistent, attractive interfaces. Developers who share these values would do well to create software for the Mac, where they are likely to be rewarded handsomely for their efforts. Developers who would prefer to program more features with less attention to detail should not.


## Further Reading


[Dan Benjamin’s Hivelogic](https://web.archive.org/web/20021221111954/http://www.hivelogic.com/220.html).



| **Previous:** | [I.P. Freely](https://daringfireball.net/2002/09/ip_freely) |
| **Next:** | [VersionCrapper User Reviews](https://daringfireball.net/2002/09/versioncrapper_user_reviews) |


PreviousNext