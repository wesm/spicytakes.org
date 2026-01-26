---
title: "Junit New Instance"
description: "I often get questions that surround one of the design choices in 		theJUnittesting framework - the decision to make a new object for 	each test method run. Enough to warrant a quick bliki 	entry. (How"
date: 2004-08-24T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/JunitNewInstance.html
slug: JunitNewInstance
word_count: 1325
---


I often get questions that surround one of the design choices in
		the [JUnit](http://junit.org) testing framework - the decision to make a new object for
	each test method run. Enough to warrant a quick bliki
	entry. (However I feel almost compelled to point out that my writing
	about JUnit does not mean that that I don't  think that other
	forms of testing are important. There are lots of useful testing
	activities, and although JUnit and its cousins are valuable for many
	of them it isn't the solution for everything. For more blogging on
		testing I suggest you look at the blogs of [Brett Pettichord](http://www.io.com/~wazmo/blog/), [Brian
			Marick](http://www.testing.com/cgi-bin/blog), and [James Bach](http://blackbox.cs.fit.edu/blog/james/). You should also not assume that my writing about
	xUnit testing implies suggests the unimportance of refactoring,
	use cases, or flossing.)


Consider the following little Java test class


```

import junit.framework.*;
import java.util.*;

public class Tester extends TestCase {
  public Tester(String name) {super(name);}
  private List list = new ArrayList();
  public void testFirst() {
    list.add(âoneâ);
    assertEquals(1, list.size());
  }
  public void testSecond() {
    assertEquals(0, list.size());
  }
}

```


Some people may not realize this, but both tests pass - and will
	pass in whichever order they are run. This is the case because to
		run this JUnit creates *two* instances of Tester, one for each testXXX
	method. The list field is thus freshly initialized for test method
		run. Now some people think this is a [bug in JUnit](https://beust.com/weblog/2004/02/08/junit-pain/), but it isn't -
	it's a conscious design decision. (For more on this kind of thing
		watch out for [Kent's new book](http://www.amazon.com/exec/obidos/tg/detail/-/0596007434).)


The basic design of JUnit has its origins in a testing framework
	that Kent Beck built in Smalltalk. (Actually to call it a framework
	was a bit of a misnomer - Kent never shipped it out as a
	framework. He preferred people to build it themselves since it would
	only take an hour to two - that way they wouldn't be afraid to
	change it when they wanted something different.) One of the key
	principles in JUnit is that of isolation - that is no test should
	ever do anything that would cause other tests to fail.


Isolation provides several advantages.

- Any combination of tests can be run in any order with the same
			results.
- You never have a situation where you're trying to figure out
		why one test failed and the cause is due to the way another test
		is written.
- If one test fails, you don't have to worry about it leaving
		debris that will cause other tests to fail. That helps prevent
		cascading errors that hides the real bug.


Now JUnit provides other mechanisms that support isolation - in
		particular the `setUp` and `tearDown` methods
		that are run at the beginning and end of each test
		*method*. To use this for my simple example you do this.


```

  public void setUp() {
    list = new ArrayList();
  }
	
```


Most of the time you don't need to use `tearDown`
since the `setUp` can do any reinitialization that you
need.


You could isolate your test methods by having all the
	state be in local variables and not use fields at all. However this
	would mean duplicating your `setUp` code in every test -
	and you know how much I despise [duplication](https://martinfowler.com/ieeeSoftware/repetition.pdf).


Critics of the JUnit approach have argued that since you have
`setUp` and `tearDown` you don't need a fresh
object each time. You can just make sure you reinitialize all your
fields in those methods. Fans of the JUnit approach argue that this
may be true, but many people initialize in fields, and you might as
well provide this greater degree of isolation. After all an important
part of framework design is to make it easy to the right thing (isolation)
and hard (but not impossible) to do things that cause problems. After
all what's the cost of doing it?


The main argument about the cost of the JUnit approach is based
	on the extra objects that are created, both the JUnit test cases and
	all the other objects created in the setup and field
	initializers. Most of the time I think this argument is
	bogus. There's a lot of fear about creating lots of objects, but
	most of the time [it isn't justified](http://www-106.ibm.com/developerworks/java/library/j-jtp01274.html#author1) - it's based on an outdated
	mental model of how object allocation and collection work. Certainly
	there are environments where object creation could be an issue and
	Java was one them in its early days. However modern Java can create
	objects with virtually no overhead, it's no longer an issue. (It
	wasn't in Smalltalk for longer, which is why Kent and Erich didn't
	worry about it.) So most of the time just don't worry about creating
	objects.


That said, mostly doesn't mean alwaysly. One good example of an
	object you don't want to create frequently is a database
	connection. This does make sense to share, but sharing across all
	the test methods in one test case class isn't enough - you'll want
	to share it across much more than that. A cheap and nasty way to do
	this is with static variables. Generally it's wise to shy away from
	statics, but often they're fine in the context of a test run -
	although I still prefer to shun them. JUnit
		actually provides a very flexible mechanism for sharing test
		fixture objects - the [TestSetup](http://junit.sourceforge.net/javadoc/junit/extensions/TestSetup.html)
	decorator. This allows you to setup some common state for any test
	suite, which gives you a lot of more flexibility about sharing state
	across	groups of tests - much more so than just sharing across the
	methods in a single test case class.


Perhaps the biggest problem with TestSetup is that finding
	information on it is so hard that that I almost expected to see âbeware
	of the leopardâ in the documentation. And there is a leopard around
	- if you use TestSetup you are breaking  isolation and
	broken isolation tends to lead to awkward to find bugs. Don't use it
	unless you really, really need it. (But if you do [this forum thread](http://www.testdriven.com/modules/newbb/viewtopic.php?viewmode=flat&order=ASC&topic_id=1115&forum=7&move=prev&topic_time=1089140252) gives you
	some hints on using it, as does J.B. Rainsberger's [new book](https://www.amazon.com/gp/product/1932394230/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1932394230&linkCode=as2&tag=martinfowlerc-20))


(All of this may make you wonder why each test method isn't in its
	own class. Indeed the earliest forms of JUnit did do that, using an
 inner class that subclassed the test case with the fixture. While
 this was a more obvious design, it made it harder to write the tests.
 So they went for the more obscure use of the [pluggable selector](http://junit.sourceforge.net/doc/cookstour/cookstour.htm) pattern.)


A second objection to the JUnit approach is that it isn't
	intuitive - in that the mechanism it uses to pull this off is tricky
	to understand. I sympathize with this, the Pluggable Selector
	pattern isn't well known, and a design style that uses unfamiliar
	patterns is often uncomfortable. On the whole I like the JUnit
	approach because I think the isolation and ease of test writing
	outweighs the esoteric implementation.


But good people disagree with me. Cedric
Beust's [TestNG](http://www.beust.com/testng/) doesn't do
this, perhaps more surprisingly the popular [NUnit](http://nunit.org) implementation doesn't do it
(although [Jim now regrets that decision](http://blogs.msdn.com/jamesnewkirk/archive/2004/12/04/275172.aspx)). The
following NUnit test causes a failure.


```

  [TestFixture]
  public class ServerTester
  {
    private IList list = new ArrayList();
    [Test]
    public void first() {
      list.Add(1);
      Assert.AreEqual(1, list.Count);
    }
    [Test]
    public void second() {
      Assert.AreEqual(0, list.Count);
    }
  }

```


If you're using a framework that works in this style, I strongly
	recommend you initialize all your instance variables in a setup
	method. That way you'll keep your tests isolated, and avoid some
	debug induced hair removal.


I don't happen to agree with reusing the test
	case instance - but I don't think those that made that decision
have a single-digit IQ, have some complex financial killing in mind,
or are embarking on some strange behavior with their lower torsos.
They called the design trade-off differently - and I think life is
better when we can respectfully disagree over the fluid nature of
software design.
