---
title: "Semantic Diff"
description: "Most version control systems rely on using and understanding the 	changes between versions of artifacts - often referred to as diffs 	from the command that can produce them in Unix.  Good diff (and me"
date: 2004-12-06T00:00:00
tags: ["version control"]
url: https://martinfowler.com/bliki/SemanticDiff.html
slug: SemanticDiff
word_count: 200
---


Most version control systems rely on using and understanding the
	changes between versions of artifacts - often referred to as diffs
	from the command that can produce them in Unix.  Good diff (and merge) algorithms are around for text and
	binary files. The trouble with
	these diffs is that they are rather dumb. All they do is look at the
	two artifact versions and generate a simple way of getting from one
	to another.


A semantic diff would understand the purpose of the change,
	rather than just the effect.


For example, lets imagine I make a change to a class by executing
	an Extract Method refactoring in a tool and that's my only change
	between versions. With current tools they see the change in the
	program text, but they don't know that I did a refactoring. As a
	result when I examine the diff between the two versions it can show
	me the changes, but it can't do it in such a way that highlights the
	refactoring. This also can make merges more awkward than it might if
	it actually knew what I was doing.


(There may be a generally accepted term for this, if so please
	let me know.)
