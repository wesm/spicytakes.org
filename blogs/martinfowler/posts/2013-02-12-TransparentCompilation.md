---
title: "Transparent Compilation"
description: "Increasingly web developers are using languages likeCoffeeScriptandSCSSthat compile to other textual source   languages that execute in the browser. Such source-to-source   compilers (also called tran"
date: 2013-02-12T00:00:00
tags: ["language feature", "web development"]
url: https://martinfowler.com/bliki/TransparentCompilation.html
slug: TransparentCompilation
word_count: 1083
---


Increasingly web developers are using languages like [CoffeeScript](http://coffeescript.org) and [SCSS](http://sass-lang.com) that compile to other textual source
  languages that execute in the browser. Such source-to-source
  compilers (also called transpilers 1) are not new, [Cfront](http://en.wikipedia.org/wiki/Cfront) was widely used in
  the early days of C++ to generate target C code. But for me there is
  a difference that picks out CoffeeScript and SCSS as
  *transparent* compilers


1: 
     Hunting around usage, it seem to me that the the term
     âtranspilerâ is used as a synonym for source-to-source compiler.
     So transpilers may or may not be transparent. I've also seen the
     term âsource-to-source translationâ used equivalently to
     âsource-to-source compilationâ.


With most compilers, you don't care very much about what is
  generated downstream. As long as it follows the semantics of the
  source language it's effectively a big lump of bits. But if you're
  going to generate JavaScript for the browser, this ignorance is hard
  to live with. Debugging environments are getting pretty nifty these
  days, but they are all in terms of the HTML/CSS/JavaScript triad. So
  it's important that you understand how your input language
  translates to its executable target.


This constraint has a big effect upon the source language. You
  need to ensure that the output corresponds very clearly to the
  source. When I write this CoffeeScript


```
$(window).on 'touchTap', (event) ->
  window.touchPanel.tap(event)

```


I can easily recognize the resulting JavaScript in my browser debugger


```
$(window).on('touchTap', function(event) {
  return window.touchPanel.tap(event);
});
```


This remains true even for more complicated bits of CoffeeScript's
 transformation, such as turning


```
runSetupBuild: (slide, positionClass) ->
  switch positionClass
    when 'current', 'next'
      @buildsFor(slide)?.setupBuild?.forwards()
      # ...
```


into


```
Infodeck.prototype.runSetupBuild = function(slide, positionClass) {
  var _ref, _ref1, _ref2, _ref3;
  switch (positionClass) {
    case 'current':
    case 'next':
      return (_ref = this.buildsFor(slide)) != null ? 
           (_ref1 = _ref.setupBuild) != null ? _ref1.forwards() : void 0 
           : void 0;
    /* ... */
```


There's a lot going on in that transformation - but still the
 correspondence is pretty clear. If I need to debug in that code, I
 can easily see how it matches up to the source CoffeeScript. This is
 the essence of what makes the compilation process *transparent* - the
 intention that you will work in the output language 2.


2: 
     Even with opaque compilation there are cases when people study
     the outputs. Occasionally there are odd behaviors or bugs that do
     require you to dig into the compiler outputs. Some programmers
     like to understand what the compiler is doing, although that's
     got less common as compilers and virtual machines get more
     sophisticated. But such activity is an exception.


In contrast, there are source-to-source compilers that don't
 expect you to work in the output language, or see visibility of the
 output language as an unfortunate temporary mechanism. These can
 still be useful, and you see them in the javascript world with
 languages like Dart, GWT, and ClojureScript. It's this difference in
 *intention* which is what separates the transparent style of
 transpilation from the more common approach. 3


3: 
     It's interesting to see whether the development of [sourcemaps](http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/)
     will shift languages like coffeescript away from transparency.


The fact that you have to work at keeping the compilation
 transparent puts limits on what you can do in the source
 language. You don't have the degree of freedom in your language
 constructs that you get with a more unconstrained form of
 compilation. You have to follow the basic semantics of the target
 language, and keep to much the same program structure. These
 constraints haven't been widely talked about as a feature of language
 design.


CoffeeScript illustrates that despite these constraints you can
 get a considerable difference in syntax between source and target
 languages. CoffeeScript feels much more like Python in syntax than
 the C-like JavaScript. Such syntactic variation isn't always the
 case, indeed there is an important subset of transparent compilation
 languages that strive to be a superset of the target language. SCSS
 and [TypeScript](http://www.typescriptlang.org) fit into
 this category - any CSS expression is valid in SCSS. Using a superset
 language makes the correspondence even clearer and I feel works well
 for CSS where CSS's syntax works well but the language misses some
 handy features.


Some say there's little point in using transparent
 compilation - if you have to understand the target code for
 debugging, what's the value in using a different source? For me, the
 value lies in a couple of directions. First off it's a way of getting
 useful language features that are missing in the target language.
 SCSS gives me handy capabilities such as variables (so I can say
 `$light-purple` instead of `#f8c8fe` and change
 it in only one place should I want to tweak it).


More drastic syntax changes, such as CoffeeScript, require
 stronger justification. One of my colleagues put it very well after finishing a
 project. He's an experienced JavaScript programmer and the project
 wrote well-disciplined JavaScript from the beginning. As a result he
 was very happy with the quality of the JavaScript codebase. However
 he still concluded that they would have been better off working in
 CoffeeScript, because it's easier to understand what is going on when
 you're reading the CoffeeScript, even when you're debugging in the
 generated JavaScript code. The transformation may not look like such
 a big deal for small fragments, such as those I show above. But it
 makes a big difference once you're up to hundreds of lines of code,
 let alone beyond.4


4: 
     I've only done a few hundred lines of coffeescript while working
     on my infodecks, but I agree with him and will continue to use
     coffeescript for any non-trivial amounts of javascript.


## Notes


1: 
     Hunting around usage, it seem to me that the the term
     âtranspilerâ is used as a synonym for source-to-source compiler.
     So transpilers may or may not be transparent. I've also seen the
     term âsource-to-source translationâ used equivalently to
     âsource-to-source compilationâ.


2: 
     Even with opaque compilation there are cases when people study
     the outputs. Occasionally there are odd behaviors or bugs that do
     require you to dig into the compiler outputs. Some programmers
     like to understand what the compiler is doing, although that's
     got less common as compilers and virtual machines get more
     sophisticated. But such activity is an exception.


3: 
     It's interesting to see whether the development of [sourcemaps](http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/)
     will shift languages like coffeescript away from transparency.


4: 
     I've only done a few hundred lines of coffeescript while working
     on my infodecks, but I agree with him and will continue to use
     coffeescript for any non-trivial amounts of javascript.
