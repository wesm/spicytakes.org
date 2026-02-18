---
title: "Nvidia sucks and I'm sick of it"
date: 2017-10-26
url: https://drewdevault.com/2017/10/26/Fuck-you-nvidia.html
slug: Fuck-you-nvidia
word_count: 595
---

There’s something I need to make clear about Nvidia. Sway 1.0, which is the
release after next, is  *not*  going to support the Nvidia proprietary driver,
EGLStreams, or any other proprietary graphics APIs. The only supported driver
for Nvidia cards will be the open source nouveau driver. I will explain why.

Today, Sway is able to run on the Nvidia proprietary driver. This is not and has
never been an officially supported feature - we’ve added a few things to try and
make it easier but my stance has  *always*  been that Nvidia users are on their
own for support. In fact, Nvidia support was added to Sway without my approval.
It comes from a library we depend on called wlc - had I’d made the decision on
whether or not to support EGLStreams in wlc, I would have said no.

Right now, we’re working very hard on replacing wlc, for reasons unrelated to
Nvidia. Our new library, wlroots, is better in every conceivable way for Sway’s
needs. The Nvidia proprietary driver support is not coming along for the ride,
and here’s why.

So far, I’ve been speaking in terms of  *Sway*  supporting Nvidia, but this is
an ass-backwards way of thinking.  *Nvidia*  needs to support Sway. There are
Linux kernel APIs that we (and other Wayland compositors) use to get the job
done. Among these are KMS, DRM, and GBM - respectively Kernel Mode Setting,
Direct Rendering Manager, and Generic Buffer Management. Every GPU vendor
but Nvidia supports these APIs. Intel and AMD support them with mainlined 1 ,
open source drivers. For AMD this was notably done by replacing their
proprietary driver with a new, open source one, which has been developed in
cooperation with the Linux community. As for Intel, they’ve always been friendly
to Linux.

Nvidia, on the other hand, have been fucking assholes and have treated Linux
like utter shit for our entire relationship. About a year ago they announced
“Wayland support” for their proprietary driver. This included KMS and DRM
support (years late, I might add), but  *not*  GBM support. They shipped something
called EGLStreams instead, a concept that had been discussed and shot down by
the Linux graphics development community before. They did this because it makes
it easier for them to keep their driver proprietary without having work with
Linux developers on it. Without GBM, Nvidia  *does not*  support Wayland, and they
were real pricks for making some announcement like they actually did.

When people complain to me about the lack of Nvidia support in Sway, I get
really pissed off. It is  *not my fucking problem*  to support Nvidia, it’s
Nvidia’s fucking problem to support me. Even Broadcom,  *fucking Broadcom* ,
supports the appropriate kernel APIs. And proprietary driver users have the gall
to  *reward*  Nvidia for their behavior by giving them  *hundreds of dollars*  for
their GPUs, then come to  *me*  and ask me to deal with their bullshit  *for free* .
Well, fuck you, too. Nvidia users are shitty consumers and I don’t even want
them in my userbase. Choose hardware that supports your software, not the other
way around.

Buy AMD. Nvidia– fuck you!

**Edit** : It’s worth noting that Nvidia is evidently attempting to find a better
path with  [this new GitHub project](https://github.com/cubanismo/allocator) . I
hope it works out, but they aren’t really cooperating much with anyone to build
it - particularly nouveau. It’s more throwing code/blobs over the wall and
expecting everyone to change for them.

1. Mainlined means that they are included in the upstream Linux kernel source code. ↩︎
