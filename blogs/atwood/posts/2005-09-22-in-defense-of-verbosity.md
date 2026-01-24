---
title: "In Defense of Verbosity"
date: 2005-09-22
url: https://blog.codinghorror.com/in-defense-of-verbosity/
slug: in-defense-of-verbosity
word_count: 701
---

During the fantastic [Monad](https://web.archive.org/web/20051219170356/http://www.microsoft.com/downloads/details.aspx?FamilyID=2AC59B30-5A44-4782-B0B7-79FE2EFD1280&displaylang=en) session at PDC 2005,* Jeffrey Snover and Jim Truher illustrated the tradeoff between verbosity and conciseness:

kg-card-begin: html

```

cp c:apples c:oranges -fo -r

```

kg-card-end: html
kg-card-begin: html

```

copy-item c:apples c:oranges -force -recurse

```

kg-card-end: html

Monad has a ton of aliases for common commands (e.g., echo is the same as write-object), and it’s smart enough to disambiguate parameters if you type enough characters. You get to choose: do I want to be verbose, or do I want to be concise?


Even UNIX tools, which aren’t exactly known for their user friendliness, typically offer both verbose and concise options. Consider [the excellent wget](https://web.archive.org/web/20051016012907/http://xoomer.virgilio.it/hherold/) utility as an example. What the heck does this mean:

kg-card-begin: html

```

wget -m -k -K -E http://www.gnu.org/ -o /home/me/weeklog

```

kg-card-end: html

Who knows? It could be doing anything. But if we disambiguate with the verbose parameters...

kg-card-begin: html

```

wget –mirror –convert-links –backup-converted
–html-extension -o /home/me/weeklog
http://www.gnu.org/

```

kg-card-end: html

Suddenly it’s quite plain what is happening.


**People say VB.NET is too verbose like that’s a bad thing.** Is English too verbose? Would this post be easier to read in a court reporter’s [shorthand](http://en.wikipedia.org/wiki/Shorthand)? Would it be easier to read if I dropped the vowels and the stopwords?


Compare this elegant, concise C# code...

kg-card-begin: html

```

}
}
}

```

kg-card-end: html

... to its VB.NET equivalent:

kg-card-begin: html

```

End Select
End If
End If

```

kg-card-end: html

VB.NET has its problems, to be sure, but verbosity isn’t one of them. **Saving keystrokes while writing code is a fool’s economy.** Isn’t that why we have these fancy IDEs? As Steve McConnell notes in [Write Programs for People First](http://www.amazon.com/exec/obidos/ASIN/0735619670), Computers Second, optimizing for conciseness is a poor tradeoff. Most code is written only once, but read dozens of times:


> *The computer doesn’t care whether your code is readable. It’s better at reading binary machine instructions than it is at reading high-level language statements. You write readable code because it helps other people to read your code.
> Readable code doesn’t take any longer to write than confusing code does, at least not in the long run. It’s easier to be sure your code works if you easily read what you wrote. That should be a sufficient reason to write readable code. But code is also read during reviews. It’s read when you or someone else fixes an error. It’s read when the code is modified. It’s read when someone tries to use part of your code in a similar program.
> **Making code readable is not an optional part of the development process, and favoring write-time convenience over read-time convenience is a false economy.** You should go to the effort of writing good code, which you can do once, rather than the effort of reading bad code, which you’d have to do again and again.
> The idea of writing unreadable code because you’re the only person working on a project sets a dangerous precedent. Your mother used to say, “What if your face froze in that expression?” And your dad used to say, “You play how you practice.” Habits affect all your work; you can’t turn them on and off at will, so be sure that what you’re doing is something that you want to become a habit. A professional programmer writes readable code, period.
> Even if you think you’re the only one who will read your code, in the real world chances are good that someone else will need to modify your code. One study found that 10 generations of maintenance programmers work on an average program before it gets rewritten (Thomas 1984). Maintenance programmers spend 50 to 60 percent of their time trying to understand the code they have to maintain, and they appreciate the time you put into documenting it (Parikh and Zvegintzov 1983).*


The ethic Steve is promoting here isn’t specific to any language, of course. But it certainly does skew the results in favor of verbosity – if it’s available.


*Which were evidently [rated #3](https://web.archive.org/web/20060223031830/https://blogs.msdn.com/monad/archive/2005/09/20/472036.aspx) right after Anders’ two talks, so if you didn’t go, you missed a great session!

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[command-line interfaces](https://blog.codinghorror.com/tag/command-line-interfaces/)
[verbosity](https://blog.codinghorror.com/tag/verbosity/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
