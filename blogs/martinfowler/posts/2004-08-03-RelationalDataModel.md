---
title: "Relational Data Model"
description: "The relational data model is best known to most people through 	relational data bases, and through the SQL language. Colloquially, 	we think of the database as a set of tables, each row of which 	cont"
date: 2004-08-03T00:00:00
tags: ["database"]
url: https://martinfowler.com/bliki/RelationalDataModel.html
slug: RelationalDataModel
word_count: 199
---


The relational data model is best known to most people through
	relational data bases, and through the SQL language. Colloquially,
	we think of the database as a set of tables, each row of which
	contains data. We can manipulate these tables in various ways to do
	queries, each query results in another table. In contrast to
	[NetworkDataModel](https://martinfowler.com/bliki/NetworkDataModel.html), there are no explicit pointers between tables,
	links are made by join tables on common values (although the use of
	surrogate keys means you have pointers in practice.)


The relational model has become the primary model for databases
	these days, primarily due to the common standard of SQL. It's worth
	pointing out that many relational fans consider SQL to be be a weak
	form of the relational model.


You can think of relational models as network models with foreign
	key references as pointers. However I think this misses a vital
	point. The record types in network data models are seen as different
	things, but all relations in a relational model are seen as
	essentially the same thing. Expressions in SQL operate on relations
	and produce relations - which gives the relational model a quality
	of composability that network models typically don't have.
