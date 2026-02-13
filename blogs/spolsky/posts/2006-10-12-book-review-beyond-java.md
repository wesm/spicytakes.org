---
title: "Book Review: Beyond Java"
date: 2006-10-12
url: https://www.joelonsoftware.com/2006/10/12/book-review-beyond-java/
word_count: 514
---


Programmers under the age of thirty probably don’t realize why Aged Senile Programmers like me are so slow to adopt exciting new programming languages the day they come out, and why we roll our eyes at hip bandwagon ideas that sell books and consulting engagements (forgive me if I don’t seem excited enough about your new book, “Extreme UML Refactoring Patterns”).


It’s probably because we read [No Silver Bullet](http://www-inst.eecs.berkeley.edu/%7Emaratb/readings/NoSilverBullet.html), a stunningly important essay from way back in 1986, by Frederick P. Brooks (he of Mythical Man-Month) that has proven again and again to be spot-on.


Programming consists of overcoming two things: accidental difficulties, things which are difficult because you happen to be using inadequate programming tools, and things which are *actually difficult*, which no programming tool or language is going to solve. An example of an accidental difficulty is manual memory management, e.g. “malloc” and “free,” or the singleton classes people create in Java because they don’t have top level functions. An example of something which is actually difficult is dealing with the subtle interactions between different parts of a program, for example, figuring out all the implications of a new feature that you just added.


Improvements in programming languages can eliminate accidental difficulties, but after you’ve done that, you’re left with the actual complexity of software development, so the No Silver Bullet theory basically warns us to expect diminishing returns from new technologies. I’m not really doing justice to Brooks’ argument, so if you haven’t read [No Silver Bullet](http://www-inst.eecs.berkeley.edu/%7Emaratb/readings/NoSilverBullet.html) recently, I would highly recommend it.


There have been about five great advances, since the 1950s, in eliminating accidental difficulties in programming. These are, very broadly:

1. Assemblers
2. Algebraic languages (including Fortran)
3. Structured languages (Algol-60 and C)
4. Declarative languages (including SQL)
5. Memory-managed languages (including Lisp, VB, and Java)


So the question is, what’s number 6?


Bruce Tate’s book [Beyond Java](http://www.amazon.com/gp/redirect.html?ie=UTF8&location=http%3A%2F%2Fwww.amazon.com%2FBeyond-Java-Bruce-Tate%2Fdp%2F0596100949%2Fsr%3D8-1%2Fqid%3D1160670053%3Fie%3DUTF8&tag=joelonsoftware&linkCode=ur2&camp=1789&creative=9325) tries to address that, and does a good job of explaining why so many experienced Java programmers are getting fed up with that language and moving to Python and Ruby.


On page 56 and page 57, Steve Yegge, who didn’t actually write the book, but plays an important walk-on role, bangs out the list. These are actually the most important two pages of the book, because these are the things that Python and Ruby (and, underappreciated, JavaScript) actually solve.


Although Stevey lists lots of accidental difficulties in Java, when you read the book, you will notice a theme, which seems to be that it’s explicit typing, where the programmer is asked to declare the type of things, that leads to most of the problems. For example, the inability to express data in Java code is mostly just a side effect of the requirement that types be declared explicitly. Yes, there are other problems in Java, but this is The Big Hairy Problem right at the heart.


To a historian, it’s starting to look like type declarations are one of those accidental difficulties that good programming languages can eliminate. *Beyond Java* is a good summary of the arguments and worth reading.
