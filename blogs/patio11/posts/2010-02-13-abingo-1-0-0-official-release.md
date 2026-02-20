---
title: "A/Bingo 1.0.0 Official Release"
date: 2010-02-13
url: https://www.kalzumeus.com/2010/02/14/abingo-1-0-0-official-release/
slug: abingo-1-0-0-official-release
word_count: 1044
---


[Back in August](https://www.kalzumeus.com/2009/08/15/introducing-abingo-rails-split-testing/) I released [A/Bingo](http://www.bingocardcreator.com/abingo), an MIT-licensed OSS Rails A/B testing framework.  I have been using it continuously on [Bingo Card Creator](http://www.bingocardcreator.com), and judging from the support requests I’ve been getting it has gotten some traction in the Rails world.  The 5,000 or so people seeing A/B tests on my site on Valentine’s Day are almost certainly less than 1% of the beneficiaries of the software now. Yay.


As A/Bingo has grown in popularity, I have begun to get requests for features that I did not need urgently for my own development, as well as the usual support requests, patches, and the like.  I want to make your use of the software as pleasant as possible to further evangelize the cause of A/B testing, so here you go:


## New features:


**A/Bingo now ships with a default dashboard**.  Previously, I assumed that everyone would be writing their own dashboard code, so I just included the absolute minimum to show you what you’d need to do to get data out of A/Bingo.  Many people have remarked that they would really appreciate a “works out of the box” solution.  Your wish is my command — you can now enable a default dashboard in about ~30 seconds. It would work totally out of the box, but there are security implications, so I wanted you to have to think for a moment prior to enabling it.


You can customize the dashboard code yourself. Nota bene: it uses your application layout, and has CSS classes applied to most of the elements, so you can style it quickly with CSS if you desire to. By default, it probably looks terrible. If you want to send me a patch to make it pretty, be my guest.


**Experiments can now be stopped**: Using either the built-in links on the above controller or, if you prefer programmatically scripting things, experiment.end_experiment!(alternative_content), you can now stop an experiment without touching the code.  Stopping an experiment causes all users to get the specified alternative rather than what they would have gotten randomly.  It also ceases stats collection.  Stopping an experiment is irreversible (currently — that might change later).  I tried to make this feature not affect the performance of A/Bingo for larger sites — it makes each test require one extra cache access.  (*cough* Rounding error, hopefully.)


**A/Bingo internals are now fairly thoroughly tested**: Unit tests are not exactly my cup of tea (“Argh, it works in production, what else do you want from me?!”), but Rails developers look askance at software that does not include them.  So I knuckled down and wrote a test suite.  (Hat tip to [Nathaniel Talbott](http://blog.talbott.ws/) for mentioning A/Bingo in a [conference presentation](http://rubyconf2009.confreaks.com/19-nov-2009-17-15-how-tdd-missed-the-point-introducing-edd-nathaniel-talbott.html).  The constructive criticism regarding testing drove this change.)


I have not written thorough integration tests for the syntax sugar that you get via the included helper methods, but I’ll fix that eventually.


**Named conversions**: Previously, all A/Bingo tests required one line to add the test and one line somewhere else to track conversions.  Typically, since businesses have very many tests and fairly few conversion events, this resulted in code like:


That isn’t very DRY at all.


Now, A/Bingo will take an optional parameter :conversion (or :conversion_name) when you’re defining a test, telling it to listen to a particular named conversion. This way, you can reuse the same conversion for as many tests as you want, decreasing the lines of code needed to create most new tests from two to one.


**A/Bingo handles tests with spaces in them more gracefully**: Although I still don’t recommend doing it, A/Bingo has been improving its handling of test names which have a space in them.  (The reason I don’t recommend it is because some cache stores — particularly memcached — do not support this well.)


**Official support for Redis**: [Assaf Arkin](http://labnotes.org/) picked Redis for his awesome [Vanity](http://vanity.labnotes.org) project (which also does A/B testing for Rails, among other things), which inspired me to take a look into it.  It appears to be a much, much better alternative for a key/value store than Memcachedb, which is what I use for persistence.  A/Bingo has always accepted any cache store that Rails does, but I want to make it explicitly clear that I run tests against Redis, Memcached, and MemcacheDB. Just add the following to your environment:


I intend to migration my own deployment to Redis when it becomes reasonably convenient for doing so.


**Versioning**: Previously I’ve just released patches to the A/Bingo git repository when I got done coding them, but I feel that is suboptimal now that there are substantial deployments which I could potentially break with changes.  So, here’s the skinny: A/Bingo is now, as of this blog post, 1.0.0.  I’ll communicate breaking changes by bumping that number up.  If it goes up by a tenth or more, expect that you need to re-run the migrations and that you will probably lose data on any tests in-progress, so plan ahead for that.  Version increases in that last number *should* be safe to apply directly.


I do not anticipate breaking the published A/Bingo API (i.e. methods mentioned in the docs) until at least v2.0.0, if ever, so upgrading A/Bingo should almost never cause you to need to update your own code.


## How To Contribute


I would like to thank everyone who has submitted bug reports and patches. As usual, I’m always happy to get bug reports or feature requests. If you’d like to contribute code, make it available via git anywhere you please, and then send me an email telling me about it.


## How Do I…


If the question isn’t answered in the (copious)  [documentation](http://www.bingocardcreator.com/abingo), feel free to ask me over email. If your business has particular needs for A/Bingo or you just want to talk A/B testing strategy with somebody who breathes it, I’m available for consulting engagements starting April 1st.


## You Should Be Doing A/B Testing


I really can’t stress this enough: A/B testing is an easy, reproducible process that you can use to improve your marketing, website copy, product, user experience, etc. If you haven’t started yet, take [A/Bingo](http://www.bingocardcreator.com), [Vanity](http://vanity.labnotes.org), or your other framework of choice for a spin. It won’t take you five minutes until you’re getting **actionable data** which you can use to make money.
