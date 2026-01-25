---
title: "J Notation as a Tool of Thought"
date: 2020-08-14
url: https://www.hillelwayne.com/post/j-notation/
slug: j-notation
word_count: 2654
---

Kenneth Iverson’s 1964 language, APL, won him the Turing Award. His award lecture, [Notation as a Tool of Thought](https://www.jsoftware.com/papers/tot.htm),
argued that better notations would lead people to deeper insights about mathematics.
He provided a number of examples
ranging across linear algebra,
arithmetic, probability,
and logic.


Unfortunately, most of the mathematics he covers isn’t relevant to programming.
However, his core idea still applies, and changing how we describe programs changes how we think about them.
I’d like to show how some of Iverson’s notations
lead to a better appreciation of what we can do
with programming languages.


Disclaimer: while *NaaToT* was written in APL, I’m going to use **J**, Iverson’s successor language, as I’m more familiar with it.
The notation examples I list should translate easily to other APL-based languages.
I’m also going to use non-idiomatic J in order to make things clearer for non-APLers.


## A Crash Course on J Syntax


Before we can talk about J’s notation, I need to introduce its peculiarities.
The APL lineage follows a different set of standards and design philosophies
than other programming languages. It also uses slightly different terminology.


APL is notorious for being very terse.
Instead of descriptive names, most functions (“verbs”) are single characters.
APL even used its own symbols, like `⌿` and `↑`, that required special keyboards.
J instead uses digraphs. `(* y)` is the [sign function](https://en.wikipedia.org/wiki/Sign_function).
`(*. y)` converts Cartesian coordinates to polar coordinates.
`(*: y)` squares y.


To further terse things up, every symbol represents both a unary function (a **monad**) and a binary function (a **dyad**).1
While `* y` gives the sign of y, `x * y` is multiplication. Similarly, (`*.`) and (`*:`) have dyadic forms that have little to do with their monadic forms.


These peculiarities help give APL code its characteristic “line noise” density.
This is some J code I wrote to get random weighted rows in a CSV:


```
x =: ".>1{"1}. csv
sample =: (> ?@$&0@#)@:%

csv #~ 0 , sample x

```


This drives people away from APLs and leaves the deeper elegance undiscovered.


## Arrays


If we want to talk about APL’s influence, we need to talk about arrays.


Most languages treat single numbers (scalars) as primitives and arrays as collections of primitives.2
Operations on arrays work by repeating an operation on scalars in the array.
If I want to double each element of an array, I’d have to do something like this:


```
def double_array(a):
  out = a[:]
  for i, n in enumerate(out):
    out[i] = 2 * n
  return out

```


We can simplify this by using something like `map`, but `map` itself is defined as stepping through the array.
Scalar operations are the primitives we use to emulate array operations.


J is different.  Instead of having arrays as “collections of scalars”, the array *is* the primitive.  If I write `1` I get an array with one  element.3 If I write `1 3 5` I get an array with three. All operations are designed with arrays in mind.
Here’s how I double every element in an array:


```
   2 * 4 5 6
8 10 12

```


And here’s how I multiply two arrays element-wise:


```
   1 2 3 * 4 5 6
4 10 18

```


This isn’t an overloaded operator: `*` just works on the whole array at once. We’ll discuss this in more detail later.


First class arrays become especially important when we go past one dimension.
Most languages represent a matrix
as a nested array, an array where each element is also an array.
There’s no guarantee that all the arrays
will have the same length
and there’s no way
to write a generalized operator
on any dimensional array.
If I have that `map`
that works on lists
I have to manually extend that to work on 2D matrices, and extend it again to work on 3D tensors.


Whereas in J, it’s the exact same thing.


```
   ]x =: i. 3 3
0 1 2
3 4 5
6 7 8
   6 * x
 0  6 12
18 24 30
36 42 48

```


One important consequence of this is that J arrays are purely *structural* collections of data, not *conceptual* ones.
In most languages,
nested arrays enforce
both a structural
and conceptual
representation of the data.
Since operations have to be specialized
to the dimensionality of the array,
our algorithm fixes the structure of the data.
By contrast,
in J we can reorder the axes however we want.


Short example. Imagine we have three light sensors that take hourly readings for four hours each day, two days total.
There are three dimensions of information here:
the day,
the hour of the day,
and the specific sensor.


```
   ]x =: i. 2 3 4
 0  1  2  3
 4  5  6  7
 8  9 10 11

12 13 14 15
16 17 18 19
20 21 22 23

```


Here I organized the data as
an array of matrices.
Each matrix represents a day
where the rows are distinct sensors and the columns are hours.
But I’m not tied to this organization.
I might want to instead have one matrix per sensor, where the rows are hours and the columns are days.
I can rearrange the data with a one-liner:


```
  1 0 2 |: x
 0  1  2  3
12 13 14 15

 4  5  6  7
16 17 18 19

 8  9 10 11
20 21 22 23

```


### Rank


Since we can work with entire arrays at once,
we need some way to talk about the components of an array.
It doesn’t make sense to add a vector to a matrix,
but we could add the vector to each row or each column of the matrix.


J supports this expressiveness
with **rank**.
The rank of a verb represents how much of the array it naturally acts on. Something with rank zero acts on individual elements, a verb with rank one operates on rows, rank two operates on matrices. Addition has rank `(0 0)`: `x + y` adds x and y element-wise, taking y’s structure into account.4


```
   ]x =: i. 3 3
0 1 2
3 4 5
6 7 8

   10 + x   
10 11 12
13 14 15
16 17 18

   10 20 30 + x
10 11 12
23 24 25
36 37 38

```


We can modify the rank of a verb with (`"`). Writing (`x +"1 y`) adds each row of x to each row of y.


```
   10 20 30 +"1 x
10 21 32
13 24 35
16 27 38

```


Rank makes it easy to
treat subsets of data
at the same level as the aggregate.
Back to the sensor example: there are three base dimensions I can cut the data on. With rank, I can choose with dimension I want.


```
   NB. first day
   0 { x
0 1  2  3
4 5  6  7
8 9 10 11

   NB. first hour
   0 {"1 x
 0  4  8
12 16 20
  
   NB. first sensor
   0 {"2 x
 0  1  2  3
12 13 14 15

```


In addition to refining how we manipulate arrays, rank helps us think about our script as a collection of executions, not just individual ones. Imagine we have an array of values and we want to see how many are below a certain threshold. But we’re not sure what we want the threshold to be; we should instead try the same operation several times with different thresholds and compare the results. In most languages we’d do this as N separate calls that would need to be aggregated. Using rank, we can see it as a single operation.


`x < y` has rank `(0 0)`, just like addition. Instead of giving it rank 1, we give it rank (0 `_`): apply every element of x to all of y at once.


```
   3 5 7 <"(0 _) 6 2 8 3 1 5 3 0 7 1
1 0 1 0 0 1 0 0 1 0
1 0 1 0 0 0 0 0 1 0
0 0 1 0 0 0 0 0 0 0

```


This particular use is so common that J provides a special adverb, `u/`, as syntactic sugar.


```
   3 5 7 </ 6 2 8 3 1 5 3 0 7 1
1 0 1 0 0 1 0 0 1 0
1 0 1 0 0 0 0 0 1 0
0 0 1 0 0 0 0 0 0 0

```


Since we have the entire set of runs with us, we can analyze how all the results relate. Which indices passed exactly two of the thresholds? Which indices passed at least one threshold, but not all of them?


```
   NB. exactly 2   
   2 = +/ x
1 0 0 0 0 0 0 0 1 0

   NB. at least one but not all
   (*./ ~: +./) x
1 0 0 0 0 1 0 0 1 0

```


## Sieves


You might have noticed that the boolean operators returned numbers. J doesn’t have a special boolean type: 1 is true and 0 is false. Rather than being just a hack, J integrates this equivalence into its array paradigm. Among other things, this provides a means of filtering that’s unlike any other language.


Say you want to select all of the elements of a list that are under 5. What’s your mental model of filtering? It’s probably something like “check the first element, append it to a new list if true, check the next element, etc.” Even if you think in terms of a `filter` primitive, that’s likely how you imagine it implemented. The J model of filtering is totally different:


```
(5 > y) # y

```


This works on a pun. The (`#`) dyad is **copy**: given element `y_i` of `y`, we copy it `x_i` times.


```
   1 2 3 1 # 'abcd'
abbcccd

   ] y =: ?.~ 10
4 3 6 2 9 8 5 1 7 0
   (5 > y)   
1 1 0 1 0 0 0 1 0 1
   (5 > y) # y
4 3 2 1 0

```


We constructed the result of `5 > y`, the **sieve**, as a separate step from the actual filtering. *The sieve is a distinct value*. This opens up all sorts of uses. We can filter a *different* list with the same sieve:


```
   ] sieve =: 5 > y
1 1 0 1 0 0 0 1 0 1
   sieve # 0 2 4 6 8 1 3 5 7 9
0 2 6 5 9

```


We can also operate on the sieve. We can invert it to reject matching elements or left shift it to get the elements that preceded matches:


```
   NB. reject instead of select
   (-. sieve) # y
6 9 8 5 7

   lshift =: 1&(|.!.0)
   lshift sieve
1 0 1 0 0 0 1 0 1 0
   (lshift sieve) # y
4 6 5 7

```


We can even use the sieve to modify the original list in ways other than filtering. The simplest example would be `(f y) + y`: increment every element that satisfies `f`. J provides a [general-purpose mechanism](https://code.jsoftware.com/wiki/Vocabulary/hatco) to fuse mapping and filtering,5 but that involves introducing J machinery that’s out of scope for this essay.


Finally, we can directly study the properties of the sieve. We can take the mean to get the percentage of the original array that passes the filter. We can get the distance between the indices of filtered elements, or see how filtered elements cluster in the original array. Our means of filtering becomes itself data.


### Grading


As with filtering and sieves, J has an array-based construction for sorting: the **grade**. The grade of an array, (`/: y`), is the [permutation vector](https://en.wikipedia.org/wiki/Permutation) that, if used to index y, would return a sorted array.


```
   ] y =: 1 9 2 8 3 7
1 9 2 8 3 7
   ] g =: /: y
0 2 4 5 3 1

   NB. Pick indexes
   g { y
1 2 3 7 8 9

```


This fundamentally captures what we mean by “sorting”. It’s easy to define what it means for a list to be *sorted*: increasing indices correspond to increasing values.6 However, this is not sufficient to define *sorting*. The following function guarantees all outputs are sorted:


```
def sort(l):
  return []

```


You need to specify that the output array has the same elements with the same cardinalities as the input array, which is a considerably more complex property to check. But that property is given to us for free by applying a permutation vector.7 “Return the permutation that is sorted” is the simplest mathematical definition of “sorting”.


Like with sieves, we can use the grades independently of the original array, such as to sort a different array.  We can also analyze the grade as a permutation vector. We can invert it, calculate how “unsorted” our original array was, or find the fixed points of the array.


```
NB. Invert the permutation
   /: g
0 5 1 4 2 3

NB. How far was each element from sorted?
   | g - i.6
0 1 2 2 1 4

NB. What are the fixed points?
   g = i.6
1 0 0 0 0 0

```


This is one of the things I miss most in other languages. Among other things, having the grade makes it easy to keep a “history” of the list sorting. Storing a length N permutation vector only takes ≈4N bytes, as compared to however many bytes the original array took. You can see a set of data in the original view, sort it, and then “flip” back to the original view when you’re done.


```
   ] sortedy =: g { y
1 2 3 7 8 9
   NB. invert g
   ] ig =: /: g
0 5 1 4 2 3
   NB. gives us back y
   y = (ig { sortedy)
1 1 1 1 1 1

```


---


When people think of APLs, they think of the syntax. But this isn’t the essence of APLs and there’s nothing preventing an APL from being verbose.  The essence of APL is in how it thinks about arrays as primitives and how it represents array transformations. The notation is just there to encourage exploration, to help the core ideas shine through. It’s there to help us think better about arrays and programs.


I may not use J in my everyday programming, but I’m glad I learned it and think it made me a better programmer. If you’re interested in J, you can download it [here](https://www.jsoftware.com/#/). You can also try it online [here](https://tio.run/##y/r/PzU5I19B3SM1JydfRyE8vygnRVH9/38A).


*I shared the first draft of this essay on my [newsletter](https://buttondown.email/hillelwayne/). If you like my writing, why not subscribe?*


---

1. APL was the first language to use “monad” as a term. The popular FP meaning only appeared thirty years later.
 [return]
2. This has changed a little in recent decades, with languages like MATLAB and Julia having array-first primitives and libraries like numpy augmenting existing languages. Most of these were inspired by APL.
 [return]
3. Okay this is a bit of a lie. As an optimization, J will treat this as a scalar. But *morally* it behaves as an array of one element except in very niche circumstances.
 [return]
4. The dimensions of `x` should match the “most significant dimensions” of y. So `x + y` works if x is a 2x3 matrix and y is a 2x3x19x7 matrix.
 [return]
5. More precisely, a mechanism that *can be used* to fuse the two. Almost everything in J pulls septuple-duty with common use cases.
 [return]
6. I’m considering only lists of integers right now, but the same specification can be extended to arbitrary sorting keys.
 [return]
7. This is because permutations form a group, so every permutation has an inverse. 
 [return]
