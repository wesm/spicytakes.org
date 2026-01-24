---
title: "Revisiting 7-ZIP"
date: 2007-02-23
url: https://blog.codinghorror.com/revisiting-7-zip/
slug: revisiting-7-zip
word_count: 259
---

In my previous post, I extolled the virtues of [WinRAR and the RAR archive](https://blog.codinghorror.com/dont-use-zip-use-rar/) format. I disregarded [7-ZIP](http://www.7-zip.org/) because it didn’t do well in [that particular compression study](https://web.archive.org/web/20070228113951/http://www.maximumcompression.com/data/summary_mf3.php), and because my previous experiences with it had shown it to be [efficient, but brutally slow](https://blog.codinghorror.com/compression-and-cliffs/).


But that’s no longer true. Consider the following test I just conducted:

- Two files: a 587 MB virtual hard disk file, and a 11 KB virtual machine file.
- Test rig is a Dual Core Athlon X2 4800+.
- All default GUI settings were used.
- All extracting and archiving done from one physical hard drive to another, to reduce impact of disk contention.

kg-card-begin: html


|  | Extraction | Compression | Size |
| WinRAR 3.70 beta 2 | 0:39 | 3:09 | 135 MB |
| 7-ZIP 4.20 | - | 6:04 | 127 MB |
| 7-ZIP 4.44 beta | 0:40 | 3:03 | 125 MB |


kg-card-end: html

**7-ZIP performance has doubled over the last two years.** And it’s slightly more efficient at compression, too. That’s impressive.


Performance is no longer a reason to choose WinRAR over 7-ZIP. Granted, this is a sample size of one, a single test on a single machine, but it’s hard to ignore the dramatic reversal of fortune.


I still like WinRAR’s ultra-slick shell integration. But 7-ZIP is a viable competitor now in terms of raw clock time performance, and as always, it tends to produce smaller archives than RAR. This more than addresses my previous criticisms. Mea culpa, 7-ZIP.

[compression](https://blog.codinghorror.com/tag/compression/)
[7-zip](https://blog.codinghorror.com/tag/7-zip/)
[software](https://blog.codinghorror.com/tag/software/)
[performance](https://blog.codinghorror.com/tag/performance/)
[technology](https://blog.codinghorror.com/tag/technology/)
