---
title: "Nasty Software Hacks and Intel’s CPUID"
date: 2005-08-16
url: https://blog.codinghorror.com/nasty-software-hacks-and-intels-cpuid/
slug: nasty-software-hacks-and-intels-cpuid
word_count: 589
---

We were discussing nasty software hacks today at lunch. The worst hacks are always in software, but those software hacks have an insidious tendency to seep into the hardware, too. I was reminded of Intel’s [infamous CPUID hack](https://web.archive.org/web/20051102082349/http://linux.omnipotent.net/article.php?article_id=11457):


> Prior to the Pentium, software had to jump through elaborate loops to determine exactly what type of CPU was installed on an 80x86 computer. These methods involved checking for illegal opcodes, using known bugs in prior processors, a voodoo doll of Charles Babbage, and a Ouija board. Intel fixed some of these problems with CPUID.
> The CPUID opcode was introduced to the late models of the Intel 486 (486SL and 486DX4). The Intel Pentium, along with its various clones and successors, have all included this instruction. CPUID allows software to gain information on the CPU type and version. CPUID Function 0 returns an ASCII string, identifying the vendor (“GenuineIntel,” “CyrixInstead,” “AuthenticAMD,” etc.). CPUID Function 1 returns the CPU family, model, and stepping.
> Intel identifies its various processor using a combination of the family and model codes. Pentium processors are identified by a family code of 5. A family code of 6 covers the PentiumPro and all of its variants. Since the PentiumPro, Pentium II, Pentium III and Celeron are all based on the same processor architecture, they are all part of the P6 family( hence, family code 6). The model code is used to tell the various P6 processors apart, along with the cache size and brand ID, depending on the CPU (it’s messy; don’t ask).
> Intel decided to make a new family code for the Pentium 4. That’s where the fun begins.
> The average person would think Intel would just increment the family code, making the Pentium 4 part of ‘family 7.’ That does make sense, but Intel already has a family code 7 processor: the Itanium (it came before the Pentium 4, even though the P4 hit the market first). Ok, no problem. Just make the Pentium 4’s family code 8 instead of 7. Wrong. Big problem.
> Microsoft Windows NT 4.0 ran into a bit of a snag with “family 8.” For those not schooled in the ways of binary, the decimal number 8 is “1000” in binary. That’s four binary digits. Four bits.
> Four bits. Remember that, because it’s important.
> When Windows NT 4.0 and its six service packs were released, the largest CPU family code was 6. That’s “110” in binary. Only three bits. So **the NT code only looks at the first three bits of the CPU family when configuring the system.**
> If you haven’t figured it out by now, the first three bits of 8 are zero, zero and, you guessed it, zero. Windows NT goes wacko when it sees a CPU family zero. Serious wacko. Jack with an axe at the end of [The Shining.](http://www.imdb.com/title/tt0081505/) wacko. Since Windows 2000 wasn’t in wide release at the time, and Intel wanted to avoid this tech support issue, the family code had to be changed to avoid a conflict with Windows NT.
> So **now the family code for the Pentium 4 is 15, or “1111” in binary, so the first three bits look like ‘CPU family 7’ to Windows NT.**


This hack is nasty enough to make even Raymond Chen, the patron saint of [nasty software hacks](https://web.archive.org/web/20051125231632/http://blogs.msdn.com/oldnewthing/archive/2003/12/24/45779.aspx), blanch. On the other hand, it is an instant upgrade from processor family 8 to processor family 15! Gee, thanks Windows NT 4.0!

[security](https://blog.codinghorror.com/tag/security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[intel](https://blog.codinghorror.com/tag/intel/)
[cpuid](https://blog.codinghorror.com/tag/cpuid/)
