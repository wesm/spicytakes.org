---
title: "Concluding the Great MP3 Bitrate Experiment"
date: 2012-06-27
url: https://blog.codinghorror.com/concluding-the-great-mp3-bitrate-experiment/
slug: concluding-the-great-mp3-bitrate-experiment
word_count: 866
---

And now for the dramatic conclusion to [The Great MP3 Bitrate Experiment](https://blog.codinghorror.com/the-great-mp3-bitrate-experiment/) you’ve all been waiting for! The actual bitrates of each audio sample are revealed below, along with how many times each was clicked per the [goo.gl](http://goo.gl/) URL shortener stats between Thursday, June 21st and Tuesday, June 26th.

kg-card-begin: html


| Limburger | ~160kbps VBR | 10,265 |
| Cheddar | 320kbps CBR | 7,183 |
| Gouda | raw CD | 6,159 |
| Brie | ~192kbps VBR | 5,508 |
| Feta | 128kbps CBR | 5,567 |


kg-card-end: html

During that six day period, my overall Amazon CloudFront and S3 bill for these downloaded audio samples was $103.72 for 800 GB of data, across 200k requests.


Based on the raw click stats, it looks like a bunch of folks clicked on the first and second files, then lost interest. Probably because of, y’know, Starship. Still, it’s encouraging to note that the last two files were both clicked about 5.5k times for those that toughed their way out to the very end. Of those listeners, **3,512** went on to contribute results. Not bad at all! I mean, considering I made everyone listen to what some people consider to be one of the [best worst “rock” songs](http://en.wikipedia.org/wiki/List_of_music_considered_the_worst#Songs) of all time. You guys are troopers, taking one in the ear for the team in the name of *science*. That’s what I admire about you.


I belatedly realized after creating this experiment that **there was an easy way to cheat**. Simply compress all the samples with [FLAC](http://flac.sourceforge.net/), then sort by file size.

kg-card-begin: html

```

10,836,505   We+Built+This+City+-+Excerpt+(Feta).flac
11,054,288   We+Built+This+City+-+Excerpt+(Limburger).flac
11,294,757   We+Built+This+City+-+Excerpt+(Brie).flac
11,731,999   We+Built+This+City+-+Excerpt+(Cheddar).flac
11,816,415   We+Built+This+City+-+Excerpt+(Gouda).flac

```

kg-card-end: html

The higher the bitrate, apparently, the less compressible the audio files are with lossless FLAC compression. It’s a small difference in absolute file size, but it’s enough to sort *exactly* with quality. At least you can independently verify that I wasn’t tricking anyone in this experiment; each sample was indeed different, and the bitrates are what I said they were.


But you guys and gals wouldn’t do that, because you aren’t dirty, filthy cheaters, right? Of course not. Let’s go over the actual results. Remember each sample was ranked in a simple web form from **1 to 5**, where 1 is worst quality, and 5 is highest quality.


![Mp3-experiment-results-graph](https://blog.codinghorror.com/content/images/uploads/2012/06/6a0120a85dcdae970b017615e00eec970c-800wi.png)


The summary statistics for the 3,512 data points:

kg-card-begin: html


|  |  | Avg | Std dev |
| 160kbps VBR | (Limburger) | 3.49 | 1.38 |
| 320kbps CBR | (Cheddar) | 3.30 | 1.34 |
| raw CD audio | (Gouda) | 3.34 | 1.26 |
| 192kbps VBR | (Brie) | 3.27 | 1.29 |
| 128kbps CBR | (Feta) | 2.95 | 1.40 |


kg-card-end: html

(If you’d like to perform more detailed statistical analysis, [download the Excel 2010 spreadsheet](https://web.archive.org/web/20120711143831/http://www.codinghorror.com/files/codinghorror-mp3-experiment-2012-final.zip) with all the data and have at it.)


Even without busting out hard-core statistics, I think it’s clear from the basic summary statistics graph that **only one audio sample here was discernably different than the rest – the 128kbps CBR**. And by different I mean “audibly worse.” I’ve maintained for a long, long time that typical 128kbps MP3s are not acceptable quality. Even for the worst song ever. So I guess we can consider this yet another blind listening test proving that point. Give us VBR at an average bitrate higher than 128kbps, or give us death!


But what about the claim that people with dog ears can hear the difference between the higher bitrate MP3 samples? Well, first off, it’s incredibly strange that the first sample – encoded at a mere 160kbps – does better on average than everything else. I think it’s got to be bias from appearing first in the list of audio samples. It’s kind of an outlier here for no good reason, so we have to almost throw it out. More fuel for the argument that **people can’t hear a difference at bitrates above 128kbps**, and even if they do, they’re probably imagining it. If we didn’t throw out this result, we’d have to conclude that the 160kbps sample was somehow superior to the raw CD audio, which is… clearly insane.


Running [T-Test](http://en.wikipedia.org/wiki/Student's_t-test) and [Analysis of Variance](http://en.wikipedia.org/wiki/Analysis_of_variance) (it’s in the spreadsheet) on the non-insane results, I can confirm that the 128kbps CBR sample is lower quality with an *extremely* high degree of statistical confidence. Beyond that, as you’d expect, nobody can hear the difference between a 320kbps CBR audio file and the CD. And the 192kbps VBR results have a *barely* statistically significant difference versus the raw CD audio at the 95% confidence level. I’m talking absolutely *wafer thin* here.


Anyway, between the anomalous 160kbps result and the blink-and-you’ll-miss-it statistical difference between the 192kbps result and the raw CD audio, I’m comfortable calling this one as I originally saw it. The data from this experiment confirms what I thought all along: for pure listening, the LAME defaults of 192kbps variable bit rate encoding do indeed provide a safe, optimal aural bang for the byte – **even dogs won’t be able to hear the difference between 192kbps VBR MP3 tracks and the original CD.**

[audio](https://blog.codinghorror.com/tag/audio/)
[mp3](https://blog.codinghorror.com/tag/mp3/)
[bitrate](https://blog.codinghorror.com/tag/bitrate/)
[experiment](https://blog.codinghorror.com/tag/experiment/)
[amazon cloudfront](https://blog.codinghorror.com/tag/amazon-cloudfront/)
