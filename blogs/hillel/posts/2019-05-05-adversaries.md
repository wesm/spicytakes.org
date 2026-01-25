---
title: "Modeling Adversaries with TLA+"
date: 2019-05-05
url: https://www.hillelwayne.com/post/adversaries/
slug: adversaries
word_count: 2431
---

A common question I get about specs is how to model bad actors. Usually this is one of two contexts:

1. The spec involves several interacting agents sharing a protocol, but some of the nodes are faulty or malicious: they will intentionally try to subvert the system.
2. The spec involves an agent subject to outside forces, like someone can throw a rock at your sensor.


These “open world” situations are a great place to use formal methods. We can’t easily represent rock-dropping with line-of-code verification. But with specs, we can independently design and verify the invariants of our program, and then explore how the invariants change when we add in outside forces. This works for both adversaries and environmental effects, albeit with somewhat-different implementations.


One note: this is a bit more advanced than my usual TLA+ stuff. In particular, I’m not using PlusCal: you can still model this all in PlusCal tool but it’s much more elegant in pure TLA+. If you know TLA+, great! This is an essay on specification patterns. If you don’t know TLA+, then consider this a demonstration of how powerful it is.1


## Environmental Effects


Following Michael Jackson (not the singer)’s convention we’ll define the parts of the system we can control as the **machine** and the parts of the system we can’t control as the **world**. We’ll start by writing a very simple TLA+ spec for the machine, then compose it with a spec of the world.


Our example will be a **controller**. We have some quantity - temperature, utilization, number of online servers - which takes a discrete value on some `TotalInterval`. We want to keep the value within a `Goal` interval: it should converge to it in finite time and stay there. Normally we’d also implement some form of sensor and actuator. We’ll go extremely high level and say that our machine can either directly increment or decrement x.2 I’ll go ahead and hardcode the interval and goal.


```
---- MODULE Machine ----
EXTENDS Integers

VARIABLES x

TotalInterval == 0..10
Goal == 2..4
 
TypeInvariant ==
  /\ x \in TotalInterval

ChangeX ==
  IF x < 3 THEN x' = x + 1 ELSE x' = x - 1

Machine == ChangeX

Init ==
  /\ x \in TotalInterval

Next ==
  \/ Machine
    
Spec == Init /\ [][Next]_x /\ WF_x(Machine)

====

```


`x` can start at any arbitrary point in the interval. The machine will nudge it down unless `x` is less than 3, where it instead will nudge it up. The machine is **fair**: over an infinite interval, it will nudge `x` an infinite number of times. This prevents it from crashing on us.3


We want to test that the spec is **stable**: eventually `x` enters the `Goal` and never leaves. We can express this property by combining **always** (`[]`) and **eventually** (`<>`) to get “eventually-always”:


```
Safe == x \in Goal
Stable == <>[]Safe

```


If we check this spec with TLC, the property holds. In addition to guaranteeing it converges to stability, we might also want to verify short-term safety. For example, we might want to show that once our spec reaches the `Goal`, it will never under any circumstances leave the goal:


```
AlwaysSafe == [][Safe => Safe']_x

```


This also passes.


### The World


Now let’s add the world. `World` is our generic term of any kind of outside actor, whether malicious, environmental, or just buggy. Not only can it do things our machine cannot, but it’s not something we can “control”. Any restrictions to the world is a weakening of our spec.4


```
Machine == ChangeX

+ SpiteUs == 
+  /\ x' \in TotalInterval
+ 
+ World == SpiteUs
 
Init ==
  /\ x \in TotalInterval

Next ==
  \/ Machine
+ \/ World

```


By saying `x' \in TotalInterval`, I’m saying that the world can, at any point, set x to any integer in that interval.  At every step of our behavior, at least one of `Machine` and `World` are true: the machine adjusts `x` and/or the world spites us. In some cases, *both* are simultaneously true, for example when `x = 7 /\ x' = 6`. Does our property still hold?


```
PROPERTY Stable
<temporal properties violated>
Trace: x = 0, x = 1, x = 0, x = 1

```


We don’t have anything preventing the `World` from continually acting, ever-thwarting our attempts to properly control our system. The `Machine` may be able to get it within spitting distance of the goal, but each time the world pushes us back. If we want to get any guarantee at all, we need to weaken our requirement in some way. We can quickly show that just strengthening the machine is not enough, by making it more powerful and rerunning the spec:


```
ChangeX ==
-  IF x < 3 THEN x' = x + 1 ELSE x' = x - 1
+  x' \in Goal

```


This still fails, with the trace `x = 0, x = 2, x = 0...`. Let’s roll that change back and focus on how we can tweak our requirements.


### Finite Spites


