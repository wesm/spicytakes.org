---
title: "Pull Request"
description: "When people think of code reviews, they usually think in terms of an   explicit step in a development team's workflow. These days the Pre-Integration Review, carried out on aPull Requestis the most co"
date: 2021-01-28T00:00:00
tags: ["continuous delivery", "tools"]
url: https://martinfowler.com/bliki/PullRequest.html
slug: PullRequest
word_count: 1076
---


Pull Requests are a mechanism popularized by github, used to help facilitate merging of
  work, particularly in the context of open-source projects. A contributor works
  on their contribution in a fork (clone) of the central repository. Once their
  contribution is finished they create a pull request to notify the owner of the
  central repository that their work is ready to be merged into the mainline.
  Tooling supports and encourages code review of the
  contribution before accepting the request.  Pull requests have become widely
  used in software development, but critics are concerned by the addition of
  integration friction which can prevent continuous integration.


Pull requests essentially provide convenient tooling for a development
  workflow that existed in many open-source projects, particularly those using a
  distributed source-control system (such as git). This workflow begins with a
  contributor creating a new logical branch, either by starting a new branch in
  the central repository, cloning into a personal repository, or both. The
  contributor then works on that branch, typically in the style of a [Feature Branch](https://martinfowler.com/articles/branching-patterns.html#feature-branching), pulling any updates from [Mainline](https://martinfowler.com/articles/branching-patterns.html#mainline) into their branch. When they are done they communicate
  with the maintainer of the central repository indicating that they are done,
  together with a reference to their commits. This reference could be the URL of
  a branch that needs to be integrated, or a set of patches in
  an email.


Once the maintainer gets the message, she can then examine the commits to
  decide if they are ready to go into mainline. If not, she can then suggest
  changes to the contributor, who then has opportunity to adjust their
  submission. Once all is ok, the maintainer can then merge, either with a
  regular merge/rebase or applying the patches from the final email.


Github's pull request mechanism makes this flow much easier. It keeps track
  of the clones through its fork mechanism, and automatically creates a message
  thread to discuss the pull request, together with behavior to handle the
  various steps in the review workflow. These conveniences were a major part of
  what made github successful and led to âpull requestâ becoming a fundamental
  part of the developer's lexicon.


So that's how pull requests work, but should we use them, and if so how? To
  answer that question, I like to step back from the mechanism and think about
  how it works in the context of a source code management workflow. To help me
  think about that, I wrote down a series of [patterns for managing source code branching](https://martinfowler.com/articles/branching-patterns.html). I
  find understanding these (specifically the Base and Integration patterns)
  clarifies the role of pull requests.


In terms of these patterns, pull requests are a mechanism designed to
  implement a combination of [Feature Branching](https://martinfowler.com/articles/branching-patterns.html#feature-branching) and
  [Pre-Integration Reviews](https://martinfowler.com/articles/branching-patterns.html#reviewed-commits). Thus to assess the
  usefulness of pull requests we first need to consider how applicable those
  patterns are to our situation. Like most patterns, they are sometimes
  valuable, and sometimes a pain in the neck - we have to examine them based on
  our specific context. Feature Branching is a good way of packaging together a
  logical contribution so that it can be assessed, accepted, or deferred as a
  single unit. This makes a lot of sense when contributors are not trusted to
  commit directly to mainline. But Feature Branching comes at a cost, which is
  that it usually limits the frequency of integration, leading to complicated
  merges and deterring refactoring. Pre-Integration Reviews provide a clear
  place to do code review at the cost of a significant increase in integration
  friction. 1


1: 
      A colleague of mine recently calculated the time a client spent waiting
      for pull requests that had no comments (true of 91% of them). Total time
      waiting in 2020 for 7000 PRs was 130,000 hours. This figure included time
      elapsed over nights and weekends.


That's a drastic summary of the situation (I need a lot more words to
  explain this further in the feature branching article), but it boils down to
  the fact that the value of these patterns, and thus the value of pull
  requests, rest mostly on the social structure of the team. Some teams work
  better with pull requests, some teams would find pull requests a severe drag
  on the effectiveness. I suspect that since pull requests are so popular, a lot
  of teams are using them by default when they would do better without them.


While pull requests are built for Feature Branches, teams can use them
  within a [Continuous Integration](https://martinfowler.com/articles/branching-patterns.html#continuous-integration) environment. To do
  this they need to ensure that pull requests are small enough, and the team
  responsive enough, to follow the CI rule of thumb that everybody does [Mainline Integration](https://martinfowler.com/articles/branching-patterns.html#mainline-integration) at least daily. (And I should
  remind everyone that Mainline Integration is more than just merging the
  current mainline into the feature branch). Using the [ship/show/ask](https://martinfowler.com/articles/ship-show-ask.html)
  classification can be an effective way to integrate pull requests into a more
  CI-friendly workflow.


The wide usage of pull requests has encouraged a wider use of code review,
  since pull requests provide a clear point for Pre-Integration Review, together
  with tooling that encourages it. Code review is a Good Thing, but we must
  remember that a pull request isn't the only mechanism we can use for it. Many
  teams find great value in the [continuous
  review](https://martinfowler.com/articles/on-pair-programming.html#CodeReviewOn-the-go) afforded by Pair Programming. To avoid reducing integration
  frquency we can carry out post-integration code review in several ways. A
  formal process can record a review for each commit, or a tech lead can examine
  risky commits every couple of days. Perhaps the most powerful form of code
  review is one that's frequently ignored. A team that takes the attitude that
  the codebase is a fluid system, one that can be steadily refined with repeated
  iteration carries out [Refinement Code Review](https://martinfowler.com/bliki/RefinementCodeReview.html) every time a
  developer looks at existing code. I often hear people say that pull requests
  are necessary because without them you can't do code reviews - that's rubbish.
  Pre-integration code review is just one way to do code reviews, and for many
  teams it isn't the best choice.


## Acknowledgements

Chris Ford, Dan Mutton, Jeremy Huiskamp, Kief Morris, Pramod
    Sadalage, and Ryan Boucher commented on drafts of this post on
    our internal mailing list.

## Notes


1: 
      A colleague of mine recently calculated the time a client spent waiting
      for pull requests that had no comments (true of 91% of them). Total time
      waiting in 2020 for 7000 PRs was 130,000 hours. This figure included time
      elapsed over nights and weekends.
