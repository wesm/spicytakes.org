---
title: "Using the Strangler Fig with Mobile Apps"
description: "Incremental replacement of a legacy mobile application is a challenging concept to articulate         and execute. However, we believe by making the investment in the pre-requisites of legacy moderniz"
date: 2024-11-05T00:00:00
tags: ["mobile", "legacy modernization"]
url: https://martinfowler.com/articles/strangler-fig-mobile-apps.html
slug: strangler-fig-mobile-apps
word_count: 4997
---


In this article we aim to show why taking an incremental approach to
    legacy mobile application modernization can be preferable to the classical
    'rewrite from scratch' methodology. Thoughtworks has the benefit of working with
    large enterprise clients that are dependent on their in-house mobile
    applications for their core business. We see many of them asking their
    applications to do more and evolve faster, while at the same time, we see an
    increasing rejection of reputationally damaging high risk releases.


As a solution, this article proposes alternative methods of legacy
    modernization that are based in Domain Driven Design and hinge on the
    application of the Strangler Fig pattern. While these concepts are far from
    new, we believe that their usage in mobile applications are novel. We feel
    that despite incurring a larger temporary overhead from their usage, this is
    an acceptable tradeoff. We assert how the methodology is used to combat the
    aforementioned attitudinal shifts in legacy mobile application development
    while gaining a platform to lower risk and drive incremental value
    delivery.


We discuss how this works in theory, diving into both the architecture
    and code. We also recount how this worked in practice when it was trialled on
    a large, legacy mobile application at one of Thoughtworks’ enterprise
    clients. We highlight how the pattern enabled our client to rapidly build,
    test and productionize a modernized subset of domain functionalities inside
    an existing legacy application.


We move on to evaluate the effectiveness of the trial by highlighting the business
    facing benefits such as a signficantly faster time to value and a 50% reduced median cycle
    time. We also touch on other expected benefits that should be used to
    measure the success of this methodology.


## The Problem with Mobile Legacy Modernization


As applications age and grow, they tend to deteriorate both in quality
      and performance. Features take longer to get to market while outages
      and rolled back releases become more severe and frequent. There is a
      nuanced complexity to be understood about the reasons why this
      occurs both at the code and organizational level.
      To summarize though, at some point, an
      organization will grow tired of the poor outcomes from their
      software and start the process of legacy replacement. The decision
      to replace may be made based on multiple factors, including (but not limited to)
      cost/benefit analysis, risk analysis, or opportunity cost. Eventually a legacy modernization strategy will be chosen.
      This will be dependent on the organization’s attitude to risk. For
      example, a complex, high availability system may demand a more
      incremental or interstitial approach to legacy
      replacement/displacement than a simpler, less business critical one.


In the case of mobile application modernization, those decisions have
      in recent memory been reasonably clear cut. A mobile application was
      often designed to do an individual thing- Apple’s “There’s an app for
      that” still rings out loud and clear in people’s minds 15 years after
      the initial batch of advertisements. That message was one that was taken
      to heart by organizations and startups alike: *If you need to do
      something, write an app to do it. If you need to do something else, write
      another app to do that.* This example struck me when I was
      pruning the apps on my phone a couple of years ago. At the time I noticed I
      had several apps from the manufacturer of my car; an older one and a newer
      one. I also had two apps from my bank; one showed my checking account,
      another that analyzed and illustrated my spending habits. I had three apps
      from Samsung for various IoT devices, and at least two from Philips that
      controlled my toothbrush and light bulbs. The point I’m laboring here is
      that a mobile application was never allowed to get so complicated,
      that it couldn’t be torn down, split out or started from scratch again.


