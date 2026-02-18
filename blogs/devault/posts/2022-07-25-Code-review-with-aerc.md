---
title: "Code review at the speed of email"
date: 2022-07-25
url: https://drewdevault.com/2022/07/25/Code-review-with-aerc.html
slug: Code-review-with-aerc
word_count: 1015
---

I’m a big proponent of the email workflow for patch submission and code review.
I have previously published some content ( [How to use git.sr.ht’s send-email
feature](https://spacepub.space/w/no6jnhHeUrt2E5ST168tRL) ,  [Forks & pull requests vs email](https://spacepub.space/w/3JhBcvEYbminv8ji4k84gx) ,  [git-send-email.io](https://git-send-email.io) ) which
demonstrates the contributor side of this workflow, but it’s nice to illustrate
the advantages of the maintainer workflow as well. For this purpose, I’ve
recorded a short video demonstrating how I manage code review as an
email-oriented maintainer.

*Disclaimer: I am the founder of [SourceHut](https://sourcehut.org), a platform built on this
workflow which competes with platforms like GitHub and GitLab. This article’s
perspective is biased.*

*
  This blog post provides additional material to supplement this video, and also
  includes all of the information from the video itself. For those who prefer
  reading over watching, you can just stick to reading this blog post. Or, you
  can watch the video and skim the post. Or you can just do something else! When
  was the last time you called your grandmother?
  *

With hundreds of hours of review experience on GitHub, GitLab, and SourceHut, I
can say with confidence the email workflow allows me to work much faster than
any of the others. I can review small patches in seconds, work quickly with
multiple git repositories, easily test changes and make tweaks as necessary,
rebase often, and quickly chop up and provide feedback for larger patches.
Working my way through a 50-email patch queue usually takes me about 20 minutes,
compared to an hour or more for the same number of merge requests.

This workflow also works entirely offline. I can read and apply changes locally,
and even reply with feedback or to thank contributors for their patch. My mail
setup automatically downloads mail from IMAP using  [isync](https://isync.sourceforge.io/)  and outgoing mails
are queued with  [postfix](http://www.postfix.org/)  until the network is ready. I have often worked
through my patch queue on an airplane or a train with spotty or non-functional
internet access without skipping a beat. Working from low-end devices like a
Pinebook or a phone are also no problem — aerc is very lightweight in the
terminal and the SourceHut web interface is  [much lighter & faster](https://forgeperf.org)  than any
other web forge.

The centerpiece of my setup is an email client I wrote specifically for software
development using this workflow:  [aerc](https://aerc-mail.org/) . 1  The stock configuration of aerc
is pretty good, but I make a couple of useful additions specifically for
development on SourceHut. Specifically, I add a few keybindings to
 `~/.config/aerc/binds.conf` :

```
[messages]
ga = :flag<Enter>:pipe -mb git am -3<Enter>
gp = :term git push<Enter>
gl = :term git log<Enter>

rt = :reply -a -Tthanks<Enter>
Rt = :reply -qa -Tquoted_thanks<Enter>

[compose::review]
V = :header -f X-Sourcehut-Patchset-Update NEEDS_REVISION<Enter>
A = :header -f X-Sourcehut-Patchset-Update APPLIED<Enter>
R = :header -f X-Sourcehut-Patchset-Update REJECTED<Enter>
```

The first three commands, ga, gp, and gl, are for invoking git commands. “ga”
applies the current email as a patch, using  [git am](https://git-scm.com/docs/git-am) , and “gp” simply runs
git push. “gl” is useful for quickly reviewing the git log. ga also flags the
email so that it shows up in the UI as having been applied, which is useful as
I’m jumping all over a patch queue. I also make liberal use of \ (:filter) to
filter my messages to patches applicable to specific projects or goals.

rt and Rt use aerc templates installed at  `~/.config/aerc/templates/`  to reply
to emails after I’ve finished reviewing them. The “thanks” template is:

```
X-Sourcehut-Patchset-Update: APPLIED

Thanks!

{{exec "{ git remote get-url --push origin; git reflog -2 origin/master --pretty=format:%h | xargs printf '%s\n' | tac; } | xargs printf 'To %s\n   %s..%s  master -> master'" ""}}
```

And quoted_thanks is:

```
X-Sourcehut-Patchset-Update: APPLIED

Thanks!

{{exec "{ git remote get-url --push origin; git reflog -2 origin/master --pretty=format:%h | xargs printf '%s\n' | tac; } | xargs printf 'To %s\n   %s..%s  master -> master'" ""}}

On {{dateFormat (.OriginalDate | toLocal) "Mon Jan 2, 2006 at 3:04 PM MST"}}, {{(index .OriginalFrom 0).Name}} wrote:
{{wrapText .OriginalText 72 | quote}}
```

Both of these add a magic “X-Sourcehut-Patchset-Update” header, which updates
the status of the patch on the mailing list. They also include a shell pipeline
which adds some information about the last push from this repository, to help
the recipient understand what happened to their patch. I often make some small
edits to request the user follow-up with a ticket for some future work, or add
other timely comments. The second template, quoted_reply, is also particularly
useful for this: it quotes the original message so I can reply to specific parts
of it, in the commit message, timely commentary, or the code itself, often
pointing out parts of the code that I made some small tweaks to before applying.

And that’s basically it! You can browse all of my dotfiles  [here](https://git.sr.ht/~sircmpwn/dotfiles)  to see more
details about my system configuration. With this setup I am able to work my way
through a patch queue easier and faster than ever before. That’s why I like the
email workflow so much: for power users, no alternative is even close in terms
of efficiency.

Of course, this is the power user workflow, and it can be intimidating to learn
all of these things. This is why we offer more novice-friendly tools, which lose
some of the advantages but are often more intuitive. For instance, we are
working on user interface on the web for patch review, mirroring our existing
 [web interface for patch submission](https://spacepub.space/w/no6jnhHeUrt2E5ST168tRL) . But, in my opinion, it doesn’t get
better than this for serious FOSS maintainers.

Feel free to reach out on IRC in #sr.ht.watercooler on Libera Chat, or  [via
email](mailto:sir@cmpwn.com) , if you have any questions about this workflow and
how you can apply it to your own projects. Happy hacking!

1. Don’t want to switch from your current mail client? Tip: You can use more than one 🙂 I usually fire up multiple aerc instances in any case, one “main” instance and more ephemeral processes for working in specific projects. The startup time is essentially negligible, so this solution is very cheap and versatile. ↩︎
