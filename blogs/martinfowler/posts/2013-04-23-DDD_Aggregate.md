---
title: "D D D_ Aggregate"
description: "Aggregate is a pattern in Domain-Driven Design. A DDD aggregate is a   cluster of domain objects that can be treated as a single unit. An   example may be an order and its line-items, these will be se"
date: 2013-04-23T00:00:00
tags: ["domain driven design", "object collaboration design"]
url: https://martinfowler.com/bliki/DDD_Aggregate.html
slug: DDD_Aggregate
word_count: 192
---


Aggregate is a pattern in Domain-Driven Design. A DDD aggregate is a
  cluster of domain objects that can be treated as a single unit. An
  example may be an order and its line-items, these will be separate
  objects, but it's useful to treat the order (together with its line
  items) as a single aggregate.


An aggregate will have one of its component objects be the
  aggregate root. Any references from outside the aggregate should
  only go to the aggregate root. The root can thus ensure the
  integrity of the aggregate as a whole.


Aggregates are the basic element of transfer of data storage -
  you request to load or save whole aggregates. Transactions should
  not cross aggregate boundaries.


DDD Aggregates are sometimes confused with collection classes
  (lists, maps, etc). DDD aggregates are domain concepts (order,
  clinic visit, playlist), while collections are generic. An aggregate
  will often contain mutliple collections, together with simple
  fields. The term âaggregateâ is a common one, and is used in various
  different contexts (e.g. UML), in which case it does not refer to
  the same concept as a DDD aggregate.


For more details see the [Domain-Driven
  Design book](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20).
