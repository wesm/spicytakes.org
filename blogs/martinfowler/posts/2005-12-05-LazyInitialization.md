---
title: "Lazy Initialization"
description: "Lazy Initialization is a technique that initializes a variable 	(in OO contexts usually a field of a class) on it's first access. It 	canonical form is something like this:"
date: 2005-12-05T00:00:00
tags: ["object collaboration design"]
url: https://martinfowler.com/bliki/LazyInitialization.html
slug: LazyInitialization
word_count: 213
---


Lazy Initialization is a technique that initializes a variable
	(in OO contexts usually a field of a class) on it's first access. It
	canonical form is something like this:


```

public FooClass Foo {
  get {
    if (_foo = null) _foo = calculateFoo();
    return _foo;
  }
}

```


Lazy initialization is useful when calculating the value of the
	field is time consuming and you don't want to do it until you
	actually need the value. So it's often useful in situations where
	the field isn't needed in many contexts or we want to get the object
	initialized quickly and prefer any delay to be later on.


Remember that this is an optimization technique to help
	responsiveness in situations where a client doesn't need the lazy
	initialized value. As with any optimization you shouldn't use this
	technique unless you have a real performance problem to solve.


In particular lazy initialization can cause debugging woes
	because if you try look at the field during debugging you'll cause a
	state change in the system that doesn't happen under normal
	use. (While the [ObservableState](https://martinfowler.com/bliki/ObservableState.html) doesn't change the actual state
	does.) This can lead to situations where bugs seem to disappear when
	you add a print statement - always a good recipe for major ulcers
	on Friday afternoons.
