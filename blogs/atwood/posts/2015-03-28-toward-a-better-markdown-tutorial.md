---
title: "Toward a Better Markdown Tutorial"
date: 2015-03-28
url: https://blog.codinghorror.com/toward-a-better-markdown-tutorial/
slug: toward-a-better-markdown-tutorial
word_count: 999
---

It’s always surprised me when people, especially technical people, say they don’t know [Markdown](http://en.wikipedia.org/wiki/Markdown). Do you not use GitHub? Stack Overflow? Reddit?


I get that an average person may not understand how Markdown is based on simple old-school plaintext ASCII typing conventions. Like when you’re *really* excited about something, you naturally put asterisks around it, and Markdown makes that automagically italic.


But how can we expect them to know that, if they grew up with wizzy-wig editors where the only way to make italic is to click a toolbar button, like an animal?


![](https://blog.codinghorror.com/content/images/2015/03/classic-wysiwyg-toolbar.png)


I am not advocating for WYSIWYG here. While there’s certainly more than one way to make italic, I personally [don’t like invisible formatting tags](https://blog.codinghorror.com/invisible-formatting-tags-are-evil/) and I find that WYSIWYG is more like [WYCSYCG](https://blog.codinghorror.com/what-you-cant-see-you-cant-get/) in practice. It’s dangerous to be dependent on these invisible formatting codes you can’t control. And they’re especially bad if you ever plan to care about differences, revisions, and edit history. That’s why I like to teach people simple, *visible* formatting codes.


We can certainly debate [which markup language is superior](https://blog.codinghorror.com/is-html-a-humane-markup-language/), but in Discourse we tried to build a rainbow tool that satisifies everyone. We support:

- HTML (safe subset)
- BBCode (basic subset)
- Markdown (full)


This makes coding our editor kind of hellishly complex, but it means that for you, the user, whatever markup language you’re used to will probably “just work” on any Discourse site you happen to encounter in the future. But BBCode and HTML are supported mostly as bridges. What we view as our primary markup format, and what we want people to learn to use, is Markdown.


However, one thing I have really struggled with is that **there isn’t any single great place to refer people to with a simple walkthrough and explanation of Markdown.**


When we built Stack Overflow circa 2008-2009, I put together my best effort at the time which became [the “editing help” page](http://www.stackoverflow.com/editing-help):


![](https://blog.codinghorror.com/content/images/2015/03/markdown-help.png)


It’s just OK. And GitHub has their [Markdown Basics](https://help.github.com/articles/markdown-basics/), and [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/) help pages. They’re OK.


The [Ghost](https://ghost.org/) editor I am typing this in has an OK Markdown help page too.


![](https://blog.codinghorror.com/content/images/2015/03/ghost-markdown-help.png)


But none of these are *great*.


**What we really need is a *great* Markdown tutorial and reference page**, one that we can refer anyone to, anywhere in the world, from someone who barely touches computers to the hardest of hard-core coders. I don’t want to build another one for these kinds of help pages for Discourse, I want to build one for everyone. Since it is for everyone, I want to involve everyone. And by everyone, I mean you.


After writing about [Our Programs Are Fun To Use](https://blog.codinghorror.com/our-programs-are-fun-to-use/) – which I just updated with a bunch of great examples contributed in the comments, so go check that out even if you read it already – I am inspired by the idea that **we can make a fun, *interactive* Markdown tutorial together.**


So here’s what I propose: **a small contest** to build an interactive Markdown tutorial and reference, which we will eventually host at the home page of [commonmark.org](http://commonmark.org/), and can be freely mirrored anywhere in the world.


Some ground rules:

- It should be *primarily* in JavaScript and HTML. Ideally entirely so. If you need to use a server-side scripting language, that’s fine, but try to keep it simple, and make sure it’s something that is reasonable to deploy on a generic Linux server anywhere.
- You can pick any approach you want, but it should be [highly interactive](https://blog.codinghorror.com/our-programs-are-fun-to-use/), and I suggest that you at minimum provide two tracks:
- There’s a lot of variance in Markdown implementations, so teach the most common parts of Markdown, and cover the optional / less common variations either in the advanced reference areas or in extra bonus sections. People do love their tables and footnotes! We recommend using a [CommonMark compatible implementation](http://talk.commonmark.org/c/implementation), but it is not a requirement.
- Your code must be MIT licensed.
- Judging will be completely at the whim of myself and John MacFarlane. Our decisions will be capricious, arbitrary, probably nonsensical, and above all, final.
- We’ll run this contest for a period of one month, from today until April 28th, 2015.
- If I have hastily left out any clarifying rules I should have had, they will go here.


Of course, the real reward for building is the admiration of your peers, and the knowledge that an entire generation of people will grow up learning basic Markdown skills through your contribution to a global open source project.


But on top of that, I am offering… *fabulous prizes!*

1. Let’s start with my [Recommended Reading List](https://blog.codinghorror.com/recommended-reading-for-developers/). I count sixteen books on it. As long as you live in a place Amazon can ship to, I’ll send you all the books on that list. (Or the equivalent value in an Amazon gift certificate, if you happen to have a lot of these books already, or prefer that.)
2. Second prize is a [CODE Keyboard](https://blog.codinghorror.com/the-code-keyboard/). This can be shipped worldwide.
3. Third prize is *you’re fired*. Just kidding. Third prize is your choice of any three books on my reading list. (Same caveats around Amazon apply.)


Looking for a place to get started? Check out:

- [https://github.com/gjtorikian/markdowntutorial.com](https://github.com/gjtorikian/markdowntutorial.com) and [http://markdowntutorial.com](http://markdowntutorial.com/) by Garen Torikian
- [https://github.com/chrisalley/commonmark-website](https://github.com/chrisalley/commonmark-website) and [https://web.archive.org/web/20150403041531/http://chrisalley.github.io/commonmark-website](https://web.archive.org/web/20150403041531/http://chrisalley.github.io/commonmark-website/) by Chris Alley


If you want privacy, you can mail your entries to me directly (see the about page here for my email address), or if you are comfortable with posting your contest entry in public, I’ll create a topic on [talk.commonmark](http://talk.commonmark.org/) for you to post links and gather feedback. Leaving your entry in the comments on this article is also OK.


We desperately need a *great* place that we can send everyone to learn Markdown, and we need your help to build it. Let’s give this a shot. Surprise and amaze us!


> Update: we selected [winners](http://talk.commonmark.org/t/markdown-tutorial-contest-feedback/1149/19) in June 2015 and the final result is now permanently located at [**commonmark.org/help**](http://commonmark.org/help) – enjoy!

[markdown](https://blog.codinghorror.com/tag/markdown/)
[tutorial](https://blog.codinghorror.com/tag/tutorial/)
[github](https://blog.codinghorror.com/tag/github/)
[stack overflow](https://blog.codinghorror.com/tag/stack-overflow/)
[reddit](https://blog.codinghorror.com/tag/reddit/)
