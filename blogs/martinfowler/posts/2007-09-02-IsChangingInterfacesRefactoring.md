---
title: "Is Changing Interfaces Refactoring"
description: "Is changing the interface of part of the code a refactoring?"
date: 2007-09-02T00:00:00
tags: ["refactoring boundary"]
url: https://martinfowler.com/bliki/IsChangingInterfacesRefactoring.html
slug: IsChangingInterfacesRefactoring
word_count: 191
---


**Is changing the interface of part of the code a refactoring?**


The answer to this question is pretty simple - changing an
  interface is a refactoring
  providing you change all the callers too. A great example of this is
  [Rename Method](http://www.refactoring.com/catalog/renameMethod.html), which is an interface changing refactoring present on
  pretty much all refactoring tools.


The changing of all the callers is an essential part of this
  refactoring. Just changing an interface declaration will break the
  system - and thus isn't a behavior preserving change.


Interface changing refactorings do assume that you can get hold
  of all the callers, which is why you have to be much more careful
  with [PublishedInterfaces](https://martinfowler.com/bliki/PublishedInterface.html). With a published interface, the
  interface itself is part of the observable behavior of the system.


Dynamic languages can make these changes much more
  awkward. Static typing really does help here in pinning down exactly
  which interface is being called at various points. Reflective calls
  that can also make it harder to find, either by embedding method
  names in strings or even composing them at run-time. This is another
 area where tests are essential even in environments that have
 refactoring tools.
