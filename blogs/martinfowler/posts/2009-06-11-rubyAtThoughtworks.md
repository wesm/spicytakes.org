---
title: "Ruby at Thoughtworks"
description: "Thoughtworks started using Ruby for production projects in   2006, from then till the end of 2008 we had done 41 ruby projects. In   preparation for a talk at QCon I surveyed these projects to examine"
date: 2009-06-11T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/articles/rubyAtThoughtworks.html
slug: rubyAtThoughtworks
word_count: 4331
---


Thoughtworks, my employer, is primarily a software delivery
    company. We build software for people, including products built
    for ourselves. An important part of our philosophy is an openness
    to to different development platforms, so we can choose the
    appropriate platform for our widely varying clients. When I
    joined Thoughtworks in 2000, Java was our overwhelmingly major
    platform. Shortly afterwords we started working with .NET and
    these two platforms dominated our work by the middle of the decade.


A few people, however, had started experimenting with LAMP
    scripting languages, in particular Ruby. The appearance of the
    Ruby on Rails web framework gave Ruby a big push, enough that in
    2006, we started doing some serious project work with the Ruby
    platform. As I write this in 2009, the Ruby platform has a firm
    share of our work, not as high as Java and C#, but a significant
    portion.


During these three years we've learned a lot about Ruby in
    practice. As 2009 began, I was asked to give a talk on our
    experiences with Ruby for the QCon conference. To prepare for this
    I conducted an extensive survey of our Ruby projects and probed
    our Ruby leaders for their thoughts and experiences. It's taken me
    a bit longer than I'd like to produce this article as well, but
    here it is.


I've divided the article into three parts. To start with I'll
    look at the profile of our Ruby project experience, to give you a
    sense of what kinds of projects we've been tackling over the
    years. Next I'll move onto several common questions about Ruby and
    how our experiences answer these questions. Finally I'll launch
    into some lessons we've learned from using Ruby.


## The Shape of Our Projects


During 2006-8, Thoughtworks has been involved in some 41
    Ruby projects. I define a Ruby project as a project where Ruby was
    the primary development language. Ruby has appeared on other
    projects too, there's a lot of recent developments using ruby for
    build automation or functional testing for Java projects. Almost
    all these projects have involved Rails, and most of them are web
    site projects where Rails is at least as important as Ruby.


![](rubyAtThoughtworks/projectScatter.png)


Figure 1: 
      Scatterplot of peak headcount versus involved length for
      Thoughtworks Ruby projects in 2006-8.


Figure 1 gives
    a feel for the size of the projects we've been involved in. The
    headcount here is the peak headcount of everyone involved
    (Thoughtworks, client and others; developers, project managers,
    analysts etc). The length is the duration that we've been involved
    in the project.


Ruby projects are generally seen as shorter and smaller than
    other projects. Sadly I don't have comparative data for our
    projects on other platforms to get a better feel on whether this
    is true. Certainly we can see that most projects involve less than
    20 people for less than a year.


There are a few projects that stand out. By far our largest
    project is the one that I'll refer to as the Atlanta project, with
    a peak headcount of over 40 people involved. Another large and
    long running project is the Jersey project. These two are related
    in that there's been a good bit of rotation between the two, so
    many of our more experienced Ruby people have been on both projects.


The third project I've called out here is Mingle, which is a
    particularly interesting case as it's a product from Thoughtworks
    Studios - and as such we can be more public about it than we can
    about projects done for clients. It's been a long running project
    and also an international project: starting in Australia, moving
    to Beijing, and now multi-sited in Beijing and San Francisco.


![](rubyAtThoughtworks/yearStrip.png)


Figure 2: Strip chart showing
    effort for project for each year.


Figure 2 looks at
    the shape a different way, looking at the effort involved in
    the various projects we've been involved in for each year. Each
    dot on the strip chart represents total effort (all people) in one
    project during that year. This chart provides a good feel for how
    much increase we've seen in ruby projects over the last three
    years.


![](rubyAtThoughtworks/countryStrip.png)


Figure 3: Strip chart
    showing project effort per host country


