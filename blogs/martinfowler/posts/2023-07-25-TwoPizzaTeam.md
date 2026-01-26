---
title: "Two Pizza Team"
description: "A two-pizza team is a small team   that fully supports software for a particular business capability. The term   became popular as it used to describe how Amazon organized their software staff."
date: 2023-07-25T00:00:00
tags: ["team organization"]
url: https://martinfowler.com/bliki/TwoPizzaTeam.html
slug: TwoPizzaTeam
word_count: 579
---


A two-pizza team is a small team
  that fully supports software for a particular business capability. The term
  became popular as it used to describe how Amazon organized their software staff.


The name suggests the most obvious aspect of such teams, their size. The
  name comes from the principle that the team should no larger than can be fed
  with two pizzas. (Although we are talking about American Pizzas here, which
  seemed alarmingly huge when I first encountered them over here.) Keeping a
  team small keeps it cohesive, forming tight working relationships. Typically I
  hear this means such teams are about 5-8 people, although my experience
  suggests that the upper limit is somewhere about 15.


Although the name focuses solely on the size, just as important is the
  team's focus. A two-pizza team should have all the capabilities it needs to
  delivery valuable software to its users, with minimal hand-offs and
  dependencies on other teams. They can figure out what their customer needs,
  and quickly translate that into working software, able to experiment and
  evolve that software as their customer's needs change.


Two-pizza teams are [Outcome Oriented](https://martinfowler.com/bliki/OutcomeOriented.html) rather than
  [Activity Oriented](https://martinfowler.com/bliki/ActivityOriented.html). They don't organize along lines of skills
  (databases, testing, operations), instead they take on all the responsibilities
  required to support their customers. This minimizes inter-team hand-offs in the
  flow of features to their customers, allowing them to reduce the cycle-time
  (the time required to turn an idea for a feature into code running in
  production). This outcome-orientation also means they deploy code into
  production and monitor its use there, famously responsible for any production
  outages (often meaning they on the hook for off-hours support) - a principle
  known as âyou build it, you run itâ.


Focusing on a customer need like this means teams are long-lived, [Business Capability Centric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) teams that support their business
  capability as long as that capability is active. Unlike project-oriented teams -
  that disband when the software is âdoneâ - they think of themselves as
  enabling and enhancing a [long-lived
  product](https://martinfowler.com/articles/products-over-projects.html). This aspect often leads to them being referred to as **product
  teams**.


The wide scope of skills and responsibilities that a two-pizza team needs
  to support its product means that although such teams can be the primary
  approach to team organization, they need support from a well-constructed
  software platform. For small organizations, this can be a commercial platform,
  such as a modern cloud offering. Larger organizations will create their own
  internal platforms to make it easier for their two-pizza teams to collaborate
  without creating difficult hand-offs. [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html)
  provides a good way to think about the different kinds of teams and
  interactions required to support two-pizza teams (Team Topologies calls them
  **stream-aligned teams**).


For business-capability centric teams to be effective, they will need to
  make use of each others' capabilities. Teams will thus need to provide their
  capabilities to their peers, often though thoughtfully designed APIs. This
  responsibility for such teams to provide services to their peers is often
  overlooked, if it doesn't happen it will lead to sclerotic information
  silos.


Organizing people around business capabilities like this has a profound
  interaction with the way the software for an organization is structured - due
  to the effect of [Conways Law](https://martinfowler.com/bliki/ConwaysLaw.html). Software components built by
  two-pizza teams need well-controlled interactions with their peers, with clear
  APIs between them. This thinking led to the development of [microservices](https://martinfowler.com/microservices/), but that's not the only approach -
  well-structured components within a monolithic run-time is often a better
  path.
