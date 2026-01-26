---
title: "Spreading Incrementalism"
description: "From time to time people question whether a particular specialty can be 	used incremental way: âYou can't do (security | user interface 	design | databases | internationalization | * ) with an agile"
date: 2005-01-05T00:00:00
tags: ["agile", "agile adoption", "process theory"]
url: https://martinfowler.com/bliki/SpreadingIncrementalism.html
slug: SpreadingIncrementalism
word_count: 453
---


From time to time people question whether a particular specialty can be
	used incremental way: âYou can't do (security | user interface
	design | databases | internationalization | * ) with an agile
	project because this aspect has to be done up front.â


When a question like that's put to me, I'm immediately on a
	sticky wicket because I'm not that knowledgeable on that
	specialty. Application design is something I think I can talk
	about, but security (for instance) isn't - and my questioner may
	well be a well regarded leader in that field.


Despite my acknowledged limitations in that field, I'm not about
	to say that you can only use planned design in
	that area. What I can say is that we don't really know whether you
	can do incremental design in that area. I've seen enough cases where
	people have said âyou can't use incremental design for xâ only to
	find you can. Application design is one, database design is
	another. So until people try incremental design out in a serious
	way, I'm very reluctant to rule it out.


Part of the difficulty of assessing this question is that it's
	too easy to do incremental design poorly. If you do incremental
	design in an uncontrolled way, you are most likely to end up with a
	design that is a mess - to make incremental design work you need something
	that makes the design converge into order. In [Is Design Dead](https://martinfowler.com/articles/designDead.html) I
	referred to these as enabling practices. For software design I
	labeled testing, continuous integration, and refactoring as key
	enabling practices to get software design to converge and avoid
	software entropy. When we talk about something else, like UI design,
	the issue is finding what those enabling practices are. They may be
	similar or inspired by those in software design, or they may be
	something different. In database design, for instance, incremental data
	migration is a key enabling practice. Until you find a good set of
	enabling practices, incremental design is thin ice.


Despite that thinness, I do think that an incremental approach is
	so worthwhile, that it's worth experimenting to find the right
	way. Phased up-front design approaches fail far too frequently -
	furthermore they do a poor job in the chance of volatile
	requirements - which I see as a unavoidable factor, at least in
	enterprise software development.


The biggest reason, however, that I favor incrementalism is the
	oldest one - risk management. Without trying out your designs, you
	are too vulnerable to things not working out the way you think they
	would, too vulnerable to schedule slippages late in
	development. These risks are reason enough to look for ways to
	introduce incrementalism into more aspects of software development.
