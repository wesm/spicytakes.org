---
title: "Working on CityDesk, Part Four"
date: 2001-10-29
url: https://www.joelonsoftware.com/2001/10/29/working-on-citydesk-part-four/
word_count: 1654
---


Boy, what a terrible weekend. I’ve come down with a cold. Fever. Runny nose. General malaise. And WININET.DLL.


WININET.DLL, you see, is a software file provided by Microsoft. It comes with Internet Explorer and with all versions of Windows since about 1996, and it was the bane of my weekend. And it illustrates a fascinating fact about how much software developers’ day-to-day lives have changed in the last decade.


Here’s what happened. Late on Friday afternoon I was setting up some new web servers designed to handle the increased load we’re expecting when we ship CityDesk. One of the first things I did was try to use CityDesk to copy files to the new servers using the FTP protocol. We had a firewall set up that prevented FTP from going through. CityDesk froze up.


“No problem,” I thought, “I’ll use passive-mode FTP, which can get through that firewall.”


That’s when I noticed CityDesk doesn’t *support* passive-mode FTP.


“OK, how hard can that be to implement? It’s probably available as an option on the file transfer library we’re using.” One checkbox and I’m done.


But … where’s the checkbox?


No mention of it in the documentation.


Searching the object file itself didn’t turn up anything likely.


I checked Google Groups, formerly known as* *DejaNews. It’s a complete archive of every UseNet discussion. This is where programmers ask each other questions about the most arcane topics. As I told Babak once: it’s a big world out there. You’re never the first person to have this problem.


After about five minutes searching, the conclusion was inescapable. Our file transfer library, which Microsoft gives away for free with the Visual Basic compiler, can’t do passive-mode FTP.


OK, back to the drawing board. What are my choices? I wrote up a list:

1. Do without Passive FTP. This would make CityDesk useless to a large number of people, something I wasn’t willing to do.
Purchase a commercial FTP library. Honestly, I’ve always had bad luck with commercial libraries, having discovered one too many times that their code quality is rarely up to the meticulous standards we set for Fog Creek. When I looked around the discussion groups where developers were discussing other FTP libraries, they always seemed to have scary bugs that I couldn’t live with.
Use Microsoft’s *other* file transfer library, the infamous WININET.DLL. This is actually what Microsoft Internet Explorer uses to transfer files, which, despite its dismal reputation, is used so widely that I thought it *had* to be *reasonably* bug free (by now, at least). Anyway, lots of programmers use WININET.DLL and if I run into trouble I’m sure to find ample discussion of the problems on DejaNews, er, Google Groups.


I thought that #3 seemed painless enough. In fact I was already using WININET.DLL somewhere else in our code to import web pages, using the HTTP protocol.


A search of Microsoft’s online knowledge base revealed that you can’t really do FTP with WININET.DLL from Visual Basic code; it does some complicated stuff with threads that mean that you have to call it from C or C++. I thought the easiest thing to do would be to create my own custom FTP control written in C++, which talked to WININET. I chose to use Microsoft’s ATL library to create the custom control, because it makes the smallest files. ATL is the most complicated programming environment in the world, requiring a brain the size of Colorado and 10 years of solid experience to understand what’s going on. I have studied ATL in depth three, maybe four times in my career and I can never remember all the bizarre template crap that’s going on in there. Nobody can.


Yes, Virginia, it *is* possible to create a software development environment which is so difficult to use that no human being can do it. ATL and COM+ are my two favorite examples (the latter is so complicated that only one man on Earth, Don Box, actually understands everything that’s going on). C++ itself comes pretty darn close. But most programmers are too macho to admit this.


Luckily, Microsoft provides some wizards with ATL which write all the hard code for you. If you want to do something unusual, you’re on your own, so my motto was Nothing Unusual. No sudden moves. Just add some simple methods and events and get the hell outta there, hopefully with my brains non-exploded.


