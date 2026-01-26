---
title: "Humble Object"
description: "Some program elements are inherently difficult, or even impossible to test.   Any logic in these elements is thus prone to bugs and difficult to evolve. To   mitigate this problem, move as much as log"
date: 2020-04-29T00:00:00
tags: ["testing"]
url: https://martinfowler.com/bliki/HumbleObject.html
slug: HumbleObject
word_count: 197
---


Some program elements are inherently difficult, or even impossible to test.
  Any logic in these elements is thus prone to bugs and difficult to evolve. To
  mitigate this problem, move as much as logic as possible out of the
  hard-to-test element and into other more friendly parts of the code base. By
  making untestable objects humble 1, we reduce the
  chances that they harbor evil bugs.


1: 
        The use of the word âhumbleâ originated in [an article by Michael
        Feathers](https://martinfowler.com/articles/humble-dialog-box.html) .


![](images/humble-object/sketch.png)


A common example of this is in the user-interface. Some platforms provide
  no hooks to enable us to run automated tests against UI controls. Even those
  that do often make it difficult, with complex setup, special frameworks, and
  slow-running tests. But we can often test effectively by ensuring these
  controls have the absolute minimum of behavior, using patterns like [Presentation Model (MVVM)](https://martinfowler.com/eaaDev/PresentationModel.html) and [Passive
  View](https://martinfowler.com/eaaDev/PassiveScreen.html).


For more details on this approach the key source is Gerard Meszaros's xUnit
  Test Patterns book - the entry on [Humble
  Object](http://xunitpatterns.com/Humble%20Object.html) is online and includes much more depth including variations and
  examples.


## Notes


1: 
        The use of the word âhumbleâ originated in [an article by Michael
        Feathers](https://martinfowler.com/articles/humble-dialog-box.html) .
