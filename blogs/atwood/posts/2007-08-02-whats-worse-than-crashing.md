---
title: "What’s Worse Than Crashing?"
date: 2007-08-02
url: https://blog.codinghorror.com/whats-worse-than-crashing/
slug: whats-worse-than-crashing
word_count: 650
---

Here’s an interesting thought question from Mike Stall: [what’s worse than crashing?](https://web.archive.org/web/20070909090958/http://blogs.msdn.com/jmstall/archive/2007/07/26/there-are-things-worse-than-crashing.aspx)


Mike provides the following list of crash scenarios, in order from best to worst:

1. Application works as expected and never crashes.
2. Application crashes due to rare bugs that nobody notices or cares about.
3. Application crashes due to a commonly encountered bug.
4. Application deadlocks and stops responding due to a common bug.
5. Application crashes long after the original bug.
6. **Application causes data loss and/or corruption.**


Mike points out that there’s a natural tension between...

- failing *immediately* when your program encounters a problem, e.g. “fail fast”
- attempting to recover from the failure state and proceed normally


The philosophy behind “fail fast” is best explained in [Jim Shore’s article](http://www.martinfowler.com/ieeeSoftware/failFast.pdf) (pdf).


> Some people recommend making your software robust by working around problems automatically. This results in the software “failing slowly.” The program continues working right after an error but fails in strange ways later on. A system that fails fast does exactly the opposite: when a problem occurs, it fails immediately and visibly. Failing fast is a nonintuitive technique: “failing immediately and visibly” sounds like it would make your software more fragile, but it actually makes it more robust. Bugs are easier to find and fix, so fewer go into production.


Fail fast is reasonable advice – if you’re a developer. What could possibly be easier than calling everything to [a screeching halt](https://blog.codinghorror.com/unnecessary-dialogs-stopping-the-proceedings-with-idiocy/) the minute you get a byte of data you don’t like? Computers are spectacularly unforgiving, so it’s only natural for developers to reflect that masochism directly back on users.


But from the user’s perspective, failing fast isn’t helpful. To them, it’s just another [meaningless error dialog](https://blog.codinghorror.com/teaching-users-to-read/) preventing them from getting their work done. The best software never pesters users with meaningless, trivial errors – it’s [more considerate than that](https://blog.codinghorror.com/making-considerate-software/). Unfortunately, **attempting to help the user by fixing the error could make things worse by leading to subtle and catastrophic failures down the road.** As you work your way down Mike’s list, the pain grows exponentially. For both developers *and* users. Troubleshooting #5 is a brutal death march, and by the time you get to #6 – you’ve lost or corrupted user data – you’ll be lucky to have any users *left* to fix bugs for.


What’s interesting to me is that despite causing more than my share of software crashes and hardware bluescreens, I’ve *never* lost data, or had my data corrupted. You’d figure Murphy’s Law would force the worst possible outcome at least once a year, but it’s exceedingly rare in my experience. Maybe this is an encouraging sign for the current state of software engineering. Or maybe I’ve just been lucky.


So what can we, as software developers, do about this? If we adopt a “fail as often and as obnoxiously as possible” strategy, we’ve clearly failed our users. But if we corrupt or lose our users’ data through misguided attempts to prevent error messages – if we fail to treat our users’ data as sacrosanct – we’ve *also* failed our users. You have to do both at once:

1. If you *can* safely fix the problem, you should. Take responsibility for your program. Don’t slouch through the easy way out by placing the burden for dealing with every problem squarely on your users.
2. If you *can’t* safely fix the problem, always err on the side of protecting the user’s data. Protecting the user’s data is a sacred trust. If you harm that basic contract of trust between the user and your program, you’re hurting not only your credibility – but the credibility of the entire software industry as a whole. Once they’ve been burned by data loss or corruption, users don’t soon forgive.


The guiding principle here, as always, should be to **respect your users**. Do the right thing.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
