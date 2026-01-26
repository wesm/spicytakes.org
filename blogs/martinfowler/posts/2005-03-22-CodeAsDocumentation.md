---
title: "Code As Documentation"
description: "One of the common elements of agile methods is that they raise 	 programming to a central role in software 	development - one much greater than the software engineering 	community usually does. Part o"
date: 2005-03-22T00:00:00
tags: ["agile", "documentation"]
url: https://martinfowler.com/bliki/CodeAsDocumentation.html
slug: CodeAsDocumentation
word_count: 682
---


One of the common elements of agile methods is that they raise
	 programming to a central role in software
	development - one much greater than the software engineering
	community usually does. Part of this is classifying the code as a
	major, if not the primary documentation of a software system.


Almost immediately I feel the need to rebut a common
	misunderstanding. Such a principle is not saying that code is the
	only documentation. Although I've often heard this said of Extreme
	Programming - I've never heard the leaders of the Extreme
	Programming movement say this. Usually there is a need for
	further documentation to act as a supplement to the code.


The rationale for the code being the primary source of
	documentation is that it is the only one that is sufficiently
	detailed and precise to act in that role - a point made so
	eloquently by Jack Reeves's famous essay [âWhat
  is Software Design?â](http://www.developerdotstar.com/mag/articles/reeves_design_main.html)


This principle comes with a important consequence - that it's
	important that programmers put in the effort to make sure that this
	code is clear and readable. Saying that code is documentation isn't
	saying that a particular code base is good documentation. Like any
	documentation, code can be clear or it can be gibberish. Code is no
	more inherently clear than any other form of documentation. (And
	other forms of documentation can be hopelessly unclear too - I've
	seen plenty of gibberish UML diagrams, to flog a popular horse.)


Certainly it seems that most code bases aren't very good
	documentation. But just as it's a fallacy to conclude that declaring
	code to be documentation excludes other forms, it's a fallacy to say
	that because code is often poor documentation means that it's
	*necessarily* poor. It is possible to write clear code, indeed I'm
	convinced that most code bases can be made much more clear.


I think part of the reason that code is often so hard to read is
	because people aren't taking it seriously as documentation. If
	there's no will to make code clear, then there's little chance it
	will spring into clarity all by itself. So the first step to clear
	code is to accept that code is documentation, and then put the
	effort in to make it be clear. I think this comes down to what was
	taught to most programmers when they began to program. My teachers didn't put much emphasis on
	making code clear, they didn't seem to value it and certainly didn't
	talk about how to do it. We as a whole industry need to put much
	more emphasis on valuing the clarity of code.


The next step is to learn how, and here let me offer you the
	advice of a best selling technical author - there's nothing like
	review. I would never think of publishing a book without having many
	people read it and give me feedback. Similarly there's nothing more
	important to clear code than getting feedback from others about
	what is or isn't easy to understand. So take every opportunity to
	find ways to get other people to read your code. Find out what they
	find easy to understand, and what things confuse them. (Yes, pair
	programming is a great way to do this.)


For more concrete advice - well I suggest reading good books on
	programming style. [Code Complete](https://www.amazon.com/gp/product/0735619670/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0735619670&linkCode=as2&tag=martinfowlerc-20) is the first place to look. I'll
	naturally suggest [Refactoring](https://martinfowler.com/books/refactoring.html) - after all much of refactoring is
	about making code clearer. After Refactoring, [Refactoring to
	Patterns](https://martinfowler.com/books/r2p.html) is an obvious suggestion.


You'll always find people will disagree on various
	points. Remember that a code base is owned primarily by a team (even
	if you practice individual code ownership over bits of it). A
	professional programmer is prepared to bend her personal style to
	reflect the needs of the team. So even if you like ternary operators
	don't use them if your team doesn't find them easy to
	understand. You can program in your own style on your personal
	projects, but anything you do in a team should follow the needs of
	that team.


reposted on 25 Mar 2015
