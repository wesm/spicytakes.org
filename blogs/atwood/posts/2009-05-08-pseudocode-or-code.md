---
title: "Pseudocode or Code?"
date: 2009-05-08
url: https://blog.codinghorror.com/pseudocode-or-code/
slug: pseudocode-or-code
word_count: 918
---

Although I’m a huge fan of [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670) – it is my [single most recommended programming book](https://blog.codinghorror.com/recommended-reading-for-developers/) for good reason – there are chapters in it that I haven’t been able to digest, even after 16 years.


One of those chapters describes something called the **Pseudocode Programming Process**. And on paper, at least, it sounds quite sensible. Before writing a routine, you describe what that routine should do in plain English. So if we we set out to write an error handling lookup routine, we’d first write it in **pseudocode**:

kg-card-begin: html

```

set the default status to “fail”
look up the message based on the error code
if the error code is valid
if doing interactive processing, display the error message
interactively and declare success
if doing command line processing, log the error message to the
command line and declare success
if the error code isn’t valid, notify the user that an
internal error has been detected
return status information

```

kg-card-end: html

Then, when you’re satisfied that you understand what the routine should do, you turn that pseudocode into comments that describe the code you’re about to write.

kg-card-begin: html

```

// set the default status to “fail”
Status errorMessageStatus = Status_Failure;
// look up the message based on the error code
Message errorMessage = LookupErrorMessage( errorToReport );
// if the error code is valid
if ( errorMessage.ValidCode() ) {
// determine the processing method
ProcessingMethod errorProcessingMethod = CurrentProcessingMethod();
// if doing interactive processing, display the error message
// interactively and declare success
if ( errorProcessingMethod == ProcessingMethod_Interactive ) {
DisplayInteractiveMessage( errorMessage.Text() );
errorMessageStatus = Status_Success;
}

```

kg-card-end: html

Pseudocode is sort of like the [Tang](http://en.wikipedia.org/wiki/Tang_(drink)%22) of programming languages – you hydrate the code around it.


![](https://blog.codinghorror.com/content/images/2025/04/image-363.png)


But why pseudocode? Steve offers some rationales:

- **Pseudocode makes reviews easier**. You can review detailed designs without examining source code. Pseudocode makes low-level design reviews easier and reduces the need to review the code itself.
- **Pseudocode supports the idea of iterative refinement**. You start with a high-level design, refine the design to pseudocode, and then refine the pseudocode to source code. This successive refinement in small steps allows you to check your design as you drive it to lower levels of detail. The result is that you catch high level errors at the highest level, mid-level errors at the middle level, and low-level errors at the lowest level – before any of them becomes a problem or contaminates work at more detailed levels.
- **Pseudocode makes changes easier**. A few lines of pseudocode are easier to change than a page of code. Would you rather change a line on a blueprint or rip out a wall and nail in the two-by-fours somewhere else? The effects aren’t as physically dramatic in software, but the principle of changing the product when it’s most malleable is the same. One of the keys to the success of a project is to catch errors at the “least-value stage,” the stage at which the least effort has been invested. Much less has been invested at the pseudocode stage than after full coding, testing, and debugging, so it makes economic sense to catch the errors early.
- **Pseudocode minimizes commenting effort**. In the typical coding scenario, you write the code and add comments afterward. In the PPP, the pseudocode statements become the comments, so it actually takes more work to remove the comments than to leave them in.
- **Pseudocode is easier to maintain than other forms of design documentation**. With other approaches, design is separated from the code, and when one changes, the two fall out of agreement. With the PPP, the pseudocode statements become comments in the code. As long as the inline comments are maintained, the pseudocode’s documentation of the design will be accurate.


All compelling arguments. As an acolyte of McConnell, it pains me to admit this, but every time I’ve tried the Pseudocode Programming Process, I almost immediately abandon it as impractical.


Why? Two reasons:

1. **code > pseudocode**. I find it easier to think about code *in code*. While I’m all for describing the overall general purpose of the routine before you write it in plain English – this helps name it, which is [incredibly difficult](https://blog.codinghorror.com/i-shall-call-it-somethingmanager/) – extending that inside the routine doesn’t work well for me. There’s something fundamentally... unrealistic... about attempting to using precise English to describe the nuts and bolts of code.
2. **Starting with the goal of adding comments to your code seems backwards**. I prefer [coding without comments](https://blog.codinghorror.com/coding-without-comments/), in that I want the code to be as self-explanatory as humanly possible. Don’t get me wrong; comments do occur regularly in my code, but only because the code could not be made any clearer without them. Comments should be a method of last resort, not something you start with.


Of course, PPP is just one proposed way to code, not the perfect or ideal way. McConnell has no illusions about this, and acknowledges that refactoring, TDD, design by contract, and even plain old “hacking” are valid and alternative ways to construct code.


But still – I have a hard time seeing pseudocode as useful in anything other than possibly job interviews. And even then, I’d prefer to sit down in front of a computer and write real code to solve whatever problem is being posed. What’s your take? Is pseudocode a useful tool in your programming? **Do you write pseudocode before writing code?**

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[coding practices](https://blog.codinghorror.com/tag/coding-practices/)
[pseudocode](https://blog.codinghorror.com/tag/pseudocode/)
[code patterns](https://blog.codinghorror.com/tag/code-patterns/)
