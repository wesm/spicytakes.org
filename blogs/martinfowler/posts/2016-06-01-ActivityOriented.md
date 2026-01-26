---
title: "Activity Oriented"
description: "Any significant software development effort requires several different activities to   occur: analysis, user experience design, development, testing, etc. Activity-oriented   teams organize around the"
date: 2016-06-01T00:00:00
tags: ["bad things", "team organization"]
url: https://martinfowler.com/bliki/ActivityOriented.html
slug: ActivityOriented
word_count: 756
---


Any significant software development effort requires several different activities to
  occur: analysis, user experience design, development, testing, etc. Activity-oriented
  teams organize around these activities, so that you have dedicated teams for
  user-experience design, development, testing etc. Activity-orientation promises many
  benefits, but software development is usually better done with
  [OutcomeOriented](https://martinfowler.com/bliki/OutcomeOriented.html) teams.


![](images/activityOriented/activity-oriented.png)


Traditionally, big businesses with large IT departments (Enterprise IT) have tended
  to execute IT development projects with a bunch of activity-oriented teams drawn from a
  matrix IT organization (functional organization). The solid-lined arms of the 
  matrix (headed by a VP of development, testing and so on) are usually along activity 
  boundaries and they loan out “resources” to dotted-lined project or program organizations. 
  Common justifications for doing so include:

- It helps standardization of conventions and techniques in development if all
    developers report into a single organization (arm of the matrix). Same for testing
    etc.
- It helps the cause of mentoring, training and nurturing the competency in general
    if all developers have long-lived development/engineering managers. Same for testing
    etc.
- It helps maximize utilization of talent (and thereby improve cost-efficiency) by
    staffing projects from pools of supposedly fungible developers, testers etc.


However, activity-oriented teams are prone to optimize for their own activity and not
  for the bigger picture of delivering useful software. This is a consequence of what they
  are held responsible for and how they are measured. It is common for a team of only
  developers to only be measured by their [velocity](https://martinfowler.com/bliki/XpVelocity.html). If they are only tasked with
  delivering scope, they will not think about whether it is going to solve the problems it
  was meant to. Even if they do so, they may be discouraged by the product management team
  - another activity-oriented team that is only responsible determining the spec.


Organizing by activity gets in the way of lowering batch size of work that is
  handed-off between teams. A separate team of testers won’t accept one story at a time
  from a team of developers. They’d rather test a release worth of stories or at least all
  stories in a feature at a time. This lengthens the feedback loop, increases end-to-end
  cycle time and hurts overall responsiveness.


High speed IT calls for motivated teams. Autonomy is a key motivator for teams.
  However, activity oriented organization can only be granted so much autonomy because
  they tend to use it for optimizing their sphere of activity.


A variation of activity-oriented organization are super-specialized teams that may result
  in the following ways:

- Tool or skill centric teams: e.g. a WebSphere Portal Server team or a BizTalk
    team
- Architectural Layer teams: e.g. a presentation layer team, middleware team, data
    layer team.


They are problematic because they have a narrow focus and they tend to optimize for
  team performance rather than the big picture. For sure, some tools may need specialists
  but that is no reason to isolate them in a separate team. **Specialization isn’t the
  problem; organizing along lines of specialization is.**


## What works better


Software development is an iterative design process. In order to achieve true
    iteration and realize the value of fast feedback, its activities need to be performed
    with a single team (having a common reporting line) as far as possible. Many internet
    business and independent software vendors (ISVs) already operate in this way.


Sriram's book goes into more detail on how to build an effective IT organization
      using agile approaches.


Activity-oriented organization may be attractive from the perspective of maximizing
    utilization but it comes in the way of maximizing value-addition and end-to-end
    responsiveness. In today’s business climate, market responsiveness (time-efficiency)
    is more important than cost-efficiency especially when it comes to capital expenditure
    items such as software development. Besides, solid-line reporting should be aligned to
    the most important goals which are responsiveness and value-addition.


In order to effectively nurture competencies in the absence of an aligned reporting
  structure, set up communities of practice along with expert community leads who have the
  ability to mentor and the budget to organize community events, buy books and arrange for
  training. These communities also help with standardizing conventions and techniques
  without going overboard with standardization. As for having a stable reporting manager,
  it is only an issue in project-centric IT. A [BusinessCapabilityCentric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) setup allows
  for stable reporting managers.


## Acknowledgements

Thanks to Bill Codding, David Wang (Wang Wei), James Lewis, Kief Morris, Patrick Kua, Patrick Sarnacke, Steven Lowe and Venkatesh Ponniah for their comments. Special thanks to Martin Fowler for his guidance with the content, help with publishing and for the nice illustrations.