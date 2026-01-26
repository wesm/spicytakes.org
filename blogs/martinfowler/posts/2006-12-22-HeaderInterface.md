---
title: "Header Interface"
description: "A role interface is defined by 	looking at a specific interaction between suppliers and consumers. A 	supplier component will usually implement several role interfaces, 	one for each of these patterns"
date: 2006-12-22T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/HeaderInterface.html
slug: HeaderInterface
word_count: 60
---


A header interface is an explicit interface that mimics the
	implicit public interface of a class. Essentially you take all the public
	methods of a class and declare them in an interface. You can then
	supply an alternative implementation for the class. This is the
	opposite of a [RoleInterface](https://martinfowler.com/bliki/RoleInterface.html) - I discuss more details and the pros
	and cons there.
