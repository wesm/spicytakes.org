---
title: "Why Do Computers Suck at Math?"
date: 2009-05-13
url: https://blog.codinghorror.com/why-do-computers-suck-at-math/
slug: why-do-computers-suck-at-math
word_count: 848
---

You’ve probably seen [this old chestnut](http://www.google.com/search?&q=399999999999999-399999999999998) by now.


Insert your own joke here. Google can’t be wrong – *math is!* But Google is hardly alone; this is just another example in a long and storied history of obscure little computer math errors that go *way* back, such as [this bug report from Windows 3.0](https://web.archive.org/web/20090317043704/http://support.microsoft.com/kb/72540).

1. Start Calculator.
2. Input the largest number to subtract first (for example, 12.52).
3. Press the MINUS SIGN (-) key on the numeric keypad.
4. Input the smaller number that is one unit lower in the decimal portion (for example, 12.51).
5. Press the EQUAL SIGN (=) key on the numeric keypad.


On my virtual machine, 12.52 - 12.51 on Ye Olde Windows Calculator indeed results in 0.00.


![](https://blog.codinghorror.com/content/images/2025/04/image-365.png)


And then there was the [famous Excel bug](http://www.lawtechguru.com/archives/2007/09/25_excel_2007_multiplication_math_bug.html).


> If you have Excel 2007 installed, try this: Multiply 850 by 77.1 in Excel.
> One way to do this is to type “=850*77.1” (without the quotes) into a cell. The correct answer is 65,535. However, Excel 2007 displays a result of 100,000.


At this point, you might be a little perplexed, as **computers are supposed to be pretty good at this math stuff**. What gives? How is it possible to produce such blatantly incorrect results from seemingly trivial calculations? Should we even be trusting our computers to do math at all?


Well, numbers are harder to represent on computers [than you might think](http://www.johndcook.com/blog/2009/04/06/numbers-are-a-leaky-abstraction/):


> A standard floating point number has roughly 16 decimal places of precision and a maximum value on the order of 10308, a 1 followed by 308 zeros. (According to [IEEE standard 754](http://en.wikipedia.org/wiki/IEEE_754), the typical floating point implementation.)
> Sixteen decimal places is a lot. Hardly any measured quantity is known to anywhere near that much precision. For example, the constant in Newton’s Law of Gravity is only known to four significant figures. The charge of an electron is known to 11 significant figures, much more precision than Newton’s gravitational constant, but still less than a floating point number. So **when are 16 figures not enough?** One problem area is subtraction. The other elementary operations – addition, multiplication, division – are very accurate. As long as you don’t overflow or underflow, these operations often produce results that are correct to the last bit. But subtraction can be anywhere from exact to completely inaccurate. If two numbers agree to n figures, you can lose up to n figures of precision in their subtraction. This problem can show up unexpectedly in the middle of other calculations.


Number precision is a funny thing; did you know that an infinitely repeating sequence of 0.999... [is equal to one](http://en.wikipedia.org/wiki/0.999...)?

kg-card-begin: html

> In mathematics, the repeating decimal 0.999… denotes a real number equal to one. In other words: the notations 0.999… and 1 actually represent the same real number.
> This equality has long been accepted by professional mathematicians and taught in textbooks. Proofs have been formulated with varying degrees of mathematical rigour, taking into account preferred development of the real numbers, background assumptions, historical context, and target audience.

kg-card-end: html

Computers [are awesome](https://blog.codinghorror.com/computer-hardware-pornography/), yes, but they aren’t *infinite.*.. yet. So any prospects of storing any infinitely repeating number on them are dim at best. The best we can do is work with approximations at varying levels of precision that are “good enough” where “good enough” depends on what you’re doing, and how you’re doing it. And it’s complicated to get right.


Which brings me to [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://web.archive.org/web/20090227080227/http://docs.sun.com/source/806-3568/ncg_goldberg.html).


> **Squeezing infinitely many real numbers into a finite number of bits requires an approximate representation.** Although there are infinitely many integers, in most programs the result of integer computations can be stored in 32 bits. In contrast, given any fixed number of bits, most calculations with real numbers will produce quantities that cannot be exactly represented using that many bits. Therefore the result of a floating-point calculation must often be rounded in order to fit back into its finite representation. This rounding error is the characteristic feature of floating-point computation.


What do the Google, Windows, and [Excel](https://web.archive.org/web/20090521061345/http://www.lomont.org/Math/Papers/2007/Excel2007/Excel2007Bug.pdf) (pdf) math errors have in common? They’re all related to number precision approximation issues. Google doesn’t think it’s important enough to fix. They’re probably right. But some mathematical rounding errors can be [a bit more serious](https://web.archive.org/web/20090517060208/http://www.maa.org/mathland/mathland_5_12.html).


> Interestingly, the launch failure of the Ariane 5 rocket, which exploded 37 seconds after liftoff on June 4, 1996, occurred because of a software error that resulted from converting a 64-bit floating point number to a 16-bit integer. The value of the floating point number happened to be larger than could be represented by a 16-bit integer. The overflow wasn’t handled properly, and in response, the computer cleared its memory. The memory dump was interpreted by the rocket as instructions to its rocket nozzles, and an explosion resulted.


I’m starting to believe that it’s not the computers that suck at math, but the people programming those computers. I know I’m [living proof of that](https://blog.codinghorror.com/your-favorite-np-complete-cheat/).

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[bug reports](https://blog.codinghorror.com/tag/bug-reports/)
[software bugs](https://blog.codinghorror.com/tag/software-bugs/)
[computer math errors](https://blog.codinghorror.com/tag/computer-math-errors/)
[excel bug](https://blog.codinghorror.com/tag/excel-bug/)
