---
title: "The Sugar UI"
date: 2007-01-04
url: https://blog.codinghorror.com/the-sugar-ui/
slug: the-sugar-ui
word_count: 805
---

I’ve largely been ignoring Nicholas Negroponte’s [One Laptop Per Child](http://wiki.laptop.org/go/Main_Page) initiative. I appreciate the nobility of the gesture, but how interesting can sub-$100 hardware running Linux really *be*? Well, that was before I read about [the novel user interface](https://web.archive.org/web/20070109044136/http://www.cnn.com/2007/TECH/01/02/hundred.dollarlaptop.ap/index.html) they’re building into those small green and white laptops.


> For most of these children the XO machine, as it’s called, likely will be the first computer they’ve ever used. Because the students have no expectations for what PCs should be like, the laptop’s creators started from scratch in designing a user interface they figured would be intuitive for children.
> **The result is as unusual as – but possibly even riskier than – other much-debated aspects of the machine, such as its economics and distinctive hand-pulled mechanism for charging its battery.** (XO has been known as the $100 laptop because of the ultra-low cost its creators eventually hope to achieve through mass production.)
> For example, students who turn on the small green-and-white computers will be greeted by a basic home screen with a stick-figure icon at the center, surrounded by a white ring. The entire desktop has a black frame with more icons.
> This runic setup signifies the student at the middle. The ring contains programs the student is running, which can be launched by clicking the appropriate icon in the black frame.
> When the student opts to view the entire “neighborhood” – the XO’s preferred term instead of “desktop” – other stick figures in different colors might appear on the screen. Those indicate schoolmates who are nearby, as detected by the computers’ built-in wireless networking capability.
> Moving the PC’s cursor over the classmates’ icons will pull up their names or photos. With further clicks the students can chat with each other or collaborate on things – an art project, say, or a music program on the computer, which has built-in speakers.


![Sugar UI screenshot -- neighborhood](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfIzRf8M7foAkzu0UxePbBROgtNHFzj_klsDZ2S6BEis3zWF3wooqXU9caJoSw-4O8VR4QZmp95c7NgD-zUPKpK6LPmqCPgl4yjQeSIjg9-4_By3igOx5sss9o9WvYoX0mzkUU4PA?key=EFBg8Ij0aJ1EmCyuDte1jBlv)


I’m interested now.


I’ve been disappointed in the lack of GUI innovation over the last decade. Sure, Microsoft and Apple take small jabs at each other every couple of years. And the Linux community apes both companies, occasionally throwing in a curveball of their own. **But when was the last time anyone tried a radically different UI on the desktop?** The Sugar UI featured in the OLPC appears to finally break from the well worn conventions of Windows and MacOS.


I wanted to try it out myself. I downloaded [the emulated OLPC laptop image](http://wiki.laptop.org/go/OS_images_for_emulation) and ran it under QEMU. The documentation even warns you to prepare yourself for this alien UI experience.


> Before you launch the emulated image, we strongly recommend reading through the [Sugar Instructions](http://wiki.laptop.org/go/Sugar_Instructions) on how to use the environment – **this does not look like the Windows or Mac operating systems!**


They weren’t kidding. It’s nothing like any traditional GUI.


![Sugar UI screenshot -- browser](https://blog.codinghorror.com/content/images/uploads/2007/01/6a0120a85dcdae970b0128776fe70e970c-pi.png)


I was inclined to like Sugar almost immediately because it embodies a number of experimental GUI concepts I’ve talked about before:

- The frame menu makes perfect use of the [infinite width at the edges of the screen](https://blog.codinghorror.com/fitts-law-and-infinite-width/).
- It [abandons files and folders](https://blog.codinghorror.com/filesystems-arent-a-feature/) as an organizing concept.
- The start page, a ring of running tasks around a student, is a type of [pie menu](http://en.wikipedia.org/wiki/Pie_menu), which is a [no-frills version of mouse gestures](https://blog.codinghorror.com/will-mouse-gestures-ever-be-mainstream/).
- The seamless integration of collaboration and sharing – with or without the internet – is very Web 2.0.


Sugar UI development appears to lag quite a bit behind the challenging, sub-$100 design goal of the OLPC hardware itself. This doesn’t surprise me, because [developing UI is hard](https://blog.codinghorror.com/ui-is-hard/). And developing a radically different UI has to be especially difficult. Innovation and experimentation is much riskier than following the roadmaps from Redmond and Cupertino. That’s why, despite the rough edges, I’m excited about Sugar.


The Sugar instructions offer an excellent basic overview of the UI, with many more screenshots. If you’re a designer, check out the [Sugar UI design guide](http://wiki.laptop.org/go/OLPC_Human_Interface_Guidelines/Design_Fundamentals). There’s also a [video walkthrough](http://www.youtube.com/watch?v=DwzCsOFxT-U) of the Sugar UI available.


I have to admit that I didn’t find the Sugar UI particularly intuitive or discoverable, even after using it for 10 minutes and learning the basics. But I’m not a child. Maybe something unusual is necessary to get kids’ creative juices flowing. Mr. Negroponte has strong feelings on this topic:


> In fact, one of the saddest but most common conditions in elementary school computer labs (when they exist in the developing world), is the children are being trained to use Word, Excel and PowerPoint. I consider that criminal, because children should be making things, communicating, exploring, sharing, not running office automation tools.


He’s got a point. I don’t know many kids that want to grow up to be “Information Workers.”

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
