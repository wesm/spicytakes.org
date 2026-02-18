---
title: "Why are monoidal categories interesting?"
date: 2019-03-26
url: https://jvns.ca/blog/2019/03/26/what-are-monoidal-categories/
slug: what-are-monoidal-categories
word_count: 1287
---


Hello! Someone on Twitter asked a question about tensor categories recently and I remembered “oh,
I know something about that!! These are a cool thing!”. Monoidal categories are also called “tensor
categories” and I think that term feels a little more concrete: one of the biggest examples of a
tensor category is the category of vector spaces with the tensor product as the way you combine
vectors / functions. “Monoidal” means “has an associative binary operation with an identity”, and with
vector spaces the tensor product is the “associative binary operation” it’s referring to. So I’m
going to mostly use “tensor categories” in this post instead.


So here’s a quick stab at explaining why tensor categories are cool. I’m going to make a lot of
oversimplifications which I figure is better than trying to explain category theory from the ground
up. I’m not a category theorist (though I spent 2 years in grad school doing a bunch of category
theory) and I will almost certainly say wrong things about category theory.


In this post I’m going to try to talk about [Seven Sketches in Compositionality: An Invitation to
Applied Category Theory](https://arxiv.org/pdf/1803.05316.pdf) using mostly plain English.


## tensor categories aren’t monads


If you have been around functional programming for a bit, you might see the word “monoid” and
“categories” and wonder “oh, is julia writing about monads, like in Haskell”? I am not!!


There is a sentence “monads are a monoid in the category of endofunctors” which includes both the
word “monoid” and “category” but that is not what I am talking about at all. We’re not going to talk
about types or Haskell or monads or anything.


### tensor categories are about proving (or defining) things with pictures


Here’s what I think is a really nice example from this [“seven sketches in compositionality”](([https://arxiv.org/pdf/1803.05316.pdf](https://arxiv.org/pdf/1803.05316.pdf)) PDF (on
page 47):


![](https://jvns.ca/images/monoidal-preorder.png)


The idea here is that you have 3 inequalities

1. `t <= v + w`
2. `w + u <= x + z`
3. `v + x <= y`,


and you want to prove that `t + u <= y + z`.


You can do this algebraically pretty easily.


But in this diagram they’ve done something really different! They’ve sort of drawn the inequalities
as boxes with lines coming out of them for each variable, and then you can see that you end up with
a `t` and a `u` on the left and a `y` and a `z` on the right, and so maybe that means that `t + u <= y + z`.


The first time I saw something like this in a math class I felt like – what? what is happening? you
can’t just draw PICTURES to prove things?!! And of course you can’t *just* draw pictures to prove
things.


What’s actually happening in pictures like this is that when you put 2 things next to each other in
the picture (like `t` and `u`), that actually represents the “tensor product” of `t` and `u`. In
this case the “tensor product” is defined to be addition. And the tensor product (addition in this case) has
some special properties –

1. it’s associative
2. if `a <= b` and `c <= d` then `a + c <= b + d`


so saying that this picture proves that `t + u <= y + z` **actually** means that you can read a
proof off the diagram in a straightforward way:


```
      t    + u 
<= (v + w) + u 
=  v + (w + u) 
<= v + (x + z) 
=  (v + x) + z 
<=   y     + z

```


So all the things that “look like they would work” according to the picture actually do work in
practice because our tensor product thing is associative and because addition works nicely with the
`<=` relationship. The book explains all this in a lot more detail.


## draw vector spaces with “string diagrams”


Proving this simple inequality is kind of boring though! We want to do something more interesting,
so let’s talk about vector spaces! Here’s a diagram that includes some vector spaces (U1, U2, V1, V2)
and some functions (f,g) between them.


![](https://jvns.ca/images/tensor-vector.png)


Again, here what it means to have U1 stacked on top of U2 is that we’re taking a tensor product of
U1 and U2. And the tensor product is associative, so there’s no ambiguity if we stack 3 or 4 vector
spaces together!


This is all explained in a lot more detail in this nice blog post called [introduction to string diagrams](https://qchu.wordpress.com/2012/11/05/introduction-to-string-diagrams/) (which I took that picture from).


## define the trace of a matrix with a picture


So far this is pretty boring! But in a [follow up blog
post](https://qchu.wordpress.com/2012/11/06/string-diagrams-duality-and-trace/), they talk about
something more outrageous: you can (using vector space duality) take the lines in one of these diagrams and move them
**backwards** and make loops. So that lets us define the trace of a function `f : V -> V` like this:


![](https://jvns.ca/images/trace.png)


This is a really outrageous thing! We’ve said, hey, we have a function and we want to get a number
in return right? Okay, let’s just… draw a circle around it so that there are no lines left coming
out of it, and then that will be a number! That seems a lot more natural and prettier than the usual
way of defining the trace of a matrix (“sum up the numbers on the diagonal”)!


When I first saw this I thought it was super cool that just drawing a circle is actually a
legitimate way of defining a mathematical concept!


## how are tensor category diagrams different from regular category theory diagrams?


If you see “tensor categories let you prove things with pictures” you might think “well, the whole
point of category theory is to prove things with pictures, so what?”. I think there are a few things
that are different in tensor category diagrams:

1. with string diagrams, the lines are objects and the boxes are functions which is the opposite of
how usual category theory diagrams are
2. putting things next to each other in the diagram has a specific meaning (“take the tensor product
of those 2 things”) where as in usual category theory diagrams it doesn’t. being able to combine
things in this way is powerful!
3. half circles have a specific meaning (“take the dual”)
4. you can use specific elements of a vector space in a diagram which usually you wouldn’t do
in a category theory diagram (the objects would be the whole vector space, not one element of
that vector space)


## what does this have to do with programming?


Even though this is usually a programming blog I don’t know whether this particular thing really has
anything to do with programming, I just remembered I thought it was cool.
I wrote my [master’s
thesis](https://github.com/jvns/masters-thesis/raw/master/thesis.pdf) (which i will link to even
though it’s not very readable) on topological quantum computing which involves a bunch of monoidal
categories.


Some of the diagrams in this post are sort of why I got interested in that area in the first place
– I thought it was really cool that you could formally define / prove things with pictures. And
useful things, like the trace of a matrix!


## edit: some ways this might be related to programming


Someone pointed me to a couple of twitter threads (coincidentally from this week!!) that relate
tensor categories & diagrammatic methods to programming:

1. [this thread from @KenScambler](https://twitter.com/KenScambler/status/1108738366529400832) (“My best kept secret* is that string & wiring diagrams–plucked straight out of applied category theory–are *fabulous* for software and system design.)
2. [this other thread by him of 31 interesting related things to this topic](https://twitter.com/KenScambler/status/1109474342822244353)
