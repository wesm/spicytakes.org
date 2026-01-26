---
title: "MDS and DSL"
description: "What is the connection betweenModelDrivenSoftwareDevelopment(MDSD) andDomainSpecificLanguages(DSLs)?"
date: 2008-07-14T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/MDSDandDSL.html
slug: MDSDandDSL
word_count: 504
---


**What is the connection between
	[ModelDrivenSoftwareDevelopment](https://martinfowler.com/bliki/ModelDrivenSoftwareDevelopment.html) (MDSD) and
	[DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html) (DSLs)?**


It's pretty common to see the term âDSLâ crop up in the context
	of MDSD. Indeed some MDSD people seem to think that DSLs only exist
	within the MDSD world. I've been writing a lot on DSLs recently for
	my book, but so far I haven't really touched on the MDSD angle much
	Instead I've concentrated on DSLs role in more conventional
	programming. DSLs exist in both the textual language and MDSD worlds
	and play pretty much the same role for both.


In an MDSD context DSLs are again a language targeted at a
	specific kind of problem as opposed to general purpose languages
	such as the UML. As a result they can have the same kind of
	relationship: build a system in the general purpose modeling
	language and use DSLs for various specific aspects. Since MDSD
	hasn't caught on that much, however, you also see a different
	approach where modeling DSLs are used in the context of a
	traditional language environment. Here you might use several
	modeling DSLs that generate Java code to be combined in a Java
	project. In this case there's no general purpose MDSD model around -
	you use MDSD for each DSL relatively independently.


In order to use model-oriented DSLs you need a different,
	[ProjectionalEditing](https://martinfowler.com/bliki/ProjectionalEditing.html), 
	approach to tooling. This introduces quite a few pragmatic issues as
	the general support environment for such tools is less
	established. In order to define your own DSLs you need more
	specialized tooling - something I call a [Language
	Workbench](https://martinfowler.com/articles/languageWorkbench.html).


DSLs seem to have a proportionately higher emphasis in the MDSD
	world than they do in the mainstream programming world. Cynics think
	this is a result of the MDSD community desperately searching for a
	way to remain relevant, fans of MDSD regard it as a sign of MDSD's
	superior sophistication. I think this is mainly due to the fact that
	the MDSD community is smaller and has far less in the form of
	established practice.


A particularly visible sub-community of MDSD is centered around
	ModelDrivenArchitecture (MDA). I'm not much of a fan of MDA in
	particular, but am [particularly
	skeptical of MDA DSLs](https://martinfowler.com/articles/mdaLanguageWorkbench.html).


There is much that model-oriented DSLs share with textual DSLs. I
	put a lot of emphasis with textual DSLs in basing work around a
	[Semantic
	Model](https://martinfowler.com/dslwip/SemanticModel.html). MDSD, as its name indicates, is very much about driving a
	system from that kind of a model. A difference is that most MDSD
	people assume that you'll want to generate code from that model
	rather than executing the model directly.


As I write this, I'm not sure how much I'm going to cover 
	language workbenches in my book. Certainly I'll at least discuss the
	overall concept behind them, but the coverage may not be that
	deep. This will be partly due to the large amount of material I seem
	to be generating on textual DSLs and partly due to the fact that
	language workbenches are much newer and thus more volatile and less
	mature.
