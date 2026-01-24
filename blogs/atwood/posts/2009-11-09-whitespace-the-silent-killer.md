---
title: "Whitespace: The Silent Killer"
date: 2009-11-09
url: https://blog.codinghorror.com/whitespace-the-silent-killer/
slug: whitespace-the-silent-killer
word_count: 406
---

Ever have one of those days where **everything you check into source control is wrong?**


Also, how exactly is that day is different from any other? But seriously.


Code that is visible is [code that can be wrong](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/). No surprise there. But did you know that even the code you *can’t* see may be wrong, too?


These are the questions that drive young programmers to madness. Take this perfectly innocent code, for example.


![](https://blog.codinghorror.com/content/images/2025/04/image-444.png)


Looks fine, doesn’t it? But hold on. Wait a second. Let’s take another, closer look.


![](https://blog.codinghorror.com/content/images/2025/04/image-443.png)


*OH. MY. **GOD!***


If you’re not a programmer, you may be looking at these two images and wondering what the big deal is. That’s fine. But I humbly submit that, well, you’re not one of us. You don’t appreciate what it’s like to spend every freaking minute of every freaking day agonizing over the tiniest details of the programs you write. Not because we *want* to, you understand, but because the world explodes when we don’t.


I mean that literally. Well, [almost](https://web.archive.org/web/20091112104818/http://bugsniffer.blogspot.com/2007/11/infamous-software-failures.html). If one semicolon is out of place, [everything goes sideways](http://www.google.com/search?q=failure+%27missing+semicolon%27). That’s how programming works. It’s fun! Sometimes! I swear!


We got into this industry because, quite frankly, we are control freaks. It’s who we are. It’s what we do. Now to imagine, to our dismay, that there’s all this stupid, useless *whitespace* at the ends of our lines. Stuff that’s there, but we can’t see it. Well, those are the nightmares OCD horror movies are made of. I have a full-body itchiness just talking about it.


Depending on how far down the rabbit-hole you want to go, there’s any number of things you could do here:

- Have a post-build step, perhaps something with a regular expression like `s*?$` in it, that auto-cleans extra spaces checked into source control
- Execute a local macro which removes whitespace from ends of lines
- Have a special rule to highlight extra spaces
- Run your IDE in whitespace-always-visible mode, or toggle it frequently


OK, fine, so maybe the world won’t explode if there are a few extra bits of whitespace in my code.


But all the same, I think I’ll go back and make *extra double plus sure* no more of that pesky whitespace has accumulated in my code when I wasn’t looking. Just because I can’t see it doesn’t mean it’s not out to get me.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[code quality](https://blog.codinghorror.com/tag/code-quality/)
[coding standards](https://blog.codinghorror.com/tag/coding-standards/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[code review](https://blog.codinghorror.com/tag/code-review/)
