---
title: "Mastering GUIDs with Occam's Razor"
date: 2005-09-27
url: https://blog.codinghorror.com/mastering-guids-with-occams-razor/
slug: mastering-guids-with-occams-razor
word_count: 684
---

Do you remember the scene from the movie [Full Metal Jacket](http://www.imdb.com/title/tt0093058/) where the marines recite the [USMC creed](http://www.usmcpress.com/heritage/marine_corps_rifleman's_creed.htm)?


![](https://blog.codinghorror.com/content/images/2025/03/image-289.png)


It’s a little known fact, but **programmers have a similar creed**:


> This is my GUID. There are many like it but this one is mine. My GUID is my best friend. It is my life. I must master it as I must master my life. Without me, my GUID is useless. Without my GUID I am useless.


In fact, GUIDs are so near and dear to our hearts that we recently had a spirited discussion about them at work. **Let’s say you had a string and needed to determine whether it was a valid GUID**. The easy way is a .Parse() style Try-Catch code block:

kg-card-begin: html

```
guid g;
try
{
g = new Guid("x");
}
catch
{
}

```

kg-card-end: html

This is the correct answer... *most of the time*. But you know programmers. **They never met an edge condition they didn’t enjoy discussing ad nauseam**. And I was one of the first to chime in:

kg-card-begin: html

> This is definitely a good way to validate a data type, however, just be aware of the exception performance penalty. Throwing exceptions on [failure to cast is expensive](https://blog.codinghorror.com/tryparse-and-the-exception-tax/), so if this is something that
> will be invalid often
> appears in a loop
> occurs with high frequency
> then you’d want to go with a non-exception based check. However most of the time none of these things are true, so the performance is irrelevant.

kg-card-end: html

Then someone suggested trying a regular expression. Oh great, [now we have two problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/):

kg-card-begin: html

```
Regex r = new Regex(
"^((?-i:0x)?[A-Fa-f0-9]{32}|
[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}|
{[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}})$");

```

kg-card-end: html

It’s valid, but I couldn’t resist tweaking this regex for simplicity’s sake. The [official GUID spec](http://www.ics.uci.edu/~ejw/authoring/uuid-guid/draft-leach-uuids-guids-01.txt) only defines one format for GUID strings, the familiar 8-4-4-4-12 format:

kg-card-begin: html

```
Regex r = new Regex(
@"^({|()?[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}(}|))?$");

```

kg-card-end: html

This is my post, so I’ll skip the part where others poked holes in my regex. Just when we thought it was over, a fellow developer whipped out a code snippet that benchmarks how long it takes to validate GUIDs via each method:

kg-card-begin: html

```
static void Main(string[] args)
{
Guid g = Guid.NewGuid();
string s = g.ToString();
DateTime before = DateTime.Now;
for (int i = 0; i < 10000; i++)
{
bool retVal = IsGuid(s);
}
Console.WriteLine(DateTime.Now.Subtract(before));
before = DateTime.Now;
for (int i = 0; i < 10000; i++)
{
bool retVal = IsGuid2(s);
}
Console.WriteLine(DateTime.Now.Subtract(before));
Console.ReadLine();
}
public static bool IsGuid(string guidString)
{
try
{
Guid guid = new Guid(guidString);
return true;
}
catch
{
return false;
}
}
public static bool IsGuid2(string guidString)
{
Regex r;
r = new Regex(
@"^({|()?[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}(}|))?$");
Match m = r.Match(guidString);
if (m.Success)
return true;
else
return false;
}

```

kg-card-end: html

According to this, **constructor validation is 3 to 4 times faster than the regex**... or is it? I immediately noticed a few problems that made this a rather questionable benchmark. And, as before, I couldn’t resist investigating:

kg-card-begin: html

> If I increase the iterations to **100,000**:
> 00.1874856
> 00.7968138
> You typically wouldn't want to create a new regex inside the loop, because it's too expensive. If I **move the regex creation outside the loop**:
> 00.2031094
> 00.5780806
> If I set **RegexOptions.Compiled** on the regex:
> 00.1874856
> 00.3437236
> If I run the above with CTRL+F5 (**sans debugger**):
> 00.1718673
> 00.1874916

kg-card-end: html

It was definitely a fun discussion. I certainly [learned a few things](https://web.archive.org/web/20080915052122/http://msdn.microsoft.com/en-us/library/aa446557.aspx) about GUIDs I didn’t know. Heck, discussions like this are why I joined a software development company in the first place. **But it’s also a pointless discussion.**


Performance was a complete non-issue in this particular scenario. That’s why we should always program with [Occam’s Razor](http://en.wikipedia.org/wiki/Occam's_Razor) in mind:


> Given two similar code paths, choose the simpler one.


Edge conditions and fancy techniques are interesting, but they’re not necessarily a worthwhile use of time. **Sometimes the simple and stupid solution is all you need.**

[guids](https://blog.codinghorror.com/tag/guids/)
[programming](https://blog.codinghorror.com/tag/programming/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
