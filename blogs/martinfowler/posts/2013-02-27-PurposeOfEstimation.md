---
title: "Purpose Of Estimation"
description: "My first encounter with agile software development was working   with Kent Beck at thedawn of Extreme Programming. One of the things   that impressed me about that project was the way we went about   "
date: 2013-02-27T00:00:00
tags: ["metrics", "project planning", "estimation"]
url: https://martinfowler.com/bliki/PurposeOfEstimation.html
slug: PurposeOfEstimation
word_count: 1912
---


My first encounter with agile software development was working
  with Kent Beck at the [dawn of Extreme Programming](https://martinfowler.com/bliki/C3.html). One of the things
  that impressed me about that project was the way we went about
  planning. This included an approach to estimating which was both
  lightweight yet more effective than what I'd seen before. Over a
  decade has now passed, and now there is an argument amongst
  experienced agilsts about whether estimation is worth doing at all,
  or indeed is actively harmful 1. I think that to answer this question
  we have to look to what purpose the estimates will be used for.


1: 
      A recent read is [Estimation
      is Evil](http://pragprog.com/magazines/2013-02/estimation-is-evil) an excellent discussion by Ron Jeffries of the
      problems that estimates can cause.


A common scenario runs like this:

- Developers are asked for (or given) estimates for upcoming work.
- These tasks and estimates are turned into release plans
    tracked with burn-down charts
- Time and effort goes into monitoring progress against these
    plans. Everyone is upset when actuals end up being more
    than estimates. In effort to
    increase pace with the estimates, developers are told to sacrifice
    quality, [which only makes things worse](https://martinfowler.com/bliki/DesignStaminaHypothesis.html).


In this narrative, effort put into estimates is, at best, waste
   - since âan estimate is a guess in a clean shirtâ 2. Usually estimates end up being actively harmful as
   they encourage [FeatureDevotion](https://martinfowler.com/bliki/FeatureDevotion.html), a nasty condition where
   people start valuing ticking off features more than tracking the real
   outcome of the project.3


2: 
      I got this analogy from Ron Jeffries, although I don't have a
      written reference for it.


3: 
      This situation is an excellent example of an [inappropriate use of metrics](https://martinfowler.com/articles/useOfMetrics.html).


Estimates also set expectations, and since estimates are usually
   too low, they set unrealistic expectations. 4 Any increase in time or
   reduction in features is then seen as a loss. Due to [loss-aversion](http://en.wikipedia.org/wiki/Loss_aversion),
   these losses have a magnified effect. 5


4:


I particularly liked a comment on this by my colleague Angela
      Ferguson âthe way that estimates set expectations is up to us -
      *it is poor project management (whether by project managers or
      other team members)* that results in a client who thinks
      estimates are fixed, or that raw estimates = actual
      effort/durationâ


âI, in fact, try to practice delivery bad news on a weekly
      basis with my key client, even when things are travelling as
      expected ... 'so we're looking quite well on track now, but if
      we had discovered something that took longer than expected, or a
      requirement had blown up to be larger than expected, or we found
      something new and very important, what do you think the best
      course of action would be?' And then you explore the options -
      cut stories, add time, add capacity, etc. This means that when
      the expected unexpected thing happens (because we know it will
      happen), the conversation doesn't seem new and scary to the
      client.â


5: 
      Very roughly people feel twice as much pain for a loss as
      pleasure for a gain.


Faced with situations like this, it's easy to see how people
   turn their angry glares towards estimation. This leads to an
   increasing notion that anyone indulging in estimating is Not a
   True Agilist. Critics of agile say this means
   that agile development is about developers going off and doing vague
   stuff with promises that it'll be done when its done and you'll like it.


I don't share this view of estimation as an inherently evil
   activity. If I'm asked if estimation is a Bad Thing my answer is
   the standard consultants' answer of âit dependsâ. Whenever someone
   answers âit dependsâ the follow-up question is âupon whatâ. To
   answer that we have to ask why we are doing estimation - as I like
   to say âif it's worth doing well, it's worth asking why on earth you're doing
   it at allâ.


For me, **estimation is valuable when it helps you make
   a significant decision**.


My first example of an estimation-informed decision is allocation
   of resources. Organizations have a mostly fixed amount of money and
   people, and usually there are too many worthwhile things to do. So
   people are faced with decisions: do we do A or B? Faced with such a
   decision it's useful to know how much effort (and cost) each will
   involve. To make sensible decisions about what to do, you need to
   have a feel for both the cost and the benefits.


Another example is to help with coordination. The blue team
   wants to release a new feature to their web site, but cannot do so
   until the green team builds a new service to give them crucial
   data. If the green team estimates they will be done in two months
   and the blue team estimates that it will take them a month to build
   the feature, then the blue team knows it's not worthwhile to start
   today. They can spend at least a month working on some other
   feature that can be released earlier.


So whenever you're thinking of asking for an estimate, you
   should always clarify what decision that estimate is informing. If
   you can't find one, or the decision isn't very significant, then
   that's a signal that an estimate is wasteful. When you do find a
   decision then knowing it focuses the estimate because the decision
   provides context. It should also clarify the desired precision and
   accuracy.


Understanding the decision may also lead you to alternative
   actions that may not involve an estimate. Maybe task A is so much
   more important than B that you don't need an estimate to put all
   your available energies into doing it first. Perhaps there is a way
   for blue team members to work with the green team to get the
   service built more quickly.


Similarly, tracking against a plan should also be driven by how
   it informs decision making. My usual comment here is that a plan
   acts as a baseline to help assess changes - if we want to add a new
   feature, how do we fit it into the [FivePoundBag](https://martinfowler.com/bliki/FivePoundBag.html)?
   Estimates can help us understand these trade-offs and thus decide
   how to respond to change. On a larger scale re-estimating a whole
   release can help us understand if the project as a whole is still
   the best use of our energy. A few years ago we had a year-long project
   that was cancelled after a re-estimate a couple of months in. We
   saw that as a success because the re-estimate suggested the project
   would take much longer than we had initially expected - early
   cancellation allowed the client to move resources to a better target.


But remember with tracking against plans that estimates have a
   limited shelf life. I once remember a gnarly project manager say
   that plans and estmates were like a lettuce, good for a couple of
   days, rather wilty after a week, and unrecognizable after a couple
   of months.


Many teams find that estimation provides a useful forcing
   function to get team members to talk to each other. Estimation
   meetings can help get better understanding of various ways to
   implement upcoming stories, future architectural directions, and
   design problems in the code base. In this case any output
   estimation numbers may be unimportant. There are many ways such
   conversations can happen, but estimation discussions can be
   introduced if these kinds of conversations aren't happening. 6
   Conversely if you're thinking of stopping estimation, you need to
   ensure that any useful conversation during estimation still
   continues elsewhere.


6: 
      If you do this an approach like [ThrownEstimates](https://martinfowler.com/bliki/ThrownEstimate.html) can
      help the discussion move at a good pace.


Go to any conference with agile leanings and you'll hear talks
   of teams that work effectively without estimation. Often this works
   because they, and their customers, understand that making estimates
   isn't going to affect significant decisions. An example is a small
   team working closely with business. If the broader business is
   happy with allocating some people to that business unit, then work
   can be carried out in priority order; often this is helped by the
   team breaking down work into small enough units. 7 A team's level in the [agile fluency
   model](https://martinfowler.com/articles/agileFluency.html) plays a big role here. As teams progress they first
   struggle with estimation, then can get quite good at it, and then
   reach a point where they often don't need it. 8


7: 
      Of course breaking work down into small units requires some
      implicit estimation, but that's really a different animal to
      the more common explicit estimation activity.


8: 
      James Shore has a recent blog post that [details his observations](http://www.jamesshore.com/Blog/Estimation-and-Fluency.html)
      about how fluency influences estimation practice. I think a
      similar analysis of practices at various stages of fluency could
      be very useful.


Estimation is neither good or bad. If you can work effectively
   without estimation, then go ahead and do without it. If you think
   you need some estimates, then make sure you understand their role
   in decision making. If they are going to affect significant
   decisions then go ahead and make the best estimates you can. Above
   all be wary of anyone who tells you they are always needed, or
   never needed. Any arguments about use of estimation always defer to
   the agile principle that you should decide what are the right techniques for
   your particular context.


## Acknowledgements

I repeat myself again in thanking varous ThoughtWorkers on internal
  lists for their comments. In particuarly I'd like to call out Angela
  Ferguson, Dave Pattinson, and Pat Kua. I should also thank James Shore for responding
  so rapidly and well for my question about the links to the fluency model.

## Notes


1: 
      A recent read is [Estimation
      is Evil](http://pragprog.com/magazines/2013-02/estimation-is-evil) an excellent discussion by Ron Jeffries of the
      problems that estimates can cause.


2: 
      I got this analogy from Ron Jeffries, although I don't have a
      written reference for it.


3: 
      This situation is an excellent example of an [inappropriate use of metrics](https://martinfowler.com/articles/useOfMetrics.html).


### 4: Estimates and expectations


I particularly liked a comment on this by my colleague Angela
      Ferguson âthe way that estimates set expectations is up to us -
      *it is poor project management (whether by project managers or
      other team members)* that results in a client who thinks
      estimates are fixed, or that raw estimates = actual
      effort/durationâ


âI, in fact, try to practice delivery bad news on a weekly
      basis with my key client, even when things are travelling as
      expected ... 'so we're looking quite well on track now, but if
      we had discovered something that took longer than expected, or a
      requirement had blown up to be larger than expected, or we found
      something new and very important, what do you think the best
      course of action would be?' And then you explore the options -
      cut stories, add time, add capacity, etc. This means that when
      the expected unexpected thing happens (because we know it will
      happen), the conversation doesn't seem new and scary to the
      client.â


5: 
      Very roughly people feel twice as much pain for a loss as
      pleasure for a gain.


6: 
      If you do this an approach like [ThrownEstimates](https://martinfowler.com/bliki/ThrownEstimate.html) can
      help the discussion move at a good pace.


7: 
      Of course breaking work down into small units requires some
      implicit estimation, but that's really a different animal to
      the more common explicit estimation activity.


8: 
      James Shore has a recent blog post that [details his observations](http://www.jamesshore.com/Blog/Estimation-and-Fluency.html)
      about how fluency influences estimation practice. I think a
      similar analysis of practices at various stages of fluency could
      be very useful.
