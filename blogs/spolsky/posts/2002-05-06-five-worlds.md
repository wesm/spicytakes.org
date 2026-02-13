---
title: "Five Worlds"
date: 2002-05-06
url: https://www.joelonsoftware.com/2002/05/06/five-worlds/
word_count: 1874
---


Something important is almost never mentioned in all the literature about programming and software development, and as a result we sometimes misunderstand each other.


You’re a software developer. Me too. But we may not have the same goals and requirements. In fact there are several different worlds of software development, and different rules apply to different worlds.


You read a book about UML modeling, and nowhere does it say that it doesn’t make sense for programming device drivers. Or you read an article saying that “the 20MB runtime [required for .NET] is a [NON issue](http://radio.weblogs.com/0105852/2002/05/06.html)” and it doesn’t mention the obvious: if you’re trying to write code for a 32KB ROM on a pager it very much *is* an issue!


I think there are five worlds here, sometimes intersecting, often not. The five are:

1. Shrinkwrap
Internal
Embedded
Games
Throwaway


When you read the latest book about Extreme Programming, or one of Steve McConnell’s excellent books, or *Joel on Software*, or *[*Software Development*](http://www.sdmagazine.com/)* magazine, you see a lot of claims about how to do software development, but you hardly ever see any mention of what *kind* of development they’re talking about, which is unfortunate, because sometimes you need to do things differently in different worlds.


Let’s go over the categories briefly.


**Shrinkwrap** is software that needs to be used “in the wild” by a large number of people. It may be actually wrapped in cellophane and sold at CompUSA, or it may be downloaded over the Internet. It may be commercial or shareware or open source or GNU or whatever — the main point here is software that will be installed and used by thousands or millions of people.


Shrinkwrap has special problems which derive from two special properties:

- Since it has so many users who often have alternatives, the user interface needs to be easier than average in order to achieve success.
Since it runs on so many computers, the code must be unusually resilient to variations between computers. Last week someone emailed me about a bug in [CityDesk](http://www.fogcreek.com/CityDesk) which only appears in Polish Windows, because of the way that operating system uses Right-Alt to enter special characters. We tested Windows 95, 95OSR2, 98, 98SE, Me, NT 4.0, Win 2000, and Win XP. We tested with IE 5.01, 5.5, or 6.0 installed. We tested US, Spanish, French, Hebrew, and Chinese Windows. But we hadn’t *quite* gotten around to Polish yet.


There are three major variations of shrinkwrap. **Open Source** software is often developed without anyone getting paid to develop it, which changes the dynamics a lot. For example, things that are not considered “fun” often don’t get done in an all-volunteer team, and, as Matthew Thomas [points out eloquently](http://mpt.phrasewise.com/2002/04/13), this can hurt usability. Development is much more likely to be geographically dispersed, which results in a radically different quality of team communication. It’s rare in the open source world to have a face to face conversation around a whiteboard drawing boxes and arrows, so the kind of design decisions which benefit from drawing boxes and arrows are usually decided poorly on such projects. As a result geographically dispersed teams have done far better at cloning existing software where little or no design is required.


**Consultingware** is a variant of shrinkwrap which requires so much customization and installation that you need an army of consultants to install it, at outrageous cost. CRM and CMS packages often fall in this category. One gets the feeling that they don’t actually *do* anything, they are just an excuse to get an army of consultants in the door billing at $300/hour. Although consultingware is disguised as shrinkwrap, the high cost of an implementation means this is really more like internal software.


**Commercial web based software** such as Salesforce.com or even the more garden variety eBay still needs to be easy to use and run on many browsers. Although the developers have the luxury of (at least) some control over the “deployment” environment — the computers in the data center — they have to deal with a wide variety of web browsers and a large number of users so I consider this basically a variation of shrinkwrap.


**Internal **software only has to work in one situation on one company’s computers. This makes it a lot easier to develop. You can make lots of assumptions about the environment under which it will run. You can require a particular version of Internet Explorer, or Microsoft Office, or Windows. If you need a graph, let Excel build it for you; everybody in our department has Excel. (But try that with a shrinkwrap package and you eliminate half of your potential customers.)


Here usability is a lower priority, because a limited number of people need to use the software, and they don’t have any choice in the matter, and they will just have to deal with it. Speed of development is more important. Because the value of the development effort is spread over only one company, the amount of development resources that can be justified is significantly less. Microsoft can afford to spend $500,000,000 developing an operating system that’s only worth about $80 to the average person. But when Detroit Edison develops an energy trading platform, that investment must make sense for a single company. To get a reasonable ROI you can’t spend as much as you would on shrinkwrap. So sadly lots of internal software sucks pretty badly.


**Embedded Software** has the unique property that it goes in a piece of hardware and in almost every case can never be updated. This is a whole different world, here. The quality requirements are much higher, because there are no second chances. You may be dealing with a processor that runs dramatically more slowly than the typical desktop processor, so you may spend a lot of time optimizing. Fast code is more important than elegant code. The input and output devices available to you may be limited. The GPS system in the car I rented last week had such pathetic I/O that the usability was dismal. Have you ever tried to input an address on one of these things? They displayed a “keyboard” on screen and you had to use the directional arrows to choose letters from five small matrices of [9 letters each](http://www.hertz.co.uk/serv/us/prod_lost.html). (Follow the link for more illustrations of this UI. The GPS in my own car has a touch screen which makes the UI dramatically better. But I digress).


**Games** are unique for two reasons. First, the economics of game development are hit-oriented. Some games are hits, many more games are failures, and if you want to make money on game software you recognize this and make sure that you have a portfolio of games so that the blockbuster hit makes up for the losses on the failures. This is more like movies than software.


The bigger issue with the development of games is that there’s only one version. Once your users have played through Duke Nukem 3D, they are not going to upgrade to Duke Nukem 3.1D just to get some bug fixes and new weapons. With some exceptions, once somebody has played the game to the end, it’s boring to play it again. So games have the same quality requirements as embedded software and an incredible financial imperative to get it right the first time. Shrinkwrap developers have the luxury of knowing that if 1.0 doesn’t meet people’s needs and doesn’t sell, maybe 2.0 will.


Finally **Throwaway **code is code that you create temporarily solely for the purpose of obtaining something else, which you never need to use again once you obtain that thing. For example, you might write a little shell script that massages an input file that you got into the format you need it for some other purpose, and this is a one time operation.


There are probably other kinds of software development that I’m forgetting.


Here’s an important thing to know. Whenever you read one of those books about programming methodologies written by a full time software development guru/consultant, you can rest assured that they are talking about internal, corporate software development. Not shrinkwrapped software, not embedded software, and certainly not games. Why? Because corporations are the people who hire these gurus. They’re paying the bill. (Trust me, id software is *not* about to hire Ed Yourdon to talk about structured analysis.)


Last week Kent Beck made a claim that you don’t really need bug tracking databases when you’re doing Extreme Programming, because the combination of pair programming (with persistent code review) and test driven development (guaranteeing 100% code coverage of the automated tests) means you *hardly ever have bugs*. That didn’t sound right to me. I looked in our own [bug tracking database](http://www.fogcreek.com/FogBUGZ) here at Fog Creek to see what kinds of bugs were keeping it busy.


Lo and behold, I discovered that very few of the bugs in there would have been discovered with pair programming or test driven development. Many of our “bugs” are really what XP calls stories — basically, just feature requests. We’re using the bug tracking system as a way of remembering, prioritizing, and managing all the little improvements and big features we want to implement.


A lot of the other bugs were only discovered after much use in the field. The Polish keyboard thing. There’s no way pair programming was going to find *that*. And logical mistakes that never occurred to us in the way that different features work together. The larger and more complex a program, the more interactions between the features that you don’t think about. A particular unlikely sequence of characters ({${?, if you must know) that confuses the lexer. Some ftp servers produce an error when you delete a file that doesn’t exist (our ftp server does not complain so this never occurred to us.)


I carefully studied every bug. Out of 106 bugs we fixed for the service pack release of CityDesk, exactly 5 of them could have been prevented through pair programming or test driven design. We actually had more bugs that we *knew about *and thought weren’t important (only to be corrected by our customers!) than bugs that could have been caught by XP methods.


But Kent is right, for other types of development. For most corporate development applications, none of these things would be considered a bug. Program crashes on invalid input? Run it again, and this time watch your {${?’s! And we only have One Kind of FTP server and nobody in the whole company uses Polish Windows.


Most things in software development are the same no matter what kind of project you’re working on, but not everything. When somebody tells you about methodology, think about how it applies to the work *you’re* doing. Think about where the person is coming from. Steve McConnell, Steve Maguire, and I all come from a very narrow corner: the world of mass market shrinkwrap spreadsheet applications written in Redmond, Washington. As such we have higher bars for ease of use and lower bars for bugs. Most of the other methodology gurus make their living doing consulting for in house corporate development, and that’s what they’re talking about. In any case, we should all be able to learn something from each other.
