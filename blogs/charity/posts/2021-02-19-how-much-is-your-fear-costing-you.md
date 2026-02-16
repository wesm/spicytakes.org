---
title: "How much is your fear of continuous deployment costing you?"
date: 2021-02-19
url: https://charity.wtf/2021/02/19/how-much-is-your-fear-costing-you/
word_count: 576
---


Most people aren’t doing true CI/CD. Most teams wait far too long to get their code into prod after writing it. Most painful of all are the teams who have done all the hard parts — wired up continuous integration, achieved test coverage, etc — but still deploy by hand, thus depriving themselves of the payoff for their hard work.


Any time an engineer merges a diff back to main, this ought to trigger a full run of your CI/CD pipeline, culminating with an automatic deploy to production. This should happen once per mergeset, never batching multiple engineers’ diffs in a run, and it should be over and done with in 15 minutes or less with no human intervention.


[It’s 2021, and everyone should know this by now](https://stackoverflow.blog/2021/01/19/fulfilling-the-promise-of-ci-cd/).


✨✨**15 minutes or bust✨✨**


Okay, but what if you don’t? How costly can it be, really?


Let’s do some back of the envelope math. First you’ll need to answer a couple questions about your org and deploy pipeline.

- How many engineers do you have? ____________
- How long typically elapses between when someone writes code and that code is live in production? _____________


Let (n) be the number of engineers it takes to efficiently build and run your product, assuming each set of changes will autodeploy individually in <15 min.

- If changes typically ship on the order of hours, you need 2(n).
- If changes ship on the order of days, you need 2(2(n)).
- If changes ship on the order of weeks, you need 2(2(2(n)))
- If changes ship on the order of months, you need 2(2(2(2(n))))


Your 6 person team with a consistent autodeploy loop would take 24 people to do the same amount of work, if it took days to deploy their changes. Your 10 person team that ships in weeks would need 80 people.


At cost to the company of approx 200k per engineer, that’s $3.6 million in the first example and $14 million in the second example. **That’s how much your neglect of internal tools and kneejerk fear of autodeploy might be costing you.**


It’s not just about engineers. The more delay you add into the process of building and shipping code, the more pathologies multiply, and you find yourselves needing to spend more and more time addressing those pathologies instead of making forward progress for the business. Longer diffs. Manual deploy processes. Bunching up multiple engineers’ diffs in a single deploy, then spending the rest of the day trying to figure out which one was at fault for the error.


Soon you need an SRE team to handle your reliability issues, build engineering specialists to build internal tools for all these engineers, managers to manage the teams, product folks to own the roadmap and project managers to coordinate all this blocking and waiting on each other…


You could have just fixed your build process. You could have just committed to continuous delivery. You would be moving more swiftly and confidently as a small, killer team than you ever could at your lumbering size.


✨✨**15 minutes or bust✨✨**


In 2021, how will *you* achieve the dream of CI/CD, and liberate your engineers from the shackles of pointless toil?


P.S. if you want to know my methodology for coming up with this equation, it’s called “pulled out of my ass because it sounded about right, then checked with about a dozen other technical folks to see if it aligned with their experience.”
