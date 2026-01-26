---
title: "Fixed Length String"
description: "Look at most libraries that talk between application programming 	languages and relational databases, and you'll notice that they map 	the string type in the database (char or varchar) to a string typ"
date: 2003-08-11T00:00:00
tags: ["application architecture"]
url: https://martinfowler.com/bliki/FixedLengthString.html
slug: FixedLengthString
word_count: 343
---


Look at most libraries that talk between application programming
	languages and relational databases, and you'll notice that they map
	the string type in the database (char or varchar) to a string type
	in the programming language. Simple, obvious, but perhaps it's wrong.


The reason I question this is that SQL varchars are fixed length,
	while most application language strings handle any length. This
	causes lots of potential problems on database updates as you always
 have the risk of updating the database with a string that's too large.


One way of dealing with this is to create a fixed length string
	type, where instances know both the length and their value. That way
	whenever you assign a string value to them, they can check it
	against their length. Such an object can then throw an exception or
	truncate, or execute some other behavior. Indeed the behavior of too
	long an input string can be added to the instance data.


Using such a type can make the UI better since UI field widgets
	can interrogate the fixed length string for its size and make a
	widget that only takes that size of input. That's by far the nicest
	way of dealing with over-long input strings, but it's only possible
	if the information is brought forward from the database. Usually
	such information gets lost.


This notion is a specific example of more general design
	issues.

- Insulating the data store, is good, but you still have to
	live by the constraints it imposes on you.
- People are often reluctant to create simple value types when
		they can often make things much easier (see [When To Make a Type](https://martinfowler.com/ieeeSoftware/whenType.pdf)
		for more)
- Putting simple validations in the UI results in a nicer
		interface. The trick is to find ways of doing that without
		duplicating the validation logic.


An object that holds and validates a string can do more than just
	length check. You can include such things as checking against a
	regular expression. But length checks are a simple example that
	makes dealing with databases easier.
