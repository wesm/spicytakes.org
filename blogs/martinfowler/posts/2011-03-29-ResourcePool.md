---
title: "Resource Pool"
description: "Many programs need to make use of resources that are expensive to create and maintain. Examples of these are database connections and threads. A resource pool provides a good way to manage these resou"
date: 2011-03-29T00:00:00
tags: ["database", "application architecture"]
url: https://martinfowler.com/bliki/ResourcePool.html
slug: ResourcePool
word_count: 321
---


Many programs need to make use of resources that are expensive to
create and maintain. Examples of these are database connections and
threads. A resource pool provides a good way to manage these resources.


When a client needs to use a database connection, rather than
create one itself, it asks the pool to give it one. After the client
is done with the connection it returns it to the pool. Often a pool
will create a bunch of connections when it starts up. The size of the
pool can usually be set through configuration controls and can be
adapted depending on how much need there is from clients and the costs
of maintaining the resources.


If all the resources are in use when a client requests a new one,
there are a couple of different responses. One is to throw an
exception, another is to make the client wait until a resource comes
available. Often the best response, if possible, is to grow the pool
by creating further connections. That way the pool can be set to a low
initial size and will grow as needed. If you do this you may need a
mechanism to see if many resources are idle and then shrink the pool
if the resources are a problem to hold onto. Even with dynamic
growing, you will probably still need some limit for the pool's size,
at which point you don't want the pool to grow any more.


One problem you often run into with resource pools is clients not
handing back the resources - which is a resource leak. A good way of
combating that is to set the pool limit to 1 during testing, and
configure the pool so that asking for a resource at limit raises an
exception. That makes it easier to find the leaky client.


A good source for more information on resource pools is the Pooling
pattern in [POSA 3](https://www.amazon.com/gp/product/0470845252/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470845252&linkCode=as2&tag=martinfowlerc-20)
