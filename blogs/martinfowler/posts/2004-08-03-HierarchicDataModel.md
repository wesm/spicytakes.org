---
title: "Hierarchic Data Model"
description: "A hierarchic data model organizes in the form of a hierarchy or 	tree structure. Early databases and programming data structures 	commonly used hierarchic models, but these fell out of favor. In the 	"
date: 2004-08-03T00:00:00
tags: ["database"]
url: https://martinfowler.com/bliki/HierarchicDataModel.html
slug: HierarchicDataModel
word_count: 122
---


A hierarchic data model organizes in the form of a hierarchy or
	tree structure. Early databases and programming data structures
	commonly used hierarchic models, but these fell out of favor. In the
	database world the [RelationalDataModel](https://martinfowler.com/bliki/RelationalDataModel.html) became dominant, while for
	most in-memory programming the [NetworkDataModel](https://martinfowler.com/bliki/NetworkDataModel.html) dominates. This was
	due to the fact that a hierarchy, while a simple organizational
	tool, breaks down as you get more complex data.


Yet the simplicity of a hierarchy is hard to deny, and hierarchic
	models keep showing value. The big return of hierarchic data models
	these days is with the rise of XML, which with its various
	associated technologies offers standard facilities for manipulating
	hierarchic data which are similar to what SQL offers for the
	[RelationalDataModel](https://martinfowler.com/bliki/RelationalDataModel.html).
