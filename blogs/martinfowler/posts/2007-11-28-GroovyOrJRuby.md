---
title: "Groovy or JRuby"
description: "Currently there's quite a debate raging over the relative merits 	of Groovy and JRuby as scripting languages running on the Java 	virtual machine. Curious minds want to know - which of these 	language"
date: 2007-11-28T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/GroovyOrJRuby.html
slug: GroovyOrJRuby
word_count: 1184
---


Currently there's quite a debate raging over the relative merits
	of Groovy and JRuby as scripting languages running on the Java
	virtual machine. Curious minds want to know - which of these
	languages will win this upcoming language war? People want to know
	which language to pick for a project, or which language to commit to
	learn.


Perhaps the first thing to point out is that it's perhaps rather
	unfair to see this as a race between these particular two
	horses. Scripting has been available on the JVM for a long
	time. Jython, a Java implementation of Python, has been around for
	several years. There's plenty of other, more obscure languages,
	which I daren't mention for fear of offending all the ones I miss out.


JRuby has got a lot of attention due to the attention of the Ruby
	language generally - attention particularly ignited by the interest
	around Rails. We've seen a sharp spike of interest around Ruby and
	Rails work at Thoughtworks, and JRuby adds an extra dimension since
	it allows people to deploy Rails applications using their existing
	Java infrastructure.


Groovy gets its attention because it, more than any other
	language, is designed to work seamlessly with the JVM, and got a lot
	of attention from an early JSR.


Personally I'd dropped Groovy from my radar a couple of years ago
	when its development seemed to bog down. With its 1.0 release and
	further interesting positive vibes from some of my colleagues I've
	started to pay attention again.


Lets begin by talking about similarities. Both JRuby and Groovy
	(and indeed Jython) are modern OO scripting languages. They combine
	the well-chosen terseness of scripting languages with good solid
	structures for building larger programs. As such they are suitable
	both for classical scripting and for writing larger programs. Both
	are comfortable with dynamic type checking, although Groovy does
	offer some static facilities too. Both support [Lambdas](https://martinfowler.com/bliki/Lambda.html)
	which are an important feature for the greater expressiveness that
	people want from this kind of language.


The biggest difference between them is their broader platform
	philosophy. Groovy is designed to be a scripting language for
	Java. As much as possible its syntax tries to match the equivalent
	in Java. (Including such ugly things as the default fall-through in
	switch statements.) It also works with Java's class library
	directly, although it dynamically adds many methods to Java's
	classes, vital in order to make use of things like closures.


JRuby, however, is a Java implementation of the Ruby
	*platform*. Ruby can run directly on mainstream operating systems with
	a C runtime, and is starting to run on .NET's CLR. When you
	program in JRuby you primarily use Ruby's libraries which are
	implemented in Java, and may also use Java's libraries at your
	discretion. If you stick to Ruby's libraries, or at least wrap any
	foreign elements, you can run Ruby programs on the C, Java, or (in
	time) .NET
	runtimes. So you can use JRuby to both run Ruby programs on the JVM
	and as a language for scripting the JVM.


One of the big differences between JRuby and Jython is around the
	libraries. One of the tricky aspects of porting this kind of
	scripting language to the JVM is that these languages are usually
	closely intertwined with libraries implemented in C. Porting these
	libraries to Java involves rewriting the libraries in Java. Jython
	didn't do much of this, as a result many Python apps can't run in
	Jython. However the JRuby implementers decided from early on that their
	goal was to run Rails apps, as a result many libraries including all
	the Ruby standard libraries needed to be ported.


The fact that JRuby is a Ruby platform on the JVM means that in
  JRuby you have two kinds of objects - JRuby objects and Java
  objects. Although there are ways for the two to talk to each other
  and to convert there is a difference. There are times when you need
  to know whether you're dealing with a Java string or a JRuby
  string. With Groovy you don't have that boundary, there are just
  Java objects.


It's too early, or rather too difficult, to say if one language
	will win out. Both are pretty young, only just finding their feet on
	the JVM. On a more personal level, your choice has a lot to do with what
	you expect to do with it. If you are only interested in running on
	the JVM, then Groovy could well be the easier choice. You are
	working directly with Java's library and object model, and the syntax
	requires less getting used to. A strong reason to prefer Ruby is the
	fact that it lives in multiple implementations. Ruby is a tool you
	can use in a lot of other places. As a long time Rubyist, there's
	not much incentive for me personally to get heavily into Groovy,
	even though I actually like the language a lot from what I've seen
	of it.


Rails is an important factor. The Java world is hardly
	lacking in web frameworks, but Rails is widely liked by those who've
	used it. I've not got many reports yet about Grails (the Groovy
	knock-off) so can't give a firm opinion on that. But I can imagine
	that the ability to deploy web apps with Rails could be a major
	factor in making JRuby popular. Something else to look at is the
	growth of RSpec as a new spin on testing environments.


With any platform it's as important to consider the people
involved in the community as much as any technical factors. Good people
can overcome technical weaknesses quickly and a vibrant community is a
potent source for big innovations. [RubyPeople](https://martinfowler.com/bliki/RubyPeople.html) have formed
a particularly strong community, which has already spawned things like
Rails, Rake, and Rspec.


Will either matter to Java? After all Jython's been around for a
	long time without making a huge impact on the JVM. Tool support is
	frankly pathetic for any of these languages when you compare it to
	what you have for Java at the moment.


I think we're actually at an inflection point with Java. Until
recently the Java cry was One VM and [OneLanguage](https://martinfowler.com/bliki/OneLanguage.html). (As
opposed to the CLR which started with the cry of one VM and many
languages - providing
they're C# or VB.) This seems to be changing as people realize the
limitations of Java and begin to seek out different capabilities. It's
likely the future will see multiple languages closely integrated
within the JVM.


There are plenty of people who dislike the hype around Rails and
	Ruby. But even if you dislike Ruby, the hype has led to a resurgence
	of interest in new languages. I doubt if the interest in Groovy
	would be anywhere near as great as it is if it wasn't for this hype,
	nor would Jython be awaking from its slumbers. The ruby/rails hype
	has also generated interest in other exotic JVM languages. The
	really nice thing here is that the JRuby people have been
	encouraging their dynamic rivals - recognizing that the point
	here is to encourage multi-lingual inter-operability and innovation.
