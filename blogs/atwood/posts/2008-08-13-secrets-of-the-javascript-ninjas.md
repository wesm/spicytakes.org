---
title: "Secrets of the JavaScript Ninjas"
date: 2008-08-13
url: https://blog.codinghorror.com/secrets-of-the-javascript-ninjas/
slug: secrets-of-the-javascript-ninjas
word_count: 687
---

One of the early technology decisions we made on Stack Overflow was to go with a fairly [JavaScript intensive site](http://blog.stackoverflow.com/2008/06/is-it-ok-to-require-javascript/). Like many programmers, I’ve been historically ambivalent about JavaScript:

- [The Power of “View Source”](https://blog.codinghorror.com/the-power-of-view-source/)
- [The Day Performance Didn’t Matter Any More](https://blog.codinghorror.com/the-day-performance-didnt-matter-any-more/)
- [JavaScript and HTML: Forgiveness by Default](https://blog.codinghorror.com/javascript-and-html-forgiveness-by-default/)
- [JavaScript: The Lingua Franca of the Web](https://blog.codinghorror.com/javascript-the-lingua-franca-of-the-web/)
- [The Great Browser JavaScript Showdown](https://blog.codinghorror.com/the-great-browser-javascript-showdown/)


However, it’s difficult to argue with the demonstrated success of JavaScript over the last few years. JavaScript code has gone from being a peculiar website oddity to – dare I say it – delivering useful core features on websites I visit on a daily basis. Paul Graham had [this to say](http://www.paulgraham.com/web20.html) on the definition of Web 2.0 in 2005:


> One ingredient of its meaning is certainly Ajax, which I can still only just bear to use without scare quotes. Basically, what “Ajax” means is “Javascript now works.” And that in turn means that web-based applications can now be made to work much more like desktop ones.


Three years on, I can’t argue the point: **JavaScript now works**. Just look around you on the web.


Well, to a point. We can no longer luxuriate in the – and to be clear, I mean this ironically – [golden age of Internet Explorer 6](https://blog.codinghorror.com/did-ie6-make-web-20-possible/). We live in a brave new era of [increasing browser competition](https://blog.codinghorror.com/what-if-they-gave-a-browser-war-and-microsoft-never-came/), and that’s a good thing. Yes, JavaScript is now mature enough and ubiquitous enough and fast enough to be a viable client programming runtime. But this vibrant browser competition also means there are **hundreds of aggravating differences in JavaScript implementations** between Opera, Safari, Internet Explorer, and Firefox. And that’s just the big four. It is *excruciatingly* painful to write and test your complex JavaScript code across (n) browsers and (n) operating systems. It’ll make you pine for the good old days of HTML 4.0 and CGI.


But now something else is happening, something arguably even more significant than “JavaScript now works.” The rise of commonly available JavaScript frameworks means you can **write to higher level JavaScript APIs that are guaranteed to work across multiple browsers**. These frameworks spackle over the JavaScript implementation differences between browsers, and they’ve (mostly) done all the ugly grunt work of testing their APIs and validating them against a host of popular browsers and platforms.


[The JavaScript Ninjas](https://www.manning.com/books/secrets-of-the-javascript-ninja) have delivered their secret and ultimate weapon: common APIs. They transform working with JavaScript from an unpleasant, write-once-debug-everywhere chore into something that’s actually – dare I say it – *fun*.


![](https://blog.codinghorror.com/content/images/2025/04/image-190.png)


Frankly, it is foolish to even *consider* rolling your own JavaScript code to do even the most trivial of things in a browser now. Instead, **choose one of these mature, widely tested JavaScript API frameworks. Spend a little time learning it.** You’ll ultimately write less code that does more – and (almost) never have to worry a lick about browser compatibility. It’s basically browser coding nirvana, [as Rick Strahl noted](http://www.west-wind.com/WebLog/posts/370180.aspx):


> I’ve kind of fallen into a couple of very client heavy projects and jQuery is turning out to be a key part in these particular projects. jQuery is definitely one of those tools that has got me really excited as it has changed my perspective in Web Development considerably from dreading doing client development to actually looking forward to applying richer and more interactive client principles.


There are several popular Javascript API frameworks to choose from:

1. [Prototype](http://www.prototypejs.org/) and [Script.aculo.us](http://en.wikipedia.org/wiki/Script.aculo.us)
2. [JQuery](http://en.wikipedia.org/wiki/JQuery)
3. [Yahoo UI Library](http://en.wikipedia.org/wiki/Yahoo!_UI_Library)
4. [ExtJS](http://extjs.com/)
5. [Dojo](http://dojotoolkit.org/)
6. [MooTools](http://mootools.net/)


I don’t profess to be an expert in any of these. Far from it. But I will echo what Rick said: using JQuery while writing Stack Overflow is probably the only time in my entire career as a programmer that I have *enjoyed* writing JavaScript code.


It’s sure pleasant to write code against **solid, increasingly standardized JavaScript API libraries** that spackle over all those infuriating browser differences. I, for one, would like to thank [John Resig](http://ejohn.org/) and all the other JavaScript Ninjas who share their secrets – and their frameworks – with the rest of the community.

[javascript](https://blog.codinghorror.com/tag/javascript/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
