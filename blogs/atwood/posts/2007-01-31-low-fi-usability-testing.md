---
title: "Low-Fi Usability Testing"
date: 2007-01-31
url: https://blog.codinghorror.com/low-fi-usability-testing/
slug: low-fi-usability-testing
word_count: 1233
---

Pop quiz, hotshot. **How do you know if your application *works?*** Sure, maybe your app compiles. Maybe it passes all the unit tests. Maybe it ran the QA gauntlet successfully. Maybe it was successfully deployed to the production server, or packaged into an installer. Maybe your beta testers even signed off on it.


But that doesn’t mean it works.


Can users actually *understand* your application? Can they *get their work done* in your application? That’s what defines a working application. All the other stuff I listed is just noise. **You don’t know if your application truly works until you’ve performed usability tests on it with actual users.**


And you regularly do usability testing on your application, right?


That’s what I thought. One of the central concepts in Steve Krug’s book [Don’t Make Me Think](http://www.amazon.com/exec/obidos/ASIN/0321344758) is that usability testing is essential to any software project. Krug calls his simplified approach to usability testing *lost our lease, going-out-of-business-sale usability testing*:


> Usability testing has been around for a long time, and the basic idea is pretty simple: If you want to know whether your software or your Web site or your VCR remote control is easy enough to use, watch some people while they try to use it and note where they run into trouble. Then fix it, and test it again.
> In the beginning, though, usability testing was a very expensive proposition. You had to have a usability lab with an observation room behind a one-way mirror, and at least two video cameras so you could record the users’ reactions and the thing they were using. You had to recruit a lot of people so you could get results that were statistically significant. It was Science. It cost $20,000 to $50,000 a shot. It didn’t happen very often.
> But in 1989 Jakob Nielsen wrote a paper titled “[Usability Engineering at a Discount](http://www.useit.com/papers/guerrilla_hci.html)” and pointed out that it didn’t have to be that way. You didn’t need a usability lab, and you could achieve the same results with a lot fewer users. The idea of discount usability testing was a huge step forward. The only problem is that a decade later most people still perceive testing as a big deal, hiring someone to conduct a test still costs $5,000 to $15,000, and as a result it doesn’t happen nearly often enough.
> What I’m going to commend to you in this chapter is something even more drastic: Lost our lease, going-out-of-business-sale usability testing. I’m going to try to explain how to do your own testing when you have no money and no time. If you can afford to hire a professional to do your testing, by all means do it – but *don’t* do it if it means you’ll do less testing.


Krug points out that **usability testing is only as difficult as you make it**. It’s possible to get useful results from a usability test with a *single user*, even:


> [Usability] testing always works, and even the worst test with the wrong user will show you things you can do to improve your site. I make a point of always doing a live user test at my workshops so that people can see it’s very easy to do and it always produces an abundance of valuable insights. I ask for a volunteer and have him try to perform a task on a site belonging to one of the other attendees. These tests last less than ten minutes, but the person whose site is being tested usually scribbles several pages of notes. And they always ask if they can have the recording of the test to show their team back home. Once person told me that after his team saw the recording, they made one change to their site which they later calculated had resulted in $100,000 in savings.


For more proof that you don’t need a lot of users to have an effective usability test, Jakob Neilsen offers [the following graph](http://www.useit.com/alertbox/20000319.html):


![usability-problems-found-graph](https://blog.codinghorror.com/content/images/uploads/2007/01/6a0120a85dcdae970b0120a86d8273970b-pi.png)


Obviously, not doing any usability testing at all is a disaster. But what’s not so obvious is that usability testing with just a few users is remarkably effective. And it can be relatively painless if you follow Krug’s broad guidelines for low-fidelity usability testing:

- **When should I test?** Ideally, once per month. You should be running small usability tests continuously throughout the development process. The tests should be short and simple, so you can conduct them almost any time with little advance planning.
- **How many users do I need?** Three or four max.
- **What kind of users?** Grab some people. Anyone who can use a computer will do. The best-kept secret of usability testing is that *it doesn’t much matter who you test*. It’s a good idea to get representative users, but it’s much more important to test early and often. Don’t be embarrassed to ask friends and neighbors.
- **How much time will it take?** 45 minutes to an hour per user. Keep it simple. Keep it small. Although it does take extra time to conduct usability tests, even simple ones, ultimately you will save time. The results of the usability tests will prevent you from wasting time arguing endlessly, or redoing things at the end of a project.
- **Where do I conduct the test?** Any office or conference room. All you need is a room with a desk, a computer, and two chairs where you won’t be interrupted.
- **Who should do the testing?** Any reasonably patient human being. Choose someone who tends to be patient, calm, emphathetic, and a good listener. With a little practice, most people can get quite good at it.
- **What equipment do I need?** All you need is some form of [screen recording software](https://blog.codinghorror.com/screencasting-for-windows/), such as [Camtasia](http://www.techsmith.com/products/studio/default.asp). If you want to get really fancy you can bring in a camcorder to record the person and the screen.
- **How do I prepare for the tests?** Decide what you want to show. Have [a short script](https://web.archive.org/web/20070410083029/http://www.sensible.com/Downloads/script.doc) (doc) ready to guide the participants through the test.
- **How much will it cost?** Minus the moderator’s time, a $50-$100 stipend per user.
- **How do we interpret the results?** Debrief the development team and any interested stakeholders over lunch the same day. One of the nicest things about usability testing is that the results tend to be obvious to everyone who’s watching. The serious problems are hard to miss.


If you don’t already own a copy of Don’t Make Me Think, shame on you. In the meantime, I highly recommend downloading [Chapter 9 of Steve Krug’s Don’t Make Me Think](http://sensible.com/Downloads/DMMTchapter09_for_personal_use_only.pdf) (pdf), which has much more detail than the summary I’ve presented.


Usability testing doesn’t have to be complicated. If you really want to know if what you’re building works, **ask someone to use it while you watch**. If nothing else, grab Joe from accounting, Sue from marketing, *grab anyone nearby who isn’t directly involved with the project*, and have them try it. Don’t tell them what to do. Give them a task, and remind them to think out loud while they do it. Then quietly sit back and *watch what happens*. I can tell you from personal experience that the results are often eye-opening.


The benefits of usability testing are clear. You just have to *do it* to realize any of those benefits.

[usability testing](https://blog.codinghorror.com/tag/usability-testing/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
