---
title: "Just a Whole Bunch of Different Tests"
date: 2018-04-02
url: https://www.hillelwayne.com/post/a-bunch-of-tests/
slug: a-bunch-of-tests
word_count: 2782
---

I’ve been working on a bunch of longform obligation pieces and while they’re a lot of fun, they’re also steadily driving me insane. So I took a day off to write about all of the kinds of automated testing I know about. I’m defining **tests** here to be “an independent verification program that, as part of verification, executes the code we want to verify.” This means types are not tests, as they don’t involve execution of the code, and contracts are not tests, because they’re not executed as an independent program. It also means that we’re (for the purposes of this essay) excluding things like load testing or performance testing.


I tried to include some categorization and links and stuff but if you have a better reference for any of these, feel free to email me. All examples are written in pseudo-python with pytest unless otherwise noted.


# Automanual Tests


**Automanual**, or **example** tests are the most common type of automated test. They’re any tests where the setup, input, and assertions are all exactly specified by the programmer. This is in contrast to **generative** tests, where the testing program is allowed to determine its own parameters. The advantage of automanual tests is that they are easy to write, are (supposed to be) deterministic, and don’t need heavy infrastructure. The disadvantage is that each one only tests a tiny sliver of the overall state space, meaning that they don’t scale well.


Agile and XP practices really heavily emphasize automanual tests, which has mixed benefits. Agilists tend to talk about a [testing pyramid](https://martinfowler.com/bliki/TestPyramid.html) which consists of many unit tests, fewer integration tests, and fewest acceptance tests. In other disciplines, automanual tests are often used as “base cases” to guarantee a system does what you want it to in the happy path, and to check complicated edge cases that would be too hard or specific for generative testing.


#### Unit Tests


A tests that tests a “unit”. There’s no consensus on what a “unit” is or the boundary between a unit test and an integration test. I think a good difference is that unit tests are unaffected by **emergence**, or complex behavior that arises from multiple interacting components. As a corollary of this, unit tests cannot test connections to third party services or significant side effects. Agilists suggest that unit tests are supposed to be completely isolated from each other and complete extremely quickly: a hundred unit tests should complete in less than a second.


```
def test_flatten_list_of_lists():
  assert flatten([[1], [4, 1], [9, [10]]]) == [1, 4, 1, 9, 10]

```


To keep unit tests small, fast, and isolated, people sometimes replace code that’s not part of the “unit” with *doubles*, minimal code substitutions for the purposes of testing. [There are different kinds](http://blog.tremblay.pro/2017/09/mocks.html) of code doubles: *stubs* return canned values, *mocks* assert they were called with the right values, and *spies* combine stubs and mocks.


One common use case of unit tests is to catch **regressions**. If you find a bug in your program, you write a unit test that checks the bug isn’t there. If you later refactor the code and accidentally reintroduce the bug, the unit test will catch it.


#### Integration Tests


A test that tests whether units “integrate”. As mentioned before, the boundaries between units, integrations, etc can get very fuzzy. Most people seem to implicitly use it as shorthand for “tests that might fail due to emergence.” If an integration test spanning two units fails, the issue could be in either of the two units, or both of them, or in the specific ways they interact. They may involve side effects or I/O, but calls to third party services are usually stubbed out.


```
def test_grade_job_updates_grades():
  # A bunch of setup
  assert student.class_grade == "F"
  ProblemSet.grade_for(teacher.class)
  assert student.class_grade == "F-"

```


Integration tests test more than unit tests, but have three comparative disadvantages. First of all, integration tests are brittler and more likely to *flake*, or fail nondeterministically. Second, they can be considerably slower than unit tests. Finally, they don’t localize errors well: it’s often hard figure out *what* part of the code is causing the integration test to fail. For all of these reasons, the Testing Pyramid-style recommends you write more unit tests than integration tests.


You might hear that integration tests don’t test as much as unit tests do. This is technically untrue. Rather, a given integration test covers a smaller percentage of the total possible integrations than a unit test covers the total existing units. This is because [emergence is a hellishly complicated problem](http://www.pamelazave.com/faq.html) and many, many bugs hide in the interactions between units. For this reason, it’s generally a good idea to do generative integration testing instead of automanual testing.


You might see integration tests called “contract tests”, as they test the “contract” between the code and the caller. I really hate this name, as contracts are a [well-defined verification discipline](https://www.eiffel.com/values/design-by-contract/introduction/). Calling integration tests “contract tests” is completely missing the point of contracts.


#### Acceptance Tests


A test that only interacts with the program through the public API. For a web app, this could mean running a fake browser and simulate clicking buttons. For a script, this could mean invoking it from a shell and checking the file it modified. The purpose of acceptance testing is to check that a “user” will see the program behave correctly. Hence the name: will the user accept the program as meeting the required functionality?


```
def test_clicking_button_changes_page():
  driver = webdriver.Firefox()
  driver.get("http://website.example.com")
  driver.find_element_by_id("button").click()
  assert driver.title == "New Page"

```


Acceptance tests make up the top of the Testing Pyramid. They’re considered important [but should be used sparingly](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html). They are even slower than integration tests and can have serious nondeterminism issues. This is especially true with browser automation, as the browser still has to wait on server response, load all of the assets, run js, etc. And what happens if the server never responds? The test would hang unless you include a timeout, but then what if the server is responds, just slowly? And we haven’t even discussed the challenges of simulating the entire system, or dealing with third-party interactions. Once we get to the level of “product” we’re dealing with reality and reality is pretty damn hard to test.


Another problem with acceptance tests is it’s hard to isolate them, especially if the program is supposed to have effects, *especially* especially if the driver also has state.


#### Feature Tests


A test that also acts as documentation for the user. Feature tests are defined by their syntax, not their semantics or scope. This was popularized by the BDD movement and the [Cucumber](https://cucumber.io/) tool in particular. Their goal was to make it possible for business clients to both [understand the tests](https://martinfowler.com/bliki/BusinessReadableDSL.html) and, hopefully, write some themselves. Here’s an example of what Gherkin (the testing DSL) looks like:


```
SCENARIO: Trying to withdraw too much money
  GIVEN I have $10 in my account
    AND I have $0 in my pocket
  WHEN I try to withdraw $15
  THEN I have $0 in my account
    AND I have $10 in my pocket

```


Each line would match to a regex rule with a corresponding code snippet, and the parser would construct an automanual test out of the matching snippets. Since the snippets can be arbitrary, this means that you could describe unit tests, integration tests, and acceptance tests in this style.


Feature tests simultaneously try to be tests, specifications, and documents. Unfortunately, all three of these have different requirements, f.ex a good specification isn’t necessarily a good test. This can make striking the right balance very challenging, and in practice this has impeded wider adoption of feature testing.1


#### Diff Tests


A test that compare the output against some reference data to see if they match. What makes this different from ‘regular’ automanual tests is that a failure could iindicate the *reference* is out of date. For example, if you are diffing against an html output, changing the internals of your server shouldn’t change the output but changing the layout of the webpage should. If you do the latter, the proper way to fix the failing test is to update the reference output.


Diff testing is heavily used where there’s no way to “break down” the output into decoupled parts, such as [screenshots](http://techblog.hotwire.com/2016/05/19/image-comparison-in-automated-testing/) or [graphics](https://blogs.unity3d.com/2016/12/21/graphics-tests-the-last-line-of-automated-testing/). It’s also used for comparing large amounts of structured data, such as [html](https://facebook.github.io/jest/docs/en/snapshot-testing.html).


#### Parameterized Tests


A test template that takes a set of parameters and generates a test from that. The tester manually determines a list of such sets to pass in, with the intent of checking multiple cases. As an example, a single unit test versus the parameterized version, using the syntax of the [DDT](http://ddt.readthedocs.io/en/latest/example.html) Python library:


```
def individual_test():
  assert 1 + 2 == 3
  assert 1 + 3 == 5
  assert 1 + 4 == 6

@data(*[(1, 2, 3), (1, 3, 5), (1, 4, 6)])
def parameterized_test(a, b, c):
  assert a + b == c

```


In addition to being more compact, the parameterized test provides more information. In Python, the first test will fail on the second statement and never check the third statement. The parameterized test, though, will generate three subtests and evaluate them all, correctly surfacing both errors.


Parameterized tests are usually unit tests, but this seems more of a social thing than a technical restriction. Most libraries will let you load a file of values in for the test. They still count as automanual tests, though, as a human is expected to come up with all of the individual cases.


# Generative Tests


In **generative** tests, instead of specifying the whole test the programmer defines an assertion, a test template, and input rules. The program is then free to search for an input that makes a failing test. The search can be *exhaustive*, meaning it will check every possible input, or *nonexhaustive*, where it only tries a subset. Since most functions can take an infinite number of possible inputs, exhaustive generative tests are pretty rare.


Generative tests are more powerful than automanual tests, as they explore a much wider space. A unit test might test one input, while a property test might check several hundred. For this reason, generative tests are often better at finding edge cases or integration bugs than humans are. The price is specificity: while automanual tests give you complete information about a single input, generative tests only give you partial information on a range of inputs. They also often require more testing infrastructure than automanual tests do.


A common concern with generative testing is that, since most are probabilistic, they might have nondeterministic failures. For this reason most testing libraries track failing cases to specifically retry on future runs.


#### Property Tests


Tests which check that the code preserves some **invariant** on the input space. This is the most common type of generative test. An example, using the [Hypothesis](http://hypothesis.readthedocs.io/en/latest/index.html) Python library:


```
@given(lists(integers(), min_size=1))
def test_f_in(l):
  assert f(l) in l

@given(recursive(booleans(), lists))
def test_flatten_reduces_depth_by_one(l):
  assume(max_depth(l) > 1)
  assert max_depth(flatten(l)) == max_depth(l) - 1

```


The first asserts that for the user-created function `f`, `f(l)` will never return something outside of `l`. The second asserts that the `flatten` function will always reduce the nested depth of an arbitrarily nested list of lists by one, ie `max_depth(flatten([[],[[]]]) = 2`.


Most PBT frameworks also provide *shrinking*, where they take a failing test and find the smallest possible failing input. For example, if we are asserting that for all integers `2*x > x`, Hypothesis might first find `x = -12491` as a counterexample, but would quickly shrink that down to `x = 0`.


Finding good invariants to test can be a very difficult problem. Property testers often [collect ideas](https://fsharpforfunandprofit.com/posts/property-based-testing-2/) for invariant “tactics” they can apply to many kinds of problems.2 A popular one is the [encode/decode](https://hypothesis.works/articles/encode-decode-invariant/) invariant, where you check that a property is reversable. Another is the [oracle](https://www.hillelwayne.com/post/hypothesis-oracles/) invariant, where you decide in advance what the answer is going to be and back-construct the test to match it.


Many property testers frame PBT as [verifying mathematical properties](https://fsharpforfunandprofit.com/posts/property-based-testing/), but that’s certainly not the only way to think about it.


#### Fuzz Tests


Tests where you don’t assert anything on the output. If the program doesn’t do something “stupid”, like crash or memory leak, then the test passes. One of the oldest forms of testing, dating back to when programmers would pull [punch cards out of the trash](http://secretsofconsulting.blogspot.com/2017/02/fuzz-testing-and-fuzz-history.html) and feed them into programs.


Fuzzers are usually classified by how they generate their inputs. *Dumb* fuzzers use random junk as inputs, like passing `]9{{{{` as JSON. *Structured* fuzzers pass in valid data to confirm that the program handles them properly, like [passing](https://gist.github.com/jimbojw/448057) `{"/*":"*/","//":"",/*"//"*/"/*/"://\n"//"}` as JSON. Since that’s valid JSON, the program shouldn’t violate any internal assertions or invariants in processing it.


*Genetic* or *evolutionary* fuzzers adapt their input to the program responses, for example by measuring which inputs lead to higher memory consumption. The most famous fuzzer in this category is [American Fuzzy Lop](http://lcamtuf.coredump.cx/afl/), which is smart enough to generate valid jpegs from [first principles](https://lcamtuf.blogspot.com/2014/11/pulling-jpegs-out-of-thin-air.html).


Fuzz testing is heavily used in systems programming and infosec. For higher level systems people usually fuzz via a mix of property testing and code contracts. Combining fuzzing and contracts makes for a pretty decent integration test.


#### Model tests


Model tests generalize PBT. The test is modeled as a [state machine](http://hypothesis.readthedocs.io/en/latest/stateful.html) and can choose its own transitions. That way not only can the test search for failing inputs, it can also search for failing steps. This is still in the realm of “wildly experimental” so here’s some handwavey pseudocode:


```
@rule(i=integer())
def add_to_stack(i):
  stack.attempt_push(i) 

@rule
def pop_from_stack():
  stack.pop()

@rule
def add_top_two():
  i = stack.pop()
  j = stack.pop()
  stack.attempt_push(i + j)

@invariant
def stack_is_unique():
  len(stack) == len(set(stack))

@test
def start_from_empty():
  apply_rules(empty_stack())

```


In this case we have an (admittedly arbitrary) implementation of a stack that’s supposed to be unique. The test is required to start with an empty stack but otherwise is allowed to apply whatever rules it wants with whatever values it wants to whatever depth it wants.


While generalized model testing is mostly unexplored territory, we’ve historically used it to find complex concurrency bugs, such as with the [Go Race Detector](https://blog.golang.org/race-detector). Another special case is *model-based* testing, where you use transition system to drive both the code and a [simplified code model](https://medium.com/@tylerneely/reliable-systems-series-model-based-property-testing-e89a433b360), then make sure they match. I’ve also seen experiments on using transition systems to cover [UI interactions](https://www.youtube.com/watch?v=HXGpBrmR70U)3 or derive tests from [UML diagrams](https://pdfs.semanticscholar.org/a158/b0ec69344d7e69513807d94d193e17b664bf.pdf).


The biggest issue with this is that the explorable space can get extremely large. You also can’t easily shrink the failing examples, so it can be hard to find out what *actually* caused the bug. Usually people take a failing path test, investigate it, and then write a more specific automanual bug. The EiffelStudio IDE tries to [do this automatically](https://www.eiffel.org/doc/eiffelstudio/Using%20generated%20tests) but it’s relatively crude.


The other biggest issue is that they can require significant infrastructure to set up and run, which means that there’s a good chance that your testing code will have bugs in it. A lot of people don’t like the idea of having to test your tests. However, the payoff can be pretty big for complex systems.


# Miscellaneous Tests


#### Mutation Tests


A means of ensuring your tests are nontrivial and properly cover your code. Mutation tests rerun your other tests on randomly modified versions of the code: `if(x)`replaced with `if(!x)`, `false` flipped with `true`, etc. If your tests still pass, they’re probably broken. Mutation testing usually doesn’t find errors in your code, but it *does* find errors in your tests.


#### Doctests


Tests embedded in your documentation. They’re usually unit tests or property tests, rarely more complicated than that. Their purpose is to validate the *documentation*: if the doctest fails, then your documentation is wrong or out of date.


```
def add(a, b):
  """ This subtracts the two numbers from each other.
  >>> add(1, 2)
  -1
  """
  return 1 + 2

```


This is intended to help keep the documentation in sync with the code. If you update the code but forget to update the docs, the doctest will alert you.


This list is non-exhaustive, but if there’s an obvious kind I missed, feel free to ping me.


---

1. I’m irrationally against feature testing because they’ve gotten everybody to think that tests are specs, which (like contracts) are a different thing entirely.
 [return]
2. There’s no widely-used term for this kind of thing, but I like *tactic* a lot and that’s how I think about it my head.
 [return]
3. I call “a script that randomly clicks buttons on the GUI and sees if anything crashes” a *salamander* and I have no idea why.
 [return]
