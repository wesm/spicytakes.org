---
title: "What You Can’t See You Can’t Get"
date: 2012-03-23
url: https://blog.codinghorror.com/what-you-cant-see-you-cant-get/
slug: what-you-cant-see-you-cant-get
word_count: 807
---

I suppose What You See Is What You Get has its place, but as an OCD addled programmer, I have a problem with [WYSIWYG](http://en.wikipedia.org/wiki/WYSIWYG) as a one size fits all solution. Whether it’s [invisible white space](https://blog.codinghorror.com/whitespace-the-silent-killer/), or [invisible formatting tags](https://blog.codinghorror.com/invisible-formatting-tags-are-evil/), it’s been my experience that **forcing people to work with invisible things they cannot directly control… inevitably backfires**. [A lot](https://blog.codinghorror.com/death-to-the-space-infidels/).


I have a distinctly [Ghostbusters](http://en.wikipedia.org/wiki/Ghostbusters) attitude to this problem.


![](https://blog.codinghorror.com/content/images/2025/04/image-593.png)


I need to *see* these invisible things, so that I can zap them with my [proton pack](http://en.wikipedia.org/wiki/Proton_pack). I mean, er, *control* them. And more importantly, understand them; perhaps even [master them](http://www.amazon.com/dp/B005Y3EDR4).


I recently had the great privilege of meeting [Ted Nelson](http://en.wikipedia.org/wiki/Ted_Nelson), who gave me an in-person demo of his [ZigZag](http://xanadu.com/zigzag/) project and his perpetually [in-progress since 1960 Xanadu project](https://blog.codinghorror.com/the-xanadu-dream/), currently known as [Xanadu Space](https://www.xanadu.net/). But one thing he mentioned as he gave the demo particularly intrigued me. Being Ted Nelson, of course he went much further than my natural aversion to invisible, hidden markup in content – he insisted that markup and content should *never* be [in the same document](http://www.xml.com/pub/a/w3j/s3.nelson.html). Far more radical.

kg-card-begin: html

> I want to discuss what I consider one of the worst mistakes of the current software world, embedded markup; which is, regrettably, the heart of such current standards as SGML and HTML. (There are many other embedded markup systems; an interesting one is RTF. But I will concentrate on the SGML-HTML theology because of its claims and fervor.)
> There is no one reason this approach is wrong; I believe it is wrong in almost every respect.
> I propose a three-layer model:
> A **content layer** to facilitate editing, content linking, and transclusion management.
> A **structure layer**, declarable separately. Users should be able to specify entities, connections and co-presence logic, defined independently of appearance or size or contents; as well as overlay correspondence, links, transclusions, and “hoses” for movable content.
> A **special-effects-and-primping layer** should allow the declaration of ever-so-many fonts, format blocks, fanfares, and whizbangs, and their assignment to what’s in the content and structure layers.

kg-card-end: html

It’s an interesting, albeit extremely hand-wavy and complex, alternative. I’m unclear how you would keep the structure layer in sync with the content layer if someone is editing the content. I don’t even know if there are any real world examples of this three layer approach in action. (And as usual, feel free to correct me in the comments if I’ve missed anything!)


Instead, what we do have are existing, traditional methods of **intermixing content and markup** ala HTML or TeX.


![](https://blog.codinghorror.com/content/images/2025/04/image-592.png)


When editing, there are two possible interfaces:

1. **WYSIWYG** where the markup layer is magically hidden so, at least in theory, the user doesn’t ever have to know about markup and can focus entirely on the content. It is an illusion, but it is simple enough when it’s working. The downside is that the abstraction – this idea that the markup is truly “invisible” – is rarely achieved in practice and often breaks down for anything except the most basic of documents. But it can be good enough in a lot of circumstances.
2. **Two windows** where the markup is fully visible in one window, and shown as a live rendered preview in the other window, updated as you type, either side-by-side or top-and-bottom. Users have a dynamic sandbox where they can experiment and learn how markup and content interact in the real world, rather than having it all swept under the rug. Ultimately, this results in less confusion for intermediate and advanced users. That’s why I’m particularly fond of this approach, and it is what [we use on Stack Exchange](https://blog.codinghorror.com/treating-user-myopia/). The downside is that it’s a bit more complex, depending on whether or not you use [humane markup](https://blog.codinghorror.com/is-html-a-humane-markup-language/), and it certainly takes a bit more screen space and thinking to process what’s going on.


What I didn’t realize is that there’s actually a *third* editing option: **keep the markup visible, and switch rapidly back and forth between the markup and rendered view with a single keystroke**. That’s what the [Gliimpse project](http://www.aviz.fr/gliimpse/) reveals:


Please watch the video. The nearly instantaneous and smooth transition that Gliimpse demonstrates between markup and preview has to be seen to be appreciated. The effect is a bit like [Expose on the Mac, or Switcher on PC](https://blog.codinghorror.com/on-expos-flip3d-and-switcher/). I’m not sure how I feel about this, mainly because I don't know of any existing IDEs that even attempt to do anything remotely like it.


But I’d sure like to try it. As a software developer, it’s incredibly frustrating to me that we have generational improvements in games like Skyrim and [Battlefield 3](https://blog.codinghorror.com/multiple-video-cards/) that render vastly detailed, dynamic worlds at 60 frames per second, yet our [source code editors are advancing](https://blog.codinghorror.com/its-the-ide-dummy/) only in tiny incremental steps, year after year.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
