---
title: "Test Invariant"
description: "There's been a long-running, if low-key,  argument between the 	advocates of Design by Contract (DbC) and Test Driven Development 	(TDD). I'm not going to delve into that right now, but I will pass 	o"
date: 2006-01-05T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/TestInvariant.html
slug: TestInvariant
word_count: 280
---


There's been a long-running, if low-key,  argument between the
	advocates of Design by Contract (DbC) and Test Driven Development
	(TDD). I'm not going to delve into that right now, but I will pass
	on an idea to merge the two that came up when I was talking with
	[Daniel Jackson](http://people.csail.mit.edu/dnj/).


In DbC you define an invariant for each class. This invariant
	states the properties of the class that must always be true. A
	object must always satisfy its invariant (unless it's in the middle
	of doing anything.) Using Eiffel the class invariant is
	automatically checked before calling a method (in pre-condition
	checking) and after (in post-condition checking). A failure in the
	invariant throws an exception. (This checking may be turned off for
	production use if desired for performance.)


Applying this idea to TDD means that you define a common method
to test the invariant in your production classes and test it in your
test code.


It's time for the usual trivial example.


```

public class Bowler ...
    int overs, runs, wickets;

```


A simple invariant for a bowler is that these values should all by non-negative. So you could have an invariant defined like this.


```

    public boolean passesInvariant() {
        return (runs >= 0 && overs >= 0 && wickets >= 0);
    }
```


You would then using during testing after the setup and exercise
phases of the test.


```

    public void testConcedingRunsAddsToRunsScore() {
        Bowler botham = new Bowler();       // setup - showing my age
        assert botham.passesInvariant();
        botham.concedeRuns(4);              //exercise
        assert botham.passesInvariant();
        assertEquals(4, botham.getRuns());  //verify
    }

```


I haven't tried this myself, nor am I aware of anyone else who
	does. But I thought I'd mention it as an interesting thought.
