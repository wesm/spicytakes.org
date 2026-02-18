---
title: "Status update, January 2020"
date: 2020-01-15
url: https://drewdevault.com/2020/01/15/Status-update-January-2020.html
slug: Status-update-January-2020
word_count: 616
---

I forgot to write this post this morning, and I’m on cup 3 of coffee while
knee-deep in some arcane work with tarballs in Python. Forgive the brevity of
this introduction. Let’s get right into the status update.

First of all,  [FOSDEM 2020](https://fosdem.org/2020/)  is taking place on February 1st and 2nd, and
I’m planning on being there again this year. I hope to see you there! I’ll be
hosting another  [small session](https://fosdem.org/2020/schedule/event/bof_sourcehut/)  for SourceHut and aerc users
where I’ll take questions, demo some new stuff, and give out stickers.

In Wayland news, the upcoming Sway 1.3 release is getting very close - rc3 is
planned to ship later today. We’ve confirmed that it’ll ship with VNC support
via  [wayvnc](https://github.com/any1/wayvnc)  and improvements to input latency.
I haven’t completed much extra work on Casa (and “Sway Mobile” alongside it),
but there have been some small improvements. I did find some time to work on
 [Sedna](https://git.sr.ht/~sircmpwn/sedna) , however. We’ve decided to use it as
a proving grounds for the new wlroots scene graph API, which plans to
incorporate Simon Ser’s  [libliftoff](https://github.com/emersion/libliftoff)  and put to rest the eternal
debate over how wlroots renderer should take shape. This’ll be  *lots*  of work
but the result will be a remarkably good foundation on which we can run
performant compositors on a huge variety of devices — and, if we’re
lucky, might help resolve the Nvidia problem. I also did a bit more work on the
 [Wayland Book](https://wayland-book.com) , refactoring some of the chapter
ordering to make more sense and getting started with the input chapter. More
soon.

On SourceHut, lots of new developments have been underway. The latest round of
performance improvements for git.sr.ht finally landed with the introduction of
new server hardware, and it’s finally competitive with its peers in terms of
push and web performance. I’ve also overhauled our monitoring infrastructure
 [and made it public](https://metrics.sr.ht) . Our  [Q4 2019 financial
report](https://sourcehut.org/blog/2020-01-13-sourcehut-q4-2019-financial-report/)  was also published earlier this week. I’m currently
working on pushing forward through the self-service data ownership goals, and
we’ve already seen some improvements in that todo.sr.ht can now re-import
tracker exports from itself or other todo.sr.ht instances.

I’ve also been working more on  [himitsu](https://git.sr.ht/~sircmpwn/himitsu) 
recently, though I’m taking it pretty slowly because it’s a security-sensitive
project. Most of the crypto code has been written at this point - writing
encrypted secrets to disk, reading and writing the key index - but reading
encrypted secrets back from the disk remains to be implemented. I know there are
some bugs in the current implementation, which I’ll be sorting out before I
write much more code. I also implemented most of the support code for the Unix
socket RPC, and implemented a couple of basic commands which have been helpful
with proving out the secret store code (proving that it’s wrong, at least).

Simon Ser’s  [mrsh](https://mrsh.sh)  has also been going very well lately, and is
now a nearly complete implementation of the POSIX shell. I’ve started working on
something I’ve long planned to build on top of mrsh: a comfortable interactive
shell, inspired by fish’s interactive mode, but with a strictly POSIX syntax. I
call the project  [imrsh](https://git.sr.ht/~sircmpwn/imrsh) , for interactive
mrsh. I’ve already got it in somewhat good shape, but many of the features
remain to be implemented. The bulk of the work was in Simon’s mrsh, so it
shouldn’t be too hard to add a pretty interface on top. We’ll see how it goes.

That’s all for today. In the coming month I hope to expand on each of these, and
I’m also working on a new Secret Project which may start bearing fruits soon
(but likely not). Thank you for your continued support! I’ll see you at FOSDEM.
