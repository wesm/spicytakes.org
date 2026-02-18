---
title: "Dependencies and maintainers"
date: 2020-02-06
url: https://drewdevault.com/2020/02/06/Dependencies-and-maintainers.html
slug: Dependencies-and-maintainers
word_count: 746
---

I’m 34,018 feet over the Atlantic at the moment, on my way home from FOSDEM. It
was as always a lovely event, with far too many events of interest for any
single person to consume. One of the few talks I was able to attend 1  left a
persistent worm of thought in my brain. This talk was put on by representatives
of Microsoft and GitHub and discusses whether or not there is a sustainability
problem in open source ( [link](https://fosdem.org/2020/schedule/event/foss_sustainability_issues/) ). The content of the talk,
interpreted within the framework in which it was presented, was moderately
interesting. It was more fascinating to me, however, as a lens for interpreting
GitHub’s (and, indirectly, Microsoft’s) approach to open source, and of the
mindset of developers who approach problems in the same ways.

The presenters drew attention to a few significant crises open-source
communities have faced in recent years — left-pad, in which a trivial
library was removed from npm and was unknowingly present in thousands of
dependency graphs; event-stream, in which a maintainer transferred project
ownership to an unknown individual who added crypto mining; and heartbleed, in
which a bug in a critical security library caused mass upgrades and panic
— and asks whether or not these can be considered sustainability issues.
The talk has a lot to dissect and will frame my thinking and writings for a
while. Today I’ll focus on one specific problem, which I called attention to
during the Q&A.

At a few points, the presenters spoke from the perspective of a business which
depends on up to thousands of open-source libraries or tools. In such a context,
how do you prioritize which of your thousands of dependencies requires
attention, for financial support, contributions upstream, and so on? I found
this worldview dissonant, and asked the following question: “why do you have
thousands of dependencies in the first place?” Because this approach seems to be
fast becoming the norm, this may seem like a stupid question. 2  If any Node
developers are reading, scan through your nearest node_modules directory and see
how many of these dependencies you’ve even heard of.

Such an environment is primed to fail in the ways enumerated by this talk.
Consider the case of the maintainer who lost interest and gave their project to
an untrusted third party. If I had depended on this library, I would have
noticed long ago that the project was effectively unmaintained. It’s likely that
I or my peers would have sent patches to this project, given that bugfixes would
have stopped coming from upstream. We would be aware of the larger risk this
project posed, and have studied alternatives. Earlier than that, I would
probably have lent my ear to the maintainer to vent their frustrations, and
offered my help where possible.

For most of my projects, I can probably list the entire dependency graph,
including transitive dependencies, off of the top of my head. I can name most of
their maintainers, and many of their contributors. I have shaken the hands of
these people, shared drinks and meals with them, and count many of them among my
close friends. The idea of depending on a library I’ve never heard of, several
degrees removed via transitive dependencies, maintained by someone I’ve never
met and have no intention of speaking to, is  *absolutely nuts*  to me. I know of
these problems well in advance because I know the people affected as my friends.
If someone is frustrated or overworked, I’m right there with them trying to find
solutions and correct the over-burden. If someone is in dire financial
straights, I’m helping them touch up their resume and introducing them to
companies that I know are looking for their skillset, or helping them work on
more sustainable sources of donations and grants. They do the same for me, and
for each other.

Quit treating open-source projects like a black box that conveniently solves
your problem. Engage with the human beings who work on it, participate in the
community, and  *make*  it healthy and sustainable. You shouldn’t be surprised
when the 3 AM alarm goes off if the most you see of a project is a line in your
 `package.json` .

1. And strictly speaking I even had to slip in under the radar to attend in the first place — the room was full. ↩︎
2. If so, you may be pleased by a Microsoft’s ridiculous answer: “we have 60,000 developers, that’s why.” ↩︎
