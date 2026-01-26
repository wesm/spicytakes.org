---
title: "Transactionless"
description: "A couple of years ago I was talking to a couple of friends of 	mine who were doing some work at eBay. It's always interesting to 	hear about the techniques people use on high volume sites, but 	perhap"
date: 2007-03-18T00:00:00
tags: ["database", "application architecture"]
url: https://martinfowler.com/bliki/Transactionless.html
slug: Transactionless
word_count: 452
---


A couple of years ago I was talking to a couple of friends of
	mine who were doing some work at eBay. It's always interesting to
	hear about the techniques people use on high volume sites, but
	perhaps one of the most interesting tidbits was that eBay mostly
	hardly ever uses database transactions.


For most people, coming into a transactionless environment is
	quite a shock. Using transactions is a very accepted part of working
	with databases. A lot of people, including myself, see transactions
	as one of the key benefits that databases give you.


The rationale for not using transactions was that they harm
	performance at the sort of scale that eBay deals with. This effect
	is exacerbated by the fact that eBay heavily partitions its data
	into many, many physical databases. As a result using transactions
	would mean using distributed transactions, which is a common thing
	to be wary of.


This heavy partitioning, and the database's central role in
	performance issues, means that eBay doesn't use many other database
	facilities. Referential integrity and sorting are done in
	application code. There's hardly any triggers or stored procedures.


My immediate follow-up to the news of transactionless was to ask
	what the consequences were for the application programmer, in
	particular the overall feeling about transactionlessness. The reply
	was that it was odd at first, but ended up not being a big deal -
	much less of a problem than you might think. You have to pay
	attention to the order of your commits, getting the more important
	ones in first. At each commit you have to check that it succeeded
	and decide what to do if it fails.


This style of programming intrigued me, but since I was told
	about it quietly, I wouldn't talk about it more widely. I can now
	because [Dan Pritchett](http://www.addsimplicity.com/)
	gave a fascinating [talk](http://www.infoq.com/presentations/operational-manageability) at QCon this week
	about eBay's architecture, including this aspect. (He also [talked
  about this in an interview](http://www.infoq.com/interviews/dan-pritchett-ebay-architecture) and there's a useful [pdf info-deck](http://www.addsimplicity.com/downloads/eBaySDForum2006-11-29.pdf) .)


I'd like to see more about the details of programming without
transactions in this kind of manner. Apart from the fact that it's
always worth thinking about alternatives, it's also the case that
transactionlessness is more common than many people think. It's common
to have multi-step business processes with multiple resources that
either would need long-running distributed transactions, or resources
that have no support for transactions.


We shouldn't read too much into this. Nobody is arguing that we
should tear transactions out of our toolkit. I don't know enough
details about eBay to judge whether avoiding transactions is the right
approach even for them. But eBay's example suggests that living
without transactions is far less impossible than many people
think.
