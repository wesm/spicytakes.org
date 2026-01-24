---
title: "Java vs. .NET RegEx performance"
date: 2004-08-28
url: https://blog.codinghorror.com/java-vs-net-regex-performance/
slug: java-vs-net-regex-performance
word_count: 898
---

I was intrigued when I saw a cryptic reference to “the lackluster RegEx performance in .NET 1.1” on [Don Park’s blog](https://web.archive.org/web/20060105064414/http://www.docuverse.com/blog/donpark/EntryViewPage.aspx?guid=347c93ab-96eb-45fa-84c1-04d795b94292). Don referred me to [this page](https://web.archive.org/web/20040709201923/http://www.manageability.org/blog/archive/20030210%23p_i_found_a_a/document_view), which displays some really crazy benchmark results from [a Java regex test class](https://web.archive.org/web/20040804052701/http://tusker.org/regex/regex_benchmark.html) – **calling C#’s regex support “20 times slower than [Java].”** First of all, them’s fightin’ words, and second, those results are just too crazy to really make sense. Why would C# be over an order of magnitude slower than Java at a classic computer science problem like a regular expression parser? I don’t believe it.


So I downloaded the Java JDK, a [freeware Java development environment](https://web.archive.org/web/20040719080036/http://www.jcreator.com/download.htm), and I ran that benchmark class on my own machine:

kg-card-begin: html

```
Regular expression library: java.util.regex.Pattern
RE: ^(([^:]+)://)?([^:/]+)(:([0-9]+))?(/.*)
MS    MAX     AVG     MIN     DEV     INPUT
46    16      0.0046  0       0       'http://www.linux.com/'
61    16      0.0061  0       0       'http://www.thelinuxshow.com/main.php3'
61    16      0.0061  0       0       'usd 1234.00'
172   16      0.0172  0       0       'he said she said he said no'
RE: usd [+-]?[0-9]+.[0-9][0-9]
MS    MAX     AVG     MIN     DEV     INPUT
0     0       0.0     0       0       'http://www.linux.com/'
15    15      0.0015  0       0       'http://www.thelinuxshow.com/main.php3'
15    15      0.0015  0       0       'usd 1234.00'
15    15      0.0015  0       0       'he said she said he said no'
RE: b(w+)(s+1)+b
MS    MAX     AVG     MIN     DEV     INPUT
0     0       0.0     0       0       'http://www.linux.com/'
31    16      0.0031  0       0       'http://www.thelinuxshow.com/main.php3'
31    16      0.0031  0       0       'usd 1234.00'
47    16      0.0047  0       0       'he said she said he said no'
Total time taken: 266
```

kg-card-end: html

Note that I only ran this for the “built in” Java regex library **java.util.regex.Pattern**; the benchmark has template code for dozens of alternative regex parsers. I snipped that code out for simplicity. The standard Java regex class performs very well according to the results shown on the referring page.


I then converted the sample code to VB.NET, and got these results:

kg-card-begin: html

```
Regular expression library: System.Text.RegularExpressions
RE: ^(([^:]+)://)?([^:/]+)(:([0-9]+))?(/.*)
MS    MAX     AVG     MIN     DEV     INPUT
32    3.033   0.0032  0.0025  0.0325  'http://www.linux.com/'
63    3.04    0.0063  0.0053  0.0325  'http://www.thelinuxshow.com/main.php3'
122   3.053   0.0122  0.0109  0.0327  'usd 1234.00'
234   3.067   0.0234  0.0212  0.0328  'he said she said he said no'
RE: usd [+-]?[0-9]+.[0-9][0-9]
MS    MAX     AVG     MIN     DEV     INPUT
20    0.729   0.002   0.0017  0.0073  'http://www.linux.com/'
40    0.732   0.004   0.0036  0.0073  'http://www.thelinuxshow.com/main.php3'
63    1.748   0.0063  0.0056  0.0175  'usd 1234.00'
82    1.751   0.0082  0.0075  0.0175  'he said she said he said no'
RE: b(w+)(s+1)+b
MS    MAX     AVG     MIN     DEV     INPUT
19    0.25    0.0019  0.0017  0.0037  'http://www.linux.com/'
38    0.252   0.0038  0.0034  0.0038  'http://www.thelinuxshow.com/main.php3'
62    4.961   0.0062  0.0053  0.0497  'usd 1234.00'
81    4.963   0.0081  0.007   0.0497  'he said she said he said no'
Total time taken: 170
```

kg-card-end: html

So... yeah. I don’t know what kind of crack the guys at manageability.org are smoking, but I can’t seem to find a local vendor.


You may be interested in my [VS.NET 2003 console solution](https://web.archive.org/web/20060208063203/http://www.codinghorror.com/files/code/regexbenchmark.zip) which includes both the stripped down java class and the VB.NET equivalent, so you can run this test on your own machine. A few notes on the test:

- My PC is an Athlon FX-53 (3800+), although the relative scores are all that matter. Just for fun, I’ll try both versions on a few other boxes I have here, and post the results in the comments.
- No optimizations were enabled for either the Java or .NET solutions.
- Console apps were executed directly without a debugger. Having a debugger running will double your runtime. I check for this in the .NET version and display a warning if you have the debugger attached.
- The timing code is a little different between the Java and .NET versions. The .NET conversion uses the **QueryPerformanceCounter** windows API call to get accurate sub-millisecond timing. One side effect of this is that I have to make two passes to get all the benchmark results: the first pass times each of the 120,000 regex calls individually into an array, and the second pass times just the total execution time. You’ll notice that the first pass takes twice as long; that’s due to the overhead of calling QueryPerformanceCounter 120,000 times. The upside is that I provide far more accurate timing results, as you can see in the table above. I think the built in Java timer **System.currentTimeMillis** is kind of like the .NET **DateTime.Now.Ticks**, e.g., limited to a resolution of about 10ms. This was OK back in early 2002 when the Java benchmark was originally constructed, but on today’s PCs, it’s kind of tough to measure a single regex call with a granularity of 10ms...
- I think there’s a small bug in the original source. Notice that the innermost timing loop takes a start time before it enters the loop, then calculates the elapsed time inside the loop against that start time. This seems wrong to me, because each loop will reflect not only its time but the total time since the loop was entered. Anyway, I’ve preserved this “feature” in my VB.NET source so the timings will be comparable.


**Even though .NET appears to perform almost 40 percent faster than Java in this test**, it’s still interesting that in only 6 months since that Java benchmark was run (813ms), I can produce Java code that runs over three times as fast (266ms)! So before we put our language war hats on, consider that perhaps the real winner here is the hardware. Doh!

[java](https://blog.codinghorror.com/tag/java/)
[.net](https://blog.codinghorror.com/tag/net/)
[regex](https://blog.codinghorror.com/tag/regex/)
[performance](https://blog.codinghorror.com/tag/performance/)
[benchmark](https://blog.codinghorror.com/tag/benchmark/)
