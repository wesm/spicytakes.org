---
title: "Snippet Enumeration Macro"
date: 2006-03-01
url: https://blog.codinghorror.com/snippet-enumeration-macro/
slug: snippet-enumeration-macro
word_count: 259
---

Inspired by my recent post on [C# code snippets](https://blog.codinghorror.com/c-snippet-parity/), I found [a little console app](https://web.archive.org/web/20060518174933/http://www.dotnet2themax.com/blogs/fbalena/PermaLink,guid,4ca4874e-1e9d-4c75-a291-dea053cbf850.aspx) by Francesco Balena* that enumerates all the [snippets](https://blog.codinghorror.com/code-snippets-in-vsnet-2005/) on your system along with their shortcut text.


I improved his console app and turned it into a convenient IDE macro along the lines of my [keyboard shortcut enumerating IDE macro](https://blog.codinghorror.com/keyboard-shortcut-summary-macro/):


![](https://blog.codinghorror.com/content/images/2025/05/image-223.png)


[Download the Snippet List Macro](https://web.archive.org/web/20060321051456/http://www.codinghorror.com/blog/files/snippets-list-macro-2.zip) (3kb ZIP)


I found out the hard way that the snippet manager writes all of its changes to the registry. So I use the registry to enumerate all possible snippet paths (this picks up all the per-system snippets and per-user snippets) and also to locate the snippet XML index file that cross-references all the physical paths.


The macro defaults to enumerating the C# snippets, but you can change the _Lang variable to enumerate any available snippet library: VB, C#, J#,** and Xml.


This macro only works in **Visual Studio 2005**, obviously. Here’s how to run it:

1. go to Tools - Macros - IDE
2. create a new Module named “Snippets” under “MyMacros”
3. paste the macro code into the module
4. close the macro IDE window
5. go to Tools – Macros – Macro Explorer
6. A new macro named “List” will be under “Snippets.” Double-click it to run.
7. The macro will take a minute or so to write a HTML file to your My Documents file, and open that HTML file in the IDE.


*One of my earliest coding heroes!


**Does anyone actually *use* J#? C'mon. Seriously.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[ide](https://blog.codinghorror.com/tag/ide/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[macro](https://blog.codinghorror.com/tag/macro/)
