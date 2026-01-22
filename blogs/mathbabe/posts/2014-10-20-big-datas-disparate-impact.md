---
title: "Big Data’s Disparate Impact"
date: 2014-10-20
url: https://mathbabe.org/2014/10/20/big-datas-disparate-impact/
word_count: 545
---


Take a look at [this paper](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2477899) by [Solon Barocas](http://solon.barocas.org/) and [Andrew D. Selbst](https://twitter.com/aselbst) entitled [*Big Data’s Disparate Impact*](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2477899).


It deals with the question of whether current anti-discrimination law is equipped to handle the kind of unintentional discrimination and digital redlining we see emerging in some “big data” models (and that we suspect are hidden in a bunch more). See for example [this post](https://mathbabe.org/2014/05/02/no-sandy-pentland-lets-not-optimize-the-status-quo/) for more on this concept.


The short answer is no, our laws are not equipped.


Here’s the abstract:


> This article addresses the potential for disparate impact in the data mining processes that are taking over modern-day business. Scholars and policymakers had, until recently, focused almost exclusively on data mining’s capacity to hide intentional discrimination, hoping to convince regulators to develop the tools to unmask such discrimination. Recently there has been a noted shift in the policy discussions, where some have begun to recognize that unintentional discrimination is a hidden danger that might be even more worrisome. So far, the recognition of the possibility of unintentional discrimination lacks technical and theoretical foundation, making policy recommendations difficult, where they are not simply misdirected. This article provides the necessary foundation about how data mining can give rise to discrimination and how data mining interacts with anti-discrimination law.
> The article carefully steps through the technical process of data mining and points to different places within the process where a disproportionately adverse impact on protected classes may result from innocent choices on the part of the data miner. From there, the article analyzes these disproportionate impacts under Title VII. The Article concludes both that Title VII is largely ill equipped to address the discrimination that results from data mining. Worse, due to problems in the internal logic of data mining as well as political and constitutional constraints, there appears to be no easy way to reform Title VII to fix these inadequacies. The article focuses on Title VII because it is the most well developed anti-discrimination doctrine, but the conclusions apply more broadly because they are based on the general approach to anti-discrimination within American law.


I really appreciate this paper, because it’s an area I know almost nothing about: discrimination law and what are the standards for evidence of discrimination.


Sadly, what this paper explains to me is how very far we are away from anything resembling what we need to actually address the problems. For example, even in this paper, where the writers are well aware that training on historical data can unintentionally codify discriminatory treatment, they still seem to assume that the people who build and deploy models will “notice” this treatment. From my experience working in advertising, that’s not actually what happens. We don’t measure the effects of our models on our users. We only see whether we have gained an edge in terms of profit, which is very different.


Essentially, as modelers, we don’t humanize the people on the other side of the transaction, which prevents us from worrying about discrimination or even being aware of it as an issue. It’s so far from “intentional” that it’s almost a ridiculous accusation to make. Even so, it may well be a real problem and I don’t know how we as a society can deal with it unless we update our laws.
