---
title: "Slow database test fallacy"
date: 2014-04-30
url: https://dhh.dk/2014/slow-database-test-fallacy.html
slug: slow-database-test-fallacy
word_count: 735
---


The classical definition of a unit test in TDD lore is one that doesn't touch the database. Or any other external interface, like the file system. The justification is largely one of speed. Connecting to external services like that would be too slow to get the feedback cycle you need.


That was probably true in 1997 when you were connecting to a mainframe database or some Oracle abomination. It's not true in 2014 where you can run your MySQL or PostgreSQL database locally off a super-fast SSD. You'll be hard pressed to even find a development machine today that doesn't have gobs of RAM, an SSD drive, and a speedy CPU.


Thus is the progress of computers. Heuristics and principles we adopt in one era of computing do not necessarily apply tomorrow. In fact, anything that's based on a definition of "slow" should be revisited frequently. Sound lessons can turn unsound very quickly. This is exactly what's happened to the "don't touch the database!" recommendation for unit testing.


As I detailed in [test-induced design damage](http://david.heinemeierhansson.com/2014/test-induced-design-damage.html), it's far from free to abstract yourself away from touching the database in most MVC systems. The amount of indirection and additional layers needed end up scarring the code base and hurting the clarity of the system. Inflicting such damage may well had been worth it back in the old days when a full suite of tests hitting the database would have taken hours to run. It so much certainly is not when we're talking about a few minutes.

**All tests in 4 minutes, all model tests in 80 seconds**

I can run every single model test in the Basecamp suite in 80 seconds. That's 3333 assertions, all hitting the database, all going through Active Record, and all using the killer Rails feature of test fixtures. The entire suite, which includes controller and integration tests that likewise go through the database and test fixtures, runs in 4 minutes and 30 seconds. That's for a 1:1 test:code ratio.


You might think, well, that's pretty fast for a whole suite, but I still wouldn't want to wait 80 seconds every time I make a single change to my model, and want to test that. Of course not! Why on earth would you run your entire test harness for every single line change in a particular model? If you have so little confidence in the locality of your changes, the tests are indeed telling you that the system has overly high coupling.


What I do is to run just the suite for the model in question. For large Rails applications, this used to still be a little painful. You had to wait for Rails to boot the entire application every time you wanted to run the suite, which took about 5 seconds for Basecamp. Enough to be annoying.


Rails has since adopted a persistent test process through the wonderful [Spring preloader](https://github.com/rails/spring). Just like CGI was a bad model for any complicated web application, so too is reloading your entire application and framework on every test run. These days I can run the entire test suite for our Person model — 52 cases, 111 assertions — in just under 4 seconds from start to finish. Plenty fast enough for a great feedback cycle!

**The power of test fixtures**

This great speed is partly due to the wonders of test fixtures. The default test fixtures in Rails are reset on a per case basis, such that each test case runs in isolation, but it's done through a transaction wrapper. Before each test case, we do BEGIN TRANSACTION, and at the end of the case, we do ROLLBACK TRANSACTION. This is crazy fast, so there's no setup penalty.


Then when you're done working on your model, and you're ready to check in your new feature, or just take a little break, you run the entire 80-second suite. Just to make sure that you didn't inadvertently break something in a far away model.


Between the two modes of testing, you'll have great confidence in your ability to make changes and develop new functionality, without the anxiety of breaking stuff left and right. THAT'S the true power of testing!


So please. Don't pervert your architecture in order to prematurely optimize for the performance characteristics of the mid-nineties. Embrace the awesome power of modern computers, and revel in the clarity of a code base unharmed by test-induced design damage.

