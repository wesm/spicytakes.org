---
title: "Is Declaration Ordering Refactoring"
description: "Is it a refactoring to change the order of declarations, eg 	methods and fields in a Java program?"
date: 2004-09-01T00:00:00
tags: ["refactoring boundary"]
url: https://martinfowler.com/bliki/IsDeclarationOrderingRefactoring.html
slug: IsDeclarationOrderingRefactoring
word_count: 211
---


**Is it a refactoring to change the order of declarations, eg
	methods and fields in a Java program?**


The order in which you declare features in modern programming
	languages doesn't alter the program at all. If you swap two methods
	around in your text file, the program doesn't care. Thus the
	argument against it being a refactoring is that it doesn't
	change how the program works, thus it doesn't change the design,
	thus it can't be a refactoring.


In my [DefinitionOfRefactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html), I used the phrase âto
	make it easier to understand and cheaper to modifyâ. Can changing
	declarations do this? In some cases I think it does. It can make
	sense to put related features in a class together. You can also
	order the features in such a way to help explain how the class works
	- this is particularly valuable when you writing test cases
	  (although here, in some xunit implementations, the order might
	  affect the execution). So since it improves the understandability of the code, I
	  would count reordering declarations as a refactoring.


The fact that it doesn't alter the internal execution is a
	red-herring. Changing the name of a method doesn't alter the
	execution, yet renaming is a very important refactoring to improve
	the understandability of a program.
