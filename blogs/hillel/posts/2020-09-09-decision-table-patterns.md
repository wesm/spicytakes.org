---
title: "Decision Table Patterns"
date: 2020-09-09
url: https://www.hillelwayne.com/post/decision-table-patterns/
slug: decision-table-patterns
word_count: 3706
---

Decision tables are easy, simple, and powerful. You can teach them in five minutes and write one in half that time. You can look at a table and understand what it’s saying, see if it matches your problem, and check for design flaws. So it’s kinda weird that there’s basically nothing about them online. I wrote an [introduction](https://www.hillelwayne.com/post/decision-tables/) a while back, but I want something a little more formal. So this post will reintroduce the core ideas in a more formal way and then talk about some of the techniques you can apply to make better tables.


Note that this is a theorycrafting post. I haven’t tested all of the content in production and can’t guarantee that they work well in practice. Caveat emptor.


## Basics


A decision table maps finite enumerated inputs to outputs. The outputs can be anything: returned values, side effects, whatever, but all possible inputs must map to an output. By looking at the table, you know what’s supposed to happen. This makes them good for case analysis and examining requirements.



| A | B | C | O |
| T | T | T | **1** |
| T | T | F | **3** |
| T | F | T | **7** |
| T | F | F | **0** |
| F | - | - | **2** |



For all of these examples we’ll assume one output, O, unless otherwise specified. There is more technique involved in encoding inputs than outputs.


A decision table is **complete** if every possible combination of inputs is represented by a row. It is **sound** if a row of inputs doesn’t appear twice with two different outputs. It is **valid** if it is both complete and sound. A valid table, then, will have exactly one row for each possible combination of inputs. If we have two boolean inputs and one 3-value enumeration, then the table will have 12 rows.


Because decision tables must satisfy rules to be considered valid, they are considered a form of **formal specification**. By being formalized, 1) we can analyze correctness of a table with automated tooling, and 2) errors in the construction of the table often map to errors in our design itself.


Decision tables are also called Parnas tables, especially when they’re used as part of formal verification.


### vs. Pattern Matching


A common question asked about decision tables is “why not pattern match?” In many languages we can do something like this:


```
let patternMatch a b c =
    match (a, b, c) with
    | (true, true, true)   -> 1
    | (true, true, false)  -> 3
    | (true, false, true)  -> 7
    | (true, false, false) -> 0
    | (false, _, _)        -> 2

```


In which case we already have an execution. So why use decision tables if they don’t map to execution?


This is because decision tables are *specification*, not code.  Pattern matching is good for representing a single decision in the code. Decision tables represent a decision at any abstraction level, whether for the code or the entire system. They can even represent high-level non-code decisions:



| PR passed review? | PR passed tests? | O |
| T | T | Merge |
| T | F | Fix tests |
| F | T | Fix review comments |
| F | F | Fix tests first |



Pattern matching is part of the language implementation. Decision tables are more to help you with the design.


That said you also see decision tables as a control-flow  construct. Decision tables are pretty popular in both rules engines and automated QA tools that large enterprises use. SAP advertises their automated decision tables. I am much more interested in their use as specification tools and will not discuss their use as an implementation construct further.


### Representing Infinite States


The system can have an infinite number of states as long as they map to a finite number of values. We can do this by grouping the states into “effectively similar inputs”, or **equivalence classes**. Then we replace the raw input with the class. As an instructive example, we *cannot* make a “naïve” odd-or-even table, as there are infinite positive numbers:



| N | O |
| 1 | odd |
| 2 | even |
| 3 | odd |
| 4 | even |
| … | … |



Since not every possible input can be represented, this table is not complete and so not valid. What we can do is replace the number N with the equation `N % 2`. That has only a finite number of inputs and leads to a valid table.



| `N % 2` | O |
| 0 | even |
| 1 | odd |



Another thing we can do is partition inputs into **intervals**: giving lower and upper bounds for the numbers in each class. Another trite example, “can this person drink in the US?”



| Age | O |
| 0-21 | F |
| 21- | T |



Intervals can be ambiguous: does `0-21` include 0, 21, or both? If both, how do you express the real numbers between 0 and 21, exclusive? We can adapt some math notation here: `(0, 21)` excludes both while `[0, 21]` includes both.



| Age | O |
| `[0, 21)` | F |
| `[21, ∞)` | T |



