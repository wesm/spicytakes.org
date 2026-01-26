---
title: "Projectional Editing"
description: "Source based programing environments hold the definition of a system in a set of source files which act as both an editable and storage representation of the system definition. These sources are then "
date: 2008-01-22T00:00:00
tags: ["programming environments"]
url: https://martinfowler.com/bliki/ProjectionalEditing.html
slug: ProjectionalEditing
word_count: 682
---


An alternative to [SourceEditing](https://martinfowler.com/bliki/SourceEditing.html) is the idea that the
	core definition of a system should be held in a model and edited
	through projections.


To talk about this style of environment I find it handy to
	think in terms of multiple representations of the system:

- editable representation: what you edit in order to change the
system.
- storage representation: the persistent record of the system
definition.
- executable representation: what is executed to make the system run
- the executable.
- abstract representation: used to manipulate and reason about
system definition.
- visualization representation: a non-editable view of the system
definition.


Source code combines the editable and storage
  representations. It executes the source by
  transforming the source into an executable representation either in
  one observable step (interpretation) or multiple steps via a
  compiler. In order to do this it usually transforms the source into
  an abstract representation as an intermediate step, but this
  abstract representation is transitory and only around during
  compilation. The source is seen as the core definition of the
  system.


![](https://martinfowler.com/articles/compile.gif)


With projectional editing the abstract representation is the
  is core definition of the system. A tool manipulates the abstract
  representation and projects multiple editable representations for
  the programmer to change the definition of the system. The tool
  persists the abstract representation in a storage representation,
  but this is entirely separated from any of the editable
  representations that it projects. The relationship to the executable
  representation is pretty much the same - the executable is produced
  through a series of transformations from the abstract
  representation.


![](https://martinfowler.com/articles/workbench.gif)


An important difference between source and projectional editing
	environment is the split between persistent storage and
	editing. Projectional editing systems can choose any persistence
	mechanism that they choose, while source systems need to have some
	universal storage mechanism - which is why they are almost always
	text files.


The abstract representation may be edited through multiple
	projections, each projection can show a limited amount of the total
	information which isn't tied to the actual structure of the abstract
	representation. Projectional editing thus usually displays a wider range
	of editing environments - including graphical and tabular structures
	- rather than just a textual form.


Sophisticated source based IDEs also show multiple projections -
	for instance a side pane showing a list of methods for a class with
	graphical annotations to indicate their
	[AccessModifiers](https://martinfowler.com/bliki/AccessModifier.html). However these projections are usually
	very much secondary to a source editor, and often the projections
	can't be edited directly - you have to change the source and see the
	projection update.


Such [PostIntelliJ](https://martinfowler.com/bliki/PostIntelliJ.html) IDEs do this by creating an abstract
	representation when they load the source files (which is why they
	can take a while to start up). They also use the abstract
	representation to do perform lots of other code-assistance features
	such as contextual code completion and refactoring.


A significant pragmatic problem with projectional editing is
	the fact that there is no generally accepted  format for the
	storage representation. The fact that programmer-readable text is
	the universal choice for source files means that a whole slew of
	tools can be built to process them: editors, source-code control,
	difference visualizers etc. Projectional systems have to do all this
	themselves, which is often why these things are often lacking. In
	particular many projectional environments suffer greatly because
	they don't have a decent configuration control system, which makes
	it much harder for multiple people to collaborate on the same system
	definition. This is a big contrast to source environments that
	have a plethora of source code control systems to do this task.


Projectional based systems are closely connected with [ModelDrivenSoftwareDevelopment](https://martinfowler.com/bliki/ModelDrivenSoftwareDevelopment.html), although I don't think the two are entirely
	synonyms. In an MDSD context the abstract representation is usually
	referred to as the model. Certainly almost all MDSD tools are
	repository based, but many all repository based tools, eg
	Microsoft Access, would not consider themselves to be MDSD.


(I first explored this way of looking at environments in my essay
	on [Language
	Workbenches](https://martinfowler.com/articles/languageWorkbench.html). I've described it here because I think the notion
	of projectional environments is broader than just in Language
	Workbenches.)
