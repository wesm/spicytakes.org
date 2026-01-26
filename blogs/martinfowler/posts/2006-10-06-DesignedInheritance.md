---
title: "Designed Inheritance"
description: "One of the longest running arguments on object-oriented circles 	is the debate betweenOpenInheritanceand 	Designed Inheritance. The principle of Designed Inheritance is 	probably best summed up byJosh"
date: 2006-10-06T00:00:00
tags: ["encapsulation", "api design"]
url: https://martinfowler.com/bliki/DesignedInheritance.html
slug: DesignedInheritance
word_count: 514
---


One of the longest running arguments on object-oriented circles
	is the debate between [OpenInheritance](https://martinfowler.com/bliki/OpenInheritance.html) and
	Designed Inheritance. The principle of Designed Inheritance is
	probably best summed up by [Josh Bloch](https://www.amazon.com/gp/product/0201310058/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201310058&linkCode=as2&tag=martinfowlerc-20): âDesign and document for
	inheritance or else prohibit itâ. With this approach you take care
	to decide which methods can be inherited and [Seal](https://martinfowler.com/bliki/Seal.html) the
	others to stop them being overridden.


The most common argument for designed inheritance is that since
inheritance is a very intimate (and encapsulation breaking)
relationship, it's easy for subclasses to effectively break their
superclasses by, for instance,  omitting necessary behavior when they
the methods are called.


Many developers, particularly those with a [EnablingAttitude](https://martinfowler.com/bliki/EnablingAttitude.html) find
	this style of argument unconvincing. Another argument that I've
	found more appealing is that of Elliote Rusty Harold while
	discussing the [design
	principles of XOM](http://www.cafeconleche.org/XOM/designprinciples.xhtml). The point here is that âAPIs  are written
by experts for non expertsâ. The library writer should be well versed
in the technology that the library works with. She should work to
simplify this technology for library users. Encapsulation is all about
hiding secrets, so a good library should hide all sorts of
complications and danger points from library users, whether they use
that library though calling or inheritance. So with XOM  I can
safely override the library classes to do what I want yet the library
guarantees that it will still produce well-formed XML, without me
having to worry my ugly little head about all the things that might
otherwise go wrong.


Such an argument is much more convincing to me that the usual one
	which carries the subtext that library writers are smart and users
	stupid. This isn't about ability, but about detailed knowledge. I
	want to be as ignorant as I can be the sordid details of XML. By
	relieving me of needing to understand these kinds of details, I can
	use my brain power the actual task I want to accomplish.


Despite this persuasive argument my instinct, and the fact that I
have an enabling attitude, tends to prefer open inheritance. Perhaps
the crux of the problem is the mechanism we use to signal safe areas
of inheritance. Usually all we have is the ability to seal classes and
methods. An alternative to placate both camps would be to have an ability to
overcome a seal. That way you have to go out of your way to override
something that wasn't designed. If you don't explicitly open the seal,
then the compiler only allows normal inheritance, but if you use the
seal-opening 
mechanism then the compiler will hand over the trust to you - and you
are responsible for the consequences. So I'd prefer to replace Josh
Bloch's 'prohibit' with a 'discourage'.


Taking a broader view my guess is there's still a lot of room for
improvement in how we think about interfaces, both for calling and
inheritance. Ideas like [Consumer

Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html) are needed to help us rethink what it means to
have an interface definition. I don't know what the answer would be,
but I think a good answer would surprise all of us.
