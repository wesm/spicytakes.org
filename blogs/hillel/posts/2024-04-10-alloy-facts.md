---
title: "Don't let Alloy facts make your specs a fiction"
date: 2024-04-10
url: https://www.hillelwayne.com/post/alloy-facts/
slug: alloy-facts
word_count: 1287
---

I’ve recently done a lot of work in [Alloy](https://alloytools.org/) and it’s got me thinking about a common specification pitfall. Everything in the main post applies to all formal specifications, everything in dropdowns is for experienced Alloy users.


---


Consider a simple model of a dependency tree. We have a set of top-level dependencies for our program, which have their own dependencies, etc. We can model it this way in Alloy:


```
sig Package {
  , depends_on: set Package
}

run {some depends_on}

```


Show Alloy tip
  
I’m going to use a slightly different model for the next example:
`abstract sig Package {
  , depends_on: set Package
}

lone sig A, B extends Package {}

run {some depends_on}
`
I do things this way because it gives visualizations with `A` and `B` instead of `Package$0` and `Package$1`. Alloy has built-in enums but they don’t play nice with the rest of the language (you can’t extend them or give them fields).

show all


If we look through some of the generated examples, we see something odd: a package can depend on itself!


These kinds of nonsensical situations arise often when we’re specifying, because we have an *intent* of what the system should be but don’t explicitly encode it. When this happens, we need to add additional constraints to prevent it. For this reason, Alloy has a special “fact” keyword:1


```
fact no_self_deps {
    all p: Package {
       p not in p.depends_on 
    }
}

```


Show Alloy tip
  
You can write the same fact purely relationally:
`fact {
    no depends_on & iden
}
`
In general, the model checker evaluates purely-relational expressions *much* faster than quantified expressions. This can make a big difference in large models!

show all


Alloy will not generate any models that violate a fact, nor will it look for invariant violations in them. It’s a “fact of reality” and doesn’t need to be explored at all.


## The pitfall of facts


“No self-deps” is a great example of a fact. It’s also an example of a terrible fact. Beginners often make this mistake where they use facts to *model* the system, which quickly leads to problems.


Consider the real system for a second, not the spec. Where do the package manager dependencies come from? Usually a plain text file like `package.json` or `Cargo.toml`. What if someone puts manually a self-dependency in that file? Presumably, you want the package manager to detect the self-dep and reject the input as an error. How do you know the error-handling works? By having the checker verify that it accepts valid manifests and rejects ones with self-loops.


Except it can’t test the rejection because we told it not to generate any self-dependencies. Our fact made the self-deps *unrepresentable*.


Normally in programming languages, “making illegal states unrepresentable” (MISU) is a *good* thing ([1](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/) [2](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) [3](https://www.hillelwayne.com/post/constructive/) [4](https://corrode.dev/blog/illegal-state/)). But specification covers both the software you are writing and the environment the software is running in, [the machine and the world](https://www.hillelwayne.com/post/world-vs-machine/). If you cannot represent the illegal state, you cannot represent the world *creating* an illegal state that your software needs to handle.


Show Alloy tip
  
There is a technique to make invalid states representable in the world *but not in the machine*: [refinement](https://www.hillelwayne.com/post/refinement/). The link goes to a TLA+ explanation but the same principle works in Alloy too: write an abstract spec without MISU, write an implementation spec with it, then show that the implementation refines the abstract spec. But you’ll do this with signatures and predicates, not with facts.

show all


Instead of facts, you want predicates. Then you can test for the predicate being true or check that it’s necessary to get other properties. Make the constraint explicit instead of implicit.


```
// instead of

fact no_self_deps {/*body*/}

run {some_case}
check {some_property}

// do

pred no_cycles {/*body*/}

run {
  no_cycles and some_case
}

check {no_cycles implies some_property}

```


Predicates have the additional benefit of being “locally scoped”: if you have three facts and want to check a model with only two of them, you have to comment the third fact out.


## When to use facts


So where *should* we use facts? When does it make sense to universally enforce constraints, when doing so could potentially weaken our model?


First, facts are useful for narrowing the scope of a problem. “No self-deps” is a perfectly reasonable fact **if** we’re only specifying the package installer and something else is responsible for validating the manifests. Writing the as a fact makes it clear to the reader that we’re not supposed to validate the manifest. This means we don’t make any guarantees if the assumption is false.


Second, facts rule out *fundamentally uninteresting* cases. Say I’m modeling linked lists:


```
sig Node {
  next: lone Node //lone: 0 or 1
}

```


This generates regular lists and lists with cycles, which are interesting to me. I don’t want to constrain away either case. But it *also* generates models with two disjoint lists. If I only care about single linked lists, I can eliminate extra lists with a fact:


```
fact one_list {
    some root: Node | root.*next = Node
}

```


Show Alloy tip
  
`one_list` also rules out “two link lists that merge into one”. If that’s something you want to keep, use the [graph](https://alloy.readthedocs.io/en/latest/modules/graph.html) module:
`open util/graph[Node]

fact {
    weaklyConnected[next]
}
`

show all


Similarly, you can use facts to eliminate extraneous detail. If I’m modeling users and groups, I don’t want any empty groups. I’d add a fact like `Users.groups = Group`.


Third, you can use constraints to optimize a slow model. This is usually through [symmetry breaking](https://en.wikipedia.org/wiki/Symmetry-breaking_constraints).


Finally, you can use facts to define necessary relationships that Alloy can’t can’t express natively. In the project I worked on, we had Red and Blue nodes in our graph. Red nodes had *at least one* edge to another node, Blue nodes had *at most one*. We wrote this as


```
abstract sig Node {
}

sig Red extends Node {
  edge: some Node
}

sig Blue extends Node {
  edge: lone Node
}

```


But then we couldn’t write generic predicates on nodes that use `edge`, because Alloy treated it as a type error. Instead we wrote it with a fact:


```
abstract sig Node {
  edge: set Node
}

sig Blue, Red extends Node {}

fact {
  all r: Red  | some r.edge
  all r: Blue | lone r.edge
}

```


Show Alloy tip
  
Okay, one more (rather niche) use case. Say you have a temporal model and a canonical `spec` predicate for system behavior. Then a lot of your assertions look like
`module main

// spec

check {spec => always (prop1)}
check {spec => always (prop2)}

// etc
`
You can clean this up a lot by exporting all of properties to `properties.als` and writing it like this:
`open main

fact {spec}

check {always (prop1)}
check {always (prop2)}
// etc
`

show all


## Conclusion


Constraints are dangerous because you need error states in order to check that your program avoids error states.


If you’re interested in learning more about Alloy, there’s a good book [here](https://alloytools.org/book.html) and [I maintain some reference documentation](https://alloy.readthedocs.io/en/latest/). I’m also working on a new Alloy workshop. I ran an alpha test last month and plan to run a beta test later this summer. Sign up for [my newsletter](https://buttondown.email/hillelwayne/) to stay updated!


*Thanks for [Jay Parlar](https://twitter.com/parlar) and [Lorin Hochstein](http://lorinhochstein.org/) for feedback. If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*


---

1. In other specification languages this is usually either a runtime constraint (like in [TLA+](https://learntla.com/topics/toolbox.html#additional-spec-options)) or a direct modification to the system spec itself. 
 [return]
