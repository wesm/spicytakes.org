---
title: "Day 33: How to make music with ClojureScript"
date: 2013-11-25
url: https://jvns.ca/blog/2013/11/25/day-33-how-to-make-music-with-clojurescript/
slug: day-33-how-to-make-music-with-clojurescript
word_count: 252
---


I am working on a small project to practice
[change ringing](https://en.wikipedia.org/wiki/Change_ringing) with
ClojureScript.


As always when starting a new project I have been consulting
approximately a million resources to get started. So I thought I’d
collect them all together in one place instead of searching for them
over and over forever.


### Getting started with ClojureScript

- [Empty ClojureScript project, with instructions](https://github.com/maryrosecook/barecljs),
from [Mary](https://github.com/maryrosecook)
- [CLJSFiddle](http://cljsfiddle.net/), for trying out ClojureScript
snippets
- [Explanation of cljs/js interop](http://gist.io/7610122), from
[Zach](https://github.com/zachallaun)


### Web Audio


There’s a newish API for synthesizing sound in the browser called the
WebAudio API.

- [Some demos](http://webaudiodemos.appspot.com/)
- [Very cool player piano app](https://github.com/liamgriffiths/music-box)
by Liam Griffiths, a Hacker Schooler in my batch. You will have to
run it on your computer but it will be worth it.
- [Hum](https://github.com/mathias/hum), a small ClojureScript wrapper
around the WebAudio API. If you want to test if it works in your
browser, try
[this CLJSFiddle](http://cljsfiddle.net/fiddle/jvns.cljs-music-test).
It should make an annoying noise when you run it..


### Sound samples


If you don’t want to synthesize music, there are tons of samples on
[freesound.org](http://www.freesound.org/)

- [Freesound API documentation](http://www.freesound.org/docs/api/)
- [Get a Freesound API key](http://www.freesound.org/api/apply/). It says
“Apply”, but it gives it to you automatically.
- [freesound.js](https://github.com/g-roma/freesound.js), a JS library
for working with freesound
- [IDs for a set of piano samples](https://github.com/overtone/overtone/blob/master/src/overtone/samples/piano.clj),
from the Overtone project.
- [JSFiddle demoing the Freesound API](http://jsfiddle.net/jvns/J4sW2/).
Scroll to the bottom to see the actual code; I copied all of `freesound.js`
into it. It should make a piano sound when you run it.
