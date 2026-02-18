---
title: "Markdown Licensing"
date: 2004-12-17
url: https://daringfireball.net/2004/12/markdown_licensing
slug: markdown_licensing
word_count: 957
---


The other big change with Markdown [1.0.1](https://daringfireball.net/2004/12/markdown_101) is related to
licensing. Markdown 1.0 and earlier were released under the [GPL](http://creativecommons.org/licenses/GPL/2.0/);
starting with version 1.0.1, Markdown is now licensed under a
[less-restrictive BSD-style license](https://daringfireball.net/projects/markdown/license).


If you’re just someone who uses Markdown, this licensing change makes
little difference from your perspective. Markdown is still available
free of charge (more on this in a bit, though).


(If you’re *not* using Markdown, but might be interested, I encourage
you to take a look as some example Markdown syntax. It’s the best way
to “get” what it is that Markdown does. You can see my Markdown source
for any Daring Fireball article by adding a ‘.text’ suffix to the URL
of any article. E.g., to see the original Markdown source for *this*
article, [look here](https://daringfireball.net/2004/12/markdown_licensing.text). I’ll explain how this trick works some other
day.)


However, if you’re a developer who wishes to use Markdown as part of
or in conjunction with your own project or app, my switching to the
BSD should make this significantly easier — especially for other open
source projects that are themselves licensed under BSD-style licenses.


Licensing discussions make me sleepy, so I’ll try to keep this short.


In a nut, the reason I originally chose the GPL for Markdown was that
I had the vague, poorly-thought-out notion that Markdown could be
available freely to users who simply wanted to use it, and to
developers writing other open source projects. And that business
users and developers writing non-open source projects who wanted to
include Markdown might be willing to pay me some sort of reasonable
fee to license Markdown under something other than the GPL.


That was just a notion, though. And in practice, using the GPL
didn’t help with two of my goals:

- Developers creating open source projects licensed under the BSD
(or similar) felt like they couldn’t include Markdown under the
GPL. That’s not what I want — I want other open source developers
to feel free to use Markdown in their systems.
- No commercial developers or business users volunteered to pay any
license fees anyway.


Even stranger, I happily granted permission to indie Mac developers
like Adriaan Tijsseling and Brent Simmons to include copies of
Markdown in their weblog editing apps, [Ecto](http://ecto.kung-foo.tv/) and [MarsEdit](http://ranchero.com/marsedit/).


The reason I was happy to do this, even though their apps aren’t free,
is that it’s obvious that it’s the way it ought to be. Among Markdown
users who use desktop weblog editors like Ecto and MarsEdit, there’s
strong demand for “previewing” Markdown-formatted entries before
publishing them to their weblogs. But due to the nature of current
desktop weblog editing APIs, the only way for these apps to provide
this feature is for the software to run a copy of Markdown locally.


But the irony of this is that non-open-source software like Ecto and
MarsEdit are including Markdown for free, but the authors of several
BSD-licensed open source projects feel they can’t include Markdown, on
the grounds that they don’t believe they can include a GPL-licensed
Perl script as part of a BSD-licensed project.


Switching to a BSD-style license makes things easy. If you want to use
it, go ahead and download it, it’s free. If you want to use it as part
of your own programming project, you may do so freely, with the only
provisions being: (a) you must give me credit; and (b) you can’t use
the name “Markdown” without my permission.


This licensing change also applies to [Michel Fortin’s PHP Markdown
port](http://www.michelf.com/projects/php-markdown/), version 1.0.1 of which should be released shortly, and
which will also now be available under a BSD-style license.


As for making a few bucks from my efforts (read: *cashing in on
Markdown’s popularity*), I put a PayPal donation form on the [Markdown
project page](https://daringfireball.net/projects/markdown/). If you enjoy Markdown and feel it’s worth a small
contribution, I’d be delighted. I suspect the main reason people
ignore online tip jars and donation boxes, even for projects they
enjoy, is that they hope “someone else” is chipping in. So, I’ve also
included a running tally of the total amount contributed by everyone.
It should update “live” with each contribution. Can you make money
giving away open source software? We’ll see.


What this means is that *you* get to set the price for Markdown. If you
think it ought to be free, that’s fine, go ahead and use it for free,
no strings attached. But if you think it’s worth $5, or $15, or $25 — you decide what to pay.


(And, even if the total remains pegged at or near $0, I’m not exactly
coming away empty-handed. Because Markdown placed third in [Six Apart’s
Movable Type developer contest](http://www.sixapart.com/log/2004/07/plug_in_to_mova.shtml), I did win a 40 GB iPod and the
Adobe Creative Suite.)


There have been a lot of good feature ideas for Markdown discussed on
the [Markdown-Discuss mailing list](http://six.pairlist.net/mailman/listinfo/markdown-discuss). Among the features I’d like
to add for version 1.1:

- A smarter parsing system for inline block of raw HTML.
- A way to optionally allow Markdown formatting to be processed
within a `<div>` or `<span>` HTML tag. People want this so they
can apply CSS classes and IDs to the parent tags, but still be
able to write the contents in Markdown format.
- Syntax for definition lists.
- Syntax for creating simple tables.
- A way to specify a `cite` attribute for blockquotes.
- When used as the format for weblog comments, it’d be useful to
be able to configure Markdown to strip out any raw HTML tags.


If this donation thing works, I might be able to spend time working on
Markdown 1.1 sooner rather than later.



| **Previous:** | [Markdown 1.0.1](https://daringfireball.net/2004/12/markdown_101) |
| **Next:** | [Software Update Tips and Voodoo](https://daringfireball.net/2004/12/software_update) |


PreviousNext