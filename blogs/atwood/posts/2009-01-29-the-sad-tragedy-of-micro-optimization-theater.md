---
title: "The Sad Tragedy of Micro-Optimization Theater"
date: 2009-01-29
url: https://blog.codinghorror.com/the-sad-tragedy-of-micro-optimization-theater/
slug: the-sad-tragedy-of-micro-optimization-theater
word_count: 1144
---

I’ll just come right out and say it: [I love strings](https://blog.codinghorror.com/i-heart-strings/). As far as I’m concerned, there isn’t a problem that I can’t solve with a string and [perhaps a regular expression or two](https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/). But maybe that’s just my [lack of math skills](http://steve-yegge.blogspot.com/2006/03/math-for-programmers.html) talking.


In all seriousness, though, the type of programming we do on [Stack Overflow](http://stackoverflow.com/) is intimately tied to strings. We’re constantly building them, merging them, processing them, or dumping them out to a HTTP stream. Sometimes I even give them relaxing massages. Now, if you’ve worked with strings at all, you know that this is code you desperately want to avoid writing:

kg-card-begin: html

```

static string Shlemiel()
{
string result = "";
for (int i = 0; i < 314159; i++)
{
result += getStringData(i);
}
return result;
}

```

kg-card-end: html

In most garbage collected languages, strings are immutable: when you add two strings, the contents of both are copied. As you keep adding to `result` in this loop, more and more memory is allocated each time. This leads directly to [awful quadradic n2 performance](https://web.archive.org/web/20090202095136/http://www.yafla.com/dforbes/String_Concatenation_and_Immutable_Strings_Speeding_Spidermonkey/), or as Joel likes to call it, [Shlemiel the painter performance](http://www.joelonsoftware.com/articles/fog0000000319.html).


> Who is Shlemiel? He’s the guy in this joke:
> Shlemiel gets a job as a street painter, painting the dotted lines down the middle of the road. On the first day he takes a can of paint out to the road and finishes 300 yards of the road. “That’s pretty good!” says his boss, “you’re a fast worker!” and pays him a kopeck.
> The next day Shlemiel only gets 150 yards done. “Well, that’s not nearly as good as yesterday, but you’re still a fast worker. 150 yards is respectable,” and pays him a kopeck.
> The next day Shlemiel paints 30 yards of the road. “Only 30!” shouts his boss. “That’s unacceptable! On the first day you did ten times that much work! What’s going on?”
> “I can’t help it,” says Shlemiel. “Every day I get farther and farther away from the paint can!”


This is a softball question. You all knew that. ***Every* decent programmer knows that string concatenation, while fine in small doses, is deadly poison in loops.**


But what if you’re doing nothing but small bits of string concatenation, dozens to hundreds of times – as in most web apps? Then you might develop a nagging doubt, as I did, that lots of little Shlemiels could possibly be as bad as onw *giant* Shlemiel.


Let’s say we wanted to build this HTML fragment:

kg-card-begin: html

```

<div class="user-action-time">stuff</div>
<div class="user-gravatar32">stuff</div>
<div class="user-details">stuff<br/>stuff</div>

```

kg-card-end: html

Which might appear on a given Stack Overflow page anywhere from one to sixty times. And we’re serving up hundreds of thousands of these pages per day.


Not so clear-cut, now, is it?


So, which of these methods of forming the above string do you think is fastest over a hundred thousand iterations?


**1: Simple Concatenation**

kg-card-begin: html

```

string s =
@"<div class=""user-action-time"">" + st() + st() + @"</div>
<div class=""user-gravatar32"">" + st() + @"</div>
<div class=""user-details"">" + st() + "<br/>" + st() + "</div>";
return s;

```

kg-card-end: html

**2: String.Format**

kg-card-begin: html

```

string s =
@"<div class=""user-action-time"">{0}{1}</div>
<div class=""user-gravatar32"">{2}</div>
<div class=""user-details"">{3}<br/>{4}</div>";
return String.Format(s, st(), st(), st(), st(), st());

```

kg-card-end: html

**3: string.Concat**

kg-card-begin: html

```

string s =
string.Concat(@"<div class=""user-action-time"">", st(), st(),
@"</div><div class=""user-gravatar32"">", st(),
@"</div><div class=""user-details"">", st(), "<br/>",
st(), "</div>");
return s;

```

kg-card-end: html

**4: String.Replace**

kg-card-begin: html

```

string s =
@"<div class=""user-action-time"">{s1}{s2}</div>
<div class=""user-gravatar32"">{s3}</div>
<div class=""user-details"">{s4}<br/>{s5}</div>";
s = s.Replace("{s1}", st()).Replace("{s2}", st()).
Replace("{s3}", st()).Replace("{s4}", st()).
Replace("{s5}", st());
return s;

```

kg-card-end: html

**5: StringBuilder**

kg-card-begin: html

```

var sb = new StringBuilder(256);
sb.Append(@"<div class=""user-action-time"">");
sb.Append(st());
sb.Append(st());
sb.Append(@"</div><div class=""user-gravatar32"">");
sb.Append(st());
sb.Append(@"</div><div class=""user-details"">");
sb.Append(st());
sb.Append("<br/>");
sb.Append(st());
sb.Append("</div>");
return sb.ToString();

```

kg-card-end: html

Take your itchy little trigger finger off that compile key and *think* about this for a minute. Which one of these methods will be faster?


Got an answer? Great!


And... drumroll please... the correct answer:


# It. Just. Doesn’t. Matter!


We already know none of these operations will be performed in a loop, so we can rule out brutally poor performance characteristics of naïve string concatenation. All that’s left is micro-optimization, and the minute you begin worrying about tiny little optimizations, you’ve already [gone down the wrong path](https://blog.codinghorror.com/micro-optimization-and-meatballs/).


Oh, you don’t believe me? Sadly, I didn’t believe it myself, which is why I got drawn into this in the first place. Here are my results – for 100,000 iterations, on a dual core 3.5 GHz Core 2 Duo.

kg-card-begin: html


| **1: Simple Concatenation** | 606 ms |
| **2: String.Format** | 665 ms |
| **3: string.Concat** | 587 ms |
| **4: String.Replace** | 979 ms |
| **5: StringBuilder** | 588 ms |


kg-card-end: html

Even if we went from the *worst* performing technique to the best one, we would have saved a lousy 391 milliseconds over a hundred thousand iterations. Not the sort of thing that I’d throw a victory party over. I guess I figured out that using `.Replace` is best avoided, but even that has some readability benefits that might outweigh the miniscule cost.


Now, you might very well ask which of these techniques has the lowest **memory usage**, [as Rico Mariani did](https://web.archive.org/web/20090216085259/http://blogs.msdn.com/ricom/archive/2004/03/12/88715.aspx). I didn’t get a chance to run these against `CLRProfiler` to see if there was a clear winner in that regard. It’s a valid point, but I doubt the results would change much. In my experience, techniques that abuse memory also tend to take a lot of clock time. Memory allocations are fast on modern PCs, but they’re far from free.


Opinions vary on just [how many strings](https://web.archive.org/web/20090202180754/http://blog.briandicroce.com/2008/02/04/stringbuilder-vs-string-performance-in-net/) you have to concatenate before you should start worrying about performance. The general consensus is **around 10**. But you’ll also read crazy stuff, like this:


> **Don’t use += concatenating ever.** Too many changes are taking place behind the scene, which aren’t obvious from my code in the first place. I advise you to use String.Concat() explicitly with any overload (2 strings, 3 strings, string array). This will clearly show what your code does without any surprises, while allowing yourself to keep a check on the efficiency.


Never? Ever? Never ever ever? Not even once? Not even if *it doesn’t matter?* Any time you see “don’t ever do X,” alarm bells should be going off. Like they hopefully are right now.


Yes, you should avoid the obvious beginner mistakes of string concatenation, the stuff every programmer learns their first year on the job. But after that, you should be more worried about the maintainability and readability of your code than its performance. And that is perhaps the most tragic thing about letting yourself get sucked into micro-optimization theater – **it distracts you from your real goal: writing better code.**

[strings](https://blog.codinghorror.com/tag/strings/)
[programming](https://blog.codinghorror.com/tag/programming/)
[optimization](https://blog.codinghorror.com/tag/optimization/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[performance](https://blog.codinghorror.com/tag/performance/)
