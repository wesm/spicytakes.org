---
title: "Glitch: write fun small web projects instantly"
date: 2017-11-13
url: https://jvns.ca/blog/2017/11/13/glitch--write-small-web-projects-easily/
slug: glitch--write-small-web-projects-easily
word_count: 557
---


I just wrote about Jupyter Notebooks which are a fun interactive way to write Python code. That
reminded me I learned about Glitch recently, which I also love!! I built a small app to [turn of twitter retweets](https://turn-off-retweets.glitch.me/) with it. So!


[Glitch](https://glitch.com/) is an easy way to make Javascript webapps. (javascript backend,
javascript frontend)


The fun thing about glitch is:

1. you start typing Javascript code into their web interface
2. as soon as you type something, it automagically reloads the backend of your website with the new
code. You don’t even have to save!! It autosaves.


So it’s like Heroku, but even more magical!! Coding like this (you type, and the code runs on
the public internet immediately) just feels really **fun** to me.


It’s kind of like sshing into a server and editing PHP/HTML code on your server and having it
instantly available, which I kind of also loved. Now we have “better deployment practices” than
“just edit the code and it is instantly on the internet” but we are not talking about Serious
Development Practices, we are talking about writing tiny programs for fun.


### glitch has awesome example apps


Glitch seems like fun nice way to learn programming!


For example, there’s a space invaders game (code by [Mary Rose Cook](https://maryrosecook.com/)) at [https://space-invaders.glitch.me/](https://space-invaders.glitch.me/). The thing I love about this is that in just a few clicks I can

1. click “remix this”
2. start editing the code to make the boxes orange instead of black
3. have my own space invaders game!! Mine is at [http://julias-space-invaders.glitch.me/](http://julias-space-invaders.glitch.me/). (i just
made very tiny edits to make it orange, nothing fancy)


They have tons of example apps that you can start from – for instance
[bots](https://glitch.com/handy-bots), [games](https://glitch.com/games), and more.


### awesome actually useful app: tweetstorms


The way I learned about Glitch was from this app which shows you tweetstorms from a given user: [https://tweetstorms.glitch.me/](https://tweetstorms.glitch.me/).


For example, you can see [@sarahmei](https://twitter.com/sarahmei)’s tweetstorms at [https://tweetstorms.glitch.me/sarahmei](https://tweetstorms.glitch.me/sarahmei) (she
tweets a lot of good tweetstorms!).


### my glitch app: turn off retweets


When I learned about Glitch I wanted to turn off retweets for everyone I follow on Twitter (I know
you can do it in Tweetdeck!) and doing it manually was a pain – I had to do it one person at a
time. So I wrote a tiny Glitch app to do it for me!


I liked that I didn’t have to set up a local development environment, I could just start typing and
go!


Glitch only supports Javascript and I don’t really know Javascript that well (I think I’ve never
written a Node program before), so the code isn’t awesome. But I had a really good time writing it
– being able to type and just see my code running instantly was delightful. Here it is:
[https://turn-off-retweets.glitch.me/](https://turn-off-retweets.glitch.me/).


### that’s all!


Using Glitch feels really fun and democratic. Usually if I want to fork someone’s web project and
make changes I wouldn’t do it – I’d have to fork it, figure out hosting, set up a local dev
environment or Heroku or whatever, install the dependencies, etc. I think tasks like installing
node.js dependencies used to be interesting, like “cool i am learning something new” and now I just
find them tedious.


So I love being able to just click “remix this!” and have my version on the internet instantly.
