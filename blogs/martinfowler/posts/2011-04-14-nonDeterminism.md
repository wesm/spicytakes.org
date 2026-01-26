---
title: "Eradicating Non-Determinism in Tests"
description: "An automated regression suite can play a vital role on a software project, valuable both for reducing defects in production and essential for evolutionary design. In talking with development teams I'v"
date: 2011-04-14T00:00:00
tags: ["continuous delivery", "testing"]
url: https://martinfowler.com/articles/nonDeterminism.html
slug: nonDeterminism
word_count: 4047
---


I've enjoyed watching Thoughtworks tackle
  many difficult enterprise applications, bringing successful
  deliveries to many clients who have rarely seen success. Our
  experiences have been a great demonstration that agile methods,
  deeply controversial and distrusted when we wrote the manifesto a
  decade ago, can be used successfully.


There are many flavors of agile development out there, but in
  what we do there is a central role for automated testing. Automated
  testing was a core approach to Extreme Programming from the
  beginning, and that philosophy has been the biggest inspiration to
  our agile work. So we've gained a lot of experience in using
  automated testing as a core part of software development.


Automated testing can look easy when presented in a text
  book. And indeed the basic ideas are really quite simple. But in the
  pressure-cooker of a delivery project, trials come up that are often
  not given much attention in texts. As I know too well, authors have a
  habit of skimming over many details in order to get a core point
  across. In my conversations with our delivery teams, one recurring
  problem that we've run into is tests which have become unreliable,
  so unreliable that people don't pay much attention to whether they
  pass or fail. A primary cause of this unreliability is that some
  tests have become non-deterministic.


A test is non-deterministic when it passes sometimes and fails
    sometimes, without any noticeable change in the code, tests, or
    environment. Such tests fail, then you re-run them and they
    pass. Test failures for such tests are seemingly random.


Non-determinism can plague any kind of test, but it's
    particularly prone to affect tests with a broad scope, such as
    acceptance or functional tests.


## Why non-deterministic tests are a problem


Non-deterministic tests have two problems, firstly they are
    useless, secondly they are a virulent infection that can
    completely ruin your entire test suite. As a result they need to
    be dealt with as soon as you can, before your entire deployment
    pipeline is compromised.


I'll start with expanding on their uselessness. The primary
    benefit of having automated tests is that they provide bug
    detection mechanism by acting as regression tests1. When a regression test goes red, you know
    you've got an immediate problem, often because a bug has crept
    into the system without you realizing.


1: 
    Yes, I know many advocates of TDD consider that a primary
    virtue of testing is the way it drives requirements and design. I
    agree that this is a big benefit, but I consider the regression
    suite to be the single biggest benefit that automated tests give
    us. Even without TDD tests are worth the cost for that.


Having such a bug detector has huge benefits. Most obviously it
    means that you can find and fix bugs just after they are
    introduced. Not just does this give you the warm fuzzies because
    you kill bugs quickly, it also makes it easier to remove them
    since you know the bug got in with the last set of changes that
    are fresh in your mind. As a result you know where to look for the
    bug, which is more than half the battle in squashing it.


The second level of benefit is that as you gain confidence in
    your bug detector, you gain the courage to make big changes
    knowing that when you goof, the bug detector will go off and you
    can fix the mistake quickly. 2 Without this teams are frightened to
    make the changes code needs in order to be kept clean, which leads
    to a rotting of the code base and plummeting development speed.


2: 
    Sometimes, of course, a test failure is due to a change in what
    the code is supposed to do, but the test hasn't been updated to
    reflect the new behavior. This is essentially a bug in the tests,
    but is equally easy to fix if it's caught right away.


The trouble with non-deterministic tests is that when they go
    red, you have no idea whether its due to a bug, or just part of
    the non-deterministic behavior. Usually with these tests a
    non-deterministic failure is relatively common, so you end up
    shrugging your shoulders when these tests go red. Once you start
    ignoring a regression test failure, then that test is useless and
    you might as well throw it away.3


