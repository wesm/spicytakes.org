---
title: "Observable State"
description: "What do people mean when they say a method doesn't change   the observable state of an object?"
date: 2006-01-05T00:00:00
tags: ["encapsulation"]
url: https://martinfowler.com/bliki/ObservableState.html
slug: ObservableState
word_count: 277
---


**What do people mean when they say a method doesn't change
  the observable state of an object?**


It's very useful to separate methods into those that change state
  and those that don't. Non-state changing methods (which I call
  queries), can be used in any context without worrying about how they
  sequence with other methods.


The key here is not so much that they don't change any state, but
  they don't change *observable* state. The observable state of an
  object is what can be detected from its query methods - let me
  illustrate with a couple of quick examples.


The simplest example is that of a cache. Imagine a range class
  like this.


```

# ruby
class MyRange
  attr_reader :start, :finish
  def initialize start, finish
    @start, @finish = start, finish
    @lengthCache = nil
  end
  def length
    @lengthCache = (@finish - @start) unless @lengthCache
    return @lengthCache
  end
end

```


Here we have a `lengthCache` variable that is filled on the first
  access using [LazyInitialization](https://martinfowler.com/bliki/LazyInitialization.html). Putting a value in the
  lengthCache clearly changes the real state of the object. It doesn't
  change the observable state because you can't tell that the object's
  state has changed from the outside.


By can't tell from the outside I mean that the result of calling
  any method on MyRange from another object will be the same whether or not the
  lengthCache value is filled.


Typically you'd get this effect by
  ensuring that any method on `MyRange` uses the length method to get
  the range rather than using the field directly. Caches are an
  obvious case of state whose changes should never be observable. It's
  also true that any lazy initialization shouldn't change observable state.
