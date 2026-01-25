---
title: "Property Tests + Contracts = Integration Tests"
date: 2017-12-17
url: https://www.hillelwayne.com/post/pbt-contracts/
slug: pbt-contracts
word_count: 735
---

I’m a pretty big fan of [contracts](https://www.hillelwayne.com/post/contracts) and [property-based testing](https://www.hillelwayne.com/post/hypothesis-oracles). While they’re both powerful, they do have tradeoffs:

- **Contracts** are simple and allow for complex conditionals, but you need to test them over a wide space to confirm them.
- **Property-Based Testing** can test your code over a very wide search space, but you have to come up with good generators and invariants.


Maybe they complement each other: “your code doesn’t violate any contracts” counts as a PBT invariant. Maybe we can generate inputs that match the preconditions and confirm that all of the postconditions (and preconditions of other called functions) are preserved.


Let’s start with a simple example. I’m using [hypothesis](https://hypothesis.readthedocs.io/) as my PBT library and [dpcontracts](https://github.com/deadpixi/contracts) for Python contracts, which is new but very promising. Our toy function will be “remove from list”.


```
@require("`x` must be in `l`", lambda args: args.x in args.l)
@ensure("`x` must be removed from `l`", lambda args, result: args.x not in result)
def remove(l, x):
  l.remove(x)
  return l

```


If `x` starts out in `l`, the returned value will not have x. I know this is also mutating `l`, but again, toy example. Here’s our PBT:


```
@given(lists(integers()), integers())
def test_with_contracts(l, x):
  remove(l, x)

```


Normally we’d have an `assert` in our PBT to check that some invariant holds. We don’t need to do that here because the contracts *are* our invariant. If the test completes without throwing an error, our invariant holds. In this case, it doesn ot:


```
E           AssertionError: `x` must be in `l`
Falsifying example: test_with_contracts(l=[], x=0)

```


Our test failed because we violated a precondition. Since this is the function we directly called from the test, and not a deeper-level function, this probably corresponds to an error in our test. Our function is only supposed to work if `x in l`, so there’s no reason to try it with bad data.1 Let’s add an assumption to our test and rerun.


```
def test_with_contracts(l, x):
  assume(x in l)
  remove(l, x)

```


```
E           AssertionError: `x` must be removed from `l`
Falsifying example: test_with_contracts(l=[0, 0], x=0)

```


In python `[0, 0].remove(0) == [0]`, which is why our postcondition failed. It could be that we made the precondition too loose and need a stricter one, or it could be that our implementation is bad. It’s probably the latter.


```
def remove(l, x):
  return [y for y in l if y != x]

```


Note we’ve tested our function without ever specifying what we’re checking in the test! All it’s doing is acting as a **fuzzer**. It generates inputs that check the contracts, because if the contracts break our program has a bug. What’s especially cool is that this “chains”. If the function we call calls other functions with contracts, those contracts are checked too. Combining contracts and PBT gives us integration tests!


As a demonstration, I wrote up a quick [siteswap validator](https://en.wikipedia.org/wiki/Siteswap). It takes a juggling pattern and returns how many balls it has.


```
@require("Should get a nonempty pattern", lambda a: a.pattern)
@ensure("Ball count should be integer", lambda _, r: r == round(r))
@ensure("... less than highest throw", lambda a, r: r <= max(a.pattern))
@ensure("Balls should be nonnegative", lambda _, r: r r >= 0)
def balls_in_siteswap(pattern: List[int]):
    return sum(pattern) / len(pattern)

@require("Should get a nonempty pattern", lambda a: a.pattern)
def valid_pattern(pattern: List[int]) -> bool:
    landing_pattern = set()
    for indice, throw in enumerate(pattern):
        beat = (throw + indice) % len(pattern)
        if beat in landing_pattern:
            return False
        landing_pattern.add(beat)
    return True

def siteswap_to_balls(pattern: List[int]) -> Optional[int]:
  if pattern and valid_pattern(pattern):
      return balls_in_siteswap(pattern)
  return None

@given(lists(integers()))
def test_siteswap(pattern):
  siteswap_to_balls(pattern)

```


When this is run, `test_siteswap` tries an empty pattern, which fails in `valid_pattern`. If I make `siteswap_to_balls` check for that, it passes a negative number, which fails a postcondition in `balls_in_siteswap`. The test doesn’t have to know anything about what `siteswap_to_balls` does, only that it accepts lists of integers. The contracts do the rest.


Given that one of the big challenges in PBT is coming up with invariants and one of the challenges of integration testing is the integration, I think this idea is worth exploring. I tried combining PBT and contracts for a task at work and it seems promising.


---

1. In a more realistic environment, we’d have this behind a layer of defensive code. If the contract is violated then the defensive layer probably has a bug and we should fix that instead.
 [return]
