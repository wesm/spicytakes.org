---
title: "Revisiting Edit and Continue"
date: 2006-02-05
url: https://blog.codinghorror.com/revisiting-edit-and-continue/
slug: revisiting-edit-and-continue
word_count: 660
---

Edit and Continue, which shipped in Visual Studio 2005, is generally regarded as *A Good Thing*. It’s pretty difficult to argue against the benefits of [immediacy when debugging](https://blog.codinghorror.com/edit-and-continue/), but that isn’t about to stop some people:

- [Frans Bouma](http://weblogs.asp.net/fbouma/archive/2003/08/01/22211.aspx)
*People who grew up with assemblers, the gnu commandline C debugger and other terrible tools, know that debugging using a debugger is a last resort and also learned that debugging is not about using a debugger, but about understanding the difference between the source code which should have been written and the source code that is written. Edit and Continue doesn’t help you with finding more bugs at a faster rate. You know what does? Design by contract like Eiffel has, pre/post conditions in the code and proper design by designing algorithms first on paper or in a design tool, not behind a keyboard with a code editor in front of you.*
- [John Robbins](https://web.archive.org/web/20060219194112/http://wintellect.com/WEBLOGS/wintellect/archive/2004/10/17/546.aspx)
*Edit and continue is a bug-introducing machine. Why? Because you get to focusing on that one bug and twiddle the code to fix that one bug and introduce six more. When you’re debugging, you’re debugging, not editing. When you start editing, you need to stop to think and plan for the ramifications of those changes. To paraphrase Dykstra: “Use of a debugger is an indication of sloppy thinking. Use of edit and continue is an indication of insanity!”*
- [Sam Gentile](https://web.archive.org/web/20060221144806/http://samgentile.com/blog/archive/2004/10/19/12240.aspx)
*Program logic should not be tested in the debugger. You are wasting your time and your company’s time if you do so. The debugger is for intractable problems. It was John who taught me that lesson in his seminal Windows Debugging book – you shouldn’t be in the debugger unless you have to be. Unit tests are the place to verify, refactor and edit as you go; not the debugger.*


While they raise some valid points, the underlying argument is essentially the same in all three cases: **Edit and Continue should be removed because it’s dangerous**. And we’re clearly too stupid to be trusted with a dangerous tool like edit and continue!


This reminds me of a similar scenario in video games. There are two types of video games:

1. games that allow you to save your progress anywhere you like.
2. games that only allow you to save your progress at specific points placed in the game by the developers.


If you are killed between saves, you have to go back to the last save.


Certain groups of hard-core gamers think “save anywhere” games are fatally flawed. Real men, they say, work their way through a level and earn the save point. They believe that games should remove the “save anywhere” option, lest we all become a bunch of spoiled, lazy gamers who can barely lift our thumbs.


But here’s what drives me crazy: **the hard-core gamers *don’t have to use save anywhere!*** If they’re so hard-core, they should easily be able to resist the temptation to save their game. They can simply save at the beginning of a level, or confine themselves a few saves per level, or whatever. So when they say the “save anywhere” option should be removed, **what they’re really saying is, “everyone should play games the same way we do,”** and veiling it in some macho rhetoric to intimidate people into agreeing with them.


The comparison between game saves and edit and continue is fairly apt; either you can edit a program whenever you want – even at a breakpoint in a debugger – or you can only do it when the program is stopped. Clearly, offering both options is more flexible and inhibits no one.


However, there’s a big difference between *encouraging people to take challenges* and *forcing them* *to take challenges by removing flexibility from the product*. Not everyone plays games for the same reasons you do. And not everyone writes code for the same reasons you do, either.

[debugging](https://blog.codinghorror.com/tag/debugging/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[edit and continue](https://blog.codinghorror.com/tag/edit-and-continue/)
