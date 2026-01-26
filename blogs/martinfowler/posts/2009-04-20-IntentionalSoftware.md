---
title: "Intentional Software"
description: "Several years ago, my then colleague Matt Foemmel, dissatisfied   with the tools with which we were building software, managed to get   in touch with Charles Simonyi to find out more about the shadowy"
date: 2009-04-20T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/IntentionalSoftware.html
slug: IntentionalSoftware
word_count: 1938
---


Several years ago, my then colleague Matt Foemmel, dissatisfied
  with the tools with which we were building software, managed to get
  in touch with Charles Simonyi to find out more about the shadowy [Intentional Software](http://www.intentsoft.com/). What
  he saw impressed him, and he persuaded me and other ThoughtWorkers
  to get involved too. What we saw was a tool with startling
  potential, but we remained frustrated by the secrecy and lack of
  urgency to release. That frustration ended last week.


Last week I set off for Chris Sells's [DSL Devcon](http://www.sellsbrothers.com/conference/), and
  Magnus Christerson - Intentional's product manager - suggested
  I pop in to see how they were going on. After several years of âReal
  Soon Nowâ, I was unsure, but Rebecca Parsons, my colleague who has
  been keeping regular contact with Intentional, said that now would
  be a good time.


I spent a fascinating and exciting day at their office in
  Bellevue. It's not that I saw anything particularly new - these were
  all ideas and capabilities that had been around for a while - but
  there was a realness and maturity that I hadn't seen before. Indeed
  Intentional had released a version 1.0 of their product a few weeks
  earlier. The usual approach is to trumpet a version 1.0 release of a
  ground-breaking product from the mountaintops. Only Intentional
  would make such a release and not bother to tell anyone. Indeed as I
  write this there's no mention of their product on their website - if
  you want more information you have to talk to them.


## What's There


This isn't a comprehensive discussion of their tool
    (called the Intentional Domain Workbench), I haven't had time to
    put something like that together. But I hope my scattered thoughts
    and observations will be interesting. The Intentional Domain
    Workbench is a [LanguageWorkbench](https://martinfowler.com/bliki/LanguageWorkbench.html), indeed it's one of
    the systems that made me coin that term. A Language Workbench is a
    tool that allows people to design
    [DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html): not simply to parse them, but build
    a comprehensive environment that includes rich editing. In
    Intentional's case this is a [ProjectionalEditing](https://martinfowler.com/bliki/ProjectionalEditing.html)
    environment.


One of the examples they have is the state machine example I use
  for my [book
  introduction](https://martinfowler.com/dslwip/Intro.html). The workbench allows you to define the schema of
  the semantic model state machine in its schema definition
  language. In order to manipulate state machines you define
  projections of the semantic model. One of the striking features of
  the Intentional Domain Workbench is its ability to support multiple
  projections of the same semantic model. For the state machine
  example they've defined projections in several of the DSLs I've used
  in discussing the example: XML, custom syntax, and Ruby. All three
  of these projections are reversible, meaning that you can edit
  through them, updating the semantic model and other
  projections. Switching between the projections is just a matter of
  selecting a menu item.


They also had read-only projections in fluent C#, command-query
  C, and a state machine diagram. Although they hadn't set up the
  diagram to be editable, the workbench can handle editable
  diagrammatic representations. In another example they
  show  an electronic circuit which is editable in both a
  tree structured property sheet projection and in a circuit diagram
  projection.


The circuit diagram also showed another really powerful feature
  of the workbench - the ability to fluidly integrate example
  executions with the program definition. In the electronic circuit
  case, this means that you can give the various elements of the
  circuit properties and the model will calculate the impedance of
  various parts of the circuit and display them as you are editing the
  circuit. Of course you can build a custom program to do this kind of
  thing - but the point is that this behavior comes easily as part of
  a DSL definition in the workbench.


Combining example execution with program definition is one of the
  features of spreadsheets - and may be a reason why spreadsheets have
  become so successful as an environment for
  [LayProgrammers](https://martinfowler.com/bliki/LayProgrammer.html). It's also a notion that's been propelling
  much of Jonathon Edwards's [interesting and wild ideas](http://alarmingdevelopment.org). My
  sense is that interesting DSLs in language workbenches will have
  this characteristic, particularly if they are aimed at being used by
  lay-programmers.


Another way that you can combine execution with specification is
  with test cases. They have an example of a pension workbench, build
  with Capgemini, that allows actuaries to enter formulas using full
  mathematical notation, together with FIT-like tables to show test
  cases. These test cases are live with the appropriate red/green
  behavior as you edit the formulas.


The pension workbench also illustrates the combination of
  multiple languages. When you look at a pension document on the
  screen, you're looking at three independent languages:
  word processed text for the prose, mathematical notation for the
  formulae, and test case tables. These languages are developed
  independently but integrated in the workbench's core data structure
  (called the Intentional Tree). This integration
  extends to the execution too - you can step into a test case and
  delve into the intermediate values in the mathematical formulae.


In order to make these things run, you have to include behavior
  with the semantic model. Intentional have developed their own
  general purpose language, whose working name is CL1, to do this. CL1 can
  look like superset of C#, but such a view is again a projection of
  the core semantic model. I found it interesting that this is a
  similar feature to JetBrains MPS who have their âbase languageâ
  which projects into a Java-like general purpose
  language. Increasingly much of these tools are programmed using this
  in-workbench general purpose language.


The intended way of working is that developers use the
  Intentional Domain Workbench to build a domain-specific
  workbench. They provide a runtime (the Intentional Domain Runtime)
  for them to run without language editing capabilities. So Capgemini
  used the Intentional Domain Workbench to build the Pension Workbench
  as their own product. The Intentional Domain Workbench allows you to
  define new model schemas and projections, while the Pension
  Workbench allows you to build pension plans using these languages.


The Intentional system is primarily arranged in the .NET
  ecosystem. Both the workbench and runtime run on the CLR and core
  parts of them are written in C#. The workbench makes it really easy
  to generate .NET assemblies that can be automatically loaded into
  the workbench for testing or run with the runtime. Custom
  workbenches can generate code for any environment, and Intentional
  have done some work with another partner that involves generating
  Java code so that people can specify behavior in the custom
  workbench and then deploy the resulting system in a Java environment.


An interesting aspect of the implementation is that they handle
  representational transformations by using lots of little
  transformations rather than one large one. As an example, code
  generating C# from a semantic model involves about a dozen small
  transforms lined up in a pipeline similar to a multi-stage compiler,
  the last step being a transformation from a C# AST to text. Much of
  their internal design goes into making this approach efficient so
  you can happily string together a lot of small transforms without
  worrying about any efficiency cost. A further consequence is that
  the pipeline of transforms for code-generation is very similar to
  that used for editing projections.


A common problem with tools that use projectional editing is how
  they deal with version control. Often the answer is to just let
  multiple people edit the same store simultaneously, which makes many
  serious developers quake. The Intentional Domain Workbench has a built in
  version control mechanism that records all the changes made to the
  Intentional Tree and can do commits and merges at the tree
  level. You then see diffs in languages by doing another projection.


An interesting feature of this version control approach
  is that you can commit with conflicts and the conflicts are
  committed into the repository as conflicts. Unlike with text files
  they don't mess up your text - you have a real data structure
  present, so you can find the conflicts and fix them. The developers
  use this feature to commit a conflict they can't sort out to a
  branch so that developers more familiar with the conflicted area can
  update to the branch and fix it.


The fact that editing is done on an intentional tree rather than
  text also changes some other things. For example unordered
  collections are tagged so that a change in the ordering of the
  elements in an editor doesn't trigger a conflict. You can also
  include domain-specific conflict detection and resolution
  behavior.


## Going Public


Historically the lack of releasing of Intentional has been one
  problem, their secrecy is another. To see anything real about the
  Intentional Domain Workbench has required what Neal Ford refers to as an
  [UnforgivenContract](https://martinfowler.com/bliki/UnforgivenContract.html). Intentional have given some [public
  talks](http://www.infoq.com/news/2009/03/DSL-Magnus-Christerson-Henk-Kolk), but they've really boiled down to saying âtrust us, we
  have some really cool technologyâ. We'd known that indeed they had,
  but couldn't explain to people why.


So I awaited the talk at DSL DevCon, given by Magnus and Shane Clifford
  (their development manager), with quite some expectation. They said they
  were going to finally open the curtain. Would they - and how would
  people react?


They started worryingly, with the usual unrevealing Powerpoints,
  but then they switched to showing the workbench and the curtain finally
  opened. To gauge the reaction, take [a look at
  Twitter](http://search.twitter.com/search?page=10&q=%23dsldevcon).

- *@pandemonial* Quite impressed! This is sweet!
  Multiple domains, multiple langs, no question is going
  unanswered
- *@csells* OK, watching a live electrical circuit
  rendered and working in a C# file is pretty damn cool.
- *@jolson* Two words to say about the Electronics
  demo for Intentional Software: HOLY CRAPOLA. That's it, my brain has
  finally exploded.
- *@gblock* This is not about snazzy demos, this is about completely
    changing the world we know it.
- *@twleung* ok, the intellisense for the actuarial formulas
  is just awesome
- *@lobrien* This is like seeing a 100-mpg carburetor : OMG someone is going to buy this and put it in a vault!


Afterwards a couple of people said it was the most important demo
  they'd ever seen, comparing it even to the [Mother of all
  Demos](http://en.wikipedia.org/wiki/The_Mother_of_All_Demos). For many there was a sense that the whole world of
  software development had just changed.


(Many thanks to Chris Sells and co for organizing this conference
  and inviting me to speak. They also made a [video of the
  talk available](http://msdn.microsoft.com/en-us/oslo/dd727740.aspx).)


So now what? There's more to all this than a demo can
  reveal. Right now we want to get several of our hands on the
  workbench and kick its tires - hard. Assuming it passes
  that test, we want to use it on commercial projects and see how
  works for real. No system designed using the Intentional Domain Workbench
  has yet gone live, and as any agilist knows you never really
  understand something till you deploy it into production every week.


Shortly the other major similar workbench to this - JetBrains's
  [Meta Programming
  System](http://www.jetbrains.com/mps/index.html) - will have version 1.0 released as open-source. So this year could
  well be the year when these Language Workbenches will finally step
  out into the light and see their first external pilot projects. (I
  should also mention that the MetaEdit workbench has been out for a
  while, although it hasn't had much visibility.) I don't know whether
  these workbenches will change the face of programming as we know it,
  after all I once thought Smalltalk was going to be our future; but these
  workbenches do have the potential to be such a profound
  change. Certainly I'm excited that we're now on the next, more
  public, stage of this journey.
