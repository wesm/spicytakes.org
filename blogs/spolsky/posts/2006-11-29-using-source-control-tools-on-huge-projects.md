---
title: "Using source control tools on huge projects"
date: 2006-11-29
url: https://www.joelonsoftware.com/2006/11/29/using-source-control-tools-on-huge-projects/
word_count: 638
---


Of all the things broken at Microsoft, the way they use source control on the Windows team is *not* one of them.


A young Windows engineer writes:


> “… prior to the restart effort of Longhorn, there were about seven [branches], reverse-integrating into one main branch every two or three weeks perhaps. Now, imagine several thousand developers checking in directly into seven branches. This will lead to two things:
> “1. you check in frequently, and there’s a very high chance of either breaking the build, or breaking functionality in the OS, or 2., as a counter-reaction, you don’t check in very often, which clearly is bad, since now you don’t have a good delta history of what you did.
> “So this clearly didn’t scale. As part of the restart effort, we decided that each team would get its own feature branch, each feature area (multiple teams) would go up to an aggregation branch, and those would lead up to the final main branch. (As such there’s now north of a hundred branches in tiers, leading up to about six aggregation branches.) Teams were free to choose how many sub-feature branches they wanted, if any, and they were free to choose how often they wanted to push up their changes to the aggregation branch. As part of the reverse-integration (RI, i.e. pushing up) process, various quality gates had to pass, including performance tests. Due to how comprehensive those gates ended up being, this would take at least a day to run, plus perhaps a day or two to triage issues if any cropped up; so there was a possibly considerable cost to doing an RI in the first place. However, these gates were essential in upholding the quality of the main branch, and had they not existed, the OS would have never shipped. I suppose it’s one of those ‘what doesn’t kill you…’ type deals.
> “Some teams did manage to manufacture pathological cases for themselves where changes wouldn’t RI up for several months, but that’s the individual team’s fault (or their release management), and not the process. Generally, the more disciplined teams were about quality, the faster and more frequently they’d RI. From what you know about the varying levels of stability/quality of components of the OS, it’s pretty easy to map that back to RI velocity and so forth, since it all goes hand-in-hand pretty nicely.”


When you’re working with source control on a huge team, the best way to organize things is to create branches and sub-branches that correspond to your individual feature teams, down to a high level of granularity. If your tools support it, you can even have private branches for every developer. So they can check in as often as they want, only merging up when they feel that their code is stable. Your QA department owns the “junction points” above each merge. That is, as soon as a developer merges their private branch with their team branch, QA gets to look at it and they only merge it up if it meets their quality bar.


The best way to imagine this is to look at [this screenshot from Accurev](http://www.accurev.com/images/screenshots3_7/BigStream.png). As you can see there are a lot of “leaf” branches but as things get merged up towards the trunk, they have to pass through QA which basically just checks that it’s OK and then merges it closer to the trunk. By the way, [Accurev](http://www.accurev.com/) makes a nice source control system that is designed for this style of intensive branching and merging. The Windows team itself uses their own source control system which, it is rumoured, is just an old version of [Perforce](http://www.perforce.com/) for which they bought a source license; Perforce has a reputation among developers for being expensive, solid, and extremely fast when working with extremely large source code bases.
