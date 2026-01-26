---
title: "Network Data Model"
description: "The relational data model is best known to most people through 	relational data bases, and through the SQL language. Colloquially, 	we think of the database as a set of tables, each row of which 	cont"
date: 2004-08-03T00:00:00
tags: ["database"]
url: https://martinfowler.com/bliki/NetworkDataModel.html
slug: NetworkDataModel
word_count: 142
---


The network data model structures data as record types, with
		pointer links to allow to navigate between one record and another.
		So to query a network data model you begin at one record and move
		around pointer references.


Network model data bases fell out of favor a while ago to the
		[RelationalDataModel](https://martinfowler.com/bliki/RelationalDataModel.html), but this data model is by no means
		dead. Indeed it's the primary model for in-memory data. Almost
		every mainstream language has facilities for defining record types
		and pointers.


You can think of object models as a form of network data model,
		since they also have data structures linked by pointers. The vital
		difference is that objects incorporate data and behavior, as a
		result I think they feel much different in practice. However many
		object models ([AnemicDomainModel](https://martinfowler.com/bliki/AnemicDomainModel.html)) are really only
		network data models since they don't have any significant
		behavior.
