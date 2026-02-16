---
title: "Conversation: LLMs and the what/how loop"
description: "A conversation between Unmesh, Rebecca, and Martin on how LLMs help   us shape the abstractions in our software. We view our challenge as building   systems that survive change, requiring us to manage"
date: 2026-01-21T00:00:00
tags: ["generative ai"]
url: https://martinfowler.com/articles/convo-what-how.html
slug: convo-what-how
word_count: 3248
---


Unmesh


The primary challenge of software development is to build systems that survive change.


People new to programming, and people who don't code for a living but hire those who do, often
        think of programming as a linear translation of requirements into programming language syntax.
        This view misguides people into either spending a lot of time getting the requirements or
        specifications right, or gaining expertise in programming language syntax.


In the context of LLM usage, this view manifests in phrases like 'Human in the loop'. This terminology implies that the
        primary work of translating requirements into code is performed by the LLM,
        using the human only for cleanup when the machine fails.


But as any experienced programmer knows, the real challenge is not converting requirements to
        code, but building systems that survive change.


What makes systems easier to manage as change happens?


Martin


To make things easier to change, we need to manage cognitive load.


One key to making things easier to change is managing cognitive load
      for those who need to make the change. I might not be able to fit a
      million lines of code into my head, but if the system is well structured
      into modules, I might only need to understand a few hundred of those lines
      - then I can make progress.


Another key is when the code mirrors something that's already familiar
      to me. If I'm working on a shipping system, and the code has elements like
      ships, ports, and containers - and those elements behave in ways I expect
      them to from my knowledge of the domain - then it helps me reason about
      how the code works.


Rebecca


Managing cognitive load also requires understanding the domain at various levels of granularity. 
    This decomposition allows us to reason about properties through our abstractions without always 
    getting lost in the weeds. Like other aspects of the design process, getting the right abstraction levels is iterative.


Unmesh


At its core, the act of programming is mapping the “real”
      domain (the What) onto a computational model (the How)


Cognitive load does not necessarily reduce if you need to deal with English-language prompts, or diagrams.
      At its core, the act of programming is mapping the ârealâ domain (the What) onto a
      computational model (the How). We must preserve the essence of the domain while translating it
      into a form the machine can execute. Crucially, this is not a one-way street; it is a
      continuous feedback loop where the “what” and “how” provide deep insights into each other.


Together, they uncover the stable parts of the system and the axes along which the system
      might change in the future, allowing us to use programming paradigms to provide hooks for
      these changes.


Martin


I've often heard folks use âwhatâ and âhowâ to describe the difference
      between requirements analysis and programming. Requirements are about
      âwhatâ and programming about âhowâ. But I've never liked that framing, it
      tries to separate âwhatâ and âhowâ into separate universes and I don't
      think that's an effective way to think about the world.


Unmesh


The 'What' and 'How' are not separate universes but are intertwined.


I agree. On the surface it seems like that makes a good distinction.

      We start with whiteboarding and high-level user journeys to discuss the system goals. We map
      these to the implementation landscape—databases, services, and UI. But the “what” question
      persists at every level:

- System level: What is the user trying to achieve?
- Class level: What is this component supposed to do?
- Function level: What is this specific block for?


The impact: the answer to “what” determines the logical grouping and, most importantly, the
      naming. Once the intent is named (and refined by our implementation insights), we face the mechanics
      of execution. The decisions we make here shape the structure of the solution.


Rebecca


A crucial part of the “how” is choosing how we represent the
      real domain in something a computer can execute


A crucial part of the “how” is choosing how we represent the real domain in something a
        computer can execute. We often do this by mapping the domain onto a familiar computational
        model—like a state machine, a table, a stream, or a log. This mapping is not neutral: using the
        state machine as an example, if we
        map something to a state we start reasoning about it differently than if we map it to a
        transition.


The shape of this mapping is often where the structure of the solution starts to
        emerge.
        If we don't use a model that comes with built-in semantics
        then we have to develop a mental model
        (abstraction) that we can then represent in code.
        At this point, our choice of language paradigm will matter a great deal, as there are
        abstractions that are readily represented in a particular paradigm and others that are more
        difficult. For example, an unbounded yet finite list is much easier to represent in a
        functional style language.


