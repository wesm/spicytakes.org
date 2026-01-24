---
title: "The Visual Studio IDE and Regular Expressions"
date: 2006-07-12
url: https://blog.codinghorror.com/the-visual-studio-ide-and-regular-expressions/
slug: the-visual-studio-ide-and-regular-expressions
word_count: 622
---

The Visual Studio IDE supports **searching and replacing with regular expressions**, right? Sure it does. It’s right there in grey and black in the find and replace dialog. Just tick the “use Regular expressions” checkbox and we’re off to the races.


![](https://blog.codinghorror.com/content/images/2025/05/image-335.png)


However, you’re in for an unpleasant surprise when you attempt to actually *use *regular expressions to find anything in Visual Studio. Apparently the Visual Studio IDE has its own [bastardized regular expression syntax.](http://msdn2.microsoft.com/en-us/library/2k3te2cs(d=ide).aspx) Why? Who knows. Probably for arcane backwards compatibility reasons, although I have no idea why you’d want to perpetually carry forward insanity. Evidently it [makes people billionaires](https://blog.codinghorror.com/microsoft-1978/), so who am I to judge.


God forbid we all learn one standard* regular expression dialect.


At any rate, some of the Visual Studio IDE regular expressions look awfully similar to standard regex:

kg-card-begin: html


|  | **Visual Studio IDE** | **Standard** |
| Any single character | . | . |
| Zero or more | * | * |
| One or more | + | + |
| Beginning of line | ^ | ^ |
| End of line | $ | $ |
| Beginning of word | < | (no equivalent) |
| End of word | > | (no equivalent) |
| Line break | n | n |
| Any character in set | [ ] | [ ] |
| Any character not in set | [^ ] | [^ ] |
| Or | | | | |
| Escape special char |  |  |
| Tag expression | { } | ( ) |
| C/C++ identifier | :i | ([a-zA-Z_$][a-zA-Z0-9_$]*) |
| Quoted string | :q | (("[^"]*")|('[^']*')) |
| Space or Tab | :b | [ |t] |
| Integer | :z | [0-9]+ |


kg-card-end: html

But they certainly don’t *act* related when you try to use them. For example, try something simple, like finding “[A-Za-z]+.” That’s all occurrences of more than one letter in a row. When I try this via the Visual Studio find dialog with the regex option checked, I get positively *bizarre* results. It finds a word made up of all letters, true, but as I click “Find Next,” it then finds each subsequent letter in the word. Again. What planet are these so-called “regular expressions” from?


The semi-abandoned Microsoft VSEditor blog has a three part tutorial ([part one](https://web.archive.org/web/20060719115139/http://blogs.msdn.com/vseditor/archive/2004/06/16/157276.aspx), [part two](https://web.archive.org/web/20060719115152/http://blogs.msdn.com/vseditor/archive/2004/06/18/159515.aspx), [part three](https://web.archive.org/web/20060719115203/http://blogs.msdn.com/vseditor/archive/2004/07/12/181078.aspx)) on using the crazy Visual Studio dialect of Regex. There’s a lot of emphasis on the strange < and > begin/end word match characters, which have no equivalent that I know of in the .NET and Perl dialect of regular expressions.


You might say that **searching with regular expressions is such an extreme edge condition for most developers** that it’s not worth the Visual Studio development team’s time. I won’t disagree with you. It is rare, but it’s hardly esoteric. Every developer should be able to grok the value of searching with the basic regular expressions that are a staple of their toolkit these days. Heck, some developers are so hard core they [search through their code](http://steve-yegge.blogspot.com/2006/06/shiny-and-new-emacs-22.html) with Lisp expressions. Basic regex search functionality is awfully mild compared to that.


To be honest, searching with regular expressions isn’t a common task for me either. But I’d be a lot more likely to use it if I didn’t have to perform a lot of mental translation gymnastics on the occasions that I needed it. [Don’t make me think](https://blog.codinghorror.com/dont-make-me-think-second-edition/), man. But there is hope. There’s a free add-in available which offers real regular expression searching in Visual Studio.


*Well, *mostly* standard, anyway. Certainly JavaScript regex syntax could be considered standard these days.

[regex](https://blog.codinghorror.com/tag/regex/)
[visual studio ide](https://blog.codinghorror.com/tag/visual-studio-ide/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[programming](https://blog.codinghorror.com/tag/programming/)
[software development](https://blog.codinghorror.com/tag/software-development/)
