---
title: "Some links on Java garbage collection"
date: 2016-04-23
url: https://jvns.ca/blog/2016/04/23/some-links-on-java-garbage-collection/
slug: some-links-on-java-garbage-collection
word_count: 904
---


Basically every time I write a blog post like [yesterday’s on garbage collection](https://jvns.ca/blog/2016/04/22/java-garbage-collection-can-be-really-slow/), people reply with a huge amount of information about the topic; way more than I can take in immediately. This is great. Please do not stop doing that.


I want to get better at recording what everyone tells me so I can refer back to it later when I need to know more. So here are some cool resources if you want to know more about Java garbage collection! I may add more as I come up with them.


There’s a great series of blog posts by [Cory Watson](http://onemogin.com/) – [Why Garbage Collection](http://onemogin.com/programming/gc/why-garbage-collection.html), [Java GC Tuning for Noobs: Part 1
](http://onemogin.com/java/gc/java-gc-tuning-for-noobs-1.html), [Java GC Tuning for Noobs Part 2: Generational
](http://onemogin.com/java/gc/java-gc-tuning-generational.html), [GC Tuning for Noobs: Part 3, Parallelism
](http://onemogin.com/java/gc/java-gc-cms.html). This is my favorite intro to Java GC so far because it’s so conversational and doesn’t assume a lot. In one of them he lists every JVM configuration flag. holy crap there are a lot of possible flags. No wonder people can spend their whole career just learning about Java and how to make it work well!


My favorite thing is that he wrote that last post *this morning* and I read it and learned a ton from it. I love it when the awesome people I know write blog posts and it teaches me stuff. Please do this more everyone.


A few people pointed out that [the docs from Oracle on GC tuning](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html) are surprisingly quite useful. I often forget to check official documentation so this was a great reminder.


Several people recommended the book [Java-Performance-The-Definitive-Guide](http://www.amazon.com/Java-Performance-The-Definitive-Guide/dp/1449358454) and its section about garbage collection. Good books are a goldmine so I will probably buy it.


Hacker News, as it often does, provided a mix of extremely helpful and informative comments and insults ([comments here](https://news.ycombinator.com/item?id=11554700)). Stick with the informative comments, Hacker News. You all know so much great stuff <3.


At this point so many people have told me that they appreciate that I blog about stuff that seems “obvious” to many people that comments like “in other news, the sky is blue” don’t bother me too much. Writing about stuff that is pretty well-known but not obvious to newcomers is one of my favorite things. If you already know everything I’m talking about, maybe tell me something new I don’t know and make my day!


One of the many informative comments (from `__ph__`) said: (quoting it here because it was so great and I don’t want to forget it).


> Probably a book needs to be written as in “Pragmatic Garbage Collection” summarizing some good practices to avoid surprises as the author of the article encountered. Having used Java since its creation and other GCed languages, I would summarize them as follows:


> avoid allocating objects on the heap which you do not have to allocate. The less fresh allocations you have, the less the GC has to do. That does not mean you should write ugly and complex code, but if the tool described in the article was for example grep-like, then one should not have to allocate each line read separately on the heap just to discard it. If possible use a buffer for reading in, if the io libraries allow it.
> generational GCs try to work around this a bit, as the youngest generation is collected very quickly, assuming the majority of the objects is already “dead” when it happens, only the “survivors” are copied to older generations. Make sure that the youngest generation is large enough, that this assumption is true and only objects are promoted to older generations which indeed have a longer lifetime.

- language/library design makes a huge difference how much pressure there is on the GC system. Less heap allocations help, also languages, which try not to create too complex heap layouts. In Java, an array of objects means an array of pointers to objects which could be scattered around the heap, while in Go you can have an array of structs which is one contiguous block of memory which drastically reduces heap complexity (but of course, is more effort to reallocate for growing).
- good library design can bring a lot of efficiency. At some point in time, just opening a file in Java would create several separate objects which referred to each other (a buffered reader which points to the file object…). My impression is, “modern” Java libraries too often create even larger object chains for a single task. This can add to the GC pressure.


> Of course, all these practices can be used equally well to bring down a program with manual allocation to a crawl. So in summary I am a strong proponent of GC, but one needs to be aware of at least the performance tradeoffs different factorings of one program can bring. Modern GCs are incredibly fast, but that is not a magic property.


A few more tidbits:

- [apparently there’s a pauseless garbage collector you can pay for called Zing](https://www.azul.com/products/zing/zinqfaq/)
- there’s also an open source pauseless garbage collector called [Shenandoah](http://openjdk.java.net/jeps/189), [homepage?](https://wiki.openjdk.java.net/display/shenandoah/Main). I saw a talk about it at strange loop 2014 and it’s not clear what the state of it is.
- Several people pointed out that you can use different garbage collectors in Java (the G1 collector! the parallel collector!) and it seems like experimenting with choices of garbage collectors is definitely a pro move.
