---
title: "Scaling the Practice of Architecture, Conversationally"
description: "Architecture need not be a monologue; delivered top-down from the      minds and mouths of a centralised few. This article describes another way      to do architecture; as a series of conversations, "
date: 2021-12-15T00:00:00
tags: ["enterprise architecture", "evolutionary design", "technical leadership"]
url: https://martinfowler.com/articles/scaling-architecture-conversationally.html
slug: scaling-architecture-conversationally
word_count: 6987
---


## When âtraditionalâ approaches to architecture break down


I'll be honest, “traditional” approaches to software architecture (i.e. 
      non-coding, decision-taking, diagram-drawing) are hard for me to make work at the 
      best of times. But while using them in the world of continuously delivering
      autonomous teams I’ve repeatedly found myself faced with an impossible
      task: to be everywhere, tolerating significant contextual variance, and
      blocking no-one.


It made me wonder. Was there an alternative?


Since publishing this article, Andrew has delved deeper into this
        content, and published [a book with O'Reilly](https://facilitatingsoftwarearchitecture.com).


There was: I stopped taking architectural decisions. Completely.


In this article I’ll introduce this alternative mindset and the
      associated set of tools and practices which allow me to upend the
      traditional role of a “Software Architect” while simultaneously bringing
      the practice of software architecture to the fore across development
      teams. More importantly, I’ll explain how, within this alternative
      approach, everyone can do the architecting they need, safely and
      efficiently, without everything descending into chaos. 1


1: 
      Although there will be a healthy dose of anarchy...


**We need more ways to “do” architecture, not less.**


The moves in software delivery towards
        ever-increasing team autonomy have, in my mind at least, heightened the
        need for more architectural thinking combined with alternative approaches
        to architectural decision-making.


Ensuring our software teams experience true autonomy raises a key
        problem: how might a small group of architects feed a significant number
        of hungry, value-stream-aligned teams? Why? Because in this environment
        Architects 2 now need to be in many, many more
        places at once, doing all that traditional âarchitectureâ.


2: 
      And I include myself in this group.


What we need is a workable way to approach the human-scaling challenges
        of team autonomy and the architectures which manifest as a result.


In the remainder of this article I’ll introduce an alternative way of
        doing and governing architecture. I’ll explain in detail what it is, how
        it works, and how you might adopt it yourself. Most importantly, I’ll
        highlight how to fail, in order that you might succeed.


## The most fundamental element: decision-making via the “Advice Process”


Let’s take as our starting point a team which we aim to make maximally
      independent. Clearly this team will need somehow to engage in
      architectural thinking and decision-taking, but how?


These “many centres of decision making” are precisely what we need, yet
      straight away it’s clear that traditional, top-down architecture, with a
      select group of all-powerful architects taking all the decisions, runs
      contrary to such a decentralised model. “And yet”, the challenge is voiced
      “decisions still need to be made - that’s what architecture is”, and these
      skeptics are right.


These architectural decisions must still be made deliberately -
      otherwise we’ll be back where we started, or worse. Therefore, the first
      aspect in this alternative approach, it’s core element in fact, must
      describe how it delivers on decision-making. It’s called the “Advice
      Process”.


The Advice Process is the core element of this anarchist, decentralised
      approach to architecture. It’s greatest quality is it’s remarkably
      simplicity. It comprises one rule, and one qualifier:


**The Rule:** anyone can make an architectural decision.


**The Qualifier:** before making the decision, the decision-taker must
      consult two groups: The first is everyone who will be meaningfully
      affected by the decision. The second is people with expertise in the area
      the decision is being taken.


That’s it. That’s the Advice Process in its entirety.


This apparent straightforwardness hides however a key concept which
      it’s worth making explicit; while decision-takers are in no way obliged to
      agree with the advice the folks in these two consulted groups give them,
      they must seek it out, and they must listen to and record it. We are not
      looking for consensus here, but we are looking for a broad range of inputs
      and voices.


A challenge frequently raised against this concerns just how many
      people must be consulted. It is a valid concern, but a mitigatable one.
      When deploying this technique we create a checklist to help those in the
      decision-making seat identify who to speak to, and in which regard.
      InfoSec impacted? Talk to the CISO. Getting close to PII? Engage Mary in
      the data team and Vanessa in legal. A potential change to the user
      onboarding flow? Talk to your UX lead. About to adopt a new cloud service?
      Chat to Kris the cloud architect. Thinking about a change to your API?
      Speak to all the leads of the teams who are your consumers.


Sometimes this list of consultees can be a long one. That’s fine. Some
      decisions are large ones, and the advice-scope is a clear indication of
      both size and import. Sometimes decisions can be made smaller in scope and
      many consequently are. Other times the sheer number of folks impacted
      makes the decide-ee think again. Is this thing which might make their life
      a little bit easier really worth the effort of consulting all those
      people? Or, can they split this large decision into multiple, smaller
      decisions? When decisions do proceed, they are frequently right-sized
      purely as a matter of expediency. 3


3: 
      The economics of decision-making is dealt with in great detail in The
      [Principles of Product Development Flow](https://www.amazon.com/gp/product/1935401009/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1935401009&linkCode=as2&tag=martinfowlerc-20) by
      Donald G. Reinertsen. Principles E8: The Principle of Small Decisions,
      E10: The First Perishability Principle and E11: The Subdivision Principle
      are particularly interesting in light of what we are discussing here.


Can we push the Advice Process further? Yes we can, and we ought. I
      always encourage those following it to specifically seek out those who
      will disagree with them. Freed from the need to agree with what they hear,
      they inevitably engage far more seriously. Consequently the depth and
      breadth of advice received is greater. Decisions don’t tend to suffer as a
      consequence either. Neither does their learning.


Which brings us to the broader topic of benefits of the Advice Process.
      When deployed, I have always seen better, faster, more accountable
      decisions, and most importantly decisions which are understood and owned 
      by those who implement them, precisely because the decidee is the 
      one with the need as well as the one who is accountable.


As a side-effect, the pool of available decision-takers also grows, each 
      of whom will soon be on the look-out for decisions which need to be made, 
      and, given the feeling of empowered safety that the Advice Process gives 
      them, flag them up and drive them to conclusion. The fact that a team's 
      need for a decision to be taken can be met by themselves also leads to 
      appropriate levels of bias-to-action, with accountability acting as a 
      brake when it's required.


By working in this way we remove both the need for a fixed and
      permanent hierarchy and an abiding master decision-taker. It is for these
      two reasons that the Advice Process is the most fundamental element of
      this approach to architecture, because decentralised decision-making is
      the core element of anything which aspires to call itself
      “anarchistic”.


But wait, did we just remove in one fell swoop all need for we
      “traditional” architects? Not at all, but clearly our role has changed. In
      the following sections of this article - which introduces the supporting
      elements of this approach - we will see a set of rejuvenated practices and
      tools which allow us to get the teams, and the businesses they underpin,
      where they need to be.


Before we proceed to these supporting elements it is useful to take a
      short detour to highlight and discuss the one thing that all the remaining
      elements to this decentralised approach share, and also have in common
      with the core element: their focus on conversation, and it’s role in
      efficiently arriving at, and spreading, shared understanding.


### The fundamental role of conversations


Alberto Brandolini, inventor of Event Storming famously quipped “it is
        the developer’s assumptions which get shipped to production” and he’s
        right; it’s primarily what a developer understands about a target
        architecture that matters, not what is in the head or diagrams of a lead
        architect. This problem is age-old. Eric Evans tackled it in 
        “[Domain Driven Design: Tackling Complexity in 
        the Heart of Software](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20)” and more recently my colleague Erik 
        Dörnenberg has spoken about it in his presentation 
        “[Architecture without Architects](https://www.youtube.com/watch?v=qVyt3qQ_7TA)”.


To me, it is this architecture, the one which is in the heads of those
        writing the code, that is the most important. In adopting this
        decentralised approach, where the practice of architectural
        decision-making is much more dispersed, this problem is in many ways,
        mitigated.


That’s something which helps me sleep at night.


However this decentralised, anarchistic approach then places front and
        centre another problem which all architectures must address: the delivery
        of a coherent whole. Here, we would seem to be at a disadvantage with our
        alternative approach. If everyone is empowered to make a decision, how do
        we, the “traditional” architects and ones who perhaps care most about the
        overall end result, ensure that the sum of all the individual decisions
        combine to form a coherent whole? How might we incorporate a longer-term
        perspective into those same decisions? And how might we support those who
        suddenly find themselves taking on levels of responsibility for which they
        might not feel comfortable?


Fortunately, another practitioner, and thinker in this space, Ruth
        Malan, has seen this before and shares the answer in her article “Do we
        still need architects?”:


> [In order for an architecture to be
>         successful] it is very much about ensuring that conversations that are
>         needed to be happening are happening - not always initiating them, nor
>         always helping to focus or navigate them, but ensuring they do happen […]
>         and guiding when needed
> -- [Ruth Malan](https://web.archive.org/web/20201222143814/https://www.ruthmalan.com/Journal/2016/2016JournalFebruary.htm#Still_Need_Architects)


Our adoption of the Advice Process opened up the space for anyone to
        make decisions, but it has also put conversations, the responsibility to
        seek out expertise, and think about impact at the core. The remainder of
        the elements of this approach, each of which supports the core element
        focus specifically on ensuring those conversations are as timely, focused
        and effective as possible. There are four of them:

1. a thinking and recording tool
2. a time and place for conversations;
3. a light to illuminate and guide towards a unified direction;
4. a means to sense the current technical landscape and climate.


We'll cover each of these in turn in a few seconds, but first I need to 
          clarify two things.


### What about strategy and cross-functional requirements?


It's worth a few sentences on what isn't covered in this approach:
          technical strategy and cross-functional requirements (CFRs).


Clearly both are essential for all software endeavors of any meaningful 
          size:


A well evangelized strategy can help the organization advance by 
          having decentralized teams prioritize technical activities which are best
          aligned with the org's maturity and needs. Clearly the best technical 
          decisions are those which support the strategy, and when this is the case 
          this can be called out clearly.


A clear set of testable CFRs also helps a decentralised set of teams 
          ensure that they look beyond their immediate, local delivery, and meet the 
          minimum requirements for playing coherently in the shared ecosystem.


However, technical governance refers to both these rather than encompassing 
          them - they contribute to the context within which it operates - and so I've
          not gone into any detail on them here. But what does governance include beyond 
          a means to ensure good technical decisions? Let's take a look.


## The Four Supporting Elements


### 1. A thinking and recording tool: Decision Records


The first supporting element is [Architectural 
        Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) or ADRs. These are lightweight documents, 
        frequently stored in source code repositories alongside the artefacts they 
        describe. Now, there are a variety of formats which various adopters have 
        chosen to champion, but the key elements which I insist on are as follows: 
        4


4: 
      There are actually two more, but we’ll get to those and discuss them 
      separately in detail in supporting elements 3 and 4.



| name | description |
| title | which includes a unique identifier, and the
            decision itself (e.g. “ADR001 - Use AKS for Kubernetes Pods”) |
| status | typically “Draft”, “Proposed”, “Adopted”, “Superseded” and
            “Retired” |
| decision | the decision that has been taken in a few
          sentences (frequently bold or italicized so it stands out) |
| context | the forces and current contextual
          circumstances which have necessitated this decision |
| options considered | each option considered, described briefly, with pros and cons.
            (Typically the option proposed / adopted comes first in this
            list) |
| consequences | the ramifications of this decision, both positive and
            negative |
| advice | this reflects the raw outputs from following the Advice
            Process. It is here that all advice given is recorded. This ought to
            include the name of the advice giver, and the date the advice was
            given. This can frequently take the forms of comments, and if these
            are provided directly by the advice-giver, then recording the
            meta-data is automatic. |



I’ve found in practice that having such a lightweight ADR template
        structure is not only a great way to record architectural decisions - it
        also helps teams learn to make architectural decisions. These key
        elements operate like a thinking checklist, and prompt the decide-ee
        regarding what they need to think about, and more importantly have
        conversations about.


What’s more, ADRs serve to reinforce the Advice Process by making it
        a requirement on ADR authors to capture and record all advice they get.
        I also encourage authors to engage with this advice directly in their
        ADR options section, whether they choose to follow it or not. It is one
        thing to seek advice and write it down. It is quite another to actively
        wrestle with it. The fruits get sweeter the more you engage.


It will come as no surprise to learn that consequently, a series of
        ADRs, and their surrounding conversations provide an excellent learning
        ground for people wanting to begin to take on the task of
        decision-taking; everything is out in the open, including the dissent
        and compromise-making. Less experienced practitioners of architecture
        can peruse the history of what went before them quickly and easily, see
        good (and quite likely less-good) examples, and see decisions being
        taken (and perhaps also being revoked when circumstances change / the
        team learned more). They are almost a thinking and decision lore for a
        set of software, written in the hand of those who contributed most to
        it.


While sadly I can’t share with you examples of these conversations
        I’ve had with my clients, there are some [
        great examples](https://web.archive.org/web/20210506014629/https://upmo.com/dev/decisions/0010-som-synthetic-monitoring.html) of ADRs out on the public internet, courtesy of 
        Thoughtworks-alumni Wisen Tanasa and his startup 
        [Upmo](https://upmo.com). I’d encourage you to take a look. 
        They come [blessed by none other than Michael 
        Nygard himself](https://twitter.com/mtnygard/status/1315647651854135297?lang=en).


### 2. A time and place for conversations: The Architecture Advisory Forum


The second supporting element in this alternative approach exists to
        make all the conversations supporting this advice-seeking easier: a
        weekly, hour-long Architecture Advisory Forum (“AAF”).


Fundamentally, this is a regular and recurring place and time for
        conversations. Your ideal attendees are delegates from each team as well
        as your key representatives from your Advice Process checklist. However,
        the invite should remain completely open to encourage transparency and
        openness. The timeliness and quality of the conversations which take
        place is a key indicator of success, but equally important is the
        breadth and diversity of views shared, and the same goes for the
        contributors. If architecture is being “done” here, and lessons shared
        and learned, then you’re winning.


The standing agenda typically begins as follows:

- team representatives quickly share new 
          [spikes](http://www.extremeprogramming.org/rules/spike.html) (giving early warning of 
          probable future decisions and allow the attendees to share existing 
          knowledge and experience)
- discussions about each new “proposed” decision (presented by those
          making the decision, captured ahead of time in the form of an
          ADR)
- a re-visit of other decision-statuses (we timebox these, both to
          limit the window for incoming advice, and also to allow us to revisit
          a decision which we made with imperfect information)
- a look at our collective four key metrics, our cloud spend trends, 
          and finally
- any other business (aka “AOB”)


A cursory glance might give the impression that an AAF is just a new
        title for a standard meeting. The one typically known as a “Tech
        Advisory Board”, “Architecture Decision Forum” or “Architecture Review
        Board”. There are however several key differences.


Firstly, the Advice Process reigns. Decisions taken to the AAF are
        still owned and made by the originators. The only thing other attendees
        can do is offer advice, or suggest additional people to seek advice
        from. Hence the name.


This brings us to the second key difference. Given the Advice Process
        qualifiers, the invitees to the AAF are those typically affected /
        possessing relevant expertise. This means those typically present
        include representatives from each feature team (and not just the lead;
        BAs/POs and QAs are frequently present), people from other programmes of
        work, UX, Product, Operations, and occasionally senior execs.


The combination of these two differences leads us to the third, and
        most important key difference: the conversations. The Advice Process is
        great, but it’s conversations can frequently be 1-1. When they take
        place in an AAF there is an audience, so many people can listen and
        everyone can learn. The amount of organisational, domain, legacy, and
        experiential information and architectural skill-deployment shared at
        these sessions is unlike anything I have ever seen, and despite being a
        potentially dry meeting, it is the most well-attended, and most broadly
        participated hour of our week. It is one of the most significant
        contributors to the quest for a learning organisation that there is.
        AAFs encourage disagreement, and celebrate failure / changes of decision
        based on lessons learned. This all combines to broaden and deepen the
        general understanding of an architecture, virtually guaranteeing it ends
        up in the running software.


### 3. A light to illuminate a unified goal: Team-sourced Architectural 
        Principles


Having architectural principles is not new, though sadly I rarely
        encounter serviceable ones. Always important, in a world of
        highly-autonomous-teams they become essential because they are the means
        by which an aligned delivery direction is achieved without the need for
        control.


So what makes a good architectural principle? Firstly, it must
        provide a criteria with which to evaluate our architectural decisions
        (which in practice means it must be specific, measurable, achievable,
        realistic and testable, aka “S.M.A.R.T”). Secondly, it must support the
        business’s strategic goals. Thirdly, it must articulate the consequences
        / implications it necessarily contains within it. Finally, taken
        together as a set, they should number neither too few to cover the key
        needs which architectural principles meet, nor too many that teams
        cannot remember them all.


There is a great deal I could write here about bad architectural
        principles but I’ll stick to the key aspects. Firstly, they are not
        practices. Practices are how you go about something, such as following
        TDD, or Trunk Based Delivery, or Pair Programming. This is not to say
        that practices are bad (indeed Dr Forsgren’s “Accelerate” is full of
        recommendations regarding for their set of circumstances)
        they’re just not architectural principles.


Watch out for slipping into the other end of the scale too - general
        principles. “Keep it simple” and “Don’t repeat yourself” are principles,
        but they’re not architectural. Nor are the various principles you’ll see
        around project planning, and software quality management. What we need
        are means to direct and evaluate our architectural practice and
        decisions. What we need is something which helps me pick between 
        [various approaches to implementing 
        micro-frontends](https://martinfowler.com/articles/micro-frontends.html#IntegrationApproaches), or helps me decide if it really makes sense to 
        [hand-roll my own OAuth 2.0 implementation](https://frontend.turing.edu/lessons/module-4/oauth/index.html#OSP), or
        guides me in evaluating self-hosted [Lucene](https://lucene.apache.org/) 
        on AWS vs [Amazon Elastic
        Search Service](https://aws.amazon.com/elasticsearch-service/).


Given all this, now let’s share a good principle, based around the
        [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) “Stream-Aligned Team” 
        organisation model:


**Title:** Value independence of teams most highly


**Subtitle:** Split solutions along team lines


**Rationale:** The strength of our approach to building and running our
        products relies fundamentally on the independence of our teams. The
        downsides to this are acknowledged, but the upsides are felt to outweigh
        it, especially when the difficulty of predicting future needs is taken
        into consideration.


**Implications:**

- Duplication of both function, and data, will inevitably arise. Rather 
          then fight this, we embrace it, acknowledging the need, in certain 
          circumstances, for noticeable eventual consistency and data replication
- The combined licencing, runtime and support costs of multiple 
          third-party solutions may be higher than the costs of a single, shared, 
          cross-product-team solution
- Solutions can be designed for the needs of the team which owns and runs
          them. They need not concern themselves the needs of other teams
- Both systems and the third-party services / solutions they are build on 
          will tend to be smaller, and more specific-task-focussed
- Teams who go their own way need to self-support any third-party services /
          solutions which they adopt independently


If you want to see more examples, please have a look at the
        publicly-available [John Lewis “Software Engineering 
        Principles”](https://engineering-principles.jlp.engineering/). 5


5: 
      Please note, at the time of writing, the John Lewis principles includes a 
      few items which fall outside our definition of an “architectural” 
      principle. I’m thinking of for example 
      [“Understandability”](https://engineering-principles.jlp.engineering/principles/practices/understandability/) and 
      [“Performance Importance”](https://engineering-principles.jlp.engineering/principles/practices/performance-importance/). This 
      doesn’t mean these aren’t bad goals, they just don’t meet our definition.


So far, so general. Nothing I have said so far in this section would
        be controversial in any approach to architecture. Why then am I
        stressing these points so much? Not only is the importance of
        architectural principles heightened in this decentralised approach, but
        also everyone concerned needs to know how to structure them and what
        good looks like because they will be sourced from, and maintained by,
        the teams themselves.


Our approach is, to a great extent, taken directly from the excellent
        [“The Art of Scalability”](http://theartofscalability.com/) by Abbot 
        and Fisher. While their book assumes a slightly more top-down, hierarchical 
        approach to architecture than presented here, the authors very much recognise 
        the impact of the human element on their topic. In fact, the edition I read had 
        been significantly re-written to give more weight to this perspective. 
        One key aspect of this is their argument 
        that for any architectural principle to be successful, teams which deliver
        against them need to feel a sense of ownership over it.


I’d encourage you to take a look at their book for a wealth of detail
        on how to source these from the collective. Suffice it to say, when
        presented with the business’s strategic goals, the “S.M.A.R.T.” criteria
        from earlier, and a broad set of invitees from across technology and
        beyond (yet again your AAF invitee list will prove invaluable here) you
        will rapidly and collectively arrive at 8-15 principles which will serve
        you well. 6 It’s well worth capturing the adoption 
        of a principle as an ADR. These will be very lightweight (don’t fall into 
        the trap of repeating the principle itself) offering a great opportunity to
        articulate why this principle is important.


6: 
      It’s worth pointing out that, while their [JADs](https://en.wikipedia.org/wiki/Joint_application_design) 
      and ARB’s in the following chapter don’t fit so well the approach we’re 
      following here, they do contain some great thoughts on when to revisit / 
      update the principles, thereby ensuring they keep fresh through constant 
      usage and re-evaluation.


There is one final point to make on the principles. Remember that
        this approach is aimed at supporting team autonomy, so one key role
        played by our principles is as a minimal viable set of understandings
        and agreements between everyone. This raises a key point, because one
        thing we ask teams to explicitly flag in their ADRs is not just the
        principles which apply, but also when their decision conflicts with one
        or more principles. This becomes a great point to engage the Advice
        Process and the power of the collective at the AAF to really get all the
        best minds and varied perspectives on the problem, and then record all
        this in the ADR. Yet again, the various elements support each other,
        amplifying their benefits, and helping us get to successful
        architectures. Remember, if, as a consequence of this a principle
        changes, call that out as a separate ADR that supersedes the
        original.


That’s architectural principles covered, which play the role of a
        guiding light for everyone to aim for, but how do we also take note of
        our surrounding landscape and climate? Architectural decisions are also
        frequently based on what everyone else is doing, who has which skills,
        and what the general trends in the tech industry are. Enter the fourth
        and final supporting element: your own Technology Radar.


### 4. A tech landscape and current climate sensing tool - Your own Tech Radar


Many people have heard of the ThoughtWorks 
        [Technology Radar](https://www.thoughtworks.com/radar) - an opinionated guide to 
        current trends (predicted, current, and receding) in software languages and 
        frameworks, tools, platforms, and techniques. It’s strengths lie in how it 
        visually represents both the current landscape and the movements of various 
        “blips” across it, allowing viewers to very rapidly see (for example) what 
        is up and coming in the world of front-end frameworks, what’s current flavour 
        of the month, and what’s beginning to fade.


Sadly, far fewer know about 
        the fact you can [build your own radar](https://www.thoughtworks.com/radar/byor). The “BYOR” 
        allows you, as a collective, to capture and map out your local version of the 
        technology trends you see across your organisation. It’s very configurable 
        too. In my most recent usage we kept the quadrants (Techniques, Tools, 
        Platforms and Languages & Frameworks) but changed the rings to reflect 
        the transit of technologies through our programme of work (they became 
        “experiment”, “adopt”, “hold” and finally “retire”).


As with the architectural principles, these radar blips need to be
        crowd-sourced in a workshop. The first run of this will capture
        everything you have now in your organisation - a baseline sweep or scan
        if you will. Prior to this you need to figure out how wide you will go
        (org-wide? just your project? Will you include disciplines such as Ops
        and UX? etc.) and what your quadrants will be. It’s also possible to add
        extra fields for data capture, but I typically try to keep it simple.
        The first time you do this it can take a fair time (we’ve taken four
        hours and more before) but this is because it is essential that you involve 
        all team members, not just architects, and the end result will give a great 
        overview of the landscape and prevailing climate, and brings many 
        discussions about where effort should be directed, and where it should be 
        reduced. And just as with the principles, give rise to a general aligning 
        of team understanding.


What about the usage of your radar? As with the principles, there is
        also a place in our ADRs for “Relevant Radar Blips”. This is where we
        flag both adherence to the existing landscape as reflected in the
        current radar, but also, and more importantly, potential changes to the
        existing radar which this decision will introduce. Perhaps it’s the
        spiking of a new framework, or a move from “experiment” to “adopt” for a
        specific practice.


Again, this is great grist for the AAF discussion forum, and great
        content to capture in the ADR itself. You can even go so far as linking
        specific types of blip appearances and movements to the need to submit
        ADRs, though in my experience this happens anyway without anyone having
        to push it explicitly. Remember, your goals here are the broadest
        engagement with your evolving architecture as possible, as well as a
        growing architectural mindset across all team members.


How about keeping your radar up to date? I've seen quarterly cadences 
        work, and half-yearly too. The key is to pay attention to how the radar 
        is being consumed (or not) at the AAF and elsewhere. That should give 
        you a good idea when it's worth investing in a refresh.


## How this typically works in practice


Given all this, how might you see it all working in practice? Let’s
      take a look…


When the need for an architectural decision first arises it will most
      likely be vague and possibly poorly understood. It’s therefore great to
      open up a new ADR template right away and start trying to fill it in.


First to be tackled is the “context” section. To attempt this we need
      to understand the “why” of our decision as well as surrounding forces
      which we need to balance. We’ll probably rapidly realise we need to do
      some research to be able to complete even this short section.


Early ports of call in this research ought to be the architectural
      principles and radar. The principles, you’ll recall, give us an idea of
      the direction of travel which our ideal solution will ideally manifest.
      Not all will be relevant, but some principles ought to help our
      decision-making. Recall that it’s an architectural principal’s primary
      goal to assist in the evaluation of multiple technical possibilities, and
      highlight the one which fits best.


Sometimes, the experience will be a little different. One alternative
      is that a relevant principle cannot help you pick between two options,
      then there is either very little difference to choose between, or
      potentially, your principle isn’t S.M.A.R.T. enough. This is a good reason
      to revisit the principle and re-define it.


The other alternative also may end, perhaps a little later, in a
      re-evaluated set of principles. These arise when in order to make your
      decision you feel inclined to contravene one or more principles. That’s
      ok; good decisions can go against the principles, but to do so you’ll need
      to state clearly why this course of action was the right step to take.
      Overriding a principle is a significant step because it means we are
      effectively diverging from the general direction of travel. Consequently,
      the decision, and resulting ADR must be clearly argued and strongly
      justified. It might also signal the time to revisit the principle in light
      of this development.


The radar in comparison is a lot more advisory in nature. It will give
      an idea of what, if anything, is the current de-facto standard in our
      problem space, what’s been done in the past, and what other teams might be
      experimenting with. Going a different way is a lot less likely to raise
      eyebrows, but it is again a definite reason to address the deviation in
      the ADR.


Given all this, we can start to come up with our key criteria to
      evaluate options against, as well as a list of alternatives. Perhaps we’ve
      realised we really need to do some homework and in which case we might
      spin off a timeboxed Spike to learn more about something. Our ADR thinking
      will help write super-clear acceptance criteria here. If we don’t need to
      do a Spike, we will think instead about seeking advice.


Having these inputs from the context (which will include, for example, 
      a technical strategy), applicable principles, radar blips, and key criteria 
      / alternatives will in turn help us think about who to speak to for advice. 
      In my experience it is helpful to engage in this when you are relatively 
      confident you understand the problem space / need, but before you become too 
      attached to a specific solution. When you go and seek advice, spend most 
      time and effort speaking to people who will disagree with you; those who you 
      know think along different lines and where you know you will have blind 
      spots. Not only this, challenge yourself. Consider “what’s bad about this 
      alternative? What are its shortcomings?” Spend the most time thinking about 
      the alternatives which challenge your decision most directly and 
      fundamentally.


Before you have the discussion, it helps to have the ADR ready in a
      rough form, and share it with them in advance. This will give them
      thinking time. Then when you do meet, go through every element of the ADR
      template. Have you missed something from the context? From the principles
      / blips? From the evaluation criteria? Solicit and capture their advice on
      all these things. More importantly, ask them why they are making these
      suggestions. It is the answers to these questions that the keys to
      learning to make better architectural decisions lie. Your advisors will
      help you understand how they see problems, what they’ve encountered that
      was similar in the past, and even entire aspects which you don’t even
      think about. 7


7: 
      Classic examples include people who’ve had to find, hire and retain 
      developers and people who’ve been the “support” end of a decision thinking 
      differently about new technologies.


What about the AAF? Isn’t that the place to gather advice? Yes, and
      everything I’ve shared above should guide you wherever you have the
      conversation, but for the first few decisions a team or individual takes
      it really helps to have these in a more targeted way with the key
      advisors. The ADR you present before the AAF will then be really solid and
      focused before it is shared widely, meaning that the resulting AAF
      conversations will be richer and more focused. Sometimes a quick
      conversation in the AAF will lead to a subsequent, more in depth, 1-1
      conversation.


Remember, once you have advice, wherever it came from, you must roll it
      into your ADR. You need not take the advice given, but you have to record
      it. An excellent practice here is to prioritise things in your writing
      which people would find non-intuitive or surprising. If you disagree with
      key advice, state how and why. If you are doing something new, make it
      clear why the current way doesn’t work for you. Remember to use the
      principles. Sometimes they will support your decision. Make it clear how.
      Sometimes you will have to contravent them. Make it clear why. Your goal
      is to make the reader understand why you took the decision you took. If
      you meet this goal, then you will not just have a solid decision, you’ll
      most likely have learned a great deal in the process. 
      8


8: 
      There are some great blog posts which meet this criteria that are in many 
      ways just extended ADRs. [“Why not Rust?”](https://matklad.github.io/2020/09/20/why-not-rust.html) 
      and [“No, we don’t use Kubernetes”](https://ably.com/blog/no-we-dont-use-kubernetes) are 
      excellent examples, and worth reading if you want to see some really great 
      decision-taking (and cargo-cult-avoiding) in progress.


Before I close this section, remember, all decisions are point-in-time,
      and no-one can ever foresee every eventuality, but you want to be able to
      go back later and still feel good about a decision, given what you knew /
      understood at the time. In this, the context and criteria you capture are
      key. This re-visiting of decisions is another great learning tool. With
      the benefit of hindsight you can now ask questions such as: “did we
      understand the context well enough?” and “were we honest enough with
      ourselves about what we knew and what we didn’t?”


## How to fail


So that’s the extent of our alternative, decentralised, anarchistic
      approach to architecture, and an idea of how it typically all fits
      together. But before we conclude, we ought to address one final aspect -
      the key ways in which you can fail. Let’s enumerate them.


The majority of failures you will see will actually be good ones - mini
      failures as decisions are taken by those who are less experienced. These
      are good because the process facilitates quick decisions, by those who
      need them, and more importantly, it facilitates transparency and rapid
      identification of failures (as those who took the decision will be aware
      of the issues as they code it) and a safe means to re-visit, and share the
      learnings. Embrace these, calling them out specifically and celebrating
      them in the AAF. This is a key aspect of building a learning culture.


To learn most effectively you need to feel safe, and when learning
      collectively everyone benefits from the broadest, most diverse range of
      inputs contributing to discussions. Remember, in this approach, we are
      explicitly not looking for consensus, but we are looking for a broad range
      of inputs and voices. It is here that the next failure mode lies, and it
      is far more insidious and damaging than the first. This second failure
      mode arises when you, in your job as a conversation-starter and
      space-holder, fail to include all who ought to be contributing and
      deciding and learning. For a great part early adoption stages of this
      style of architecture can feel like great successes. “It’s working! More
      and more people are taking decisions, writing them up in ADRs, giving
      advice and discussing them in the AAF! I’ve never seen such engagement
      with principles before!”. Only later, on reflection, will you realise the
      gains could have been far greater. It is precisely when this first flush
      of satisfaction strikes that you must be most on your guard. Are you
      really observing mass participation and learning, or is it a core group of
      usual suspects? You mitigate this problem actively. Watch out for who
      contributes. Amplify voices and ensure others listen to the quieter
      contributors. Make sure influence is balanced and not based on reputation,
      tenure or place in the hierarchy. Actively encourage many viewpoints and
      highlight the value it brings so that it becomes self-sustaining.


The third failure mode is an early warning that you are encountering
      the preceding failure mode, however, this one lives more in the grey area
      between desired and unwelcome. As you proceed along this journey you will
      uncover off-the-grid decisions. Decisions which never came up at the AAF,
      and which never made it into an ADR. There are two ways to approach them.
      The first, correct way, is to treat the discovery as what you hope it is -
      an honest mistake, and an opportunity to learn and teach others. Perhaps
      the decide-ees weren’t even aware of the fact it was a key decision they
      were taking. Perhaps they were under pressure from elsewhere. Perhaps they
      thought it wasn’t as significant as it turned out to be. Perhaps they felt
      they would be shouted down in the AAF. Whatever the reason, treat it as a
      way for both them, and you, to learn. To improve the process. The other,
      wrong way to treat these, is to fall back to old ways, and take back
      control. Which takes us nicely to the failure mode which completely
      destroys this approach and all that it promises.


It’s easy to slip into this fourth and most dangerous failure mode, and
      so it needs constant vigilance on your part. The only thing which needs to
      happen to trigger this is for “capital-A” architects such as yourself to
      fail to trust people; it is to not practice what you preach; it is to not
      clear enough space for the mini failures and consequent learning
      opportunities just mentioned; it is to continue to perform “shadow
      architecture” behind the scenes to make sure things still go how you think
      they ought to, despite all the signals from elsewhere. The sole benefit of
      this failure mode is that it becomes evident very rapidly as all the
      benefits I’ve listed above fail to materialize.


If you’re wondering if it’s this key failure mode which makes this
      approach to architecture hard to pull off you’d be right. I have been
      lucky in the past. Colleagues have called me out when I’ve made decisions
      for others, and I’ve caught myself getting frustrated that folks don’t
      know what I know. But then I realise I’m failing in my real task as a
      practitioner of architecture - I’m failing to get the right conversations
      happening, with the right people, at the right time. Remember that
      (perhaps even task others with calling you out when you fail to stick to
      the process) and you’ll be surprised how easy (and satisfying) it is to
      succeed.


## The five elements again, and possible further steps


Given we now have both the good and the (potentially) bad, as well as a
      collection of failure modes to look out for, let’s conclude. We recall we
      have the five elements of our alternative approach to architecture:


One core element: Advice Process


Four supporting elements:

- Architecture Advisory Forum
- Lightweight ADRs
- Team-sourced Principles
- Your own Tech Radar


Hopefully I’ve made it clear that while none of the elements may be new
      to you (aside from perhaps the Advice Process) there is something very
      different. This difference lies in the interplay/mutual reinforcement
      between all of these against a backdrop of conversations, learning and
      safety. What is hopefully enticing is the fact that, in my experience at
      least, this is far more likely to provide successfully deployed
      architectures, now, and into the future. It is my go-to for scaling
      myself, and making sure that the teams I work with deliver on the promises
      we have made to our users, which is, after all, the goal.


## Afterword: What next?


Of course, while I’ve tried to keep this article focused, it’s possible
      to go further. I’ve seen teams working in this way naturally starting to
      pave their own roads - self-serving their own delivery platform before a
      (Delivery) Platform Team comes into existence. (See my colleague Evan
      Bottcher’s excellent [“What I talk about when 
      I talk about Platforms”](https://martinfowler.com/articles/talk-about-platforms.html) and Skelton and Pais’ 
      [Team Topologies](https://martinfowler.com/bliki/TeamTopologies.html) for more detail on this.)


I’ve also seen teams put in place their own 
      [Architectural Fitness Functions](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) (and not 
      just around [run cost](https://www.thoughtworks.com/radar/techniques/run-cost-as-architecture-fitness-function)) so that they know when 
      the collective architecture strays outside its intended bounds.


The biggest lesson I’ve learned is that, once you empower people,
      giving them an environment in which to succeed, and recognise their
      successes, they will rapidly, and as a collective, start thinking about
      things which haven’t even crossed your mind. That’s the real benefit of
      this kind of approach: access to the collective intelligence of the many,
      over reliance on the much more restricted intelligence of the few.


---
