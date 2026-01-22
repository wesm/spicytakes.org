---
title: "The tricky thing about disparate impact"
date: 2015-10-02
url: https://mathbabe.org/2015/10/02/the-tricky-thing-about-disparate-impact/
word_count: 817
---


Today I’m fascinated by the story described in [this three-part American Banker series](http://www.americanbanker.com/news/law-regulation/cfpb-overestimates-potential-discrimination-documents-show-1076742-1.html) on the Consumer Financial Protection Bureau’s (CFPB’s) use of disparate impact, written by Rachel Witkowski. Disparate impact, according to the article, is a legal theory that says lenders can be penalized if they have a neutral policy that creates an adverse impact against a protected class of borrowers, regardless of intent.


Witkowski reports on the CFPB trying to understand and punish auto lenders for their process for figuring out fees and interest rates on auto loans. In general, the auto dealers, who work in partnerships with auto lenders, have discretion to add on some interest rate and pocket the difference. They seem to be pocketing fatter differences for certain populations, specifically black car buyers.


The problem is, it’s hard to measure exactly how much fatter and who is getting screwed, by how much. And in the world of law and punishment, it’s not enough to prove that there’s been a disparate impact – you have to actually make restitutions to the victims. So for example, the CFPB is in discussions with Ally Financial for exactly this problem, and the question is how much money to they give to which borrowers as a refund.


The first reason this is hard to get right is that auto dealers and lenders don’t actually collect race information, in contrast to mortgage lending, where it’s a requirement of the lending process, specifically to ward against redlining. So the CFPB, in its investigation, has to rely on proxy data like zip codes and names to guess the race of a given borrower. In fact [their methodology is described in this white paper](http://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf), but unsurprisingly the auto lenders under scrutiny complain it is not sufficiently transparent.


What that translates into is the possibility that some white car buyers people will get refunded accidentally and some black car buyers won’t, even if there were shenanigans going on with their car loan. From my perspective as a data person, this tells me that, as long as we have problems like this, we should probably require race to be recorded in a car loan.


That’s not the only problem, though. The thing about these modern cases of measuring disparate impact is that it’s a model, and models are extremely squishy things. Two people asked to build a disparate impact model on the same data will likely come up with different answers, because all sorts of decisions have to be made on the way. From the article:


> Each financial regulator has its own method for determining disparities and harm in fair-lending cases, and each of those cases can differ depending on the business model of the bank and what variables the regulators will consider. The Federal Reserve, for instance, generally adds controls, such as geography, to the statistical model if the bank’s business model indicates that certain pricing criteria can influence the price or markup, according to a 2013 Fed presentation.


Given this uncertainty, plus the uncertainty of the race of the borrowers, you end up firmly in a land of statistics, where each borrower is assigned a probability of being minority and a probability of having been screwed. Then the question becomes, do we err on the side of under- or over-refunding these borrowers? The lenders, who are paying for this all, tend to lean on the side of not giving any money away at all unless we’re sure.


In this particular story, [specifically in part 3](http://www.americanbanker.com/news/law-regulation/cfpbs-outside-expert-on-disparate-impact-also-advises-banks-1076979-1.html), there’s even an expert consultant named Dr. Bernard Siskin who happens to work for both sides – the banks and the CFPB. The excuse for that questionable arrangement is that there aren’t enough statisticians who can do this work (my hand is raised!), but the end result is that Siskin seems to help the banks complain about exactly this issue: which version of the disparate impact model is to be used, and what kind of attributes will be controlled for, so that they can each get the least expensive settlement.


Here’s my theory. This is a big new field in statistics and data science, and this is just the tip of the iceberg. We will be seeing a large amount of work being done and tools being made which aim to measure and audit processes and algorithms, whether they are auto loans that discriminate against minority borrowers or car computers that bypass emissions tests. And we will have to develop standards by which we measure a company’s work. The standards won’t be perfect, mind you, and people will end up getting away with certain things, but at leas we won’t have the gaming that’s obviously going on now, because there will be a set way, hopefully reasonably thought out, to measure discrimination, or lying, or cheating, or what have you.


That’s the field I want to go into. Building models that call bullshit on other models.
