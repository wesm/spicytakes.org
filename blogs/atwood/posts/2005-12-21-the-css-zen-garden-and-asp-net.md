---
title: "The CSS Zen Garden and ASP.NET"
date: 2005-12-21
url: https://blog.codinghorror.com/the-css-zen-garden-and-asp-net/
slug: the-css-zen-garden-and-asp-net
word_count: 387
---

The [CSS Zen Garden](http://www.csszengarden.com/) site isn’t exactly new news these days, but I’ve been digesting the excellent [CSS Zen Garden book](http://www.amazon.com/exec/obidos/ASIN/0321303474) over the last few months and we now have an opportunity to pursue a completely CSS-driven site layout on one of our projects.


Although everyone has used stylesheets before for trivial things like colors and font sizes, **switching to completely CSS-driven layout is a more daunting proposition**. Consider the actual Zen Garden HTML, before and after a stylesheet treatment:

kg-card-begin: html


| HTML | HTML with CSS Stylesheet |
|  |  |


kg-card-end: html

That’s one radical makeover.


The book does a fantastic job of breaking down a number of the CSS stylesheets and focusing on particular areas of interest within each one. I highly recommend it. It’s fun to click through these to get a visual sense of what’s possible, and what still works in IE6. Here are the examples presented in the book, in order by section:


**Layout**
[Backyard](http://www.csszengarden.com/029/), [Entomology](http://www.csszengarden.com/030/), [White Lily](http://www.csszengarden.com/036/), [Pret-a-porter](http://www.csszengarden.com/037/), [CS(S) Monk](http://www.csszengarden.com/070/), [Not So Minimal](http://www.csszengarden.com/024/)


**Imagery**
[Japanese Garden](http://www.csszengarden.com/096/), [Revolution!](http://www.csszengarden.com/102/), [Deco](http://www.csszengarden.com/094/), [No Frontiers!](http://www.csszengarden.com/097/), [Coastal Breeze](http://www.csszengarden.com/013/), [What Lies Beneath](http://www.csszengarden.com/019/)


**Typography**
[Oceans Apart](http://www.csszengarden.com/085/), [si6](http://www.csszengarden.com/044/), [Release One](http://www.csszengarden.com/035/), [Dead or Alive](http://www.csszengarden.com/009/), [Blood Lust](http://www.csszengarden.com/005/), [Golden Mean](http://www.csszengarden.com/017/)


**Special Effects**
[This is Cereal](http://www.csszengarden.com/057/), [Gemination](http://www.csszengarden.com/062/), [Bonsai Sky](http://www.csszengarden.com/069/), [Tulipe](http://www.csszengarden.com/088/), [door to my garden](http://www.csszengarden.com/041/), [Elastic Lawn](http://www.csszengarden.com/063/)


**Reconstruction**
[Hedges](http://www.csszengarden.com/031/), [Radio Zen](http://www.csszengarden.com/058/), [South of the Border](http://www.csszengarden.com/093/), [Corporate Zenworks](http://www.csszengarden.com/095/), [Open Window](http://www.csszengarden.com/090/), [mnemonic](http://www.csszengarden.com/025/)


It’s admirable how the Zen Garden puts **the holy grail of separating content from presentation squarely in view**.


But I’m a little uncertain how this will work in practice under ASP.NET 1.1 and 2.0. Ideally the user controls will emit a bunch of <div> tags and ultra-simple HTML, then we let the CSS file have its way with position, graphics, sizing, and even hiding elements. The one example I can find of [someone retrofitting pure CSS layout](http://support.rainbowportal.net/confluence/display/DOX/Introduction+to+Zen) on an existing ASP.NET 1.1 site is... rather scary. And there are pages and pages of [advice on CSS gotchas](https://web.archive.org/web/20051221035517/http://www.mezzoblue.com/css/cribsheet/), starting with the most important rule: **develop in Firefox first, then fix the inevitable CSS compatibility bugs in IE6 second.**


Although this approach has a lot to recommend it, I still worry that we’re trading one set of problems for another. Has anyone gone the full CSS Zen Garden route with an ASP.NET 1.1 or 2.0 site yet?

[css](https://blog.codinghorror.com/tag/css/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[css zen garden](https://blog.codinghorror.com/tag/css-zen-garden/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[stylesheet](https://blog.codinghorror.com/tag/stylesheet/)
