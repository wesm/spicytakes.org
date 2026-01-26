---
title: "Business Readable DSL"
description: "Will DSLs allow business people to write software rules   without involving programmers?"
date: 2008-12-15T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/BusinessReadableDSL.html
slug: BusinessReadableDSL
word_count: 457
---


**Will DSLs allow business people to write software rules
  without involving programmers?**


When people talk about DSLs it's common to raise the question of
  business people writing code for themselves. I like to apply the
  COBOL inference to this line of thought. That is that one of the
  original aims of COBOL was to allow people to write software without
  programmers, and we know how that worked out. So when any scheme is
  hatched to write code without programmers, I have to ask what's
  special this time that would make it succeed where COBOL (and so
  many other things) have failed.


I do think that programming involves a particular mind-set, an
  ability to both give precise instructions to a machine and the
  ability to structure a large amount of such instructions to make a
  comprehensible program. That talent, and the time involved to
  understand and build a program, is why programming has resisted
  being disintermediated for so long. It's also why many
  ânon-programmingâ environments end up breeding their own class of
  programmers-in-fact.


That said, I do think that the greatest potential benefit of DSLs
  comes when business people participate directly in the writing of
  the DSL code. The sweet spot, however is in making DSLs
  business-*readable* rather than business-*writeable*. If
  business people are able to look at the DSL code and understand it,
  then we can build a deep and rich communication channel between
  software development and the underlying domain. Since this is the [Yawning
  Crevasse of Doom](http://www.infoq.com/news/2008/08/Fowler-North-Crevasse-of-Doom) in software, DSLs have great value if they can
  help address it.


With a business-readable DSL, programmers write the code but they
  show that code frequently to business people who can understand what
  it means. These customers can then make changes, maybe draft some
  code, but it's the programmers who make it solid and do the
  debugging and testing.


This isn't to say that there's no benefit in a business-writable
  DSL. Indeed a couple of years ago some colleagues of mine built a
  system that included just that, and it was much
  appreciated by the business. It's just that the effort in creating a
  decent editing environment, meaningful error messages, debugging and
  testing tools raises the cost significantly.


While I'm quick to use the COBOL inference to diss many tools
  that seek to avoid programmers, I also have to acknowledge the big
  exception: spreadsheets. All over the world suprisingly big business
  functions are run off the back of Excel. Serious programmers tend to
  look down their noses at these, but we need to take them more
  seriously and try to understand why they have been as successful as
  they are. It's certainly part of the reason that drives many
  [LanguageWorkbench](https://martinfowler.com/bliki/LanguageWorkbench.html) developers to provide a different
  vision of software development.
