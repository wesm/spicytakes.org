---
title: "Why Does \"=\" Mean Assignment?"
date: 2018-04-10
url: https://www.hillelwayne.com/post/equals-as-assignment/
slug: equals-as-assignment
word_count: 1469
---

Take the following code:


```
a = 1
a = a + 1
print(a)

```


A common FP critique of imperative programming goes like this: “How can `a = a + 1`? That’s like saying `1 = 2`. Mutable assignment makes no sense.” This is a notation mismatch: “equals” should mean “equality”, when it really means “assign”. I agree with this criticism and think it’s bad notation. But I also know some languages don’t write `a = a + 1`, instead writing `a := a + 1`. Why isn’t that the norm?


The usual answer is “because of C”. But that’s just passing the buck: *why* does C do it that way? Let’s find out!


## The Big Four


In the early 1960’s we had four dominant high-level languages: COBOL, FORTRAN II, ALGOL-60, and LISP. At the time, people broke assignment into two classes: *Initialization* is when you define a variable for the first time, and *reassignment* is when you change the value of an existing variable. So, annotating our python example, we have


```
a = 1 # Init
a = a + 1 # Reassignment
print(a)

```


People didn’t use these specific terms, but it captures what everybody was doing. Here’s what the operators were for every language, as well as how you did an equality check:



| Language | Initialize | Reassign | Equality |
| FORTRAN | `=` | `=` | `.EQ.` |
| COBOL | `INITIALIZE` | `MOVE`1 | `EQUAL` |
| ALGOL | N/A | `:=` | `=` |
| LISP | `let` | `set`2 | `equal` |



ALGOL didn’t have a special operator for initialization. Rather, you created the variable with the type, and then later used an operator to assign to it. You could do `integer x; x := 5;`, but you couldn’t do `integer x := 5;`. This makes FORTRAN the only one that used `=` for any kind of assignment, so would seem the right candidate for modern usage. But we know that C descends from ALGOL, which means somehow the `:=` assignment was dropped and `=` was changed from an equality check.


## ALGOL Begat CPL


ALGOL-60 might be the most influential programming language in the history of CS. It might also be one of the most useless. The language, by intention, didn’t have any I/O features in the core spec. You could hardcode inputs and measure outputs, but if you wanted to actually *do* anything with it, you had get a compiler that extended the core language. ALGOL was designed for researching algorithms and broke down if you were doing anything else.


It was such a strong language, though, that people wanted to generalize it for business and industry. The first big push came in 1963 from Christopher Strachey and University of Cambridge. Their language, CPL, added a bunch of innovations on top of ALGOL, most of which we would come to regret. One of them was *initialized definition*, where a variable could be initialized and assigned in the same statement! Instead of writing `integer x; x := 5;` you could write `integer x = 5`. Groovy!


But we switched from `:=` to `=` there. That’s because CPL had *three* kinds of variable initialization:

- `=` meant initialize by value.
- `≃` meant initialize by reference, so that if `x ≃ y`, reassigning to `x` would also mutate `y`. But if you wrote `x ≃ y + 1` and tried reassigning the `x`, the program would crash.
- `≡` meant initialize by substitution, aka make `x` a niladic function that evaluates the RHS every time it’s used. They never explain what’s supposed to happen if you try reassigning to `x` and I’m afraid to find out.


A problem: now `=` was used for both initialization and equality. Fortunately CPL was clear-ish enough on this in practice: anywhere you wrote `=` it was unambiguous which one you meant.


Just a year later Ken Iverson invented APL, which uses `←` for all assignments. Since most keyboards don’t have that as a key, not even Iverson kept with it, and his followup language, J, uses `=:` for assignments.3 But APL deeply influenced S, which deeply influenced R, which is why `<-` is the preferred R assignment operator.


## CPL Begat BCPL


