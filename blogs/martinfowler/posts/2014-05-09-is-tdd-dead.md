---
title: "Is TDD Dead?"
description: "David Heinemeier   Hansson, the creator of Ruby on Rails, gave a keynote at RailsConf   where he declared that TDD is Dead. This caused a predictably large   amount of controversy in both the Rails an"
date: 2014-05-09T00:00:00
url: https://martinfowler.com/articles/is-tdd-dead/
slug: is-tdd-dead
word_count: 6031
---


# Is TDD Dead?


A series of conversations between [Kent Beck](https://twitter.com/KentBeck),
[David Heinemeier Hansson](http://david.heinemeierhansson.com/), and myself on the topic of
[Test-Driven Development (TDD)](https://martinfowler.com/bliki/TestDrivenDevelopment.html) and its impact upon software design.


## Where This Came From


A provocative talk and blog
    posts has led to a conversation where we aim to understand each
    others' views and experiences

moreâ¦

This conversation began as a consequence to [Davidâs RailsConf keynote](http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html) where he expressed his unhappiness with TDD and Unit Testing in the Rails community. He shortly followed this with some blog posts, the first of which declared that [âTDD is deadâ](http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html).


A couple of days after this, I sent him a typo correction to a follow-on post, and he said heâd welcome my thoughts on his talk and blog post. We then had an enjoyable and thoughtful discussion for an hour on Skype. David had a similar discussion with Kent, and Kent suggested that we continue the discussion with all three of us, and make the conversation public. David tweeted the idea and got a lot of positive reactions.


We didnât have much of a plan for this series, other than a rough notion of half a dozen 30 minute conversations. We mostly did this because we wanted to learn about each othersâ experiences and points of view - weâre just narcissistic enough to think lots of other people wanted to watch us. We didnât take questions in the early episodes, but did take a couple in the last one. As we did this we enjoyed how the discussion continued on blogs and twitter.


Weâd like to thank Thoughtworks, in particular Wesley Clock, for helping by doing much of the logistics of organizing the video setup and arranging the hangout times. After each episode I wrote up minutes of the discussion for those that preferred to read rather than watch.


## 1: TDD and Confidence


9 May 2014


[video](https://www.youtube.com/watch?v=z9quxZsLcfo)


[audio](http://assets.thoughtworks.com/podcast/is-tdd-dead-episode-1-09-may-2014.mp3)


We talk about our varying experiences with the flow of TDD, and
      the way TDD and self-testing code are often confused.


moreâ¦


### Minutes


David opened the discussion by raising his three major issues
        with TDD and Unit Testing: 
        confusion over the definition of TDD
        and unit testing, test-induced damage through using mocks
        to drive architecture, and how the red/green/refactor cycle of
        TDD never worked for him. 
        I commented that to understand
        where TDD etc came from, it's useful to understand the history, so
        Kent explained the origins of TDD. He began by trying
        things out in Smalltalk, finding that TDD worked well for
        his personality.


I commented that when we first worked together at C3, we
        didn't start using TDD, but ensured each programming episode
        delivered code and tests together. Kent said that
        programmers deserve to feel confident that their code works, TDD
        is one (not the only) way to reach that. David likes Ruby's design goal of programmer
        happiness, and is on board with the notion that you're not
        done till you have tests - but doesn't like TDD as a way to
        get there. He thinks people
        have different brains and thus like different techniques and
        languages, he doesn't like that TDD gets conflated with the
      confidence you get from self-testing code.


Kent talked about a recent hackathon at Facebook, about half
      of which he could use TDD and half wasn't suitable. In the
      TDDable code he found he was in an enjoyable flow, but found the
      other part more tricky. But in the non-TDD part he still used regression tests and short
      feedback loops. He has no problem mixing both styles,
      it's like playing both classical and jazz. TDD reminds
      him of how he learned mathematics at school - always needing examples.


David has been in situations where TDD flowed well, but most
      of his work isn't like that - his question is what are you
      willing to sacrifice to get that flow? Many people make bad
      trade-offs, especially with heavy mocking. Kent thinks
      it's about trade-offs: is it worth making intermediate results
      testable? He used the example of a compiler where an
      intermediate parse-tree makes a good test point, and is also a
      better design. But in response to David's question about
      mocks, he said he rarely uses them,  he's concerned that
      those that do often find refactoring difficult, while he finds
      testing makes refactoring easier.


I comment that there are two problems with terminology where
        different things get conflated:
         first that DHH's critique of TDD
        was based on an assumption that you had to use heavy mocking in
        TDD, which isn't the case; second that there is a difference between
        self-testing code and TDD. TDD is one way to achieve
        self-testing code. David said his reaction was to seeing people describe TDD in a
        mock-heavy style as a moral thing to do  and the result was a lot of code that was
        poorly designed due to its desire to enable isolated unit
        tests.


I finished by playing time-cop and saying that in the next
         session we'll explore how TDD may lead to damage, if that is
         really damage, and how we can judge if it's damage.


### Further Reading

- David's [RailsConf talk](https://www.youtube.com/watch?v=9LfmrkyP81M) that started it all off.
- David's essays on [TDD is
        Dead](http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html) and [test-induced design damage](http://david.heinemeierhansson.com/2014/test-induced-design-damage.html).
- My distinction between [self-testing code](https://martinfowler.com/bliki/SelfTestingCode.html) and [TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html).
- My approach to [defining unit tests](https://martinfowler.com/bliki/UnitTest.html)


## 2: Test-induced design damage


16 May 2014


[video](https://www.youtube.com/watch?v=JoTB2mcjU7w)


[audio](http://assets.thoughtworks.com/podcast/is-tdd-dead-episode-2-16-may-2014.mp3)


David feels that using TDD leads to approaches such as
      hexagonal rails that is test-induced design damage due to
      the complexity of excessive indirection. Kent thinks it's less
      about TDD and more about the quality of design decisions.


**Before watching this conversation **
      you should look at [the gist David
      prepared](https://gist.github.com/dhh/4849a20d2ba89b34b201) to show an example of the design damage he is
      concerned about. You might also watch the video where the
      much-missed Jim Weirich [explores this approach to a hexagonal architecture](https://www.youtube.com/watch?v=tg5RFeSfBM4).


moreâ¦


### Minutes


I began by opening with questions. Can TDD lead to design
        damage? Is the resulting damage really damage? How do we judge
        if a design is damaged or not? David describes [the gist he posted earlier](https://gist.github.com/dhh/4849a20d2ba89b34b201). It's an
        example of the kind of architecture he sees people arriving at
        using TDD with lots of mocks. Each layer of the 
        application is separated, eg a controller can be tested
        without talking to real models, databases, or the
        request/response cycle. What matters to David isn't the specific example, so much as
        the unnecessary indirection and complexity required to make it
        easier to test in isolation.


Kent said that ascribing test-induced damage to
        TDD was like driving a car to a bad place and
        blaming the car for it. The design David showed wasn't due to
        TDD, the real issue is that these indirections are all good
        tricks under some circumstances and we need to understand
        whether they are worth the cost or not. David disagreed, saying that once you jump on the TDD horse
        (or car) it encourages you to go a certain way  - it leads to a
        monstrosity one test at a time. Kent countered that it was rather
        one *design decision* at a time. TDD puts an evolutionary
        pressure on a design, people have different preferences for
        the grain-size of how much is covered by their tests.


Kent asked David what kinds of thing he wanted
        to do with the gist that its structure made hard.
         (âIf it's just sitting there who
        cares - 
        it's when I want to change it that the design actually
        mattersâ). David replied that there's a direct correlation between the
        size of code and how easy it is to change it. All these
        indirections have to be kept in sync, something that's 10
        lines of code is easier to understand and change than
        something that's 60 lines of code. Every layer of
        indirection introduces a high cost. David continued by
        saying that TDD's red/green/refactor flow was very addictive  (Kent observed
        that he's the poorest drug dealer on the planet)  and
        this addiction led people to these poor decisions. 
        I disagreed with this, saying it wasn't due to TDD but due to
        a desire for isolation,  the essence of a hexagonal
        architecture being isolation from its environment (in this
        case Rails).


David said the reason people wanted isolation
        was due to TDD, he'd heard various arguments for isolation, but
        only the testing one made sense. He thinks the idea that someone wants to turn a rails
        application into a command-line application is so rare it's
        laughable, similarly you can't just swap out an in-memory store for a
        call to a web service because they have different operational
        characteristics. These swapability pipedreams aren't
        the real goal - the real goal is isolated testing. Kent agreed that you can't treat in-memory and web services
        the same (âyou may think you're decoupled, but you're really,
        really notâ) as the failure cases are different. The boundaries between elements will leak to some degree âthe
        question is how much are we willing to spend to get how much decoupling between elementsâ.


Kent saw the difference between 10 lines of code and 60 as a
        cohesion issue. David agreed but argued that cohesion and coupling are often
        opposed. Higher coupling is usually worth the price to get
        better cohesion. Kent observed that there are other ways to eliminate external
        dependencies, you can also use intermediate results, this is
        what happens with compilers. Something that's hard to test is an indication that you need a
        design insight, it's often useful to get up and take a walk to
        find those insights that lead to better designs that are also
        more testable. David agreed that testing can lead to better designs, but said
        his experience often was also the opposite, that there wasn't
        a good testable design. Kent accused David of not having enough self-confidence, maybe
        you can't see the insight today, so you have to make progress
        in the meantime, but he's optimistic that he will find them
        eventually. David dismissed this as âfaith-based
        TDDâ - he used to feel this but got stuck in a depressing
        loop when he wasn't finding an ideal solution that wasn't there. Kent clarified he wasn't talking about TDD, but about software
        design in general, it's not about TDD it's about how to get feedback.
        Thinking about software design is the thing, because it pays
        off so big when you get a good design insight. Getting these
        insights isn't about your workflow, it's about things like
        knowing when to work and when to rest, gathering influences
        from other places, collaborating with other people.


We finished by saying our theme next time would be to explore
        the trade-offs around how you seek out feedback while programming.


### Further Reading

- [David's
        gist](https://gist.github.com/dhh/4849a20d2ba89b34b201) to show examples of the kind of design damage he's
        concerned about. The gist is based on an exploration of a
        hexagonal Rails architecture given in [a talk by Jim Weirich](https://www.youtube.com/watch?v=tg5RFeSfBM4).
- David's blog post [introducing the problem of test-induced
        design damage](http://david.heinemeierhansson.com/2014/test-induced-design-damage.html)
- The term âhexagonal architectureâ was [originally coined by
        Alistair Cockburn](http://alistair.cockburn.us/Hexagonal+architecture), it's also less-known as âports and adaptersâ.
- Following this hangout, I did another one with my colleague Badri
        Janakiraman about [the nature of a hexagonal Rails architecture
        and trade-offs around using it](https://martinfowler.com/articles/badri-hexagonal).


## 3: Feedback and QA


20 May 2014


[video](https://www.youtube.com/watch?v=YNw4baDz6WA)


[audio](http://assets.thoughtworks.com/podcast/is-tdd-dead-episode-3-20-may-2014.mp3)


We discuss the various ways in which we get feedback while
      programming and the role of QA in providing feedback to developers.


moreâ¦


### Minutes


Kent opened by saying that decisions involving TDD were about
        trade-offs:  âin some ideal world we would have instant,
        infallible feedback about our programming decisionsâ… âevery key stroke that I make,  if the code is
        ready to deploy, it would just instantly deploy.â But that ideal is impossible at the moment so the question is
        how far do we back off from that. 
        He went to enumerate several constraints in the trade-off.

- *Frequency: *how rapidly do we want our feedback ?
- *Fidelity:* how accurate do we want the red/green signal to be?
- *Overhead:* how much are we prepared to pay?
- *Lifespan: *how long is this software going to be around,
        which is probability as well as time.


Those four are the constraints he thinks we
        need to compare. âWe're not in this hangout to agree - my personal goal
        is just to understand the set of trade-offs by articulating
        them to people who are prepared to tear my ideas apart in a
        constructive wayâ


I outline three things that we look to get feedback on.

- *Is the software doing something useful for the user of the
        software?* Sometimes tests help with this (eg payroll
        calculations) and sometimes not (eg html rendering).
- *Have I broken anything?* âThis is where self
        testing code… is such a lifesaver.â I want to see every
        test fail at least once.
- *Is my code-base healthy?* This so I can continue to build
        things quickly. This element gets more tricky when you're not
        sure who will take over the code.


David introduced the topic that TDD's success had led to a
     neglect of QA. 
     Many shops took on TDD and got rid of QA, Basecamp didn't have QA until a couple of years
     ago. 
     He thinks
     TDD got programmers to where âthey got so over-confident that
     they felt they didn't need QAâ. While the old model was broken,
     the pendulum had swung too far: âI don't think you can work on
     anything of material quality and produce great software without
     having somebody who's not *you* test it.â This is
     disappointing because he's seen how powerful it is to have a QA
     person come in.


The other issue is that to understand trade-offs you have to
       understand the costs, all the talk of TDD has been on the
       benefits. This neglect of costs is why people cannot comprehend that
       there is such a thing as test-induced damage. The trade-off continuum is true of other things. Consider the
       cost of reliability: going from 99% to 99.999% is exponentially
       more expensive than getting to 99%. We must also consider criticality. High reliability is
       important for space shuttles and pacemakers, but wrong for an
       exploratory web site. The rule of not writing a line of production
       code without a test doesn't fit in with trade-offs around
       criticality.


Kent wanted to go back to the issue of QA, he considered
           the old relationship with QA was dysfunctional. His one
           piece of Facebook swag in his office is a poster that says
           âNothing at Facebook is somebody else's problemâ and he
           feels Facebook follows that remarkably well for a
           company its size. Facebook didn't have QA until recently and programmers live
           up to that responsibility. âIt's a question of 'compared to what?'â Compared to having
           an effective QA then no-QA is worse, but no-QA is better
           than the old dysfunctional relationship. I added that at Thoughtworks we almost always have QA on
           our projects. I also feel that the big shift from the 90's
           is not just getting rid of the dysfunctional adversarial
           relationship, but also getting rid of manual scripted
           tests. And it's liberating that startups can operate
           without QA. David agreed that it was good to mindfully trade-off QA for
           initial speed, but some have taken programmer testing too
           far and don't see the value of exploratory testing. If developers think they can create high-enough quality
           software without QA they are wrong, your tests may be green
           but when it's in production users do things you don't expect.


David says that worst of all is when developers are not part of
            of customer service. Many programmers don't want to be on-call because it's
            drudgery, but it's also a feedback loop. Code with green
            tests can be a plateau that's below where you want to
            be. Kent considered that we should stipple a few red pixels
            in the green bar to remind us of these limitations . 

            âThe on-call is the feedback loop that
            teaches you what tests you didn't write.â Facebook programmers have to go on-call, everyone complains about
            it, but there's no way they are going away from it. As soon as you think you don't make
            mistakes any more, that's a mistake, and you stop growing.
            Eventually âthe world won't let you pretend that you're
            not screwing up any more.â He'd rather pay the price of catching that early with
            a phone call at 2am.


I finish by observing we didn't get to talk more about the
           costs of testing (David's second point from earlier) so
           propose that we look at that next time. I also mention that
           by chance [there's an article
           by Mike Bland
           published on my site today that looks at
           exactly that topic.](https://martinfowler.com/articles/testing-culture.html#costs)


## 4: Costs of Testing


27 May 2014


[video](https://www.youtube.com/watch?v=dGtasFJnUxI)


[audio](http://assets.thoughtworks.com/podcast/is-tdd-dead-episode-4-27-may-2014.mp3)


We discuss some downsides of testing and TDD: can you do too
      much testing, and is there a problem with teams valuing tests
      more than they value the functional code?


moreâ¦


### Minutes


David starts by saying âto talk about
      trade-offs, you really have to understand the drawbacks, because
      if there are no drawbacks there are no trade-offs.â He continued by saying that TDD doesn't force you to do
      things, but it does nudge you in certain directions.
       The first issue he wanted to raise was over-testing. It's often said you shouldn't
      write a line of code without a failing test, at first this seems
      reasonable but it can lead to over-testing, such as where there
      are four lines of test code for every line of production code.
      This means that when you need to change behavior, you have more
      code to change . 
      Kent has said 'you aren't paid to write tests,
      you just write enough to be confident' - so he asked if Kent and
      I wrote tests
      before every line of production code?


Kent replied âit depends, and that's going to be the beginning
        to all of my answers to any question that's
        interestingâ. With JUnit they were very strict about test-first and were very
        happy with how it turned out - so he doesn't think you always get
        over-testing when you use TDD. Herb Derby came up with the notion of delta coverage - what
        coverage does this test provide that's unique? Tests with zero
        delta coverage should be deleted unless they provide some kind
        of communication purpose. He said he'd often write a system-y test, write some code to
        implement it, refactor a bit, and end up throwing away the
        initial test. Many people freak out at throwing away tests, but
        you should if they don't buy you anything. If the same thing is tested multiple ways, that's coupling,
        and coupling costs.


I said that I'm sure there is over-tested code,
        indeed if anyone does it would be Thoughtworks since we have a
        strong testing culture. It's hard to get the amount just
        right, sometimes you'll overshoot and sometimes undershoot. I
        would expect to overshoot from time to time and it's not
        something to worry about unless it's too large. On the test-every-line-of-code point I 
        ask the question: âif I screw up this line of code is a test
        going to fail?â I sometimes deliberately comment a line out
        or reverse a conditional and run the tests to ensure one
        fails. My other mental test (from Kent) is only test things that can
        possibly break. I assume libraries work (unless they are really wonky). I ask
        if I can mess up my use of the library and how critical are the
        consequences of the mistake.


Kent declared that the ratio of lines of test code to lines of
        production code was a bogus metric. A formative experience for him was watching Christopher Glaeser
        write a compiler, he had 4 lines of test code for every line
        of compiler code - but this is because compilers have lots of
        coupling. A simpler system would have a much smaller
        ratio. David said that that to detect commenting out a line of code
        implies 100% test coverage. Thinking about what can break is
        worth exploring, Rails's declarative statements don't lead to
        enough breakage to be worth testing, so he's comfortable with
        significantly less than 100% coverage.


I replied that âyou don't have enough tests (or good enough
        tests) if you can't confidently change the code,â  and 
        âthe
        sign of too much is whenever you change the code you think you
        expend more effort changing the tests than changing the
        code.â You want to be in the Goldilocks zone, but that comes
        with experience of knowing what mistakes you and your team tend to make and
        which ones don't cause a problem. I said I like the âcan I comment out a line of codeâ approach
        when I'm unsure of my ground, it's a starting place but as I
        work more in an environment I can come up with better heuristics. David felt that this tuning is different between product teams that
        are stable rather than consulting teams that are handing the
        code over
        to an unknown team and thus need more tests. Kent said that it's good to learn the discipline of
        test-first, it's like a 4WD-low gear for tricky parts of
        development.


David introduced the next issue: many people used to think
        that documentation was more important than code. Now he's
        concerned that people think tests are more important than
        functional code. Connected with this is an under-emphasis on
        the refactor part of the TDD cycle. All this leads to
        insufficient energy to refactoring and keeping the code
        clear. Kent described that he just went through an episode where he
         threw away some production code, but keeping the
        tests and reimplementing it. He really likes that approach as
        the tests tell him if the new code is working. This leads to
        an interesting question: would you rather throw away the code
        and keep the tests or vice-versa? In different situations you'd
        answer that question differently.


I said I'd found situations where reading the tests helped me
        understand what the code was doing. I didn't think one was
        more important than the other - the whole point is the double
        check where there is an error if they get a mismatch. I agreed with David that I'd sometimes sensed teams making the
        bad move of putting
        more energy into the testing environment than in supporting
        the user, tests should be means to the end. I find I get a dopamine shot when I clarify code, but my biggest
        thrill is when I have to add a feature, think it will be tricky,
        but it turns out easy. That happens due to clean code, but
        there is a distance between cleaning the code and getting the
        dopamine shot. Kent showed a metaphor for this from Jeff Eastman, that is too
        tricky to describe in text. He got his rush from big design
        simplifications. He feels that it's easy to explain the value of a new test
        working, but hard to state the value of cleaning the design.


David said we often focus on things we can quantify, but you
        can't reduce design quality to a number - so people prioritize things
        that are low on the list like test speed, coverage,
        and ratios. These things are honey traps, and we need to be
        aware of their siren calls. Cucumber really gets his goat - glorification of a testing
        environment rather than production code. Only useful in the
        largely imaginary sweetspot of writing tests with
        non-technical stakeholders. It used to be important to sell TDD, but now
        it's conquered all, we need to explore its drawbacks. I disagreed that TDD was dominant, hearing many places where
        it's yet to gain traction.


### Further Reading

- On the topic of misusing measurements, take a look at Pat
        Kua's article on [an appropriate use of metrics](https://martinfowler.com/articles/useOfMetrics.html).
- I've written more on the [use and misuse of test coverage](https://martinfowler.com/bliki/TestCoverage.html).


## 5: Answering Questions


4 June 2014


[video](https://www.youtube.com/watch?v=gWD6REVeKW4)


[audio](http://assets.thoughtworks.com/podcast/is-tdd-dead-episode-5-6-4-jun-2014.mp3)


We answer questions from our viewers: what open-source examples of
    TDD exist, what changes would make us change our use of TDD, and
    how well it works for inexperienced developers. We finish by
    summing up our view of the health of TDD.


moreâ¦


### Minutes


I begin by saying we'll structure this hangout by picking and
    answering some questions submitted by viewers.

    David starts by picking a question from Mike Harris, who asks for
    examples of open-source projects that have used TDD and either got
    test-induced design damage or used TDD well. David responds by
    saying there aren't good examples and this is one of the problems
    of debates like this. We don't have good application examples in general, because open-source contributors
    often work on private applications and open-source common
    frameworks and libraries. As a result we go into these discussions with different contexts, which often makes it look like there is more disagreement than
    there really is. People come together when you have real code
    rather than philosophical principles. The code examples we have are minor examples rather than things people are
    actually working on, so you have to understand people via presentations - which is why
    he used Jim Weirich's example for design damage. For good rails
    code he suggests Rails books that show standard testing approaches.


I comment that it takes lots of effort to
      understand real code. I do some some digging into our code bases
      but it takes a lot of time, and even then it's not the same
      understanding as you get by working with the team. Kent says that [JUnit](http://junit.org/) is an example of a project that used TDD
      strictly and turned out well.  But it isn't a good example for this discussion because it has
      clear interfaces that make a sweet spot for TDD. We are talking
      here about different kinds of applications. If someone has a good example, they should write
      it up.


David says my comments illustrate that we can't treat programming as
      a science - we can't evaluate techniques objectively. This doesn't mean it isn't worth debating. We can't get a
      definitive answer, it's your job to figure out what makes
      sense. Kent agrees we can't replicate experiments, but
      says we still can look at things personally with a scientific
      mindset. We can try things out empirically for ourselves, but
      you can't get universal answers.


Kent picks the next question (asked by Graham Lee): what could
      change about the way we write software to make TDD redundent or
      obsolete for Kent and Martin and what could change about how TDD
      is performed to make it useful for David? Kent replied by saying his [RIP TDD post](https://www.facebook.com/notes/kent-beck/rip-tdd/750840194948847) points out his postion
      (if rather sarcastically). TDD solves several problems, starting
      with confidence. TDD also allows him to break problems down piecemeal, tackling
      specific cases without having to solve the general case all at
      once. He's not prepared to give up on TDD just because
      it's hard.


I say that for me it's not about changes that would make TDD
      obsolete, rather the applicability of TDD in different contexts.
      I've experienced following TDD in a mechanical way with a calm
      ârapid unhurriednessâ where I've blundered into good
      designs. Most of my programming these days is my website toolchain and
      while I do piecemeal progress, and have a good regression test
      suite - I don't find TDD applicable. But when I built the
      infodeck code, there was a lot of application behavior
      where TDD was effective.  âSome contexts are very suitable for TDD, some
      contexts less soâ. And people bring their personality into 
      that context.


David said his experience was similar. His introduction to
      testing was through TDD, he liked it and tried to apply it to
      everything but slowly realized that lots of areas in an MVC web
      application didn't feel good for TDD.  This doesn't mean TDD
      isn't effective for some situations, just that those cases are a small
      percentage of his work.  But abandoning TDD doesn't mean he wants to give up self-testing
      code - that's always been the value of TDD to him.


I say that this is exactly how someone should take on TDD (or any
      technique). Try it out, overuse it, settle into a mode that
      works for you. Then also look a bit deeper: âtdd is gateway drug
      to self-testing codeâ. Kent said he didn't mind where people end up with their workflow
      having done this kind of process. His experience of using TDD
      differs to David's. He finds there are moments in development
      where something is hard and he gets an idea of an object with a certain protocol
      that simplifies things. TDD gives him a mechanism to quickly get feedback on such an
      idea, trying and example usage of the API and implementing
      it. He also finds cases where TDD doesn't fit. He then
      finds command-R is a good way of getting feedback, but he's hoping for the moment when he can see
      the simplifying object and try it out with TDD.


I pick the next question (from Tudor Pavel): how does TDD work
      with less experienced developers. I reply by saying that TDD
      forces people to do small pieces and helps them separate interface
      from implementation. It doesn't guarantee great results, because
      you can't do good design without experience. When less experienced people do TDD they typically don't
      refactor enough, leading to sub-optimal designs. You can't
      compare an inexperienced developer's output to an experienced
      developer's output, you have to compare it to what that
      indexperienced developer would have done without tdd. Although
      we can't measure this, it does seem to be advantageous, and
      creates a self-testing code base which is easier to improve
      later through refactoring. So TDD gives you a good start
      point.


David said that was the value he got from TDD. He started with
      TDD and found it was great training wheels, however he felt the
      discussion didn't move on enough since.  He's skeptical when people say you must give simple, direct,
      bombastic advice to new people otherwise they won't do it. That
      shows a lack of confidence in what you're teaching. I agreed with that dislike for dogmatic statements. I get
      suspicious if I can't find arguments against something I'm
      describing. One twist, however, is that we do have to keep
      repeating introductory stuff for new people: some people resist
      repeating the basics.


David thinks this is why we're having this conversation now. As
      people describe TDD they add their own spin to the basics, after
      ten years of this you end up a long way down the road from where you
      started, and not in a good place. You need to hit the reset button, an approach that's crude but
      effective. When he says TDD is dead, he's referring to this
      current mutation - we have to get back to first principles. Kent said his gut reaction to David's original
      keynote was at that level. Programmers will often do the same
      thing many times, make things too complicated, and stick with
      dysfunctional systems at work. He's happy to reboot to first
      principles, but doesn't want to lose the evolution of people's
      expectations about programming in the last ten years. You should
      be able to feel confident, point to progress, have productive
      technical collaborations. He feels he can be his whole self at
      work now in a way that he couldn't be when he started his career.


David thinks that several things came together at
      the same time : TDD, XP, and Ruby. People laughed at the notion
      that programming should be fun, but he wanted to continue with
      that notion in developing Rails. Now he thinks that the Ruby world takes
      that happiness for granted - these things have won - as has
      agile. I disagree that agile has won - the label has
      won, but many people say they do agile but don't really. This is
      typical for things like this, a process I call [semantic
      diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html). The big win is that now we are able to do agile
      openly at clients. David observes this reboot problem with other things -
      after ten years you get lots of cruft. He used the example of
      Pinkberry which started with just two flavors, but then got
      a complicated range of flavors just like other ice-creams -  âmost people can't leave good ideas the fuck
      alone.â TDD and Agile are very broad tents now. People who say they are
      doing agile do opposite things. Kent says that he hasn't seen the things with TDD that David
      has. He always applies TDD from first principles in his work.


Kent appreciates that David has brought attention to TDD acquiring
      some barnacles and needs some scraping. David said he's seen similar issues with Rails. He uses Rails in
      its basic form and is shocked by some Rails usage he's
      seen. Kent remembers the first OOPSLA when XP got
      attention, Jim Rumbaugh said you won't recognize what happens to
      XP in ten years and he was right. I said that this is what success looks like, the
      alternative is that things don't take off. It's always hard to tell if
      something bad happens due to something inherent in a technique
      or due to misuse of a technique. All we can do is keep repeating
      the basics and the good lessons. David agreed:  âyou either die a hero or become
      the villan.â Ruby was a reboot of good ideas about programming. Functional
      Programming is another reboot. These reboots are healthy. He's impressed by how long Rails and TDD have
      lasted. Before Rails he worked with PHP. You can write good code with
      PHP if you use it well, he feels that other languages do a
      better job of encouraging good usage. He things that using TDD well
      in an MVC web app is harder than writing clean PHP.


Kent hasn't found that - any time he can break off a piece of a
      problem into a useful abstraction he can use TDD. He wants to
      explore other avenues to these big goals of bringing his whole
      self to programming. He will continue to explore this with
      experiments:  doing it too much, not enough, finding the golidlocks
      zone, and understanding why. He comes out firmly contradicting David: TDD isn't dead, but is
      glad David set fire to it so it could come out like a phoenix.


David said he started this discussion because people wouldn't
      talk about cases where TDD wasn't effective. They weren't
      feeling good or confident, but were told they must use TDD. He
      wants to open the sphere of acceptable reactions so we can
      discuss when TDD is and isn't appropriate.  Lots of people on the internet talk about how good TDD is, but
      people were afraid to say it wasn't working for them. For David
      the baby is self-testing code, we don't want to lose that when
      questioning TDD.


I concluded by saying that (as I suspected before we started)
      there is lots we agree on. We all value self-testing code a lot,
      we all agree TDD is valuable in some contexts, we might disagree
      on how many contexts (although it's hard to really tell).  Everything still boils down to the point that
      if you're involved in software development you have to be
      thoughtful about it, you have to build up what practices work
      for you and your team, you can't take any technique blindly. You
      need to try it, use it, overuse it, and find what works for you
      and your team.
      We're not in a codified science, so we have to work with our own
      experience.


![](mf-kb-dhh.png)


To join in this conversation, tweet with the [#isTDDDead hashtag](https://twitter.com/search?f=realtime&q=%23isTDDDead&src=typd).


Weâve added audio for all these discussions to the Thoughtworks podcast feed which you can get via [itunes](https://itunes.apple.com/us/podcast/thoughtworks/id881136697?mt=2) or [soundcloud](https://soundcloud.com/thoughtworks).


If you enjoyed this video, you might enjoy
[this conversation I had with Badri Janakiraman](https://martinfowler.com/articles/badri-hexagonal/) where we go into
more depth on hexagonal architecture, whether to use Active Record or
Data Mapper, and whether to treat Rails as a platform or a suite of
components.


There are also more articles on this site on the topics of [testing](https://martinfowler.com/tags/testing.html)
and [ruby](https://martinfowler.com/tags/ruby.html)


These pages, including the minutes of our conversation, have been
translated into [Korean](http://jinson.tistory.com/271)

Korean translation from ê¹ì§ì <pub.jinson@gmail.com>