Conventionally a missing bound is implied to extend to infinity, so we write `[21, ∞)` as `[21, )`.


## Aesthetics


These are habits that make decision tables more visually pleasing. I have no idea if they actually make them better or are just decoration.


### Row ordering


Rows should be ordered by column value. The leftmost column is the most significant key, then the second leftmost, all the way forward. In other words:


**BAD**


**GOOD**



| P | Q |
| F | T |
| T | F |
| T | T |
| F | F |




| P | Q |
| T | T |
| T | F |
| F | T |
| F | F |



This makes it easier to read the table. If you know your inputs and are looking for the output, you can binary search the values.


Values should all be sorted the same way. If one column places T before F, other columns shouldn’t place F before T. I strongly prefer to sort with T first.1


### Column Ordering


The order of the columns should match the order someone would naturally reason through the decision. If you’re making the table for a login flow, you might have conditions for `valid_user?` and `correct_password?`. Since it doesn’t make sense to talk about the password before you have the user, most people would think about finding the user first. The column for that condition should appear before the password column.


A lesser consideration is handling `Any` fields (see below). Columns with `-` values matter less in the table and should be placed later.


**BAD**


**GOOD**



| P | Q |
| `-` | T |
| T | F |
| F | F |




| Q | P |
| T | - |
| F | T |
| F | F |



I don’t think the `-` rule is as aesthetically valuable as the “most important columns first” rule, and neither rule is as important as the row rule.


### Legends


If one of your fields isn’t a boolean, explicitly enumerate the possibilities. It might be implicitly defined in the table, but that’s too easy to confuse.



| P | Q |
| T | - |
| F | red |
| F | blue |



Is this table complete? We don’t know. It could be missing the row `|F, Yellow|`! The legend doesn’t have to be part of the table itself, as long as the reader can infer it from the surrounding context.  Let the reader know that Q can have values `{red, blue}`.


## Techniques


The most common problem with decision tables is bloat: if you have five boolean columns, your table will have 32 rows. Add a sixth and then you’re at 64. Most techniques are about reducing bloat, such as by compressing rows or decomposing tables.


### Any/-


Pretty much everybody does this. `-` means “for any value”. These two tables are equivalent:



| P | Q | O |
| T | T | 1 |
| T | F | 1 |
| F | T | 2 |
| F | F | 3 |




| P | Q | O |
| T | - | 1 |
| F | T | 2 |
| F | F | 3 |



`-` is great for simplifying tables. It’s easy to check for completeness, as you can map the compact version to the full version. If a table consists of four booleans, then `|T - - -|` maps to 8 rows. 2


Aesthetically it looks more pleasant when values don’t follow `-`. `|T - - F|` just looks funny. Sometimes I shuffle around the columns to make the dashes line up. This isn’t always possible, though, and it might obscure the natural flow of the rules.


There’s a couple pitfalls to `-`. First, you can accidentally be unsound, as each `-` expands to several rows. For example:



| P | Q | O |
| T | `-` | 1 |
| `-` | T | 2 |
| F | F | 3 |



This is complete but unsound, as `|T T|` maps to both 1 and 2. The other pitfall is implicit ordering. We might have



| P | O |
| A | T |
| B | F |
| C | F |



It’s tempting to write this as



| P | O |
| A | T |
| `-` | F |



Now the order of the rows matters! Someone can figure out what you mean here, but now it’s no longer explicit. Prefer to list things out here.


Notation note: `-` usually means “any”, but that’s not always clear. It’s easy to think the symbol means “unknown” or “n/a”. If you have concerns then prefer to be explicit. You should probably use a different symbol if you’re using `+` as a value.


#### Input Elimination


Often by using `-` we find that a column is unnecessary. Given the table



| P | Q | O |
| T | T | 1 |
| T | F | 1 |
| F | T | 2 |
| F | F | 2 |



We can simplify this as


`Simplify`


`Drop Q`



| P | Q | O |
| T | - | 1 |
| F | - | 2 |




| P | O |
| T | 1 |
| F | 2 |



In this way decision tables can help us determine if some inputs are unnecessary for our logic.


### Table Decomposition


An output is **dependent** on an input if that input plays “some role” on that output. Not all outputs may be dependent on all inputs.



| P | Q | O1 | O2 |
| T | T | F | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | F |



O1 only depends on P and O2 only depends on Q. We can decompose this table into two smaller ones:



