---
title: "Standard Flavored Markdown"
date: 2014-09-03
url: https://blog.codinghorror.com/standard-flavored-markdown/
slug: standard-flavored-markdown
word_count: 1030
---

In 2009, I [lamented the state of Markdown](https://blog.codinghorror.com/responsible-open-source-code-parenting/):


> Right now we have the worst of both worlds. Lack of leadership from the top, and a bunch of fragmented, poorly coordinated community efforts to advance Markdown, none of which are officially canon. This isn’t merely incovenient for anyone trying to find accurate information about Markdown; it’s actually harming the project’s future.


In late 2012, David Greenspan from [Meteor](https://www.meteor.com/) approached me and proposed we move forward, and [a project crystallized](https://blog.codinghorror.com/the-future-of-markdown/):


> I propose that Stack Exchange, GitHub, Meteor, Reddit, and any other company with lots of traffic and a strategic investment in Markdown, all work together to **come up with an official Markdown specification, and standard test suites to validate Markdown implementations**. We’ve all been working at cross purposes for too long, accidentally fragmenting Markdown while popularizing it.


We formed a small private working group with key representatives from GitHub, from Reddit, from Stack Exchange, from the open source community. We spent months hashing out the details and agreeing on the necessary changes to turn Markdown into a language you can parse without feeling like you just walked through a sewer – while preserving the simple, clear, ASCII email inspired spirit of Markdown.


We really struggled with this at [Discourse](http://www.discourse.org/), which is also based on Markdown, but an even more complex dialect than the one we built at Stack Overflow. In Discourse, you can mix *three* forms of markup interchangeably:

- Markdown
- HTML (safe subset)
- BBCode (subset)


Discourse is primarily a JavaScript app, so naturally we needed a nice, compliant implementation of Markdown in JavaScript. Surely such a thing exists, yes? Nope. Even in 2012, we found *zero* JavaScript implementations of Markdown that could pass the only Markdown test suite I know of, [MDTest](https://github.com/michelf/mdtest/). It isn’t authoritative, it’s a community created initiative that embodies its own decisions about rendering ambiguities in Markdown, but it’s all we’ve got. We contributed many [upstream fixes to markdown.js](https://github.com/evilstreak/markdown-js/commits/master) to make it pass MDTest – but it still only passes in our locally extended version.


As an open source project ourselves, we’re perfectly happy contributing upstream code to improve it for everyone. But it’s an indictment of the state of the Markdown ecosystem that any remotely popular implementation wasn’t already testing itself against a formal spec and test suite. But who can blame them, because *it didn’t exist!*


Well, now it does.


It took a while, but I’m pleased to announce that **Standard Markdown** is now finally ready for public review.


[**standardmarkdown.com**](http://standardmarkdown.com/)


It’s a spec, including embedded examples, and implementations in portable C and JavaScript. We strived mightily to stay true to the spirit of Markdown in writing it. The primary author, John MacFarlane, explains in the introduction to the spec:


> Because Gruber’s syntax description leaves many aspects of the syntax undetermined, writing a precise spec requires making a large number of decisions, many of them somewhat arbitrary. In making them, I have appealed to existing conventions and considerations of simplicity, readability, expressive power, and consistency. I have tried to ensure that “normal” documents in the many incompatible existing implementations of markdown will render, as far as possible, as their authors intended. And I have tried to make the rules for different elements work together harmoniously. In places where different decisions could have been made (for example, the rules governing list indentation), I have explained the rationale for my choices. In a few cases, I have departed slightly from the canonical syntax description, in ways that I think further the goals of markdown as stated in that description.


Part of my contribution to the project is to host the discussion / mailing list for Standard Markdown in a Discourse instance.


Fortunately, Discourse itself [just reached version 1.0](http://blog.discourse.org/2014/08/introducing-discourse-1-0/). If the only thing Standard Markdown does is help save a few users from the continuing horror that is mailing list web UI, we all win.


What I’m most excited about is that we got a massive contribution from the one person who, in my mind, was the most perfect person in the world to work on this project: [John MacFarlane](http://johnmacfarlane.net/). He took our feedback and wrote the entire Standard Markdown spec and both implementations.


![](https://blog.codinghorror.com/content/images/2025/05/image-188.png)


A lot of people know of John through his [Pandoc](http://johnmacfarlane.net/pandoc/) project, which is amazing in its own right, but I found out about him because he built [Babelmark](http://johnmacfarlane.net/babelmark2/faq.html). I learned to refer to Babelmark extensively while working on Stack Overflow and MarkdownSharp, a C# implementation of Markdown.


Here’s how crazy Markdown is: to decide what the “correct” behavior is, you provide sample Markdown input to 20+ different Markdown parsers… and then pray that some consensus emerges in all their output. That’s what Babelmark does.


Consider this simple Markdown example:


```
# Hello there

This is a paragraph.

- one
- two
- three
- four

1. pirate
2. ninja
3. zombie

```


Just for that, I count *fifteen* different rendered outputs from 22 different Markdown parsers.


![](https://blog.codinghorror.com/content/images/2025/05/image-189.png)


In Markdown, we *literally* built a [Tower of Babel](http://en.wikipedia.org/wiki/Tower_of_Babel).


Have I mentioned that it’s a good idea for a language to have a formal specification and test suites? Maybe now you can see why that is.


Oh, and in his spare time, John is also the chair of the department of philosophy at the University of California, Berkeley. *No big deal.* While I don’t mean to minimize the contributions of anyone to the Standard Markdown project, we all owe a special thanks to John.


Markdown is indeed everywhere. And that’s a good thing. But it needs to be sane, parseable, and standard. That’s the goal of Standard Markdown – but we need your help to get there. If you use Markdown on a website, **ask what it would take for that site to become compatible with Standard Markdown**; when you see the word “Markdown” you have the right to expect consistent rendering across all the websites you visit. If you implement Markdown, take a look at the spec, try to **make your parser compatible with Standard Markdown**, and discuss improvements or refinements to the spec.


Update: The project was renamed [CommonMark](http://commonmark.org/). See [my subsequent blog post](https://blog.codinghorror.com/standard-markdown-is-now-common-markdown/).

[markdown](https://blog.codinghorror.com/tag/markdown/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[community efforts](https://blog.codinghorror.com/tag/community-efforts/)
[standardization](https://blog.codinghorror.com/tag/standardization/)
[collaboration](https://blog.codinghorror.com/tag/collaboration/)
