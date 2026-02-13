---
title: "Working on CityDesk, Part Five"
date: 2001-11-13
url: https://www.joelonsoftware.com/2001/11/13/working-on-citydesk-part-five/
word_count: 1678
---


As promised I’ve been writing a series of articles about the creation of [CityDesk](https://www.joelonsoftware.com/articles/fog0000000010.html). The primary purpose of these articles is to share the reasoning behind some of the decisions we made as a software company, and the techniques we used in developing our flagship software product. Today I want to talk about the five guiding principles that shaped the architecture.


One of the biggest decisions we made about CityDesk was to make a standalone Windows executable. With all the hubbub about web services, not to mention the noisy Internet dotcom boom we just lived through, this was a non-obvious decision. Why is CityDesk one of those old-fashioned programs you download and run, instead of, say, a web site you go to, in the style of Blogger or Atomz? Or a web server you install, like the Big Iron content management systems (Interwoven, Vignette StoryServer, etc.)?


An even more non-obvious decision was not to use XML. People who were a little bit too close to Silicon Valley groupthink looked at us like we were crazy because CityDesk is *not* based on XML and is not delivered through a web browser.


Now we’re thanking our lucky stars that we didn’t have a bunch of stupid venture capitalists forcing us to copy all the other content management companies, and we’re grateful that we’re not in Silicon Valley where everyone meets at Bucks and Stanford University seminars and copies each other’s bad ideas, because the one thing we’ve heard from everybody who’s tried CityDesk, *consistently*, is that CityDesk is the easiest content management software they’ve ever seen, full stop. And we got this ease-of-use because we believed certain things about software.


**1. You can’t do good UIs in a web browser.**


When we started building CityDesk we kept hearing one thing about Big Iron content management systems, which were all web-browser-based. Despite the fact that these systems had web-based editing interfaces and advanced workflow, we kept hearing that in real life, reporters created their content in Microsoft Word, did the workflow the old way (email), and only at the very last minute, a secretary opened the Word file and cut and pasted it into the content management system.


Why?


Because nobody wants to compose in a big TEXTAREA on an HTML page.


There are too many things that are impossible to deliver properly in a web browser. First of all, there’s the latency. Even if the web server is running on your *own machine*, round trips still take a certain amount of time, so all web applications feel somewhat sluggish. Second, there is no decent text editing widget for web browsers. With CityDesk as a Windows program, I can give you a feature where you can drag a picture from the desktop into an article. There is no way to create that kind of user interface through the web. I can keep a word count in the corner of the screen and update it in the background whenever you stop typing. You can use Ctrl+S to save without losing your place in the document — something many writers have learned to do regularly. (Good luck creating a word processor inside a web browser that doesn’t instantly lose everything, without prompting, if the user closes the browser). CityDesk has menus. Remember menus? And they work exactly like you expected them to, because the web browser doesn’t have it’s own menu, with a bunch of irrelevant commands, that wants to eat the Alt key. We don’t have to waste any screen real estate on browser geegaws (like “back” buttons and spinning e-globes) that have no meaning for CityDesk. We get our own icon in the taskbar instead of looking like all the other web browsers you have open. I could go on for days about the nice UI things we can do in a Windows application that just can’t be done with a web browser. In fact there’s a whole chapter about it in the printed edition of [my book](https://www.joelonsoftware.com/uibook/chapters/fog0000000057.html).


“Sure,” you say, “you can’t get *as* slick an app through the web, but you get ubiquity! People can go to an Internet cafe in Phuket and …”  Yeah, OK, that sounds great for Hotmail. And in the future we *will* build a typical compromise-laden web interface to CityDesk for those times when you’re at the beach in Thailand. In the meantime, my number one priority is to make an application that’s easy to use so that people like it, so that they tell their friends about it, so that everybody buys it and we have to hire full time employees just to slit open the envelopes and take out the checks.


**2. XML is a Dumb Format For Storing Data**


I’m not sure *why* XML got so sexy. It has its advantages; it’s sure a good idea for data interchange or for all those little files you need to store settings. But for real work it just can’t do what a solid, multiuser, relational database can do. The next time some uninformed analyst at Gartner or Giga or Forrester tells you “in the future, everything will be XML,” ask them how to do “SELECT author FROM books” fast with XML. Hint: you can’t. It has to be slow. XML is not the way to store a lot of data. Now tell me how to insert a new book at the beginning of the table without massive bitblts. Of course, I doubt if there is an analyst in one of those companies who would even understand that sentence, but that’s life. In the meantime, CityDesk uses a relational database. Over and out.


**3. Most People Don’t Control Their Web Servers**


Of all the people in the world who need to put data up on the web, only a tiny percentage of them have any control whatsoever over what software runs on their web server. We decided that CityDesk has to be an all-client application because probably 95% of the people who maintain web sites simply do not have the ability to install a content management system on their web server, even if they wanted to. We reduced the server requirements of CityDesk to (a) any web server that knows how to serve static files and (b) ftp or file copy access to that server. We think this will open up content management to a whole new universe of potential users.


**4. If You Can Only Do One Platform, Do Windows.**


I’d love to have a Mac version and a Linux version, but they are not good uses of limited resources. Every dollar I invest in CityDesk Windows will earn me 20 times as many sales as a dollar invested in a hypothetical Mac version. Even if you assume that Mac has a higher percentage of creative and home users, I’m still going to sell a heck of a lot more copies on Windows than I could on Mac. And that means that to do a Mac version, the cost had better be under 10% of the cost of a Windows version. Unfortunately, that’s nowhere near true for CityDesk. We benefit from using libraries that are freely available on Windows (like the Jet multiuser [ACID](http://www.arsdigita.com/books/panda/databases-choosing) database engine and the DHTML edit control) for which there are no equivalents on the Macintosh. So if anything, a Mac port would cost *more* than the original Windows version. Until somebody does something about this fundamental economic truth, it’s hard to justify Mac versions from a business perspective. (Incidentally, I have said time and time again, if Apple wants to save the Mac, they have to change this equation.)


And don’t get me started about Linux. I don’t know of anyone making money off of Linux desktop software, and without making money, I can’t pay programmers and rent and buy computers and T1s. Despite romantic rhetoric, I really do need to pay the rent, so for now, you’re going to have to rely on college kids and the occasional charitable big company for your Linux software.


**5. Content Management Can’t Require Programmers**


One of the reasons Big Iron content management costs so much is the team of programmers it takes to figure out the thing and set it up. Even the free and low-cost content management systems are designed by geeks for geeks. People have said to me that there’s no market for CityDesk because “with XML and XSL it’s a solved problem.”


Uh huh. Thanks. Even I can’t figure out XML and XSL, and I’m pretty sharp.


We decided that everything in CityDesk has to be simple enough for web designers and HTMLers, who are not necessarily programmers. And for the end-user, even HTML is too much. To the end-user CityDesk can’t be any more complicated than a WYSIWYG word processor.


The rule of thumb with ease-of-use is that if you make your program 10% easier, you’ll *double *the potential number of users of your product. In CityDesk we made absolutely no compromises on ease of use. Sure, it’s not the most powerful system out there. We’ll compromise on that. And you can’t update your blog from an Internet Cafe in Bali. Another compromise. But I guarantee you that any HTMLer can create CityDesk sites, and anyone who can use a word processor can manage a site that was created for them by an HTMLer, and you’ll never need a programmer.


**Summary**


All in all we made a bunch of decisions based on a world view that, frankly, was not very popular during the Internet boom. There was a time when you couldn’t get funding for a company that wasn’t a web pure play. And the lemming VCs thought that they had to do what all the other VCs were doing: pure web interfaces. To which I say, Thank you! Thank you for keeping your dumb overfunded companies out of my way, because now, over here in GUI land, I can’t find any real competition, and now you’re not funding *anyone*, so it’s smooth sailing for Fog Creek.


Working on CityDesk Part: [1](https://www.joelonsoftware.com/articles/fog0000000009.html) [2](https://www.joelonsoftware.com/articles/fog0000000008.html) [3](https://www.joelonsoftware.com/articles/fog0000000006.html) [4](https://www.joelonsoftware.com/articles/fog0000000250.html) [5](https://www.joelonsoftware.com/articles/fog0000000296.html)