CPL was a great language with a minor problem: nobody could implement it. A few people managed partial implementations of subsets of the features, but it was too big and complicated for compilers of the era. So Martin Richards stripped out a lot of the extraneous complexity to create BCPL. The first BCPL compiler came out in 1967… and the first CPL compiler in 1970.


Among other simplifications, the “three kinds of initialization” rules had to go. Richards believed that substitution expressions were niche and could be replaced by functions, and the same with assignments. So he collapsed them all into just `=`, with the exception of naming global memory addresses, which used `:`. As with CPL, `=` was also the equality check. For reassignment, he used `:=` just as CPL and ALGOL did. A lot of later languages follow this convention: `=` for initialization, `:=` for reassignment, and `=` for equality. But it went mainstream when Niklaus Wirth created Pascal, which is why we now call it “Pascal style”.


As far as I can tell, BCPL was also the first “weakly-typed” language, as the only data-type was the data word.4 This made the compiler a lot more portable at the expense of leading to more logic errors, but Richards expected/hoped that better process improvements, descriptive naming, would counteract this. BCPL also introduced braces as a means of defining blocks.


## BCPL Begat B


Ken Thompson wanted to convert BCPL to run on the PDP-7. While BCPL had a “small compiler”, it was still four times larger than the minimum working memory of the PDP-7, 16 kb to 4 kb. So Thompson needed to create a new, more minimal language. He also personally, aesthetically, wanted to minimize the number of characters in source code. This ended up being the biggest factor in B’s design. That’s why we have, for example, `++` and `--` operators.


Once you get rid of named global memory addresses, BCPL always uses `=` for initialization and `:=` for reassignment. Thompson decided to merge these into a single token for all forms of assignment, and picked `=` because it’s shorter. However, this makes determining the use ambiguous: if `x` was already declared, is `x = y` an assignment or an equality check? And there are some cases where it’s supposed to be both! He added a new token, `==`, as the sole form of “equal to”. As Thompson [put it](https://ia801303.us.archive.org/1/items/TheCProgrammingLanguageFirstEdition/The%20C%20Programming%20Language%20First%20Edition%20%5BUA-07%5D.pdf):


> Since assignment is about twice as frequent as equality testing in typical programs, it’s appropriate that the operator be half as long.


Thompson (joined by Dennis Ritchie) released the first version of B around 1969. In the time between the two Ole Dahl and Kristen Nygaard invented Simula 67, the first OOP language. Simula follows ALGOL conventions of strictly-separate initialization and reassignment steps. Alan Kay also started work on smalltalk around this time, which adds blocks but follows the same syntax. So even up until 1971 or so most new languages were using `:=` for assignment.


## B Begat C


…and the rest is history.


Okay, there’s still a bit more to cover. ML came out a year later and AFAICT was the first language to really emphasize pure functions and no mutation. But it still has an escape hatch in reference cells, which can be reassigned to new values with `:=`. Starting 1980 we begin seeing correctness-oriented imperative languages, particularly Eiffel and Ada, which both use `:=` for assignment.


Looking at this as a whole, `=` was never “the natural choice” the assignment operator. Pretty much everybody in the ALGOL tree used `:=` for assignment instead, possibly *because* `=` was so associated with equality. Nowadays most languages use `=` entirely because C uses it, and we can trace C using it to CPL being such a trash fire.


I don’t know if this adds anything to the conversation. I just like software history.


---

1. COBOL is super weird here. They have several operators that implicitly mutate, like `ADD TO` and `COMPUTE`. COBOL is a bad language.
 [return]
2. I earlier had both LISP operators as `apply`. A couple of people pointed out that I misread the [Lisp 1.5 Manual](http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf) and that the actual terms were `let` and `set`. I updated the page accordingly.
 [return]
3. I like to think this was an intentional pun on a backwards `:=`, but it follows the rest of the language, which uses . and : as verb suffixes.
 [return]
4. BCPL later adding a floating point keyword. And when I say “later”, I mean in [2018](http://www.cl.cam.ac.uk/~mr10/bcplman.pdf).
 [return]
