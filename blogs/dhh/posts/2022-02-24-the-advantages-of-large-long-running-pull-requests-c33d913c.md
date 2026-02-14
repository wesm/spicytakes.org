---
title: "The advantages of large, long-running pull requests"
date: 2022-02-24
url: https://world.hey.com/dhh/the-advantages-of-large-long-running-pull-requests-c33d913c
slug: the-advantages-of-large-long-running-pull-requests-c33d913c
word_count: 564
---

My favorite part of doing code reviews is to see all the trade-offs, design decisions, and changes in context together. You can't easily do that if your feature has been chopped into itty bitty pieces as independent pull requests under pressure never to let them run longer than a week. So at Basecamp, we let pull requests run as long as they need to encompass a complete feature or fix. That's everything from a few weeks up to as much as six (since we follow
[Shape Up](https://basecamp.com/shapeup)
).
This approach isn't entirely without trade-offs. The longer your pull request is running off the main branch, the greater the chance that you'll have merge conflicts. But you can mitigate much of this by ensuring you keep your pull request up to date with main by frequently merging main into the pull request. I can appreciate how very large organizations with high traffic on the same bits of code might hit a point where that still just doesn't cut it, but is that really you?
It's never been us. And we've frequently had a handful of teams working on the same product, working in close proximity. And yes, we've occasionally hit merge conflicts, but I can't remember the last time those were seriously impeding the work. Still, there's a cost, and the larger you are, the bigger it may become.
But that's what frustrates me a little about the debate over how long to let your pull requests run. It focuses mostly on the cost, not on the value. And the value is tremendous to any organization that seeks to keep high design standards and a cohesive architecture.
One way to think about the degradation of code reviews that results from doing them across many, separate, disjointed pull requests, without seeing the big picture until the end, is through the negative externalities that this process produces.
High design standards and a cohesive architecture bank the rivers of clear code. When you pour those partially-there, I-havent-seen-the-end pull requests in, you easily end up polluting those pristine waters. It isn't clear right away what that might do, it's just a drop in the river after all, but if you keep it up, eventually the rivers no longer run clear.
I'm thinking of code that didn't embrace a key insight to simplify the whole thing when viewed as a whole from 30,000 feet. Code that doesn't leave the campsite in a better condition than it found it, because doing the cleanup is something for another pull request, on another day (by no one ever). Code that's been shipped now feeling too much of a hassle to change.
We often think of the code review as something done by others, but it's frequently just as powerful a method for a programmer to do to themselves. When working on a substantial piece of work, I'm frequently hopping back and forth between TextMate and the complete GitHub diff for all the commits. It's in this dance you see the shape of the code, pick up on bad smells, and ultimately decide whether you're happy with the whole.
So please don't chop up your pull requests until the cost of doing so definitively outpaces the value. What works for mega corps working on million-line code bases probably isn't fit for smaller systems that still have a fighting chance at keeping their structural integrity.
