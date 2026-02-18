---
title: "Fostering a culture that values stability and reliability"
date: 2021-01-04
url: https://drewdevault.com/2021/01/04/A-culture-of-stability-and-reliability.html
slug: A-culture-of-stability-and-reliability
word_count: 514
---

There’s an idea which encounters a bizarre level of resistance from the broader
software community: that software can be completed. This resistance manifests in
several forms, perhaps the most common being the notion that a git repository
which doesn’t receive many commits is abandoned or less worthwhile. For my part,
I consider software that aims to be  *completed*  to be more worthwhile most of
the time.

There are two sources of change which projects are affected by: external and
internal. An internal source of change is, for example, a planned feature, or a
discovered bug. External sources of change are, say, when a dependency makes a
breaking change and your software has to be updated accordingly. Some projects
will necessarily have an indefinite source of external change to consider, often
as part of their value proposition.  [youtube-dl](https://youtube-dl.org/)  will always evolve to add
new sites and workarounds,  [wlroots](https://github.com/swaywm/wlroots)  will continue to grow to take advantage
of new graphics and input hardware features, and so on.

Any maintained program will naturally increase in stability over time as bug
fixes accumulate, towards some finite maximum. However, change drives this trend
in reverse. Introducing new features, coping with external change factors, even
fixing bugs, all of this often introduce new problems. If you want to produce
software which is reliable, robust, and stable, then managing change is an
essential requirement.

To this end, software projects can, and often should, draw a finish line. Or, if
not a finish line, a curve for gradually backing off on feature introduction,
raising the threshold of importance by which a new feature is considered.

[Sway](https://github.com/swaywm/sway) , for instance, was “completed” some time
ago. We stopped accepting most major feature requests, preferring only to
implement changes which were made necessary by external sources: notably,
features implemented in i3, the project sway aimed to replace. The i3 project
 [announced this week](https://old.reddit.com/r/i3wm/comments/kn8pa2/an_update_on_the_future_of_i3/)  that it was adopting a similar policy regarding new
features, and thus sway’s change management is again reduced in scope to only
addressing bugs and performance. Sway has completed its value proposition, and
now our only goal is to become more and more stable and reliable at delivering
it.

[scdoc](https://sr.ht/~sircmpwn/scdoc)  is another project which has met its
stated goals. Its primary external source of change is roff — which is
almost 50 years old. Therefore, it has accumulated mainly bugfixes and
robustness over the past few years since its release, and users enjoy a great
deal of reliability and stability from it. Becoming a tool which “just works”
and can be depended on without a second thought is the only goal going forward.

Next time you see a git repo which is only getting a slow trickle of commits,
don’t necessarily write it off as abandoned. A slow trickle of commits is the
ultimate fate of software which aims to be stable and reliable. And, as a
maintainer of your own projects, remember that turning a critical eye to new
feature requests, and evaluating their cost in terms of complexity and
stability, is another responsibility that your users are depending on you for.
