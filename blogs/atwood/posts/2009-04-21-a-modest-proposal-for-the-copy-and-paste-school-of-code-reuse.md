---
title: "A Modest Proposal for the Copy and Paste School of Code Reuse"
date: 2009-04-21
url: https://blog.codinghorror.com/a-modest-proposal-for-the-copy-and-paste-school-of-code-reuse/
slug: a-modest-proposal-for-the-copy-and-paste-school-of-code-reuse
word_count: 1089
---

Is **copying and pasting code** dangerous? Should control-c and control-v be treated not as essential programming keyboard shortcuts, but registered weapons?


![](https://blog.codinghorror.com/content/images/2025/04/image-356.png)


(yes, I know that in OS X, the keyboard shortcut for cut and paste uses “crazy [Prince symbol key](http://en.wikipedia.org/wiki/Love_Symbol)” instead of control, like God intended. Any cognitive dissonance you may be experiencing right now is also intentional.)


Here’s my position on copy and paste for programmers:


> Copy and paste doesn’t create bad code. Bad programmers create bad code.


Or, if you prefer, guns don’t kill people, *people* kill people. Just make sure that source code isn’t pointed at me when it goes off. There are always risks. When you copy and paste code, vigilance is required to make sure you (or someone you work with) isn’t falling into the trap of [copy and paste code duplication](http://www.stevemcconnell.com/ieeesoftware/bp16.htm):


> Undoubtedly the most popular reason for creating a routine is to avoid duplicate code. Similar code in two routines is a warning sign. **David Parnas says that if you use copy and paste while you’re coding, you’re probably committing a design error.** Instead of copying code, move it into its own routine. Future modifications will be easier because you will need to modify the code in only one location. The code will be more reliable because you will have only one place in which to be sure that the code is correct.


Some programmers agree with Parnas, going so far as to advocate [disabling cut and paste entirely](http://www.secretgeek.net/copy_paste_dont_do_it.asp). I think that’s rather extreme. I use copy and paste while programming all the time, but **never in a way that runs counter to **[**Curly’s Law**](https://blog.codinghorror.com/curlys-law-do-one-thing/).


But pervasive high-speed internet – and a whole new generation of hyper-connected young programmers weaned on the web – has changed the dynamics of programming. Copy and paste is no longer a pejorative term, but a simple observation about how a lot of modern coding gets done, like it or not. This new dynamic was codified into law as [Bambrick's 8th Rule of Code Reuse](http://www.secretgeek.net/open_code_sharing.asp):


> It’s far easier and much less trouble to find and use a bug-ridden, poorly implemented snippet of code written by a 13 year old blogger on the other side of the world than it is to find and use the equivalent piece of code written by your team leader on the other side of a cubicle partition.
> (And I think that the copy and paste [school of code reuse](http://secretgeek.net/howtobeaprogrammer.asp) is flourishing, and will always flourish, even though it gives very suboptimal results.)


Per Mr. Bambrick, copy and pasted code from the internet is **good** because:

- Code stored on blogs, forums, and the web in general is very easy to find.
- You can inspect the code before you use it.
- Comments on blogs give some small level of feedback that might improve quality.
- Pagerank means that you’re more likely to find code that might be higher quality.
- Code that is easy to read and understand will be copied and pasted more, leading to a sort of viral reproductive dominance.
- The programmer’s ego may drive her to only publish code that she believes is of sufficient quality.


But copy and pasted code from the internet is **bad** because:

- If the author improves the code, you’re not likely to get those benefits.
- If you improve the code, you’re not likely to pass those improvements back to the author.
- Code may be blindly copied and pasted without understanding what the code actually does.
- Pagerank doesn’t address the quality of the code, or its fitness for your purpose.
- Code is often ‘demo code’ and may purposely gloss over important concerns like error handling, sql injection, encoding, security, etc.


Now, if you’re copying entire projects or groups of files, you should be inheriting that code from a project that’s already under proper source control. That’s just basic software engineering (we hope). But the type of code I’m likely to cut and paste *isn’t* entire projects or files. It’s probably a **code snippet** – an algorithm, a routine, a page of code, or perhaps a handful of functions. There are several established code snippet sharing services:

- [DZone Snippets](https://web.archive.org/web/20090805112932/http://snippets.dzone.com/)
- [Snipplr](http://snipplr.com/)
- [Refactor My Code](http://refactormycode.com/)
- [CodeProject](http://www.codeproject.com/)


Source control is great, but it’s massive overkill for, say, this little [Objective-C animation snippet](http://snipplr.com/view/12252/animate-a-fadeout-of-a-nswindow-with-objectivec/):

kg-card-begin: html

```

- (void)fadeOutWindow:(NSWindow*)window{
float alpha = 1.0;
[window setAlphaValue:alpha];
[window makeKeyAndOrderFront:self];
for (int x = 0; x < 10; x++) {
alpha -= 0.1;
[window setAlphaValue:alpha];
[NSThread sleepForTimeInterval:0.020];
}
}

```

kg-card-end: html

To me, the most troubling limitation of [copypasta programming](http://everything2.com/title/copypasta) is the complete disconnect between the code you’ve pasted and all the other viral copies of it on the web. It’s impossible to locate new versions of the snippet, or fold your features and bugfixes back into the original snippet. Nor can you possibly hope to find all the other nooks and crannies of code all over the world this snippet has crept into.


What I propose is this:

kg-card-begin: html

```

// codesnippet:1c125546-b87c-49ff-8130-a24a3deda659
- (void)fadeOutWindow:(NSWindow*)window{
// code
}
}

```

kg-card-end: html

Attach **a one line comment convention** with a new GUID to any code snippet you publish on the web. This ties the snippet of code to its author and any subsequent clones. A trivial search for the code snippet GUID would identify every other copy of the snippet on the web:

kg-card-begin: html

```

http://www.google.com/search?q=1c125546-b87c-49ff-8130-a24a3deda659

```

kg-card-end: html

I realize that what I’m proposing, as simple as it is, might still be an onerous requirement for copy-paste programmers. They’re too busy copying and pasting to bother with silly conventions! Instead, imagine the centralized code snippet sharing services **automatically applying a snippet GUID comment to every snippet they share**. If they did, this convention could get real traction virtually overnight. And why not? We’re just following the fine software engineering tradition of [doing the stupidest thing that could possibly work](http://www.globalnerdy.com/2007/06/01/do-the-stupidest-thing-that-could-possibly-work/).


No, it isn’t a perfect system, by any means. For one thing, variants and improvements of the code would probably need their own snippet GUID, ideally by adding a second line to indicate the parent snippet they were derived from. And what do you do when you combine snippets with your own code, or merge snippets together? But let’s not over think it, either. This is a simple, easily implementable improvement over what we have now: utter copy-and-paste code chaos.


Sometimes, **small code requires small solutions**.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[code reuse](https://blog.codinghorror.com/tag/code-reuse/)
[programming best practices](https://blog.codinghorror.com/tag/programming-best-practices/)
[developer productivity](https://blog.codinghorror.com/tag/developer-productivity/)
