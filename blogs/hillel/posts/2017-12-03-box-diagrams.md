---
title: "How is a Class like a Microservice?"
date: 2017-12-03
url: https://www.hillelwayne.com/post/box-diagrams/
slug: box-diagrams
word_count: 1533
---

At work we’re discussing moving some stuff to microservices. A lot of people said that they like “how microservices separate concerns while monoliths entangle them”. Others argued that “monoliths can be separated just fine with modules”, to which someone responded “it’s really hard to keep modules separate”. But “don’t you have the same problem with federated microservices?” etc etc etc.


As the discussion went on I realized that we all actually wanted the same thing out of our architecture, but we weren’t able to make that thing explicit. We didn’t have a common language to talk about what we actually mean by “separation of concerns”. I’d like to try to pin that down here. Note that we’re going to be discussing microservices exclusively on separation of concerns: other qualities, like independent scaling, language freedom, etc are not a part of this essay.


First, let’s abstract out the implementation of code. No classes, no services, no functions, just this black box we’re going to call… a **box**.1


A box is a pile of stuff. We don’t know or care how it’s organized. It just sits there. To make it useful we’ll add **arrows**, which represent interactions.


We can have more than one box, of course. If an arrow starts in a box, it (the box) is doing the interacting, and if it ends in a box, that box is being interacted with. Arrows don’t have to start or end in boxes, which represents an interaction with the environment, like a person kicking it.


With boxes and arrows we can draw pretty diagrams, but to actually make it useful for our purposes we need to add just one more thing. Every box has some number of circles on the ends, or **ports**. We’ll also put in the restriction that arrows must end on ports. This gives us enough structure to call diagrams valid or invalid based on whether or not they obey this restriction.


It’s obvious that we can use our boxes-and-ports diagram to represent some code organization. It’s a little less obvious *just how many* things we can represent. We can say that the boxes are classes, the arrows are method calls, and the ports are public methods. That gives us OOP. Or we can say that the boxes are services, the arrows are HTTP calls, and the ports are APIs. That gives us a microservice architecture. Abstract far enough and classes and microservices have the same representation!


From a design perspective, an OO monolith and a collection of microservices have the same topology. Can we use this to figure out why the monolith has a higher risk of coupling? We’ll add another property to our abstraction: we’ll make it **fractal**. This means you can zoom out of a diagram to see the containing box, and you can zoom in on an box to see the internal diagram.


To make this more concrete, here’s a class:


```
class Foo
  def bar; end
private
  def baz; end
end

```


In the context of the program, `Foo` is a box with `bar` as a port. `baz` is not a port, since an outside class can’t call it. But in the context of `Foo`, both `bar` and `baz` are boxes with their function calls as ports. In the context of our software system, this ruby program is itself a box with some ports, most likely its I/O classes. `Foo.bar` may or may not be a port of the program box. And that program may be part of a larger server application. We can keep zooming in and out with arbitrary resolution, albeit limited usefulness.


As a final rule, we’ll say that arrows cannot cross into a box. If box A contains box B, an arrow starting from outside A can end on a port of A but not a port of B. We’ll still allow an arrow to cross from B to outside A. We want to see what we can do with as few rules as possible.


We have a way of describing **encapsulation**. We can hide a collection of code sharing a single domain inside a larger box that abstracts away the implementation. If done properly, we have an expectation (of sorts) that we don’t need to know what’s inside the outer box to use its ports. This is the idea of interface/implementation decoupling, or the “black box”. As long as the interface stays the same, we can make whatever changes we want to the implementation without having to QA our entire system. The box is our structure, the ports are our interface, and the insides are the implementation. If something outside a box can’t use a port inside of the box, we’ll say that box is/has a **proper interface**.


In Ruby, the biggest box with a proper interface is the class.2 Modules are intended to be a bigger box, but they don’t have a proper interface. Rather, they only act as namespaces. You can make internal modules and classes private via `private_constant`, but this is both obscure and not very Rubyish.3 Rather, we generally ‘enforce’ proper interfaces via convention, telling people not to use “internal classes”. Convention, as we all know, is fragile:

- The programmer has to know that you’re using a boxes-and-ports abstraction in the first place, and that you want only certain methods to be usable to outside classes.
- You need some way to document what methods are the ports. Comments might work for small projects but they don’t scale, especially when you have a complex code architecture.
- It’s easy for a programmer to accidentally violate the interface, putting extra pressure on code review to catch the error.
- It’s easy for a harried programmer to *intentionally* violate the interface and convince everybody else it’s “just this once”.


Eventually, the system becomes entangled and everything becomes terrible. A microservice architecture, on the other hand, has a bigger proper interface than the class: the microservice. The only way to interact with a microservice is to make an HTTP request.4 You can choose what methods the API exposes, thereby enforcing a proper interface. We can guarantee decoupling between the boxes in different services!


This only goes so far, though. In the architecture discussion, one engineer warned against “federated microservices”. This was where services “knew about” other services and added API calls to their logic. In his experience this leads to implicit couplings and a “microlith” in practice, where the services all depended on each other. In many cases this happened because the “microservice” was the largest possible proper interface, but they needed a bigger box. There was no way to group clusters of services into larger boxes with proper interfaces. Not only that, but there was no way to describe this as a problem. Without a common notation for boxes, ports, and interfaces, there’s no easy to communicate what, exactly, it is you’re losing.


And without that notation, it’s hard to see that one of the major claimed benefits of a microservice architecture, separation of concerns, is us using devops to compensate for a flaw in our programming language. This doesn’t mean that microservices are bad. What it *does* mean is that we need to be clear of what we want out of microservices. If we want microservices to improve scalability or use multiple languages, then they may be the right choice. But if we want them primarily for the separation of concerns, I think that’s a bad idea.


Let’s tie this off with an exercise for the reader. Notation is really powerful. With just three components and a couple rules we were able to see symmetries between classes and services. By defining a specific subset of this abstraction we were able to show why Ruby’s module system encourages coupling. But there are all sorts of ways we can strengthen or weaken the model. Just a few examples:

- Arrows have to end at ports. What if we placed restrictions on where they start?
- For proper interfaces, arrows can’t cross into a box. What if arrows couldn’t cross *out* of a box?
- Can two boxes intersect? Can a box be inside two different boxes at once?
- What if we assigned boxes and ports different “colors” and used that to restrict arrows?


Make some small tweaks to the model. What real-world programming structures does it represent now? What can we learn from it?


*Thanks to [Alex Koppel](http://alexkoppel.com/) for feedback.*


---

1. I’m trying really hard to avoid any terms already used to describe code organization because all the good ones are overloaded into meaninglessness.
 [return]
2. Technically classes don’t have proper interfaces, because you can always use `Object.send` to call private methods. In practice classes do have proper interfaces: use `send` and your coworkers will throw rocks at you.
 [return]
3. While reading a draft of this article, [Alex Koppel](http://alexkoppel.com/) discovered `private_constant` in [this article](https://blog.arkency.com/2016/02/private-classes-in-ruby/), which was the first he’d ever heard of it. He’s been professionally writing Ruby for almost a decade now. Nobody else in our company had heard of it, either.
 [return]
4. This isn’t the only way, of course. You can interact with message queues, pub/sub, a shared data store, etc. I’m simplifying here.
 [return]
