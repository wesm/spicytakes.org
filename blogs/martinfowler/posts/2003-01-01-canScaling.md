---
title: "Canadian Workshop on Scaling XP/Agile Methods"
description: "As XP and other Agile methods gain popularity, questions are beginning to surface regarding how to scale XP beyond teams of 10-12 people.  In mid February 2003 a workshop dedicated to the subject was "
date: 2003-01-01T00:00:00
tags: ["agile", "conferences", "process theory"]
url: https://martinfowler.com/articles/canScaling.html
slug: canScaling
word_count: 2171
---


## Questions raised


In preparation for the conference participants were asked to submit their views on how
to scale XP and Agile methods for large teams.  Depending on whom you ask, the definition
of large can vary anywhere from 20-200 plus developers.


Specific questions posed to conference participants were:

- How scalable are the agile methods?
- What has been the experience of early adopters?
- What experiments can we conduct to expand the use of those methods?


Having participated in several XP projects, we were keen on hearing how others viewed
scaling XP as well as share our own experiences with XP on large teams.


## Ken Schwaber


The first keynote speaker was Ken Schwaber.  Ken and Jeff Sutherland are the authors
and founders of the Scrum agile methodology.  Ken started by describing his experiences
working with Scrum on large projects and several techniques he had successfully used in
the early stages of the project life cycle.


Ken explained on one project how the team was very concerned with getting the overall
architecture of the system proven in the early stages of development.  Early project
iterations (sprints in Scrum terminology) contained stories focused on proving the system
architecture peppered with several real business cases.  After several iterations, during
which the architecture was continuously refined and tested, the team had a good sense of
whether the architecture was sufficient for the demands of the business.


Scaling was then achieved by starting new teams with the founders of the original
architecture team.  With most of the architectural issues addressed, the new teams
could focus on implementing business logic on top of the then stable architecture.


Ken also emphasized the importance of having a Scrum master who did not manage the
team - rather it was very important that the team managed itself.  Ken found teams
were much more effective when they were self-organizing and could decide for themselves
how best to complete the work they were given.  This was a challenge for managers who
were used to a command and control style of leadership and was initially very counterintuitive.


An interesting point Ken touched on was how outsiders would initially perceive Agile methods.
As with all things new that have achieved some element of success, people will naturally ask
how this can work for them.  Is this the âsilver bulletâ they have been looking for?
Ken wondered if XP and Agile were to suffer a similar fate to CMM (Capability Maturity Model).


CMM had many great people behind it, articulating things that companies could do to
improve their chances of success on software projects, and demonstrate software process
maturity.  However, CMM has never been embraced and successfully implemented to the degree
the authors had originally intended.  It was reported that 2/3 of CMM project implementations
were broken.  Further, many in industry took on a cynical view of CMM when the level of
certification a company could achieve was often dependant on who they hired to perform
the certification.


Will Agile methods suffer a similar fate?  Sure the early adopters have had success,
but these teams are often filled with highly skilled, motivated, people who are passionate
about writing software.  Arguably, teams filled with these types of people would have been
successful regardless of the methodology used in name or practice.


In our opinion, this has less to do with Agile, and more the inescapable fact that
people have a first order effect on projects.  This becomes apparent when you look at
the converse of building these sorts of teams (less skilled, unmotivated, people who
are not passionate about writing software).  For these teams, no methodology used in
name or practice will make them successful.


While Ken agreed that excellent developers help make the process hum, in his experience
it has been equally true that people who have been categorized as average, or even poor,
often rise to excellence given a supportive, creative, team oriented environment as
provided by Agile.  He has seen previously disparate groups of average professionals
accomplish truly great things that he previously thought only the top tier people could
perform.


## Reports from the field


The middle part of the conference was reserved for other practitioners and researchers
to share their thoughts and experiences with large projects.


Philippe Kruchten (Rational) described how large teams (200+ persons) using RUP had
successfully delivered large projects in the past.  In the earlier project stages, a
team consisting of senior practitioners is used to complete the initial high-level
architecture and set the development practices.


As the project moves into the construction phase, more teams are added (seeded with
founders of the elaboration team).  When broken up appropriately, each team can work
fairly autonomously (in an iterative cycle).  In those instances where one team needs
components built from another, sync points and milestones can be coordinated between
the two.  Handling large projects this way gave teams the illusion they were decoupled
enough to gain the advantages of small Agile teams.


Gerard Meszaros of ClearStream Consulting shared his experiences working with large
teams building digital switches at a large telecommunications company. They used frequent
releases and had significant architectural change throughout the life cycle of the project.
However, the system had reached critical mass before they were able to do this.


Gerard also raised an interesting point regarding the current industry literature regarding
XP and Agile practices. In his opinion, most of today's literature is targeted towards
people who already know how to develop software. If XP is going to be brought beyond
the early adopters, a very different set of literature will be required. To repeat the analogy
used: âToday we have the cook books for people who know how to cook.  What we do not have
today are cook books for people who do not know how to cook.â


