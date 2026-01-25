---
title: "Solving Knights and Knaves with Alloy"
date: 2019-02-11
url: https://www.hillelwayne.com/post/knights-knaves/
slug: knights-knaves
word_count: 2745
---

There’s a famous logic puzzle, originally from Raymond Smullyan, called a “Knights and Knaves” puzzle. We have a set of people, all of whom are either a *Knight* or a *Knave*. Knights only make true statements, and Knaves only make false statements. Usually the goal of the puzzle is to find out who is what. For example, if we have two people, A and B, and A says “both of us are knaves”, we know A is a knave and B is a knight. If A was a knight, then they’d both be knaves, which is a contradiction, so A is knave. Then we know “both of us are knaves” is false, which means at least one person is a knight. Since A is already a knave, B must be a knight. On the other hand, if A said “both of us are the same”, it would also be a valid for both of them to be knights.


Knights and Knaves puzzles are supposed to be solved through creativity and cleverness: you read the statements and figure out the contradictions. Let’s instead take all the fun out and solve them with a program.


### Alloy


We’re going to use 
  
    [Alloy](http://www.alloytools.org)
  

 for this. I’ve talked extensively about Alloy [here](https://www.hillelwayne.com/post/alloy-randomizer), but that was in regards to modeling complex relational problems. We don’t need that here. Instead, Alloy shines because of its model-*finding* abilities. Not only can it find errors in our spec, it can find examples that satisfy our spec. More importantly it can find *all* matching models, so we can see if a given puzzle has multiple solutions.1


First, the types:


```
abstract sig Person {}

sig Knight extends Person {}
sig Knave extends Person {}

```


By saying `Person` is an abstract signature, there are no people who aren’t Knights or Knaves. In this case Knight and Knave are disjoint, so nobody can be both. This isn’t a strict requirement of the Alloy type system, as we’ll see later. This all means that `Knight + Knave = Person`: the set of knights, unioned with the set of knaves, is equal to the set of people.


Now we’ll define a predicate that corresponds to a puzzle:


```
pred Puzzle {
  #Person = 2

```


The first line says that there are exactly two people. Remember, since Knight and Knave are disjoint covering subsets of the Person set, saying there are two people also means that `#(Knights + Knaves) = 2`.


```
  some disj A, B: Person {

```


After that we want to place conditions on the two people. We say the two people are `disj` because otherwise Alloy could select `A = B`.


```
    A in Knight <=> (A + B) in Knave

```


This might take some unpacking, so I’ll build it up iteratively. First of all, `P <=> Q` is the logical statement “P is true if and only if Q is true”, or more intuitively, “P and Q are either both true or both false”. `P <=> Q` might not be true! If it isn’t, then we have “If P is true then Q is false, and vice versa”. By making `P <=> Q` part of our predicate, it must be true for our predicate to be true. Since our predicate corresponds to a Knights and Knaves solution, finally, our predicate holding means we found a correct solution.


Now we have `A in Knight <=> Q`. Since the clauses are both true or both false, if A is a knight then `Q` will be true. But if A is a knave, then `!Q` is true. Every clause associated with a knight is true, and every clause associated with a knave is false.


Finally, we have `A in Knight <=> (A + B) in Knave`. So this says either A is a knight and both A and B are knaves, or A is not a knight and it’s not the case that both A and B are knaves. We could have also written `Knave = Person`, which would have the same meaning.


```
  }
}

run Puzzle for 10

```


`for 10` means *up to* ten of each signature (in this case, people) can be in the model. We’ve already capped the number of people at 2 as part of the predicate. I did 10 so that I could freely tweak the problem without having to change the model finder. Final model:


```
abstract sig Person {}

sig Knight extends Person {}
sig Knave extends Person {}

pred Puzzle {
  #Person = 2
  some disj A, B :Person {
    A in Knight <=> (A + B) in Knave
  }
}

run Puzzle for 10

```


Running it gives us a valid solution:2


```
A: Knave
B: Knight

```


Alloy is unable to find any more matching models, so there’s exactly one correct solution to this puzzle. We could also try “we are both the same”:


```
-  A in Knight <=> (A + B) in Knave
+  A in Knight <=> (A + B) in Knave or (A + B) in Knight

```


Alloy finds two solutions:


```
A: Knight
B: Knight

A: Knave
B: Knight

```


Which is as we expected.


### Some logic weirdness


Propositional logic is weird and often unintuitive. To show this, imagine if A instead said “I am a knave and B is a knave.”


```
A in Knight <=> A in Knave and B in Knave

```


This gives us the same answer as before. But if A said “I am a knave. B is a knave”, is that the same?


```
A in Knight <=> A in Knave 
A in Knight <=> B in Knave

```


Alloy can’t find a solution for this! This is different from before because the opposite of `A & B` is `!(A & B)`, and `!(A & B) != !A & !B`. Our first clause is then `A <=> !A`, which is impossible to satisfy.


Let’s make it even stranger. What if we had just one person, who said “I am a knave”?


```
pred Puzzle {
  #Person = 1
  some disj A: Person {
    A in Knight <=> A in Knave 
  }
}

```


This is, as before, unsatisfiable. But what if A said “If you asked me, I would say I was a knave”? If “I claim X” is the logical statement `A in Knight <=> X`, then “I claim ‘I claim X’” is the logical statement `A in Knight <=> (A in Knight <=> X)`. The predicate is then


```
    A in Knight <=> (A in Knight <=> A in Knave)

```


Which has a valid solution if A is a knave. This means, confusingly enough, that if we want to know whether `P` is true or false, we don’t need to know whether we’re talking to a knight or a knave. Both of them will answer “If I asked you, would you claim P” as if they were a knight. We can test this by importing the helper module `boolean`, and then checking that everybody, regardless of their orientation, will give the correct answer:


```
open util/boolean
abstract sig Person {}
sig Knight extends Person {}
sig Knave extends Person {}

assert Question {
  all p: Person, b: Bool {
    b.isTrue <=> (p in Knight <=> (p in Knight <=> b.isTrue))
  }
}

check Question //instead of run Puzzle

```


We use an `assert` instead of a `pred` because we’re not interested in finding specific examples where the works. We’re interested in finding counterexamples where this doesn’t work. But we don’t find any, which means everybody answers the question truthfully.


### Some more examples


I grabbed some Knights and Knaves puzzles from [here](https://champ-outreach.org/images/2016-Spring/Week1/Knights-and-Knaves-Solutions.pdf).


> Problem 1: There are two native islanders, named Alice and Bob, standing next to each other.  You do not know what type either of them is.  Suddenly, Alice says “At least one of us is a Knave.”


```
pred Problem1 {
  #Person = 2
  some disj A, B: Person {
    A in Knight <=> #Knave >= 1
  }
}

```


```
A: Knight
B: Knave

```


> Problem 2: Again,  there are two native islanders standing next to each other.  One is named Claire and the other is named Desmond.  You do not know  what  type  either  of  them  are.   Claire  suddenly  says,  “We  are  both Knights”.  After this,  Desmond says “Either Claire is a Knight or I am a Knight, but we are not both Knights.


```
pred Problem2 {
  #Person = 2
  some disj C, D: Person {
    C in Knight <=> Knight = C + D
    D in Knight <=> (C in Knight or D in Knight) and Knight != C + D 
  }
}

```


```
C: Knave
D: Knight

C: Knave
D: Knave

```


> Problem 3: There are three native islanders, named Elena, Fernando, and Gary,  standing  together.   You  ask  Elena,  “How  many  knights  are  among you?”, and Elena answered but you couldn’t quite hear what she said.  You then ask Fernando, “What did Elena say?”, and Fernando replies, “Elena said there is one knight among us.”  At this point, Gary says “Don’t believe Fernando; he is lying.”


I don’t like this one. The PDF thinks it means this:


```
pred Problem3 {
  #Person = 3
  some disj E, F, G: Person {
    F in Knight <=> (E in Knight <=> #Knight = 1)
    G in Knight <=> F not in Knight
  }
}

```


```
E: Knave
F: Knave
G: Knight

E: Knight
F: Knave
G: Knight

```


But this is actually wrong! If F is a knave, then E didn’t say ‘there’s one knight among us.” The PDF assumes that she said something that’s *incompatible* with it, aka F is a knave and E is a knight, we can infer there is not exactly one knight. The problem is that all we can infer from “F is a knave” is “E did not say ‘there is one knight among us.’” It does not restrict what E said, or what she could say later. We could have had the following:


```
You: "How many knights are among you?"
E: "I'm hungry."
You: "What did E say?"
F: "E said there is one knight among us."

```


To accurately capture the logic of the problem, we need to make the following adjustment:


```
-  F in Knight <=> (E in Knight <=> #Knight = 1)
+  F in Knight => (E in Knight <=> #Knight = 1)

```


If F is a knight, then E made that claim. If F is a knave, we can infer nothing. In this case the two predicates give equivalent answers. For a case where using `<=>` instead of `=>` gives the wrong answer, try replacing F’s statement with “E said there is *at least* one knight.”


> Problem 4: You travel along a road that comes to a fork producing a path to the right and a path to the left.  You know that one path leads to Death and the other path leads to Freedom, but you have no idea which is which.  You can only choose one path to follow.  Fortunately, at the fork in the road are two native islanders, named Horace and Ingrid.  You know that one of Horace and Ingrid is a Knight and the other is a Knave, but you don’t know which  is  which.   You  are  allowed  to  ask  only  one  question.   You  can  ask either Horace or Ingrid (but not both), and the person you ask will answer you.


This is the most famous Knights and Knaves puzzle. We can’t just plug everything in because we aren’t provided with the answers to check. We instead need to figure out a question to ask. We can test, though, if a given question works or not. “Works” here means that regardless of who we ask, we can use the answer to consistently find the right path. Since we can only ask one question, this means finding a question that both always answer the same way.


The usual solution is “ask them what the other would say is the path to Freedom”.


```
assert Problem4 {
  #Person = 2 and #Knave = 1 implies
  all p: Person, b: Bool | //is b the path to freedom?
    let o = Person - p { //the other one
     (o in Knight <=> (p in Knight <=> b.isTrue)) <=> 
     (p in Knight <=> (o in Knight <=> b.isTrue))
    }
}

```


They answer this consistently… and *falsely*. If b is the path to freedom, they will both say b leads to death, You have to invert their answer.


```
-   (o in Knight <=> (p in Knight <=> b.isTrue)) <=> 
-  (p in Knight <=> (o in Knight <=> b.isTrue))
+   b.isFalse <=> (p in Knight <=> (o in Knight <=> b.isTrue))

```


The other problem is that this *only* works if we have exactly one knight and one knave. If we have two knights or two knaves, they will answer *truthfully*.


```
- #Person = 2 and #Knave = 1 implies
+ #Person = 2 and (Person = Knight or Person = Knave) implies

-   b.isFalse <=> (p in Knight <=> (o in Knight <=> b.isTrue))
+   b.isTrue <=> (p in Knight <=> (o in Knight <=> b.isTrue))

```


It’s really funny to me that the famous solution only works in this special case, while the general case is both simpler and always gets true answers *regardless* of what pair you have.


```
- b.isWhatevs <=> (p in Knight <=> (o in Knight <=> b.isTrue))
+ b.isTrue <=> (p in Knight <=> (p in Knight <=> b.isTrue))

```


Not only that, but the general case doesn’t even use `o`! It works even if we’re talking to a single person.


## Advanced Knights and Knaves


These puzzles can get a lot trickier. One way is by adding another layer of properties. For example, in addition to being a knight or a knave, a given person is also either drunk or sober. Sober people act normally, drunk people believe false things are true and true things are false. For example, if you asked a drunk knight “are you a knight”, they will believe they are a knave, and will truthfully (in their mind) answer “no, I am a knave”. By contrast, if you ask a drunk knave “are you a knight”, they will believe they are a knight, and will lie and answer “no, I am a knave”.


Making two signatures `extend` an abstract type make them mutually exclusive. Instead, we want to say that each of our four qualifiers is `in` the abstract type. That way they are not mutually exclusive.


```
- sig Knight extends Person {}
- sig Knave extends Person {}
+ sig Knight, Knave, Drunk, Sober in Person {}

```


We want to declare Knight/Knave are mutually exclusive, as are Drunk/Sober. We also want to say that everybody belongs to both categorizations. We can do this with a `fact`.


```
fact {
  Person = (Knight + Knave) & (Drunk + Sober)
  no (Knight & Knave) + (Drunk & Sober) 
}

```


A person tells the truth if they are a sober knight or a drunk knave. Writing `p in (Knight & Sober) + (Knave & Drunk)` will get tiring after a while. We should pull it out into it’s own `claims` predicate of form `p.claims[statement]`. However, all arguments to predicates must have a signature type, and logical expressions aren’t typed. We could instead express it as `p.claims <=> statement`, or we could use a [macro](http://alloytools.org/quickguide/macro.html):


```
let claims[p, bool] {
  p in (Knight & Sober) + (Knave & Drunk) <=> (bool)
}

```


We can now use this to find solutions for the new setup:


```
pred Puzzle {
  #Person = 1
  some disj A: Person {
    A.claims[A in Knave]
  }
}

```


```
A: Drunk Knight

A: Drunk Knave

```


Other variations of the puzzle, such as day and night knights or knights/knaves/spies are also easy to include in this format.


---

1. Some FM folks don’t see model finding as that different from model checking. If you want to find a model that satisfies `x`, you can just write a spec that claims `!x` and find a counterexample. But model-checking should consistently return the same counterexample, while model-finding should return a set of matching examples.
 [return]
2. The output is as a visualized graph but I’m too lazy to embed images here.
 [return]