At one point, after I had written almost half the code, I discovered that one of the checkboxes that I had checked on the wizard which wrote the inscrutable ATL code for me was wrong. But once the code is written, it’s written. For the life of me, I couldn’t figure out what the checkbox had done and where to change it in the code. I searched MSDN (a gigabyte of documentation on programming Windows which I keep on my hard drive), the online knowledge base, and finally the entire Internet using Google, and didn’t find an easy way to change it. So I created two entirely new projects using the wizard, checking the box in one case and not checking it in the other, and then ran WinDiff, which compares two entire directories listing all the differences, to find what the checkbox really changed so I could change it in my code. (Somewhere, I had to change a hardcoded number to 131473, because I wanted my controls to be visible at runtime. A classic example of why COM programming is not for humans.)


The Microsoft documentation for WinInet was pretty decent, as these things go, but not decent enough. In the page documenting **FtpOpenFile**, you find both of these mutually contradictory quotes:

1. “No file handle is returned”
“Return value: Returns a handle if successful”


Well, which is it? Empirically, it wasn’t returning a file handle.


The next thing I discovered is that if there is a packet filter (a simple form of firewall) somewhere between you and the server, the code hangs trying to copy files. That’s normal; it’s the way of the Internet; there’s nothing you can do about it. After a minute, WinInet will realize that packets are not getting through and will time out. But the user is likely to get impatient long before a minute is up and hit the Cancel button.


When you hit the Cancel button, my code tells WinInet to give up and close down the connection. But as I discovered, if you do this in one of these packet-filter situations, WinInet will simply crash, bringing your program down with it. It’s clearly a bug in Microsoft’s code. An exhaustive search of all my Internet sources found a couple of people reporting the same crashing behavior, but nobody had a workaround.


How can that be? I thought. Since Internet Explorer uses the exact same code, wouldn’t Internet Explorer crash in the same situation?


I tried it. What I discovered is that Internet Explorer doesn’t crash in this situation — it shows an hourglass and freezes for a couple of minutes, waiting for the time-out it knows it will get. This proves that Microsoft’s programmers *knew* about this bug in WinInet and worked around it, instead of just fixing the code in the first place. Stupid stupid stupid. For the umpteenth time, I found myself dependent on a code library which had a crashing bug that was unacceptable in code *I* shipped. What are you supposed to do if you’re the chef at Les Halles and your fishmonger is giving you smelly fish?


Another two hours of investigation and experimentation. Finally I decided that in this case, when the user hits the Cancel button, instead of freezing like Internet Explorer, I will simply hide the file transfer so it *looks* like the operation has been cancelled. In the background, invisible to the user, I’ll wait around for the time-out to happen.


So, as I said, developers’ lives have changed. All weekend I couldn’t sleep. Tossing and turning in sweat-drenched sheets, I had feverish ATL nightmares. Sunday morning I got up at 3 am and coded for 4 hours just to avoid the bad dreams about Structured Exception Handling.


Ten years ago, to write code, you needed to know a programming language, and you needed to know a library of maybe 50 functions that you used regularly. And those functions worked, every time, although some of them (**gets**) could not be used without creating security bugs.


Today, you need to know how to work with libraries of *thousands* of functions, representing buggy code written by other people. You can’t possibly learn them all, and the documentation is never good enough to write solid code, so you learn to use online resources like Google, DejaNews, MSDN. (I became much more productive after a coworker at Google showed me that you’re better off using Google to search Microsoft’s knowledge base rather than the pathetic search engine Microsoft supplies). In this new world, you’re better off using common languages like Visual Basic and common libraries like WinInet, because so many other people are using them it’s easier to find bug fixes and sample code on the Web. Last week, Michael added a feature to CityDesk to check the installed version of Internet Explorer. It’s not hard code to write, but why bother? It only took him a few seconds to find the code, in VB, on the Web and cut and paste it.


We used to write algorithms. Now we call APIs.


Nowadays a good programmer spends a lot of time doing defensive coding, working around other people’s bugs. It’s not uncommon to set up an exception handler to prevent your code from crashing when your crap library crashes.


Times have changed. Welcome to a world where the programmer who knows how to tap into other people’s brains and experience using the Internet has a decisive advantage.


Working on CityDesk Part: [1](https://www.joelonsoftware.com/articles/fog0000000009.html) [2](https://www.joelonsoftware.com/articles/fog0000000008.html) [3](https://www.joelonsoftware.com/articles/fog0000000006.html) [4](https://www.joelonsoftware.com/articles/fog0000000250.html) [5](https://www.joelonsoftware.com/articles/fog0000000296.html)
