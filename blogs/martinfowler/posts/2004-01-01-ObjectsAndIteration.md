---
title: "Objects And Iteration"
description: "From the very beginnings of object-oriented development, OO design has been linked with iterative and incremental development. But as many point out, there's no inherent link between the two. You can "
date: 2004-01-01T00:00:00
tags: ["computer history"]
url: https://martinfowler.com/bliki/ObjectsAndIteration.html
slug: ObjectsAndIteration
word_count: 392
---


From the very beginnings of object-oriented development, OO
design has been linked with iterative and incremental development. But
as many point out, there's no inherent link between the two. You can
do OO in a waterfall, and you can do IID without objects. So why are
the two so closely linked?


I don't think there's a definitive reason, but there are few
indicators. One is a technical aspect. Objects provide a very fine
grained modularity, where the program is divided into small
substitutable modules with separation of interface and implementation.
The class provides the encapsulation that supports the
interface/implementation division and polymorphism provides a simple
substitution mechanism.


This fine-grained modularity, when done well, allows you to make
changes to an existing code base much more easily. This is important
for IID because the whole point of IID is that you don't have a
comprehensive design at the beginning, you grow the design and the
code together. Good modularity is essential to this. (An interesting
non OO example of this is the Unix community, which stresses
modularity in order to evolve, but isn't so keen on OO.)


A large part of the impetus in the OO world comes from Smalltalk,
even though the number of Smalltalkers are (and were) small, they were
disproportionately loud. Smalltalk is an environment that has many
features, beyond just the OO ones, that support IID. Immediate
compiles and links into a running system, a good IDE that really helps
navigate around the source code, emphasis on a graphical user
interface (before this was common), an environment that hides many low
level issues like memory management, a large class library - all of
these things enable iteration. (Again the Lisp community also had all
of this and is also strongly iterative.)


So there's technical reasons why objects encourage IID, but also
there's social reasons. The leaders of the OO world pushed IID right
from the beginning, which is why it's no surprise that the leaders of
the agile movement almost entirely are OO people. When the leadership
embraces both movements so fervently that has an effect on the whole
community. I certainly grew up in this community with both objects and
iteration as given.


All this doesn't mean that objects and IID are mutually
necessary, but I think it does indicate why the two have such a strong
affinity.
