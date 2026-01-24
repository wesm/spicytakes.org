---
title: "Have You Met Your Dog, Patches?"
date: 2009-08-27
url: https://blog.codinghorror.com/have-you-met-your-dog-patches/
slug: have-you-met-your-dog-patches
word_count: 622
---

The Gamasutra article [Dirty Coding Tricks](https://web.archive.org/web/20090821181409/http://www.gamasutra.com/view/feature/4111/dirty_coding_tricks.php) is a fantastic read. One part of it in particular rang true for me.


> Consider the load of pain I found myself in when working on a conversion of a 3D third person shooter from the PC to the original PlayStation.
> Now, the PS1 has no support for floating point numbers, so we were doing the conversion by basically recompiling the PC code and overloading all floats with fixed point. That actually worked fairly well, but were it fell apart was in collision detection.
> The level geometry that was supplied to us worked reasonably well in the PC version of the game, but when converted to fixed point, all kinds of seams, T-Junctions and other problems were nudged into existence by the microscopic differences in values between fixed and floats. This problem would manifest itself by the main character (called “Damp”) simply falling through those tiny holes, into the abyss below the level.
> We patched the holes we found, tweaking the geometry until Damp no longer fell through. But then the game went into test at the publisher, and suddenly a flood of “falling off the world” bugs were delivered to us. Every day a fresh batch of locations were found with these little holes that Damp could slip through. We would fix that bit of geometry, then the next day they would send us ten more. This went on for several days. The publisher’s test department employed one guy whose only job was to jump around the world for ten hours a day, looking for places he could fall through.
> **The problem here was that the geometry was bad.** It was not tight and seamless geometry. It worked on the PC, but not on the PS1, where the fixed point math vastly magnified the problems. The ideal solution was to fix the geometry to make it seamless.
> However, this was a vast task, impossible to do in the time available with our limited resources, so we were relying on the test department to find the problem areas for us.


There’s never time to do it right, but there’s always time to do it over. If this sounds familiar, you’re not alone. I have at times found myself slipping into this pattern, continually patching the same code over and over. It’s the kind of code that, when submitted for code review, you’re tempted to self-deprecatingly introduce as **have you met my dog, patches?**


![](https://blog.codinghorror.com/content/images/2025/04/image-426.png)


While “patchiness” isn’t always a bad thing – the venerable Apache HTTP Server is testament to that – it’s [probably an exception](http://en.wikipedia.org/wiki/Apache_HTTP_Server#History_and_name).


> the original FAQ on the Apache Server project’s website, from 1996 to 2001, claimed that “The result after combining [the NCSA httpd patches] was a patchy server.”


Reading the Gamasutra article shamed me into to attacking a section of extra-patchy Stack Overflow code. Code which I constantly had to tweak in various ongoing ways to get it to work right. But first, I had to [get over my fear](https://blog.codinghorror.com/dont-be-afraid-to-break-stuff/). Fear. That’s what led to all the patching in the first place. It was obvious this was working code which had [become crufty over time](https://blog.codinghorror.com/paying-down-your-technical-debt/), but it *was working*. And it’s one of the core bits of functionality in the site. In those circumstances, it’s easy to mentally justify “just this small change, just this once” rather than the fundamental rewrite you really need.


When you finally realize you’ve spent the last six months telling yourself the same “just this small change, just this once” lie, then **you’ve met your dog patches, too**.


Now what are you going to do about that rascally scamp?

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[game development](https://blog.codinghorror.com/tag/game-development/)
[conversion techniques](https://blog.codinghorror.com/tag/conversion-techniques/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
