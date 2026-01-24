---
title: "You’re Reading The World’s Most Dangerous Programming Blog"
date: 2008-10-23
url: https://blog.codinghorror.com/youre-reading-the-worlds-most-dangerous-programming-blog/
slug: youre-reading-the-worlds-most-dangerous-programming-blog
word_count: 1065
---

Have you ever noticed that **blogs are full of misinformation and lies?** In particular, I’m referring to *this* blog. The one you’re reading right now. For example, [yesterday’s post](https://blog.codinghorror.com/the-one-thing-every-software-engineer-should-know/) was so bad that it is conclusive proof that [I’ve jumped the shark](http://www.reddit.com/r/programming/comments/78vq3/jeff_atwood_finally_jumps_the_shark/).


Again.


Apparently, according to one Reddit commenter, the information presented here is downright *dangerous*:


> **Jeff Atwood has always held the distinction of having the most dangerous programming blog**, in that some young or aspiring developers may actually listen to some of his “advice,” but now he’s somehow managed to snag the achievement of having the most inane programming blog as well.
> To put it in more frank terms Jeff: What you’ve just written is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having read this post. I award you no points, and may God have mercy on your soul.


I enjoyed the [Billy Madison](http://www.imdb.com/title/tt0112508/) quote, but I’m not sure my blog has earned that particular distinction yet. If *this* blog is the most dangerous content that young, inexperienced developers have ever read then, well, I’d have to seriously question whether or not they’ve ever actually used this thing we call the “world wide web.”


Allow me to illustrate with an example.


Today I happened across this [blog entry from Mads Kristensen](https://web.archive.org/web/20081217065645/http://blog.madskristensen.dk/post/Compression-and-performance-GZip-vs-Deflate.aspx). In it, Mads explains that [Deflate](http://en.wikipedia.org/wiki/DEFLATE) is faster than [GZip](http://en.wikipedia.org/wiki/Gzip).


> First I tested the `GZipStream` and then the `DeflateStream`. I expected a minor difference because the two compression methods are different, but the result astonished me. **I measured the DeflateStream to be 41% faster than GZip**. That’s a very big difference. With this knowledge, I’ll have to change the HTTP compression module to choose Deflate over GZip.


This was a surprising result to me, because the two compression algorithms are very closely related. On the other hand, we use GZip extensively and heavily to cache HTML fragment output strings on the Stack Overflow server, [as Scott Hanselman explains](http://www.hanselman.com/blog/TheWeeklySourceCode35ZipCompressingASPNETSessionAndCacheState.aspx). If Deflate really is that much faster, we need to switch to it!


But, like any veteran internet user, I never take what I read on a blog – or any other site on the internet, for that matter – as fact. Rather, it’s a germ of an intriguing idea, a call to action. I fired up my IDE and built a small test harness to test for myself: **is `Deflate` faster than `GZip`?**

kg-card-begin: html

```

public static class StopwatchExtensions
{
public static long Time(this Stopwatch sw, Action action, int iterations)
{
sw.Reset();
sw.Start();
for (int i = 0; i < iterations; i++) { action(); }
sw.Stop();
return sw.ElapsedMilliseconds;
}
}
class Program
{
static void Main(string[] args)
{
string s = File.ReadAllText(@“c:test.html”);
byte[] b;
var sw = new Stopwatch();
b = CompressGzip(s);
Console.WriteLine(“gzip size: ” + b.Length);
Console.WriteLine(sw.Time(() => CompressGzip(s), 1000));
Console.WriteLine(sw.Time(() => DecompressGzip(b), 1000));
b = CompressDeflate(s);
Console.WriteLine(“deflate size: ” + b.Length);
Console.WriteLine(sw.Time(() => CompressDeflate(s), 1000));
Console.WriteLine(sw.Time(() => DecompressDeflate(b), 1000));
}
}

```

kg-card-end: html

The results were surprising: on my box, **GZip is just as fast as Deflate.** For giant strings, for medium strings, for small strings. In every possible testing combination I can think of, Deflate is nowhere near 40% faster.

kg-card-begin: html

```

gzip size: 3125
242
171
deflate size: 3107
225
149

```

kg-card-end: html

That’s not exactly what Mads’ blog entry tells me should happen. Do I think Mads is an idiot for posting this? Well, no. I don’t.

- The original blog entry was posted in late 2006; since then new versions of the .NET framework have shipped and hardware has gotten faster. Perhaps there was some significant change in either that produces this different outcome.
- My test is a bit different than Mads’ testing. I use a random HTML file as the compression target; I can’t tell exactly what he’s compressing in his benchmark. I also tried with small, medium, and large strings. The tests are similar, but they’re not the same.


Is this the type of dangerous misinformation that blogs are vilified for? Should I be angry at Mads for posting this? Not at all. I learned a bit more about Deflate and GZip. It provided an opportunity for me to refactor my compression code some. I even learned how to [benchmark using lambda syntax](http://stackoverflow.com/questions/232848/wrapping-stopwatch-timing-with-a-delegate-or-lambda). If I hadn’t read this post, if it hadn’t provided that impetus of an idea for me to ponder, I wouldn’t have bothered.


I am a better programmer for having read that blog post. Even though, near as I can tell, it’s offering inaccurate advice.

kg-card-begin: html

Update: I got a bit more curious about this, so I ran some more tests on different machines. Here are the results, in milliseconds, for a thousand runs each using the Google homepage HTML as the target (it’s about 7 Kb):

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/04/image-209.png)


How much faster *is* Deflate than GZip?

kg-card-begin: html


|  | Core 2 Duo
3.5 Ghz | Core 2 Quad
1.86 Ghz | Athlon X2
2.1 Ghz |
| Compress | 8% faster | 8% faster | 50% faster |
| Decompress | 15% faster | 17% faster | 37% faster |


kg-card-end: html

There’s the 40% Mads was talking about. That is a little shocking when you consider that GZip is simply Deflate plus a checksum and header/footer! (You can download the source code for this test and try it yourself.)


So my point – and I do have one – is this: **when you say that the information presented on a blog is “dangerous,” you’re implying the audience is too dumb or inept to read critically**.


I, for one, have too much respect for my audience to ever do that. I am continually humbled by the quality of the comments and discussion on the blog entries I post. In fact, I’d say that has been the single most surprising thing I’ve learned in my four plus years of blogging: **the best content always begins where the blog post ends.** My audience is far, far smarter than I will ever be.


On second thought, maybe what I promote on this blog *is* dangerous: **thinking for yourself**.


But I’m pretty confident you can handle that.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[security](https://blog.codinghorror.com/tag/security/)
