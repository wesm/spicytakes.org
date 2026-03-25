---
title: "Architecture Decision Record"
description: "An Architecture Decision Record (ADR) is a short document that captures and   explains a single decision relevant to a product or ecosystem. Documents   should be short, just a couple of pages, and co"
date: 2026-03-24T00:00:00
tags: ["enterprise architecture", "collaboration", "application architecture"]
url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
slug: ArchitectureDecisionRecord
word_count: 881
---


An Architecture Decision Record (ADR) is a short document that captures and
  explains a single decision relevant to a product or ecosystem. Documents
  should be short, just a couple of pages, and contain the decision, the context
  for making it, and significant ramifications. They should not be modified if
  the decision is changed, but linked to a superseding decision.


As with most written documents, writing ADRs serves two purposes. Firstly they
  act as a record of decisions, allowing people months or years later to
  understand why the system is constructed in the way that it is. But perhaps
  even more valuable, the act of writing them helps to clarify thinking,
  particularly with groups of people. Writing a document of consequence
  often surfaces different points of view - forcing those differences to be
  discussed, and hopefully resolved.


A general rule is to follow an âinverted pyramidâ style of
  writing, commonly associated with news stories. The key is to put the most
  important material at the start, and push details to later in the record.


The common advice is to keep decision records in the source repository of
  the code base to which they apply. A common choice for their location is
  `doc/adr`. This way they are easily available to those
  working on the code base. For similar reasons they should be written in a
  lightweight markup language, such as markdown, so they can be easily read and
  diffed just like any code. We can use a build task to publish them to a product
  team's website.


Storing them in a product repository won't work for ADRs that cover a broader
  ecosystem than a single code base. Some folks also feel that keeping ADRs in
  git makes it too hard for non-developers to work with them.


Each record should be its own file, and should be numbered in a monotonic
  sequence as part of their file name, with a name that captures the decision,
  so that they are easy to read in a directory listing. (for example:
  â`0001-HTMX-for-active-web-pages`â).


Each ADR has a status. âproposedâ while it is under discussion, âacceptedâ
  once the team accepts it and it is active, âsupersededâ once it is
  significantly modified or replaced - with a link to the superseding ADR. Once
  an ADR is accepted, it should never be reopened or changed - instead it should be
  superseded. That way we have a clear log of decisions and how long they
  governed the work.


ADRs contain not just the decision, but also a brief rationale for the
  decision. This should summarize the problem that led to this decision being
  needed and the trade-offs that were taken into account. A good way to think of
  them follows the notion of âforcesâ when writing a pattern. As part of this
  it's valuable to explicitly list all the serious alternatives that were
  considered, together with their pros and cons.


Any decision has consequences. Sometimes these are clearly implied from the
  rationale, but sometimes it's worth clearly stating them in a explicit
  section. Decisions are usually made under some degree of uncertainty, so it's
  handy to record the confidence level of the decision. This is a good place
  to mention any changes in the product context that should trigger the team to
  reevaluate the decision.


ADRs play a central role in the [Advice Process](https://martinfowler.com/articles/scaling-architecture-conversationally.html),
  where they are not only used to document decisions, but the act of writing
  them is used to elicit expertise and alignment. In this case they should also
  include advice gathered in forming the ADR, although in order to keep things
  brief, it may be better to summarize the advice in the ADR and keep a full
  record of advice separately.


The most important thing to bear in mind here is brevity. Keep the ADR
  short and to the point - typically a single page. If there's supporting
  material, link to it.


While ADRs are a form for recording decisions in software architecture, the
  broader concept of writing short decision records is worth considering in
  other contexts. This kind of decision log creates a valuable historic record
  that can do much to explain why things are the way they turned out.


## Further Reading


Michael Nygard coined the term âArchitecture Decision Recordâ with an
    [ADR-formatted article](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) in 2011. While he did not
    originate the idea of a decision log he did
    make case for a lightweight document, with a focus on the decision
    itself. In this he was particularly inspired  by
    Phillipe Kruchten talking about decision registers / decision logs, and by
    the writing style of [software patterns](https://martinfowler.com/articles/writingPatterns.html). His
    article is better than pretty much everything else written on the topic, my only
    desire to write this one was to point to some developments since.


On this site, there are brief examples of ADR formats in articles by [Harmel-Law](https://martinfowler.com/articles/scaling-architecture-conversationally.html#adr) and [Rowse and Shepherd](https://martinfowler.com/articles/building-infrastructure-platform.html#ArchitecturalDecisionRecords).


[adr-tools](https://github.com/npryce/adr-tools) is a simple command line tool to
    manage ADRs. It includes a set of ADRs for itself that are a good example of
    the form.


## Acknowledgements


Andrew Harmel-Law, Brandon Cook, David Lucas, Francisco Dias, Giuseppe Matheus Pereira, John King, Kief Morris, Michael Joyce, Neil Price, Shane
    Gibson, Steven Peh, and Vijay
    Raghavan Aravamudhan discussed drafts of this post on
    our internal chat. Michael Nygard gave some background on the origins of his
    writing.
