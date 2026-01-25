---
title: "Teaching Leaky Abstractions"
date: 2018-01-30
url: https://www.hillelwayne.com/post/teaching-leaky-abstractions/
slug: teaching-leaky-abstractions
word_count: 1106
---

I’m writing a book on TLA+! It’s going to be aimed at the same audience as [Learn TLA+](https://learntla.com), but dive much deeper and go much further. I’ll be showing not just how to use TLA+, but how to think about systems, write good specifications, and fix models. I’m really excited and I’m sure you’ll be, too!


I’m also trying to make it much better than *Learn TLA+*, because

1. People are going to be paying money for this, so I can’t just phone it in
2. I asked my technical reviewer to be “almost-comically brutal” and he’s risen to the challenge.1


This means a lot more obsessing over pedagogy, which means I’m now going to rant to you about pedagogy.


### Leaky Abstractions


TLA+ is a mathematical formalism, which makes it both extremely powerful and cumbersome. Here’s how you update a field `f` on structure `struct` to a new value:


```
struct' = [struct EXCEPT !.f = newvalue]

```


In 2009, Lamport introduced *PlusCal*, which is a DSL that compiles to TLA+. It looks like pseudocode, and you’d write the exact same thing like


```
struct.f := newvalue;

```


*Much* better. I prefer to teach PlusCal instead of pure TLA+ for a few reasons. First of all, it’s easier for most programmers to start with. Second, you’re still learning most of TLA+: PlusCal only abstracts away setting and updating values, which happens to be the most convoluted part of TLA+. It’s only a short hop to learning that bit once you know everything else. Finally, it’s really good for modeling Communicating Sequential Processes (CSP) style-concurrency, which nicely fits a lot of practical problems.


What I do is do some stuff in PlusCal, then teach a bit of TLA+ that’s immediately useful. Then more PlusCal etc, keeping the TLA+ continually useful to the reader. I find this works really well. The problem is there’s some cases where you need to know A and B to understand C, except *A and B aren’t useful in PlusCal*. I don’t want to sledgehammer the reader with information that only makes sense much later.


In some cases, I can just leave C out.2 But there are also cases where C is worth knowing. One case that’s been on my mind is with invariants. It’s easy to write the invariant “x is less than 10”. But how about the invariant “x never decreases”? In TLA+, it’s easy: `[][x' >= x]_x`. “For all states, EITHER the next-state value of x is geq to the current value of x OR x does not change at all.” But now I have to explain what `[][foo]_bar` means, what `x'` means and what a stutter state is! None of these are needed to write Pluscal, and that’s a normally good thing. But it’s biting us in the butt right now.


This is doable in PlusCal without knowing any of that, but it’s really janky and I don’t like janky. First, we define a new variable `x_last`. Then instead of doing `x := foo`, we add a macro


```
macro set_x_to(val) begin
  x_last := x;
  x := val;
end macro;

```


Finally, we specify the invariant as `x >= x_last`. This works, but it has two major problems.

1. `x_last` has no meaning in the specification. We’ve added another variable to track solely to help with the bookkeeping.
2. We have to make sure that we don’t do a naked assign to `x`, since we *must* assign through `set_x_to`.


But it works!3 So let’s push it further. What if the invariant is “if y is true, x never decreases”? We’d try to update our invariant to `y => x >= x_last`, but this will throw false positives. Consider the case where `x_last = 2` and `x = 1`, then you flip y to true without updating x. You get `TRUE => 1 >= 2`, which fails. But x didn’t decrease while y was true! `x_last` doesn’t represent the change in x at any given step, just what it was before the last change.


The ‘simplest’ workaround here is to add a model value `NULL` and the macro


```
macro set_y_to(val) begin
  x_last := NULL
  y := val
end macro;

```


Then we rewrite the invariant as `y /\ (x_last /= NULL) => x >= x_last`. We’ve added yet another accounting value and can’t naked-assign y anymore. We make things cumbersome **or** we could write `[][y => x' >= x]_x`. No bookkeeping needed at all.4 Either we use a shitty workaround or we bite the bullet and teach a bunch of inapplicable concepts to get to the good stuff.


Or maybe there’s a third way? While all these concepts are unnecessary in Pluscal, I can find ways to *make* them useful. Then I can teach them all in small pieces throughout the book. If this kind of problem ever comes up, I’d be able to synthesize them without needing to infodump.

- **Temporal operators** are easy: I’m already writing a chapter on them. It may not cover `[][]_`, but the reader will already have a basis.
- **Stuttering** is a little trickier, but I figured out a natural place. I can introduce it in the context of simulating crashes, since “this server stopped handling data” is represented as “the server process is stuttering.”
- **Primed variables** are the hardest one, and I was stuck on this for a while. But I think I’ve got it: you can use primed variables in debugging error traces. I can say “if you’re debugging, you can write x for the value of x when the step started, and x’ for the value when the step ended”.


At that point, if necessary I can synthesize them in a couple paragraphs instead of over several pages. I don’t know if this will work, but I’m pretty hopeful about it. We’ll see what the reviewer thinks.


Teaching is hard!!!


---

1. Five points if I scrap a chapter and start over, 15 if his feedback makes me cry.
 [return]
2. Still in the starting stages of the book, though, and over rounds of revision C might get back into the book.
 [return]
3. You can argue that the abstraction double-leaks here, because there are valid cases where you’d want to do it Pluscal style! Invariants with temporal operators like `[][]_` can’t be multithreaded, so adding an accounting variable might make model-checking faster.
 [return]
4. This doesn’t mean that TLA+ *never* needs bookkeeping stuff. Imagine if the invariant was “if y is true, x cannot decrease *as of two states later*”. For this particular case, the proper TLA+ solution is “try not to need that invariant.”
 [return]
