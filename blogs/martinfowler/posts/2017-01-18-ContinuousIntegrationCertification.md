---
title: "Continuous Integration Certification"
description: "Continuous Integration is a popular technique in software development. At conferences   many developers talk about how they use it, and Continuous Integration tools are common   in most development or"
date: 2017-01-18T00:00:00
tags: ["certification", "continuous delivery"]
url: https://martinfowler.com/bliki/ContinuousIntegrationCertification.html
slug: ContinuousIntegrationCertification
word_count: 1098
---


[Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) is a popular technique in software development. At conferences
  many developers talk about how they use it, and Continuous Integration tools are common
  in most development organizations. But we all know that any decent technique needs a certification
  program — and fortunately one does exist. Developed by one of the foremost experts in
  continuous delivery and devops, it’s known for being remarkably rapid to administer, yet
  very insightful for its results. Although it’s quite mature, it isn’t as well known as
  it should be, so as a fan of the technique I think it’s important for me to share this
  certification program with my readers. Are you ready to be certified for Continuous
  Integration? And how
  will you deal with the shocking truth that taking the test will reveal?


By now my regular readers are wondering if they’ve come across a parody post 1, and yes
  I am having a little fun with my opening teaser. But like any good joke there’s an
  important kernel of truth buried in it. There is a remarkably good test for proper
  Continuous Integration that was created by [Jez Humble](https://twitter.com/jezhumble) - and he certainly is a leading
  expert in [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html). It’s also a rapid test, he often administers it to his
  audience during his talks. The only problem is that I’ve never heard him refer to it as a
  certification test - which just shows his lack of vision for money-making schemes.


1: 
      In general, I'm not a fan of software certification schemes, as they usually fail
      the [CertificationCompetenceCorrelation](https://martinfowler.com/bliki/CertificationCompetenceCorrelation.html)


He usually begins the certification process by asking his audience to raise their
  hands if they do Continuous Integration. Usually most of the audience raise their hands.


He then asks them to keep their hands up if everyone on their team commits and pushes
  to a shared mainline (usually shared master in git) at least daily.


Over half the hands go down.


He then asks them to keep their hands up if each such commit causes an automated
  build and test. Half the remaining hands are lowered.


Finally he asks if, when the build fails, it’s usually back to green within ten
  minutes. 2


2: 
      For this step, âgreenâ counts as passing the [commit
      build](https://martinfowler.com/articles/continuousIntegration.html#commit-build), typically compilation and unit tests. While we usually expect a full
      [DeploymentPipeline](https://martinfowler.com/bliki/DeploymentPipeline.html) to be run for release to production, a repository
      should be fine for developers to work on after the commit build is green. You should
      have a commit build that takes no more than ten minutes, so quickly fixing it and
      re-running the commit build works if the fix is easy. If you can't fix and get a
      green commit build within ten minutes, then you should revert to the last green build.


With that last question only a few hands remain. Those are the people who pass his
  certification test.


![](images/ci-certification/sketch.png)


It’s a simple set of questions, but it gets to the core of what Continuous
  Integration is about. The whole idea is that nobody is working on a code base that
  deviates significantly from anyone else’s. Continuous Integration means the team knows
  what the current state of the code truly is, we avoid big risky merges, and people can
  refactor as much as they need to.


The reason so many people raise their hands at the beginning is the common view that
  Continuous Integration means running some “Continuous Integration Server” against their
  feature branches. But Continuous Integration — as it was originally described and named
  by Kent Beck as part of [ExtremeProgramming](https://martinfowler.com/bliki/ExtremeProgramming.html) — has nothing to do with tools. At the
  beginning it was a human workflow and Jim Shore [made an excellent argument](http://www.jamesshore.com/Blog/Continuous-Integration-on-a-Dollar-a-Day.html) that it
  *should* be that. The idea of running a daemon process against a source code
  repository came later, and while it is helpful, it’s only Continuous Integration if it’s
  run on a shared mainline that people commit to every day. Running such a process
  otherwise, such as on every [FeatureBranch](https://martinfowler.com/bliki/FeatureBranch.html), is [CI theater](https://www.thoughtworks.com/radar/techniques/ci-theatre) that debases the name 3, yielding a workflow that doesn't give you the benefits that make the whole
  thing worth the effort.


3: 
      The problem of CI theater leads some people to use the name [Trunk-Based Development](http://paulhammant.com/2013/04/05/what-is-trunk-based-development/), arguing that
  [SemanticDiffusion](https://martinfowler.com/bliki/SemanticDiffusion.html) has rendered the term “Continuous Integration” useless.
  While I understand their view, I believe that we shouldn’t give in to semantic
  diffusion, instead we need to keep working at re-explaining the proper meaning of
  Continuous Integration, just as we should with other terms under this kind of semantic
  assault (such as “agile” and “refactoring”). After all Kent was quite clear in
  his definition of the term, and using another diminishes the important role he
  had in popularizing the technique via the Extreme Programming community.


## Further Reading


For more details on Continuous Integration, see [my main
    article](https://martinfowler.com/articles/continuousIntegration.html), while written in 2006 it's still a solid summary and definition of the
    technique. Jez explains why [Continuous Integration is a foundation
    for Continuous Delivery](https://continuousdelivery.com/foundations/continuous-integration/). He states the three questions in the FAQ on that page.
    Paul Duvall wrote [the definitive book](https://martinfowler.com/books/duvall.html) on Continuous
    Integration. Watch [Jez administer the certification test](https://www.youtube.com/watch?v=mBUJ-fg4EKA#t=16m27s)
    at GOTO Chicago in 2014 (sadly there was no camera on the audience).


## Acknowledgements

All credit for the three questions go to Jez, whose talks I've always
    enjoyed.

## Notes


1: 
      In general, I'm not a fan of software certification schemes, as they usually fail
      the [CertificationCompetenceCorrelation](https://martinfowler.com/bliki/CertificationCompetenceCorrelation.html)


2: 
      For this step, âgreenâ counts as passing the [commit
      build](https://martinfowler.com/articles/continuousIntegration.html#commit-build), typically compilation and unit tests. While we usually expect a full
      [DeploymentPipeline](https://martinfowler.com/bliki/DeploymentPipeline.html) to be run for release to production, a repository
      should be fine for developers to work on after the commit build is green. You should
      have a commit build that takes no more than ten minutes, so quickly fixing it and
      re-running the commit build works if the fix is easy. If you can't fix and get a
      green commit build within ten minutes, then you should revert to the last green build.


3: 
      The problem of CI theater leads some people to use the name [Trunk-Based Development](http://paulhammant.com/2013/04/05/what-is-trunk-based-development/), arguing that
  [SemanticDiffusion](https://martinfowler.com/bliki/SemanticDiffusion.html) has rendered the term “Continuous Integration” useless.
  While I understand their view, I believe that we shouldn’t give in to semantic
  diffusion, instead we need to keep working at re-explaining the proper meaning of
  Continuous Integration, just as we should with other terms under this kind of semantic
  assault (such as “agile” and “refactoring”). After all Kent was quite clear in
  his definition of the term, and using another diminishes the important role he
  had in popularizing the technique via the Extreme Programming community.