Martin


This is why when we think about domain modeling, it's not just about
      modeling the data structures, it's also about modeling how computation
      works with those data structures. Object-oriented modeling took a step in
      that direction by binding behavior to the data structures, but it's only an
      initial step. When working with more complex domains you have to
      design computation into the fabric of the model.


Unmesh


These decisions are not implementing a requirement to make it run;
      they are about choosing the
      right structure.


As we oscillate between these two modes, something important happens:

- What → How: While refining the intent, the mechanism reveals itself. “Ah, these requests
        are strictly prioritized based on delivery time. I can use a priority queue here.”
- How → What: While implementing the mechanics, the true nature of the system reveals
        itself. “Oh, looking at how we persist these events, we aren’t just saving data; we are
        actually implementing a write-ahead log mechanism.”


Martin


Start with scenarios and use them to drive the abstractions
      that link âhowâ and âwhatâ


This raises the question of how we should best understand
      how we understand and think about the higher-level âwhatâ. We can't come
      up with a broad, abstract, statement of requirements because we cannot
      figure out how to talk about that abstract statement
      without understanding the mechanism to implement it. The intertwining of
      âwhatâ and âhowâ traps us in circular dependencies.


The way forward that's always appealed to me is to start with concrete
      examples of how people use a system. Take these scenarios/use-cases and
      use them to drive the abstractions that support them.


Unmesh


And these scenarios operate at two levels:

- At the system level (use cases): We define the narrative. “A user adds an item to the
        cart” defines system boundaries.
- At the module level (test cases): We define the contract. A unit test is simply a
        micro-scenario (Given → When → Then) that solidifies the “what” for a single function.


TDD is a design strategy that operationalizes the feedback loop between “what” and “how”


When I first encountered [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) (TDD), I found it attractive because it felt like a design strategy
      that operationalizes the feedback loop between “what” and “how.”


TDD works because it makes this what/how loop explicit:

- Locking the “what”: By writing the test first, you force yourself to answer the “what”
        question (naming, inputs, outputs) before getting distracted by implementation details. You
        are temporarily acting as the client of your own code.
- Iterating the “how”: Once the test exists (red), you are free to implement the solution
        (green).
- Refining the structure: You then refactor. This is where the “how” often tells you that
        your “what” (your API design or test scenario) was awkward or leaky, leading to a better
        design.


Rebecca


This connection between TDD and use-cases is important, since they are
      both ways of focusing on the âwhatâ. Tests should be, but often aren't,
      focused on that âwhatâ.


Martin


Writing a test encourages us to think about the interface without coupling it to an implementation.


I regularly noticed that people struggle with doing encapsulation well,
      because they find it hard to think about an interface without coupling it
      to an implementation. Tests help with this, because writing a test before
      I implement it encourages me to think solely about the API. It's also an immediate
      usability test. When I write a test, I'm approaching the problem as a user
      of an API, that focuses on a low-level âwhatâ frames the way I think
      about the API.


Now in the refactoring step I reconsider both the implementation and
      the interface with what I've learned from making the test work. That
      sometimes will lead me to new ideas about how to represent the âwhatâ,
      both for the immediate API and for my broader understanding of the model
      as a whole. It won't happen with every test, even with most tests, but it
      happens enough to make a difference.


Unmesh


All this matters even when we use LLMs and prompt them. 
        I recently experimented with writing a miniature object store inspired by the MinIO codebase.
        When I asked the LLM to derive the implementation for MinIO, it produced something that was
        too procedural and harder to understand. When I wrote it myself, step by step, I ended up with
        fewer and crisper abstractions, and the code was easier to read and evolve.


This matches a pattern I keep seeing. Without a stable vocabulary of abstractions,
        LLM-generated code tends to be procedural. If I push it to “refactor,” it often swings to the
        other extreme and creates too many classes and layers, making the design unnecessarily
        complicated.


This is why I prefer to use LLMs as a translation layer inside my what/how loop. I use them to
        quickly sketch a first version, but I still rely on writing and refactoring to shape the
        structure—because the code I keep is the code I can explain, test, and change with confidence.


