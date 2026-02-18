---
title: "The unrealized potential of federation"
date: 2020-09-20
url: https://drewdevault.com/2020/09/20/The-potential-of-federation.html
slug: The-potential-of-federation
word_count: 705
---

There are some major problems on the internet which may seem intractable. How do
we prevent centralization of our communication tools under the authority of a
few, whose motivations may not align with our interests? How do we build
internet-scale infrastructure without a megacorp-scale budget? Can we make our
systems reliable and fault-tolerant — in the face of technical  *and* 
social problems?

**Federation**  is an idea which takes a swing at all of these problems.

*Note: apparently some cryptocurrency enthusiasts are parading this article
around to peddle their garbage. Cryptocurrency is the digitally woke techbro’s
ponzi scheme, and is a massive waste of electricity and developer effort. Anyone
who tells you anything positive about anything which is even remotely connected
to cryptocurrency almost certainly has ulterior motives and you should steer
clear. So hopefully that settles that. And cryptocurrency is a P2P system,
anyway, NOT a federation!*

The key trait of a software system which is  *federated*  is that the servers are
controlled by independent, sovereign entities, and that they exist together
under a common web of communication protocols and social agreements. This
occupies a sort of middle ground between the centralized architecture and the
peer-to-peer (or “decentralized”) architecture. Federation enjoys the advantages
of both, and few of the drawbacks.

In a federated software system, groups of users are built around small,
neighborly instances of servers. These are usually small servers, sporting only
modest resource requirements to support their correspondingly modest userbase.
Crucially, these small servers speak to  *one another*  using standard protocols,
allowing users of one instance to communicate seamlessly with users of other
instances. You can build a culture and shared sense of identity on your
instance, but also reach out and easily connect with other instances.

The governance of a federated system then becomes distributed among many
operators. Every instance has the following privileges:

1. To set the rules which govern users of their instance
2. To set the rules which govern who they federate with

And, because there are hundreds or even thousands of instances, the users get
the privilege of choosing an instance whose rules they like, and which federates
with other instances they wish to talk to. This system also makes it hard for
marketing and spam to get a foothold — it optimizes for a self-governing
system of human beings talking to human beings, and not for corporations to push
their products.

The costs of scaling up a federation is distributed manageably among these
operators. Small instances, with their modest server requirements, are often
cheap enough that a sysadmin can comfortably pay for the expenses out of pocket.
If not, it’s usually quite easy to solicit donations from the users to keep
things running. New operators appear all the time, and the federation scales up
a little bit more.

Unlike P2P systems, the federated model allows volunteer sysadmins to use their
skills to expand access to the service to non-technical users, without placing
the burden on those non-technical users to set up, understand, maintain, or
secure servers or esoteric software. The servers are also always online and
provide strong identities and authenticity guarantees — eliminating an
entire class of P2P problems.

A popular up-and-coming protocol for federation is ActivityPub, but it’s not the
only way to build a federated system. You’re certainly familiar with another
federation which is not based on ActivityPub: email. IRC and Matrix also provide
federated protocols in the instant messaging domain. Personally, I don’t like
ActivityPub, but AP is not necessary to reap the benefits of federation. Many
different kinds of communication systems can be designed with federation in
mind, and adjust their approach to accommodate their specific needs, evident in
each of these examples.

In short, federation distributes governance and cost, and can allow us to tackle
challenges that we couldn’t overcome without it. The free software community
needs to rally behind federation, because no one else will. For all of the
reasons which make it worth doing, it is not rewarding for corporations.  They
would much rather build walled gardens and centralize, centralize, centralize
— it’s more profitable!  Democratic software which puts control into the
hands of the users is something we’re going to have to take for ourselves. Viva
la federación!
