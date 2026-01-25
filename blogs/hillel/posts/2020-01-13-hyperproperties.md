---
title: "Hypermodeling Hyperproperties"
date: 2020-01-13
url: https://www.hillelwayne.com/post/hyperproperties/
slug: hyperproperties
word_count: 2230
---

When we design programs, we usually look for two kinds of properties: that “bad things” never happen and that “good things” are guaranteed to happen. These are called **safety** and **liveness** properties, respectively. These are properties that we want to hold true for every possible program behavior. “We always complete every request” is a liveness property. If our system has it, every program trace will complete every request. If it doesn’t hold, I can give you a example behavior where the server never responds. “Our maximum response time is under 10ms” is a safety property. If false, I can give a trace where the server takes longer than 10ms to respond.


But what about “our average response time is under 10ms”? This can’t be safety *or* liveness, because it’s not defined for individual behaviors. If I give you a trace where the server takes more than 10ms, you can just respond “that’s just an outlier”. Instead, I need to show you that *all* of the behaviors of the program average out to more than 10ms.


Properties which are only defined for sets of behaviors are **hyperproperties**. Hyperproperties can be significantly more complex than regular properties and are correspondingly more difficult to check. They’re also harder to reason about in general. We can sort of relate our intuition of safety to hypersafety, but we can’t do that with hyperliveness.1


