---
title: "Function As Object"
description: "In programming, the fundamental notion of an object is the bundling of data and   behavior. This provides a common data context when writing a set of related functions.   It also provides an interface"
date: 2017-02-13T00:00:00
tags: ["encapsulation", "language feature", "object collaboration design"]
url: https://martinfowler.com/bliki/FunctionAsObject.html
slug: FunctionAsObject
word_count: 837
---


In programming, the fundamental notion of an object is the bundling of data and
  behavior. This provides a common data context when writing a set of related functions.
  It also provides an interface to manipulating the data that allows the object to control
  access to that data, making it easy to support derived data and prevent invalid
  modifications of data. Many languages provide explicit syntax to define classes, which
  act as definitions for objects. But if you have a language with first-class functions
  and closures, you can use these constructs to create objects using the Function As
  Object pattern (originally described by Eugene Wallingford).


Here is an example of a simplistic person object, done using the function-as-object
  style in JavaScript. 1


1: 
      For date handling I'm using [js-joda](https://js-joda.github.io/js-joda/), a port of the
      Joda-Time library that cleaned up the appalling mess that was Java's date and time
      handling. I'm glad joda-js is repeating the service of bringing sanity to date and
      time handling.


```
function createPerson(name) {
  let birthday;
  return {
    name: () => name,
    setName: (aString) => name = aString,
    birthday: () => birthday,
    setBirthday: (aLocalDate) => birthday = aLocalDate,
    age: age,
    canTrust: canTrust,
  };
  function age() {
    return birthday.until(clock.today(), ChronoUnit.YEARS);
  }
  function canTrust() {
    return age() <= 30;
  }
}

```


The outer form of a function-as-object is a function, which is called as a
  constructor function. The result of the call is, in essence, a hashmap of functions
  2 which acts as a method selector. This map captures the state
  of any variables in the function in a closure, allowing the data to persist beyond a
  single function invocation. This result hashmap can be treated like a classical object.


2: 
      In JavaScript terminology it's called an object, although it is a JavaScript object,
      not the classical object that we're trying to create. I'll thus refer to it as a
      hashmap, to try and reduce the confusion.


```
const kent = createPerson("kent");
kent.setBirthday(LocalDate.parse("1961-03-31"));
const youngEnoughToTrust = kent.canTrust();
```


Looking at the function-as-object from a classical OO point of view:

- the fields of the object are represented by the parameters to the constructor
    function `(name)`together with the local variables `(birthday)`.
- the methods of the object are the functions nested within the constructor
    function. Like object methods they can freely call each other and manipulate the data
    in these locally scoped variables (fields)
- Nothing outside the constructor function can access the variables, preserving data
    encapsulation.
- The public methods of the object are those functions that are present in the
    result hashmap.
- Any functions nested inside the constructor function but not present in the result
    hashmap are private methods
- The names of the public methods are the keys of the result hashmap, not the names
    of the functions within the constructor function. I prefer to keep the keys and
    function names the same to avoid confusion (although it can be handy to alias
    functions if needed). 3


A common alternative implementation of this pattern is to return a function as the
  method selector rather than the hashmap which is the natural method selector in
  JavaScript. To use a function as the method selector, I'd return a function whose first
  argument is the name of the method to invoke. The function body then switches on that
  value (see [Wallingford](http://www.cs.uni.edu/~wallingf/patterns/envoy.pdf) for more on this).


The function-as-object approach has been around for a long time, I've seen it
  described in lisp many times, and it's been widely used in JavaScript (until ES6,
  JavaScript had a very limited notion of classes). It's often used as an argument that a
  specific syntax for classes isn't necessary, which is the equivalent of
  object-aficionados arguing that you don't need first class functions when you can write
  a class with a single âcallâ method. As a consequence many people in the JavaScript
  world argue against using the ES6 class syntax. Personally, I like having both first
  class functions and first class classes, and prefer ES6's class syntax.


## Further Reading


Eugene Wallingford coined the name âFunction as Objectâ in his [1999 pattern language âEnvoyâ](http://www.cs.uni.edu/~wallingf/patterns/envoy.pdf). His paper is worth reading for more
    details on this, including using a function as the method selector and delegation to
    support some notion of inheritance. The examples in the paper use Scheme.


## Acknowledgements


Chris Ford, Fred George, James Shore, Kevin Yeung, Lucas Lego, Matteo Vaccari, 
     Rob Miles, and Eugene Wallingford

     commented on drafts of this post


## Notes


1: 
      For date handling I'm using [js-joda](https://js-joda.github.io/js-joda/), a port of the
      Joda-Time library that cleaned up the appalling mess that was Java's date and time
      handling. I'm glad joda-js is repeating the service of bringing sanity to date and
      time handling.


2: 
      In JavaScript terminology it's called an object, although it is a JavaScript object,
      not the classical object that we're trying to create. I'll thus refer to it as a
      hashmap, to try and reduce the confusion.


3: 
      In ES6 I can use shorthand property names to remove the duplication by replacing
      â`age: age,`â with â`age,`â.