If the world is only kicking things out of alignment a finite number of times, say one million, then it *should* still be stable. My argument is that after the millionth kick, we’re now somewhere in `TotalInterval` and the spec is equivalent to one without the `World`. We can represent “finite `World` actions” by saying “it’s not always eventually the case that `World` happens”, which we’d write in TLA+ as `~[]<><<World>>_x`. Here the `<<>>` means “an action that changes x”, not sequence.


```
Stable == <>[]Safe
+ FiniteWorldStable == ~[]<><<World>>_x => Stable

```


While `Stable` still doesn’t hold, `FiniteWorldStable` does.


### Resilience vs Stability


We can’t guarantee stability if `World` can happen an infinite number of times. We can never guarantee stability in this case. But we might be able to guarantee **resilience**. A system is stable if it can’t be pushed out of `Goal`. A system is resilient if, after being pushed out of `Goal`, it eventually returns to `Goal`.5 For our purposes the difference is we write `[]<>` (always-eventually) instead of `<>[]` (eventually-always). Note that stability implies resilience but not vice-versa.


```
Resilient == []<>Safe

```


Our system is not resilient for the same reason it wasn’t originally stable: if the `World` action keeps happening, we never return to equilibrium. However, to get resilience we don’t need to require `World` to only happen finite times. Instead, we only need to guarantee it happens finite times *while we’re out of equilibrium.* If eventually the world only kicks `x` out of `Goal` when it’s already *in* `Goal`, then we’re giving our machine enough time to return `x` *to* `Goal` and we have resilience.


Another way of looking at it: if `World` happens rarely enough, say one-tenth as often as `Machine`, then we’ll return to `Goal` before the next `World` action pushes us out again.


```
RareWorldResilient == <>[][World => Safe]_x => Resilient

```


This property holds.6


## Machine Invariants


That takes care of `Stable`: while our spec doesn’t satisfy `Stable`, it does satisfy `FiniteWorldStable` and `RareWorldResilient`. But `Stable` was only one of our two properties. The other was `AlwaysSafe`:


```
Safe == x \in Goal
AlwaysSafe == [][Safe => Safe']_x

```


This cannot possibly still be true. If `x \in Goal`, then any `World` action violates `AlwaysSafe`!


What we actually want to capture is that our *machine* is safe. The world is free to violate our invariants, but our machine isn’t. That’s what we can control, and that’s what we want to confirm does nothing unsafe. A more accurate spec, then, is to say that any `Machine` action won’t push `x` out of `Goal`.


```
MachineSafe == [][Machine /\ Safe => Safe']_x

```


This passes, which means that we know that the part of the system we control will not break this invariant.


## Adversaries


That covers how to cover environmental effects. We can also model adversaries. In the TLA+ formulation, and we can think of an adversary as an agent in the system who can take a *superset* of the actions everybody else can. The attacker can *choose* to act like a regular agent, but can also intentionally break the protocol. This means that the general case of our spec is the one where everybody is an attacker, and the “normal” case is actually the exceptional one!


This is a rudimentary spec of a very simple ring system. Each node can send messages to one other node. One node is the leader and starts emitting a signal. As each follower receives the signal, it flips some value to ‘on’ and emits the signal to the next node in the ring. *Ideally*, when the leader starts receiving the signal, we know that it propagated to all of the nodes in the ring.


```
---- MODULE Nodes ----
EXTENDS Integers, FiniteSets
CONSTANT NumNodes, NumAttackers
ASSUME NumNodes \in Nat /\ NumAttackers \in Nat
ASSUME NumNodes > 0 \* TLA+ Naturals start at 0
ASSUME NumAttackers <= NumNodes

VARIABLES node, atk, receiving
vars == <<node, atk, receiving>>

\* Helper op: sequences in TLA+ start at 1
a %% b == IF a % b = 0 THEN b ELSE a % b

Nodes == 1..NumNodes

\* The attackers can be any subset of the nodes of the right size
Attackers == {
  A \in SUBSET Nodes: Cardinality(A) = NumAttackers
}

Node == [next: Nodes, val: BOOLEAN]

Rings == {
  r \in [Nodes -> Node]:
    \A n \in Nodes:
      r[n].next = (n + 1) %% NumNodes
  }


Init ==
  /\ atk \in Attackers
  /\ LET 
       InitRing(ring) ==
         /\ ring[1].val
         /\ \A n \in 2..NumNodes:
             ~ring[n].val
     IN
       node \in {r \in Rings: InitRing(r)}        
  /\ receiving = {}

\* Allow next node to receive
Emit(n) ==
  /\ node[n].val
  /\ receiving' = receiving \union {node[n].next}
  /\ UNCHANGED <<node, atk>>
  
\* Set as received
Receive(n) ==
  /\ n \in receiving
  /\ node' = [node EXCEPT ![n].val = TRUE]
  /\ UNCHANGED <<receiving, atk>>

Next ==
  \/ \E n \in Nodes:
      \/ Emit(n)
      \/ Receive(n)

Spec == Init /\ [][Next]_vars  

----

AllReceived == \A n \in Nodes: node[n].val

\* If the leader marks itself received, all nodes before have received
Safety == 1 \in receiving => AllReceived

====

```


