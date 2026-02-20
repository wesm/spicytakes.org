---
title: "Introducing Widget Bakery"
date: 2008-06-28
url: https://www.kalzumeus.com/2008/06/28/introducing-widget-bakery/
slug: introducing-widget-bakery
word_count: 581
---


After 8 very productive hours with my designer today, I have a bit to show.  We worked at his house and, in between random banter with his wife and eating some very nice Japanese-style pizza, he banged away at the design of the page and default widget behavior and I got to work on some heavy duty Rails/Javascript magic.  Sadly he is much better at design than I am at web programming, so I did not progress quite as far, but things are looking up.


So the project name, which I haven’t mentioned to anybody yet, is [Widget Bakery](http://www.widgetbakery.com).  I’d encourage you to go open that up in another window — there is a full design for the front page posted, less much of the content.  As should be obvious, everything is heavily in development so don’t expect you’ll see any of the verbiage or design work stay there permanently, but I thought I would get the ball rolling so that people didn’t think I had completely abandoned the Sprint.


On the functionality front, I’m afraid that because Widget Bakery’s fundamental behavior involves being responsible for content on 3rd party websites, I really can’t show you anything useful this early in development.  Database schema and whatnot are still in a state of flux and anything which I post, and which you might subsequently post to your blog, could suddenly break.


Plus I would really, really hate if one of my widgets actually became popular before I had, oh, put indexes on the table ids or turned on caching… almost melted my poor laptop today during testing.  Word to the wise, kiddies: despite it being so obviously necessary you’d expect them to do it for you, Rails will not automatically slap database indexes on your id columns, and then you get to do full table scans every time you pull in linked objects.  *Gotcha!*


So in lieu of live functionality I give you this screenshot of a widget which does actually function:


As you can see I sort of have my work cut out for me on the CSS front, to get that footer text working properly.  You can’t see all the “fun” I had playing with iFrames, Javascript, and the DOM model to be able to inject that sucker into (just about) any page on the Internet *and* have that plus button bring up a Lightbox in the middle of their page to give instructions on how to embed the widget.  There still needs to be quite a bit more tuning done there — if you don’t hit the “close” button for the Lightbox at the moment there is no way to cancel out of it, which is quite unfriendly to the user.  (I’d like to get back the old “click anywhere to dismiss” Lightbox functionality, which is going to require further DOM spelunking.)


The RSS parsing, though, is done.  It needs to have error handling and some caching added, but after that I’ll have one widget ready of the baker’s dozen I hope to launch with.  Unfortunately, at the moment actually making that widget requires access to the server console and typing things like


@widget.version.latest.options[:rss_url] = “http://www.example.com/rss”


I’m going to have to get that functioning in a nice, easy to use GUI.  And then repeat or reuse that GUI for each type of widget, while making their internal differences fairly transparent to the user.  Lots of work to do, no time to do it — time to shake and bake!
