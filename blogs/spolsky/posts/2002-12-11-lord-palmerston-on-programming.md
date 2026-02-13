---
title: "Lord Palmerston on Programming"
date: 2002-12-11
url: https://www.joelonsoftware.com/2002/12/11/lord-palmerston-on-programming/
word_count: 2234
---


There was a time when if you read [one book](http://www.amazon.com/exec/obidos/tg/detail/-/067130948X) by Peter Norton, you literally knew everything there was to know about programming the IBM-PC. Over the last 20 years, programmers around the world have been hard at work building abstraction upon abstraction on top of the IBM-PC to make it easier to program and more powerful.


But the [law of leaky abstractions](https://www.joelonsoftware.com/articles/LeakyAbstractions.html) means that even as they built the abstractions that are supposed to make programming easier, the sheer amount of stuff you have to know to be a great programmer is expanding all the time.


Becoming proficient, really proficient, in just one programming world takes years. Sure, lots of bright teenagers learn Delphi one week and Python the next week and Perl the next week and think they are proficient. Yet they don’t have the foggiest clue how much they’re missing.


I’ve been working with ASP and VBScript since it first came out. VBScript is the dinkiest language on earth and ASP programming consists of learning about 5 classes, only two of which you use very often. And only now do I finally feel like I know the best way to architect an ASP/VBScript application. I finally think I know where the best place to put database access code is, the best way to use ADO to get recordsets, the best way to separate HTML and code, etc. And I finally use regexps instead of one-off string manipulation functions. Only last week, I learned how to get COM objects out of memory so you can recompile them (without restarting the whole web server).


Fog Creek is too small to have specialists, so when I needed to write a really good [installer](https://www.joelonsoftware.com/news/20021002.html) for [FogBUGZ](http://www.fogcreek.com/FogBUGZ), our ASP/VBScript based product, I drew on several years of C++/MFC experience, and years of experience with Windows APIs, and good Corel PhotoPaint skills to create a neat picture in the corner of the wizard. Then to get FogBUGZ to work perfectly with Unicode, I had to write a little ActiveX control using C++ and ATL, which drew upon years of C++ and COM experience and a week or so learning about character encodings when I implemented that code in CityDesk.


So when we had a weird NT 4.0-only bug, it took me 3 minutes to debug, because I knew how to use VMWare, and I had a clean NT 4.0 machine set up in VMWare, and I knew how to do remote debugging with Visual C++, and I knew to look in the EAX register to get the return value from a function. Someone who was new to this all might have taken an hour or more to debug the same problem, but I already knew a tremendous amount of “stuff” that I’ve been learning, basically, since 1982 when I got my first IBM-PC and that Norton book.


Leaky abstractions mean that we live with a hockey stick learning curve: you can learn 90% of what you use day by day with a week of learning. But the other 10% might take you a couple of years catching up. That’s where the really experienced programmers will shine over the people who say “whatever you want me to do, I can just pick up the book and learn how to do it.” If you’re building a team, it’s OK to have a lot of less experienced programmers cranking out big blocks of code using the abstract tools, but the team is not going to work if you don’t have some really experienced members to do the really hard stuff.


There are a lot of programming worlds, each of which requires a tremendous amount of knowledge for real proficiency. Here are the three I personally know best:

- MFC/C++/Windows
VBScript/ASP
Visual Basic


All, basically, what you would call Windows programming. Yes, I’ve written Unix code and Java code, but not very much. My proficiency in Windows programming comes from knowing not just the basic technologies but also the whole supporting infrastructure. So, I claim, I’m really good at Windows programming because I also know COM, ATL, C++, 80×86 Assembler, Windows APIs, IDispatch (OLE Automation), HTML, the DOM, the Internet Explorer object model, Windows NT and Windows 95 internals, LAN Manager and NT networking, including security (ACEs, ACLs, and all that stuff), SQL and SQL Server, Jet and Access, JavaScript, XML, and a few other [cheerful facts](http://www.zeitcom.com/majgen/021msong.html) about the square of the hypotenuse. When I can’t get the StrConv function in VB to do what I want, I bang out an COM control so I can drop into C++ with ATL and call the MLang functions without dropping a beat. It took me years to get to this point.


There are lots of other programming worlds. There’s the world of people developing for BEA Weblogic who know J2EE, Oracle, and all kinds of Java things that I don’t even know enough about to enumerate. There are hard core Macintosh developers who know CodeWarrior, MPW, Toolbox programming in System 6 through X, Cocoa, Carbon, and even nice obsolete things like OpenDoc that don’t help any more.


Very few people, though, know more than one or two worlds, because there’s just so much to learn that unless you have to work in one of these worlds for more than a couple of years, you don’t really grok it all.


But learn you must.


People get kind of [miffed](http://www.treedragon.com/ged/map/ti/newOct02.htm#23oct02-interview) when they go on job interviews and get rejected because, for example, they don’t have Win32 (or J2EE, or Mac programming, or whatever) experience. Or they get annoyed because idiot recruiters, who would not know an MSMQ if it bit them in the tailbone, call them up and ask if they “have 5 years MSMQ.”


Until you’ve done Windows programming for a while, you may think that Win32 is just a library, like any other library, you’ll read the book and learn it and call it when you need to. You might think that basic programming, say, your expert C++ skills, are the 90% and all the APIs are the 10% fluff you can catch up on in a few weeks. To these people I humbly suggest: times have changed. The ratio has reversed.


Very few people get to work on low level C algorithms that just move bytes around any more. Most of us spend [all our time](https://www.joelonsoftware.com/articles/fog0000000250.html) these days calling APIs, not moving bytes. Someone who is a fantastic C++ coder with no API experience only knows about 10% of what you use every day writing code that runs on an API. When the economy [is doing well](https://www.joelonsoftware.com/articles/fog0000000050.html), this doesn’t matter. You still get jobs, and employers pay the cost of your getting up to speed on the platform. But when the [economy is a mess](http://sfgate.com/cgi-bin/article.cgi?f=/c/a/2002/10/20/IN.DTL) and 600 people apply for every job opening, employers have the luxury of choosing programmers who are already experts at the platform in question. Like programmers who can name four ways to FTP a file from Visual Basic code and the pros and cons of each.


The huge surface area of all these worlds of programming leads to pointless flame wars over whose world is better. Here’s a smug comment somebody anonymously made on my discussion board:


> “Just one more reason why I’m glad to be living in the ‘free world.’ Free as in speech (almost) and freedom from pandering to things like setup programs and the registry – just to name a few.”


I think this person was trying to say that in the Linux world they don’t write setup programs. Well, I hate to disappoint you, but you have something just as complicated: imake, make, config files, and all that stuff, and when you’re done, you still distribute applications with a 20KB INSTALL file full of witty instructions like “You’re going to need zlib” (*what’s that?*) or “This may take a while. Go get some runts.” (Runts are a kind of candy, I think.) And the registry — instead of one big organized hive of name/value pairs, you have a thousand different file formats, one per application, with .whateverrc and foo.conf files living all over the place. And emacs wants you to learn how to program lisp if you’re going to change settings, and each shell wants you to learn its personal dialect of shell script programming if you want to change settings, and on and on.


People who only know one world get really smarmy, and every time they hear about the complications in the other world, it makes them think that their world doesn’t have complications. But they do. You’ve just moved beyond them because you are proficient in them. These worlds are just too big and complicated to compare any more. Lord Palmerston: “The Schleswig-Holstein question is so complicated, only three men in Europe have ever understood it. One was Prince Albert, who is dead. The second was a German professor who became mad. I am the third and I have forgotten all about it.” The software worlds are so huge and complicated and multifaceted that when I see otherwise intelligent people writing blog entries saying something [vacuous](http://www.winterspeak.com/2002_10_01_archive.html#85572348) like “Microsoft is bad at operating systems,” frankly, they just look dumb. Imagine trying to summarize millions of lines of code with hundreds of major feature areas created by thousands of programmers over a decade or two, where no one person can begin to understand even a large portion of it. I’m not even defending Microsoft, I’m just saying that big handwavy generalizations made from a position of deep ignorance is one of the biggest wastes of time on the net today.


Frequent readers, by now, have noticed that I’ve been thinking of the problem of how one might deliver an application on Linux, Macintosh, and Windows without paying disproportionately for the Linux and Macintosh versions. For this you need some kind of cross-platform library.


Java attempted this but Sun didn’t grok GUIs well enough to deliver really slick native-feeling applications. Like the [space alien](http://www.voyager.cz/tos/epizody/19squireofgothostrans.htm) in Star Trek watching Earth through a telescope, they knew exactly what human food was supposed to *look* like but they didn’t realize it was supposed to *taste* like something. Java apps have menus in the right places but there are all these keyboard things that don’t work the same way as every other Windows app and their tabbed dialogs look a little scary. And there is no way, no matter how hard you try, to make their menubars look exactly like Excel’s menubars. Why? Because Java doesn’t give you a very good way to drop down to the native facilities whenever the abstraction fails. When you’re programming in AWT, you can’t figure out the HWND of a window, you can’t call the Microsoft APIs, and you certainly can’t intercept WM_PAINT and do it differently. And Sun made it plenty clear that if you tried to do that, you weren’t Pure. You were Polluted, and to hell with you.


After a number of highly publicized failures to build GUIs with Java (e.g. Corel’s Java Office suite and Netscape’s Javagator), enough people know to stay away from this world. [Eclipse](http://www.eclipse.org/) built [their own](http://www.eclipse.org/articles/Article-SWT-Design-1/SWT-Design-1.html) windowing library from the ground up using native widgets just so they could write Java code that had a reasonably native look and feel.


The Mozilla engineers decided to address the cross platform problem with their own invention called XUL. So far, I’m impressed. Mozilla finally got to the point where it tastes like real food. Even my favorite bugaboo, Alt+Space N to minimize a window, works in Mozilla; it took them long enough but they did it.


Mitch Kapor, who founded Lotus and created 123, [decided](http://blogs.osafoundation.org/mitch/000007.html) for his next application to go with something called wxWindows and wxPython for cross platform support.


Which is better, XUL, Eclipse’s SWT, or wxWindows? I don’t know. They are all such huge worlds that I couldn’t really evaluate them and tell. It’s not enough to read the tutorials. You have to sweat and bleed with the thing for a year or two before you really know it’s good enough or realize that no matter how hard you try you can’t make your UI taste like real food. Unfortunately, for most projects, you have to decide on which world to use before you can write the first line of code, which is precisely the moment when you have the least information. At a previous job we had to live with some pretty bad architecture because the first programmers used the project to teach themselves C++ and Windows programming at the same time. Some of the oldest code was written without any comprehension of event-driven programming. The core string class (of course, we had our own string class) was a textbook example of all the mistakes you could make in designing a C++ class. Eventually we cleaned up and refactored a lot of that old code but it haunted us for a while.


So for now, my advice is this: don’t start a new project without at least one architect with several years of solid experience in the language, classes, APIs, and platforms you’re building on. If you have a choice of platforms, use the one your team has the most skills with, even if it’s not the trendiest or nominally the most productive. And when you’re designing abstractions or programming tools, go the extra mile to make them leak proof.
