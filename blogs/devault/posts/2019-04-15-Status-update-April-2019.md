---
title: "Status update, April 2019"
date: 2019-04-15
url: https://drewdevault.com/2019/04/15/Status-update-April-2019.html
slug: Status-update-April-2019
word_count: 696
---

Spring is here, and I’m already miserable in the heat. Crazy weather here in
Philadelphia - I was woken up at 3 AM by my phone buzzing, telling me to take
immediate shelter from a tornado. But with my A/C cranked up and the tornado
safely passed, I’ve been able to get a lot of work done.

The project with the most impressive progress is
 [aerc2](https://git.sr.ht/~sircmpwn/aerc2) . It can now read emails, including
filtering them through arbitrary commands for highlighting diffs or coloring
quotes, or even rendering HTML email with a TUI browser like w3m.

Here’s another demo focusing on the embedded terminal emulator which makes this
possible:

Keybindings are also working, which are configured simiarly to vim - each
keybinding simulates a series of keystrokes, which all eventually boil down to
an ex-style command. I’ve bought a domain for aerc, and I’ll be populating it
with some marketing content and a nice tour of the features soon. I hope to have
time to work on sending emails this month as well. In the immediate future, I
need to fix some crashiness that occurs in some situations.

In other email-related news,  [git-send-email.io](https://git-send-email.io)  is
now live, an interactive tutorial on using email with git. This workflow is the
one sourcehut focuses on, and is also used by a large number of important free
software projects, like Linux, gcc, clang, glibc, musl, ffmpeg, vim, emacs,
coreutils… and many, many more. Check it out!

I also spent a fair bit of time working on lists.sr.ht this month. Alpine Linux
has provisioned some infrastructure for a likely migration from their current
mailing list solution (mlmmj+hypermail) to one based on lists.sr.ht, which I
deployed a lists.sr.ht instance to for them, and trained them on some
administrative aspects of lists.sr.ht. User-facing improvments that came from
this work include tools for importing and exporting mail spools from lists,
better access controls, moderation tools, and per-list mime whitelisting and
blacklisting. Admin-facing tools include support for a wider variety of MTA
configurations and redirects to continue supporting old incoming mail addresses
when migrating from another mailing list system.

Stepping outside the realm of email, let’s talk about Wayland. Since Sway 1.0,
development has continued at a modest pace, fixing a variety of small bugs and
further improving i3 compatibility. We’re getting ready to split swaybg into a
standalone project which can be used on other Wayland compositors soon, too. I
also have been working more on Godot, and have switched gears towards adding a
Wayland backend to Godot upstream - so you can play Godot-based video games on
Wayland. I’m still working with upstream and some other interested contributors
on the best way to integrate these changes upstream, but I more or less
completed a working port with support for nearly all of Godot’s platform
abstractions.

In smaller project news, I spent an afternoon putting together a home-grown
video livestreaming platform a few weeks ago. The result:
 [live.drewdevault.com](https://live.drewdevault.com) . Once upon a time I was
livestreaming programming sessions on Twitch.tv, and in the future I’d like to
do this more often on my new platform. This one is open source and built on the
shoulders of free software tools. I announce new streams on
 [Mastodon](https://cmpwn.com/@sir) , join us for the next one!

I’m also starting on another project called cozy, which is yak-shaving for
several other projects I have in mind. It’s kind of ambitious… it’s a full
end-to-end C compiler toolchain. One of my goals (which, when completed, can
unblock other tasks before cozy as a whole is done) is to make the parser work
as a standalone library for reading, writing, and maniuplating the C AST. I’ve
completed the lexer and basic yacc grammar, and I’m working on extracting an AST
from the parser. I only started this weekend, so it’s pretty early on.

I’ll leave you with a fun weekend project I did shortly after the last update:
 [otaqlock](https://qlock.drewdevault.com/) . The server this runs on isn’t awash
with bandwidth and the site doesn’t work great on mobile - so your milage may
vary - but it is a cool artsy restoration project nonetheless. Until next time,
and thank you for your support!
