---
title: "A Conversation with Badri Janakiraman about Hexagonal Rails"
description: "A couple of videos of a conversation between me and my colleague     Badri about hexagonal architecture and its role in a Rails     application. In the first video we talk about what Hexagonal     Arc"
date: 2014-06-05T00:00:00
url: https://martinfowler.com/articles/badri-hexagonal/
slug: badri-hexagonal
word_count: 2087
---


# A Conversation with Badri Janakiraman about Hexagonal Rails


The recent conversation Iâve been having with  Kent Beck, David
Heinemeier Hansson about whether [TDD is dead](https://martinfowler.com/articles/is-tdd-dead/) has spawned plenty of
other conversations. One such exchange was with my colleague, [Badri
Janakiraman](https://twitter.com/badrij), one of our senior developers at Thoughtworks. Badri has
over a decade of experience, working both in Ruby on Rails, but also in
other development stacks with Java and .NET. For the last six years
heâs been working in [Studios, our product division, ](http://www.thoughtworks.com/products)where much of his
time has been with [Mingle](http://www.thoughtworks.com/products/mingle-agile-project-management/), our project collaboration tool that is a
long running Rails project.


Since our discussions were so interesting, I thought it would be fun
to capture them on video. So we scheduled some time together for a
video chat, which I think youâll find an interesting viewpoint into the
role of Hexagonal Architecture in Ruby on Rails, and an useful
complement to the âIs TDD Deadâ discussion.


## 1: Active Record or Data Mapper?


5 June 2014


[video](http://thoughtworks.wistia.com/medias/uxjb0lwrcz)


We introduce the notion of Hexagonal Architecture, and Badri
      describes the trade-offs between using Active Record or a Data
      Mapper to push the database outside the hexagon.


moreâ¦


### Minutes


Badri began by explaining the notion of
        Hexagaonal Architecture, [originally
        laid out by Alistair Cockburn](http://alistair.cockburn.us/Hexagonal+architecture). The
        main idea of this architecture is that your domain is a
        self-contained entity with no dependencies on external
        components. This allows you to reason about, and test, your
        application independently from those components. This leads to the question of what is external and what is
        internal? The descriptions of hexagonal architecture in Rails
        usually consider the database as external, but that isn't
        a given. The original article also considers driving your application
        through different forms of UI.


Martin drew the relationship between hexagonal
        architecture and the notion of a layered
        architecture. A common layering is some variation on having
        layers for UI, domain, and data source: with dependencies
        running UI → domain → data source. Hexagonal architecture
        changes the dependencies between domain and data source so
        your dependencies run: UI → domain ←︎ data source. When Martin wrote [P of
        EAA](https://martinfowler.com/books/eaa.html), he described this approach as the [Data Mapper](https://martinfowler.com/eaaCatalog/dataMapper.html) pattern, which
        is in contrast to [Active Record](https://martinfowler.com/eaaCatalog/activeRecord.html) which ties
        the domain to the data source.


Martin asked Badri how he
        characterized the differences between Data Mapper and Active
        Record. He replied that it's all about the kind of application
        you need to build. In his early career he built applications
        with complex business logic such as leasing and insurance.
        When the domain has that kind of complexity you need to
        separate it from database concerns.


In the last six years or so, he's been working
        with rails on product applications with much simpler domain
        logic. For example [Mingle](http://www.thoughtworks.com/products/mingle-agile-project-management/)
        is a project collaboration tool that helps you manage your
        backlog with a card wall metaphor. Since Thoughtworks's
        philosophy is that the tool should not constrain a team's
        process, we need lots of flexibility for the data, required
        user defined fields. The usual approaches for user-defined
        fields don't work very well, so we dynamically alter the
        relational schema to add custom fields. This has worked very
        well and ties the domain objects to the database, bringing the
        database into the heart of the application. Martin summarized that the theme here is that Data Mapper
        should be used when you want domain model and data source to
        evolve independently.


Badri continued by saying his pre-rails work involved
        cases where the application developers didn't have
        complete control over the database structure. This makes Data
        Mapper more attractive. Data Mapper gives you more isolation
        from the database, but it isn't complete isolation - you still
        need to take into account data management concerns, such as
        loading the same data with different domain model objects
        depending on the particular need.


Badri described how Mingle works with a few different
        databases (Postgres, Oracle, and at one time MySQL). The fact
        that the unit tests hit the database greatly helps portability across
        these databases - contrary to the usual notion that says you
        need isolation for this.


Martin summarized the trade-off between Data Mapper and Active
        Record by saying that the reasons to use Data Mapper are if
        you don't control the database (for instance when you are
        using an integration database) or if you have complex domain
        logic. But if these forces aren't in play, then Active Record
        is simpler (and hence better).  We point out that the size of the database isn't a factor
        here: Mingle is a 50 KLOC app with over a hundred database
        tables, yet works well with Active Record.


Martin asked how long it takes for the tests to run.
         Badri replied that the tests run in around ten
        minutes or so with tests running in parallel with multiple
        browsers and databases. The team finds a ten minute commit
        suite is fast enough to maintain flow. They commit into a [pending head](https://martinfowler.com/bliki/PendingHead.html).


## 2: Rails: Platform or Suite of Components?


12 June 2014


[video](http://thoughtworks.wistia.com/medias/jhdk2wa37j)


When working with a rich framework like Ruby on Rails you can
      treat it as with a platform or as a suite of components. Badri
      discusses the difference between these and we discuss what
      trade-offs go with the decison.


moreâ¦


### Minutes


We started this conversation with Martin asking what the
        attitude towards Rails (and other similar frameworks) should
        be. Should we treat them as platforms, accepting them, warts
        and all? Or should we treat them a suite of components in
        which you pick the parts of the framework you like and leave
        out the parts that you don't. Badri responded by saying that while Rails has come quite a
        ways in being more modular, it is possible today to subset
        Rails more easily than to swap out whole components. For
        example, one could leave out Action Mailer in an application
        that doesn't need to either send or receive emails. One could
        pull in Action Support into a standard Ruby application and
        get a lot of the convenience methods and core-extensions that
        it provides. That said, one cannot, for example trivially
        replace the Rails request-response dispatch cycle with an
        evented system- like the one in Node.js for example. And this
        is because Rails is built to support a very specific kind of
        application. Martin chuckled, referring to the trope that
        Rails is a framework meant to build Basecamp.


Badri countered by saying that the sweet spot for Rails is a
        deeply webby application that talks to a relational datastore.
         In other words, your application has limited
        number of users and regardless of whether it is humans using
        your application through a web UI or other machines
        interacting with your application through a REST API, the web
        was not an accidental element. Badri further speculated that perhaps the problem is that people
        decide on using frameworks too early. Frameworks take away a
        lot of design options in return for a lot of convenience- and
        that means that perhaps we should understand how we would want
        to design our application and then pick a framework that
        doesn't prohibit those design choices rather than choosing a
        framework first and having it get in the way of how you would
        like to design the system


Martin replied that the choice to use the framework and design
        your application one way might have been made some time ago.
        That said, the framework designers might choose a different
        road and you might find yourself stuck in a corner. Martin
        then summarized our conversation so far by saying that if you
        are in the sweet spot for the framework, it makes sense to
        embrace it as a platform rather than spending the effort
        upfront to isolate oneself from possible future change. Badri agreed with this summary and said that some people find
        the additional layers they put in to be beneficial in guiding
        their design thoughts. That said, he personally tends to lie
        on the side of using Rails as a platform.


His personal preference for using a framework as a platform
        came from experiences in trying to circumvent frameworks in
        the past. Using the example of rich-client frameworks in .NET,
        He recalled the one time when he worked on an application
        where they attempted to not use two-way data binding. Due to
        how some members of the team felt the application should be
        tested, they tried to create a [humble
        view](http://www.objectmentor.com/resources/articles/TheHumbleDialogBox.pdf) by not using the data binding mechanisms. This led to
        a considerable mess because the framework was not designed to
        be used that way and we ended up writing far too much code and
        re-inventing major chunks of the framework. This is the kind
        of cost that needs to be understood by teams who wish to run
        against the grain of a framework. Perhaps the cost is
        sometimes worth it, but the fact that there is often a huge
        cost is unavoidable. He added that teams might wish to pick
        best of breed libraries and building a-la-carte applications
        if they find themselves wishing to make significant changes to
        a framework. Martin reiterated that the point is to make an
        informed choice to use a framework as a Platform or as Suite
        of Components driven by need- and not by blindly going
        full-embrace of either mode without having taken into
        consideration the costs and benefits of either approach.


Martin asked if there is value in frameworks
        making certain design choices for you and if that enables new
        members of the team to get started more quickly. Badri responded by saying that this is an advantage of
        frameworks in general - including ones such as Spring in the
        Java world. He claimed that he personally found the common usage
        patterns that people follow when using a framework to be more
        important- citing the example of how back in the Enterprise
        Java world, around 2001, almost every application would have
        it's own implementation of where transaction boundaries lay
        and how they were implemented. This was a something that he had
        to learn over and over in each application he worked on. In
        Rails, on the other hand, there is a common pattern of
        starting transactions and rolling them or committing them in a
        filter that wraps every request-response cycle. This sort of
        learning is useful to be able to carry from one Rails codebase
        to the next.


Martin called out for people not to push frameworks
        into places which are not their sweet spot. Badri added that this while this point is perfectly valid,
        Rails certainly does leave the door wide open for all sorts of
        design choices in places where the framework does not have an
        opinion. He illustrated this with a couple of examples from
        projects he was involved in. The first example is where they would fetch
        commit data from a version control system so that it could be
        shown in the context of other data in the application. Due to
        the needs of having the application work without this
        functionality and also the need to have data from multiple
        version control systems all be pulled into the application,
        they designed a port which defined the point of entry for this
        information into the system. This port became the single point
        for adapting all incoming data on by appropriate use of
        adapters for each kind of data that would arrive onto this
        port.


The second example was of two way communication where they
        built a Jabber chatroom bot that would pull in messages in
        team chat rooms that were relevant to stories that were being
        worked on, and attach them as a discussion thread to the story
        in the application that managed the backlog. Once again,
        because this functionality wasn't core to the application and
        they needed to let individual teams turn this functionality on
        or off as needed, they implemented a gateway that took care of
        all communication between the chat room and the core
        application which was completely oblivious as to whether this
        functionality was even configured. This gave them a good level
        of isolation for the core of the domain logic.


Martin summarized these two examples by saying
        that using Rails is not about avoiding avoiding isolation
        completely. He empasizes that you don't want to isolate
        yourself from your platform- but you do want to isolate
        yourself from external pieces. 

        The distinction between what constitutes external and what
        constitues internal parts of your application brings us back a
        full circle to where we started our chat with Hexagonal
        Architecture pattern.


![](badri.jpg)
