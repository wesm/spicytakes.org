---
title: "Working on CityDesk, Part Three"
date: 2001-10-17
url: https://www.joelonsoftware.com/2001/10/17/working-on-citydesk-part-three/
word_count: 1322
---


Like all good hackers, I have been programming since junior high, using my dad’s account on the University of New Mexico IBM 360 mainframe. But the first real computer science course I took was during the first year of college. The course covered C and assembler. It had hundreds of students, most of whom, like me, had been fooling around in Pascal or Basic since they were toddlers.


The course proceeded merrily until one day, the professor introduced pointers.


Dread.


Suddenly, the majority of the students in the class were in deep trouble. For some reason, some people just do not seem to be able to write code with pointers in it. They were born without the part of the brain that does indirection, I guess.


Since then, I’ve mentally divided the world into three groups. The largest group of people can’t program at all. There’s another, smaller group of people who can program, but not with pointers. And there’s a tiny group of people who can program, even with pointers. Those elite few can even understand what it means to write **CString*&** in C++.


My first job at Microsoft was putting a decent scripting language into Excel. Although I was given free rein to implement whatever language I saw fit, we went with Basic for several reasons. (1) We had a Basic compiler team in house. (2) You didn’t need pointers, which meant that (3) more people are comfortable using Basic than any other language. Indeed Visual Basic is the best-selling language product of all time.


Visual Basic is an extremely productive way to write code, especially GUI code. Want bold text on a dialog box? It’s one click in VB. Now try doing it in MFC. You have to create a subclassed control, it’s a big mess, you have to know all about LOGFONTS and Windows window subclassing and a bunch of other things and you need about three lines of code once you have the magic class.


But many VB programs are spaghetti, either because they’re done as quick and dirty one-offs, or because they’re written by hack programmers without training in object oriented programming, or even structured programming.


What I wondered was, what happens if you take top-notch C++ programmers who dream in pointers, and let them code in VB. What I discovered at Fog Creek was that they become super-efficient coding machines. The code looks pretty good, it’s object-oriented and robust, but you don’t waste time using tools that are at a level lower than you need. I’ve spent years writing code for C++/MFC and years writing code in Visual Basic, and let me tell you, VB is just much, much more productive. Michael and I had a good laugh today when we discovered [somebody](http://www.appowersystems.com/APPowerBetaTest.htm) selling a beta crash-reporting product at $5000 for three months that Michael implemented in CityDesk in two days. (And we actually implemented a good part of ours in C++/ATL). And I also guarantee you that our Visual Basic code in CityDesk looks a lot better than most of the code you find written in macho languages like C++, because we’re good programmers, and we write comments, and our variable names are well-chosen, and we do things the simple way, not the clever way, and so forth.


I’ll go out on a limb here. In my years of experience, I have seen many language and programming fads come and go. But there’s only ONE, that’s right, ONE language feature I’ve ever seen that actually improves your productivity significantly. No, it’s not object oriented programming; no, it’s not intentional programming or assertions or programming by example or CASE or UML or XML or Java. The only thing that improves your programming productivity is using *managed code* – that is, using a language in which memory management is automatic. Java and .NET languages do this with garbage collection; VB does this with reference counting; I don’t care how you do it, just let me concatenate strings without thinking about where the new bigger string will go and I’ll be happy.


One of the things about Visual Basic is that it doesn’t always give you access to the full repertoire of Windows goodies that you need to make a polished application. But what it does do, better than almost any other programming environment, is let you drop into C++ code (or call C APIs) when you’re desperate or when you need that extra speed. For example, you can always get the HWND of a control and do native stuff to it, which is not the case in Java. As another example, a lot of the non-GUI, time-sensitive inner loops, like the word counter, in CityDesk are actually implemented in C or C++ for speed. This ability gave us the confidence to use Visual Basic even though it can’t do everything and it tends to do string processing slowly. But since we’re all C++ programmers, we have no fear of creating a DLL or OCX to count words, or parse script, or call a Windows API. So about 5% of CityDesk is actually in C or C++, and we’ll probably move a little bit more of the code to C++ to speed up a few more inner loops.


Now, Visual Basic is not the perfect programming language. It’s fairly object oriented but there are little things that you can’t do with it, like have base classes with implementation reuse. It’s limited to Windows. And the worst part about coding in VB is that people think you’re not cool because your code doesn’t have {‘s and }’s. I can live with the shame if it means I’m more productive.


Philosophically, I think that C# has a bright future in the Windows GUI programming world. It’s not as embarrassing as VB, and it uses the type of syntax which C/C++/Java programmers have come to love. VB programmers looking to upgrade can’t upgrade painlessly to VB.NET, because there are so many major differences in the programming environment. Even Microsoft admits that you can’t port from VB to VB.NET, you have to rewrite. And that’s enough of a pain that many VB programmers will use this opportunity to look around at what else is out there. I think many will choose C#, because it’s virtually the same language as VB.NET with slightly different syntax and vastly less stigma attached to it.


What about Java? Yes, I’ve used Java extensively, but unfortunately the language, the code libraries, and especially the GUI libraries are just too primitive for a commercial desktop application. I like the language and I appreciate the benefit of write-once-run-anywhere, but frankly not a lot of desktop software is sold for Sun Solaris and I think that WORA benefits Sun more than it benefits software developers, and I’m not willing to write an app that behaves in an inferior way on 95% of my customer’s computers to benefit the 5% with alternate platforms. Every Java app LOOKS like a Java app, takes forever to launch, and just doesn’t feel completely native. Since CityDesk’s competitive advantage comes from having an excellent GUI, that’s one area where I refuse to skimp.


I am virtually certain that I will now receive a million emails from lovers of tcl/tk, or Delphi, or C++ Builder, or NextStep, or Cocoa, or perl, or Python, or RealBASIC, or some other programming environment which may or may not be suitable for creating a professional Windows GUI. That’s nice. I don’t really want to get into a debate about language features or programming environment features — at some point, you have to stop debating and write code! I’m just trying to explain why we chose to use VB for the GUI part and C++ for time sensitive bits of code. If you do want to have a fun religious war over programming languages, please do so on the [discussion group](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=319)!


Working on CityDesk Part: [1](https://www.joelonsoftware.com/articles/fog0000000009.html) [2](https://www.joelonsoftware.com/articles/fog0000000008.html) [3](https://www.joelonsoftware.com/articles/fog0000000006.html) [4](https://www.joelonsoftware.com/articles/fog0000000250.html) [5](https://www.joelonsoftware.com/articles/fog0000000296.html)