`Safety` is satisfied here. We encoded attackers, but didn’t actually give them anyway to attack. We’ll say an attacker can act like a normal node, but can *also* decide at any point it received the signal and start emitting it anyway.


```
+ FlipSelf(n) ==
+   /\ node' = [node EXCEPT ![n].val = TRUE]
+   /\ UNCHANGED <<receiving, atk>>

  Next ==
    \/ \E n \in Nodes:
        \/ Emit(n)
        \/ Receive(n)
+   \/ \E a \in atk:
+       \/ FlipSelf(a)

```


`Safety` no longer holds for all values of `NumAttackers`. If the last node in the ring is an attacker, it can immediately switch to “on” and emit to the leader. However, not all properties collapse on us. For example, if we made `Emit` and `Receive` weakly fair for all nodes, then `<>AllReceived` would still hold even if all the nodes are attackers! We’d have to allow attackers to decide not to emit to model that case.


---


This is just the tip of the iceberg in terms of what we can model. With a little more expertise, we can do things like

- Use refinements to show that a specific implementation is a valid machine, but successfully maintains invariants and prevents negative properties.
- Compose the spec as part of a larger one
- With some finesse, compare two instances of the spec to find **hyperproperties**, like “four attackers can’t do more damage than one attacker.”


If this kind of stuff interests you, I wrote a [book](https://www.apress.com/us/book/9781484238288) on TLA+, though this material is too advanced to be covered there. I also do [consulting and workshops](https://www.hillelwayne.com/consulting/) on TLA+ and other formal methods, like Alloy. Feel free to [email](mailto:consulting@hillelwayne.com) me if you’re interested in learning more!


*Thanks to [Andrew Helwer](https://ahelwer.ca/) for feedback.*


## Update 14 May 2019


Markus Kuppe, the head developer on TLC, points out a subtle error in the Machine spec. `~[]<><<World>>_x => Stable` is an invariant, sure… but so is `~[]<><<World>>_x => FALSE`! What gives?


The problem is that every `Machine` action is also a `World` action! `x' = x - 1 => x' \in TotalInterval`, so `Machine => World`. Saying that we eventually have no `World` actions, then, also means we don’t have any `Machine` actions. But since we made `Machine` fair, it will happen infinitely often and `~[]<><<World>>_x` is always false. Since `FALSE => FALSE` is true, our property was vacuously true.


The *actual* property we want is


```
~[]<><<World /\ ~Machine>>_x => Stable

```


Which holds. Alternatively, we could make `Machine` and `World` mutually exclusive:


```
- World == SpiteUs

+ World == 
+   /\ SpiteUs
+   /\ ~Machine  

```


This depends on the ordering of the two clauses: if `~Machine` is before `SpiteUs`, the possible values of `x'` are not defined and TLC raises an error. There’s a similar issue with `RareWorldResilient`: we want


```
+ <>[][x' \notin Goal /\ ~Machine => Safe]_x => Resilient 
- <>[][World => Safe]_x => Resilient 

```


To properly model “kicking it outside” of goal.
Markus discusses other solutions [here](https://lemmster.de/tla-liveness-review.html). In particular, he shows how we can use **history variables** to cleanly model this. Give it a read!


---

1. If you want to follow along, the filename must match the module name. So `MODULE Machine` must go in a file named `Machine.tla`. This is case-sensitive.
 [return]
2. One nice thing about TLA+ we can write the implementation, including the sensor and actuator, as a separate spec and show it properly models this one. This is called **refinement**. 
 [return]
3. It’s actually only **weakly** fair: it’s only guaranteed to run an infinite number of times because it’s never blocked by anything. If something was intermittently-but-repeatedly blocking it, we couldn’t guarantee anything without upgrading to **strong** fairness. 
 [return]
4. This doesn’t mean our spec is invalid, just that we’ve narrowed the circumstances in which we can guarantee our required properties. In practice this may be the best we can hope for.
 [return]
5. Everybody comes up with their own meanings for “stability”, “robustness”, and “resilience” and they all contradict each other. 
 [return]
6. Funnily enough, we can’t formally verify a weaker version of this! `[][World => Safe]_x => Resilient` means that if we *only* have `World` while in equilibrium, then we’re Resilient. But TLC can’t check statements of the form `[][P]_x => Q`, despite it being a weaker property than `<>[][P]_x => Q`.
 [return]
