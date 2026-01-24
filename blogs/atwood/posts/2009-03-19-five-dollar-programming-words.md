---
title: "Five Dollar Programming Words"
date: 2009-03-19
url: https://blog.codinghorror.com/five-dollar-programming-words/
slug: five-dollar-programming-words
word_count: 991
---

I’ve been a longtime [fan of Eric Lippert’s blog](https://blog.codinghorror.com/eric-lipperts-purple-crayon/). And one of my favorite (albeit short-lived) post series was his **Five Dollar Words for Programmers**. Although I’ve sometimes been [accused of being too wordy](https://web.archive.org/web/20090322221750/http://gandolf.homelinux.org/blog/index.php?id=52), I find that learning the right word to describe something you’re doing is a small step on the road towards [understanding and eventual mastery](https://blog.codinghorror.com/sharpening-the-saw/).


Why are these words worth five dollars? They’re **uncommon words that have a unique and specialized meaning in software development**. They are a bit off the beaten path. Words you don’t hear often, but also words that provide the thrill of discovery, that “aha” moment as you realize a certain programming concept you knew only through experimentation and intuition has a *name*.


![](https://blog.codinghorror.com/content/images/2025/04/image-338.png)


Eric provides examples of a few great five dollar programming words on his blog.


1. [**Idempotent**](https://web.archive.org/web/20080428225937/http://blogs.msdn.com:80/ericlippert/archive/2005/10/26/483900.aspx)


> There are two closely related definitions for idempotent. A value is “idempotent under function foo” if the result of doing foo to the value results in the value right back again.
> A function is “idempotent” if the result of doing it twice (feeding the output of the first call into the second call) is exactly the same as the result of doing it once. (Or, in other words, every output of the function is idempotent under it.)


This isn’t just academic. Eric notes that idempotence is used all the time in caching functions that create the object being requested. Calling the function two or a thousand times returns the same result as calling it once.


**2. **[**Orthogonality**](https://web.archive.org/web/20090321231640/http://blogs.msdn.com/ericlippert/archive/2005/10/28/483905.aspx)


> Imagine for instance that you were trying to describe how to get from one point in an empty room to another. A perfectly valid way to do so would be to say how many steps to go north or south, and then how many steps to go northeast or southwest. This hockey-stick navigation system is totally workable, but it feels weird because north and northeast are not orthogonal – you can’t change your position by moving northeast without also at the same time changing how far north you are. With an orthogonal system – say, the traditional north-south/east-west system – you can specify how far north to go without worrying about taking the east-west movement into account at all.
> Nonorthogonal systems are hard to manipulate because it’s hard to tweak isolated parts. Consider my fish tank for example. The pH, hardness, oxidation potential, dissolved oxygen content, salinity and conductivity of the water are very nonorthogonal; changing one tends to have an effect on the others, making it sometimes tricky to get the right balance. Even things like changing the light levels can change the bacteria and algae growth cycles causing chemical changes in the water.


Orthogonality is a powerful concept that [applies at every level of coding](https://web.archive.org/web/20090321205328/http://brandonbyars.com/blog/articles/2008/07/21/orthogonality), from the architecture astronaut to the lowest level code monkey. If modifying item #1 results in unexpected behavior in item #2, you have a major problem – that’s a form of unwanted coupling. Dave Thomas illustrates with a [clever helicopter analogy](http://www.artima.com/intv/dry3.html):


> It sounds fairly simple. You can use the pedals to point the helicopter where you want it to go. You can use the collective to move up and down. Unfortunately, though, because of the aerodynamics and gyroscopic effects of the blades, all these controls are related. So one small change, such as lowering the collective, causes the helicopter to dip and turn to one side. You have to counteract every change you make with corresponding opposing forces on the other controls. However, by doing that, you introduce more changes to the original control. So you’re constantly dancing on all the controls to keep the helicopter stable.
> That’s kind of similar to code. We’ve all worked on systems where you make one small change over here, and another problem pops out over there. So you go over there and fix it, but two more problems pop out somewhere else. You constantly push them back – like that Whack-a-Mole game – and you just never finish. If the system is not orthogonal, if the pieces interact with each other more than necessary, then you’ll always get that kind of distributed bug fixing.


3. [**Immutability**](https://web.archive.org/web/20090506003020/http://blogs.msdn.com/ericlippert/archive/2007/11/13/immutability-in-c-part-one-kinds-of-immutability.aspx)


Immutability is a bit more broad, but the commonly accepted definition is based on the fact that `String` objects in Java, C#, and Python [are immutable](http://en.wikipedia.org/wiki/Immutable_object).


> There’s nothing you can do to the number one that changes it. You cannot paint it purple, make it even or get it angry. It’s the number one, it is eternal, implacable and unchanging. Attempting to do something to it – say, adding three to it – doesn’t change the number one at all. Rather, it produces an entirely different and also immutable number. If you cast it to a double, you don’t change the integer one; rather, you get a brand new double.
> Strings, numbers and the null value are all truly immutable.


Try to imagine your strings painstakingly carved out of enormous blocks of granite. Because they are – they’re immutable! It may seem illogical that every time you modify a `string`, the original is kept as-is and an entirely new `string` is created. But this is done for [two very good technical reasons](http://stackoverflow.com/questions/93091/why-cant-string-be-not-immutable-in-java-and-net). Understanding immutability is [essential to grok string performance](https://blog.codinghorror.com/the-sad-tragedy-of-micro-optimization-theater/) in those languages.


I don’t pretend that these three words are particularly unique or new, just a tiny bit off the beaten path. They were, however, new *to me* at one time, and discovering them marked a small milestone in my own evolution as a programmer.


**What’s *your* favorite five dollar programming word?** And how did it help you reach that particular “aha” moment in *your* code? (Links to references/definitions greatly appreciated in comments – perhaps we can all discover at least *one* new five dollar programming word today. Remember, learn four and you’ll earn a cool twenty bucks worth of knowledge!)

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
