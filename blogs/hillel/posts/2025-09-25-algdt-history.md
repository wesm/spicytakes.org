---
title: "A Very Early History of Algebraic Data Types"
date: 2025-09-25
url: https://www.hillelwayne.com/post/algdt-history/
slug: algdt-history
word_count: 3428
---

Been quiet around here! I’ve been putting almost all of my writing time into [*Logic for Programmers*](https://leanpub.com/logic/) and my whole brain is book-shaped. Trust me, you do not want to read my 2000-word rant on Sphinx post-build LaTeX customization. But I spent the past week in a historical rabbit hole and had to share what I found.


It started with [Algebraic [Data] Types are not Scary, Actually](https://blog.aiono.dev/posts/algebraic-types-are-not-scary,-actually.html). The post covers AlgDTs1 in more detail, but a quick overview is:

- Product types are things like `(Int, Bool)` or `Dog(name: str, owner: Person, age: Int`). They have a value for *each* field. Almost all modern languages have product types, usually calling them something like “structs” or “records” or “value object” or whatever.
- Sum types are “tagged unions”, things like `Int + Nothing`, `Result + ErrorType`, or `Address + Number + Email`. They are a choice between several options. The “tag” means that we do not eliminate overlapping choices. `Bool + Bool` has four possible values, colloquially `Left True, Right True, Left False, Right False`. Sum types are relatively rare in modern programming languages, outside functional programming and some places like Rust.


Where do these get their names? The usual explanation is it comes from their cardinalities (number of possible values): if `#T` is the cardinality of type T, then `#(S + T) == #S + #T` and `#(S, T) == #S * #T`. Try this with `Bool + Weekday` and `(Bool, Weekday)` if you feel unsure.


But it could instead be that the names come from the fact that sums and products of types *act* like sums and products of numbers! I think this is pretty known but it doesn’t appear very often in introduction to AlgDTs. For example: Addition over numbers is associative, meaning `a + (b + c) == (a + b) + c`. This tells us that `Int + (String + Null)` is isomorphic (≅) to `(Int + String) + Null`: we can convert values between the two types without losing any useful information.


A more interesting example is that AlgDTs follow the distributive property `a*(b + c) == a*b + a*c`. If we have a value of type `Account(name: str, contact: (Email + Phone))`, we can transform it into a value of type `EmailAccount(name, email) + PhoneAccount(name, number)`. That’s pretty neat!


So this got me curious: which property of AlgDTs gave the name to “sum” and “product” type, and which properties were discovered later? As I continued to researched this the blog sort of blew up into an early history of algebraic data types.


## Finding an origin


Normally finding the origins of terms is a nightmare, but this is [general academia nonsense](https://en.wikipedia.org/wiki/Abstract_nonsense) so everything relevant is in a paper somewhere. There’s two research techniques I like to use:

1. Read a paper that definitely uses the terms, see what it cites, read those papers, repeat
2. Go to the [ACM Digital Library](https://dl.acm.org/), search a term, and read every paper starting from the oldest.2


Usually I find a combination of the two works best. This eventually got me to John McCarthy’s (the inventor of LISP) [“A Basis for a Mathematical Theory of Computation”](https://www-formal.stanford.edu/jmc/basis1.pdf), published in 1961. As far as I can tell, this is the first treatment of AlgDTs in any form.


### The McCarthy paper


So first off, the paper doesn’t use “type” (in the CS sense) or “algebra” at all, or even really cover computer science. But it does cover “A way of defining new data spaces in terms of given base spaces”, and one of these new data spaces is “Π of truth values whose only elements are T (for truth) and F (for falsity)”, aka ‘booleans’. But he was certainly familiar with types, [being on the ALGOL-60 committee](https://www.softwarepreservation.org/projects/ALGOL/report/Algol60_report_CACM_1960_June.pdf), so I’m guessing he deliberately avoids the word “type” here.


The whole paper is about a simple mathematical model of program functions and their properties. In section 2.6 he defines two ways of generating new data spaces from existing ones:


> The Cartesian product A × B of two sets A and B is the set of all ordered pairs (a · b) with a ∈ A and b ∈ B. If A and B are finite sets and n(A) and n(B) denote the numbers of members of A and B respectively then n(A × B) = n(A) · n(B).


Unsurprisingly, the product type is named after the Cartesian product. The record `Dog(name: str, owner: Person, age: Int)` is a tagged version of the Cartesian product `Str × Person × Int`. Here we also see that, in our lingo, `#(A, B) == #A * #B`.


> The direct union A ⊕ B of the sets A and B is the union of two non-intersecting sets one of which is in 1-1 correspondence with A and the other with B. If A and B are finite, then n(A ⊕ B) = n(A) + n(B) **even if A and B intersect** [emphasis mine]. The elements of A ⊕ B may be written as elements of A or B subscripted with the set from which they come, i.e. a_A or b_B


As far as I can tell, “direct union” was coined by McCarthy, but it corresponds exactly with the [disjoint union](https://en.wikipedia.org/wiki/Disjoint_union). McCarthy later refers to these two as the “direct **sum** and Cartesian product”. He does not *name* them “sum and product types” but I think it’s believable that they are named after the corresponding disjoint union and Cartesian product set operations. I’m not going to dig into the history of *those* names but I’d guess they were named in analogy to arithmetic sum and product.


Shortly after defining the direct sum and Cartesian product3 McCarthy defines isomorphisms between data spaces:


> We will not regard the sets `A × (B × C) and (A × B) × C` as the same, but there is a canonical 1-1 mapping between them … We shall write
> `(A × B) × C ≅ A × (B × C)` to express the fact that these sets are canonically isomorphic.


He goes on to show a number of isomorphisms, including the distributive `A × (B ⊕ C) ≅ A × B ⊕ A × C` that I found so neat. All of these properties of “algebraic data types” were known from the start, even if they weren’t called that yet.


## Is that where it spread from?


While researching this I found a curious article called [“Some Observations Concerning Large Programming Efforts”](https://dl.acm.org/doi/pdf/10.1145/1464122.1464146) (1964). The author presented the Agile manifesto almost 50 years before the Agile manifesto! Nobody ever cited it and the author published nothing else.


What I’m saying is that it doesn’t matter if you’re the first to have an idea if nobody else hears you have it.


So, let’s continue tracing development of algebraic types. In 1964 McCarthy published [Definition of new data types in ALGOL x](https://dl.acm.org/doi/10.5555/1060978.1060993).4 In this he proposes adding two new types, “cartesian” and “union”, to the next version of ALGOL. Notably this is the first place we see “tagged” algebraic types, where both sums and products have string tags. ALGOL-68 would later implement both of them but also be a curious dead end in language history; it would have little impact on modern programming languages.


Here’s where the history gets messy. In looking for next steps, I found two influential papers that cite McCarthy: Tony Hoare’s [Notes on Data Structuring](https://www.cs.cornell.edu/courses/cs4860/2018fa/lectures/Notes-on-Data-Structuring_Hoare.pdf) (1970) and Rod Burstall’s [Proving properties of programs by structural induction](https://www.cse.chalmers.se/~coquand/TSUG/Burstall.pdf) (1968). These correspond to a split between imperative and functional languages, so I’ll treat them in separate sections.


### The Hoare paper


Hoare seems to have independently come up with the idea of sum and product types. In [“A contribution to the development of ALGOL”](https://dl.acm.org/doi/pdf/10.1145/365696.365702) (1966) he proposes records tagged with “classes” and a `union` keyword to join disjoint classes into a single supertype. He does not give any algebraic properties of records or unions, though. By the time of “Notes on Data Structuring” his terminology shifts to match McCarthy’s:


> The types in which we are interested are those already familiar to
> mathematicians; namely, Cartesian Products, Discriminated Unions, Sets,
> Functions, Sequences, and Recursive Structures.


Both his “cartesian products” and “discriminated unions” are tagged, matching how we use algebraic types today. As he is mostly concerned with data storage, he does not list any algebraic properties but does note their cardinalities as part of a discussion on how to most-efficiently store these types.


This paper may also be the first time sum types are discussed as a means of detecting errors at compile-time:


> If the programmer attempts to convert a discriminated union value
> back to a type from which it did not originate, this is a serious programming error, which could lead to meaningless results. This error can be detected only by a runtime check, which tests the tag field whenever such a conversion is explicitly or implicitly invoked. Such a check is time consuming and when it fails, highly inconvenient. We therefore seek a notational technique which will guarantee that this error can never occur in a running program; and the guarantee is given by merely inspecting the text, without any knowledge of the runtime values being processed. Such a guarantee could be given by an automatic compiler, if available.


This is also the first time I can find *anybody* calling sum types “discriminated union”.5 Barbara Liskov then uses “discriminated union” to [describe CLU’s `oneof` sum type](https://dl.acm.org/doi/pdf/10.1145/359763.359789) and Niklaus Wirth uses “discriminated union” why [Pascal *doesn’t* have sum types](https://dl.acm.org/doi/pdf/10.1145/800027.808421). For this reason, I suspect the imperative world first learned about sum types from Hoare’s lecture, and Hoare was influenced (but not totally inspired) by McCarthy.6


After this point sum types disappear from imperative programming. Late 20th century imperative languages were dominated by the influence of Pascal and C. Pascal did not have sum types because Wirth thought they were less flexible than untagged unions. C possibly does not have sum types because they adopted the type system of IBM’s PL/I. PL/I, first released in 1964, had product types (which they called `structs`) but only untagged unions. Recent imperative languages instead got sum types from the functional programming world, which brings us back to [“Proving properties of programs by structural induction”](https://www.cse.chalmers.se/~coquand/TSUG/Burstall.pdf).


### The Burstall paper


Burstall is *incredibly* frustrating to research. [His obituary](https://arxiv.org/html/2505.06456v1) lists an enormous number of papers and influential students, so he clearly had a huge role in the early development of functional programming. But *very* few of those papers are online, so there’s huge gaps in what I’m able to easily research. This is my best attempt to figure out his part of the history.


The paper is about proving properties of recursive types, like lists and trees. This is how he defines a list:


> I suggest that each construction of operation introduce a new type and that disjunctions of these types should also be types, (roughly following Landin 1964)
> a *cons* has an atom and a list, a *nil* has no components, a *list* is a *cons* or a *nil*.


Burstall says he gets his notation from P. J. Landin’s [“The Mechanical Evaluation of Expressions”](https://jhc.sjtu.edu.cn/~yutingwang/files/fp/landin-1964.pdf) (1964). Landin’s use doesn’t *seem* to be quite sum types— it’s not clear he has a mechanism to discriminate between types if they had overlapping values.Rather, it seems to me that Burstall is “following” Landin’s means of writing a recursive definition. It’s hard to tell from a few readings, though, and I could easily be wrong.


The ISWIM near miss
  
Burstall also cites Landin’s [“The Next 700 Programming Languages”](https://www.cs.cmu.edu/~crary/819-f09/Landin66.pdf) (1966), which proposes the influential ISWIM language. According to [“Some History of Functional Programming Languages”](https://www.cs.kent.ac.uk/people/staff/dat/tfp12/tfp12.pdf) (2012), This was the first language to have algebraic data types:

The ISWIM paper also has the first appearance of algebraic type definitions used to define structures. This is done in words, but the sum-of-products idea is clearly there.

However, I don’t think this is correct. For one, ISWIM was a proposed language, not an implemented one. If we count languages proposals then McCarthy beat it by two years and Hoare/Wirth by a couple of months. But also, I don’t think that ISWIM defined sum types at all! This is a weaker belief but I have it for three reasons:

I read the paper six times and cannot figure out where he’s using “sum-of-products”. It *could* be that SHFP is referring to Landin’s definition of an `amessage`, but I *think* that section is about the structure of an ISWIM program, not the data structures inside of it.
I read the specs of two ISWIM implementations, PAL and POP-2, and neither has sums-of-products.
SHFP later says that Burstall’s paper “extended ISWIM with algebraic type definitions — still defined in words”, which implies ISWIM didn’t have them at the start.

None of these are super strong reasons and I’m open to being wrong.

show all


Burstall *does* have sum types, though, which we see in his definition of a tree. A tree is “a node or a tip or a niltree”, but a tip “*has* an item”, not *is* an item. And later, he has this pseudocode:


```
cases t:
    niltree(): nil()
    tip(i): i::nil()
    node(t1, i1, i2): concat(flatten(t1), flatten(t2))

```


Burstall also says his ideas “are based on the work of John McCarthy”, citing his mathematical theory paper. It’s not impossible that Burstall was inspired by McCarthy’s notion of the direct union.


As of 2025 this paper has been cited [over 500 times](https://scholar.google.com/scholar?cites=4186643938001872432&as_sdt=400005&sciodt=0,14&hl=en). Burstall would later go on to make an even bigger contribution but that’s in 1980 so we have to cover ML first.


### The Milner paper


So far we’ve seen the definitions of algebraic data types and common use of “Cartesian product”, but not the *terms* “sum type” and “product type”. As far as I can tell, that comes from Robin Milner’s ML
, as publicized in [“A Theory of Type Polymorphism in Programming”](https://homepages.inf.ed.ac.uk/wadler/papers/papers-we-love/milner-type-polymorphism.pdf) (1977):


> The fully determined types (i.e., the monotypes) of ML are built from a set of basic
> types (int, bool etc.) by the binary infixed operators x (Cartesian product), + (disjoint
> sum) and -> (function type), and the unary postfixed operator `list`.


A few things to note about this paper. First, of course, is it describes constructing types with the “disjoint sum” and uses the `+` symbol. Second, it does not justify nor *define* “disjoint sum”, in contrast with Hoare and McCarthy. By this point it may have been common knowledge for Milner’s audience. Finally, the paper claims that sums and products had already been implemented in ML for at least two years.


We don’t have a complete spec for the oldest versions of ML but we do have the released source code of the [LCF prover](https://en.wikipedia.org/wiki/Logic_for_Computable_Functions) that ML was designed for. This is in [files.ml](https://github.com/theoremprover-museum/LCF77/blob/7a43e95deee18ae37389d98e184b38fdfb3df923/src/files.ml#L284-L285):


```
let instintype insttylist ty = inst ty whererec inst ty =
     fst(revassoc ty insttylist)
     ?(failwith phylumoftype ty
    ??``consttype vartype`` ty
    ??``funtype`` mkfuntype((inst # inst)(destfuntype ty))
+   ??``sumtype`` mksumtype((inst # inst)(destsumtype ty))
+   ??``prodtype`` mkprodtype((inst # inst)(destprodtype ty))
      )  ;;

```


There we have it: “sum” and “product” types! These aren’t tagged, though. Li-yao Xia’s post [Where does the name “algebraic data type” come from?](https://blog.poisson.chat/posts/2024-07-26-adt-history.html) notes that “early versions did not feature data types (see [the first version of Edinburgh LCF](https://github.com/theoremprover-museum/LCF77))“, which I take to mean tagged algebraic types; ML had the `abstype` keyword for naming constructed types. You could define `EmailOrAddress` to be `Str + Str` but couldn’t call the left `Str` “email”.


“A Theory of Type Polymorphism” doesn’t cite the McCarthy paper, nor the Hoare or Burstall papers, so it’s not clear if Milner was influenced by them or developed AlgDTs independently. Some tentative evidence is the followup paper [“A Metalanguage for Interactive Proof in LCF”](https://dl.acm.org/doi/pdf/10.1145/512760.512773) (1978), where he thanks all three for their contributions:


> We are indebted to Dana Scott for providing
> a large part of the theoretical basis for our work: to John McCarthy for encouraging the forerunner of this project at Stanford: to Richard Weyhrauch who contributed greatly to that project: to Tony Hoare and Jerry Schwarz for help with the notion of
> abstract types in ML: to Avra Cohn for help in
> the final design stages through her experiments: to Rod Burstall and many colleagues in Edinburgh
> for illuminating discussions.


Okay, just three more languages to go.


### Hope, VAX ML, and Miranda


Around this time Burstall was applying [category theory to specify software](https://www.ijcai.org/Proceedings/77-2/Papers/095.pdf), eventually leading him to develop HOPE. [“HOPE: An experimental applicative language”](https://dl.acm.org/doi/10.1145/800087.802799) (1980) marks the first introduction of tagged unions to functional programming, but *not* tagged products:


> To define a type ‘tree-of-numbers’ we could say
> `data numtree == empty ++ tip(num) ++ node(numtree#numtree)
> `
> (the sign `#` gives the Cartesian product of types.)


On top of this, the paper introduces a couple of important ideas. The first is that the compiler can exhaustively check that all disjoint choices in a sum type are handled:


> Each data type will have a set of disjoint subtypes, each with a different constructor function; e.g., lists are made with cons or nil It should be easy to do case analysis with respect to these constructors and easy for a compiler to check whether the analysis is exhaustive. This avoids mistakes like forgetting to include a test for the empty list.


On top of this, the paper proposes that the *use* of sum types can be dramatically simplified via pattern matching. This is not the first appearance of structural pattern matching in a language (Prolog had it first), but it’s the first appearance of pattern matching in functional programming.


Around the same time as HOPE, Burstall’s grandstudent [Luca Cardelli](https://www.cs.ox.ac.uk/ralf.hinze/WG2.8/32/slides/ml.pdf)7 was working on porting ML to VAX and Unix, in the process [adding record and variant types](http://lucacardelli.name/Papers/ML%20Introduction%20and%20Examples.pdf). As far as I can tell, this is the first time tagged sums *and* tagged products were present in a functional programming language.


All of these ideas would later be incorporated into [Standard ML](https://smlfamily.github.io/sml97-defn.pdf), codifying what people consider core features of algebraic types today: tags, compiler-based exhaustiveness checking, and pattern matching.


Finally, to reference [Xia again](https://blog.poisson.chat/posts/2024-07-26-adt-history.html),  [“Miranda: A non-strict functional
language with polymorphic types”](https://www.cs.kent.ac.uk/people/staff/dat/miranda/nancypaper.pdf) (1985) is the first paper to actually *use* the term “Algebraic Data Type”. I highly recommend reading Xia’s post for more info.


## A Very Shaky Summary

- McCarthy first proposes the concepts and properties of algebraic data types in his paper, though he doesn’t call it that.
- This has at least some influence on Tony Hoare and Rod Burstall, who write influential papers of their own.
- AlgDTs are implemented in ALGOL-68, CLU, and ML. It’s unclear if Milner knew of McCarthy’s theories, but I’d venture it’s more likely than not.
- Pascal and C prevent sum types from getting a foothold in imperative programming.
- Burstall and Luca Cardelli fill out the main AlgDT features, establishing it as a cornerstone in typed FP.


This is the best I could do with the time and resources I had available. Let me know if you spot any mistakes!


*If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*


---

1. Algebraic Data Types are normally abbreviated ADT, but so are *Abstract* data types, so for clarity I abbreviate them as “AlgDT” and “AbDT”.
 [return]
2. [Kagi](https://kagi.com/) makes this a lot easier: I have a [custom bang](https://help.kagi.com/kagi/features/bangs.html) for searching the DL by “earliest first”.
 [return]
3. For fans of early programming language theory, there’s a bunch of other fun type related stuff here. For example, he presents the famous “power series” definition of the sequence type by first writing `S = 1 ⊕ A × S` and then “solving formally for S, getting S = 1/(1 − A) which we expand in geometric series to get S = 1 ⊕ A ⊕ A² ⊕ …”
 [return]
4. [Tony Finch](https://dotat.at) sent this my way, thank you!
 [return]
5. This *might* also be the first appearance of the “pack of cards” example; Hoare writes it as `type pokercard = (normal: (s: suit; r: rank), wild: (joker 1, joker 2))`. Yes, `,` is *sum* and `;` is *product*.
 [return]
6. On the other hand, Wirth coauthored “In Contribution to the Development of ALGOL”, so he probably had a sense of their value, just maybe not a formal model.
 [return]
7. Cardelli’s doctoral advisor was Gordon Plotkin, and *his* doctoral advisor was Burstall. Small world! 
 [return]
