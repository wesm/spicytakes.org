---
title: "Modeling Message Queues in TLA+"
date: 2018-10-31
url: https://www.hillelwayne.com/post/tla-messages/
slug: tla-messages
word_count: 2422
---

I recently did a [corporate TLA+ workshop](https://www.hillelwayne.com/consulting/) and some people asked what TLA+ specs look like in practice. If you looked at the most common public examples, you’d probably come away thinking that people only used it for critical consensus algorithms. This is a problem for two reasons: first, it makes it harder to learn TLA+, as there aren’t simpler examples to experiment with. Second, it makes it hard for people to see how TLA+ is useful for *them*. My problem isn’t verifying Paxos, it’s figuring out why my microservices aren’t deduping the message queue.


Let’s spec out some messaging! In this post we’ll write simple specs for pub/sub and message queues, in the process showing how we can represent high-level concepts in TLA+ and how we can represent complications. This post assumes knowledge of TLA+: you can read gentler introductions [here](https://www.hillelwayne.com/post/augmenting-agile) and [here](https://www.hillelwayne.com/post/modeling-deployments/).


## Message Queues


Let’s start with something like Amazon SQS: we have some *readers* and some *writers*. Writers add messages to a FIFO queue. Readers pop messages off the queue and process them.


```
---- MODULE messaging ----

EXTENDS Sequences, Integers, TLC, FiniteSets
CONSTANTS Writer, Readers, Data, NULL, MaxQueue

ASSUME Writer \notin Readers
ASSUME NULL \notin Data

```


Initial constants. `MaxQueue` doesn’t necessarily mean we’re modeling bounded queues: I’m mostly adding it to keep the model itself bounded. I won’t have the writer block on a full-queue. I’ll instead add it as a **state constraint** later.


```
SeqOf(set, n) == UNION {[1..m -> set] : m \in 0..n}
seq (+) elem == Append(seq, elem)

```


A couple of helper operators. `SeqOf` generates all sequences no longer than `n` consisting of elements in `set`. `(+)` slaps an element onto the end of a sequence, in case I need to do something like `Tail(seq) (+) Head(seq)`.


```
(*--algorithm polling
variables 
  queue = <<>>; \* Ordered messages

define
  TypeInvariant ==
    queue \in SeqOf(Data, MaxQueue)
end define;

```


TLA+ is an untyped formalism. Lamport [argued](https://lamport.azurewebsites.net/pubs/lamport-types.pdf) that type systems in specifications are often a hindrance. However, while TLA+ is untyped, the system we’re building does have types. We express that as a *type invariant*, which is a regular invariant that places constraints on the values our variables can take. The type of `queue` is “Any finite sequence of `Data`.”1 But I could just as easily make types like “two-digit primes except 11” or “sequences of messages no reader has seen yet.”


Again, we need to be explicit that in our particular case, `TypeInvariant` is catching both *spec failures* and *model failures*. If an element of `queue` is not a piece of data, then that’s a spec failure. If `queue` has more than `MaxQueue` elements, then it’s a model failure: we forgot to add our state constraint. If part of our spec was that we were using a bounded model and `queue` had more than `MaxQueue` elements, then *that* would be a spec failure too. Mixing spec invariants and model constraints is bad practice. You should really separate them out.


```
process writer = Writer
variable d \in Data
begin
  Write:
    while TRUE do
      queue := queue (+) d;
    end while;
end process;

process reader \in Readers
variables local = NULL;
begin
  Read:
    while TRUE do
      await queue /= <<>>;
      local := Head(queue);
      queue := Tail(queue);
    end while;
end process;

end algorithm; *)
====

```


Rest of it isn’t too hard. We need to assign values our constaints and add state constraints:


```
Data <- [model value] {d1, d2}
MaxQueue <- 3
NULL <- [model value]
Readers <- [model value] {r1, r2}
Writer <- [model value]


INVARIANT TypeInvariant
CONSTRAINT Len(queue) < MaxQueue

```


And this passes with no failures. Of course, this is a very simple model. SQS guarantees **at-least once** delivery. What this means exactly depends on how much we care about modeling our broker’s mechanism of enforcing this. I see at least three different ways of defining “at-least once” for different purposes of modeling:

1. The system will only declare a message received if a client received it.
2. (1) holds *and* if the client and system are both **weakly fair**, then the message will at some point be marked “received”.
3. Clients might receive the message multiple times.


The difference between (1) and (2) is that (2) is stronger: the first case permits the client to *never* receive the message if it **stutters**, or (*very* roughly) is allowed to “crash”. Saying the client is “fair” means that it will never “crash” and always make progress if it can.2 The difference between them and (3) is that (1) and (2) are *properties* of the system, while (3) is a detail about our system that implictly assumes those properties. If we were modeling the messaging protocol itself, we’d probably want to use (1) or (2). If we’re modeling a system using the message protocol, (3) is closer to what we want. Here’s one way to model it:


```
  while TRUE do
    await queue /= <<>>;
    local := Head(queue);
-   queue := Tail(queue);
+    either
+      queue := Tail(queue);
+      DoStuff:
+        \* blah blah blah
         skip;
+    or
+      skip;
+    end either;

```


Instead of the client always removing the received message from the queue, sometimes it sets `local` without tailing the queue. This means on the next request, another client might receive the same message. We’d want our properties to still hold even if the message is duplicated. We could also easily permit the client to fail to process the message, but “clean up” by popping it from the queue and putting it on the end:


```
    either
      queue := Tail(queue);
+   or
+     queue := Tail(queue) (+) local;
    or
      skip;
    end either;

```


Or sometimes fail to ack we’ve received the message *and* fail to process it, in which case the message gets duplicated.


```
    either
      queue := Tail(queue);
    or
      skip;
    end either;

+   DoStuff:
+     either
+       \* blah blah blah
+     or
+       queue := queue (+) local;
+     end either;

```


Now imagine if we actually *wanted* to bound the queue. We’d tell the writer not to write by adding an `await` and remove our state constraint.


```
  Write:
    while TRUE do
+     await Len(queue) < MaxQueue;
      queue := queue (+) d;
    end while;

- CONSTRAINT Len(queue) < MaxQueue

```


This now fails, a reader can append to a full queue during `DoStuff`. We’ll undo these changes for the next section.


### Complex data


If we actually wanted to spec a system, we’d want to fill out `DoStuff` with logic based on the messages or other bits of state. Just having the messages be model constants doesn’t give us much flexibility. To show what a more flexible system would look like, let’s also attach the sender to each message.


```
+ set ++ e == set \union {e}
+ Messages == [from: Readers ++ Writer, msg: Data]

(*--algorithm polling

```


`Messages` is the set of all possible structures with those keys and values. It includes elements like `[from |-> r1, msg |-> d1]`, `[from |-> Writer, msg |-> d2]`, etc. Our `TypeInvariant` can be changed to be a sequence of all possible complex messages. We can change writer and reader to use the new format.3


```
  TypeInvariant ==
-    queue \in SeqOf(Data, MaxQueue)
+    queue \in SeqOf(Messages, MaxQueue)

  Write:
    while TRUE do
-     queue := queue (+) d;
+     queue := queue (+) [from |-> Writer, msg |-> d];
    end while;

  Read:
    while TRUE do
      await queue /= <<>>;
      local := Head(queue);
      either
        queue := Tail(queue);
        DoStuff:
          skip;
      or
-       queue := Tail(queue) (+) local;
+       queue := Tail(queue) (+) [from |-> self, msg |-> local]
      or
        skip;
      end either;      
    end while;

```


Our spec now fails as `TypeInvariant` is violated. We forgot to extract the data from `msg`, so we ended with a message like `[from |-> r1, msg |-> [from |-> Writer, msg |-> d1]`. One soluton would be to instead set `local` to `Head(queue).msg`, but then we lose information about the source. Another choice would be to instead have `from` be the set of all nodes that put this particular message on the queue.


```
- Messages == [from: Readers ++ Writer, msg: Data]
+ Messages == [from: SUBSET (Readers ++ Writer), msg: Data]

  Write:
    while TRUE do
-     queue := queue (+) [from |-> Writer, msg |-> d];
+     queue := queue (+) [from |-> {Writer}, msg |-> d];
    end while;

  Read:
    while TRUE do
      await queue /= <<>>;
      local := Head(queue);
      either
        queue := Tail(queue);
        DoStuff:
          skip;
      or
-       queue := Tail(queue) (+) [from |-> self, msg |-> local]
+       queue := Tail(queue) (+) [from |-> local.from ++ self, msg |-> local.msg]
      or
        skip;
      end either;      

```


We could then add retry logic, for example “if this reader has seen this message already, ignore it instead of retrying”:


```
      or
+       if self \notin local.from then
          queue := Tail(queue) (+) [from |-> local.from ++ self, msg |-> local.msg]
+       end if;

```


On the other hand, if we can’t change our old fields for legacy reason, we can add another field to the structure: `[from: ..., msg: ..., through: ...]`.


## Pub-Sub


A **pub-sub** messaging system is one where there are multiple clients which receive each message the server sends. We can represent this as each reader having its own queue. The writer, instead of appending its message to a single queue, simply appends it to all of them.


```
\* same constants and operators as last time

(*--algorithm pubsub
variables 
  queues = [r \in Readers |-> <<>>]; \* Ordered messages

```


Instead of a single queue, we have one queue for each reader. This is represented with a TLA+ **function**, which maps elements from some set to some value. For people who don’t see the “math” there, the best analogy is a python dictionary comprehension: this is sort of like writing `{r: [] for r in Readers}`.


Of course, since we no longer have a single queue, we need to change our `TypeInvariant`:


```
  TypeInvariant ==
    queues \in [Readers -> SeqOf(Data, MaxQueue)]

```


`[A -> B]` is the **function set** where the domain is `A` and all of the values are in `B`. Function sets are one of the biggest stumbling blocks for people new to TLA+, but they are amazingly powerful once you get used to them.


And for the rest of the code:


```
process writer = Writer
variable d \in Data
begin
  Write:
    while TRUE do
      queues := [r \in Readers |->
        queues[r] (+) d
      ];
    end while;
end process;

process reader \in Readers
variables local = NULL;
begin
  Read:
    while TRUE do
      await queues[self] /= <<>>;
      local := Head(queues[self]);
      queues[self] := Tail(queues[self]);
    end while;
end process;

```


We have to adjust our constraint, too:


```
CONSTRAINT \A r \in Readers: Len(queues[r]) < MaxQueue

```


This works as normal. Pub-sub is usually **at-most once** delivery. No client will receive a given message more than one time. We can pretty easily model this by simply having the clients occasionally drop messages in their queue:


```
process reader \in Readers
variables local = NULL;
begin
  Read:
    while TRUE do
      await queues[self] /= <<>>;
+     either
        local := Head(queues[self]);
+     or
+       local := NULL;
+     end either;
      queues[self] := Tail(queues[self]);
    end while;
end process;

```


### Subscription


Not all readers may be subscribed to every writer. Their subscription state is also time dependent, and they might change what they subscribe to over the course of our run. Here’s one way of representing that that:


```
(*--algorithm pubsub
variables 
  queues = [r \in Readers |-> <<>>]; \* Ordered messages
+ subscribed = {};

define
  TypeInvariant ==
-   queues \in [Readers -> SeqOf(Data, MaxQueue)]
+   /\ queues \in [Readers -> SeqOf(Data, MaxQueue)]
+   /\ subscribed \in SUBSET Readers
end define;

  Write:
    while TRUE do
      queues := [r \in Readers |->
+       IF r \in subscribed THEN
          queues[r] (+) d
+       ELSE queues[r]
      ];
    end while;

  Read:
    while TRUE do
+     either
+       \* receive
        await queues[self] /= <<>>;
        either
          local := Head(queues[self]);
        or
          local := NULL;
        end either;
        queues[self] := Tail(queues[self]);
+     or
+       await self \notin subscribed;
+       Subscribe:
+         subscribed := subscribed ++ self;
+     or
+       await self \in subscribed;
+       Unsubscribe:
+         subscribed := subscribed \ {self};
+     end either;  
    end while;
end process;

```


Now, instead of sending each message to every single reader, the writer only sends messages to readers that are subscribed to it. We could more compactly write the message logic this way:


```
- queues := [r \in Readers |->
-   IF r \in subscribed THEN
-   queues[r] (+) d
-   ELSE queues[r]
- ];
+ queues := [r \in subscribed |-> queues[r] (+) data] @@ queues

```


Where `@@` is the “function merge” operator imported from TLC.


One way we could make this more complex (if your model needs it) is to instead have readers subscribe to topics, and writers message all readers for a given topic. This would be useful if one writer was writing to two sets of readers, or two writers were messaging one set of readers.


## Thoughts


I really need to make a library or cookbook or whatever of common TLA+/PlusCal patterns. It took me only a couple minutes to whip each example up but I’ve been doing this a while- it’s probably a lot harder to ‘see’ these if you’re just starting out. Having a library would go a long way to making it easier for people to pick things up.


I’ve regularly used these messaging designs as part of larger specs. Hopefully you find them useful! You can find other examples in my [new book](https://www.apress.com/us/book/9781484238288), too!


*Interested in using TLA+ at work? Hire me as a [consultant](https://www.hillelwayne.com/consulting/)!*


*Thanks to [Andrew Helwer](https://ahelwer.ca/) for feedback.*


---

1. A lot of TLA+ people use `TypeOk` instead of `TypeInvariant`. I prefer the latter for two reasons. One, I’ve seen a lot of people misread `TypeOk` as `TypeOK` and get frustrated when that didn’t work. Two, I like how `TypeInvariant` emphasizes that the spec being well-typed is just another invariant of the system.
 [return]
2. It’s a little more complex than that. It’s only guaranteed to make progress if it is always able to make progress. To guarantee progress if it *cycles* between enabled and disabled, we need to use **strong** fairness.
 [return]
3. Tangent: it’s a bit too advanced for this post, but we could easily add a safety property saying that if a message is added to the queue, it’s `from` is the client that added it.
 [return]
