---
title: "Constructive vs Predicative Data"
date: 2020-05-18
url: https://www.hillelwayne.com/post/constructive/
slug: constructive
word_count: 1850
---

Consider a data type that represents users, which includes “favorite people” and “blocked people”:1


```
data Person:
  favorites: set of Person
  blocked: set of Person

```


We want a validation that says that these two sets are disjoint, a.k.a. no person can belong to both sets at once. We call these kinds of validations **predicates**, or boolean functions that correspond to our requirements. The predicates determine if a *representable* item is also a *valid* item. We can represent a user with overlapping favorites and blocked, but then that user is invalid.


In many cases we don’t want to allow representable invalid data, as it makes bugs more likely. An alternative is to “make illegal states unrepresentable”, structuring the data in such a way that it is always valid no matter what.2


```
enum status {Favorite, Blocked}

data Person:
  person_of_note: dict of [Person, status]

```


Now we cannot express the data in an invalid way. All users are valid because it is only possible to construct a valid user. This is often seen as obviously good. But obvious things are often obvious for very subtle reasons. We consciously make the choice to make illegal states unrepresentable and should study how we make that choice.


The two methods of satisfying the requirement are the **predicative** and **constructive** approaches. In the predicative approach we have a universe of all representable items and use predicates to select a subset of that universe which we consider ‘valid’. In the constructive approach we take a collection of generating rules and use them to build a set of items. As we don’t have to create a universe of data before we start building from the rules, we can make only valid data representable.


The constructive approach does not necessarily guarantee that all valid data can be generated. It is sound but not complete. Consider generating a two digit number which has nine in it. A possible constructive approach would be to pick a random number between 90 and 99. This will only give you about half of all valid items. A different constructive approach would be to pick a random number between 10 and 99, then pick a random digit of that number and set it to 9. This will get all possible items but will not draw them evenly, and you will get some numbers more often than others.3 Finding a good constructive solution requires that you be “clever” in a way finding a predicative solution does not. As a corollary, there is a steeper learning curve to writing constructive solutions.


This means that predicative data is easier to express at the cost of permitting representable invalid data. This is enough of a problem that we prefer constructive data whenever feasible.4 Predicative data should be the fallback for when constructive data is infeasible. In practice this means that most data will be a mix of constructive and predicative.


Then what makes constructive data infeasible? No strict answers, but some heuristics:


### Ergonomics


Making something constructive often means changing how we represent the data. This makes writing general-purpose functions harder, as the function must now account for all the different representations.5


A user has a list of emergency contacts. Alpha users require at least one and Gamma users require at least two. We can enforce this in both a predicative and constructive way:


```
//predicative
data Person:
  contacts: set of Person

invariant {
  either { IsAlpha && #contacts ≥ 1 }
  or { IsGamma && #contacts ≥ 2 }
}

//constructive
data Person:
  contacts: set of Person

data AlphaPerson:
  contact: Person
  other_contacts: set of Person

data GammaPerson:
  first_contact: Person
  second_contact: Person
  other_contacts: set of Person

```


(This construction does not preserve *all* the invariants: there’s nothing preventing `first_contact` and `second_contact` from being the same Person. )


Now you want to check if X is a contact of `person`. In the predicative case it’s easy: it’s just `X in person.contacts`. In the constructive case we need to write separate branches to check each case of user. More code means more places to write bugs, somewhat mitigating the benefits of constructive data.


### Overlapping Data


The above construction is incomplete: it’s impossible for an `AlphaPerson` to be a contact. There’s an is-a relationship between `AlphaPerson` and `Person` that we need to make explicit. We may need to do something like this:


```
data Person:
  ...

data RegularPerson is Person:
  contact: Person

data AlphaPerson is Person:
  contact: Person
  other_contacts: set of Person

data GammaPerson is Person:
  first_contact: Person
  second_contact: Person
  other_contacts: set of Person

```


This becomes more complicated as categories become more inclusive. What happens we have both `Person` and `PremiumPerson`, and want to say that a user can be both an `AlphaPerson` and a `PremiumPerson`?


This is less of a problem with the predicative approach because the intersection of two sets is the set of all elements that satisfy both predicates.


### Nonmonotonic Predicates


Most predicates are **monotonic**: they are true iff certain information is present. Constructive data is very good at dealing with monotonic properties, such as “this structure contains a `date` field.” That are monotonic because, once true, we cannot add additional information that would make it false. It is true and stays true. Merging the structure with another structure will still preserve the property as it will still have the `date` field. By contrast, a **nonmonotonic** property can be falsified by additional information. It would be something like “this structure does not contain both a `date` field and a `time` field.” We can take two independent structures that both satisfy the property and merge them to get something that violates it.6


