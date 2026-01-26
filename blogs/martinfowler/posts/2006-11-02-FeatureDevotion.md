---
title: "Feature Devotion"
description: "A common, perhaps dominant, practice of agile methods is to 	develop a list of features (often called stories) for the software 	that's being built. These features are tracked with index cards, 	work "
date: 2006-11-02T00:00:00
tags: ["agile", "bad things", "requirements analysis", "process theory"]
url: https://martinfowler.com/bliki/FeatureDevotion.html
slug: FeatureDevotion
word_count: 504
---


A common, perhaps dominant, practice of agile methods is to
	develop a list of features (often called stories) for the software
	that's being built. These features are tracked with index cards,
	work queues, burndown charts, backlogs, or whatever your tool of
	choice is.


On the whole I like this kind of approach. By breaking down
	everything you need to do into small tasks that you can complete in
	a week or few, you can visualize progress and get a sense of how much
	you can get done. I've often said that the key benefit of iterative
	development is to reduce risk by forcing completion of software in
	chunks instead of the waterfall habit of leaving long and hard to
	manage activities (testing, integration) till late in the project.


The problem comes when this list [suddenly grows horns and fangs
and becomes a Fixed-Price Fixed-Scope Big Up-Front Project
Plan.](http://dannorth.net/2006/10/28/outcomes-over-features-the-fifth-agile-value/) Craig Larman once joked that the waterfall process has
strong antibodies that reject iterative processes by warping them into
some form of waterfall. RUP has been a common victim of these
antibodies, seeing its phases turn into some variant of the
analysis-design-build-test conveyor.


The key to beating off the waterfall is to realize that, as Dan
	puts it, agilists value Outcomes over Features. The feature list is
	a valuable tool, but it's a means not an end. What really matters is
	the overall outcome, which I think of as value to the customers.


An important part of this thinking is that you expect the feature
list to change as the project goes on. This happens you discover new
things that you can do, and re-prioritize old things. This is the
essence of [adaptive

planning](https://martinfowler.com/articles/newMethodology.html#PredictiveVersusAdaptive), which has always been a key indicator of agile thinking.
This results a big shift in how people think about a plan. In
plan-driven projects, success and failure is often worded in terms of
âdid things go according to the plan?â In agile projects this is a
meaningless question, because plans change so often. The plan is a
tool, primarily one that you use to gauge the effect of changes: âhow
will adding this feature affect what we doâ. The plan is a tool to
figure out what should fit in the [FivePoundBag](https://martinfowler.com/bliki/FivePoundBag.html). If your
plan's not constantly changing, you are very unlikely to be doing
adaptive planning, and hence aren't agile.


Feature lists have another problem - you easily lose sight of the
context that makes the feature valuable. This is a reason why Alistair
Cockburn is a proponent of use cases, because they concentrate on a
narrative of how someone uses a system. Marc NcNeil also talks about
this in terms of [Customer

Journeys](http://www.dancingmango.com/blog/2006/10/19/ditch-the-feature-shopping-list-think-customer-journeys/). The weakness of use cases in planning is that they don't
give you clear units to tick off so you can assess progress and
project consequences of choices into the future. That makes them less
useful as a planning tool, but that doesn't negate their value as tool
for imagining what a good outcome would be.
