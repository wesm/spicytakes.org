---
title: "Unit Testing vs. Beta Testing"
date: 2005-10-17
url: https://blog.codinghorror.com/unit-testing-vs-beta-testing/
slug: unit-testing-vs-beta-testing
word_count: 537
---

Why does Wil Shipley, the [author of Delicious Library](https://blog.codinghorror.com/how-to-be-successful-happy-fulfilled-and-drive-a-totally-hot-car/), hate unit testing so much?


> *I’ve certainly known companies that do “unit testing” and other crap they’ve read in books. Now, you can argue this point if you’d like, because I don’t have hard data; all I have is my general intuition built up over my paltry 21 years of being a professional programmer.
> [. . .] You should test. Test and test and test. But I’ve NEVER, EVER seen a structured test program that (a) didn’t take like 100 man-hours of setup time, (b) didn’t suck down a ton of engineering resources, and (c) actually found any particularly relevant bugs. **Unit testing is a great way to pay a bunch of engineers to be bored out of their minds and find not much of anything.** [I know – one of my first jobs was writing unit test code for Lighthouse Design, for the now-president of Sun Microsystems.] You’d be MUCH, MUCH better offer hiring beta testers (or, better yet, offering bug bounties to the general public).
> Let me be blunt: YOU NEED TO TEST YOUR DAMN PROGRAM. Run it. Use it. Try odd things. Whack keys. Add too many items. Paste in a 2MB text file. FIND OUT HOW IT FAILS. I’M YELLING BECAUSE THIS IS IMPORTANT.
> Most programmers don’t know how to test their own stuff, and so when they approach testing they approach it using their programming minds: “Oh, if I just write a program to do the testing for me, it’ll save me tons of time and effort.”*


It’s hard to completely disregard the opinion of a veteran developer shipping an application that gets excellent reviews. Although his opinion may seem heretical to the Test Driven Development cognoscenti, I think he has some valid points:

- **Some bugs don’t matter.** Extreme unit testing may reveal... extremely rare bugs. If a bug exists but no user ever encounters it, do you care? If a bug exists but only one in ten thousand users ever encounters it, do you care? Even Joel Spolsky [seems to agree](http://www.joelonsoftware.com/articles/SetYourPriorities.html) on this point. Shouldn’t we be fixing bugs based on data gathered from actual usage rather than a stack of obscure, failed unit tests?
- **Real testers hate your code.** A unit test simply verifies that something works. This makes it far, far too easy on the code. Real testers hate your code and will do whatever it takes to break it – feed it garbage, send absurdly large inputs, enter unicode values, double-click every button in your app, etcetera.
- **Users are crazy.** Automated test suites are a poor substitute for real world beta testing by actual beta testers. Users are erratic. Users have favorite code paths. Users have weird software installed on their PCs. Users are crazy, period. Machines are far too rational to test like users.


While I think basic unit testing can *complement* formal beta testing, I tend to agree with Wil: **the real and best testing occurs when you ship your software to beta testers.** If unit test coding is cutting into your beta testing schedule, you’re making a very serious mistake.

[unit testing](https://blog.codinghorror.com/tag/unit-testing/)
[beta testing](https://blog.codinghorror.com/tag/beta-testing/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