Ensuring that `blocked` and `favorites` didn’t overlap was a nonmonotonic property. We were able to construct data that implicitly satisfies the property, but it is very difficult to construct data that explicitly satisfies it. Constructive systems are very bad at negating properties, in the same way that most sound static type systems cannot type “everything that is not an integer.”


Other nonmonotonic properties: Search terms with NOT. Arrays with a constrained sum. “The password may not contain your username.”


### Invalid vs Undesirable


In addition to multiple shades of valid, there can be multiple levels of invalid. We often need to distinguish between “invalid” data and “undesirable” data. Data should never be invalid, but sometimes data is in a valid but undesirable state. Oftentimes the purpose of the program itself is to take undesirable data and move it out of the undesired state. If an `AlphaUser` has not listed an emergency contact, we may want to still save their info but block them from using our services until they supply a contact.


This conflicts with the goal of constructive data, that the only representable states are valid ones. We need to be able to represent undesired states, too. This can still be done; we can construct the set of valid states and conjoin it with a construction of undesirable states. But this adds considerably more complexity to the solution. People will generally opt to make one construction that covers both valid and undesirable states and then distinguish the two with a predicate.


## Constructive Solutions as a Skill


Just as we should explore the limits of constructive feasibility, we should also explore techniques to make our data more constructive. If finding constructive solutions is a skill, then it is a skill we can improve. The more skilled we are, the better we are at finding constructive ways to represent complex information while maintaining ergonomics.


One way we can improve this skill is by identifying common patterns we constantly use in constructive solutions. This is similar to how we have software design patterns. Some common patterns I’ve seen are:

- Restricting values to finite enumerations
- Wrapping primitive types in user-defined types or structures. We can guarantee nonempty lists by replacing `[T]` with `{head: T, rest: [T]}`.
- Replacing multiple distinct fields with a constrained dictionary, as we did with `favorites` and `blocked`.
- Inversions: taking a dictionary of form `A ↦ B` and replacing it with a form `B ↦ A` ensure that all of the B’s are unique.


A more complex technique, **channels**, comes from operations research. This involves constructing redundant representations of the data and then using a predicate to link the constructs together. This is useful for contraint solving. Example: If we schedule a set of talks to a set of rooms and times we want to make sure that there is a 1-1 mapping between talks and room-time pairs. There is no easy way to encode both requirements into a single data representation, but we can create two separate ones:


```
array[TIMES, ROOMS] of var talks: sched;
array[talks] of var TIMES: talk_time;
array[talks] of var ROOMS: talk_room;

```


We then need to guarantee the two representations are equivalent. Here’s where we add the channel predicate.


```
constraint forall(t in talks) (t = sched[talk_time[t], talk_room[t]]);

```


Validating the two are sync is more complicated for programs than constraint solvers, as constraint solvers don’t have to deal with mutation. I still think it’s an avenue worth exploring.


## Thoughts


I’m fascinated by how there is a lot to discuss in a very simple concept and by how broadly it applies. I think a lot of specific issues in software have the constructive versus predicative spectrum as an underlying foundation. For example, database schemas are constructive while their constraints are predicative. It makes me curious about what other insights we can glean by taking every day programming and trying to figure out the implicit reasoning we use. I’m also fascinated by how “finding constructive solutions” can be seen as a skill with patterns and techniques, while this is less true with finding predicative solutions.


*I shared the first draft of this essay on my [newsletter](https://buttondown.email/hillelwayne/). If you like my writing, why not subscribe?*


*Thanks to [Jimmy Koppel](http://www.jameskoppel.com/) for corrections and feedback.*


---

1. I’m using a Pascal-esque pseudocode here.
 [return]
2. For a general treatment of making illegal states unrepresentable, [see here](https://fsharpforfunandprofit.com/posts/designing-with-types-making-illegal-states-unrepresentable/).
 [return]
3. There are nine numbers that each have a 50% chance of being transformed into 19, and 19 has a 50% chance of transforming into 99. There are 17 numbers that each have a 50% chance of transforming into 99, and 99 has a 0% chance of transforming into a different number.
 [return]
4. Part of the benefit here is coincidental: most mainstream languages do not provide a first-class mechanism to check predicates. You have to check them yourself whenever you think one *might* have been broken. Whereas most constructive approaches map neatly to the type system.
 [return]
5. I’m deliberately avoiding the use of the word “type” here. Type systems add additional expressiveness beyond what we’re dealing with here.
 [return]
6. As another way of explaining this: the predicate may be either uncertain, true, or false based on information available. With a monotonic property, getting more information can make the predicate go from uncertain to true or from uncertain to false. With the nonmonotonic property, adding more information can additionally make a predicate go from true to false.
 [return]
