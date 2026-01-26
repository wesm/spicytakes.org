---
title: "Overloaded Getter Setter"
description: "I've been poking around in JavaScript recently and one thing   that's struck me is the habit of using the same function name for a   getter and a setter. So if you want to find out the height of your "
date: 2011-08-02T00:00:00
tags: ["bad things", "api design"]
url: https://martinfowler.com/bliki/OverloadedGetterSetter.html
slug: OverloadedGetterSetter
word_count: 649
---


I've been poking around in JavaScript recently and one thing
  that's struck me is the habit of using the same function name for a
  getter and a setter. So if you want to find out the height of your
  banner in jQuery you would use `$(â#bannerâ).height()`
  and if you want to change the height you would use
  `$(â#bannerâ).height(100)`.


This convention is familiar to me, as it was used by
  Smalltalk. You might get a value with `banner height`
  and change it with `banner height: 100`. Knowing it was
  a smalltalk convention is enough to expect me to like it, since I
  have an distant but abiding love for that language. But even the
  best things have flaws, and I can't hide my dislike for this coding
  style.


My principal objection is that the act of retrieving data is
  fundamentally different to that of setting a value, so the names
  should be more clearly different. 1


1: 
      By getters and setters, I mean methods that look like they
      get/set a value, but may be implemented in any way - following
      the [UniformAccessPrinciple](https://martinfowler.com/bliki/UniformAccessPrinciple.html).


Another reason is the confusion between a setter and a getter
  that takes an argument. If I see
  `$(â#bannerâ).css('height')` the general expectation is
  that it's setting a css property to 'height'. It's only my knowledge
  of the jQuery API that tells me that `css('height')` gets
  the value of the height, which I would update with
  `css('height', 100)`.


The lack of explicitness between getter and setter is greater in
  JavaScript than in Smalltalk because there's only one
  method. Smalltalk is a dynamically typed language, but does overload based on
  the number of arguments to the method.2 JavaScript doesn't overload
  in the language, so the getter and setter shows up as a single
  method. Documentation can help, but the API itself doesn't
  distinguish between them. The presence of the extra argument acts as
  a [FlagArgument](https://martinfowler.com/bliki/FlagArgument.html), which is usually a Bad Thing.


2: Technically it isn't an
    overload, as 'height' and 'height:' are different names (due to
    the colon). But it certainly feels like it.


I'm not proposing that Java's
  ugly `getHeight()` / `setHeight(100)`
  convention is better. I think using a bare value for the getter is usually the
  best way. My preference is to make any setter clearly stand out.


In general I like to do this through different syntax, so the
  property setting syntax of C# and Ruby scores best here. In these
  languages you can get a value with `banner.height` and
  change it with `banner.height = 100`. The point here is
  that use of assignment clearly signals mutation. You don't get the
  ambiguity you get between `$(â#bannerâ).height(100)` and
  `$(â#bannerâ).css('height')` because you would never use
  `=` in a getting method.


This approach does, however, depend on a language that supports
  it. You can't do this with JavaScript 3. In this cases I'd prefer a
  bare getter and prefixed setter, so you'd get the value with
  `banner.height()` and change it with
  `banner.setHeight(100)`.


3: Since I posted this, a couple of people
    pointed out there is now some [javascript](https://developer.mozilla.org/en/JavaScript/Reference/Operators/Special/get) [property](https://developer.mozilla.org/en/JavaScript/Reference/Operators/Special/set) [syntaxes](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Object/defineProperty), although they aren't
     widely used yet.


Despite this preference, you do have to follow the conventions of
  the language you're dealing with. If I were writing Smalltalk again
  I'd still use `height:100` in order retain consistency
  with the conventions of the language. JavaScript, however, isn't
  noted for having strong conventions, so here I'd prefer to avoid this
  convention, even if it is used by jQuery.


## Notes


1: 
      By getters and setters, I mean methods that look like they
      get/set a value, but may be implemented in any way - following
      the [UniformAccessPrinciple](https://martinfowler.com/bliki/UniformAccessPrinciple.html).


2: Technically it isn't an
    overload, as 'height' and 'height:' are different names (due to
    the colon). But it certainly feels like it.


3: Since I posted this, a couple of people
    pointed out there is now some [javascript](https://developer.mozilla.org/en/JavaScript/Reference/Operators/Special/get) [property](https://developer.mozilla.org/en/JavaScript/Reference/Operators/Special/set) [syntaxes](https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Object/defineProperty), although they aren't
     widely used yet.
