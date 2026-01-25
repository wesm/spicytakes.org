---
title: "Finding Property Tests"
date: 2019-04-08
url: https://www.hillelwayne.com/post/contract-examples/
slug: contract-examples
word_count: 2535
---

A while back I was ranting about APLs and included this python code to get the mode of a list:


```
def mode(l):
  max = None
  count = {}
  for x in l:
    if x not in count:
      count[x] = 0
    count[x] += 1
    if not max or count[x] > count[max]:
      max = x
  return max

```


There’s a bug in it. Do you see it? If not, try running it on the list `[0, 0, 1]`:


```
>>> mode([0, 0, 1])
1

```


The issue is that 0 is falsy, so if max is 0, `if not max` is true.


I could say this bug was a result of carelessness. I didn’t write any tests for this function, just tried a few obvious examples and thought “yeah it works”. But I don’t think writing bespoke manual unit tests would have caught this. To surface the bug, the mode of a list must be a falsy value like 0 or `[]` *and* the last value of the list must be something else. It’s a small intersection of Python’s typing and the mechanics of `mode`, making it too unusual a case to be found by standard unit testing practice.


A different testing style is property based testing (PBT) with [contracts](https://www.hillelwayne.com/post/contracts/). By generating a random set of inputs, we cover more of the state space than we’d do manually. The problem with PBT, though, is that it can be hard to find good properties. I’d like to take mode as a case study in what properties we could come up with.


There are a few things I’m looking for:

- The property test should find the bug.
- The test should be *simple*. I’m presumably not putting a lot of effort into testing such a simple function, so a complex test doesn’t accurately capture what I’d do.
- The test should be *obvious*. I’m looking for a natural test that finds the bug, not a post-hoc one. Catching a bug with tests is much less believable if you already know what you’re looking for.


So, let’s talk some tests and contracts! I’m using [hypothesis](http://hypothesis.works) for the property tests, [dpcontracts](https://github.com/deadpixi/contracts) for my contracts library, [pytest](https://docs.pytest.org/en/latest/) for the runner1.  For the sake of this problem, assume we’re only passing in nonempty lists.


```
@require("l must not be empty", lambda args: len(args.l) > 0)
def mode(l):
  ...

```


## Contract-wise


One property of a function is “all of the contracts are satisfied”. We can use this to write “thin” tests, where we don’t put any assertions in the test itself. If any of our contracts raise an error then the test will fail.


```
@given(lists(integers(), min_size=1))
def test_mode(l):
    mode(l)

```


### Types


Typically in dynamic programming languages, contracts are used as a poor replacement of a static type system. Instead of checking the type at compile time, people check the type at runtime. Most contract libraries are heavily geared towards this kind of use.


```
@ensure("result is an int", lambda _, r: isinstance(r, int))

```


This is a bad contract for three reasons:

1. It requires the function to return integers when it’s currently generic. We *could* try to make it generic by doing something like `type(a.l) == type(r)`, but *ugh*.
2. We should be using mypy for type checks anyway.
3. It doesn’t actually find the error. The problem isn’t the type, it’s that we got the wrong result.


### Sanity Checking


We can go further than replicating static types. One common type of contract is a “sanity check”: some property that does not fully specify our code, but is easy to express and should hold true anyway. For example, we know the mode will be an element of the list, so why not check that we’re returning an element of the list?


```
@ensure("result is in list", lambda a, r: r in a.l)

```


This is a pretty good contract! It tells us useful things about the function, and it’s not easily replacable with a typecheck. If I was writing production code I’d probably write a lot of contracts like this. But it also doesn’t find the problem, so we need to go further.


### First element


Our sanity check was only minimally related to our function. There are lots of functions that return elements in the list: `head`, `random_element`, `last`, etc. The issue is a subtle bug in our implementation. Our contract should express some important property about our function. In mode’s case, it should relate to the count of the value.


One *extremely* useful property is adding bounds. The mode of a list is the element that occurs most frequently. Every element of the list should occur less often, or as often, as the mode.2 One good arbitrary element is the first element:


```
@ensure("result > arbitrary", 
  lambda a, r: a.l.count(r) >= a.l.count(a.l[0]))

```


This finds the bug!


```
args = ([0, 0, 1],), kwargs = {}, rargs = Args(l=[0, 0, 1])
result = 1
E           dpcontracts.PostconditionError: result > arbitrary

```


Personally, I’d prefer this as a property test clause instead of a contract clause. It doesn’t feel “right” to me. I think it’s more an aesthetic judgment than a technical one here.


```
@given(lists(integers(), min_size=1))
def test_mode(l):
    x = mode(l)
    assert l.count(x) >= l.count(l[0])

```


Either way, this is only a partial contract: while it will catch *some* incorrect outputs, it won’t catch them all. We could get this with `[1, 0, 0, 2]`: `count(0) > count(2) >= count(1)`, but our broken function would return `2`. In some cases, this is all we can feasibly get. For simpler functions, though, we can rule out all incorrect outputs. We want a total contract, one which always raises on an incorrect output and never raises on a correct one.


### The dang definition


Why not just use the definition itself?


```
@ensure("result is the mode", 
  lambda a, r: all((a.l.count(r) >= a.l.count(x) for x in a.l)))

```


To make this nicer we can extract this into a dedicated helper contract:


```
def is_mode(l, m):
    return all((l.count(m) >= l.count(x) for x in l))

@ensure("result is the mode", lambda a, r: is_mode(a.l, r))

```


This also catches the error.


```
args = ([0, 0, 1],), kwargs = {}, rargs = Args(l=[0, 0, 1])
result = 1


```


This is the same faulty input as before. Property-based Testing libraries **shrink** inputs to find the smallest possible error, which is `[0, 0, 1]`.


### Compare to an Oracle


If we had another way of getting the answer that we knew was correct, we could just compare the two results and see if they’re the same. This is called using an **oracle**. Oracles are often a good choice when you’re trying to refactor a complex function or optimize an expensive one. For our purposes, it goes too far.


```
from collections import Counter

def math_mode(l):
    c = Counter(l)
    return c.most_common(1)[0][0]

@require("l must not be empty", lambda args: len(args.l) > 0)
@ensure("result matches oracle", lambda a, r: r == math_mode(a.l))
def mode(l):
  ...

```


This is too heavy. Not only is it cumbersome, but it overconstrains what the mode can be. We see this in the error it finds: it finds an error with a smaller input than the other two!


```
args = ([0, 1],), kwargs = {}, rargs = Args(l=[0, 1]), result = 1

```


We haven’t precisely defined the semantics of `mode`. If there are two values which tie for the most elements, which is the mode? Our prior contracts didn’t say: as long as we picked an element that had at least as many instances as any other element, we were good. With `math_mode`, we’re arbitrarily choosing one of them as the “real” mode and checking that our `mode` picked that arbitrary element. We can see this better by writing a manual test:


```
def test_mode():
    mode([3, 2, 2, 3])

...

args = ([3, 2, 2, 3],), kwargs = {}, rargs = Args(l=[3, 2, 2, 3])
result = 2

```


Whereas with our previous contract passes on this.


## Property-wise


Our contract approach converged on “testing the definition” as the best result. There are many cases where code-under-test does not have a nice mathematical definition. Contracts are still useful here, as they can rule out bad cases, but you’ll need additional tests.


*Hypothetically* contracts can express all possible properties of a function. In practice you’re limited to what your framework can express and check. For most complicated properties we’re better off sticking it in a dedicated test.


“Property-wise” property tests have several advantages over “contract-wise” property tests:

1. We can test properties that aren’t “ergonomic” in our contract framework.
2. We can test properties that involve effects.
3. We can test [metamorphic relations](https://www.hillelwayne.com/post/metamorphic-testing/) which involve comparing multiple function calls.


For this `mode` problem we don’t need any of them, but let’s show off some possible tactics anyway.


### Preserving Transformation


We find some transformation of the input that should give the same output. For lists, a good transformation is sorting.3 The mode of a list doesn’t change if you sort it:


```
@given(lists(integers(), min_size=1))
def test_sorting_preserves_mode(l):
    assert mode(l) == mode(sorted(l))

...

l = [0, 0, -1]

```


We could also reverse the list instead of sort it, but that gives us an error case of `[1, -1]`, which again is due to overconstraints.


Or we could assert that the mode doesn’t change if we add it again to the list:


```
def test_can_add_to_mode(l):
    m = mode(l)
    assert mode(l + [m]) == m

```


This does *not* find the bug, though.


### Controlled Transformation


Instead of finding a solution that doesn’t change the answer, we could find one that changes it in a known way. One of them might be “doubling all of the numbers doubles the mode”:


```
@given(lists(integers(), min_size=1))
def test_doubling_doubles_mode(l):
    doubled = [x * 2 for x in l]
    assert 2*mode(l) == mode(doubled)

```


This does not find the bug. We could also try “adding 1 to every element adds 1 to the mode”:


```
@given(lists(integers(), min_size=1))
def test_incrementing_increments_mode(l):
    incremented = [x + 1 for x in l]
    assert mode(l)+1 == mode(incremented)

...

l = [0, 1]

```


It gives the same output as in our overconstrained case, but it only “is wrong” when we have 0’s anyway. If we restrict the list to only positive integers, it will pass (unlike our oracle contract).


If we wanted to be extra thorough we could generatively pick both a slope and an increment:


```
@given(lists(integers(), min_size=1), integers())
def test_affine_relation(l, m, b):
    transformed = [m*x+b for x in l]
    assert  m*mode(l)+b == mode(transformed)

...

l = [0, 1], m = 1, b = 1

```


It depends on how paranoid you want to get.


### Oracle Generators


The big advantage of manual tests to generative ones is that you can come up with the appropriate outputs for a given input. Since we can’t easily do that in PBT, we’re stuck testing properties instead of oracles.


Or we could go in reverse: take a random output and generate a corresponding input. One way we can do that:

1. generate pairs of elements and counts. Make sure that the elements are unique
2. construct a list from that
3. pass in both the list and the corresponding mode, selected from the pair.


```
@composite
def list_and_mode(draw):
    out = []
    pairs_max_10 = tuples(integers(), integers(min_value=1, max_value=10))
    counts = draw(lists(pairs_max_10, 
        min_size=1,
        max_size=5, 
        unique_by= lambda x: x[0]))
    for number, count in counts:
        out += ([number] * count)
    mode_of_out = max(counts, key=lambda x: x[1])[0]
    return out, mode_of_out

@given(list_and_mode())
def test_can_find_mode(lm):
    l, m = lm
    assert mode(l) == m

...

lm = ([0, 1], 0)

```


This overconstrains (we’re not ruling out two pairs having the same counts), but it *does not* raise a false positive for `[3, 2, 2, 3]`. This is because we construct the list in the same way `max` interprets the list. If we do


```
-   for number, count in counts:
+   for number, count in reversed(counts):

```


Then it raises `[3, 2]` as a “counterexample”. Between the cumbersomeness and the overconstraining, making an oracle generator is not a good choice for this problem. There are some cases, though, where it can be more useful.


## Limitations


Here’s a fixed version that *looks* like it will work:


```
def mode(l):
  max = None
  count = {}
  for x in l:
    if x not in count:
      count[x] = 0
    count[x] += 1
+   if max is None or count[x] > count[max]:
-   if not max or count[x] > count[max]:
      max = x
  return max

```


And this passes all of our tests. But there’s still a bug in it. Again, take a minute to see if you can find it. If you can’t, try the following:


```
mode([None, None, 2])

```


This will select the mode as `2`, when it really should be `None`. The problem isn’t in our contracts or assertions. It’s in our test generator: we’re only testing with lists of integers. Hypothesis can generate heterogenous lists, but you still have to explicitly list the types you want to be in the list. In order to find this bug we’d have to explicitly realize that `None` might be a problem for us.


If we only want to call `mode` on homogenous lists, we should instead use a typechecker to catch the bug:


```
+ def mode(l: List[T]) -> T:
- def mode(l):
    max = None
+   count = {} # type: Dict[T, int]
-   count = {}

```


This will raise a spurious error, saying that the return value is actually an `Optional[T]`. If we change `max = None` to `max = l[0]` both the error and the bug go away. But we can change the return value to `Optional[T]` and the bug remains- mypy can’t actually detect if we’re passing in a heterogenous list. More type-oriented languages can ban heterogenous lists outright but even those will miss the bugs our contracts caught. Static and dynamic analysis are complementary, not contradictory.4


## Summary


This was a pretty short dive into what makes a good property or contract. It also focused on just pure functions: a lot of languages use contracts to maintain class invariants or monitor the side effects of procedures.


If you’re interested in learning more about properties, [this](https://fsharpforfunandprofit.com/posts/property-based-testing-2/) is a canonical article on abstract properties and [this](https://wickstrom.tech/programming/2019/03/24/property-based-testing-in-a-screencast-editor-case-study-1.html) is a series on applying it to business problems. If you’re interested in learning more about contracts, I’d recommend… actually, I can’t think of anything that’s not language-specific. Kind of surprising given how useful they are.


---

1. Oddly enough I’m getting increasingly less sold on using pytest, purely because I want to experiment with weird janky metaprogramming in my tests and pytest doesn’t really support that.
 [return]
2. We have to say “less than *or equal to*” for two reasons. First, the mode is not strictly more frequent than other elements, like in `[1, 1, 2, 2]`. Second, what if the mode *is* `l[0]`?
 [return]
3. Unless you’re trying to test a sorting function.
 [return]
4. Both contracts and properties can be checked statically, but *most* people using them will be checking them at runtime. This is because static analysis of contracts quickly turns into formal verification, which is really, really hard.
 [return]
