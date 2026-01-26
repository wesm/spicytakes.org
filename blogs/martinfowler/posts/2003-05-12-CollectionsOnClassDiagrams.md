---
title: "Collections On Class Diagrams"
description: "Lets say you have an album class which has an ArrayList of tracks. How do you show this in a UML class diagram?"
date: 2003-05-12T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/CollectionsOnClassDiagrams.html
slug: CollectionsOnClassDiagrams
word_count: 175
---


**Lets say you have an album class which has an ArrayList of tracks. How
do you show this in a UML class diagram?**


Usually you don't show the collection on the class diagram as a
class. All you do is show an association between the album class and
the track class. By marking the association with a ***** multiplicity you
imply that a collection is in play.


This raises the question of which collection. To be strict with the
UML you should always use a set for your collections since multivalued
properties have set semantics in UML. To show an ordered collection,
like a list, you need to mark the association as `{ordered}`. In
practice most people use lists for collections (if nothing else it can
help testing). That's okay too, although strictly you should be aware
of introducing duplicates to the collection.


If you want to show some special collection is being used, then you
can use a stereotype such as `<<doubly linked list>>`. However you
should find you only do this very rarely.
