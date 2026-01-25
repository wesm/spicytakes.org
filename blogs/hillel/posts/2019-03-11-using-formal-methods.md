---
title: "Using Formal Methods at Work"
date: 2019-03-11
url: https://www.hillelwayne.com/post/using-formal-methods/
slug: using-formal-methods
word_count: 3455
---

A few people have told me that they’ve enjoyed learning formal methods but aren’t sure how to actually use it. They’re mostly doing short sprints at work and aren’t building new systems from scratch. This tells me there’s some confusion about what makes specifications useful, and that we need a resource on applying them in practice. This is a short guide to using specifications at work in a way that’s accessible to beginners, applicable in many contexts, and provides solid business value.


There’s a major disclaimer I have to make here: **I teach formal methods workshops for a living.** That makes everything I write on formal methods at least a little bit of an advertisement. I’d rather be up front about that so you know what you’re getting into.


If this is your first encounter with formal methods, you might be more interested in my essay on its [history and limitations](https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/), or my talk on its [practical applications](https://www.hillelwayne.com/talks/distributed-systems-tlaplus/).


## Assumptions


I’m using formal specifications here to mean languages you can express high-level properties in, but formalized enough that you can machine-check them for conformance. This includes languages like [TLA+](http://lamport.azurewebsites.net/tla/tla.html), 
  
    [Alloy](http://www.alloytools.org)
  

, and [Event-B](http://www.event-b.org/), and excludes things like [Coq](https://coq.inria.fr/), [decision tables](https://www.hillelwayne.com/post/decision-tables/), and [Gherkin](https://docs.cucumber.io/gherkin/).1


This all assumes you’re writing a “typical” business or infrastructure system, whatever that’s supposed to mean. Some amount of minor bugs are tolerated, but major bugs are to be avoided. These are rough rules of thumb to keep in mind for your specs. Break them as appropriate.


### Specs are high-level


Consider a component that receives a message and does something with it. If there’s a problem with the message, ill-formed, delivered wrong, anything, we instead do something else. The error checking, formatting, auditing, everything can be an entire subsystem, but if it’s not the one we care about we can collapse it all into something like this:


```
pred handle_message {
  do_good_thing or
  do_error_thing
}

```


This corresponds to “every message is good”, “every message is bad”, “the first ten messages are bad and the rest good”, etc. These are all valid paths in the spec, just as they all can happen in the real system. When I run a model checker against it, it will check all of these.


### Specs are partial


Specs don’t need to describe the total behavior of the system. If your system does A, B, and C, it’s usually much faster to write three different specs, each of which assumes two of the components are already working correctly. A fourth spec might show how all three interact, but with less detail about each component than the specialized specs have.


This doesn’t give you as much detail comprehensiveness as modeling everything at once, but it has a lot of benefits. First, each partial spec can focus on what you care about with that component. Second, you can use each partial spec without having to whole system designed out; it’s useful more early. Third, it model checks a lot faster. Four, composing specs is a *lot* harder than writing independent specs, and you often have to “weaken” a spec to easily pull off composition. 2


### Specs are short


A corollary of the first two. A high level spec can be orders of magnitude smaller than the actual code.


### Specs are imperfect


The more time you invest in writing a spec, the more comprehensive it is. But- as with everything- there’s diminishing returns. It requires a lot more work to go from 95% correct to 99% correct than to go from 85% to 95%. I’m staying in that zone of maximal returns, purely because it’s what’s most accessible and pragmatic for most people. Speccing in this style won’t make your software bug-free, but it will make it much higher quality than not speccing at all.


### Specs are not code


Most formal specification languages cannot be automatically **refined**: you can’t easily verify your lines of code match the specification. In some ways this is a problem, but it also has a surprising benefit: the spec exists apart from your code and is not a dependency. This means that trying specifications, unlike trying new languages, does not carry a risk of technical debt or add any maintenance burden. You also don’t have to change the code to make writing specs possible. This all reduces the friction of experimenting with FM. Harder than trying a new monitor setup, but easier than adding Elixir to your tech stack or getting your coworkers to pair program.


### Specs are not tests


There are two kinds of system errors: **implementation errors** and **design errors**. Tests are good for showing your code matches your expectations but very bad for showing your expectations match your needs. Specs are the opposite. You need both. Specs are also not documentation, code review, code static analysis, or post-release analytics. It might make it easier to do all of them, but it does not remove the need for them.


There are cases where specs can remove the need for code testing, but that kind of spec is [much harder to write and useful in a more specialist domain](https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/).


## Approaches


Writing a specification serves three main purposes:

1. It provides clear documentation of the system requirements, behavior, and properties.
2. It clarifies your understanding of the system.
3. It finds really subtle, dangerous bugs.


(3) is the most *unique* benefit and arguably the one that delivers the most *obvious* business value. But all of these are very valuable. The easiest ways to start applying specifications mostly give you (1) and (2). Since people don’t notice those benefits as much, it makes them think they have to dive into the deep end to get any use out of specs.


The following projects are in ascending order of effort/skill. This is a rough guide, not a lesson plan: don’t feel obligated to do them all as “exercises” or anything. You can use this to figure out where you’re most comfortable starting and how you’re most comfortable progressing. This is also not in ascending order of *usefulness*. Even documenting your own systems can be very useful.


### Documenting your existing system


Take a system you’ve worked with for a while, that you think you know pretty well. Write a high level specification of the architecture or some of its features. Don’t worry about composing specs, just write disconnected models of various points of interest. You aren’t necessarily looking for errors in the architecture; the goal is to get hands-on practice writing a spec. If your spec shows behavior you don’t see in the existing system, it’s usually a sign that you made a mistake in writing the spec.


*Usually*. It’s also possible that you misunderstood some aspect of the system. This is useful to know, but the uncertainty (is it a translation error or an understanding error?) might not be great for improving your modeling skill. That’s why you document a system you know well. It isolates just the modeling practice.


There’s also a chance that you didn’t make any mistakes and there’s actually a subtle problem with the system. This happens a lot more often than you’d expect. I’d say if you’re just starting out to still consider this a possibility, but not to make it your first assumption.


While doing this focuses on you learning FM, it still produces enough tangible benefits for a business case. First, you have a spec of your system, with the assumptions, behavior, and requirements rigorously stated. I’ve found that this makes a great documentation supplement when explaining something to other engineers. Also if you later need to modify the system, you already have the model part done.


### Showcasing a bug


Take a system for which you’ve fixed a complicated bug. Write a model that matches the broken version of the system and show that it catches the same bug. This gives you good practice with writing invariants. It also helps you find invariants for the existing system: what’s the weakest possible property that is violated by the bug?


There’s an ulterior reason to do this, too: it’s great for showing the value of writing specifications. If you have data on how long the bug was present and how long it took to find the bug, you can show the time difference between “catching this bug in production” and “catching this bug in the model”. The difference could very well be something like “several weeks” versus [half an hour](https://www.hillelwayne.com/post/augmenting-agile/).


### Finding a bug


Take an existing system with an observed bug and write a model that has the bug. This is different from showcasing a bug in that you don’t have full information on the bug, as you haven’t actually localized or fixed it yet. The purpose of the spec is to make it easier to find the bug. If you can accurately reproduce it in the model, it will show you the series of steps that leads to the bug. You can then determine where things start going sideways in the spec, and use that to localize the bug in the code itself.


If you can’t reproduce the bug, it could be from a few common reasons. One is that the spec could be too high level. You might be abstracting the error handling as correct but you actually missed an error case. Another is that the bug could be a *slip*: you got some implementation detail wrong. Think something like writing `merge(f, g)` instead of `merge(g, f)`, putting two lines in the wrong order, etc. These are all problems that easily sneak past a spec. Specs are better at reproducing bugs from holes in the design, or when a design has “correct” but unintended behavior.


Sometimes you’ll find the bug because of the model checker. In many cases, though, the spec makes the bug “obvious”. It’s much easier to see a race condition in 10 lines of spec than in 1,000 lines of code. This leads to a common beginner frustration with formal specifications, that they’ve already figured things out before finishing the model. This is actually one of the big benefits of specification: most of the model checking can happen in your head.


One example I worked on: why wasn’t a kill-switch working? After a couple days fruitlessly trying to track it down, I wrote a spec and immediately went “oh right, the kill-switch prevented us *enqueueing* jobs, not *processing* them.” Obvious in the spec, less so in the codebase.


### Understanding an unfamiliar system


Take a system you want to understand better and write a model for it. A spec error is much more likely to mean you misunderstood something than a failed spec meant for your own system. But writing the spec will help significantly even before you verify it. You can’t really handwave in a spec: everything you write must be precise and rigorous. This does wonders for understanding something.


It also provides a good way to verify your knowledge is correct. You can see what happens when you run it through a model checker and compare it to the behavior of the real system. You can also show the model to a domain expert and see if it matches their understanding of the system.3 If it does not, you have a precise way of knowing how your understanding diverges.


In my experience you’re also more likely to find critical bugs by modeling unfamiliar systems than ones you’re familiar with. I have no idea why. Regardless if you decide to bring up a bug with someone, remember to be respectful and empathetic. Just as specs don’t replace tests, specs don’t replace social skills.


### Changing an existing system


Take a system, a model of that system, and a new requirement or desired change. Show that it does not satisfy the requirement, and then modify the model until it does.


At least in my experience this ends up being the most regular use of FM on a project. Since the spec is high level, most changes will map to only a few lines of modified spec. Before you make a change, vet that the change you make actually does what you want. This helps you understanding what you’re doing. It also helps a ton with finding bugs, showing how a small change in your system propagates into global invariant violation.


Another benefit you get here: Writing a spec sanity-checks the requirements. If I say “at least one node must always be online”, do I mean “there is at least one node that is online the entire time” or “at all points in time, there is at least one node online”?4 It’s a lot easier to see the difference when writing a spec than when knee-deep in the codebase. Sometimes the client will be able to clarify which they meant, and in rare cases the client will realize they don’t actually know what they want.


### Building a new system


Make a new system from scratch, using specifications. Alternatively, add a significant new feature to a system using specs. This requires the most skill in both writing specs and knowing when to *stop* writing a spec, but it’s actually not that much harder than modeling an existing system. It also has the most drastic benefits, as you’re getting all of the knowledge boosting and model-checking right from the start.


A common beginner mistake is trying to model the system in too much detail before you start building it. Remember, the spec is your design. It’s incredibly valuable to have a design, but it’s not the code, and much of the code you write won’t be reflected in the design. It doesn’t matter to the system the specific classes or functions you have, just that there is a behavior they produce.


-


One of the big things you might notice: these are all iterative. You’re not spending weeks and months writing exhaustive specifications before doing a day of coding. And you’re not blindly following a plan: if reality intervenes you adjust the spec and see what the consequences are. The spec is there to amplify your ability to think through the design, not force you on a rigid path.


The biggest gap here is that this is all individual-based, not team-based. Enterprise FM is still extremely new as a practice, so we don’t have solid information on how it fits into a larger team workflow. There’s a few different companies adopting FM more widely and I’m excited to see how it works out for them.


There are some projects where exhaustive specification makes sense. Most of us aren’t doing those. There are some projects where specs don’t make sense at all. Most of us aren’t doing those, either. We’re in the sweet spot where *some* form of specification helps a lot, but the vast majority of us don’t use it.


But part of using something well is knowing when it applies. So to make specifications useful, we should also know when they aren’t.


## When not to spec


You don’t write specs when it’s not worth writing specs. Of course that’s circular, we’re more interested in what makes it not worth writing specs. There’s actually two facets to this question: when not to write specs at all, and when not to add more lower-level detail to an existing spec. Both are driven by the same constraints.


There are some things that make specs less useful. Speccing might still be worthwhile even if these hold, but you’d likely be investing less time and effort into it. Also, this is biased towards my experiences with specifications: there could be languages out there that are good for these kinds of problems.


### Low Cost of Error


If there’s an error, it’s obvious, easy to isolate, and causes few issues. This doesn’t mean you don’t want errors, it just means that you can quickly find and fix them. One example is a batch job that looks at a low volume of data and constructs a report: most of the errors that a spec would surface would be obvious in production, and once you fix it you can easily rerun on the old data. Ideally. Specs could still help here, but their correctness benefits are less valuable.


### Too Low-Level


Not all code is a projection of some abstract design. Sometimes the essential idea lies at the code level, in which case a spec is missing the trees for the forest.


A lot of munging and data plumbing is like this. Take a program that hits ten APIs, extracts the information and splices it together. There’s some higher-level design there, with error handling and the retry behavior and all, but the majority of the work lies in the implementation-level transformations of the raw data. Design specs are too far removed from that to be much help; you want something closer.


And any kind of numerical computing is right out. Most specification languages can express integers but very few can actually model-check them. The only tool I’ve seen that can handle any kind of real number is [PRISM](http://prismmodelchecker.org/), which has… other issues.5 You will not be verifying your mathematical operations at the design level.


### Ambiguous Properties


As the Agile folk are fond of saying, the best way to understand what people need is to see how they interact with an existing system. But that doesn’t necessarily mean the system has to be complete: often a prototype is enough. Requirements change often, and our understanding of what’s needed in the early stages is often minimal. There are some properties a system probably *shouldn’t* have, like “crashes randomly” or “explodes”. But these aren’t necessary properties of a prototype! If a person is using a system to understand what they want from the system, then it’s less important that the system “work”. We’re gathering data.


In a sense, the prototype takes the place of the spec in this stage: instead of iterating on a spec to find system issues, you’re iterating on a prototype to find client issues.


### Augmentation Code


This one’s a little messier than the rest. One of my software beliefs is that most programs are either written to *automate* something so humans don’t have do to it, or *augment* a human so they can do something better. Graydon Hoare calls this the difference between [batch processing and interactive computing](http://graydon2.dreamwidth.org/3186.html). The lines between the two aren’t clear-cut: is a calculator automating away the rote computation or augmenting your ability to do calculations? Little of both, really. But I still find this a useful model.


In my experience, specs are much more useful for automations than augmentations. In an automation, a human might start it up but not necessarily do anything afterwards, so it’s more important that it satisfies invariants. Augmented code has a human constantly in the loop, who can adjust the system and self-correct.


## The Pitch


Okay, you’ve read this far, time for the pitch. Formal methods are an incredibly powerful tool. The biggest barrier to using them, in my opinion, is education. FM requires a different mindset from coding and sometimes people have trouble building the intuition. There’s also an implicitly-assumed set of math skills that are easy to learn but hard to realize you need to learn. I wrote [a book](https://www.apress.com/us/book/9781484238288) to help people with this, but nothing beats having an experienced teacher.


You can hire me to do corporate workshops or provide 1-on-1 training to people in your company. I’ve had clients see savings of six-figure savings per year by writing specs, for much the same reasons you save money writing tests. You can contact me [here](mailto:consulting@hillelwayne.com) or read more about my services [here](https://www.hillelwayne.com/consulting/).


*Thanks to [Jay Parlar](https://twitter.com/parlar), [Lorin Hochstein](http://lorinhochstein.org/), and [Miikka Koskinen](https://miikka.me/) for feedback.*


---

1. *Very* briefly: Coq is more for verifying code than designs, which is a more specialist domain. Decision tables are **flyweight methods**: easy to learn and use, applicable in focused, narrow contexts. Gherkin is informal and code-level, not design-level.
 [return]
2. There’s lots of reasons for this. One is the **frame problem**: X’s doesn’t say what happens to the values in Y’s spec and vice versa, so the composed spec is ill-defined unless you carefully define how they compose.
 [return]
3. This requires them to understand the spec language, of course. But I’ve found if you walk someone through a spec, you can explain exactly as much as they need to know relatively quickly. It’s easier to learn to read specs than learn to write them.
 [return]
4. More formally, it’s the difference between `∃n ∈ Nodes:`□`Online(n)` and □`∃ n ∈ Nodes: Online(n)`.
 [return]
5. Like the lack of arrays. And strings. And functions. PRISM is an interesting but *extremely* niche modeling language.
 [return]
