---
title: "Call Super"
description: "Call Super is a minor smell (or anti-pattern if you like) that 	crops up from time to time in OO frameworks. Its symptoms are 	pretty easy to spot. You are inheriting from a super-class in order 	to p"
date: 2005-08-11T00:00:00
tags: ["bad things", "language feature"]
url: https://martinfowler.com/bliki/CallSuper.html
slug: CallSuper
word_count: 1246
---


Call Super is a minor smell (or anti-pattern if you like) that
	crops up from time to time in OO frameworks. Its symptoms are
	pretty easy to spot. You are inheriting from a super-class in order
	to plug into some framework. The documentation says something like
	âto do your own thing, just subclass the process method. However
	it's important to remember to start your method with a call to the
	super-classâ. An example might be something like this.


```

public class EventHandler ...
  public void handle (BankingEvent e) {
    housekeeping(e);
  }
public class TransferEventHandler extends EventHandler...
  public void handle(BankingEvent e) {
    super.handle(e);
    initiateTransfer(e);
  }
    
```


Whenever you have to remember to do something every time,
that's a [sign

of a bad API](http://www.aristeia.com/Papers/IEEE_Software_JulAug_2004.pdf). Instead the API should remember the housekeeping
call for you. The usual way to do this is to make the handle method a
Template Method, like this.


```

public class EventHandler ...
  public void handle (BankingEvent e) {
    housekeeping(e);
    doHandle(e);
  }
  protected void doHandle(BankingEvent e) {
  }
public class TransferEventHandler extends EventHandler ...
  protected void doHandle(BankingEvent e) {
    initiateTransfer(e);
  }
    
```


Here the super-class defines the public method and provides a
separate method (often referred to as a **hook method**) for the
subclass to override. The subclass writer now doesn't have to worry
his ugly head about calls to super. Furthermore the super-class writer
is free to add calls after the subclass method if she wishes.


There are a couple of ways to define the hook method. In this
case I've shown an empty implementation. This is useful if many
subclasses don't need to provide their own additional behavior. If
many subclasses have to do the same thing, you can consider a default
implementation, which can also be a template method itself to allow
for variation within the common scheme. If every subclass should
provide unique behavior, then you can make the hook method abstract in
the super-class.


One of the problems with this is that there's usually no way to
	indicate that a certain method is a hook method, i.e. that it's the
	one that the framework writer expects to be overridden. You do see
	conventions (the handle/doHandle is one common one), but mostly you
	have to explain how it works. One of the best ways
	to explain it is with an example. When I'm looking at one of these
	cases I usually find the best thing to do is look at an existing
	subclass and see what it does.


In this case there's single, and relatively obvious hook method.
Often, however, there are many methods, all of which could be hooks,
depending on how much control the subclass wants to take.  A quick
glance at the abstract base class for my HTML layout class shows half
a dozen methods that could be overridden. Some subclasses want to do
something simple, and override small hooks; others need to do more
fancy things and override larger scoped methods.


In some languages you can [Seal](https://martinfowler.com/bliki/Seal.html) the handle method to prevent the
	subclass from overriding it. Since I
	have an [EnablingAttitude](https://martinfowler.com/bliki/EnablingAttitude.html), I'm usually reluctant to do this -
	especially if the inheritance is effectively a published
	interface. The argument in favor of sealing is that it means that
	subclasses can't break your super-class. I don't think of overriding
	the wrong thing as 'breaking the super-class'. The subclass and
	super-class have to collaborate closely, after all inheritance is a
	very intimate relationship. Either the whole thing works or it
	doesn't. Sealing can be a good way to indicate to someone that they
	are overriding the wrong thing, and as such I'd be inclined to use
	it for a non-published interface (i.e. the subclasses are part of the
	same code base). My problem with sealing is that a subclass may want
	to override the handle call to do something particularly fancy. I
	can't predict the subclass's needs, so I'd rather say âgo ahead, but
	on your own head be itâ, rather than ânoâ. If it's all one code base
	then we can always take the seal off if we need to.


## Multi-Level Hooks


So I hope you can see that you shouldn't have to rely on call
		super for this kind of situation. But there's a complication when
		you have more than one level of framework.


Here I'll switch to a real example, one that has come up from
		time to time: JUnit. JUnit uses a template method to control the overall
		running of its test cases, it looks like this:


```

public abstract class TestCase
  public void runBare() throws Throwable {
    setUp();
    try {
      runTest();
    }
    finally {
      tearDown();
    }
  }
  protected void setUp() throws Exception {
  }
  protected void tearDown() throws Exception {
  }

```


It's a familiar template method with two empty hook methods for
		overriding. So far, so good; it's easy to add your own set up and
		tear down code as you need it.


The complication comes when a user wants to derive another
		framework from JUnit. There are plenty of examples out there, but
		let's take some simple case where we have a project specific
		convention, say something like this.


```

public class AlphaTestCase extends TestCase
   protected void setUp() throws Exception {
     alphaProjectSetup();
   }

```


This is where you run into the call super problem. So if we use
		the advice from earlier on we could redefine it like this.


```

public class AlphaTestCase  extends TestCase...
  final protected void setUp() throws Exception {
    alphaProjectSetup();
    doSetUp();
  }    
  protected void doSetUp() throws Exception {        
  }

```


While this works, it runs into the problem of confusing anyone
		who is familiar JUnit. Every project they've been on, every book
		they've read says they should override setUp, not this new-fangled
		doSetUp. This is a good case to use final, since there's such a
		high chance that people will get confused. But even with final,
		the confusion a different setup method causes is very painful.


There is another option. The second level framework can
		override the caller of setUp.


```

public class AlphaTestCase extends TestCase...
  public void runBare() throws Throwable {
    alphaProjectSetup();
    setUp();
    try {
      runTest();
    }
    finally {
      tearDown();
    }
  }
  protected void setUp() throws Exception {
  } 

```


Now everyone can use setUp just like normal. The framework
		writer also have more options if they want to add other bits of
		behavior in interesting places. This is always an option worth
		considering - if a template method doesn't work where you are, consider
		going up a level.


Of course there's no such thing as a free template. In some cases
you can't do this because you're not sure what to do because the
source isn't available. In others the framework writers have a
[DirectingAttitude](https://martinfowler.com/bliki/DirectingAttitude.html) and have sealed the calling method,
stopping you from overriding it.


Even if you can do it, there is something to watch. What if the
primary framework writers need to change the method you've overridden
(which indeed JUnit did on the 9th of October 2004). As usual the
power of inheritance comes with responsibility, you have to keep an
eye on what changes occur in the super-class.


Another option that's coming available now is to use an
[Annotation](https://martinfowler.com/bliki/Annotation.html). JUnit and other Java based frameworks have been
working with annotations in the last few months, following the lead
set by [NUnit](http://nunit.org). Annotations allow you to
give more metadata to a method than just the name, allowing you more
options in this kind of situation. But that's the topic for another
day.
