---
title: "What if we rotate pairs every day?"
description: "Benefits of pair programming are widely accepted but advice around pair rotation     remains controversial. When and how frequently should teammates     rotate pairs? And… What if we rotate pairs ever"
date: 2024-03-06T00:00:00
tags: ["collaboration"]
url: https://martinfowler.com/articles/rotate-pairs-experiment.html
slug: rotate-pairs-experiment
word_count: 2499
---


The majority of developers work solo. Tasks are commonly assigned to
    single individuals in a practice that is called “solo coding”. Developers
    that practice solo coding are often isolated in silos that prevent knowledge
    sharing across the team. These silos also make it difficult for team members
    to bond and create personal relationships, especially in a remote working
    environment. Onboarding of new team members is complicated and the
    establishment of quality gates like code reviews result in a bottleneck for
    delivery efficiency. In addition, binding the work to individual team
    members also creates a risk for whenever this person leaves the team (eg.
    vacations or sick leave). Finally, individuals eventually become owners of
    regions of the system and the person to go to for feature-specific
    knowledge.


Pair programming is a viable alternative to solo coding. 
    [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html) explores its benefits and challenges.
    When developing in pairs, people can work closely together with the goal to
    constantly share knowledge and information. This leads to better refinement
    of stories because everyone will have the necessary context to contribute.
    Also, there is no need for specific code review processes since all code is
    being reviewed ​​on the fly. Pairing creates more opportunities for people to
    know each other and develop personal bonds thus increasing team’s cohesion.
    Pairing processes should be accompanied by a periodic pair rotation ceremony
    so that pair switching can happen. This enables people to experience working
    with everyone in the team. After this ceremony developers should share the
    current tasks’ context and progress with the new pair so that the delivery
    flow can continue.


The frequency of pair rotations can vary between teams. Even though
    frequent pair rotations are preferred in order to maximize the benefits of
    pairing, some teams have reported that rotating pairs frequently creates
    friction. There is a perception that rotating pairs every day, or every
    other day, is more costly and more difficult than rotating once a week. On
    the other end of the spectrum, there are also teams which rotate pairs once
    a month. This means an individual would take at least 5 months to pair with
    other 5 people in the team at least once, assuming no repeated pairs during
    this period. Another routine is when pairs rotate only when they finish a
    task, which makes the frequency indeterminate. It is also not practical to
    rotate pairs on task completion since it is unlikely that other pairs
    finish at the same time.


We started noticing that teams with infrequent pair rotations tend to
    present similar symptoms seen in teams that do solo coding. Long-lived pairs
    start to become “partners in crime”. Context sharing gets harder the longer it takes for
    pair switching to happen: Developers need to share all the context from the
    previous month with a new pair in the context of monthly rotations. We had
    evidence that our pair switching practice wasn't yielding the desired
    outcomes, so we decided to run an experiment with the goal to improve team
    performance through pairing best practices.


## Our Experiment


We decided to challenge teams that practiced infrequent pair rotations
      to radically increase this frequency as part of an experiment. What if for
      two weeks we rotated pairs every day? What were the difficulties found
      during this time, and what can we do to address them? Did we reap the
      benefits of pairing during this time? Going forward, does the team want to
      keep rotating pairs every day or go back to the previous frequency?


We developed an exercise designed to help a team explore frequent pair
      rotation and make critical analysis of its impact. The exercise begins
      with a one hour, facilitated whiteboarding session, during which the team
      members write up and discuss their thoughts on the following three
      questions:

- Why is pairing valuable?
- What makes pairing difficult?
- What makes pairing easy?


These questions are presented in order. The team has three minutes to
      post answers for each question on the board and seven minutes to discuss
      what they have shared.


![](rotate-pairs-experiment/mural-board.png)


Figure 2: 
        Mural board displaying team's feedback during the pair rotation experiment


For the following days of the exercise the team continues working on
      their backlog while rotating pairs every day. For any task in progress one
      member of the pair stays with the task as “anchor” while the other 
      rotates onto another task. “Anchors” of a task rotate every
      other day, ensuring that no team member will work on a single task for
      more than two days consecutively.


The team meets every morning for 30 minutes on a whiteboard session
      with the following three questions:

