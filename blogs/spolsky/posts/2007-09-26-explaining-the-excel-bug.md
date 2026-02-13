---
title: "Explaining the Excel Bug"
date: 2007-09-26
url: https://www.joelonsoftware.com/2007/09/26/explaining-the-excel-bug/
word_count: 1087
---


By now you’ve probably seen a lot of the brouhaha over a [bug](http://groups.google.com/group/microsoft.public.excel/browse_thread/thread/2bcad1a1a4861879/2f8806d5400dfe22?hl=en&lnk=st&q=excel+2007+bug+100000+molham+serry&rnum=29#2f8806d5400dfe22) in the newest version of Excel, 2007. Basically, multiplying 77.1*850, which should give you 65,535, was actually displaying 100,000.


Before I try to explain this, I should disclose that I did work on the Excel team, but that was *thirteen years ago*. I haven’t been there for a long time. I don’t even think I know anyone on that team any more. I’m just trying to explain the bug a little bit as a public service.


The first thing you have to understand is that Excel keeps numbers, internally, in a binary format, but displays them as strings. For example, when you type 77.1, Excel stores this internally using 64 bits:


0100 0000 0101 0011 0100 0110 0110 0110
0110 0110 0110 0110 0110 0110 0110 0110


The display is showing you four characters: “7”, “7”, “.”, and “1”.


Somewhere inside Excel is a function that converts binary numbers to strings for displaying. This is the code that has the bug that causes a few numbers which are *extremely close* to 65,535 to be formatted incorrectly as 100,000.


If you use the number further along in calculations, for example, if you add 2 to the results, you’ll get the right thing.


=77.1*850 -> displays 100000


=77.1*850+2 -> displays 65537, correctly.


Just to throw people off, this bug also exists for a few numbers which are *extremely close* to 65,536. They display incorrectly as 100,001.


=77.1*850+1 -> displays 100,001, incorrectly.


This is still only a bug in the number formatting code; if you try to make a chart with that number in it, you’ll get a correct chart.


Now… you may have noticed that I said that this bug exists for numbers which are *extremely close to 65,535*, but not for 65,535 itself. Indeed if you enter 65,535 you see 65,535. But, you notice, 77.1 * 850 should be exactly 65,535, not *extremely close to* 65,535!


Look closely at the binary representation for 77.1:


0100 0000 0101 0011 0100 0110 0110 0110
0110 0110 0110 0110 0110 0110 0110 0110


See how there’s a lot of 0110 0110 0110 there at the end? That’s because **0.1** has *no exact representation in binary*… it’s a repeating binary number. It’s sort of like how 1/3 has no representation in decimal. 1/3 is 0.33333333 and you have to keep writing 3’s forever. If you lose patience, you get something inexact.


So you can imagine how, in decimal, if you tried to do 3*1/3, and you didn’t have time to write 3’s forever, the result you would get would be 0.99999999, not 1, and people would get angry with you for being wrong.


The same thing happens in binary with  numbers ending in 0.1: they are repeating decimals, so when you do mathematical operations on them, very small insignificant errors creep in somewhere *way* to the right of the decimal point. (PS: same for .2, .3, .4, .6, .7, .8, and .9, but not .5).


The [IEEE](http://www.ieee.org/) has a standard, [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating-point_standard), for how to represent floating point numbers in binary, and this is what almost everybody uses, including [Excel](http://support.microsoft.com/kb/78113), and they have for a really long time, and it means sometimes you get imprecise results when you add a lot of 0.1’s together, but if you’re rounding the numbers to a reasonable number of decimal points, you won’t really care.


Back to the Excel bug, which is a genuine bug, not just an artifact of this IEEE 754 stuff. Since 77.1 has no *exact* representation, Excel stores it as


0100 0000 0101 0011 0100 0110 0110 0110
0110 0110 0110 0110 0110 0110 0110 0110


and then when you try to multiply it by 850, you get something very close to 65,535, but not *exactly* 65,535, because of the fact that 77.1 wasn’t stored exactly because that would take infinite memory. And this number, which is very close to 65,535, happens to be one of only [12 possible floating point numbers which trigger this bug in Excel](http://blogs.msdn.com/excel/archive/2007/09/25/calculation-issue-update.aspx).


OK, Q&A.


**Q: Isn’t this really, really bad?**


A: IMHO, no, the chance that you would see this in real life calculations is microscopic. Better worry about getting hit by a meterorite. Microsoft, of course, will be forced to tell everyone “accuracy is extremely important to us” and I’m sure they’ll have a fix in a matter of days, and they’ll be subjected to all kinds of [well-deserved ridicule](http://weblog.raganwald.com/2007/09/dear-valued-client-thank-you-for-your.html), but since I don’t work there I’m free to tell you that the chance of this bug actually mattering to you as an individual is breathtakingly small.


**Q: Shouldn’t they be testing for these kinds of things?**


A: I’ll bet that most of the numeric testing done on the Excel team is done automatically with VBA code. Cells containing this value *display* as 100,000, but from VBA, they’re going to look like 65,535 (since the number would be passed into the Basic runtime in binary, before the display formatting.) I’m sure there’s plenty of code to test display formatting, but with a bug like this that only happens on 12 out of 18446744073709551616 possible floating point binary numbers, it’s unlikely that any set of black-box tests would cover this case.


**Q: What caused the bug?**


A: I’m not sure exactly, since I don’t have the code. Off the top of my head, I can’t think of anything that would cause this behavior. Play around with [Quanfei Wen’s IEEE-754 calculator](http://babbage.cs.qc.edu/IEEE-754/Decimal.html), maybe you’ll find something.


**Q: Why not use “exact” (decimal) arithmetic?**


A: It’s much slower than floating point arithmetic, since there’s no hardware on your CPU chip to do it for you natively.


Over the years, Microsoft got so much heat for floating point rounding artifacts in the Windows Calculator that they rewrote it to use an arbitrary-precision arithmetic library. Since you have to poke at Windows Calculator with a stick, it doesn’t have to be as fast as Excel. That said, CPUs have gotten pretty fast. I’ll bet an arbitrary-precision version of Excel would perform pretty well these days. Still, the Microsoft Excel support team has spent the last 20 years defending IEEE 754, and it’s not surprising that they’ve started to believe in it.


And let’s face it — do you really want the bright sparks who work there now, and manage to break lots of perfectly good working code — rewriting the core calculating engine in Excel? Better keep them busy adding and removing dancing paper clips all day long.
