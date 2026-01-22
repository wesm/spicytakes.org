---
title: "Nadia Asparouhova"
date: 2018-10-31
url: https://nadia.xyz/foundations
word_count: 2069
---


# [Nadia Asparouhova](https://nadia.xyz/)

- [projects](https://nadia.xyz/projects)
- [notes](https://nadia.xyz/notes)
- [newsletter](https://nayafia.substack.com/)
- [twitter](https://twitter.com/nayafia)

[<-- home](https://nadia.xyz/)

# Governance without foundations


October 31, 2018


I’ve recently had several conversations with projects about software foundations, so I figured I should type up my thoughts here.


The term “foundation” is associated with a lot of warm fuzzy things, like nonprofits and giving. As a result, foundations are given a lot of leeway, because people assume their incentives are somehow better aligned with the public interest.


Structurally speaking, however, a foundation isn’t much more than a tax designation, and they come in all shapes and sizes, especially when it comes to software foundations. [1] [There is nothing about a foundation](https://nadia.xyz/zuckerberg-llc) that is inherently good, neutral, or charitable, simply because they have a 501(c) status. [2]


If anything, I’d argue that foundations are, counterintuitively, subject to *less* public accountability than companies. I think this looks like some version of a free-rider problem, where we assume foundations are default-good and don’t pay as much attention to them, whereas we assume a company is default-bad and hold them to task.


## Rethinking the software foundation


Within the world of foundations, software foundations are an even weirder subset, because they’re used as a catch-all solution to a disjointed set of activities, such as:

- Hold financial assets associated with the project
- Hold the trademark/IP assets of the project
- Promote educational initiatives for the community
- Serve as a governance check on corporate interests


My concern with software foundations isn’t about any specific example. Rather, I think that *“the foundation”*, as a single point of failure, is structurally at odds with the idea of *“the project”*, which is inherently distributed.


Foundations suffer from a **winner-take-all mentality**, where for any given project, only one foundation is assumed to exist. Like a government, because they ostensibly serve the public interest, they’re endowed with the highest form of authority. By contrast, a project’s contributors are assumed to be distributed across multiple companies, organizations, and other independent setups. While it doesn’t always work out this way, it’s easier to figure out how to diversify the contributors to a project than it is to dismantle a foundation.


Of course, even in a distributed context, some coordination is always necessary. I like to highlight the role of project *maintainers* over *contributors* for this reason. However, foundations strike me as a bloated and unmaneuverable solution to a set of needs that could probably be broken apart and resolved through other means.


Software foundations, like other governance bodies, only function so long as their interests are well-aligned with the project. Sometimes, this works out. Other times, foundations veer off the path into their own game, fundraising for the sake of fundraising, or prioritizing work that doesn’t benefit the project.


Many of the newer open source projects, even big ones, are hesitant about starting software foundations today. I think this hesitation is justified. On the other hand, by avoiding foundations, projects also avoid the question of how to formalize their governance, thus risking a “tyranny of structurelessness” that might range from projects living inside a company forever, to disorganized chaos that negatively impacts project velocity.


Today, we can develop governance solutions that spread the risk across multiple entities, whose incentives are more closely aligned with the project. What could alternatives to the software foundation look like?


## Foundations as a service provider


I mentioned that software foundations are used to manage a mismash of project needs, so I’d like to start by breaking these apart.


When it comes to legal and financial services, foundations serve a critical role. They can hold the [trademark and other IP assets](http://fossmarks.org/) of the project. They also provide a way to accept, hold, and manage financial assets associated with the project.


It’s hard to think of alternatives to managing these services. However, I also don’t think it’s necessary for a project to start its own 501(c) to handle these tasks. It’s more efficient for these services to be “virtualized” by a few providers, who lower coordination costs for everyone.


Some organizations, like [Software Freedom Conservancy](https://sfconservancy.org/projects/services/) and [Open Collective](https://opencollective.com/), offer services like fiscal sponsorship and IP asset stewardship. It’s worth noting that this model is prevalent in the nonprofit sector more generally: many “nonprofits” are actually housed under fiscal sponsors, who accept funds in exchange for a percent of revenue, because it’s so expensive and cumbersome to set up 501(c)s.


In the long run, it’s also possible that some of these tasks will become obsolete. For example, companies currently prefer funding projects over individual contributors. Not only do they benefit from brand association with the project, but it’s also just logistically easier than managing contractor invoices. But eventually, services like Patreon might make it easier to fund contributors in a highly visible way. While I’m not sure we could do away with every legal need, it’s worth imagining a world where we don’t need to associate a legal entity with the project at all.


## Foundations as a governance tool


When we take out legal and financial services, what’s left? Historically, software foundations were used to manage governance issues, and that’s where I’d like to see us think a little harder about our options today.


If a project is wildly successful, it’s rare that it will continue to grow without *any* governance conflicts. [3] A few scenarios that might emerge:

- There’s one company or person behind the project, who doesn’t want to be seen as the BDFL (“benevolent dictator for life”)
- Spinning the project out of a company’s “incubation”
- Several companies contribute paid engineers to a project, who want to work together more intentionally
- Independent contributors are getting lost in the shadow of a major entity (ex. a company) who’s strategically contributing a lot of developers


Most of these problems have to do with separating the project out from corporate influence. In the early 2000s, software foundations became the standard response to these issues.


Some foundations tried to lean *out* of the corporate problem by requiring that developers only contribute code as themselves. While I find this approach admirable, there are plenty of projects whose major contributors all work for the same company, whether they’re explicitly affiliated or not. (Several corporate contributors have told me they “launder” their contributions to avoid detection.)


Other projects leaned *into* the corporate problem by setting up foundations with a “pay-to-play” model, where companies donate large sums of money in exchange for formal recognition. As mentioned earlier, this approach can take a life of its own, where an overfunded foundation loses focus, and their mission begins to diverge from that of the project.


When a foundation is involved, the typical governance model looks something like this:


FOUNDATION - COMPANY

 | 

PROJECT


Or, perhaps the project is effectively “donated” to the foundation, so the model looks like this:


FOUNDATION

 | 

PROJECT


I find both these models problematic for all the reasons previously described. In either case, we’ve managed to *formalize* one or two points of failure for *“the project”*, which is otherwise inherently distributed.


Open source projects are often conflated with the people or organizations who represent them. But just as “the government” is not “the people”, but rather a representative body whose legitimacy derives from sustained popular support, “the foundation” is not “the project”, and should not be treated as such.


## A distributed, not oligarchic, system


So how do we avoid the monopoly of the foundation model, or the oligarchy of the foundation-company model? If we return to the original question of how to maintain project independence, another way to check corporate power is to actively minimize their influence in the ecosystem: basically, turn the model upside down. Something like this:


PROJECT

 | 

ENTITY(0)...ENTITY(n)


Rather than checking power with more power, the intended approach is to dilute all central nodes of influence over time, using a decentralized model. Doing so upholds the sovereign power of the project, where companies are merely participating actors within, rather than the other way around.


How does this work in practice? Early on, there’s usually one person or company who’s responsible for the creation of a project. Let’s call them **Entity(0)**. At this stage, centralization is desirable, because getting things off the ground requires a high degree of coordination. You’d expect to see one or a few people writing most of the code, and/or one company funding the work.


The medium-to-long term goal, however, is to distribute the *opportunity* for contribution across multiple locations. I emphasize “opportunity” because I think it’s conceivable that Entity(0) continues to be the only major actor, if they earn and maintain the trust of their community. But the community (i.e. *“the project”*) should be able to eject or impeach them if they fail to do a good job.


It might be tempting to imagine Entity(0) hiring and paying for all of the project’s development, particularly if they have the capital. Instead, Entity(0) should actively prioritize: *“How do we get other entities to participate?”*


Entity(0) should try to find major contributors who aren’t funded or supported by them. They might continue to fund a few contributors themselves, and they might coordinate their contribution efforts with others. But the goal of Entity(0) is to make themselves just *one* actor in the ecosystem, rather than a single point of failure. And, as part of this social contract, it’s the community’s job to hold them to it.


While not every company is a good actor, it’s more likely that companies *can* make themselves obsolete, versus foundations, because they aren’t structurally designed to be the only governing body.


You might ask yourself, *“Why would Entity(0) do this?”* Because in the long run, it’s better for them. When an open source project succeeds, it looks more like a standard than an organization, and standards succeed when they propogate. Rather than a sign of failure, attracting other funders is a sign of demand, which increases the value of the entire ecosystem and ultimately benefits Entity(0). Another way of saying this: there’s a reason why it’s easy to get paid as a Linux developer.


Finally, some projects, particularly in the cryptocurrency space, are lucky to have financial assets large enough that they don’t make sense to funnel through a fiscal sponsor. Although the common approach is to create a foundation to hold these assets, I’d like to suggest two alternatives:

1. Entity(0) holds the assets and uses them to drive early adoption and development
2. Funds are distributed to major or strategically desirable contributors, who help drive adoption and development (ex. [Handshake](https://www.coindesk.com/handshake-revealed-vcs-back-plan-to-give-away-100-million-in-crypto/) and [Decred](https://www.coindesk.com/one-of-investors-favorite-governance-blockchains-is-handing-over-20-million/))


Much like language, religion, or etiquette, successful open source projects should exist beyond the control of any one company or foundation. Given the tools at our disposal today, we should be able to design governance solutions that better align with one of open source’s greatest strengths: a distributed, resilient organizational culture.


### Notes


*Thanks to [Mikeal Rogers](https://twitter.com/mikeal) for feedback on an early draft of this post.*

1. While there are some 501(c)(3) software foundations, many are 501(c)(6)s. Both fall into the [501(c) nonprofit category](https://en.wikipedia.org/wiki/501(c)_organization), but the latter is used for trade associations. 501(c)(6)s are a popular format, in part, because they’re easier to get IRS approval, who were historically suspicious of the idea of “software nonprofits”. 501(c)(6)s also lend themselves better to the “pay-to-play” model that plagues software foundations today, although I don’t know whether form followed function or the other way around. ↩
2. Not all software foundations are 501(c)s, which is the nonprofit tax designation in the United States. I’m only focusing on 501(c)s in this post because they’re extremely prevalent among software foundations, even internationally. ↩
3. Side bar: when does a project even need to formalize its governance? I have a pet theory (confidence: medium) that projects only need to define governance at the first sign of conflict. Too often, we do things based on what we think others want, when it turns out nobody actually wanted it at all. In theory, if you scaled to thousands of happy contributors and millions of happy users without anybody raising concerns about who’s running the thing, I’m not sure why you really need to define anything. Maybe you can’t avoid the governance conversation forever, but I definitely think some projects worry about it earlier than they need to. ↩


---


*For future updates, subscribe via [newsletter](https://nayafia.substack.com/) or [RSS](https://nadia.xyz/feed.xml). Get in touch via [Twitter](https://twitter.com/nayafia).*

Google tag (gtag.js)