Figure 3 looks at
    the projects by host country. It's somewhat rough and ready, as I
    haven't tried to properly deal with the few multi-site projects or
    projects that have moved (Mingle, for example, I classed as a China
    although it's history is more varied.)


The country split shows that the US has seen the biggest
    interest in Ruby work. India has also seen a fair amount - indeed
    our first Ruby project was run out of Bangalore. The UK has seen
    less uptake. This probably reflects the fact that our early Ruby
    advocates were mostly US based and there was considerable skepticism
    to Ruby in the UK. The level of involvement from India is
    encouraging, traditionally India is seen as a laggard in using new
    technologies but we seem to be doing a reasonable job of making
    our Indian offices be rather different.


Our experience selling Ruby work is that using a dynamic
    language like Ruby fits in well with our overall appeal. Our
    strength is that we hire highly talented people who are difficult
    to attract to the typical IT organization. Ruby has a philosophy
    of an environment that gives a talented developer more leverage,
    rather than trying to protect a less talented developer from
    errors. An environment like Ruby thus gives our developers more
    ability to produce their true value.


Ruby also fits in with our preference for using agile software
    development processes. The agile philosophy is one of rapid
    feedback by building software and reviewing it regularly with the
    customer. The more productive an development environment, the more
    frequently you can review progress, and the better the agile
    âinspect and adaptâ process works.


## Questions About Ruby


### Was Ruby the Right Choice?


When looking back on our 41 projects, perhaps the most
    important question to ask is whether the Ruby platform was the
    correct choice. One way to approach that question is to ask
    technical leads on the project whether, in hindsight, they think
    the choice was correct.


![](rubyAtThoughtworks/hindsightPie.jpg)


Figure 4: Was Ruby the correct choice of platform for
    this project?


As Figure 4
    indicates, the vote was a very positive 36 to 5 support of the
    choice. As a group our technical leads are usually not shy of
    indicating if they are unhappy with a technological choice. So I
    see this as a firm statement of the viability of the Ruby platform
    as a reasonable choice.


I dug a little more into the five regretful projects. The first
    thing that stood out was that in four of the five cases, the leads
    felt that using Ruby wasn't a worse choice than the
    alternatives. Ruby's relative unusualness means that we feel that
    using Ruby has to come with a benefit over alternatives, if Ruby
    is the same as a more widely used option, then it isn't worth
    introducing the unusual technology. Four of the five also reported
    problems due to integration with other technologies that Ruby
    isn't as well suited for. .NET tools tend to integrate better with
    .NET technologies, for example. Another theme that two of the
    projects reported was social issues - that people in the client
    organization were opposed to Ruby or other dynamic languages. The
    one worse-off project showed these social problems - an IT
    organization that resisted Ruby tooth and nail (the business
    sponsor in this case was a Ruby fan).


Indeed when I asked further about red flags for using Ruby in
    software project, the only clear answer was around social issues.
    Ruby was generally accepted or encouraged for our software
    development work, but the biggest sign to avoid it was a social
    resistance from the client.


### Is Ruby More Productive?


When people are asked about why Ruby should be used on a
    project, the most common answer is for increased productivity. One
    early indicator was an assessment of a project that suggested that
    Ruby would have yielded an order of magnitude improvement in
    productivity.


As a result it seemed obvious to survey the project technical
    leads and ask them about productivity - had ruby increased
    productivity and if so, by how much. I asked them to compare this
    to a mainstream (Java or .NET) project done in the most productive
    way they knew how.


![](rubyAtThoughtworks/productivityBar.jpg)


Figure 5: How much did
    Ruby improve productivity for this project? (Compared to the best
    mainstream tools you know.)


You should take these result with some salt. After all there is
    no way we can objectively measure software productivity. These are
    just the subjective, qualitative assessments from the technical
    lead of each project. (I didn't get a response from all projects.)
    However they are still suggestive that there's a real productivity
    boost going on.


This suggestion is further reinforced by staffing
    considerations. Scott Conley, who manages our Atlanta office,
    reports that once a ruby project has got going, he expects them to
    need 50% more people whose focus is on requirements preparation
    than would be expected for other technologies.


One thing we have seen is that you shouldn't expect these
    productivity increases to turn up right away. I've heard several
    times that people were alarmed in early weeks about the slow
    progress of a new Ruby team - a consequence of what I call the
    [Improvement
    Ravine](https://martinfowler.com/bliki/ImprovementRavine.html). It does take time for a Ruby team to get the hang of
    how the platform works and during that time they'll be slower than
    you expect.


The improvement ravine is a common phenomenon and a usual
    palliative is to ensure there are some experienced people on the
    team. Our history, however, is that the most important experience
    here is that of dynamic languages that support the kinds of
    meta-programming features that Ruby does, rather than specifically
    Ruby experience. As Scott Conley puts it: the difference is between
    efficiency risk and delivery risk. A team with dynamic language
    experience but little Ruby experience will be slower initially
    (efficiency risk) but a team without any dynamic language
    experience can produce a knotty code base that could risk the
    overall delivery.


### Is Ruby Slow?


In a word âyesâ. Search around for benchmarks on the net and
    you'll find numerous surveys that show that, even by the standards
    of scripting languages, Ruby is a tortoise.


On the whole, however, this has been irrelevant to us. Most of
    our uses of Ruby are in building database backed websites. I've
    visited many projects over the decades like this, using Ruby and
    other technologies, nearly every project has spent time working on
    performance issues and in almost every case those performance
    issues are database access. People spend time tuning SQL not
    tuning their processing code. So since most applications are I/O
    bound, the use of a slow language for processing doesn't make any
    appreciable impact to the overall performance of a system.


You'll notice I've used the usual pundit weasel words in the
    above paragraph. Although almost every project is I/O bound, you
    do run into the occasional exception - and an interesting one is
    Mingle. Mingle is unusual in many ways. It's very dynamic display
    means it can't use any page caching to improve performance, which
    immediately makes it unlike most web applications. As a result it
    isn't I/O bound and for good performance needs more hardware than
    many people expect (a four core box with 2GB of memory to support
    a 20-40 person team).


But the Mingle team still feel they made the right choice in
    using Ruby. The Mingle team has built many features very quickly
    and they feel the productivity boost they got from Ruby is worth
    the higher hardware demands on the final product. As with so many
    things, this is a hardware versus productivity trade-off - one of
    the oldest trade-offs in computing. Each team needs to think about
    which matters. The good news here is that Mingle has good
    horizontal scalability (throw more processors at it and you get
    proportionally good performance). Hardware scalability is often the
    most valuable thing you can have in these situations as hardware
    costs keep declining.


I should re-emphasize. For most projects Ruby's speed has been
    irrelevant as almost all of them are I/O bound. Mingle is an
    exception, not the common case.


### Is a Ruby Code-base Hard to Understand?


A concern we frequently hear about Ruby is that its dynamic
    typing, support for meta-programming, and lack of tools makes it
    liable to leave a code base that's difficult to follow. In general
    this hasn't turned out to be a issue in practice for us. The story
    I hear is that the fact that you can write much less code for the
    same functionality means that it's easier to keep the code clean
    than it is for mainstream languages.


That said, it's important to remember our context. Thoughtworks
    developers tend to be far above average in terms of ability and
    also very keen on highly disciplined approaches, such as Extreme
    Programming. We place a high value on testing (something that's
    true of the Ruby community generally) and these tests do much to
    keep the code base clear. So I can't say whether our experiences
    will carry over to less able and disciplined developers. (Even the
    tooling and relative control of other languages doesn't stop us
    from seeing some pretty horrible code, so it's open to question
    whether a poor Ruby code base would be that much worse.)


We have seen a common sequence of attitudes to
    meta-programming.


![](rubyAtThoughtworks/metaprogramming.png)


Figure 6: Progression
    of feelings about meta-programming

- Scary and Bad: People are wary of meta-programming and don't use it much
- Scary and Good: people begin to see the value of
      meta-programming but are still uncomfortable with using it.
- Easy and Good: as people get comfortable they begin to use
      it too much, which can complicate the code-base.
- Easy and Bad: people are wary of meta-programming and realize
      that it's very useful in small doses.


In the end the analogy I like best for these kinds of
    techniques is that they are like prescription drugs. They are very
    valuable in small amounts but you need to ensure that you don't
    overdose.


As with many things, experience is the great helper here as it
    can get you through this curve more rapidly. In particularly it's
    important to expect this adoption curve, particularly the
    over-usage. When learning something new it's common to over-use it
    at some stage because without crossing the line it's hard to know
    where that line is. It can also be useful to try and build a
    sandbox - a relatively contained area of the code-base for people
    to overdo the meta-programming in. With a suitable sandbox it's
    easier to undo the over-usage later on.


### Is Ruby a Viable Platform


All of these questions sum up into the key question for us: is
    Ruby (and Rails) a viable platform for us and our clients. The
    answer thus far is a resounding âyesâ. It offers palpable gains in
    productivity, allowing us to be more responsive and produce better
    software, more quickly for our clients. This isn't to say it's the
    right choice for all situations. Choosing a development platform
    is never a simple choice, particularly since it usually is more of
    a social choice than a technological choice. But the headline
    conclusion is that Ruby is a choice that's worth considering,
    worthy enough for us to want to keep this tool in our toolkit.


An interesting side question here is the role of other
    less-common languages. Should we be using Groovy, F#, Python,
    Smalltalk, and others? I wouldn't be surprised if many of the same
    trade-offs we see for Ruby are true also for these other
    languages. I hope we'll see some of these added to our toolkit in
    the future.


I should also stress that it isn't a case of either/or when it
    comes to using these languages and the mainstream Java/C#
    options. I've always advocated that development teams using a
    language like Java/C# should also use a scripting language for
    various support tasks. Ruby makes an excellent choice for this,
    and we are seeing this combination increase on our projects. With
    the rise of support for these languages on the JVM and CLR, we see
    more opportunities to intermix different languages with different
    strengths - an approach Neal Ford refers to as [Polyglot
    Programming](http://memeagora.blogspot.com/2006/12/polyglot-programming.html).


## Some Development Tips


In this last section, I'll run over a grab-bag of lessons we've
    learned from using Ruby.


### Testing with Active Record


Right at the beginning of our use of Ruby, there was a debate on
    how best to organize testing in the presence of the Active Record
    database layer in Rails. The basic problem is that most of the
    time, performance of enterprise applications is dominated by
    database access. We've found that by using a [Test Double](https://martinfowler.com/bliki/TestDouble.html) we
    can greatly speed up our tests. Having fast tests is crucial to
    our test-intensive development process. Kent Beck recommends a
    basic commit build of under ten minutes. Most of our projects
    manage this these days, and using a database double is a vital
    part of achieving it.


The problem with Active Record is that by combining database
    access code with business logic, it's rather harder to create a
    database double. The Mingle team's reaction to this was to accept
    that Rails binds the database tightly and thus run all the commit
    tests against a real database.


The contrary view was advocated most firmly by the Atlanta and
    Jersey teams. Ruby has a powerful feature that allows you to
    redefine methods at run-time. You can use this to take an active
    record class, and redefine the the database access methods in that
    class as stubs. The team started the gem [unitrecord](http://github.com/dan-manges/unit-record) to help
    with this.


In the three years, we've not seen a generally accepted victor
    in this debate. The Mingle team run a couple of thousand tests
    against a real postgres database in around 8
    minutes. (They parallelize the tests to make use of multiple
    cores.) The Atlanta and Jersey teams consider it valuable that
    their commit test runs in 2 minutes with stubs versus 8 minutes
    without. The trade-off is the simplicity of the direct database tests
    versus the faster commit build of the stubbed tests.


While both teams are broadly happy with their positions in this
    debate, the use of stubbing has led to another issue for the
    Atlanta/Jersey teams. As the teams became familiar with using
    method stubbing, they used it more and more - falling into the
    inevitable over-usage where unit tests would stub out every method
    other than the one being tested. The problem here, as often with
    using doubles, is brittle tests. As you change the behavior of the
    application, you also have to change lots of doubles that are
    mimicking the old behavior. This over-usage has led both teams to
    move away from stubbed unit tests and to use more rails-style
    functional tests with direct database access.


### Active Record Leaks


A common situation that people report is time spent futzing
    with SQL. Active Record does a good job of hiding much database
    access from the programmer, but it fails to hide it all -
    essentially the abstraction leaks. As a result people have to
    spend a reasonable amount of time working with SQL directly.


This leakiness is a common feature of object/relational mapping
    frameworks. Pretty much every time I talk to people on a project,
    they'll say that the O/R mapping framework hides the SQL
    efficiently about 80-90% of the time, but you do need to spend
    some time working on SQL in order to get decent performance. So in
    this respect Active Record is really no different from any other
    O/R mapper.


Indeed one comment I do hear is that with Active Record, the
    abstraction breaks cleanly. When chatting with DHH, he's always
    stressed that he believes that developers who use a relational
    database should know how to work with SQL. Active Record simplifies
    the common cases, but once you start getting to more complicated
    scenarios it expects you use SQL directly.


I don't see the leakiness of the O/R abstraction as a
    condemnation of these frameworks. The point of these frameworks is
    to improve productivity by making the easier to do common
    things. It allows a team to focus its effort on the few cases that
    really matter. The problem only comes when a team believes the
    abstraction is water-tight, and puts no effort into working with
    SQL. It's a common failing, but not a reason to abandon the real
    advantages of O/R frameworks when they are used correctly.


### Long Running Requests


A common problem we've seen is applications that get into a
    tangle when they take on a task that takes some time to carry
    out. Done naively this can result in the web request handler going
    dark for a worryingly long time while it deals with the request.


This is a very common issue with any human interface, and has a
    common solution - handing off the task to a background 
    process or thread. Anyone who has programmed with a rich-client
    GUI application will recognize doing something like this. People
    do get themselves into trouble, however, if this hand-off and
    communication is done badly.


The route I prefer, and fortunately it seems most
    ThoughtWorkers agree with, is to use an actor. In this
    model the web request handler takes any long-running task, wraps
    it in a command and puts it it onto a queue. The background
    actor then monitors the queue, taking commands off the queue and
    executing them, signaling the human-interaction actor when it's
    done with each one. The queue usually starts as a table in the
    database, and then may migrate to a real message queue system if
    required.


As with the leakiness of Active Record, I point this out not
    because it's a particular problem to Rails applications, we see
    this in all sorts of applications. It's worth pointing out because
    it seems too easy for many people using Rails to forget that this
    kind of thing happens, and thus they need to use this kind of
    pattern. We have found that Rails makes much of the repetitive
    part of web application easier and quicker to do - but the more
    involved stuff remains.


### Deployment


Rails applications are easy to build, but sadly have been very
    awkward to deploy. The common scenario of using a pack of 
    several mongrel web servers is at best rather fiddly to set
    up. This is something that has stuck out rather starkly due to the
    contrast with the smoothness of much of the rest of the ruby
    experience.


The current consensus is that Phusion Passenger makes this
    whole thing very much simpler and is now the recommended
    deployment approach with the MRI.


We've been also big fans of using JRuby for deployments. JRuby
    allows people to use the standard Java Web-App stack, which can
    make it much easier to deal with in many corporate
    settings. Mingle has also used this approach to make it easier to
    install for customers. Indeed the Mingle team does all its
    development with the MRI but deploys to JRuby. They do this
    because the faster startup time of the MRI makes it quicker to
    develop on. (JRuby requires a JVM start-up, which is noticeably
    hesitant.)


### Controlling Gems


Ruby includes a package-management system, Ruby Gems, that
    makes it easy to install and upgrade third-party libraries. Rails
    also has plugins that carry out a similar task for rails. These
    are good tools, but it's easy for teams to get in a tangle if
    different machines are set up with different versions of different
    libraries.


There's a couple of ways to handle this. The first approach
    involves taking a copy of the source code for all third-party
    libraries and checking that into source control. This way a simple
    checkout will get you all the right version of all the
    libraries. A second approach is to use a script that downloads and
    activates the correct versions of all libraries. This script needs
    to be kept in source control.


Along similar lines, most teams also takes a copy of the Rails
    source itself. This allows them to apply patches to Rails directly
    to fix any bugs or other vital issues. These patches can then be
    sent to the core team. Using distributed version control systems,
    like git, have made this a good bit easier to manage. It's
    certainly much easier than our memories of having to decompile and
    patch Java application servers in the past.


### Schedule Time for Updates


Ruby generally, and Rails in particular, moves quickly. There
    are frequent updates to the rails system, with features that we
    want to use. We've found that we need to ensure we schedule time
    for handling rails updates and include these in the planning
    process. They are more significant than for other platforms, but
    the good news is that there's a steady stream of new capabilities.


### Developing on Windows


Ruby was born in the unix world, and most of the people who
    have flocked to the platform use forward slashes for directory
    paths. It is possible to run, deploy, and develop for ruby on a
    windows platform, but it's also much more tricky. Our general
    advice is to use a unix platform for all development. Macs are
    commonly preferred, but plenty of people use other FOSS Unixen
    too.


We hope this situation will change as Iron Ruby develops. It
    would be nice to have the option to deploy Ruby applications on
    the base Unix, JVM, or the CLR. Indeed this would make Ruby a
    particularly flexible option for runtime support across multiple
    platforms. It would also help our .NET projects to have Ruby as a
    scripting language in conjunction with the mainline .NET languages.


---
