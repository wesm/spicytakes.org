---
title: "Branching Strategies"
date: 2012-11-09
url: https://mrocklin.github.io/blog/work/2012/11/09/BranchingStrategies
slug: BranchingStrategies
word_count: 424
---

In my last post on  [strategies](http://matthewrocklin.com/blog/work/2012/11/07/Strategies/)  I introduced a set of higher order functions to represent common control patterns (like  `top_down` ).  We combined these with transformation rules (like  `flatten` ) to create complex functions for tree manipulation (like  `flatten_tree` )

```
rule     :: expr -> expr
strategy :: parameters, rule -> rule
```

In my post on  [unification](http://matthewrocklin.com/blog/work/2012/11/01/Unification/)  we showed how to easily create rules from patterns.  At the end of this post I described that because patterns might match in multiple ways one rule might produce many different results.  To avoid combinatorial blowup in the number of possible matches we solved this by yielding matches lazily.

Transformation rules produced by unify don’t return values, they yield possible solutions lazily.  How do we reconcile this with our previous notion of rules and strategies? We make a new set of strategies for branching rules.

```
branching-rule      :: expr -> {expr}
branching-strategy  :: parameters, branching-rule -> branching-rule
```

In  `sympy.rules.branch`  we have implemented lazy analogs for the strategies found in  `sympy.rules` .  This allows us to apply strategies to transformations like the  `sincos_to_one`  rule created in the unification post.

## Toy Problem

Lets see branching strategies with a toy problem. Consider the following
“function”

And it’s equivalent in Python

Notice that in the case where  `x = 5`  there are two possible outcomes. Each of these is preserved by the application of branching strategies. We use the branching version of the  `exhaust`  strategy to make a new exhaustive
version of this function

## Practical Problem

We have all the machinery necessary. Lets make a  `sin(x)**2 + cos(x)**2 -> 1`  tree-wise simplification function.

Lets make a rule to simplify expressions like  `c**1`

We see how we can easiy build up powerful simplification functions through the separate description of logic

```
sin(x)**2 + cos(x)**2 -> 1
x ** 1 -> x
```

and control

```
simplify = exhaust(top_down(multiplex( ... )))
```

*Footnote 1* : At the time of this writing this line should actually be

```
map(rebuild, sincos_tree( ... )
```

The  `rebuild`  function is necessary because rules don’t play well with  `Expr` s. Expr’s need to be constructed normally in order to function properly. In particular all expressions built by rules lack the  `is_commutative`  flag which is attached onto the object at construction time. I neglected to mention this above to simplify the discussion.

*Footnote 2* : This also requires a slight modification due to the Expr/rules mismatch. In particular the pattern  `Pow(x, 1, evaluate=False)`  unfortunately matches to just  `x`  because  `x == x**1`  in SymPy.
