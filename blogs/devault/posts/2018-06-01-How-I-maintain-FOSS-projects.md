---
title: "How I maintain FOSS projects"
date: 2018-06-01
url: https://drewdevault.com/2018/06/01/How-I-maintain-FOSS-projects.html
slug: How-I-maintain-FOSS-projects
word_count: 1318
---

Today’s is another blog post which has been on my to-write list for a while. I
have hesitated a bit to write about this, because I’m certain that my approach
isn’t perfect. I think it’s pretty good, though, and people who work with me in
FOSS agreed after a quick survey. So! Let’s at least put it out there and
discuss it.

There are a few central principles I use to guide my maintainership work:

1. Everyone is a volunteer and should be treated as such.
2. One patch is worth a thousand bug reports.
3. Empower people to do what they enjoy and are good at.

The first point is very important. My open source projects are not the work of a
profitable organization which publishes open source software as a means of
giving back. Each of these projects is built and maintained entirely by
volunteers. Acknowledging this is important for keeping people interested in
working on the project - you can never expect someone to volunteer for work they
aren’t enjoying 1 . I am always grateful for any level of involvement a person
wants to have in the project.

Because everyone is a volunteer, I encourage people to work on their own
agendas, on their own schedule and at their own pace. None of our projects are
in a hurry, so if someone is starting to get burnt out, they should have no
reservations about taking a break for as long as they wish. I’d rather have
something done slowly, correctly, and by a contributor who is enjoying their
work than quickly and by a contributor who is burnt out and stressed. No one
should ever be stressed out because of their involvement in the project. Some of
it is unavoidable - especially where politics is involved - but I don’t hold
grudges against anyone who steps away and I try to shoulder the brunt of the
bullshit myself.

The second principle is closely related to the first. If a bug does not affect
someone who works on the project and the problem doesn’t interest anyone who
works on the project, it’s probably not going to get fixed. I would much rather
help someone familiarize themselves with the codebase and tooling necessary for
them to solve their own problems and send a patch, even if it takes ten times
longer than fixing the bug myself. I have never found a user who, even if they
aren’t comfortable with programming or the specific technologies in use, has
been unable to solve a problem which they were willing to invest time into and
ask questions about.

This principle often leads to conflict with users whose bugs don’t get fixed,
but I stick to it. I would rather lose every user who is unwilling to attempt a
patch than invest the resources of my contributors into work they’re
uninterested in. In the long term, the health of the project is far better if I
always have developers engaged in and enjoying their work on it than if I lose
users who are upset by my approach.

These first two principles don’t affect my day-to-day open source work so much
as they set the tone for it. The third principle, however, constitutes most of
my job as a maintainer, and it’s with it that I add the most value. My main role
is to empower people who contribute to do work they enjoy, which benefits the
project, and which keeps them interested in coming back to do more.

Finding things people enjoy working on is the main task in this role. Once
people have made a few contributions, I can get an idea of how they like to work
and what they’re good at, and help them find things to do which play to their
strengths. Supporting a contributors potential is important as well, and if
someone expresses interest in certain kinds of work or I think they show promise
in an area, it’s my responsibility to help them find work to nurture these
skills and connect them with good mentors to help.

This starts to play in another major responsibility I have as a maintainer,
which is facilitating effective communication throughout the project. As people
grow in the project they generally become effective at managing communication
themselves, but new contributors appear all the time. A major responsibility as
a maintainer is connecting new contributors to domain experts in a problem, or
to users who can reproduce problems or are willing to test their patches.

I’m also responsible for keeping up with each contributor’s growth in the
project. For those who are good at and enjoy having responsibility in the
project, I try to help them find it. As contributors gain a better understanding
of the code, they’re trusted to handle large features with less handholding and
perform more complex work 2 . Often contributors are given opportunities to
become better code reviewers, and usually get merge rights once they’re good at
it. Things like commit access are a never a function of rank or status, but of
enabling people to do the things that they’re good at.

It’s also useful to remember that your projects are not the only game in town. I
frequently encourage people who contribute to contribute to other projects as
well, and I personally try to find ways to contribute back to their own projects
(though not as much as I’d often like to). I offer support as a sysadmin to many
projects started by contributors to my projects and I send patches whenever I
can. This pays directly back to the project in the form of contributors with
deeper and more diverse experience. It’s also fun to take a break from working
on the same stuff all the time!

There’s also some work that someone’s just gotta do, and that someone is usually
me. I have to be a sysadmin for the websites, build infrastructure, and so on.
If there are finances, I have to manage them. I provide some kind of vision for
the project and decide what work is in scope. There’s also some boring stuff
like preparing changelogs and release notes and shipping new versions, or
liaising with distros on packages. I also end up being responsible for any
marketing.

Getting and supporting contributors is the single most important thing you can
do for your project as a maintainer. I often get asked how I’m as productive as
I seem to be. While I can’t deny that I can write a lot of code, it’s peanuts
compared to the impact made by other contributors. I get a lot of credit for
sway, but in reality I’ve only written 1-3 sway commits per week in the past few
months. For this reason, the best approach focuses on the contributors, to whom
I owe a great debt of gratitude.

I’m still learning, too! I speak to contributors about my approach from time to
time and ask for feedback, and I definitely make mistakes. I hope that I’ll
receive more feedback soon after some of them read this blog post, too. My
approach will continue to grow over time (hopefully for the better) and I hope
our work will enjoy success as a result.

1. Some people do work they don’t enjoy out of gratitude to the project, but this is not sustainable and I discourage it. ↩︎
2. Though I always encourage people to work on the things they’re interested in, I sometimes have to *discourage* people from biting off more than they can chew. Then I help them gradually ramp up their skills and trust among the team until they can take on those tasks. Usually this goes pretty quick, though, and a couple of bugs caused by inexperience is a small price to pay for the *gain* in experience the contributor gets by taking on hard or important tasks. ↩︎
