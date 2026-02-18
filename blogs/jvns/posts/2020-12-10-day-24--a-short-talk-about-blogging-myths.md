---
title: "Day 24: a short talk about blogging myths, and a debugging tip"
date: 2020-12-10
url: https://jvns.ca/blog/2020/12/10/day-24--a-short-talk-about-blogging-myths/
slug: day-24--a-short-talk-about-blogging-myths
word_count: 277
---


Today at RC I gave a 10-minute talk about blogging myths. I might turn it into a blog
post later, but for now I’ll just post the slides.


### “blogging myths” slides


The myths are:

1. you need to be original
2. you need to be an expert
3. posts need to be 100% correct
4. good bloggers don’t write bad posts
5. you need to explain every concept
6. page views matter


Here’s a [link to the slides on speakerdeck](https://speakerdeck.com/jvns/blogging-myths-d66598f5-e061-4799-b745-ae8e23e297b5),
though the aspect ratio there is broken for some reason as I’m writing this.


### debug by adding print statements to a library’s code


I was debugging with someone today and I was reminded of one of my favourite debugging techniques!


Sometimes when I’m debugging, I’m using a library, and I’m getting an error,
and I have NO IDEA why and all the Googling in the world just does not tell me anything useful.


When this happens, I like to:

1. grep the library’s code for the function/class I’m trying to use (or the error I’m getting)
2. add extra print statements to the library to give me more information
3. figure out the bug
4. remove the print statements


This works really well with Ruby / Node / Python / Go – anywhere where it’s
normal to have a directory like `node_modules` with all the code for all your
dependencies where you can easily edit & rerun the code.


Occasionally doing this helps me find a bug in the library, but 90% of the time
the problem is with my code and it just helps me understand how the library is
actually supposed to work.
