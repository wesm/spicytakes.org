---
title: "Clock Wrapper"
description: "If you need to get the current date or time in your code, don't 	access the system routines for that data directly. Put some form of 	wrapper around it that allows you to override it by setting the â"
date: 2005-03-26T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/ClockWrapper.html
slug: ClockWrapper
word_count: 50
---


If you need to get the current date or time in your code, don't
	access the system routines for that data directly. Put some form of
	wrapper around it that allows you to override it by setting the âcurrent date/timeâ
	to a particular value. This is important to simplify testing.
