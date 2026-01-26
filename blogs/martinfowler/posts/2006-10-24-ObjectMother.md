---
title: "Object Mother"
description: "An object mother is a kind of class used in testing to help 	create example objects that you use for testing."
date: 2006-10-24T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/ObjectMother.html
slug: ObjectMother
word_count: 452
---


An object mother is a kind of class used in testing to help
	create example objects that you use for testing.


When you write tests in a reasonably sized system, you find you
	have to create a lot of example data. If I want to test a sick pay
	calculation on an employee, I need an employee. But this isn't just
	a simple object - I'll need the employee's marital status, number of
	dependents, some employment and payroll history. Potentially this
	can be a lot of objects to create. This set data is generally
	referred to as the test fixture.


The first move is to create fixture in the setup method of an
	xunit test - that way it can be reused in multiple tests. But the
	trouble with this is often you need similar data in multiple test
	classes. At this point it makes sense to have a factory object that
	can return standard fixtures. Maybe 'John', an employee who just got
	hired last week; 'Heather' and employee who's been around for a
	decade.


Object Mother is just a catchy name for such a factory. The name
	was coined on a Thoughtworks project at the turn of the century
	and it's catchy enough to have stuck.


The canned objects that the Object Mother produces become
	familiar to the team, often invading even discussions with the
	users. In this way they resemble the notion of personas - although
	they aren't always people. They could be insurance policies, supply
	contracts, whatever data a test framework needs. Using similar data
	on multiple tests helps people be familiar with the examples you're using.


These canned objects often aren't just right for a particular
	test, but often can be made right with some additional setup. âLet's
	take John and make him go off sick two months ago.â Occasionally you'll
	need to add a new canned object to the mother, but try to tweak an
	existing one if you can - that way the reader of the test will
	understand quicker if they are familiar with the existing canned objects.


Usually you'll have several kinds of objects that you'll need to
  birth, so it's handy to make different mothers for different
  classes: eg `CustomerMother`, `ProductMother`,
  etc.


Object Mothers do have their faults. In particular there's a
	heavy coupling in that many tests will depend on the exact data in
	the mothers. As a result it's tricky should you want to change that
	standard data for any reason. Changes to classes will also result in
	the need to migrate the tests - although that will be an issue in
	any case.


## Further Reading


Peter Schuh and Stephanie Punke wrote a [paper on object mothers](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.4710&rep=rep1&type=pdf)
	for XP Universe.