Prompts alone satisfy a scenario, but don't build the structure
     of the solution to accommodate future scenarios


This is also why generating test cases with LLMs to improve “test coverage” is not something
      I find very useful.


Passing the test, or making the code work for a scenario, is merely the baseline. The primary
      goal is not just to satisfy the current scenario, but to solidify and build the structure of
      the solution so it can accommodate future scenarios.


If we simply “make it work,” we create fragile code. We must organize the solution so that
      the “how” can evolve without breaking the “what.” We achieve this through:

- Cohesion: Grouping parts that share the same “what” (business intent).
- Decoupling: Separating parts that have different reasons to change.


We extract similar behavior into
    modules, creating domain-specific abstractions that help us manage
    cognitive load


Martin


This is about managing cognitive load. We could write a complex program
      as one very long function, with all variant behavior handled through
      simple if/else conditionals. But that's too much for someone to
      understand. If we take bits of repeated code and turn them into
      sub-functions, we capture the similarity in behavior and make it explicit
      in the code, making it easier to understand. If two chunks of code are
      nearly the same, we can extract them into functions and capture the
      variation by parameters - again clearly marking where variation occurs.
      Then we can arrange those sub-functions into broader patterns, again to
      explicate where variation occurs. These patterns form abstractions that
      are specific to our particular domain.


Rebecca


Once we have done the refactoring described by Martin, we then need to decide how to achieve the behavior we want through the interactions of these different modules. Again, getting the level of granularity right supports both reasoning about the behavior and helps us to manage cognitive load.


Unmesh


Programming paradigms provide conventions for how to organize
    these abstractions


Programming paradigms provide conventions for these decisions, effectively
      representing stable parts while providing hooks for variation.


Object-oriented programming focuses on identifying common behaviors (interfaces). The
      variations are the specific classes that group data along with implementations of those
      interfaces. We use it when we expect actions (interfaces) to remain stable while types change.


Functional programming often treats the data structures as the stable part, and the
      variations as the operations (pipelines/filters). We bet that the data shape stays stable
      while transformations change.


Martin


