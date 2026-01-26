---
title: "How to manage a program in a product-mode organization"
description: "In their ideal state, product-mode     organizations are formed of loosely coupled, autonomous teams that     respond rapidly to articulated and unarticulated user needs. On occasion     however, oppo"
date: 2020-01-23T00:00:00
tags: ["enterprise architecture", "project planning", "team organization"]
url: https://martinfowler.com/articles/programs-in-product-mode.html
slug: programs-in-product-mode
word_count: 2961
---


## Why are programs so hard?


Organizations operating in [product-mode](https://martinfowler.com/articles/products-over-projects.html) 
      use durable, ideate-build-run teams working on a persistent 
      business issue to continuously deliver value to customers.
      Over time, through the process of removing waste in their value stream, 
      these organizations structure themselves in a way that decreases 
      the need for coordination across multiple teams often resulting in a 
      [microservices](https://martinfowler.com/articles/microservices.html) systems architecture.
      It is common for organizations operating in this way to have 
      an organizational structure that mirrors their architecture; small teams with their own backlogs 
      of work, owning and operating the systems that provide their product feature or 
      business capability.


Occasionally however, opportunities present themselves that require new features 
      and capabilities to be built in multiple areas of the organization, resulting in 
      the need for cross-team coordination to deliver the value. The coordination 
      effort involved in these initiatives is what we call programs.


Programs — where delivering customer value demands orchestration across
      multiple teams — are a real challenge for product-mode organizations.
      That’s because :

- It is hard to identify the change in operating model required to
        deliver the value of a program;
- they can challenge the autonomous culture that is common within product
        teams as programs benefit by standardizing the delivery process across
        multiple streams of work;
- leadership styles suitable for single product teams may not translate
        to the program level where multiple teams with different priorities need
        to be aligned and kept accountable.


![](programs-in-product-mode/sketch.png)


In our experience, we’ve observed both successful and unsuccessful
      programs in product-mode organizations. What follows is a fictional
      example of the difficulties of coordinating cross-team efforts in one 
      such organization inspired by real issues that we’ve encountered.


## An example: a digital-first bank wants to enter a new customer
      segment


A modern fintech company in South America has built a successful
      digital-first bank for everyday transactional consumers. Being a startup,
      it seeded its business with agile principles and have scaled the
      culture along with its architecture as it has grown.


It now employs around 200 people in its product division and the
      organizational structure is similar to the widely publicized [Spotify model](https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf) with squads and tribes aligned to the
      underlying modularized product architecture.


After a few months of user research, the bank realized it was in a 
      solid position to offer its services to a new customer segment; business 
      customers. As a result of this insight, the organization decided to put 
      a team together to with the intention of releasing the new offering 
      within a few months.


![](programs-in-product-mode/program-timeline.png)


Figure 1: The anticipated program timeline for the MVP delivery of
      the business banking product


Three leaders from existing product teams within the organization were
      identified to orchestrate the effort: a design lead, a technical lead and a
      product manager. Over some months the trio worked on a discovery and built
      a plan to establish the specifics for the first phase of delivery
      resulting in a definition of the MVP user journey and a high level story
      map.

User Goals
Tasks
Sign up for business banking
- Add business banking product to product catalog

Login to homepage
- Create business bank homepage
- Create business bank login
- Add business banking capability to customer api
- Add business banking capability to auth api

View recent transactions
- Create business bank transaction history page
- Add business banking capability to transaction api


The MVP of the program consisted of a new business account product, the
      ability to log in as a business customer and view business account
      transactions. After establishing the MVP user journey, the trio identified
      the existing product teams who would be required to deliver the scope.

Team
Ownership
Web UI
Web frontend
Customer
Customer CRM, api and database
Transactions
Transactions api and database
Auth
Authentication and authorization platform
Catalog
Product catalog api and database

The teams were typical of product teams at the organization: autonomous
      and self-managing. Each of the teams involved already had a specific
      delivery process that worked for them; some used a structured agile
      process working from a product roadmap, leading to epics and stories with
      estimates. Whereas others were more comfortable working with loosely
      defined goals broken down into small tasks.


In the interest of preserving the culture of self-organization, the
      trio chose to present the product vision to each of the product teams
      separately and allow them to figure out what changes they would need to
      deliver in order to accommodate the new customer segment. This, coupled
      with the inconsistent delivery methodologies between the teams, meant that
      the trio couldn’t foresee the number of dependencies hidden in each
      high-level user story.



|  | Add business banking product to product catalog | Create business bank login | Create business bank transaction history page |
| Web UI |  | log in page | view transactions page |
| Customer | support for new constituents | support for new constituents | support for new constituents |
| Transactions | support for new constituents |  | support for new constituents |
| Auth | support for new constituents |  | support for new constituents |
| Catalog | new business banking product |  |  |



In order to learn from the experience, at the end of the program the
      team conducted a retrospective to discover the root causes of the
      challenges they faced. This is what they discovered:

- **the operating model wasn’t changed to reflect the change in the value
        stream** and due to the trio’s desire to not challenge the culture of
        self-organization, the delivery teams optimized locally rather than
        holistically for the flow of value to the customer;
- **the organization’s leaders weren’t empowered to use their influence** to
        help the program as information on the status of the program was difficult
        to acquire;
- **progress updates focused on individual delivery team updates** as
        opposed to the broader overall working solution addressing the customer
        needs, which was a missed opportunity for alignment and focus, the teams
        weren’t aware of their contribution to the program;
- **risk management was left as an implicit task** assumed to be managed
        within the delivery teams, but not as an explicit program-level effort.
        This meant there were many surprises along the way impacting the delivery
        date;
- **unmanaged dependencies between teams and a lack of cross-team
        collaboration** led to tensions forming between the delivery teams which
        degraded the working environment and impacted individual’s morale;
- **program leadership team didn’t change their communication style to suit
        the situation**, the context and the program goals weren’t fully shared by
        the teams and leadership. There's a false sense of understanding, based on
        the assumption that everyone has the information needed to do their
        jobs;
- **overall team motivation and accountability was compromised** due to the
        other problems above.


## Best practices for managing programs in product-mode
      organizations


While hypothetical, the example above describes what we’ve seen to be
      common challenges for product-mode organizations when responding to
      cross-team coordination, program-like opportunities. We’ll use the rest of 
      this article to explain some strategies, practices and principles that we’ve 
      used successfully when working with programs similar to the one described above.


### Invest time at the beginning to set the program up for success


The beginning of the program provides a natural pause point in which
        to run focused workshops that set the teams and the program up for
        success. By the end of the program kickoff, business stakeholders and
        team members should be aware of the initiative and its significance,
        their role in it, how it’ll be delivered and the high-level scope of the
        first release. Investing time upfront in a project kickoff like this is
        proper risk mitigation for a multi-month missed delivery date. We advise
        setting aside time to run a set of workshops that provide the following
        outcomes:

- align all stakeholders on what needs to be done and why (including
          any changes to the current operating model);
- define consistent ways of working, ceremonies and best practices;
- socialize the business, technical and customer context with all teams
          involved;
- build trust across the teams by making explicit the roles,
          responsibilities and motivations of individuals;
- lay a foundation for building empathy and understanding within the
          team;
- shine a light on the risks, dependencies, assumptions and complexity
          that exists in the delivery.


An example schedule for a kickoff intending to address these outcomes
        might look like this:



|  | Mon | Tue | Wed | Thu | Fri |
| Morning | Context setting (all stakeholders) | Target architecture) | Non-functional requirements | Ways of working | Showcase (all stakeholders) |
| Afternoon | User journey mapping | RAIDs (risks, assumptions, issues, dependencies) | Trade off sliders | Story mapping & release planning | Team outing (all stakeholders) |



### Choose a leadership style that’s appropriate for the program


Depending on the organization, the current culture in the product
        division may not be receptive to the urgency and level of process
        standardization that the delivery of a program requires. Therefore, 
        program leaders, acting like solution-champions, may find that they 
        need to adapt their leadership style to the demands of the initiative.


As an example, the situational leadership model provides a useful
        description of some common communication styles in various states of
        leadership (see sidebar). In the ideal state, leaders of
        self-organizing product teams will be involving and empowering their
        teams. However, as the program may require a change in operating model
        that challenges the self-organizing nature of the product teams
        involved, leaders may need to adapt their style and spend more time
        clarifying and defining than they’re used to.


In addition to changing their communication style, program leaders
        will need to keep teams accountable for those changes required to
        support the new operating model. A commonly used tool to communicate
        responsibility and accountability is a responsibility assignment matrix
        (see RACI matrix sidebar). Something 
        like this can be used to help team members understand what’s expected 
        from them with regards to upholding process standards and attending 
        critical program meetings.


### Manage dependencies and risks diligently


Dependencies between teams (known as backlog coupling) are common in
        program delivery as multiple teams will be responsible for delivering
        different discrete parts of the solution. A good practice for
        proactively managing these dependencies is to frontload the program
        delivery with activities intended to decouple individual team backlogs,
        with a view to enabling teams to deliver more autonomously.


For example, in order to reduce the backlog coupling between the
        product teams in our example, the program team might decide to spend its
        first few iterations swarming around building a walking-skeleton (see
        Figure 7 below). Assuming a mature continuous delivery setup, the
        walking-skeleton can be deployed to production behind feature flags,
        enabling future program progress updates to focus on the evolution of
        the walking-skeleton as more fidelity and depth of scope is added by the
        product teams. Below is an example of a release plan that shows where the 
        walking skeleton swarm team fits into the product roadmap.



|  | Walking Skeleton | Release 1 | Release 2 |
| Swarm Team | low-fi UI for all screens
stubbed apis
mocked static data |  |  |
| Web UI |  | login page built on stubs
view transactions page built on stubs |  |
| Customer |  |  | full business customer support |
| Transactions |  |  | full business customer support |
| Auth |  |  | full business customer support |
| Catalog |  |  | full business customer support |



In our example above, the walking-skeleton would have consisted of
        the entire MVP user journey but with little time invested in the
        fidelity of the user interface. Moreover, all API integrations would be
        stubbed with any data mocked and hard-coded. The intention isn’t for the
        walking-skeleton to be used by a customer, but for the work that couples
        the product teams to each other to be mostly resolved before the teams
        proceed with delivery of their own backlogs. Moreover, once the
        walking-skeleton is built it allows all teams to continuously integrate
        their code mitigating the risk of late integration.


There’ll be many other risks to the delivery of the program, so
        therefore actively managing risks as part of the normal iteration cycle
        is imperative to success. Active risk management isn’t always a part of
        the standard product delivery cycle (as evidenced in the example above)
        so some discipline may be required on the part of the leadership team to
        keep the momentum going throughout delivery.


### Develop a strong communication strategy


A large part of the coordination effort in program management is
        spent on communication in order to:

- make sure all relevant stakeholders are kept informed and given the
          chance to raise issues and ask questions;
- facilitate the communication across teams to help relieve bottlenecks
          in delivery;
- surface blockers to the program leadership team so that they can help
          alleviate them.


Due to this required overhead of communication in programs, program
        leadership should look to create a strong communication strategy with
        touch points that satisfy the needs of each stakeholder group. An
        example communication strategy might look something like this:



| Touch Point | Purpose | Audience | Cadence |
| Program Standup | To surface blockers to program leadership | Representatives from each product team | Twice Weekly |
| Program Clinic | To elicit feedback and field questions from any interested
            parties | Any interested party with questions | Weekly |
| Showcase | To celebrate progress and demonstrate it back to
            stakeholders | All program stakeholders | per iteration |
| Update Email | Async communication for status updates | The organization | per iteration |
| Program all-hands | To provide status updates to the company | The organization | In line with organization all-hands |



### Invest in visual artifacts that aid in information radiation


Visual artifacts such as a physical program wall (see Figure 9 below)
        can be used as a great information radiator for the program not only to
        the benefit of key stakeholders, but also for the entire company.


A program wall can be seen as an isolated initiative in the
        beginning, but also new organizational habits and disciplines can be
        created by keeping it up to date and forcing conversations to happen
        around it. An interesting additional side benefit of physical walls is
        that they can promote collaboration and accountability among the teams.
        Moreover, program walls can help prompt questions from other people in
        the company by allowing them to consume information quickly without
        needing to schedule time with anyone.



|  | In-Flight | Done | Status | Blockers |
| Swarm Team |  | low-fi UI
stubbed-apis |  |  |
| Web UI | view transaction page | login page | green |  |
| Customer | business customer api |  | amber | future dependency on auth |
| Transactions | add business customer transaction types |  | green |  |
| Catalog |  | add business product | green |  |
| Auth | new auth for business customers |  | amber | will potentially block customer |



An ideal program wall contains just enough information to provide a
        status update at a glance. From the example above we can tell that the
        swarm team has completed its work and disbanded, and that the delivery
        teams are now working through their deliverables with one of the teams
        in need of some assistance to remove a future blocker.


### Don’t be afraid of having a defined role for managing the program


We believe that the discipline of program management is crucial to
        ensuring success when any initiative involves the orchestration and 
        coordination of multiple teams to deliver value. However, the actual role definition and
        responsibilities will depend on the organizational context and program 
        complexity and therefore we prefer to call this role âsolution championâ as opposed to program manager. 
        Fundamentally though, there needs to be someone who is responsible 
        for the overall health of the initiative focusing their efforts on the 
        following strategic elements:

- continually ensuring alignment between teams;
- ensuring that communication flows smoothly between the teams and
          external stakeholders;
- keeping relevant and critical information fresh;
- managing program dependencies and risks.


It’s important to make sure the responsibilities of the role are made explicit 
        to everyone involved, preferably at the program kickoff. A risk we have observed 
        when introducing solution champions at product-mode organizations is that product 
        team members and the solution champion can end up with overlapping responsibilities,
        making both roles less effective. As mentioned, solution champions should
        be focused on the strategic aspects of the program and not on the
        tactical product delivery tasks of the teams involved. The following
        RACI matrix shows the separation of responsibilities between roles:



| Program Delivery | A/R | R | R | R | R |
| Dependency and Risk Management | A/R | R | R | R | C/I |
| Iteration Planning | I | A/R | R | R | R |
| Communication | A/R | C/I | C/I | C/I | C/I |
| Story Writing | I | A/C | C | C | R |



Note the separation of accountability between the solution champion
        and the product delivery leadership and team.


## Conclusion


As we’ve discussed, once a program has been identified it becomes
      clear that a change in operating model is required to deliver value to
      the customer. Although we have listed a number of strategies, practices
      and principles that can put the program on a path to success, there’s no
      silver bullet. No matter the mechanisms you choose, make sure you put in
      place a feedback loop with the program constituents, to learn and adapt
      whenever necessary.


---