Let’s look at an example of a hypersafety property. All examples are in TLA+ and assume some basic familiarity with both raw TLA+ and PlusCal. The post should be followable without it; if not, you might find [this](https://www.hillelwayne.com/post/modeling-deployments/) introduction helpful.


## Example: Observational Determinism


We have two threads that are nonatomically incrementing a counter. Each first stores the value of the current thread, increments the stored value by one, and reassigns to the global counter.


```
EXTENDS Integers, TLC, Sequences
Threads == 1..2

(*--algorithm threads

variables
  x = 0;

define
  FinalIsTwo == <>[](x = 2)
end define

fair process thread \in Threads
variables tmp = 0;
begin
  Get:
    tmp := x;

  Inc:
    x := tmp + 1;
end process;

end algorithm; *)

```


The intention of this spec is *probably* that we increment `x` twice. That corresponds to the property `FinalIsTwo`: “at the end of the run, `x` is 2.” If we check `FinalIsTwo`, the model checker gives us a counterexample:


show error trace
  
`State 1:
/\ x = 0
/\ pc = <<"Get", "Get">>
/\ tmp = <<0, 0>>

State 2:
/\ x = 0
/\ pc = <<"Inc", "Get">>
/\ tmp = <<0, 0>>

State 3:
/\ x = 0
/\ pc = <<"Inc", "Inc">>
/\ tmp = <<0, 0>>

State 4:
/\ x = 1
/\ pc = <<"Done", "Inc">>
/\ tmp = <<0, 0>>

State 5:
/\ x = 1
/\ pc = <<"Done", "Done">>
/\ tmp = <<0, 0>>

State 6: Stuttering
`

show all


What if `FinalIsTwo` isn’t what we want? Maybe we want a weaker property: we don’t care what the final answer is, as long as *all possible executions* get it. In that case us eventually get 1 might not be a problem, as long as all other executions get 1 too. This is called **Observational Determinism**, or OD. While the system may be internally nondeterministic, to an outsider observer it looks deterministic.


OD is a hypersafety property. You can’t provide a single timeline as a counterexample; for all we know, all the other timelines get the same `x` value. On the other hand, you can provide *two* traces as a counterexample, as long as they get different `x` values. Since the property is defined over pairs of behaviors, we say that OD is 2-safety.


### Specifying hyperproperties in TLA+


You can’t.


This is a fundamental limit of the language. A TLA+ spec describes whether a given sequence of states is a valid behavior for the system. There’s no way to step outside that frame and talk about the behavior itself. This isn’t something unique to TLA+: like all spec languages, it makes tradeoffs about what’s important to specify. Leslie Lamport’s [“Sometime” is Sometimes “Not Never”](https://www.microsoft.com/en-us/research/uploads/prod/2016/12/Sometime-is-Sometimes-Not-Never.pdf) covers a lot of the principles he later used in TLA+. These principles also happen to make natively expressing hyperproperties impossible.


We can still do this, we just need to cheat a little. TLA+ can only express properties about individual behaviors. We need to express 2-safety over pairs of behaviors. What we can do is write a new specification where each behavior of the new spec corresponds to a pair of behaviors in the old spec. Think of it as running two copies of the old spec and comparing their results. The 2-safety in the regular spec becomes 1-safety in the hyperspec.


### The Hyperspec


First the hyperspec, then the breakdown:


show spec
  
`EXTENDS Integers, TLC, Sequences

VARIABLES
  x1, pc1, tmp1 
 
VARIABLES 
  x2, pc2, tmp2

vars1 == <<x1, pc1, tmp1>>
vars2 == <<x2, pc2, tmp2>>

Thread1 == INSTANCE threads 
           WITH x <- x1,
                pc <- pc1, tmp <- tmp1

Thread2 == INSTANCE threads 
           WITH x <- x2,
                pc <- pc2, tmp <- tmp2
                
Init ==
  /\ Thread1!Init
  /\ Thread2!Init

Next ==
  /\ Thread1!Next 
  /\ Thread2!Next
     
Spec == Init /\ [][Next]_<<vars1, vars2>> 
      /\ WF_vars1(Thread1!Next) /\ WF_vars2(Thread2!Next)

Hypersafe == <>[](x1 = x2)
`

show all


```
EXTENDS Integers, TLC, Sequences

VARIABLES
  x1, pc1, tmp1 

VARIABLES 
  x2, pc2, tmp2

vars1 == <<x1, pc1, tmp1>>
vars2 == <<x2, pc2, tmp2>>

```


Each thread spec has three variables. Since we’re going to include two copies, we need a separate set of variables for each. `pc1` and `pc2` are for the `pc` bookkeeping variable you get when translating PlusCal to raw TLA+.


```
Thread1 == INSTANCE threads 
           WITH x <- x1,
                pc <- pc1, tmp <- tmp1

\* Threads2 etc

```


These are **instantiations** of the `threads` module. `Thread1` is effectively a namespace for all of the operators in `threads.tla`. Since `threads` has three variables, we need to **parameterize** the spec by saying which variables are described by its actions. That’s what the `WITH` does.2


In TLA+, modules are namespaced with `!`. For example:


```
\* Not part of the breakdown

Thread1!FinalIsTwo == <>[](x1 = 2)
Thread2!FinalIsTwo == <>[](x2 = 2)

```


All of the actions in `Thread1` are only defined over `<<x1, pc1, tmp1>>`. We’ll express the behavior of the hyperspec in terms of the behavior of `Thread1` and `Thread2`.


```
Init ==
  /\ Thread1!Init
  /\ Thread2!Init

Next ==
  /\ Thread1!Next 
  /\ Thread2!Next

```


Since the two sets of variables are disjoint, we don’t need to do anything special for `Init`. It’s just the initialization of the two `thread` modules.


Normally `Next` is where things get complicated. The next-state relation needs to describe how *all* variables change, and `Thread1!Next` doesn’t describe how any of the `Thread2` variables change. But we’re lucky here: `threads` is a weakly-fair, always terminating algorithm and the two instances don’t share any variables in common. In this *specific* case we can safely just run the two specs in parallel.


```
Spec == Init /\ [][Next]_<<vars1, vars2>> 
      /\ WF_vars1(Thread1!Next) /\ WF_vars2(Thread2!Next)

Hypersafe == <>[](x1 = x2)

```


The spec needs to be stutter-invariant on both `vars1` and `vars2`. The `WF` guarantees that neither instance is allowed to “crash”. Finally, `Hypersafe` is the hyperproperty we want to test. In the hyperspec it’s just a regular property and we can express it with TLA+.


Running the model gives us an error, as expected.


show error trace
  
`State 1:
/\ pc1 = <<"Get", "Get">>
/\ pc2 = <<"Get", "Get">>
/\ tmp1 = <<0, 0>>
/\ tmp2 = <<0, 0>>
/\ x1 = 0
/\ x2 = 0

State 2:
/\ pc1 = <<"Get", "Inc">>
/\ pc2 = <<"Get", "Inc">>
/\ tmp1 = <<0, 0>>
/\ tmp2 = <<0, 0>>
/\ x1 = 0
/\ x2 = 0

State 3:
/\ pc1 = <<"Inc", "Inc">>
/\ pc2 = <<"Get", "Done">>
/\ tmp1 = <<0, 0>>
/\ tmp2 = <<0, 0>>
/\ x1 = 0
/\ x2 = 1

State 4:
/\ pc1 = <<"Inc", "Done">>
/\ pc2 = <<"Inc", "Done">>
/\ tmp1 = <<0, 0>>
/\ tmp2 = <<1, 0>>
/\ x1 = 1
/\ x2 = 1

State 5:
/\ pc1 = <<"Done", "Done">>
/\ pc2 = <<"Done", "Done">>
/\ tmp1 = <<0, 0>>
/\ tmp2 = <<1, 0>>
/\ x1 = 1
/\ x2 = 2

State 6: Stuttering
`

show all


### Hyperproperties are hard


This particular style of hyperspec is called **self-composition** and works for any k-safety property. K-safety is only a subset of hypersafety, though, and general hypersafety leads to *much* more complicated hyperspecs. That’s the challenge with emulation: sure, you can sort of hack in what you need, but *maybe* you’re using the wrong tool for the job.


The right tool is a notation that can naturally represent the same concept as a 1-prop. Reachability is a hyperproperty in TLA+ but a regular (and trivially checkable) property in [CTL](https://en.m.wikipedia.org/wiki/Computation_tree_logic). Some hyperproperties are equivalent to probabilistic 1-properties, meaning you can use something like [PRISM](https://www.hillelwayne.com/post/prism/). In practice, model checkers strong enough to handle hyperproperties only work on very limited specifications. PRISM can say “we reach consensus at least 20% of the time”, but it can’t handle tuples or strings. Tradeoffs.


There are also some specialist notations designed for hyperproperties, such as [HyperLTL](https://arxiv.org/abs/1401.4492). HyperLTL is even more niche than the rest of formal methods. If I have any readers who would find HyperLTL immediately useful *and also* don’t already know about it then I’ll eat a hat.3


## Applications


### Hyperproperties in the Research


Almost all hyperproperty research is on security. Many interesting security properties are hyperproperties, which is one reason why they’re so hard to get right. Take **noninterference**. There are several different flavors of noninterference, but they all boil down to a more serious version of access control. If a system enforces access control, you can’t see “secret” resources. In a noninterfering system, you can’t *infer* anything about “secret” resources. Example: Alice sets their Facebook friend-list to “only me”. Bob is friends with Alice and Eve. If I go to “show friendship” between Alice and Eve, it will show Bob as a mutual friend. From that, I infer that Bob is on Alice’s friend list, even though I cannot see her friend list. This breaks noninterference. Satisfying noninterference here means showing that all behaviors with secret information have identical public information. That’s a hyperproperty.


SLAs like mean response time or uptime percentage are technically hyperproperties, but they’re usually studied as probabilistic 1-properties. Lots of papers namedrop SLAs as an example but nobody actually tries to specify an SLA as a hyperprop. I think it’s mostly there to show that hyperproperties exist outside of security.


### Hyperproperties in Industry


The only people who’ve used the formalism in industry is [Toyota](http://www.taylortjohnson.com/research/nguyen2017memocode.pdf), who did some proof-of concept work on verifying hardware. Other groups work with hyperproperties but don’t think of them in those terms. For example, the seL4 team proved their [OS is noninterfering](http://www.ssrg.nicta.com/publications/papers/Murray_MBGK_12.pdf) but only brought up that noninterference is hypersafety as an “oh hey that’s kinda neat” aside.


### Using Hyperproperties


While you’re not going to be formally verifying hyperproperties any time soon, I still think they’re very useful. It helps you think about systems in a different way. Once I learned about hyperproperties, I started seeing them everywhere:

- “Was this a correct optimization” and “Was this a safe refactoring” are hyperproperties. Do two codebases produce the same output for the same input? Does this produce the same output as it did ten commits ago?
- A logic puzzle is “cooked” if there’s two distinct solutions. This is a hyperproperty and you can use self-composition to make sure logic puzzles have a unique solution. Pretty handy if you’re [inventing your own](https://gist.github.com/hwayne/23cf70e209abb8a7bc45541038ccf52f).
- Partial degradation of a system. “The system works even if one server goes down” is a one property. “The system degrades by at most X if one server goes down” is a hyperproperty. Similarly, “Two malicious nodes cannot do more damage than one malicious node”.


Hyperproperties also give us better intuition about verifying code. The majority of verification falls into the [triad of contracts, types, and tests](https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/). Types and contracts are very good at capturing behavior of the individual function calls (“this is positive”), but not relationships between function calls (“this is associative”). Tests are much better at capturing relations between function calls. This looks just like raising a spec to a hyperspec! The test can run the function several times, just as hyperspec can run the spec several times. I also suspect that hyperproperties can be more “generic” than regular properties, which might explain why most [property-based testing tactics](https://fsharpforfunandprofit.com/posts/property-based-testing-2/) involve hyperproperties.


See also [metamorphic relations](https://www.hillelwayne.com/post/metamorphic-testing/), another angle on the same topic with a lot of success stories behind it. Arguably metamorphic relations are a subset of hyperproperties.


## Additional Resources

- [Hyperproperties](https://www.cs.cornell.edu/fbs/publications/Hyperproperties.pdf): The source that formalized hyperproperties.
- [Hyperproperties (slides)](http://www.cs.cornell.edu/courses/cs5430/2016sp/l/27-hyperproperties/lec.pdf) A slightly more accessible introduction to the idea.
- [Verifying Hyperliveness](https://link.springer.com/chapter/10.1007/978-3-030-25540-4_7): Some of the challenges of both expressing and checking hyperliveness. Much more math-heavy than the other two.


---

1. This shouldn’t be surprising. Liveness is more complex than safety, too.
 [return]
2. “Why can’t TLA+ just automatically include the variables when you import?” Because that would make `INSTANCE` too weak. We couldn’t then have two instances share a variable (shared state), or parameterize a variable with an expression (refinement).
 [return]
3. Someone else’s hat.
 [return]
