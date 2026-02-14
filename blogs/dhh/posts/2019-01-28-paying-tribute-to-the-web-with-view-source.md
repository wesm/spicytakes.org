---
title: "Paying tribute to the web with View Source"
date: 2019-01-28
url: https://signalvnoise.com/svn3/paying-tribute-to-the-web-with-view-source/
slug: paying-tribute-to-the-web-with-view-source
word_count: 889
---


The web isn’t just another software platform. It’s the greatest software platform the world has ever seen. And yet even in its obvious glory, we’re still learning how to be grateful for all its constituent parts. Take View Source, for example.


I owe much of my career to View Source. It’s what got me started with web development in the first place. Going to sites that I liked, learning how they did what they did. Yes, I also bought a bunch of animal books from O’Reilly, and I read WIRED’s Webmonkey, and the web was full of tutorials even then. But it’s not the same. Seeing how something real is built puts the individual pieces of the puzzle together in a way that sample code or abstract lessons just don’t.


I’m clearly not alone in this story. [Jason learned HTML the same way](https://twitter.com/jasonfried/status/1089945973483278337). [Lots](https://twitter.com/adambader/status/1089983309843640320) [of](https://twitter.com/obezuk/status/1089978781182226432) [people](https://twitter.com/kennethpbowen/status/1089991690688122883) on the internet owe their formative steps to the marvelous wonder that is View Source.


Unfortunately View Source has been receding in recent years. Building stuff for the web has [never been more complicated](https://css-tricks.com/the-great-divide/). And few of these new tools, frameworks, or techniques have seemed to prioritize making the web readable through View Source. That’s a real shame, because progress needn’t be the enemy of learning.


Take source maps. JavaScript has flourished in the same timeframe that View Source has been receding. In part because Babel, and other transpilers, as well as Webpack, and other bundlers, made it easier to build bigger things with features from The Future of JavaScript and entire dialects like TypeScript and CoffeeScript. But the output of these tools are usually difficult for humans to read, especially once they’ve been minified. That’s where those source maps come in.


A source map allow developers to see the code as it was written by the creator. Complete with comments, understandable variable names, and all the other help that makes it possible for programmers to understand code. And as a bonus, it’s only sent over the wire when the user has the dev tools open in their browser.


But source maps have long been seen merely as a local development tool. Not something you ship to production, although people have also been doing that, such that live debugging would be easier. That in itself is a great reason to ship source maps.


And so is wanting to pay tribute to the web. To the heritage that is View Source. To make it easier for people who want to tinker, learn, or audit the code that runs in our browsers. The interactive development tools available in modern browsers make this an amazing experience, if you can read the code.


It’s akin to the [Right To Repair](https://repair.org/stand-up/). Don’t glue your application together in such a way that it won’t come apart for people who’re inclined to inspect what’s under the hood.


Source maps alone aren’t enough, though. Sending humanely readable HTML and CSS is just as important. Modern web applications are a harmony of HTML, CSS, and JavaScript. To understand the app, you need to be able to understand all of its parts.


At [Basecamp](https://basecamp.com), we’ve long been on the this track with our HTML and CSS. We follow the BEM CSS naming convention, and if you introspect any of the markup and styling, [you really can understand what’s going on](https://xotv.me/channels/22-important/vod_videos/781-important-slash-slash-basecamp-dot-com).


But as [Tom Dale pointed out](https://twitter.com/dhh/status/1089284763230195717) when I [ranted about compiler barf in HTML](https://twitter.com/dhh/status/1089179428788133888) over the weekend, we hadn’t done our part when it comes to making our JavaScript readable via View Source. That was a mistake. And we’re rectifying it in part today!


![](https://signalvnoise.com/assets/svn3/images/2019/01/Screen-Shot-2019-01-28-at-1.25.53-PM.png?fit=640%2C553&ssl=1)

*Learn how we use Stimulus by reading the pure, unminified source code!*


All the JavaScript that runs Basecamp 3 under Webpack now has source maps available! We’re still looking into what it’ll take to get source maps for the parts that were written for the asset pipeline using Sprockets, but all our Stimulus controllers are compiled and bundled using Webpack, and now they’re easy to read and learn from.


Additional, [Rails 6 just committed to shipping source maps by default in production](https://github.com/rails/webpacker/issues/769#issuecomment-458216151), also thanks to Webpack. You’ll be able to turn that feature off, but I hope you won’t. The web is a better place when we allow others to learn from our work.


That’s a mission that’s near and dear to my heart at Basecamp. It’s why we open source so much of all the software we write. I’d say a good 90% of all the code that runs Basecamp is open source in form of Ruby on [Rails](https://rubyonrails.org), [Turbolinks](https://github.com/turbolinks/turbolinks), [Stimulus](https://stimulusjs.org), and the myriad of other packages we’ve released over the decades.


I like to think of Basecamp as a teaching hospital. The care of our users is our first priority, but it’s not the only one. We also take care of the staff running the place, and we try to teach and spread everything we learn. Pledging to protect View Source fits right in with that.


The web is just a marvel of a platform. So unique. So empowering. It’s easy to just fall into the trap of “what can the web do for me, for my business, for my customers”. Some times it’s worth taking a step back and ask yourself: What can I do for the web? One answer: Protect and promote View Source.

