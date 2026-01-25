---
title: "We've Already Thought the Unthinkable"
date: 2018-02-09
url: https://www.hillelwayne.com/post/thinking-the-unthinkable/
slug: thinking-the-unthinkable
word_count: 1752
---

I recently read Tomas Petricek’s [Thinking the Unthinkable](http://tomasp.net/blog/2016/thinking-unthinkable/), where he argues that modern PLT makes several restrictive assumptions about the nature of programming. Our reliance on mathematics in CS is not fundamental and our obsession with formal logic and algorithms keeps us from seeing other possible paradigms. He proposes two other unthinkable paradigms that are unrelatable to modern mathematical programming.


I disagree with his premises: I think there’s a very valid reason to ground aspects of programming in mathematics. However, I want to focus on his core conclusion: that other paradigms are ‘unthinkable’. I’d like to argue that both of his proposed paradigms are 1) implemented, 2) at least somewhat explored, and 3) mathematically formalizable.


## Programming as Taxonomy


> Theoretical computer scientists try to extract mathematical essence of programming languages and study its formal properties. Now consider a kind of knowledge that instead aims to explore the design space and build a taxonomy of objects (ideas, concepts, …) that occupy the space. It considers the entities as they are, rather than trying to extract their mathematical essence. What would be the consequence of such way of thinking that attempts to relate and organize programming ideas in taxonomies, rather than abstracting?


Petricek proposes a paradigm where we create a taxonomy of objects and explore the relationships between them. It’s programming with connections versus abstractions, data versus algorithms.


This is no different from OOP. While modern OOP has mostly collapsed into “implements”, “is-a” and “has-a” type relationships, historically there was a much wider variety. For example, Business Object Notation had concepts for aggregates, while OOSE included “traces” and “controls”.


![](relations.png)

*Source*


The taxonomy fad reached its peak between 1980-1995 during a period called the “method wars”. OOP was new and everybody thought it was the key to building large, complex systems. They just disagreed on *how* it did that. By 1991 there were over 50 different methods, all with corresponding sets of useful relationships. Eventually, the biggest methods merged into the notation we now call UML.1


