---
title: "Outcome Over Output"
description: "Imagine a team writing software for a shopping website. If we look at the   team's output, we might consider how many new features they produced in the   last quarter, or a cross-functional measure su"
date: 2020-02-11T00:00:00
tags: ["productivity", "metrics"]
url: https://martinfowler.com/bliki/OutcomeOverOutput.html
slug: OutcomeOverOutput
word_count: 1028
---


Imagine a team writing software for a shopping website. If we look at the
  team's output, we might consider how many new features they produced in the
  last quarter, or a cross-functional measure such as a reduction in page load
  time. An outcome measure, however, would consider measure increased sales
  revenue, or reduced number of support calls for the product. Focusing on
  outcomes, rather than output, favors building features that do more to improve
  the effectiveness of the software's users and customers.


![](images/outcome-over-output/sketch.png)


As with any professional activity, those of us involved in software
  development want to learn what makes us more effective. This is true of an
  individual developer trying to improve her own performance, for managers looking
  to improve teams within an organization, or a maven like me trying to raise
  the game of the entire industry. One of the things that makes this difficult
  is that there's no clear way to measure the productivity of a software team.
  And this measurement question gets further complicated by whether we base
  effectiveness on output or outcome.


I've always been of the opinion that outcome is what we should concentrate
  on. If a team delivers lots of functionality - whether we measure it in lines
  of code, function points, or stories - that functionality doesn't matter if it
  doesn't help the user improve their activity. Lots of unused features are
  wasted effort, indeed worse than that they bloat the code base making it
  harder to add new features in the future. Such a software development team needs
  to care about the usefulness of the new functionality, they improve as they
  deliver less features, but of greater utility.


One argument I've heard against using outcome-based observations is that it's
  harder to come up with repeatable measures for outcomes than it is for output.
  I find this point difficult to fathom. Measuring pure output for software is
  famously difficult. Lines of code are a useless measure even if they weren't
  so easily gamed. There's poor replicability with Function Point or Story
  Points - different people will give the same things different point scores.
  Compared to this, we are very good at measuring financial outcomes. Of course,
  many outcome observations are more tricky to make - consider customer satisfaction -
  but I don't see any of them as more difficult than software functionality.


Just calling something an “outcome”, of course, doesn't make something the
  right thing to focus on, and there is certainly a skill to picking the right
  outcomes to observe. One handy notion is that of [Seiden](https://www.amazon.com/gp/product/B07QJ1Y8Y5/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07QJ1Y8Y5&linkCode=as2&tag=martinfowlerc-20), who says that an outcome should be a change in
  behavior of a user, employee, or customer that drives a good thing for the
  organization. He makes a distinction between “outcomes”, which are behavioral
  changes that are easier to observe, and “impacts” which are broader effects upon
  the organization. In developing EDGE, [Highsmith, Luu,
  and Robinson](https://www.amazon.com/gp/product/0135263077/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0135263077&linkCode=as2&tag=martinfowlerc-20) advise that outcomes about customer value (reliability of
  a dishwasher) should be given more weight than outcomes about business value
  (warranty repair costs).


A consequential concern about using outcome observations is that it's harder to
  apportion them to a software development team. Consider a customer team that uses software
  to help them track the quality of goods in their supply chain. If we assess
  them by how many rejects there are by the final consumer, how much of that is
  due to the software, how much due the quality control procedures
  developed by quality analysts, and how much due to a separate initiative to
  improve the quality of raw materials? This difficulty of apportionment is a
  huge hurdle if we want to compare different software teams, perhaps in order
  to judge whether using Clojure has helped teams be more effective. Similarly
  there is  the case that
  the developers work well and deliver excellent and valuable software to track
  quality, but the quality control procedures are no good. Consequently rejects
  don't go down and the initiative is seen as a failure, despite the developers
  doing a great job on their part.


But the problems of apportionment shouldn't be taken as a reason to observe
  the wrong thing. The common phrase says âyou get what you measureâ, in this
  case it's more like âyou get what you try to measureâ. If you focus appraisal
  of success on output, then everyone is thinking about how to increase the
  output. So even if it's tricky to determine how a team's work affects outcome, the
  fact that people are instead thinking about outcomes and how to improve them
  is worth more than any effort to compare teams' proficiency in producing the
  wrong things.


## Further Reading


[Seiden](https://www.amazon.com/gp/product/B07QJ1Y8Y5/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07QJ1Y8Y5&linkCode=as2&tag=martinfowlerc-20) provides a nice framework for
    thinking of outcomes, one that's informed by experiences with non-profits
    who have a similarly tricky job of evaluating the impact of their work.


My colleagues developed [EDGE](https://www.amazon.com/gp/product/0135263077/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0135263077&linkCode=as2&tag=martinfowlerc-20) as an
    operating model for transforming businesses to work in the digital world.
    Focusing on outcomes is a core part of their philosophy.


Focusing on outcomes naturally leads to favoring [Outcome Oriented](https://martinfowler.com/bliki/OutcomeOriented.html) teams.


## Acknowledgements


My fellow pioneers in the early days of Extreme Programming were very
    aware of the faults of assessing software development in terms of output. I
    remember Ron Jeffries and I arguing at an early agile conference workshop
    that any measures of a team's effectiveness should focus on outcome rather
    than output - although we did not use those words yet. That thinking is also
    reflected in my post [Cannot Measure Productivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html).


I recall starting to hear my colleagues at Thoughtworks talking about a
    distinction between outcome and output appearing in the 2000s, leading
    Daniel Terhorst-North to suggest that outcome over features should be a
    [fifth agile value](https://dannorth.net/2006/10/28/outcomes-over-features-the-fifth-agile-value/). This favor to outcomes is a
    regular theme in Thoughtworks-birthed books such as [Lean Enterprise](https://www.amazon.com/gp/product/1449368425/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1449368425&linkCode=as2&tag=martinfowlerc-20), [EDGE](https://www.amazon.com/gp/product/0135263077/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0135263077&linkCode=as2&tag=martinfowlerc-20), and
    the [Digital Transformation Game Plan](https://www.amazon.com/gp/product/1492054399/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1492054399&linkCode=as2&tag=martinfowlerc-20).


Alexander Steinhart, Alexandra Mogul, Andy Birds, Dale Peakall, Dean Eyre, Gabriel Sixel, Jeff Mangan, Job Rwebembera, Kief Morris, Linus
    Karsai, Mariela Barzallo, Peter
    Gillard-Moss, Steven Wilhelm, Vanessa Towers, Vikrant Kardam, and Xiao Ran discussed drafts of this post
    on our internal mailing list. Peter Gillard-Moss led me to the Seiden
    book and other work from the non-profit world.