A large Canadian energy company shared their experiences regarding Agile adoption
within their company.  Using a combination of Scrum and XP, they have had great
success in managing projects.  With managements backing, they now have a team dedicated
to showing other groups within the company how Agile can be used to increase their chances
of success.  Further comments regarding XP and Scrum were the ability it provided teams to
adapt and modify the practices to meet each individual teams needs.  They preferred this to
the one size fits all form of project management they had used in the past.


The authors (Jonathan Rasmusson and Jim McDonald) were also given the opportunity to
share our own experiences with XP and large teams.  Because we had mostly worked with XP,
we looked at the core practices and broke them into two groups - those practices we
thought could scale, and those that would not.


We believe the XP practices related to the mechanics of writing coding could be scaled.
We see little that will prevent large teams of developers from writing tests, refactoring,
and pair programming.  People have been successfully practicing these techniques for many
years (before XP or Agile) on both large and small projects.  These are simply good practices.


However, those practices that were communication centric will be challenging to scale.
For instance daily standup meetings would become awkward with teams of 20+ people.
Iteration planning meetings, where all the developers and analysts gather to plan the
upcoming iteration, would be tough to manage due to the organizational and communication
overhead with coordinating so many people.  The greatest challenge we see with scaling XP,
is the same challenge we see every large project faces - how to effectively communicate
and coordinate large numbers of people.


We also start to question the question itself.  Why do people want to scale XP?
With success on small teams, it seems very counter intuitive to us to want to scale.
Rather, we would prefer to first look for alternatives on how large projects could be
scaled down to the size where we know XP works well.


## Martin Fowler


The last day of the conference started with a keynote from Martin Fowler titled âWhy Scaling
Agile is the Last Thing You Want To Doâ.  The title of his keynote changed the tone of
the conference.  Up until that point, much of the conference was dedicated towards trying
to answer the question around how to scale XP.  Martins keynote however turned the question
on its head and asked the audience if this is something we really want to do.


His talk was broken into two parts.  The first part was an experience report regarding a
Thoughtworks project involving a large team using a XP type of process on a complex leasing
application.  The second part further expanded on the title explaining why we should look for
alternatives before trying to scale XP.


Martin started by reminding us why building complicated business applications is challenging.
Business logic is an oxymoron.  There is nothing logical about most aspects of business
(especially leasing).  Capturing the business rules, hidden assumptions, special cases and
abstracting these into a solid, war crafted domain model one of the most challenging parts
of software design.


Requirements gathering is also very tough on large projects.  Martin provided an
interesting comparison between writing requirements documentation and writing books.
Writing a book requires a very large investment of time and energy.  Even after peer
reviews and feedback from professional editors, the author still is not always successful
at communicating his/her intended message to the audience.  His point was that if authors
have a hard time doing this with books, imagine what it must be like to capture the
requirements around a complicated business application given far fewer resources.


One practice that worked very well on the project was the rotation of people to different
parts of the application.  This was initially frustrating for the project analysts as a
developer just was beginning to understand the problem domain when they would moved to
another part of the system.  As the project progressed however, the benefits of moving
people to other parts of the application began to pay off.  Eventually, most developers
knew enough portions of the application that they could fill in many roles.  There was
less dependence on a small number of people to do work in specific parts of the application.
The developers themselves became stronger both technically and in the business domain.
Having a more global view of the application gave them insight into how best implement new
features while maintaining the overall system architecture.


The latter part of Martins keynote focused on why we should look for alternatives to
scaling agile.  Some projects do require large teams.  The amount of work needed to be
complete is often too large for a small team to handle within a reasonable period of time.
Examples of this are projects from the telecommunications industry and large military
applications.  For these teams, the question of how to scale Agile is very real.


Martin's experience however was that many teams were unnecessarily large.  These teams
should look for alternatives (like scaling the team size down) before trying to scale Agile.
Martin asked the audience to raise their hand if they had ever been on a project that could
have kept about the same level of productivity after removing the weakest half of the team.
The majority of the room raised their hands.  This seemed to reflect that many in the audience
had similar experiences and worked on projects where the teams had been much larger then
necessary.  Hence, instead of first looking at ways to scale XP and Agile, Martin recommended
teams first look for ways of scaling down projects that are unnecessarily large.


## Where's the proof?


One of the questions attendants seemed to have difficulty answering was what experiments
would provide empirical evidence that XP/Agile can be utilized on large projects.
The academic/research community has taken on the challenging task of coming up with
experiments and empirical evidence that Agile methods can scale to large teams.


While we empathize with the researchers desire to prove that Agile works, we see several
challenges in proving it.  Jonathan sees the challenge as trying to objectively measure
software quality and productivity.  Without definite, quantifiable measures around quality
and productivity, how can one conduct experiments around software engineering practices?
Jim believes that the path to truly understanding Agile is through the study of sociology
and studying the difficulty in quantifying and describing how humans interact.  With
communication playing such a pivotal role in Agile projects, he feels research in
these areas would shed more understanding into why Agile works.


## Summary


The conference itself was a great success and all attendants enjoyed the opportunity
to share their thoughts and ideas on how best to tackle the challenging problems put
forward by the research community.  It seems XP and other Agile processes are starting
to gain the attention of the academic world and are beginning to be taken seriously.
Regardless of any advice provided by early adopters, it seems clear that like any new tool,
XP will be applied and misapplied in the upcoming years.


---
