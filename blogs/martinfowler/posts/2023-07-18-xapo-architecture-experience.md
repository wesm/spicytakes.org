---
title: "Decentralizing the Practice of Architecture at Xapo Bank"
description: "Xapo was founded as a Bitcoin service provider and developed into an   online bank. During this transition it needed to reassess its software estate   and establish an architecture capability to guide"
date: 2023-07-18T00:00:00
tags: ["enterprise architecture", "experience reports", "technical leadership", "domain driven design"]
url: https://martinfowler.com/articles/xapo-architecture-experience.html
slug: xapo-architecture-experience
word_count: 4967
---


## Introduction


The role of software architecture in the practice of building software 
        systems has been long debated. At most organisations you will find some 
        sort of “Architecture” function, often under the banner of “Enterprise 
        Architecture”. This is usually a centralised team with the valid and 
        well-meaning aim of ensuring that all software built adheres to industry 
        and company standards, uses patterns and technologies that are the right 
        fit for the problem, is optimised for the problem space, will scale as 
        required, and avoids any unnecessary duplication. Indeed, it is essential 
        that all of these facets are considered when building any valuable 
        software within any domain and at any meaningful scale.


Typically, this architecture function undertakes the architectural 
        design work for all system changes, often (but not always) in isolation 
        from the development teams that will ultimately implement the solution. 
        These designs, once complete, are then handed over to the developers to 
        implement. This has been the way many organisations have worked for 
        decades. So what’s the problem? Lets list some:

- Centralised control keeps the knowledge in the heads of those who make 
          up the architecture function which removes the same responsibility from 
          implementing teams. This stifles creative thinking and curiosity, and 
          the inclination to respond to systems as they are seen running. 
          Architecture, to the teams which actually build them, is literally 
          “someone else’s problem”;
- Consequently, the team creating the architectural designs can be far 
          removed from the front line of implementation and can fail to acknowledge 
          genuine challenges related to a specific domain. Nor are they exposed to 
          the unforeseen (and unforeseeable) consequences of their designs as they 
          run within their containing ecosystem;
- This leads to long feedback loops between developers and architects 
          resulting in delays to delivery and, frequently, inadequate or 
          inappropriate architectures and designs;
- Ultimately the Architecture function becomes a bottleneck, with long 
          queue times as they have to manage the architectural changes, and learn 
          from the myriad results, from across the entire organisation.


When you add the 2020 global pandemic into the mix (and the fact that 
        systems are now increasingly distributed and evolve constantly and 
        incrementally) these challenges are multiplied. There has been a huge 
        rise in the number of organisations moving to a more remote and more 
        flexible way of working. Traditional face to face collaborative forums, 
        where knowledge is retained within a small group of individuals, broke 
        down. Understanding of the rationale behind decisions is lost, gaps form 
        in collective knowledge and often the outcomes are poor software design 
        and even more delays.


Of course these challenges existed prior to the pandemic, however, the 
        recent wholesale changes we have seen in how people work have thrown a 
        bright light onto the flaws of the old centralised ways of thinking about 
        software architecture.


Xapo had always worked in a decentralised and fully remote way, but when 
        the pandemic hit, they doubled down on decentralisation, but with the goal of 
        not compromising on architectural quality, responsiveness to change, or 
        conceptual integrity.


## Some Historical Context…


