---
title: "Doctests in Python"
date: 2017-02-16
url: https://www.hillelwayne.com/post/python-doctests/
slug: python-doctests
word_count: 624
---

Doctests are one of the most fascinating things in Python. Not necessarily because it’s particularly elegant or useful, but because it’s *unique*: I haven’t found another language that has a similar kind of feature.


Here’s how it works. Imagine I was writing an adder:


```
def add(a,b):
    return a + b

```


There’s two kinds of ways we can test it. The first is with unit tests, which everybody’s already used to. In pytest, that’d just be something like `assert add(1,2) == 3`. But we can also write a *doctest*:


```
def add(a,b):
    """ Adds two numbers.
    >>> add(5,6)
    11
    """
    return a + b

```


Then I can run the doctest with `python -m doctest`. It will simulate adding every input in the REPL and confirm it matches the given outputs. They were invented in 1999, well before TDD really took off, so there wasn’t a common convention on how to write unit tests. Doctests experimented with providing a different use-case than unittest did: the test is embedded right in the documentation and directly matches the HCI.


Nobody really uses them anymore. Turns out they make pretty bad tests! Since there’s no corresponding `beforeEach` for doctests (which would arguably miss the whole point), you have to repeat the same setup for every single doctest. Not a big deal when it’s a simple function, but imagine trying to use something like [hypothesis](http://hypothesis.works) in a doctest! Code-tests-code is much more flexible and scalable than documents-test-code. So for error checking, unittests are heavily used across languages while doctests remains a Python curiosity.


I think this is a huge shame. While doctests are much less efficient than unittests, they do have a unique property. Imagine you’re looking at this code:


```
def f(a,b):
  """ I think this adds two numbers but I'm not sure...
  >>> f(1, 2)
  3
  """
  return a - b

```


The doctest fails. So what should you do? Depends on if the *unit test* fails. If it does, then you have a bug in your function. If it passes, though, you can reasonably assume that it was intended from the start to be a subtraction. That means **there’s a problem with your documentation.** Unit tests check your code for bugs, while doctests check your guide for bugs!


I find that really cool. A lot of people have talked about how hard it is to keep your docs in sync with your code. Some have even advocated that docs are somehow dysfunctional: the only way to know what your code is supposed to do is to look at the tests. It’s at the point where BDD advocates even call their tests ‘specs’, which is kind of like throwing a hammer at a car and calling the dent a blueprint. I can see the temptation, though: tests are constantly running, so they’re theoretically forced to stay in sync. Whether they actually do is another matter, of course, but it’s the dynamic nature, the tests as motion, that makes it an appealing substitute for documentation.


Doctests go the other way. Instead of making the tests have documentation, it adds a tool to test documentation consistency. It’s not very good at it, which is why nobody uses it, but that’s not its fault. People have iterated on how to best do unit testing for two decades now, while doctesting is a niche part of a single language.


I’ve seen a lot of work on automatically generating documentation from code. I’d be interested in seeing how people approach it the other way, writing documentation in human language and instead verifying it from the code. Partially because it would allow for clearer documentation, and partially because it seems like nobody’s looked that hard. Finding beauty in the missing places.
