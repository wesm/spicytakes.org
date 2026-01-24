---
title: "Separating Programming Sheep from Non-Programming Goats"
date: 2006-07-14
url: https://blog.codinghorror.com/separating-programming-sheep-from-non-programming-goats/
slug: separating-programming-sheep-from-non-programming-goats
word_count: 1146
---

⚠ Please note, this paper was ultimately [retracted by its author](http://www.eis.mdx.ac.uk/staffpages/r_bornat/papers/camel_hump_retraction.pdf) (pdf) in 2014:


> In 2006 I wrote an intemperate description of the results of an experiment carried out by Saeed Dehnadi. Many of the extravagant claims I made were insupportable, and I retract them. I continue to believe, however, that Dehnadi had uncovered the first evidence of an important phenomenon in programming learners. Later research seems to confirm that belief.


A bunch of people have linked to this [academic paper](https://web.archive.org/web/20090401003425/http://www.cs.mdx.ac.uk/research/PhDArea/saeed/), which proposes **a way to separate programming sheep from non-programming goats in computer science classes** – long before the students have ever touched a program or a programming language:


> All teachers of programming find that their results display a ‘double hump.’ **It is as if there are two populations: those who can [program], and those who cannot [program], each with its own independent bell curve.** Almost all research into programming teaching and learning have concentrated on teaching: change the language, change the application area, use an IDE and work on motivation. None of it works, and the double hump persists. We have a test which picks out the population that can program, before the course begins. We can pick apart the double hump. You probably don’t believe this, but you will after you hear the talk. We don’t know exactly how/why it works, but we have some good theories.


I wasn’t aware that the dichotomy between programmers and non-programmers was so pronounced at this early stage. Dan Bricklin touched on this topic in his essay, [Why Johnny Can’t Program](http://www.bricklin.com/wontprogram.htm). But evidently it’s common knowledge amongst those who teach computer science:


> Despite the enormous changes which have taken place since electronic computing was invented in the 1950s, some things remain stubbornly the same. **In particular, most people can’t learn to program: between 30% and 60% of every university computer science department’s intake fail the first programming course.** Experienced teachers are weary but never oblivious of this fact; bright eyed beginners who believe that the old ones must have been doing it wrong learn the truth from bitter experience; and so it has been for almost two generations, ever since the subject began in the 1960s.


You may think the test they’re proposing to determine programming aptitude is complex, but it’s not. Here’s question one, verbatim:

kg-card-begin: html

```
Read the following statements and tick the box next to the correct answer.
int a = 10;
int b = 20;
a = b;
The new values of a and b are:
[ ] a = 20  b = 0
[ ] a = 20  b = 20
[ ] a = 0   b = 10
[ ] a = 10  b = 10
[ ] a = 30  b = 20
[ ] a = 30  b = 0
[ ] a = 10  b = 30
[ ] a = 0   b = 30
[ ] a = 10  b = 20
[ ] a = 20  b = 10
```

kg-card-end: html

This test seems trivial to professional programmers, but remember, it’s intended for students who have never looked at a line of code in their lives. The other 12 questions are all variations on the same assignment theme.

The authors of the paper posit that the primary hurdles in computer science are...

- assignment and sequence
- recursion / iteration
- concurrency*


... in that order. Thus, we start by testing the very first hurdle novice programmers will encounter: assignment. The test results divided the students cleanly into three groups:

1. 44% of students formed a consistent mental model of how assignment works (even if incorrect!)
2. 39% students never formed a consistent model of how assignment works.
3. 8% of students didn’t give a damn and left the answers blank.


The test was administered twice; once at the beginning, before any instruction at all, and again after three weeks of class. The striking thing is that there was virtually no movement at all between the groups from the first to second test. Either you had a consistent model in your mind immediately upon first exposure to assignment, the first hurdle in programming – *or else you never developed one!*


The authors found an extremely high level of correlation between success at programming and forming a consistent mental model:


> Clearly, Dehnahdi’s test is not a perfect divider of programming sheep from non-programming goats. **Nevertheless, if it were used as an admissions barrier, and only those who scored consistently were admitted, the pass/fail statistics would be transformed. In the total population 32 out of 61 (52%) failed; in the first-test consistent group only 6 out of 27 (22%).** We believe that we can claim that we have a predictive test which can be taken prior to the course to determine, with a very high degree of accuracy, which students will be successful. This is, so far as we are aware, the first test to be able to claim any degree of predictive success.


I highly recommend reading through [the draft paper](https://web.archive.org/web/20070318023700/http://www.cs.mdx.ac.uk/research/PhDArea/saeed/paper1.pdf) (pdf), which was remarkably entertaining for what I thought was going to be a dry, academic paper. Instead, it reads like a blog entry. It’s filled with interesting insights like this one:


> It has taken us some time to dare to believe in our own results. It now seems to us, although we are aware that at this point we do not have sufficient data, and so it must remain a speculation, that what distinguishes the three groups in the first test is their different attitudes to meaninglessness.
> Formal logical proofs, and therefore programs – formal logical proofs that particular computations are possible, expressed in a formal system called a programming language – are utterly meaningless. **To write a computer program you have to come to terms with this, to accept that whatever you might want the program to mean, the machine will blindly follow its meaningless rules and come to some meaningless conclusion.** In the test the consistent group showed a pre-acceptance of this fact: they are capable of seeing mathematical calculation problems in terms of rules, and can follow those rules wheresoever they may lead. The inconsistent group, on the other hand, looks for meaning where it is not. The blank group knows that it is looking at meaninglessness, and refuses to deal with it.


Everyone should know how to use a computer, but [not everyone](https://blog.codinghorror.com/please-dont-learn-to-code/) needs to be a programmer. It’s still a little disturbing that **the act of programming seems literally unteachable to a sizable subset of incoming computer science students**. Evidently not everyone is as fascinated by meaningless rules and meaningless conclusions as we are; I can’t imagine why not.


*Which I hope to master sometime [between now and my death](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/).

[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[computer science education](https://blog.codinghorror.com/tag/computer-science-education/)
[programming skills](https://blog.codinghorror.com/tag/programming-skills/)
[academic research](https://blog.codinghorror.com/tag/academic-research/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
