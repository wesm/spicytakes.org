---
title: "On Unnecessary Namespacing"
date: 2006-09-15
url: https://blog.codinghorror.com/on-unnecessary-namespacing/
slug: on-unnecessary-namespacing
word_count: 212
---

Is it really necessary to qualify everything in Windows Vista with the “Windows” namespace?


![](https://blog.codinghorror.com/content/images/2025/05/image-362.png)


Hey, guess what operating system this is!


At least the Vista start menu lets me do a containing search, so if I start typing ‘fax,’ the menu dynamically filters itself to show only items *containing* what I typed. The revamped Start menu is one of my favorite Vista features; it directly addresses XP’s [abysmal start menu user experience](https://blog.codinghorror.com/the-start-menu-must-be-stopped/).


But still – **what’s with all the Windows noise**? Wouldn’t that list be so much easier to navigate if we deleted the words “Microsoft” and “Windows” from each entry?


![](https://blog.codinghorror.com/content/images/2025/05/image-363.png)


I’m sure the very suggestion of dropping those key *branding* words will drive the marketing weasels apoplectic. But who’s more important? The users, or your marketing weasels?* Repeated words, if they’re repeated often enough, are just babbling noise.


I have a similar problem with the add reference dialog in Visual Studio.


![](https://blog.codinghorror.com/content/images/2025/05/image-364.png)


Unfortunately this dialog does not support containing search – only “starts with” search – so it’s a royal pain to find what I need. This is a concrete example of how [unnecessary namespacing hurts usability](https://blog.codinghorror.com/a-modest-namespace-proposal/). Thank goodness the System namespace is actually named **System** and not “Microsoft.Windows.dotNet.System.”


*A rhetorical question.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[namespace](https://blog.codinghorror.com/tag/namespace/)
[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[software development](https://blog.codinghorror.com/tag/software-development/)
