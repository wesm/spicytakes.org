---
title: "Prefer Design Skills"
description: "Imagine a hiring situation. There's two candidates both with a few years of experience. In the blue corner we have someone with good broad design skills in the style of design that you favor (in my ca"
date: 2008-01-17T00:00:00
tags: ["team organization", "recruiting", "technical leadership", "thoughtworks"]
url: https://martinfowler.com/bliki/PreferDesignSkills.html
slug: PreferDesignSkills
word_count: 1156
---


Imagine a hiring situation. There's two candidates both with a few
years of experience. In the blue corner we have someone with good
broad design skills in the style of design that you favor (in my case
that would be things like DRY, judicious use of patterns, TDD,
communicative code etc, but the actual list isn't important - just
that it's what you favor). However she knows nothing of the particular
platform technology that you're using. In the red corner we have
someone who has little knowledge (or interest) in those issues, but
knows your platform really well - edge cases in the language, what
libraries are available, fingers move naturally over the
tools. Assume all else about them is equal (which it never is except for
thought experiments like this) and that your team doesn't have any
gaping holes that this candidate might fill. Which one would you
prefer?


My answer is simple, I'd take the one in the with broad design
skills. I've always held the view that a good programmer should be
able to pick up a new platform relatively quickly. Learning basic
design aesthetics is both harder and carries over better to new
platforms. Good design practices that matter in Java are equally
valuable in .NET. Not being familiar with the platform does slow you
down (how do I get a literal class name in C# again?), but producing
well designed code is what really makes a difference.


Broad design skills aren't completely portable. Java and .NET are
mostly equivalent as languages - moving to Ruby, however, changes
more. Moving to a significantly different beast, like functional
languages, is a bigger shift. In any case, you can't just blindly
replicate all design habits in a new environment. But if you're aware
of the new world, an awful lot does carry over.


We've seen this principle prove itself at Thoughtworks. In our
early days with Java, we found the skills experienced developers had
learned in Forte gave us excellent instincts for working with Java. We
moved away early from the EJB-dominant thinking, and I think it was
experience with other platforms that guided us. We saw it even more
strongly with .NET. Time and again we saw that good developers with a
Java background were rapidly more effective than those with a longer
.NET or Microsoft background who lacked those skills. The difference
was visible in weeks, not months (and sometimes days).


At the moment we see this shift most notably in Ruby. We've had
quite the run of Ruby projects this year, and often we turn to people
with long experience in curly-brace languages to fill the need. Again
we've seen the value that broad design skills gives us.


It's not always a sure thing. I have seen cases where someone
experienced in another platform just doesn't desire to get in and
learn the new one. Desire to learn is a necessary component here - I'd take
the single platform specialist if he wanted to learn broad design and
the broad designer didn't want to learn the new platform. It's also
essential to have someone on the team who knows the platform well.


I'd say most people at Thoughtworks prefer design skills over
platform knowledge. Many clients don't share that point of view -
which can lead to some difficult pragmatic and ethical choices.


What happens if you have someone you want to bring onto the team
with strong design skills and no platform background - yet the client
insists on at least two years experience on the platform. In your
professional judgment, the broad candidate is going to be more
productive than anyone else available. You need to be honest with your
client, but on the other hand he is paying you for your professional
judgment. Does this change if the client has given you responsibility
for delivery of the project?


For us these questions are more charged because there is a
financial interest involved. If we add a ThoughtWorker to a team, then
we bill for that person. If a client hires a platform specialist
contractor, we don't get that income. For many people this is a
crucial fact in the situation, yet I expect our project managers are
wise enough to know that the risk of adding the wrong person is much
more important than one billable income.


Consider another case where you're open with the client and the
client demands a reduced rate for the broad design person due to her
lack of platform knowledge as she'll be learning on the job. You're
sure that she, despite that lack, will be more productive than the
competing platform expert due to those design skills. Should you
accept a reduced rate?


It's the nature of our, and most other, professions that
you learn on the job. A platform specialist also has to learn broad
design skills if he's going to produce maintainable code. Here
it's important to remember that not just is it usually harder to learn
design than platforms, it's also less certain. Given a motivated
broad-designer, I can be pretty sure she'll pick up a platform in
time. But there's no guarantee the other way around. Some people are
good at learning details of a platform, but never figure out how to
write clear code.


I've talked here about broad design skills - and I do believe this
makes a difference on the technical axis. But there are other
dimensions of broadness too. Most risk in software projects lies in
the communication between businesspeople and programmers, so a
candidate who can communicate well with users brings a great deal to a
team.


A similar issue is knowledge of the problem domain. Often clients
want people who already know their business, yet are surprised when
someone rapidly gains enough understanding to be useful. I've long
held that it's the ability to collaborate with others which is central
here. By collaborating with a domain expert, or a platform expert,
someone with broad skills can be become effective very
quickly. Knowledge of other domains often introduces surprising
insights into a project and similarities often crop up in sup-rising
places. It's remarkable how often things like core accounting patterns
crop up in places that don't look like accounting on the surface. In
the end it's the ability to work with others, coupled with being a
fast learner, that is the critical skill.


I'm not dismissing deep platform knowledge here. In an ideal world
every team member would be excellent broad programmers with several
years platform experience, good familiarity with the problem domain,
and written similar systems at least twice before. But we all know how
far our world is from that ideal. You need some platform knowledge on
a team, and if it were a gap I would reach for the platform
specialist to fill it. But that doesn't alter my default position to
prefer broad design skills most of the time.
