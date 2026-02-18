---
title: "Don't sign a CLA"
date: 2018-10-05
url: https://drewdevault.com/2018/10/05/Dont-sign-a-CLA.html
slug: Dont-sign-a-CLA
word_count: 681
---

A large minority of open-source projects come with a CLA, or Contributor License
Agreement, and require you to sign one before they’ll merge your patch. These
agreements typically ask you to go above and beyond the rights you afford the
project by contributing under the license the software is distributed with. And
you should never sign one.

Free and open source software licenses grant explicit freedoms to three groups:
the maintainers, the users,  *and*  the contributors. An important freedom is the
freedom to make changes to the software and to distribute these changes to the
public. The natural place to do so is by contributing to the upstream project,
something a project should be thankful for. A CLA replaces this gratitude with
an attempt to weaken these freedoms in a manner which may stand up to the letter
of the license, but is far from the spirit.

A CLA is a kick in the groin to a contributor’s good-faith contribution to the
project. Many people, myself included, contribute to open source projects under
the assumption that my contributions will help serve a project which continues
to be open source in perpetuity, and a CLA provides a means for the project
maintainers to circumvent that. What the CLA is actually used for is to give the
project maintainers the ability to relicense your work under a more restrictive
software license, up to and including making it entirely closed source.

We’ve seen this happen before. Consider the Redis Labs debacle, where they
adopted the nonfree 1  Anti-Commons Clause 2 , and used their CLA to pull along
any external contributions for the ride. As thanks for the generous time
invested by their community into their software, they yank it out from
underneath it and repurpose it to make money with an obscenely nonfree product.
Open source is a commitment to your community. Once you make it, you cannot take
it back. You don’t get the benefits associated with being an open source project
if you have an exit hatch. You may argue that it’s your right to do what you
want with your project, but making it open source is  *explicitly waiving that
right* .

So to you, the contributor: if you are contributing to open source and you want
it to stay that way, you should not sign a CLA. When you send a patch to a
project, you are affording them the same rights they afforded you. The
relationship is one of equals. This is a healthy balance. When you sign a CLA,
you give them unequal power over you. If you’re scratching an itch and just
want to submit the patch in good faith, it’s easy enough to fork the project and
put up your changes in a separate place. This is a right afforded to you by
every open source license, and it’s easy to do. Anyone who wants to use your
work can apply your patches on top of the upstream software. Don’t sign away
your rights!

Additional reading:  [GPL as the Best Licence – Governance and Philosophy](https://blog.hansenpartnership.com/gpl-as-the-best-licence-governance-and-philosophy/)

Some responses to the discussion around this article:

*What about the [Apache Foundation
CLA](https://www.apache.org/licenses/cla-corporate.txt)?*  This CLA is one of the
better ones, because it doesn’t transfer copyright over your work to the Apache
Foundation. I have no beef with clauses 1 and 3-8. However, term 2 is too broad
and I would not sign this CLA.

*What about the Linux kernel [developer certificate of
origin](https://elinux.org/Developer_Certificate_Of_Origin)?*  I applaud the
Linux kernel’s approach here. It covers their bases while still strongly
protecting the rights of the patch owner. It’s a short statement with little
legalese and little fanfare to agreeing to it (just add “Signed-off By” to your
commit message). I approve.

Update April 2021: I wrote a follow-up article about the Developer Certificate
of Origin in particular:  [The Developer Certificate of Origin is a great alternative to a CLA](https://drewdevault.com/2021/04/12/DCO.html)

1. [Free as in freedom](/2018/08/22/Commons-clause-will-destroy-open-source.html) ↩︎
2. Call me petty, but I can’t in good faith call it the “Commons Clause” when its purpose is to *remove* software from the commons. ↩︎
