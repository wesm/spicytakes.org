---
title: "Goodbye Wordpress"
date: 2020-06-22
url: https://zedshaw.com/blog/2020-06-22-goodbye-wordpress/
slug: goodbye-wordpress
word_count: 936
---



# Goodbye Wordpress


Today I spent the day finally getting all of my content off wordpress and getting it back on my own software. I use a project called [wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown#readme) to take the XMl file that Wordpress spits out and convert it into Markdown. This project is really great, and even downloaded all the images for me. There's a few of these, but this one did a nice job of creating the markdown in the flavor that I already use.


Now I feel like I can finally get back to writing regularly and also work on some fun new blogging software. I've been cooking up a lot of little components in [Svelte](https://svelte.dev) for doing WebTorrent videos, and I'd like to experiment with that more here.


## About The Dump


I grabbed the better essays off wordpress, and some things for nostalgia, but most likely I'll have to go through and annotate some things. I also will probably try to create a commenting system for this since that seems to be the next thing you do when you write a blog. We'll see. Otherwise, if you read something I wrote, check with me to see if I still feel that way and I'll update the post.


## Why Did You Use Wordpress Anyway?


I setup wordpress around 2014 since I was too busy studying painting to maintain blog software. Thinking back this was a terrible idea because my programming skills didn't have anywhere to exercise, and a blog is an excellent way to stay sharp. I could have just worked on rewriting the blog in the latest technology and stayed ahead of a lot of technology curves, but I was too busy. Wordpress seemed like an easy way to do it.


As the years went on I started to realize that Wordpress is terrible if you want to post anything but text. They don't handle media well, have problems even organizing anything, and the UI is just really confusing. But, you get sucked into doing something that's barely capable and there's not much of a reason to change even if it could be better.


## What Changed?


Two significant projects came in my tunnel vision that have radically changed how I'm approaching web applications, and my writing. The first is the [Svelte](https://svelte.dev) project which is easily the best User Interface system I've ever used. I *really* want everyone to adopt the "assignment is reactive" model in the near future and feel that Rich is a genius. It's so simple I'm constantly asking, "Why didn't I think of that." With Svelte I had a prototype of my dream artist website at [zedshaw.art](https://zedshaw.art/) working in about a week, and even managed to get a first pass at a WebTorrent video serving system.


Then I had to go on this long trip around the world (more on that in another post) and couldn't continue that work. Svelte though really made me want to get back into programming web applications, and I suspect also my 6+ years studying painting have made my visual abilities stronger so I'm able to handle the UI much better than before. I didn't really have too much of a problem in the past, but lately there's been major advances in CSS and Reactive JavaScript, plus ES6 improvements, that have made JavaScript a fantastic system for developing what I want.


After my trip it took me almost two months of study and recovery before I started rewriting everything in JavaScript, and also re-learing how to develop websites using modern technologies. This blog is based off Svelte, [Sapper](https://sapper.svelte.dev), and the [Spectre.css](https://picturepan2.github.io/spectre/) SaSS framework since it's simple enough to comprehend. I'm finding these technologies to be very easy to use, simple, and malleable for base web development purposes.


## Then Zettlr


I really despise writing in the browser. Just the fact that the backspace key can cause all of my work to disappear gives me hives. I typically do all of my writing with Vim, but for just pure writing or crafting notes and organizational content it's not ideal. Then I ran into the fantastic [Zettlr](https://www.zettlr.com/) which hits all of my pain points with writing. It's got a few flaws in how it handles symlinks (clue: just don't do anything with symlinks) but other than that it's a great writing tool, and also allows me to collect all those notes and references I need for my essays.


It's really the note organization and searching system that makes Zettlr great for the writing I want to do. I'll have an idea for an essay and can just start a note with links and thoughts, and make links between them to follow. Then when I go to write the actual essay or part of my book, I can quickly look up the things I need and write very quickly. It also supports Markdown well, with a kind of "almost-WYSIWYG" style that works well. Finally, it has a good "focus mode" so I can just write and not see anything else while I'm writing.


I use [Hammerspoon](https://www.hammerspoon.org/) to setup up a few hotkeys for starting Zettlr and getting into writing. I really don't use Hammerspoon to its full potential, but it does most of what I need so far. Each morning I need to write I just fire up Zettlr real fast and go into write mode and write. Then I have my little blog generator that takes all my writings and crafts this Svelte/Sapper app you're looking at now.


It's lots of fun. And, I won't get charged for "domain redirect" from wordpress anymore.



---


###### More from Zed A. Shaw
