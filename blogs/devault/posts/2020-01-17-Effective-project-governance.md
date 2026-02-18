---
title: "A philosophy of project governance"
date: 2020-01-17
url: https://drewdevault.com/2020/01/17/Effective-project-governance.html
slug: Effective-project-governance
word_count: 940
---

I’ve been in the maintainer role for dozens of projects for a while now, and
have moderated my fair share of conflicts. I’ve also been on the other side,
many times, as a minor contributor watching or participating in conflict within
other projects. Over the years, I’ve developed an approach to project governance
which I believe is lightweight, effective, and inclusive.

I hold the following axioms to be true:

1. Computer projects are organized by humans, creating a social system.
2. Social systems are fundamentally different from computer systems.
3. Objective rules cannot be programmed into a social system.

And the following is true of individuals within those systems:

1. Project leadership is in a position to do anything they want.
2. Project leadership will ultimately do whatever they want, even if they have
to come up with an interpretation of the rules which justifies it.
3. Individual contributors who have a dissonant world-view from project
leadership will never be welcome under those leaders.

Any effective project governance model has to acknowledge these truths. To this
end, the simplest effective project governance model is a BDFL, which scales a
lot further than people might expect.

The BDFL (Benevolent Dictator for Life) is a term which was first used to
describe Python’s governance model with Guido van Rossum at the helm. The “for
life” in BDFL is, in practice, until the “dictator” resigns from their role.
Transfers of power either involve stepping away and letting lesser powers decide
between themselves how to best fill the vacuum, or simply directly appointing a
successor (or successors). In this model, a single entity is in charge —
often the person who started the project, at first — and while they may
delegate their responsibilities, they ultimately have the final say in all
matters.

This decision-making authority derives from the BDFL. Consequently, the
project’s values are a reflection of that BDFL’s values. Conflict resolution and
matters of exclusion or inclusion of specific people from the project is the
direct responsibility of the BDFL. If the BDFL delegates this authority to other
groups or project members, that authority derives from the BDFL and is exercised
at their leisure, on their terms. In practice, for projects of a certain size,
most if not all of the BDFL’s authority is delegated across many people, to the
point where the line between BDFL and core contributor is pretty blurred. The
relationships in the project are built on trust between individuals, not trust
in the system.

As a contributor, you should evaluate the value system of the leadership and
make a personal determination as to whether or not it aligns with your own. If
it does, participate. If it does not, find an alternative or fork the
project. 1

Consider the main competing model: a Code of Conduct as the rule of law.

These attempt to boil subjective matters down into objectively enforcible rules.
Not even in sovereign law do we attempt this. Programmers can easily fall into
the trap of thinking that objective rules can be applied to social systems, and
that they can deal with conflict by executing a script. This is quite untrue,
and attempting to will leave loopholes big enough for bad actors to drive a
truck through.

Additionally, governance models which provide a scripted path onto the decision
making committee can often have this path exploited by bad actors, or by people
for whom the politics are more important than the software. By implementing this
system, the values of the project can easily shift in ways the leaders and
contributors don’t expect or agree with.

The worst case can be that a contributor is ostracized due to the letter of the
CoC, but not the spirit of it. Managing drama is a sensitive, subjective issue,
but objective rules break hearts. Enough of this can burn out the leaders,
creating a bigger power vacuum, without a plan to fill it.

In summary:

**For leaders** : Assume good faith until proven otherwise.

Do what you think is right. If someone is being a
dickhead † ,
tell them to stop.  If they don’t stop, kick them out. Work with contributors
you trust to elevate their role in the project so you can delegate
responsibilities to them and have them act as good role models for the
community. If you’re not good at moderating discussions or conflict resolution,
find someone who is among your trusted advisors and ask them to exercise their
skills.

If you need to, sketch up informal guidelines to give an approximation of your
values, so that contributors know how to act and what to expect, but make it
clear that they’re guidelines rather than rules. Avoid creating complex systems
of governance. Especially avoid setting up systems which create paths that
untrusted people can use to quickly weasel their way into positions of power.
Don’t give power to people who don’t have a stake in the project.

**For contributors** : Assume good faith until proven otherwise.

Do what you think is right. If someone is being a
dickhead † ,
talk to the leadership about it. If you don’t trust the project leadership, the
project isn’t for you, and future conflicts aren’t going to go your way. Be
patient with your maintainers — remember that you have the easier job.

† According to your subjective definition of dickhead.

1. Note that being able to fork is the escape hatch which makes this model fair and applicable to free & open source projects. The lack of a similarly accessible escape hatch in, for example, the governments of soverign countries, prevents this model from generalizing well. ↩︎
