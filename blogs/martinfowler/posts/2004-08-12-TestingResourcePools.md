---
title: "Testing Resource Pools"
description: "I was digging through some old notes, and came across a simple 	but useful tip that Rich Garzaniti gave me."
date: 2004-08-12T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/TestingResourcePools.html
slug: TestingResourcePools
word_count: 112
---


I was digging through some old notes, and came across a simple
	but useful tip that Rich Garzaniti gave me.


Many applications use resource pools - a good example is
	connection pools for database connections. Teams often get into
	trouble because people forget to release the resource back to the
	pool when they are done with it. As a result you get resource leaks.


To help spot these in testing, make sure you set the resource
	pool size to 1 in your tests. That way if some code doesn't release
	its resource the next test that uses that resource will fail, and
	you don't have too far to look for the culprit.
