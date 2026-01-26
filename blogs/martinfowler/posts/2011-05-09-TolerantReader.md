---
title: "Tolerant Reader"
description: "One of the benefits of using web services is that it helps you to   decouple various parts of a system. People can work on separate   code-bases with some degree of separation. Although you get some  "
date: 2011-05-09T00:00:00
tags: ["application integration", "evolutionary design"]
url: https://martinfowler.com/bliki/TolerantReader.html
slug: TolerantReader
word_count: 712
---


One of the benefits of using web services is that it helps you to
  decouple various parts of a system. People can work on separate
  code-bases with some degree of separation. Although you get some
  decoupling, you cannot eliminate the coupling completely because the services
  still have to communicate to each other through their
  interfaces. The sad thing is that many teams make this coupling much
  worse than it should be.


The governing law for decoupled collaboration should be Postel's
  Law:


> be
>   conservative in what you do, be liberal in what you accept from
>   others.
> -- [Jon Postel](http://tools.ietf.org/html/rfc793)


In the case of collaborating services, one of the stickiest
  points is evolution. Although there are some people who believe that
  you should just get your service definitions right first time so you
  never need to change them, my regular readers will not be surprised
  to find me absent from their parties. In order to be able to evolve
  services you need to ensure that a provider can make changes to
  support new demands while causing minimal breakage to their existing
  clients.


Since writing this bliki entry, Rob Daigneau published a full description of this
    pattern in [Service Design Patterns](https://martinfowler.com/books/sdp.html)


A common way to stuff this up is to use some kind of
  schema-driven binding of your service endpoints. An example of this
  is code-generating C# classes from an XSD definition. This is touted
  as a time-saving feature - the service provider publishes an XSD
  definition of their service, the consumer takes a copy and generates
  a class. Look ma, no programming. It works well until the provider
  needs to make any change to the interface, such as adding a
  field. Adding field to an interface like this shouldn't be a breaking
  change for anyone - but often does break these schemes.


My recommendation is to be as tolerant as possible when
  reading data from a service. If you're consuming an XML file,
  then only take the elements you need, ignore anything you
  don't. Furthermore make the minimum assumptions about the structure
  of the XML you're consuming. Rather than use an XPath search like
  `/order-history/order-list/order` use
  `//order`. Your aim should be to allow the provider to
  make any change that ought not to break your code. A group of XPath
  queries are an excellent way to do this for XML payloads, but you
  can use the same principle for other things too.


On top of this, make sure there's only one bit of code that
  reads data payloads like this. One of the purposes of a [Data Transfer
  Object](https://martinfowler.com/eaaCatalog/dataTransferObject.html) is to wrap the data payload behind a convenient object so the
  rest of the system can just go `anOrderHistory.orders`
  and be impervious to changes that would even break a tolerant
  reader.


It's worth bearing this principle in mind even if your data
  transfer protocol is binary. Imagine you have java programs at both
  ends of the connection, and want to use a binary transfer to keep
  your message sizes down. Most people in this situation would use the
  built-in serialization mechanism of java to serialize objects
  directly, but then if one side adds a field the transfer breaks. You
  can avoid this pretty easily by first putting the data into generic
  collections (lists and maps) and then serializing those collections.
  If you add an extra field to a map, it will still deserialize on the
  other side and it's easy for a tolerant reader to ignore it.


To help the service provider evolve their service, you can then
  communicate which bits of the communication you are reading. A
  good way to do this is to send them the reader and its tests,
  so they can use them in their build process to detect potential
  breakages. Some of you may recognize this as the next step to
  [Consumer-Driven
  Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html)


## Further Reading


There is a full description of this pattern in [Service Design Patterns](https://martinfowler.com/books/sdp.html).


My colleague Ian Cartwright posted a set of useful blog posts
    about this a few years ago. He points out that [schema validation
    offers a false sense of security](http://blog.iancartwright.com/2006/11/schema-validation-offers-false-sense-of.html), and that there are [dangers in
    serialization](http://blog.iancartwright.com/2006/11/dangers-of-serialization.html), both in general and [particularly for domain objects](http://blog.iancartwright.com/2006/12/dont-make-your-domain-objects.html).


Saleem Siddiqui describes how a Tolerant Reader works well with
    a [Magnanimous Writer](http://tenderware.blogspot.com/2011/05/magnanimous-writer.html).
