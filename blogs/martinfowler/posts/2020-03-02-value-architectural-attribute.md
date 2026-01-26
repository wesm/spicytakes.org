---
title: "The Elephant in the Architecture"
description: "We, and our colleagues, are often called on to perform architectural     assessments for our clients. When we do this, the architects involved with     these systems will talk about the performance of"
date: 2020-03-02T00:00:00
tags: ["enterprise architecture", "technical leadership", "collaboration"]
url: https://martinfowler.com/articles/value-architectural-attribute.html
slug: value-architectural-attribute
word_count: 2794
---


We, and our colleagues, are often called on to perform architectural
    assessments for our clients. When we do this, the architects involved with
    these systems will talk about the performance of these systems, how
    resilient they are to faults, and how they are designed to evolve to
    easily support new capabilities. The elephant that rarely comes up,
    however, is how
    different systems contribute to business value, and how this value interacts
    with these other architectural attributes.


Without understanding value, many architectural decisions become much
    harder to make. In one example we were asked about adding fault tolerance to
    a trading system. The cost of doing this, via a hot fail-over to another server, was
    in the range of tens of thousands of dollars. Could this cost be justified?
    Our approach to this was to ask about the value of trades that passed
    through the system and how much revenue this provided to the client. Once
    they looked into it, and saw the systems were handling millions of dollars a
    day in trades, adding fault tolerance was trivially easy to justify.


