---
title: "Clever vs Insightful Code"
date: 2021-06-06
url: https://www.hillelwayne.com/post/cleverness/
slug: cleverness
word_count: 1820
---

“Don’t write clever code.” Why not? “Because it’s hard to understand.” People who say this think of clever code such as [Duff’s Device](https://en.wikipedia.org/wiki/Duff%27s_device):


Duff's Device
  
`send(to, from, count)
register short *to, *from;
register count;
{
    register n = (count + 7) / 8;
    switch (count % 8) {
    case 0: do { *to = *from++;
    case 7:      *to = *from++;
    case 6:      *to = *from++;
    case 5:      *to = *from++;
    case 4:      *to = *from++;
    case 3:      *to = *from++;
    case 2:      *to = *from++;
    case 1:      *to = *from++;
            } while (--n > 0);
    }
}
`

show all


This code is “clever” because it exploits knowledge about the language, in this case the peculiarities of fall-through. Clever code can also exploit knowledge about the operating environment or special topics like bit twiddling. Conventional wisdom says this clever code is “bad”.


There’s a second kind of “clever code”: code which exploits knowledge about the *problem*. Consider sorting all 300+ million people in the US by birth date. The “simple” solution is to use quicksort, which has a “log₂ factor” of ~30. The “clever” solution is to exploit the fact that everybody in the US is under 120 years old and instead bucket sort with ~45000 buckets. That sorts the list in a single pass, which is an order of magnitude more efficient.


This kind of clever code can also be easier to understand. Since you’re solving a simpler problem than the general case, you can write less code and make things clearer. This usually ends up being highly domain specific, but one simple example in python is testing if every element of a list is unique:


```
def is_unique(l):
  return len(set(l)) == len(l)

```


We talk about cleverness as if it’s Just Bad, such as “clever code is harder to debug”. That’s going too far. Cleverness can lead to faster, safer, even clearer code. I’m going to call this class of cleverness “insightful” to distinguish them.


### Issues with Insight


Insights can make code faster, simpler, and safer. But it’s also fragile: insights only work because they exploit some property in the problem. If the problem changes, even slightly, the insightful solution might break down. We can’t adapt our implementation of `is_unique` to check whether each element appears *twice*.1 Insight is often non-generalizable: the clever solution for problem will look nothing like the clever solution for a similar one.


This leads into a scalability problem with insightful code: it’s “read-only”. You need a lot of tacit knowledge to consistently come up with useful insights, and that’s not something that transfers between people. I can find an insightful solution to a problem and then find a new insight when the problem perturbs. But if I leave the project, the rest of the team might not be able to do this. They might not have the same skills or background information and can’t be clever in the same way I was.2


This doesn’t mean that insightfulness is *bad*. It just means that we need to account for it in our projects. Requirement changes will disproportionately affect insightful code. It makes sense to document what parts of the codebase use insightful code and what premises we base them on. I’m guessing we can also debug insightful code by reexamining the premises and seeing if any changed, but I haven’t tried this in practice.


### Insight as a confounding factor


A couple years back there was a string of essays on “beating C with $LANGUAGE”, starting with [Beating C with 80 lines of Haskell: wc](https://chrispenner.ca/posts/wc). Chris Penner, working with Haskell, was able to write a wordcount tool that was ~2x faster than [Mac’s default `wc`](https://opensource.apple.com/source/text_cmds/text_cmds-68/wc/wc.c.auto.html). It took him a lot of work to get there, though:


> It may not be immediately apparent how a monoid like this works, but there’s a class of counting problems that all fall into the same category like this, and luckily for me I’ve worked on these before. Basically we need to count the number of times a given invariant has changed from the start to the end of a sequence. I’ve generalized this class of monoid before, naming them flux monoids. What we need to do is count the number of times we change from characters which ARE spaces to those which AREN’T spaces. We could probably express this using the Flux monoid itself, but since we need to be so careful about strictness and performance I’m going to define a bespoke version of the Flux monoid for our purposes.


Penner wasn’t beating C with Haskell, he was beating C with *clever* Haskell. The expert Haskeller may have sufficient insight to hyperoptimize Haskell, but we can’t expect the average Haskeller have that expertise. Also, we’re comparing insightful Haskell to regular C. The standard `wc` Penner used isn’t optimized at all. When someone insightful optimized the C program, [They got a 100x speedup](https://github.com/expr-fi/fastlwc/). Insightful Haskell is faster than regular C and much slower than insightful C.


This isn’t to discount Penner’s work: it’s an impressive showcase of Haskell’s strengths. But it’s a good example of how insight can warp analysis. It’d be easy to read his piece and come away believing that Haskell is genuinely faster than C, completely missing the confounding factor.


I should be clear that this problem isn’t confined to a particular language. Expert C programmers argue they don’t need memory safety, expert Clojurists argue that static types wouldn’t help them, etc. Regardless of the other merits of their argument, they’re all arguing from the perspective of an expert. Experts are more easily able to work around problems. This doesn’t mean their arguments are wrong, nor does it mean they *shouldn’t* rely on their insight. It’s just something we have to be conscious about.


### Insight as an adoption barrier


I’ve set it up as “cleverness is about code trickery, insight is about problem trickery.” That’s not quite true. Sometimes you need insight to write the code in the first place because you can’t encode the solution in the “obvious” way. For example, with [property-based testing](https://increment.com/testing/in-praise-of-property-based-testing/) input generators. How do you generate a list where the first element is the lowest value? In [Hypothesis](https://hypothesis.works/), you could do it with a filter predicate:


```
@given(@s.lists(s.integers())).filter(lambda l: l[0] == min(l))
def test_foo(l):
  ...

```


But that will [filter out too many examples](https://hypothesis.readthedocs.io/en/latest/healthchecks.html), leading to failed healthchecks and long runtimes. You should write a manual generator:


```
@s.composite
def example(draw):
    i = draw(s.integers())
    l = draw(s.lists(s.integers(min_value=i)))
    return [i] + l

```


Almost every interesting generator requires some insight to come up with. That’s a big barrier to people just starting out with PBT, which hurts adoption.


This is especially bad with formal specification languages. A lot of them focus on being easy to verify at the cost of being easy to express things. PRISM, for example, can verify probabilistic properties… but doesn’t have arrays or functions. You need all sorts of insights to cram your problem into the language straitjacket. To model [two workers pulling messages off a queue](https://www.hillelwayne.com/post/queueing-prism/), I used the following insights:

- Because I’m modeling total latency, I don’t need to track individual messages.
- All messages are indistinguishable, so a message queue is just the number of messages in it. “Processing” a message just means decrementing the counter.
- I could represent different messages taking different times to process by probabilistically decrementing the counter.
- If all workers are indistinguishable, I could represent multiple workers as a single step with different chances of removing up to N messages, *and those chances are binomial coefficients.*


That all led to this spec:


```
dtmc

const int N; // Number of tasks

module workers
  left : [0..N] init N;
  queue: [0..N] init 0;

  [enqueue] (queue < left) ->
    0.5: (queue' = queue + 1)
    + 0.5: true;

  [worker] (left >= 1 & queue = 1) ->
        0.5: (left' = left - 1) & (queue' = queue - 1)
        + 0.5: true;

  [worker] (left > 1 & queue > 1) ->
         0.25: (left' = left - 2) & (queue' = queue - 2)
        + 0.5: (left' = left - 1) & (queue' = queue - 1)
        + 0.25: true;

  [] (left = 0) -> true;
endmodule

```


The spec is beautiful but fragile. If I want to model multiple message priorities then I have to start from scratch. I’m confident I *could* come up with something that worked here, but I’d need new insights. Compare to writing a simulation in Python: I wouldn’t have all of PRISM’s guarantees, I wouldn’t have the same analysis power, but I wouldn’t need to be insightful either. I could just represent a message queue with a list. Done.


On one hand, having things like arrays would make expressing PRISM specs much easier. On the other, PRISM’s inexpressivity is the price we pay for its tractability. Maybe we *can’t* make powerful spec languages that don’t require insight to use. It’s an adoption barrier, but there’s no getting around it.


I think a good middle ground could be adding expressive features, but limiting what you can verify with them. So like adding arrays to PRISM, but any spec that uses them can’t use the full verification suite, only a subset. That way people can build expertise with more expressive specs, and when they need advanced verification they know enough to write insightful specs.


---


I’m drawn to this distinction because I feel like our discussions of “clever code” are too constrained. While “pure” cleverness is something we should discourage, “insightful” cleverness seems like something we should be approaching differently. It’s something that often is necessary to make things work and which can be better than the equivalent “boring” code. It’s important to note the use of insight as well as the contextual constraints that made use of insight possible and what happens if they change.


We also should see how it affects our discussions about software. How does “this tool needs insight to use” relate to “this tool is hard to learn”? Are there different expectations of insight in different fields, or at different levels of expertise? Do certain coding approaches depend more on insight than others, and does that affect generalizability?


Are there ways to teach insight? People get some baseline insight as they develop expertise in something, but I don’t know if you can teach insight *on top of that*. My gut says no, but I think I’m wrong here.


*Thanks to [Jimmy Koppel](http://www.jameskoppel.com/) and Eileen McFarland for feedback.*


---

1. This doesn’t mean there’s [*no* insightful solution](https://docs.python.org/3/library/collections.html#collections.Counter), just that it would look different from the one we already had.
 [return]
2. The converse is also true. Insight is domain specific. My replacement could easily be insightful in *other* domains where I am not, and find a completely different solution. This suggests that cleverness is an asset in small, tightly-knit teams, where everybody is having insights at the same time.
 [return]
