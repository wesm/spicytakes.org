---
title: "Test Doubles: A Taxonomy of Pretend Objects"
date: 2007-01-08
url: https://blog.codinghorror.com/test-doubles-a-taxonomy-of-pretend-objects/
slug: test-doubles-a-taxonomy-of-pretend-objects
word_count: 206
---

[Ned](https://web.archive.org/web/20070116203529/http://www.nedbatchelder.com/blog/200701.html#e20070108T073027) recently pointed out Martin Fowler’s article [Mocks Aren’t Stubs](http://martinfowler.com/articles/mocksArentStubs.html).


> The vocabulary for talking about [pretend objects] soon gets messy – all sorts of words are used: stub, mock, fake, dummy. For this article I’m going to follow the vocabulary of [Gerard Meszaros’s upcoming book](http://xunitpatterns.com/). It’s not what everyone uses, but I think it’s a good vocabulary and since it's my essay I get to pick which words to use. Meszaros uses the term **Test Double as the generic term for any kind of pretend object used in place of a real object for testing purposes**.


Personally, I like to think of them as *Stunt Objects*. Meszaros, via Fowler, defines the following taxonomy of pretend objects:


![](https://blog.codinghorror.com/content/images/2025/05/image-471.png)


**Dummy objects** are passed around but never actually used. Usually they are just used to fill parameter lists.


![](https://blog.codinghorror.com/content/images/2025/05/image-472.png)


**Fake objects** actually have working implementations, but usually take some shortcut which makes them not suitable for production.


![](https://blog.codinghorror.com/content/images/2025/05/image-473.png)


**Stub objects** provide canned answers to calls made during the test, usually not responding at all to anything outside what’s programmed in for the test.


![](https://blog.codinghorror.com/content/images/2025/05/image-474.png)


**Mock objects** are pre-programmed with expectations which form a specification of the calls they are expected to receive.

[mock](https://blog.codinghorror.com/tag/mock/)
[stub](https://blog.codinghorror.com/tag/stub/)
[fake](https://blog.codinghorror.com/tag/fake/)
[dummy](https://blog.codinghorror.com/tag/dummy/)
[test double](https://blog.codinghorror.com/tag/test-double/)
