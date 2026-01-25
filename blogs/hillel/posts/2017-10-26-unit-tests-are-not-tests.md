---
title: "Unit Tests Aren't Tests"
date: 2017-10-26
url: https://www.hillelwayne.com/post/unit-tests-are-not-tests/
slug: unit-tests-are-not-tests
word_count: 698
---

This is an absolutely insane idea and I’m delighted by its audacity so I’m sharing it with all y’all. There’s like a bazillion things wrong with it but saying dumb shit has never stopped me before so let’s do some [grambling](https://twitter.com/malt_skull/status/628295687403343872)!


The way I see it, unit tests act as a frame around your coding. The most common practice is you write the tests to cover the return values and calls, write your code, and enforce that it passes the unit tests. This happens at the unit level, hence “unit” tests. We mock out any dependencies in order to keep it fast and focused on the unit. You write the tests as a scaffolding for the code.


The problem is that your program is a collection of interdependent units, and you’re not testing the total program with unit tests. There’s this idea in physics called “emergence”, where simple systems interacting with simple rules give rise to complex systems acting by effectively different rules. For example, atoms are relatively well-understood, self-contained models. Chuck enough of them in a box and suddenly you have the entire field of solid-state physics. Add the assumption that “electrons can’t be inside the protons” and now you have semiconductors. Add a couple more rules and physics throws its hands in the air, says “fuck this”, and fobs it off on the chemists.


Code exhibits emergence too. Enough interacting units and your program is vastly more complex than the sum of its parts. Even if each unit is well-behaved and works according to its unit tests, the bulk of the complexity is in their integration. Since you’re interested in the program behaving correctly, not its individual units of code, and since unit tests don’t determine the program is behaving correctly (only the code), they’re not testing the program. Ergo, they’re not tests. They’re development.


Look, I already said it’s an insane idea. That means I’m immune to criticism. And if I’m being honest with myself, I’m less interested in making a watertight argument as much as exploring the consequences of this assumption. So if you can pretend to be convinced, let’s see what happens when you say “unit tests aren’t tests!”


**Waterfall and Agile converge.** You know how everybody’s all “Agile rules, waterfall sucks?” When you get down to it, all “waterfall” is is organized phases of work, design-develop-test-rollout. “Agile” as most companies practice it is ‘just’ waterfall with really tight work cycles.1 Instead of a few big cycles, you do a bunch of small ones and call it “iterations”.


“But waterfall has testing as a separate phase, while agile has you write tests while developing!” In practice, you actually write *unit tests* while developing. If that counts as development and not testing, we’re back to having mostly-separate phases, and the two methodologies stop contracting each other. We can share lessons between them again.


**We can stop fighting over whether developers or testers write unit tests.** Developers write unit tests, since it’s development. Testers write other tests.


**Testing gets a lot wilder.** Since unit tests are no longer tests, you can no longer point at a codebase swathed in unit tests and say “yeah that’s tested.” So how, then, *could* we test? Turns out there’s a lot of crazy stuff out there that most people ignore because we think unit tests are sufficient. You can take visual snapshots and compare them to master. You can build rule-based state machines. You can match the logic against a fault tree.2 Since tests are not coupled to your unit test suite, you can prioritize thoroughness over runspeed.


**We’re forced to treat QA Engineers as equals.** I mean we should be doing this either way, but it’s starker under the “unit tests don’t count” assumption. Good testing is really, *really* hard. In many cases it’s harder than slinging the business logic. QA engineers aren’t second-class citizens, they’re specialists.


This post doesn’t deserve a good conclusion.


---

1. Yeah sure there’s probably companies that do agile way better but let’s ignore them because BECAUSE, that’s why
 [return]
2. “Hey Hillel, why aren’t you shilling formal methods?” Formal methods are fantastic tools, but they’re for designing systems, not testing them.
 [return]
