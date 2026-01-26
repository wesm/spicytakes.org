---
title: "Dsl Migration"
description: "One danger that DSL advocates need to guard against is the notion   that first you design a DSL, then people use it. Like any other   deice of software, a successful DSL will evolve. This means that  "
date: 2009-02-04T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/DslMigration.html
slug: DslMigration
word_count: 789
---


One danger that DSL advocates need to guard against is the notion
  that first you design a DSL, then people use it. Like any other
  deice of software, a successful DSL will evolve. This means that
  scripts written in an earlier version of a DSL may fail when run
  with a later version.


Like many properties of DSL, good and bad, this is really very
  much the same as happens with a library. If you take a library from
  a someone and they upgrade the library, you may end up stuck. In
  essence DSLs don't really do anything to change that. Your DSL
  definition is essentially a [PublishedInterface](https://martinfowler.com/bliki/PublishedInterface.html) and you
  have to deal with the consequences just the same.


This problem can be more prominent with external DSLs. Many
  changes to an internal DSL can be handled through refactoring tools
  (for those languages that have them). But refactoring tools won't
  help with an external DSL. In practice this problem is less of an
  issue than it might be. An internal DSL with scripts that are
  outside the control of the DSL implementors won't be picked up with
  refactoring. So the only difference between internal and external
  lies with DSL scripts within the same code base.


One technique for handling evolution of DSLs is to provide tools
  that automatically migrate a DSL from one version to another. These
  can be run either during an upgrade, or automatically should you try
  to run an old version script against a new version.


There are two broad ways to handle migration. The first is an
  **incremental migration** strategy. This is essentially the same notion
  that's used by people doing [evolutionary database
  design](https://martinfowler.com/articles/evodb.html). For every change you do to your DSL definition, create a
  migration program that automatically migrates DSL scripts from the
  old version to the new version.


An important part of incremental
  migration is that you keep the changes as small as you can. Imagine
  you are upgrading from version 1 to 2, and have ten changes you want
  to make to your DSL definition. In this case, don't create just one
  migration script to migrate from version 1 to 2, instead create at
  least 10 scripts. Change the DSL definition one feature at a time,
  and write a migration script for each change. You may find it useful
  to break it down even more and add a feature with more than one step
  (and thus more than one migration). They way I've described it may
  sound like more work than a single script, but the point is that
  migrations are much easier to write if they are small, and it's easy
  to chain multiple migrations together. As a result you'll be much
  faster writing ten scripts than one.


The other approach is **model-based migration**. This is a
  tactic you can use if you are using a [Semantic
  Model](https://martinfowler.com/dslwip/SemanticModel.html) (which is something I almost always recommend). With this
  approach you support multiple parsers for your language, one for
  each released version. (So you only do this for version 1 and 2, not
  for the intermediate steps.) Each parser populates the semantic
  model. When you use a semantic model, the parser's behavior is
  pretty simple, so it's not too much trouble to have several of them
  around. You then run the appropriate parser for the version of
  script you are working with. This handles multiple versions, but
  doesn't migrate the scripts. To do the migration you write a
  generator from the semantic model that generates a DSL script
  representation. This way you can run the parser for a version 1
  script, populate the semantic model, and then emit a version 2
  script from the generator.


One problem with the model-based approach is that it's easy to
  lose stuff that doesn't matter to the semantics, but is something
  that the script writers want to keep. Comments are the obvious
  example. This is exacerbated if there's too much smarts in the
  parser, but then the need to migrate this way may help encourage the
  parsers to stay dumb - which is Good Thing.


If the change to the DSL is big enough, you may not be able to
  transform a version 1 script into a version 2 semantic model. In
  which case you may need to keep a version 1 model (or intermediate
  model) around and give it the ability to emit a version 2
  script.


I don't have a strong preference between these two alternatives.


Migration scripts can be run by script programmers themselves
  when needed, or automatically by the DSL system. In order to run
  automatically it's very useful to have the script record which
  version of the DSL it is so the parser can detect it easily and
  trigger the resulting migrations.
