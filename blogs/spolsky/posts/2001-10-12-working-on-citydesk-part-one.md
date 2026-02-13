---
title: "Working on CityDesk, Part One"
date: 2001-10-12
url: https://www.joelonsoftware.com/2001/10/12/working-on-citydesk-part-one/
word_count: 750
---


I’ve been rather quiet lately on this weblog — mainly because we’ve been working so hard at Fog Creek getting ready for the beta of [CityDesk](https://www.joelonsoftware.com/articles/fog0000000010.html), our flagship product. But I’d like to spend some time now talking about the design and development of CityDesk, because it’s a great case study for the kind of software development practices that I’ve been advocating here for more than a year. Over the next few columns, I’ll focus on “The Story of CityDesk,” with a look at some of the behind-the-scenes, day-to-day stories of a real software development project.


We’re launching the beta on October 15th — just three days away! This is officially On Time. We made a schedule for shipping CityDesk way back in June. We figured out estimates for all the remaining tasks and bug fixes, added them up, and got October 15th.


Every couple of weeks, we checked through our task list, revised estimates, and so forth. We’ve found a lot of bugs over that time and added a lot of small features, but we’ve also killed a lot of features that we just won’t have time for. And lo and behold, now we are almost completely done.  Most of what we’re doing these days is getting set up to run the beta. Michael added a dialog box to CityDesk for sending feedback. He also wrote some very spiffy code that catches any unhandled exception on any copy of CityDesk running anywhere in the world, prevents the app from crashing, and pushes the exception info up to our [FogBUGZ](http://www.fogcreek.com/FogBUGZ) bug tracking database here in New York City. I’ve been fixing bugs, writing the help file, and writing some pages for our corporate web site that will explain what CityDesk is and why you would buy it.


A common misconception, I assume popularized by Hollywood, is that as you get closer to shipping software, activity becomes frenetic as everybody scrambles to finish all the things that need to be done in time for the deadline. In the typical crappy movie, there’s a mad rush of typing in a room full of cool alterna-dressed programmers with found-object earrings and jeans jackets. Somebody stands up and shouts to the room in general “I need the Jiff subroutine! Somebody give me the Jiff subroutine!” A good looking young woman in Vivienne Tam urbanwear throws a floppy disk at him. “Thanks!”


As the second hand swoops towards the :00, the whole team waits breathlessly around Ryan Phillipe’s computer and watches the “copy” progress indicator as the final bits are put onto a floppy disk with less than a second to spare before the VC cuts off funding.


I suppose some software shops have last-minute coding frenzies like this. If so, their software is probably marked by incredibly poor quality. No code works the way you expected it to work the first time, and if you’re writing code up until the last minute, it’s going to suck. The first Netscape open source release, documented in the excellent movie [Code Rush](http://www.amazon.com/exec/obidos/ASIN/B00004T128/joelonsoftware) , demonstrates this.


On good teams, the days before shipping just get quieter and quieter as programmers literally run out of things to do one at a time. (Yesterday I took the day off to explore New York City with my wee niece and nephews.)


The number of new bugs being found has decreased to a point at which we feel confident about releasing the beta. It is crucial to get to zero known bugs (what Netscape famously called “Zarro Boogs”) before releasing a beta. If you don’t, you’ll waste a lot of time during the beta reading 200 emails about a bug that you already knew about. And you’ve just used up time and goodwill of those 200 beta testers, so they may not bother telling you about the next bug they find, something you *didn’t* know about. Or the bug may stop them from trying other parts of the program that needs some pounding. This seems self-evident, but almost every time I’ve been on a real product, everybody starts to think that releasing the beta on time is more important than releasing a Zero Known Bugs beta. (After all, it’s *ok* to have bugs in the beta, they say. And I agree: it *is* ok to have bugs in the beta, just not *known bugs*.)


I’ll keep posting The Story of CityDesk over the next few days, keep an eye out for frequent updates.


Working on CityDesk Part: [1](https://www.joelonsoftware.com/articles/fog0000000009.html) [2](https://www.joelonsoftware.com/articles/fog0000000008.html) [3](https://www.joelonsoftware.com/articles/fog0000000006.html) [4](https://www.joelonsoftware.com/articles/fog0000000250.html) [5](https://www.joelonsoftware.com/articles/fog0000000296.html)
