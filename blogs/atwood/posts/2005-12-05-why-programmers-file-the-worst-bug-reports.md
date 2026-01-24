---
title: "Why Programmers File the Worst Bug Reports"
date: 2005-12-05
url: https://blog.codinghorror.com/why-programmers-file-the-worst-bug-reports/
slug: why-programmers-file-the-worst-bug-reports
word_count: 406
---

Who files better bugs? Users or developers? In [How to Report Bugs Effectively](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html), Simon Tatham notes that software developers, contrary to what you might think, file some of the worst bug reports:


> It isn’t only non-programmers who produce bad bug reports. **Some of the worst bug reports I’ve ever seen come from programmers, and even from good programmers.**
> I worked with another programmer once, who kept finding bugs in his own code and trying to fix them. Every so often he’d hit a bug he couldn’t solve, and he’d call me over to help. “What’s gone wrong?” I’d ask. He would reply by telling me his current opinion of what needed to be fixed.
> This worked fine when his current opinion was right. It meant he’d already done half the work and we were able to finish the job together. It was efficient and useful.
> But quite often he was wrong. We would work for some time trying to figure out why some particular part of the program was producing incorrect data, and eventually we would discover that it wasn’t, that we’d been investigating a perfectly good piece of code for half an hour, and that the actual problem was somewhere else.
> I’m sure he wouldn’t do that to a doctor. “Doctor, I need a prescription for Hydroyoyodyne.” People know not to say that to a doctor: you describe the symptoms, the actual discomforts and aches and pains and rashes and fevers, and you let the doctor do the diagnosis of what the problem is and what to do about it. Otherwise the doctor dismisses you as a hypochondriac or crackpot, and quite rightly so.


Programmers file bad bug reports for the same reason that programmers screw up [usability tests](https://web.archive.org/web/20051218031257/http://www.webpagecontent.com/arc_archive/124/5/): **they mean well, but they’re heavily prone to prescription instead of observation.** In a usability test, most developers can’t bear to see the user fail, and will actually intervene on the user’s behalf. “Wait – don’t click there! Click here!”


This, of course, completely screws up the usability test.


Developers’ heads are full of cool technical arcana, and that’s precisely why they need to resist the urge to screw up their bug reports with inappropriate prescriptions. Cultivate your observation skills! Slapping together a hastily concocted call to action is easy; patiently observing and collecting evidence to make a compelling case is much more difficult.

[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[bug reports](https://blog.codinghorror.com/tag/bug-reports/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