3: 
    There is a useful role for non-deterministic tests. Tests seeded
    from a randomizer can help hunt out edge cases. Performance tests
    will always come back with different values. But these kinds of
    tests are quite different from automated regression tests, which
    are my focus here.


Indeed you really ought to throw a non-deterministic test away,
    since if you don't it has an infectious quality. If you have a
    suite of 100 tests with 10 non-deterministic tests in them, than
    that suite will often fail. Initially people will look at the
    failure report and notice that the failures are in
    non-deterministic tests, but soon they'll lose the discipline to
    do that. Once that discipline is lost, then a failure in the
    healthy deterministic tests will get ignored too. At that point
    you've lost the whole game and might as well get rid of all the
    tests.


## Quarantine


My principal aim in this article is to outline common cases
      of non-deterministic tests and how to eliminate the
      non-determinism. But before I get there I offer one piece of
      essential advice: quarantine your non-deterministic
      tests. If you have non-deterministic tests keep them in a
      different test suite to your healthy tests. That way you'll you
      can continue to pay attention to what's going on with your
      healthy tests and get good feedback from them.


Place any non-deterministic test in a quarantined
      area. (But fix quarantined tests quickly.)


Then the question is what to do with the quarantined test
      suites. They are useless as regression tests, but they do
      have a future as work items for cleaning up. You should not
      abandon such tests, since any tests you have in quarantine are
      not helping you with your regression coverage.


A danger here is that tests keep getting thrown into
      quarantine and forgotten, which means your bug detection system
      is eroding. As a result it's worthwhile to have a mechanism that
      ensures that tests don't stay in quarantine too long. I've come
      across various ways to do this. One is a simple numeric limit:
      e.g. only allow 8 tests in quarantine. Once you hit the limit
      you must spend time to clear all the tests out. This has the
      advantage of batching up your test-cleaning if that's how you
      like to do things. Another route is to put a time limit on how
      long a test may be in quarantine, such as no longer than a
      week.


The general approach with quarantine is to take the
      quarantined tests out of the main deployment pipeline so that
      you still get your regular build process. However a good team can
      be more aggressive. Our Mingle
      team puts its quarantine suite into the deployment pipeline one
      stage after its healthy tests. That way it can get the
      feedback from the healthy tests but is also forced to ensure
      that it sorts out the quarantined tests quickly. 4


4: 
    This works well for the Mingle team as they are skillful enough to
    find and fix non-deterministic tests quickly and disciplined
    enough to ensure they do it quickly. If your build remains
    broken for long due to your quarantine tests failing you will lose
    the value of continuous integration. So for most teams I'd advise
    keeping the quarantined tests out of the main pipeline.


## Lack of Isolation


In order to get tests to run reliably, you must have clear
      control over the environment in which they run, so you have a
      well-known state at the beginning of the test. If one test
      creates some data in the database and leaves it lying around, it
      can corrupt the run of another test which may rely on a
      different database state.


Therefore I find it's really important to focus on keeping
      tests isolated. Properly isolated tests can be run in any
      sequence. As you get to the larger operational scope of functional
      tests, it gets progressively harder to keep tests isolated. When
      you are tracking down a non-determinism, lack of isolation is a
      common and frustrating cause.


Keep your tests isolated from each other, so that
      execution of one test will not affect any others.


There are a couple of ways to get isolation - either always
      rebuild your starting state from scratch, or ensure that each
      test cleans up properly after itself. In general I prefer the
      former, as it's often easier - and in particular easier to find
      the source of a problem. If a test fails because it didn't build
      up the initial state properly, then it's easy to see which test
      contains the bug. With clean-up, however, one test will contain
      the bug, but another test will fail - so it's hard to find the
      real problem.


Starting from a blank state is usually easy with unit tests,
      but can be much harder with functional tests 5 - particularly if you have a lot of data
      in a database that needs to be there. Rebuilding the database
      each time can add a lot of time to test runs, so that argues for
      switching to a clean-up strategy.6


