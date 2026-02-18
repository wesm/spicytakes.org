---
title: "General-purpose OS, special-purpose OS, and now: vendor-purpose OS"
date: 2020-06-26
url: https://drewdevault.com/2020/06/26/Vendor-purpose-OS.html
slug: Vendor-purpose-OS
word_count: 405
---

There have, historically, been two kinds of operating systems: general-purpose,
and special-purpose. These roles are defined by the function they serve for the
user. Examples of general-purpose operating systems include Unix (Linux, BSD,
etc), Solaris, Haiku, Plan 9, and so on. These are well-suited to general
computing tasks, and are optimized to solve the most problems possible, perhaps
at the expense of those in some niche domains. Special-purpose operating systems
serve those niche domains, and are less suitable for general computing. Examples
of these include FreeRTOS, Rockbox, Genode, and so on.

These terms distinguish operating systems by the problems they solve for the
user. However, a disturbing trend is emerging in which the user is not the party
whose problems are being solved, and perhaps this calls for a new term. I
propose “vendor-purpose operating system”.

I would use this term to describe Windows, macOS, Android, and iOS, and perhaps
some others besides. Arguably, the first two used to be general purpose
operating systems, and the latter two were once special-purpose operating
systems.  Increasingly, these operating systems are making design decisions
which benefit the vendor  *at the expense*  of the user. For example: Windows has
ads and excessive spyware, prevents you from making a local login without a
Microsoft account, and aggressively pushes you to switch to Edge from other web
browsers, as well as many other examples besides.

Apple is more subtle from the end-user’s perspective. They eschew standards to
build walled gardens, opting for Metal rather than Vulkan, for example. They use
cryptographic signatures to enforce a racket against developers who just want to
ship their programs. They bully vendors in the app store into adding things like
microtransactions to increase their revenue. They’ve also long been making
similar moves in their hardware design, adding anti-features which are
explicitly designed to increase their profit — adding false costs which
are ultimately passed onto the consumer.

All of these decisions are making the OS worse for users in order to provide
more value to the vendor. The operating system is becoming  *less*  suited to its
general-purpose tasks, as the vendor-purpose anti-features deliberately get in
the way. They also become less suited at special-purpose tasks for the same
reasons. These changes  *are*  making improvements for one purpose: the vendor’s
purpose. Therefore, I am going to start refering to these operating systems as
“vendor purpose”, generally alongside a curse and a raising of the middle
finger.
