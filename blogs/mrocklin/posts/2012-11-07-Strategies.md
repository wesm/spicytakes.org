---
title: "Strategies"
date: 2012-11-07
url: https://mrocklin.github.io/blog/work/2012/11/07/Strategies
slug: Strategies
word_count: 670
---

In  [my last post](http://matthewrocklin.com/blog/work/2012/11/01/Unification/)  I showed how unification and rewrite rules allow us to express  *what*  we want without specifying  *how*  to compute it.  As an example we were able to turn the mathematical identity  `sin(x)**2 + cos(x)**2 -> 1`  into a function with relatively simple code

However we found that this function did not work deep within an expression tree

`sincos_to_one`  does not know  *how*  to traverse a tree.  It is pure logic and has no knowledge of control.  We define traverals separately using strategies.

*Short version* : we give you a higher order function,  `top_down`  which turns a
expression-wise function into a tree-wise function.  We provide a set of similar functions which can be composed to various effects.

## A Toy Example

How do we express control programmatically?

Traditional control flow is represented with constructs like  `if` ,  `for` ,  `while` ,  `def` ,  `return` ,  `try` , etc….  These terms direct the flow of what computation occurs when.  Traditionally we mix control and logic.  Consider the following toy problem that reduces a number until it reaches a multiple of ten

While the logic in this function is somewhat trivial

the control pattern is quite common in serious code

It is the “Exhaustively apply this function until there is no effect” control pattern. It occurs often in general programming and very often in the SymPy sourcecode.  We separate this control pattern into a higher order function named  `exhaust`

We show how to use this function to achieve the previous result.

By factoring out the control strategy we achieve several benefits

1. Code reuse of the  `while(old != new)`  control pattern
2. Exposure of logic - we can use the  `dec_10`  function in other contexts more easily. This version is more extensible.
3. Programmability of control - the control pattern is now first class.  We can manipulate and compose it as we would manipulate or compose a variable or function.

## Example - Debug

When debugging code we often want to see the before and after effects of running a function.  We often do something like the following

This common structure is encapsulated in the debug strategy

Because control is separated we can inject this easily into our function

## Traversals

Finally we show off the use of a tree traversal strategy which applies a function at each node in an expression tree.  Here we use the  `Basic`  type to denote a tree of generic nodes.

## Use in Practice

We have rewritten the canonicalization code in the Matrix Expression module to use these strategies.  There are a number of small functions to represent atomic logical transformations of expressions.  We call these rules.  Rules are functions from expressions to expressions

```
rule :: expr -> expr
```

And there are a number of strategies like  `exhaust`  and  `top_down`  which transform rules and parameters into larger rules

```
strategy :: parameters, rule -> rule
```

For example there are general rules like  `flatten`  that simplify nested expressions like

`Add(1, 2, Add(3, 4)) -> Add(1, 2, 3, 4)`

We compose these general rules (e.g. ‘flatten’, ‘unpack’, ‘sort’, ‘glom’) with strategies to create large canonicalization functions

## Going Farther

We use strategies to build large rules out of small rules.  Can we build large strategies out of small strategies? The  `canonicalize`  function above follows a common pattern “Apply a set of rules down a tree, repeat until they have no effect.” This is built into the  `canon`  strategy.

## Previous Work

This implementation of strategies was inspired by the work in the language StrategoXT. Stratego is a language for control that takes these ideas much farther and implements them more cleanly.  It is a language where control structure are the primitives that can be built up, composed, and compiled down.  It is a language in which ideas like “breadth first search” and “dynamic programming” are natural expressions.

## References

1. Ralf Lämmel , Eelco Visser , Joost Visser,  [*The Essence of Strategic Programming*](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CDMQFjAA&url=http%3A%2F%2Fhomepages.cwi.nl%2F~ralf%2Feosp%2Fpaper.pdf&ei=bJuaUNWwNuOc2AWQtICYCA&usg=AFQjCNHG1lJTjP05tO1aElYQkXMYSmgNuw&sig2=EwanltC52lXaC4gU4OtVvA) , 2002
2. Eelco Visser,  [*Program Transformation with Stratego/XT*](http://www.springerlink.com/content/my9we5tj86u2f59n/)
