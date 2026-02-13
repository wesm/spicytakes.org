---
title: "Daily Builds Are Your Friend"
date: 2001-01-27
url: https://www.joelonsoftware.com/2001/01/27/daily-builds-are-your-friend/
word_count: 1849
---


In 1982, my family took delivery of the very first IBM-PC in Israel. We actually went down to the warehouse and waited while our PC was delivered from the port. Somehow, I convinced my dad to get the fully-decked out version, with *two* floppy disks, 128 K memory, and both a dot-matrix printer (for fast drafts) and a Brother Letter-Quality Daisy Wheel printer, which sounds exactly like a machine gun when it is operating, only louder. I think we got almost every accessory available: PC-DOS 1.0, the $75 technical reference manual with a complete source code listing of the BIOS, Macro Assembler, and the stunning IBM Monochrome display with a full 80 columns and … lower case letters! The whole thing cost about $10,000 including Israel’s then-ridiculous import taxes. Extravagant!


Now, “everybody” knew that BASIC was a children’s language that requires you to write spaghetti code and turns your brain into Camembert cheese. So we shelled out $600 for IBM Pascal, which came on three floppy diskettes. The compiler’s first pass was on the first diskette, the second pass was on the second diskette, and the linker was on the third diskette. I wrote a simple “hello, world” program and compiled it. Total time elapsed: 8 minutes.


Hmm. That’s a long time. I wrote a batch file to automate the process and shaved it down to 7 1/2 minutes. Better. But when I tried to write long programs like my stunning version of Othello which *always* beat me, I spent most of the time waiting for compiles. “Yep,” a professional programmer told me, “we used to keep a sit-up board in the office and do sit-ups while we were doing compiles. After a few months of programming I had killer abs.”


