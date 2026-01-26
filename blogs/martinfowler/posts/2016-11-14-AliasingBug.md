---
title: "Aliasing Bug"
description: "Aliasing occurs when the same memory location is accessed through more than one   reference. Often this is a good thing, but frequently it occurs in an unexpected way,   which leads to confusing bugs."
date: 2016-11-14T00:00:00
tags: ["bad things"]
url: https://martinfowler.com/bliki/AliasingBug.html
slug: AliasingBug
word_count: 396
---


Aliasing occurs when the same memory location is accessed through more than one
  reference. Often this is a good thing, but frequently it occurs in an unexpected way,
  which leads to confusing bugs.


Here's a simple example of the bug.


```
Date retirementDate = new Date(Date.parse("Tue 1 Nov 2016"));

// this means we need a retirement party
Date partyDate = retirementDate;

// but that date is a Tuesday, let's party on the weekend
partyDate.setDate(5);

assertEquals(new Date(Date.parse("Sat 5 Nov 2016")), retirementDate);
// oops, now I have to work three more days :-(
```


What's happening here is that when we do the assignment, the partyDate variable is
  assigned a reference to the same object that the retirement data refers to. If I then
  alter the internals of that object (with `setDate`) then both variables are
  updated, since they refer to the same thing.


![](images/aliasingBug/flow.png)


Although aliasing is a problem in that example, in other contexts it's what I expect.


```
Person me = new Person("Martin");
me.setPhoneNumber("1234");
Person articleAuthor = me;
me.setPhoneNumber("999");
assertEquals("999", articleAuthor.getPhoneNumber());
```


It's common to want to share records like this, and then if it changes, it changes
  for all references. This is why it's useful to think of *reference objects*, which
  we deliberately share 1, and [Value Objects](https://martinfowler.com/bliki/ValueObject.html) that we don't want this kind of shared update behavior. A good way to
  avoid shared updates of value objects is to make value objects immutable.


1: 
      The [Evans Classification](https://martinfowler.com/bliki/EvansClassification.html) has the notion of Entity, which I see as a common form of
      reference object.


Functional languages, of course, prefer everything to be immutable. So if we want
  changes to be shared, we need to handle that as the exception rather than the rule.
  Immutability is a handy property, one that makes it harder to create several kinds of
  bugs. But when things do need to change, immutability can introduce complexity, so it's
  by no means a free breakfast.


## Acknowledgements


Graham Brooks and James Birnie's comments on our internal mailing list led me to
    write this post.


## Further Reading


The term aliasing bug has been around for a while. It appears in Eric Raymond's
    [Jargon
    file](http://www.catb.org/jargon/html/A/aliasing-bug.html) in the context of the C language where the raw memory accesses make it even more
    unpleasant.


## Notes


1: 
      The [Evans Classification](https://martinfowler.com/bliki/EvansClassification.html) has the notion of Entity, which I see as a common form of
      reference object.