| P | O1 |
| T | F |
| F | T |




| Q | O2 |
| T | T |
| F | F |



Decomposing tables makes them simpler but isn’t always the right choice. If O1 and O2 are conceptually related, this might things less clear to the reader. Nor does decomposing always reduce the size of your table. An outcome might be dependent on one value while the other might be dependent on both.



| P | Q | O1 | O2 |
| T | T | T | T |
| T | F | T | F |
| F | T | T | T |
| F | F | F | F |



Decomposing this table would give you two tables with a total of six rows. On the other hand, if O1 and O2 are totally conceptually distinct it might be clearer to break them into separate tables. As always, what’s best is highly context-dependent.


### Input Dependence


Inputs are dependent if one can restrict the values of another. Take the following three business rules:

1. If a form doesn’t exist, redirect them to the “start” page.
2. If the form exists and hasn’t been submitted, redirect to “continue”.
3. If the form exists and has been submitted, redirect to “review”.


We could write this as two booleans: `form_exists?` and `submitted?`. Submitted is only a meaningful boolean if the form already exists. We can instead fold these two booleans into a single column, such as `form_status`:



| `form_status` | O |
| `not_started` | “start” |
| `incomplete` | “continue” |
| `submitted` | “review” |



This breaks down for larger tables. Consider a login table with three values: `password_correct?`, `2auth_enabled?`, and `2auth_correct?`. Whether or not you have 2auth is irrelevant if you don’t know the password, and asking if you passed the 2auth is nonsensical if you have it disabled. There’s a few different ways to model this, all awkward. The simplest is probably to use another symbol, like `/`, to tell the reader that it’s impossible:



| `password-correct?` | `2auth-enabled?` | `2auth-correct?` | O |
| T | T | T | 4 |
| T | T | F | 3 |
| T | F | / | 2 |
| F | - | / | 1 |



If you’d prefer to not introduce a new symbol and turn your booleans into trileans then another alternative is to use `any`. This is a little deceptive, as it implies the column *has* a value, we just don’t care what it is. It works but make logicians very sad.


#### Pitfalls


When handling dependent inputs, it matters whether the dependence is a **fact** or if it’s an **assertion**. A fact is something that *cannot possibly* be false. If we run into a case where it is false, then a software bug is the least of our worries. This most often happens when the conditions are incompatible and only one of them can be true. In this case, we can fold the columns into an enumeration.



| `thread1_lock?` | `thread2_lock?` | O |
| T | F | 1 |
| F | T | 2 |
| … | … | … |




| `lock_held_by` | O |
| None | 1 |
| Thread 1 | 2 |
| Thread 2 | 3 |



An assertion, by contrast, is something we build the system to guarantee. It can, in reality, be false, but ideally it’s never false in our system.


Ideally is a dangerous word. In this case I’d want to be clear that the odd combination is not something that *can’t possibly* happen, it’s something that *shouldn’t* happen. That means if it *does* happen, there’s something wrong and we should stop and figure that out. Perhaps we wrote our own locking mechanism and aren’t completely sure it’s correct, maybe we’re worried about cosmic rays, whatever. These possibilities should be explicitly enumerated, and the output should be clearly marked as unspecified or an error.



| `thread1_lock?` | `thread2_lock?` | O |
| T | T | **???** |
| F | F | **error** |
| … | … | … |



The simplest answer here is to redesign your system to handle it, but that might not be feasible.


### Subtables


