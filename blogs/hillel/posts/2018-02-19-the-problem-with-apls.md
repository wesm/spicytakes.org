---
title: "The Problem With APLs"
date: 2018-02-19
url: https://www.hillelwayne.com/post/the-problem-with-apls/
slug: the-problem-with-apls
word_count: 1336
---

Note: I’m coming from this from the perspective of a J programmer. Maybe K or Dyalog or something solved this already, I don’t know, but I would be pretty surprised if they did.


The more I work with an APL, the more I notice a serious problem. Not the weird symbols, you get used to that pretty fast. Not the write-only aspect, that’s annoying but can be solved with a good syntax highlighter. The biggest problem with APLs, in my opinion, is discoverability: it’s hard to know what you’re supposed to be writing.


I’ll use J to demonstrate what I mean. Here’s the [J Vocabulary](http://code.jsoftware.com/wiki/NuVoc). There’s about 200 primitives there. There’s also the [minimal beginning J](http://code.jsoftware.com/wiki/User:Devon_McCormick/MinimalBeginningJ) which is ‘only’ 35 primitives. This isn’t, by itself, a problem. Part of an APL’s power comes from the diversity of primitives baked into the language. Using the right primitives will make your code fast, simple, and elegant.


How do you find the right primitive, though?


Here’s a python program that calculates the mode of a list using just ‘python primitives’: no high level functions, no modules, etc.


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


That’s 177 characters without golfing. It has to go through every single element in order, so it’s slow and not parallelizable. Now for the J:


```
mode =: (i. >./) & (#/.~) { ~.

```


That’s 22 characters. It’s fast, clean, and took 40 damn minutes to write. Most of it was poring through NuVoc to see what I actually needed to use. Was table something I should be using? Reducing? Maybe I was supposed to grade it and cluster the numbers? Sort? I was lucky and stumbled on a phrase for [keys](http://code.jsoftware.com/wiki/Vocabulary/slashdot#dyadic) that got me closer, but I needed to figure out what to *do* with the counts. Find the max, I guess, but how would I use that? I started by trying to find the indice, then when that failed spent a while chasing an equality and tally as a solution before doubling back to using indices and succeeding. Not to mention finagling all of the operations together in the proper fork: I had to eventually draw it out in a whiteboard.


I’m sure a J expert can look at this and say “no you’re supposed to use the Foobar primitive which makes it trivial”, but that’s my whole point: to find the right primitive I have to review 200 of them. I don’t think what I was doing was all that complicated, and all of the primitives I actually used are relatively simple. But when you load up the vocabulary you see nuts and bolts like `{` (select indice) and `$` (get shape) mixed in with things like `|:` (rearrange axes of N-dimensional array) and `#:` (generalized antibase).


And that’s just the basics. Note the `/.` dyadic adverb, aka “key”. `x u/. y` partitions elements of y based on the indices of x, then applies the `u` monad to each partition of y. When I use the same array for both x and y, it gives me the count of each element. Solving this problem meant knowing the right adverb and the right verb, and the right adverb isn’t immediately obvious. Here are some of the other modifiers that J provides:

- The `/.` *monadic* adverb, which partitions y by its antidiagonals before applying u
- The `^:_` conjunction, which finds the fixed point of verb u on y
- The `;._3` dyadic adverb, which applies u to the subarrays in the regular tiling of y
- The `:;` dyad, which partitions y based on **a specified Mealy machine**.


All of these adverbs have *extremely* specific use cases, but they’re mixed in with more general purpose modifiers, like `/` (reduce) and `&` (bond). If I’m doing an arbitrary task, I might need `\` but I probably won’t need `:;`. This gives me proposal one: **label primitives by their complexity.** I’m thinking roughly “basic”, “advanced”, and “expert”. This is under the assumption that ‘basic’ stuff is the most general, of course. ‘Advanced’ is probably anything that is mostly used in a few specified ways, and ‘expert’ is for crazy library builders (and anything involving gerunds). Note that the same symbol can have different complexities for the monad and dyad forms. `{` is a basic dyad but an advanced monad.


That reduces the space I have to look over. To help me narrow in, it’d be good to **label the useful primitives for a problem domain**. If I’m finding or filtering my thoughts should immediately go to `# i. = {`, while for manipulating shapes I might want `$ {. }. {: }:`. If a verb has an unusual use case, we should also list what it belongs to that domain. For example, the `-.` monad is “not”. This is important because filtering is often done with a boolean array. `fy # y` filters y by array fy, and `(-. fy) # y` *rejects* from y by fy. And primitives can, of course, belong to multiple domains: `-.` is also good for boolean logic and probabilities.


Certain primitives are useful to certain domains. In addition, you can construct versatile verbs out of multiple primitives. In contexts where `#` is used as filter, then the corresponding ‘reject’ verb is `(#~ -.)~`. `\` is ‘infix’, `/\` is the more commonly-used ‘accumulate’. J defines `f . g` as `u@(v"(1+lv,_))`, but most people only need it for `+/ . *`, which is ‘matrix product’.


This gives us the last proposal: **create a library of useful components**. These can be both complete components you use directly (`?&$` for ‘random matrix’) and partial components you parameterize (`f#]` for ‘filter on f’). J has a phrasebook that’s supposed to kind of fill this role, but it gives you complete solutions to specific problems, not reusable pieces you can build with. I’m thinking more like intermediates you use to get your final answer.


Here’s what the mode problem would look like with a good component library: I want to find the mode of a list.  That will probably involve using an index, so I’ll be using the `f { ]` idiom where f’s top-level verb will be an `i.` dyad. Thinking it through, if I had the counts `c` for each element I could get the index of the max with `(i. >./) c`. I get the counts by checking the library and finding `#/.~`. I combine everything, watch it raise a length error, and realize the counts of the elements of a list is going to be smaller than the list, since it’s just the nub. I have to replace `]` in the find-by-index idiom with `~.`, and the verb is complete. Instead of 40 minutes, it takes 5.1


In addition to making J more discoverable, a good component library might also make it more parsable. I have to work out what `(f g h) y` is supposed to do, but if I see `(f # ]) y` I immediately know it’s a boolean filter. One interesting possibility is adding semantic highlighting, where we highlight instantiated partial components and tooltip the description.


In summary: when working with an APL finding the right primitive is really tough, and verb classification and a better phrasebook would go a long way towards fixing that.


### Update 10/1/18


[Mike Arntzenius](https://twitter.com/arntzenius/status/1044913763156197376) pointed out an error with the Python. It should actually be this:


```
def mode(l):
  max = None
  count = {}
  for x in l:
    if x not in count:
      count[x] = 0
    count[x] += 1
-    if not max or count[x] > count[max]:
+    if count[x] > count.get(max, 0):
      max = x
  return max

```


Otherwise it blows up on falsey values. Thanks for catching that!


---

1. I hope because it’s actually easier and not because I already solved this problem before.
 [return]
