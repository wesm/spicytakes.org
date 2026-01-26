---
title: "Unwanted Modeling Language"
description: "The UML means different things to different people, which is why 	I find the notion of people using a differentUmlModeuseful. Most people I talk to are interested inUmlAsSketchand this group isn't ver"
date: 2003-11-03T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/UnwantedModelingLanguage.html
slug: UnwantedModelingLanguage
word_count: 335
---


The UML means different things to different people, which is why
	I find the notion of people using a different [UmlMode](https://martinfowler.com/bliki/UmlMode.html)
	useful. Most people I talk to are interested in
	[UmlAsSketch](https://martinfowler.com/bliki/UmlAsSketch.html) and this group isn't very impressed with UML
	2.


The reason for this unhappiness is that the drive for UML 2 was
	to formalize and complete the UML to support MDA; primarily for
	[UmlAsProgrammingLanguage](https://martinfowler.com/bliki/UmlAsProgrammingLanguage.html) (and secondarily for
	[UmlAsBlueprint](https://martinfowler.com/bliki/UmlAsBlueprint.html)). As a result sketchers were pretty much
	ignored. This was largely their own fault as sketchers aren't
	interested enough in the UML to take an active role in the UML committees.


All this didn't surprise me. Something new that I discovered in
	the last couple of weeks (that included visiting UML 2003 and
	OOPSLA) was that disdain for UML is pretty rampant amongst the
	[UmlAsProgrammingLanguage](https://martinfowler.com/bliki/UmlAsProgrammingLanguage.html) community too. After my talk at
	UML 2003 (broadly an appeal to not ignore the need of sketchers)
	several people came up to me to point out that people active in the
	MDA weren't particularly interested in the UML either.


Even on the MDA panel at OOPSLA, the pro-MDA speakers based their
	assumptions on the fact that they would be using a simplified subset
	of UML, and emphasized that you should not judge MDA on the
	UML. (Which didn't save them from a blistering attack by [Dave âOTIâ Thomas](http://c2.com/cgi/wiki?DaveThomas).)


I wonder where this will leave the UML in the future. I hear more
	mutterings from sketchers about the growing irrelevance of UML
	standards. In the MDA community it seems that we will see a rise of
	tools all using different subsets of the UML standards, probably
	extended subsets using profiles. What will this mean for the UML as
	an interchange mechanism between MDA tools? Some people are saying
	that the UML will not be the interchange mechanism - that the OMG
	MOF will play that role. This is all very well, but will users of
	MDA tools get portability in practice, or will each tool turn into
	its own proprietary language?
