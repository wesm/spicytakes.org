---
title: "Proving Games are Winnable with Alloy"
date: 2018-01-15
url: https://www.hillelwayne.com/post/alloy-randomizer/
slug: alloy-randomizer
word_count: 3510
---

One of my vices is watching [Link to the Past Randomizer games](http://vt.alttp.run/). This gist is it’s a regular Zelda game except all of the items in chests are randomized. A chest that normally has bombs might have a critical item, while the chest that’s supposed to have the moon pearl might only have 10 rupees. People use randomizers to run races, since you can’t just memorize the “correct” path through the game.


![](race1.png)

*This was supposed to be the bow.(source)*


Of course, there are some restrictions. The game must still be finishable, which means all of the items you need to beat the game must still be accessible. If you need the hammer to reach a chest, putting the hammer in that chest will make the game unwinnable. Any randomized assignment that does that is invalid and must be avoided. The randomizer takes care of that by tracking what’s been placed and adding restrictions on what to place next.


![A place the hammer can't be](race2.png)

*The hammer can't be in this chest or the game is unwinnable.*


Can we guarantee that a given set of rules is enough? We can check with unit tests, but tests don’t give us 100% certainty. If we want that, we need to use formal methods. So let’s use formal methods! We’ll construct a model of the game, place some restrictions, and check that every possible item assignment leads to a winnable game.


I normally do all my modeling in TLA+, but I want to try using [Alloy](http://alloytools.org/) here. Alloy was inspired by relational algebra and has been used to model data structures and [security systems](http://alloytools.org/citations/case-studies.html). It’s also a lot more lightweight than TLA+ which is why I want to do a short demo.


We’ll start with a couple of **signatures**, which represent the possible **atoms** that relate to each other. In our case, we’ll start with two: chests and items.


```
sig Chest {}

sig Item {}

```


Next we’ll add a **relation** between them. Each chest has one item it requires to open and one item it contains.


```
sig Chest {
  requires: Item,
  contains: Item
}

```


Most model checkers only look for counterexamples. Alloy can also do the opposite, look for an example of what a consistent model looks like. Alloy can also visualize the examples so you can see if your model looks “off” in any way. We haven’t fleshed out our model at all, so let’s see what we have with `run {}`.


```
Generating CNF...
Generating the solution...
211 vars. 24 primary vars. 320 clauses. 32ms.
Instance found. Predicate is consistent. 46ms.

```


By default, Alloy will search for all examples with up to three atoms of each signature. The search takes under 50 milliseconds. For a verifier, Alloy is pretty damn fast!1 I skimmed the visualizations and found this one:


No chest contains Item1. Is this a problem? No, there’s plenty of chests in LttP that don’t require *any* items to reach; we can just assume that Item1 was in one of those “free” chests. On the other hand, Item2 is contained in two separate chests. This *is* a problem: you can only get an item from one chest.2 This is a physical property of the game, so this particular instance is straight up impossible.


We can exclude examples by adding a **fact**. The analyzer will only check instances where the fact holds. If it doesn’t, that particular instance can’t be used as an example or a counterexample. It simply can’t occur.


```
fact ChestsHoldUniqueItems {
  all i: Item | lone c: Chest | c.contains = i
}

```


`lone` means “at most one”. An item either belongs to exactly one chest or no chest at all and is “free”. Not all chests may contain items, either, since some will contain rupees or arrows or whatever. We’ll adjust the signature to match:


```
sig Chest { 
  requires: Item,
  contains: lone Item
}

```


### Adding some predicates


The chests, and the requirements to reach each chest, are fixed. The types of items are fixed, too. It’s only which chests contain which items that is randomized. We can add specified items and a fact that relates the requirements.


```
abstract sig Chest { 
  requires: Item,
  contains: lone Item
}
one sig A, B, C extends Chest {}

abstract sig Item {}
one sig Bow, Glove, Boots, Sword extends Item {}


fact ChestRequirements {
  A.requires = Boots
  B.requires = Bow
  C.requires = Glove
}

```


We do have to change the signatures to **abstract** sigs so that the **extensions** are considered exhaustive. Obviously, we’re dealing with a very simplified model; I’m not modeling all of the randomizer for a blog post.


Now we need a **predicate**. A predicate is a statement about the model that may or may not be true. Our ultimate goal is to see if certain predicates guarantee other predicates. Ultimately, we’ll be checking something like `restrictions implies winnable`; if our randomizer follows all of the restrictions we give it, the game must be winnable. Unlike facts, predicates can take atoms as arguments. As this is just a simplification, we’ll say that the only things you need to win is the sword and the boots.


```
pred reachable(i: Item) {
  i in free
}

pred winnable {
  reachable[Sword] and reachable[Boots]
}

```


As a quick prototype, the only way to reach an item is if you start with it. `free` will be a **function** (which is exactly what it sounds like).


```
fun free: set Item {
  {i: Item | no contains.i}
}

```


Why can we say `contains.i`? `contains` is a relation on Chest, not Item! This is one of the core features of the Alloy language: relations are just tuples of atoms. `requires` and `contains` are sets of these tuples: based on our fact, `requires = {A -> Boots, B -> Bow, C -> Glove}`. `A.contains` takes all the pairs in `contains` that start with `A` and returns whatever item they each end with. This goes both ways, so `contains.Boots` takes the pairs that end with `Boots` and returns whatever chest they each start with. We can also apply relations to entire sets at a time: we could have written `free` as `Item - Chest.contains`, too.


Now let’s finish `reachable`. We currently have that only free items are reachable. But you could use a free item to open a chest, so we should write `i in free + requires.free.contains`. But we could use *those* items to open further chests, which is `requires.(requires.free.contains).contains`, and then do that *again*, for…


Okay, backtrack time. `~` inverts a relationship. `requires` is `Chest -> Item`, so `~requires` is `Item -> Chest`, and represents which items open which chests. `~requires.contains`, then, is `Item -> Item` and represents which items make which items directly accessible. Next, we apply the **transitive closure** operator `*`: `a.*b = a + a.b + a.b.b + ...`. This means our `reachable` predicate can be written as


```
pred reachable(i: Item) {
  i in free.*(~requires.contains)
}

```


By running `run {winnable}`, we can find an example of a winnable instance. If we instead write `check {winnable}`, we’ll see if there are *unwinnable* instances. If we do that, we’ll find a counterexample.


The problem here is obvious: we can’t have a chest that contains the item you need to open it. Time to start adding restrictions. We’ll do this in its own predicate and change our assertion to `restrictions implies winnables`. In other words, it’s okay for completely random maps to be unwinnable, but if these restrictions hold the map *must* be winnable.


```
pred restrictions {
  all c: Chest | c.requires != c.contains
}

check {restrictions implies winnable}

```


Even with this, the analyzer finds an unwinnable map:


We need the glove to get the boots and the boots to get the glove. No chest contains its own requirement, but we didn’t exclude closed cycles of requirements! We could add that as a restriction, but that seems difficult to implement in code. Let’s find something simpler, first. What if we forced the boots to always be free?


```
pred restrictions {
  all c: Chest | c.requires != c.contains
  Boots in free
}

```


```
Generating CNF...
Generating the solution...
405 vars. 24 primary vars. 536 clauses. 41ms.
No counterexample found. Assertion may be valid. 46ms.

```


Perfect! Here’s where our model currently stands.


```
abstract sig Chest { 
  requires: Item,
  contains: lone Item
}
one sig A, B, C extends Chest {}

abstract sig Item {}
one sig Bow, Glove, Boots, Sword extends Item {}


fact chestRequirements {
  A.requires = Boots
  B.requires = Bow
  C.requires = Glove
}

fun free: set Item {
  {i: Item | no contains.i}
}

pred reachable(i: Item) {
  i in free.*(~requires.contains)
}

pred winnable {
  reachable[Sword] and reachable[Boots]
}

fact chestsHoldUniqueItems {
  all i: Item | lone c: Chest | c.contains = i
}

pred restrictions {
  all c: Chest | c.requires != c.contains
  Boots in free
}

check {restrictions implies winnable}

```


### Adding a trace


We’ve been assuming that every chest requires only one item. Most chests require several items, though. Usually you need at least one to get into the area itself, and then a couple more to reach the chest itself. We’d assume that the right way to do this would be to make the `requires` relation a set of items, instead of a single item.


```
requires: set Item

fact chestRequirements {
    A.requires = Boots + Bow
}

```


*This doesn’t work*. Here’s something very, *very* important about Alloy: it does not support multisets. `A -> (B + C)` is not a single relation `A -> {B, C}`. It’s flattened into *two* relations, `{A -> B, A -> C}`. Our `reachable` is a transitive closure over all relations, so it actually acts as an “or”. `A`’s requirement is satisfied if you have the boots *or* the bow.


To get an “and” relation, we need to rewrite `reachable`. What if we used a recursive predicate?


```
pred reachable(i: Item) {
    i in free or all items: (contains.i).requires | reachable[items]
}

```


This doesn’t work, either. Another important thing: Alloy doesn’t like recursion. The call to `reachable[items]` will fail as “`reachable` cannot call itself recursively”. There is an option to add recursive calls, but it is incredibly slow (for Alloy) and has a max depth of 3. Good for demos, less good for real work.


Alternatively, we could replace `reachable[items]` with `items in free`, but then we’re back to before: we can’t use items in chests to open other chests. We need a different approach.


The proper Alloy solution is to use the “trace” pattern. An item’s reachability isn’t just a boolean. The items are also partially ordered on their reachability. If A is a requirement of B, then you know that B is reachable after A. One way to figure out the ordering is to imagine the player doing the following:

1. After starting the game, the player goes around and collects all of the free items. This makes up their first inventory.
2. The player then collects any items that require only free items. These, plus the free items, make up the second inventory.
3. The player then collects any items that require only items in the second inventory, etc etc etc.


Under this process, we gradually place all of the reachable items into an inventory. If at any point we collect both the Boots and the Sword, we win.3 While the items in the inventories are partially ordered, the inventories themselves are totally ordered. If we apply the `ordering` module to them with `open` we get a bunch of nice properties for the signature, like `first`, `last`, and `next`.4


```
open util/ordering[Inventory]

sig Inventory {
    items: set Item
}

```


Then we define our trace. The first inventory has all the free items. Successive inventories have the same items, plus whatever else we can access with the current inventory.


```
fact Trace {
  first.items = free
  all inv: Inventory - last | 
    let inv' = inv.next |
      inv'.items = inv.items + {i: Item | reachable[i, inv]}
}

```


Finally, we adjust our predicate to say an item is reachable if all the required items are in the current inventory:


```
pred reachable(i: Item, inv: Inventory) {
  i in inv.items or all i': (contains.i).requires | i' in inv.items
}

```


We have to do some minor adjustments to the rest of our model, e.g. change win condition and our restriction to `contains not in requires`. After all of this, we see something interesting. Not only are there are still counterexamples to our model, there aren’t any examples! Instead of making it impossible to lose, our restrictions made it impossible to win.


Here’s where we currently are:


```
open util/ordering[Inventory]

sig Inventory {
  items: set Item
}

abstract sig Chest { 
  requires: set Item,
  contains: lone Item
}
one sig A, B, C extends Chest {}

abstract sig Item {}
one sig Bow, Glove, Boots, Sword extends Item {}


fact chestRequirements {
  A.requires = Boots + Bow
  B.requires = Bow
  C.requires = Glove
}

fun free: set Item {
  {i: Item | no contains.i}
}

fact Trace {
  first.items = free
  all inv: Inventory - last | 
    let inv' = inv.next |
      inv'.items = inv.items + {i: Item | reachable[i, inv]}
}

pred reachable(i: Item, inv: Inventory) {
  i in inv.items or all i': (contains.i).requires | i' in inv.items
}

pred winnable {
  some inv : Inventory |
    reachable[Sword, inv] and reachable[Boots, inv]
}

fact chestsHoldUniqueItems {
  all i: Item | lone c: Chest | c.contains = i
}

pred restrictions {
  all c: Chest | c.contains not in c.requires
  Boots in free
}

check {restrictions implies winnable}

```


And here’s what a counterexample looks like:


It’s starting to get cluttered. Alloy provides a bunch of tools to make diagrams easier to explore, projecting over signatures. Worst case, you can inspect the text dump, which people save for the *really* complicated counterexamples.


### Ands and ors (or ands or ors?)


What if we do want alternate requirements? Maybe the chest can be opened if you have the bow+boots *or* the sword. Right now we can only express and relationships. To do this, we need one more layer of indirection. Instead of chests directly having requirements, chests have sets of puzzles, where each puzzle has a set of requirements. Then we can open the chest if we have all the items for at least one puzzle.


```
abstract sig Puzzle {
  solution: Chest -> set Item
}
one sig PA0, PA1, PB0, PC0 extends Puzzle {}


fact chestRequirements {
  PA0.solution = A -> (Boots + Bow)
  PA1.solution = A -> Sword
  PB0.solution = B -> Bow
  PC0.solution = C -> Glove
}

```


We make the Puzzle sig abstract since the puzzles per chest are fixed.5 `solution` is a triplet relation of form `Puzzle -> Chest -> Item`. We have to change our requirements to something a little jankier, to account for there being multiple puzzle solutions.


```
pred reachable(i: Item, inv: Inventory) {
  i in inv.items or
    some p: Puzzle |
      let sol = p.solution[contains.i] |
        some sol and sol in inv.items
}

```


To simplify we added a **bracket**, which acts how you intuitively expect it to. Internally, `A.B[C] = C.(A.B)`. We also add `some sol` to weed out irrelevant solutions, which would have empty item sets.


We also need to update our restriction. In fact, we can weaken it: it’s okay for a chest to contain its own requirement as long as there’s some alternative way of opening it.


```
pred restrictions {
  all c: Chest | some sol: Puzzle.solution[c] | c.contains not in sol
    Boots in free
}

```


This has counterexamples. But if we change it to `Sword in free`, there’s no counterexamples. There are also satisfying examples, so these two restrictions lead to playable games. Our final model:


```
open util/ordering[Inventory]

sig Inventory {
  items: set Item
}

abstract sig Chest { 
   contains: lone Item
}
one sig A, B, C extends Chest {}

abstract sig Item {}
one sig Bow, Glove, Boots, Sword extends Item {}

abstract sig Puzzle {
  solution: Chest -> set Item
}
one sig PA0, PA1, PB0, PC0 extends Puzzle {}


fact chestRequirements {
  PA0.solution = A -> (Boots + Bow)
  PA1.solution = A -> Sword
  PB0.solution = B -> Bow
  PC0.solution = C -> Glove
}

fun free: set Item {
  {i: Item | no contains.i}
}

fact Trace {
  first.items = free
  all inv: Inventory - last | 
    let inv' = inv.next |
      inv'.items = inv.items + {i: Item | reachable[i, inv]}
}

pred reachable(i: Item, inv: Inventory) {
  i in inv.items or
    some p: Puzzle |
      let sol = p.solution[contains.i] |
        some sol and sol in inv.items
}

pred winnable {
  some inv : Inventory |
    reachable[Sword, inv] and reachable[Boots, inv]
}

fact chestsHoldUniqueItems {
  all i: Item | lone c: Chest | c.contains = i
}

pred restrictions {
  all c: Chest | some sol: Puzzle.solution[c] | c.contains not in sol
  Sword in free
}

check {restrictions implies winnable}

```


### Thoughts


Some people have asked me to do a full “TLA+ vs Alloy” post. This is not that post, but I can share some thoughts on Alloy.


First of all, it’s really lightweight for a modeler. Even our most complex model checked in under 150 ms. Also, it’s tiny. This example covered almost all of the language features, which means it’s pretty close to what a practical Alloy spec looks like. By contrast, for the [TLA+ example](https://www.hillelwayne.com/post/modeling-deployments) I did a while back, I contorted the spec around minimizing the stuff I had to introduce. Alloy is just a lot simpler.


I also like the UX a lot. There’s a REPL for quick exploration, the visualizer makes presenting data easy, and you’ve got a ton of debug info. The visualizations are customizable, too, and you can project them over a signature or relation. That means when you do have a counterexample, you can easily inspect it or run queries.


Alloy’s simplicity is also a weakness. It’s pretty tuned to inspecting relationships in data structures. The further you get from that, the harder things get. In particular you shouldn’t use it to model dynamic systems. We saw it could handle linear time dependence, but even that got a little hairy. Concurrency or liveness checking? Not a chance.6


All in all, I like Alloy. It’s not as flexible or powerful as other formal methods tools, but it’s fun and you can get up and going pretty quickly. And it’s good for its niche. For the record, this problem is *not* part of that niche.


If you’re interested in Alloy, there’s the [main site](http://alloytools.org/), a [really good book](https://mitpress.mit.edu/books/software-abstractions-revised-edition), and this neat [puzzle builder](http://alloy4fun.di.uminho.pt/) I found. If you’re interested in zelda randomizers, sorry for making you sit through 2000 words about formal methods. You can find the main site [here](http://vt.alttp.run/) and the source code [here](https://github.com/sporchia/alttp_vt_randomizer/).


### Update


I’ve been chatting with Daniel Jackson, the inventor of Alloy. He’s an incredibly friendly and intelligent guy. I realized in the conversations that this post might be casting Alloy as a fun toy, but unsuitable for solving “real” problems. This is absolutely not the case! I’ve used it to design constraints on relational data and it works beautifully for that. Here are some other things people have done:

- [Verifying security of internet protocols](https://www.adambarth.com/papers/2010/akhawe-barth-lam-mitchell-song.pdf)
- [Fixing Meltdown and Specter exploits](https://arxiv.org/pdf/1802.03802.pdf)
- [Designing medical devices](https://homes.cs.washington.edu/~emina/doc/neutrons.snapl15.pdf)
- [Checking memory consistency models](https://johnwickerson.github.io/papers/memalloy.pdf)


It’s a pretty damn useful language and you should definitely consider adding it to your toolbox.


*If you enjoyed this, why not send me an [email](mailto:hwayne@gmail.com)? Tell me something you’re excited about!*


---

1. Alloy translates your model into a SAT problem before looking for solutions. While this is much faster than a brute-force state search, it means Alloy has some restrictions on what it can check. Most notably, you can’t check unbounded models.
 [return]
2. Technically untrue: some items have upgrades, and can be represented with duplicates. The first time you find the item, you get the base version, the second time you get the first upgrade, etc. We’ll exclude that case for simplicity.
 [return]
3. “What if the game is winnable but there aren’t enough Inventory atoms to reach all the items?” Then it’ll be a false positive. We can specify how many Inventories there are when running the model, but managing finite traces is a bit of an art. And infinite traces are impossible by design.
 [return]
4. In fact we can use these unqualified, since there’s only one ordered signature. If we had two, we’d have to write `Inventory.first` and such to be unambiguous.
 [return]
5. Again, technically untrue. Depending on the mode, the puzzles might change. Fex there might be fewer solutions if you’re doing a glitchless run.
 [return]
6. Counterpoint: Pamela Zave used it to break the [Chord protocol](http://www.pamelazave.com/chord.html). Countercounterpoint: Zave is so far beyond us mortal coders that we couldn’t possibly extrapolate from that.
 [return]
