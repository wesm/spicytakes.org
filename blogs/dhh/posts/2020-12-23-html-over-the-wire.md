---
title: "HTML over the wire"
date: 2020-12-23
url: https://signalvnoise.com/svn3/html-over-the-wire/
slug: html-over-the-wire
word_count: 599
---


You can write fast, modern, responsive web applications by generating your HTML on the server, and delivering that (with a little help) directly to the browser. You don’t need JSON as an in-between format. You don’t need client-side MVC frameworks. You don’t need complicated bundling and transpiling pipelines. But you do need to think different.


Because the mainstream story in web development of the past decade or so has been one of JavaScript all the things! Let’s use it on the server! Let’s use it on the client! Let’s have it generate all the HTML dynamically! And, really, it’s pretty amazing that you really can do all that. JavaScript has come an incredibly long way since the dark ages of Internet Explorer’s stagnant monopoly.


But just because you can, doesn’t mean you should.


The price for pursuing JavaScript for everything has been a monstrosity of modern complexity. Yes, it’s far more powerful than it ever was. But it’s also far more convoluted and time-consuming than is anywhere close to reasonable for the vast majority of web applications.


Complexity isn’t really a big problem if you’re a huge company. If you have thousands of developers each responsible for tiny sliver of the application, you might well find appeal and productivity in complicated architectures and build processes. You can amortize that investment over your thousands of developers, and it’s not going to break your back.


But incidental complexity can absolutely break your back if you’re a small team where everyone has to do a lot. The tools and techniques forged in the belly of a huge company is often the exact opposite of what you need to make progress at your scale.


This is what HTML Over The Wire is all about. It’s a celebration of the simplicity in HTML as the format for carrying data and presentation together, whether this is delivered on the first load or with subsequent dynamic updates. A name for a technique that can radically change the assumptions many people have about how modern web applications have to be built today.


Yes, we need a bit of JavaScript to make that work well enough to compete with the fidelity offered by traditional single-page applications, but the bulk of that can be abstracted away by a few small libraries, and not leak into the application code we write.


Again, it’s not that JavaScript is bad. Or that you don’t need any to write a modern web application. JavaScript is good! Writing a bit to put on the finishing touches is perfectly reasonable. But it needn’t be at the center of everything you do on the web.


When we embrace HTML as the format to send across the wire, we liberate ourselves from having to write all the code that creates that HTML in JavaScript. You now get to write it in Ruby or Erlang or Clojure or Smalltalk or any programming language that might set your heart aflutter. We return the web to a place full of diversity in the implementations, and HTML as the lingua franca of describing those applications directly to the browser.


HTML over the wire is a technique for a simpler life that’ll hopefully appeal to both seasoned developers who are tired of dealing with the JavaScript tower of complexity and to those just joining our industry overwhelmed by what they have to learn. A throwback to a time where you could view source and make sense of it. But with all the affordances to create wonderfully fluid and appealing modern web applications.


Intrigued? Checkout [Hotwire](https://hotwire.dev) for a concrete implementation of these ideals.

