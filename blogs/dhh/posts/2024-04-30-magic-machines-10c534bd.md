---
title: "Magic machines"
date: 2024-04-30
url: https://world.hey.com/dhh/magic-machines-10c534bd
slug: magic-machines-10c534bd
word_count: 434
---

There's an interesting psychological phenomenon where programmers tend to ascribe more trust to computers run by anyone but themselves. Perhaps it's a corollary to imposter syndrome, which leads programmers to believe that if a computer is operated by AWS or SaaS or literally anyone else, it must be more secure, better managed, less buggy, and ultimately purer. I wish that was so, but there are no magic machines and no magic operators. Just the same kind of potentially faulty bits and brains.
A great example of this was the feedback to our declaration that
[we're bringing continuous integration back to developer machines](https://world.hey.com/dhh/we-re-moving-continuous-integration-back-to-developer-machines-3ac6c611)
. The most common objection was to invoke "it works on my machine", as to imply that developer machines were somehow a different breed than the ones running in the cloud or the data center. They really aren't! The computer running tests remotely is indeed just that: Another computer. It isn't magical, and it's no less prone to be reliant on unaccounted for dependencies or environmental factors.
In fact, when it comes to testing, it's a feature not a bug to have the suite run on multiple machines. It's like an extra fuzzy check that will uncover undeclared dependencies, and help you produce a more resilient system. Because even the best CI setup isn't production. And just because it works in CI doesn't mean it'll be free of issues in production.
Which leads us to the whole point of testing systems in the first place: It's about confidence, not certainty. The road to programmer misery is paved with delusional aspirations that you can ever be fully, truly certain that any sufficiently complicated system will ever work as intended in production. All you have is degrees of confidence to trade-off against increasingly cumbersome protocols and procedures. There's no such thing as 100% test coverage that's meaningful and achievable at the same time.
And it's the fundamental lack of confidence in their own abilities that lead programmers to think that the people operating their cloud computers are so much smarter or better than they are. They rarely are. They're just hidden, and it's that opaqueness that false implies a higher competence. If only you knew what kind of frazzled mechanical turk it takes to run most cloud institutions or SaaS operations, you wouldn't be so quick to doubt your own abilities.
There's no magic class of computers and no magic class of computing clerics. "It works on my computer" is just the midwit version of "it works on THAT computer". It's all just computers. You can figure them out, you can make them dance.
