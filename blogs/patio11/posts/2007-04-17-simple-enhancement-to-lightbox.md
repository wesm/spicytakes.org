---
title: "Simple Enhancement To Lightbox"
date: 2007-04-17
url: https://www.kalzumeus.com/2007/04/17/simple-enhancement-to-lightbox/
slug: simple-enhancement-to-lightbox
word_count: 143
---


I [posted recently](http://microisvjournal.wordpress.com/2007/04/14/lightbox-quick-pretty-screenshot-previews/) about how to use [Lightbox](http://www.huddletogether.com/projects/lightbox/) to make your web site prettier and more useable, and someone pointed out to me that it would be even better if Lightbox would let you dismiss the image by hitting the escape key.  Doing that required working around some compatibility quirks in Firefox versus IE, so to save anyone else the trouble of doing it you can just [grab it from my site](http://www.bingocardcreator.com/lightbox.js).


For those interested in idiosyncracies of Javascript compatibility, here is what posed the issues:


a)  IE will let you test a keyCode against an integer, including a non-printing ASCII code such as 27 (the escape key).  Firefox requires you to test against a constant, something like event.DOM_VK_ESCAPE .


b)  IE captures non-printing keyboard keys (other than F1-F12, apparently) in the keypressed event, but Firefox only captures them in the keydown event.
