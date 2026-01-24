---
title: "Pressing the Software Turbo Button"
date: 2008-12-23
url: https://blog.codinghorror.com/pressing-the-software-turbo-button/
slug: pressing-the-software-turbo-button
word_count: 1005
---

Does anyone remember [the Turbo Button](https://web.archive.org/web/20081226074343/http://www.pcguide.com/ref/case/switchTurbo-c.html) from older IBM PC models?

kg-card-begin: html

> A leftover from machines of five to ten years ago, the turbo switch still remains on many cases, even though it serves no purpose.
> In the early days of the PC, there was only IBM, and there were only a handful of different speeds a PC could run at. Early software was written by programmers who believed they were writing it to run on a machine of a specific speed. When newer, faster machines would come out, some of this software (especially games) would stop working properly because it would run too fast. Turning off the “turbo” function of the PC (which meant anything that made it run faster than an IBM of a particular era) would make the machine run slower so this software would work. In essence, it was a “compatibility mode” feature, to slow down the machine for older software.
> Now there are dozens of different combinations of processor types and speeds. Software cannot rely on knowing the speed of the machine, so most programs use speed-detection algorithms. The turbo button no longer serves any useful purpose. On many motherboards there either isn’t anywhere to connect it, or there is a place but the motherboard does nothing when you press the button. The best use for this button is to never touch it, or use it for some other purpose. Some older machines will still slow down when the button is pressed, and if you press it by accident your machine will lose performance. It can be surprisingly hard to track down the problem; the front of the machine is the last place anyone appears to notice anything.

kg-card-end: html

I, too, remember the Turbo Button, although by the time I got heavily into PCs in the early 1990s it was already well in decline. **The strange thing about a turbo button is that you’d pretty much *always want it on***; there’s almost no situation where you’d want to keep some power in reserve for that extra “oomph” required by, say, a particularly intensive Lotus 1-2-3 spreadsheet. You wanted your PC to run at full tilt, maximum possible speed, all the time.


I think this hardware philosophy is also true of software, and it applies at both ends of software development:

- Developers need [fast machines to be productive](https://blog.codinghorror.com/the-programmers-bill-of-rights/).
- Agile software development practices work best when you [iterate rapidly](https://blog.codinghorror.com/boyds-law-of-iteration/).
- Users [prefer software that’s responsive](https://blog.codinghorror.com/speed-still-matters/).


Whether you’re a coder or a user, performance is a *hugely* important feature, [as the codist notes](https://web.archive.org/web/20081226182431/http://thecodist.com/article/turbo_productivity_in_programming_is_the_only_thing):


> In my first job at a defense contractor, I met a couple guys (I thought they were old but they were probably my age now!) who had been writing code since the late 50s and then writing batch applications on an IBM mainframe. Since they could only compile/run once per day (and get the printouts the next day) they would work on 6-8 projects at the same time and weren’t concerned when these projects might take years to complete. After two weeks on this I was ready to go insane and got switched to working on a supermini which at least had a realtime operating system. I could write code, compile it and run it at the same time. The only drawback was we had 7 people sharing one terminal at the start. Suggestions that each programmer get a terminal were laughed at initially. Being productive in such a limited time was really hard.
> After a couple years I switched to working on PCs (which were just out) and having my own “computer” was wonderful. Working in Pascal and assembly still wasn’t fast yet but at least I had my own space.
> Then I got Turbo Pascal and life was forever changed. I could write, compile and debug applications virtually instantly and my need for speed has never looked back. Even on the compared-to-today crappy hardware I never really found another environment as fast until I started using PHP this year (which of course has no compilation).
> Later when I started Mac coding in C we started off with a dreadful C compiler/linker that took 20 minutes to do its thing. When Think-C came out it was almost a Turbo moment again. Eventually it began to get slower and slower and we switch to Metrowerks Codewarrior which was fast but the applications were getting so big that it still took 30-60 seconds to build sometimes.
> When I moved to Java in 1998 compiling and linking still took a fairly long time until the IDEs (and the JVM) began to catch up to the hardware. **Still nothing was ever as instant as Turbo had been, despite the hardware being 100x faster.**


I’m a speed freak too. As far as I’m concerned, everything on a PC should happen instantaneously. Or at least as close to instantaneous as the laws of physics will allow. Simply doing everything *faster*, all other things being equal, will allow you to get more done. I’m not alone in this; Fred Brooks made a similar observation way back in [The Mythical Man-Month](https://blog.codinghorror.com/edit-and-continue/):


> There is not yet much evidence available on the true fruitfulness of such apparently powerful tools. There is a widespread recognition that debugging is the hard and slow part of system programming, and slow turnaround is the bane of debugging. So the logic of interactive programming seems inexorable.
> Further, we hear good testimonies from many who have built little systems or parts of systems in this way. The only numbers I have seen for effects on programming of large systems were reported by John Harr of Bell Labs. [. . .] **Harr’s data suggest that an interactive facility at least doubles productivity in system programming.**


Never underestimate the power of **pressing the software turbo button**. What’s keeping you from going as fast as you can? As a user? As a software developer?

[legacy hardware](https://blog.codinghorror.com/tag/legacy-hardware/)
[software compatibility](https://blog.codinghorror.com/tag/software-compatibility/)
[performance tuning](https://blog.codinghorror.com/tag/performance-tuning/)
[technology history](https://blog.codinghorror.com/tag/technology-history/)
[software development](https://blog.codinghorror.com/tag/software-development/)