While OOP was concerned with representing reality, it also had several means of formalization. The most popular is probably **contracts**. Most famously associated with Bertrand Meyer, contracts are an implementation of **Hoare logic**.2 Every procedure has precondition and postconditions that must hold: if either are violated, the program is formally invalid. I talk a little more about it [here](https://www.hillelwayne.com/post/contracts), but the key thing here is that in OOP, *contracts affect relationships.* For “implements” relationships, the contract rule is “the whole public API must be available”. For inheritance, the rule is “preconditions cannot be strengthened and postconditions cannot be weakened.” Nobody’s really explored how contracts affect other types of relationships, which I’m going to chalk up to a lack of academic interest. I agree with Petricek there.


Like any paradigm, taxonomy programming has both power and limitations. One of the most difficult problems is something I’m going to name **Kent’s Law**, after the phenomenal book [Data and Reality](https://www.amazon.com/Data-Reality-Perspective-Perceiving-Information/dp/1935504215):


> All nontrivial classification systems inevitably ban some useful categories.


An example of this is inheriting a sum type: in almost all OO languages, you can’t say that objects of A *either* inherit from B or inherit from C, but not both. In most cases you can work around this, for example by composing with a sum type instead of inheriting, but that’s still fundamentally a workaround. There’s a possible category that could be useful to our purposes and that we can conceive of in abstract, but in the actual classification systems we used it’s impossible to represent.


Another big problem is something I’m *also* going to name **Kent’s Law**, because his book is *seriously that good*:


> All taxonomies have horrible edge cases.


This is because reality is way too messy to categorize. All people have a birthday? Does “King Arthur” have a birthday? Is that even a useful question?


Okay, I’m getting a little off topic. The point is that taxonomic programming isn’t a new paradigm: it’s one we’ve seen before, if not deeply explored.


### Metaphorical Programming


> Signs and resemblances provide the missing link between layers. In object-oriented design, an object is a metaphor for an object in the real-world, but metaphors can be found in many areas of programming. We use them to conceive an idea and use our intuition at the higher level to guide design at lower levels. Since our scientific way of thinking does not consider such resemblances important, we then hide them (for brevity, or out of disinterest) from our published narrative.


If I understand correctly, the idea behind metaphorical programming is that we’re mixing human abstraction and language actions. If the metaphor is “plants”, then the user can infer the existence of a `grow` operation and intuit what it, from a programming perspective, actually does. The user could also intuit some behavior of the system as a whole: they could extend the metaphor to the program “blooming”, “reproducing”, and eventually dying. Unlike with taxonomic programming, I don’t think there’s as strong a case to be made that we’ve “done” metaphor programming. Nonetheless, I think there are still a couple of interesting takes we *have* seen.


The first are APLs. APLs are considered functional programming languages, which seems to me an admission that nobody really knows what’s going on with them. They treat everything as arrays, have a ridiculous number of primitives, and consider readability  a wasteful luxury. In J there’s approximately 200 primitives, all of them 1-2 characters and with at least two unrelated use cases.


```
  1 2 3 * 4 5 6
4 10 18
  3 * 4 5 6
12 15 18
  * 4 5 6
1 1 1
  *. 4 5 6
4 0
5 0
6 0

```


The APLs might seem insane, but there’s a hidden genius in them. Kenneth Iverson, the inventor of APL and J, believed that our modes of thought were based on the tools we had. I’m not going to see the value of `map` if my language doesn’t have higher order functions! By adding the right primitives, [he argued](http://www.jsoftware.com/papers/tot.htm), we could use APL to see problems in entirely new ways. This seems to be a form of metaphorical programming, where the metaphor is arithmagic.


So how does this play out in practice? Let `c` be a set of N-dimensional points. Which two points in c have the furthest Euclidian distance between them?


```
  NB. Rotated for clarity
  |: c [ c =: ? 15 3 $ 100
25 39 48 25 51 29 34 16  2 49 10 21 85 88 65
89 23  7 18 83 93 73 68 47 53 87 46  4 78 57
21 19 48 46 58 58 87 96 59 13 65  8 37 16 31
   
   farthest =: 3 : 0
 t =. +/&.:*:@:-"1/~
 i =. (-. #)@:(i."1 >./@:,)
 (i t y) { y
)
   farthest c
85  4 37
10 87 65

```


I want to call attention to `t` in particular. That’s a J verb defined as “create a table where for indices i and j in y, cell (i, j) of the table is `|y[i] - y[j]|`.3 Most languages don’t even *have* a ‘table’ primitive. In J, it’s just one of dozens of other primitives. Thinking in metaphors. APL also is easily formalizable as math: it’s simply not math in the theory-heavy, proof-based form most CS is. Rather, it’s math in the common, day-to-day form of arithmetic and spreadsheets and statistics. Math that’s easy to check by hand, done a million times faster.


The other big source of metaphorical programming I can think of is DSLs and 4GLs. Think Salesforce, LabVIEW, Visual Basic, GameMaker. In AutoHotKey, my basic operations are keystrokes and mouse clicks. In Inform 7, the code is a description of the fiction game you’re constructing. Metaphorical programming is everywhere. They don’t appear a lot in the theory, though, because DSLs are pretty ‘applied’ in nature and don’t necessarily have a whole lot in common. 4


---


I agree with a lot of what Petricek says: we overemphasize lambda calculus and we can learn a lot from alternate paradigms. Where we disagree, I think, is on how “alternate” those paradigms are. Petricek seems to believe they are incommensurate and unrealized. I believe they’re more mundane. Taxonomic and metaphorical programming are already present, we just don’t pay attention to them.


Tomas, if you’re reading this, there are a few languages I’d recommend checking out. They’re all useful, mature, and very different from the usual crop:

- **APLs**. I’m a big fan of J, as you can tell, but Dyalog is popular, too. The interesting thing here is how programming changes when complicated operations are turned into primitives.
- **Inform 7**. Inform is a DSL for making interactive fiction games. It’s natural language, ultra-metaphorical, and has an incredibly advanced IDE. “This is a door that is closed and barred” is a semantically valid statement.
- **Python**. You prob already know this but I want to call attention to how it can leverage dynamic typing to create some really unusual taxonomies. In particular, Abstract Base Classes can use `__subclasshook__` to define what counts as a child class. This means you can easily create categories like “classes with instantiated objects that don’t have relationships with each other.”
- **Eiffel**. Not so much a deep dive, just to see what formalized taxonomies can look like in practice.


Finally, I’d suggest looking at the languages created for the [Code Golf Stack Exchange](https://codegolf.meta.stackexchange.com/questions/6918/what-programming-languages-have-been-created-by-ppcg-users). Some examples include *Marbelous*, where programs are represented as marbles falling down a board, *Retina*, a langauge based entirely on regexes, and all of the [intentionally unusable](https://codegolf.stackexchange.com/questions/61804/create-a-programming-language-that-only-appears-to-be-unusable) languages.


---

1. The rise and fall of UML is actually a pretty wild story. I’m slowly working on a history, which should be done in… 2020 maybe? It’s a big topic. 
 [return]
2. Okay confession I haven’t been able to find out if he introduced the word “contract” or just the term “Design by Contract”. IIRC he wasn’t the first implementer of contract-like code: Liskov beat him with CLU.
 [return]
3. The magnitude calculation is itself super cool: `+/&.*:` means “apply `*:`, apply `+/`, then apply the inverse of `*:`”. In practice this means “square, sum the elements, square root”. That’s just the magnitude!
 [return]
4. Part of it is also, I think, because they’re not aimed at programmers. This makes them less respectable for some bizarre reason. Which is a huge shame: a lot of mindbending, interesting, and useful languages are DSLs.
 [return]
