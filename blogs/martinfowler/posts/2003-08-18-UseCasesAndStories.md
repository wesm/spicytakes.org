---
title: "Use Cases And Stories"
description: "What is the difference between aUseCaseand XP'sUserStory?"
date: 2003-08-18T00:00:00
tags: ["requirements analysis", "uml"]
url: https://martinfowler.com/bliki/UseCasesAndStories.html
slug: UseCasesAndStories
word_count: 307
---


**What is the difference between a [UseCase](https://martinfowler.com/bliki/UseCase.html) and XP's
	[UserStory](https://martinfowler.com/bliki/UserStory.html)?**


This is a common question, and not one that has a generally
	agreed on answer. Many people in the XP community consider stories
	to be a simplified form of use cases, but although I used to hold
	this view I see things differently now.


Use cases and stories are similar in that they are both ways to
	organize requirements. They are different in that they organize for
	different purposes. Use cases organize requirements to form a
	narrative of how users relate to and use a system. Hence they focus
	on user goals and how interacting with a system satisfies the
	goals. XP stories (and similar things, often called features) break
	requirements into chunks for planning purposes. Stories are explicitly
	broken down until they can be estimated as part of XP's release
	planning process. Because these uses of requirements are different,
	heuristics for good use cases and stories will differ.


The two have a complex correlation. Stories are usually more
	fine-grained because they have to be entirely buildable within an
	iteration (one or two weeks for XP). A small use case may correspond
	entirely to a story; however a story might be one or more scenarios
	in a use case, or one or more steps in a use case. A story may not
	even show up in a use case narrative, such as adding a new asset
	depreciation method to a pop up list.


Do you need to do both? As in many things, in theory you do but
	in practice you don't. Some teams might use use cases early on to
	build a narrative picture, and then break down into stories for
	planning. Others go direct to stories. Others might just do use cases
	and annotate the use case text to show what features get done when.