If many inputs or outputs are dependent on a single input, it makes sense to break this into a separate table. The two tables should refer to each other. See for example [here](https://help.sap.com/viewer/2754875d2d2a403f95e58a41a9c7d6de/1911/en-US/2bccc3ed722d1014a688d77c71096543.html). I’ve struggled to find a good teaching example so am only mentioning this for completeness.


## More difficult situations


### Independent Intervals


When working with intervals we run into a problem where different conditions may depend on distinct partitions of the interval into ranges.



| P | Q | O |
| T | `[0, 2]` | 1 |
| T | `(2, 10]` | 2 |
| F | `[0, 4)` | 3 |
| F | `[4, 10]` | 4 |



This is especially common when working with date intervals, as we saw with the [Rose Kata](https://www.hillelwayne.com/requirements/). The problem is ensuring completeness. If we have two separate sets of interval covers, we lose our direct mapping between the possible values and the total number of rows. It’s also easy to accidentally miss something.


A thorough-but-bloaty solution is to combine all of the intervals into one superset with no overlaps.



| P | Q | O |
| T | `[0, 2]` | 1 |
| T | `(2, 4)` | 2 |
| T | `[4, 10]` | 2 |
| F | `[0, 2]` | 3 |
| F | `(2, 4)` | 3 |
| F | `[4, 10]` | 4 |



This makes the table more formalized at the cost of bloat and concealing the underlying logic. You also need to watch for mistakes in translating to the new partitions, especially at the boundaries of intervals.


### State


Really you should be using transition tables or state machines to formalize state, but we can handle small problems with decision tables. If we want a decision table to represent a mutation, we need to make explicit the difference between the old and new values on the table. The convention is write the variable with a prime. If the table mutates `x`, we write the original value as `x` and the new value as `x'`.



| `x % 2 == 0` | `x'` |
| T | `x/2` |
| F | `3x+1` |



Each table should only model one step. In the body of the table, `x` always refers to the old value and `x'` should not appear at all. Multiple outputs can depend on `x`, though, making this useful for representing simultaneous mutations:



| P | `x'` | `y'` |
| T | `x+y` | `x` |
| F | `x` | `x-y` |



If we need to represent a more complex update, we can break it down into one table that defines `x'` and one that defines `x''`:



| `x'` | `x''` |
| `(, 0]` | 0 |
| `[1, 50]` | `x'` |
| `[51, )` | 50 |



Representing state in decision tables gets awkward quickly and it doesn’t quite scale to complex state.


#### More Complex State


Make a damn state machine


### When you’re going too far


Decision tables have minimal syntax and semantics. They are easy to use. They also quickly hit limits.


I don’t like saying “don’t use them when they’re inappropriate”, because that sounds like smug avoidance to me. That answer doesn’t give you any insight into when they are inappropriate. We want to be specific about when they become inappropriate.


Decision tables work best when the entire problem can be modeled as discrete, independent inputs. Break that and everything falls apart. Sometimes you can refine the problem space like we did with intervals, but that only gets you so far. Other signs that decision tables are inappropriate include:

- When you have complex data structures. If one of the inputs is a list of integers, your table is going to be huge.
- When the decision is made “over time”, where you have to perform some effects in order to complete the decision. DTs model instantaneous decisions. Consider a flowchart instead.
- When there’s no easy way to encode your data in a way that the table is “obviously” complete. If your input is “three events with a ranking”, a complete table will still look like it is missing rows.3
- When the table gets extremely large.
- When a table layout doesn’t make anything clearer.


## Shortcuts


How strict you need to be about your decision tables depends on what you’re using them for. If your goal is to have a specification artifact then you want to be as rigorous as possible. You want to be strict if you’re trying to explicitly shakeout design issues or plan to high-level project-level decisions based on the table. If you’re using the decision table as a mental augmentation tool, then taking shortcuts is fine. The goal is to help you think better and excessive formalism doesn’t always lead to insight.


## Final Thoughts


Decision tables are easy, simple, and powerful. You can teach them in five minutes and write one in half that time. And while they have a low expressiveness ceiling, there’s no opportunity cost to trying them first. Worst case is you lose a few minutes before realizing they’re inappropriate for your problem.


If you want to see decision tables used in the wild, two good examples are [here](https://github.com/rails/rails/pull/36795#issuecomment-515914165) and [here](https://twitter.com/jesterxl/status/1222728288117972992).


I hope this made decision tables more accessible to you. If you’re interested in my other writing, in addition to this site I have a twice-weekly [newsletter](https://buttondown.email/hillelwayne/) on software and a [Twitter](https://twitter.com/hillelogram) that’s a mix of tech, math, confectioning, and general Twitter inanery.


*Thanks to [Nicolas Rinaudo](https://nrinaudo.github.io/) for feedback.*


---

1. In an ideal world we’d have decision tables that were interactive so you could freely slice and pivot the rows and columns, but I’ve not been able to find a tool that does this. Maybe some Excel plugin?
 [return]
2. Each `-` can be one of two possible values, so there are `2*2*2` combinations of values.
 [return]
3. There are `3!` orderings: `|1 2 3|`, `|1 3 2|`, etc. It will look like each column can have one of 3 values, so people might be confused and think there should be `3^3` rows.
 [return]