Yes.... except I don't think that thinking of OO and functional as
      separate paradigms is helpful. I think of objects (binding data and
      behavior), first-class functions, polymorphism, pipelines, etc - as tools.
      An ideal programming environment allows me to use any of these tools
      as I need to. Pipelines of functions are often seen as a functional
      programming thing, but [I first ran into them](https://martinfowler.com/articles/collection-pipeline/#FirstEncounters)
      when I used Smalltalk.


The point that these things are all tools for building abstractions.
      When folks talk about the enormously important move from assembly
      languages to the first high-level languages, they usually talk about how
      it increased the level of abstractions. That's true, but more importantly
      the high-level languages also gave us the first tools to create our own
      abstractions. Early ones were often crude (like subroutines in Fortran IV)
      but some were more capable (such as Lisp). We've steadily discovered and
      refined more tools since.


Unmesh


As abstractions stabilize, programming looks like expressing
      intent using well-established abstractions


Once the abstractions that we've built are stable, we then program with
      them in the form of declarative programming. Some domains, where there is
      a standard set of abstractions, work especially well with declarative
      languages—for example, SQL for database queries or makefiles for builds.
      As abstractions stabilize, programming increasingly looks like expressing
      intent using well-established abstractions.


Martin


I think of these as alternative computational models, it was the heart
      of what [Rebecca and I were exploring in our DSL
      book](https://martinfowler.com/books/dsl.html). It's still an area I'd like to explore more, and I wonder if
      working with LLMs may help us in that direction.


As an aside, I'll mention that I'm not a big fan of SQL. I much
      prefer to query tabular data using a pipeline of functions, such as [R's
      dplyr](https://dplyr.tidyverse.org) package.


Unmesh


Communities give us a human vocabulary for organizing abstractions.


While creating something as precise as an alternative computational model
      is difficult, and therefore rare, communities of developers come up with a
      human vocabulary of idioms and patterns around their common implementation
      concerns. Programming is after all a human activity, and communities
      naturally form around programming languages and paradigms. As Bjarne Stroustrup
      said âDesign and development are human activities, forget that and all is
      lostâ.


We see such communities form naturally as people use languages to solve
      real-world problems. Using Ruby and Ruby on Rails for web development,
      Python for data science and infrastructure development, Java and
      Java-based tools in the data engineering community, and Go for systems
      development are notable examples. These idioms and patterns not only make
      it easier to make implementation decisions, they also provide vocabulary
      to communicate the “how” part of the design.


Statements like “just use a List-and-Watch pattern to work with etcd,”
      or “use message passing with a select loop over a channel in Go,” make it
      easy to understand how to do a robust implementation. These idioms also
      make it easier to translate between intent and implementation.


LLMs work fantastically when used with this understanding. They act as a translation layer
      and allow us to express intent in natural language.


Martin


Since LLMs can operate at a lower level of precision they
        allow us to explore abstractions with more fluidity.


This is an opportunity for LLMs. Building abstractions requires
      precision, which is why it's hard. Since LLMs can operate at a lower level
      of precision, that of patterns and idioms, this allows us to use them to
      explore ideas with more fluidity. I'm interested in seeing if this helps
      move more easily to the precision of an alternative computational
      model.


Rebecca


The choice of representation is driven by the domain and its mapping
      to the programming paradigm. Once we have this mapping—even if it is still
      informal—we can use TDD and the LLM to drive the paradigm-appropriate
      'how.'


Unmesh


When we are iterating between “what” and “how,” LLMs can quickly show code once we express an
      intent or describe a scenario. It is important to remember that
      generated code is usually the first version that makes the test pass. We still need to
      structure the solution using the tools provided by the programming paradigm and the language,
      and using the idioms of the community.


Good abstractions make intent easy to translate into implementation.


When abstractions stabilize and programming is mostly about using those abstractions in a
      declarative syntax, the LLM’s strength in language representation becomes especially useful. A
      few prompts can produce a working implementation. Because abstractions form the essential
      vocabulary for the prompts, the generated program is more predictable and easier to review.


“Order the requests by delivery timestamp in a priority queue” or “store this customer record
      using a repository” tends to generate code that follows well-understood idioms, making it
      easier to review and manage.


Rebecca


LLMs rely on mature training data - who builds what comes next?


However, there is a hidden dependency here: LLMs rely on maturity. If a
      language is not suitably mature, or if we are exploring a novel paradigm,
      the LLM will be insufficiently trained. In these frontiers, tools are
      scarce, and we are effectively on our own. This constraint raises a
      critical question: Since LLMs can only operate where there is abundant
      training data, where will new languages and paradigms come from in the age
      of AI? Will we even care if they never come?


Martin


This makes me think of something the [writer Will
      Wilkinson said](https://bsky.app/profile/wlknsn.xyz/post/3m5tnpfqpgs2e): âThe very best writing ‘defamiliarizes’ the
      familiar - makes it fresh, conjures it anew, etc. But LLM outputs are an
      averaged rehash of the familiar, by design.â If we are struggling with a
      common (familiar) problem, a good solution is by necessity going to be
      *un*familiar.


LLMs can come up with random, new ideas - humans can then select
      and develop them


On the other hand, I do think LLMs can come up with unfamiliar ideas,
      both in writing and in programming. Essentially this is due to their
      random creations, they are hallucinating things are unfamiliar. On my
      third hand what they can't do is to develop that new creation, because
      they don't have the training data required. A human can use an LLM to
      hallucinate something weird but with potential, and then build on it.
      Which is why it's often useful to ask an LLM to generate three different
      alternatives, so the human can pick the best one, or assemble bits from
      all three into something that's better.


Unmesh


This is why, when we are evolving our understanding and building stable structures, we
        cannot simply 'prompt' the LLMs to do the work. We make use of them, certainly, but we must
        iteratively drive the code to build the stable structure ourselves. Referring to the
        Domain-Specific Languages book, this is the phase where we build the Semantic Model. LLMs
        should be treated as powerful instruments in this phase, but the developer must remain the
        primary architect of the model.


Martin


Personally, I find this a comforting thought. One of my favorite things
      about programming is model-building. I'm hopeful that LLMs won't take that
      away - indeed will make it easier and more fulfilling.


---
