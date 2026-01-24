---
title: "The Story About PING"
date: 2007-01-05
url: https://blog.codinghorror.com/the-story-about-ping/
slug: the-story-about-ping
word_count: 744
---

Everyone loves [ping](http://en.wikipedia.org/wiki/Ping). It’s simple. It’s utilitarian. And it does exactly what the sonar inspired name implies. Ping tells you if a remote computer is responding to network requests.


![](https://blog.codinghorror.com/content/images/2025/03/image-393.png)


The ping utility was written by Mike Muuss, a senior scientist at the [U.S. Army Research Laboratory](https://web.archive.org/web/20070114031652/http://www.arl.army.mil/main/Main/default.htm). Mike also wrote ttcp, which I’m a big fan of. I’ve [used the PC port of ttcp](https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/) many times to test network throughput.


Mike was [tragically killed](http://www.ping127001.com/pingpage/muuss.htm) in an automobile accident 7 years ago, but [his legacy lives on in Ping](https://web.archive.org/web/20070116094736/http://ftp.arl.mil/~mike/ping.html):


> In December of 1983 I encountered some odd behavior of the IP network at BRL. Recalling Dr. Mills’ comments, I quickly coded up the PING program, which revolved around opening an ICMP style SOCK_RAW AF_INET Berkeley-style socket(). The code compiled just fine, but it didn’t work – there was no kernel support for raw ICMP sockets! Incensed, I coded up the kernel support and had everything working well before sunrise. Not surprisingly, Chuck Kennedy (aka “Kermit”) had found and fixed the network hardware before I was able to launch my very first “ping” packet. But I’ve used it a few times since then. If I’d known then that it would be my most famous accomplishment in life, I might have worked on it another day or two and added some more options.


Ping isn’t very useful on today’s internet because most routers and hosts [filter it out](http://www.ping127001.com/pingpage.htm). But it’s still quite useful on local networks; not a month goes by that I’m not pinging something. Ping is always a solid starting point, but sometimes you’ll need to [perform deeper network diagnostics](https://blog.codinghorror.com/quick-and-dirty-internet-connection-troubleshooting/), too.


Of course, we can’t talk about ping without mentioning one of the [most famous Amazon book reviews](https://web.archive.org/web/20071124150415/http://www.amazon.com/review/R2VDKZ4X1F992Q) of all time.


![](https://blog.codinghorror.com/content/images/2025/03/image-394.png)


> PING! The magic duck!
> Using deft allegory, the authors have provided an insightful and intuitive explanation of one of Unix’s most venerable networking utilities. Even more stunning is that they were clearly working with a very early beta of the program, as their book first appeared in 1933, years (decades!) before the operating system and network infrastructure were finalized.
> The book describes networking in terms even a child could understand, choosing to anthropomorphize the underlying packet structure. The ping packet is described as a duck, who, with other packets (more ducks), spends a certain period of time on the host machine (the wise-eyed boat). At the same time each day (I suspect this is scheduled under cron), the little packets (ducks) exit the host (boat) by way of a bridge (a bridge). From the bridge, the packets travel onto the internet (here embodied by the Yangtze River).
> The title character – er, packet, is called Ping. Ping meanders around the river before being received by another host (another boat). He spends a brief time on the other boat, but eventually returns to his original host machine (the wise-eyed boat) somewhat the worse for wear.
> If you need a good, high-level overview of the ping utility, this is the book. I can’t recommend it for most managers, as the technical aspects may be too overwhelming and the basic concepts too daunting.
> As good as it is, The Story About Ping is not without its faults. There is no index, and though the ping(8) man pages cover the command line options well enough, some review of them seems to be in order. Likewise, in a book solely about Ping, I would have expected a more detailed overview of the ICMP packet structure.
> But even with these problems, The Story About Ping has earned a place on my bookshelf, right between Stevens’ Advanced Programming in the Unix Environment, and my dog-eared copy of Dante’s seminal work on MS Windows, Inferno. Who can read that passage on the Windows API (“Obscure, profound it was, and nebulous, So that by fixing on its depths my sight – Nothing whatever I discerned therein.”), without shaking their head with deep understanding. But I digress.


It’s a timeless geek humor classic. The original was posted in March 1999 by an anonymous reviewer from “Upper Volta, Uzbekistan.” It must have been deleted by Amazon, because it was reinstated by another reviewer later in 2000.


You may be familiar with the command line version of Ping, and maybe even the book, but did you ever play the arcade version of Ping?


![](https://blog.codinghorror.com/content/images/2025/03/image-395.png)


It’s milliseconds of fun for the entire family.

[networking](https://blog.codinghorror.com/tag/networking/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
