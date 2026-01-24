---
title: "What’s Wrong With CSS"
date: 2010-04-30
url: https://blog.codinghorror.com/whats-wrong-with-css/
slug: whats-wrong-with-css
word_count: 629
---

We’re currently in the midst of a [CSS Zen Garden type exercise](https://blog.codinghorror.com/the-css-zen-garden-and-aspnet/) on our family of Q&A websites, which I affectionately refer to as “[the Trilogy](http://blog.stackoverflow.com/2009/05/the-stack-overflow-trilogy/)”:

- [Server Fault](http://serverfault.com/)
- [Super User](http://superuser.com/)
- [Stack Overflow](http://stackoverflow.com/)
- [Meta Stack Overflow](http://meta.stackoverflow.com/)


(In case you were wondering, yes, meta *is* the [Star Wars Holiday Special](http://en.wikipedia.org/wiki/The_Star_Wars_Holiday_Special).)


These sites all run the same core engine, but the logo, domain, and CSS “skin” that lies over the HTML skeleton is different in each case:

kg-card-begin: html


|  |  |
|  |  |


kg-card-end: html

They are not *terribly* different looking, it’s true, but we also want them to be recognizable as a family of sites.


We’re working with two amazing designers, Jin Yang and Nathan Bowers, who are helping us whip the CSS and HTML into shape so they can produce a set of about 10 different Zen Garden designs. As new sites in our network [get democracied into being](https://web.archive.org/web/20100425013924/http://blog.stackexchange.com/post/518474918/stack-exchange-2-0), these designs will be used as a palette for the community to choose from. (And, later, the community will decide on a domain name and logo as well.)


Anyway, I bring this up not because [*my pokemans, let me show you them*](http://www.google.com/images?q=my+pokemans+let+me+show+you), but because I have to personally maintain four different CSS files. And that number is only going to get larger. *Much* larger. That scares me a little.


Most of all, what I’ve learned from this exercise in site theming is that **CSS is kind of painful**. I fully support CSS as a (mostly) functional [user interface Model-View-Controller](https://blog.codinghorror.com/understanding-model-view-controller/). But even if you have extreme HTML hygiene and Austrian levels of discipline, CSS has some [serious limitations](http://en.wikipedia.org/wiki/Cascading_Style_Sheets#Limitations) in practice.


Things in particular that bite us a lot:

- Vertical alignment is a giant, hacky PITA. (Tables work great for this though!)
- Lack of variables so we have to repeat colors all over the place.
- Lack of nesting so we have to repeat huge blocks of CSS all over the place.


In short, CSS violates the living crap out of [the DRY principle](https://blog.codinghorror.com/curlys-law-do-one-thing/). You are c*onstantly* and *unavoidably* repeating yourself.


That’s why I’m so intrigued by two Ruby gems that attempt to directly address the deficiencies of CSS.


1. [**Less CSS**](http://lesscss.org/)

kg-card-begin: html


| /* CSS */
#header {
-moz-border-radius: 5;
-webkit-border-radius: 5;
border-radius: 5;
}
#footer {
-moz-border-radius: 10;
-webkit-border-radius: 10;
border-radius: 10;
} | // LessCSS
.rounded_corners (@radius: 5px) {
-moz-border-radius: @radius;
-webkit-border-radius: @radius;
border-radius: @radius;
}
#header {
.rounded_corners;
}
#footer {
.rounded_corners(10px);
} |


kg-card-end: html

2. [**SASS**](http://sass-lang.com/)

kg-card-begin: html


| /* CSS */
.content_navigation {
border-color: #3bbfce;
color: #2aaebd;
}
.border {
padding: 8px;
margin: 8px;
border-color: #3bbfce;
} | // Sass
!blue = #3bbfce
!margin = 16px
.content_navigation
border-color = !blue
color = !blue - #111
.border
padding = !margin / 2
margin = !margin / 2
border-color = !blue |


kg-card-end: html

As you can see, in both cases we’re **transmogrifying CSS into a bit more of a programming language**, rather than the static set of layout rules it currently exists as. Behind the scenes, we’re generating plain vanilla CSS using these little dynamic languages. This could be done at project build time, or even dynamically on every page load if you have a good caching strategy.


I’m not sure how many of these improvements [CSS3](http://www.w3.org/Style/CSS/current-work) will bring, never mind when the bulk of browsers in the world will support it. But I definitely feel that the core changes identified in both Less CSS and SASS address very real pain points in practical CSS use. It’s worth checking them out to understand why they exist, what they bring to the table, and how you could possibly adopt some of these strategies in your own CSS and your favorite programming language.

[css](https://blog.codinghorror.com/tag/css/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[design](https://blog.codinghorror.com/tag/design/)
[html](https://blog.codinghorror.com/tag/html/)
