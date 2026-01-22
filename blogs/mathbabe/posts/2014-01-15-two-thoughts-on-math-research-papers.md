---
title: "Two thoughts on math research papers"
date: 2014-01-15
url: https://mathbabe.org/2014/01/15/two-thoughts-on-math-research-papers/
word_count: 551
---


Today I’d like to mention two ideas I’ve been having recently on how to make being a research mathematician (even) more fun.


**1) Mathematicians should consider holding public discussions about papers**


First, math nerds, did you know that in statistics they have formal discussions about papers? It’s been a long-standing tradition by the [Royal Statistical Society](http://www.rss.org.uk/site/cms/contentChapterView.asp?chapter=1), whose motto is “Advancing the science and application of statistics, and promoting use and awareness for public benefit,” to choose papers [by some criterion](http://www.rss.org.uk/uploadedfiles/userfiles/files/Discussion_Paper_Criteria_2013.pdf) and then [hold regular public discussions](http://www.rss.org.uk/site/cms/contentCategoryView.asp?category=88) about those papers by a few experts who are not the author, about the paper. Then the author responds to their points and the whole conversation is published for posterity.


I think this is a cool idea for math papers too. One thing that kind of depressed me about math is how rarely you’d find people reading the same papers unless you specifically got a group of people together to do so, which was a lot of work. This way the work is done mostly by other people and more importantly the payoff is much better for them since everyone gets a view into the discussion.


Note I’m sidestepping who would organize this whole thing, and how the papers would be chosen exactly, but I’d expect it would improve the overall feeling that I had of being isolated in a tiny math community, especially if the conversations were meant to be penetrable.


**2) There should be a good clustering method for papers around topics**


This second idea may already be happening, but I’m going to say it anyway, and it could easily be a thesis for someone in CS.


Namely, the idea of using [NLP](http://en.wikipedia.org/wiki/Natural_language_processing) and other such techniques to cluster math papers by topic. Right now the most obvious way to find a “nearby” paper is to look at the graph of papers by direct reference, but you’re probably missing out on lots of stuff that way. I think a different and possibly more interesting way would be to use the text in the title, abstract, and introduction to find papers with similar subjects.


This might be especially useful when you want to know the answer to a question like, “has anyone proved that such-and-such?” and you can do a text search for the statement of that theorem.


The good news here is that mathematicians are in love with terminology, and give weird names to things that make NLP techniques very happy. My favorite recent example which I hear Johan muttering under his breath from time to time is *[Flabby Sheaves](http://www.encyclopediaofmath.org/index.php/Flabby_sheaf)*. There’s no way that’s not a distinctive phrase.


The bad news is that such techniques won’t help at all in finding different fields who have come across the same idea but have different names for the relevant objects. But that’s OK, because it means there’s still lots of work for mathematicians.


By the way, back to the question of whether this has already been done. My buddy [Max Lieblich](https://www.math.washington.edu/~lieblich/) has a website called [MarXiv](http://www.marxiv.org/?query=&page=0&type=home) which is a wrapper over the math [ArXiv](http://arxiv.org/) and has a “similar” button. I have no idea what that button actually does though. In any case I totally dig the design of the similar button, and what I propose is just to have something like that work with NLP.
