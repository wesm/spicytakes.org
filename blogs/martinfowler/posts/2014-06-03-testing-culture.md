---
title: "Goto Fail, Heartbleed, and Unit Testing Culture"
description: "Two computer security flaws were discovered in early 2014: Apple’s “goto     fail” bug and OpenSSL’s “Heartbleed” bug. Both had the potential for     widespread and severe security failures, the full "
date: 2014-06-03T00:00:00
tags: ["testing"]
url: https://martinfowler.com/articles/testing-culture.html
slug: testing-culture
word_count: 26052
---


At the beginning of 2014 the security of the Internet was
    rocked by two serious flaws: Apple’s “goto fail” bug
    ([CVE-2014-1266](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-1266)) and OpenSSL’s
    “Heartbleed” bug ([CVE-2014-0160](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)). Both
    were vulnerabilities in the Secure Sockets Layer technology upon
    which the majority of secure communications on the Internet
    relies. These bugs are as instructive as they were devastating: They
    were rooted in the same programmer optimism, overconfidence, and
    haste that strike projects of all sizes and domains.


These bugs arouse my passion because I've seen and lived the
    benefits of unit testing, and this strongly-imprinted experience
    compels me to reflect on how unit testing approaches could prevent
    defects as high-impact and high-profile as these SSL bugs. Unit
    testing is the process of looking for chunks of code that make for
    convenient “units” to which to apply automated [Unit Tests](https://martinfowler.com/bliki/UnitTest.html), small programs designed to verify
    low-level implementation details and detect coding errors early.
    The nature of the defects inspired me to write my own proof-of-concept
    unit tests to reproduce the errors and verify their fixes. I wrote
    these tests to validate my intuition, and to demonstrate to others
    how unit tests could have detected these defects early and without
    heroic effort.


Writing unit tests produces benefits beyond detecting low-level
    coding errors. In this article, I explore the question of whether
    unit testing could have helped prevent the âgoto failâ and
    Heartbleed bugs. In doing so, I hope to establish a compelling
    case for the adoption of unit testing as part of everyday
    development, so that the experience of [Self Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html) becomes universal. I offer my insights in
    the hope that they may help avoid similar failures in the future,
    in the spirit of a [postmortem](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=526833) or
    [project retrospective](https://www.amazon.com/gp/product/0932633447/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0932633447&linkCode=as2&tag=martinfowlerc-20). My
    experience doesn't mean I'm owed deference based on [mah authoritah](http://www.southparkstudios.com/clips/150368/you-will-respect-my-authoritah), but I hope to make a sufficiently
    compelling case that will lead more people and organizations to consider
    the benefits of a unit-testing culture.


Many popular and technical media stories have run with
    explanations of how these defects originated, why they slipped past
    existing safeguards before being so widely deployed, and what
    should be done to prevent such bugs from happening again. It
    troubles me that most of these analyses fall back on facile
    excuses that miss the mark, and promote resigned acceptance of
    such defects due to the ever-increasing complexity of modern
    software systems. It is as though the software industry at large,
    as well as the public that depends on it, is anxious to accept
    such failures as inevitable fate, the price we pay for the modern
    conveniences that technology affords us. It's the easiest possible
    explanation that allows us to make sense of a bad situation and
    move on as a society.


I don't accept such defects as inevitable. Rather, we must
    seize this opportunity to reflect on how we developers can do far
    better than rely on fate, or more funding, or any number of
    external factors to prevent security vulnerabilities or other
    high-impact defects caused by low-level coding errors. Bugs will
    happen, but neither software developers nor the public should be
    satisfied with that as a response to defects this colossal in
    scope. Deep, genuine reflection is difficult and encounters a lot
    of resistance, as it calls on developers to accept responsibility
    for their human limitations—which is often a challenge to the very
    self-image of a programmer. That makes it all the more important
    to dive deeply into these two bugs in particular, to search for
    genuine solutions and to avoid setting a dangerous precedent: If
    everything in the short-term turns out OK in the wake of âgoto
    failâ and Heartbleed, then why bother changing anything about
    current software development practices?


## goto fail


The “goto fail” bug first shipped to iPhones, iPads, and
      AppleTVs in September 2012, appeared in iOS 7.0 and OS X
      Mavericks, and was not fixed until February 2014—seventeen
      months after it was introduced. A short-circuit skipping the
      final step of the SSL/TLS handshake algorithm left users
      vulnerable to a man-in-the-middle attack, whereby a malicious
      system relaying traffic between an affected system and another
      system could present the illusion of a secure connection using
      false credentials, and subsequently intercept all communications
      between the other two systems.


The bug earned its name from this now infamous code
      snippet:


```
if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
    goto fail;
    goto fail;

```


Some have argued that all goto statements are bad, based on
      Edsger Dijkstra's famous essay [A Case against
      the GO TO Statement](http://www.cs.utexas.edu/users/EWD/ewd02xx/EWD215.PDF), summarized by the popular axiom âGoto
      [considered harmful](http://en.wikipedia.org/wiki/Considered_harmful)â. However, the
      `goto fail` statement expresses an idiom familiar to C
      programmers. In the case of an unrecoverable error, such statements pass
      control immediately to a recovery block at the end of a function, where
      locally-allocated resources are properly released. Other languages
      have built-in support for such “abortion clauses”, as Dijkstra
      called them in the conclusion to his essay: destructors in C++;
      `try/catch/finally` in Java;
      `defer()/panic()/recover()` in Go;
      `try/except/finally` and the `with`
      statement in Python. In C, there is no essential problem with or
      confusion surrounding the use of `goto` in this
      context. In other words, `goto` should not be considered
      harmful here.


C programmers will also immediately recognize that the first
      `goto fail` statement is bound to the result of the
      `if` statement preceding it, but the second `goto
      fail` is not: The matching indentation of the two statements
      bears no significance in C, as surrounding curly braces are required
      to bind more than one statement to an `if` condition. If
      the first `goto fail` is not executed, the second one
      certainly will be. This means that subsequent steps of the handshake
      algorithm will never be executed, but any exchange successfully
      passing this point will always produce a successful return value even
      if the final verification step would have failed. More plainly: The
      algorithm gets short-circuited by the extra `goto fail`
      statement.


Some have claimed that a coding style requiring the use of
      curly braces for all `if` statements or enabling
      unreachable-code compiler warnings could have helped. However, there
      are deeper problems with the code that unit testing could help to
      resolve.


### How Could Unit Testing Have Helped?


While looking for “units” to which to apply “unit” tests,
        the entire block of code containing the buggy algorithm, with
        its cluster of conditional logic, leaps out as such a unit
        (from the `SSLVerifySignedServerKeyExchange()` function
        in [version 55471 of Apple’s Secure
        Transport library](http://opensource.apple.com/source/Security/Security-55471/libsecurity_ssl/lib/sslKeyExchange.c)):


```
if ((err = ReadyHash(&SSLHashSHA1, &hashCtx)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &clientRandom)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &serverRandom)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
    goto fail;
    goto fail;
if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)
    goto fail;

```


Such a block of code is easier to test when extracted into its
        own function. Extracting chunks of code like this is habitual practice
        for people writing unit tests and can help get parts of an existing
        code base under test a piece at a time. Looking closely at the
        variables and data types used in the algorithm make it clear that
        this block of code is performing a handshake on the hashes. By looking
        up the type of `SSLHashSHA1`, we can also see that it is an
        instance of a `HashReference` “[jump
        table](http://stackoverflow.com/questions/48017/what-is-a-jump-table)”, a structure containing function pointers that enables C
        programmers to implement virtual function-like behavior (i.e.
        [substitutability](http://en.wikipedia.org/wiki/Liskov_substitution_principle) and run-time polymorphism).
        We can extract this operation into a function with a name signifying
        its intent (leaving out the extra `goto fail`):


```
static OSStatus
HashHandshake(const HashReference* hashRef, SSLBuffer* clientRandom,
    SSLBuffer* serverRandom, SSLBuffer* exchangeParams,
    SSLBuffer* hashOut) {
  SSLBuffer hashCtx;
  OSStatus err = 0;
  hashCtx.data = 0;
  if ((err = ReadyHash(hashRef, &hashCtx)) != 0)
    goto fail;
  if ((err = hashRef->update(&hashCtx, clientRandom)) != 0)
    goto fail;
  if ((err = hashRef->update(&hashCtx, serverRandom)) != 0)
    goto fail;
  if ((err = hashRef->update(&hashCtx, exchangeParams)) != 0)
    goto fail;
  err = hashRef->final(&hashCtx, hashOut);
fail:
  SSLFreeBuffer(&hashCtx);
  return err;
}

```


Now the series of statements comprising the previously buggy
        algorithm can be replaced by:


```
if ((err = HashHandshake(&SSLHashSHA1, &clientRandom, &serverRandom,
     &signedParams, &hashOut)) != 0) {
  goto fail;
}

```


This function is more easily understood in isolation. Faced
        with such a self-contained function like this, a programmer can begin
        to focus on the external effects of the code, considering questions
        such as:

- What is the contract fulfilled by the code under test?
- What preconditions are required, and how are they enforced?
- What postconditions are guaranteed?
- What example inputs trigger different behaviors?
- What set of tests will trigger each behavior and
          validate each guarantee?


In the case of `HashHandshake()`, the contract can be
        described as: Five steps, all must pass. Success or failure is
        propagated to the caller by the return value. The
        `HashReference` is expected to respond correctly to the
        series of calls; whether it makes use of any functions or data beyond
        that passed in by `HashHandshake()` is an implementation
        detail opaque to `HashHandshake()` itself.


For an algorithm this straightforward, the test cases will rather
        closely âmirrorâ the implementation: One success case, five failure
        cases. For higher-level or more complex operations, such close
        âmirroringâ can make for brittle tests and should generally be
        avoided. This is especially important to keep in mind when using mocks
        or other [Test Doubles](https://martinfowler.com/bliki/TestDouble.html) to test code in
        isolation from its collaborators.


It's arguably even more important to test that the code
        doesn't do what it shouldn't do.


Regardless of the scope of the code under test, it's critical to
        exhaustively test failure cases to the extent possible. It is tempting
        to test that the code does what it should do and leave it at that, but
        it's arguably even more important to test that it doesn't do what it
        shouldn't do.


### Proof-of-Concept Unit Test


Despite the fact that C is not an object-oriented programming
        language, the existing code for this algorithm exhibits a clearly
        object-oriented design that actually makes for easy unit testing once
        the code is extracted into its own function. The
        [`tls_digest_test.c`](http://goo.gl/PBt9S7)
        proof-of-concept unit test shows how a `HashReference`
        stub can be used to effectively cover every path through the
        extracted `HashHandshake()` algorithm. The actual test
        cases look like this:


```
static int TestHandshakeSuccess() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = SUCCESS;
  return ExecuteHandshake(fixture);
}

static int TestHandshakeInitFailure() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = INIT_FAILURE;
  fixture.ref.init = HashHandshakeTestFailInit;
  return ExecuteHandshake(fixture);
}

static int TestHandshakeUpdateClientFailure() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = UPDATE_CLIENT_FAILURE;
  fixture.client = FAIL_ON_EVALUATION(UPDATE_CLIENT_FAILURE);
  return ExecuteHandshake(fixture);
}

static int TestHandshakeUpdateServerFailure() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = UPDATE_SERVER_FAILURE;
  fixture.server = FAIL_ON_EVALUATION(UPDATE_SERVER_FAILURE);
  return ExecuteHandshake(fixture);
}

static int TestHandshakeUpdateParamsFailure() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = UPDATE_PARAMS_FAILURE;
  fixture.params = FAIL_ON_EVALUATION(UPDATE_PARAMS_FAILURE);
  return ExecuteHandshake(fixture);
}

static int TestHandshakeFinalFailure() {
  HashHandshakeTestFixture fixture = SetUp(__func__);
  fixture.expected = FINAL_FAILURE;
  fixture.ref.final = HashHandshakeTestFailFinal;
  return ExecuteHandshake(fixture);
}

```


The `HashHandshakeTestFixture` holds all the variables
        needed as input to the code under test and to check the expected
        outcome:


```
typedef struct
{
    HashReference ref;
    SSLBuffer *client;
    SSLBuffer *server;
    SSLBuffer *params;
    SSLBuffer *output;
    const char *test_case_name;
    enum HandshakeResult expected;
} HashHandshakeTestFixture;

```


`SetUp()` initializes all of the members of a
        `HashHandshakeTestFixture` to default values; each test
        case overrides only those members pertinent to that specific test
        case:


```
static HashHandshakeTestFixture SetUp(const char *test_case_name) {
  HashHandshakeTestFixture fixture;
  memset(&fixture, 0, sizeof(fixture));
  fixture.ref = SSLHashNull;
  fixture.ref.update = HashHandshakeTestUpdate;
  fixture.test_case_name = test_case_name;
  return fixture;
}

```


`ExecuteHandshake()` executes the
        `HashHandshake()` function and evaluates the outcome,
        printing an error message and returning an error value if the outcome
        differs from what was expected:


```
/* Executes the handshake and returns zero if the result matches expected, one
 * otherwise. */
static int ExecuteHandshake(HashHandshakeTestFixture fixture) {
  const enum HandshakeResult actual = HashHandshake(
      &fixture.ref, fixture.client, fixture.server, fixture.params,
      fixture.output);

  if (actual != fixture.expected) {
    printf("%s failed: expected %s, received %s\n", fixture.test_case_name,
           HandshakeResultString(fixture.expected),
           HandshakeResultString(actual));
    return 1;
  }
  return 0;
}

```


Adding a duplicate `goto fail` statement anywhere in the
        `HashHandshake()` algorithm before the `final()`
        call will cause the test to fail.


This test was written without a testing framework, to demonstrate
        that an effective test can be written using tools already in-use by a
        project. Even without referencing a standard framework, the
        explanation in the preceding paragraph should prove relatively easy to
        follow: Well-organized test cases using well-organized objects and
        functions with well-chosen names mean that if a test fails, you can
        usually diagnose the failure from the information in the test case
        alone without digging through the full implementation of the test
        program. Testing frameworks can help in writing tests more
        efficiently, but are not a prerequisite for writing well-organized,
        thorough unit tests.


Writing a set of tests to exercise this function is straightforward
        because now we’re thinking about concrete examples rather than
        conditions. Furthermore, the tests act as a double-check: It’s easy to
        make a mistake with conditional logic, accidentally reversing
        one test in the chain; but when you write tests you are stating the
        behavior twice, once with examples, once with logic. You have to make
        the same mistake in two different representations for a bug to get
        through.


It’s likely that the programmer who wrote this algorithm the first
        time did execute the program to check for errors in the new code. Most
        programmers will run a program with some sample inputs to verify that
        it’s doing what they think it should do. The problem is that these
        runs are often ephemeral and thrown away once the code is working; an
        automated test captures those runs as a permanent double-check.


That permanent double-check is important here: We don’t know
        exactly how that rogue second `goto fail` got into the
        code; [a likely reason is that it was
        the result of a large merge operation.](https://gist.github.com/alexyakoubian/9151610/66bd7797572db0a353a16e03933c45523a7d5d93)
        When merging a branch into the mainline, large differences can
        result. Even if a merge compiles, it can still introduce
        errors. Inspecting such merge differences can be time-consuming,
        tedious, and error-prone, even for experienced developers. In this
        case the automated double-check provided by unit tests provides a fast
        and painstaking (yet painless!) code review, in the sense that the
        tests will likely catch potential merge errors before a human
        inspects the merged code. It’s unlikely the original author
        introduced the âgoto failâ bug into the code, but a suite of tests
        doesn’t just help you find your own mistakes: It helps reveal
        mistakes made by programmers far into the future.


In the case of the “goto fail” bug, the unit testing habit of
        looking for, and extracting, testable functions has a second
        benefit.


### Déjà Vu All Over Again


A copy of the same algorithm with a different
        `HashReference` instance appears immediately above the
        buggy algorithm in the same function. In total, the algorithm appears
        six different times in the same file
        ([sslKeyExchange.c from
        Security-55471](http://opensource.apple.com/source/Security/Security-55471/libsecurity_ssl/lib/sslKeyExchange.c)):

- twice in `SSLVerifySignedServerKeyExchange()`, which
              contained the bug
- once in
              `SSLVerifySignedServerKeyExchangeTls12()`
- twice in `SSLSignServerKeyExchange()`
- once in `SSLSignServerKeyExchangeTls12()`


The [updated version of
        sslKeyExchange.c in Security-55471.14](http://opensource.apple.com/source/Security/Security-55471.14/libsecurity_ssl/lib/sslKeyExchange.c) has eliminated the
        duplicated `goto fail` statement from
        `SSLVerifySignedServerKeyExchange()`, but the duplicated
        algorithm remains.


Code duplication is a [Code Smell](https://martinfowler.com/bliki/CodeSmell.html) that is known
        to increase the likelihood of software errors. It is also apparent
        from the function names above that there’s more duplication besides
        that of the core handshake algorithm. This cut-and-paste code reuse
        also supports the hypothesis that the bug might have been caused by a
        large merge operation, as duplicate code increases the available “code
        surface” during merges and compounds the potential for undetected
        merge errors.


Unit testing introduces pressure to minimize copy/paste, because
        the copy/pasted code also has to be unit tested. It could have ensured
        that only one copy of this algorithm existed since it would have been
        easier to test. A unit test could have easily verified that this
        algorithm was correct, merge or no, and could have prevented the “goto
        fail” bug from being written in the first place.


Also, the [Security-55471 version of
        ssl_regressions.h](http://opensource.apple.com/source/Security/Security-55471/libsecurity_ssl/regressions/ssl_regressions.h), which appears to list a number of SSL
        regression tests for this library, remains unchanged in the
        [Security-55471.14 version of
        ssl_regressions.h](http://opensource.apple.com/source/Security/Security-55471.14/libsecurity_ssl/regressions/ssl_regressions.h). The only substantial difference between the
        two versions of the library is the deletion of the `goto
        fail` statement itself, with no added tests or eliminated
        duplication:


```
$ curl -O http://opensource.apple.com/tarballs/Security/Security-55471.tar.gz
$ curl -O http://opensource.apple.com/tarballs/Security/Security-55471.14.tar.gz
$ for f in Security-55471{,.14}.tar.gz; do gzip -dc $f | tar xf - ; done
# Since diff on OS X doesn't have a --no-dereference option:
$ find Security-55471* -type l | xargs rm
$ diff -uNr Security-55471{,.14}/libsecurity_ssl
diff -uNr Security-55470/libsecurity_ssl/lib/sslKeyExchange.c
Security-55471.14/libsecurity_ssl/lib/sslKeyExchange.c
--- Security-55471/libsecurity_ssl/lib/sslKeyExchange.c 2013-08-09
20:41:07.000000000 -0400
+++ Security-55471.14/libsecurity_ssl/lib/sslKeyExchange.c      2014-02-06
22:55:54.000000000 -0500
@@ -628,7 +628,6 @@
         goto fail;
     if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
         goto fail;
-        goto fail;
     if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)
         goto fail;

diff -uNr Security-55471/libsecurity_ssl/regressions/ssl-43-ciphers.c
Security-55471.14/libsecurity_ssl/regressions/ssl-43-ciphers.c
--- Security-55471/libsecurity_ssl/regressions/ssl-43-ciphers.c 2013-10-11
17:56:44.000000000 -0400
+++ Security-55471.14/libsecurity_ssl/regressions/ssl-43-ciphers.c
2014-03-12 19:30:14.000000000 -0400
@@ -85,7 +85,7 @@
     { OPENSSL_SERVER, 4000, 0, false}, //openssl s_server w/o client side
auth
     { GNUTLS_SERVER, 5000, 1, false}, // gnutls-serv w/o client side auth
     { "www.mikestoolbox.org", 442, 2, false}, // mike's  w/o client side auth
-//    { "tls.secg.org", 40022, 3, false}, // secg ecc server w/o client side
auth - This server generate DH params we dont support.
+//    { "tls.secg.org", 40022, 3, false}, // secg ecc server w/o client side
auth

     { OPENSSL_SERVER, 4010, 0, true}, //openssl s_server w/ client side auth
     { GNUTLS_SERVER, 5010, 1, true}, // gnutls-serv w/ client side auth

```


### Cultural Implications


The presence of six separate copies of the same algorithm clearly
        indicates that this bug was not due to a one-time programmer error:
        This was a pattern. This is evidence of a development culture that
        tolerates duplicated, untested code.


I've never worked at Apple, nor do I know any Apple developers. I
        don't know exactly what the company-wide development culture is there,
        and whether this code is representative or exceptional. Even if this
        code is the exception rather than the norm, it's still unacceptable.
        It doesn't matter to me, as someone whose privacy and security
        might've been violated by this coding error, what the circumstances
        were âexcusingâ this particular error or what the rest of the culture
        looks like. I want to see greater accountability for such mistakes.
        Not shaming, not condemnation, etc., but accountability and the due
        diligence that follows it. That's the deeper strategy for how we
        prevent the next âgoto failâ from happening.


I do know that development cultures can change. Bugs such as these
        give us an occasion to reflect upon our own development cultures, if
        unit testing is not already a vital part, and begin to appreciate why
        unit testing is such an important development practice. I'll discuss
        my experience with changing a development culture in detail in a later
        section of this article, and offer advice for how to effect change in
        other development cultures, from a single team to an entire
        company.


My proof-of-concept unit test for âgoto failâ may be easy to
        dismiss as a one-off test written with 20/20 hindsight. I would
        rather it appear as an example of the kind of accessible unit testing
        approach that development teams everywhere can apply to existing code,
        right now, to avoid similarly embarrassing (and potentially
        catastrophic) bugs. A development culture that values unit testing and
        whose members work to improve their craft will produce tests that will
        most likely catch programming errors exactly like âgoto failâ long
        before they have a chance to impact any users.


Next, let's take a look at the
        Heartbleed bug to examine how unit testing might've been applied in
        that context.


## Heartbleed


Heartbleed was a similarly heartbreaking case of untested
      security-critical code which appeared as part of the ubiquitous
      OpenSSL library. It was introduced in January 2012 as part of
      [a large, untested change implementing
      TLS heartbeats in OpenSSL-1.0.1-beta1](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=4817504d069b4c5082161b02a22116ad75f822b1). The bug enabled an
      attacker to send an empty
      handshake request and declare that it sent up to 64k of data; a
      vulnerable system would read but not verify the declared size and
      would respond with whatever contents resided in up to 64k of its
      memory adjacent to the request buffer. There was no logging of this
      exchange; there would be absolutely no trace of the attack.


The change introducing the bug was code reviewed; it is apparent
      that the reviewer did not insist that the change include unit tests.
      The bug was not discovered and fixed until April 2014 and released
      as part of 1.0.1g.


It appeared in both `dtls1_process_heartbeat()`
      (`ssl/d1_both.c`) and
      `tls1_process_heartbeat()`
      (`ssl/t1_lib.c`):


```
int
dtls1_process_heartbeat(SSL *s)
  {
  unsigned char *p = &s->s3->rrec.data[0], *pl;
  unsigned short hbtype;
  unsigned int payload;
  unsigned int padding = 16; /* Use minimum padding */

```


The local pointer variable `*p` is initialized to
      the beginning of the heartbeat request buffer. The first byte will
      identify the type of the request, to be stored in `hbtype`.
      The next two bytes specify the client-supplied size of the request data
      that the client expects to be copied and sent back as the response; this
      size will be stored in `payload`. (`payload_size`
      or `payload_len` would’ve been a better name to match
      the variable's intent.) Following that is the beginning of the
      client-supplied data, or “payload”, to be copied and returned to the
      client, which will be pointed to by `pl`. (*This*
      variable should’ve been named `payload`.)


The data is read into the corresponding variables:


```
/* Read type and payload length first */
hbtype = *p++;
n2s(p, payload);
pl = p;
```


`n2s()` is a macro (from `ssl/ssl_locl.h`) that
      reads the next two bytes of the pointer `p`, stores the value
      in `payload`, and advances `p` by two bytes.


Provided `hbtype` is `TLS1_HB_REQUEST`, the
      affected system then allocates a response buffer and copies
      `payload` bytes into it (`s2n()` is the companion
      macro to `n2s()` that copies the payload length into the
      response buffer):


```
unsigned char *buffer, *bp;
int r;

/* Allocate memory for the response, size is 1 byte
 * message type, plus 2 bytes payload length, plus
 * payload, plus padding
 */
buffer = OPENSSL_malloc(1 + 2 + payload + padding);
bp = buffer;

/* Enter response type, length and copy payload */
*bp++ = TLS1_HB_RESPONSE;
s2n(payload, bp);
memcpy(bp, pl, payload);
```


The `memcpy()` is bad because the length value,
      `payload`, is not verified as matching the length of what was
      actually read from the request. The request could have contained the
      empty string, but indicated a length up to 64 kilobytes. As a result, up
      to 64 kilobytes of the process's memory are returned as a response, not
      the contents of the request buffer. Again, there is no logging of this
      event; it literally leaves no trace.


The fix provides the missing checks on the buffer size:


```
/* Read type and payload length first */
if (1 + 2 + 16 > s->s3->rrec.length)
  return 0; /* silently discard */
hbtype = *p++;
n2s(p, payload);
if (1 + 2 + payload + 16 > s->s3->rrec.length)
  return 0; /* silently discard per RFC 6520 sec. 4 */
pl = p;
```


The first check covers the case where the client has sent the empty
      string as a payload, making sure the actual size of the data read from
      the socket matches this minimum request size; the second ensures the
      client-supplied payload size does not exceed that of the buffer
      containing the payload data.


In `dtls1_process_heartbeat()`, a check was added to
      confirm that the payload size does not exceed the maximum allowed for
      the response:


```
unsigned int write_length = 1 /* heartbeat type */ +
          2 /* heartbeat length */ +
          payload + padding;
int r;

if (write_length > SSL3_RT_MAX_PLAIN_LENGTH)
  return 0;
```


### How Could Unit Testing Have Helped?


As opposed to the case of the “goto fail” bug, there is no need
        to extract a new function: both `dtls1_process_heartbeat()`
        and `tls1_process_heartbeat()` are already good-sized units
        that don’t require a large amount of complicated setup to get under
        test. We can get right to the same questions posed earlier in the
        context of “goto fail”:

- What is the contract fulfilled by the code under test?
- What preconditions are required, and how are they enforced?
- What postconditions are guaranteed?
- What example inputs trigger different behaviors?
- What set of tests will trigger each behavior and
          validate each guarantee?


Given that the heartbeat functions process request buffers
        containing externally-supplied data, a programmer accustomed to
        self-testing would find it habitual to probe for weaknesses in
        handling such input—especially as it pertains to the reading and
        allocation of memory buffers.


In addition to this natural unit tester's instinct, here's an excerpt
        from [the section of the protocol defining the
        heartbeat request](https://tools.ietf.org/html/rfc6520#section-4):


```
payload_length:  The length of the payload.

[...snip...]

If the payload_length of a received HeartbeatMessage is too large,
the received HeartbeatMessage MUST be discarded silently.
```


In this case, the protocol spec practically defines the appropriate
        unit test for us. It doesn't explicitly say that there should be
        verification that `payload_length` match what is actually
        read, but provides a strong hint that `payload_length`
        should receive special attention.


### Proof of Concept Unit Test


The
        [`heartbleed_test.c`](http://goo.gl/w1bGyR)
        proof-of-concept unit test is a bit more involved than that of
        “goto fail”, but still follows a similar structure. Here are
        the test cases for `dtls1_process_heartbeat()`:


```
static int TestDtls1NotBleeding() {
  HeartbleedTestFixture fixture = SetUpDtls(__func__);
  /* Three-byte pad at the beginning for type and payload length */
  unsigned char payload_buf[] = "   Not bleeding, sixteen spaces of padding"
          "                ";
  const int payload_buf_len = HonestPayloadSize(payload_buf);

  fixture.payload = &payload_buf[0];
  fixture.sent_payload_len = payload_buf_len;
  fixture.expected_return_value = 0;
  fixture.expected_payload_len = payload_buf_len;
  fixture.expected_return_payload = "Not bleeding, sixteen spaces of padding";
  return ExecuteHeartbeat(fixture);
}

static int TestDtls1NotBleedingEmptyPayload() {
  HeartbleedTestFixture fixture = SetUpDtls(__func__);
  /* Three-byte pad at the beginning for type and payload length, plus a NUL
   * at the end */
  unsigned char payload_buf[4 + kMinPaddingSize];
  memset(payload_buf, ' ', sizeof(payload_buf));
  payload_buf[sizeof(payload_buf) - 1] = '\0';
  const int payload_buf_len = HonestPayloadSize(payload_buf);

  fixture.payload = &payload_buf[0];
  fixture.sent_payload_len = payload_buf_len;
  fixture.expected_return_value = 0;
  fixture.expected_payload_len = payload_buf_len;
  fixture.expected_return_payload = "";
  return ExecuteHeartbeat(fixture);
}

static int TestDtls1Heartbleed() {
  HeartbleedTestFixture fixture = SetUpDtls(__func__);
  /* Three-byte pad at the beginning for type and payload length */
  unsigned char payload_buf[] = "   HEARTBLEED                ";

  fixture.payload = &payload_buf[0];
  fixture.sent_payload_len = kMaxPrintableCharacters;
  fixture.expected_return_value = 0;
  fixture.expected_payload_len = 0;
  fixture.expected_return_payload = "";
  return ExecuteHeartbeat(fixture);
}

static int TestDtls1HeartbleedEmptyPayload() {
  HeartbleedTestFixture fixture = SetUpDtls(__func__);
  /* Excluding the NUL at the end, one byte short of type + payload length +
   * minimum padding */
  unsigned char payload_buf[kMinPaddingSize + 3];
  memset(payload_buf, ' ', sizeof(payload_buf));
  payload_buf[sizeof(payload_buf) - 1] = '\0';

  fixture.payload = &payload_buf[0];
  fixture.sent_payload_len = kMaxPrintableCharacters;
  fixture.expected_return_value = 0;
  fixture.expected_payload_len = 0;
  fixture.expected_return_payload = "";
  return ExecuteHeartbeat(fixture);
}

static int TestDtls1HeartbleedExcessivePlaintextLength() {
  HeartbleedTestFixture fixture = SetUpDtls(__func__);
  /* Excluding the NUL at the end, one byte in excess of maximum allowed
   * heartbeat message length */
  unsigned char payload_buf[SSL3_RT_MAX_PLAIN_LENGTH + 2];
  memset(payload_buf, ' ', sizeof(payload_buf));
  payload_buf[sizeof(payload_buf) - 1] = '\0';

  fixture.payload = &payload_buf[0];
  fixture.sent_payload_len = HonestPayloadSize(payload_buf);
  fixture.expected_return_value = 0;
  fixture.expected_payload_len = 0;
  fixture.expected_return_payload = "";
  return ExecuteHeartbeat(fixture);
}

```


The `HeartbleedTestFixture`, `SetupDtls()`,
        and `ExecuteHeartbeat()` items correspond closely to
        similar items in the “goto fail” proof-of-concept unit test:


```
typedef struct {
  SSL_CTX *ctx;
  SSL *s;
  const char* test_case_name;
  int (*process_heartbeat)(SSL* s);
  unsigned char* payload;
  int sent_payload_len;
  int expected_return_value;
  int return_payload_offset;
  int expected_payload_len;
  const char* expected_return_payload;
} HeartbleedTestFixture;

static HeartbleedTestFixture SetUp(const char* const test_case_name,
    const SSL_METHOD* meth) {
  HeartbleedTestFixture fixture;
  int setup_ok = 1;
  memset(&fixture, 0, sizeof(fixture));
  fixture.test_case_name = test_case_name;

  fixture.ctx = SSL_CTX_new(meth);
  if (!fixture.ctx) {
    fprintf(stderr, "Failed to allocate SSL_CTX for test: %s\n",
            test_case_name);
    setup_ok = 0;
    goto fail;
  }

  /* snip other allocation and error handling blocks */

fail:
  if (!setup_ok) {
    ERR_print_errors_fp(stderr);
    exit(EXIT_FAILURE);
  }
  return fixture;
}

static HeartbleedTestFixture SetUpDtls(const char* const test_case_name) {
  HeartbleedTestFixture fixture = SetUp(test_case_name,
                                        DTLSv1_server_method());
  fixture.process_heartbeat = dtls1_process_heartbeat;

  /* As per dtls1_get_record(), skipping the following from the beginning of
   * the returned heartbeat message:
   * type-1 byte; version-2 bytes; sequence number-8 bytes; length-2 bytes
   *
   * And then skipping the 1-byte type encoded by process_heartbeat for
   * a total of 14 bytes, at which point we can grab the length and the
   * payload we seek.
   */
  fixture.return_payload_offset = 14;
  return fixture;
}

static HeartbleedTestFixture SetUpTls(const char* const test_case_name) {
  HeartbleedTestFixture fixture = SetUp(test_case_name,
                                        TLSv1_server_method());
  fixture.process_heartbeat = tls1_process_heartbeat;
  fixture.s->handshake_func = DummyHandshake;

  /* As per do_ssl3_write(), skipping the following from the beginning of
   * the returned heartbeat message:
   * type-1 byte; version-2 bytes; length-2 bytes
   *
   * And then skipping the 1-byte type encoded by process_heartbeat for
   * a total of 6 bytes, at which point we can grab the length and the payload
   * we seek.
   */
  fixture.return_payload_offset = 6;
  return fixture;
}

static void TearDown(HeartbleedTestFixture fixture) {
  ERR_print_errors_fp(stderr);
  SSL_free(fixture.s);
  SSL_CTX_free(fixture.ctx);
}

static int ExecuteHeartbeat(HeartbleedTestFixture fixture) {
  int result = 0;
  SSL* s = fixture.s;
  unsigned char *payload = fixture.payload;
  unsigned char sent_buf[kMaxPrintableCharacters + 1];

  s->s3->rrec.data = payload;
  s->s3->rrec.length = strlen((const char*)payload);
  *payload++ = TLS1_HB_REQUEST;
  s2n(fixture.sent_payload_len, payload);

  /* Make a local copy of the request, since it gets overwritten at some
   * point */
  memcpy((char *)sent_buf, (const char*)payload, sizeof(sent_buf));

  int return_value = fixture.process_heartbeat(s);

  if (return_value != fixture.expected_return_value) {
    printf("%s failed: expected return value %d, received %d\n",
           fixture.test_case_name, fixture.expected_return_value,
           return_value);
    result = 1;
  }

  /* If there is any byte alignment, it will be stored in wbuf.offset. */
  unsigned const char *p = &(s->s3->wbuf.buf[
      fixture.return_payload_offset + s->s3->wbuf.offset]);
  int actual_payload_len = 0;
  n2s(p, actual_payload_len);

  if (actual_payload_len != fixture.expected_payload_len) {
    printf("%s failed:\n  expected payload len: %d\n  received: %d\n",
           fixture.test_case_name, fixture.expected_payload_len,
           actual_payload_len);
    PrintPayload("sent", sent_buf, strlen((const char*)sent_buf));
    PrintPayload("received", p, actual_payload_len);
    result = 1;
  } else {
    char* actual_payload = strndup((const char*)p, actual_payload_len);
    if (strcmp(actual_payload, fixture.expected_return_payload) != 0) {
      printf("%s failed:\n  expected payload: \"%s\"\n  received: \"%s\"\n",
             fixture.test_case_name, fixture.expected_return_payload,
             actual_payload);
      result = 1;
    }
    free(actual_payload);
  }

  if (result != 0) {
    printf("** %s failed **\n--------\n", fixture.test_case_name);
  }
  TearDown(fixture);
  return result;
}

```


The `tls1_process_heartbeat()` tests are nearly
        identical, except they call `SetUpTls()` to initialize a
        `HeartbleedTestFixture` and don’t cover the
        `ExcessivePlaintextLength` case.
        `ExecuteHeartbeat()` and other test helper functions are a
        little more complicated than those of the “goto fail” test, but only
        slightly.


Like the “goto fail” test, this test was written without the help
        of a testing framework. It may be copied directly into the
        `test/` directory of any OpenSSL release from 1.0.1-beta1
        to 1.0.1g without any modification and executed. When executed for
        version 1.0.1g, the test passes and produces no output. For the other
        versions, the test cases with “Heartbleed” in the name fail with
        output resembling:


```
TestDtls1Heartbleed failed:
  expected payload len: 0
  received: 1024
sent 26 characters
  "HEARTBLEED                "
received 1024 characters
  "HEARTBLEED                \xde\xad\xbe\xef..."
** TestDtls1Heartbleed failed **

```


The contents of the returned buffer in the failing test will depend
        on the contents of memory on the machine executing the test. The value
        of `kMaxPrintableCharacters`, set to 1024 by default at the
        top of the test file, can be increased to see even more memory contents
        returned.


### Break It Up, Break It Down


There is another issue we can address in the Heartbleed example
        that we could not in the “goto fail” example. With “goto fail”, we
        have no visibility into the exact change that introduced the bug;
        available evidence suggests that it was possibly a large merge
        operation, compounded by code duplication. Still, the “complicated
        merge” theory is only a guess. With Heartbleed, we can see the exact
        change that introduced both the TLS heartbeat feature and the
        Heartbleed bug buried within it, and that it had been
        code-reviewed.


Developers well-accustomed to unit testing would have produced or
        insisted upon a small series of well-tested changes building up to a
        feature rather than a single, monolithic change such as the one in
        question. A smaller, well-tested change containing only the above
        functions could have better enabled the author, the reviewer, or an
        interested onlooker to notice the use of an externally-supplied
        value to read a block of memory, and to verify that such a value had
        been handled properly. An explicit reference to the specific
        section of the protocol defining the structure and handling of
        heartbeat requests might've also helped focus the testing and the
        review.


A coding standard document could also help with this process. In
        addition to specifying the particulars of naming, whitespace, and
        brace placement, such a standard could require that request- and
        buffer-handling code be accompanied by tests to verify the absence of
        buffer overrun issues. This would be in addition to requiring that all
        code submitted for review be covered by new or existing unit tests as
        a matter of policy.


### If It Ain’t Tested, It Ain’t Fixed


The proof-of-concept test above shows that it is conceivable that
        had someone tried to unit test the code, they could have possibly
        caught and prevented one of the most catastrophic computer bugs in
        history. The existence of the proof-of-concept unit test eliminates
        the assertion that it would've been impossible.
        [Sadly the fix submitted for the bug](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=731f431497f463f3a2a97236fe0187b11c44aead)
        also lacked a unit test to verify it and guard against regression.


No bug is considered properly fixed without an automated
        regression test.


In a unit testing culture, when a bug is discovered, the natural
        reaction is to write a test that exposes it, then to fix the code to
        squash it. To expand the point made during the “goto fail” discussion,
        that manual tests run to verify a code change prove ephemeral, a fix
        unaccompanied by a test is vulnerable to becoming undone. An automated
        regression test guards against future errors just as a test written
        for the code in the first place could have.


Given the power of modern version control systems and the
        increasingly-common practices of forking, merging, and
        cherry-picking, tests have become more important than ever to guard
        against unintentional changes, especially changes leading to a
        regression of a known catastrophic bug. The apparent removal of a
        regression test during a cherry pick or a merge should set off
        alarm bells, even more so if the test was included in the same
        change as the fix, as the fix could become undone as well.


### Déjà Vu All Over Again


One last point to make: By opening each of
        `dtls1_process_heartbeat()`
        (`ssl/d1_both.c`)
        and `tls1_process_heartbeat()`
        (`ssl/t1_lib.c`) in
        separate browser tabs and flipping between them, again we see apparent
        tolerance of duplicated, untested code, as we did in the “goto
        fail” example. With the proof-of-concept test in place, it would
        be possible to eliminate the duplication by extracting one common
        function with an extra set of parameters—perhaps a small “jump
        table”—to implement the slight differences between the
        algorithms.


### Linus’s Law Revisited


It should be clear by now that both the “goto fail” and
        Heartbleed bugs were fairly straightforward programming errors,
        which are among the kind of errors unit tests are so great at
        catching early. It should also be clear from the above discussion,
        supported by the implementation of both proof-of-concept unit tests,
        that it is likely that these bugs could have been prevented, had
        the teams that produced each bug embraced the practice of unit
        testing.


These catastrophic defects also demonstrate the limitations
        of “Linus’s Law”—*Given enough eyes, all bugs are
        shallow*—at the same time that it demonstrates the law’s
        true potential.


Given enough eyes, all exploitable bugs are found—but not
        necessarily by the good guys.


It is unknown whether either bug has ever been successfully
        exploited, but the code has been available as Open Source on Apple’s
        and OpenSSL’s servers for years, providing the opportunity for a
        malicious agent to discover either bug and use knowledge of it to
        his/her advantage without notifying anyone else. In light of this
        realization, let’s propose a corollary to Linus’s Law:


*Not all eyes that notice bugs in Open Source code belong to
        saints who will report or repair them in the interest of the public
        good.*


At the same time, providing open access to the source code meant
        that, in both cases, anyone in the world with Internet access could
        inspect the code after-the-fact to grasp the nature and severity of
        the errors, report on their technical details and ramifications, and
        debate about lessons learned and appropriate responses to prevent a
        recurrence. The quality of those reports varies, naturally, but the
        transparency afforded by Open Source software enables an open debate
        that should, ultimately, ideally, lead to object lessons that will
        be of benefit to society. Had a similar vulnerability occurred in
        closed-source software, this valuable discussion would be more
        difficult to have—it’s actually quite possible that similar
        vulnerabilities have existed, and the software development community
        at large will likely never get a chance to learn from them.


Having access to the Open Source code enabled me to
        submit my unit/regression test to the central OpenSSL source
        repository.


Also in both cases, having access to the Open Source code enabled
        me to dive into each code base and, in a matter of hours, write
        conclusive proof-of-concept unit tests for each bug. It also enabled
        me to engage the OpenSSL developers and submit a
        [pull request for the proof-of-concept
        Heartbleed unit test](https://github.com/openssl/openssl/pull/81) (adapted from Google to OpenSSL coding
        style, of course) which was ultimately included in the central
        OpenSSL source repository as
        `ssl/heartbeat_test.c`.


Of course, this raises the question: Why didn’t the teams
        responsible for the code write or insist upon such tests years ago
        at the time the bugs were introduced?


The buck stops with the code review process, whereby a change is
        accepted for inclusion into the code base by the developers who
        control access to the canonical source repository. If unit tests are
        not required by a code reviewer, then cruft will pile on top of cruft,
        multiplying the chances of another âgoto failâ or Heartbleed slipping
        through. As was perhaps the case with âgoto failâ, the development
        teams at many companies are focused on high-level business goals, lack
        any direct incentive to improve code quality, and perceive an
        investment in code quality to be at odds with shipping on-time. As was
        the case with Heartbleed, many Open Source projects are
        volunteer-driven, and the central developers are short on either the
        time or the skills required to enforce the policy that each code
        change be accompanied by thorough, well-crafted unit tests. No one is
        paying, rewarding, or pressuring them to maintain a high level of code
        quality.


Consequently, the development cultures which produced the bugs
        either had not considered unit testing at all, or had considered it
        and rejected it on some basis, which I believe can be described as
        a perceived âopportunity costâ. This means that unit testing was
        deemed to provide insufficient value in return for the investment,
        draining precious resources from other priorities and opportunities.
        This may not have been a conscious decision, but the choice is
        manifest by the other tools and practices a team has decided to adopt
        instead.


However such decisions are made, it is true that developing and
        sustaining a high-functioning unit testing culture is not a cost-free
        proposition. In the next section I'll explore those costs and consider
        whether or not they're worthwhile.


## The Costs and Benefits of a Unit Testing Culture


While unit testing can greatly reduce the number of low-level
      defects, including defects as high-visibility and high-impact as âgoto
      failâ and Heartbleed, and have a positive influence on other aspects of
      code quality and the development process, building and maintaining a
      unit testing culture comes at a cost. There’s no such thing as a free
      lunch.


### Startup Costs


There will be a learning curve. Like any skill that relies on
        craft rather than rote processes, a programmer learning to write
        unit tests will have to go through phases of learning and
        development, of trial and error, reflection, experimentation,
        and integration.  This takes time, energy, and funding away from
        other activities. It will cause an initial slow-down in development as
        people grow accustomed to the practice.


That said, this is a one-time cost. The cost of bringing someone
        up to speed on unit testing is relatively low if good unit testing
        practices are already in place on a team, and unit testing skills are
        portable from one project to the next. Hence, the learning curve is
        steepest for teams that don't have any unit testing practices at
        all.


Unit testing, like any other tool, language, or process,
        can be applied poorly—especially when one first begins, and even
        more so if one has no good examples to follow, nor mentors for
        guidance. Unit tests which are brittle, large, slow, perpetually
        broken (and subsequently ignored), or flaky set bad examples which
        can get replicated through an entire test suite like a virus.
        Poorly-written tests can actually be worse than no tests at all,
        leaving the impression that testing is a waste of time. Builds
        remain broken and ignored, flooding the testing signal with
        the noise of constant failures. Developers uninterested in working
        with the testing environment become willing to live with the fear
        of making slow and painful changes. The end result is a drag on
        productivity, an increased risk of defects, and a team convinced
        that testing is for other people.


### Training


To remedy this lack of knowledge and experience, motivated
        developers can band together to improve one another's unit testing
        skills and increase the amount of test coverage of the code base over
        time. In this section, I will describe how the Google Web Server Team
        built up its test coverage and achieved a high degree of overall
        productivity; in later sections I will explain how Google as a
        whole was able to adopt a unit testing culture, and how
        lessons from that experience may apply to individual teams. However,
        self-training will take time and energy, and the big-picture payoff
        may not be immediately apparent, so it requires patience, honest
        effort, and commitment to see all the way through. Over time,
        though, as the code base grows and more developers join the team,
        the value becomes increasingly clear. A two-person team might manage
        without unit testing, but a twenty-person team will have a harder
        time, as feature and communication complexity is compounded.


If developers are not motivated to research available materials
        and improve their skills, or just don't have any idea how to
        begin, this may imply the need to invest in internal training programs
        or to contract outside help to provide training. This can lead to a
        bit of price-shock if resources are tight, deadlines are looming, and
        the future benefits do not seem clear. The time required to learn the
        necessary skills should be no greater than that required to train
        developers in any other skill or technology; but if developers
        resist, the process can become more drawn-out, painful, and
        expensive.


### Painting Yourself Into a Corner


Sometimes, tests themselves can become a maintenance burden; it
        may seem like they paint a project into a corner, restricting progress
        rather than maximizing it. This is a particular danger to new teams
        that lack experience with unit testing and don't understand its
        value. Mock objects are prone to misuse by inexperienced
        practitioners, leading to brittle tests of dubious value. With
        experience, this scenario becomes less likely. You eventually learn
        to step back, reevaluate the goal of the code and the test, and
        rewrite one, the other, or both. In the meanwhile, it may become
        necessary at times to replace an overly-restrictive test rather
        than to spend the effort salvaging it.


Speaking of new projects or teams or companies or domains, as
        ideal as it may be to follow [Agile](https://martinfowler.com/agile.html)
        practices to the letter and practice pure
        [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) (TDD) at all times,
        sometimes a developer or a team needs to explore, to play,
        before getting serious about defining expectations and behavior.
        (Some argue that always following all Agile practices to the letter
        is a demonstration that you don't understand Agile.) While it’s
        always nice to get testing experience as early as possible on a
        project, sometimes you just need to write throw-away, prototype
        code; in that case thorough unit testing is probably overkill. This
        may be especially true of startups trying to launch a product as
        fast as possible.


On the other hand, be aware of the saying: âThere is nothing
        more permanent than throw-away code.â The trade-off is that the
        more features are implemented without accompanying tests, the more
        [Technical Debt](https://martinfowler.com/bliki/TechnicalDebt.html) a team builds up that must be
        repaid later. Unit testing can be difficult if you don't design for
        testability from the start—using [dependency
        injection](https://martinfowler.com/articles/injection.html), writing well-defined classes that focus on one
        thing, and so forth. It is up to the team to gauge the acceptable
        limits of such debt, and at which point it must be paid to avoid an
        even more expensive rewrite once maintenance and new feature
        development grow too cumbersome.


### Who Tests the Tests?


There's no guarantee that unit tests themselves will be
        bug-free. Consider this example (in C++-like pseudocode based on
        the [Google Test](https://code.google.com/p/googletest/) framework):


```
TEST_F(FooTest, IfAPresentFilterB) {
  setup input and add "A:" , "B:"
  run call
  EXPECT_TRUE(PresentInOutput("A:"))
  EXPECT_FALSE(PresentInOutput("B"))
}

```


The second expectation in this test should check for
        `âB:â`, with a colon, not just `âBâ`.  If the
        code under test accidentally filters for `âBâ` without a
        colon, the test will pass when it should fail.


It's arguable that the test makes things worse in this case,
        providing a false sense of security. However, the bug could exist even
        if the test hadn't been written; given the existence of the buggy
        test, fixing the code and the test is tantamount to providing a
        regression test for the bug.  Fixing the test and learning from the
        mistake provides value; blaming the test and deleting it is a step
        backwards. As one possible measure to avoid buggy tests in the future,
        the team responsible for such a bug could endeavor to take a closer
        look at the test code submitted as part of future code reviews, to
        provide it with the same priority and care as âproductionâ code.


In practice, buggy unit tests tend to be the exception. If
        practicing pure Test-Driven Development, a failing test should be
        written before the code that makes it pass; this could help to prevent
        such bugs. If not practicing pure TDD, temporarily adding an error
        into the code under test to make sure the test will fail can also
        help. In either case, writing multiple test cases that check that the
        code doesn't do what it shouldn't do (instead of just checking the
        happy path where all inputs are valid) may reveal bugs in other test
        cases. Still, the possibility remains that unit tests themselves may
        contain bugs, especially if care isn't taken to ensure that they fail
        when they're supposed to.


### Tests Are For Chumps


There have been examples in the past of successful teams or
        companies full of rock star programmers banging out code that
        changes the world. Google certainly fit this description for its
        first several years of existence. In that case, it’s arguable
        that, during that era, the time spent on unit testing would’ve
        been wasteful, as it might've needlessly slowed down those top-notch
        developers, especially if they weren't already used to writing unit
        tests. Since the company and the code base was smaller, and code
        reviews were already mandatory, the company effectively could manage
        the complexity by only hiring the âsmartestâ programmers who could
        rapidly get up to speed in that environment.


The question then becomes: Why didn't that state of affairs remain
        permanent?


### The Google Web Server Story


Despite the risks and the costs, it's important to realize that the
        benefits of unit testing go beyond merely minimizing the chances of
        releasing catastrophic bugs.


When I joined Google in 2005, it was already very successful and
        many âlong timersâ believed it was because we were doing everything
        right. As a result, at that time and for some years afterwards, there
        was a lot of resistance to change. However, as the user base and
        potential for catastrophe exploded, and as success and the growth that
        came with it caught up to Google, it became clear that more “rock
        stars” producing “rock star” code was going to produce nothing but a
        bunch of noise and confusion in the long-term. An influx of new Google
        developers eventually helped accelerate the cultural shift towards unit
        testing adoption, both because these new developers were open to the
        idea, and because testing eventually proved effective in helping these
        new folks get up to speed and avoid making mistakes.


As a concrete example, let's take what is possibly the most popular
        page on the Internet: Google's home page. The Google Web Server (GWS)
        team's unit testing story became well-known throughout the company.
        The GWS Team had gotten into a position in the mid 2000's where it was
        difficult to make changes to the web server, a C++ application serving
        Google's home page and many other Google web pages. Despite this
        difficulty, integrating new features was integral to the success of
        Google as a business. The barrier that was stopping people from making
        changes as rapidly as possible was the same that slows change on most
        mature codebases: a quite reasonable fear that changes will introduce
        bugs.


[Fear is the mind-killer.](http://en.wikipedia.org/wiki/Bene_Gesserit#Litany_against_fear)
        It stops new team members from changing things because they
        don't understand the system, and it stops experienced people
        changing things because they understand it all too well.


The Google Web Server Team took a hard line: No code was
        accepted without an accompanying unit test.


Determined to overcome this fear, the GWS Team introduced a testing
        culture. They took a hard line: No code was accepted, no code
        review was approved without an accompanying unit test. This
        often frustrated contributors from other teams trying to
        launch their features, but the GWS Team stuck to its guns.


Over time, unit test coverage and development momentum went
        up, while defect, production rollback, and emergency release
        counts went down. New team members found themselves becoming
        productive far more quickly because the tests allowed
        them to gain a deeper perspective on a system one unit at a
        time, and to begin contributing changes with the confidence
        that the existing tests would likely detect any unexpected
        side-effects. Any tests they caused to fail in the course of
        their early efforts accelerated their grasp of the system.
        Experienced members of the team, who had grown cautious of
        making changes and accepting changes from contributors, were
        able to make and accept changes quickly for the same reason
        and no longer had to rely primarily upon large and expensive
        system or manual tests with feedback cycles on the order of
        hours or days. Adding more new developers actually allowed the team to
        move faster and do more, avoiding the scenario described by
        [Brooks's Law](http://en.wikipedia.org/wiki/Brooks%27_law) in which âadding manpower
        to a late software project makes it laterâ.


Furthermore, the mitigation of fear led to the expansion of
        their joy in programming, as they could see tangible progress
        being made towards exciting new milestones without being held
        back by chronic outbreaks of high-priority bugs. The impact on
        productivity of high morale, based on the ability to remain in
        a state of creative flow, cannot be overstated. While I was at
        Google, the GWS Team exhibited the ideal testing culture,
        integrating an enormous number of complex changes
        from outside contributors while making their own constant
        improvements.


Thanks to the GWS example inspiring the efforts of the
        Testing Grouplet (a team of developers volunteering to promote
        unit testing adoption, described in a later section of this
        article), many teams at Google were able to transition to a
        unit testing culture and benefit from reduced fear and
        increased productivity. It did take time to overcome inertia,
        indifference, the friction of outdated tools, and resistance,
        since at first unit testing felt like a cost and some people
        worried that the time spent writing that second representation
        of behavior could be spent writing new code (that would get them
        promoted). Eventually, as people experienced what it meant to
        cast aside the fear of change, they came to see this
        side-effect as easily outweighing those lines of code, in
        terms of its impact on their happiness, on their team's
        happiness, and on the bottom-line of productive output.


### Tight Feedback Loops


Over time, unit testing discipline allowed the Google Web
        Server Team to move faster and do more. Unit tests are just as much
        about improving productivity as catching bugs.


In case you missed it, the important point about the GWS Team story
        is that over time, unit testing discipline allowed the team to move
        faster and do more. Unit tests are just as much about improving
        productivity as they are about catching bugs, so proper unit
        testing sped them up rather than slowed them down. Let's highlight
        a few factors that contributed to this outcome.


Unit testing is not in the same class as integration testing, or
        system testing, or any kind of adversarial âblack-boxâ testing that
        tries to exercise a system based solely on its interface contract.
        These types of tests can be automated in the same style as unit tests,
        perhaps even using the same tools and frameworks, and that's a good
        thing. However, unit tests codify the intent of a specific low-level
        unit of code. They are focused, and they are fast. When an automated
        test breaks during development, the responsible code change is rapidly
        identified and addressed.


This [rapid feedback cycle](http://en.wikipedia.org/wiki/OODA_loop) generates a
        sense of [flow](http://en.wikipedia.org/wiki/Flow_(psychology)) during development, which is
        the ideal state of focus and motivation needed to solve complex
        problems. Contrast that with the opposite phenomenon, using the
        familiar operating systems metaphor of
        [context switching](http://en.wikipedia.org/wiki/Context_switch). Context
        switching requires that the present state of operations be saved
        somehow, and that a new state of operations be swapped in before
        initiating the new activity; then there's the time and effort involved
        in switching back. Plus, there's the issue of how much state must
        be managed per operation. Without unit tests, we have to use more
        of our brains to remember weird corner cases and strange
        side-effects, giving us less time and energy to do the thing we're
        better at than the computer: advancing solutions to new problems
        rather than juggling the weight of all the problems that have
        already been solved.


In other words, you can be more productive since you can iterate
        on code much quicker: You don't need to start up some heavyweight
        server if you can just run a unit test instead. So if it takes a
        few tries to get some code right, those few tries might take
        minutes (or longer) if you have to start up a server again and
        again, compared to seconds if you just need to rerun the unit tests
        each time.


### Improved Code Quality


Just as dogfooding is good practice at the product level,
        having to write code that uses your own code can lead to improved
        designs.


Far from being an exercise in academic purity, code quality
        matters. Bad code provides bugs with plenty of shadows in which to
        hide; good code increases the chances that they will be found
        and squashed sooner rather than later. When the author of a piece of code
        writes a test for that code, the author effectively becomes the first
        user. Just as [eating your own dogfood](http://en.wikipedia.org/wiki/Eating_your_own_dog_food) is
        good software development practice at the overall product level,
        having to write code that uses your own code can lead to improved
        designs that are more readable, maintainable, and debuggable.


Think of what problems you're trying to solve with the code you're
        writing; then think of the code you'd like to write, as a
        client, to make use of the solution. That ideal client code
        can be expressed as unit test cases that use the interface of
        the code you're developing.


When code-level design is approached this way, all of the smaller
        pieces that make up the larger system become not just more reliable,
        but easier to understand. This makes everyone more productive, as the
        mental effort required to comprehend what a specific piece of code
        does is minimized.


### Executable Documentation


Unit test names can act as a specification of the code's
        behavior; the tests themselves act as code samples for each
        behavior case. To achieve this, set the same quality bar for test
        code as production code.


Well-written unit tests can provide two types of documentation:
        the test names act as a sort of specification of the code's
        behavior; and the tests themselves act as code samples for each
        behavior case. Even better than typical Application Programming
        Interface (API) documentation, well-maintained unit tests are by
        definition an up-to-date representation of actual behavior. The author
        of a unit test effectively communicates to other developers how a
        piece of code should be used, and what to expect from it. These âother
        developersâ may be brand new to the team, or may not yet be hired (or
        even born). Such documentation helps developers understand unfamiliar
        code, even entire systems, without interrupting anyone else to the
        degree that they might without unit tests.


Poorly-written unit tests lack this quality, usually because
        less thought is given to test code than âproductionâ code. The
        solution: Set the same quality bar for test code as production
        code. If you don't, your tests will become hard to maintain and
        slow down the team.


### Accelerated Understanding


Every time a test fails, that is an opportunity to deepen
        your understanding of the system.


Think of it like this: Every time a test fails, that is an
        opportunity to deepen your understanding of the system. If you're new
        to a team, breaking many tests as you begin to make changes to the
        system can help you become productive far more quickly, as each of
        these events align your awareness of the system more closely with
        reality. If you've been on the team for a long time, existing tests
        will answer many questions that new contributors may have, saving your
        time and focus. They will also remind you of all the nuances of the
        code you might have written in the past, and haven't had to think
        about for some time, should you have to dive back into it. In other
        words, you benefit your future self when adding a well-crafted suite
        of tests to your code, minimizing the time needed to context-switch
        back into that prior state of mind.


Think of the opposite, as was the case in the pre-unit testing
        days of GWS: When you're on a project that doesn't have ample unit
        testing coverage, you're afraid to do anything since you don't know
        what you might break.


### Faster Bug Hunting


Imagine a bug is found in integration or system
        testing, or after a new release is pushed to a datacenter, or perhaps
        by a user some time after that. The developers responsible for the
        buggy code have already moved on to other tasks, and are likely under
        deadline pressure to deliver. If the bug is severe enough, at least
        one of those developers will have to stop to address it, slowing the
        progress of the new development work underway.


If the buggy code is well-covered by a suite of automated tests,
        especially small unit tests, this interruption may not take much time
        on the part of the developer assigned to fix the bug. The existing
        tests serve as documentation of the intent of the affected code. The
        developer adds a new test to reproduce the bug, verifying that the
        defect is well-understood before attempting to fix it. This new test
        verifies the fix for the bug, and the existing tests provide a high
        degree of confidence that the fix is free of unintentional
        side-effects. The new test becomes a permanent part of the test suite
        to guard against regression, the fix is released, and development on
        the new release continues. The interruption is finished.


Contrast that against the situation where the buggy code isn't
        well-covered by unit tests. The developer must take time to understand
        the affected code and far more care to pinpoint the error and ensure
        its fix is free of side-effects. Verification of the fix may not come
        for days or even longer, depending on the nature of whatever
        pre-release testing happens to be in place, if any. The interruption
        is prolonged, and drains more development and testing time from
        the new release.


Or, even worse: The team may decide to leave the bug in-place
        from fear of breaking something else. That certainly doesn't
        inspire user trust, much less developer confidence and
        productivity.


### Are You Experienced?


After all these [words, words, words](http://shakespeare.mit.edu/hamlet/hamlet.2.2.html#speech52), do
        you remain unconvinced of the value and power of unit testing? Can't
        say I blame you. To be honest, like other good things in life, you
        can't really know what it's like until you've actually tried it. On
        top of that, it's possible you won't enjoy it at all until someone
        helps you learn how to do it well.


My own experience with unit testing did not begin with some
        extensive rational argument, or compelling objective evidence
        convincing me to try it. The team I was a member of at Northrop
        Grumman had just finished a brutal push to meet a required
        certification deadline; in the following months, while rewriting a
        subsystem for performance and stability reasons, I tried unit testing
        out for kicks. The difference between the two experiences couldn't
        have been more different, or more convincing. I could see and feel the
        progress of the new system as every new feature was added, and the
        finished product turned out exactly as intended. When the rare bug did
        occur, it took no more than a couple hours to pinpoint it, reproduce
        it, fix it, and ship the fix—without adding any new defects in the
        process.


There is no greater argument in favor of unit testing than
        the actual experience of unit testing. Best of all, unit testing
        skill is portable across domains, languages, and companies, just
        like any other basic programming skill.


What I'm saying is, there is no greater argument in favor of unit
        testing than the actual experience of unit testing. You
        [Cannot Measure Productivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html), but you can feel it.
        Even if your first unit tests prove ugly, complicated, and brittle,
        trust me, you can get better at it, and the reward will be well worth
        the journey.


Best of all, unit testing skill is portable across domains,
        languages, and companies, just like any other basic programming skill.
        It is an investment that pays returns over the course of a lifetime.
        Remember: Past unit testing experience is what enabled me to write
        proof-of-concept unit tests for both “goto fail” and Heartbleed so
        quickly, having no familiarity with the code and not programming on a
        regular basis for years.


### Get Your Hands Dirty


The first two sections of this article contain links to
        the âgoto failâ unit test
        bundle and the Heartbleed unit
        test. If you haven't done it already, download the code, build it
        and run it on your system. Make sure the tests pass. Then, change
        something, either in the test code or in the code under test, to make
        it break. Look at the output. Take it in, reflect. Then fix the code
        to make the test pass again.


You thought you've understood the âgoto failâ and Heartbleed
        code, but now you've actually felt how it works.


What you (should have) experienced is the intellectual thrill that
        comes from making a change to part of a real system, and seeing the
        impact of that change in near-real time, without having to build and
        launch the entire product and poke around through the user
        interface. Think about it: Up until now, you think you've
        understood the âgoto failâ and Heartbleed code by just reading it,
        or the explanations earlier in this article, or perhaps other
        sources you may have read. But now you've actually felt how the
        code works. In the case of the Heartbleed test, you could actually
        see the contents of your machine's memory spilled onto the screen.
        (On my machine, I can clearly see my `PATH` and other
        environment variables.)


The exhilaration of immediately verifying that the code you just
        added or changed really did what you intended it to do is its own
        reward. The feeling of (relative) certainty that your code will
        correctly handle any input thrown at it is invigorating. The rush of
        excitement when a test detects an error in code you just wrote, an
        error you (or some other poor sap) won't have to spend hours
        debugging, fixing, verifying, and cleaning up later, is addictive.


And reproducing major bugs in code you've never seen before?
        Priceless.


Immediate gratification is what really hooked most
        of us who swear by our unit tests. No rational arguments, no data,
        no charts or dollar amounts needed.


That sense of immediate gratification is what really hooked most
        of us who swear by our unit tests. For others, it's the high degree
        of trust that regressions won't occur. In either case, unit testing
        creates a pure high, based on a sense of forward progress, a sense
        of fearless productivity, with none of the other nasty side effects
        of addiction. No rational arguments, no data, no charts or dollar
        amounts needed.


### No Test Is an Island


However, despite all of its benefits, unit testing shouldn't be the
        only tool in your development toolbox for ensuring high-quality,
        mostly bug-free code. Next, let's consider a number of other available
        tools and practices that can be used in concert with unit testing as
        part of day-to-day development, and why it's still worth adopting unit
        testing in light of these other items that can be brought to bear in
        catching defects early.


## Other Useful Tools and Practices


Despite the effectiveness of unit testing in detecting programming
      errors early, and despite its other productivity benefits, it is far
      from a [silver bullet](http://en.wikipedia.org/wiki/No_Silver_Bullet), a miracle cure
      that is guaranteed to eliminate all software defects prior to release.
      No tool can effectively do so, as developing a tool to guarantee that a
      piece of sofware is bug-free would be equivalent to solving the
      [Halting Problem](http://en.wikipedia.org/wiki/Halting_problem). As goes the famous
      quote:


> ...program testing
>       can be used very effectively to show the presence of bugs but never to
>       show their absence.
> -- [Edsger W. Dijkstra](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD03xx/EWD303.html)


Indeed, some classes of bugs are notoriously difficult to effectively
      unit test, at least in a general sense. The shining example of this is
      the class of concurrency bugs that can happen as a result of shared
      mutable memory, such as race conditions and deadlocks. This can involve
      threads sharing data within a single program, processes on the same
      machine sharing a file on disk, or distributed systems that must ensure
      the consistency of information stored in a database. While unit testing
      each bit of logic in a single-threaded context is a first step towards
      ensuring correctness in a multithreaded context, it is far from
      sufficient to ensure the absence of concurrency bugs. Other tools,
      layers of testing, staging environments, and forms of monitoring and
      logging are needed to detect and debug such issues. (Though, when such a
      bug is discovered, it would be ideal to provide a unit test to reliably
      reproduce it and verify its fix.)


In light of these truths, it is not only advisable, but critical to
      bring other tools and practices to bear on the problem of detecting
      defects early, to ensure a high degree of code quality and to maximize
      the chances for a product’s success and minimize its potential for
      failure. However, when considering other tools, remember this: As
      demonstrated by the proof-of-concept tests in the earlier sections of
      this article, unit testing can be applied in any language, with existing
      development tools, in the context of any other development practices, to
      existing code. Certain tools, frameworks, languages, and practices may
      make unit testing easier and more productive, but are not a
      prerequisite. The primary costs involved are those of educating
      developers, managers, and executives about unit testing and convincing
      the developers to do it.


The real magic happens when unit testing and other tools are used in
      concert. The same tools and practices that make code easier to write and
      maintain help make unit tests easier to write and maintain. At the same
      time, designing for testability, when done well and not pushed to
      logical extremes, often results in code that's easier to review,
      maintain, extend, debug, analyze with other tools, and document. Every
      tool and practice has its strong points and its weak points; each one
      integrated into a development culture reduces the chances of bugs
      slipping into the product, and reduces the time and effort needed to
      address the ones that still do.


Programming is a craft and, like most crafts, the expert is a master
      of choosing the right tools for the job, and creating the custom tools
      needed for each individual product. When a builder is laying a cement
      foundation, the first thing that builder creates is the wooden structure
      that will contain and shape that foundation. An expert carpenter might
      start by building a framework that will hold all the pieces in place. In
      software, the same is true.  When crafting an application, we choose the
      platforms, languages, and tools that provide the foundation for the
      development environment, then we build the bespoke tools we need for
      that application: stubs and fakes that allow us to isolate pieces and
      focus our attention on them; unit tests that hold a piece of code up to
      the light so we can inspect it. Without the right tools for the job, the
      risk of shoddy results remains high.


### Static Analysis/Compiler Warnings


Static analysis and compiler warnings are great tools to apply
        even to well-tested code. Complementary safeguards that ensure code
        quality from different perspectives are always a good idea,
        as these tools may highlight problem spots that existing tests
        currently miss. Even so, unit testing can shine a light on potential
        problems that a machine might never complain about. The “goto fail”
        bug could have been caught by static analysis or an unreachable-code
        compiler warning; however, while warnings or mandatory curly braces
        could've stopped this one line of code from producing a defect, a
        culture of unit testing would've encouraged the developers responsible
        for the code to root out the duplication that provided cover for it.
        After extracting a new function writing a test to thoroughly exercise
        this critical algorithm, the programmer could then replace all six
        copies of the same algorithm appearing in the same file with six calls
        to the single isolated function, improving long-term code quality and
        decreasing the long-term potential for bugs to creep in and hide.


Static analysis tools are getting better at detecting duplicate
        code, but programmers writing unit tests are still the first and most
        effective line of defense. Also, while such tools can detect dead
        code, if indeed âgoto failâ was the result of a bad merge, imagine
        if the merge error had been this instead:


```
- if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)
-     goto fail;

```


In other words, if the result of the merge had been to accidentally
        delete the last step in the algorithm. Same bug, but all of the
        curly braces and static analysis and compiler warnings in the world
        wouldn't have helped. A unit test could've caught it. (You can try
        this with the proof-of-concept unit test to see for yourself.)


Still, static analysis and compiler warnings can help detect
        typical errors in both the code under test and the tests themselves.
        Compiler warnings, in particular, are one of the easiest tools to
        apply, since they're already built into the existing toolchain.


Programmers sometimes complain about âfalse warningsâ when applying
        such tools for the first time, since it can result in an overwhelming
        barrage of output. Indeed, some tools may complain about things like
        race conditions or null/nil pointers that, upon inspection, appear
        spurious. It could be that the tool is not yet mature, or isn't
        applicable to your particular product. Usually static analysis tools
        enable certain warnings to be suppressed, allowing a team to decide on
        a case-by-case basis whether or not to ignore particular warnings or
        to silence them temporarily.


When issues have piled up, chip away at the problem.
        Incremental progress isn't just for feature development.


On the other hand, many tools, and especially compiler warnings,
        are capable of detecting legitimate issues with relatively little
        noise; and when potential issues have gone undetected for a length of
        time, they tend to pile up, leading to a flood of warnings and errors
        when the tools are applied. The real solution in this case is to
        chip away at the problem, just like adding unit tests to existing
        code. Fix one class of warnings, for one file. Move on to the next.
        Try to add a test for the code if it isn't already covered.
        Incremental progress isn't just for feature development.


### Modern Languages


When starting a new project or application that doesn't need the
        low-level efficiency of C or even C++, a “modern” language like
        Python, Ruby, Java, Scala, C#, or Go might prove more attractive, as
        these languages feature:

- first-class Object-Oriented Programming features (e.g.
          inheritance/composition, encapsulation, polymorphism);
- automated memory management;
- array bounds checking; and
- common libraries for many low-level programming tasks.


This decision remains largely orthogonal to the decision to
        invest in building a unit testing culture—and most modern languages
        have robust features and libraries to support unit testing built
        into their standard distributions, which can only help!


For existing projects, switching to a new language is largely
        unnecessary when it comes to building a unit testing culture. The
        “goto fail” and Heartbleed bugs belonged to code written in C; but
        as the proof-of-concept unit tests show, effective unit testing
        can catch such bugs and prevent their spread without resorting to
        a more “modern, safer” language. Rewriting an existing system in a
        new language is an expensive and perilous process, and may not
        produce benefits for years. That isn’t to say it isn’t still worth
        it, but developing a unit testing culture is something you can
        start to make happen today, with the benefits far exceeding
        perceived costs and risks. This is because unit tests can be
        applied incrementally to existing code, even if such code must be
        updated a piece at a time to support improved testability, as is
        demonstrated by the “goto fail” example. What’s more, as described
        in a later section of this article, Google’s Testing Grouplet
        helped the company achieve this in the large, proving conclusively
        that adding unit tests to existing code is a solved problem.


If a team decides it's worth the risk to rewrite a system in a new
        language, that language shouldn't be seen as the solution to all
        potential defects. Unreachable code and unsafe memory accesses are not
        the only bugs waiting to bite, and a rewrite provides a prime
        opportunity to add unit tests as features are reimplemented.
        If the language is dynamically-typed, it's even more crucial to
        have a suite of unit tests to document expected types and guard
        against errors that compilers for other languages catch
        automatically. If porting an application to a new platform requires a
        rewrite in a new language, e.g. porting from iOS to Android, having a
        suite of unit tests to port as well can help smooth the
        transition and guard against porting errors.


For rewriting a low-level systems project like OpenSSL, C++ and
        Go are among the few realistic language options besides C.
        The testing tools and frameworks available in both of those
        languages are more powerful than what's available in C, making unit
        testing even easier. [Google Test](https://code.google.com/p/googletest/) and
        [Google Mock](https://code.google.com/p/googlemock/) rival the power and
        flexibility of comparable Java testing frameworks.
        [Go has amazing coverage tools
        built-in](http://blog.golang.org/cover), and [ogletest](https://github.com/jacobsa/ogletest) is a
        framework heavily influenced by Google Test.


### Open-Sourcing


Open-sourcing code does not render it bug-free by definition,
        proven by “goto fail” and Heartbleed. As mentioned in the above
        discussion of “Linus’s Law”, Open
        Source provides many positive benefits to society. It can also buy a
        lot of good faith and support from the development community, and from
        potential customers and employees. However, Open Source code does not
        automatically guarantee high-quality, bug-free code, despite the
        popular belief that it does.


If you do decide to open-source your code, you would do well to
        follow another corollary to Linus’s Law in addition to the earlier
        proposed corollary:


*If you release code as Open Source, make sure it is
        unit-tested and insist that contributed changes be accompanied by
        high-quality unit tests and documentation.*


If unit tests were granted first-class status along with feature
        development, âgoto failâ and Heartbleed could've been avoided.
        What's more, it would be easier for people to contribute to a
        project's development and long-term health by spotting missing test
        cases, or adding new tests to uncovered code. New developers would
        also have an easier time getting a grasp of the system, having tests
        as a safety net, a form of executable
        documentation, and a feedback mechanism that
        accelerates understanding.


### Style Guides/Coding Standards


It’s never too late to develop and abide by a set of coding
        standards that can provide clues to a reviewer that a piece of
        code should receive greater scrutiny. Not only can style guides
        serve to avoid countless potential arguments over the use of
        whitespace, the placement of curly braces, and the names of
        symbols, they can help programmers detect, through familiar visual
        conventions, when code deviating from a particular convention might
        indicate the presence of a defect. Coding standards don't obviate the
        need for tests; the two practices reinforce one another. Again, making
        the same mistake in two different representations is harder than
        making it once.


However, while style guidelines can help avoid many errors, they
        cannot catch an incorrect logical condition or mathematical operation.
        Neither can (most) compilers nor static analyzers for that matter, and
        untested code can be far more difficult to review for such errors.
        Style guides alone might not exert the design pressure that promotes
        the so-called SOLID design principles; designing for testability is
        practically indistinguishable from good Object-Oriented design.


As mentioned in the earlier section of this article discussing
        Heartbleed, the OpenSSL project could adopt a standard whereby any
        code that processes request buffers or allocates and writes to output
        buffers must be accompanied by tests to protect against common buffer
        vulnerabilities, in addition to requiring that all code submitted for
        review be covered by new or existing unit tests.


### Code Review


Code review is a practice worth adopting, ideally in addition to
        unit testing rather than in place of it. It helps tease out implicit
        assumptions: We all have knowledge we take for granted, and we often
        don't realize that it may not be obvious to other people. In the
        process of making the code understandable by the reviewer, the author
        is often forced to spell out his assumptions and make the code's
        intent more obvious. Also, it increases the motiviation to âdo things
        rightâ given the knowledge that your peers will actually see the code
        and comment on it openly. This improves code quality and sometimes
        exposes bugs.


Code review is also useful for documentation. Reading the
        reviewers' comments can be very enlightening to someone who is trying
        to write documentation, by revealing what is confusing to others
        and highlighting details that might've otherwise remained overlooked.
        A code review is also a good opportunity to review documentation right
        along with the code.


It may take a bit of time for developers to streamline the review
        process, and time spent reviewing code is time spent not writing
        it—neither is it, I might add, time spent debugging it—but the
        potential for knowledge transfer leading to a higher level of coding,
        domain, and product expertise across the team or company is enormous.
        Whether it happens as part of a formally documented process or as an
        undocumented side-effect of [pair
        programming](http://en.wikipedia.org/wiki/Pair_programming), every change committed to source control should be
        code-reviewed.


Smaller changes are easier to code review, since the reviewer has
        less code to examine at once. Well-tested changes are easier to code
        review, as the reviewer can see what cases the author has considered,
        and may be inspired to suggest more. Tests make the overall code
        change larger, but when written well, should serve to clarify the
        changes to the code under test, and should prove relatively
        straightforward to review. Combining these two principles, relatively
        small, well-tested code changes building up to a complete feature are
        easier to review than a monolithic change without tests, such as the
        change that produced the Heartbleed bug—which was code reviewed. Had
        the reviewer required a series of smaller, well-tested changes, that
        reviewer could have verified that the author had probed for weaknesses
        in handling invalid user input and defended against it. In other
        words, tests improve the quality of code reviews just as they improve
        the quality of code.


This improvement in quality is due to the fact that âunitsâ are
        relatively narrowly scoped, making them easier to read and understand.
        Good code review practice involves ensuring that both success and
        failure cases are covered by appropriate unit tests.


### Integration/System Tests


Some argue that integration or system testing should be a priority
        over unit testing. Certainly integration and system testing for
        large, complex projects is critical, and the more automated the
        better. However, as the two specific bugs in question demonstrate,
        sometimes the worst bugs can be the hardest to detect at a system
        level, and the easiest to test for at the unit level. Unit testing
        should be the first line of defense against bugs, as a developer is
        writing each line of code and sending changes out for review; it can
        exercise corner cases and error handling cases that are practically
        infeasible at other levels of testing.


In short: You should not be catching bugs at the integration or
        system levels that could have been caught at the unit level. When
        a bug does slip through, write a test at the lowest possible level to
        reproduce it and guard against regression. Writing an equivalent test
        at a higher level only serves to make the test more complex than it
        needs to be.


Integration and system tests can be orders of magnitude slower than
        unit tests. They often tend to interact with other modules or systems,
        some of which are external to the application. This adds time to the
        test. The slower the tests are, the less immediate value they give to
        the developer and the more chance of bugs being introduced. The slower
        the tests are, the less immediate value they give. When you're
        developing code, you want tests that run so fast that they let you
        know of an error almost as soon as you finish typing it. While what
        you're working on is fresh in your mind, that's the moment to strike
        down attendant bugs. Correct it now, then move on with confidence.


That said, integration and system tests are necessary. Unit tests
        alone can’t ensure that an integration between higher-level components
        doesn’t fail, or that an entire system can successfully perform
        complete operations from end to end. In fact, depending on the nature
        of your product, integration-level tests may prove easier to write,
        almost as fast to run, and prove reliable and maintainable enough to
        provide significant value. Done well, integration tests can enable
        aggressive refactoring across a component, often requiring little to
        no changes to the existing integration tests, while some unit tests
        may need to be adapted or rewritten in the process.


Whether a test is a pure âunitâ test by definition or a
        well-controlled integration test that runs quickly, automated tests of
        narrow scope can detect potentially devastating low-level programming
        errors that can slip through the cracks of other tools and testing
        layers. A balance of tests of different sizes is desirable; an absence
        of tests of any particular size is asking for trouble.


Unit testing can actually lead to easier and more effective
        integration and system testing. Improved code
        quality through unit testing can lead to better composition of
        the system as a collection of meaningful components with well-designed
        interfaces. This provides a better foundation for higher-level tests
        and easier debugging when those tests discover problems. If you find
        your design forces you to do system testing instead of unit testing,
        it's a sure sign your design needs to change


### Documentation


Eventually, every system of value will require documentation. This
        can range from low-level technical documentation of Application
        Programming Interfaces (APIs) up to high-level documentation of system
        behavior. These documents effectively define the requirements, the
        contracts that the code or system aims to fulfill. If part of a
        system is difficult to document, that's often a red flag that there's
        something amiss with the design.


Unit tests and other automated tests provide a form of
        executable documentation, but may
        not be the most accessible documentation to programmers not directly
        responsible for the code. Taken together, however, good unit tests and
        good documentation can help ensure a high-quality product: Good
        documentation defines the expectations of the code or system; good
        unit tests or other automated tests verify those expectations.
        Well-written tests that contribute to coherent designs also contribute
        to more accurate and coherent documentation.


### Fuzz Testing


[Fuzz testing](http://en.wikipedia.org/wiki/Fuzz_testing) is another style of
        testing worthy of mention; [Codenomicon
        discovered Heartbleed while fuzz testing its own product](http://www.theguardian.com/technology/2014/apr/24/heartbleed-why-did-a-computer-bug-have-a-name). It
        involves running a program to generate inputs to another program
        automatically, in an attempt to discover errors. The discovery of
        Heartbleed, if nothing else, is a ringing endorsement of its
        effectiveness.


It's another complementary safeguard. Fuzz testing is not, however,
        a replacement for unit testing. Fuzz testing can reveal cases
        uncovered by existing tests, but unit testing can catch many errors
        before a fuzz test is ever run. If a fuzz test does find an error, it
        should be standard practice to reproduce the error with an automated
        test at the appropriate scope to prevent regression.


### Continuous Integration


[Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) is the process of
        always updating, building, and testing the mainline of your code base
        to ensure that it is always in a releasable state. CI systems that
        rebuild a project with every code change provide value in detecting
        when a code change leads to a compile failure. However, using it
        only for that purpose is a gross neglect of its true power: the
        ability to detect when a code change leads to an overall build
        failure, including test failures. A continuous integration system
        that doesn’t run tests is like a heavy-duty pickup truck that is
        only driven to the grocery store and back. Yes, it helps serve a
        vital function, but there’s so much more you could be doing with
        it! In fact, it's arguable that [unless
        your build is self-testing, it's not really a Continuous
        Integration system.](https://martinfowler.com/articles/continuousIntegration.html#MakeYourBuildSelf-testing)


Continuous integration systems can take some effort to set up and
        maintain, but are often well worth it.
        [Jenkins](http://jenkins-ci.org/) is a popular Open Source CI system
        written in Java. [Buildbot](http://buildbot.net/) is another Open
        Source CI framework used by Chromium, WebKit, and other projects.
        [Thoughtworks's Go continuous delivery system](http://www.gocd.org/)
        (not to be confused with Google's Go programming language) is another
        Open Source system that can manage very complex pipelines of
        dependencies and not just integrate, but deploy a product
        continuously.


Google's Test Automation Platform, described in a later section of
        this article, was an extremely powerful system that changed many of
        the rules of how large-scale development was done at Google. It relied
        on a massively distributed build and test infrastructure to provide
        results within minutes for every single change submitted to the
        central repository from throughout the company.
        [Solano CI](https://www.solanolabs.com/) is a proprietary distributed
        CI service for projects written using one of the
        [supported languages](http://docs.tddium.com/ConfiguringLanguage/#configuring-language).


### Crashing and Core Dumps


It's common practice for programmers to insert assertions
        into the code that will crash the program and, depending on the
        language and operating environment, produce a stack trace or a memory
        image (âcore dumpâ in UNIX parlance) rather than risk data corruption,
        runaway processes, or other dangers. This is a good defensive practice
        regardless of whether or not the code for the program is
        unit-tested. However, crashing processes should be a last resort;
        trying to diagnose what amounts to a basic coding error after the
        code has been integrated, manually-tested, pre-launched into a
        staging area, or perhaps launched into production is a much more
        expensive proposition than trying to catch such errors up front by
        writing unit tests. If other processes choke on the same input the
        same way, the service's ability to handle other traffic may be
        degraded until the issue is resolved, potentially resulting in a loss
        of business, revenue, and trust.


### Release Engineering


Release Engineering is the process of tracking all of the features,
        bug fixes, and other inputs to a particular software release,
        and doing so in a way that all artifacts are labeled and archived, and
        that the final product is reproducible upon command. For cloud-based
        software, it also involves performing controlled rollouts to
        production, and paying close attention to production monitoring
        signals indicating either success or the need for a rollback. RelEng
        becomes the last line of defense against bugs getting into production
        and to users. Release Engineers are among the truest believers
        in testing in general and automated testing in particular, as passing
        automated tests is one of the biggest signals they depend on to
        determine whether or not to proceed with a release. This is due
        to:

- Repeatability: automated tests are inherently more repeatable
          than manual tests
- Auditability: automated tests produce more auditable records
          than manual tests
- Integration with release automation: automated tests are just
          one piece of the overall release automation story, but manual tests
          interrupt things


### Site Reliability Engineering and Production Monitoring


Once a service is running in the cloud, it becomes the domain of
        web operations, or Site Reliability Engineering in Google parlance.
        If a team lacks dedicated SREs, at least one developer is necessarily
        responsible for the task. In addition to tools to monitor the
        externally observable behavior of a running process or group of
        processes, SREs also depend critically on monitoring variables
        exported by running processes and computations based on these
        variables. You can think of exported variables as the âvital signsâ
        of the health of a process.


Monitoring and SRE support are necessary and critical, but
        shouldn't be the primary means of discovering errors. Yes, in any
        sufficiently complex system, an error will slip through every now and
        then; but it is in the SREs' interests to minimize the number of
        production fires that consume their time and energy, and to minimize
        the amount of time each one takes to resolve. It's in the developers'
        interests as well; but given the SREs' lack of attachment to the
        underlying code (generally speaking), and thus the lack of confidence
        that the code is as correct as the developers might think it is,
        they're far less tolerant of any excuses leading to more emergency
        production work—especially any such work they're paged to handle at
        3am or over weekends and holidays.


The good news is that standard monitoring hooks can be useful
        testing tools. Rather than trying to contrive ways to verify internal
        behaviors via special interfaces or mock objects, checking counters or
        other monitoring variables exported by a program can provide outputs
        that you can easily validate in automated tests of any size.


### Costs


It's worth remembering that all of these tools and practices,
        including unit testing, do incur startup and maintenance costs. This
        cost is most acute for individuals contributing to Open Source
        projects who have no money, no hardware, little documentation of the
        correct process, and often a day job working on something else.
        Setting up a continuous build is often a major effort, unless
        you have a developer support team, as Google has. All of these
        recommendations should be considered in that light, and this argues
        strongly in favor of centralizing many of the functions of
        build/test/QA across an organization. Even so, the cost of doing
        nothing will, in the long run, be greater than that of adopting unit
        testing and every other tool you can apply to ensure high code quality
        and prevent defects. If your product is somehow critical to the
        well-being of its user base, you can't afford not to.


### All Part of a Balanced Breakfast


There are still more tools and practices worthy of discussion:
        defensive programming/design by contract styles; bug reporting and
        user feedback mechanisms; logging and the role it can play in error
        detection and diagnosis; automated stacktrace collation and analysis
        tools. Hopefully it's clear that all of these tools and practices, in
        combination with diligent unit testing practice, can make an enormous
        difference in improving the quality of code as it's written, or some
        time after. Every one of them is worth considering, but I hope I've
        made a persuasive case that unit testing should be among the first
        adopted. It requires knowledge and experience to do well, but does not
        necessarily require that any additional tools, any specific
        programming language, or any additional practice be adopted in order
        to begin reaping the benefits. Plus, it can be added incrementally to
        existing code to improve code quality and reduce the occurrence of
        defects steadily over time.


As I've mentioned before in this article, I know this because
        I've lived it. One of the hardest parts about deciding to leave
        Google was the knowledge that I'd likely never experience another
        development environment quite like it again. Plus, I was
        walking away from an achievement of which I was immeasurably proud:
        My partners-in-crime and I helped drive the adoption of unit
        testing throughout a development culture that was largely ignorant,
        indifferent, or hostile towards it. In the next section, I'd like to
        share some of the details of our efforts, along with a few other
        elements of the Google development environment that made for
        high-quality code at scale.


## Google's Retrofitted Testing Culture, or: Déjà Vu All Over
      Again


The biggest reason to make instructional examples out of the “goto
      fail” and Heartbleed bugs, aside from their high visibility, is because
      detecting and preventing bugs like these is a solved problem. At the
      time I joined Google, the development culture was largely averse to unit
      testing. The work that I and others did as part of Google's Testing
      Grouplet helped to make writing tests the norm, rather than the
      exception. What follows is a brief description of how the Testing
      Grouplet fostered a strong unit testing culture at a large, growing,
      successful company with most developers either ignorant about unit
      testing or hostile towards it, claiming “My code is too hard to test” or
      “I don’t have time to test”.


I'll also mention a few other components of the Google development
      environment during the time I worked there, to provide a more complete
      picture of how Google maintained a high level of code quality despite
      its massive scale and rate of feature development. Some of this
      information may be out of date, but I believe the overall picture based
      on my memories may still prove helpful. This description is provided not
      to prescribe a guaranteed process, but to provide inspiration to other
      individuals and teams looking to make similar changes in their own
      organizations.


For a more complete view of Testing Grouplet activity and the
      cast of characters that made everything happen, visit the
      [Testing Grouplet tag page on
      my blog](http://mike-bland.com/tags/testing-grouplet.html).


### Resistance


You may believe that it was easy for Google to adopt a unit
        testing culture because Google is the mythical Google, with endless
        resources and talent at its disposal. Trust me, âeasyâ is not the word
        I would use to describe our efforts. In fact, vast pools of resources
        and talent can get in the way, as they tend to reinforce the notion
        that everything is going as well as possible, allowing problems to
        fester in the long shadows cast by towering success. Google was not
        able to change its development culture by virtue of being Google;
        rather, changing Google's development culture is what helped its
        development environment and software products continue to scale and to
        live up to expectations despite the ever-growing ranks of developers
        and users.


Resistance to unit testing at Google was largely a matter of
        developers undereducated in unit testing struggling to write new code
        using old tools that were straining heavily under the load of Google's
        ever-growing operation. Adding tests to existing code appeared
        prohibitively difficult, and given the status quo, providing tests for
        new code appeared futile. People who cared about unit testing did the
        hard work of convincing other Googlers that writing unit tests not
        only provides the confidence that the code they write is correct
        today, but that it'll stay correct in six months' time when some
        one else (or even the original developer) needs to change the
        code.


The Testing Grouplet provided a community for those of us who cared
        about unit testing. The Testing Grouplet and its allies worked
        steadily over the course of years, and was successful in disseminating
        testing knowledge throughout Google, as well as driving the
        development and adoption of new tools. These tools gave Google
        developers the time to test, and this shared knowledge made their code
        easier to test over time. Metrics and success stories shared by
        participants in the Testing Grouplet's Test Certified program also
        helped convince other teams to give unit/automated testing a try.
        Participating teams often credited Test Certified with helping improve
        productivity metrics they most cared about, such as the number of code
        changes and/or features submitted over a given period of time relative
        to bugs, rollbacks, and emergency releases over the same period.


### What Is the Testing Grouplet?


The [Testing Grouplet](http://mike-bland.com/2011/09/27/testing-grouplet.html) was a
        team of Google developers who worked together in their 20% time
        (time provided by Google to allow developers to work on Google-related
        projects of their choosing aside from their main projects) to address
        the challenges in promoting unit testing adoption throughout Google.
        An all-volunteer group with little funding and no direct authority, it
        relied on persuasion and innovation to convince Google developers of
        the value of unit testing, and provided them with the tools and
        knowledge needed to do it well. The Testing Grouplet successfully
        employed unconventional tactics to achieve its grand strategy of
        driving unit testing culture throughout Google, many of which are
        described in the following subsections.


These Testing Grouplet-related efforts represent a number of our
        best ideas, which happened to be the right ideas at the right time.
        There's plenty more things we tried that didn't stick as well; the
        important point is that we persevered. We continued to experiment with
        new ideas and learn from our experiences until we found a set of
        methods that worked especially well in the context of Google culture
        at the time. Some of the same methods may work for other teams and
        other companies; then again, they may not.  Still, I hope they serve
        as a source of inspiration for ideas that could work in other
        development organizations.


The Testing Grouplet was but one of a collection of
        “Intergrouplets” which aimed to improve the quality of day-to-day
        development life and productivity throughout Google by helping solve
        issues that cut across all teams. The Grouplets often complemented the
        efforts of official, dedicated teams by providing grassroots feedback,
        advocacy, and other forms of support. For example, the Testing
        Grouplet had a close relationship with the Testing Technology and
        Build Tools teams, the EngEDU internal training organization, and the
        Engineering Productivity department as a whole (discussed below in the
        âTest Certifiedâ subsection). Other Grouplets formed by passionate
        volunteers that extended the effort to improve development quality and
        experience included: the Documentation Grouplet; the Mentoring
        Grouplet; the Hiring Grouplet; the Readability Grouplet, guardians of
        the Google style guides and the readability tradition; and the Fixit
        Grouplet, which maintained the tradition of âfixitsâ, which were
        focused company-wide efforts designed to address widespread issues or
        to roll out new tools.


### Testing on the Toilet


[Testing on the Toilet](http://mike-bland.com/2011/10/25/testing-on-the-toilet.html) (TotT), a series of
        one-page articles posted in Google bathrooms, is the most visible of
        the Testing Grouplet’s efforts and achievements. Started in 2006,
        weekly episodes continue to be published. Each episode is a one-page
        overview of a particular testing technique, tool, or related issue,
        distributed to bathrooms in Google development offices throughout the
        world. “Ads” at the bottom, which approximate Google search result
        ads, provide links to more information related to the topic. Each
        episode is written, vetted, edited, and distributed all by volunteers.
        Over the years, it has been immensely effective in educating Google
        developers about the benefits and proper application of unit testing,
        and in starting company-wide conversations using standard concepts
        that have further enriched the Testing Grouplet’s efforts. These
        conversations helped prevent the echo-chamber effect by allowing
        non-Testing Grouplet members to contribute their ideas, arguments, and
        experiences.


Why post flyers in the bathrooms, as opposed to other public
        spaces? Why not blast out email newsletters? The idea was thrown out
        during a Testing Grouplet brainstorming session; no idea was
        off-limits. We'd tried a number of conventional methods—internal
        training, guest speakers, handing out books—and were looking for some
        new angle to take in getting people's attention. The boldness of this
        particular idea and the alliterative name just clicked with the group;
        it worked for us. Fortunately, once we got rolling and started
        actually posting the flyers, the idea stuck. Despite early objections
        from the vocal minority (as expected), the value of the medium became
        apparent, and the message it conveyed—that testing was an accessible
        skill, conducive to incremental learning and improvement—resonated
        more deeply the longer the series continued.


### Test Certified


[Test Certified](http://mike-bland.com/2011/10/18/test-certified.html) was a program designed by
        the Testing Grouplet which provided development teams a clear path
        towards improved unit testing practices and code quality. It
        originally consisted of three “levels” composed of discrete steps
        that a team could adopt as quarterly goals and achieve over time.
        (It eventually defined five levels, last I heard.) The first level
        focused on establishing the use of tools and baseline measurements
        (e.g. a continuous integration server,
        code coverage, identification of chronically
        broken and “flaky” tests); the second level
        focused on adopting and enforcing a testing policy requiring tests for
        all code changes and new code, and setting easily-reachable test
        coverage goals; the third level focused on guiding a team towards a
        high level of test coverage and the accompanying productivity
        benefits.


Getting every Google development team to achieve Test Certified
        Level Three status became the ultimate goal of all the Testing
        Grouplet-related efforts. The Engineering Productivity department
        became sold on the idea that Test Certified could provide Test
        Engineers and Software Engineers in Test with a tool to better
        communicate with development teams and make better use of
        everyone’s time, and threw its weight behind the program. The goal
        was effectively met with the rollout of the Test
        Automation Platform continuous integration system in 2010, after
        which nearly every development team at Google was operating at Test
        Certified Level Three.


### Test Mercenaries


The [Test Mercenaries](http://mike-bland.com/2012/07/10/test-mercenaries.html) were a team of
        software developers dedicated full-time to helping Google
        development teams achieve Test Certified status. The Testing
        Grouplet proposed the concept for the team and it existed from
        late 2006 until early 2009. Ideally, at least two Mercs would be
        assigned to a team for three months, during which the Mercs would
        learn about the product, the code, and the team dynamic, and then
        try to introduce improved unit testing practices along the path
        set by Test Certified. Success on a team-by-team basis was varied
        and difficult to measure in terms of productivity impact, but the
        focused, full-time efforts of the Test Mercenaries greatly
        augmented all other volunteer-based Testing Grouplet efforts. Test
        Mercenary experiences informed many Test Certified discussions and
        Testing on the Toilet episodes, as well as inspired tool
        developments that proved critical to driving unit testing adoption
        throughout the culture.


### Testing Fixits


[Fixits](http://mike-bland.com/2011/10/04/fixits.html) were short events organized to
        focus Google’s entire development community on issues that were
        important but had been largely put aside. They were also
        useful for rolling out new tools, and helping address any problems
        developers may have encountered. Fixits typically lasted from a day to
        a week, and were one of the most effective techniques used by several
        Grouplets and other teams for making big changes happen, thanks to the
        critical mass of planning and participation that went into each
        event.


The Testing Grouplet organized Testing Fixits in [August 2006](http://mike-bland.com/2012/10/10/testing-fixits.html) and [March 2007](http://mike-bland.com/2012/10/23/testing-fixit-2007.html) focused on fixing broken
        tests and writing new tests for uncovered code, as well as the [Revolution Fixit](http://mike-bland.com/2013/01/31/viva-la-revolucion.html) in January 2008 that
        introduced powerful new tools from the Build Tools team that
        dramatically improved development and testing speed. The Test
        Certified Challenge, lasting several months during summer 2008,
        recruited many new projects and helped many others move to higher Test
        Certified levels. The Build Tools team’s October 2009 Forgeability
        Fixit finished getting nearly every build target and test built and
        executing in the cloud, perfectly setting up the capstone of the
        entire Testing Fixit/Testing Grouplet arc: The March 2010 TAP Fixit,
        which introduced the Test Automation Platform throughout Google.


These goal-focused events served to punctuate the other
        long-term efforts initiated by the Testing Grouplet, driving
        the overall unit testing adoption mission to the next level.
        Each new fixit capitalized on the experiences and momentum of
        previous fixits. Testing on the Toilet proved an invaluable
        tool in getting the word out about these events and preparing
        the Google development community for them well in advance.


No executive permission or directives were required to run
        a fixit. Once a group decided to run one, they ran one. (A VP
        of Engineering was usually willing to send a prepared
        announcement encouraging participation, however.) The Fixit
        Grouplet existed to help coordinate between fixit teams to
        ensure they picked optimal dates (e.g. avoid any fixits during
        Burning Man week in early September, because half of Mountain
        View will be on the playa) and didn’t cannibalize each others’
        efforts, leading to a condition known as “fixit fatigue”. The
        Fixit Grouplet also provided tools, documentation, history, and
        advice so that new fixits could benefit from the experience of
        past fixits.


### Style Guides/Coding Standards


All Google developers had to “earn readability” in each language
        they regularly used. “Earning readability” was a guided process
        whereby a developer internalized much of the language-specific style
        guide. Though âearning readabilityâ involved writing code, the
        ultimate intent was to ensure that code you write remains âreadableâ
        to other developers according to company-wide conventions. The
        undersung Readability Grouplet was the all-volunteer team that
        maintained this invaluable process. Source control mechanisms made it
        prohibitively cumbersome to produce code in a language over the long
        term without earning readability status. This ensured that the style
        guides remained relevant and widely enforced.


As an example of a style guideline aimed at avoiding errors
        (as opposed to avoiding frivolous arguments over braces,
        spaces, and names), the current Google C++ style guide insists
        that heap-allocated function parameters must be passed in via
        `std::unique_ptr` if the callee is to assume
        [ownership](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Ownership_and_Smart_Pointers), and must
        be passed by [const
        reference](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Reference_Arguments) if the caller is to retain ownership. This is
        necessary because memory is not automatically managed in C++, and
        training developers to recognize poor memory management by sight
        is worth the cost compared to waiting for static and dynamic analysis
        tools to catch such errors. (Google ran such tools as well, but
        they were costly and provided a longer feedback cycle.)


Nearly all of Google’s source code repository was available to
        all developers to browse and check out into a personal working
        copy. Since the Google style guides applied to all projects in a
        given language, and many of the naming conventions were similar
        across language guides, Google developers could easily scan code in
        parts of the code base that they’d never seen before and make
        sense of it relatively quickly. This made it easy for Googlers
        to contribute to different projects, to extract repeated code into
        common libraries reusable by all projects, to identify and
        possibly patch bugs in other projects, and even to switch projects
        without enduring the friction of adapting to a new coding
        style.


### Code Review


Google instituted the practice of code reviews since its
        inception: No code was committed to source control until it had been
        reviewed and explicitly approved by someone other than the author.
        Controls existed to ensure that project “owners” were included in any
        relevant reviews. Reviewing code was just as much of a programmer’s
        day-to-day responsibility as writing code—sometimes more so—and
        the common style guidelines removed a ton of friction from the
        process, allowing the reviewer to quickly flag potential issues
        where the style appeared wrong, and to remain as focused on the
        implication of the change itself as possible. Internal tools helped
        developers manage their queue of incoming and outgoing reviews, and
        gave every developer visibility into the status of and discussion
        around every code change.


Thanks to Test Certified Level Two requirements, nearly every team
        had a formal, written development policy that every code change be
        accompanied by tests (except for pure refactorings that didn’t change
        existing behavior in already-covered code). Eventually the Build
        Tools and Testing Technology teams integrated test results (or the
        lack thereof) directly into the code review tool. The reviewer could
        see whether the author had bothered to run any tests and ensure that
        they had passed, especially if changes had been made in response to
        previous review comments.


### Common Infrastructure to Hide Low-Level Details


Given the large shared source repository and uniform language
        styles applied throughout, Google encouraged the development of
        common libraries to hide low-level details that were reused
        throughout all Google projects. The most widespread examples were
        the infrastructure for Remote Procedure Calls (RPCs) and
        [protocol buffers](https://developers.google.com/protocol-buffers/), a data
        description language used within the RPC system and in many other
        places where hierarchical, often serialized data structures were
        required. If anyone at Google tried to define serialized
        structures and manipulate memory buffers directly (such as the buffer
        manipulation in the code containing the Heartbleed bug), the first
        thing a code reviewer would've said is, âWhy not use a protobuf?â


All of this common infrastructure was extensively unit-tested,
        and unit testing infrastructure existed that made simulating RPC
        interactions and initializing/comparing protobuf values easy.


### Test Automation Platform Continuous Integration Service


When the Testing Grouplet first started in 2005, the existing
        centralized testing service, called the Unit Test Framework, was
        unable to keep up with demand. It used a dedicated set of machines to
        build and execute every test in the company and store the results in a
        database. However, the feedback cycle grew ever longer due to
        increased load on the system, diminishing its value.


In response, two Ads developers developed their own single-machine,
        project-specific continuous integration framework, known as the
        “[Chris/Jay Continuous Build](http://mike-bland.com/2012/06/21/chris-jay-continuous-build.html)”. This
        framework spread throughout Google thanks in part to its inclusion as
        a Test Certified Level One requirement. It provided a relatively
        flexible continuous integration server for Google projects and
        supported the Testing Grouplet’s Test Certified mission well for many
        years, but a C/J build did require a fair amount of maintenance from
        each team that used one.


An outcome of the January 2008 Revolution Fixit, the Test
        Automation Platform (TAP) became Google’s centralized continuous
        integration system. Rolled out Google-wide during the March 2010
        TAP Fixit, TAP was built upon Google’s in-house toolchain that
        made use of cloud infrastructure to massively parallelize
        build actions and test executions. TAP executed every test in the
        entire company’s code base affected by every code change, and only
        those tests affected by a given change, within minutes. (This time
        scale may have shifted by now, as Google's continued to grow since
        I left.) A TAP build was configured by a single short web form,
        and any project could have multiple builds. TAP’s data collection
        component, Sponge, collected the results of every build attempt and
        test run, whether run by an automated build or an individual
        developer, recorded its build commands and complete execution
        environment, and archived the information for later inspection. The
        TAP UI provided easy visibility into every change affecting every
        project in the company.


TAP represented the ultimate crowning achievement of the Testing
        Grouplet’s efforts. Developed by the Testing Technology team in
        close collaboration with the Build Tools team, TAP pushed the
        boulder over the top of the hill after years of steady effort. By the
        time I left Google, nearly every team had at least one TAP build, and
        most build breakages were rolled back or fixed before most build cops
        had a chance to notice a breakage in the first place.


### TAP Goes to Eleven


In case that last section hasn't sunk in yet: Centrally-managed
        continuous integration infrastructure. One-page, one-click setup of
        build projects. Every change in the company was integrated, built and
        tested within minutes (at least at the time I was there) via
        distributed build and execution in the cloud. Every result was stored
        and made visible to every developer in the company. Most breakages
        were fixed before most affected projects even noticed. Heaven,
        Nirvana, Valhalla, [Stonehenge](http://www.imdb.com/title/tt0088258/quotes?item=qt0261716)—whatever
        you want to call it, TAP was it.


### Build Monitoring Orbs


My first coding project at Google was to write a script that would
        change the color and pulse of a glowing orb—a spherical lamp small
        enough to be balanced in one hand and large enough that, when placed
        on a cube wall or a shelf, it could be seen by a whole team—based on
        the pass/fail status of a Chris/Jay continuous build. Over time, this
        script would expand in scope to handle a dizzying combination of build
        projects running on different continuous integration systems
        (ultimately including TAP) and controlling several different hardware
        orb devices, including the NYC-inspired Statue of Lorberty (yes, the
        torch would glow with different colors). Eventually browser plugins
        would serve as more visible reminders to individual team members
        regardless of whether they were at their desks or logged in using
        their laptops, but physical orbs in a shared team space never went
        entirely out of style.


The point of the orbs was threefold: For one, they were fun to
        hack on. For people who wanted to promote testing culture in an
        immediately tangible fashion, putting together or extending an orb
        project was a fun way to go about it. This helped recruit people into
        Testing Grouplet projects and generate a sense of energy and progress,
        boosting morale. For another, the Testing Grouplet used them as
        âprizesâ for teams that signed up for the Test Certified program, in
        the time-honored Google tradition of persuading people to take action
        by rewarding them with nifty swag. We went with the grain of Google
        nature, not against it. Absent funding and authoritah, the Testing
        Grouplet had to make the best use of available resources and cultural
        forces to effect change. In fact, I'd argue that these constraints
        forced us to produce creative solutions that had more staying power
        than any amount of money or authoritah ever could.


Finally, physical build orbs are highly-visible
        [information radiators](http://alistair.cockburn.us/Information+radiator), the next best
        thing to a full-blown [Communal Dashboard](https://martinfowler.com/bliki/CommunalDashboard.html). Arguably,
        orbs still might have a place on a team with a full-blown dashboard,
        as it encourages a playful âshamingâ culture, whereby team members
        grow personally concerned about the well-being of the orb, and hold
        each other accountable when it appears unhappy due to build
        breakages.


### Noogler Indoctrination


Working with EngEDU, Google's in-house training organization, the
        Testing Grouplet produced an introductory unit testing lecture and
        lab. This helped ensure that every new developer coming into Google
        was at least aware of the available tools and frameworks, of the
        rationale behind unit testing, and of some basic unit testing
        principles and techniques. Normally, after the one-hour lecture given
        by a member of the Testing Grouplet, the Nooglers would attend a lab
        proctored by another Testing Grouplet member to gain some immediate
        hands-on experience with what they'd just learned. The Testing
        Grouplet helped produce and maintain the internal materials used in
        this lab.


After Testing on the Toilet launched, Nooglers became the primary
        mechanism for improving distribution throughout Mountain View as the
        company grew and acquired more office space. We ended the unit testing
        lecture with the promise of books or
        [T-shirts](http://mike-bland.com/2011/10/11/t-shirts.html) for any brave Nooglers who'd
        volunteer to post that week's TotT episode in their buildings. We
        called them the âNoogler Armyâ. This was yet another way to get people
        engaged in the unit testing culture, to have fun and feel a sense of
        belonging and early contribution to the cause.


### And More…


Google had other tools, processes, and layers of testing and
        staging in place to ensure the highest possible code quality and avoid
        catastrophic, preventable defects. They didn’t catch every defect, but
        many that did slip through were relatively minor and easy to pinpoint
        and repair swiftly, free of the fear of negative side effects. More
        challenging defects could usually be addressed with a greater degree
        of confidence and speed as well. Automated testing, including high
        levels of unit test coverage, was critical to this fear-free
        environment that enabled high productivity despite the massive scale
        of the development operation and user base.


However, I don't want to leave you with the impression that Google
        is wonderful and does everything right, but your own team or company
        is hopelessly screwed. I've provided this description to foster ideas,
        not remind you of how far from the ideal your environment may be.
        Trust me, this environment I'm describing of the Google I left is in
        stark contrast to the Google I first joined, and my Testing Grouplet
        partners-in-crime and I were underfunded and woefully outnumbered. We
        had to start small and grind away for years to effect the change in
        the culture that we'd committed to make happen.


The point is, eventually, we did make it happen, despite the odds
        being stacked against us. To wrap up this article, I'd like to spell
        out a few general principles I've drawn from my Google experience that
        may provide clearer insight into how to effect similar changes in your
        own team or throughout your own company over time.


## How to Change a Culture


You may be convinced that âgoto failâ and Heartbleed could've
      been prevented by unit testing. You may be convinced
      that open-sourcing code should increase the need for unit
      testing, not decrease it. You may be convinced that unit testing
      produces a slew of benefits in addition to defect prevention,
      and that it's worth the cost. You may have the taste for it after
      playing with the proof-of-concept tests from this article, and perhaps
      beginning to test some of your own code. You may be convinced that unit
      testing can serve to improve the application of existing tools
      and practices, and you may be inspired by Google's example of
      driving unit testing throughout a company in the large.


Now you are ready to start making a change in your own project, your
      own team, or your own company...but you might not have any clue how to
      start. Here I'll offer a few personal insights which may help guide you.
      This is not a prescription to follow to the letter, nor does it
      guarantee results. However, I hope that they will serve to foster
      insights of your own that may prove helpful in driving unit testing
      adoption throughout your environment.


### Be the Change You Wish to See


(Quote courtesy of [Mahatma Gandhi](http://www.goodreads.com/quotes/24499-be-the-change-that-you-wish-to-see-in-the))


Whether you realize it or not, you've already started. You've read
        through this article and internalized its arguments. You've
        internalized the experience of unit testing for yourself. This has
        given you a foundation to build from, a perspective to take in any
        discussion on the topic of software development. There's nothing
        stopping you from walking the walk now, even if no one else follows
        you. Don't try to change any minds directly yet; just try to show how
        it's done, by writing tests for your own code. Seek out blogs,
        magazines, books, and seminars to hone your skills, such as those in
        the Further Reading section below. Read
        through everything here on Martin's website. Join a
        [Meetup](http://www.meetup.com/), such as the AutoTest
        Meetups in [Boston](http://www.meetup.com/Automated-Testing-Boston),
        [New York](http://www.meetup.com/Automated-Testing-NYC),
        [San Francisco](http://www.meetup.com/Automated-Testing-San-Francisco), and
        [Philadelphia](http://www.meetup.com/Automated-Testing-Philadelphia), or start your
        own. Lead by example and stay the course.


### Start Small with the Existing Code


As demonstrated by the âgoto failâ and Heartbleed proof-of-concept
        examples, the Google Web Server story, and the Google story as a
        whole, you can begin making improvements in existing code, right now.
        The only way your code base will improve is by working with it, and no
        amount of discussion or argument will be as effective as actually
        writing tests. By setting an example, by providing a pattern for
        others to follow, you're demonstrating that these ideas can work even
        in your team's code—and working code is its own best argument.


Take a small part of the existing code base, and write a test for
        it. Refactor the code if you have to; extract functions and classes
        that would serve as good, isolated units to test. When adding new
        functionality to existing code, make sure it's part of a well-tested
        unit, refactoring the code using the new unit if need be.


Add a unit testing framework if you can; otherwise, study the
        examples provided in this article to learn how to get by without one.
        Chip away at the problem; in time, you will be amazed at how much you
        alone have been able to accomplish.


### The Small/Medium/Large Test Pyramid


Unit tests are not a one-size-fits-all solution for code or product
        quality. You should never promise that. The Testing Grouplet pioneered
        the concept of the [Small/Medium/Large test size
        schema](http://mike-bland.com/2011/11/01/small-medium-large.html); Mike Cohn's [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) bears an
        uncanny resemblance to it. Make sure everyone is the clear of the
        fundamental role that unit tests play, but don't oversell them.


### Set Up Continuous Integration


Do whatever you can, even if you have to beg, borrow, or steal, to
        set up a continuous integration environment. Roll your own using a
        shell script and a `cron` job if you have to, even if it
        runs on your own workstation. Even if it doesn't run tests at first,
        being able to ensure that the code can build (for compiled languages)
        and the program can launch at all times is a critical prerequisite for
        spreading a unit testing culture; unit tests are pretty useless if the
        code can't compile to begin with.


If your team isn't already in the habit of ensuring that the code
        is always in a compilable state, that may be the first battle you need
        to win before driving the adoption of unit testing. If everyone
        develops on completely separate branches and integration comes long
        after-the-fact, take it upon yourself to perform the integration work
        covertly. Set up your own [git repository](http://git-scm.com/) to
        pull from these different branches and integrate between them. When
        people see what you've been up to and how many headaches you're
        helping to avoid, you'll gain credibility that will serve you
        well.


### Maximize Visibility


Make sure other people can see when the build is broken. People and
        managers who were once indifferent or hostile towards continuous
        builds and testing have had their minds changed by monitoring devices
        set up within easy sight of their desks. This works because people
        will naturally start to ask questions when the build breaks (âWhy is
        that thing red again?â), and over time it can have a major effect on
        everyone's attitude. It's human nature to care about only the problems
        we can see, so make it easy for people to see when there's a
        problem.


The monitoring device can be in the form of a plugin in
        individuals' browsers, centrally-located glowy orbs, large monitor
        screens displaying a build dashboard, specially-wired traffic lights,
        you name it. It should be conspicuous enough that people should have
        to make a deliberate effort to remain unaware of the build's current
        status.


Visibility aids can add a sense of fun as well. Teams can be
        imaginative and amusingly competitive with how they display their test
        statuses. One team at Google had a flapping penguin that came noisily
        to life when their build broke. Of course, all the surrounding teams
        had to try to find something just as good.  It all helps to spread the
        message.


### Partners-In-Crime


Eventually you will have to join forces with some
        partners-in-crime, people who need no convincing. You will both
        challenge and reinforce one another's ideas, and provide moral support
        to one another when the time comes to make a stand in the face of
        resistance. Develop your arguments, methods, idioms, etc. by bouncing
        them off of one another. Be more critical of these ideas than any
        potential critics might be, but treat each other with courtesy and
        respect. Make each other better, and eventually you may make the rest
        of your team or company better.


When trying to persuade a group of people (in anything), it's
        always easiest to start with those who are already closest to agreeing
        with you. Once you get one other person seeing it your way, you are
        no longer a loner, no longer the crazy guy with that wacky idea that
        no one else believes, and there are now two of you doing the
        persuading. Once you get a third, and then a fourth, you have some
        momentum.


Another subtle, effective way to get other people involved is to
        ask for advice. If someone on your team is resistant to testing, or
        even just unfamiliar with it, ask that person to review your code and
        tests. Ask whether there are other tests you haven't thought of. Most
        programmers are happy to offer an opinion, and it's a way to involve
        them in testing without forcing them. Over time, they might become
        convinced to the point of advocating for unit testing of their own
        volition.


### Educate


Find a way to spread knowledge throughout your team. It can be as
        straightforward as a weekly brown-bag lunch or as crazy as posting
        weekly flyers in the bathroom. Invite people to speak to your team, or
        organize a team outing to go to a talk or a Meetup. Start an internal
        mailing list to share and discuss ideas and tools.


### Delegate, Delegate, Delegate!


Paradoxically, the less you have to do directly to make things
        happen, the more things you can make happen. If you can establish a
        vision and a direction, you'll find volunteers who are more than happy
        to assume specific roles and run with them, which will give them a
        sense of belonging and value within the community you're building and
        will free you to stay focused on the larger picture.


After running a couple of Fixits, I
        realized that rather than holding onto every responsibility for
        myself, it was far more productive to create an explicit list of
        roles I needed people to fill. From then on, presenting a list of
        roles up-front worked like a charm to get a grassroots organization up
        and running very, very quickly. Some roles you might consider right
        now for your team or organization (and some of the names are
        deliberately silly, to keep it light and fun):

- **Historian**: Documents, summarizes, and archives notable
          issues or activities and their artifacts in a centrally-accessible
          repository (e.g. a wiki or a team blog)
- **Minister of Information**: Personally solicits people to
          produce talks, blog posts, articles, etc.; this person can then head
          a sub-community of speakers, authors, and volunteer editors (a la
          Testing on the Toilet), maybe even
          cultivate a community-specific knowledge base (e.g. using a
          wiki)
- **Minister of Propaganda**: Oversees announcements of team
          activities through a variety of media, e.g. emails, flyers,
          prominent wall projections, scripts given to high-profile
          managers, executives, or other representatives, etc.
- **Minister of Communication**: Monitors the health of the
          communication channels available to the team, suggests and
          implements improvements (along with the Minister of Information);
          perhaps maintains a list of contact information and archives of
          artifacts (along with the Historian)
- **Wordsmith**: Someone to specifically handle the upkeep and
          organization of new artifacts, e.g. to make sure posts are tagged,
          maybe experiment with CSS styles, do SEO work to make sure the
          content is easily discoverable by search engines (if artifacts are
          public), etc.
- **Scheduler**: Keeps track of the logistics, e.g. who is
          speaking when, where events are taking place; maintains a list of
          suitable venues and seeks out new ones, etc.
- **Festmeister**: For events, makes sure that beer and pizza
          and any goodies to be given out are all taken care of.
- **Heart and Soul**: Follows-up with speakers, authors, or
          other contributors and guests and personally expresses gratitude on
          behalf of the team, in a variety of forms: Personal emails, gift
          certificates, schwag, small parties, etc.


These are just a few off the top of my head, but I want you to
        notice something: Right now, *you* may be filling all of these
        roles, whether you're aware of it or not. It's a lot for one person to
        do, and it both bogs you down and misses an important opportunity to
        grow the team into a real, honest-to-goodness community.


### Be the Walrus


So what role would be left for you after delegating away
        everything? I called myself â[The Walrus](http://www.azlyrics.com/lyrics/beatles/iamthewalrus.html)â
        because I'm a silly Beatlemaniac, but the essence of the role is
        âOrganizerâ. You're the one with an eye on the big picture who manages
        a team of specialists. You're the one who gets to set the direction
        and priorities, who has the privilege of providing feedback to the
        creative people you've trusted with important responsibilities and
        helping to remove any obstacles they encounter, and who gets to be
        constantly amazed at the energy and creativity people bring to their
        tasks to do incredible things you'd never even dreamed possible.


### Embrace the Power of Teamwork


Holding on to all those other roles only impedes your ability to
        thrive as an Organizer, which in turn holds the community back from
        its full potential. So I'd encourage you to come up with your own list
        of things that you do for the community already, codify them in a set
        of roles, and actively engage individuals who you think would best
        suit each role.


I would sometimes even produce a list of role names with my name
        next to them in bold red type, and tell everyone that the success of
        the enterprise would be inversely proportional to the number of roles
        that still had my name next to them in red. (The only one with my name
        next to it in green was âThe Walrusâ.) When confronted with such a
        list, and with clearly defined roles as such, it's amazing how quickly
        they will volunteer and act.


That said, folks in such roles should be encouraged to interact
        without running every decision through you; the roles help clarify
        responsibilities so that *you* don't have to be involved in every
        little detail, and people can work many things out between themselves.
        Everyone should be encouraged to seek out good ideas, to develop good
        ideas, and to share them amongst themselves. You should be keeping an
        ear to the ground, of course, but people should feel like you're
        listening, not like you're listening in or trying to be their boss.
        Expect them to pleasantly surprise you, and they will.


### Make Yourself Obsolete


Start looking for your replacement on day one. No enterprise should
        be so fragile such that it falls apart after you've moved on. That
        goes for life in general. With regards to spreading a unit testing
        culture, you don't want to be stuck with the title âThe Testing Guyâ
        or âThe Testing Girlâ. You want to make sure people are willing and
        able to step up whenever you may need or want to step aside. That's
        how a legacy is built.


### Run a Fixit


Speaking of roles and fixits, a fun and productive way to rally the
        community you're building to promote unit testing is to run a
        fixit. You can start with a small
        team-sized fixit, and later run office-wide or even company-wide
        events. All you need to get started is a clear goal (e.g. fix all
        broken code/tests, increase coverage by X%, adopt some nifty new
        tool), a set of well-defined volunteer roles (as mentioned above), and
        a shared spreadsheet of some kind to track tasks that need to be done
        and who's assigned to handle each. Then pick a day, get the word out,
        and make it happen! There's nothing like applying concerted team
        effort to boost morale and solve nasty, lingering problems.


As an example of why fixits are not only fun and productive, but
        may prove vital to the cause, consider the case where a large project
        is in a state such that parts of it cannot even be compiled. This
        completely undercuts any effort to set up continuous integration, and
        encourages people to start selecting the branches of the project that
        they test rather than trying to test everything before committing
        their changes. In other words, they will execute `<tool>
        test subprojectyBitA/**/* anotherBitB/ohAndThis/**/* partC/**/*
        ...` rather than `<tool> build **/*` or testing
        by some other more appropriate selection criteria, such as
        test size. Consequently, chronic
        problems potentially get worse, and continuous integration remains out
        of reach.


This case would be perfect for a fixit: broken areas of the code
        can be identified in advance and compiled into a spreadsheet; then
        people can volunteer to handle specific breakages to avoid duplicate
        effort. The team can attack these problems in one dedicated
        sprint, can make the event festive and fun, and the code will be in a
        state conducive to continuous integration and testing at the end of
        the day—hopefully. Even if everything isn't fixed right away, the team
        should be encouraged by tangible progress made to resolve a chronic
        issue, and should have gained insights that will motivate them to
        eventually solve the problem completely.


### Eschew Authoritah


The best solutions are not those imposed top-down; the best
        solutions are those that individuals independently perceive as
        providing value and embrace willingly. Often those solutions will
        provide people with a sense of empowerment and purpose, as opposed to
        forced solutions that produce feelings of powerlessness and
        senselessness. Resist the temptation to solve problems by issuing
        orders, or asking managers or executives to issue orders on your
        behalf; they will almost certainly backfire. People hate being told
        how to do their jobs; you know how programmers hate that exponentially
        more than most.


To that end, emphasize the goal you're trying to achieve, rather
        than insisting on the exact way to achieve it. Provide clear, concrete
        ideas, but allow people the flexibility to adapt them to their
        situation. Very few programmers will argue that reducing the number of
        build breakages, rollbacks or late-night fire drills is a bad thing.
        Unit tests, continuous integration, and code reviews are ways of
        reducing stress, increasing confidence in the code, and spending less
        time diagnosing and fixing problems that have worked for many
        different teams in many different situations to solve similar
        problems; but no two sets of unit tests, continuous builds, or code
        review practices are exactly alike.


Soliciting support from management or executive management is
        another matter. Encouragement and endorsements can raise the
        visibility of your efforts in a helpful way, so long as they are
        presented as suggestions rather than orders from on high.


In contrast, if management is passive, keep plowing ahead as best
        you can; at least they aren't obstructing or threatening you in any
        way. If management is actively hostile or dismissive, then the choice
        becomes harder. Is pushing for change worth risking your job over? Is
        it worth quitting? These are risks you have to weigh for yourself; but
        despite the unpleasantness of getting fired or quitting, that doesn't
        mean it isn't worth trying. You do have a choice, like it or not, and
        you will have to live with it.


Also, remember that no matter how much leadership and
        responsibility you assume, you are the boss of no one. You are helping
        everyone do their best work, just as they are volunteering to help you
        with yours. Stay focused on the shared outcome you all desire, not
        your ego.


### Trust Yourself


Changing a development culture is not a formulaic affair; we can't
        just plug in the right data and get the desired results. Perhaps one
        day someone will produce a formal academic study and collect
        universally agreed-upon metrics that make a reasonable case for the
        effectiveness of unit testing, but even that's no guarantee that
        people will listen and change their behavior. By way of analogy, the
        [scientific research confirming the
        efficacy of having doctors wash their hands in preventing
        infections](http://www.cdc.gov/handwashing/publications-data-stats.html) has been collected for over a century, and research
        continues to this day. Despite this significant body of evidence,
        [some doctors still need to be reminded
        to wash their hands for their patients' sake](http://well.blogs.nytimes.com/2011/09/01/getting-doctors-to-wash-their-hands/).


Despite the lack of formal research at this point in the industry's
        history, the long-term benefits produced by the experience of (good)
        unit testing are observable phenomena that have been reproduced many
        times. Many teams have collected data on defect rates and other
        factors that they consider reflective of improvement in quality and
        productivity; ideas for such are considered in the
        Measure, Enforce, Strive subsection
        below. Once you've gained experience with unit testing—especially if
        you've had success with it on another team, or at another
        company—there's nothing wrong with relying on âin my experienceâ
        arguments. Isn't your experience a big part of why your team or
        company hired you? Ostensibly they must value that experience to some
        degree; don't underestimate it. Though I advise âEschew Authoritahâ,
        you're not saying âbecause I say soâ, you're saying âbecause I've done
        soâ, and you can point to your concrete efforts and
        achievements. Big difference.


This is because arguing from a position of experience isn't
        hand-waving, so long as you have actual experience to point to.
        For example: saying that âgoto failâ and Heartbleed could've been
        detected by unit tests might be hand-waving; producing the working
        proof-of-concept code isn't. Saying that your code is âtoo hard to
        testâ is hand-waving; saying it doesn't have to stay that way, because
        the Google Web Server went from horribly crufty to well-oiled thanks
        to disciplined unit testing practice, isn't.


It's lovely to have a conscience and a degree of humility, and to
        take care not to oversell the benefits of unit testing or automated
        testing in general, but don't forget to trust yourself. Conscience and
        humility are useless without confidence—which is ultimately a function
        of experience, not data.


### Maintain Focus


The ultimate goal of culture change, whether it's to drive unit
        testing adoption or achieve some other outcome, is to make everyone's
        lives better in some way. Unit testing is a means to an end, namely
        fewer defects, increased productivity, and business success, all of
        which hopefully translate into developer and user happiness. It's easy
        to lose sight of this when we're deeply focused on technical,
        tactical, or strategic discussions. It's important to discuss such
        things, but it's at least as important to keep the association between
        unit testing and its long-term benefits in clear view.


To that end, make sure to check in with everyone involved in the
        effort, as well as the folks you're trying to influence, to the extent
        possible. However informally this takes place—over coffee or lunch, in
        passing comments during team meetings and code reviews, etc.—make it a
        habit to seize every opportunity to solicit feedback and correct
        course. Cultivating this habit will also subtly influence folks to
        think more about unit testing issues and opportunities, slowly opening
        everyone's minds to larger changes over time.


### Develop Fingertip Feel


[Fingerspitzengefühl](http://en.wikipedia.org/wiki/Fingerspitzengef%C3%BChl) is a term
        that originated in a military context which implies an extreme
        situational awareness. Learn how to sense who is handling and doing
        what, where, and when. You don't need to do everything yourself, but
        you need to know what's going on so that you can better direct the
        action carried out by your team, your community.  Encourage others to
        foster the same sense, to remain open and sensitive to opportunities,
        and to seize them when the time is right.


### Let a Strategy Emerge


It's not important to start off with a grand strategy in mind, but
        try to build the community such that it's well positioned to act on
        one when it appears. In fact, I'd argue that the best strategy at the
        beginning is to focus on building the community, rather than worrying
        about what the community will accomplish one day. When the right
        strategy comes along, and people have developed their sense of
        fingertip feel, the community will then already naturally know what to
        do to implement it. (My reference being, of course, how the
        Testing Grouplet rolled various
        ideas around for a couple years before the grand, unified
        Test Certified strategy emerged.)


That said, it's good to look for areas of focus that show promise.
        High-visibility software bugs and development project failures are
        great ones. As I did with âgoto failâ and Heartbleed, use them to
        illustrate in as concrete and in-depth detail as possible the value
        of unit testing. Build case after case after case, and build up the
        community's sensitivity to such opportunities. Encourage community
        members to produce blog posts and talks—and maybe even take some of
        those on the road, giving talks at local Meetups, various companies
        and conferences. (After all, what is a Meetup if not a very
        localized, periodic conference?) Find promising speakers and
        authors and gently encourage them to do even more.


If this particular angle doesn't appeal to you, find another
        suitable, promising thread and keep pulling on it to see how far it
        can go.


### Find a Mentor


It's always very, very helpful as you're trying to pull all of this
        together to have a mentor in whom you can confide and from whom you
        can solicit advice. Ask anyone and everyone who you think could
        provide you with solid guidance; they may not be interested or have
        the time, but it's cheap and painless to ask. Many times folks are
        quite flattered, and will readily accept; or if they can't, they may
        recommend someone else and arrange an introduction.


Either way, put your feelers out. Don't try to keep all this up on
        your own.


### Work With Nature, Not Against It


Be fully aware of your audience. Different people are responsive to
        different forms of persuasion; some will never be persuaded at all,
        and must be dragged along by history. Influence people one-at-a-time,
        by providing them with the insights and experiences that resonate most
        deeply. If there are common excuses, fix the root problems. If it's âI
        don't have time to testâ, then make the tools faster; if it's âMy code
        is too hard to testâ, then provide information and examples of how to
        make it easier to test. Volunteer to work with someone to write tests
        for a tricky piece of code. Persuasion is always preferable to
        enforcement, but seek out either opportunity and take your chances
        when you get 'em.


### One Team at a Time


Though the Testing Grouplet's goal was to change all of Google,
        that goal was ultimately achieved one team at a time. The Test
        Certified program provided a step-by-step plan to improve unit testing
        practice and coverage at a single-team level, and provided mentors to
        help each team answer questions and make progress. Trying to change
        the company as a whole from the top down is likely doomed to failure,
        and not likely to endure even if it appears to succeed in the short
        term.


### Measure, Enforce, Strive


One of the challenges for any development approach is measuring its
        effectiveness. Doubters may understandably ask you to âproveâ that
        investing in testing is worth the cost. Just as with any other
        development choice (such as which language, framework, or IDE to
        use) there are many factors that make this difficult to measure
        cleanly. Instead, measure what the team considers meaningful in terms
        of its current goals and issues. Watertight metrics may be impossible
        to achieve, but you can make progress using any reasonable proxy that
        people are unlikely to game for their personal benefit. For example,
        the team may have a set of features it hopes to deliver this quarter;
        it may want to reduce the frequency of reported defects or emergency
        launches; or it may want to increase the frequency of regular
        releases. At the same time, institute a Test
        Certified-like program to collect test metrics, establish
        policies, and work towards testing goals. Over time, progress on Test
        Certified-like goals should correlate with progress on the other team
        goals. On a logical level, correlation doesn't prove causation, but on
        the experiential level, there should be an understanding that unit
        testing has had a positive impact.


It's very difficult to measure all the problems that didn't happen
        because they were caught by tests, or all the issues that a developer
        uncovered while choosing and writing tests. You can measure side
        effects like release cycle speed, rollback frequency, and reported
        bugs, but in the beginning of a project that hasn't done testing,
        you're taking a lot of the benefit on faith. On some teams,
        experimenting with unit testing for a few months and following up with
        a developer survey (âDo you feel the code is getting healthier? Are
        you less worried your change will break something in production? Do
        you uncover bugs when writing tests?â) might demonstrate to a dubious
        management that testing is helping the team.


### Make a Stand


If people dismiss your results and demand further evidence of unit
        testing efficacy, point to the increased degree of developer
        confidence, productivity, and happiness, as well as increased user
        happiness if such data is available. Can skeptics measure these same
        outcomes, and the ultimate value delivered to the customer, with
        regard to other factors? Programming language choice? Code editor
        choice? Holiday parties, conferences, offsites, and bonuses? If we're
        going to pick on testing for a lack of hard data justifying its
        practice and confirming its value, let's go all the way and produce
        the academic research that went into all these other technical and
        business decisions and the indisputable empirical evidence
        demonstrating their impact.


The point is, a lot of factors go into the production of a
        successful team, product, and business. Not all of them are perfectly
        measurable, but that's no reason not to adopt them, because we have a
        sense that the sum of the effects is greater than that of the
        parts. Unit testing is no different from many other business factors
        in that regard.


If people try to claim that unit testing won't work because their
        situation is âdifferentâ, stand up to such baseless dismissal. You
        can argue from a position of strength that there are many, many
        different people with many, many different experiences who will all
        vouch for the efficacy of unit testing. The differences between those
        people, teams, products, and experiences strengthen the argument for
        the efficacy of unit testing rather than weaken it. The only
        requirement to overcome the challenges to unit testing presented by
        any âdifferencesâ is the courage to try. Spare no opportunity to
        expose cowardice masquerading as reason.


### Be Redundant and Repeat Yourself


Not everyone will respond to your first set of arguments. Different
        people will respond differently to different explanations. Experiment
        to find the best way to communicate your ideas to different people.
        Keep reworking your ideas to find ways to make them appealing to a new
        audience.


### Man on the Moon


Start with incremental steps towards achievable short-term goals,
        but don't be afraid to set huge goals and take a leap towards them
        when the time comes. The Testing
        Grouplet started by hosting talks, producing internal training
        materials, and handing out books. Eventually it grew bolder, launching
        Testing on the Toilet and running
        Testing Fixits. It was only after a
        couple years' worth of experimentation that the grand
        Test Certified strategy fell into place, and
        it still took a couple years before TAP
        finished the job. Our success came about by first recruiting a small,
        enthusiastic group of volunteers; working together to build a solid
        community and a foundation of tools and practices; then setting an
        extremely aggressive goal.


Your efforts should follow a similar arc. Once you've got enough
        teammates on board, and have measurements, policies, and goals
        in-place for your team, you've got a âMan on Earthâ. Now you can set
        your sights higher. You can organize a Fixit for your team, or maybe
        several teams in your office, keeping a spreadsheet of goals, tasks,
        and people assigned to each task. Having pulled off a successful unit
        testing-focused event, you now have a âMan in Orbitâ. Reflecting on
        the lessons from that event, and riding on the momentum produced by
        it, you're set up to take a shot at putting a âMan on the Moonâ and
        changing your entire company.


And once your company has gotten hip, maybe you've got a crack at
        putting a âMan on Marsâ and changing the entire industry. It's
        something to think about.


### Persevere


Convincing people of the value of unit testing isn't always going
        to be easy. Rely on your support network; lean on them for
        reinforcement and relief. You don't have to fight the battle all by
        yourself. Delegate. Let others take the lead at times while you
        recharge. Be ready to step back up when someone needs to lean on
        you.


### Follow Through


Even if you achieve your most ambitious culture-changing goals, the
        job really is never done. Healthy cultures require vigilant
        maintenance, and the next giant step beyond establishing a unit
        testing culture is to teach good automated testing aesthetics. This
        isn't limited to the unit testing level; the full spectrum of unit,
        integration, and system tests should be brought to bear to ensure high
        code quality, and people need to be educated as to the appropriate
        application and best practices of each level of testing. Remember,
        people may become convinced to adopt automated testing, but that's no
        guarantee they're going to do it well.


Absent guidance and feedback, people may write extremely elaborate,
        complex, difficult-to-maintain tests against badly organized code or
        poorly written APIs. Heavyweight integration-scale tests may check
        trivial things. People may write tests that have high costs and low
        value without even realizing it, such as tests that flake out due to
        checking for the wrong thing (e.g. testing whether a specific pixel is
        blue, rather than checking whether the page finished loading), or
        tests that have needless redundancy. There'll always be some people
        who'll take a good idea a bit too far, or in a bad direction. That
        doesn't mean the idea lacks value, just that no idea standing on its
        own is impervious to abuse.


A suite of well-written automated tests can be a powerful tool to
        confirm that your code works as intended and that it's cleanly
        organized and decoupled (thanks to the design pressure exerted by the
        practice of automated testing). However, automated testing is a skill
        like any other, takes time and effort to develop, and there's always
        room for improvement. The goal isn't to achieve perfect test coverage
        by any means necessary, it's to make development as efficient,
        effective, and reliable as possible. Once you've convinced people of
        the value of automated testing, help them continuously improve their
        skills to ensure that their tests help achieve this goal.


### Reward and Recognize


Few things in life are more disappointing that pouring your life
        into something important, that makes a difference, only to have that
        effort largely ignored—or worse, to have someone else take credit for
        it. Don't let that happen to the people who are standing with you to
        make real change happen. Don't pour it on thick, but do make a habit
        out of letting people know their efforts are acknowledged and
        appreciated.


### Make It Fun


Never underestimate the power of fun in achieving an ambitious
        goal. Fun lightens the burden and bonds people to one another. Fun
        makes for great stories that you'll love telling to your grandkids—or
        at least new junior developers that join your team or your company
        long after the deed is done.


## Final Thoughts


If unit testing doesn’t require any extra tools, doesn’t
      require rewriting everything in a new language, augments the
      application of other tools and practices, can be applied
      incrementally to existing code, incurs a cost no greater than
      learning any other new technology or product domain, has become the
      expected cultural norm of one of the most complex development
      operations in the world, and is capable of detecting or preventing
      catastrophic bugs that can slip through every other possible
      safeguard and layer of testing, the big question is:


Why isn’t unit testing a part of every development culture?


Some programmers and teams just don't know about unit testing
      and what it can do for them, lack experience with it, or need help to
      get started. Hopefully this article makes a persuasive argument that
      convinces them to adopt the practice of unit testing. As an encouraging
      example, [the OpenSSL project itself has
      been receptive to my offer to help increase unit/automated test
      coverage](https://groups.google.com/forum/#!topic/mailing.openssl.dev/-kpZAajd3f4), and I am actively recruiting people to help out with
      the effort.


Beyond that: Developers neglect to write unit tests because
      their teams or companies at best tolerate the absence of tests,
      and at worst actively discourage them. Such teams often claim
      that they “don’t have time to test”, or that their code is “too
      hard to test”. This may be due to willful ignorance,
      indifference, bad past experiences, corporate incentive
      structures and pressures, or stereotypical cowboy-coder
      machismo. Whatever the primary motivation, [the
      effect is maintenance of the status quo](http://modelviewculture.com/pieces/the-making-of-myths), justification of the
      easy way out. âBugs happenâ because accepting that as a foregone
      conclusion is a lot more comfortable than making a change in one's
      habits or surrounding culture. And it's convenient that the public is
      willing to buy that excuse because they have no reasonable way of
      knowing any better.


As developers, the caretakers in which an under-informed
      public has placed its (arguably undeserved) trust, we
      can and must do better than this. Easy, convenient excuses may
      help us all blow past the discomfort of controversy, but they
      accomplish nothing genuinely productive.


If we do not rise to overcome the cultural obstacles to the
      adoption of unit testing, we withhold one of the most effective
      development tools at our disposal from being applied to the
      real challenge of preventing expensive, embarrassing, and
      potentially dangerous software defects. By allowing empathy for
      fellow programmers (and the secret fear of being judged
      ourselves) to cloud our judgment, leading us to draw quick and
      comfortable conclusions that excuse otherwise preventable
      defects as a matter of course, we become just as guilty of
      whatever damage may result as any programmer, team, or company who
      produces such defects in the absence of unit testing.


“Culture” is the least tangible explanation we can provide
      for technical failures, especially to users with no background
      in software development—hence the press’s eagerness to accept
      reasons it can comprehend and run stories upon, as
      comprehension provides the illusion of control over events.
      Culture is also the least comfortable reason we’re able to give
      ourselves, as an admission of culture failure provokes
      identity-based psychological conflicts that pointing to external
      factors largely avoids. However, avoiding this uncomfortable
      truth is to continue to tolerate the overconfidence which produced
      “goto fail” and Heartbleed and the damage they have done to a
      largely unaware, trusting society that has come to depend more
      and more on software as a means of doing business and living life
      efficiently, securely, safely.


Hand washing alone does not a doctor make, nor a patient save,
      but we would not trust a doctor who didn’t wash his or her
      hands. As software developers, we should assume a similar
      [duty of care](http://en.wikipedia.org/wiki/Duty_of_care) on behalf of our users. No
      one should trust software developed without unit tests.


---
