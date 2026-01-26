---
title: "Decorated Command"
description: "As a writer and speaker on software development, I dish out a huge amount of general advice about our profession. Whether it's as specific as saying how aDecoratedCommandworks, or as philosophical as "
date: 2004-05-12T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/DecoratedCommand.html
slug: DecoratedCommand
word_count: 347
---


This is a very common pattern and also very simple, it's really
	just the decorator pattern applied to commands. I've seen it used a
	lot with [CommandOrientedInterface](https://martinfowler.com/bliki/CommandOrientedInterface.html)s. You also hear this
	referred to as interceptors and as a form of Aspect Oriented Programming.


You start with some command, usually of some form of basic
	functionality that may need some additional function added to it
	later. So this might be a domain oriented command such as
	PayInvoice. These commands will have some kind of execute
	method.


```
// psuedo C#
class PayInvoiceCommand : Command ...
void Execute() {
  // do interesting domain logic
}
```


Let's say we want to do this inside a transaction. We can
	decorate the command with a suitable transactional decorator.


```
// pseudo C#
class TransactionalDecorator : CommandDecorator ...
  void Execute() {
    Transaction t = TransactionManager.beginTransaction();
    try {
      Component.Execute();
      t.commit();
    } catch (Exception) {
      t.rollback();
    }
  }
    
```


We can also do a security check this way


```
// pseduo C#
class SecurityDecorator : CommandDecorator ...
  void Execute() {
    if (passesSecurityCheck())
      Component.Execute();
  }
```


With these classes in place we can then easily combine them to
	get the right kinds of behavior.


```
//psuedo C#
  // Transaction Invoice Payment
  Command c = new TransactionalDecorator(new PayInvoiceCommand(invoice));
  c.Execute();
  //Transactional and secure payment
  Command c = new SecurityDecorator(
                  new TransactionalDecorator(
                      new PayInvoiceCommand(invoice)));
  c.Execute();
```


Indeed this ability to add behavior dynamically is one of the big
	benefits of a [CommandOrientedInterface](https://martinfowler.com/bliki/CommandOrientedInterface.html).


A lot of things are doing this kind of thing under the aspect
	oriented banner these days. At some point I'm going to dig into this
	more, to see if there's more than this pattern in play.


This is aspectish, but there's more to aspect oriented
	programming than this. In aspect terms, the decorators provide
	advice to the domain command's Execute method. However in order to
	do this, you have to organize everything around the commands, since
	only the Execute method can be advised. More flexible AOP tools,
	such as aspectJ allow you to advise *any* method, and indeed some
	other things such as field access.