The important thing about this story isn't the fact that the client team
    neglected to ask about value as part of their decision-making (although
    there's certainly a lesson in there). The point is that the architecture
    team didn't know what the value of their systems were, or how different
    components contributed to the broader business performance. We find this to
    be a common gap in thinking, when we do these assessments we usually ask to
    talk to the relevant people from the finance department. That's usually
    greeted by âwhy would you want to talk to them?â


In another example we were asked by an insurance company to help break
    their monolithic system into microservices. They had identified, reasonably,
    that they wanted to separate them by different product lines (home,
    personal, car, etc). What they didn't know was what proportion of the
    company's profits came from each of these product lines, which is an
    important element in deciding priorities for a breakup like this. The first
    item to separate probably shouldn't be the most important one in value
    terms, since the first separation will carry the many risks of doing something for
    the first time. But once a team is practiced with the separation, then we
    should get the most valuable product line separated to make it easier to
    modify and scale.


## Examine the architecture with value stream mapping


A good first step in assessing the business value in your architecture is
      to
      do a value stream mapping
      that focuses on the various systems and components in the IT landscape.
      Business often do some kind of value-stream mapping for business processes,
      examining how each part of a customer journey impacts revenue and margin,
      but often once they reach IT the mapping stops and no attempt is made to
      map value streams through the various systems.


Architects should build on this, allocating similar business measures to the
      systems that support business processes by extending the mapping into
      those systems. As well as financial measures, important non-financial measures
      can also be looked at - to what extent does your customer's ability to check
      their claim status online affect customer retention? (Such measures are usually
      more difficult to make, but thinking about how to measure them can often yield
      important insights.)


With a recent client we conducted such an exercise, starting with customer
      journeys that described how customers interacted with the client company. We
      put these steps on the top of a wall in the team room, and then tied each
      step to the systems and components in the client's IT portfolio. We could
      then assess how each system contributed to the step in the customer journey
      and what the effects of a failure might be.


## Consider the business value impact of failures


As our first example suggested, there's a particular importance when it
      comes to assessing consequences of failures. If we want to take measures to
      improve the resilience of a system, it's good to express it in terms of the
      value at risk should it fail. One retailer was struggling to justify testing
      the backup restoration process for their inventory database. With a large
      backlog of business-visible features needed before the Christmas season, it
      was hard to prioritize such a technical task. Our suggestion was to ask how
      the business felt about a database crash on Black Friday: what would be the
      cost, how quickly would they want the system back up? These questions led to
      a business-led decision around doing dress-rehearsals for database restores
      and reducing the time to recovery that otherwise would be buried in IT's
      work queue.


When doing an assessment of value that would be at risk, it's worth approaching in two
      complimentary ways. One route is to go top-down, looking at a business
      function and identifying which software systems support that function. The
      other is the reverse, starting with a software system, and considering what
      ramifications a failure here would have.


An important part of analyzing how much value is at risk is recognizing that, since
      different failures have differently severe consequences, all [Software Components](https://martinfowler.com/bliki/SoftwareComponent.html) do not need the same levels of resilience. Imagine a failure of a
      stock management system on Boxing Day (a British equivalent to Black
      Friday). If that means we can't check stock levels, we either confirm orders
      we can't fill, or don't take orders - both of which cause a significant
      loss. However a failure in a fulfillment system might have orders sitting on
      queue waiting to process, which may lead to delayed deliveries. Business
      leaders may consider the latter a lesser concern, and thus be prepared to
      live with lesser resilience for that system. Whatever the particulars, the
      key is that the level of resilience is a business decision. Similarly with
      data consistency. When looking at distributed databases, architects often
      balk at relaxing consistency for availability. But the business cost of
      double-booking a few hotel rooms may be much less worrying than not taking
      bookings at all.  The trade off between consistency and availability,
      enshrined in the CAP theorem, is a business decision, not a technical
      one.


## Cross-functional requirements should be justified by business value


A theme here is that we shouldn't just be assessing the value of
      features, but also of system characteristics that are often categorized as
      cross-functional requirements (our preferred name for non-functional
      requirements, or âilitiesâ). If we want our systems to adhere to some
      technical standard, then we need to understand what value is lost by failing
      to do that - and communicate that value to non-technical stakeholders.
      Assessing value for CFRs is often difficult, and many technologists shy away
      from the resulting debate. But failing to do this does more harm than just
      the risk of over-investing in low-value technology. It also erects a real
      barrier to the collaboration between technologists and their users.


Understanding value should inform decisions about the flexibility of
      components. One client had a payment processing component that was
      programmed to work with a particular payment processing company. They wanted
      it to be easily configurable so they could adjust it quickly should the
      payment processor change. Two broad options existed. One would hard-code the
      interaction with the payment provider's system in the payment processing
      component, while the other option made all such interactions be configurable. The
      configurable option would allow the payment provider to be changed by
      altering a configuration file in a few days. As is usually the case,
      however, such configurablity would add complexity to the component's code
      that would increase the cost of any other changes. This is a common
      trade-off with configurablity - you ease changes in the configurable bits at
      a cost of harder changes elsewhere. The vital piece of business context here
      was that the hard part in changing a payment provider was actually
      negotiating a new legal contract - an exercise that usually took over a year
      to do. So configuring the provider information here wasn't worth it, as
      modifying a non-configurable component was still much quicker than legal
      negotiations.


## Business value implies CFRs vary by component


The last two examples both illustrate that having a âone size fits allâ
      approach to things like resilience and flexability can be unhelpful and
      wasteful. Several years ago we worked with an organisation that had decided
      to impose a blanket âfive ninesâ availability requirement, amazingly they
      even applied this to the sandwich ordering system used by staff to reserve
      their favourite lunchtime snack. We've found agreeing different tiers of
      service with the business can be very useful, for example does loss of a
      service immediately impact customer experince or revenue, or can we afford
      for it to be down for a few hours while a database is restored?


Another issue that can be highlighted by understanding how systems support
      business value is where a single component has to support multiple different
      value flows and levels of reliablilty. This is common in monolithic components
      where multiple different business processes are supported and can be an
      important motivation for breaking things apart, for example allowing us to only
      pay the premium for high availability when justified by the corresponding business
      value


## Use monitoring to assess business value


We're big fans of using rich monitoring to get a better understanding of
      how systems behave, something that's particularly important with the growing
      complexity of increasingly distributed systems. Such monitoring is often
      focused on system health, supporting [QA in production](https://martinfowler.com/articles/qa-in-production.html). But we can also
      use this kind of monitoring to assess the contribution of systems to
      business value - such as determining how much sales revenue passes through a
      particular component. One retail client found that
      monitoring queue lengths and message rates on their mainframe could be a good
      proxy measure for revenue taken in each of their shops, while not accurate
      making this available to the business stakeholders let them spot issues that
      monitoring from a purely technical perspective might have missed. Another
      client was able to derive an accurate revenue measure for every transaction
      on their web site and they displayed this minute by minute on screens around their
      offices. Over time far more attention was paid to these than the screens
      showing CPU, memory and other technical measures.


One might argue that gathering such data isn't part of understanding
      the system's behavior, but we would assert that this is vital intelligence
      in understanding the contribution software components make to the
      business. As more systems get hosted on clouds, we can see bills generated
      for individual FaaS functions. If we can get costs to this granularity, we
      should also strive to gather data on benefits too.


Regular monitoring data can inform investment decisions all on their
      own. We came across a government agency that used the web to provide
      services to its citizens. Its costs for adding new features to its web
      application were being significantly increased by the cost to support
      older browsers - which was considered mandatory for those citizens that
      couldn't upgrade. Looking at the traffic revealed that so few citizens
      used such older browsers that rather than supporting the old browser, it
      would be cheaper to give them a new computer and a bunch of flowers.


## If you're moving to the cloud, take just the valuable bits


With this rise of cloud systems, we are seeing many organizations wishing
      to move their software systems to cloud hosting. This parallels a long
      history of system replacements, where companies look to replace existing
      systems with something that supports the same capabilities but runs on more
      modern (and hopefully more efficient) infrastructure. With several decades
      of seeing these kinds of efforts during our careers, we've seen that there
      are easy mistakes to make. Perhaps the most common of these is the idea that
      the simplest way to do a system replacement is a feature-parity replacement
      that seeks to exactly mimic the existing functionality on a new platform.
      Such a like-for-like approach misses the fact that much existing
      functionality is of little value, some not used at all, and some actively
      interfering with an optimal business process. A feature-parity replacement is
      harder than people usually think, and taking the time to avoid copying
      little-used functions pays for itself easily.


One organisation we worked with kicked off a migration effort by moving
      100% of their logistics handling code into a new system, this took several
      months and involved many of their development staff. When we talked to the
      business about their future plans they explained they planned to drop support
      for many kinds of packaging due to high costs. Dealing with all the edge
      cases around the packaging turned out to be the thing that consumed most
      time on the migration, and yet the business would have been happy without it.


Understanding the contribution to business value can thus be a
      significant help in identifying how to do a better re-platforming effort. If
      existing components aren't contributing much value, then they shouldn't be
      copied into the new platform. A common case here is a service company that
      has most of its services follow a few common cases, but has a few unusual
      offerings that only come up rarely. Such unusual cases often involve special
      software support - but such marginal cases should always be reviewed before
      they are re-implemented on a new platform. If the business expects to stop
      oferring this service in the next six months, that's something that should
      be understood as part of the re-implementation plan.


## Business value is vital but inconstant


As with anything in life or software architecture, such assessments of
      value aren't constant. We worked with an insurance company that had a
      competitive advantage through its rating model. This software was seen as
      one of the company's crown jewels. But over time there was a big shift to
      doing insurance quotes on-line with straight-through processing. The crown
      jewel required lots of parameters, which could reasonably be captured in the
      pre-online era with an agent meeting with the customer, but the complicated
      form was too unappealing on the web. With this shift the value of their
      crown jewel withered away. So as well as getting an understanding of the
      current value of software assets, it's worth trying do a rough forecast of
      how that value is affected by changes in the technical and business
      environment.


Another case was retailer whose catalog management system coped
      comfortably with updating twice a year, but couldn't deal with the shift to
      rapid online changes. The opportunity cost of lost revenue is never an easy
      thing to quantify, but it needs to be considered when deciding where to
      place an investment in restructuring or rewriting components.


## Business knowledge should be part of a technical career path


When people look at the growth of technical leaders, most attention
      tends to go into “hard” technical subjects. Training courses (certified,
      no less) abound for various software platforms. For technical skills
      development we advocate training that focuses on core principles rather
      than today’s popular platform. Wise skill development realizes that the
      much more difficult area of “soft” skills (note our irony-quotes)
      become increasingly important as folks rise up the leadership ladder, and
      that's something we endorse too. 1


1: 
      These are called “soft” skills because they are harder than “hard” skills.


Valuable though these things are, we also think it's vital to ensure
      technical leaders have a firm understanding of the business they operate
      in, and how value is generated by the various players in the domain. This
      is usually not something that comes through training courses, rather it's
      something that comes through regular interaction with business leaders.
      This social interaction should begin early in a technologist's career. The
      notion that separating IT staff from business staff causes untold ills to
      such a profession like software development whose value is rooted in how
      much software is deeply entwined in the activity of the enterprise it
      supports. Developers need to learn early on that constant contact with
      their users and customer is normal, and learn how to do it well. Years of
      such contact reap great rewards when they become leaders and are familiar
      with those in the business that they have grown up with.


The barriers in communication between business and IT has been one of
      the sadly enduring themes of our long careers in software development.
      When architects are disconnected from the understanding the flow of
      business value, it raises costs both in wasted technical effort and in
      loss of opportunities presented by changes in the environment. Software
      leaders need to put more attention into the interplay of business
      activities and software decision making, and ensure that this is part of
      the career development process for all the technical staff.


---
