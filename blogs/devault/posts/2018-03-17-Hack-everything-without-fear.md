---
title: "Hack everything without fear"
date: 2018-03-17
url: https://drewdevault.com/2018/03/17/Hack-everything-without-fear.html
slug: Hack-everything-without-fear
word_count: 599
---

We live in a golden age of open source, and it can sometimes be easy to forget
the privileges that this affords us. I’m writing this article with vim, in a
terminal emulator called urxvt, listening to music with mpv, in a Sway desktop
session, on the Linux kernel. Supporting this are libraries like glibc or musl,
harfbuzz, and mesa. I also have the support of the AMDGPU video driver, libinput
and udev, alsa and pulseaudio.

All of this is open source. I can be reading the code for any of these tools
within 30 seconds, and for many of these tools I already have their code checked
out somewhere on my filesystem. It gets even better, though: these projects
don’t just make their code available - they accept patches, too! Why wouldn’t we
take advantage of this tremendous opportunity?

I often meet people who are willing to contribute to one project, but not
another. Some people will shut down when they’re faced with a problem that
requires them to dig into territory that they’re unfamiliar with. In Sway, for
example, it’s often places like libinput or mesa. These tools might seem foreign
and scary - but to these people, at some point, so did Sway. In reality these
codebases are quite accessible.

Getting around in an unfamiliar repository can be a little intimidating, but do
it enough times and it’ll become second nature. The same tools like gdb work
just as well on them. If you have a stacktrace for a segfault originating in
libinput, compile libinput with symbols and gdb will show you the file name and
line number of the problem. Go there and read the code! Learn how to use tools
like  `git grep`  to find stuff. Run  `git blame`  to see who wrote a confusing line
of code, and send them an email! When you find the problem, don’t be afraid to
send a patch over instead of working around it in your own code. This is
something every programmer should be comfortable doing often.

Even when the leads you’re chasing down are written in unfamiliar programming
languages or utilize even more unfamiliar libraries, don’t despair. All
programming languages have a lot in common and huge numbers of resources are
available online. Learning just enough to understand (and fix!) a particular
problem is very possible, and something I find myself doing it all the time. You
don’t have to be an expert in a particular programming language to invoke trial
& error.

If you’re similarly worried about the time investment, don’t be. You already set
aside time to work your problem, and this is just part of that process. Yes,
you’ll probably be spending your time differently from your expectations - more
reading code than writing code.  But how is that any less productive? The
biggest time sink in this process is all the time you spend worrying about how
much time it’s going to take, or telling me in IRC you can’t solve your problem
because you’re not good enough to understand mesa or the kernel or whatever.

An important pastime of the effective programmer is reading and understanding
the tools you use. You should at least have a basic idea of how everything on
your system works, and in the places your knowledge is lacking you should make
it your business to study up. The more you do this, the less scary foreign code
will become, and the more productive you will be. No longer will you be stuck in
your tracks because your problem leads you away from the beaten path!
