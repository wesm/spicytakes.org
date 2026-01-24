---
title: "Code Smaller"
date: 2007-02-13
url: https://blog.codinghorror.com/code-smaller/
slug: code-smaller
word_count: 506
---

Unless you’ve been living under a rock for the last few years, you’ve probably heard about the game [Katamari Damacy](http://en.wikipedia.org/wiki/Katamari_Damacy). The gameplay consists of little more than *rolling stuff up* into an ever-increasing ball of stuff. That’s literally all you do. You start by rolling up small things like matchsticks, thimbles, pushpins, and so on. As the ball gets larger, you roll up ever larger and larger items. Eventually, your Katamari ball gets so large you end up rolling together cities, mountains, clouds – eventually entire *planets*. It’s unbelievably fun, and completely mesmerizing.


After I played for a while, I realized that **Katamari Damacy is a game about *the scale of life***, reminiscent of the classic Eames powers of ten movie.


![](https://blog.codinghorror.com/content/images/2025/06/image-115.png)


As Bob Koss points out, code has a natural tendency to become a giant Katamari [ball of “stuff,”](https://web.archive.org/web/20070217045318/http://blog.objectmentor.com/articles/2006/12/21/size-matters) too:


> I travel a lot and I get to visit a lot of different companies. No matter which industry a company is in or which programming language a team is using, there is one commonality in all of the code that I see – classes are just too damn big and methods are just too damn long.
> We programmers must take matters into our own hands and become masters of our domains. Unless we take action, things are just going to get bigger and bigger until we have a real mess on our hands.


Bob’s article is about **managing the scale of your code**:


> This notion of breaking a class into smaller and smaller pieces is exactly opposite to what I learned when I first started studying OO. Way back when I worried about bad-hair days, people believed that a class should encapsulate everything that concerned it. A Customer class would know the business rules of being a Customer as well as how to retrieve itself from the database and display it’s data. That’s a fine idea, provided the database schema never changes, the display never changes, or the business rules never change. If any one of those responsibilities change, we are at a high risk of breaking other things that are coupled to it.


So many aspects of software development can be summarized as **small is beautiful**:

- The odds of failure for a software project are directly proportional to [the size of the project](https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/). Slicing a large project into several smaller subprojects is the single most direct way to increase your project’s chances of success.
- The relationship between lines of code and bugs is completely linear. Fewer code means fewer bugs.
- Smaller code avoids TL; DR (Too Long; Didn’t Read) syndrome. The less code there is to read, the higher the odds are that someone *will* actually read it.
- If you keep your [dependencies to a minimum](https://blog.codinghorror.com/dependency-avoidance/), your code will be simpler and easier to understand.


It’s up to us to resist the natural tendency of any project to snowball into a giant rolling Katamari ball of code. **Code smaller!**

[code quality](https://blog.codinghorror.com/tag/code-quality/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[scalability](https://blog.codinghorror.com/tag/scalability/)
[clean code](https://blog.codinghorror.com/tag/clean-code/)
[refactoring](https://blog.codinghorror.com/tag/refactoring/)
