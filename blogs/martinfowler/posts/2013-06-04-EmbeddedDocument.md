---
title: "Embedded Document"
description: "Flowing JSON data structures through a server is something I'm   seeing more these days. JSON documents can be persisted directly,   either by using anAggregateOrientedDatabaseor aserialized LOBin   a"
date: 2013-06-04T00:00:00
tags: ["nosql", "encapsulation", "object collaboration design"]
url: https://martinfowler.com/bliki/EmbeddedDocument.html
slug: EmbeddedDocument
word_count: 943
---


Flowing JSON data structures through a server is something I'm
  seeing more these days. JSON documents can be persisted directly,
  either by using an [AggregateOrientedDatabase](https://martinfowler.com/bliki/AggregateOrientedDatabase.html) or a
  [serialized LOB](https://martinfowler.com/eaaCatalog/serializedLOB.html) in
  a relational database. JSON documents can also be served directly
  to web browsers or used to transfer data to server-side page
  renderers. When JSON is being used in this way, I hear people saying
  that using an object-oriented language gets in the way because the
  JSON needs to be translated into objects only to be rendered out
  again - a waste of programming effort 1. I agree
  with the point about waste, but I argue that it's not a problem with objects but
  a failure to understand encapsulation.


1: 
      Some might argue it's a waste of computing effort too - although
      I would be surprised if it were significant. I would certainly
      not accept a performance argument against converting to an
      object graph unless it was accompanied by measurements - just
      like [any performance argument](https://martinfowler.com/ieeeSoftware/yetOptimization.pdf).


Let's imagine we're storing an order as a JSON document and
  serving it up with minor server-side processing, again as JSON. An
  example document might be like this.


```
{ "id": 1234,
  "customer": "martin",
  "items": [
    {"product": "talisker", "quantity": 500},
    {"product": "macallan", "quantity": 800},
    {"product": "ledaig",   "quantity": 1100}
  ],
  "deliveries": [
    { "id": 7722,
      "shipDate": "2013-04-19",
      "items": [
        {"product": "talisker", "quantity": 300},
        {"product": "ledaig",   "quantity": 500}
      ]
    },
    { "id": 6533,
      "shipDate": "2013-04-18",
      "items": [
        {"product": "talisker", "quantity": 200},
        {"product": "ledaig",   "quantity": 300},
        {"product": "macallan", "quantity": 300}
      ]
    }
  ]
}
```


We'll assume we haven't got much server-side processing to do, but we do have
  some. Let's also assume we're using an OO language. A naive approach
  might be to read in the JSON document, convert the data to the
  appropriate object graph (with orders, line-items, and deliveries),
  apply any processing, and then serialize the object graph to JSON
  for the client.


In many of these situtiations a better way to proceed is to keep
  the data in a JSONish form, but still wrap it with objects to
  coordinate manipulation. Most programming environments provide 
  generic libraries that take a document and deserialize it to generic
  data structures. So a JSON document would deserialize to a structure
  of lists and dictionaries, an xml document to a tree of xml nodes.
  We can then take this generic data structure and put it into a field
  of an order object - here's an example with Ruby and JSON.


class Order...


```
  def initialize jsonDocument
    @data = JSON.parse(jsonDocument)
  end

```


When we want to manipulate the data, we can define methods on the
  object as usual, and implement them by accessing this data structre.


class Order...


```
  def customer
    @data['customer']
  end
  def quantity_for aProduct
    item = @data['items'].detect{|i| aProduct == i['product']}
    return item ? item['quantity'] : 0
  end

```


This includes cases with more complex logic. 2


2: 
      Note the chaining of [collection pipelines](https://martinfowler.com/articles/collection-pipeline/) in
      this method. One of my pet annoyances is hearing some functional
      fans say that this style of code isn't object-oriented. While it
      may seem foreign to those with a C++/Java background, this style
      is perfectly natural to smalltalkers.


class Order...


```
  def outstanding_delivery_for aProduct
    delivered_amount = @data['deliveries'].
      map{|d| d['items']}.
      flatten.
      select{|d| aProduct == d['product']}.
      inject(0){|res, d| res += d['quantity']}
    return quantity_for(aProduct) - delivered_amount
  end

```


The embedded document can be enriched before sending to the client.


class Order...


```
  def enrich
    @data['earliestShipDate'] = 
      @data['deliveries'].
      map{|d| Date.parse(d['shipDate'])}.
      min.
      to_s
  end

```


If needed, you can form similar objects on sub-trees of the
  embedded document.


class Order...


```
  def deliveries
    @data['deliveries'].map{|d| Delivery.new(d)}
  end

```


class Delivery


```
  def initialize hash
    @data = hash
  end
  def ship_date
    Date.parse(@data['shipDate'])
  end

```


One thing be wary of here is that such object wrappers aren't
  quite the same as normal objects. The delivery objects returned in
  the above code fragment don't have the same equality semantics that
  you'd expect from objects arranged in the more usual structure.


Despite its compartive rareity, an embedded document fits well
  with object-orientation. The point of encapsulated data is the
  hiding of the data structure, so that users of the object don't know or care about
   the internal structure of the order.


Those familiar with functional programming will recognize the
  style of flowing a generic data structure through a series of
  functions - you can think of the object as providing a namespace for
  manipulating the generic data stuctures.


The sweet spot for an embedded document is when you're providing
  the document in the same form that you get it from the data store,
  but still want to do some manipulation of that data. If you don't
  have any need to access the contents of the JSON document, then
  there's no need to even deserialize it into a generic data
  structure. The order object needs only a constructor and a method to
  return its JSON representaiton. On the other hand as you do more
  work on the data - more server side logic, transforming into
  different representations - then it's worth considering whether it's
  easier to turn the data into an object graph.


## Notes


1: 
      Some might argue it's a waste of computing effort too - although
      I would be surprised if it were significant. I would certainly
      not accept a performance argument against converting to an
      object graph unless it was accompanied by measurements - just
      like [any performance argument](https://martinfowler.com/ieeeSoftware/yetOptimization.pdf).


2: 
      Note the chaining of [collection pipelines](https://martinfowler.com/articles/collection-pipeline/) in
      this method. One of my pet annoyances is hearing some functional
      fans say that this style of code isn't object-oriented. While it
      may seem foreign to those with a C++/Java background, this style
      is perfectly natural to smalltalkers.
