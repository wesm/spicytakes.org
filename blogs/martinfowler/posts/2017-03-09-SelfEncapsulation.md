---
title: "Self Encapsulation"
description: "Data encapsulation is a central tenet in object-oriented style. This says that the   fields of an object should not be exposed publicly, instead all access from outside the   object should be via acce"
date: 2017-03-09T00:00:00
tags: ["encapsulation"]
url: https://martinfowler.com/bliki/SelfEncapsulation.html
slug: SelfEncapsulation
word_count: 606
---


Data encapsulation is a central tenet in object-oriented style. This says that the
  fields of an object should not be exposed publicly, instead all access from outside the
  object should be via accessor methods (getters and setters). There are languages that
  allow publicly accessible fields, but we usually caution programmers not to do this.
  *Self-encapsulation* goes a step further, indicating that all *internal*
  access to a data field should also go through accessor methods as well. Only the
  accessor methods should touch the data value itself. If the data field isn't exposed to
  the outside, this will mean adding additional private accessors.


Here's an example of a reasonably encapsulated java class


class Chargeâ¦


```
  private int units;
  private double rate;

  public Charge(int units, double rate) {
    this.units = units;
    this.rate = rate;
  }
  public int getUnits() { return units; }
  public Money getAmount() { return Money.usd(units * rate); }

```


Both fields are immutable. The units field is exposed to clients of the class via a
  getter, but the rate field is only used internally, so doesn't need a getter.


Here is a version using self-encapsulation.


class ChargeSEâ¦


```
  private int units;
  private double rate;

  public ChargeSE(int units, double rate) {
    this.units = units;
    this.rate = rate;
  }
  public int getUnits()    { return units; }
  private double getRate() { return rate; }
  public Money getAmount() { return Money.usd(getUnits() * getRate()); }

```


Self encapsulaton means that `getAmount` needs to access both fields
  through getters. This also means I have to add a getter for `rate`, which I
  should make private.


Encapsulating mutable data is generally a good idea. Update functions can contain
  code to execute validations and consequential logic. By restricting access through
  functions, we can support the [UniformAccessPrinciple](https://martinfowler.com/bliki/UniformAccessPrinciple.html), allowing us to hide
  which data is computed and which is stored. These accessors allow us to modify the data
  structures while retaining the same public interface. Different languages differ in
  details of what is âoutsideâ for an object by various kinds of
  [AccessModifier](https://martinfowler.com/bliki/AccessModifier.html), but most environments support data encapsulation to some
  degree.


I've come across a few organizations that mandated self-encapsulation, and whether to
  use it or not was a regular topic of debate since the 90's. Its advocates said that
  encapsulation was such a benefit, that you wanted to incorporate it to internal access
  too. Critics argued that it was unnecessary ceremony leading to unnecessary code that
  obscured what was going on.


My view on this is that most of the time there's little value in self-encapsulation.
  The value of encapsulation is proportional to the scope of the data access. Classes are
  usually small (at least mine are) so direct access isn't going to be an issue within
  that scope. Most accessors are simple assignments for the setter and retrieval for the
  getter, so there's little value in using them internally.


But there are common circumstances where self-encapsulation is worth the effort. If there is
  logic in the setter, then it's wise to consider it for any internal updates too. Another
  circumstance is when the class is part of an inheritance structure, in which case the
  accessors provide valuable hook points for subclasses to override behavior.


So my usual first move is to use direct access to fields, but refactor using [Self Encapsulate
  Field](http://www.refactoring.com/catalog/selfEncapsulateField.html) should circumstances demand it. Often the forces that lead me to
  consider self-encapsulation I can resolve by [extracting a new class](https://martinfowler.com//refactoring.com/catalog/extractClass.html).


## Further Reading


Kent Beck discusses these trade-offs under the names Direct Access and
    Indirect Access in both [Implementation Patterns](https://www.amazon.com/gp/product/0321413091/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321413091&linkCode=as2&tag=martinfowlerc-20) and
    [Smalltalk Best Practice Patterns](https://www.amazon.com/gp/product/013476904X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=013476904X&linkCode=as2&tag=martinfowlerc-20)


## Acknowledgements

Ian Cartwright, Matteo Vaccari, and Philip Duldig

    commented on drafts of this post