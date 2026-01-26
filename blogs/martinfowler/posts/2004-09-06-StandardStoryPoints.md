---
title: "Standard Story Points"
description: "I've heard a couple of questions recently about coming up with a 	standard story point mechanism for multiple teams using extreme 	programming's planning approach. The hope is have several teams all 	"
date: 2004-09-06T00:00:00
tags: ["metrics", "requirements analysis", "project planning", "estimation"]
url: https://martinfowler.com/bliki/StandardStoryPoints.html
slug: StandardStoryPoints
word_count: 451
---


I've heard a couple of questions recently about coming up with a
	standard story point mechanism for multiple teams using extreme
	programming's planning approach. The hope is have several teams all
	using equivalent story points, so that three story points of effort
	on one team is the same as on another.


I think trying to come up with this at best of limited value, and
	at worst dangerous.


The estimating system of extreme programming is based on
		[XpVelocity](https://martinfowler.com/bliki/XpVelocity.html) and [YesterdaysWeather](https://martinfowler.com/bliki/YesterdaysWeather.html). Inherent
		in this is the idea that when you make estimates, the actual units
		you estimate aren't important - what's important is you estimate
		by rough comparative value and use [YesterdaysWeather](https://martinfowler.com/bliki/YesterdaysWeather.html)
		for calibration.


In this situation the story points act as an anchor for the
		feedback loop that Yesterday's Weather provides - nothing more.
		Baked into them are all sorts of assumptions about the nature of
		the team's task, the capability of the team, and whether the team
		are optimistic or pessimistic estimators. Once you try to come up
		with a standard across teams you are trying to normalize all of
		these factors. Trying to do this sounds very hard to me, and I'm
		not aware of anyone who has done this effectively. This doesn't
		mean its impossible, it just means it's hard.


The dangerous aspect comes from once you have a standard unit for
	measurement across teams, someone is inevitably going to use it to
	compare the performance of teams. Even if everyone swears till they
	are blue in the face that they won't use it for cross team
	measurement, there will always be the suspicion that this will
	happen eventually. This will cause teams to distort their
	measurements so that it seems that they get more story points
	done. My fear is that this will break the feedback loop of
	yesterday's weather and knock the planning process off kilter. I'm
	always suspicious about these things because while it would be
	incredibly valuable to have a way to measure productivity I think
		the nature of software is such that we [CannotMeasureProductivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html).


So to be worth trying, this has to yield some valuable benefits -
	but I don't see any. One reason that I've heard is to help people
	move onto teams and estimate more quickly. But you can't estimate on
	a new team until you get reasonably familiar with the problem and
	the current code base. As you do that you'll also get a feel for the
	relative sizes of story points on that team. We move people around
	between projects at Thoughtworks and I've never heard anyone
	complain about difficulty of estimating when coming onto a new team
	due to differences in story points.


reposted on 10 May 2012
