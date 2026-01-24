---
title: "Regular Expressions: Now You Have Two Problems"
date: 2008-06-27
url: https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/
slug: regular-expressions-now-you-have-two-problems
word_count: 1498
---

I love regular expressions. No, I’m not sure you understand: [I really *love* regular expressions](https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/).


You may find it a little odd that a hack who grew up using a [language with the ain’t keyword](http://stackoverflow.com/questions/2055205/there-is-an-if-else-is-there-a-neither-nor-statement/2055442#2055442) would fall so head over heels in love with something as obtuse and arcane as regular expressions. I’m not sure how that works. But it does. **Regular expressions rock**. They should absolutely be a key part of every modern coder’s toolkit.


If you’ve ever talked about regular expressions with another programmer, you’ve invariably heard this 1997 chestnut:


> Some people, when confronted with a problem, think “I know, I’ll use regular expressions.” Now they have two problems.


The quote is from Jamie Zawinski, a world class hacker who I admire greatly. If he’s telling us not to use regular expressions, should we even bother? Maybe, if you live and die by soundbites. But there’s a bit more to the story than that, as evidenced by Jeffrey Friedl’s exhaustive [research on the Zawinski quote](http://regex.info/blog/2006-09-15/247). Zawinski himself commented on it. Analyzing the full text of Jamie’s posts in the original 1997 thread, we find the following:


> Perl’s nature encourages the use of regular expressions almost to the exclusion of all other techniques; they are far and away the most “obvious” (at least, to people who don’t know any better) way to get from point A to point B.


The first quote is too glib to be taken seriously. But this, I completely agree with. Here’s the point Jamie was trying to make: **not that regular expressions are evil, per se, but that *overuse* of regular expressions is evil.**


I couldn’t agree more. Regular expressions are like a particularly spicy hot sauce – to be used in moderation and with restraint only when appropriate. Should you try to solve every problem you encounter with a regular expression? Well, no. Then you’d be writing [Perl](http://en.wikipedia.org/wiki/Perl), and I’m not sure you need those kind of headaches. If you drench your plate in hot sauce, you’re going to be very, very sorry later.


![](https://blog.codinghorror.com/content/images/2025/03/image-13.png)


In the same way that I can’t imagine food without a dash of hot sauce now and then, I can’t imagine programming without an occasional regular expression. It’d be a bland, unsatisfying experience.


But wait! Let me guess! The last time you had to read a regular expression and figure it out, your head nearly exploded! Why, it wasn’t even code; it was just a bunch of unintelligible [Q*Bert line noise!](https://blog.codinghorror.com/regex-use-vs-regex-abuse/)


Calm down. Take a deep breath. Relax.


Let me be very clear on this point: If you read an incredibly complex, impossible to decipher regular expression in your codebase, **they did it wrong**. If you write regular expressions that are difficult to read into your codebase, ***you* are doing it wrong**.


Look. Writing so that people can understand you is *hard*. I don’t care if it’s code, English, regular expressions, or Klingon. Whatever it is, I can show you an example of someone who has written something that is pretty much indistinguishable from gibberish in it. I can also show you something written in the very same medium that is so beautiful it will make your eyes water. So the argument that regular expressions are somehow fundamentally impossible to write or read, to me, holds no water. Like everything else, it just takes a modicum of skill.


Buck up, soldier. Even Ruby code is hard to read until you learn the symbols and keywords that make up the language. If you can learn to read code in whatever your language of choice is, you can *absolutely* handle reading a few regular expressions. It’s just not that difficult. I won’t bore you with a complete explanation of the dozen or so basic elements of regular expressions; Mike already covered this ground better than I can:

- [The absolute bare minimum every programmer should know about regular expressions](http://web.archive.org/web/20090209182018/http://immike.net/blog/2007/04/06/the-absolute-bare-minimum-every-programmer-should-know-about-regular-expressions/)
- [5 regular expressions every web programmer should know](http://web.archive.org/web/20090318193321/http://immike.net/blog/2007/04/06/5-regular-expressions-every-web-programmer-should-know/)
- [Extreme regex-fu: what you need to know to become a regular expression pro](http://web.archive.org/web/20091217102803/http://immike.net/blog/2007/06/21/extreme-regex-foo-what-you-need-to-know-to-become-a-regular-expression-pro/)


I’d like to illustrate with an actual example, a regular expression I recently wrote to strip out dangerous HTML from input. This is extracted from [the SanitizeHtml routine](https://web.archive.org/web/20110210133151/http://refactormycode.com/codes/333-sanitize-html) I posted on RefactorMyCode.

kg-card-begin: html

```
var whitelist = 
@"</?p>|<brs?/?>|</?b>|</?strong>|</?i>|</?em>|
</?s>|</?strike>|</?blockquote>|</?sub>|</?super>|
</?h(1|2|3)>|</?pre>|<hrs?/?>|</?code>|</?ul>|
</?ol>|</?li>|</a>|<a[^>]+>|<img[^>]+/?>";
```

kg-card-end: html

What do you see here? The variable name whitelist is a strong hint. One thing I like about regular expressions is that they generally look like what they’re matching. You see a list of HTML tags, right? Maybe with and without their closing tags?


Honestly, is this so hard to understand? To me it’s perfectly readable. But we can do better. In most modern regex dialects, you can flip on a mode where whitespace is no longer significant. This frees you up to **use whitespace and comments in your regular expression**, like so.

kg-card-begin: html

```
var whitelist = 
@"</?p>|
&ltbrs?/?>| (?# allow space at end)
</?b>|  
</?strong>|
</?i>|
</?em>|
</?s>|
</?strike>|
</?blockquote>|
</?sub>|
</?super>|
</?h(1|2|3)>| (?# h1,h2,h3)
</?pre>|
<hrs?/?>|  (?# allow space at end)
</?code>|
</?ul>|
</?ol>|
</?li>|
</a>|
<a[^>]+>|  (?# allow attribs)
<img[^>]+/?> (?# allow attribs)
";
```

kg-card-end: html

Do you understand it now? All I did was add a smattering of comments and a lot of whitespace. The same exact technique I would use on any code, really.


But how did I cook up this regular expression? How do I know it does what I think it does? How do I test it? Well, again, I do that the same way I do with all my other code: I use a tool. My tool of choice is [RegexBuddy](http://www.regexbuddy.com/cgi-bin/affref.pl).


![](https://blog.codinghorror.com/content/images/2025/03/image-15.png)


Now we get **syntax highlighting** and, more importantly, **real time display of matches** there at the bottom in our test data as we type. This is huge. If you’re wondering why your IDE doesn’t automatically do this for you with any regex strings it detects in your code, tell me about it. I’ve been wondering that very same thing for years.


RegexBuddy is far and away the best regex tool on the market in my estimation. Nothing else even comes close. But it does cost money. If [you don’t use software that costs money](https://blog.codinghorror.com/we-dont-use-software-that-costs-money-here/), there are plenty of [alternatives](http://regexpal.com/) out there. You wouldn’t read or write code in notepad, right? Then why in the world would you attempt to read or write regular expressions that way? Before you complain how hard regular expressions are to deal with, **get the right tools!**


This trouble is worth it, because regular expressions are incredibly powerful and succinct. How powerful? I was able to write a no-nonsense, special purpose HTML sanitizer in about 25 lines of code and four regular expressions. Compare that with a general purpose HTML sanitizer which would take hundreds if not *thousands* of lines of procedural code to do the same thing.


I do have some tips for keeping your sanity while dealing with regular expressions, however:

1. **Do not try to do everything in one uber-regex.** I know you *can* do it that way, but you’re not going to. It’s not worth it. Break the operation down into several smaller, more understandable regular expressions, and apply each in turn. Nobody will be able to understand or debug that monster 20-line regex, but they might just have a fighting chance at understanding and debugging five mini regexes.
2. **Use whitespace and comments.** It isn’t 1997 any more. A tiny ultra-condensed regex is no longer a virtue. Flip on the `IgnorePatternWhitespace` option, then use that whitespace to make your regex easier for us human beings to parse and understand. Comment liberally.
3. **Get a regular expression tool.** I don’t stare at regular expressions and try to suss out their meaning through sheer force of will. Neither should you. It’s a waste of time. I paste them into my regex tool of choice, RegexBuddy, which not only tells me what the regular expression does, but lets me step through it, and run it through some test data. All in real time as I type.
4. **Regular expressions are not Parsers.** Although you can do some amazing things with regular expressions, they are weak at balanced tag matching. Some regex variants [have balanced matching](https://learn.microsoft.com/en-us/archive/blogs/bclteam/net-regular-expressions-regex-and-balanced-matching-ryan-byington), but it is clearly a hack – and a nasty one. You can often make it kinda-sorta work, as I have in the sanitize routine. But no matter how clever your regex, don’t delude yourself: it is in no way, shape or form a substitute for a real live parser.


If you’re afraid of regular expressions, don’t be. Start small. Used responsibly and with the right tooling they are big, powerful – dare I say, *spicy* – wins. If you make regular expressions a part of your toolkit, you’ll be able to write less code that does more. It’ll just... taste batter.


You might enjoy them so much, in fact, that you completely forget about that “second problem.”

[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
