---
title: "Self Initializing Fake"
description: "One of the classic cases for using aTestDoubleis   when you call a remote service. Remote services are usually slow and   often unreliable, so using a double is a good way to make your tests   faster "
date: 2009-08-04T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/SelfInitializingFake.html
slug: SelfInitializingFake
word_count: 426
---


One of the classic cases for using a [TestDouble](https://martinfowler.com/bliki/TestDouble.html) is
  when you call a remote service. Remote services are usually slow and
  often unreliable, so using a double is a good way to make your tests
  faster and more stable.


When you're querying a remote service, you need to find a way to
  load the expected data into your double. One way to do this is to
  use what I'm dubbing a self-initializing fake. The basic plan is
  simple. The first time you call the fake it passes the call onto
  the actual remote service, and as it returns the data it takes and
  saves a copy. Further calls just return the copy. In a sense this is
  like a cache, but with the important difference that there is no
  attempt to handle cache invalidation, which is handy as that's one
  of the [TwoHardThings](https://martinfowler.com/bliki/TwoHardThings.html).


![](images/selfInitializingFake/mainCommDiag.png)


I've called this a fake, as that seems the closest fit from the
  various varieties of test doubles. The other reasonable alternative
  is a stub, but the distinction here is that a stub needs setting up
  when you build the fixture, while fakes are autonomous.


The interesting thing about a self-initializing fake is how you deal
  with situations where the remote service changes its response.


One time I saw this approach was with a database controlled by
  another application. In this case the data did change,
  frequently. This is unhelpful for tests, because automated tests
  rely on getting the same answers to the same questions. But usually
  tests don't care whether the data is up to date or not, so saving an
  old value worked just fine.


I ran into this again recently while chatting with my colleague
  Josh Price. In his case the remote data was supposedly static, but
  occasionally there were changes, which would imply that the system
  he was developing needed to change - usually to handle formatting
  issues. In this case he had a special test suite that would get all
  self-initializing fakes to call the remote service and check that they
  returned the same value that was saved.


In this case early stages of their build pipeline ran against the
  fake, and the last (slowest) stage ran against the service
  itself. One interesting problem was that the remote service required
  some unimportant parameters which changed from call to call but
  didn't alter the results. These were stripped out of the URL when
  the fake looked the values up from the store.


(Thanks to Josh Price, Darren Cotterill, and Gerard Meszaros for
  their help with this piece.)