[Xapo](https://www.xapobank.com/?utm_source=mediaarticle&utm_medium=text&utm_campaign=gaq22023_earned_martinfowler&utm_content=decentralising) was founded in 2014, initially offering 
        Bitcoin services including hosted wallets, trading, payments and cold 
        storage to both retail and institutional customers, becoming the largest 
        and most trusted Bitcoin custodian in the world. In 2018 in line with it’s 
        mission to “Protect Your Life Savings” Xapo set out to become a fully licensed 
        and regulated Bank and VASP (Virtual Asset Service Provider) leveraging its 
        presence in Gibraltar under the GFSC. This pivot of approach allowed Xapo to 
        provide traditional banking services including a USD debit card, alongside 
        Bitcoin services from a fully regulated environment. In 2020 Xapo was granted 
        Banking and VASP licences and work to build the new Xapo Bank began.


Much of the existing Xapo software estate was able to be repurposed as 
        Xapo moved from e-money to full banking and VASP business models. However, 
        as you might expect, over the six years since Xapo was founded the weight 
        of technical debt, tight coupling and low cohesion of services exerted a 
        significant drag on delivery and speed of change. Changes often impacted 
        multiple teams and crossed several functional and subdomain boundaries. 
        To add to the challenges, Xapo personnel are distributed in over 40 
        countries and over 25 timezones!


Teams were organised around functional departments (Product, Design, 
        Architecture, Engineering, QA etc) and work flowed through those 
        departments in a fairly waterfall manner. Queuing and long wait times 
        were common and this was particularly pronounced as the small centralised 
        architecture team were required to contribute to, review and approve all 
        designs.


Deeply experienced and talented engineers were creating novel and high 
        quality software - it was clear the challenges here had nothing to do with 
        their skills or efforts. Processes and the organisation had 
        developed in an effort to do the right thing and ensure ongoing quality, 
        however, unwittingly that system and associated controls were now slowing 
        progress. How could Xapo create an organisation and system that allowed individual 
        contributors to reach their full potential, improving flow and reducing 
        friction all while maintaining and even improving our software and 
        architecture?


Finally, it’s useful to note that there had been previous efforts to regularly convene 
        the collective intelligence of Xapo with the purpose of making architectural 
        decisions. Named “the athenaeum'', it allowed engineers to raise, discuss and 
        decide on issues of architecture and design.  While well-attended initially, 
        it had floundered. Discussions became increasingly extended, failing to reach 
        conclusions, and consequently, the decisions required to make progress were 
        rarely made, or if they did, were rolled back after a subsequent week’s 
        discussion.


## Laying the Groundwork


It was clear measures were needed to reduce friction in the development 
        workflow. Additionally, in order to reduce queuing and hand-offs, the ability for 
        teams to be able to act independently and autonomously (as far as possible) 
        became key success factors.


The first thing Xapo did was to start thinking about our software in terms of 
        business domains rather than through the lens of technology functions. Noush and her team 
        knew that [Domain-Driven Design](https://www.goodreads.com/en/book/show/179133) was the way forward 
        ultimately but she started off by undertaking a crude assessment of how the 
        software fitted in to broad business subdomains (Payments, Cards, Banking 
        Operations, Compliance etc) and we leaned heavily on the 
        [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) work of Matthew Skelton and Manuel 
        Pais to create truly cross functional teams. Partnering with her colleagues 
        in Product and Operations over a few months, Noush and her team migrated the whole delivery 
        organisation to business-aligned Stream Aligned Teams (SATs).


In parallel Noush aimed to vastly improve our developer experience; previously 
        centralised operations and tight controls made it frustrating and difficult to 
        create or change services, change configurations or do anything without the 
        need for a ticket. In order to move at pace, Xapo engineering needed to optimise our processes 
        and tooling for team autonomy and full ownership of services throughout their 
        entire lifecycle. Xapo changed the mission of the Platform team to align with 
        this and started work in earnest to refactor infrastructure and tooling 
        to support it.


It was at this stage Noush engaged Thoughtworks. The aim of having access to 
        folks experienced in making this kind of transformational change across 
        entire organisations was to accelerate this change while supporting our 
        engineering and product folks and help them learn about these new principles 
        in a safe way.


Together we laid the groundwork across engineering by defining our core engineering 
        principles - the primary focus was to build software that was optimised for 
        team autonomy and a reduction in hand-offs - and socialising DDD as a key 
        organising concept. In this we continued the work started with the move to SATs, 
        thinking in more detail about our bounded contexts and aligning them 
        increasingly closely with the teams, informing our roadmaps and incrementally 
        improving our underlying architecture.


These foundations meant we knew where we wanted to go, and broadly how to get 
        there, but how to do it as a fully-remote, rapidly growing, incrementally 
        changing organisation was the next challenge.


As an organisation Xapo needed to get better at working even more asynchronously. 
        Being global and fully remote presents a number of challenges that don't exist 
        in organisations based in a few consolidated office locations. How could we 
        ensure that all team members shared the same overall goals and understanding? 
        How might we manage time so that engineers could optimise their working day in a way that 
        worked best for them? How should we support the onboarding of new team members and 
        help them to understand the context, reasoning and constraints of the 
        architectural decisions we made? Working with Thoughtworks Tech Principle 
        Andrew Harmel-Law and leaning heavily on his blog post we aimed to implement 
        a decentralised, conversational and advisory approach to our architecture which 
        empowered teams to make decisions independently, while ensuring advice was sought 
        from key stakeholders and experts. The Architecture Advisory Forum (AAF) at 
        Xapo was born. It’s somewhat fitting that a company founded around the 
        principles of decentralised access to finance should choose to manage 
        architecture in this way, fully decentralised and without the need for a 
        central approving authority.


## How it Works


The approach we followed was laid out in Andrew’s blog post: 
        [“Scaling the Practice of Architecture 
        Conversationally”](https://martinfowler.com/articles/scaling-architecture-conversationally.html). As with all instances of this approach, the 
        specifics of the Xapo organisation, our people, our software, the goals of our 
        business, and the nature of our culture all played key roles in how things ended 
        up working.


Three key factors are worth noting: firstly, Xapo was a company that had 
        pivoted, and was [in the early stages of a 
        significant, global, scale-up](https://martinfowler.com/articles/bottlenecks-of-scaleups/). Secondly, Xapiens were based everywhere. 
        Xapo truly is a global company, and as such, the default comms mode was 
        asynchronous and written. Thirdly, this global talent pool meant Xapiens were 
        smart people with extensive experience, and many opinions / advice to offer. It 
        had been noted by some that this had in the past got in the way of decision making 
        at pace.


We initially focused roll-out on three key areas: the architecture advice 
        process, ADRs (Architecture Decision Records), and the AAF. We kicked off all 
        these core elements together, instituting the AAF with a session which introduced 
        the architecture advice process. We pre-seeded proceedings with some 
        retrospective ADRs. These were nice and meaty, covering a recently made, 
        significant decision to migrate certain key services to a third-party supplier. 
        This was something all attendees would at least be partially interested in.


Our invitee list for the AAF was carefully curated: voices from across all 
        teams were present, as was architecture, infosec, infra, product, delivery, 
        regulatory, operations, treasury and even the executive. The standing agenda 
        that laid out the focus was key too. Beyond the standard AAF activities of 
        looking at [spikes followed by in-play ADRs](https://medium.com/@cat-mo/how-to-use-spikes-as-a-foundation-for-adrs-92bc1617617b), 
        we added further slots as follows:

- team-coupling issues (product and delivery were particularly important here - as 
          mentioned above, Xapo had initiated a Team Topologies-driven re-org to align for 
          flow just as Thoughtworks engaged),
- the four key metrics (as outlined in the [DORA State 
          of DevOps Report](https://cloud.google.com/devops/state-of-devops/) and the book [“Accelerate”](https://itrevolution.com/product/accelerate/)1,
- cloud spend


After a few iterations of AAFs we added a further slot where we discussed the progress 
        of ADRs. We wanted to see not only how rapidly decisions were being made, but also how 
        quickly those decisions were getting into code and out to prod. As a consequence of this 
        we added a further ADR status to the standard set: “adopted” which signified when the 
        ADR had been implemented and was running in prod.  We’ll talk about this in more detail 
        below.


A few notes on general aspects of the Xapo AAF are useful here. As an “async-first” 
        company, Noush constantly challenged Andrew to maximise the asynchronicity of the 
        implementation. Andrew initially pushed back against this, having seen the value of 
        conversation for all, not only those directly in the conversation. He needn’t have 
        worried. The face to face element - the weekly AAF meeting was halved in size from the 
        usual hour, but kept the same cadence. AAFs were always well attended and conversation 
        focused and valuable. Pre-work (sharing in-progress Spikes and proposed ADRs for early 
        advice-giving) and post-work (adding the advice that came up in the intense face-to-face 
        conversations in the AAF) was done diligently and the written records of ADRs, including 
        the oh-so-valuable advice sections rapidly became a great resource. It didn’t hurt that 
        the Xapo Architect who took over the running of the process once Andrew left had a 
        background in technical writing, a great ability to organise, and a superb attention to 
        detail.


Why did we not include architectural principles, or a tech radar (or even CFRs) at the 
        outset? The short answer is ‘they weren’t urgent’. Xapo engineering already had written 
        principles, but more importantly they already existed in the minds of the Xapien dev 
        teams. This does not mean however that we ignored challenges, and potential enhancements 
        to these implicit principles when they came up in the course of advice-giving.


The radar was also brought in later as self-management began to increasingly embed in the 
        growing and increasingly decoupled teams as instances of potential valuable divergence 
        and [“bounded buys”](https://www.thoughtworks.com/en-gb/radar/techniques/bounded-buy) became evident. Prior to that 
        point, the tech landscape had been incredibly (especially for an ex-startup) focussed: 
        when it was realised something was useful, Xapiens took it up, evaluated it, and 
        started using it.


ADRs also underwent an interesting evolution. Taking advantage of the aforementioned strong information 
        management skills of one of the Xapien architects we moved rapidly from a wiki-based 
        ADR repository (Confluence) to a ticketing-system-based one (Jira). Why? We’ve already 
        mentioned the strong desire to improve the throughput of decisions, right that way to 
        implementation and deployment. Having Jira as our ADR home allowed us to make the 
        “status” field and transitions between its various values into a data point.  Whenever 
        a new ADR-ticket was opened we had an auto-generated timestamp and the status set to 
        “draft”. When it came to the AAF the only requirement was to set the status “proposed” 
        and another timestamp would be added. (Making the agenda became easier too - we had a 
        standing “everything in proposed” query in the page template). Later moves to 
        “accepted” also had their timestamps and when we added the aforementioned status of 
        “adopted” to indicate when the decision had been coded and was running in PROD. By 
        moving to this tool we took nothing away from the teams - we still had a ticket 
        template which made the key ADR sections self-evident without losing any of the rich 
        text elements. We also took away the need to remember to update the timestamps when 
        statuses changed. Most importantly, we were still resident in the tooling developers 
        used on a daily basis. Most importantly, we gave ourselves the ability to run various 
        queries and draw various charts which gave insight into the progress of things.


What were we looking for in this additional data? The number of ADRs created was an 
        interesting data point, but key was the time taken to move from “draft” through to 
        “adopted”, both in aggregate and across the individual steps. As with the DORA four 
        key metrics “lead time (for decisions)” turned out to be a reliable indicator of 
        process and system health.  All these data points were shared with teams to allow 
        them to incrementally improve and self-correct, asking questions like “why has this 
        been in draft / proposed / accepted for so long?”.


The move to Jira also had a further benefit: its simple integrations with comms 
        systems such as Slack were far richer and focused in a way that matched Xapo’s 
        async culture. New ADRs could be auto-announced on by a slackbot. Changes in 
        status could be handled in the same way.  None of this was manual and we got 
        transparency for free.  Not only that, but by associating implementation Stories 
        with the ADR tickets we could start seeing work associated with ADRs and its 
        statuses. This came in particularly handy for cross-team ADRs such as the one 
        putting in improved trace-routing across many core systems.


## Benefits Realised


It was clear that the AAF/ADR approach would work very well at Xapo from an early 
        stage, and as various elements were moulded to fit with the Xapo culture, benefits 
        kept accruing. We’ve already mentioned a few wins arising from this, but what other 
        benefits were realised?


While not part of this approach, cross-functional requirements (CFRs) and tech 
        strategy gradually made their way to the surface. The former naturally arose as 
        ADRs were proposed, and were captured explicitly 
        when this happened.  The fact they became explicit allowed key AAF delegates to 
        weigh in at relevant points with their needs as these came to the fore. For 
        example, representatives from Regulatory and their delegates in the Product org 
        were able to make explicitly clear in a technical forum what the exact needs were 
        from a compliance perspective.


Points of technical strategy emerged too. Noush, present as CTO at most AAFs, 
        could share her thoughts on the overall technical direction, as well as the 
        constraints she was under.  These could then be discussed in the context of 
        specific decisions meaning that they were not only aligned with the 
        overall strategy, but also that the strategy could be stress-tested in the harsh 
        light of the team’s day-to-day reality.  Not only that, but by being exposed to, 
        and encouraged to participate in, discussions of this kind, the general strategy 
        became widely understood.


Also stress-tested were the team’s experience of, and alignment to, the principles. 
        We’ve already highlighted the most prominent example of a team’s and their ADR’s 
        encounter with a core principle, but this happened again and again in smaller ways. 
        As with the strategy, teams exposure to these conversations allowed them to not 
        only give implicit feedback on how the principles were shaping up in reality, but 
        also to propose changes. Consequently attendees could gain a view on alignment to 
        these principles across the organisation, not only abstractly but in their delivery 
        of software; a valuable data point.


This general “sense-making” capability of the AAF was powerful in more general ways 
        too. A key aspect of the scale-up work already mentioned was the transition to an 
        explicitly domain-driven architecture. As the work progressed, week-by-week, the 
        prevalence of domain-language notably increased. While initially not always distinct, 
        nor aligned to bounded contexts, the fact it was being used in relation to specific 
        ADRs meant advice on key DDD-approaches could be given in relation to real problems. 
        This accelerated the understanding of these various patterns, but also super-charged 
        the deeper understanding of Domain-Driven Design across the engineering teams, 
        initiating a virtuous cycle of paying attention to domain language, noting when it 
        gave insight into coupling and other key design issues (e.g. when it became clear two 
        teams were talking about the same domain concept in subtly different ways, or they 
        both seemed to be tending towards implementation of a service only one of them should 
        have implemented and the other delegated to), using this to get to the 
        point in discussions of those design issues, and then deploying them to solve 
        them and consequently improve both individual team and overall veolcities.


The introduction of the AAF didn’t mean there was no longer a role for the 
        architects in the organisation. Far from it, our small team continue to be as busy as ever 
        providing advice, supporting the AAF and focusing their time on high impact projects 
        that are moving the needle for Xapo. The move to empower our teams and having 
        decisions made much closer to the code base by the experts in those areas has had a 
        material impact on the time it takes to effect real change. Designs and decisions 
        that used to take weeks (or months!) now happen in days, are well documented, 
        understood by all and form part of the collective intelligence of our technical 
        community. Architecture is now a collective responsibility where anyone can share 
        ideas or challenge approaches all in line with our guiding principles.


## Lessons Learned


It would be negligent of us to give the impression that the adoption of this set 
        of interlinked practices, tools, approaches and mindsets was easy or without 
        challenge.  At the core is a need to shift to a new system of “common sense” and 
        that is an internal, human and group-level change.


The clearest indication of this is in the fact that the comfort of consensus is a 
        hard thing to let go of. You will recall that the Architectural Advice Process has 
        only one rule: “anyone can then take an architectural decision” and requires neither 
        need to reach either agreement, or seek approval from a higher power. Despite this, 
        even when conscious minds surrendered to the idea, the phrase “so, do we all agree?” 
        would be heard at AAF after AAF, just slipping out when discussions were concluding. 
        While this was a signal that the move to the new mindset was not yet complete, the 
        vocalising of this unconscious need did allow us to remind attendees that consensus 
        was not required, and decisions could be taken and actioned without it.


Another signal came in the form of the pursuit of “perfect” (without-compromise) 
        solutions aligned to the principles. While this happened far less, it was initially 
        evident that those less experienced in decision-making felt that those who used to 
        have these responsibilities, the “architects”, might just be sage-like in their 
        wisdom, and able to find the path to the best of all worlds.  Explicit focus on 
        trade-offs, and advice on the same from the architects slowly unpicked this mindset, 
        achieving real resolution when these began to be explicitly captured in the ADRs.  
        Bringing this out into the open meant that everyone concerned could be brought to 
        understand that not only was this compromise ok, but it was inevitable. For example 
        it was recognised that in the course of optimising Xapos services for team autonomy 
        effort was being duplicated. Was this a bad thing? Not necessarily. Coordination and 
        synchronisation can frequently have a greater overhead than the benefits the removal 
        of duplication delivers. What the discussion brought to the forefront was the general 
        understanding that in certain circumstances duplication could lead to a disjointed user 
        experience. In such cases, the benefits clearly outweighed the drawbacks of the 
        alignment effort. The consideration of this up front, and as a collective, helped 
        greatly on where to put the emphasis when compromises were being made.


Decisions also benefited greatly from always being couched in the context of business 
        decisions. Many times the deciding fact as to whether one option or another was the 
        “best” came down to product or business strategy. Having product representation in the 
        room for AAFs meant that they had all the context available for pending architectural 
        decisions, and could share their advice accordingly. A great example here is the 
        foundational product and design decision to have a single, universal user experience 
        wherever the mobile app was being used, whoever was using it, and most importantly 
        irregardless of platform. A great deal of effort was required to ensure the iOS and 
        Android experiences aligned everywhere, and without this product guidance it would 
        have been a significant waste of effort. However, because it was central to the whole 
        product ethos and experience it was essential.  Knowing this, teams could make 
        multiple strategically-aligned decisions very rapidly, with the beneficial side-effect 
        that everyone present knew why.


It’s also worth pointing out the more general benefits of this regular synchronous 
        catch-up. Not only did decisions collect the advice inputs they needed efficiently, but 
        (more importantly) everyone present, whether the decision was pertinent to them or not, 
        were exposed to the specifics of Xapo’s business and collective reasoning process.  This 
        had an incredible benefit when going back to work asynchronously, and teams were far 
        more aware of the details and subtleties of the path that Xapo was forging, week by 
        week. This is fundamentally important, because team autonomy without guidance and 
        direction results in chaos. Constraints like the Advice Process (including 
        responsibility) helped set Xapo free and reduced the vast array of things our engineers 
        needed to think about. Taking the time to think hard about Xapo’s tech pillars and 
        principles was also a key success factor.  With this general alignment and shared 
        understanding in place, and strengthened and updated every week by the short AAF, the 
        ability of all teams to deliver value in their focus time was impressive.


These high-value, high-impact weekly sessions had another benefit: they made it safe 
        for people to change minds, and occasionally, to be wrong or to fail. This was modelled 
        by everyone up to and including the CTO. For example, as the teams collectively learned 
        more about the tools of Domain-Driven Design (DDD), and saw how Xapo’s software 
        manifested many of DDDs patterns, it became necessary to re-assign services to different 
        teams, or refactor them to align with more appropriate teams and their bounded contexts. 
        This is not to say that the first cut of team splits made at the beginning of the Team 
        Topologies transformation wasn't too far away from ideal, but it could bear incremental 
        improvement.2  The CTO was the one who had made 
        the initial decisions on these teams, and the allocations of software to them.  By 
        refactoring these responsibility boundaries, based on and driven in part by the learnings 
        which arose with ADRs, people saw first hand designs, including organisational designs, 
        don't need to be right the first time.


2: 
      Our message here is don't get too hung up on getting it all perfect, get it good enough and make progress.


In order for this all to work, it became clear that consistent and regular curation of 
        the ADR backlog and well defined ADR ownership was important. Additionally, the benefits 
        of internally marketing the complete approach, both inside and outside of technology, 
        allowed folks to keep it at the front of their minds and see the benefits. Due to the 
        asynchronous and global nature of Xapo, it was decided to dedicate one full time person 
        to driving collaboration across engineering and beyond to ensure that this happens.


An example of this manifesting beneficially occurred when various ADRs were 
        re-visited. All decisions are made at a point in time, and should strive to capture as 
        much about the specifics of that context as possible. When it is clear that this 
        decision-context will change predictably at some point in the future, a re-evaluation 
        can be scheduled. This happened at Xapo when a non-strategic hosting decision was made 
        as it was the only viable option available at the time.  A fixed time period later, this 
        decision was re-visited, and another, subsequent ADR was undertaken to bring things back 
        into line and migrate onto the strategic cloud provider.


Before concluding this section it's important that we highlight one key fact: The AAFs 
        and Architecture Advice Process never existed in isolation. At Xapo, the groundwork laid up front had a 
        significant positive impact, as did the strengths of the existing Xapien culture.  The team 
        clearly benefited from the move to a Team-Topologies style org structure, a concurrent 
        focus on product thinking, continuous delivery infrastructure, and data provided by the 
        DORA four key metrics. Moving from a functional to stream-aligned team (SAT) model looks 
        easy on paper. In reality itwais a big change for any organisation and it was important 
        that Noush and co took the time and space to let it bed in and begin to fire well.


A crucial lesson that both Noush and Kamil learned at Xapo during the adoption of the AAF after 
        Thoughtworks left us is that it requires ongoing care and attention. Creating a 
        forum or structure alone is not enough to ensure its continued success. Rather, it 
        needs regular assessment and support to maintain its momentum and impact. This means we 
        have to encourage participation, provide resources and guidance, address any issues that 
        arise, and adapt to changing circumstances. Only by consistently nurturing and refining 
        our approach and outcomes can we ensure that it remains effective and valuable for Xapo 
        over the long term.


## What's Next?


The AAF and advice process has undoubtedly provided many benefits to Xapo. However, we in the engineering team 
        can’t allow ourselves to become complacent and we are seeking ways that we can continue 
        to improve. This is an opportunity to continue enhancing software development 
        practices and culture, and there are several opportunities under consideration at time of publishing.


Kamil is seeking to formalise an internal open-source model that will allow teams to 
        contribute across bounded contexts. This will enable developers to share code and best 
        practices across teams, reduce duplication of effort and provide great opportunities for 
        knowledge sharing. By leveraging the collective knowledge and expertise of our developers, 
        we can accelerate innovation, further improve the quality of our code and reduce queuing 
        and friction.


Kamil and the team also recognise the importance of continuing the work to improve and iterate on 
        developer experience (DevX) and tooling. By investing in tools and processes that 
        streamline development and reduce friction, Xapo can enable our developers to work even 
        more efficiently and effectively.


The entire Xapo engineering team will continue to develop and refine our tech principles to ensure that they align 
        with the evolving business goals and priorities. By regularly reviewing and updating our 
        principles, we can ensure that they remain relevant and provide guidance for our 
        development efforts.


Everyone sees the implementation of the AAF as just the beginning of our journey towards 
        continuously improving our software development practices and culture. By pursuing these 
        initiatives, the developers can be enabled to work more collaboratively, experiment with 
        new ideas, work more efficiently, and make better-informed decisions. This will ultimately 
        help deliver better software more quickly and support our broader business goals.


---
