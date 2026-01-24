---
title: "When Good Comments Go Bad"
date: 2004-11-13
url: https://blog.codinghorror.com/when-good-comments-go-bad/
slug: when-good-comments-go-bad
word_count: 516
---

Now that [XML comments](https://web.archive.org/web/20041205022710/http://dotnet.mvps.org/dotnet/faqs/?id=tooltipsxmldocumentation) are confirmed for VB.NET in VS.NET 2005, I’ve started to aggressively adopt the [VBCommenter add-in](https://web.archive.org/web/20050304100843/http://www.gotdotnet.com/team/ide/), which adds XML comment support to the current version of VS.NET.


XML comments are great primarily because of the additional IDE tooltip feedback they provide to developers for methods and variables – well, as long as you’re using C#. If you’re using VB.NET you have to reference a binary version of the project to get that to work, at least until VS.Next.


However, as a general purpose documentation tool, XML comments are... kind of verbose, hard to maintain, and annoying. The potential for abuse is high. This [15 seconds article](https://web.archive.org/web/20050108093849/http://www.15seconds.com/issue/040303.htm) is a prime example; just take a look at the author’s recommended XML documentation template:

kg-card-begin: html

```
''' ***********************************************************
''' Copyright [year]  [client name]. All rights reserved.
''' ***********************************************************
''' Class.Method:     IConfigProvider.GetSetting
''' <summary>
'''  [summary goes here]
''' </summary>
''' <param name="name">
'''       [description goes here].
'''       Value Type: <see cref="String" />   (System.String)
''' </param>
''' <param name="defaultValue">
'''       [description goes here].
'''       Value Type: <see cref="String" />   (System.String)
''' </param>
''' <exception cref="System.ApplicationException">
'''       Thrown when...
''' </exception>
''' <returns><see cref="String" />(System.String)</returns>
''' <remarks><para><pre>
''' RevisionHistory:
''' -----------------------------------------------------------
''' Date        Name              Description
''' -----------------------------------------------------------
''' mm/dd/yyyy  [logged in user]  Initial Creation
''' </pre></para>
''' </remarks>
''' -----------------------------------------------------------
```

kg-card-end: html

What next? Blood type? Mother’s maiden name? Favorite color? It’s ridiculous and detrimental to the code. **Comments are supposed to make your code easier to understand and maintain – not harder**.


When commenting, there are a few essential rules I believe in:

1. **The value of a comment is directly proportional to the distance between the comment and the code.** Good comments stay as close as possible to the code they’re referencing. As distance increases, the odds of developers making an edit without seeing the comment that goes with the code increases. The comment becomes misleading, out of date, or worse, incorrect. Distant comments are unreliable at best.
2. **Comments with complex formatting cannot be trusted.** Complex formatting is a pain to edit and a disincentive to maintenance. If it is difficult to edit a comment, it’s very likely a developer has avoided or postponed synchronizing his work with the comments. I view complex comments with extreme skepticism.
3. **Don’t include redundant information in the comments.** Why have a Revision History section – isn’t that what we use source control for? Besides the fact that this is totally redundant, the odds of a developer remembering, after *every single edit*, to update that comment section at the top of the procedure are... very low.
4. **The best kind of comments are the ones you don’t need.** The only “comments” guaranteed to be accurate 100% of the time – and even that is debatable – is the body of the code itself. Endeavor to write self-documenting code whenever possible. An occasional comment to illuminate or clarify is fine, but if you frequently write code full of “tricky parts” and reams of comments, maybe it’s time to refactor.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[code documentation](https://blog.codinghorror.com/tag/code-documentation/)
[ide features](https://blog.codinghorror.com/tag/ide-features/)
