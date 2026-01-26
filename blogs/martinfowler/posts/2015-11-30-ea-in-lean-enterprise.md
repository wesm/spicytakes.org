---
title: "The Role of an Enterprise Architect in a Lean   Enterprise"
description: "When an organization takes on an agile mindset, enterprise architecture     doesn't go away, but the role of enterprise architects changes. Enterprise     Architects no longer make choices, but help o"
date: 2015-11-30T00:00:00
tags: ["agile", "enterprise architecture", "technical leadership", "lean"]
url: https://martinfowler.com/articles/ea-in-lean-enterprise.html
slug: ea-in-lean-enterprise
word_count: 2335
---


If you are an Enterprise Architect (EA) in an organization transitioning to lean or
    agile practices, you may be feeling a bit lost. You have worked hard to get
    where you are. You probably wrote most of the critical system software keeping your
    enterprise running. You helped implement and maybe even designed the architecture. You
    know some of it is older technology and a bit fragile, but with too few resources and
    too little time, compromises have to be made. In fact, your own ability to keep up
    with the latest trends have suffered because only you know how to keep things working.
    To help manage time, you have implemented universal standards and tried to funnel
    requests to architecture review boards or other planned meetings. Developers routinely
    work around the system, complaining that process holds them back, but you know that
    these things are there for the good of the company so you reinforce the policy to try
    to keep control.


Now, new leadership or a consulting firm arrives and declares that the organization is
    âbecoming agileâ. The developers read this as a mandate to do whatever they want in the
    name of agility and flexibility. They start to treat you like a relic of the past and
    subvert or ignore you. They introduce practices and technologies that risk
    destabilizing the infrastructure or failing at a critical moment. You know that the
    business needs you to do your job, but you feel like everyone is working against
    you.


![](ea-in-lean-enterprise/dev-flow-chart.png)


The truth is that they need your job to be done, perhaps more now than ever. That
    job is to use your knowledge and experience to minimize risk, manage cost, build
    capability in IT and align the technology mission with the business. The mission
    remains the same, but the way to go about it is a bit different. Both Lean and agile
    focus on value creation, waste reduction and rapid feedback, so you will need some new
    practices to be successful in these new environments. The new toolbox includes sharing
    a simple vision, building bridges, aligning the business, and providing guidance, all in
    an effort to promote innovation.


## How to get there


Overall, this is a shift from the traditional practices of the EA and
      architecture team. Instead of a centralized EA group making decisions for the
      development teams, you are now an influencer and aggregator of information. Your
      role is no longer to make choices, but to help others make the right choice and then
      radiate that information. Doing this requires some new tools and techniques. Following 
      are some ideas on how to act in this new role. All of them are high level and do not 
      all apply to every organization. The goal is to be nimble and responsive to the needs 
      of the teams you support; experiment with some techniques, measure their effectiveness, 
      keep the ones that work and pivot on the ones that do not.


### Have and share a vision


A first and important step to promoting consistency is having a long-term
        vision for the enterprise portfolio. Being able to describe both the current state
        and future state architectures is essential to bringing projects in line. Start by
        assessing the current portfolio. Map out what systems exist and what they do. This
        does not need to be deeply detailed or call out individual servers. Instead, focus
        on applications and products and how they relate. Multiple layers may be required.
        If the enterprise is big enough, break the problem down into functional areas and
        map them out individually. If there is an underlying architectural pattern or
        strategy, identify it and where it has and has not been followed. For example, if
        the enterprise strategy is a Service Oriented Architecture, which applications
        work around it and access the master data directly? Where are applications
        communicating via a common database?


Once you have the current state mapped out, think about what you would like
        the architecture to look like in the future. Do you want to keep the same
        underlying strategy? Would it be better to pivot to a different model altogether?
        What are the strengths and weaknesses of your current strategy? If you want to
        evolve the current strategy, produce an updated view of the architecture where the
        inconsistent areas are made true with the rest. If you think that a wholesale
        strategic change is necessary, map out what the ideal end-state would look like.
        Understand that this is a long range vision but one that you want the rest of the
        technology group to follow.


Now that you have a vision, you need to make sure that it is understood by the
        project technical leaders in your organization. Present your vision to key
        developers and get their feedback and input. They likely know better than you why
        some things are the way they are and can help you understand.
        Be willing, even eager, to adjust the vision based on their reaction.
        If you are making
        radical changes to the overall architecture or a particular group’s area, try to
        get them bought in on the change. It will make bringing your vision to life
        easier. Try to avoid making the architecture a mandate, instead use it as a tool
        for common understanding with developers and their teams. Remember that you are
        trying to make them your collaborators and allies.
        Their active engagement with the vision is more valuable than
        getting the vision exactly the way you'd like it.


When you feel some level of consensus, make the current and future state
        architectures visible. This does not mean in a folder on a drive or a Sharepoint
        site or a Wiki. Make posters or wall size printouts. Display them in multiple
        areas. The goal is to make sure that everyone can share the vision and continue to
        move towards it. As the architecture evolves, update the visuals to reflect the
        work done and any change in direction. Show where improvement is being made and
        acknowledge the teams that are making it. Help others have pride in coming
        together to build something great and they will support it.


### Build bridges


