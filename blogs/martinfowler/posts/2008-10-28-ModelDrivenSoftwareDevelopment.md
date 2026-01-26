---
title: "Model Driven Software Development"
description: "Oslo is a project at Microsoft, of which various things have been heard but with little details until this week's PDC conference. What we have known is that it has something to do withModelDrivenSoftw"
date: 2008-10-28T00:00:00
tags: ["programming environments", "domain specific language", "language workbench", "uml"]
url: https://martinfowler.com/bliki/ModelDrivenSoftwareDevelopment.html
slug: ModelDrivenSoftwareDevelopment
word_count: 356
---


Model Driven Software Development (MDSD) is a style of software
	development that considers itself as an alternative to the
	traditional style of programming. The approach centers itself on
	building models of a software system. These models are typically
	made manifest through diagrammatic design notations - the UML is one
	option. The idea is that you use these diagrams, to specify your
	system to a modeling tool and then you generate code in a
	conventional programming language.


The MDSD vision evolved from the development of graphical design
	notations and CASE tools. Proponents of these techniques saw
	graphical design notations as a way to raise the abstraction level
	above programming languages - thus improving development
	productivity. While these techniques and tools never caught on too
	far, the basic core ideas still live on and there is an ongoing
	community of people still developing them.


Although I've been involved, to some extent, in MDSD for most of
	my career, I'm rather skeptical of its future. Most fans of MDSD
	base their enthusiasm on the basis that models are *ipso facto* a
	higher level abstraction than programming languages. I don't agree
	with that argument - sometimes graphical notations can be a better
	abstraction, but not always - it depends on the specific
	cases. Furthermore To use MDSD you need tools that support
	[ProjectionalEditing](https://martinfowler.com/bliki/ProjectionalEditing.html), and these tools currently introduce
	a number of pragmatic issues in tooling - of which source control is
	the canonical example.


MDSD is surrounded by a terminological mess. One particular vision
	of MDSD is [ModelDrivenArchitecture](https://martinfowler.com/bliki/ModelDrivenArchitecture.html) (MDA) which is an OMG
	initiative based on the UML. Many people in the MDSD community,
	however, don't think that MDA or UML is the right vision for
	MDSD. For a long time I would hear people talking about Model Driven
	Development (MDD) as the general concept and MDA as the OMG's
	specific vision. However the OMG has trademarks on several âModel
	Driven *â and âModel Based *â phrases - including MDD. As a
	consequence people have to be careful about what model driven phrase
	they use. I'm using MDSD as that is the title of a [useful book](https://www.amazon.com/gp/product/0470025700/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470025700&linkCode=as2&tag=martinfowlerc-20) on the topic.
