---
title: "Don’t Use ZIP, Use RAR"
date: 2007-02-22
url: https://blog.codinghorror.com/dont-use-zip-use-rar/
slug: dont-use-zip-use-rar
word_count: 868
---

When I wrote [Today is “Support Your Favorite Small Software Vendor Day,”](https://blog.codinghorror.com/today-is-support-your-favorite-small-software-vendor-day/) I made a commitment to spend at least $20 per month supporting my fellow independent software developers. [WinRAR](http://www.win-rar.com/rarproducts.html) has become increasingly essential to my toolkit over the last year, so this month, [I’m buying a WinRAR license](http://www.win-rar.com/125.html?prod=winrar).


Sure, ZIP support is built into most operating systems, but the support is rudimentary at best. I particularly dislike the limited “compressed folder wizard” I get by default in XP and Vista. In contrast, WinRAR is full-featured, powerful, and integrates seamlessly with the shell. There’s a reason WinRAR [won the best archive tool](http://www.donationcoder.com/Reviews/Archive/ArchiveTools/index.html) roundup at DonationCoder. And WinRAR is very much a living, breathing piece of software. It’s frequently updated with neat little feature bumps and useful additions; two I noticed over the last year were dual-core support and real-time stats while compressing, such as estimated compression ratio and predicted completion time.


WinRAR fully supports creating and extracting ZIP archives, so choosing WinRAR doesn’t mean you’ll be forced into using the RAR compression format. But you should use it, because **RAR, as a compression format, *clobbers* ZIP. It produces much smaller archives in roughly the same time**. If you’re worried the person on the receiving end of the archive won’t have a RAR client, you can create a self-extracting executable archive (or SFX) at a minimal cost of about 60 KB additional file size.


RAR also supports solid archives, so it can exploit intra-file redundancies. ZIP does not. This is a big deal, because it can result in a substantially smaller archive when you’re compressing a lot of files. When I compressed all the [C# code snippets](https://blog.codinghorror.com/c-snippet-parity/), the difference was enormous:

kg-card-begin: html


| ZIP | 229 KB |
| RAR | 73 KB |


kg-card-end: html

But even in an apples-to-apples comparison, RAR offers some of the very best “bang for the byte” of all compression algorithms. Consider this recent, comprehensive [multiple file compression benchmark](https://web.archive.org/web/20070213032432/http://www.maximumcompression.com/data/summary_mf3.php). The author measured both compression size and compression time to produce an efficiency metric:


> The most efficient (read: useful) program is calculated by multiplying the compression time (in seconds) it took to produce the archive with the power of the archive size divided by the lowest measured archive size.
> 2 ^ (((Size/SmallestSize)) - 1) / 0.1) * ArchiveTime
> The lower the score, the better. The basic idea is a compressor X has the same efficiency as compressor Y if X can compress twice as fast as Y and resulting archive size of X is 10% larger than size of Y.


And sure enough, if you sort the results by efficiency, WinRAR rises directly to the top. Its scores of 1871 (Good) and 1983 (Best) rank third and fourth out of 200. The top two spots are held by an archiver I’ve never heard of, [SBC](https://web.archive.org/web/20070222143535/http://www.geocities.com/sbcarchiver/).


> WinRAR and SBC 0.970 score very well on efficiency. Both SBC and WinRK are capable of compressing the 301 MB testset down to 82 MB [a ~73% compression ratio] in under 3 minutes. People looking for good (but not ultimate) and fast compression should have a look at those two programs.


The raw data on the comparison page is a little hard to parse, so I pulled the data into Excel and created some alternative views of it. Here’s a graph of **compression ratio versus time**, sorted by compression ratio, for all compared archive programs:


What I wanted to illustrate with this graph is that beyond about 73% compression ratio, [performance falls off a cliff](https://blog.codinghorror.com/compression-and-cliffs/). This is something I’ve noted before in previous compression studies. You don’t just hit the point of diminishing returns in compression, you slam into it like a brick wall. That’s why **the time scale is logarithmic** in the above graph. Look at the massive differences in time as you move toward the peak compression ratio:

kg-card-begin: html


| 72.58% | 02:54 | WinRAR 3.62 |
| 75.24% | 11:20 | UHARC 0.6b |
| 77.16% | 30:38 | DRUILCA 0.5 |
| 78.83% | 05:51:19 | PAQ8H |
| 79.70% | 08:30:03 | WinRK 3.0.3 |


kg-card-end: html

Note that I cherry-picked the most efficient archivers out of this data, so this represents *best case* performance. Is an additional two percent of compression worth taking five times longer? Is an additional four percent worth *ten* times longer? Under the right conditions, possibly. But the penalty is severe, and the reward miniscule.


If you’re interested in crunching the multiple file compression benchmark study data yourself, I converted it to a few different formats for your convenience:

- [Download Excel spreadsheet](https://web.archive.org/web/20071019175542/http://www.codinghorror.com/blog/files/compression-comparison-excel-file.zip) (36 KB)
- [Google Spreadsheet](http://spreadsheets.google.com/pub?key=pKxDW35algYclyZXMRfMLOA) (view-only)
- Google Spreadsheet (editable, but need Google login)


Personally, I recommend the Excel version. I had major performance problems with the Google spreadsheet version.


After poring over this data, I’m more convinced than ever. RAR offers a nearly perfect blend of compression efficiency and speed across all modern compression formats. And WinRAR is an exemplary GUI implementation of RAR. It’s almost a no-brainer. Except in cases where backwards compatibility trumps all other concerns, **we should abandon the archaic ZIP format – and switch to the power and flexibility of WinRAR.**

[compression](https://blog.codinghorror.com/tag/compression/)
[file management](https://blog.codinghorror.com/tag/file-management/)
[winrar](https://blog.codinghorror.com/tag/winrar/)
