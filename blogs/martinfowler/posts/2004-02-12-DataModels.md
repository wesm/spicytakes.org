---
title: "Data Models"
description: "One of my early favorite books wasTsichritzis  			and Lochovsky'sbook on Data Models. The book discussed 		different models for thinking about data, in particular the three 		models most discussed at "
date: 2004-02-12T00:00:00
tags: ["database"]
url: https://martinfowler.com/bliki/DataModels.html
slug: DataModels
word_count: 563
---


One of my early favorite books was [Tsichritzis 
			and Lochovsky's](http://www.amazon.com/exec/obidos/tg/detail/-/0131964283) book on Data Models. The book discussed
		different models for thinking about data, in particular the three
		models most discussed at the time: [RelationalDataModel](https://martinfowler.com/bliki/RelationalDataModel.html),
		[HierarchicDataModel](https://martinfowler.com/bliki/HierarchicDataModel.html) and [NetworkDataModel](https://martinfowler.com/bliki/NetworkDataModel.html).


These days I don't see people talking about the pros and cons of
		different data models very much. The people who talk about data
		models tend to be database people, and most people seem to think
		that that contest was long since won by the
		relational model.


However I don't think that was ever really true, and things are
		getting more and more interesting.


There's no doubt that the relational model is
		dominant in the database world, almost every business application
		I run into these days uses a SQL database, which is close enough
		to relational for 99% of the population. However if you look at
		in-memory data structures you see a different world. Here the
		network model reigns supreme. Indeed people often go to great
		efforts to turn a relational model on disk to a
		network model in memory (this, I think is one of the
		reasons why the [AnemicDomainModel](https://martinfowler.com/bliki/AnemicDomainModel.html) is so popular.)


I find this interesting. Time and time again I ask people why
		they bother to go through all the fuss of turning relations into
		records. The answer I get back pretty much always boils down to
		the same thing - most developers find the network model  easier
		to deal with than the relational model. Certainly this is not
		always the case, but I do think there's a majority of those that
		prefer records.


This may have something to do with the fact that while SQL works
		well for databases, we don't have the equivalent for in-memory
		processing. Thinking relationally is one of the things I find
		interesting about ADO.NET, yet again I see many people who don't
		want to work with datasets in a relational style.


The other thing that's steadily challenging the current data
		model picture is the rise of XML. XML based technologies like
		XPath and XQuery provide a standard way of accessing hierarchic
		data structures. In many ways the fact the XML provides a standard
		textual serialization of that data is just a bonus to having this
		standard way of querying and manipulating hierarchic data.


A fundamental technological shift will I think cause further data
		model churn. As memory sizes grow as fast as prices drop, we are
		increasingly reaching the point where most databases can be kept
		entirely in memory. Couple this with a mechanism for durable
		changes, and you have a whole different kind of database with
		fundamentally different assumptions about what it takes to
		perform. (See [Prevayler](http://www.prevayler.org) as
		an example of this kind of thinking. I have no idea how valid
		their performance numbers are, but they could be a couple of orders
		of magnitude off and still be impressive.)


So maybe its time again to dust off those assumptions about which
		data models make sense, and get start thinking about some of the
		basics of these models. My sense is that different kinds of data
		work well with different kinds of models. The
		relational model is perfect for tabular data, but
		suck really badly if you want to store [The
			Tempest](http://www.gutenberg.net/browse/BIBREC/BR2235.HTM). So it makes sense to be aware of different data
		models, the technologies that use them, and which ones suit what
		kinds of data.
