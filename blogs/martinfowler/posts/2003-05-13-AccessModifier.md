---
title: "Access Modifier"
description: "Object-oriented languages divide a program into modules called classes. Each class contains features, which consist of data (fields) and methods. (Not all languages use these terms, but they'll do for"
date: 2003-05-13T00:00:00
tags: ["encapsulation", "language feature"]
url: https://martinfowler.com/bliki/AccessModifier.html
slug: AccessModifier
word_count: 682
---


Object-oriented languages divide a program into modules called
classes. Each class contains features, which consist of data (fields)
and methods. (Not all languages use these terms, but they'll do for
this.) Languages have various rules about what other classes can
access the features of a class, these are often based on access
modifiers that apply to a class.


## C++ Choice


Probably the most influential set of access modifiers started with
C++, which has three.

- *public:* Any class can access the features
- *protected:* Any subclass can access the feature
- *private:* No other class can access the feature


A class can also give access to another class or method with the
`friend` keyword - hence the comment that in C++ friends can touch
each others' private parts.


## Java


Java based itself on C++. It added the notion of package to the
language, and this influenced behavior.

- *public:* Any class
- *(package):* (The default, and doesn't use a keyword in
the code) Any class in the same package
- *protected:* Any subclass or class in the same package
- *private:* No other class


Notice the subtle distinction between Java's protected and C++'s
protected (just to keep things confusing.)


## C#


C# also is based on the C++ model

- *public:* Any class
- *internal:* Any class in the same assembly (default for
			methods and classes, but may be specified)
- *protected:* Any subclass
- *protected internal:* Any subclass or class in the same assembly
- *private:* No other class (default for fields)


In C# an assembly is a physical unit of composition - equivalent to a
dll, jar, or binary. C# also has logical units (namespaces) that are
similar to java packages, but they don't play in access modifiers.


## Smalltalk


Smalltalk is often considered to be the purest OO language, and
predates C++, Java, and C#. It didn't use keywords to control access,
but used a basic policy. Smalltalkers would say that fields were
private and methods were public.


However the private fields don't really mean the same as what they
mean in C++ based languages. In C++ *et al* access is thought of as
textual scope. Consider an example with a class Programmer which is a
subclass of class Person with two instances: Martin and Kent. In C++
since both instances are of the same class then Martin has access to
the private features of Kent. In Smalltalk's world view access is
based on objects, so since Martin and Kent are different objects
Martin has no business getting at Kent's fields. But again, since
everything is object based Martin can get at all his fields even if
they were declared in the Person class. So data in Smalltalk is closer
to protected than private, although the object scope makes things
different in any case.


## Access control does not control access


If you have a field that's private it means no other class can get at
it. **Wrong!** If you really want to you can subvert the access control
mechanisms in almost any language. Usually the way through is via
reflection. The rationale is that debuggers and other system tools
often need to see private data, so usually the reflection interfaces
allow you to do this.


C++ doesn't have this kind of reflection, but there you can just use
direct memory manipulation since C++ is fundamentally open memory.


The point of access control is not to prevent
		access, but more to signal that the class prefers to keep some
		things to itself. Using access modifiers, like so many things in
		programming, is primarily about communication.


## Published Methods


I've argued that there is really room for another access type:
[PublishedInterface](https://martinfowler.com/bliki/PublishedInterface.html). I think there is a
fundamental difference between features you expose to other classes
within your project team and those you expose to other teams (such as
in an API). These published features are a subset of public features
and have to be treated differently, so much so that I believe that the
distinction between published and public is more important than that
between public and private..
