---
title: "Measuring Developer Productivity via Humans"
description: "Measuring developer productivity is a difficult challenge. Conventional metrics focused on development cycle time and throughput are limited, and there aren't obvious answers for where else to turn. Q"
date: 2024-03-19T00:00:00
tags: ["metrics", "productivity"]
url: https://martinfowler.com/articles/measuring-developer-productivity-humans.html
slug: measuring-developer-productivity-humans
word_count: 4570
---


Somewhere, right now, a technology executive tells their directors: “we
    need a way to measure the productivity of our engineering teams.” A working
    group assembles to explore potential solutions, and weeks later, proposes
    implementing the metrics: lead time, deployment frequency, and number of
    pull requests created per engineer.


Soon after, senior engineering leaders meet to review their newly created
    dashboards. Immediately, questions and doubts are raised. One leader says:
    “Our lead time is two days which is ‘low performing’ according to those
    benchmarks – but is there actually a problem?”. Another leader says: “it’s
    unsurprising to see that some of our teams are deploying less often than
    others. But I’m not sure if this spells an opportunity for improvement.”


If this story arc is familiar to you, don’t worry – it's familiar to
    most, including some of the biggest tech companies in the world. It is not uncommon
    for measurement programs to fall short when metrics like DORA fail to provide
    the insights leaders had hoped for.


There is, however, a better approach. An approach that focuses on
    capturing insights from developers themselves, rather than solely relying on
    basic measures of speed and output. We’ve helped many organizations make the
    leap to this human-centered approach. And we’ve seen firsthand the
    dramatically improved understanding of developer productivity that it
    provides.


What we are referring to here is *qualitative measurement*. In this
    article, we provide a primer on this approach derived from our experience
    helping many organizations on this journey. We begin with a definition of
    qualitative metrics and how to advocate for them. We follow with practical
    guidance on how to capture, track, and utilize this data.


Today, developer productivity is a critical concern for businesses amid
    the backdrop of fiscal tightening and transformational technologies such as
    AI. In addition, developer experience and platform engineering are garnering
    increased attention as enterprises look beyond Agile and DevOps
    transformation. What all these concerns share is a reliance on measurement
    to help guide decisions and track progress. And for this, qualitative
    measurement is key.


**Note:** when we say “developer productivity”, we mean the degree to which
    developers' can do their work in a frictionless manner – not the individual
    performance of developers. Some organizations find “developer productivity”
    to be a problematic term because of the way it can be misinterpreted by
    developers. We recommend that organizations use the term “developer
    experience,” which has more positive connotations for developers.


## What is a qualitative metric?


We define a qualitative metric as a measurement comprised of data
      provided by humans. This is a practical definition – we haven’t found a
      singular definition within the social sciences, and the alternative
      definitions we’ve seen have flaws that we discuss later in this
      section.


![](measuring-developer-productivity-humans/qualitative-metrics.png)


Figure 1: Qualitative metrics are measurements derived from humans


