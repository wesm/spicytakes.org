---
title: "Language Workbenches and Model Driven Architecture"
description: "There's been a recent surge in development of tools that allow you integrate between multiple Domain Specific Languages (DSL) - tools that I refer to as language workbenches. Much of the discussion ar"
date: 2005-06-12T00:00:00
tags: ["language workbench"]
url: https://martinfowler.com/articles/mdaLanguageWorkbench.html
slug: mdaLanguageWorkbench
word_count: 2307
---


As I was working on my article on [language workbenches](languageWorkbench.html), an immediate
question was the relationship between them and Model Driven
Architecture (MDA): a group of standards promoted by the Object
Management Group (OMG). This is particularly relevant for the case of
Software Factories, where's there's been considerable dispute about
Microsoft's intentions in ignoring the OMG's standards. (If you
haven't already you might want to read [language workbenches](languageWorkbench.html) to get an
understanding of how I describe language oriented programming and
language workbenches.


You'll notice that many of the arguments around MDA are similar
to those around language workbenches. Indeed many MDA tools could be
argued to be language workbenches.


## The Three MDA Camps


The first step in discussing this is to realize that MDA
actually means a number of distinctly different - indeed incompatible
- things to different people. Steve Cook described the variation as
falling into [three

mutually disdainful camps](http://blogs.msdn.com/stevecook/archive/2004/10/27/248322.aspx):

- **UML PIM:** Use UML to build Platform Independent
Models which are transformed (or elaborated) into Platform Specific
Models which are transformed (or elaborated) into code.
- **MOF:** Don't use the UML at all but define languages
and transformations using the OMG's Meta Object Facility (MOF).
- **Executable UML:** Build a compiler for the UML (or
extended subset) and treat the UML as a programming language.


Of these three camps the UML PIM and MOF camps are, to some
extent, working on language oriented programming. The Executable UML
camp isn't really interested in language oriented programming. This
isn't a bad thing - indeed some of the Executable UML folks seem the
most sensible of the various UML advocates, but they aren't relevant
to the discussion here.


There is another camp, which is best to refer to as the Model
Driven Development (MDD) camp. They aren't really part of MDA at all,
since they don't take the OMG standards seriously - and MDA is an OMG
standard. The confusion arises because people often incorrectly refer
to MDD efforts without OMG as MDA. To be correct it's better to say
that MDA is MDD using OMG standards. (I'll discuss MDD shortly.)


All this means that in order to discuss the role of MDA in
language workbenches I have to examine the UML PIM and MOF camps
separately, since the the way in which they think of language oriented
programming is quite different.


## The UML PIM Camp


UML PIM style MDA is based on the idea of developing a system
using the UML as a 'Platform Independent Model (PIM)' first. (Although
[it

isn't really platform independent.](https://martinfowler.com/bliki/PlatformIndependentMalapropism.html)) Once you've done that it's
transformed (via a Platform Specific Model - PSM) into code. This PIM
is UML and, like a language workbench, the key source of the
information is stored in abstract representation using the UML
meta-model. Editing (usually by graphical tools that dare not call
themselves CASE tools any longer) is done through projectional editors
which render using the UML's diagrammatic standards.


Using persistent abstract representations and projectional
editors is certainly what language workbenches do, but isn't enough to
qualify as a language workbench. To be a language workbench you have
be able to define new languages yourself and integrate them into the
rest. The UML PIM way of doing this is to use the language extension
features built into the UML - stereotypes and their ilk.


In theory there's no reason why a UML PIM system can't be a
language workbench. The question is whether using the UML PIM approach
is a good way to build a language workbench. Since the approach with
UML is to extend the UML in a way defined by the UML, working DSLs
with UML more like an internal DSL rather than the integrated external DSLs of a
language workbench. In this case you don't need to think of the
language workbench trio of schema, editor, and generator - rather you
consider how easy it is to extend the UML enough to satisfy your
needs.


The problem here is that the UML is a mightily complex
language. The extension mechanisms are also quite complex and it's not
easy to see how they will work out in practice. It's also not clear
how well tools will be able to manipulate these extensions. One
particular gray area is that of generation. There is no standard
generation standards to define how UML diagrams get interpreted as
code. As a result there's no sufficiently precise semantics for the
UML. Indeed I've heard UML proponents proud to say that UML has no
semantics.


You could use the UML meta-model to define a DSL schema, but
here the UML is both too much and too little. The UML includes many
elements that you don't need for defining a schema - and it's not
clear that it gives you the constructs you need. Furthermore the UML
provides nothing to help define editors or generators. For this
purpose the UML meta-model is a large, complex beast that doesn't
cover the core requirements of a language workbench and adds lots of
unnecessary stuff. It's rather like saying we should build a speedboat
out of a truck because they both have a steering wheel.


Despite my obvious disdain for this approach there are people
doing language workbench work on a UML PIM basis. If you disagree with
my assessment of the UML's suitability for this work you should
certainly investigate these people further.


## The MOF camp


The Meta Object Facility comes out of a separate community
within the OMG than the UML and relationships between the MOF and UML
camps have often been frosty. The MOF efforts are more tied into the
OMG's CORBA work, and much of the driver for MOF came from working
with CORBA.


The MOF standard is a standard for meta models of meta
models. So you might use MOF as a language for defining the UML meta
model. Indeed MOF compatibility of the UML meta-model was a long
running issue in UML work. In terms of language workbench the MOF
corresponds to a DSL for defining DSL schemas - similar to the [MPS
structure language](mpsAgree.html#defineSchema). If you look at MOF documentation you'll notice
many similar features to what we saw the MPS structure editor. So
essentially MOF is (yet another) data modeling meta-model. It's object
history also gives it operations, although there's no behavioral
modeling mechanisms (unlike UML.)


MOF is much smaller than UML - essentially a subset of the
class diagramming part of UML. Since this is exactly the kind of thing
you need for DSL schemas - MOF makes a much better fit than UML for
this task. Indeed some people propose that MOF would be a good schema
for abstract representations, or at least storage representations for
a language workbench.


However MOF is still not a perfect fit - operation
definitions make sense in the context of remote object
interoperability (CORBA) but rather less so than for DSL schemas. So
much of the debate about using MOF for DSL schemas turns on the
question of how good a fit it really is. Does MOF carry unnecessary
baggage or does it miss important elements? I don't have a strong
opinion on this, so for me this is an open question.


Rather more to the point, MOF misses anything to speak of
editor or generator definitions. Since these are two key elements of a
language workbench these are big holes in MOF from a language
workbench perspective. The OMG is preparing a standard to address some
of this called QVT - Query, View, Transformation. QVT in principle may
plug the generator gap - but it's still early in its development.


Where MOF may be useful is as an interchange mechanism
between language workbenches for DSL schemas. So it could be useful in
that context but it wouldn't be enough to fully interchange DSLs as it
lacks the editor and generator pieces. Still it strikes me as a more
useful part of the MDA standards world for language workbenches than
the bloated UML.


## MDA and Standardization


One of the small brush-fires around language workbenches has
been criticism of Microsoft for ignoring MDA in its Software Factories
effort. A number of people have taken this as yet another case of evil
Microsoft ignoring community standards in favor of a proprietary
solution.


You'll probably notice that Intentional Software and MPS also
ignore the MDA - both of them see the various MDA standards as not
really useful for what they are doing. Microsoft's knowledge of MDA is
better than most, many members of the Software Factories team have
been long time members of the UML community. They've come to the same
decision - the MDA standards are just not a good fit for what they
want to do.


I think there's very valid reasons for this attitude. Both
the UML PIM and MOF camps of MDA can only claim support for
standardizing DSL schemas - the equally important elements of editors
and generators are utterly ignored. Furthermore the whole thing is
backwards. In my view you define standards once you've figured out
common elements of working technologies. language workbenches are too
immature to be ready for standards yet. I suspect that a standard for
DSL schemas could be built on MOF, or at least would look like MOF -
if only because these schemas are data models and most of MOF is a
data modeling standard. But language workbench tools are still trying
to figure out what they need - so any attempt to get a standard
together now risks premature standardization.


There are people building tools under the banner of some form
of MDA which could be considered language workbenches. I haven't
looked at any of these in depth. Such tools should have as good a
chance of any as being useful, but it seems that UML or MOF is only
going to be helpful for part of such a tool's capability and UML, due
to its complexity, could actually be harmful.


All of this isn't to say that UML notation isn't useful for
language workbenches. Indeed I think there is some validity in
criticizing Software Factories here in that their graphical standards
could be closer to UML. For certain types of diagrams, UML-like
notation makes a lot of sense. UML (at least in [sketching
mode](https://martinfowler.com/bliki/UmlAsSketch.html)) has become moderately well-known. I expect tools will use
UML-like diagrams when it makes sense - although they may not follow
UML standards absolutely and not use the UML meta model as their
abstract representation.


## Model Driven Development


As I mentioned above, there is a strand of people who like
many of the ideas of using (primarily) graphical models to drive
software development, but aren't so keen on the OMG stack of
standards. This community is best referred to as the Model Driven
Development (MDD) community.


They share a number of common strands with the MDA community.
Many of them come out of the CASE tool efforts of the 80's and 90's.
They tend to prefer graphical to textual models. The like the idea of
editing abstract representations through projecting editors. Many of
them support the idea of letting people define their own graphical
languages.


In these senses there is a lot of philosophic agreement with
MDD and language workbenches. Indeed one can reasonably say that
language workbench interest comes from two backgrounds - programming
language people and modeling people. The Software Factories team has
more of a modeling background.


Not all MDD followers consider it important that people
easily define and integrate their own language. For many people in the
MDD world, the important thing is defining system in terms of a set of
models - there is less priority in coming up with ways to define and
integrate multiple DSLs. While mostly a difference of emphasis - it's
still an important distinction between MDD and many of the language
oriented programming efforts.


There's no particular reason why efforts from the MDD
community cannot produce language workbenches. Indeed, other than a
(to me irrelevant) argument between graphical and textual languages
MDD and language oriented programming share most things. One tendency
I've noticed, however, is that MDD people often don't pay serious
attention to generators. There's often an attitude amongst modelers
that generating code is a trivial implementation issue - once the
modeling is done, all the hard work is done. Yet getting the
generators sorted out is key to making language oriented programming
work, because generators effectively define the semantics of DSLs. The
tendency to play down generators is a major reason why so many
programmers don't take modelers seriously. The UML communities
disinterest in providing any kind of mapping between UML and common
target language in any form other than hand waving is a good example
of this gap.


## Closing Thoughts


I've become known for having a pretty skeptical view of the
MDA. Most of this negativity is towards the UML PIM camp - I think the
UML is too complex and is too  semantically incoherent to act as a
serious base for future work. The question in this article, however,
is what role the MDA should play in language workbenches?


My answer is ânot muchâ. Certainly there is a need to define
effective interchange representations between language workbenches.
Without it there is a risk of vendor lock-in which will deter many
users and could stunt the usage of language workbenches. However I'm
not convinced that the OMG standards are the answer, primarily because
they were designed for a different purpose. I take the view that first
you need to figure out how to do something, then you should figure out
what and how to standardize. The OMG standards might be applicable to
some parts of the picture (MOF for schemas spring to mind). But it's
too early in the language workbench life-cycle to tell.


---