But what happens when this isn’t the case? Surely not all apps are
      created equal? Many believe that the mobile experience of the future
      will be centered around so-called [
      “super-apps”](https://www.theverge.com/23940924/elon-musk-x-twitter-all-hands-linda-yaccarino-super-app); apps where you can pay, socialize, shop, call,
      message, and game, all under one application. To some degree this has
      already happened in China with “do-everything” applications like
      ‘WeChat’ and ‘AliPay’- we see the mobile device and its operating
      system as more of a vehicle to allow the running of these gigantic
      pieces of software. Comments from industry indicate a realization
      that the [West
      is not quite as far along as China in this regard](https://hbr.org/2023/04/are-super-apps-coming-to-the-u-s-market). But while not
      at the super-app, there is no doubt that complexity of the mobile
      app experience as a whole has increased significantly in recent
      years. Take the example of YouTube, when first installed, back in
      the early 2010’s, the application could play videos and not much
      else. Opening the application today one is presented with “Videos”
      and “Shorts”, a news feed, controllable categories, subscriptions,
      not to mention a content editing and publishing studio. Similarly
      with the Uber app, the user is asked if they want to order food.
      Google Maps can show a 3D view of a street and Amazon now recommends
      scrollable product-recommendation mood boards. These extra features
      have certainly enriched a user’s experience but they also make the
      traditional build, use, rebuild technique much more difficult.


This difficulty can be explained by considering some of the existing
      common problems of mobile application development:

- Massive View Controllers/Activities/Fragments
- Direct manipulation of UI elements
- Platform specific code
- Poor Separation of Concerns
- Limited Testability


With discipline, these problems can be managed early on. However, with
      a large application that has grown chaotically inline with the business it
      supports, incremental change will be difficult regardless. The solution then, as
      before, is to build new and release all at once. But what if you only want
      to add a new feature, or modernize an existing domain? What if you want to
      test your new feature with a small group of users ahead of time while
      serving everyone else the old experience? What if you’re happy with your
      app store reviews and don’t want to risk impacting them?


Taking an incremental approach to app replacement then is the key to
      avoiding the pitfalls associated with ‘big bang releases’. The [Strangler
      Fig pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) is often used to rebuild a legacy application in
      place: a new system is gradually created around the edges of an old
      one through frequent releases. This pattern is well known, but
      not widely used in a mobile context. We believe the reason for this is that there are several prerequisites that need to be in
      place before diving headfirst into the pattern.


In their article on [Patterns
      of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), the authors describe four broad
      categories (prerequisites) used to help break a legacy problem into
      smaller, deliverable parts:

1. Understand the outcomes you want to achieve
2. Decide how to break the problem up into smaller parts
3. Successfully deliver the parts
4. Change the organization to allow this to happen on an ongoing
        basis


Only in the third point, can we envisage the invocation of the Strangler Fig
      pattern. Doing so without an understanding of why, what or how it might
      continue in the future is a recipe for failure.


Going forward, the article charts how Thoughtworks was able to help one
      of its enterprise clients expand its existing mobile legacy modernization
      efforts into a successful experiment that demonstrated the value behind
      the use of the Strangler Fig pattern in a mobile context.


## Satisfying the Prerequisites


At this point, it seems appropriate to introduce the client that
      inspired the writing of this article – a globally distributed business
      with an established retail organization that had embraced mobile
      applications for many years. Our client had realized the benefits an
      app brought to provide a self-service experience for their
      products. They had quickly expanded and developed their app domains to allow millions
      of customers to take full advantage of all the products they sold.


The organization had already spent a significant amount of time and
      effort modernizing its mobile applications in its smaller
      sub-brands. Responding to a lack of reuse/significant duplication of
      efforts, [high
      cognitive load](https://itrevolution.com/articles/cognitive-load/) in app teams and slow feature delivery, the
      organization chose a mobile technology stack that leveraged a
      Modular Micro-app architecture. This strategy had been largely
      successful for them, enabling proliferation of features common to
      the organization (e.g. ‘login/registration/auth’ or ‘grocery shopping’)
      across different brands and territories, in a fraction of the time it
      would have taken to write them all individually.


![](strangler-fig-mobile-apps/d1.svg)


The diagram above is a simplified representation of the modular
      architecture the organization had successfully implemented. React
      Native was used due to its ability to entirely encapsulate a
      domain’s bounded context within an importable component. Each
      component was underpinned by its own [backend
      for frontend (BFF) ](https://samnewman.io/patterns/architectural/bff/) that came with the infrastructure as code to
      instantiate and run it. The host apps, shown above as UK and US,
      were simply containers that provided the app specific configuration
      and theming to the individual micro-apps. This ‘full slice’ of
      functionality has the advantages of both allowing re-use and
      reducing complexity by abstracting application domains to micro-apps
      managed by individual teams. We speak in depth about the results of
      this architecture in the already referenced article on [‘Linking
      Modular Architecture’](https://martinfowler.com/articles/linking-modular-arch.html).


As touched upon earlier, the organization’s mobile estate was made up of
      a number of smaller sub-brands that served similar products in other
      territories. With the modular architecture pattern tried and tested, the
      organization wanted to focus efforts on its 'home-territory' mobile
      application (serving its main brand). Their main mobile app was much
      larger in terms of feature richness, revenue and user volumes to that of
      the sub brands. The app had been gaining features and users over many
      years of product development. This steady but significant growth had
      brought success in terms of how well-regarded their software was on both
      Google and Apple stores. However, it also started to show the
      characteristic signs of deterioration. Change frequency in the application
      had moved from days to months, resulting in a large product backlog and
      frustrated stakeholders who wanted an application that could evolve as
      fast as their products did. Their long release cycle was related to risk
      aversion: Any outage in the application was a serious loss of revenue to
      the organization and also caused their customers distress due to the
      essential nature of the products they sold. Changes were always tested
      exhaustively before being put live.


The organization first considered a rewrite of the entire application
      and were shocked by the cost and duration of such a project. The potential
      negative reception of a ‘big bang’ new release to their app store
      customers also caused concerns in the levels of risk they could accept.
      Suggestions of alpha and beta user groups were considered unacceptable
      given the huge volumes of users the organization was serving. In this
      instance, a modernization effort similar to that seen in their sub-brands
      was believed to be of considerably higher cost and risk.


Thoughtworks suggested an initial proof of concept that built on the
      successes of the reusability already seen with a modular
      architecture. We addressed the organization’s big bang risk aversion
      by suggesting the [Strangler
      Fig pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) to incrementally replace individual domains. By
      leveraging both techniques together we were able to give the
      organization the ability to reuse production-ready domains from
      their modernized mobile apps inside their legacy app experience. The
      idea was to deliver value into the hands of customers much sooner
      with less duplication than in a full rewrite. Our focus was not on
      delivering the most beautiful or cohesive full app experience (-not
      quite yet anyway). It was about obtaining confidence both in the
      stability of the iterative replacement pattern and also in how well
      the new product was being received. These pieces of information
      allowed the organization to make more informed product decisions
      early on in the modernization process. This ensured the finished product
      had been extensively used and molded by the actual end users.


## Strangler Fig and Micro-apps


So how far did we get with the proof of concept and more importantly
      how did we actually do this? Taking the learnings from Modular Micro-app
      architecture (described above), we theorized the design to be as follows:


![](strangler-fig-mobile-apps/d2.svg)


The initial state of the application involved the identification of
      domains and their navigation routes *(Decide how to break the problem into
      smaller parts)*. We focused our efforts on finding navigation entry points
      to domains, we called them our ‘points of interception’. Those familiar
      with mobile application development will know that navigation is generally
      a well encapsulated concern, meaning that we could be confident that we
      could always direct our users to the experience of our choosing.


![](strangler-fig-mobile-apps/d3.svg)


Once we identified our ‘points of interception’, we selected a domain
      for incremental replacement/retirement. In the example above we focus on
      the Grocery domain within the existing application. The ‘new‘ Grocery domain,
      was a micro-app that was already being used within the sub-brand apps. The
      key to implementation of the Strangler Fig pattern involved embedding an
      entire React Native application inside the existing legacy application.
      The team took the opportunity to follow the good modularity practices that
      the framework encourages and built Grocery as an encapsulated component. This
      meant that as we added more domains to our Strangler Fig Embedded
      Application, we could control their enablement on an individual level.


As per the diagram, in the legacy app, Grocery functionality was
      underpinned by a monolithic backend. When we imported the New Grocery
      Micro-app, it was configured to use that same monolithic backend. As
      mentioned previously, each micro-app came with its own Backend for
      Frontend (BFF). In this instance, the BFF was used as an anti-corruption
      layer; creating an isolating layer to maintain the same domain model as
      the frontend. The BFF talked to the existing monolith through the same
      interfaces the legacy mobile application did. Translation between both
      monolith and micro-app happened in both directions as necessary. This
      allowed the new module’s frontend not to be constrained by the legacy API
      as it developed.


We continued the inside out replacement of the old application by
      repeating the process again on the next prioritized domain. Although out
      of scope for this proof of concept, the intention was that the process
      shown be repeated until the native application is eventually just a shell
      containing the new React Native application. This then would allow the removal of the
      old native application entirely, leaving the new one in its place. The new
      application is already tested with the existing customer base, the
      business has confidence in its resilience under load, developers find it
      easier to develop features and most importantly, unacceptable risks
      associated with a typical big bang release were negated.


## Diving Deeper…


So far we’ve presented a very broad set of diagrams to
      illustrate our Mobile Strangler Fig concept. However, there are
      still many
      outstanding implementation-focused questions in order to take theory
      into
      practice.


### Implanting the Strangler Fig


A good start might be, how did we abstract the complexity of
        building both native and non-native codebases?


Starting with the repository structure, we turned our original native
        application structure inside out. By inverting the control
        of the native application to a React Native (RN) application
        we avoided significant duplication associated with nesting
        our RN directory twice inside each mobile operating system’s
        folder. In fact, the `react-native init` default
        template gave a structure to embed our iOS and Android
        subfolders.


![](strangler-fig-mobile-apps/d4.svg)


From a developer perspective, the code was largely unchanged. The
        legacy application’s two operating-system-separated teams were able to
        target their original directories, only this time it was within a single
        repository. The diagram below is a generalized representation (that is,
        applicable to both iOS and Android) of the current pipeline from the
        Client as we understood:


![](strangler-fig-mobile-apps/d5.svg)


### Bi-Directional Communication using the Native Bridge


We’ve already touched on navigation with our previously mentioned
        ‘points of interception’. It is worth looking deeper into how we
        facilitated communication and the transfer of control between native and
        React Native as it would be easy to oversimplify this area.


The [React
        Native ‘Bridge’](https://reactnative.dev/docs/communication-ios#other-ways-of-cross-language-interaction-events-and-native-modules) enables communication between both
        worlds. Its purpose is to serve as the message queue for
        instructions like rendering views, calling native functions,
        event handlers, passing values etc. Examples of
        properties passed across the bridge would be *isCartOpen*
        or *sessionDuration*. While an example of a bridge
        function call might be js invocations of the device’s native [geolocation
        module](https://github.com/michalchudziak/react-native-geolocation).


![](strangler-fig-mobile-apps/d6.svg)


The diagram above also references the concept of a ‘React Native
        Micro App’. We introduced this concept earlier in the article when we
        described our app in terms of journeys. To recap though, a micro-app is a self-contained
        encapsulation of UI and functionality related to a single
        domain. A React Native app may be made up of many micro-apps
        similar to the [micro
        frontend pattern](https://martinfowler.com/articles/micro-frontends.html). In addition to those advantages we have already discussed, it also allows us to have a greater
        degree of control over how our Strangler Fig application
        grows and is interacted with. For example, in a situation
        where we have more confidence in one of our new journeys
        than another we are afforded the option to divert a larger
        proportion of traffic to one micro-app without impacting
        another.


Bringing both concepts together, we utilized the bridge to
        seamlessly move our users back and forth across experiences.
        The ability to pass information allowed us to preserve any
        immediate state or action from the UI that needed to
        persevere across experiences. This was particularly useful
        in our case as it helped us to decouple domains at
        appropriate fracture points without worrying whether we
        would lose any local state when we crossed the bridge.


### Handling Sensitive Data


So far we’ve discussed moving between legacy and new codebases as
        atomic entities. We’ve touched on how local state can be
        shared across the bridge, but what about more sensitive
        data? Having recently replaced their login and registration (auth)
        process in their other customer-facing React Native apps
        with a modular, configurable, brand agnostic one, the client
        was keen for us to reuse that experience. We set ourselves
        the task of integrating this experience as an
        initial demonstration of the Strangler Fig pattern in
        action.


We leveraged the techniques already discussed to implant the
        Strangler Fig: i.e. the new authentication journey on the
        React Native side. When a customer successfully logged in or
        registered, we needed to ensure that if they moved away from
        the new experience (back into the legacy journey), their
        authentication status was preserved no matter where they
        were.


![](strangler-fig-mobile-apps/d7.svg)


For this, we utilized the native module code calling side of the
        bridge. The diagram above explains how we achieved this by
        using a React Native library that served as a wrapper to
        save authentication data to the Android
        EncryptedSharedPreferences or iOS Keychain after a
        successful login. Due to the flexible structure of the data
        inside the keystore, it allowed us to seamlessly share the
        (re)authentication process irrespective of whether
        the user was in the native or non-native experience. It also
        gave us a pattern for the secure sharing of any sensitive
        data between experiences.


### Regression Testing at Domain Boundaries


An important part of a cutover strategy is the ability to know
        from any vantage point (in our case, different teams working within the same app) whether a change made affected the
        overall functionality of the system. The embedded app
        pattern described above presents a unique challenge in this
        regard around scalable testability of a multi-journey
        experience. Moreover one that is managed by multiple teams
        with numerous branching paths.


![](strangler-fig-mobile-apps/d8.svg)


The interaction diagram above shows an example journey flow
        within the embedded app. One thing to notice is the amount
        of branching complexity across a journey that is carrying
        out just two concurrent experiments. We speak more on accidental complexity later in this section.


The [test
        pyramid](https://martinfowler.com/bliki/TestPyramid.html) is a well known heuristic that recommends a
        relationship between the cost of a test (maintenance and
        writing) and its quantity in the system. Our client had kept
        to the test pyramid and we found unit, subcutaneous and
        journey-centric UI-driving tests when we examined their
        code. The solution therefore was to continue to follow the
        pattern: Expanding the number of tests across all layers and
        also extending the suite of journey tests to incorporate the
        jumping in and out of our embedded Strangler Fig app. But
        there was a potential problem, ownership. We realized
        that it would be unreasonable to tie the success of another
        team’s build to code they did not write or were in control of.
        We therefore proposed the following test strategy across
        teams:



| Test Type | Native | React Native |
| Unit | X | X |
| Subcutaneous | X | X |
| Legacy Journey | X |  |
| e2e Micro-app Journey |  | X |
| Contract tests for interactions with âThe Bridgeâ (journeys with both legacy and micro-app components) | X | X |



On the last table row, by contract we simply mean:


*If I interact with the bridge interface a particular way, I
          expect a specific event to fire*


For Native to RN interactions, these contracts act as blueprints
        for micro-apps and enable unit testing with mocks. Mocks
        simulate the behavior of the micro-app, ensuring it utilizes
        the required context correctly.


The other way around (RN to Native) was similar. We identified
        the Native functionality we wished to call through the
        Bridge. RN then provided us with an object called
        NativeModules which, when mocked, allowed us to assert
        against the resulting context.


Defining these boundaries of responsibility meant that we could
        limit the ‘regression-related’ cognitive load on teams through
        ‘hand-off’ points without compromising on overall app test
        coverage.


This strategy was largely well received by both the native and
        non-native teams. Where we did run into friction was the
        complexity behind the implementation of the contract tests
        across the bridge. The team running the legacy application
        simply did not have the bandwidth to understand and write a
        new category of tests. As a compromise, for the duration of
        the PoC, all contract tests were written by the React Native
        team. From this we learned that any interstitial state
        required thought to be paid to the developer experience. In
        our case, simply layering complexity to achieve our goals
        was only part of the problem to be solved.


### Creating the Experiment


Bringing everything together to form an experiment was the last
        hurdle we had to overcome. We needed a means to be able to
        demonstrate measurable success from two different
        experiences and also have an ability to quickly backout and
        revert a change if things were going wrong.


The organization had an existing integration with an
        experimentation tool, so out of ease, we chose it as our
        tool for metric capture and experiment measurement. For experiment
        user selection, we decided device level user selection (IMEI
        number) would be more representative. This was due to the
        potential for multiple device usage across a single account
        skewing the results.


We also utilized the feature
        flagging component of the experimentation tool to allow us to ‘turn off’ the experiment (revert to
        native app only) without the need for a release; greatly
        reducing the time taken to recover should any outage occur.


## Results


We’ve told the story of how we implemented the Strangler Fig pattern
      against a large, complex legacy application, but how
      successful was it with our client?


Our client chose a domain/journey that mapped to an existing smaller
      micro-app to be the first that would be incrementally replaced
      inside the legacy application. This was because the micro-app was
      tried and tested in other applications around the business and was
      generic enough that it could be easily ‘white labeled’ by our team.
      Following the success of the first micro-app integration, a second,
        larger micro-app was then implanted to demonstrate the pattern
      was extensible. These were the results:


### Time to First Value


Getting a product in front of users early enables value to be
        realized cumulatively over time and actual user feedback to be collected
        and iterated upon. A longer time to value increases the impact of
        changing requirements and delays the realization of benefits. The first
        metric concerned time to first value for our new experience. This figure
        is derived from the time it took to create the Strangler Fig framework
        inside the existing legacy app and all regression/integration activities
        around the first micro-app.


![](strangler-fig-mobile-apps/d9.svg)


By comparison, our client had been quoted
          around two years for an entire application rewrite. In the case of the Strangler Fig, It took around 1 month to implant the micro-app structure into the existing
        application, 3 months to build the first micro-app, and 5 months for the
        second. Hence, from a blank page, it would take 4 months to yield first
        value (implantation plus first app). While that's the fairest way to
        make the comparison, in fact the client saw first value much quicker.
        This is because both micro-apps had already been built for use in
        separate mobile applications. So the time to first value in this case
        was only the implantation time of 1 month.


### Cycle Time


Our second measurement is [Cycle Time](https://martinfowler.com/bliki/CycleTime.html). It represents the time to
        make a change inside the micro-app code and includes time taken for
        regression with the Strangler Fig app. It *excludes* pushing an app
        to the store - a variable length process that app type has no bearing on.
        In the case of our legacy app, we calculated cycle time as the duration
        it took to make and regression test a change in the existing native code
        base.


The metric is useful because its uplift represents a shift in
        organizational risk aversion against the product; changes in the past
        being exhaustively tested due to the potential for unrelated side
        effects and outages. As our existing micro app was an entirely
        encapsulated domain, we knew that the vast majority of changes would be
        owned by the micro-app team and therefore fully testable inside the micro-app
        itself. Any exceptions where the bridge was invoked (e.g. native
        functionality requested) could be mapped to contract tests at the
        boundaries.



| App Type | Median Cycle Time (over 30 days) |
| Micro-App 1 | 9 days |
| Micro-App 2 | 10 days |
| Legacy App | 20 days |



The
        results above show a significant uplift in
        speed to make code changes inside
        encapsulated domain boundaries (micro-apps)
        when compared to a coupled monolithic
        app structure.


## Limitations and Identified Drawbacks


So far we’ve mostly highlighted the benefits of a Strangler Fig
      approach to legacy mobile App displacement. However, there are some
      significant limitations to this pattern that should be taken into account
      before choosing to replicate our experiment. We acknowledge that our use
      of the
      pattern originated from a proof of concept: A request from a client
      unwilling to accept that there was only one option to replace their legacy
      application. While the data we see thus far is encouraging in terms of
      cumulative value delivery and improvements in cycle time, it is hard to
      ignore a lack of data from the [right side of the development process](https://www.browserstack.com/guide/shift-left-vs-shift-right#toc1). Before
      recommending this as an option for legacy replacement, we would need to
      see data on app resilience such as [time to restore service](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance) and number/severity of outages. Thinking further ahead, we also recognize the
      limitations of only applying the pattern to two of the many domains the
      client’s app was composed of. It remains to be seen if there are any
      complexity problems created when more domains are introduced to the
      interstitial app state.


## Summary


Recapping, we started this article by explaining why, as mobile
      apps have grown in complexity, incremental legacy
      modernization has become more attractive. From there, we
      introduced the Strangler Fig pattern for Mobile
      Applications. We showed the various stages in the process
      from initial feature deployment through to eventual complete
      replacement. We examined some of the more complex
      implementation challenges in detail. We demonstrated how our
      Strangler Fig was implanted into the legacy app. We dove deeper into the concept by examining the React
      Native Bridge as a means to facilitate communication between
      old and new. We discussed how the handling of sensitive data took place. We also showed how effective regression
      test coverage could happen when faced with multiple independent teams. Lastly, we touched on how leveraging experimentation against the pattern, was useful in an incremental delivery environment.


We discovered encouraging results in that our PoC was able to
        significantly shorten the path to first value when compared to the estimated time for a full app rewrite.
        Our use of modular micro-apps also showed a 50% improvement in the median cycle time when
        compared against that of the existing
        legacy mobile app. With that being said, we acknowledge the
        limitations of our status as a PoC and the accidental complexity incurred that needed managing. We
        suggest further exploration of the resiliency and scalability of the
        pattern before it is a reliable alternative
        to the traditional methods of mobile app modernization.


To sum up, we believe that it is innevitable mobile apps will continue to
        increase in scope and complexity.
        We also think that attitudes around risk mitigation and faster value
        delivery will become more commonplace
        when considering modernization of a sufficiently complex app. To
        some extent, this demands a new approach, perhaps that which was
        proposed in this article. However, despite the successes we have
        seen, this should not be overplayed
        as more than a tool as part of a wider 'legacy modernization
        toolbelt'. Those looking to replicate
        should understand first and foremost that Legacy Modernization,
        regardless of technology, is a multifaceted
        problem that demands significant analysis and alignment. Putting in
        the investment upfront, will not only help you select
        the correct tool for your situation, but ensure that your app is
        better aligned to the customers it serves
        and the problems it solves.


---