5: 
    There's no hard-and-fast definitions here, but I'm using the early
    Extreme Programming terminology of using âunit testâ to mean
    something fine-grained and âfunctional testâ as a test that's more
    end-to-end and feature related.


6: 
     One trick is to create the
     initial database and copy it using file system commands before
     opening it for each test run. File system copies are often faster
     than loading data using the database commands.


One trick that's handy when you're using databases, is to
      conduct your tests inside a transaction, and then to rollback
      the transaction at the end of the test. That way the transaction
      manager cleans up for you, reducing the chance of
      errors7.


7: 
    Of course this trick only works when you can conduct the test
    without committing any transactions.


Another approach is to do a single build of a
      mostly-immutable starting fixture before running a group of
      tests. Then ensure that the tests don't change that initial
      state (or if they do, they reverse the changes in
      tear-down). This tactic is more error-prone than rebuilding the
      fixture for each test, but it may be worthwhile iff it takes too
      long to build the fixture each time.


Although databases are a common cause for isolation problems,
      there are plenty of times you can get these in-memory too. In
      particular be aware with static data and singletons. A good
      example for this kind of problem is contextual environment, such
      as the currently logged in user.


If you have an explicit tear-down in a test, be wary of
      exceptions that occur during the tear-down. If this happens the
      test can pass, but cause isolation failures for subsequent
      tests. So ensure that if you do get a problem in a tear-down,
      it makes a loud noise.


Some people prefer to put less emphasis on isolation and more
      on defining clear dependencies to force tests to run in a
      specified order. I prefer isolation because it gives you more
      flexibility in running subsets of tests and parallelizing tests.


## Asynchronous Behavior


Asynchrony is a boon that allows you to keep software
      responsive while taking on long term tasks. Ajax calls allow a
      browser to stay responsive while going back to the server for
      more data, asynchronous message allow a server process to
      communicate with other system without being tied to their
      laggardly latency.


But in testing, asynchrony can be curse. The common mistake
      here is to throw in a sleep:


```

        //pseudo-code
        makeAsyncCall;
        sleep(aWhile);
        readResponse;
      
```


This can bite you two ways. First off you'll want to set the
      sleep time to long enough that it gives plenty of time to get
      the response. But that means that you'll spend a lot of time
      idly waiting for the response, thus slowing down your tests. The
      second bite is that, however long you sleep, sometimes it won't
      be enough. There will be some change in the environment that will
      cause you to exceed the sleep - and you'll get false failure. As
      a result I strongly urge you to never use bare sleeps
      like this.


Never use bare sleeps to wait for asynchonous
      responses: use a callback or polling.


There are basically two tactics you can do for testing an
      asynchronous response. The first is for the asynchronous service
      to take a callback which it can call when done. This is the best
      since it means you'll never have to wait any longer than you
      need to 8. The biggest problem with this is that the environment
      needs to be able to do this and then the service provider needs
      to do it. This is one of the advantages of having the
      development team integrated with testing - if they can provide a
      callback then they will.


8: 
    Although you'll still need a timeout in case you never get a reply
    - and that time out is subject to the same danger when you move to
    a different environment. Fortunately you can set that timeout to
    be pretty high, which minimizes the chances of that biting you.


The second option is to poll on the
      answer. This is more than just looking once, but looking
      regularly, something like this


```

        //pseudo-code
        makeAsyncCall
        startTime = Time.now;
        while(! responseReceived) {
          if (Time.now - startTime > waitLimit) 
            throw new TestTimeoutException;
          sleep (pollingInterval);
        }
        readResponse
      
```


The point of this approach is that you can set the
      `pollingInterval` to a pretty small value, and know that that's
      the maximum amount of dead time you'll lose to waiting for a
      response. This means you can set the `waitLimit` very
      high, which minimizes the chance of hitting it unless something
      serious has gone wrong. 9


9: 
    In that case, however the tests will run very slowly. You may want
    to consider aborting the whole test suite if you reach the
    wait limit.


