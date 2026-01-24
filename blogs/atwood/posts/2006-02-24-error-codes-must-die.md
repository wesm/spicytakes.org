---
title: "Error Codes Must Die"
date: 2006-02-24
url: https://blog.codinghorror.com/error-codes-must-die/
slug: error-codes-must-die
word_count: 517
---

A [recent Scott Hanselman post](http://www.hanselman.com/blog/WindowsDefenderErrors0x8024402c0x80240022And1609.aspx) described a problem he had with Windows Defender:


> Defender was unable to update my signatures, instead throwing a COM-ish 0x8024402c. Others are getting Error 1609 and still others 0x80240022.


![](https://blog.codinghorror.com/content/images/2025/05/image-217.png)


This isn’t an isolated incident. The latest release candidate of [Team Foundation Server](https://web.archive.org/web/20060411035133/http://msdn.microsoft.com/vstudio/teamsystem/team/default.aspx) also returns error codes during install:


> Most of my installations of TFS have been pretty straight forward. However, certain instances where my installation failed, I would get weird, cryptic error messages. For example, one common error I keep getting when trying to install TFS on a certain server configuration is:
> The installer has encountered an unexpected error installing this package. This may indicate a problem with this package. The error code is 26105.
> Can anyone decrypt this error message? I’ve seen this error so many times that the number 26105 is now tattooed into my brain! Looking at the log files helped me pinpoint the error, but I still couldn’t figure out the problem.


I thought error codes went out with 8-bit computers over a decade ago. **Is it unreasonable to expect human-readable error messages instead of undecipherable error codes in the year 2006?**


Allow me to channel Alan Cooper’s classic [About Face](http://www.amazon.com/exec/obidos/ASIN/0764526413) for a second, because here’s how users see that error code dialog:


![](https://blog.codinghorror.com/content/images/2025/05/image-218.png)


It really isn’t that hard to build a decent error dialog. Just **try to communicate like a human being instead of a computer**. Alan Cooper provides these three guidelines:


> **Be Polite**
> Never forget that an error message box is the program reporting on its failure to do its job, and it is interrupting the user to do this. The error message box must be unfailingly polite. It must never even hint that the user caused this problem, because that is simply not true from the user’s perspective. The customer is always right.
> **Be Illuminating**
> The error message must illuminate the problem for the user. This means it must give him the kind of information he needs to make an appropriate determination to solve the program’s problem. It needs to make clear the scope of the problem, what the alternatives are, what the program will do as a default, and what information was lost, if any. The problem should treat this as a confession.
> **Be Helpful**
> It is wrong for the program to just dump the problem on the user’s lap and wipe its hands of the matter. It should directly offer to implement at least one suggested solution right there on the error message box. It should offer buttons that will take care of the problem in various ways. If a printer is missing, the message box should offer options for deferring the printout or selecting another printer.


Error code dialogs go 0 for 3: they’re rude, unhelpful, and about as illuminating as a mineshaft. This is one scenario where it’s easy for us to write better software than Microsoft.


A dialog presenting an error code is utter and complete failure. **Don’t *ever* use error codes**.

[error codes](https://blog.codinghorror.com/tag/error-codes/)
[troubleshooting](https://blog.codinghorror.com/tag/troubleshooting/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
