---
title: "The strong and weak forces of architecture"
description: "Good technical design decisions are very dependent on context. Teams   that regularly work together on common goals are able to communicate regularly and negotiate changes quickly.  These teams exhibi"
date: 2021-11-10T00:00:00
tags: ["application integration", "enterprise architecture", "collaboration"]
url: https://martinfowler.com/articles/strong-weak-arch.html
slug: strong-weak-arch
word_count: 1676
---


Technology governance and what is considered ‘good architecture’ is mostly considered with a ‘one size fits all’ approach. Many
    organisations try to apply the same strict governance at all levels -
    limiting tech choices, and disempowering teams. Others have allowed teams
    complete autonomy at all levels, meaning teams are left to make their own choices with no constraints at all. Neither of those approaches are
    ideal.


Taking a specific example, we’ve long seen integration architects striving
    for the 'one true' integration approach at all levels of the architecture.  They cite 'best practice', mandating extremely
    loose coupling, backward compatible interfaces, and careful encapsulation for every system interaction at all levels. This universal approach has created a lot of unnecessary complexity and delay in many cases - but how do you work out where it's ok to move faster and ease those requirements?


## Teams at MYOB


At [MYOB](https://www.myob.com/) we have arranged our teams according to well-proven principles for modern digital product organisations.  Teams are aligned to our product capabilities and business capabilities, and are responsible for all aspects of planning, delivery, maintenance, and support for their software and infrastructure.


Teams are grouped into *Domains* which bring together related capabilities, with some leadership and enabling roles working at the domain level.  Domains are further grouped into much larger organisational units called *Verticals*.  The verticals represent a major segment of our customer base.


There is much more to it of course, with supporting functions and internal platforms which provide scaffolding for the whole organisation to deliver effectively.  However this simplified model is useful for reasoning about technology governance.


![](strong-weak-arch/overall.png)


In this article I'd like to explain how this structure informs our tech choices and
      design decisions, with potentially different approaches being suitable
      depending on the scope (or ‘blast radius’) of the decision. The conceptual
      model I like is the forces of attraction between different parts of the
      organisation.


## Within a domain = strong forces


Within a domain we have multiple teams, each being responsible for some capabilities and underlying systems within the domain. Sometimes this is perfectly aligned, with
      each team being custodians of a neatly bounded set of systems. More often
      this is imperfect in reality, with custodianship of some systems being
      shared across teams - often for legacy reasons. For teams within
      a domain, there is a very strong force of alignment.


![](strong-weak-arch/strong.png)


The domain structure aims to bring together systems that
      are cohesive in function - they’re closely related, they deal with the same
      concepts, they rely on common domain expertise, and they quite often change
      at the same time in order to meet a customer need.


The members of a single team are usually working across the same systems,
      and so need a very clear and aligned way of working, standards, technology
      choices, and design directions. This is the strongest force of
      alignment.


Between teams in the same domain, alignment forces are still very strong.
      Sharing of knowledge is easy and fluid. Negotiating over system interactions e.g. schemas is relatively very easy. When a feature needs to be delivered
      that cuts across the systems in the domain, often the same people will
      implement ‘both sides’ of each point of integration.


This means that the ‘private’ interactions between the systems inside a
      domain - API calls, events, data files - can have tighter coupling without having as severe a cost.  By allowing some tighter coupling, we can reduce the amount of effort that goes into versioning and backward compatibility and avoiding
      shared dependencies. Coupling between systems at a domain level is not
      always the evil monster that must be vanquished at all costs, in fact
      coupling at this scope can be a useful thing.


## Within a vertical = weakened forces


In the middle ground we have our vertical structure, with multiple
      domains. The social distance between the people in one domain and another
      is getting stretched. This makes negotiation and reaching alignment more
      strained and slower, and so necessarily this impacts our technology
      choices and approaches.


![](strong-weak-arch/weak.png)


## Whole of organisation = weak forces


When we zoom out to all of the organisation - the force of alignment
      between the verticals is very weak indeed. It is quite hard to make changes atomically across the landscape - mostly because the prioritisation of work for each vertical is deliberately independent.  Co-ordinating work at this level is necessarily much slower and limiting. This means our design decisions and approaches need to adapt accordingly.


![](strong-weak-arch/all.png)


## How do we apply this model?


Lets make this model more concrete by exploring some areas of technology decision-making that may vary depending on their scope.  The list below is not intended to be exhaustive - just a few interesting examples to consider.


### Technology choices

How do we govern the lifecycle of technology
          choices?

#### Domain (strong force)


Within a single domain there should be a small set of technology
            choices agreed.


Often this follows [Default Trial Retire](https://martinfowler.com/bliki/DefaultTrialRetire.html)
             for each class of
            technology required.


Informal governance through technology leadership is usually
            highly effective.


#### Vertical (weakened force)


At a vertical level there would be a slightly larger set of
            agreed technology choices, to cater for the differing needs of the
            multiple domains.


It is beneficial for the vertical to be
            able to move people closer to high priority work, so keeping aligned
            on technology is important here.


More formal sharing of solution options and proposals keeps
            choices aligned effectively.


#### Whole of org (weak force)


The weakest force for aligning and governing technology choices
            is at the whole of org level.


The MYOB technology radar sets direction in terms of preferred
            technologies.


Solution options and proposals encourage dialog and improve
            alignment.


### Shared code and infrastructure

Can we share codebases and internal libraries for re-use?  Can we
          share infrastructure to reduce duplication?

#### Domain (strong force)


Within a single domain, even across 3-5 teams, we should have high
            bandwidth communication and a short distance to empowered leadership.


This means that when a change needs to be made to shared code or
            infrastructure, we can quickly inform and prepare for the changes.


The coupling introduced by shared code and infrastructure has less impact, and
            the benefits often outweigh the costs.


#### Vertical (weakened force)


Sharing code, artefacts, and infrastructure can often be managed at a
            vertical level - but the drag introduced should be carefully monitored.


#### Whole of org (weak force)


Shared code at a whole of organisation level is limited to highly stable,
            highly useful things. Mostly these things are limited to libraries which can
            be distributed and versioned, and changed carefully.


Shared infrastructure is similar - at an org-wide level, shared infrastructure
            must have very high value, and be well-encapsulated (“as a service”,
            self-service).  It should very rarely need a core change in response to a need
            from a single team.


### Code Contribution models

Can teams contribute code changes into other team's codebases, to
          avoid waiting for the other team to do the work?

#### Domain (strong force)


Within a single domain - with high degrees of alignment in terms of
            practices and technology - it can be quite reasonable for teams to contribute
            code across team boundaries, with a type of collective code ownership extending to the whole domain.


Custodianship of each system should still be clearly understood, usually best kept within
            one team.


#### Vertical (weakened force)


Within a vertical it is common for code contribution to happen across systems, e.g. pull requests in source control - with only small amounts of delay and re-work required.


#### Whole of org (weak force)


At the whole of org level, it is often quite difficult (and sometimes
            harmful) to effectively manage contributions that cross verticals.


This is particularly true where systems are complex in nature, highly
            critical or sensitive in terms of accuracy, performance, privacy and
            compliance.


When completely new system features are being established, it can work well to collaborate across verticals even doing pair-programming together.  However as features are established and demand increases for changes from other verticals, 
            investment is required to make those systems safe to extend and configure.  Those changes
            are often architectural in nature - separating the ‘core’ and complex subsystems
            and introducing modularity to make extension easier to manage.


### Integration Patterns

How will we connect systems together?

#### Domain (strong force)


Systems that are owned within a single domain are relatively easy to
            change in a closely co-ordinated way. For example this means (slightly)
            less effort needs to be burned on maintaining backwards-compatibility of
            interfaces.


Even ‘forbidden’ approaches like database-level integration will have less
            impact within the systems in a single domain.  Although we shouldn’t build a
            system that way deliberately, if it exists then we can contain the impact
            within a single domain.


#### Vertical (weakened force)


Changes that must be co-ordinated across multiple domains within a vertical should be rare, but can be managed when absolutely necessary.  [Expand-contract changes to API contracts](https://www.thoughtworks.com/radar/techniques/api-expand-contract) is quite effective where the impacts are contained within the vertical.


#### Whole of org (weak force)


APIs and interfaces (e.g. events) that are published to the whole of
            MYOB must have the highest attention to published schemas, versioning,
            backwards compatibility, contracts, and deprecation strategy.


The impact of highly-coupled integration (e.g. ETLs, database integration) is
            very high, and should be absolutely avoided.


## Conclusion


In any organisation of non-trivial scale many dozens of technology decisions are made every day. We've strived for many years to enable and empower teams to make decisions closer to the work, without strict centralised governance over every single decision.  Achieving  'aligned autonomy' is no easy feat, and requires constant balancing and adjustment. Simple models can help teams understand how to make good decisions in context.  In this article I've described how at MYOB we've aligned our technology governance approach to our organisational structure and dynamics. Being aware of these forces of alignment within our organisation allows us to understand what is going to be easy and what is going to be hard, and make better technology choices as a result.


---
