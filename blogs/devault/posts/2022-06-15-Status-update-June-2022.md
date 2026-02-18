---
title: "Status update, June 2022"
date: 2022-06-15
url: https://drewdevault.com/2022/06/15/Status-update-June-2022.html
slug: Status-update-June-2022
word_count: 559
---

Hello again! I would like to open this post by acknowledging the response to my
earlier post, “bleh”. Since it was published, I have received several hundred
emails expressing support and kindness. I initially tried to provide these with
thoughtful replies, then shorter replies, then I had to stop replying at all,
but I did read every one. Thank you, everyone, for sending these. I appreciate
it very much, and it means a lot to me.

I have actually had a lot more fun programming this month than usual, since I
decided to spend more time on experimental and interesting projects and less
time on routine maintenance or long-term developments. So, the feature you’ve
been waiting for in SourceHut might be delayed, but in return, there’s cool
progress on the projects that you didn’t even know you were waiting for. Of
course, the SourceHut workload never dips below a dull roar, as I have to attend
to business matters and customer support promptly, and keep a handle on the
patch queue, and the other SourceHut staff and contributors are always hard at
work — so there’ll be plenty to discuss in the “what’s cooking” later.

The bulk of my focus has been on the Helios kernel this month, a project  [I
introduced](https://drewdevault.com/2022/06/13/helios.html)  a couple of days ago. I spent a lot of time furiously
refactoring, reworking the existing kernel code for evalutaing features like
page allocation and virtual address space management into capability-oriented
kernel services that can be provided to userspace, then overhauling our startup
code to provision a useful set of capabilities for the init process to take
advantage of. I also implemented x86_64 I/O port services, which allowed for
the first few drivers to be written in userspace — serial ports and simple
VBE graphics. We also got interrupts working properly and brought up the PIT,
which is another major step towards multi-tasking. I also implemented a new
syscall ABI with error handling, and refactored a lot of the arch-specific code
to make new ports easier. The kernel is in a much better state now than it was a
month ago (and to think it’s only three months old!).

There was also a lot of progress on  [Himitsu](https://sr.ht/~sircmpwn/himitsu) , which I plan on presenting in a
video and blog post in a few days time. The Firefox add-on actually works now
(though some features remain to be done), and Alexey Yerin fixed several
important bugs and contributed several new features. The user is now prompted to
consent before deleting keys, and we have a new GTK+ prompter written in Python,
which is much more reliable and feature-full thanks to Martijn Braam’s help
(rewriting it in C again is a long-term TODO item for any interested
contributor). I also made some progress towards what will ultimately become
full-disk encryption support.

Hare also enjoyed many improvements this month. We have some new improvements to
date/time support, including fixes for Martian time ;) I also mostly implemented
cross-compiling, which you can try out with  `hare build -t riscv64`  or something
similar. The major outstanding pain point here is that the Hare cache is not
arch-aware, so you need to  `rm -rf ~/.cache/hare`  each time you switch
architectures for now. We now have complex number support, as well as
improvements to encoding::json and net::uri.

That’s all for today. Until next time!