The definition of the word “metric” is unambiguous. The term
      “qualitative,” however, has no authoritative definition as noted in the
      2019 journal paper [What is Qualitative in
      Qualitative Research](https://link.springer.com/article/10.1007/s11133-019-9413-7):


> There are many definitions of qualitative research, but if we look for
>       a definition that addresses its distinctive feature of being
>       “qualitative,” the literature across the broad field of social science is
>       meager. The main reason behind this article lies in the paradox, which, to
>       put it bluntly, is that researchers act as if they know what it is, but
>       they cannot formulate a coherent definition.


An alternate definition we’ve heard is that qualitative metrics measure
      quality, while quantitative metrics measure quantity. We’ve found this
      definition problematic for two reasons: first, the term “qualitative
      metric” includes the term *metric*, which implies that the output is a
      *quantity* (i.e., a measurement). Second, quality is typically measured
      through ordinal scales that are translated into numerical values and
      scores – which again, contradicts the definition.


Another argument we have heard is that the output of sentiment analysis
      is *quantitative* because the analysis results in numbers. While we agree
      that the data resulting from sentiment analysis is quantitative, based on
      our original definition this is still a qualitative *metric* (i.e., a quantity
      produced qualitatively) unless one were to take the position that
      “qualitative metric” is altogether an oxymoron.


Aside from the problem of defining what a qualitative metric is, we’ve
      also encountered problematic colloquialisms. One example is the term “soft
      metric”. We caution against this phrase because it harmfully and
      incorrectly implies that data collected from humans is *weaker *than “hard
      metrics” collected from systems. We also discourage the term “subjective
      metrics” because it misconstrues the fact that data collected from humans
      can be either objective or subjective – as we discuss in the next
      section.



| Type | Definition | Example |
| Attitudinal metrics | Subjective feelings, opinions, or attitudes toward a specific subject. | How satisfied are you with your IDE, on a scale of 1–10? |
| Behavioral metrics | Objective facts or events pertaining to an individual's work experience. | How long does it take for you to deploy a change to production? |



Later in this article we provide guidance on how to collect and use
      these measurements, but first we’ll provide a real-world example of this
      approach put to practice


Peloton is an American technology company
      whose developer productivity measurement strategy centers around
      qualitative metrics. To collect qualitative metrics, their organization
      runs a semi-annual developer experience survey led by their Tech
      Enablement & Developer Experience team, which is part of their Product
      Operations organization.


Thansha Sadacharam, head of tech learning and insights, explains: “I
      very strongly believe, and I think a lot of our engineers also really
      appreciate this, that engineers aren't robots, they're humans. And just
      looking at basic numbers doesn't drive the whole story. So for us, having
      a really comprehensive survey that helped us understand that entire
      developer experience was really important.”


Each survey is sent to
      a random sample of roughly half of their developers. With this approach,
      individual developers only need to participate in one survey per year,
      minimizing the overall time spent on filling out surveys while still
      providing a statistically significant representative set of data results.
      The Tech Enablement & Developer Experience team is also responsible for
      analyzing and sharing the findings from their surveys with leaders across
      the organization.


For more on Peloton’s developer experience survey, [listen to this
      interview](https://getdx.com/podcast/developer-experience-survey-at-peloton/)
      with Thansha Sadacharam.


## Advocating for qualitative metrics


Executives are often skeptical about the reliability or usefulness of
      qualitative metrics. Even highly scientific organizations like Google have
      had to overcome these biases. Engineering leaders are inclined toward
      system metrics since they are accustomed to working with telemetry data
      for inspecting systems. However, we cannot rely on this same approach for
      measuring people.


Avoid pitting qualitative and quantitative metrics against each other.


We’ve seen some organizations get into an internal “battle of the
      metrics” which is not a good use of time or energy. Our advice for
      champions is to avoid pitting qualitative and quantitative metrics against
      each other as an either/or. It’s better to make the argument that they are
      complementary tools – as we cover at the end of this article.


We’ve found that the underlying cause of opposition to qualitative data
      are misconceptions which we address below. Later in this article, we
      outline the distinct benefits of self-reported data such as its ability to
      measure intangibles and surface critical context.


### Misconception: Qualitative data is only subjective


Traditional workplace surveys typically focus on the subjective
      opinions and feelings of their employees. Thus many engineering leaders
      intuitively believe that surveys can only collect subjective data from
      developers.


As we describe in the following section, surveys can also capture
      objective information about facts or events. Google’s [DevOps Research and
      Assessment (DORA)](https://dora.dev/) program is an excellent concrete
      example.


Some examples of objective survey questions:

- How long does it take to go from code committed to code successfully
        running in production?
- How often does your organization deploy code to production or
        release it to end users?


### Misconception: Qualitative data is unreliable


One challenge of surveys is that people with all manner of backgrounds
      write survey questions with no special training. As a result, many
      workplace surveys do not meet the minimum standards needed to produce
      reliable or valid measures. Well designed surveys, however, produce
      accurate and reliable data (we provide guidance on how to do this later in
      the article).


Some organizations have concerns that people may lie in surveys. Which
      can happen in situations where there is fear around how the data will be
      used. In our experience, when surveys are deployed as a tool to help
      understand and improve bottlenecks affecting developers, there is no
      incentive for respondents to lie or game the system.


While it’s true that survey data isn’t always 100% accurate, we often
      remind leaders that system metrics are often imperfect too. For example,
      many organizations attempt to measure CI build times using data aggregated
      from their pipelines, only to find that it requires significant effort to
      clean the data (e.g. excluding background jobs, accounting for parallel
      jobs) to produce an accurate result


## The two types of qualitative metrics


There are two key types of qualitative metrics:

1. **Attitudinal metrics** capture subjective feelings, opinions, or
        attitudes toward a specific subject. An example of an attitudinal measure would
        be the numeric value captured in response to the question: “How satisfied are
        you with your IDE, on a scale of 1-10?”.
2. **Behavioral metrics** capture objective facts or events pertaining to an
        individuals’ work experiences. An example of a behavioral measure would be the
        quantity captured in response to the question: “How long does it take for you to
        deploy a change to production?”


We’ve found that most tech practitioners overlook behavioral measures
      when thinking about qualitative metrics. This occurs despite the
      prevalence of qualitative behavioral measures in software research, such
      as the Google’s DORA program mentioned earlier.


DORA publishes annual benchmarks for metrics such as lead time for
      changes, deployment frequency, and change fail rate. Unbeknownst to many,
      DORA’s benchmarks are captured using qualitative methods with the survey
      items shown below:


Lead time


For the primary application or service you work on,
          what is your lead time for changes (that is, how long does it take to go
          from code committed to code successfully running in production)?


More than six months


One to six months


One week to one month


One day to one week


Less than one day


Less than one hour


Deploy frequency


For the primary application or service you
          work on, how often does your organization deploy code to production or
          release it to end users?


Fewer than once per six months


Between once per month and once every six months


Between once per week and once per month


Between once per day and once per week


Between once per hour and once per day


On demand (multiple deploys per day)


Change fail percentage


For the primary application or service you work on, what
          percentage of changes to production or releases to users result in
          degraded service (for example, lead to service impairment or service
          outage) and subsequently require remediation (for example, require a
          hotfix, rollback, fix forward, patch)?


0–15%


16–30%


31–45%


46–60%


61–75%


76–100%


Time to restore


For the primary application or service you work on, how long
          does it generally take to restore service when a service incident or a
          defect that impacts users occurs (for example, unplanned outage, service
          impairment)?


More than six months


One to six months


One week to one month


One day to one week


Less than one day


Less than one hour


We’ve found that the ability to collect attitudinal and behavioral data
      *at the same time* is a powerful benefit of qualitative measurement.


For example, behavioral data might show you that your release process
      is fast and efficient. But only attitudinal data could tell you whether it
      is smooth and painless, which has important implications for developer
      burnout and retention.


To use a non-tech analogy: imagine you are feeling sick and visit a
      doctor. The doctor takes your blood pressure, your temperature, your heart
      rate, and they say “Well, it looks like you’re all good. There’s nothing
      wrong with you.” You would be taken aback! You'd say, âWait, I’m telling
      you that something feels wrong.”


## The benefits of qualitative metrics


One argument for qualitative metrics is that they avoid subjecting
      developers to the feeling of “being measured” by management. While we’ve
      found this to be true – especially when compared to metrics derived from
      developers’ Git or Jira data – it doesn’t address the main objective
      benefits that qualitative approaches can provide.


There are three main benefits of qualitative metrics when it comes to
      measuring developer productivity:


### Qualitative metrics allow you to measure things that are otherwise
      unmeasurable


System metrics like lead time and deployment volume capture what’s
      happening in our pipelines or ticketing systems. But there are many more
      aspects of developers’ work that need to be understood in order to improve
      productivity: for example, whether developers are able to stay in the flow
      or work or easily navigate their codebases. Qualitative metrics let you
      measure these intangibles that are otherwise difficult or impossible to
      measure.


An interesting example of this is technical debt. At Google, a study to
      identify metrics for technical debt included an analysis of 117 metrics
      that were proposed as potential indicators. To the disappointment of
      Google researchers, no single metric or combination of metrics were found
      to be valid indicators (for more on how Google measures technical debt,
      [listen to this interview](https://getdx.com/podcast/developer-productivity-at-google/)).


While there may exist an undiscovered objective metric for technical
      debt, one can suppose that this may be impossible due to the fact that
      assessment of technical debt relies on the comparison between the current
      state of a system or codebase versus its imagined ideal state. In other
      words, human judgment is essential.


### Qualitative metrics provide missing visibility across teams and
      systems


Metrics from ticketing systems and pipelines give us visibility into
      some of the work that developers do. But this data alone cannot give us
      the full story. Developers do a lot of work that’s not captured in tickets
      or builds: for example, designing key features, shaping the direction of a
      project, or helping a teammate get onboarded.


It’s impossible to gain visibility into all these activities through
      data from our systems alone. And even if we could theoretically collect
      all the data through systems, there are additional challenges to capturing
      metrics through instrumentation.


One example is the difficulty of normalizing metrics across different
      team workflows. For example, if you’re trying to measure how long it takes
      for tasks to go from start to completion, you might try to get this data
      from your ticketing tool. But individual teams often have different
      workflows that make it difficult to produce an *accurate* metric. In
      contrast, simply asking developers how long tasks typically take can be
      much simpler.


Another common challenge is cross-system visibility. For example, a
      small startup can measure TTR (time to restore) using just an issue
      tracker such as Jira. A large organization, however, will likely need to
      consolidate and cross-attribute data across planning systems and deployment
      pipelines in order to gain end-to-end system visibility. This can be a
      yearlong effort, whereas capturing this data from developers can provide a
      baseline quickly.


### Qualitative metrics provide context for quantitative data


As technologists, it is easy to focus heavily on quantitative measures.
      They seem clean and clear, afterall. There is a risk, however, that the
      full story isn’t being told without richer data and that this may lead us
      into focusing on the wrong thing.


One example of this is code review: a typical optimization is to try to
      speed up the code review. This seems logical as waiting for a code review
      can cause wasted time or unwanted context switching. We could measure the
      time it takes for reviews to be completed and incentivize teams to improve
      it. But this approach may encourage negative behavior: reviewers rushing
      through reviews or developers not finding the right experts to perform
      reviews.


Code reviews exist for an important purpose: to ensure high quality
      software is delivered. If we do a more holistic analysis – focusing on the
      outcomes of the process rather than just speed – we find that optimization
      of code review must ensure good code quality, mitigation of security
      risks, building shared knowledge across team members, as well as ensuring
      that our coworkers aren’t stuck waiting. Qualitative measures can help us
      assess whether these outcomes are being met.


Another example is developer onboarding processes. Software development
      is a team activity. Thus if we only measure individual output metrics such
      as the rate new developers are committing or time to first commit, we miss
      important outcomes e.g. whether we are fully utilizing the ideas the
      developers are bringing, whether they feel safe to ask questions and if
      they are collaborating with cross-functional peers.


## How to capture qualitative metrics


Many tech practitioners don’t realize how difficult it is to write good
      survey questions and design good survey instruments. In fact, there are
      whole fields of study related to this, such as psychometrics and
      industrial psychology. It is important to bring or build expertise here
      when possible.


Below are few good rules for writing surveys to avoid the most common
      mistakes we see organizations make:

- Survey items need to be carefully worded and every question should only ask
        one thing.
- If you want to compare results between surveys, be careful about changing
        the wording of questions such that you’re measuring something different.
- If you change any wording, you must do rigorous statistical tests.


In survey parlance, ”good surveys” means “valid and reliable” or
      “demonstrating good psychometric properties.” Validity is the degree to
      which a survey item actually measures the construct you desire to measure.
      Reliability is the degree to which a survey item produces consistent
      results from your population and over time.


One way of thinking about survey design that we’ve found helpful to
      tech practitioners: think of the survey response process as an algorithm
      that takes place in the human mind.


When an individual is presented a survey question, a series of mental
      steps take place in order to arrive at a response. The model below is from
      the seminal 2012 book, *[The Psychology of Survey
      Response](https://www.cambridge.org/core/books/psychology-of-survey-response/46DE3D6F7C1399BCDC78D9441C630372)*:



| Component | Specific Processes |
| Comprehension | Attend to questions and instructions
Represent logical form of question
Identify question focus (information sought)
Link key terms to relevant concepts |
| Retrieval | Generate retrieval strategy and cues
Retrieve specific, generic memories
Fill in missing details |
| Judgment | Assess completeness and relevance of memories
Draw inferences based on accessibility
Integrate material retrieved
Make estimate based on partial retrieval |
| Response | Map Judgement onto response category
Edit response |



Decomposing the survey response process and inspecting each step
      can help us refine our inputs to produce more accurate survey results.
      Developing good survey items requires rigorous design, testing, and
      analysis – just like the process of designing software!


But good survey design is just one aspect of running successful surveys.
      Additional challenges include participation rates, data analysis, and knowing
      how to act on data. Below are some of the best practices we’ve
      learned.


### Segment results by team and persona


A common mistake made by organizational leaders is to focus on companywide
      results instead of data broken down by team and persona (e.g., role, tenure,
      seniority). As previously described, developer experience is highly contextual
      and can differ radically across teams or roles. Focusing only on aggregate
      results can lead to overlooking problems that affect small but important
      populations within the company, such as mobile developers.


### Free text comments are often most valuable


We’ve been talking about qualitative *metrics* but free text comments are an
      extremely valuable form of qualitative data. Beyond describing the friction or
      workflow, developers will have many great ideas to improve their developer
      experience, the free text allows us to capture those, and identify who to follow
      up with. Free text comments can also surface areas that your survey did not
      cover, which could be added in the future.


### Compare results against benchmarks


Comparative analysis can help contextualize data and help drive action. For
      example, developer sentiment toward code quality commonly skews negative, making
      it difficult to identify true problems or gauge their magnitude. The more
      actionable data point is: “are our developers *more* frustrated about code
      quality than other teams or organizations?” Teams with lower sentiment scores
      than their peers and organizations with lower scores than their industry peers
      can surface notable opportunities for improvement.


### Use transactional surveys where appropriate


Transactional surveys capture feedback during specific touchpoints or
      interactions in the developer workflow. For example, platform teams can use
      transactional surveys to prompt developers for feedback while they are in the midst of
      creating a new service in an internal developer portal. Transactional surveys can
      also augment data from periodic surveys by producing higher-frequency feedback and
      more granular insights.


### Avoid survey fatigue


Many organizations struggle to sustain high participation rates in surveys
      over time. Lack of follow-up can cause developers to feel that
      repeatedly responding to surveys is not worthwhile. It is therefore
      critical that leaders and teams follow up and take meaningful action after surveys.
      While a quarterly or
      semi-annual survey cadence is optimal for most organizations, we’ve seen some
      organizations be successful with more frequent surveys that are integrated into
      regular team rituals such as retrospectives.


### Survey Template


Below are a simple set of survey questions for getting started. Load the questions
        below into your preferred survey tool, or get started quickly by making a copy of our ready-to-go
        [Google Forms template](https://docs.google.com/forms/d/1ODvYtgE6AQ6EFmAvdYJWofzDNqg9NH6-kyeH2IHBSWc/template/preview).


The template is intentionally simple, but surveys often become quite sizable as your measurement
        strategy matures. For example, [Shopify's developer survey](https://getdx.com/podcast/shopify-developer-happiness-survey/) is 20-minutes
        long and [Google's ](https://getdx.com/podcast/developer-productivity-at-google/)is over 30-minutes long.


After you've collected responses, score the multiple choice questions
        using either mean or top box scoring. Mean scores are calculated by
        assigning each option a value between 1 and 5 and taking the average.
        Top box scores are calculated by the percentages of responses that
        choose one of the top two most favorable options.


Be sure to review open text responses which can contain great
        information. If you've collected a large number of comments, LLM tools
        such as ChatGPT can be useful for extracting core themes and
        suggestions. When you've finished analyzing results, be sure to share
        your findings with respondents so their time filling out the survey
        feels worthwhile.


How easy or difficult is it for you to do work as a
            developer or technical contributor at [INSERT ORGANIATION NAME]?


Very difficult


Somewhat difficult


Neither easy nor difficult


Somewhat easy


Very easy


For the primary application or service you work on, what
            is your lead time for changes (that is, how long does it take to go
            from code committed to code successfully running in
            production)?


More than one month


One week to one month


One day to one week


Less than one day


Less than one hour


How often do you feel highly productive in your
            work?


Never


A little of the time


Some of the time


Most of the time


All of the time


Please rate your agreement or disagreement with the following
          statements:



|  | Strongly disagree | Disagree | Neutral | Agree | Strongly agree |
| My team follows development best practices | □ | □ | □ | □ | □ |
| I have enough time for deep work. | □ | □ | □ | □ | □ |
| I am satisfied with the amount of automated test coverage in
            my project. | □ | □ | □ | □ | □ |
| It's easy for me to deploy to production. | □ | □ | □ | □ | □ |
| I'm satisfied with the quality of our CI/CD tooling. | □ | □ | □ | □ | □ |
| My team's codebase is easy for me to contribute to. | □ | □ | □ | □ | □ |
| The amount of technical debt on my team is appropriate based on our goals. | □ | □ | □ | □ | □ |
| Specifications are continuously revisited and reprioritized according to user signals. | □ | □ | □ | □ | □ |



Please share any additional feedback on how your developer experience could be improved


[open textarea]


## Using qualitative and quantitative metrics together


Qualitative metrics and quantitative metrics are complementary approaches
      to measuring developer productivity. Qualitative metrics, derived from
      surveys, provide a holistic view of productivity that includes both subjective
      and objective measurements. Quantitative metrics, on the other hand, provide
      distinct advantages as well:

- **Precision. **Humans can tell you whether their CI/CD builds are generally
        fast or slow (i.e., whether durations are closer to a minute or an hour), but
        they cannot report on build times down to millisecond precision. Quantitative
        metrics are needed when a high degree of precision is needed in our
        measurements.
- **Continuity.** Typically, the frequency at which an organization can survey
        their developers is at most once or twice per quarter. In order to collect more
        frequent or continuous metrics, organizations must gather data
        systematically.


Ultimately, it is through the combination of qualitative and quantitative metrics – a *mixed-methods approach* –
      that organizations can gain maximum visibility into the productivity and
      experience of developers. So how do you use qualitative and quantitative
      metrics together?


We’ve seen organizations find success when they start with qualitative
      metrics to establish baselines and determine where to focus. Then, follow with
      quantitative metrics to help drill in deeper into specific areas.


Engineering leaders find this approach to be effective because qualitative
      metrics provide a holistic view and context, providing wide understanding of
      potential opportunities. Quantitative metrics, on the other hand, are
      typically only available for a narrower set of the software delivery
      process.


Google similarly advises its engineering leaders to go to survey data first
      before looking at logs data for this reason. Google engineering researcher
      Ciera Jaspan explains: “We encourage leaders to go to the survey data first,
      because if you only look at logs data it doesn't really tell you whether
      something is good or bad. For example, we have a metric that tracks the time
      to make a change, but that number is useless by itself. You don't know, is
      this a good thing? Is it a bad thing? Do we have a problem?”.


A mixed methods approach allows us to take advantage of the benefits of
      both qualitative and quantitative metrics while getting a full understand of
      developer productivity:

1. Start with qualitative data to identify your top opportunities
2. Once you know what you want to improve, use quantitative metrics to
        drill-in further
3. Track your progress using both qualitative and quantitative metrics


It is only by combining as much data as possible – both qualitative and
      quantitative – that organizations can begin to build a full understanding of
      developer productivity.


In the end, however, it’s important to remember: organizations spend a lot
      on highly qualified humans that can observe and detect problems that log-based
      metrics can’t. By tapping into the minds and voices of developers,
      organizations can unlock insights previously seen as impossible.


---
