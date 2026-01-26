---
title: "Linking Modular Architecture to Development Teams"
description: "Can a modular architecture improve software delivery? Yes! -but with some caveats. This         article         charts the journey of an enterprise who set out to shift their architecture to a more   "
date: 2023-06-13T00:00:00
tags: ["enterprise architecture", "mobile", "team organization"]
url: https://martinfowler.com/articles/linking-modular-arch.html
slug: linking-modular-arch
word_count: 4411
---


This article will demonstrate the direct links between different mobile scaling issues,
            technical architecture and teams. At Thoughtworks we work with many large enterprises
            each presenting different problems and requirements when scaling their mobile presence.
            We identify two common problems seen in large enterprise mobile app development:

1. A gradual lengthening of the time it takes to introduce new features to a
                market app
2. Internal feature disparity arising from a lack of compatibility/reusability
                between in-house
                market apps


This article charts the journey one of our clients took when trying to address these
            issues. We tell the story of how their organisation had in the past, gravitated towards
            correct solutions, but was not able to see the expected benefits due to a
            misunderstanding of how those solutions were *intrinsically
                linked*.


We develop this observation by recounting how the same organisation was able to achieve a
            60% reduction in average cycle time, an 18 fold improvement in development costs and an
            80% reduction in team startup costs by shifting their [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) to match a
            modular architecture while at the same time, investing in the [developer
            experience](https://martinfowler.com/articles/developer-effectiveness.html).


## Recognising the Signs


Despite the best of intentions, software often deteriorates over time, both in
                quality and performance. Features take longer to get to market, service outages
                become more severe and take longer to resolve, with the frequent result that those
                working on the product become frustrated and disenfranchised. Some of this can be
                attributed to code and its maintenance. However, placing the blame solely on code
                quality feels naive for what is a multifaceted issue. Deterioration tends to grow
                over time through a complex interplay of product decisions, Conway's law, technical
                debt and stationary architecture.


At this point, it seems logical to introduce the organisation this article is based
                around. Very much a large enterprise, this business had been experiencing a *gradual
                lengthening of the time it took to introduce new features* into their retail
                mobile application.


As a starter, the organisation had correctly attributed the friction they were
                experiencing to increased complexity as their app grew- their existing development
                team struggled to add features that remained coherent and consistent with the
                existing functionality. Their initial reaction to this had been to ‘just add more
                developers’; and this did work to a point for them. However, eventually it became
                apparent that adding more people comes at the expense of more strained communication
                as their technical leaders started to feel the increased coordination overhead.
                Hence the [Two Pizza Team](https://martinfowler.com/bliki/TwoPizzaTeam.html) rule promoted at Amazon: any team should be small enough to be fed by two
                pizzas. The theory goes that by restricting how big a team can become, you avoid the
                situation where communication management takes more time than actual value creation.
                This is sound theory and has served Amazon well. However, when considering an
                existing team that has simply grown too big, there is a tendency towards 'cargo
                culting' Amazon’s example to try and ease that burden…


## Limiting Cognitive Load


Indeed, the organisation was no exception to this rule: Their once small monolith had
                become increasingly successful but was also unable to replicate the required rate of
                success as it grew in features, responsibilities and team members. With looming
                feature delivery deadlines and the prospect of multiple brand markets on the
                horizon, they responded by splitting their existing teams into multiple smaller,
                connected sub-squads - each team isolated, managing an individual market (despite
                similar customer journeys).


This in fact, made things worse for them, as it shifted the communication tax from
                their tech leadership to the actual team itself, while easing none of their
                expanding contextual load. Realizing that communication and coordination was sapping
                an increasing amount of time from those tasked with actual value creation, our
                initial suggestion involved the idea of [‘cognitive
                    load
                    limitation’](https://itrevolution.com/articles/cognitive-load/) outlined by Skelton & Pais (2019). This involves the
                separation of teams across singular complex or complicated domains. These seams
                inside software can be used to formulate the aforementioned ‘two pizza sized teams’
                around. The result is much less overhead for each team: Motivation rises, the
                mission statement is clearer, while communication and context switching are shrunk
                down to a single shared focus. This was in theory a great solution to our client’s
                problem, but can actually be misleading when considered in isolation. The benefits
                from cognitive load limitation can only truly be realised if an application’s domain
                boundaries are truly well defined and consistently respected inside the code.


## Domain Driven Discipline


[Domain
                    Driven
                    Design (DDD)](https://martinfowler.com/bliki/DomainDrivenDesign.html) is useful for organising complex logic into manageable groups
                and defining a common language or model for each. However, breaking apart an
                application into domains is only part of an ongoing process. Keeping tight control
                of the [
                    bounded context ](https://martinfowler.com/bliki/BoundedContext.html) is as important as defining the domains themselves.
                Examining our client’s application’s code we encountered the common trap of a clear
                initial investment defining and organising domain responsibilities correctly, only
                to have started to erode that discipline as the app grew. Anecdotal evidence from
                stakeholders suggested that *perpetually busy teams taking shortcuts driven by
                urgent product
                    requirements had become the norm* for the team. This in turn had contributed
                to a progressive slowing of value delivery due to the accumulation of technical
                debt. This was highlighted further still by a measurable downtrend in the
                application’s [Four
                Key Metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance) as it became more difficult to release code and harder to debug
                issues.


Further warning signs of a poorly managed bounded context were discovered through
                common code analysis tools. We found a codebase that had grown to become tightly
                coupled and lacking in cohesion. [Highly
                    coupled
                    code](https://www.martinfowler.com/ieeeSoftware/coupling.pdf) is difficult to change without affecting other parts of your system.
                Code with low cohesion has many responsibilities and concerns that do not fit within
                its remit, making it difficult to understand its purpose. Both these issues had been
                exacerbated over time as the complexity of each domain inside our client’s app had
                grown. Other indications came with reference again to cognitive load. Unclear
                boundaries or dependencies between domains in the application meant that when a
                change was made to one, it would likely involuntarily affect others. We noticed that
                because of this, development teams needed knowledge of multiple domains to resolve
                anything that might break, increasing cognitive load. For the organisation,
                implementing rigorous control of each domain-bounded context was a progressive step
                forward in ensuring knowledge and responsibility lay in the same place. This
                resulted in a limitation of the ‘blast radius’ of any changes, both in the amount of
                work and knowledge required. In addition, bringing in tighter controls in the
                accruing and addressing of technical debt ensured that any short term
                ‘domain-bleeds’ could be rejected or rectified before they could grow


Another metric that was missing from the organisation’s mobile applications was *optionality
                of reuse*. As mentioned earlier, there were multiple existing, mature brand
                market applications. Feature parity across those applications was low and a
                willingness to unify into a single mobile app was difficult due to a desire for
                individual market autonomy. Tight coupling across the system had reduced the ability
                to reuse domains elsewhere: Having to transplant most of an existing mobile app just
                to reuse one domain in another market brought with it high integration and ongoing
                management costs. Our utilisation of proper domain-bounded context control was a
                good first step to modularity by discouraging direct dependencies on other domains.
                But as we found out was not the only action we needed to take.


## Domains that Transcend Apps


### Scenario 1 - ‘The Tidy Monolith’


When viewed as a single application in
                    isolation, simply splitting the app into
                    domains, assigning a team, and managing their coupling (so as not to breach
                    their bounded contexts) works very well. Take the example of a feature request
                    to an individual application:


![](linking-modular-arch/d1.png)


The
                    feature request is passed to the app squads that own the relevant domain. Our
                    strict
                    bounded context means that the blast radius of our change is contained within
                    itself, meaning our feature can be built, tested and even deployed without
                    having to
                    change another part of our application. We speed up our time to market and allow
                    multiple features to be developed simultaneously in isolation. Great!


Indeed, this worked well in a singular market context. However as soon as we
                    tried to address our second scaling problem- *market feature disparity arising
                    from a lack of reusability* - we started to run into problems.


### Scenario 2 - ‘The Next Market Opportunity’


The next step for the organization on its quest for modularity of domains was to
                    achieve rapid development savings by transplanting parts of the ‘tidy monolith’
                    into an existing market application. This involved the creation of a common
                    framework (aspects of which we touch on later) that allowed
                    functionalities/domains to be reused in a mobile application outside its origin.
                    To better illustrate our methodology, the example below shows two market
                    applications, one in the UK, the other, a new app based out of the US. Our US
                    based application team has decided that in addition to their US specific domains
                    they would like to make use of both the Loyalty Points and Checkout domains as
                    part of their application and have imported them.


![](linking-modular-arch/d2.png)


For the organisation, this appeared to mean an order of magnitude development
                    saving for their market teams vs their traditional behaviour of rewriting domain
                    functionality. However, this was not the end of the story- In our haste to move
                    towards modularity, we had failed to take into account the existing
                    communication structures of the organisation that ultimately dictated the
                    priority of work. Developing our previous example as a means to explain: After
                    using the domains in their own market the US team had an idea for a new feature
                    in one of their imported domains. They do not own or have the context of that
                    domain so they contact the UK application team and submit a feature request. The
                    UK team accepts the request and maintains that it sounds like *“a great idea”*,
                    only they’re currently *“dealing with requests from UK based stakeholders”*
                    so it's unclear when they will be able to get to the work...


![](linking-modular-arch/d3.png)


We found that this conflict of interest in prioritising domain functionality
                    limits the amount of reuse a consumer of shared functionality could expect -
                    this was evident with market teams becoming frustrated at the lack of progress
                    from imported domains. We theorized a number of solutions to the problem: The
                    consuming team could perhaps fork their own version of the domain and
                    orchestrate a team around it. However, as we knew already, learning/owning an
                    entire domain to add a small amount of functionality is inefficient, and
                    diverging also creates problems for any future sharing of upgrades or feature
                    parity between markets. Another option we looked into was contributions via pull
                    request. However this imposed its own cognitive load on the contributing team -
                    forcing them to work in a second codebase, while still depending on support on
                    cross team contributions from the primary domain team. For example, it was
                    unclear whether the domain team would have enough time between their own
                    market’s feature development to provide architectural guidance or PR reviews.


### Scenario 3 - ‘Market Agnostic Domains’


Clearly the problem lay with how our teams were organised. [Conway’s
                        law](https://martinfowler.com/bliki/ConwaysLaw.html) is the observation that an organisation will design its business
                    systems to mirror its own communication structure. Our previous examples
                    describe a scenario whereby *functionality is, from a technical standpoint
                    modularised,
                        however
                        from an
                        ownership standpoint is still monolithic: **“Loyalty Points was created
                    originally
                        for the UK application so it belongs to that team”*. One potential
                    response to this is described in the [Inverse
                    Conway Maneuver](http://jonnyleroy.com/2011/02/03/dealing-with-creaky-legacy-platforms/). This involves altering the structure of development teams
                    so that they enable the chosen technical architecture to emerge.


In the below example we advance from our previous scenario and make the
                    structural changes to our teams to mirror the modular architecture we had
                    previously. Domains are abstracted from a specific mobile app and instead are
                    autonomous development teams themselves. When we did this, we noticed
                    relationships changed between the app teams as they no longer had a dependency
                    on functionality between markets. In their place we found new relationships
                    forming that were better described in terms of consumer and provider. Our domain
                    teams provided the functionality to their market customers who in turn consumed
                    them and fed back new feature requests to better develop the domain product.


![](linking-modular-arch/d4.png)


The main advantage this restructuring has over our previous iteration is the
                    clarification of focus. Earlier we described a conflict of interest that
                    occurred when a market made a request to change a domain originating from within
                    another market. Abstracting a domain from its market changed the focus from
                    building any functionality solely for the benefit of the market, to a more
                    holistic mission of building functionality that meets the needs of its
                    consumers. Success became measured both in consumer uptake and how it was
                    received by the end user. Any new functionality was reviewed solely on the
                    amount of value it brought to the domain and its consumers overall.


## Focus on Developer Experience to Support Modularity


Recapping, the organisation now had a topological structure that supported modularity
                of components across markets. Autonomous teams were assigned domains to own and
                develop. Market apps were simplified to configuration containers. In concept, this
                all makes sense – we can plot how feedback flows from consumer to provider quite
                easily. We can also make high level utopian assumptions like: *“All domains are
                independently developed/deployed”* or *“Consumers
                    ‘just’ pull in whatever reusable domains they wish to form an application”*.


In practice,
                however, we found that these are difficult technical problems to solve. For example,
                how
                do you maintain a level of UX/brand consistency across autonomous domain teams? How
                do
                you enable mobile app development when you are only responsible for part of an
                overall
                application? How do you allow discoverability of domains? Testability? Compatibility
                across markets? Solving these problems is entirely possible, but imposes its own
                cognitive load, a responsibility that in our current structure did not have any
                clear
                owner. So we made one!


### A Domain to Solve Central Problems


Our new domain was categorised as *‘the platform’*. The platform was
                    essentially an all encompassing term we used to describe tooling and guidance
                    that enabled our teams to deliver independently within the chosen architecture.
                    Our new domain team maintains the provider/consumer relationship we have seen
                    already, and is responsible for improving the developer experience for teams
                    that build their apps and domains within the platform. We hypothesised that a
                    stronger developer experience will help drive adoption of our new architecture.


But ‘Developer Experience’ (DX) is quite a non-specific term so we thought it
                    important to define what was required for our new team to deliver a good one. We
                    granularised the DX domain down to a set of necessary capabilities – the first
                    being, **Efficient Bootstrapping**.


With any common framework there is an inevitable learning curve. A good developer
                    experience aims to reduce the severity of that curve where possible. Sensible
                    defaults and starter kits are a non-autocratic way of reducing the friction felt
                    when onboarding. Some examples we defined for our platform domain:


> We Promise that: 
> You will be able to quickly generate a new domain
>                             with all associated mobile
>                             dependencies, common UI/UX, Telemetry and CI/CD infrastructure in one
>                             command
> You will be able to build, test and run your domain
>                             independently
> Your domain will run the same way when bundled into an app as it does
>                             independently”


Note that these promises describe elements of a self-service experience within a
                    developer productivity platform. We therefore saw an [effective
                    developer
                        platform](https://martinfowler.com/articles/platform-prerequisites.html) as one that allowed teams that were focused around end-user
                    functionality to concentrate on their mission rather than fighting their way
                    through a seemingly endless list of [unproductive
                    tasks](https://martinfowler.com/articles/developer-effectiveness.html).


The second necessary capability we identified for the platform domain was **Technical
                    Architecture as a Service**. In the organisation, architectural functions also
                    followed Conway’s law and as a result the responsibility for architecture
                    decisions was concentrated in a separate silo, disconnected from the teams
                    needing the guidance. Our autonomous teams, while able to make their own
                    decisions, tended to need some aspect of ‘technical shepherding’ to align on
                    principles, patterns and organisational governance. When we extrapolated these
                    requirements into an on demand service we created something that looks like:


> We Promise that:
> The best practice we provide will be accompanied
>                             with examples that you can
>                             use or actual steps you can take
>  we'll maintain an overall
>                             picture of domain usage per app and when needed,
>                             orchestrate collaboration across verticals
> The path to
>                             production will be visible and correct
> We will work with you”


Note that these promises describe a [servant
                    leadership](https://martinfowler.com/articles/scaling-architecture-conversationally.html) relationship to the teams, recognizing that everyone is
                    responsible for the architecture. This is in contrast to what some might
                    describe as command and control architectural governance policies.


One last point on the Platform Domain, and one worth revisiting from the
                    previous example. In our experience, a successful platform team is one that is
                    deeply ingrained with their customer’s needs. In Toyota lean manufacturing, [*“Genchi Genbutsu”*](https://mag.toyota.co.uk/genchi-genbutsu/) roughly translates to *“Go
                    and see for yourself”*. The idea being that by visiting the source of the
                    problem and seeing it for yourself, only then can you know how to fix it. We
                    learned that a team with the focus of improving developer experience must be
                    able to empathise with developers that use their product to truly understand
                    their needs. When we first created the platform team, we did not give this
                    principle the focus it deserved, only to see our autonomous teams find their own
                    way. This ultimately caused duplication of efforts, incompatibilities and a lack
                    of belief in the architecture that took time to rectify.


## The Results


We’ve told the story about how we modularised a mobile app, but how successful was it
                over time? Obtaining empirical evidence can be difficult. In our experience, having
                a legacy app and a newly architected app within the same organisation using the same
                domains with delivery metrics for both is a scenario that doesn’t come around too
                often. However luckily for us in this instance, the organisation was large enough to
                be transitioning one application at a time. For these results, we compare two
                functionally similar retail apps. One legacy with high coupling and low cohesion
                albeit with a highly productive and mature development team (“Legacy monolith”). The
                other, the result of the modular refactoring exercise we described previously - a
                well defined and managed bounded context but with ‘newer’ individual domain teams
                supporting (“Domain-bounded Context App”). **Cycle time** is a good measure here
                as it represents the time taken to ‘make’ a change in the code and excludes pushing
                an app to the store- A variable length process that App type has no bearing on.



| Mobile App Type | Cycle Time |
| Legacy Monolith | 17 days |
| Domain Bounded Context (Avg) | 10.3 days |



Even when cycle time was averaged across all domain teams in our second app we saw a
                significant uplift versus the Legacy App with a less experienced team.


Our second comparison concerns **optionality of re-use**, or lack thereof. In this
                scenario we examine the same two mobile apps in the organisation. Again, we compare
                one requiring existing domain functionality (with no choice but to write it
                themselves) with our modular app (able to plug and play an existing domain). We
                ignore the common steps on the path to production since they have no impact on what
                we are measuring. Instead, we focus on the aspects within the control of the
                development team and measure our development process from pre-production ‘product
                sign off’ to dev-complete for a single development pair working with a designer
                full-time.



| Integration Type | Avg Development Time |
| Non-modular | 90 days |
| Modular | 5 days |



The dramatically different figures above show the power of a modular architecture in
                a setting that has a business need for it.


As an aside, it is worth mentioning that these external factors we have excluded
                should also be measured. Optimising your development performance may reveal other
                bottlenecks in your overall process. For example, if it takes 6 months to create a
                release, and governance takes 1 month to approve, then governance is a comparatively
                small part of the process. But if the development timeline can be improved to 5
                days, and it still takes 1 month to approve, then [compliance](https://martinfowler.com/articles/devops-compliance.html)
                may become the next bottleneck to optimise.


One other advantage not represented in the results above is the effect a team
                organised around a domain has on *integration* activities. We found autonomous
                domain teams naturally seconding themselves into market application teams in an
                attempt to expedite the activity. This, we believe, stems from the shift in focus of
                a domain squad whereby success of its domain product is derived from its adoption.


We discovered two concentric feedback loops which impact the rate of adoption. The
                outer, a good integration experience from the consumer of the domain (i.e. the app
                container). This is a developer-centric feedback loop, measured by how easily the
                consumer could configure and implement the domain as part of their overall
                brand-specific product offering. The inner, a good end user experience - how well
                the overall journey (including the integrated domain) is received by the consumer’s
                market customer. A poor consumer experience impacts adoption and ultimately risks
                insulating the domain team from the actual users of the capability. We found that
                domain teams which collaborate closely with consumer teams, and which have direct
                access to the end users have the fastest feedback loops and consequently were the
                most successful.


The final comparison worth mentioning is one derived from our Platform domain.
                Starting a new piece of domain functionality is a time consuming activity and adds
                to the overall development cost for functionality. As mentioned earlier, the
                platform team aims to reduce this time by identifying the pain points in the process
                and optimising them – improving the developer experience. When we applied this model
                to domain teams within our modular architecture we found an *over 80% reduction in
                startup costs* per team. A pair could achieve in an afternoon activities that had
                been estimated for the first week of team development!


## Limitations


By now you should have quite a rosy picture of the benefits of a modular architecture
                on mobile. But before taking a sledgehammer to your ailing monolithic app, it's
                worth bearing in mind the limitations of these approaches. Firstly, and indeed most
                importantly, an architectural shift such as this *takes a lot of ongoing time and
                effort*. It should only be used to solve serious existing business problems
                around speed to market. Secondly, giving autonomy to domain teams can be both a
                blessing and a curse. Our platform squad can provide common implementations in the
                form of sensible defaults but ultimately the choices are with the teams themselves.
                Naturally, coalescing on platform requirements such as common UI/UX is in the
                interest of the domain squads if they wish to be incorporated/accepted into a market
                app. However, *managing bloat from similar internal dependencies or eclectic
                    design
                    patterns* is tricky. Ignoring this problem and allowing the overall app to
                grow uncontrolled is a recipe for poor performance in the hands of the customer.
                Again, we found that investment in technical leadership, in conjunction with robust
                guardrails and guidelines helps to mitigate this problem by providing
                architecture/design oversight, guidance and above all communication.


## Summary


To recap, at the start of this article we identified two significant delivery
                problems exhibited in an organisation with a multi app strategy. *A lengthening of
                the time it took to introduce new features into production* and an *increasing
                feature
                    disparity between other similar in house applications*. We demonstrated that
                the solution to these problems lies not in a single strategy around technical
                architecture, team structure or technical debt, but in a simultaneously evolving
                composite of all those aspects. We started by demonstrating how evolving team
                structures to support the desired modular and domain-centric architecture improves
                cognitive and contextual load, while affording teams the autonomy to develop
                independently of others. We showed how a natural progression to this was the
                elevation of teams and domains to be agnostic of their originating
                application/market, and how this mitigated the effects of Conway’s law inherent with
                an application monolith. We observed that this change allowed a consumer/provider
                relationship to naturally occur. The final synchronous shift we undertook was the
                identification and investment in the ‘platform’ domain to solve central problems
                that we observed as a consequence of decoupling teams and domains.


Putting all these aspects together, we were able to demonstrate a **60% reduction in
                cycle time** averaged across all modular domains in a market application. We also
                saw an **18 fold improvement in development cost** when integrating modular
                domains to a market app rather than writing from scratch. Furthermore, the focus on
                engineering effectiveness allowed our modular architecture to flourish due to the **80%
                reduction
                    in startup costs** for new domains and the ongoing support the ‘platform team’
                provided. In real-terms for our client, these savings meant being able to capitalise
                on market opportunities that were previously considered far too low in ROI to
                justify the effort - opportunities that for years had been the uncontested domains
                of their competitors.


The key takeaway is that a modular architecture intrinsically linked to teams can be
                highly beneficial to an organisation *under the right circumstances*. While the
                results from our time with the highlighted organisation were excellent, they were
                specific to this individual case. Take time to understand your own landscape, look
                for the signs and antipatterns before taking action. In addition, do not
                underestimate the upfront and ongoing effort it takes to bring an ecosystem like
                that which we have described together. An ill considered effort will more than
                likely cause more problems than it solves. But, by accepting that your situation
                will be unique in scope and thus resisting the pull of the ‘cargo cult’: Focusing on
                empathy, autonomy and lines of communication that enable the architecture at the
                same time, *then there is every reason you could replicate the successes we have
                seen*.


---
