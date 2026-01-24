---
title: "Variable Bit Rate: Getting the Best Bang for Your Byte"
date: 2005-12-16
url: https://blog.codinghorror.com/variable-bit-rate-getting-the-best-bang-for-your-byte/
slug: variable-bit-rate-getting-the-best-bang-for-your-byte
word_count: 856
---

I’ll probably never buy music from [iTunes](http://www.itunes.com/), or any other online music store, because **they all use constant bit rate audio encoding formats**. Once I heard the incredible difference in fidelity between variable bit rate (VBR) and constant bit rate (CBR) encoding, I can never go back. And if I’m spending my own money to “own” this music, why pay for the crappy encoded version anyway? **I’d rather buy the CD with the raw, uncompressed versions of the music** and rip it myself.


Having perfect audio fidelity, however, is not my goal. If I wanted that, I’d go for a [lossless audio compression format](http://wiki.hydrogenaudio.org/index.php?title=Lossless_comparison). They achieve 50 percent compression ratios, but that’s still **pushing 20 megabytes for the average song**. Interesting for archival purposes, but way too big for every other possible use.


What I really want is the best bang for the byte: the smallest file size I can achieve while retaining cd quality. Of course, “cd quality” is in the ear of the beholder. Here’s how I judge it: A/B listening tests between the raw WAV file and the encoded file on [nice headphones](https://blog.codinghorror.com/headphone-snobbery/). And to my ear, **the best bang for the byte is variable bit rate MP3 files with an average bitrate of at least 160 kbps**. Constant bit rate MP3s at 160 kbps do such a poor job of capturing the dynamic range of the music that it isn’t even a contender. Sure, I could just encode everything at extremely high constant bit rates like 256 kbps or 320 kbps, but I can’t hear the difference to justify the extra file size. Remember, it’s all about bang for the byte!


WinAmp displays the bitrate of a song in real time, which gives you a way to roughly correlate the encoder’s decisions to the music. For areas of silence, it’ll dip down to 32 kbps, and for areas of high energy, it’ll peak up to 320 kbps.


There are some downsides to variable bit rate encoding, however. The encoder has to make complicated decisions about bitrate instead of mindlessly encoding everything at the same bitrate. That means the encoding uses complex algorithms that take quite a bit longer – at least two times longer than constant bit rate encoding, possibly more. And you want a really smart, high quality encoder, too. Choice of encoder has always been a critical factor in how your music sounds. If you’ve got a lot of “unknown” MP3s, you may want to check them out with the [EncSpot tool](https://web.archive.org/web/20051226040239/http://www.guerillasoft.co.uk/encspot/). It will tell you what encoder was used and estimate the resulting quality of the file:


![](https://blog.codinghorror.com/content/images/2025/03/image-380.png)


MP3 isn’t the only audio encoding format in the world. But it is the most ubiquitous. The good news is that **variable bit rate MP3 fares surprisingly well against the hottest new audio encoding formats**. A recent [multiformat 128 kbps listening test](http://web.archive.org/web/20060101091034/http://www.rjamorim.com/test/multiformat128/results.html) puts VBR MP3 on par with the newer AAC format, and squarely ahead of both ATRAC3 and WMA. Only the newest [MPC](http://www.musepack.net/) and [Vorbis](http://www.vorbis.com/)  formats statistically outperformed VBR MP3 in listening tests. Interestingly, both of these formats are natively variable bit rate.


I use the free [Audiograbber](https://web.archive.org/web/20051216052607/http://www.audiograbber.com-us.net/) GUI to rip CDs. It uses the well-respected [LAME encoding engine](http://lame.sourceforge.net/) under the hood. You can also use LAME at the command line. Here’s LAME encoding a standard 128 kbps CBR MP3 file. It took 15 seconds:


![](https://blog.codinghorror.com/content/images/2025/03/image-379.png)


Here’s LAME encoding a VBR MP3 at quality level five. It encoded a ~153 kbps average bitrate file in 20 seconds. Most of the frames are encoded at 160 kbps.


![](https://blog.codinghorror.com/content/images/2025/03/image-378.png)


Here’s LAME encoding a VBR MP3 at quality level three. It encoded a ~218 kbps average bitrate file in 26 seconds. Most of the encoded frames are 224 kbps.


![](https://blog.codinghorror.com/content/images/2025/03/image-377.png)


One thing to keep in mind about variable bit rate encoding is that it’s, well… variable. If you need predictable file sizes for every song you encode, VBR is definitely not for you. I happened to pick the outlying song on this particular CD; the average bitrates range from 129 kbps to 216 kbps:

kg-card-begin: html


| bitrate | filesize | length |
| 157 kbps | 3.94 mb | 3:30 |
| 178 kbps | 5.11 mb | 4:01 |
| 172 kbps | 8.04 mb | 6:30 |
| 185 kbps | 9.81 mb | 7:23 |
| 182 kbps | 6.53 mb | 5:00 |
| 216 kbps | 7.23 mb | 4:40 |
| 129 kbps | 3.30 mb | 3:34 |
| 197 kbps | 8.03 mb | 5:42 |
| 174 kbps | 8.86 mb | 7:07 |
| 196 kbps | 5.11 mb | 3:38 |
| 175 kbps | 7.41 mb | 5:54 |
| 175 kbps | 9.33 mb | 7:25 |


kg-card-end: html

The goal is to achieve at least 160 kbps average. Some songs will need more, some might need less. There’s something magical about that extra 32 kbps; the difference between a CBR MP3 at 128 kbps and 160 kbps has always been unusually large to my ear.

[audio encoding](https://blog.codinghorror.com/tag/audio-encoding/)
[variable bit rate (vbr)](https://blog.codinghorror.com/tag/variable-bit-rate-vbr/)
[constant bit rate (cbr)](https://blog.codinghorror.com/tag/constant-bit-rate-cbr/)
[compression](https://blog.codinghorror.com/tag/compression/)
[audio quality](https://blog.codinghorror.com/tag/audio-quality/)
