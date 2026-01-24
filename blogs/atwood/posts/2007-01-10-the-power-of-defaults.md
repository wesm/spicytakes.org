---
title: "The Power of Defaults"
date: 2007-01-10
url: https://blog.codinghorror.com/the-power-of-defaults/
slug: the-power-of-defaults
word_count: 710
---

In [Typing Trumps Pointing](https://blog.codinghorror.com/typing-trumps-pointing/), I extolled the virtues of the full-text search included in Vista’s new Start Menu. As many commenters pointed out, the feature itself is nothing new:


> I love keyboard searching, but basically you say you are installing Vista, an entire operating system, just so you don’t have to install [Colibri](http://colibri.leetspeak.org/),  [SlickRun](http://www.bayden.com/SlickRun/), [Launchy](http://www.launchy.net/), or one of the many other [similar and fully functional tools](http://www.hanselman.com/blog/ReplacingStartRunTheQuestContinues.aspx) that give similar results for 10% cost and 1% hassle.


It’s true. There are dozens of third-party solutions that deliver very similar interactive full-text search UI experiences. But there’s one key difference between those solutions and the one in Vista: **I have to install them**. You may argue that, in the near term, I also have to install Vista. Fair enough. But over the next five years, *millions* of users will buy computers with Vista pre-installed. And they’ll immediately benefit from the built-in, default full-text search UI that’s accessible right out of the box with a single press of the Windows key.


There’s nothing to install. There’s nothing to configure. *It just works*.


That’s the power of defaults.


![](https://blog.codinghorror.com/content/images/2025/08/windows-vista-search-default-1.png)


**Defaults are arguably the most important design decisions you’ll ever make as a software developer.** Choose good defaults, and users will sing the praises of your software and how easy it is to use. Choose poor defaults, and you’ll face down user angst over configuration, and probably a host of tech support calls as well.


Furthermore, once a default becomes a well-accepted standard, it’s an expectation. Other vendors will be peer pressured into at least matching that default. And to truly succeed, they’ll have to come up with an even *better* default. **Defaults are how the software industry evolves.** It also highlights a problem with the Linux and Unix models; because they’re infinitely configurable, it’s impossible to tell what you’re comparing the next version of the software with. There’s no baseline, no standard, only the giant cop-out of [endless user configuration](https://blog.codinghorror.com/the-problem-with-configurability/).


Defaults aren’t just important to software developers; they’re incredibly important to UI designers, too. Jakob Nielsen [elaborates](http://www.useit.com/alertbox/defaults.html):

kg-card-begin: html

> Users rely on defaults in many other areas of user interface design. For example, they rarely utilize fancy [customization features](https://www.useit.com/alertbox/981004.html), making it important to optimize the default user experience, since that’s what most users stick to.
> In forms and applications, pre-populate fields with the most common value if you can determine it in advance. For example, on the registration form for my usability conference, if people register for an event in Boston, the country field will say “United States” by default, but if they register for London, it will say “United Kingdom.” Obviously, many people come from other countries, and they’ll have to change this entry to specify their own country — but they’d have to specify it anyway if we’d left it blank. By choosing the most common country as the default, we save many users that bit of work.
> Defaults make two essential contributions to usability:
> By showing a representative value, they serve as just-in-time instructions to help users understand how to complete a field.
> By showing a frequent value, they help users understand the commonly expected response, as opposed to more atypical ones. You can use this knowledge for sales purposes — for example, by pre-selecting the one-year option in a subscription interface that also offers monthly payments. But, if you consistently pick the most expensive option as the default, you’ll lose credibility, so don’t overdo it.
> By educating and guiding users, default values help reduce errors. It’s therefore important to select helpful defaults, rather than those based on the first letter of the alphabet or whatever the first option on your original list happened to be.

kg-card-end: html

Defaults can also affect your company’s bottom line. That’s why Google, Microsoft, and Yahoo are willing to pay millions of dollars to influence the defaults on a user’s desktop.


For most users, **the default value is the only value**. Your choice of default values will have a profound impact on how your application is used. You should agonize over every default in your software. If you aren’t, you’re doing the user, and yourself, a disservice.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[search functionality](https://blog.codinghorror.com/tag/search-functionality/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