One day, a spiffy program called Compas Pascal appeared from Denmark, which Philippe Kahn bought and renamed [Borland Turbo Pascal](http://community.borland.com/article/0,1410,20161,00.html). Turbo Pascal was sort of shocking, since it basically did everything that IBM Pascal did, only it ran in about 33K of memory *including the text editor*. This was nothing short of astonishing. Even more astonishing was the fact that you could compile a small program in less than one second. It’s as if a company you had never heard of introduced a clone of the Buick LeSabre which could go 1,000,000 MPH and drive around the world on so little gasoline than an ant could drink it without getting sick.


Suddenly, I became *much* more productive.


That’s when I learned about the concept of the *REP loop*. REP stands for “Read, Eval, Print”, and it describes what a lisp interpreter does for a living: it “reads” your input, evaluates it, and prints the result. An example of the REP loop is shown below: I type something, and the lisp interpreter reads it, evaluates it, and prints the result.


On a slightly larger scale, when you’re writing code, you are in a macro-version of the REP loop called the Edit-Compile-Test loop. You edit your code, compile it, test it, and see how well it works.


A crucial observation here is that you have to run through the loop again and again to write a program, and so it follows that the faster the Edit-Compile-Test loop, the more productive you will be, down to a natural limit of instantaneous compiles. That’s the formal, computer-science-y reason that computer programmers want *really fast hardware* and compiler developers will do anything they can to get super-fast Edit-Compile-Test loops. Visual Basic does it by parsing and lex-ing each line as you type it, so that the final compile can be super-quick. Visual C++ does it by providing incremental compiles, precompiled headers, and incremental linking.


But as soon as you start working on a larger team with multiple developers and testers, you encounter the same loop again, writ larger (it’s fractal, dude!). A tester finds a bug in the code, and reports the bug. The programmer fixes the bug. How long does it take before the tester gets the fixed version of the code? In some development organizations, this Report-Fix-Retest loop can take a couple of weeks, which means the whole organization is running unproductively. To keep the whole development process running smoothly, you need to focus on getting the Report-Fix-Retest loop tightened.


One good way to do this is with *daily builds*. A daily build is an *automatic, daily, complete* build of the entire source tree.


**Automatic* – ***because you set up the code to be compiled at a fixed time every day, using cron jobs (on UNIX) or the scheduler service (on Windows).


**Daily – **or even more often. It’s tempting to do continuous builds, but you probably can’t, because of source control issues which I’ll talk about in a minute.


**Complete –** chances are, your code has multiple versions. Multiple language versions, multiple operating systems, or a high-end/low-end version. The daily build needs to build *all* of them. And it needs to build every file from scratch, not relying on the compiler’s possibly imperfect incremental rebuild capabilities.


Here are some of the many benefits of daily builds:

1. When a bug is fixed, testers get the new version quickly and can retest to see if the bug was really fixed.
Developers can feel more secure that a change they made isn’t going to break any of the 1024 versions of the system that get produced, without actually *having* an OS/2 box on their desk to test on.
Developers who check in their changes right before the scheduled daily build know that they aren’t going to hose everybody else by checking in something which “breaks the build” — that is, something that causes *nobody* to be able to compile. This is the equivalent of the Blue Screen of Death for an entire programming team, and happens a lot when a programmer forgets to add a new file they created to the repository. The build runs fine on *their* machines, but when anyone else checks out, they get linker errors and are stopped cold from doing any work.
Outside groups like marketing, beta customer sites, and so forth who need to use the immature product can pick a build that is known to be fairly stable and keep using it for a while.
By maintaining an archive of all daily builds, when you discover a really strange, new bug and you have no idea what’s causing it, you can use binary search on the historical archive to pinpoint when the bug first appeared in the code. Combined with good source control, you can probably track down which check-in caused the problem.
When a tester reports a problem that the programmer thinks is fixed, the tester can say which build they saw the problem in. Then the programmer looks at when he checked in the fix and figure out whether it’s *really* fixed.


Here’s how to do them. You need a daily build server, which will probably be the fastest computer you can get your hands on. Write a script which checks out a complete copy of the current source code from the repository (you *are* using source control, aren’t you?) and then builds, from scratch, every version of the code that you ship. If you have an installer or setup program, build that too. Everything you ship to customers should be produced by the daily build process. Put each build in its own directory, coded by date. Run your script at a fixed time every day.

- It’s crucial that *everything* it takes to make a final build is done by the daily build script, from checking out the code up to and including putting the bits up on a web server in the right place for the public to download (although during the development process, this will be a test server, of course). That’s the only way to insure that there is *nothing* about the build process that is only “documented” in one person’s head. You never get into a situation where you can’t release a product because only Shaniqua knows how to create the installer, and she was hit by a bus. On the Juno team, the only thing you needed to know to create a full build from scratch was where the build server was, and how to double-click on its “Daily Build” icon.
There is nothing worse for your sanity then when you are trying to ship the code, and there’s *one tiny bug*, so you fix that one tiny bug right on the daily build server and ship it. As a golden rule, you should only ship code that has been produced by a full, clean daily build that started from a complete checkout.
Set your compilers to maximum warning level (-W4 in Microsoft’s world; -Wall in gcc land) and set them to stop if they encounter even the smallest warning.
If a daily build is broken, you run the risk of stopping the whole team. Stop everything and keep rebuilding until it’s fixed. Some days, you may have multiple daily builds.
Your daily build script should report failures, via email, to the whole development team. It’s not too hard to grep the logs for “error” or “warning” and include that in the email, too. The script can also append status reports to an HTML page visible to everyone so programmers and testers can quickly determine which builds were successful.
One rule we followed on the Microsoft Excel team, to great effect, was that whoever broke the build became responsible for babysitting builds until somebody else broke it. In addition to serving as a clever incentive to keep the build working, it rotated almost everybody through the job of buildmaster so everybody learned about how builds are produced.
If your team works in one time zone, a good time to do builds is at lunchtime. That way everybody checks in their latest code right before lunch, the build runs while they’re eating, and when they get back, if the build is broken, everybody is around to fix it. As soon as the build is working everybody can check out the latest version without fear that they will be hosed due to a broken build.
If your team is working in two time zones, schedule the daily build so that the people in one time zone don’t hose the people in the other time zone. On the Juno team, the New York people would check things in at 7 PM New York time and go home. If they broke the build, the Hyderabad, India team would get into work (at about 8 PM New York Time) and be completely stuck for a whole day. We started doing two daily builds, about an hour before each team went home, and completely solved that problem.


For Further Reading:

- Some [discussion](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=862) on tools for daily builds
Making daily builds is important enough that it’s one of the [12 steps to better code](https://www.joelonsoftware.com/articles/fog0000000043.html).
There’s a lot of interesting stuff about the builds made (weekly) by the Windows NT team in G. Pascal Zachary’s book [Showstopper](http://www.amazon.com/exec/obidos/ASIN/0029356717/ref=nosim/joelonsoftware).
Steve McConnell writes about daily builds [here](http://www.construx.com/stevemcc/bp04.htm).