- What makes pairing difficult?
- What makes pairing easy?
- What practices should we try today, to make our pairing easier and more
        effective?


These questions are presented in order, each with three minutes to post
      ideas on the board and five minutes to discuss. When this is finished, the
      team identifies anchors for each task in progress and facilitates the
      assignment of new pairs.


We facilitated this daily retrospective using the same board every day,
      with a unique color of sticky for each day. This allowed the team members
      to see the points raised in each area on each day, resulting in a
      visualization of the team’s learning and critical thinking throughout the
      week.


On the last day of the exercise we facilitated the final whiteboard
      session, and then asked the team to decide on a pair rotation frequency to
      continue. We then encouraged the team to continue to revisit their pair
      rotation frequency in future team retrospectives.


## Results of our Experiment


During 2022 - 2023 we engaged three separate teams to try this
      experiment for one week each. Each of these teams were fully distributed,
      working together online but never in person. Two of these
      teams were collocated between the US and Brazil.


Each team raised similar concerns at the start of the experiment. In
      the first section below we share some of those concerns and describe how
      the teams’ position evolved over the course of the experiment. The second
      section presents some feedback that displays the realized benefits of
      pairing and frequent pair rotations.


All teams that participated in our experiment used systems like Jira or
      Trello to document and track work items, and all used the term “card” to
      describe a record in that system. The following feedback and results use
      the word âcardâ in this sense.


### What makes pairing hard and how the perceptions changed


#### “Lack of empathy, alignment and communication makes pairing difficult”


Frequent pair rotation can be a powerful tool in building stronger
          team dynamics. Initially, a lack of empathy and alignment can make
          pairing challenging, especially when team members are unfamiliar with
          each other's working patterns, pace, and areas of expertise. However,
          by switching pairs frequently, team members have the opportunity to
          get to know one another better, and quickly. This familiarity makes it
          easier to empathize and align with each other, ultimately fostering
          stronger bonds within the team. Moreover, the practice of frequent
          pair rotation encourages a culture of feedback. We suggested that team members
          intentionally share feedback during short sessions at the end of their
          pairing sessions, contributing to continuous improvement and better
          collaboration.


#### “There are a lot of interruptions to pairing time”


Teams reported challenges in pairing due to frequent interruptions
          caused by a lack of long periods of uninterrupted working time. To
          address this issue, the teams established core working hours in the
          afternoon during which interruptions are minimized. As a result,
          meetings got shifted to the morning or the end of the day.
          Additionally, pairs within the team utilized the Pomodoro Technique or
          other explicit timeboxing methodology to maximize their efficiency and
          productivity during their limited working time.


#### “Switching pairs everyday makes us slower”


There is a notion that increasing the frequency of rotations
          results in a decline in delivery performance, as perceived by the
          product team. They tend to believe that more rotation leads to reduced
          efficiency and slower output.


There also exists a developer perception that frequent rotations
          introduce additional overhead, consequently slowing down the team.
          This is attributed to the need to consistently share the evolving
          context of ongoing work, which is perceived as a time-consuming
          process.


However, proponents of more frequent rotations argue that sharing
          context becomes more efficient as the frequency increases. This is
          attributed to the fact that there is typically less contextual
          information to communicate if pair switching is done frequently.
          Moreover, the efficiency of sharing context is further enhanced when
          every team member possesses a more comprehensive understanding of
          ongoing tasks. In addition, frequent pair switches creates an
          opportunity for team members to establish processes to facilitate
          context sharing.


The practice of frequent rotation becomes more manageable and
          streamlined over time. As the team becomes accustomed to this
          approach, the initial challenges associated with frequent rotation
          diminish, making the process progressively easier and more
          effective.


### The experienced benefits of frequent pair rotation


#### “Context sharing is easy and quick when you do it more often”


One concern that we heard from all three teams was that swapping
          pair members on work in progress would lead to a problem of sharing
          context with the new pair member. In fact, for each team this seemed
          to be the strongest motivation for long-lived pairs.


