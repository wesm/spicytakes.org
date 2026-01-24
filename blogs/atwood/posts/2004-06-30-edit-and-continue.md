---
title: "Edit and Continue"
date: 2004-06-30
url: https://blog.codinghorror.com/edit-and-continue/
slug: edit-and-continue
word_count: 957
---

I’m looking forward to [VS.NET 2005](https://web.archive.org/web/20040705042155/http://lab.msdn.microsoft.com/express/) like everyone else, but the one killer feature that will absolutely compel me to upgrade on day of release is **Edit and Continue**. I had no idea exactly how much time I spent editing live code in VB6’s debugger until I lost this capability in VS.NET. It is my one serious regret about .NET – which in every other respect is a massive improvement over VB6. However, I am sympathetic to the timeline crunch that [forced Microsoft to drop the feature](https://web.archive.org/web/20051124083743/http://www.ftponline.com/vsm/2004_01/online/dias/page2.aspx):


> **PM:** Given that features like edit-and-continue didn’t make it in, do you feel that any of the emphasis on your initial version of VB.NET was misplaced?
> **CD:** No. It’s easy to second-guess things in hindsight or even as you’re going along: “Are we doing the right thing? Should we do this? Should we do that?”
> But when I review the decisions we’ve made to move the tool to .NET, I still think it was the right move to cut edit-and-continue from the first release, given that the primary goal was to ensure we got on the platform. Because going forward, the developers who use this tool will reap tremendous benefits from being on the .NET Framework. All the stuff that comes from being on Longhorn, all the managed code, we’re there, and we don’t have to wait for anything.
> Today, we have full access to the platform, and the bleeding edge, hard-core developers can now write XAML, Avalon, and Longhorn apps with VB Whidbey’s managed code. Now, we can go back and figure out what we can do to make this tool easier and more productive to use for everybody, which is a nice place for us to be.


I agree, and VS.NET 2005 is right around the corner. What I don’t understand, though, is developers who think [Edit and Continue is a Bad Thing.](http://weblogs.asp.net/fbouma/archive/2003/08/01/22211.aspx) That is one of the most wrongheaded things I’ve ever read, and I have to assume it’s spoken from ignorance, e.g., developers who have never had this capability in their toolset and therefore don’t know what they are missing.


All Edit and Continue does is tighten the loop between the time a bug is detected, and the time you can fix it. **How can this possibly be a bad thing?** On the contrary, it is a huge boost to productivity. At the time of the exception, you can diagnose the problem – in perfect context of all the live code, which is the easiest way to determine what the fix should be – and make your fix. Then just keep on truckin’.


Compare with the alternative:

1. Hit an exception
2. Slap yourself on the forehead for being a moron
3. Diagnose the problem at exception time and determine a fix
4. Wait for the IDE to shut down
5. Navigate to the right place in the source code
6. Try to remember what the heck the fix you came up with actually was
7. Enter the fix
8. Compile the code
9. Run the app and exercise the fix


I burn far too much time in VS.NET 2003 doing this. Edit and Continue would cut the work I have to do to fix a bug **in half**. **IN HALF! **But then, the close relationship between immediacy of debugging and productivity isn’t a new concept. Fred Brooks talks about it in his 1975 golden oldie, The Mythical Man-Month:

kg-card-begin: html

> One of the justifications for MIT’s Multics project was its usefulness for building programming Systems. Multics (and following it, IBM’s TSS) differs in concept from other interactive computing systems in exactly those respects necessary for systems programming: many levels of sharing and protection for data and programs, extensive library management, and facilities for cooperative work among terminal users. I am convinced that interactive systems will never displace batch systems for many applications But I think the Multics team has made its most convincing case in the system programming application.
> There is not yet much evidence available on the true fruitfulness of such apparently powerful tools. **There is a widespread recognition that debugging is the hard and slow part of system programming, and slow turnaround is the bane of debugging. So the logic of interactive programming seems inexorable.**
> ProgramSizeBatch or ConversationalInstructions / man-yearEss Code800,000Batch500-10007094 ESS Support120,000Batch2100-3400360 ESS Support32,000Conversational8000360 ESS Support8,300Batch4000 
>  **Fig 12.2** Comparative productivity under batch and conversational programming
> Further, we hear good testimonies from many who have built little systems or parts of systems in this way. The only numbers I have seen for effects on programming of large systems were reported by John Harr of Bell Labs. They are shown in Fig. 12.2. These numbers are for writing, assembling, and debugging programs. The first program is mostly control program; the other three are language translators, editors, and such. **Harr’s data suggest that an interactive facility at least doubles productivity in system programming.**
> The effective use of most interactive tools requires that the work be done in a high level language, for teletype and typewriter terminals cannot be used to debug by dumping memory. With a high level language, source can be easily edited and selective printouts easily done. Together they make a pair of sharp tools indeed.

kg-card-end: html

OK, so maybe Fred’s “I am convinced that interactive systems will never displace batch systems for many applications” statement isn’t looking so hot in retrospect. I left that in for context. But he’s right on target about the strong relationship between immediacy and productivity. Edit and Continue is a killer feature if I’ve ever seen one, and I can’t wait to get my hands... back... on it.

[debugging](https://blog.codinghorror.com/tag/debugging/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
