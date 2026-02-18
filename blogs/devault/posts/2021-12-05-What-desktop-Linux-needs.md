---
title: "What desktop Linux needs to succeed in the mainstream"
date: 2021-12-05
url: https://drewdevault.com/2021/12/05/What-desktop-Linux-needs.html
slug: What-desktop-Linux-needs
word_count: 1424
---

The  [Linus Tech Tips](https://redirect.invidious.io/channel/UCXuqSBlHAE6Xw-yeJA0Tunw)  YouTube channel has been putting out a series of videos
called the  [Switching to Linux Challenge](https://redirect.invidious.io/playlist?list=PL8mG-RkN2uTyhe6fxWpnsHv53Y1I-K3yu)  that has been causing a bit of a stir
in the Linux community. I’ve been keeping an eye on these developments, and
thought it was a good time to weigh in with my thoughts. This article focuses on
what Linux needs to do better — I have also written a companion article,
“ [How new Linux users can increase their odds of success](/2021/12/05/How-new-Linux-users-succeed.html) ”, which looks at the
other side of the problem.

Linux is  *not*  accessible to the average user today, and I didn’t need to watch
these videos to understand that. I do not think that it is reasonable today to
expect a non-expert user to successfully install and use Linux for their daily
needs without a “Linux friend” holding their hand every step of the way.

This is not a problem unless we want it to be. It is entirely valid to build
software which is accommodating of experts only, and in fact this is the kind of
software I focus on in my own work. I occasionally use the racecar analogy: you
would not expect the average driver to be able to drive a Formula 1 racecar.
It is silly to suggest that Formula 1 vehicle designs ought to accommodate
non-expert drivers, or that professional racecar drivers should be driving
mini-vans on the circuit. However, it is equally silly to design a professional
racing vehicle and market it to soccer moms.

I am one of the original developers of the  [Sway](https://swaywm.org)  desktop environment for
Linux. I am very proud of Sway, and I believe that it represents one of the
best desktop experiences on Linux. It is a rock-solid, high-performance,
extremely stable desktop which is polished on a level that is competitive with
commercial products. However, it is designed for  *me* : a professional,
expert-level Linux user. I am under no illusions that it is suitable for my
grandmother. 1

This scenario is what the incentives of the Linux ecosystem favors most. Linux
is one of  *the best*  operating systems for professional programmers and
sysadmins, to such an extraordinary degree that most programmers I know treat
Windows programmers and sysadmins as the object of well-deserved ridicule. Using
Windows for programming or production servers is essentially as if the race car
driver from my earlier metaphor  *did*  bring a mini-van to the race track. Linux
is the operating system developed by programmers, for programmers, to suit  *our* 
needs, and we have succeeded tremendously in this respect.

However, we have failed to build an operating system for people who are  *not* 
like us.

If this is not our goal, then that’s fine. But, we can build things for
non-experts if we choose to. If we set “accessible to the average user” as a
goal, then we must take certain steps to achieve it. We need to make major
improvements in the following areas: robustness, intuitiveness, and community.

The most frustrating moments for a user is when the software they’re using does
something inexplicable, and it’s these moments that they will remember the most
vividly as part of their experience. Many Linux desktop and distribution
projects are spending their time on shiny new features, re-skins, and expanding
their scope further and further. This is a fool’s errand when the project is not
reliable at its current scope. A small, intuitive, reliable program is better
than a large, unintuitive, unreliable program. Put down the paint brush and pick
up the polishing stone. I’m looking at you, KDE. 2

A user-friendly Linux desktop system should not crash. It should not be possible
to install a package which yeets gnome-desktop and dumps them into a getty. The
smallest of interactions must be intuitive and reliable, so that when Linus
drags files from the decompression utility into a directory in Dolphin, it does
the right thing. This will require a greater degree of cooperation and unity
between desktop projects. Unrelated projects with common goals need to be
reaching out to one another and developing robust standards for achieving those
goals. I’m looking at you, Gnome.

Linux is a box of loosely-related tools held together with staples and glue.
This is fine when the user understands the tools and is holding the glue bottle,
but we need to make a more cohesive, robust, and reliable system out of this
before it can accommodate average end-users.

We also have a lot of work to do in the Linux community. The discussion on the
LTT video series has been exceptionally toxic and downright embarrassing. There
is a major problem of elitism within the Linux community. Given a hundred ways
of doing things on Linux (✓), there will be 99 assholes ready to tell you that
your way sucks (✓). Every Linux user is responsible for doing better in this
regard, especially the moderators of Linux-adjacent online spaces. Wouldn’t it
be better if we took pride in being a friendly, accessible community? Don’t
flame the noobs.

Don’t flame the experts, either. When Pop!_OS removed gnome-desktop upon
installing Steam, the Linux community rightly criticised them for it. This was a
major failure mode of the system in one of its flagship features, and should
have never shipped. It illuminates systemic failures in the areas I have drawn
our attention to in this article such as robustness and intuitiveness, and
Pop!_OS is responsible for addressing the problem. None of that excuses the
toxic garbage which was shoveled into the inboxes of Pop!_OS developers and
users. Be better people.

Beyond the toxicity, there are further issues with the Linux community. There
are heaps and heaps of blogs shoveling out crappy non-solutions to problems
noobs might be Googling, most of which will fuck up their Linux system in some
way or another. It’s very easy to find bad advice for Linux, and very hard to
find good advice for Linux. The blog spammers need to cut it out, and we need to
provide better, more accessible resources for users to figure out their issues.
End-user-focused Linux distributions need to take responsibility for making
certain that their users understand the best ways to get help for any issues
they run into, so they don’t go running off to the Arch Linux forums blindly
running terminal commands which will break their Ubuntu installation.

End-user software also needs to improve in this respect. In the latest LTT
video, Luke wanted to install OBS, and the right thing to do was install it from
their package manager. However,  [the OBS website](https://obsproject.com/download)  walks them through
installing a PPA instead, and has a big blue button for building it from source,
which is definitely not what an average end-user should be doing.

→ Related:  [Developers: Let distros do their job](/2021/09/27/Let-distros-do-their-job.html)

One thing that we do not need to do is “be more like Windows”, or any other OS.
I think that this is a common fallacy found in end-user Linux software. We
should develop a system which is intuitive in its own right without having to
crimp off of Windows. Let’s focus on what makes Linux interesting and useful,
and try to build a robust, reliable system which makes those interesting and
useful traits accessible to users. Chasing after whatever Windows does is not
the right thing to do. Let’s be prepared to ask users to learn things like new
usability paradigms if it illuminates a better way of doing things.

So, these are the goals. How do we achieve them?

I reckon that we could use a commercial, general-purpose end-user Linux distro.
As I mentioned earlier, the model of developers hacking in their spare time to
make systems for themselves does not create incentives which favor the average
end-user. You can sell free software — someone ought to do so! Build a
commercial Linux distro, charge $20 to download it or mail an install CD to the
user, and invest that money in developing a better system and offer dedicated
support resources. Sure, it’s  *nice*  that Linux is free-as-in-beer, but there’s
no reason it has to be. I’ve got  [my own business](https://sourcehut.org)  to run, so I’ll
leave that as  [an exercise for the reader](https://stripe.com/atlas) . Good luck!

1. However, I suspect that the LTT folks and other “gaming power-user” types would find Sway very interesting, if they approached it with a sufficiently open-minded attitude. For details, see the companion article. ↩︎
2. There is at least one person at KDE working along these lines: [Nate Graham](https://pointieststick.com). Keep it up! ↩︎
