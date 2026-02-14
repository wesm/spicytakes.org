---
title: "System tests have failed"
date: 2024-05-17
url: https://world.hey.com/dhh/system-tests-have-failed-d90af718
slug: system-tests-have-failed-d90af718
word_count: 476
---

When we introduced a
[default setup for system tests](https://guides.rubyonrails.org/5_1_release_notes.html#system-tests)
in Rails 5.1 back in 2016, I had high hopes. In theory, system tests, which drive a headless browser through your actual interface, offer greater confidence that the entire machine is working as it ought. And because it runs in a black-box fashion, it should be more resilient to implementation changes. But I'm sad to report that I have not found any of this to be true in practice. System tests remain as slow, brittle, and full of false negatives as they did a decade ago.
I'm sure there are many reasons for this state of malaise. Browsers are complicated, UI driven by JavaScript is prone to timing issues, and figuring out WHY a black-box test has failed is often surprisingly difficult. But the bottom line for me is that system tests no longer seem worth the effort the majority of the time. Or said another way, I've wasted far more time getting system tests to work reliably than I have seen dividends from bugs caught.
Which gets to the heart of why we automate testing. We do it for the quick feedback loop on changes, we do it to catch regressions, but most of all, we do it to become confident that the system works. These are all valid goals, but that doesn't mean system testing is the best way to fulfill them.
Now I'm not advocating you throw out all your system tests. Just, you know, probably most of them. System tests work well for the top-level smoke test. The end-to-end'ness has a tendency to catch not problems with the domain model or business logic, but some configuration or interaction that's preventing the system from loading correctly at all. Catching that early and cheaply is good.
The stickiest point, however, is not testing business logic, which model and controller tests do better and cheaper, but testing UI logic. Which means testing JavaScript. And I'll say I'm not sure we're there yet on the automated front.
The method that gives me the most confidence that my UI logic is good to go is not system tests, but human tests. Literally clicking around in a real browser by hand. Because half the time UI testing is not just about "does it work" but also "does it feel right". No automation can tell you that.
HEY today has some 300-odd system tests. We're going through a grand review to cut that number way down. The sunk cost fallacy has kept us running this brittle, cumbersome suite for too long. Time to cut our losses, reduce system tests to a much smaller part of the confidence equation, and
[embrace the human element of system testing](https://signalvnoise.com/svn3/the-value-of-human-exploratory-testing/)
. Maybe one day we can hand that task over to AI, but as of today, I think we're better off dropping the automation.
