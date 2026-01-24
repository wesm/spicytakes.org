---
title: "The Principle of Least Power"
date: 2007-07-17
url: https://blog.codinghorror.com/the-principle-of-least-power/
slug: the-principle-of-least-power
word_count: 299
---

Tim Berners-Lee on [the Principle of Least Power](http://www.w3.org/DesignIssues/Principles.html):


> Computer Science spent the last forty years making languages which were as powerful as possible. Nowadays we have to appreciate the reasons for **picking not the most powerful solution but the *least* powerful**. The less powerful the language, the more you can do with the data stored in that language. If you write it in a simple declarative from, anyone can write a program to analyze it. If, for example, a web page with weather data has RDF describing that data, a user can retrieve it as a table, perhaps average it, plot it, deduce things from it in combination with other information. At the other end of the scale is the weather information portrayed by the cunning Java applet. While this might allow a very cool user interface, it cannot be analyzed at all. The search engine finding the page will have no idea of what the data is or what it is about. The only way to find out what a Java applet means is to set it running in front of a person.


This was later codified in a more formal W3C document, [The Rule of Least Power](http://www.w3.org/2001/tag/doc/leastPower.html). I propose a corollary to this rule, which in the spirit of [recent](http://haacked.com/archive/2007/07/17/the-eponymous-laws-of-software-development.aspx) [memes](http://globalnerdy.com/2007/07/18/laws-of-software-development/), I’ll call **Atwood’s Law**: **any application that *can* be written in JavaScript, *will* eventually be written in JavaScript**.


![](https://blog.codinghorror.com/content/images/2025/05/atwoods-law-javascript.png)


If you liked that article, I recommend the rest of Berners-Lee’s [architectural and philosophical points](http://www.w3.org/DesignIssues/) page. Although the content is quite old in internet time – only two of the articles were written in the last year – it still contains some timeless nuggets of advice and insight from the guy who [invented the world wide web](http://en.wikipedia.org/wiki/Tim_Berners-Lee).

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
