---
title: "Why Don't People Use Formal Methods?"
date: 2019-01-21
url: https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/
slug: why-dont-people-use-formal-methods
word_count: 5665
---

I saw [this](https://softwareengineering.stackexchange.com/questions/375342/what-are-the-barriers-that-prevent-widespread-adoption-of-formal-methods) question on the Software Engineering Stack Exchange: *What are the barriers that prevent widespread adoption of formal methods*? The question was closed as opinion-based, and most of the answers were things like “its too expensive!!!” or “website isn’t airplane!!!” These are sorta kinda true but don’t explain very much. I wrote this to provide a larger historical picture of formal methods, why they’re actually so unused, and what we’re doing to make them used.


Before we begin, we need to lay down some terms. There really isn’t a formal methods community so much as a few tiny bands foraging in the Steppe.1 This means different groups use terms in different ways. Very broadly, there are two domains in FM: **formal specification** is the study of how we write precise, unambiguous specifications, and **formal verification** is the study of how we prove things are correct. But “things” includes both code and abstract systems. Not only do we use separate means of specifying both things, we often use different means to verify them, too. To make things even more confusing, if somebody says they do formal specification, they *usually* mean they both specify and verify systems, and if somebody says they do formal verification, they *usually* mean mean they both specify and verify code.


For clarity purposes, I will divide verification into **code verification** (CV) and **design verification** (DV), and similarly divide specification into CS and DS. These are not terms used in the wider FM world. We’ll start by talking about CS and CV, then move on to DS and DV.


Additionally, we can do **partial verification**, where we only verify a subset of the spec, or **full verification**, where we verify the entire spec. This could be the difference between proving “it never crashes or accepts the wrong password” or “it never crashes or admits the wrong password and locks the account if you give the wrong password three times.” Most of this history will assume we’re doing full verification.


We should also clarify the type of software we’re formalizing. Most people implicitly divide software into **high-assurance** software, such as medical devices and aircraft, and everything else. People assume that formal methods are widely used in the former and unnecessary for the latter. This, if anything, is too *optimistic*: most people in high-assurance software don’t use formal methods. We’ll focus instead on “regular” software.


Finally, a disclaimer: I am not a historian, and while I tried to do my due diligence there are probably mistakes here. Also, I specialize in formal specification (DS and DV), so there are more likely to be mistakes in anything I say about code verification. If you see something wrong, email me and I’ll fix it.2


# Formal Coding


## Getting the Spec


Before we prove our code is correct, we need to know what is “correct”. This means having some form of **specification**, or spec, for what the code should do, one where we can unambiguously say whether a specific output follows the spec. Just saying a list is “sorted” is unclear: we don’t know what we’re sorting, what criteria we’re using, or even what we mean by “sort”. Instead, we might say “A list of integers `l` is *sorted in ascending order* if for any two indices i and j, if `i < j`, then `l[i]` <= `l[j]`”.


Code specs fall into three major camps:

1. The first is writing them as statements independent of the code. We would write our sort function, and in a separate file write the theorem “this returns sorted lists”. This is the oldest form of spec and is still the way Isabelle and ACL2 do things.3
2. The second embeds specs in the code in the form of pre/postconditions, assertions, and invariants. We might add a postcondition on the function that “the return value is a sorted list”. Assertion-based specs were originally formalized as [**Hoare Logic**](https://en.wikipedia.org/wiki/Hoare_logic) and were first integrated into a programming language with [Euclid](https://dl.acm.org/citation.cfm?id=971189) in the early 1970s.4 This style is also called **Design by Contract** and is the most popular form of industrial verification.5
3. Finally, we have type systems. By [Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence), any math theorem or proof can be encoded as a dependent type. We’d define the type of “sorted lists” and declare our function has the type signature `[Int] -> Sorted [Int]`.


You can see examples of how all of these look at [Let’s Prove Leftpad](https://github.com/hwayne/lets-prove-leftpad). HOL4 and Isabelle are good examples of “independent theorem” specs, SPARK and Dafny have “embedded assertion” specs, and Coq and Agda have “dependent type” specs.6


If you squint a bit it looks like these three forms of code spec map to the three main domains of automated correctness checking: tests, [contracts](https://www.hillelwayne.com/talks/beyond-unit-tests), and types. This is not a coincidence. Correctness is a spectrum, and formal verification is one extreme of that spectrum. As we reduce the rigour (and effort) of our verification we get simpler and narrower checks, whether that means limiting the explored state space, using weaker types, or pushing verification to the runtime. Any means of total specification then becomes a means of partial specification, and vice versa: many consider [**Cleanroom**](https://web.archive.org/web/20190228165642/infohost.nmt.edu/~al/cseet-paper.html) a formal verification technique, which primarily works by pushing code review far beyond what’s humanly possible.


## “What’s the right spec?”


Verification proves code matches its spec. This raises a question: how do we know we have the right spec? Finding the right spec is one of the biggest challenges in formal methods. It’s also one of the most raised objections, but the way skeptics mean it isn’t *exactly* the same as the way advocates think of it.


When outsiders say “how do you have the right spec?” they’re *usually* thinking of **validation**: showing a spec actually does what the client wants.  If you formally prove your code sorts a list, but the customer actually wants Uber For Soups ™, you’ve just wasted a bunch of time. Only by rapid iteration and short feedback cycles, people argue, can you actually validate your requirements.


It is true that verifying code does not validate the code. There are two problems with this argument, though. The first is that it just delays the value of FM, not eliminate it entirely. Once you’ve done your rapid iterations, you presumably have an idea of what your customer wants. *Then* you start verifying code. Second, while we don’t know what exactly the customer wants, there are some things we can assume they *don’t* want. They don’t want the software randomly crashing on them. They don’t want security holes. Everybody recognizes the importance of this: after all, nobody is saying you should skip unit tests while you iterate. So, at the very least, prove your version control system doesn’t randomly delete chapters of a user’s book.7


The problem with finding the right spec is more fundamental: *we often don’t know what we want the spec to be.* We think of our requirements in human terms, not mathematical terms. If I say “this should distinguish parks from birds”, what am I *saying*? I could explain to a human by giving a bunch of pictures of parks and birds, but that’s just specific examples, not capturing the *idea* of distinguishing parks from birds. To actually translate that to a formal spec requires us to be able to formalize human concepts, and that is a serious challenge.


Don’t get me wrong, it’s possible to figure out the appropriate specs here and experts do it all of the time. But writing appropriate specs is a skill you need to develop, just as you needed to develop coding skills. This is why a lot of the more recent successes with code verification have been things with an obvious map between what we want and what we can express we want. For example, [CompCert](http://compcert.inria.fr/) is a formally verified C compiler. The spec there is “this will never miscompile”.


And none of this is the actual verification part. Once you *have* a spec, you still need to prove the code *matches* the spec.


## Proving the Spec


The earliest means of code verification we see is the the Dijkstra-style “think really hard about why it’s true” method, which is basically what ALGOL was designed to help do. For example, I might “prove” an insertion sort works by arguing

1. *Base Case*: if we have an empty list and add one element to it, that will be the only element, so it will be sorted.
2. If we have a sorted list with `k` elements and add one element, we insert the element so that it is after all smaller numbers and before all larger numbers. This means the list is still sorted.
3. By induction, insert sort will sort the entire list.


Obviously it’d look more rigorous than that, but that’s the general idea. Dijkstra and others used this style to prove a bunch of algorithms were correct, including many concurrency primitives. It’s also the style that gives rise to the [Knuth quote](https://staff.fnwi.uva.nl/p.vanemdeboas/knuthnote.pdf) “Beware of bugs in the above code; I have only proved it correct, not tried it.” It’s pretty easy to screw up a math proof in a way nobody notices, and I’ve read [estimates](http://mzone.mweb.co.za/residents/profmd/proofa.pdf) that something like 20% of published math proofs have errors in them. [Peter Guttmann](https://web.archive.org/web/20140630071239/http://www.cypherpunks.to/~peter/04_verif_techniques.pdf) has a great essay on how farcical code proofs got, where tons of “proven” code would immediately crash if run.


At the same time we were exploring how to automatically prove mathematical theorems, the first such **theorem prover** coming out in [1967](https://en.wikipedia.org/wiki/Automath). Researchers in the Pascal community were using theorem provers to verify programs by the [early 1970s](http://www.dtic.mil/dtic/tr/fulltext/u2/767331.pdf), then programming in dedicated verification languages by mid-decade. People would write some properties of the code and then write a checkable proof that the code had those properties. Earlier theorem provers simply helped humans check and verify proofs while more sophisticated ones could prove parts of the theorem on their own.


Which leads to the next problem.


## Proofs are hard


Proofs are hard. Obnoxiously hard. “Quit programming and join the circus” hard. Surprisingly, formal code proofs are often *more* rigorous than the proofs most mathematicians write! Mathematics is a very creative activity with a definite answer that’s only valid if you show your work. Creativity, formalism, and computers are a bad combination.


Take the above induction. Any mathematician could look at that and immediately know what induction is, how it works, and how it’s valid in this case. These are all things we need to rigorously formalize in the theorem prover. Same with proof by contradiction, proof by contrapositive, etc. Along with this, we also need to formalize every assumption, even the stuff that most mathematicians don’t bother to prove. For example, addition is associative: `a + (b + c) = (a + b) + c`. The theorem prover doesn’t a priori know that’s true. You either have to prove it (hard), declare it an assumption the prover can take as true (dangerous), or buy a theorem library from someone who already proved it (expensive). Early proof assistants competed on the number of inbuilt proof tactics and bundled theorem libraries. One of the first widespread proof checkers, SPADE, advertised its complete arithmetic library as a key selling point.


Next, you gotta actually get the proof. You can have the prover try to find it on its own, or write it yourself. In the general case, automatically infering a proof is undecidable. For extremely restricted cases, like propositional logic or HM type-checking, it’s “only” NP-complete. For the most part we’re stuck writing most of the proof ourselves and having the computer verify it’s correct. That means you need a strong background in:

- Math
- CS
- Whatever domain you’re working on, like hardware or compilers or whatever
- The intricacies of your program and spec
- The intricacies of the theorem prover you’re using, which is a specialty unto itself


To make things worse, computer properties throw a lot of wrenches into proofs. Remember how I said assuming addition was associative is dangerous? Some languages aren’t associative. C++ has `INT_MAX`. `((-1) + INT_MAX) + 1` is `INT_MAX`. `-1 + (INT_MAX + 1)` is undefined. If you assume associative addition in C++, your proof will be wrong, and your code will be broken. You either have to avoid making that assertion, or prove that for your specific snippet, you never cause an overflow.


Now you could say that undefined addition is a bug, and you should be using a language with unbound integers. But most languages have positive features that impede proofs. Take the following snippet:


```
a = true;
b = false;
f(a);
assert a;

```


Is that always true? Depends. Maybe `f` modifies `a`. Maybe another thread concurrency modifies `a`. Maybe `b` is aliased to `a`, so modifying it also modifies `a`.8 If any of these are possible in your language, you have to explicitly prove they don’t happen here. Purity helps in this case but can wreck proofs in other cases, as it forces you to use recursion and higher-order functions to get stuff done. Both of those, incidentally, are foundational to writing good functional programs. What’s good for coding is bad for proving!9


Formal verifiers have a dilemma: the more expressive the language, the harder it is to prove anything in it. But the less expressive the language, the harder it is to *write* anything in it. The first production verification languages were very restricted subsets of more expressive languages: ACL2 was a subset of Lisp, Euclid was a subset of Pascal, etc. And nothing we’ve discussed so far gets into actually proving real-world programs, this is all just the table stakes to start writing proofs in the first place.


Proofs are hard. They have, however, been getting better. Proof assistant researchers keep adding new heuristics, theorem libraries, preverified components, etc. Hardware improvements help, too: faster computers means faster searches.


### The SMT Revolution


These days the most population approach to proof automation is **SMT**.10 Speaking very broadly, an SMT solver can turn (some) theorems into constraint satisfaction problems. This turns a creative problem into a computational one. You may still need to feed it intermediate problems (lemmas) as steps in your theorem, but that’s better than proving every damn thing yourself. Stanford released the first “modern” SMT solver, the *Stanford Validity Checker*, in 1998. They built on that to make CVC, released in 2002, which saw minor production use. 11


The scene changed around 2006, when Microsoft Research released Z3. The big advantage of Z3 was it was a lot more user-friendly than other SMTs, which honestly wasn’t saying much. MSR used it internally to help prove properties of the Windows kernel, meaning they invested more-than-the-bare-minimum in UX. Z3 arguably made SMT the default choice for general-purpose automated proving. Many tools in CV now rely on SMT, and most of those come with Z3 by default.


Accessible SMT solving was a kick in the pants to the formal verification community, as it makes a lot of simple proofs trivial and nasty proofs tractable. This, in turn, meant people could start proving things in more expressive languages, as they now had the power to tackle the challenges of expressive statements. The incredible progress here is evident in the [IronFleet](https://www.microsoft.com/en-us/research/video/ironfleet-proving-practical-distributed-systems-correct-2/) project: by using advanced SMT solvers and a cutting-edge verification language, Microsoft was able to write 5,000 lines of verified Dafny code in only 3.7 person-years! That’s a blazing-fast rate of *four whole lines a day*. 12


Proofs are hard.


## Why Bother?


Now would be a good time to step back and ask “what’s the point?” We’re trying to prove some program conforms to some spec. Correctness is a spectrum. There are two parts of the verification question: how objectively “correct” your program is, and how much you’ve rigorously verified the correctness. Obviously, more verified is better than less verified, but verification costs time and money. If we have multiple constraints to optimize (performance, time to market, cost, etc), the optimium isn’t necessarily “fully proved correct”. Then the question becomes “what’s the minimal verification we need” and “how much does it cost to get there.” In *most* cases you can get away with, like, 90% or 95% or 99% correct. You may be better off spending time making the UX better than getting that last 1% of correctness.


The question, then: “is 90/95/99% correct significantly cheaper than 100% correct?” The answer is very yes. We all are comfortable saying that a codebase we’ve well-tested and well-typed is *mostly* correct modulo a few fixes in prod, and we’re even writing more than four lines of code a day. In fact, [the vast majority of distributed systems outages](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf) could have been prevented by slightly-more-comprehensive testing. And that’s just more comprehensive unit testing, to say nothing of fuzzing, property-based testing, or model-testing. You can get really far with simpler tricks without needing to go on to full proofs.


What if types’n’tests isn’t getting you enough verification? It’s still much easier to go from 90% to 99% than from 99% to 100%. As mentioned earlier, Cleanroom is a developer practice involving comprehensive documentation, careful flow analysis, and extensive code review. No proofs, no formal verification, not even any unit testing. But done properly, Cleanroom reduces the defect density to less than 1 bug/kLoC in production.13 Teams using it have equal or shorter delivery times than teams that don’t use it- certainly better than 4 lines a day. And Cleanroom itself is just one of many high-assurance techniques that sit between mainstream software practices and code verification. You do not need full code verification to write good software or even to write near-perfect software. There are cases where it’s necessary, but for most of the industry it’s a waste of money.


However, that does not mean formal methods as a whole is uneconomical. Many aforementioned high-assurance techniques rely on writing code specs that you don’t formally prove. As for verification, there are two common ways people benefit from it in the industry. The first is verifying designs instead of code, which we will cover in the next section. The second is *partial* code verification, which we will cover right now.


## Partial Code Verification


It’s too expensive doing full verification in day-to-day programming. What about partial verification? I could still benefit from proving some properties of some parts of my code. Instead of proving that my sort function always sorts, I can at least prove it doesn’t loop forever and never writes out of bounds.  You can still get a lot of benefit out of this. For example, writing even basic proofs about C programs is a great way to [cut out huge amounts of undefined behavior](http://www.cccblog.org/2018/06/13/the-surprising-security-benefits-of-end-to-end-formal-proofs/).


The limitation here is *availability*. Most languages are designed for either full verification or no verification. In the former case, you’re missing a lot of nice features in more expressive languages, and in the latter case you a need a way to prove stuff in a language hostile to the concept. For this reason, most of the research on partial verification focuses on a few high-priority languages, like [C](https://frama-c.com/) and Java. You also see a lot of people working with restricted subsets of languages. For example, SPARK is a restricted subset of Ada, so you can write critical stuff in SPARK and have it interop with less-critical Ada code. But most languages like that are pretty niche.


More commonly, people bake specific kinds of verification into the the core structure of languages. Production type systems are a common form of this: you may not know that `tail` always returns the tail, but at *least* you know that it has type `[a] -> [a]`. You also have cases like Rust, which proves memory safety, and Pony, which proves exception safety. These are slightly different from SPARK and Frama-C in that you can *only* do partial verification, not some partial and some full verification. They also tend to be made by programming language experts over formal methods experts, two disciplines that have a lot of overlap but aren’t identical. This might be why languages like Rust and Haskell are actually-kinda-usable in practice.


# Design Specification


So far we’ve only talked about code verification. There’s another side to formal methods, though, which is going one step more abstract and verifying the designs themselves. This is deep enough that it’s synonymous with **formal specification**: if somebody says they do formal specification, they probably mean they specify and verify designs.


As we talked about, proving every line of code is really, really hard. But many problems with production systems aren’t in a line of code: they’re in the interaction between components of a system. If we handwave away the details of implementation, like saying “just assume it can identify birds”, we can more easily look at how Park or Bird as a high-level module fits in with our overall design. Once you zoom out enough, though, it becomes possible (or at least much easier) to describe things you couldn’t possibly implement, like the runtime environment, human interactions, or the merciless flow of time.14 At this scale, we’re now formalizing our intentions with the overall system instead of our intentions with the lines of code. This is much closer to the human level, where designs and requirements can be much more ambiguous than at the code level.


To give an example: take code procedure with the rough specification “if called, it makes a syscall to persist data to storage and handles system errors.” The properties you need to verify, while difficult, are sort of straightforward. Does it serialize data properly? Do malformed inputs violate our guarantees? Do we handle all possible ways the syscall could fail? Now compare a high level logging system with the specification “all messages are logged.” You now have to answer:

- All messages, or all messages *that reach the system*? Are messages logged once or *exactly* once?
- How are messages being sent? Is it a queue? Does the transfer medium deliver once? Does it deliver in order?
- By “logged”, do we mean “permanently logged?” Is the message allowed to be logged and later unlogged? Is it allowed to “bounce” between logged and unlogged before ending logged?
- What if the server explodes in the middle of logging the message? Do we need journaling?
- Are there any properties of the storage medium that matter? Is “the medium loses data” outside the scope of our requirements or not?
- What about GDPR?
- etc etc etc


Without the benefit of a formal design, it’s harder to express what you actually need the system to do. If you can’t express what you need, you have no idea if your design actually *gives* you what you need or something else that sounds kinda the same but has very different consequences. By being formal in expressing our intentions and our design, we can more easily make sure we’re actually building what we need to build.


Just as we use programming languages to represent code, we use **specification languages** to represent designs. Spec langs are usually oriented for design specification, not code specification, although some languages can be used for both.15 Going forward, I am going to refer to specification languages as **design languages** (DLs) so as to absolutely minimize confusion.16


The first full DL was arguably VDM, which came out around 1972. Since then, we’ve seen a huge variety of different spec langs. The space of design languages is a lot more diverse and fragmented than code verification languages. As a very rough stereotype, people invented DLs as a means to an end, while people invented CVLs as an end itself. Since they’re heavily influenced by specific problem domains, DLs have all sorts of ideas and semantics. As a very, *very* brief tour of some early design languages:



| $Language | modeled | with |
| Z | Business Requirements | Relational Algebra |
| Promela | Messaging | CSP |
| SDL | Telecommunications | Flowcharts |
| Harel Statecharts | Controllers | Automata |
| Decision Tables | Decisions | Tables |



As people mostly designed DLs to solve specific problems, most of them have at least two or three real-world case studies. Results are generally very positive. Practicioners say it gives them insight into the problems and makes it easier to explore solutions. For a long time the biggest champion was Praxis (now Altran), which used [“correct-by-construction”](https://www.youtube.com/watch?v=03mUs5NlT6U)- a combination of Z designs and SPARK code- to build safety critical systems. They claimed that they could work much faster and more cheaply by writing specs, as they wouldn’t discover design mistakes in the late-stage of the project.


More recently, Pamela Zave was dabbling with Alloy and discovered that Chord, one of the major distributed hash tables, was [fundamentally broken](http://www.pamelazave.com/chord.html). More recently than that, AWS started finding [35-step critical bugs](http://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf) by writing TLA+ specs. In my experience, people who try writing specs become big fans.


But there’s also a big mismatch in the value between fans and outsiders. To fans, the biggest benefit is that the act of writing a design forces you to understand what you’re writing. When you have to formally express what your system does, suddenly a lot of subtle errors become painfully obvious. This is utterly unpersuasive to outsiders. If you want to get people to try use a DL, you need to give them a way to verify their design actually has the properties they want.


Fortunately, this is also extremely important to a lot of specifiers, so design verification is a big field of research.


## Model Checkers


As with code, we can verify designs by writing theorems. Thankfully, we’ve got another trick here: we can use a **model checker**. Instead of writing a proof that a design is correct, we just brute force the state space and see if any reachable state is *incorrect*. If we can’t find any, then we’re good.17


There’s a lot of benefits to model checking. One, you don’t have to write a proof. That saves a lot of time and effort. Two, you don’t have to learn *how* to write a proof, so the skill barrier is a lot lower. Three, if your design is broken the model checker will give you an explicit counterexample. This makes fixing issues much, *much* less painful, especially when the bug takes 35 steps to reproduce. Good luck finding that on your own.


There are also a couple of drawbacks. One is that they’re a little less powerful. Specifically, you could be dealing with an **unbounded** model, where there’s an infinite number of distinct states. For example, if you’re speccing out a message queue processor, it’s pretty straightforward that it works when given a list of ten messages. But if you need to make sure it works for any list of messages, well, there’s an infinite number of those, so an infinite number of states. Most model checkers have various tricks to handle these, like identifying equivalence classes or symmetries, but it’s really on a case-by-case basis.


The other big drawback is **state-space explosion**. Imagine you have three processes, each four sequential steps long, and can they can interleave the steps in any way. If they don’t affect each other’s behaviors, there are `(4*3)! / (4!)^3 = 34,650` total possible executions (behaviors). If each process has one of five initial states, you now have 4,300,000 total behaviors. And the model checker has to make sure all of them behave nicely. And this is assuming they don’t interact with each other! If they do, the state space gets bigger even faster. The combinatorial explosion is seen as the primary challenge to model checking, and there’s a lot of work put into making this more tractable.


But in the meantime, there’s another way to handle state explosion: throw more hardware at it. The biggest challenge to model checking is “just” a performance problem, and we are *very* good at solving performance problems. Most (but not all) model checking is easily parallelizable. After optimizing your model and checking it with small parameters, you can spin up an AWS cluster and run it with large parameters.


In practice, a lot of specifiers use model checkers and then switch to theorem provers as necessary.18 A lot more specifiers use model checkers and then, when reaching their limits, switch to less intensive forms of verification.


### The Problem with Design Specs


So design verification is easier and faster than code verification and has a lot of spectacular successes. Then why don’t people use it? The problem with DV is much more insidious. While code verification is a technical problem, design verification is a social problem: people just don’t see the point.


Much of this is a consequence of *designs are not code*. With most design languages, there is no automatic way to generate code, nor is there a way to take existing code and verify it matches a design.19 Programmers tend to mistrust software artifacts that aren’t code or forcibly synced with code. It’s the same reason documentation, comments, diagrams, wikis, and commit messages are often neglected.


Programmers also just don’t seem to believe there’s any benefit to specifying. At least in my experience, they assume whatever they currently use (pseudocode, diagrams, TDD) is more than sufficient to getting the design right. I don’t know if this is universal, and I don’t have a good explanation besides general conservatism. My reasoning is that every methodology community I know has the exact same complaint: TDD folk gripe that people don’t want to try TDD, Haskellers gripe people don’t care about static typing, etc etc etc.20 It’s just really hard to get people excited about something they don’t already do, even if they agree that there are benefits.


# Summary


Verifying code is a hard problem. More and more people are doing it, though, as theorem provers and SMT solvers get more sophisticated. It will probably remain a specialist thing for the foreseeable future.


Verifying designs is much easier, but has cultural barriers to adoption. I think this is possible to change, though. Twenty years ago automated testing and code review were pretty niche things and they eventually went mainstream. Then again, code contracts was a niche thing and still is.


Hopefully this explains more about why FM is so niche, at least better than the usual “web don’t airplane” argument. Feel free to yell at me if there is any obvious mistakes I made.


*Interested in using design specs at your work? [Buy my book](https://www.apress.com/us/book/9781484238288) or [Hire me](https://www.hillelwayne.com/consulting)!*


*Thanks to Nick P, [Richard Whaling](http://twitter.com/richardwhaling), [Ron Pressler](https://pron.github.io/),  and [John Regehr](https://blog.regehr.org/) for feedback.*


---

1. TLA+ is one of the more popular formal specification languages and you can probably fit every TLA+ expert in the world in a large schoolbus.
 [return]
2. And a disclosure: I run TLA+ and Alloy workshops for a living, so I’m highly biased towards those two languages. I tried to account for that in this history but y’know bias is bias.
 [return]
3. ML was originally invented to help write specs of this form.
 [return]
4. It’s up for debate whether work on Euclid or [SPV](http://i.stanford.edu/pub/cstr/reports/cs/tr/79/731/CS-TR-79-731.pdf) was *started* first, but AFAICT I think Euclid was *presented* to the public earlier.
 [return]
5. Design by Contract is *not* using “design” in the same way I am using it in this essay. It is about using contracts as code specs, not as design specs.
 [return]
6. Oh hey, if you do formal verification in a language we don’t have yet, why not make a pull request?
 [return]
7. Not that I’m bitter or anything.
 [return]
8. Aliasing is so hostile to writing proofs that John C Reynolds had to create an entirely new logic, **Separation Logic**, to handle it.
 [return]
9. In his [Turing Lecture](https://amturing.acm.org/vp/clarke_1167964.cfm), Edmund Clarke listed some challenging properties to verify: “floats, strings, user-defined types, procedures, concurrency, generics, storage, libraries…”
 [return]
10. SMT stands for **Satisfiability Modulo Theories**: Solving a SAT problem where some of the variables can be math equations.
 [return]
11. This section originally said the first SMT solvers started appearing around 2004, which is incorrect. They’re almost a decade older than that. It also sorta implied that SMT was the first major attempt at automated theorem proving, which is *atrociously* wrong. Thanks to Don Syme and Heidi Khlaaf for calling this out.
 [return]
12. The previous record was probably [seL4](https://sel4.systems/), whose developers wrote the equivalent of *two lines of C* a day.
 [return]
13. Most of these numbers come from Stavely’s research in *Toward Zero-Defect Programming*. As always, [be skeptical of results and reread the original papers](https://leanpub.com/leprechauns).
 [return]
14. If there’s one thing that studying formal methods has taught me, it’s that time is evil and I hate it.
 [return]
15. The process of mapping design specifications to code specifications is called **refinement**.
 [return]
16. As before, this is *not* common terminology. Most people use “specification language”, but I want to make clear the distinction between code specifications and design specifications.
 [return]
17. Model checkers are also used in code verification, such as [JMBC](https://www.cprover.org/jbmc/), but model checking makes up a much bigger percentage of design verifications than code verifications.
 [return]
18. Keep in mind “a lot of specifiers” is, like, ten people.
 [return]
19. Generating code from specifications is called **synthesis**. See [Nadia Polikarpova](https://www.youtube.com/watch?v=HnOix9TFy1A)’s work for a good crash course. Proving code matches a spec (or one spec matches another spec) is called **refinement**. Both of these are active areas of research.
 [return]
20. One argument I’ve heard is that Agile rejects up-front design, so nobody wants to do formal specification. This may contribute, but many of the people I’ve met who reject Agile also reject FM about as often as Agilists do. Another argument I’ve heard is that historically formal methods has consistently overpromised and failed to deliver. This may also contribute, but most people haven’t even *heard* of FM, much less know about the history of it.
 [return]
