---
title: "Smart Tags and Sane Keyboard Shortcuts"
date: 2006-02-02
url: https://blog.codinghorror.com/smart-tags-and-sane-keyboard-shortcuts/
slug: smart-tags-and-sane-keyboard-shortcuts
word_count: 306
---

I constantly rename variables. It’s probably the single most frequent refactoring activity I do. And that’s why I love Visual Studio 2005’s [built-in Smart Tags feature](https://web.archive.org/web/20060213155848/http://msdn.microsoft.com/vcsharp/2005/overview/productivity/#smarttags).


If you’re not familiar with smart tags, check out [K. Scott Allen’s post](http://odetocode.com/Blogs/scott/archive/2006/01/23/2771.aspx); he has some nice screenshots illustrating how it works. Here’s a demo movie of it in action:


![Smart tag rename demo movie](https://blog.codinghorror.com/content/images/uploads/2006/02/6a0120a85dcdae970b0120a86d5c4c970b-pi.gif)


Unfortunately, as Scott points out, **the smart tags are a pain to use via the keyboard**. To maintain compatibility with Microsoft Office’s implementation of smart tags, they chose the same keyboard shortcut:


Shift + Alt + F10


Go ahead. Just try to type that. I double dog dare you. It’s the most psychotic keyboard shortcut *ever*.


If that’s the best keyboard shortcut they can come up, I’ll stick with mousing over the approximately 5 pixel drop-down trigger area of the smart tag. This is really unfortunate, because the [keyboard shortcuts in Visual Studio](https://blog.codinghorror.com/visual-studio-net-2003-and-2005-keyboard-shortcuts/) are generally well thought-out and usable in my experience.


Luckily, I don’t have to suffer through this bad keyboard shortcut for a frequent activity. There’s an alternate shortcut defined:


Ctrl + .


But that’s still not very intuitive. I prefer to use...


Alt + Down


... which is an excellent physical map to the conceptual activity of “dropping down” a smart tag menu. You can easily set this new keyboard shortcut up via Options, Environment, Keyboard. Search for commands containing “ShowSmartTag:”


![](https://blog.codinghorror.com/content/images/2025/05/image-169.png)


Then just map a new global shortcut. Way better!


In general, it’s safer to learn the default keyboard shortcuts for an environment– too much customization is a [self-defeating exercise](https://blog.codinghorror.com/the-problem-with-configurability/). **But sometimes the defaults are poorly chosen and you have no alternative but to customize them.** What default keyboard shortcuts are you obliged to change in your environment, and why?

[visual studio 2005](https://blog.codinghorror.com/tag/visual-studio-2005/)
[smart tags](https://blog.codinghorror.com/tag/smart-tags/)
[keyboard shortcuts](https://blog.codinghorror.com/tag/keyboard-shortcuts/)
[refactoring](https://blog.codinghorror.com/tag/refactoring/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
