---
title: "postmarketOS revolutionizes smartphone hacking"
date: 2021-11-26
url: https://drewdevault.com/2021/11/26/postmarketos.html
slug: postmarketos
word_count: 719
---

I briefly mentioned  [postmarketOS](http://postmarketos.org/)  in  [my Pinephone review](https://drewdevault.com/2019/12/18/PinePhone-review.html)  two years ago,
but after getting my Dutch SIM card set up in my Pinephone and having another go
at using postmarketOS, I reckon they deserve special attention.

Let’s first consider the kind of ecosystem into which postmarketOS emerged:
smartphone hacking in the XDA Forums era. This era was dominated by amateur
hackers working independently for personal prestige, with little to no regard
for the values of free software or collaboration. It was common to see
hacked-together binary images shipped behind adfly links in XDA forum threads in
blatant disregard of the GPL, with pages and pages of users asking redundant
questions and receiving poor answers to the endless problems caused by this
arrangement.

The XDA ecosystem is based on Android, which is a mess in and of itself. It’s an
enormous, poorly documented ball of Google code, mixed with vendor drivers and
private kernel trees, full of crappy workarounds and locked-down hardware. Most
smart phones are essentially badly put-together black boxes and most smart phone
hackers are working with their legs cut off. Not to mention that the software
ecosystem which runs on the platform is full of scammers and ads and theft of
private user information. Android may be Linux in implementation, but it’s about
as far from the spirit of free software as you can get.

postmarketOS, on the other hand, is based on Alpine Linux, which happens to be
my favorite Linux distribution. Instead of haphazard forum threads collecting
inscrutable ports for dozens of devices, they have a single git repository where
all of their ports are maintained under version control, complete with issue
trackers and merge requests, plus a detailed centralized wiki providing a wealth
of open technical info on their supported platforms. And, by virtue of being a
proper Linux distribution, they essentially opt-out of the mess of predatory
mobile apps and instead promote a culture of trusted applications which respect
the user and are built by and for the community instead of by and for a
corporation.

Where we once had to live with illegally closed-source forks of the Linux
kernel, we now have a git repository in which upstream Linux releases are
tracked with a series of auditable patches for supporting various devices, many
of which are making their way into upstream Linux. Where we once had a forum
thread with five wrong answers to the same question on page 112, we now have a
bug report on GitLab with a documented workaround and a merge request pending
review. Instead of begging my vendor to unlock my bootloader and using janky
software reminiscent of old keygen hacks to flash a dubious Android image, I can
build postmarketOS’s installer, pop it onto a microSD card, and two minutes I’ll
have Linux installed on my Pinephone.

pmOS does not seek to elevate the glories of tiny individual hackers clutching
their secrets close to their chest, instead elevating the glory of the community
as a whole. It pairs perfectly with Pine64, the only hardware vendor working
closely with upstream developers with the same vision and ideals. There is a
promise for hope in the future of smart phones in their collaboration.

However, the path they’ve chosen is a difficult one. Android, for all of its
faults, presents a complete solution for a mobile operating system, and upstream
Linux does not. In my review, I said that software would be the biggest
challenge of the Pinephone, and 2 years later, that remains the case. Work
reverse engineering the Pine64 hardware is slow, there is not enough cooperation
between project silos, and there needs to be much better prioritization of the
work. To complete their goals, the community will have to work more closely
together and narrow their attention in on the key issues which stand between the
status quo and the completion of a useful Linux smartphone. It will require
difficult, boring engineering work, and will need the full attention and
dedication of the talented people working on these projects.

If they succeed in spite of these challenges, the results will be well worth it.
postmarketOS and pine64 represent the foundations of a project which could
finally deliver Linux on smartphones and build a robust mobile platform that
offers freedom to its users for years to come.
