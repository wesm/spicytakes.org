---
title: "E-discovery and the public interest"
date: 2013-05-08
url: https://mathbabe.org/2013/05/08/e-discovery-and-the-public-interest/
word_count: 386
---


Today I want to bring up a few observations and concerns I have about the emergence of a new field in machine learning called e-discovery. It’s the algorithmic version of discovery, so I’ll start there.


Discovery is part of the process in a lawsuit where relevant documents are selected, pored over, and then handed to the other side. Nowadays, of course, there are more and more documents, almost all electronic, typically including lots of e-mails.


If you’re talking about a big lawsuit, there could be literally millions of documents to wade through, and that takes a lot of time for humans to do, and it can be incredibly expensive and time-consuming. Enter the algorithm.


With advances in [Natural Language Processing](http://en.wikipedia.org/wiki/Natural_language_processing) (NLP), a machine algorithm can sort emails or documents by topic (after getting the documents into machine-readable form, cleaning, and [deduping](http://en.wikipedia.org/wiki/Data_deduplication)) and can in general do a pretty good job of figuring out whether a given email is “relevant” to the case.


And this is already happening – the [Wall Street Journal recently reported](http://online.wsj.com/article/SB10001424127887324582004578460860324234712.html?mod=WSJ_hps_MIDDLE_Video_Top) that the Justice Department allowed e-discovery for a case involving the merger of two beer companies. From the article:


> With the blessing of the Justice Department’s antitrust division, the lawyers loaded the documents into a program and manually reviewed a batch to train the software to recognize relevant documents. The manual review was repeated until the Justice Department and Constellation were satisfied that the program could accurately predict relevance in the rest of the documents. Lawyers for Constellation and Crown Imports used software developed by kCura Corp., which lists the Justice Department as a client.
> In the end, Constellation and Crown Imports turned over hundreds of thousands of documents to antitrust investigators.


Here are some of my questions/ concerns:

- These algorithms are typically not open source – companies like [kCura](http://kcura.com/relativity/) make good money doing these jobs.
- That means that they could be wrong, possibly in subtle ways.
- Or maybe not so subtle ways: maybe they’ve been trained to find documents that are both “relevant” and “positive” for a given side.
- In any case, the laws of this country will increasingly depend on a black box algorithm that is no accessible to the average citizen.
- Is that in the public’s interest?
- Is that even constitutional?
