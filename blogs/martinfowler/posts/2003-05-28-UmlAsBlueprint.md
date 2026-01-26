---
title: "Uml As Blueprint"
description: "For a long time engineering influenced software processes have looked for a way to express software designs in such a way that the designs can be handed off to a separate group to write the code, much"
date: 2003-05-28T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/UmlAsBlueprint.html
slug: UmlAsBlueprint
word_count: 334
---


For a long time engineering influenced software processes have
looked for a way to express software designs in such a way that the
designs can be handed off to a separate group to write the code, much
as blueprints are used in building bridges. This would allow rare and
expensive software designers to concentrate on the blueprints while
many cheaper coders concentrate on construction.


As a result [UmlAsBlueprint](https://martinfowler.com/bliki/UmlAsBlueprint.html)  is a [UmlMode](https://martinfowler.com/bliki/UmlMode.html) that focuses on completeness. In forward
engineering the idea is that blueprints are developed by a designer
whose job is to build a detailed design for a programmer to code up.
That design should be sufficiently complete that all design decisions
are laid out and the programming should follow as a pretty
straightforward activity that requires little thought. The designer
may be the same person as the programmer, but usually the designer is
a more senior developer who designs for a team of programmers.


In reverse engineering, blueprints aim to convey detailed
information about the code, either in paper documents or as an
interactive graphical browser. The blueprints can show every detail
about a class in a graphical form that's easier for developers to
understand.


Blueprints require much more sophisticated tools than sketches in
order to handle the details required for the task. Specialized CASE
(Computer Aided Software Engineering) tools fall into this category
(although the term CASE has become a dirty word and vendors try to
avoid it now.) Forward engineering tools support diagram drawing and
back it up with a repository to hold the information. Reverse
engineering tools read source code and interpret from it into the
repository and generate diagrams. Tools that can do both forward and
reverse engineering like this are referred to as round-trip tools.


Some tools use the source code itself as the repository and use
diagrams as a graphic viewport on the code. These tie much more
closely into programming and often integrate directly with programming
editors. I like to think of these as tripless tools.
