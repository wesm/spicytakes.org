---
title: "Breaking down a small language design proposal"
date: 2021-12-30
url: https://drewdevault.com/2021/12/30/Language-design-considerations.html
slug: Language-design-considerations
word_count: 1097
---

We are developing a new systems programming language. The name is a secret, so
we’ll call it  xxxx  instead. In  xxxx , we have a general requirement that all variables
must be initialized. This is fine for the simple case, such as “let x: int =
10”. But, it does not always work well. Let’s say that you want to set aside a
large buffer for I/O:

```
let x: [1024]int = [0, 0, 0, 0, 0, // ...
```

This can clearly get out of hand. To address this problem, we added the “…”
operator:

```
let x: [1024]int = [0...];
let y: *[1024]int = alloc([0...]);
```

This example demonstrates both  *stack*  allocation of a buffer and  *heap* 
allocation of a buffer initialized with 1024 zeroes. 1  This “…”
operator neatly solves our problem. However, another problem occurs to me: what
if you want to allocate a buffer of a variable size?

In addition to arrays,  xxxx  supports slices, which
stores a data pointer, a length, and a capacity. The data pointer refers to an
array whose length is equal to or greater than “capacity”, and whose values are
initialized up to “length”. We have additional built-ins, “append”, “insert”,
and “delete”, which can dynamically grow and shrink a slice.

```
let x: []int = [];
defer free(x);
append(x, 1, 2, 3, 4, 5); // x = [1, 2, 3, 4, 5]
delete(x[..2]);           // x = [3, 4, 5]
insert(x[0], 1, 2);       // x = [1, 2, 3, 4, 5]
```

You can also allocate a slice whose capacity is set to an arbitrary value, but
whose length is only equal to the number of initializers you provide. This is
done through a separate case in the “alloc” grammar:

```
use types;

let x: []int = alloc([1, 2, 3], 10);
assert(len(x) == 3);
assert((&x: *types::slice).capacity == 10);
```

This is useful if you know how long the slice will eventually be, so that you
can fill it with “append” without re-allocating (which could be costly
otherwise). However, setting the capacity is not the same thing as setting the
length: all of the items between the length and capacity are uninitialized. How
do we zero-initialize a large buffer in the heap?

Until recently, you simply couldn’t. You had to use a rather bad
work-around:

```
use rt;

let sz: size = 1024;
let data: *[*]int = rt::malloc(sz * size(int)); // [*] is an array of undefined length
let x: []int = data[..sz];
```

This is obviously not great. We lose type safety, the initialization guarantee,
and bounds checking, and we add a footgun (multiplying by the member type size),
and it’s simply not very pleasant to use. To address this, we added the
following syntax:

```
let sz: size = 1024;
let x: []int = alloc([0...], sz);
```

Much better! Arriving at this required untangling a lot of other problems that I
haven’t mentioned here, but this isn’t the design I want to focus on for this
post. Instead, there’s a new question this suggests: what about appending a
variable amount of data to a slice? I want to dig into this problem to explore
some of the concerns we think about when working on the language design.

The first idea I came up with was the following:

```
let x: []int = [];
append(x, [0...], 10);
```

This would append ten zeroes to “x”. This has a problem, though. Consider our
earlier example of “append”:

```
append(x, 1, 2, 3);
```

The grammar for this looks like the following: 2

So, the proposed “append(x, [0…], 10)” expression is  *parsed*  like this:

```
slice-mutation-expression: append
    object-selector: x
    append-items:
        [0...]
        10
```

In other words, it looks like “append the values [0…] and 10 to x”. This
doesn’t make sense, but we don’t know this until we get to the type checker.
What it really means is “append ten zeroes to x”, and we have to identify this
case in the type checker through, essentially, heuristics. Not great! If we dig
deeper into this we find even more edge cases, but I will spare you from the
details.

So, let’s consider an alternative design:

```
append(x, [1, 2, 3]);   // Previously append(x, 1, 2, 3);
append(x, [0...], 10);  // New feature
```

The grammar for this is much better:

Now we can distinguish between these cases while parsing, so the first example
is parsed as:

```
append-expression
    object-selector: x
    expression: [1, 2, 3]   // Items to append
```

The second is parsed as:

```
append-expression
    object-selector: x
    expression: [0...]    // Items to append
    expression: 10        // Desired length
```

This is a big improvement, but it comes with one annoying problem. The most
common case for append in regular use in  xxxx  is
appending a single item, and this case has worsened thanks to this change:

```
append(x, [42]);  // Previously append(x, 42);
```

In fact, appending several items at once is exceptionally uncommon: there are no
examples of it in the standard library. We should try to avoid making the common
case worse for the benefit of the uncommon case.

A pattern we  *do*  see in the standard library is appending one slice to another,
which is a use-case we’ve ignored up to this point. This use-case looks
something like the following:

```
append(x, y...);
```

Why don’t we lean into this a bit more?

```
let x: []int = [];
append(x, 42);              // x = [42]
append(x, [1, 2, 3]...);    // x = [42, 1, 2, 3]
append(x, [0...], 6);       // x = [42, 1, 2, 3, 0...]
```

Using the  `append(x, y...)`  syntax to generally handle appending several items
neatly solves all of our problems. We have arrived at design which:

* Is versatile and utilitarian
* Addresses the most common cases with a comfortable syntax
* Is unambiguous at parse time without type heuristics

I daresay that, in addition to fulfilling the desired new feature, we have
improved the other cases as well. The final grammar for this is the following:

If you’re curious to see more, I’ve extracted the relevant page of the
specification for you to read:  [download it here](https://redacted.moe/f/9c48d5d4.pdf) . I
hope you found that interesting and insightful!

*Note: Much of these details are subject to change, and we have future
improvements planned which will affect these features — particularly with
respect to handling allocation failures. Additionally, some of the code samples
were simplified for illustrative purposes.*

1. You can also use *static* allocation, which is not shown here. ↩︎
2. Disregard the second case of “append-values”; it’s not relevant here. ↩︎
