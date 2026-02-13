---
title: "Craftsmanship"
date: 2003-12-01
url: https://www.joelonsoftware.com/2003/12/01/craftsmanship-2/
word_count: 1312
---


Making software is not a manufacturing process. In the 1980s everyone was running around terrified that Japanese software companies were setting up “software factories” that could churn out high quality code on an assembly line. It didn’t make any sense then and it doesn’t make sense now. Shoving a lot of programmers into a room and lining them up in neat rows did not really help get the bug counts down.


If writing code is not assembly-line style production, what is it? Some have proposed the label *craftsmanship*. That’s not quite right, either, because I don’t care what you say: that dialog box in Windows that asks you how you want your help file indexed does not in any way, shape, or form resemble what any normal English speaker would refer to as “craftsmanship.”


Writing code is not *production*, it’s not always craftsmanship (though it can be), it’s *design*. Design is that nebulous area where you can add value faster than you add cost. The New York Times magazine [has been raving about the iPod](http://www.nytimes.com/2003/11/30/magazine/30IPOD.html) and how Apple is one of the few companies that knows how to use good design to add value. But I’ve talked [enough](https://www.joelonsoftware.com/uibook/chapters/fog0000000057.html) about design, I want to talk about craftsmanship for a minute: what it is and how you recognize it.


I’d like to tell you about at a piece of code I’ve been rewriting for CityDesk 3.0: the file import code. (Advertainment: [CityDesk](http://www.fogcreek.com/CityDesk) is my company’s easy-to-use content management product.)


The spec seems about as simple as any snippet of code can be. The user chooses a file using a standard dialog box, and the program copies that file into the CityDesk database.


This turned out to be a great example of one of those places where “the last 1% of the code takes 90% of the time.” The first draft of the code looked like this:

1. Open the file
2. Read it all into a big byte array
3. Store the byte array in a record


Worked great. For reasonable sized existing files it was practically instantaneous. It had a few little bugs, which I worked through one at a time.


The big bug surfaced when I stress-tested it by dragging a 120 MB file into CityDesk. Now, it is not common by any means for people to post 120 MB files on their web sites. In fact, it’s quite rare. But it’s not impossible, either. The code worked but took almost a minute and provided no visual feedback — the app just froze and appeared to be completely locked up. This is obviously not ideal.


From a UI perspective, what I really wanted was for long operations to bring up a progress bar of some sort, along with a Cancel button. In the ideal world you would be able to continue doing other operations with CityDesk while the file copy proceeded in the background. There were three obvious ways to do this:

1. From a single thread, polling frequently for input events
2. By launching a second thread and synchronizing it carefully
3. By launching a second process and synchronizing it less carefully


My experience with #1 is that it never quite works. It is too hard to ensure that all the code throughout your application can be run safely while a file copy operation is in progress. And [Eric S. Raymond](http://www.faqs.org/docs/artu/ch07s03.html#id2923889) has convinced me that threads are usually not as good a solution as separate processes: indeed years of experience have shown me that programming with multiple threads creates much additional complexity and introduces whole new categories of dangerously frightful [heisenbugs](http://c2.com/cgi/like?HeisenBug). #3 seemed like a good solution, especially since our underlying database is multiuser and doesn’t mind lots of processes banging on it at the same time. So that’s what I’m planning to do when I get back from Thanksgiving vacation.


Notice, though, the big picture. We’ve gone from read the file/save it in the database to something significantly more complicated: launch a child process, tell *it* to read the file and save it in the database, add a progress bar and cancel button to the child process, and then some kind of mechanism so the child can notify the parent when the file has arrived so it can be displayed. There will also be some work passing command line arguments to the child process, and making sure the window focus behaves in an expected manner, and handling the case of the user shutting down their system while a file copy is in progress. I would guesstimate that when all is said and done I’ll have ten times as much code to handle large files gracefully, code that maybe 1% of our users will ever see.


And of course, a certain type of programmer will argue that my new child-process architecture is inferior to the original. It’s “bloated” (because of all the extra lines of code). It has more potential for bugs, because of all the extra lines of code. It’s overkill. It’s somehow emblematic of why Windows is an inferior operating system, they will say. What’s all this about progress indicators? they sneer. Just hit Ctrl+Z and then “ls -l” repeatedly and watch to see if the file size is growing!


The moral of the story is sometimes fixing a 1% defect takes 500% effort. This is not unique to software, no sirree, now that I’m managing all these construction projects I can tell you that. Last week, finally, our contractor finally put the finishing touches on the [new Fog Creek offices](https://www.joelonsoftware.com/articles/BionicOffice.html). This consisted of installing shiny blue acrylic on the front doors, surrounded by aluminium trim with a screw every [20 cm](http://www.google.com/search?hl=en&lr=&ie=UTF-8&oe=UTF-8&safe=off&q=20+centimeters+in+inches&btnG=Google+Search). If you look closely at the picture, the aluminium trim goes all the way around each door. Where the doors meet, there are two pieces of vertical trim right next to each other. You can’t tell this from the picture, but the screws in the middle strips are *almost* but not *exactly* lined up. They are, maybe, 2 millimeters off. The carpenter working on this measured carefully, but he was installing the trim while the doors were on the ground, not mounted in place, and when the doors were mounted, “oops,” it became clear that the screws were not exactly lined up.


This is probably not that uncommon; there are lots of screws in our office that don’t line up perfectly. The problem is that fixing this once the holes are drilled would be ridiculously expensive. Since the correct placement for the screws is only a couple of millimeters away, you can’t just drill new holes in the door; you’d probably have to replace the whole door. It’s just not worth it. Another case where fixing a 1% defect takes 500% effort, and it explains why so many artifacts in our world are 99% good, not 100% good. (Our architect never stops raving about some really, really expensive house in Arizona where every screw lined up.)


It comes down to an attribute of software that most people think of as *craftsmanship*. When software is built by a true craftsman, all the screws line up. When you do something rare, the application behaves intelligently. More effort went into getting rare cases exactly right than getting the main code working. Even if it took an extra 500% effort to handle 1% of the cases.


Craftsmanship is, of course, incredibly expensive. The only way you can afford it is when you are developing software for a mass audience. Sorry, but internal HR applications developed at insurance companies are never going to reach this level of craftsmanship because there simply *aren’t enough users* to spread the extra cost out. For a shrinkwrapped software company, though, this level of craftsmanship is precisely what delights users and provides longstanding competitive advantage, so I’ll [take the time](https://www.joelonsoftware.com/articles/fog0000000017.html) and do it right. Bear with me.
