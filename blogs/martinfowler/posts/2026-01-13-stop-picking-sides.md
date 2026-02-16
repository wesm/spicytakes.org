---
title: "Stop Picking Sides"
description: "Many teams have turned into tribes wedded to exclusively adaptation   or optimization. But this misses the point that both of these are important,   and we need to manage the tension between them. We "
date: 2026-01-13T00:00:00
tags: ["agile", "process theory"]
url: https://martinfowler.com/articles/stop-picking-sides.html
slug: stop-picking-sides
word_count: 1425
---


I like Agile. I like discipline. I like systems that ship and systems
    that learn.


What I don’t like: tribes.


In the last couple decades, many teams camped at the ends of a
    spectrum:

- Traditional shops treated optimization as virtue and adaptation as risk.
- Agile shops treated adaptation as virtue and optimization as betrayal.


Both missed the point.


By adaptation I mean fast learning and course-correction under
    uncertainty.


By optimization I mean reliability and repeatability under
    constraints.


The mistake is treating either one as a permanent operating mode.


The adult question is: what should dominate right now?


This is a tension to manage, not a side to pick.


![](stop-picking-sides/infograph.jpg)


## Why this matters now (beyond software)


Software teams have lived inside this tension for years.


Now more industries hit the same wall—fast.


Life sciences (Biotech) provides clear examples. Tools like CRISPR
      (gene editing), AlphaFold (3-D protein folding) and other AI-assisted
      discovery models compress early cycles.


CRISPR‑based tools aided COVID‑19 research and target discovery, while
      platform technologies like mRNA and viral vectors were the key enablers of
      the one‑year vaccine timeline. AlphaFold can often do in hours on a
      computer what used to take months or years in the lab.


Using these tools teams can explore more options, faster. That sounds
      like pure upside—until you remember the other side of the tension:
      downstream work gets more expensive, more constrained, and less
      forgiving.


Faster learning does not remove constraints. It raises the cost of
      sloppy decisions.


So the capability gap shifts. It’s no longer “Can we âdoâ Agile?” It’s:
      Can we manage the Adaptation ↔ Optimization tension on purpose—at
      speed?


## What I mean by “two modes”


I use two modes as a practical shorthand. They are not philosophies.
      They are operating patterns.


### Explore mode (adaptation-dominant)


Purpose: reduce uncertainty fast.


Explore mode treats work as a series of hypotheses.

- You run short cycles: hypothesis → test → signal → decision.
- You keep costs low so you can change course.
- You protect evidence quality enough to trust the signal.


Explore mode does *not* mean chaos. It means you optimize the
        learning loop.


### Exploit mode (optimization-dominant)


Purpose: reduce variance under constraints.


Exploit mode treats work as a system you must run reliably.

- You tighten the process.
- You raise evidence thresholds.
- You protect safety, quality, security, traceability.
- You still adapt, but only inside clear guardrails.


Exploit mode does *not* mean bureaucracy. It means you optimize
        reliability.


### One important nuance: dominance, not purity


Both modes exist all the time.

- Explore phases still need optimization (cycle time, evidence hygiene, stop
          rules).
- Exploit phases still need adaptation (disciplined amendments, controlled
          experiments, risk-based exceptions).


Dominance keeps you out of religion.


## A bridge state: “Expand”


