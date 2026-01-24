---
title: "Notepad Strikes Back"
date: 2005-03-04
url: https://blog.codinghorror.com/notepad-strikes-back/
slug: notepad-strikes-back
word_count: 650
---

In [revenge of Notepad](https://blog.codinghorror.com/revenge-of-notepad/), I recommended Florian Balmer’s truly excellent freeware Notepad replacement, [Notepad2](http://www.flos-freeware.ch/notepad2.html). And when I say replacement, I mean *replacement*:

kg-card-begin: html

```
copy notepad2.exe c:windowsservicepackfilesi386notepad.exe
copy notepad2.exe c:windowssystem32dllcachenotepad.exe
copy notepad2.exe c:windowssystem32notepad.exe
copy notepad2.exe c:windowsnotepad.exe
```

kg-card-end: html

[What good is Notepad doing](https://web.archive.org/web/20050924061708/http://neopoleon.com/blog/posts/12904.aspx) anyone these days? Why even keep it around when there are so many other worthy replacements available with marginally larger memory footprints?


Unfortunately, after six months of living with Notepad2, some glaring deficiencies began to nag at me. The biggest problem was performance slowing to a crawl on my Athlon 3200+ when I opened a text file larger than a few megabytes. Or the way Notepad2 would go into minute-long convulsions if I tried to search that same file. Now, to be fair, this isn’t Florian’s fault – these are limitations of the [Scintilla engine](http://www.scintilla.org) he uses to drive his (free!) app.


I don’t think it’s unreasonable to ask a basic text editing app to have decent performance on largish text files in the 5mb - 100mb range. Although I’ve been relatively happy with Notepad2, I work with files this size fairly often, so I had no choice but to search for **Yet Another Notepad Replacement.** I felt guilty emailing Florian with questions since he was already providing such an excellent bit of software completely gratis – so this time, I figured I’d bite the bullet and purchase something with a more formal support relationship.


I did quite a bit of searching for commercial text editor recommendations from other developers, which turned up the following:

- [UltraEdit](http://www.ultraedit.com) - $40
- [EditPlus](http://www.editplus.com/) - $30
- [EditPad Pro](http://www.editpadpro.com) - $40
- [TextPad](http://www.textpad.com/products/textpad/index.html) - $32
- [EmEditor](http://www.emeditor.com/) - $40
- [NoteTab Pro](http://www.notetab.com/ntp.php) - $20


I won’t even pretend that I lived with these applications long enough to have an informed opinion about which one is “best.” I didn’t. I browsed through the screenshots and feature list for each one, and then chose two trial versions for a quick spin. Rather than harping on feature checklists, I tried to consider what I actually do in my existing text editor:

1. I sometimes edit fairly large text files.
2. I might use this for lightweight scripting and HTML coding tasks.
3. I don’t need another full-blown IDE (e.g., Visual SlickEdit). I have Visual Studio for that.
4. I expect flexible syntax highlighting.
5. I want something relatively lightweight; starts fast, runs fast.
6. [I loves me some Regex.](https://blog.codinghorror.com/regex-use-vs-regex-abuse/) I need extensive, complete Regex support.


Based on my prior usage history, I felt that EditPad Pro was the best fit: **it’s quite fast on large text files, has best-of-breed Regex support, and it doesn’t pretend to be an IDE.** I can even set up custom syntax coloring schemes using regular expressions; there’s a large library of [predefined Regex coloring schemes](http://www.editpadpro.com/cgi-bin/cscslist2.pl) available for download, along with a nice standalone color scheme editor. EditPad Pro was written by Jan Goyvaerts aka [JGSoft](http://www.jgsoft.com/), who is also the author of PowerGREP and RegexBuddy. I’ve recommended both of these Regex-centric products in [prior](https://blog.codinghorror.com/regexbuddy-and-friends/) [posts](https://blog.codinghorror.com/gettin-greppy-wit-it/), so it’s probably not too surprising that I think Jan has one of the best text editing apps. Regex-y minds think alike.


As I did with Notepad2, I’ll have to live with it for about six months before I can claim to have anything resembling an informed opinion about it. If you’re still unconvinced that spending $30 on a fancy text editor is a good idea, there are plenty of freeware alternatives as well. The ones most often mentioned are:

- [Crimson Editor](http://www.crimsoneditor.com/)
- [SynText](http://syn.sourceforge.net/)
- [Notepad2](http://www.flos-freeware.ch/notepad2.html)
- AEdiX
- [ConTEXT](http://www.context.cx/)
- [PSPad](http://www.pspad.com/en/)


Between these two lists, that covers 90% of the Windows text editors I saw recommended in my research. For the more obscure and/or UNIX based text editors, check out the [Wikipedia entry on text editors](http://en.wikipedia.org/wiki/List_of_text_editors).

[text editor.

tags:
software development concepts](https://blog.codinghorror.com/tag/text-editor-tags-software-development-concepts/)
[text editor](https://blog.codinghorror.com/tag/text-editor/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[software tools](https://blog.codinghorror.com/tag/software-tools/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
