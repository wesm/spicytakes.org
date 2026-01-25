---
title: "The Business Case for Formal Methods"
date: 2020-01-22
url: https://www.hillelwayne.com/post/business-case-formal-methods/
slug: business-case-formal-methods
word_count: 1226
---

This is an “intro packet” you can use to argue for the benefits of formal methods (FM) to your boss. It’s a short explanation, a list of benefits and case studies, and a demo. Everything’s in TLA+, but the arguments apply equally well to Alloy, B, statecharts, etc. Adapt the material to your specific needs.


Quick notational note: I’m leaving out the code verification side of formal methods, mostly because design verification is a much easier sell.


---


### Intro


Formal Methods, or FM, is a *debuggable design*. You write a specification of your system and properties you want it to have. Then you can directly test the design *without having to write any code* and see if it has problems. If it has a problem, great, you can fix it without having spent weeks building the wrong system. If it doesn’t have a problem, you can start implementing with confidence you’re building the thing right.


### Why use formal methods


It’ll save you money. FM finds complex bugs in complex systems. The more complex the system is, the more likely a bug will slip past your testing, QA, and monitoring. Since it works at a higher level of design, an hour of modeling will catch issues that days of writing tests will miss. And since it doesn’t require writing the entire system, it can catch the bugs before they’ve been implemented in the first place. That means you don’t have to spend developer time rewriting the incorrect code.


Formal Methods also saves money on development time and maintenance. If you can directly test designs, you can create much simpler systems that are easier to implement.


You can also apply FM on existing legacy systems. This can find latent bugs before people start running into them.


If you are dealing with complex systems, formal methods can be the difference between “on time and under budget” and “two months late and then another two months of maintenance fires.”


### Demo


*A short demo you can use to show specifications in action. This demo is in TLA+.*


Consider a bare minimum carbon credit trading platform:

- Every credit has an owner.
- An owner may **offer** the credit to a different user. The recipient user can accept the offer, in which case ownership of the credit transfers to them, or reject it, in which case nothing happens.
- The accept/reject is asynchronous: you can offer the same credit to multiple people (to scaffold out trades), and the person may wait a day before accepting or rejecting an offer.


There’s a serious bug in that. Do you see it?


…


Give up? Here it is:

1. Acme has credit C1.
2. Acme offers C1 to Nologo.
3. Before Nologo accepts, Acme makes a second offer of C1 to Brandco.
4. Brandco accepts. Ownership transfers to Brandco.
5. Nologo accepts. Ownership transfers to Nologo.


Brandco didn’t offer Nologo the credit; Acme did. But ownership has transfered from Brandco to Nologo. This is a very severe bug for several reasons:

- It’s **complex**. It takes three people and four steps. Your unit tests won’t find this.
- It’s **subtle**. The only symptom is credits mysteriously disappearing from people’s accounts. Your QA and monitoring won’t find this.
- It’s **dangerous**. It violates a core requirement of your system. It will cause your customers to lose money and stop trusting you.


So subtle, complex, dangerous. These are *expensive* bugs. The longer this bug is in production, the more money you lose.


By contrast, here’s what happens if you use a spec:


Show Spec
  
`EXTENDS Integers, Sequences, TLC
CONSTANTS Business, Credits

set ++ x == set \union {x}
set -- x == set \ {x}

VARIABLES owner, offers
vars == <<owner, offers>>

Init ==
  /\ owner \in [Credits -> Business]
  /\ offers = {}

Propose(from, to, credit) ==
  /\ owner[credit] = from
  /\ offers' = offers ++ <<from, to, credit>>
  /\ UNCHANGED owner

Accept(from, to, credit) ==
  /\ <<from, to, credit>> \in offers
  /\ offers' = offers -- <<from, to, credit>>
  /\ owner' = [owner EXCEPT ![credit] = to]

Reject(from, to, credit) ==
  /\ <<from, to, credit>> \in offers
  /\ offers' = offers -- <<from, to, credit>>
  /\ UNCHANGED owner
  
  
Next ==
  \E from, to \in Business, credit \in Credits:
    /\ from /= to
    /\ \/ Propose(from, to, credit)
       \/ Accept(from, to, credit)
       \/ Reject(from, to, credit)

Spec == Init /\ [][Next]_vars

\* If ownership changes from A to B
\* It's because B accepted an offer from A
ValidChange(credit) ==
  LET co == owner[credit]
  IN co /= co' =>
    Accept(co, co', credit)

\* All changes in the system are valid changes   
ChangeInvariant ==
  [][\A c \in Credits: ValidChange(c)]_owner 
`

show all


That’s fifty lines of TLA+. It took me five minutes to write. By saying that `ChangeInvariant` is a requirement of my system, I can tell a model checker to see if my design violates that requirement:


It took the model checker two seconds to find the error. In less than six minutes I designed the system and found an expensive bug. I even have a set of steps to reproduce the bug, so I can write regression tests on the code itself.


### Why *not* use formal methods


*If people ask for the downsides, or if you’re uncertain if you think this would be useful in the first place.*


Specifications are flexible enough to work with legacy systems and any programming language. The tradeoff for this is that you don’t get automatic code translation: you can’t take your design and automatically generate matching code. That would come at the cost of flexibility. You wouldn’t be able to use it for any language or on legacy code. If you need to be absolutely, 100% sure that your code matches the design, you need different tools. You will also need to spend a lot of time and money making sure they match.


Writing specifications are best when you’re working on a complex system. If you can keep the whole system “in your head”, or if it does not involve a lot of intricate logic, specifications may not provide you much benefit. As a rough rule of thumb, I don’t think specifying things that would take less than a week to implement is worth the effort.


Finally, specifications are a not very good at finding simple implementation errors, like an uncaught exception or an unhandled null. If you know that bugs are going to be simple or low-cost, you’re more likely to find them with tests and QA than with specifications.


---


If you can convince your boss, why not also get my services?


### Consulting


The AWS paper says that people can learn the basics of TLA+ within a few weeks. That’s on their own, though. With the help of a skilled instructor, students can learn it in less than three days.


I’m one of the most experienced instructors on teaching specification languages. I’ve written an [online resource](https://learntla.com/) and [a book](https://www.apress.com/us/book/9781484238288) for TLA+ and am currently working on new documentation for Alloy. My workshops are three straight days of labs, group exercises, and hands-on experience: actually teaching people as opposed to checking boxes. You can read more [here](https://www.hillelwayne.com/consulting/) and email me [here](mailto:consulting@hillelwayne.com).


*Thanks to [Colin Curtin](https://twitter.com/perplexes), [Peter Bhat Harkins](https://malaprop.org/), and [Jay Parlar](https://twitter.com/parlar) for feedback.*


---

1. Disclaimer, I lead this project at eSpark.
 [return]
