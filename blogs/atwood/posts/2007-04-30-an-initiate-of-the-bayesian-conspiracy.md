---
title: "An Initiate of the Bayesian Conspiracy"
date: 2007-04-30
url: https://blog.codinghorror.com/an-initiate-of-the-bayesian-conspiracy/
slug: an-initiate-of-the-bayesian-conspiracy
word_count: 767
---

[An Intuitive Explanation of Bayesian Reasoning](https://web.archive.org/web/20070613184853/http://yudkowsky.net/bayes/bayes.html) is an extraordinary piece on Bayes’ theorem that starts with this simple puzzle:


> 1% of women at age forty who participate in routine screening have breast cancer. 80% of women with breast cancer will get positive mammographies. 9.6% of women without breast cancer will also get positive mammographies. A woman in this age group had a positive mammography in a routine screening. What is the probability that she actually has breast cancer?


This simple puzzle is not all that simple in practice. Only 15% of doctors, when presented with this situation, come up with the correct answer.


**Can you come up with the correct answer – *without* resorting to Google, the comments to this post, or reading the answer provided in the article?**


If so, congratulations. You’re a natural initiate of the Bayesian Conspiracy. For the rest of us, Bayes’ Theorem is a bit more difficult to grasp:


> While there are a few existing [online explanations of Bayes’ Theorem](https://web.archive.org/web/20070427100839/http://www.cs.ubc.ca/~murphyk/Bayes/bayesrule.html), my experience with trying to introduce people to Bayesian reasoning is that the existing online explanations are too abstract. Bayesian reasoning is very counterintuitive. People do not employ Bayesian reasoning intuitively, find it very difficult to learn Bayesian reasoning when tutored, and rapidly forget Bayesian methods once the tutoring is over. This holds equally true for novice students and highly trained professionals in a field. Bayesian reasoning is apparently one of those things which, like [quantum mechanics](http://en.wikipedia.org/wiki/Quantum_mechanics) or the [Wason Selection Test](http://en.wikipedia.org/wiki/Wason_selection_task), is inherently difficult for humans to grasp with our built-in mental faculties.


In computer science, **it’s easy to demonstrate the immense power of Bayes’ theorem: it’s the basis for almost all spam filters in use today**. Bayesian email filtering was first publicized by Paul Graham’s [A Plan for Spam](https://blog.codinghorror.com/some-plans-for-spam/) in mid-2002. Most programmers know about Bayesian filtering now; it’s the primary weapon in any modern Spam fighting toolkit.


What you may not know, however, is that there’s something even more effective than Bayesian spam filtering. It’s eloquently described in William Yerazunis’ presentation [The Spam Filtering Plateau at 99.9% Accuracy and How to Get Past It](https://web.archive.org/web/20070505120219/http://crm114.sourceforge.net/docs/Plateau99/img0.html) (also available in [pdf paper form](https://web.archive.org/web/20080829180924/http://www.merl.com/reports/docs/TR2004-091.pdf)). And it’s been implemented as the [CRM114 Discriminator](https://web.archive.org/web/20070503232805/http://crm114.sourceforge.net/wiki/doku.php) for years. That technique is [Markovian spam filtering](https://blog.codinghorror.com/the-nigerian-spammer-anthem/):

kg-card-begin: html

> How to change a Bayesian spam filter to a Markovian spam filter:
> Change the feature generator from single words to spanning multiple words
> Change the weighting so that longer features have more weight (i.e., longer features generate local probabilities closer to 0.0 and 1.0)
> The 2^2n weighting means that the weights are 1, 4, 16, 64, 256, ... for span lengths of 1, 2, 3, 4, 5... words

kg-card-end: html

In other words, where Bayesian filters examine the relationship between individual words, Markovian filters expand the scope to examine the relationship between words and phrases. It’s a tweak, but a significant one that amplifies the accuracy of the already uncannily accurate Bayes’ theorem.


But the true power of Bayes’ theorem extends far beyond merely discriminating between spam and non-spam. As the CR114 documentation notes, you can use these powerful statistical models to discriminate between... well, just about anything:


> Spam is the big target with CRM114, but it’s not a specialized Email-only tool. CRM114 has been used to sort web pages, resumes, blog entries, log files, and lots of other things. Accuracy can be as high as 99.9 %. In other words, CRM114 learns, and it learns fast.


Now perhaps you can understand why some people are so excited about Bayes’ theorem.


> Maybe you see Bayes’ theorem, and you understand the theorem, and you can use the theorem, but you can’t understand why your friends and/or research colleagues seem to think it’s the secret of the universe. Maybe your friends are all wearing Bayes’ theorem T-shirts, and you’re feeling left out. Maybe you’re a girl looking for a boyfriend, but the boy you’re interested in refuses to date anyone who “isn’t Bayesian.” What matters is that Bayes is cool, and if you don’t know Bayes, you aren’t cool.
> Why does a mathematical concept generate this strange enthusiasm in its students? What is the so-called Bayesian Revolution now sweeping through the sciences, which claims to subsume even the experimental method itself as a special case? What is the secret that the adherents of Bayes know? What is the light that they have seen?


It’s not intuitive for most people, but look a little more closely, and I think you, too, will become **an initiate of the Bayesian conspiracy**.

[statistics](https://blog.codinghorror.com/tag/statistics/)
[probability](https://blog.codinghorror.com/tag/probability/)
[bayes' theorem](https://blog.codinghorror.com/tag/bayes-theorem/)
[medical](https://blog.codinghorror.com/tag/medical/)
[mathematics](https://blog.codinghorror.com/tag/mathematics/)
