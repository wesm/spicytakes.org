---
title: "Breaking down Apollo Federation's anti-FOSS corporate gaslighting"
date: 2021-11-05
url: https://drewdevault.com/2021/11/05/Apollo-federation-2-gaslighting.html
slug: Apollo-federation-2-gaslighting
word_count: 1394
---

Gather around, my friends, for there is another company which thinks we are
stupid and we enjoy having our faces spat in.  [Apollo Federation](https://www.apollographql.com/blog/announcement/moving-apollo-federation-2-to-the-elastic-license-v2/) 1  has
announced that they will switch to a non-free license. Let’s find out just how
much the Elastic license really is going to “protect the community” like they
want you to believe.

Let’s start by asking ourselves, objectively, what practical changes can we
expect from a switch from the  [MIT license](https://mit-license.org)  to the  [Elastic
License](https://www.elastic.co/licensing/elastic-license) ? Both licenses are pretty short, so I recommend quickly
reading them yourself before we move on.

I’ll summarize the difference between these licenses. First, the Elastic license
offers you (the recipient of the software) one benefit that MIT does not: an
explicit license for any applicable patents. However, it also has many
additional restrictions, such as:

* No sublicensing (e.g. incorporating part of it into your own program)
* No resale (e.g. incorporating it into Red Hat and selling support)
* No modifications which circumvent the license key activation code
* No use in a hosted or managed service

This is an objective analysis of the change. How does Apollo explain the changes?

> Why the new license? 
>  The Apollo developer community is at the heart of everything we do. As
> stewards of our community, we have a responsibility to prevent harm from
> anyone who intends to exploit our work without contributing back. We want to
> continue serving you by funding the development of important open-source graph
> technology for years to come. To honor that commitment, we’re moving Apollo
> Federation 2 to the Elastic License v2 (ELv2).

Taking them at their word, this change was motivated by their deep care for
their developer community. They want to “honor their commitment”, which is to
“fund the development of important open-source graph technology” and “prevent
harm from anyone who intends to exploit our work without contributing back”.

This is a very misleading statement. The answer to the question stated by the
header is “funding the development”, but they want us to first think that
they’re keeping the community at the heart of this decision — a community
that they have just withheld several rights from. Their wording also seeks to
link the community with the work, “our work”, when the change is clearly
motivated from a position where Apollo believes they have effective ownership
over the software, sole right to its commercialization, and a right to charge
the community a rent — enforced via un-circumventable license key
activation code. The new license gives Apollo exclusive right to commercial
exploitation of the software — so they can “exploit our work”, but the
community itself cannot.

What’s more, the change does not fund “open-source graph technology” as
advertised, because after this change, Apollo Federation is no longer open
source. The term “open source” is defined by the  [Open Source
Definition](https://opensource.org/osd) 3 , whose first clause is:

> [The distribution terms of open-source software] shall not restrict any party
> from selling or giving away the software as a component of an aggregate
> software distribution containing programs from several different sources. The
> license shall not require a royalty or other fee for such sale.

The OSD elaborates later:

> The license must not restrict anyone from making use of the program in a
> specific field of endeavor. For example, it may not restrict the program from
> being used in a business, or from being used for genetic research. 
>  The rights attached to the program must apply to all to whom the program is
> redistributed without the need for execution of an additional license by those
> parties.

The Elastic license clearly does not meet this criteria.

Reading the Apollo announcement further, it continues to peddle this and other
lies. The next paragraph attempts to build legitimacy for its peers in this
anti-FOSS gaslighting movement:

> Open-source licensing is evolving with the cloud. Many successful companies
> built on open-source technology (such as Elastic, MongoDB, and Confluent)
> have followed the path we’re taking to protect their communities and combine
> open, collaborative development with the benefits of cloud services that are
> easy to adopt and manage.

They continue to use “open-source” language throughout, and misleads us into
believing that they’ve made this change to protect the community and empower
developers.

> When the Elastic License v2 was released, Elastic CEO Shay Banon called upon
> open-source companies facing a similar decision to “coalesce around a smaller
> number of licenses.” We’re excited to be part of this coalition of modern
> infrastructure companies building businesses that empower developers. […]
> Moving the Apollo Federation libraries and gateway to ELv2 helps us focus on
> our mission: empowering all of you.

It should be evident by now that this is complete horseshit. Let me peel away
the bullshit and explain what is actually going on here in plain English.

Free and open source software can be commercialized — this is an essential
requirement of the philosophy! However, it cannot be  *exclusively* 
commercialized. Businesses which participate in the FOSS ecosystem must give up
their intellectual property monopoly, and allow the commercial ecosystem to
flourish within their community — not just within their own ledger. They
have to make their hosted version  *better*  than the competitors, or seek other
monetization strategies: selling books, support contracts, consulting, early
access to security patches, and so on.

The community, allegedly at the heart of everything Apollo does, participates
in the software’s development, marketing, and growth, and they are rewarded with
the right to commercialize it. The community is incentivized to contribute back
because they retain their copyright and the right to monetize the software.  [634
people](https://github.com/apollographql/apollo-client/graphs/contributors)  have contributed to Apollo, and the product is the sum of
their efforts, and should belong to them — not just to the business which
shares a name with the software. The community built their projects on top of
Apollo based on the open source social contract, and gave their time, effort,
and copyright for their contributions to it, and Apollo pulled the rug out from
under them. In the words of Bryan Cantrill, this shameful, reprehensible
behavior is  [shitting in the pool of open source](https://invidious.mnus.de/watch?v=-zRN7XLCRhc&t=2483) .

The smashing success of the free and open source software movement, both
socially and commercially, has attracted the attention of bad actors like
Apollo, who want to capitalize on this success without meeting its obligations.
This wave of nonfree commercial gaslighting is part of a pattern where a company
builds an open-source product, leverages the open-source community to build a
market for it and to  *directly*  improve the product via their contributions,
then switches to a nonfree license and steals the work for themselves, fucking
everyone else over.

Fuck Matt DeBergalis, Shay Banon, Jay Kreps, and Dev Ittycheria. These are the
CEOs and CTOs responsible for this exploitative movement. They are morally
bankrupt assholes and rent-seekers who gaslight and exploit the open source
community for personal gain.

This is a good reminder that this is the ultimate fate planned by any project
which demands a copyright assignment from contributors in the form of a
Contributor License Agreement (CLA).  [Do not sign these](https://drewdevault.com/2018/10/05/Dont-sign-a-CLA.html) ! Retain your
copyright over your contributions and contribute to projects which are
collectively owned by their community — because  *that’s*  how you honor
your community.

Previously:

* [Elasticsearch does not belong to Elastic](https://drewdevault.com/2021/01/19/Elasticsearch-does-not-belong-to-Elastic.html)
* [Open source means surrendering your monopoly over commercial exploitation](https://drewdevault.com/2021/01/20/FOSS-is-to-surrender-your-monopoly.html)
* [The Developer Certificate of Origin is a great alternative to a CLA](https://drewdevault.com/2021/04/12/DCO.html)

If you are an Apollo Federation user who is affected by this change, I have set
up  [a mailing list](https://lists.sr.ht/~sircmpwn/apollo-fork)  to organize a community-maintained fork. Please send an
email to this list if you are interested in participating in such a fork.

1. For those unaware, Apollo Federation is a means of combining many
GraphQL2 microservices into one GraphQL API. ↩︎
2. For those unaware, GraphQL is a standardized query language largely used
to replace REST for service APIs. SourceHut uses GraphQL. ↩︎
3. Beware, there are more gaslighters who want us to believe that the OSD
does not define “open source”. This is factually incorrect. Advocates of this
position usually have ulterior motives and, like Apollo, tend to be thinking
more about their wallets than the community. ↩︎
