---
title: "What's new with Himitsu 0.9?"
date: 2025-08-08
url: https://drewdevault.com/2025/08/08/2025-08-08-Whats-new-with-himitsu.html
slug: 2025-08-08-Whats-new-with-himitsu
word_count: 881
---

Last week, Armin and I worked together on the latest release of  [Himitsu](https://himitsustore.org/) , a
“secret storage manager” for Linux. I haven’t blogged about Himitsu since I
announced it  [three years ago](/2022/06/20/Himitsu.html) , and I thought it would be nice to give you a
closer look at the latest release, both for users eager to see the latest
features and for those who haven’t been following along. 1

*A brief introduction: Himitsu is like a password manager, but more general: it
stores any kind of secret in its database, including passwords but also SSH
keys, credit card numbers, your full disk encryption key, answers to those
annoying “security questions” your bank obliged you to fill in, and so on. It
can also enrich your secrets with arbitrary metadata, so instead of just
storing, say, your IMAP password, it can also store the host, port, TLS
configuration, and username, storing the complete information necessary to
establish an IMAP session.*

*Another important detail: Himitsu is written in Hare and depends on Hare’s
native implementations of cryptographic primitives – neither Himitsu nor the
cryptography implementation it depends on have been independently audited.*

So, what new and exciting features does Himitsu 0.9 bring to the table? Let me
summarize the highlights for you.

## A new prompter

The face of Himitsu is the prompter. The core Himitsu daemon has no user
interface and only communicates with the outside world through its IPC
protocols. One of those protocols is the “prompter”, which Himitsu uses to
communicate with the user, to ask you for consent to use your secret keys, to
enter the master password, and so on. The prompter is decoupled from the daemon
so that it is easy to substitute with different versions which accommodate
different use-cases, for example by integrating the prompter more deeply into a
desktop environment or to build one that fits better on a touch screen UI like a
phone.

But, in practice, given Himitsu’s still-narrow adoption, most people use the
GTK+ prompter developed upstream. Until recently, the prompter was written in
Python for GTK+ 3, and it was a bit janky and stale. The new  [hiprompt-gtk](https://git.sr.ht/~sircmpwn/hiprompt-gtk) 
changes that, replacing it with a new GTK4 prompter implemented in Hare.

I’m excited to share this one with you – it was personally my main contribution
to this release. The prompter is based on Alexey Yerin’s  [hare-gi](https://git.sr.ht/~yerinalexey/hare-gi) , which is a
(currently only prototype-quality) code generator which processes GObject
Introspection documents into Hare modules that bind to libraries like GTK+. The
prompter uses  [Adwaita](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/)  for its aesthetic and controls and  [GTK layer shell](https://github.com/wmww/gtk4-layer-shell)  for
smoother integration on supported Wayland compositors like Sway.

## Secret service integration

Armin has been hard at work on a new package,  [himitsu-secret-service](https://git.sr.ht/~apreiml/himitsu-secret-service) , which
provides the long-awaited support for integrating Himitsu with the dbus Secret
Service API used by many Linux applications to manage secret keys. This makes it
possible for Himitsu to be used as a secure replacement for, say, gnome-keyring.

## Editing secret keys

Prior to this release, the only way to edit a secret key was to remove it and
re-add it with the desired edits applied manually. This was a tedious and
error-prone process, especially when bulk-editing keys. This release includes
some work from Armin to improve the process, by adding a “change” request to the
IPC protocol and implementing it in the command line hiq client.

For example, if you changed your email address, you could update all of your
logins like so:

```
$ hiq -c email=newemail@example.org email=oldemail@example.org
```

Don’t worry about typos or mistakes – the new prompter will give you a summary
of the changes for your approval before the changes are applied.

You can also do more complex edits with the -e flag – check out the hiq(1) man
page for details.

## Secret reuse notifications

Since version 0.8, Himitsu has supported “remembering” your choice, for
supported clients, to consent to the use of your secrets. This allows you, for
example, to remember that you agreed for the  [SSH agent](https://git.sr.ht/~sircmpwn/himitsu-ssh)  to use your SSH keys
for an hour, or for the duration or your login session, etc. Version 0.9 adds a
minor improvement to this feature – you can add a command to himitsu.ini, such
as notify-send, which will be executed whenever a client takes advantage of this
“remembered” consent, so that you can be notified whenever your secrets are used
again, ensuring that any unexpected use of your secrets will get your attention.

## himitsu-firefox improvements

There are also some minor improvements landed for  [himitsu-firefox](https://git.sr.ht/~sircmpwn/himitsu-firefox)  that I’d
like to note. tiosgz sent us a nice patch which makes the identification of
login fields in forms more reliable – thanks! And I’ve added a couple of useful
programs, himitsu-firefox-import and himitsu-firefox-export, which will help you
move logins between Himitsu and Firefox’s native password manager, should that
be useful to you.

## And the rest

Check out the  [changelog](https://git.sr.ht/~sircmpwn/himitsu/refs/0.9)  for the rest of the improvements. Enjoy!

1. Tip for early adopters – if you didn’t notice, Himitsu 0.4 included a
fix for a bug with Hare’s argon2 implementation, which is used to store your
master key. If you installed Himitsu prior to 0.4 and hadn’t done so yet,
you might want to upgrade your key store with `himitsu-store -r`. ↩︎
