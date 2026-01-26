---
title: "Javascript Promise"
description: "In Javascript, promises are objects which represent the pending result of   an asynchronous operation. You can use these to schedule further   activity after the asynchronous operation has completed b"
date: 2013-04-22T00:00:00
tags: ["language feature"]
url: https://martinfowler.com/bliki/JavascriptPromise.html
slug: JavascriptPromise
word_count: 195
---


In Javascript, promises are objects which represent the pending result of
  an asynchronous operation. You can use these to schedule further
  activity after the asynchronous operation has completed by supplying
  a callback.


```

    aPromise = someAsyncOperation();
    aPromise.done(function() {
      // runs if all went well
    });
    aPromise.fail(function() {
      // runs if something went wrong
    });
    aPromise.always(function() {
      // runs either way
    }); 
```


As well as providing a clear interface to schedule activity
    with asynchronous tasks, they also compose.


```

      composedPromise = $.when(anAsyncFunction(), anotherAsyncFunction());
    
```


In this form (using jQuery promises) the composed promise will
    run its done handlers when all the passed promises succeed and its
    fail handlers if any of them fail.


There are various forms of promises in javascript, annoyingly
    they have subtly different APIs and vocabularies. Probably the
    most used is [jQuery's
    Deferred Object](http://api.jquery.com/category/deferred-object/).


You also hear these concepts described as **futures** and
    **deferreds**. These concepts appear in many languages,
    not just javascript,  often with concurrency in mind as much as
    asynchrony.


For more information I suggest getting a copy of Trevor
    Burnham's [Async JavaScript](http://pragprog.com/book/tbajs/async-javascript). If you
    want a web article, I found Burnham has a [short
    but useful article](http://net.tutsplus.com/tutorials/javascript-ajax/wrangle-async-tasks-with-jquery-promises/) summarizing them.
