---
title: "Should you move from GitHub to sr.ht"
date: 2018-06-05
url: https://drewdevault.com/2018/06/05/Should-you-move-to-sr.ht.html
slug: Should-you-move-to-sr.ht
word_count: 502
---

I’m not terribly concerned about Microsoft’s acquisition of GitHub, but I
don’t fault those who are worried. I’ve been working on my alternative platform,
 [sr.ht](https://sr.ht) , for quite a while. I’m not about to leave GitHub because
of Microsoft alone. I do have some political disagreements with GitHub and
Microsoft, but those are also not the main reason that I’m building sr.ht. I
simply think I can do it better. If my approach aligns with your needs, then
sr.ht may be the platform for you.

There are several GitHub alternatives, but for the most part they’re basically
GitHub rip-offs. Unlike GitLab, Gogs/Gitea, BitBucket; I don’t see the GitHub UX
as the pinnacle of project hosting - there are many design choices (notably pull
requests) which I think have lots of room for improvement. sr.ht instead
embraces git more closely, for example building  *on top*  of email rather than
 *instead of*  email.

GitHub optimizes for the end-user and the drive-by contributor. sr.ht optimizes
for the maintainers and core contributors instead. We have patch queues and
ticket queues which you can set up automated filters in or manually curate, and
are reusable for projects on external platforms. You have tools which allow
you to customize the views you see separately from the views visitors see, like
bugzilla-style custom ticket searches. Our CI service gives you KVM
virtualization and knobs you can tweak to run sophisticated automation for your
project. Finally, all of it is  [open
source](https://git.sr.ht/~sircmpwn/?search=sr.ht) .

The business model is also something I think I can do better. GitHub and GitLab
are both VC-funded and trapped into appeasing their shareholders (or now, in
GitHub’s case, the needs of Microsoft as a whole). I think this leads to
incentives which don’t align with the users, as it’s often more important to
support the bottom line than to build what the users want or need. Rather than
trying to raise as much money as possible, the sr.ht aims to be more a
grassroots platform. I’m still working on the money details, but each user will
be expected to pay a subscription fee and growth will be artificially slowed if
necessary to make sure the infrastructure can keep up. In my opinion, venture
capital does not lead to healthy businesses or a healthy economy on the whole,
and I think the users suffer for it. My approach is different.

As for my own projects and the plan for moving them, I don’t intend to move
anything until it won’t be disruptive to the project. I’ve been collecting
feedback from co-maintainers and core contributors to each of the projects I
expect to move and using this feedback to drive sr.ht priorities. They will
eventually move, but only when it’s ready.

I intend to open sr.ht to the public soon, once I have a billing system in place
and break ground on mailing lists (among some smaller improvements). If anyone
is interested in checking it out prior to the public release, shoot me an email
at  [sir@cmpwn.com](mailto:sir@cmpwn.com) .