Using the words explore and exploit often brings to mind Kent Beck’s
      [explore–expand–extract](https://medium.com/@kentbeck_7670/fast-slow-in-3x-explore-expand-extract-6d4c94a7539). That connection is useful.


I see expand as the bridge state where a promising signal moves from
      cheap learning to scaled evidence.


In expand, you do three things at once:

- 1. Scale proof (more cases, more volume, more environments)
- 2. Raise constraints (quality, safety, governance, integration
        discipline)
- 3. Reduce ambiguity (clear thresholds for the next commitment)


Expand is where many orgs pay the highest handoff tax, because teams
      keep explore behaviors while the work now demands exploit discipline.


## The handoff tax


Most programs don’t fail inside a phase.


They fail at the seams.


I call the hidden cost at seams the handoff tax:

- translation failures (same words, different meaning)
- evidence mismatch (different bars for “enough proof”)
- ownership fog (too many votes, too many vetoes)
- traceability gaps (no one can reconstruct why a choice happened)


If you want speed, cut handoff tax. It beats “doing Agile harder.”


## A quick detour: why bimodal IT backfired


One early “solution” to this tension was bimodal IT: put exploratory
      work in one lane and stable delivery in another—frequently as separate
      organizational units.


On paper it looked tidy.


In practice it turned into warring tribes. One side became the
      innovation heroes. The other became the stability police. Decisions
      bounced between them, handoff tax exploded, and leaders tried to manage
      conflict instead of designing the work.


The lesson: you can’t outsource this tension to an org chart. The
      capability has to live in every person who makes decisions—from team
      members to executives.


## A concrete example: Sciex and early integration


In 2004–2006 I worked with Sciex, an ISO-certified mass spectrometry
      instrument firm. A crash in the middle of a sample run can ruin an
      experiment and waste irreplaceable samples.


After a year plus working with software teams we tackled a daunting
      project–development of a new mass spec instrument.


We found the big killer to be integration debt (handoff tax)—the pain
      you store up when hardware, firmware, and software converge late.


ISO requirements kept governance real. So we avoided a false
      choice.

- Governance optimized for time, money, and traceability.
- Execution adapted to uncertainty with short feedback loops and early
        integration.


Then the Director of Product Development pushed a simple shift:

- firmware delivered to hardware in iterations, paced by hardware’s test
        schedule
- once hardware reached “enough function,” software joined to add
        applications—also in increments
- they did *not* wait for a fully populated digital board to start
        integration tests


Outcome:

- integration tests started sooner, so issues surfaced earlier and resolved
        faster
- integration stayed continuous once minimal hardware existed, so the usual
        end-game resource spike disappeared
- communication improved because all groups participated in integration, not
        just at the panic stage


That is dominance tuning in the wild:

- explore early where uncertainty stays high
- expand as evidence scales and constraints rise
- exploit once reliability matters more than option creation


## Make dominance operational: four dials


If you want dominance without debates, use dials.

- Uncertainty — what you do not know yet
- Risk — what breaks if you guess wrong
- Cost of change — what a pivot costs in time, money, credibility
- Evidence threshold — how much proof you require before you commit


Turn the dials, set dominance, then design the workflow to match.


### Explore-dominant: tune the learning loop

- short cycle time from hypothesis → test → signal → decision
- clear stop rules (kill weak bets fast)
- evidence hygiene (assumptions, controls, reproducible notes)


Two common failures: slow learning and messy evidence.


### Expand: scale proof and tighten constraints

- larger samples, broader environments, more integration points
- rising governance discipline
- explicit thresholds for the next commitment


Two common failures: false certainty and late integration.


### Exploit-dominant: adapt inside guardrails

- disciplined amendments, with triggers and clean rationale
- controlled experiments (not accidental variance)
- traceability you can defend under audit


Two common failures: compliance theater and hidden workarounds.


## Decision rights: use DARE, not RACI


Speed and accountability need clear decision rights. This is not
      hierarchy worship.


Many orgs reach for [RACI:](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)*Responsible, Accountable, Consulted,
      Informed.* In practice, RACI often turns decisions into calendar sludge
      and polite vetoes.


Use DARE instead: *Deciders, Advisors, Recommenders, Execution
      stakeholders.*


DARE keeps “servant leadership” and “self-organizing” (and their
      cousins: “empowered teams,” “decentralized decisions”) from sliding into
      soft anarchy: you can give more people a voice without giving everyone a
      vote.

- Deciders: the only votes; often one (but not exclusively)
- Advisors: strong voice, no veto
- Recommenders: build options and tradeoffs
- Execution stakeholders: execute the call and surface constraints early


DARE works at every level—from a product team to the CEO staff—because
      the pattern stays the same:

- clear decider(s)
- real input
- real options
- fast commitment


DARE saves autonomy from turning into consensus-by-exhaustion.


## Tailoring: treat it as operating design


Many teams treat tailoring like weight loss: start with a big method,
      cut steps, hope speed shows up.


That is disassembly.


Real tailoring means design for fit:

- keep constraints that protect safety, quality, traceability
- keep practices that protect learning speed and option creation
- design seams so modes don’t fight each other


Tailoring also demands judgment, and judgment stays scarce. You can buy
      tools and templates. You can’t buy discernment at scale.


## The take-away


Stop selling “Agile vs Traditional.” That story sells the problem.


Design for the tension:

- treat explore, expand, exploit as a set of dominance patterns
- turn the dials on purpose
- cut handoff tax at seams
- treat tailoring as operating design


*Where do you pay the highest handoff tax today—and which dial would
      you turn first?*


---
