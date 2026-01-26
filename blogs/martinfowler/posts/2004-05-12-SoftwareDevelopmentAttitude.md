---
title: "Software Development Attitude"
description: "As a writer and speaker on software development, I dish out a huge amount of general advice about our profession. Whether it's as specific as saying how aDecoratedCommandworks, or as philosophical as "
date: 2004-05-12T00:00:00
tags: ["process theory", "api design"]
url: https://martinfowler.com/bliki/SoftwareDevelopmentAttitude.html
slug: SoftwareDevelopmentAttitude
word_count: 298
---


Many debates in software development are underpinned by whether
the speaker has a [DirectingAttitude](https://martinfowler.com/bliki/DirectingAttitude.html) or an
[EnablingAttitude](https://martinfowler.com/bliki/EnablingAttitude.html). These different attitudes affect choices
over languages, designs, tools, processes, and lots more.


Here's some examples of this dichotomy:

- A debate a while ago triggered by Joel Spolsky's post on [exceptions](http://www.joelonsoftware.com/items/2003/10/13.html).

He didn't like exceptions because they could be misused badly, leading
to confusing code (directing). Bill Caputo [pointed
out](http://www.williamcaputo.com/archives/000009.html) that exceptions, when used well, make life much easier
(enabling).
- Some of the static/dynamic typing debate brings up these
points. Some arguments in favor of static typing talk about how they
prevent people from making certain kinds of mistake (directing) while
dynamic typers point out how static typing restricts some useful
idioms (enabling).
- Agile processes are [PeopleOriented](https://martinfowler.com/bliki/PeopleOriented.html) (enabling),
while plan-driven methods seek to ensure that even a poor team can do
an acceptable job (directing).


These aren't hard-wired attitudes. Often people are directing in
some cases and enabling in others. But I think there is a deep strain
running through here, often a personality issue, that runs underneath
much discussion on how we do software. (I'm very much in the enabling
category, as if you can't tell.)


You might think that all restrictions on what a developer does
imply a directing attitude, but it's not that simple. As an example,
consider memory management. You can think of this as a directing
feature: programmers can't be trusted to manage memory correctly so
take away their ability to allocate memory. But I look at memory
management as an enabling technology - it takes away something I don't
*want* to worry about, so I can concentrate better on those
things I do care about. Steve [tied this thought nicely](http://stevef.truemesh.com/archives/000206.html) onto the
difference between problems and difficulties.


reposted on 11 Mar 2014
