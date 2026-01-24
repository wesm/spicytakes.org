---
title: "The User Interface Is The Application"
date: 2005-08-24
url: https://blog.codinghorror.com/the-user-interface-is-the-application/
slug: the-user-interface-is-the-application
word_count: 488
---

Shawn Burke’s post [Shippin’ Ain’t Easy](https://web.archive.org/web/20051122195130/http://www.shawnburke.net/default.aspx?document=264&userinterface=9) (but [somebody gotta do it](https://www.azlyrics.com/lyrics/icet/somebodygottadoitpimpinainteasy.html)) explains why you have to resist change at the end of a project, no matter how justifiable and rational the reasons may be. Even the smallest change has a real risk of introducing additional bugs. The first commenter quipped:


> TeX doesn’t have bugs... Perhaps that’s the exception that proves the rule :-)


[Ian Ringrose](https://web.archive.org/web/20050829004535/http://www.ringrose.name/) immediately replied:


> But does it have any users? **Is the fact that it’s very hard to use not a bug in and of itself?**


Touch.


Yukihiro Matsumoto, the creator of Ruby, has [strong feelings on this subject](http://www.artima.com/intv/craft.html):


> If you have a good interface on your system, and a budget of money and time, you can work on your system. If your system has bugs or is too slow, you can improve it. But if your system has a bad interface, you basically have nothing. It won’t matter if it is a work of the highest craftsmanship on the inside. **If your system has a bad interface, no one will use it**. So the interface or surface of the system, whether to users or other machines, is very important.


It’s also something Joel calls [the iceberg secret](http://www.joelonsoftware.com/articles/fog0000000356.html):


> I learned this lesson as a consultant, when I did a demo of a major web-based project for a client’s executive team. The project was almost 100% code complete. We were still waiting for the graphic designer to choose fonts and colors and draw the cool 3-D tabs. In the meantime, we just used plain fonts and black and white, there was a bunch of ugly wasted space on the screen, basically it didn’t look very good at all. But 100% of the functionality was there and was doing some pretty amazing stuff.
> What happened during the demo? **The clients spent the entire meeting griping about the graphical appearance of the screen.** They weren’t even talking about the UI. Just the graphical appearance. “It just doesn’t look slick,” complained their project manager. That’s all they could think about. We couldn’t get them to think about the actual functionality. Obviously fixing the graphic design took about one day. It was almost as if they thought they had hired painters.


I had this *exact* experience on a project recently. We’re building all this cool back-end stuff, natch, and we needed a quickie front-end demo app to show it off. So we built a relatively simple demo app. It’s decent, but barely competitive with other companies websites.


Guess what the client thought of our project?


I don’t care how many kick-ass Visio architecture diagrams you have; as far as the user is concerned, **the UI is the application**. I know [UI is Hard](https://blog.codinghorror.com/ui-is-hard/), but you *have* to build an impressive UI if you want to be taken seriously. Give your UI the high priority it deserves.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