Make sure you use a clear exception class that
      indicates this is a test timeout that's failing. This will help
      make it clear what's gone wrong should it happen, and perhaps
      allow a more sophisticated test harness to take account of this
      information in its display.


The time values, in particular the `waitLimit`,
      should never be literal values. Make sure they are always values
      that can be easily set in bulk, either by using constants or set
      through the runtime environment. That way if you need to tweak
      them (and you will) you can tweak them all quickly.


All this advice is handy for async calls where you expect a
      response from the provider, but how about those where there is
      no response. These are calls where we invoke a command on
      something and expect it to happen without any
      acknowledgment. This is the trickiest case since you can test
      for your expected response, but there's nothing to do to detect
      a failure other than timing-out. If the provider is something
      you're building you can handle this by ensuring the provider
      implements some way of indicating that it's done - essentially
      some form of callback. Even if only the testing code uses it,
      it's worth it - although often you'll find this kind of
      functionality is valuable for other purposes too10. If the provider is someone else's work, you
      can try persuasion, but otherwise may be stuck. Although this is
      also a case when using [Test Doubles](https://martinfowler.com/bliki/TestDouble.html) for remote services is worthwhile (which I'll
      discuss more in the next section).


10: 
      If your asynchronous behavior is triggered from the UI, it's
      often a good UI choice to have some indicator to show an
      asynchronous operation is in progress. Having this be part of
      the UI also helps testing as the hooks required to stop this
      indicator can be the same hooks as detecting when to progress
      the test logic.


If you have a general failure in something asynchronous, such
      that it's not responding at all, then you'll always be waiting
      for timeouts and your test suite will take a long time to
      fail. To combat this it's a good idea to use a smoke test to
      check that the asynchronous service is responding at all and
      stop the test run right away if it isn't.


