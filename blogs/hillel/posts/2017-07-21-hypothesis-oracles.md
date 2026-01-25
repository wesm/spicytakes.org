---
title: "Hypothesis Testing with Oracle Functions"
date: 2017-07-21
url: https://www.hillelwayne.com/post/hypothesis-oracles/
slug: hypothesis-oracles
word_count: 1041
---

*This post is about the [Hypothesis](http://hypothesis.works) testing library. If you’re unfamiliar with it, check it out! Property tests are a fantastic addition to your testing suite. All examples use [pytest](https://docs.pytest.org/en/latest/).*


Imagine we’ve written a bubblesort:


```
def bubblesort(l: List[int]) -> List[int]:
    # blah blah blah

```


What are some of the properties we could test? We could check that the input has the same length as the output:


```
from hypothesis import given
from hypothesis.strategies import lists, integers 

@given(lists(integers()))
def test_same_length(l):
    assert len(bubblesort(l)) == len(l)

```


Or we could test that the sort is idempotent:


```
@given(lists(integers()))
def test_idempotent(l):
    assert bubblesort(bubblesort(l)) == bubblesort(l)

```


But neither test really gets at what we want: confirming the list is actually *sorted*. Fortunately, though, there’s a simple hypothesis test for that:


```
@given(lists(integers()))
def test_sorts(l):
    assert bubblesort(l) == sorted(l)

```


We just need to check that the output of the function matches the output of a sorting function! In this case, `sorted` is an *oracle*, something we know is correct and can compare our solution to. This may look like cheating (*“if we already have a sorting function, why would we be writing another?”*), but this can be a surprisingly powerful testing strategy. Here are some common use-cases:


### Refactoring with Oracles


One use case for an oracle is when you refactor an existing function: you want to clean up or optimize something you’re confident is correct and want to make sure your changes don’t break anything. Let’s take a toy example:


```
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

```


A common optimization we can do is only check up to the square root of the number:


```
from math import ceil, sqrt

def new_is_prime(x: int) -> bool:
    # blah blah blah
    for i in range(2, ceil(sqrt(x))):
    # sup

```


This seems like it works for simple test cases, but if we compare it to our original function, we find an error:


```
@given(integers())
def test_matches_oracle(x):
    assert is_prime(x) == new_is_prime(x)

```


This error comes from how `range` works: `list(range(2, 2)) == []`, so our function fails for 4. We found this by using our original version as an oracle against the refactored version.


### Special-Case Oracles


Sometimes we know our function works in specific cases but does not generalize. For example, the following function ostensibly takes a list and returns the highest possible product of three elements:


```
# We'll assume that all inputs will have more than 3 elements
# So no need for a bounds check
def buggy_max_triplet_prod(l: List[int]) -> int:
    a, b, c = sorted(l, reverse=True)[0:3]
    return a * b * c

```


This is correct when all of the elements are positive. However, it fails for `[-4, -3, 1, 2]`, returning -6 instead of 24. We can still use this as an oracle, though. Since we know it’s correct for certain lists, our final function must match its output for those lists.


```
@given(lists(integers(min_value=0), min_size=3)) # only positive numbers
def test_matches_on_positive(l):
    assert max_triplet_prod(l) == buggy_max_triplet_prod(l)

```


Over our restricted domain, the broken function is correct, and can be used as an oracle.


### Inefficient Oracles


Sometimes there’s a solution to a problem that we know for sure works but is too slow/memory-intensive/etc for production code. We can use that solution as an oracle to test a more sophisticated function. If you wanted to write a function to insert into a sorted array, you could use the following as a reference oracle:


```
def ordered_insert_oracle(new_element: int, ordered_list: List[int]) -> List[int]:
    return sorted(ordered_list + [new_element])

@given(lists(integers), integers())
def test_ordered_insert(l, x):
    assert ordered_insert(l, x) == ordered_insert_oracle(l, x)

```


The oracle will be O(n*log(n)), while a well written ordered insert will be O(n). That might matter in production, but it won’t matter too much in testing, so we can benefit from an oracle here.


### Reverse Oracles


Sometimes we can go the other way: instead of writing an oracle that will always get the right answer, we can write a function that takes an answer and finds a question for it. This gets a bit complicated, so let’s walk through an example. We’re writing our own [counter](https://docs.python.org/3/library/collections.html#collections.Counter).


```
from random import shuffle

@given(lists(tuples(integers(), integers(min_value=1, max_value=10)), unique_by=lambda x: x[0]))
def test_counter(l):
    test_list = []
    for val, times in l:
        test_list += [val] * times
    shuffle(test_list)
    assert count(test_list) == {val:times for val, times in l}

```


Here, we’re taking a possible answer and *generating* a list that matches that. For example, if our test generates `l = [(5, 2), (1, 1)]`, that means we want our function to return `{5: 2, 1: 1}`. So we find a list that, *if `count` is written correctly*, would match that output. Our implementation is to first create the list `[5, 5, 1]` and then shuffle it.


This test ends up being more complicated than the others because it’s easier for the test itself to have bugs. Note the `unique_by`; that’s because our test will bug if we generate `l = [(1, 1), (1, 1)]`: we’ll assert `{1: 2} == {1: 1}`.


## Caveats


Most of these caveats apply to property-based tests (PBTs) in general.

- You’ll want to write some unit tests to sanity-check your oracles. This throws you down a rabbit hole (*“I have to test my tests?!”*), but you get much wider test coverage with PBTs in return for the extra complexity.
- Sometimes coming up with the oracles can be as or more difficult than writing the final functions. As always, writing good code involves tradeoffs.
- The further you get from pure functions the harder writing PBTs gets. Reverse oracles help a bit here.
- When writing bullet points like this I’m always tempted to add something completely unrelated. Here’s something I wrote about how much I like [dogs](https://www.hillelwayne.com/post/falsehoods-programmers-believe-about-dogs).
- Don’t try to be overly clever and use oracles in cases where more basic PBTs (or even unit tests) suffice.
- The benefits PBT provides are orthogonal to the benefits you get from unit tests, type systems, [formal methods](https://www.hillelwayne.com/post/modeling-deployments), and getting a full night’s sleep. Ideally you’d want to have all five.
- Ruby doesn’t have a good PBT library and that makes me sad.
