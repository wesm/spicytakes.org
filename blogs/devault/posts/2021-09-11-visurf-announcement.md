---
title: "visurf, a web browser based on NetSurf"
date: 2021-09-11
url: https://drewdevault.com/2021/09/11/visurf-announcement.html
slug: visurf-announcement
word_count: 651
---

I’ve started a new side project that I would like to share with you:
 [visurf](https://sr.ht/~sircmpwn/visurf) . visurf, or nsvi, is a  [NetSurf](https://www.netsurf-browser.org)  frontend which provides
vi-inspired key bindings and a lightweight Wayland UI with few dependencies.
It’s still a work-in-progress, and is not ready for general use yet. I’m
letting you know about it today in case you find it interesting and want to
help.

NetSurf is a project which has been on my radar for some time. It is a small web
browser engine, developed in C independently of the lineage of WebKit and Gecko
which defines the modern web today. It mostly supports HTML4 and CSS2, plus only
a small amount of HTML5 and CSS3. Its JavaScript support, while present, is very
limited. Given the  [epidemic of complexity in the modern web](https://drewdevault.com/2020/03/18/Reckless-limitless-scope.html) , I am pleased
by the idea of a small browser, more limited in scope, which perhaps requires
the cooperation of like-minded websites to support a pleasant experience.

I was a  [qutebrowser](https://qutebrowser.org)  user for a long time, and I think it’s a great
project given the constraints that it’s working in — namely, the modern
web. But I reject the modern web, and qute is just as much a behemoth of
complexity as the rest of its lot. Due to stability issues, I finally ended up
abandoning it for Firefox several months ago.

The UI paradigm of qutebrowser’s modal interface, inspired by vi, is quite nice.
I tried to use Tridactyl, but it’s a fundamentally crippled experience due to
the limitations of Web Extensions on Firefox. Firefox has more problems besides
— it may be somewhat more stable, but it’s ultimately still an obscenely
complex, monsterous codebase, owned by an organization which cares less and less
about my needs with each passing day. A new solution is called for.

Here’s where visurf comes in. Here’s a video of it in action:

I hope that this project will achieve these goals:

1. Create a nice new web browser
2. Drive interest in the development of NetSurf
3. Encourage more websites to build with scope-constrained browsers in mind

The first goal will involve fleshing out this web browser, and I could use
your help. Please join #netsurf on irc.libera.chat,  [browse the issue
tracker](https://todo.sr.ht/~sircmpwn/visurf) , and  [send patches](https://lists.sr.ht/~sircmpwn/visurf-devel)  if you are able. Some features I have in mind
for the future are things like interactive link selection, a built-in
readability mode to simplify the HTML of articles around the web, and automatic
redirects to take advantage of tools like  [Nitter](https://github.com/zedeus/nitter) . However, there’s also
more fundamental features to do, like clipboard support, command completion,
even key repeat. There is much to do.

I also want to get people interested in improving NetSurf. I don’t want to see
it become a “modern” web browser, and frankly I think that’s not even possible,
but I would be pleased to see more people helping to improve its existing
features, and expand them to include a reasonable subset of the modern web. I
would also like to add Gemini support. I don’t know if visurf will ever be taken
upstream, but I have been keeping in touch with the NetSurf team while working
on it and if they’re interested it would be easy to see that through.
Regardless, any improvements to visurf or to NetSurf will also improve the
other.

To support the third goal, I plan on overhauling  [sourcehut’s](https://sourcehut.org)  frontend 1 ,
and in the course of that work we will be building a new HTML+CSS framework
(think Bootstrap) which treats smaller browsers like NetSurf as a first-class
target. The goal for this effort will be to provide a framework that allows for
conservative use of newer browser features, with suitable fallbacks, with enough
room for each website to express its own personality in a manner which is
beautiful and useful on all manner of web browsers.

1. Same interface, better code. ↩︎
