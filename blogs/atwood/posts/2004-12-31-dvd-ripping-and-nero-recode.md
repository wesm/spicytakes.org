---
title: "DVD Ripping and Nero Recode"
date: 2004-12-31
url: https://blog.codinghorror.com/dvd-ripping-and-nero-recode/
slug: dvd-ripping-and-nero-recode
word_count: 704
---

[Steve Makofsky](https://web.archive.org/web/20050227025159/http://www.furrygoat.com/2004/10/nero_digital_an.html) turned me on to some software I already use: [Nero Burning ROM](http://www.nero.com/us/index.html), but more specifically, [Nero Recode 2](https://www.nero.com/eng/products/nero-recode/?vlang=gb), which is a part of their expanded “ultra” Nero suite. I’ve long considered Nero the definitive DVD and CD burning software; I had no idea they also offered a DVD ripping solution.


Quick clarification: by DVD rip, I mean **re-encoding a MPEG2 DVD using some variant of the MPEG4 video and audio codecs**. The goal is to reduce the file size without losing (too much) quality. For example, you may start with ~9gb of raw, decrypted DVD data, and end up with a 700mb .avi file that has DVD-like video and sound quality. I know it sounds implausible, but I can tell you from personal experience that it works, because MPEG4 is a more modern and efficient codec than MPEG2. The tradeoff is higher CPU decoding requirements (rarely an issue on any remotely modern PC), and a lot of re-encoding time.


I’ve used XMPEG (freeware) and Dr. DivX (payware) to rip DVDs before with somewhat... unreliable results. Both apps crashed on me fairly regularly, and both apps required too many tedious, trial-and-error trips into obscure options and settings dialogs. In comparison, **I just ripped about 10 different DVDs with Nero Recode and it’s been a painless point and click operation every single time **–** **without a single crash! And my god, the speed! Recode produces encoding framerates of nearly 90fps;* the peak encoding rate of Dr. Divx or XMPEG was ~50fps. This is a huge time savings when you’re encoding a 2 hour movie!


But don’t take my word for it. The experts at [CDFreaks loved Nero Recode](https://web.archive.org/web/20050214203216/http://www.cdfreaks.com/article/131/5). When compared to the DivX and XVid encoders, Nero Recode was...

- by far the easiest and most automatic encoder to use
- 5x faster (single pass)
- delivered superior video quality


Ripping to MPEG4 is what I’m most interested in, but Recode can do much more. If you want a fuller overview of the Nero Recode software, there’s a [good review at CDRInfo](http://www.cdrinfo.com/Sections/Reviews/Specific.aspx?ArticleId=8509).


Now, there is one thing you should know about Nero Recode: it produces somewhat... *unusual*... MPEG4 video files, with a *.mp4 extension. All of the above packages technically produce MPEG4 output, but no DivX compatible decoder I found – and I tried many – could deal with the Nero Recode file format. Nero calls their format “[Nero Digital](https://web.archive.org/web/20050102021904/http://www.nerodigital.com/enu/index.html),” but it’s really just advanced MPEG4. It defaults to multi-channel AAC encoded sound instead of your typical (less sophisticated) Dolby Digital or MP3 encoded sound. AAC is a part of the MPEG4 spec, but it’s not widely used. Anyway, the upshot of all this is that **you’re forced to install the annoying Nero Showtime application on any PC you want to watch your *.mp4 files from.** Not acceptable. We should be able to download a small set of decoders and watch our *.mp4 files in any application we want.


Unfortunately, Nero hasn’t seen fit to distribute a standalone “Nero Digital” decoder, which is not exactly a great way to promote a new file format. As Steve helpfully pointed out, you can pay $7 for the 3ivx decoder which – with a small registry modification – **enables playback of *.mp4 files in good old Windows Media Player**:

kg-card-begin: html

```
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT.mp4]
"PerceivedType"="video"
@="3ivx.mp4"
"Content Type"="video/mp4"
```

kg-card-end: html

Paying $7 for a decoder irks me. As an alternative, you can download the **full** version of the [K-Lite Codec Pack](http://www.free-codecs.com/K_Lite_Codec_Pack_download.htm). No need to install every codec under the sun, unless you want to; just deselect everything except for the 3ivx video and sound decoders. That enables Nero Digital playback in WMP on my box.


Like Steve, **I can’t recommend the Nero Ultra suite highly enough. It truly is best of breed.** The only reason to go with DivX is if you have a standalone device that understands the DivX MPEG4 format.


*On my Athlon FX-53. If you plan to encode video a lot, either be very patient, or buy the fastest P4 or Athlon system you can afford. Video encoding is one of the last great frontiers where PCs can never be fast enough.

[dvd](https://blog.codinghorror.com/tag/dvd/)
[nero recode](https://blog.codinghorror.com/tag/nero-recode/)
[mpeg4](https://blog.codinghorror.com/tag/mpeg4/)
[dvd ripping](https://blog.codinghorror.com/tag/dvd-ripping/)
[mpeg2](https://blog.codinghorror.com/tag/mpeg2/)
