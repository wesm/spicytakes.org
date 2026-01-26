---
title: "Conway's Law"
description: "Conway's Law(formulated in 1968 by     Melvin Conway) says that a system's design is constrained by the     communication patterns of its designers. Birgitta, Mike, James, and I     discuss the meanin"
date: 2022-11-03T00:00:00
tags: ["team organization", "enterprise architecture", "application architecture"]
url: https://martinfowler.com/bliki/ConwaysLaw.html
slug: ConwaysLaw
word_count: 1500
---


Pretty much all the practitioners I favor in Software Architecture are deeply
  suspicious of any kind of general law in the field. Good software architecture
  is very context-specific, analyzing trade-offs that resolve differently across a wide range
  of environments. But if there is one thing they all agree on, it's the importance
  and power of Conway's Law. Important enough to affect every system I've
  come across, and powerful enough that you're doomed to defeat if you try to
  fight it.


The law is probably best stated, by its author, as:  1


1: 
      The source for Conway's law is [an
      article](https://www.melconway.com/Home/Committees_Paper.html) written by Melvin Conway in 1968. It was published by Datamation,
      one of the most important journals for the software
      industry at that time. It was later dubbed “Conway’s Law” by Fred Brooks
      in his hugely influential book [The Mythical
      Man-Month](https://www.amazon.com/gp/product/0201835959/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201835959&linkCode=as2&tag=martinfowlerc-20). I ran into it there at the beginning of my career in the
      1980s, and it has been a thought-provoking companion ever since.


> Any organization that designs a system (defined broadly) will produce a
>     design whose structure is a copy of the organization's communication
>     structure.
> -- [Melvin Conway](https://www.melconway.com/Home/Conways_Law.html)


Conway's Law is essentially the observation that the architectures of
  software systems look remarkably similar to the organization of the
  development team that built it. It was originally described to me by saying
  that if a single team writes a compiler, it will be a one-pass compiler, but
  if the team is divided into two, then it will be a two-pass compiler. Although
  we usually discuss it with respect to software, the observation applies broadly
  to systems in general. 2


2: 
      As Conway mentions, consider how the social problems around poverty, health
      care, housing, and education are influenced by the structures of government.


![](images/conwaysLaw/card.png)


As my colleague Chris Ford said to me: âConway understood that software
  coupling is enabled and encouraged by human communication.â If I can talk
  easily to the author of some code, then it is easier for me to build up a rich
  understanding of that code. This makes it easier for my code to interact, and
  thus be coupled, to that code. Not just in terms of explicit function calls,
  but also in the implicit shared assumptions and way of thinking about the
  problem domain.


We often see how inattention to the law can twist system architectures. If
  an architecture is designed at odds with the development organization's
  structure, then tensions appear in the software structure. Module interactions
  that were designed to be straightforward become complicated, because the teams
  responsible for them don't work together well. Beneficial design alternatives
  aren't even considered because the necessary development groups aren't talking
  to each other.


A dozen or two people can have deep and informal communications, so Conways Law
  indicates they will create a monolith. That's fine - so Conway's Law doesn't
  impact our thinking for smaller teams. It's when the humans need organizing
  that Conway's Law should affect decision making.


The first step in dealing with Conway's Law is know not to fight it. I
  still remember one sharp technical leader, who was just made the architect of a large
  new project that consisted of six teams in different
  cities all over the world. “I made my first architectural decision” he told
  me. “There are going to be six major subsystems. I have no idea what they are
  going to be, but there are going to be six of them.”


This example recognized the big impact location has on human communication.
  Putting teams on separate floors of the same building is enough to
  significantly reduce communication. Putting teams in separate cities, and time
  zones, further gets in the way of regular conversation. The architect
  recognized this, and realized that he needed take this into account in his
  technical design from the beginning. Components developed in different
  time-zones needed to have a well-defined and limited interaction because their
  creators would not be able to talk easily.3


3: 
      While location makes a big contribution to in-person communication
      patterns, one of the features of [remote-first](https://martinfowler.com/articles/remote-or-co-located.html#remote-first) working, is that it reduces the role of
      distance, as everyone is communicating online. Conway's Law still applies,
      but it's based on the online communication patterns. Time zones still
      have a big effect, even online.


A common mismatch with Conways Law is where an [ActivityOriented](https://martinfowler.com/bliki/ActivityOriented.html)
  team organization works at cross-purposes to feature development. Teams
  organized by software layer (eg front-end, back-end, and database) lead to
  dominant [PresentationDomainDataLayering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) structures, which is
  problematic because each feature needs close collaboration between the layers.
  Similarly dividing people along the lines of life-cycle activity (analysis,
  design, coding, testing) means lots of hand-offs to get a feature from idea
  to production.


Accepting Conway's Law is superior to ignoring it, and in the last decade,
  we've seen a third way to respond to this law. Here we deliberately alter the
  development team's organization structure to encourage the desired software
  architecture, an approach referred to as the **Inverse
  Conway Maneuver** 4. This approach is often talked
  about in the world of [microservices](https://martinfowler.com/articles/microservices.html#OrganizedAroundBusinessCapabilities), where advocates
  advise building small, long-lived [BusinessCapabilityCentric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) teams
  that contain all the skills needed to deliver customer value. By organizing
  autonomous teams this way, we employ Conway's Law to encourage similarly
  autonomous services that can be enhanced and deployed independently of each
  other. This, indeed, is why I describe microservices as primarily a tool to
  structure a development organization.


4: 
      The term “inverse Conway maneuver” was coined by Jonny LeRoy and Matt
      Simons in [an article](http://jonnyleroy.com/2011/02/03/dealing-with-creaky-legacy-platforms/) published in the December 2010
      issue of the  Cutter IT journal.



|  |
| Ignore | Don't take Conway's Law into account, because you've never heard of it, or you don't think it applies (narrator: it does) |
| Accept | Recognize the impact of Conway's Law, and ensure your architecture doesn't clash with designers' communication patterns. |
| Inverse Conway Maneuver | Change the communication patterns of the designers to encourage the desired software architecture. |



While the inverse Conway maneuver is a useful tool, it isn't all-powerful.
  If you have an existing system with a rigid architecture that you want to
  change, changing the development organization [isn't going to be an instant
  fix](https://verraes.net/2022/05/conways-law-vs-rigid-designs/). Instead it's more likely to result in a mismatch between developers
  and code that adds friction to further enhancement. With an existing system
  like this, the point of Conway's Law is that we need to take into account its
  presence while changing both organization and code base. And as usual, I'd
  recommend taking small steps while being vigilant for feedback.


Domain-Driven Design plays a role with Conway's Law to help define organization
  structures, since a key part of DDD is to identify [BoundedContexts](https://martinfowler.com/bliki/BoundedContext.html).
  A key characteristic of a Bounded Context is that it has its own
  [UbiquitousLanguage](https://martinfowler.com/bliki/UbiquitousLanguage.html), defined and understood by the group of people
  working in that context. Such contexts form ways to group people around a
  subject matter that can then align with the flow of value.


The key thing to remember about Conways Law is that the
  modular decomposition of a system and the decomposition of the development
  organization must be done together. This isn't just at the beginning,
  evolution of the architecture and reorganizing the human organization must go
  hand-in-hand throughout the life of an enterprise.


## Further Reading


Recognizing the importance of Conway's Law means that budding software
    architects need to think about IT organization design. Two worthwhile books
    on this topic are [Agile IT Organization Design](https://www.amazon.com/gp/product/0133903354/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0133903354&linkCode=as2&tag=martinfowlerc-20)
    by Narayan and [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) by Skelton and
    Pais.


Birgitta Böckeler, Mike Mason, James Lewis and I discuss our experiences
    with Conway's Law on the [ThoughtWorks Technology Podcast](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/reckoning-with-the-force-conways-law)


## Acknowledgements

Bill Codding, Birgitta Boeckeler, Camilla Crispim, Chris Ford, Gabriel
      Sadaka, Matteo Vaccari, Michael Chaffee, and Unmesh Joshi

    reviewed drafts of this article and suggested improvements

## Notes


1: 
      The source for Conway's law is [an
      article](https://www.melconway.com/Home/Committees_Paper.html) written by Melvin Conway in 1968. It was published by Datamation,
      one of the most important journals for the software
      industry at that time. It was later dubbed “Conway’s Law” by Fred Brooks
      in his hugely influential book [The Mythical
      Man-Month](https://www.amazon.com/gp/product/0201835959/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201835959&linkCode=as2&tag=martinfowlerc-20). I ran into it there at the beginning of my career in the
      1980s, and it has been a thought-provoking companion ever since.


2: 
      As Conway mentions, consider how the social problems around poverty, health
      care, housing, and education are influenced by the structures of government.


3: 
      While location makes a big contribution to in-person communication
      patterns, one of the features of [remote-first](https://martinfowler.com/articles/remote-or-co-located.html#remote-first) working, is that it reduces the role of
      distance, as everyone is communicating online. Conway's Law still applies,
      but it's based on the online communication patterns. Time zones still
      have a big effect, even online.


4: 
      The term “inverse Conway maneuver” was coined by Jonny LeRoy and Matt
      Simons in [an article](http://jonnyleroy.com/2011/02/03/dealing-with-creaky-legacy-platforms/) published in the December 2010
      issue of the  Cutter IT journal.


## Revisions


2022-10-24: I added the paragraph about the
    inverse Conway maneuver and rigid architectures. I also added the footnote
    about remote-first working.
