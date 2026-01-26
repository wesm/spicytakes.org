---
title: "Memory Image"
description: "When people start an enterprise application, one of the earliest   questions is âhow do we talk to the databaseâ. These days they may ask a   slightly different question âwhat kind of database s"
date: 2011-08-31T00:00:00
tags: ["database", "application architecture", "event architectures"]
url: https://martinfowler.com/bliki/MemoryImage.html
slug: MemoryImage
word_count: 1312
---


When people start an enterprise application, one of the earliest
  questions is âhow do we talk to the databaseâ. These days they may ask a
  slightly different question âwhat kind of database should we use -
  relational or one of these NOSQL databases?â. But there's another
  question to consider: âshould we use a database at all?â


One of the defining characteristics of enterprise applications is
  the need to store long term data, which naturally leads people to
  reach for a database. After all persisting data is one of the main
  things databases do. Using a memory image is
  a different route to persistence that doesn't involve a database.


The key element to a memory image is using [event
  sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), which essentially means that every change to the
  application's state is captured in an event which is logged into a
  persistent store. Furthermore it means that you can rebuild the full
  application state by replaying these events. The events are then the
  primary persistence mechanism.


A familiar example of a system that uses event sourcing is a
  version control system. Every change is captured as a commit, and
  you can rebuild the current state of the code base by replaying the
  commits into an empty directory. In practice, of course, it's too
  slow to replay all the events, so the system persists periodic
  snapshots of the application state. Then rebuilding involves loading
  the latest snapshot and replaying any events since that snapshot.


Event sourcing has many consequences, including the ability to
  rebuild past states. But the important property for memory images is
  that it means that there is no longer any need to worry about
  keeping the application state in an up-to-date persistent store.
  Instead you can just keep the application state in main memory. Should
  the process crash, you can rebuild it from the events (and snapshots).


Using a memory image allows you to get high performance, since
  everything is being done in-memory with no IO or remote calls to
  database systems. Perhaps more importantly it means you can get rid
  of database mapping code, or worrying about synchronizing between
  in-memory state and database state.


Against that you do have to ensure you can reliably
  store the events and process them. You also need to write the
  code to save and load snapshots and figure out how to restore the
  system quickly enough to keep your quality of service up. Databases
  also provide transactional concurrency as well as persistence, so
  you have to figure out what you are going to do about
  concurrency.


Another, rather obvious, limitation is that you have to have more
  memory than data you need to keep in it. As memory sizes steadily
  increase, that's becoming much less of a limitation than it used to
  be.1


1: 
      You may also be able to reduce memory usage if you only need a
      subset of the data that's in the events. You can send the same
      events to different memory image systems for different subsets
      of data if that makes sense for your needs.


A number of different kinds of systems can make use of a memory
  image, I'll mention three examples I've come across.


The most recent  is [LMAX](https://martinfowler.com/articles/lmax.html). LMAX is a
  high performance trading system, which processes 6 million TPS on a
  single JVM thread. Here the performance advantage of a memory image
  is obviously a big factor, but they found the simplification in
  programming model to be equally important. They don't have to worry
  about concurrency as its all about a single thread. To keep
  availability high, they run multiple copies of the memory image so
  if one goes down they can switch over to another instance while
  keeping their very high transaction rate.


A few years ago I wrote about a couple of systems using an
  [EventPoster](https://martinfowler.com/bliki/EventPoster.html) architecture. This style provides read access
  to the in-memory model to lots of UIs for analytic purposes.
  Multiple UIs mean multiple threads, but there's only one writer (the
  event processor) which greatly simplifies concurrency issues.


The oldest example is also the source for the name - the
  Smalltalk development environment. Most development tools rely on
  text files in a file system which a compiled or interpreted as
  needed. Smalltalk held all its source code and compiled method
  inside the image 2. Every command you
  executed got stored inside a change log. Most of the time you saved
  your image (snapshot) but if necessary you could replay the change
  log from a stable base if you did something foolish.


2: 
      I'm using the past tense here for Smalltalk because it's a long
      time since I used it and it may have changed its behavior over
      the years. It is still around, although sadly only a niche environment.


Like many of these kinds of ideas, it's an approach that's been
  used and reinvented many times 3, but
  never got mainstream traction. Having a database hold persistant
  data continues to be the more common approach.


3: 
      Some people also may remember the [Prevayler](http://prevayler.org/) project, which is an
      open-source implementation of this approach. It generated a lot
      of noise in the Java community a few years ago, but has been
      rather quiet since. That community uses [system
      prevalence](http://en.wikipedia.org/wiki/System_Prevalence) as a generic term for this approach.


One problem I've heard of with memory images is around
  migration. Whenever you are building a software system it's
  important to understand how it will handle changes. With a memory
  image, the essential task is to ensure you can continue to rebuild
  the memory image from the the event log.


One trap here is to use a serialization structure for the event
  log that doesn't handle evolution gracefully should you want to
  change the structure of events. If you create specific event classes
  and serialize them, this may make it difficult to process old events
  should you change the structure of the event class later. Often it's
  best to serialize with generic data structures such as maps and lists.


Also it's important to keep a good decoupling between the events
  and the model structure itself. It may be tempting to come up with
  some automatic mapping system that retrospects on the event data and
  the model, but this couples the events and model together which
  makes it difficult to migrate the model and still process old events.


At some point, it may be worthwhile to migrate the event log
  itself from an old format to a new one. Migrating the event log is
  often more hassle, but may be an option if you've evolved a long way
  from the original event structures.


For a long time, a big argument against using a memory image was
  size, but now most commodity servers have more memory than we were
  used to having in disk. As a result most working sets can now be
  held safely in memory. We noticed this a few years ago, but memory
  images are still relatively rare. I think that now the NOSQL
  movement is causing people  to re-think their options for
  persistence, we may see an upsurge in this pattern.


## Notes


1: 
      You may also be able to reduce memory usage if you only need a
      subset of the data that's in the events. You can send the same
      events to different memory image systems for different subsets
      of data if that makes sense for your needs.


2: 
      I'm using the past tense here for Smalltalk because it's a long
      time since I used it and it may have changed its behavior over
      the years. It is still around, although sadly only a niche environment.


3: 
      Some people also may remember the [Prevayler](http://prevayler.org/) project, which is an
      open-source implementation of this approach. It generated a lot
      of noise in the Java community a few years ago, but has been
      rather quiet since. That community uses [system
      prevalence](http://en.wikipedia.org/wiki/System_Prevalence) as a generic term for this approach.
