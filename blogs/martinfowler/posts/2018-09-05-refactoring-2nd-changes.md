---
title: "Changes for the 2nd Edition of Refactoring"
description: "A short summary of the changes between the first and second editions   of Refactoring"
date: 2018-09-05T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/articles/refactoring-2nd-changes.html
slug: refactoring-2nd-changes
word_count: 1504
---


At the broadest level, the second edition's structure follows that of the
    first edition. That shouldn't be too surprising, since the first edition was
    so successful, I might as well continue with what worked.


The first edition opened with four narrative chapters, these all appear
    the second edition too. All of these follow the broad forms of the original
    book.


The opening example shifts its domain, as not that many people are
    familiar with a video store any more. The flow of the refactorings is pretty
    much the same: break into functions, separate calculation from formatting,
    organize calculations by type using polymorphism.


The principles and smells chapter both had a thorough overhaul. There's
    much that survived and much that changed. I'm guessing about three-quarters
    of it changed, but that's a gut feel rather than based on a realistic
    measurement. The testing chapter had to be completely redone, particularly
    due to change from Java to JavaScript.


After those introductory chapters, I continue with the catalog, which
    I've always seen as the heart of the book. I'll go into the catalog changes
    in more detail in a moment, but one notable structural change is I put
    together an initial chapter of refactorings that contains what I judge to
    be a good set of refactorings to learn about first.


I dropped the later chapters, which explored some more tangential issues.
    I think they worked in the first edition, but these days I think it's better
    to publish essays like this on my website. That's the same reason why I also
    dropped the four âbig refactoringsâ from the catalog. The big refactorings
    were always a bit different to the majority of the refactorings, and I do
    feel these examples work better through essays on my website.


## Changes to the catalog


So what happened to the catalog? Here's a table that shows the fate of
      the original 68 refactorings. 1


1: 
      The 68 does not include the four âbig refactoringsâ from the original
      book. As I indicated earlier, I think these kinds of topic are best
      captured as essays which can appear on the web.



