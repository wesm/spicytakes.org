---
title: "Conversation: LLMs and Building Abstractions"
description: "Unmesh and Martin exchanged some emails about building abstractions   while working with an LLM. They talk about the influence of Brooks's framing of   essential and accidental complexity, and how thi"
date: 2025-08-26T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/articles/convo-llm-abstractions.html
slug: convo-llm-abstractions
word_count: 2972
---


A few weeks ago, we exchanged some emails sharing how we were thinking about how
      programmers work with LLMs. We found the conversation to be stimulating,
      and thought it would be worth sharing with a wider audience. We switched
      from emails to building up this conversation in a file, and doing some
      editing to improve the flow (and make us sound more coherent).


Unmesh


I am always a bit annoyed with all the claims happening around the
      world with the role of LLMs in software development. I was re-reading some of
      the articles and write-ups from the early days of agile to structure my
      thoughts. I thought Fred Brooks classic[ âNo Silver
      Bulletâ](https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html) articulation can be helpful


Martin


When I got into my first job, early mentors of mine
      encouraged me to read Fred Brooks's [The Mythical Man Month](https://archive.org/details/MythicalManMonth/page/n9/mode/2up). One of the themes of this
      was importance of conceptual integrity.


> I believe that large programming projects suffer management problems
>       different in kind from small ones, due to division of labor. I believe the
>       critical need to be the preservation of the conceptual integrity of the
>       product itself.
> -- [Frederick P. Brooks, Jr](https://archive.org/details/MythicalManMonth/page/n9/mode/2up)


Shortly afterwards âNo Silver Bulletâ was published, and we felt it was
      one of the most important articles thus far in our profession. The
      distinction he made there between accidental and essential complexity has been in the
      front of my mind ever since.


> Following Aristotle, I divide them into essence, the difficulties
>       inherent in the nature of software, and accidents, those difficulties that
>       today attend its production but are not inherent.
> The essence of a software entity is a construct of interlocking
>       concepts: data sets, relationships among data items, algorithms, and
>       invocations of functions. This essence is abstract in that such a
>       conceptual construct is the same under many different representations. It
>       is nonetheless highly precise and richly detailed.
> I believe the hard part of building software to be the specification,
>       design, and testing of this conceptual construct, not the labor of
>       representing it and testing the fidelity of the representation.
> -- [Frederick P. Brooks, Jr](https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html)


Unmesh


Understanding the difference between essential and accidental complexity provides clear guidance on where to apply LLMs for simplification.


I find this distinction between accidental and essential complexity
      very useful. I think it is a good way to think about the difference
      between the complexity of a system and the complexity of the process of
      building a system. I think this distinction is also useful for thinking
      about the role of LLMs in software development. Programming language syntax, 
      complexity of integrating various frameworks. All the boilerplate required just to get
      the software running is all the accidental complexity. I think LLMs are good
      at reducing accidental complexity. Need a Spring Boot service that talks 
      to Kafka and logs with OpenTelemetry? An LLM can spit out a working template 
      in seconds. But real software work is more than making code compile.
      The very act of writing software is a complex process. 
      While currently a lot of focus is on using LLMs to generate code, 
      it's important to think about what the act of 'writing code' really means.


Programming isn't just typing coding syntax that computers can understand and execute; 
      it's shaping a solution.
      We slice the problem into focused pieces, bind related data and behaviour together, 
      and—crucially—choose names that expose intent. Good names cut through complexity 
      and turn code into a schematic everyone can follow. 
      The most creative act is this continual weaving of names that reveal 
      the structure of the solution that maps clearly to the problem we are trying to solve.


Programming isn't just typing coding syntax that computers can understand and execute; 
      it's shaping a solution.


Yet no one sees the whole design on day one.
      Progress comes from a back-and-forth rhythm: think a bit, write a bit, 
      step back, and refine what you see. Each iteration sharpens both the code 
      and your understanding of the bigger picture, allowing us to
      guide the next steps. The very act of âwriting codeâ is often where design
      decisions crystallize.


In the software world, 'Impossibility Results' are a way to keep us grounded.
      They help us focus on solutions once we know what the real constraints are,
      instead of assuming that constraints don't exist.
      Understanding the basic nature of building software systems and 
      the activity commonly known as 'coding' can happen better if 
      we know 'impossibilities' better.


I like to think of this problem of 'upfront design' in terms of an impossibility
         result I call 'Upfront Specification Impossibility' (USI).


USI sets a practical limit for software design: the first spec is at
      best a hypothesis. Waterfall fought USI; Agile works with it.


Martin


Indeed the idea that design and architecture is *evolutionary* is
      one of the core notions of agile software methods. And what you've said
      about weaving names inevitably brings to my mind the [Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html) notion of
      [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html). Essentially what you're
      saying is that our interaction with the LLM is building that language,
      which Eric stresses has to be done in an iterative manner.


Unmesh


Or better than saying we are *building* a language, we are *growing* a
      language - following the title of Guy Steele's 1998 OOPLSA keynote.


> My point is that a good programmer in these times does not just write programs.
>           A good programmer builds a working vocabulary. In other words, a good programmer
>           does language design, though not from scratch, but by building on the frame of a base
>           language.
> -- [Guy Steele](https://www.youtube.com/watch?v=lw6TaiXzHAE)


Martin


For me, that's the best technical talk I've ever seen (I was lucky
      enough to be in the audience). I *strongly* encourage anyone who hasn't seen it
      to set aside an hour [and watch it](https://www.youtube.com/watch?v=lw6TaiXzHAE).


I heard it was a common theme among Lispers to say that they were
      molding their environment into a language to specifically express their
      domain - and that's a mindset I generally try to follow when programming.


Unmesh


Programming is the act of growing a language


It's interesting to see how programmers âgrow the langaugeâ. Where do the words for abstractions come from?
        Some of them are borrowed from established concepts in the domain. Some are well known patterns
        which become commonplace in the vocabulary in the community of programming language or paradigms.
        âI need a Repository to access stored dataâ, âI need a Controller to handle user requestsâ or
        âI need to use a Factory to create objectsâ are all examples of abstractions which are 
        well known in the programming community.
        It's interesting to see how programming languages and paradigms which are long lived
        have this great potential to establish vibrant communities. Ruby, Smalltalk, Lisp, Java, and now
        Python are great examples of this.


In my experience, languages and paradigms provide a great guidance 
        to shape up the thinking process for the programmers. 
        When I am building data pipelines, the functional paradigm helps to 
        think about the chain of transformations working on the stream of data.
        When I am building a web application or any interactive applications,
        the object-oriented paradigm helps to think in terms of objects which 
        encapsulate the state and behavior.


as we write code, we are also learning
        the structure of the solutions


There is another subtle but very important aspect of programming,
        as we write code, and think in terms of code, we are also learning
        the structure of the solution. There are a lot of micro decisions
        that are made in a flow. Should this be a separate class? What's a good name for this function?
        I should probably try a different approach to structure this class hierarchy.
        So there are two parts, taking the decision and getting the coding done
        to execute that decision. LLMs are excellent in generating or changing
        code for very specific decisions. But to arrive at those decisions requires
        a lot of back and forth, through code. While it might look like
        developers are 'wasting time' in this process, it's actually a very
        important part of shaping up the mental model of the solution structure 
        in a given programming language. Once this mental model is clear, 
        it's a lot easier to give specific instructions to LLMs.
        This is the process which solidifies 'abstractions' - the essence of
        forming the vocabulary for growing the language.


Many times, when I hear people saying 'drive everything through prompts', I 
        sense a lot of 'upfront design' in the making. That's dangerous, as without iterating with 
        the code, you need to speculate a lot about the structure of the design.
        More importantly, you leave the decision to build the 
        coding abstractions to the LLM. Of course, a counter argument can be 
        that you review every single change. But reviews done after
        certain decisions are already codified are not as effective.
        The same reason why we prefer pair programming over
        passive reviews.


Martin


Raising the difference between pair programming and code reviews is an
      interesting point. Although much of the software development world likes
      using [pull requests](https://martinfowler.com/bliki/PullRequest.html) and [pre-integration code reviews](https://martinfowler.com/articles/branching-patterns.html#reviewed-commits), we are in the
      smaller camp that vastly prefers [pair
      programming](https://martinfowler.com/bliki/PairProgramming.html). It strikes me that if you are used to the pull request
      model, then you are used to interacting with other programmers in this
      âhere's what I've done - review itâ style. Pair programming involves a
      higher frequency of interaction, and also a more fluid play between the
      roles. You may be reviewing my code now, but in ten minutes, I'm reviewing
      yours. Pairing is about constant discussion with the code growing out of
      that discussion.


So it strikes me as reasonable that a programmer used to pull-request
      interactions will want to interact with the LLM in a different way to how
      folks used to pairing want to work with the LLM. Those of us with a
      pairing background will naturally think of the back-and-forth with the
      machine, gradually growing our ideas in tandem, rather than coming up with
      an idea and asking the LLM for an implementation.


Unmesh


How we think about using LLMs also depends on the kind of programming
      activity we are doing. I think of programming as having two deeply
      interwoven activities.


Programming has two deeply interwoven activities: discovering
      and applying abstractions


The first of these is *Discovering and Stabilizing Abstractions*.
      This is creative in nature—the part where we explore multiple options,
      experiment, and slowly converge on stable abstractions. In this activity,
      we observe coding patterns, decide what is common, and identify what might
      vary in the future. We then choose language constructs that arrange these
      common elements in a way that makes future variation easier.


Once abstractions are stable—well-named, well-tested, and
      well-understood—we *Apply Stable Abstractions* to implement new use cases or
      variations. In Domain-Driven Design (DDD) terms, this is where we work
      with the domain model: a set of named abstractions that reflect the
      business domain and carry precise meaning.


Martin


We call both programming, but because they are different activities, we
      work in different ways with an LLM. Once we have stable abstractions, then
      generating code on top of them is something we can think about in more
      mechanical lines. We've defined the language, the LLM then knows how to
      generate code with it.


Unmesh


Exactly, because they now have
      a concrete vocabulary to work with, LLMs do not have to guess what terms
      mean. Prompts like “Implement a controller to update a customer profile
      and a repository for Customer” now give the LLM strong context. The
      result is largely boilerplate code that can be generated reliably.


LLMs also shine in other mostly mechanical parts of development:

- Setting up projects (iteration 0 tasks)
- Creating build pipelines and CI/CD setups
- Repeating established coding patterns with minor variations


We need to be selective about when to hand control to the LLM. During abstraction
      discovery, the developer must keep control—they will reap the benefits later. Once the
      abstractions are stable, hand over repetitive and mechanical coding to
      the LLM, guided by the language established by the abstractions.
      This approach maximizes both our creativity and productivity.


That said, LLMs are of great help in the process of discovering
        abstractions as well.


When coding, it's useful to see alternatives quickly - LLMs
      are well-suited to generate them


When we start coding, its often useful to see alternatives quickly to get sense 
        of the code structure. LLMs turn intent into code fast. Say
        what you want in plain English and get a small, targeted snippet in the
        language you choose. Seeing code quickly helps you test names and
        boundaries, compare options, and shape both the abstractions and the
        solution. I prefer to use LLMs in 'chat' mode in this case and not 'agent' mode
        This allows us to try out different ideas and get a sense of the code structure
        without worrying about corrupting the existing implementation.
        We can selectively choose which parts of the code to change
        and do very small iterative changes.


Another very useful technique I often do with LLMs is that of 
          language projections. Rewriting the same code in another language
          (Go, C++, etc.) is a great way to test out ideas.
          Seeing the same code in another language helps us to very quickly
          test out implementation alternatives. LLMs are very useful here, as you 
          don't need to type all that code. Better yet, you can get the code even in 
          programming languages that you are not familiar with.


I find this lot more useful than to take all the effort to write prompts
          to get the exact code I want. The conversations with the LLMs in the 
          process of finding code level abstractions and keeping the conversation 
          free from any specific rules to give prompts in a specific way
          is lot more useful.


Martin


This reminds me of how I was told off in my pre-university job
       (1980's) for not carefully triple-checking my code before trying to
       compile it on our local mini-computer. I was told the âright wayâ was to
       get a page of fortran to compile âfirst-timeâ. I found I was faster going
       a few cycles with the compiler as it found the errors faster than I
       would. I can sorta understand where my boss was coming from, an
       interactive terminal was relatively new in those days, and many people
       had grown up with punch cards, but what they missed was that once the
       feedback loop sped up, then iteration was better than pre-submission
       checking.


If I find something hard to enunciate in the language my
       abstractions have created, that suggests I need to refine them further.


I was told off for âleaning on the compilerâ then, but as my
       experience grew, I increased my interaction with the computer to explore
       abstractions. As I'm writing code, I'm paying attention to how the
       abstractions I've already created make it easier to express the behavior
       I want. If I find something hard to enunciate in the language my
       abstractions have created, that suggests I need to refine them further. The
       computer plays a vital role here to keep me honest. Without it running
       the compiler and executing the tests, it's too easy to fool myself that
       what I'm writing works. The computer forces me to confront the limitations
       of my abstractions.


Unmesh


Crucially, in this activity, we cannot fully specify upfront what
         these abstractions will look like, nor which language features or
         paradigms will best express it. The shape of the abstraction emerges
         only while working through the code. Developers see patterns in the
         concrete code and gradually refactor toward a stable structure.


Martin


LLMs seem like a natural further step on that partnership with the
       computer, providing a new and rich mechanism to get feedback on
       *vague* ideas


Unmesh


This process cannot be reduced to a static prompt for an LLM.
       Reviewing LLM-generated code is rarely enough—you miss the deep thinking
       that happens when you are coding yourself. In this stage, LLMs are most
       valuable as brainstorming partners: they can suggest alternative designs
       or ways of structuring code, but you should resist letting them generate
       the core implementation. This phase belongs to the developer.


Richard Gabriel [defines
       abstractions](https://www.dreamsongs.com/WorseIsBetter.html) as compression—encoding a well-established meaning
       into a compact form, much like words in spoken language that stand for
       larger concepts.


When we speak of a domain in a domain model, we often think only of the
       functional or problem domain—Finance, Retail, Healthcare, and so on. But
       in practice, functional knowledge alone is rarely enough to form truly
       useful domain abstractions. There is always another domain at play: the
       solution domain.


The solution domain is shaped by the architectural and technological
       choices we make: whether we are building a web-based system or an
       event-driven one; whether we rely on an in-memory data grid or a
       relational database; whether our integration patterns involve synchronous
       APIs or asynchronous messaging. These choices are not peripheral—they
       shape the abstractions we create.


the domain model and its vocabulary emerge at the
       intersection of the functional domain and the solution domain


In most projects, the domain model and its vocabulary emerge at the
       intersection of the functional domain and the solution domain. This is why
       domain experts with a narrow functional focus cannot work in isolation.
       Successful teams bring together people with deep functional expertise and
       people with deep solution/technical expertise, working closely to shape a
       shared language.


The Agile community has long recognized this: good vocabulary emerges from
       collaboration. The way we build solutions, form domain models, and create
       vocabulary has not changed with LLMs—and it still requires deliberate
       effort. In fact, failing to create a shared domain vocabulary has even
       greater costs when working with LLMs. Without it, the model has no
       concrete reference points and must guess at meaning, often producing
       results that miss the mark.


---
