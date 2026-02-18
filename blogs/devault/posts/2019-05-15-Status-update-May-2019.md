---
title: "Status update, May 2019"
date: 2019-05-15
url: https://drewdevault.com/2019/05/15/Status-update-May-2019.html
slug: Status-update-May-2019
word_count: 897
---

This month, it seems the most exciting developments again come from the realm of
email. I’ve got cool email-related news to share for aerc, lists.sr.ht, and
todo.sr.ht, and many cool developments in my other projects to share.

Let’s start with lists.sr.ht: I have broken ground on the web-based patch review
tools! I promised these features when I started working on sourcehut, to make
the email-based workflow more enticing to those who would rather work on the
web. Basically, this gives us a Github or Gerrit-esque review UI for patches
which arrive on the mailing list. Thanks to  [a cool
library](https://git.sr.ht/~emersion/python-emailthreads)  Simon Ser wrote for
me… almost a year ago… I’m able to take a thread of emails discussing a
patch and organically convert them into inline feedback on the web.

This is generated from organic discussions where the participants don’t have to
do anything special to participate - in the discussion this screenshot is
generated from, the participants aren’t even aware that this process is taking
place. This approach allows users who prefer a web-based workflow to interact
with traditional email-based patch review seamlessly. Future improvements will
include detecting new revisions of a patch, side-by-side diff and diffs between
different versions of a patch, and using the web interface to review a patch -
which will generate an email on the list. I’d also like to extend git.sr.ht with
web support for git send-email, allowing you to push to your git repo and send a
patch off to the mailing list from the web. It should also be possible to
combine this with dispatch.sr.ht to have bidirectional code reviews between
mailing lists and Github, Gitlab, etc - with no one on either side being any the
wiser to the preferred workflow of the other.

In other exciting email-related news, aerc2 now supports composing emails -
a feature which has been a long time coming, and was not even present in aerc1!
Check it out:

Outgoing email configuration supports SMTP, STARTTLS, and SMTPS, with sendmail
support planned. Outgoing emails are edited with our embedded terminal emulator
using vim, or your favorite  `$EDITOR` . Still to come: replying to emails & PGP
support. I could use your help here! If you want a chance to write some cool Go
code, stop by the IRC channel and say hello:  [#aerc on
irc.freenode.net](http://webchat.freenode.net/?channels=aerc&uio=d4) . Once aerc
matures a little bit, I also want to start working on a git integration which
will continue making email an even more compelling platform for software
development.

Let’s talk about Wayland next. I’ve been shipping release candidates for sway
1.1 -  [check out the provisional changelog
here](https://github.com/swaywm/sway/issues/3861#issuecomment-487073065) . The
highlights are probably the ability to inhibit idle with arbitrary criteria, and
touch support for swaybar. The release candidates have been pretty quiet - we
might end up shipping this as early as rc4. wlroots 0.6.0 was also released,
though for end-users it doesn’t include much. We’ve removed the long-deprecated
wl_shell, and have made plans to start removing other deprecated protocols. I’ve
also been working with the broader Wayland community on establishing a
governance model for protocol standardization -  [read the latest draft
here](https://lists.freedesktop.org/archives/wayland-devel/2019-May/040532.html) .

I’ve also started working on a Wayland book! It’s intended as a comprehensive
reference on the Wayland protocol, useful for authors hoping to write both
Wayland compositors and Wayland clients. It does not go into all of the
nitty-gritty details necessary for writing a Wayland compositor for Linux (that
is, the sort of knowledge necessary for using wlroots, or even making wlroots
itself), but that’ll be a task for another time. Instead, I focus on the Wayland
protocol itself, explaining how the wire protocol works and the purpose and
usage of each interface in  `wayland.xml` , as well as  `libwayland` . I intend to
sell this book, but when you buy it you’ll receive a DRM-free CC-NC-ND copy that
you can share freely with your friends.

Before I move on from Wayland news, also check out
 [Wio](https://wio-project.org/)  if you haven’t yet - I wrote a blog post about
it  [here](https://drewdevault.com/2019/05/01/Announcing-wio.html) . In short: I
made a novel new Wayland compositor in my spare time which behaves like plan 9’s
Rio.  See the blog post for more details!

Following the success of  [git-send-email.io](https://git-send-email.io) , I
published a similar website last week:  [git-rebase.io](https://git-rebase.io) .
The purpose of this website is to teach readers how to use git rebase,
explaining how to use its primitives to accomplish common high-level tasks in a
way that leaves the reader equipped to apply those primitives to novel
high-level tasks in the course of their work. I hope you find it helpful! I’ve
also secured git-filter-branch.io and git-bisect.io to explain additional
useful, but confusing git commands in the future.

Brief updates for other projects: I’ve been ramping up RISC-V work again,
helping Golang test their port, testing out u-Boot, and working on the Alpine
port some more. cozy has seen only a little progress, but the parser is
improving and it’s now emitting a (very incomplete) AST for source files you
feed to it. Godot is on hold pending additional upstream bandwidth for code
review.

That’s all for today! Thank you so much for your support. It’s pretty clear by
now that my productivity is way higher now that I’m able to work full-time on
open source, thanks to your support. I’ll see you for next month’s update!
