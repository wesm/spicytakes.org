---
title: "Four principles of software engineering"
date: 2020-10-09
url: https://drewdevault.com/2020/10/09/Four-principles-of-software-engineering.html
slug: Four-principles-of-software-engineering
word_count: 204
---

Software should be  **robust** . It should be designed to accommodate all known
edge cases. In practice, this means predicting and handling all known error
cases, enumerating and addressing all classes of user inputs, reasoning about
and planning for the performance characteristics of your program, and so on.

Software should be  **reliable** . It should be expected to work for an extended
length of time under design conditions without failures. Ideally, it should work
outside of design conditions up to some threshold.

Software should also be  **stable** . It should not change in incompatible or
unexpected ways; if it works today it should also work tomorrow. If it has to
change, a plan shall be written. Stakeholders (including users!) should be given
advance notice and should be involved in the planning stage.

Finally, software should be  **simple** . Only as many moving parts should be
included as necessary to meet the other three goals. All software has bugs, but
complicated software (1) has more bugs and (2) is more difficult to diagnose
and fix. Note that designing a simple solution is usually more difficult than
designing a complex solution.

*This (short) article is based on [a Mastodon post](https://cmpwn.com/@sir/104931806273081351) I wrote a few weeks ago.*
