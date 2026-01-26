---
title: "Expression Builder"
description: "One of the problems with aFluentInterfaceis that it results in 	some odd looking methods. Consider this example:"
date: 2013-08-08T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/ExpressionBuilder.html
slug: ExpressionBuilder
word_count: 398
---


One of the problems with a [FluentInterface](https://martinfowler.com/bliki/FluentInterface.html) is that it results in
	some odd looking methods. Consider this example:


```

customer.newOrder()
  .with(6, âTALâ)
  .with(5, âHPKâ).skippable()
  .with(3, âLGVâ)
  .priorityRush();

```


Methods like `with`, `skippable`, and
	`priorityRush` don't sit well on the Order class. The
	naming works well in the context of the little
	[DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html) that the fluent interface
	provides, but we usually expect APIs in the form of what I call a
	**Command-Query API**. In a command-query API each method makes
	sense individually in any context. It may also honor such principles
	as [CommandQuerySeparation](https://martinfowler.com/bliki/CommandQuerySeparation.html) which in Java means that
	methods that change the [ObservableState](https://martinfowler.com/bliki/ObservableState.html) of an object
	shouldn't have a return value. Mixing fluent-style methods with
	command-query methods may lead to confusion because fluent methods
	can violate the expectations of what most APIs should look like.


An Expression Builder is a solution to this problem. An
	expression builder is a separate object on which we define the
	fluent interface that then translates the fluent calls to the
	underlying regular API calls. So an expression builder for the order
	case would look something like this.


```

public class OrderBuilder {
  private Order subject = new Order();
  private OrderLine currentLine;

  public OrderBuilder with(int quantity, String productCode) {
    currentLine = new OrderLine(quantity, Product.find(productCode));
    subject.addLine(currentLine);
    return this;
  }

  public OrderBuilder skippable() {
    currentLine.setSkippable(true);
    return this;
  }

  public OrderBuilder priorityRush() {
    subject.setRush(true);
    return this;
  }

  public Order getSubject() {
    return subject;
  }
}
```


In this case I have a single expression builder class, but you
can also have a small structure of builders, something like a customer
builder, order builder, and line builder. Using a single object means
you need a variable to keep track of what line you are working on for
the `skippable` method. Using a structure can avoid this,
but is a bit more complicated and you need to ensure lower level
builders can handle methods that are intended for higher order
builders. In this case an `OrderLineBuilder` would need to
have delegating methods for all the methods of the
`OrderBuilder`.


## Further Reading


I talk in more detail about [Expression Builders](https://martinfowler.com/dslCatalog/expressionBuilder.html) in [my book on Domain-Specific Languages](https://martinfowler.com/books/dsl.html)


A good, open example of the use of an expression builder is in the [JMock](http://jmock.org) library. I found the [OOPSLA paper](http://www.mockobjects.com/files/evolving_an_edsl.ooplsa2006.pdf) describing the evolution of JMock's DSL handling very helpful.


## Revision History


First published 4 January 2007. Revised 8 August 2013.