In each team’s board we found that this concern would be raised
          in the first couple of days. Team members would suggest common ways
          to make context sharing easier, and by the end of the experiment it
          was no longer a concern. A practice that emerged in each team was to
          have pairs end their day by adding a note to the card itself,
          briefly capturing the work and decisions completed that day. They
          might also add or remove items from a to-do list also maintained in
          the card. These simple practices helped the card itself to carry the
          context of the work in progress, rather than having that context
          reside with specific team members.


We found that each team discovered new practices related to the
          cards. In our daily discussions the team members would ask for more
          context to be held in the card, smaller cards, and ongoing comments
          in the cards.


#### “Information is flowing through the team”


This is one of the more exciting and insightful comments we
          heard. Teams discovered that, in practice, it did not take very long
          for an anchor to share context with a new pair at the start of a
          coding session. There was not a lot of new context to share. Also,
          teams found it was easier to understand any card after working on
          many other cards of the team’s backlog. Frequent pair rotations
          accelerate this experience gain as team members are able to work on
          a wider variety of tasks every week.


#### “Knowledge silos are impossible to maintain”


Each team included members of different experience levels and
          areas of expertise. The teams initially thought of this diversity as
          a challenge for frequent pair rotations. Prior to the experiment,
          each team was organizing pairs and the cards assigned to pairs with
          consideration of who is a junior or senior team member, who is a
          front-end, back-end or devops specialist, who has prior experience
          working in a particular area of the codebase, and so on. Maintaining
          this complex matrix made it difficult to switch pairs frequently,
          and reinforced knowledge silos in the team.


It was impossible to maintain these rules with the daily pair
          rotations of the experiment. With pairs rotating every day, team
          members were forced to work in unfamiliar areas of the codebase. In
          addition, there was far less risk for any team member working in an
          unfamiliar area since that member would only stay on a card for a
          day or two before passing it to someone else.


Our teams found that frequent pair rotations leveled the
          experience impact people have on cards. Longer-term team members
          could remove blockers from newer members and share knowledge that
          help accelerate their growth and learning curve of the codebase and
          development tools.


A few months after the experiment, one team gave us some
          interesting feedback: They found that when a problem came up in
          production, they didn't need to depend on just one person to look
          into and fix it. The team could assign anyone to troubleshoot the
          issue. In addition, another feedback mentioned an incoming pair
          rotation brought new context that changed implementation direction
          and helped resolve a problem in the early stages of the feature’s
          development, thus saving the team lots of time and rework. These
          highlight the benefits of having knowledge spread among the
          team.


#### “The work is moving among the team members”


Team members found that everyone developed context related to all
          the cards in progress, even before working on each card. This
          increased the effectiveness of the daily standup sessions: Team
          members would share insights, identify risks in advance and help
          each other in removing blockers. This is only possible when all
          developers have enough context and ownership of all cards in play.
          No single individual owns any piece of work, and everyone in the
          team is responsible for the progress of the tasks as a whole.


## Conclusions


Even though the experiment involved daily pair rotations, the three
      participating teams did not opt for continuing at this frequency in the
      end. One team settled on 3 day rotations while the other two teams settled
      on 2 day rotations. We noticed that frequent rotations revealed
      bottlenecks and friction points in the development process of the teams.
      Opting for rotating every 3 days instead of everyday relates to working
      around these blockers.


It is common that on any day the team members have only a few hours,
      often fragmented throughout the day, to pair. Team members felt that they
      needed more than one day to achieve a meaningful pairing experience. In
      turn, this can also indicate high fragmentation of development time
      throughout the days. This was one of the reasons teams opted for less
      frequency than practiced in the experiment.


Many of the perceived challenges during the experiment are not
      absolutes, but rather decrease when addressed head-on (and conversely
      increase if avoided). The experiment provided a daily opportunity for
      participants to reflect on pairing challenges and discuss alternatives to
      solve them as a team. The time and effort employed in the experiment
      ceremonies had a high return of investment.


In general, running the experiment dramatically improved the frequency
      of pair rotations in these teams. One of the teams moved from rotating
      once a month to rotating every 3 days. This frequency increase was a
      result of the teams acknowledging the benefits of short-lived pairs such
      as better knowledge sharing and team building. During the experiments,
      team members also reported participating in the experiment made them learn
      more about pairing best practices. In addition, running pairing
      retrospectives and feedback exchange sessions promoted the feedback
      culture in the teams.


---
