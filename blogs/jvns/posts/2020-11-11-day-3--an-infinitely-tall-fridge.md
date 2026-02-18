---
title: "Day 3: an infinitely tall fridge"
date: 2020-11-11
url: https://jvns.ca/blog/2020/11/11/day-3--an-infinitely-tall-fridge/
slug: day-3--an-infinitely-tall-fridge
word_count: 244
---


Hello! Here are some notes from Day 3 at the Recurse Center.


This post is an extremely short one from the toy refrigerator poetry
forum website I’m working on. I needed to come up with a design for it, and
finally today I came up with an idea: just put everything on an image of a
fridge.


I found a stock image of a fridge, but I ran into a problem immediately, which
was that the entire website could not fit on said fridge image.


So I figured how to make a fridge that was as tall as I wanted it to be. (not
technically “infinite”, but “a fridge that is as big as required” didn’t have
quite the same ring).


### here’s the infinite fridge


Here’s a CodePen with the HTML/CSS required to make an infinite fridge. It’s relatively simple and I’m
very pleased about this. It basically has 3 images: one for the top of the
fridge, a 1px line that can be repeated as much as required, and then the
bottom.


See the Pen [
  infinite refrigerator](https://codepen.io/wizardzines/pen/bGeOdvJ) by Julia Evans ([Julia Evans](https://codepen.io/wizardzines))
  on [CodePen](https://codepen.io).


### that’s all!


I started writing an explanation of how exactly this infinite fridge works, but I ran out of time so maybe another day :). (the main trick is that `padding-bottom` is a percentage of the parent element’s width, not its height, so you can use it to create a box with a fixed aspect ratio)
