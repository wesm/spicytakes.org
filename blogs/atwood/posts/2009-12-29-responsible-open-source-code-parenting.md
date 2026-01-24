---
title: "Responsible Open Source Code Parenting"
date: 2009-12-29
url: https://blog.codinghorror.com/responsible-open-source-code-parenting/
slug: responsible-open-source-code-parenting
word_count: 1558
---

I’m a big fan of [John Gruber’s Markdown](http://daringfireball.net/projects/markdown/). When it comes to humane markup languages for the web, I don’t think anyone’s quite nailed it like Mr. Gruber. His philosophy was clear from the outset:


> Markdown is intended to be as easy-to-read and easy-to-write as is feasible.
> Readability, however, is emphasized above all else. **A Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions.** While Markdown’s syntax has been influenced by several existing text-to-HTML filters – including Setext, atx, Textile, reStructuredText, Grutatext, and EtText – the single biggest source of inspiration for Markdown’s syntax is the format of plain text email.


If you’re an ASCII-head of any kind, you will feel immediately at home in Markdown. It was so obviously designed by someone who has done a *lot* of writing online, as it apes common plaintext conventions that we’ve collectively been using for decades now. It’s certainly far more intuitive than [the alternatives](https://blog.codinghorror.com/is-html-a-humane-markup-language/)[ I’ve researched](https://blog.codinghorror.com/is-html-a-humane-markup-language/).


With a year and a half of real world Markdown experience [under our belts](http://blog.stackoverflow.com/2009/10/markdown-one-year-later/) on Stack Overflow, we’ve been quite happy. I’d say that Markdown is the *worst* form of markup except for all the other forms of markup that I’ve tried. Of course, tastes vary, and there are plenty of viable alternatives, but I’d promote Markdown without hesitation as one of the best – if not *the* best – humane markup options out there.


Not that Markdown is perfect, mind you. After exposing it to a large audience, both Stack Overflow [and GitHub](http://github.github.com/github-flavored-markdown/) independently discovered that Markdown had three particular characteristics that confused a lot of users:

1. URLs are never hyperlinked without placing them in some kind of explicit markup.
2. The underscore [_] can be used to delimit bold and italic, but also works for intra-word emphasis. While a typical use like “_italic_” is clear, there are disturbing and unexpected side effects in phrases such as “some_file_name” and “file_one and file_two”.
3. It is paragraph and not line oriented. Returns are not automatically converted to linebreaks. Instead, paragraphs are detected as one or more consecutive lines of text, separated by one or more blank lines.


Items #1 and #2 are so fundamental and universal that I think **they deserve to be changed in the Markdown specification itself**. There was so much confusion around unexpected intra-word emphasis and the failure to auto-hyperlink URLs that we changed these Markdown rules before we even came out of private beta. Item #3, the conversion of returns to linebreaks, is somewhat more debatable. I’m on the fence on that one, but I do believe it’s significant enough to warrant an explicit choice either way. It should be a standard configurable option in every Markdown implementation that you can switch on or off depending on the intended audience.


Markdown was originally introduced in 2004, and since then it has gained quite a bit of traction on the web. I mean, [it’s no MediaWiki](http://www.mediawiki.org/wiki/Help:Formatting) (thank God), but it’s in active use on a bunch of websites, some of them [quite popular](http://www.joelonsoftware.com/items/2009/12/13.html). And for such a popular form of markup, it’s a bit odd that the last official update to the specification and reference implementation was in late 2004.


Which leads me to the biggest problem with Markdown: **John Gruber**.


I don’t mean this as a personal criticism. John’s a [fantastic writer](http://daringfireball.net/) and Markdown has a (mostly) solid specification, with a strong vision statement. But the fact that there has been no improvement whatsoever to the specification or reference implementation for *five years* is... kind of a problem.


There are some **fairly severe bugs** in that now-ancient 2004 Markdown 1.0.1 Perl implementation. Bugs that John has already fixed in eight 1.0.2 betas that have somehow never seen the light of day. Sure, if you know the right Google incantations you can dig up the [unreleased 1.0.2b8 archive](http://six.pairlist.net/pipermail/markdown-discuss/2007-May/000615.html), surreptitiously posted May 2007, and start prying out the bugfixes by hand. That’s what I’ve had to do to fix bugs in our [open sourced C# Markdown implementation](http://blog.stackoverflow.com/2009/12/introducing-markdownsharp/), which was naturally based on that fateful (and technically *only*) 1.0.1 release.


I’d also expect a reference implementation to come with some **basic test suites or sample input/output files** so I can tell if I’ve implemented it correctly. No such luck; the official archives from Gruber’s site include the naked Perl file along with a readme and license. The word “test” does not appear in either. I had to do a ton more searching to finally [dig up MDTest 1.1](http://six.pairlist.net/pipermail/markdown-discuss/2009-February/001526.html). I can’t quite tell where the tests came from, but they seem to be maintained by Michel Fortin, the author of the [primary PHP Markdown implementation](http://michelf.com/projects/php-markdown/).


But John Gruber *created* Markdown. He came up with the concept and the initial implementation. He is, in every sense of the word, **the parent of Markdown**. It’s his baby.


![](https://blog.codinghorror.com/content/images/2025/04/image-455.png)


As Markdown’s “parent,” John has a few key responsibilities in shepherding his baby to maturity. Namely, to lead. To set direction. Beyond that initial 2004 push, he’s done precious little of either. **John is running this particular open source project the way Steve Jobs runs Apple – by sheer force of individual ego.** And that sucks.


Since then, all I can find is sporadic activity on obscure mailing lists and a bit of [passive-aggressive interaction with the community](http://six.pairlist.net/pipermail/markdown-discuss/2008-March/001173.html).

kg-card-begin: html

> On 15 Mar 2008, at 02:55, John Gruber wrote:
> *I despise what you’ve done with Text::Markdown, which is to more or less make it an alias for MultiMarkdown, almost every part of which I disagree with in terms of syntax additions.*
> Wow, that’s pretty strong language. I’m glad I’m provoking strong opinions, and it’s nice to see you actively contributing to Markdown’s direction ;)
> Personally, I don’t actually like (or use) the MultiMarkdown extensions. As noted several times on list, I *do not* consider what I’ve done to in any way be a good solution technically / internally in it’s current form, and as such Markdown.pl is still a better ‘reference’ implementation.
> However I find it somewhat ironic that you can criticise an active effort to actually move Markdown forwards (who’s current flaws have been publicly acknowledged), when it passes more of your test suite than your effort does, and when you haven’t even been bothered to update your own website about the project since 2004, despite having updated the code which can be found on your site (if you dig) much more recently than this.
> I despise copy-pasted code, and forks for no (real) reason - seeing *another two* dead copies of the same code on CPAN made me sad, and so I’ve done *something* to take the situation forwards. **Maybe if you’d put the effort into maintaining a community and taking Markdown.pl forwards at any time within the last 4 years, you wouldn’t be in a situation where people have taken ‘your baby’ and perverted it to a point that you despise.** If starting with Markdown.pl and going forwards with that *had been an option*, then that would have been my preferred route - but I didn’t see any value in producing what would have been a fifth perl Markdown implementation.

kg-card-end: html

It’s almost at the point where John Gruber, the very person who brought us Markdown, is the biggest obstacle preventing Markdown from moving forward and maturing. It saddens me greatly to see such negligent open source code parenting. Why work against the community when you can work with it? It doesn’t have to be this way. And it shouldn’t be.


I think the most fundamental problem with Markdown, in retrospect, is that the official home of the project is **a static set of web pages on John’s site**. Gruber could have hosted the Markdown project in a way that’s more amenable to open source collaboration than a bunch of static HTML. I’m pretty sure SourceForge was around in late 2004, and there are lots of options for proper open source project hosting today – GitHub, Google Code, CodePlex, and so forth. What’s stopping him from setting up shop on any of those sites with Markdown, right now, today? Markdown is Gruber’s baby, without a doubt, but it’s also bigger than any one person. It’s open source. It belongs to the community, too.


Right now we have the worst of both worlds. Lack of leadership from the top, and a bunch of fragmented, poorly coordinated community efforts to advance Markdown, *none* of which are officially canon. This isn’t merely inconvenient for anyone trying to find accurate information about Markdown; it’s actually harming the project’s future. **Maybe it’s true that you can’t kill an open source project, but bad parenting is surely enough to cause it to grow up stunted and maybe even a little maladjusted.**


I mean no disrespect. I wouldn’t bring this up if I didn’t care, if I didn’t think the project and John Gruber were both eminently worthy. Markdown is a small but important part of the open source fabric of the web, and the project deserves better stewardship. While the community can do a lot with the (many) open source orphan code babies out there, they have a much, much brighter future when their parents take responsibility for them.

[markdown](https://blog.codinghorror.com/tag/markdown/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[markup languages](https://blog.codinghorror.com/tag/markup-languages/)
[john gruber](https://blog.codinghorror.com/tag/john-gruber/)
[plain text](https://blog.codinghorror.com/tag/plain-text/)
