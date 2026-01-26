---
title: "Shifting To Code Ownership"
description: "In my recentCodeOwnershippost, I described the way in which I 	think about code ownership issues. Many of my software development 	friends are extreme programmers, and tend to favor collective code 	o"
date: 2006-05-15T00:00:00
tags: ["agile adoption", "team organization"]
url: https://martinfowler.com/bliki/ShiftingToCodeOwnership.html
slug: ShiftingToCodeOwnership
word_count: 428
---


In my recent [CodeOwnership](https://martinfowler.com/bliki/CodeOwnership.html) post, I described the way in which I
	think about code ownership issues. Many of my software development
	friends are extreme programmers, and tend to favor collective code
	ownership. However these kind of practices aren't absolute and
	should always be tempered by local considerations. One of my
	colleagues sent me a note with the following story which I thought
	was a good indication of when you have to vary your practices, even
	if you are a strong fan of XP. (As he's talking about his team, he
	prefers to be anonymous.)


> I shifted our team from the âcollectiveâ to âweakâ
> model, in order to counter some undisciplined programming by a couple
> of developers. Combined with some rather candid feedback, the result
> was a gain in velocity since the programmers who now âownâ our key
> code areas are not constantly reworking sub-par code, while those that
> were doing sub-par work in those critcal areas are instead doing
> things like bug hunting and low-risk code changes -- which further
> frees up the others.
> We also had a net gain in morale, since everyone but the sub-par
> producers were getting frustrated by having to watch their every
> check-in for issues, and fixing the problems that they didn't catch in
> time. This change rewarded those who took quality, TDD,
> non-speculation, etc. seriously.
> However, we also needed some additional practices and policies to
> counterbalance:
> - More frequent pair switching (our actual policy is that you can
> still work on any part of the code, but if its in an area other than
> one where you have âfree playâ, you need to pair with someone who
> does, or heavily vet your ideas through them first)
> - The way back in is through the owners. If they feel comfortable that
> your code will be up to snuff, you can take tasks freely there again.
> - If things don't improve, then we'll have to take further steps.
> It's been very educational for me, because I never had to go this far
> before, and I was really reluctant to âplay the heavy.â It was really
> tough for me to introduce a [directing](DirectingAttitude.html) instead of an [enabling](EnablingAttitude.html) practice,
> but things have been much improved since.


This kind of local adaptation is an essential part of extreme
	programming, or any agile method. All things being equal my
	colleague still prefers collective code ownership, but all things
	are seldom equal.
