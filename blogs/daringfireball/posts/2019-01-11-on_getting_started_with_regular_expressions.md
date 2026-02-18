---
title: "On Getting Started With Regular Expressions"
date: 2019-01-11
url: https://daringfireball.net/2019/01/on_getting_started_with_regular_expressions
slug: on_getting_started_with_regular_expressions
word_count: 783
---


Dr. Drang, regarding [Jason Snell’s tale](https://sixcolors.com/post/2019/01/using-bbedit-and-excel-to-revive-a-dead-podcast-feed/) of using BBEdit and Excel to create a working RSS feed for an old podcast, “[Don’t Fear the Regex](https://leancrew.com/all-this/2019/01/dont-fear-the-regex/)”:


> Although I do often write short programs for text munging, I
> typically resort to that only if the problem requires more than
> just large-scale text editing or if I expect to be repeating the
> process several times. And even then, I usually start out by
> playing around in BBEdit to see what searches, replacements, and
> rearrangements need to be done. It’s a convenient environment for
> getting immediate feedback on each transformation step.
> (And if you expect to do a series of text transformations often
> and really don’t want to get into writing scripts in Perl or
> Python or Ruby or whatever, BBEdit’s Text Factories allow you to
> string together any number of individual munging steps.)


After [I linked](https://daringfireball.net/linked/2019/01/09/bbedit-excel-podcast-feed) to [Snell’s piece](https://sixcolors.com/post/2019/01/using-bbedit-and-excel-to-revive-a-dead-podcast-feed/), a reader emailed to ask why I didn’t think this would’ve been better solved by writing a script in Perl/Python/Ruby or any other language with good regex support. Why use Excel for date transformations when scripting languages all have extensive date libraries?


What Drang describes above is my process too. If the task at hand is something I only need to do once or twice, right now, it’s simply easier to just do it in BBEdit. I’m only going to make a proper script if it’s something I know or suspect I’ll reuse. But even when I *do* write a script to automate some sort of text munging, it inevitably starts with me working out the regex transformations step-by-step in BBEdit. Instant visual feedback with undo support — I’ve worked with text this way since 1992.


Drang:


> Even worse, people who are thinking they should start using
> regular expressions often hear about [this great book](http://www.amazon.com/dp/B007I8S1X0/?tag=andnowitsa085-20) on the
> topic and have a natural reaction when they see it: *A 500+ page
> book to learn how to search for text? No thanks.*
> This is too bad, because while Friedl’s book is great, it’s called
> *Mastering Regular Expressions* for a reason, and that reason is not
> because it’s a tutorial. My recommendation for a tutorial is the
> one I learned from over 20 years ago: the “Searching with Grep”
> chapter in the [BBEdit User Manual](https://s3.amazonaws.com/BBSW-download/BBEdit_12.5.2_User_Manual.pdf#page182). I believe it was largely
> written by a young guy named John Gruber.


As for the Grep chapter in BBEdit’s user manual — I did write a significant part of it, but I can’t take and shouldn’t get credit for all of it. Long story short, until [BBEdit 6.5](https://web.archive.org/web/20020204160639/http://www.barebones.com:80/products/bbedit/new_in_bbedit.html), BBEdit used a rather basic regex engine. If I recall correctly, it was a highly customized version of [Henry Spencer’s classic library](https://garyhouston.github.io/regex/), which supported only the classic features of regular expression syntax. I pushed for BBEdit to switch to [Philip Hazel’s excellent PCRE](https://www.pcre.org/) (Perl Compatible Regular Expressions) library, which supports just about every advanced bit of regex syntax anyone could want — and it’s fast, supports Unicode, written in good clean cross-platform C, and more.


The Grep chapter in BBEdit’s user manual was already very good when I started working at Bare Bones — the entire manual, cover-to-cover, has always been and remains genuinely excellent. In fact, like Drang, I learned regular expressions by reading BBEdit’s Grep chapter. I went from “this stuff looks like gibberish” to “Oh, I get it, I see how this could be super useful” just by reading that chapter. If you’re regex-curious, I highly recommend that you start by reading that chapter — even if you’re not a BBEdit user. The regex syntax it describes will work in just about every current programming language or text editor. (The manual is available in BBEdit’s Help menu.)


What I contributed to the Grep chapter was all the stuff in PCRE that BBEdit’s old regex engine didn’t support, which, admittedly, is a *lot* of stuff. Prompted by Drang’s kind words, I just re-read the chapter for the first time in a few years, and it holds up. And I’m pretty sure the line about how many licks it takes to get to the center of a Tootsie Pop was mine.1


---

1. Although to be honest, even as a kid I never liked Tootsie Rolls, and so when I had a Tootsie Pop, I’d throw them out when I got to the center. [Blow Pops](http://www.tootsie.com/candy/charms/charms-blow-pops) were more my thing — some good hard bubble gum was a genuine treat to look forward to. ↩︎



| **Previous:** | [Codea’s iOS Menu Bar](https://daringfireball.net/2019/01/codeas_ios_menu_bar) |
| **Next:** | [Pentagram’s ‘Range of Possibilities’ for Slack](https://daringfireball.net/2019/01/pentagram_slack_range_of_possibilities) |


PreviousNext