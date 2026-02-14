---
title: "Don't overestimate the power of versions"
date: 2007-12-30
url: https://dhh.dk/posts/20-dont-overestimate-the-power-of-versions
slug: dont-overestimate-the-power-of-versions
word_count: 554
---


I've long been impressed and puzzled by the power of big version numbers. To open source projects like Ruby on Rails, it's such a divorced measure of quality or features that I feel we need to take it's importance down a few notches.


First of all, nothing magical happens when a certain revision of the code base is blessed with a release. It's simply the decision that what we have now should have a label. So when edge revision 8441 is given the alias of Rails 2.0.2, it's just that, an alias.


In other realms of software development, it might very well imply a large amount of release preparation. Some projects and products go months in a strict feature-freeze mode where only bugs are sought out. Most open source software doesn't adhere to something this stringent, Rails certainly doesn't.


The only real software-related attribute of versions for Rails is to communicate issues of backwards compatibility. Slapping 2.0 on something is a license to break existing code that has been deprecated in the past. But this really happens so very rarely that it hardly deserves big attention.


All this is not to say that versions are meaningless, just that they're more about culture and information than about the quality of software. Having a big release is a worthy way of celebrating that things have moved forward since last time we did a release. And to give people a chance to catch up on all the new features. That's great.


But the problem is that lots of people, especially clients paying the bills of consultants, are overestimating the value of these release names to the point of avoiding newer versions of the repository that fix particular issues that they're dealing with. That doesn't make any sense at all. If you're encountering a bug or desiring a feature that's been included in the latest edge version, you're not doing yourself any favors by waiting for the whim of a release.


The great thing about open source is that you can control your own release schedule. If you happen to run in to a bug that was fixed 5 revisions past the latest release, you can simply tie your application to exactly that revision and see your problem go away. All the information is available about what changed between the official release and the revision you want to move to. And presumably your test suite will do a reasonable job of catching any adverse changes.


I think the main problem is that people do not differentiate between low-level systems, like their OS, web server, or database server, and high-level frameworks like Rails. The latter are never unstable in the traditional sense of the word like the former. The risk of applications crashing with segfaults because of a "bad version" of Rails is incredibly unlikely. So the fear and uncertainty of things just going awry in unexplained ways doesn't belong in this realm.


So please do take control of your own release schedule. It's perfectly fine to start off with a released version, but don't dream up dragons and demons lurking in a newer version of edge. Most of the time, edge is of considerably higher quality than the last released version because we've been committing loads of bug fixes since then. Take advantage of that when you can.

