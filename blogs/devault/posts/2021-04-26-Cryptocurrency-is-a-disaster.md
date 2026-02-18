---
title: "Cryptocurrency is an abject disaster"
date: 2021-04-26
url: https://drewdevault.com/2021/04/26/Cryptocurrency-is-a-disaster.html
slug: Cryptocurrency-is-a-disaster
word_count: 1120
---

This post is long overdue. Let’s get it over with.

Starting on May 1st, users of sourcehut’s CI service will be required to be on a
paid account, a change which will affect about half of all builds.sr.ht
users. 1  Over the past several months, everyone in the industry who provides
any kind of free CPU resources has been dealing with a massive outbreak of abuse
for cryptocurrency mining. The industry has been setting up informal working
groups to pool knowledge of mitigations, communicate when our platforms are
being leveraged against one another, and cumulatively wasting thousands of hours
of engineering time implementing measures to deal with this abuse, and
responding as attackers find new ways to circumvent them.

Cryptocurrency has invented an entirely new category of internet abuse. CI
services like mine are not alone in this struggle: JavaScript miners, botnets,
and all kinds of other illicit cycles are being spent solving pointless math
problems to make money for bad actors. Some might argue that abuse is inevitable
for anyone who provides a public service — but prior to cryptocurrency,
what kind of abuse would a CI platform endure? Email spam? Block port 25.
Someone might try to host their website on ephemeral VMs with dynamic DNS or
something, I dunno. Someone found a way of monetizing stolen CPU cycles
directly, so everyone who offered free CPU cycles for legitimate use-cases is
now unable to provide those services. If not for cryptocurrency, these services
would still be available.

Don’t make the mistake of thinking that these are a bunch of script kiddies.
There are large, talented teams of engineers across several organizations
working together to combat this abuse, and they’re losing. A small sample of
tactics I’ve seen or heard of include:

* Using CPU limiters to manipulate monitoring tools.
* Installing crypto miners into the build systems for free software projects so
that the builds appear legitimate.
* Using password dumps to steal login credentials for legitimate users and then
leveraging their accounts for mining.

I would give more examples, but secrecy is a necessary part of defending against
this — which really sucks for an organization that otherwise strives to be
as open and transparent as sourcehut does.

Cryptocurrency problems are more subtle than outright abuse, too. The integrity
and trust of the entire software industry has sharply declined due to
cryptocurrency. It sets up perverse incentives for new projects, where
developers are no longer trying to convince you to use their software because
it’s good, but because they think that if they can convince you it will make
them rich. I’ve had to develop a special radar for reading product pages now: a
mounting feeling of dread as a promising technology is introduced while I
inevitably arrive at the buried lede: it’s more crypto bullshit. Cryptocurrency
is the multi-level marketing of the tech world. “Hi! How’ve you been? Long time
no see! Oh, I’ve been working on this cool distributed database file store
archive thing. We’re doing an ICO next week.” Then I leave. Any technology which
is not an (alleged) currency and which incorporates blockchain anyway would
always work better without it.

There are hundreds, perhaps thousands, of cryptocurrency scams and ponzi schemes
trussed up to look like some kind of legitimate offering. Even if the project
 *you’re*  working on is totally cool and solves all of these problems, there
are 100 other projects pretending to be like yours which are ultimately
concerned with transferring money from their users to their founders. Which
one are investors more likely to invest in? Hint: it’s the one that’s more
profitable. Those promises of “we’re different!” are always hollow anyway.
Remember the  [DAO](https://en.wikipedia.org/wiki/The_DAO_(organization)) ? They wanted to avoid social arbitration entirely for
financial contracts, but when the chips are down and their money was walking out
the door, they forked the blockchain.

That’s what cryptocurrency is all about: not novel technology, not empowerment,
but making money. It has failed as an actual  *currency*  outside of some
isolated examples of failed national economies. No, cryptocurrency is not a
currency at all: it’s an investment vehicle. A tool for making the rich richer.
And that’s putting it nicely; in reality it has a lot more in common with a
Ponzi scheme than a genuine investment. What “value” does solving fake math
problems actually provide to anyone? It’s all bullshit.

And those few failed economies whose people are desperately using cryptocurrency
to keep the wheel of their fates spinning? Those make for a good headline, but
how about the rural communities whose tax dollars subsidized the power plants
which the miners have flocked to? People who are  [suffering blackouts](https://www.rferl.org/a/bitcoin-blackouts-russian-cryptocurrency-miners-minting-millions-sucking-abkhazia-electricity-grid-dry/30968307.html) 
as their power is siphoned into computing SHA-256 as fast as possible while
dumping an entire country worth of CO₂ into the atmosphere? 2  No,
cryptocurrency does not help failed states. It exploits them.

Even those in the (allegedly) working economies of the first world have been
impacted by cryptocurrency. The price of consumer GPUs have gone sharply up in
the past few months. And, again, what are these GPUs being used for? Running
SHA-256 in a loop, as fast as possible. Rumor has it that hard drives are up
next.

Maybe your cryptocurrency is different. But look: you’re in really poor company.
When you’re the only honest person in the room, maybe you should be in a
different room. It is impossible to trust you. Every comment online about
cryptocurrency is tainted by the fact that the commenter has probably invested
thousands of dollars into a Ponzi scheme and is depending on your agreement to
make their money back. 3  Not to mention that any attempts at reform, like
proof-of-stake, are viciously blocked by those in power (i.e. those with the
money) because of any risk it poses to reduce their bottom line. No, your
blockchain is not different.

Cryptocurrency is one of the worst inventions of the 21st century. I am ashamed
to share an industry with this exploitative grift. It has failed to be a useful
currency, invented a new class of internet abuse, further enriched the rich,
wasted staggering amounts of electricity, hastened climate change, ruined
hundreds of otherwise promising projects, provided a climate for hundreds of
scams to flourish, created shortages and price hikes for consumer hardware, and
injected perverse incentives into technology everywhere. Fuck cryptocurrency.

1. If this is the first you’re hearing of this, a graceful migration is planned: [details here](https://man.sr.ht/ops/builds.sr.ht-migration.md) ↩︎
2. “But crypto is far from the worst contributor to climate change!” Yeah, but at least the worst offenders provide value to society. See also [Whataboutism](https://en.wikipedia.org/wiki/Whataboutism). ↩︎
3. This is why I asked you to disclose your stake in your comment upfront. ↩︎