| Add Parameter | 275 | replaced | â Change Function Declaration |
| Change Bidirectional Association to Unidirectional | 200 | absent |  |
| Change Reference to Value | 183 | kept |  |
| Change Unidirectional Association to Bidirectional | 197 | absent |  |
| Change Value to Reference | 179 | kept |  |
| Collapse Hierarchy | 344 | kept |  |
| Consolidate Conditional Expression | 240 | kept |  |
| Consolidate Duplicate Conditional Fragments | 243 | replaced | â Slide Statements |
| Decompose Conditional | 238 | kept |  |
| Duplicate Observed Data | 189 | absent |  |
| Encapsulate Collection | 208 | kept |  |
| Encapsulate Downcast | 308 | absent |  |
| Encapsulate Field | 206 | replaced | â Encapsulate Variable |
| Extract Class | 149 | kept |  |
| Extract Interface | 341 | absent |  |
| Extract Method | 110 | replaced | â Extract Function |
| Extract Subclass | 330 | replaced | â Replace Type Code with Subclasses |
| Extract Superclass | 336 | kept |  |
| Extract Variable | 124 | kept |  |
| Form Template Method | 345 | absent |  |
| Hide Delegate | 157 | kept |  |
| Hide Method | 303 | absent |  |
| Inline Class | 154 | kept |  |
| Inline Method | 117 | replaced | â Inline Function |
| Inline Temp | 119 | replaced | â Inline Variable |
| Introduce Assertion | 267 | kept |  |
| Introduce Foreign Method | 162 | absent |  |
| Introduce Local Extension | 164 | absent |  |
| Introduce Null Object | 260 | replaced | â Introduce Special Case |
| Introduce Parameter Object | 295 | kept |  |
| Move Field | 146 | kept |  |
| Move Method | 142 | replaced | â Move Function |
| Parameterize Method | 283 | replaced | â Parameterize Function |
| Preserve Whole Object | 288 | kept |  |
| Pull Up Constructor Body | 325 | kept |  |
| Pull Up Field | 320 | kept |  |
| Pull Up Method | 322 | kept |  |
| Push Down Field | 329 | kept |  |
| Push Down Method | 328 | kept |  |
| Remove Assignments to Parameters | 131 | replaced | â Split Variable |
| Remove Control Flag | 245 | replacedâ | â Replace Control Flag with Break |
| Remove Middle Man | 160 | kept |  |
| Remove Parameter | 277 | replaced | â Change Function Declaration |
| Remove Setting Method | 300 | kept |  |
| Rename Method | 273 | replaced | â Change Function Declaration |
| Replace Array with Object | 186 | absent |  |
| Replace Conditional with Polymorphism | 255 | kept |  |
| Replace Constructor with Factory Method | 304 | replaced | â Replace Constructor with Factory Function |
| Replace Data Value with Object | 175 | replaced | â Replace Primitive with Object |
| Replace Delegation with Inheritance | 355 | absent |  |
| Replace Error Code with Exception | 310 | keptâ |  |
| Replace Exception with Test | 315 | replacedâ | â Replace Exception with Precheck |
| Replace Inheritance with Delegation | 352 | replaced | â Replace Superclass with Delegate |
| Replace Magic Number with Symbolic Constant | 204 | replacedâ | â Replace Magic Literal |
| Replace Method with Method Object | 135 | replaced | â Replace Function with Command |
| Replace Nested Conditional with Guard Clauses | 250 | kept |  |
| Replace Parameter with Explicit Methods | 285 | replaced | â Remove Flag Argument |
| Replace Parameter with Method | 292 | replaced | â Replace Parameter with Query |
| Replace Record with Data Class | 217 | replaced | â Encapsulate Record |
| Replace Subclass with Fields | 232 | replaced | â Remove Subclass |
| Replace Temp with Query | 120 | kept |  |
| Replace Type Code with Class | 218 | replaced | â Replace Primitive with Object |
| Replace Type Code with State/Strategy | 227 | replaced | â Replace Type Code with Subclasses |
| Replace Type Code with Subclasses | 223 | kept |  |
| Self Encapsulate Field | 171 | replaced | â Encapsulate Variable |
| Separate Query from Modifier | 279 | kept |  |
| Split Temporary Variable | 128 | replaced | â Split Variable |
| Substitute Algorithm | 139 | kept |  |



â  web edition only


Refactorings marked as kept are present in the second edition under the
      same name. Those marked as absent, aren't in the new edition. There are
      various reasons I dropped refactorings from the new edition, and I may
      extend this article to discuss some of these in the future. Those marked
      replaced have a refactoring with a different name in the new editions.
      Some of these are little more than a rename, for example I changed âSplit
      Temporary Variableâ with âSplit Variableâ. Most are minor generalizations,
      such as changing âExtract Methodâ to âExtract Functionâ. Many of these
      generalizations reflect the less object-centric nature of the rewrite. In
      some cases a few first edition refactorings are combined: eg Add
      Parameter, Remove Parameter, and Rename Method are all replaced by Change
      Function Declaration. As with the ones that I left out, I may extend this
      article in the future to discuss some individual cases. 2


2: 
      Whether I do this depends on whether there seems to be interest in this
      from readers, and how I prioritize this against other things I'll want to
      write about in the coming months.


The new edition contains fifteen refactorings that are completely new,
      in that they aren't generalizations or renaming of existing refactorings.
      These are:



| Combine Functions into Class |
| Combine Functions into Transform |
| Move Statements into Function |
| Move Statements to Callers |
| Remove Dead Code |
| Rename Field |
| Rename Variable |
| Replace Command with Function |
| Replace Derived Variable with Query |
| Replace Inline Code with Function Call |
| Replace Loop with Pipeline |
| Replace Query with Parameter |
| Replace Subclass with Delegate |
| Return Modified Value |
| Split Phase |



I realize that the names alone don't convey that much
      about what these new refactorings do, or how the generalized refactorings
      differ from what's in the first edition. In due course I'll be updating
      the [online catalog](https://refactoring.com) to give more information on this.


---
