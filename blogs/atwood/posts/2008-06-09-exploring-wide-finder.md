---
title: "Exploring Wide Finder"
date: 2008-06-09
url: https://blog.codinghorror.com/exploring-wide-finder/
slug: exploring-wide-finder
word_count: 934
---

I have [decidedly mixed feelings](https://blog.codinghorror.com/code-isnt-beautiful/) about the book Beautiful Code, but one of the better chapters is Tim Bray’s “Finding Things.” In it, he outlines the creation of a small Ruby program:

kg-card-begin: html

```

counts = {}
counts.default = 0
ARGF.each_line do |line|
if line =~ %r{GET /ongoing/When/dddx/(dddd/dd/dd/[^ .]+) }
counts[$1] += 1
end
end
keys_by_count = counts.keys.sort { |a, b| counts[b] <=> counts[a] }
keys_by_count[0 .. 9].each do |key|
puts “#{counts[key]}: #{key}”
end

```

kg-card-end: html

Tim calls Ruby “the most readable of languages”; I think that’s a bit of a stretch, but I’m probably the wrong person to ask, because I’ve learned to [distrust beauty](http://alarmingdevelopment.org/?p=79):


> It seems that infatuation with a design inevitably leads to heartbreak, as overlooked ugly realities intrude. Love is blind, but computers aren’t. A long term relationship – maintaining a system for years – teaches one to appreciate more domestic virtues, such as straightforwardness and conventionality. Beauty is an idealistic fantasy: what really matters is the quality of the never ending conversation between programmer and code, as each learns from and adapts to the other. Beauty is not a sufficient basis for a happy marriage.


But I digress. Even if you have no idea what [Ruby](http://en.wikipedia.org/wiki/Ruby_programming_language) is, this simple little program isn’t too difficult to decipher. It helps if you know that [Tim Bray’s blog](http://www.tbray.org/ongoing/) URLs look like this:

kg-card-begin: html

```

http://www.tbray.org/ongoing/When/200x/2007/09/20/Wide-Finder

```

kg-card-end: html

This is a program to **count the most common HTTP GET URL entries in a webserver log file**. We loop through the entire log file, building up a key-value pair of these URLs, where the key is the unique part of the URL, and the value is the number of times that URL was retrieved.


Maybe it’s just the Windows developer in me, but one might wonder **why you’d bother writing this code at all** in the face of umpteen zillion free and commercial web logfile statistics software packages. After all, [the best code is no code at all](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/).


Well, perhaps there is a reason for this code to exist after all. Tim eventually turned this snippet of code into a benchmarking exercise – [The Wide Finder Project](http://www.tbray.org/ongoing/When/200x/2007/09/20/Wide-Finder).


> It’s a classic example of the culture, born in Awk, perfected in Perl, of getting useful work done by combining regular expressions and hash tables. I want to figure out **how to write an equivalent program that runs fast on modern CPUs with low clock rates but many cores**; this is the Wide Finder project.


A noble experiment, indeed. The benchmarks were performed on the following hardware:

- Sun T5120
- 8 UltraSPARC T2 CPU cores @ 1.4 GHz
- 64 GB RAM


The input data is as follows:

- The complete set of Tim’s web logfiles from March 2007
- 926 MB
- 4,625,236 lines


The results are sort of... well, all over the map. I’ll summarize with the worst and best scores for each language:

kg-card-begin: html


|  | Slowest | Fastest |
| [Perl](http://en.wikipedia.org/wiki/Perl) | 44.29 | 1.51 |
| [Erlang](http://en.wikipedia.org/wiki/Erlang_(programming_language)) | 37.58 | 3.54 |
| [Python](http://en.wikipedia.org/wiki/Python_(programming_language)) | 41.04 | 4.38 |
| [OCaml](http://en.wikipedia.org/wiki/Ocaml) | 49.69 | 14.64 |
| [Ruby](http://en.wikipedia.org/wiki/Ruby_programming_language) | 1:43.71 | 50.16 |


kg-card-end: html

I’m simplifying quite a bit here, and omitting languages with only one submission, so do head over to the [actual results page](http://www.tbray.org/ongoing/When/200x/2007/10/30/WF-Results) for more detail.


While you’re there, I also suggest reading [Tim’s analysis of the results](http://www.tbray.org/ongoing/When/200x/2007/11/12/WF-Conclusions), wherein he argues that some of the code optimizations that “won” the benchmarks should be automatic and nearly transparent to the programmer. He proposes that, **in a perfect world, a *one-character* change to the original Ruby program would be all it takes to enable all the necessary multicore optimizations**:

kg-card-begin: html

```

ARGF.each_line* do |line|

```

kg-card-end: html

I heartily agree. Personally, I think that’s the most important result from the Wide Finder Experiment. When it comes to multicore performance, [choice of language](https://blog.codinghorror.com/why-do-we-have-so-many-screwdrivers/) is no silver bullet. How else can we explain the *massive* disparity between the fastest and slowest versions of the code in each language?


As experiments go, Wide Finder was a reasonably successful one, if somewhat incomplete and perhaps too small. Tim has addressed both of those criticisms and rebooted with [The Wide Finder 2 Project](http://www.tbray.org/ongoing/When/200x/2008/05/01/Wide-Finder-2). It’s bigger, badder, and brawnier, but the goal remains the same:


> The problem is that **lots of simple basic data-processing operations, in my case a simple Ruby script, run like crap on modern many-core processors.** Since the whole world is heading in the slower/many-core direction, this is an unsatisfactory situation.
> If you look at the results from last time, it’s obvious that there are solutions, but the ones we’ve seen so far impose an awful complexity cost on the programmer. The holy grail would be something that maximizes ratio of performance increase per core over programmer effort. My view: Anything that requires more than twice as much source code to take advantage of many-core is highly suspect.


Check the [Wide Finder 2 Project Wiki](https://web.archive.org/web/20080609154405/http://wikis.sun.com/display/WideFinder/Wide+Finder+Home) for all the key details. The [naïve Ruby implementation](https://web.archive.org/web/20080604211318/http://wikis.sun.com/display/WideFinder/The+Benchmark) currently takes 25 hours – yes, *hours* – to complete. Some clever programmers have already beaten this result by almost two orders of magnitude, per the [results wiki page](https://web.archive.org/web/20080609154400/http://wikis.sun.com/display/WideFinder/Results).


Wide Finder isn’t a perfect experiment, but it is a relatively simple, easily understandable summary of the problems facing all of tomorrow’s software developers in the coming massively multicore world. **Can you do better on the time *without* exploding either the code size, the code complexity, or the average programmer’s head?**

[ruby](https://blog.codinghorror.com/tag/ruby/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
