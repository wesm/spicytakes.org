---
title: "Refinement Code Review"
description: "When people think of code reviews, they usually think in terms of an   explicit step in a development team's workflow. These days the Pre-Integration Review, carried out on aPull Requestis the most co"
date: 2021-01-28T00:00:00
tags: ["continuous delivery", "process theory", "collaboration", "refactoring"]
url: https://martinfowler.com/bliki/RefinementCodeReview.html
slug: RefinementCodeReview
word_count: 1061
---


When people think of code reviews, they usually think in terms of an
  explicit step in a development team's workflow. These days the [Pre-Integration Review](https://martinfowler.com/articles/branching-patterns.html#reviewed-commits), carried out on a [Pull Request](https://martinfowler.com/bliki/PullRequest.html) is the most common mechanism for a code review, to the
  point that many people witlessly consider that not using pull requests removes
  all opportunities for doing code review. Such a narrow view of code reviews
  doesn't just ignore a host of explicit mechanisms for review, it more
  importantly neglects probably the most powerful code review technique - that
  of perpetual refinement done by the entire team.


One of the most pervasive perspectives in software is the notion that it's
  something we build and complete - hence the endless metaphor of building
  construction and architecture. Yet the key property of software is that it is
  *soft*, and can be as easily modified after it's released as
  it was when initially composed in the programmer's editor. That's why Erik Dörnenburg
  wisely argues that architecture is a poor metaphor and would be better
  [replaced by town planning](https://youtu.be/qVyt3qQ_7TA?t=228). Valuable
  software is usually in a constant state of change, as we add features from a
  better understanding of the value it can bring. But the opportunity is not
  just to add new features, but also to refine that software - incorporating the
  lessons the 
  team steadily learns about how best that software can enable
  these changes.


With the right environment, I can look a bit of code written six months
  ago, see some problems with how it's written, and quickly fix them. This may
  be because this code was flawed when it was written, or that changes in the
  code base since led to the code no longer being quite right. Whichever the
  cause, the important thing is to fix problems as soon as they start getting in
  our way. As soon as I have an understanding about the code that wasn't
  immediately apparent from reading it, I have the responsibility to (as Ward
  Cunningham so wonderfully said) take that understanding out of my head and put
  it into the code. That way the next reader won't have to work so hard.


This process of refinement is exactly the same as what happens in a code
  review, but it's triggered each time the code is looked at rather than when the
  code is added to the codebase. This was, for me, a crucial insight. After all,
  many problems that code reviews seek to remedy are problems that only become
  problems when the code is read in the future. There's a strong argument for
  not worrying about them until then. After all, just like adding a large
  apartment complex changes traffic patterns, we may have altered the context of
  the code six months later, altering the kind of fix that code needs. It also
  involves more people, in this scheme every developer that reads the code is a
  reviewer, and one that's able to review based on their actual use of the code
  rather than on some general, but often hazily-justified guidelines.


A way to think about the validity of a practice is by thinking about
  what happens if it's a monopoly. What if the only code review mechanism we
  have is the iteration from later programmers? One consequence is that the
  review attention gets concentrated on the areas of code that are read more
  often - which is mostly the areas that ought to get the attention. One
  concern is that code that's never read will never get reviewed - but
  mostly that's fine. A team with good testing practices can be confident that
  the code works, performance tests can identify performance issues. Given that, if
  the code never needs to be looked at again, we don't need to spend effort on
  making it comprehensible. I'd expect such cases to be vanishingly rare, but
  it's an informative thought experiment.


But most ≠ all. One obvious exception here is security issues. Code can
  work just fine for years until an attacker finds an exploit, at that point
  we'll lament its lack of review. This is an example of high-impact but rare
  safety concerns which deserve special scrutiny. However that doesn't mean we
  shouldn't make conscious use of refinement as a code review mechanism. Instead
  it means we should be aware of rare-high-impact concerns and adjust our
  workflow to watch for that kind of specific problem to the degree that it's
  needed in our circumstances. Threat analysis should alert us to the modules
  that need additional attention and the kinds of risks they face. Targeted code
  reviews might be scheduled for security concerns, these can run more
  effectively because they are focused on a specific kind of problem.


In order to do this perpetual code refinement we require other practices.
  If I'm going to change code I need to have confidence that it won't break
  existing functionality, so I need something like [Self Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html). I need to know that it won't cause big merge
  conflicts for others, so I need [Continuous
  Integration](https://martinfowler.com/articles/branching-patterns.html#continuous-integration). We all need to be good at [refactoring](https://refactoring.com/) so we can change code effectively. Since this
  relies on many developers being expected to modify any part of the code base,
  we are best off with [collective (or at least
  weak) code ownership.](https://martinfowler.com/bliki/CodeOwnership.html) But given a team that has these skills, they
  can rely on using their regular refinement as a substantial part of their code
  review strategy.


If nothing else, I think it's important that we put more thought into the
  role of refinement as code review. One of the dangers of focusing solely on
  Pre-Integration Reviews is that it can lead teams to neglect how change works
  in a code base. If I have a pristine mainline, and ensure that every commit
  merged into that mainline is pristine - can I be sure that the codebase is
  still pristine after six months? I'd argue that I can't, because the changes
  mean a good decision about some code six months ago is no longer a good
  decision now. Refining the code allows us to evaluate old code against this
  changing usage, allowing us to sustain its health.


## Acknowledgements

Ben Noble, Chris Ford, Evan Bottcher, Ian
    Cartwright, Jeremy Huiskamp, Ken Mugrage, Mario Giampietri, Martha Rohte, Omar Bashir, Peter Gillard-Moss, and Simon Brunning commented on drafts of this post on
    our internal mailing list.