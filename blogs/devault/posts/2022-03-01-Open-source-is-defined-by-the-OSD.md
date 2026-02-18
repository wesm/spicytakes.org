---
title: "Open Source is defined by the OSI's Open Source Definition"
date: 2022-03-01
url: https://drewdevault.com/2022/03/01/Open-source-is-defined-by-the-OSD.html
slug: Open-source-is-defined-by-the-OSD
word_count: 1313
---

The  [Open Source Initiative](https://opensource.org)  (OSI) publishes a document called the  [Open Source
Definition](https://opensource.org/osd)  (OSD), which defines the term “open source”. However, there is a
small minority of viewpoints within the software community which wishes that
this were not so. The most concerning among them are those who wish open source
was more commercially favorable to  *themselves* , and themselves alone, such as
companies like Elastic.

I disagree with this perspective, and I’d like take a few minutes today to
explore several of the most common arguments in favor of this view, and explain
why I don’t agree with them. One of the most frustrating complications in this
discussion is the context of  [motivated reasoning](https://en.wikipedia.org/wiki/Motivated_reasoning)  ( [relevant xkcd](https://xkcd.com/2167) ): most
people arguing in favor of an unorthodox definition of “open source” have a
vested interest in their alternative view. 1  This makes it difficult to
presume good faith. For example, say someone wants to portray their software as
open source even if it prohibits commercial use by third parties, which would
normally disqualify it as such. Their interpretation serves to re-enforce their
commercialization plans, providing a direct financial incentive not only for
them to promote this definition of “open source”, but also for them to convince
you that their interpretation is valid.

I find this argument to be fundamentally dishonest. Let me illustrate this with
an analogy. Consider  [PostgreSQL](https://www.postgresql.org) . If I were to develop a new program called
Postgres which was similar to PostgreSQL, but different in some important ways
— let’s say it’s a proprietary, paid, hosted database service — that
would be problematic. The industry understands that “Postgres” refers to the
popular open source database engine, and by re-using their name I am diluting
the brand of Postgres. It can be inferred that my reasoning for this comes from
the desire to utilize their brand power for personal commercial gain. The terms
“Postgres” and “PostgreSQL” are trademarked, but even if they were not, this
approach would be dishonest and ethically wrong.

So too are the attempts to re-brand “open source” in a manner which is more
commercially exploitable for an individual person or organization equally
dishonest. The industry has an orthodox understanding of the meaning of “open
source”, i.e. that defined by the Open Source Initiative, which is generally
well-understood through the proliferation of software licenses which are
compatible with the OSD. When a project describes itself as “open source”,
this is a useful short-hand for understanding that the project adheres to a
specific set of values and offers a specific set of rights to its users and
contributors. When those rights are denied or limited, the OSD no longer applies
and thus neither does the term “open source”. To disregard this in the interests
of a financial incentive is dishonest, much like I would be dishonest for
selling “cakes” and fulfilling orders with used car tires with “cake” written on
them instead.

Critics of the OSD frequently point out that the OSI failed to register a
trademark on the term “open source”, but a trademark is not necessary for this
argument to hold. Language is defined by its usage, and the OSD is the popular
usage of the term “open source”, without relying on the trademark system. The
existence of a trademark on a specific term is not required for language which
misuses that term to be dishonest.

As language is defined by its usage, some may argue that they are as entitled as
anyone else to put forward an alternative usage. This is how language evolves.
They are not wrong, though I might suggest that their alternative usage of “open
source” requires a substantial leap in understanding which might not be as
agreeable to those who don’t stand to benefit financially from that leap. Even
so, I argue that the mainstream definition of open source, that forwarded by the
OSI, is a  *useful*  term that is worth preserving in its current form. It is
useful to quickly understand the essential values and rights associated with a
piece of software as easily as stating that it is “open source”. I am not
prepared to accept a new definition which removes or reduces important rights in
service of your private financial interests.

The mainstream usage of “open source” under the OSD is also, in my opinion,
morally just. You may feel a special relationship with the projects you start
and invest into, and a sense of ownership with them, but they are not rightfully
yours once you receive outside contributions. The benefit of open source is in
the ability for the community to contribute directly to its improvements —
and once they do, the project is the sum of your efforts  *and*  the efforts of
the community. Thus, is it not right that the right to commercial exploitation
of the software is shared with that community? In the absence of a CLA, 2 
contributors retain their copyright as well, and the software is legally jointly
owned by the sum of its contributors. And beyond copyright, the success of the
software is the sum of its code along with the community who learns about and
deploys it, offers each other support, writes blog posts and books about it,
sells consulting services for it, and together helps to popularize it. If you
wish to access all of these benefits of the open source model, you must play by
the open source rules.

It’s not surprising that this would become a matter of contention among certain
groups within the industry. Open source is not just eating the world, but  *has
eaten*  the world. Almost all software developed today includes substantial open
source components. The open source brand is very strong, and there are many
interests who would like to leverage that brand without meeting its obligations.
But the constraints of the open source definition are  *important* , played a
critical role in the ascension of open source in the software market, and worth
preserving into the future.

That’s not to say that there isn’t room for competing ideologies. If you feel
that the open source model does not work for you, then that’s a valid opinion to
hold. I only ask that you market your alternative model honestly by using a
different name for it. Software for which the source code is available, but
which does not meet the requirements of the open source definition, is
rightfully called “source available”. If you want a sexier brand for it, make
one! “Open core” is also popular, though not exactly the same. Your movement has
as much right to success as the open source movement, but you need to earn that
success independently of the open source movement. Perhaps someday your
alternative model will supplant open source! I wish you the best of luck in this
endeavour.

*A previous version of this blog post announced that I had submitted my
candidacy for the OSI board. Due to unforseen circumstances, I will be
postponing my candidacy until the next election. I apologise for the confusion.*

1. Am I similarly biased? I also make my living from open source software,
but I take special care to place the community’s interests above my own. I
advocate for open source and free software principles in all software,
including software I don’t personally use or benefit from, and in my own
software I don’t ask contributors to sign a CLA — keeping the copyrights
collectively held by the community at large, and limiting my access to
commercialization to the same rules of open source that are granted to all
contributors to and users of the software I use, write, and contribute to. ↩︎
2. Such CLAs are also unjust in my view. Tools like the [Developer
Certificate of Origin](https://developercertificate.org) are better for meeting the need to establish the
legitimate copyright of open source software without denying rights to its
community. ↩︎