Once you have a vision, you want to see it come to life. But since you and your
        team are not developing or managing projects, how can you make this happen? The
        best way is become a partner and resource for the development teams. Your purpose
        is not to limit or block progress but instead to enable it. When a development
        effort is starting, reach out to the technical and project leadership. Offer them
        a refreshed view of the target enterprise architecture and discuss how their
        project can enable that vision. Often times teams are engaging in work that is
        similar to other ongoing or completed projects in the enterprise. Make sure that
        they are aware of these projects so that they can leverage anything from shared
        experience to actual code and artifacts. Try to avoid getting mired in the details
        of the implementation; do not worry about what libraries or versions are going to
        be used. Focus instead on the high-level goals and design of the project and how
        it aligns to the overall vision.


![](ea-in-lean-enterprise/bridges.png)


When discussing projects, inevitably technology choices will come up. Most of
        the time teams are content to use similar technologies to other projects in the
        enterprise. Occasionally, however, technologists learn about a new technology and
        want to use it to solve their problem. Avoid the temptation to immediately say no
        or assume that they are selecting the new tool just because it is new and fun.
        While that can and does happen, new tools are created to solve problems and it
        might just be the right time to move forward. Discuss the choice with the
        technology team to determine if they have a good argument for using the new
        technology. Make sure they understand the cost and difficulty of bringing a new
        platform to production and that the benefits outweigh this cost. You may have to
        listen for a bit then do some research before finishing the discussion. Consider
        doing a time-boxed proof-of-concept with real measurements and boundaries to
        determine the feasibility. If, in the end, the new technology is not the right
        choice, try to gain consensus from the developers or their leadership. Avoid
        making it a mandate if at all possible. This will help generate good will with the
        development teams and ensure that they will include you in future decisions. When
        experimenting with new tools or technologies, limit the number of experiments
        ongoing in the enterprise at any one time. It will be hard to measure the effects
        accurately with too much simultaneous change.


Ultimately, success as an EA is only made possible with the support of the
        development teams. If you treat them like subordinates they will find ways around
        you and put your vision and strategy at risk. You will still be held accountable
        for the outcomes with little ability to change them. If, instead, you treat them
        as partners they will help you realize your vision and everyone will get to be
        successful. Embrace change but measure it and make sure that everyone understands
        the value of the change. Ultimately, always try to guide teams to the vision of
        the enterprise architecture.


### Find Opportunities for Change


Big change takes time and opportunity. Once you have your vision for the future
        and start to build excitement within the enterprise, you will want to see results
        immediately. It is important to keep in mind that big changes in architecture need
        to come gradually and at the right time. Use existing projects in the portfolio to
        start the process of change. Guide new implementations to move toward the
        architectural vision. Keep in mind that opportunities to change code and move in
        the desired direction may not come at the speed or in area that you want them to.
        Learn to celebrate the victories, however small, and stay vigilant for chances to
        make positive change.


That being said, work with the business to prioritize projects that address the
        worst parts of the existing portfolio. Business leaders rarely understand the
        value of changing technical components nor the cost of maintaining the status quo.
        When purely technical changes are warranted, it will fall to you to create
        opportunities to change them. Make sure to frame the change in terms of value to
        the business in future savings offsetting the cost to implement or in terms of
        risk reduction. If necessary, find a partner in a business function and create a
        project that both adds new business value and enables a change in architecture.
        Seek opportunities to retire old applications and hardware that are a drag on the
        budget and operations teams.


Patience with the pace of change will help avoid frustration. Remember that
        change can only happen within the context of ongoing work, so make the most of the
        projects in the budget and portfolio. Create opportunities by identifying new
        projects that will generate new value for the business or save more money than the
        cost of development. Keep in mind that generating business value is your primary
        goal, so avoid purely technical projects that are interesting but not valuable. As
        the business sees increased production and value from following your vision,
        momentum will grow and the pace of change will increase. Until it does, keep
        shaping the work and refining the vision.


### Build a Community of Learning


In addition to having a vision for the overall enterprise architecture, it
        falls to the EA to see that vision executed with the right skills and practices.
        While each development team will develop the skills it needs to succeed, sharing
        the best skills and practices across different teams will help each of them
        execute better and have a shared sense of purpose. As the bridge between teams,
        you are best suited to fostering this sense of community.


Building community can be done a variety of ways, from informal lunches to 3rd
        party training. Rather than try to determine what will work for your organization,
        form a group of technologists from tech leads to developers who are passionate
        about their craft and let them help. Have the team meet on a regular cadence to
        plan events. Make sure to build in some time for development teams to share what
        they have learned - both what has been successful and what they have rejected.
        Having a chance to share with the whole IT organization will start to build the
        sense of community that will result in a healthy organization.


Avoid forcing people to attend training and learning activities. Make them open
        to all but optional. People who are not interested will be a distraction either by
        acting out or appearing bored, demoralizing the presenter. Those who are
        passionate will welcome the chance to learn and grow; those who are not will not
        benefit from required attendance.


A sense of a community and opportunities to learn will energize developers and
        promote retention. By leading the core of the community, you can guide the
        development of your organization in alignment with your vision for its future.
        Allowing others to participate in this guidance will identify and build leadership
        from within. A strong sense of pride and community will lead to better quality and
        more collaboration.


## One day at a time


Change is neither easy nor fast. Moving to a new set of practices will take time
      and effort, but will be worth it in the end. When your teams are creating value
      together and the business sees IT as a partner instead of a burden it will all be
      worth it. Remember that to be an EA in a Lean Enterprise is to build relationships
      between development teams and the business. Create a vision and guide development
      toward it. Be broad, not deep. Help developers invest in themselves. Experiment
      wisely. Most importantly, enjoy yourself, learn new things, create value and turn
      your organization into an industry leading innovator.


---
