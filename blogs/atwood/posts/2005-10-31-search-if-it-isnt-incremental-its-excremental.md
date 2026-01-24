---
title: "Search: If It Isn’t Incremental, It’s Excremental"
date: 2005-10-31
url: https://blog.codinghorror.com/search-if-it-isnt-incremental-its-excremental/
slug: search-if-it-isnt-incremental-its-excremental
word_count: 570
---

After I discovered the CTRL+I [incremental search function](http://msdn2.microsoft.com/en-us/library/f27e8wzh) in Visual Studio, I never used the standard find dialog again. **Incremental search is so good that it makes traditional search dialogs completely obsolete.** If you think that’s hyperbole, consider that [Chris Sells](https://web.archive.org/web/20051101004130/http://www.sellsbrothers.com/spout/) calls incremental search “[pure sex](http://www.hanselman.com/blog/MyIgnoranceProceedsMeVisualStudioNETIncrementalSearch.aspx).”


This particular find dialog is from Notepad, but it’s the basically the same find dialog that appears in every Windows application:


![Standard search in Microsoft Notepad](https://blog.codinghorror.com/content/images/uploads/2005/10/6a0120a85dcdae970b0128776fd3ba970c-pi.png)


The delimited search dialog has a lot of problems:

- **It’s a dialog.** A dialog right smack dab in the middle of the text, potentially obscuring what you’re searching for. In some apps it’s even *modal!*
- **It provides very little feedback.** There’s no indication whether your search term matches anything until you type the complete search term and press return or click Find.
- **It’s an all-or-nothing operation.** Once you initiate a search, you’re committed until the search completes. If you just mistyped a search term in a 5 megabyte text file, have fun waiting for that to complete.
- **It forces you to think about directionality.** If your cursor happens to be near the bottom of the file, you may not find any matches even though some exist at the top of the file. And you get nagged with yet *another* “no matches found” dialog.


Jef Raskin, in his book [The Human Interface](http://www.amazon.com/exec/obidos/ASIN/0201379376), has some choice words for the delimited search dialog:


> This traditional method is rather punishing to the user, although most computer aficionados have become so accustomed to it that they no longer feel the pain.


Now compare that Notepad search dialog with the incremental search in [Firefox](http://www.mozilla.org/products/firefox/):


![Incremental search in Firefox](https://blog.codinghorror.com/content/images/uploads/2005/10/6a0120a85dcdae970b0128776fd3c0970c-pi.gif)


The advantages of incremental search are numerous:

- **There aren’t any dialogs in your way.** The search interface is blissfully dialog-less. There’s nothing getting in the way of you and your search results. You can search, find, and resume working with minimal interruption. This is arguably handled even better in Visual Studio, where the interactive search indicator is a cursor change after you press CTRL+I.
- **It wastes less of your time.** The search begins as soon as the first character is typed. You know immediately when you’ve got a good enough match and you can stop typing.
- **Mistakes are clearly evident.** If you mistype something, you’ll know that immediately, too. Press backspace to correct the typo and you’re back to the previous match.
- **It’s interactive.** Immediate search feedback allows you to adjust your search strategy in real time. The net result is far better searches than you’d ever get from a traditional OK-then-try-again dialog box cycle.


After you’ve worked with incremental search for a few hours, **you’ll probably wonder why incremental search isn’t included as a standard feature in every single Windows application.** As Jef Raskin notes:


> From the point of view of interface engineering, the advantages of incremental searches are so numerous and the advantages of delimited search so few that I can see almost no occasions when a delimited search would be preferred.


Jef also adds an amusing footnote to that sentence: **If it isn’t incremental, it’s excremental.** Amen, brother. I can barely stand to use editors without an incremental search mode any more. I’m so glad that (after a little prodding on my part) the latest betas of EditPad Pro 6 include this feature.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming tools](https://blog.codinghorror.com/tag/programming-tools/)
[text search](https://blog.codinghorror.com/tag/text-search/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
