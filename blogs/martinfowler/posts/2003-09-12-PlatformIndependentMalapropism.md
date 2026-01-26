---
title: "Platform Independent Malapropism"
description: "One of the big claims aboutModel Driven Architecture(MDA) is that it allows you to develop a system in a Platform Independent Model (PIM) that can then be transformed into Platform Specific Models (PS"
date: 2003-09-12T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/PlatformIndependentMalapropism.html
slug: PlatformIndependentMalapropism
word_count: 306
---


One of the big claims about [Model Driven Architecture](http://www.omg.org/mda/) (MDA) is
that it allows you to develop a system in a Platform Independent Model
(PIM) that can then be transformed into Platform Specific Models (PSM)
for technologies such as .NET or Java. An alert reader should say to
this: âhang on a moment, isn't the whole point of Java to be platform
independent? So why would I want some platform independent technology
that generates another platform independent technology?â


To think about platform independent, you first have to decide
what you mean by *platform*. For those involved in technologies
like Java, platform means your hardware and operating system. I can
take programs written in Java on my windows box and run them on my
unix box with little or no trouble. That's the form of platform
independence that I'm used to.


When MDA talks about platform independence, it's treating your
programming environment as the platform. But this is complete hogwash.
MDA uses a bunch of OMG standards (UML, MOF, XMI, CWM etc), these
standards are every bit as much a platform as the Java stack (or the
.NET stack for that matter). All you are doing is swapping one
(hardware/OS) platform independent programming environment for
another. You aren't getting any more independence.


Indeed one could say you are worse off. Let's take the simplest
program any programmer has to write: Hello World. How exactly do you
do that in the standard OMG PIM platform? Well you can't, because
there are no I/O libraries defined in the OMG PIM standards. You
either call something platform specific or you have to roll your own
libraries - which naturally are non-standard.


Now this alone doesn't mean that MDA is a waste of time. There are
other potential benefits to the MDA message. But the platform
independent argument has no foundation.
