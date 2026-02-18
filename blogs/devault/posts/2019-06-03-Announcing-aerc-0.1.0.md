---
title: "Initial pre-release of aerc: an email client for your terminal"
date: 2019-06-03
url: https://drewdevault.com/2019/06/03/Announcing-aerc-0.1.0.html
slug: Announcing-aerc-0.1.0
word_count: 321
---

After years of painfully slow development, the  [aerc email
client](https://aerc-mail.org)  has seen a huge boost in its pace of development
recently. This leads to today’s announcement:  [aerc 0.1.0 is now
available](https://git.sr.ht/~sircmpwn/aerc/refs/0.1.0) ! After my transition to  [working on free software full
time](https://drewdevault.com/2019/01/15/Im-doing-FOSS-full-time.html)  allowed me to spend more time on more projects, I was able
to invest considerably more time into aerc. Your support led us here: thank you
to all of the people who  [donate to my work](https://drewdevault.com/donate) !

I’ve prepared a short webcast demonstrating aerc’s basic features - give it a
watch if you’re curious about what aerc looks like & what makes it interesting.

In summary, aerc is an email client which runs in your terminal emulator. If
you’re coming from mutt, you’ll appreciate its more efficient & reliable
networking, a keybinding system closer to vims, and embedded terminal emulator
allowing you to compose emails and read new ones at the same time. It builds on
this foundation with a lot of new and exciting features. For example, its
“filter” feature allows us to review patches with syntax highlighting:

The embedded terminal emulator also allows us convenient access to nearby git
repositories for running tests against incoming patches, pushing the changes
once accepted, or anything else you might want to do. Want to run
 [Weechat](https://weechat.org/)  in an aerc tab? Just like that, aerc has a chat
client! Writing emails in vim, manipulating git & hg repositories, playing
nethack to kill some time… all stuff you never realized your email client was
missing.

I plan on extending aerc in the future with more integrations with version
control systems, calendar & contacts support, and more email configurations like
notmuch and JMAP. Please consider
 [contributing](https://git.sr.ht/~sircmpwn/aerc)  if you’re interested in writing
a little Go, or  [donating monthly](https://drewdevault.com/donate)  to ensure I
always have time to work on this and other free software projects. Give aerc a
try and let me know what you think!
