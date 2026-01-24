---
title: "Coding Without Comments"
date: 2008-07-24
url: https://blog.codinghorror.com/coding-without-comments/
slug: coding-without-comments
word_count: 922
---

If peppering your code with lots of comments is good, then having **zillions of comments** in your code must be *great*, right? Not quite. Excess is one way [good comments go bad](https://blog.codinghorror.com/when-good-comments-go-bad/):

kg-card-begin: html

```

'*************************************************
' Name: CopyString
'
' Purpose: This routine copies a string from the source
' string (source) to the target string (target).
'
' Algorithm: It gets the length of “source” and then copies each
' character, one at a time, into “target”. It uses
' the loop index as an array index into both “source”
' and “target” and increments the loop/array index
' after each character is copied.
'
' Inputs: input The string to be copied
'
' Outputs: output The string to receive the copy of “input”
'
' Interface Assumptions: None
'
' Modification History: None
'
' Author: Dwight K. Coder
' Date Created: 10/1/04
' Phone: (555) 222-2255
' SSN: 111-22-3333
' Eye Color: Green
' Maiden Name: None
' Blood Type: AB-
' Mother’s Maiden Name: None
' Favorite Car: Pontiac Aztek
' Personalized License Plate: “Tek-ie”
'*************************************************

```

kg-card-end: html

I’m constantly running across comments from developers who don’t seem to understand that the code already tells us *how* it works; we need the comments to [tell us *why* it works.](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) Code comments are so widely misunderstood and abused that you might find yourself wondering if they’re worth using at all. Be careful what you wish for. Here’s some code with **no comments whatsoever**:

kg-card-begin: html

```

r = n / 2;
while ( abs( r - (n/r) ) > t ) {
  r = 0.5 * ( r + (n/r) );
}
System.out.println( “r = ” + r );

```

kg-card-end: html

Any idea what that bit of code does? It’s perfectly readable, but *what the heck does it do?*


Let’s add a comment.

kg-card-begin: html

```

// square root of n with Newton-Raphson approximation
r = n / 2;
while ( abs( r - (n/r) ) > t ) {
  r = 0.5 * ( r + (n/r) );
}
System.out.println( “r = ” + r );

```

kg-card-end: html

That must be what I was getting at, right? Some sort of pleasant, middle-of-the-road compromise between the two polar extremes of no comments whatsoever and carefully formatted epic poems every second line of code?


Not exactly. Rather than add a comment, I’d refactor to this:

kg-card-begin: html

```

private double SquareRootApproximation(n) {
  r = n / 2;
  while ( abs( r - (n/r) ) > t ) {
    r = 0.5 * ( r + (n/r) );
  }
return r;
}
System.out.println( “r = ” + SquareRootApproximation(r) );

```

kg-card-end: html

I haven’t added a single comment, and yet this mysterious bit of code is now perfectly understandable.


While comments are neither inherently good or bad, they are frequently used as a crutch. **You should always write your code as if comments didn’t exist. **This *forces* you to write your code in the simplest, plainest, most self-documenting way you can humanly come up with.


When you’ve rewritten, refactored, and rearchitected your code a dozen times to make it easy for your fellow developers to read and understand – when you can’t possibly imagine any conceivable way your code could be changed to become more straightforward and obvious – then, and *only then*, should you feel compelled to add a comment explaining what your code does.


As [Steve points out](http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html), this is one key difference between junior and senior developers:


> In the old days, seeing too much code at once quite frankly exceeded my complexity threshold, and when I had to work with it I’d typically try to rewrite it or at least comment it heavily. Today, however, I just slog through it without complaining (much). When I have a specific goal in mind and a complicated piece of code to write, I spend my time making it happen rather than telling myself stories about it [in comments].


Junior developers rely on comments to tell the story when they should be relying on the *code* to tell the story. Comments are narrative asides; important in their own way, but in no way meant to replace plot, characterization, and setting.


Perhaps that’s the dirty little secret of code comments: **to write good comments you have to be a good writer**. Comments aren’t code meant for the compiler, they’re words meant to communicate ideas to other human beings. While I do (mostly) love my fellow programmers, I can’t say that effective communication with other human beings is exactly our strong suit. I’ve seen three-paragraph emails from developers on my teams that practically melted my brain. *These* are the people we’re trusting to write clear, understandable comments in our code? I think maybe some of us might be better off sticking to our strengths – that is, writing for the compiler, in as clear a way as we possibly can, and reaching for the comments only as a method of last resort.


Writing good, meaningful comments is hard. It’s as much an art as writing the code itself; maybe even more so. As Sammy Larbi said in [Common Excuses Used To Comment Code](http://www.codeodor.com/index.cfm/2008/6/18/Common-Excuses-Used-To-Comment-Code-and-What-To-Do-About-Them/2293), if your feel your code is too complex to understand *without *comments, **your code is probably just bad.** Rewrite it until it doesn’t need comments any more. If, at the end of that effort, you still feel comments are necessary, then by all means, add comments… carefully.

[tags: software development concepts](https://blog.codinghorror.com/tag/tags-software-development-concepts/)
[code comments](https://blog.codinghorror.com/tag/code-comments/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
