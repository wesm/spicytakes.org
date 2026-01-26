---
title: "Role Interface"
description: "A role interface is defined by 	looking at a specific interaction between suppliers and consumers. A 	supplier component will usually implement several role interfaces, 	one for each of these patterns"
date: 2006-12-22T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/RoleInterface.html
slug: RoleInterface
word_count: 925
---


A role interface is defined by
	looking at a specific interaction between suppliers and consumers. A
	supplier component will usually implement several role interfaces,
	one for each of these patterns of interaction. This contrasts to a
	[HeaderInterface](https://martinfowler.com/bliki/HeaderInterface.html), where the supplier will only have a single interface.


Let's look at this with an example. Consider a program for [PERT](http://en.wikipedia.org/wiki/PERT_Chart) style project
planning. In this scheme we break down a project into a set of
activities. We then arrange these activities into a network (strictly
a [directed
acyclic graph](http://en.wikipedia.org/wiki/Directed_acyclic_graph)) to show the dependencies between the tasks. So if
'have breakfast' is a task, then 'make coffee' and 'mix cereal' might
be predecessor activities. This means I cannot begin to have my
breakfast until all the predecessors have completed.


Each activity has a duration, how long we expect it to take. With
	that duration, together with the relationships in the network, we
	can figure out other information. We can calculate the earliest
	start of an activity as the latest earliest finish of its
	predecessors. We calculate the earliest finish of an activity as its
	earliest start plus its duration. Similarly we can work out the
	latest finish and latest start. The code would look something like
	this.


```

  private int duration;

  public MfDate earliestStart() {
    MfDate result = MfDate.PAST;
    for (?TYPE? p : predecessors())
      if (p.earliestFinish().after(result))
        result = p.earliestFinish();
    return result;
  }

  public MfDate earliestFinish() {
    return earliestStart().addDays(duration);
  }

   public MfDate latestFinish() {
    MfDate result = MfDate.FUTURE;
    for (?TYPE? s : successors())
      if (s.latestStart().before(result))
        result = s.latestStart();
    return result;
  }

  public MfDate latestStart() {
    return latestFinish().minusDays(duration);
  }


```


You'll notice a hole in that code above - the `?TYPE?`s. If we
ask an activity for its predecessors and successors, what type of objects
should we expect back? (To be precise we expect to return a
collection, so the real question is what should the type of the elements
of the returned collection be?)


If you use a header interface, the returned interface would be an
activity and would mirror the public methods of our activity class to
create an [InterfaceImplementationPair](https://martinfowler.com/bliki/InterfaceImplementationPair.html).


```

public interface Activity ...
  MfDate earliestStart();
  MfDate earliestFinish();
  MfDate latestFinish();
  MfDate latestStart();

class ActivityImpl...
  List<Activity> predecessors() ...
  List<Activity> successors() ...

```


With a role interface, however, we look at how the collaborating
	objects are actually used. In this case a successor is only used for
	its `latestStart` and a predecessor is only used for its
	`earliestFinish`. So as a result we create two interfaces which only
	have the methods we actually use.


```

public interface Successor {
  MfDate latestStart();
}
public interface Predecessor {
  MfDate earliestFinish();
}

class Activity
  List<Predecessor> predecessors() ...
  List<Successor> successors() ...

```


We can think of a successor as a role that a collaborating object
	plays with respect to this object. This approach of thinking about
	objects and the roles that they play in collaborating with others
	has a long history in the object-oriented world.


The strength of a role interface is that it clearly communicates
	the actual collaboration between an activity and its successors. Often a
	class doesn't use all the methods of a class, so it's good to show which
	ones are actually needed. This can be particularly useful if you
	need to substitute it later on. A header interface forces you to
	implement every method, even if you're not going to need them; but
	with a role interface you only need to implement exactly what's needed.


The disadvantage of a role interface is that it's more effort to
	come up with, since you need to look at each collaboration to form
	the role interface. With a header interface all you have to do is
	duplicate the public methods, no thought needed. There is also a
	sense of dependence on your consumers. I say a âsenseâ because there
	isn't a formal dependency, but it's still enough to make many people
	uncomfortable. They prefer header interfaces because they believe
	that you shouldn't care who uses your service, or how. You publish
	an interface and they can use it if they find it useful.


On the whole I much prefer role interfaces, so I suggest pushing
	towards them as much as you can. There is work involved in doing it,
	but my belief has always been that you should only use interfaces
	when you really need substitutability, and if you do need
	interfaces you should think hard about what the consumer of that
	interface needs.


There is an interesting twist if you think of this in
a remoting context using something like web services. If we were to
ask a remote service for details on predecessors, what should we
expect back? Some might argue that for it to be a role interface, it
should only return a document with earliest finish data. I would
disagree - I think it's perfectly valid for it to return a document
with more data than I asked for. The point is that any type checking
involved should only check that the earliest finish data is present. If 
extra data can be ignored, then it's no crime to supply it; just as a
class may implement multiple interfaces. This thinking matches the philosophy
of [Consumer

Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html), which is one of the reasons I find consumer
driven contracts so compelling.


As I've indicated, this notion has been around for a long
	time. Trygve Reenskaug wrote a [methodology book](https://www.amazon.com/gp/product/0134529308/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0134529308&linkCode=as2&tag=martinfowlerc-20) based around
	analyzing roles and synthesizing them into classes. Robert Martin
	talks about this topic as the [Interface Segregation Principle](http://www.objectmentor.com/resources/articles/isp.pdf): role interfaces follow that principle but header interfaces do not.