You can also often side-step the asynchrony
      completely. Gerard Meszaros's [Humble Object
      pattern](http://xunitpatterns.com/Humble%20Object.html) says that whenever you have some logic that's in a
      hard-to-test environment, you should isolate the logic you need
      to test from that environment. In this case it means put most of
      the logic you need to test in a place where you can test it
      synchronously. The asynchronous behavior should be as minimal
      (humble) as possible, that way you don't need that much testing
      of it.


## Remote Services


Sometimes I'm asked if Thoughtworks does any integration
      work, which I find somewhat amusing since there's hardly any
      project we do that doesn't involve a fair bit of integration. By
      their nature, enterprise applications involve a great deal of
      combining data from different systems. These systems are
      maintained by other teams operating to their own schedules,
      teams that often use a very different software philosophy to our
      heavily test-driven agile approach.


Testing with such remote systems brings a number of problems,
      and non-determinism is high on the list. Often remote systems
      don't have test system we can call, which means hitting a live
      system. If there is a test system, it may not be stable enough
      to provide deterministic responses.


In this situation it's vital to ensure determinism, so it's
      time to reach for a [Test Double](https://martinfowler.com/bliki/TestDouble.html) - a component that looks like
      the remote service, but is really just a pretend version that
      mimics the remote system's behavior. The double needs to be
      setup so that it provides the right kind of response in interaction
      with our system, but in a way we control. In this manner we can
      ensure determinism.


Using a double has a downside, in particular when we are
      testing across a broad scope. How can we be sure that the double
      behaves in the same way that remote system does? We can tackle
      this again using tests, a form of test that I call 
      [Contract Tests](https://martinfowler.com/bliki/ContractTest.html). These run the same interaction with the remote
      system and the double, and check that the two match. In this
      case 'match' may not mean coming up with the same result (due to
      the non-determinisms), but results that share the same essential
      structure. Integration Contract Tests need to be run
      frequently, but not part of our system's deployment
      pipeline. Periodic running based on the rate of the change of
      the remote system is usually best.


For writing these kinds of test doubles, I'm a big fan of
      [Self Initializing Fakes](https://martinfowler.com/bliki/SelfInitializingFake.html) - since these are very simple to manage.


Some people are firmly against using [Test Doubles](https://martinfowler.com/bliki/TestDouble.html) in
      functional tests, believing that you must test with real
      connection in order to ensure end-to-end behavior. While I
      sympathize with their argument, automated tests are useless if they are
      non-deterministic. So any advantage you gain by talking to the
      real system is overwhelmed by the need to stamp out
      non-determinism11.


11: 
    There are other advantages to using a test double in these
    circumstances, even if the remote system is deterministic. Often
    response time is too slow to use a remote system. If you can only
    talk to a live system, then your tests can generate significant,
    and unappreciated, load on that system.


## Time


Few things are more non-deterministic than a call to the
      system clock. Each time you call it, you get a new result, and
      any tests that depend on it can thus change. Ask for all the
      todos due in the next hour, and you regularly get a different
      answer12.


12: 
    You could reseed your datastore for each test based on the current
    time. But that's a lot of work, and fraught with potential timing errors.


The most important thing here is to ensure that you always
      wrap the system clock with routines that can be replaced with a
      seeded value for testing. A clock stub can be set to particular
      time and frozen at that time, allowing your tests to have
      complete control over its movements. That way you can synchronize
      your test data to the values in the seeded clock.1314


13: 
    In this case the clock stub is a common way to break isolation,
    each test that uses it should ensure it's properly re-initialized.


14: 
    One of my colleagues likes to force a test run just before and
    after midnight in order to catch tests that use the current time
    and assume it's the same day an hour or two later. This is
    especially good at times like the last day of the month.


Always wrap the system clock, so it can be easily
      substituted for testing.


One thing to watch with this, is that eventually your test
      data might start having problems because it's too old, and you
      get conflicts with other time based factors in your
      application. In this case you can move the data, and your clock
      seeds to new values. When you do this, ensure that this is the
      only thing you do. That way you can be sure that any tests that
      fail are due to time-movement in the test data.


Another area where time can be a problem is when you rely on
      other behaviors from the clock. I once saw a system that
      generated random keys based on clock values. This systems
      started failing when it was moved to a faster machine that could
      allocate multiple ids within a single clock tick.15


15: 
    Although, of course, this isn't always a non-determinism bug,
    but one that's due to a change in environment. Depending on how
    close the clock ticks are to the id allocation, it could result in
    non-deterministic behavior.


I've heard so many problems due to direct calls to the system
      clock that I'd argue for finding a way to use code analysis to
      detect any direct calls to the system clock and failing the
      build right there. Even a simple regex check might save you a
      frustrating debugging session after a call at an ungodly hour.


## Resource Leaks


If your application has some kind of resource leak, this will
      lead to random tests failing, since it's just which test causes
      the resource leak to go over a limit that gets the failure. This
      case is awkward because any test can fail intermittently due to
      this problem. If it isn't a case of one test being
      non-deterministic then resource leaks are a good candidate to
      investigate.


By resource leak, I mean any resource that the application
      has to manage by acquiring and releasing. In non-memory-managed
      environments, the obvious example is memory. Memory-management
      did much to remove this problem, but other resources still need
      to be managed, such as database connections.


Usually the best way to handle these kind of resources is through
      a [Resource Pool](https://martinfowler.com/bliki/ResourcePool.html). If you do this then a good
      tactic is to configure the pool to a size of 1 and make it throw
      an exception should it get a request for a resource when it has
      none left to give. That way the first test to request a resource
      after the leak will fail - which makes it a lot easier to find
      the problem test.


This idea of limiting resource pool sizes, is about
      increasing constraints to make errors more likely to crop up in
      tests. This is good because we want errors to show in tests so
      we can fix them before they manifest themselves in
      production. This principle can be used in other ways too. One
      story I heard was of a system which generated randomly named
      temporary files, didn't clean them up properly, and crashed on a
      collision. This kind of bug is very hard to find, but one way to
      manifest it is to stub the randomizer for testing so it always
      returns the same value. That way you can surface the problem
      more quickly.


---
