---
title: "On \"real name\" policies"
date: 2023-10-31
url: https://drewdevault.com/2023/10/31/On-real-names.html
slug: On-real-names
word_count: 878
---

Some free software projects reject anonymous or pseudonymous contributions,
requiring you to author patches using your “real name”. Such projects have a
so-called “real name” policy; Linux is one well-known example. 1

The root motivations behind such policies vary, but in my experience the most
often cited rationale is that it’s important to establish the provenance of the
contribution for copyright reasons. In the case of Linux, contributors are asked
to “sign-off” their commits to indicate their agreement to the terms of the
Developer Certificate of Origin (DCO), which includes clauses like the
following:

> The contribution was created in whole or in part by me and I have the right to
> submit it under the open source license indicated in the file.

To some extent, the DCO serves as a legal assertion of copyright and an
agreement to license a work under given copyright terms (GPLv2 in the case of
Linux). This record also means that the author of the code is accountable in
case the copyright is challenged; in the case of an anonymous or pseudonymous
contributor you’re shit out of luck. At that point, liability over the
disagreement would likely fall into the hands of the maintainer that accepted
the contribution. It is reasonable for a maintainer to ask a contributor to
assert their copyright and accept liability over the provenance of their code in
a legally meaningful and accountable form.

The possibility that someone may have something useful to offer to a free
software project, but is not comfortable disclosing their name for any number of
reasons, is a reasonable supposition. A maintainer whose “real name” policy is
challenged on this basis would also be reasonable in saying “I feel for you, but
I cannot agree to accept legal liability over the provenance of this code,
nor can I communicate that risk to end-users who acquire code under a license
that may or may not be valid as such”.

“Real name” policies are controversial in the free software community. I open
with this perspective in an attempt to cool down the room. Those who feel
marginalized by “real name” policies often skew young, and many treat matters
such as copyright and licensing with disdain. Moreover, the problem tends to
inflame deeply hurtful sentiments and raise thorny matters of identity and
discrimination, and it’s easy to construe the intent of the policymakers as the
intent to cause harm. The motivations behind these policies are reasonable.

That said, intent or otherwise, these policies can cause harm. The profile of
the contributor who is comfortable using their “real name” is likely to fall
more narrowly into over-represented demographics in our community; enforcing a
real-name policy will ostracize some people. Those with marginalized identities
tend to be less comfortable with disclosing their “real name”. Someone who has
been subject to harassment may not be comfortable with this disclosure, since it
offers more fuel to harassers keeping tabs on their activities. The use of a
“real name” also confers a gender bias; avoiding a “real name” policy neatly
eliminates discrimination on this basis. Of course, there are also many
 [falsehoods programmers believe about names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)  which can present in the
implementation of such a policy.

There is also one particular problem which has been at the heart of conflict
surrounding the use of “real-name” policies in free software: transgender
identities. A transgender person is likely to change their name in the process
of assuming their new identity. When this happens, their real name changes.
However, it may or may not match their legal name – some trans people opt to
change it, others don’t; if they do it is a process that takes time. Meanwhile,
addressing a trans person by their old name, or “deadname”, is highly
uncomfortable. Doing so deliberately, as a matter of policy or otherwise, is a
form of discrimination. Many trans people experience deliberate “deadnaming” as
a form of harassment in their daily lives, and institutionalizing this behavior
is cruel.

The truth is, managing the names of participants is more challenging than anyone
would like. On the one hand, names establish accountability and facilitate
collaboration, and importantly, credit the authors of a work for services
performed. On the other hand, names are highly personal and deeply affecting,
and their usage and changes over time are the subject of important consideration
at the discretion of their owner. A complicating factor is that handling names
properly introduces technical problems which must be overcome.

To embrace the advantages of “real name” policies – establishing provenance,
encouraging accountability, fostering a social environment – without causing
harm, the approach I have settled on for my projects is to use the DCO to
establish provenance and encourage contributors to sign-off and participate
under the identity they feel most comfortable with. I encourage people to
utilize an identity they use beyond the project’s walls, to foster a social
environment and a connection to the broader community, to establish
accountability, and to ensure that participants are reachable for further
discussion on their work. If a contributor’s identity changes, we make every
effort to support this change in contemporary, future, and historical use.

1. A [change to Linux policy](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=d4563201f33a022fc0353033d9dfeb1606a88330) earlier this year refines their approach to
alleviate the concerns raised in this article. ↩︎
