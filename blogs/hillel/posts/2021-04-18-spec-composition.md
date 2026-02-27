---
title: "Why Specifications Don't Compose"
date: 2021-04-18
url: https://www.hillelwayne.com/post/spec-composition/
slug: spec-composition
word_count: 2982
---

Recently my friend [Lars Hupel](https://lars.hupel.info/) and I had a discussion on why formal methods don’t compose well. You can read the conversation [here](https://lars.hupel.info/articles/tweetcast-verification/). We focused mostly on composing formally-verified code. I want to talk a little more about the difficulties in composing *specifications*. This is half because it’s difficult for interesting reasons and half because it’s a common question from beginners.


Beginners to formal specification expect specifications should be organized like programs: multiple independent modules that interact through public interfaces, where the modules don’t know about each others’ private implementations. This is more legible and reusable than a single giant program. We can test the individual modules and then only need to worry about how they combine. By contrast, most specifications are written as single global specs, with subcomponents rewritten from scratch per spec. Why can’t we make our specs as composable as programs?


## Setup


### Specs are Math


Specifications are mathematical expressions, usually a branch of logic. We use math to specify because it is precise, unambiguous, and expressive. The specification represents a system and its possible behaviors. Specifications have **properties**, statements that are true of all behaviors of the system. In many cases, we start out  knowing the properties we want our system to have, and *then* write the specification to satisfy them.


I’ll define **composing** two specifications as joining them in a way that preserves all properties of both specs, *without* requiring us to “dig in” to either spec. A good intuition here is function composition: if `f(x)` has type signature `a -> b` and `g(x)` has type signature `b -> c`, then `g . f = g(f(x))` has type signature `a -> c`. We know that `g . f` preserves type safety without knowing anything about the internals of either function, just the top-level type signatures. Preferably, composing specs should work the same way: we don’t need to change the internals of either spec to combine the two.


Even without “perfect” composition, we can have a “spectrum” of composability. Let’s say a spec consists of three “components”. If we only need to change one component to combine it with another spec, it’s “more” composable than if we needed to change two components. This is more in line with how we think about composing programs. We might need to modify the interface or write a wrapper around the imports, but the internal implementation of each module stays the same.


### Linear Temporal Logic


Let’s write our specifications in **Linear Temporal Logic**. In “normal” logic, the statement `x` means that x is true. In temporal logic, `x` means that x is true *in the initial state.* In future states, x doesn’t need to be true. To describe how the system evolves, we add three **temporal operators**:

- Ne**X**t (◯): `◯x` means that x is true *in the next state*.
- **F**inal (◇): `◇x` means that x is true *in some future state*.
- **G**lobal (□): `□x` means that x is true *in all future states*.1


Technical Stuff
  
“Future states” includes the current state. `◇x` is true if `x` is true in *this* state or a later state.

show all


In all cases, I’ll write “x is true” as `x` and “x is false” as `!x`. All variables are booleans.


Let’s give an example. `x && ◯!x` means that x is true in the initial state and false in the next state. `x && ◯(!x && ◯□x)` means that x is initially true, then in the next state x is false, and permanently true in the state after.


Breakdown
  

In the initial state, x is true
In the next state:


x is false
in the next state:


in all future states x is true.




show all


We could also have written `x && ◯!x && ◯◯□x`, which would mean the same thing. `◯` distributes over both `&&` and `||`, while `□` only distributes over `&&` and `◇` over `||`.


### Our Example Spec


For the purposes of this discussion, we’ll use a “blinker”:

1. `x` starts as true or false
2. In the next state, `x` flips from true to false or false to true
3. This repeats infinitely.


Here’s the spec:


```
InitX = x || !x
BlinkX = (x => ◯!x) && (!x => ◯x)

SpecX = InitX && □BlinkX

```


Technical Stuff
  

`P => Q` means that if P is true, then Q is true. So `(x => ◯!x)` means that if `x` is true now, then in the next state, `x` is not true.
`SpecX` is also a boolean formula. This lets us pick any arbitrary program behavior and ask if `SpecX` is true for it, ie `SpecX` is an accurate description of its behavior. It also means we can manipulate it like any other logical statement.


show all


This has exactly two valid behaviors:


```
x; !x; x; !x; ...
!x; x; !x; x; ...

```


One of the properties of this spec is that x is always either true or false, never any other value.2


```
TypeInvariantX = □(x || !x) 
SpecX => TypeInvariantX

```


`SpecX => TypeInvariantX` means that if `SpecX` is true of a system– that is, `SpecX` is an accurate description of its behavior– then `TypeInvariantX` is also true of the system. In other words, any system satisfying `SpecX` also has property `TypeInvariantX`.


## Composing `SpecX`


We’ll define an analogous specification `SpecY`, which is identical except it describes a different variable.3 We want to now model a system with *two* blinkers. The “obvious” way to do that is to compose `SpecX` and `SpecY`, rather than start from scratch. How bad could it be?


Let’s start by saying both are true:


```
Spec = SpecX && SpecY

```


This will guarantee that all properties of both specs are satisfied. There are exactly four valid behaviors:


```
x, y   ; !x, !y ; x, y   ...
x, !y  ; !x, y  ; x, !y  ...
!x, y  ; x, !y  ; !x, y  ...
!x, !y ; x, y   ; !x, !y ...

```


The two blinkers are always synchronous. One can’t run faster than the other, or consistently blink slightly earlier than the other, etc. This is rarely what we want when we compose specs; consider composing a heartbeat protocol with a general worker process. One *should* run more often than the other.


Technical Stuff
  
We can formally express this with a **reachability** property: that it’s always *possible* to reach a given state from any other state. Since there’s no way to reach `x && !y` from the starting state `x && y`, our system doesn’t satisfy the reachability property `R(x && !y)`.
LTL **cannot** formally express reachability properties. This is a price it pays to make other (arguably more useful) properties expressible.

show all


We want to instead say that one *or* the other can run. We could try writing this:


```
Spec = SpecX || SpecY

```


But this isn’t actually what we want either. This would also make one of the initial predicates optional: we want both of them to be *true*. We only want to `||` the `Blink` predicates. We’ve already lost simple composition, since we need to break the `Spec` predicates down into their subcomponents. That way we can write


```
Spec = (InitX && InitY) && □(BlinkX || BlinkY)

```


This still looks like “partial” composition, as long as our specs are of the form `Init && □P`. But to actually *be* composition, it should also preserve the properties of the local specs.


### Breaking Properties


One of the properties of `SpecX` is `TypeInvariantX`, which is that `□(x || !x)`. Does `Spec` also satisfy `TypeInvariantX`?


Nope. The following is a valid behavior of `Spec`:


```
x, y; x, !y; x="paprika", y; ...

```


The step between `x` to `x="paprika"` isn’t a valid under `BlinkX`, so wasn’t a valid step for `SpecX`. But `Spec` instead has `□(BlinkX || BlinkY)`, and `BlinkX` can be *false* if `BlinkY` is true. This is called the **frame problem**. Since `BlinkY` doesn’t have `x` in its “frame”, it doesn’t restrict `x` to sensible values.


What we need to say is that if `BlinkY` happens, `x` is unchanged:


```
SameX = (x => ◯x) && (!x => ◯!x)

Spec = InitX
Spec = (InitX && InitY) 
       && □((BlinkX && SameY)
          ||(BlinkY && SameX))

```


We’ve now excluded *both* `BlinkX` and `BlinkY` from happening; the two blinkers cannot synchronize. Let’s leave that aside for now to focus on a different problem. In our original spec, we knew that there was at least one point where x was true and at least one point where x was false. These kinds of properties, that the system is guaranteed to *eventually* do something we want, are called **liveness** properties.


```
LivenessX = ◇x && ◇!x

```


This is satisfied by `SpecX`. But in `Spec`, the following is a valid behavior:


```
x, y; x, !y; x, y; x, !y; ...

```


The problem is that we could only do “one thing” in `SpecX`, while in `Spec` we can do one of two things. If we keep choosing `BlinkY` *ad infinitum*, `BlinkX` never happens and `x` never changes. We say here that `BlinkX` is **unfair**: even if it *can* happen, it isn’t guaranteed *to* happen. I cover fairness in much more detail [here](https://www.hillelwayne.com/post/fairness/).


We can work around this by saying “BlinkX happens an infinite number of times”, aka “BlinkX always happens at least one point in the future:”


```
Spec = (InitX && InitY) 
       && □((BlinkX && SameY)
          ||(BlinkY && SameX))
       && □◇BlinkX && □◇BlinkY

```


Technical Stuff
  
To explain in a bit more detail: `□◇BlinkX` says that `◇BlinkX` is *always* true. So once `BlinkX` happens, `◇BlinkX` is *still always true*, meaning `BlinkX` must happen in the future again. So we have `BlinkX` an infinite number of times.
This isn’t an accurate representation of fairness, because it lacks conditionality. If something is *preventing* `BlinkX` from happening, we shouldn’t require it to happen infinitely often. I cover this in more detail in the [fairness post](https://www.hillelwayne.com/post/fairness/).

show all


Do we now have property composability? Does `Spec` guarantee everything `SpecX` does? Well, no. Here’s a property of `SpecX`:


```
BlinksTF = x => ◯!x

```


If `x` is true, it will be false *in the next state*. Since `Spec` is asynchronous, we can have two steps in a row where `x` is true.


Bummer.


### Stuttering


We hit a wall. `SpecX` requires x to change *every step*, while `Spec` only requires it to change for *some* steps. Properties that use `◯` will break. There is no way around this. It is a fundamental problem with allowing composed specifications to run at different rates.


Would composition be easier if we *forbid* `◯` properties? We can do this by introducing **stuttering**: steps where nothing changes. We say a spec is **stutter-invariant** if we can insert a stutter step anywhere in the behavior without breaking the spec. Rewriting `SpecX` to be stutter-invariant:


```
SpecX = InitX && □(BlinkX || SameX)

```


As a simplification, I’ll borrow TLA+’s box notation: `[P]_x` is equivalent to “P or stutter”, aka `P || UNCHANGED x`.


```
SpecX = InitX && □[BlinkX]_x

```


We now can’t have any `◯` properties. Any property about how the values change can be immediately foiled by stuttering, aka not changing the values. Further, specs are now *unfair* by default. `BlinkX` isn’t guaranteed to happen because we could just stutter an infinite number of times. We’d have to add that to the spec, too:


```
SpecX = InitX && □[BlinkX]_x && □◇BlinkX

```


This pushes questions of fairness from the *composed* specification to the *individual* specification. This gives us some compositionality back. Writing `SpecX && SpecY` carries each local spec’s fairness properties with it; if the individual spec is fair then so is the composed spec.


This *also* allows each spec to have a “flow of time”. Here’s some new behaviors of `SpecX` with stutter-steps:


```
x;  ; !x;  ; x;  ; !x
x;  ;  ; !x;  ;  ; x

x; !x;  ;  ;  ;  ; x

```


With the stutter steps, we can say the first two behaviors represent the blinker running at different rates and the third behavior represents a blinker that lags out a bit. That naturally gives us different specifications with different time flows. The slower spec just stutters more.


Once we make both `SpecX` and `SpecY` stutter-invariant, here’s how we can write `Spec`:


```
Spec = SpecX && SpecY

```


Derivation Notes
  
Is this equivalent to our old `Spec`? Yes, given two things:

By our definition of stutter-invariance, `BlinkX <=> !StutterX`
By the rules of modal logic, `□(A && B) = □A && □B`

Proving the two are equivalent is left as an exercise to the reader.

show all


We’ve gotten composability back! This even allows both sync *and* async blinkers. We just had to lose boundedness properties and significantly restrict our expressiveness. Hooray!


## Dependent Specs


As a rule, we can compose any number of stutter-invariant specs together and preserve all their individual properties… as long as they’re *independent* specs. The blinkers didn’t share any variables. Most of the time we want to compose specs that share some state, like a reader spec and writer spec that share a queue. This makes composition significantly more difficult.


Let’s take our blinker specs and add a flag. We’ll also have the two specs interact with it in different ways. `SpecX` will flip it on when it’s off, while `SpecY` will flip it off when it’s on.


```
On(f) = !f && ◯f
Off(f) = f && ◯!f

InitX(f) = (x || !x) && (f || !f)
InitY(f) = (y || !y) && (f || !f)

NextX(f) = BlinkX && (On(f) || (f && ◯f))
NextY(f) = BlinkY && (Off(f) || (!f && ◯!f))

SpecX(f) = InitX(f) && □[NextX(f)]_fx
SpecY(f) = InitY(f) && □[NextY(f)]_fy

```


Some important nuances:

1. We’ve parameterized `SpecX` on `f`: `f` is now a variable we can *pass into* the behavior. If we pass `f` into both specs, they’ll share the variable.4 Think of it as pass by reference, not pass by parameter.
2. We have to make sure that `f` is fully defined on every step of `NextX`, otherwise we can set `f="paprika"`. When writing specs we need to define the next state of *every* variable for every step.
3. The stutter-step includes both variables. Either `NextX(f)` is true or *neither* change.


Now we compose them together and pass in the same variable to each.


```
Spec == SpecX(z) && SpecY(z)

```


Let’s say our initial state is `!x, !y, !z`. What happens when we blink `x`?

1. Both `[NextX(z)]_zx` and `[NextY(z)]_zy` need to be true. To blink `x`, `NextX(z)` is true (we don’t stutter).
2. Since `z` started out false and `NextX(z)` is true, `On(z)` is true and we have `◯z`.
3. For `NextY(z)` to be true, we must have `◯!z`. But by (2) we have `◯z`, so `NextY(z)` is false.
4. This means that for `[NextY(z)]_zy` to be true, we need to stutter: `y` and `z` are unchanged.
5. But (2) changes `z`. If `NextX(z)` is true, then `z` must change *and* `z` must not change.
6. `NextX(z)` can never happen. QED


By sharing a flag between the two specs, we have *permanently disabled* one of them. The problem is that each spec needs to totally describe the behavior of all its component variables, meaning the composed spec can only make changes that are compatible with all of them.


This is even a *well-behaved* dependent spec, since the trouble is localized to the shared variable. You can imagine a `SpecY` where the value of *y* is what “blocks” `NextY` and forces stuttering. Then even though `SpecX` would change `z` in a way that’s compatible with `NextY`, `SpecY` stutters and forces `z` to stay unchanged. We’d have a deadlock.


Ultimately we have to give up on automatic composition and go back to manually stitching the specs together.


```
Next = (NextX(z) && Same(y)) || (NextY(z) && Same(x))
Spec = InitX && InitY && □[Next]_xyz

```


This also forces the specs always to be async and requires us to manually write out fairness requirements again, but at least it *works*.


## Discussion


Composing specs is hard because specifications need to totally describe how their variables change, and component specs don’t know about each other’s variables. If they do, they likely want to change it in incompatible ways. We can work around this by manually integrating the specs together, but then we’re not *composing* the specs, since we need to examine the internals of each spec to do so. This doesn’t mean combining specs needs to be intrinsically *hard*: we can come up with new techniques to help stitch them together. But it means that there’s a predilection in the communities to write large global specs, not combine smaller ones.


*Thanks to [Andrew Helwer](https://ahelwer.ca/), [Jay Parlar](https://twitter.com/parlar), and [Liz Denhup](https://www.linkedin.com/in/elizabeth-denhup/) for feedback.*


---

1. The “Final” and “Global” terms are more generally called “Sometimes” and “Always”. All temporal logics are **modal** logics, which is where the ◇ and □ symbols come from. ◯, as far as I can tell, is unique to LTL.
 [return]
2. I know I said that all variables here are booleans, but that’s just a convention I’m following here. There’s nothing *stopping* me from also including numbers and strings in my specs, I’m just not right now. This’ll become more important later.
 [return]
3. I could have made `InitX` and `BlinkX` take arguments and then write `Spec(y)` instead of `SpecY`. This is standard practice when specifying, but I hardcoded both specs to simplify the explanation. We will incorporate parameterization in a later section.
 [return]
4. How do we know that we’re passing in a variable and not a constant or value? In practice, we explicitly declare the variables in our spec.  The file for `SpecX` might look something like `VARS x, f; SpecX(f)`.
 [return]
