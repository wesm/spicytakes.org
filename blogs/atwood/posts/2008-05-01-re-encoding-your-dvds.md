---
title: "Re-Encoding Your DVDs"
date: 2008-05-01
url: https://blog.codinghorror.com/re-encoding-your-dvds/
slug: re-encoding-your-dvds
word_count: 1075
---

Like Donald Knuth, I think much of the current [multicore hype is overrated](http://www.informit.com/articles/article.aspx?p=1193856).


> The machine I use today has dual processors. I get to use them both only when I’m running two independent jobs at the same time; that’s nice, but it happens only a few minutes every week. If I had four processors, or eight, or more, I still wouldn’t be any better off, considering the kind of work I do – even though I’m using my computer almost every day during most of the day. So why should I be so happy about the future that hardware vendors promise? They think a magic bullet will come along to make multicores speed up my kind of work; I think it’s a pipe dream. (No – that’s the wrong metaphor! “Pipelines” actually work for me, but threads don’t. Maybe the word I want is “bubble.”)


Despite that, I’ve acknowledged all along there are [certain narrow tasks](https://blog.codinghorror.com/choosing-dual-or-quad-core/) that the proliferation of CPU cores will make *dramatically* faster. And one of my very favorite tasks in that niche is **encoding your DVD collection**.


I bought my first DVD about 10 years ago. At the time, they were [a technical marvel](http://en.wikipedia.org/wiki/DVD#Technology):

- 8.5 Gigabytes per side
- 720 x 480 MPEG-2 video at 30 frames per second
- Dolby Digital (AC-3) or Digital Theater System (DTS) digital multichannel sound


Today, those specs are [rapidly becoming pedestrian](https://blog.codinghorror.com/next-gen-dvd-are-those-additional-pixels-worth-your-money/) in the face of high definition cable, broadcast, and Blu-Ray discs. A few of the [video sharing websites](http://en.wikipedia.org/wiki/List_of_video_sharing_websites) offer something perilously close to DVD quality already.


I say **the DVD is the new MP3**. We’re going to start tossing these things around like candy.


Unlike audio CDs, DVDs are already compressed digital data. You could extract the files from the DVD as-is, and play them back to your heart’s content. No re-encoding required. But like [The Six Million Dollar Man](http://en.wikipedia.org/wiki/The_Six_Million_Dollar_Man), we can rebuild them better than they were before. Video codecs have advanced tremendously since the heady days of MPEG-2. These new codecs take a lot [more playback horsepower than MPEG-2](https://blog.codinghorror.com/high-definition-video-on-the-pc/), but offer comparable quality in about one-fourth the size. We can **turn our digital DVDs into *better* digital DVDs** through superior computer science.


But if you thought the *playback* performance demands of these new codecs were severe, wait until you see the *encoding* performance demands. It’s **only in the last year or two that typical CPUs could encode new-fangled MPEG-4 or VC1 at anything even approaching real time**. But now, with extremely fast dual cores trickling all the way down to the mainstream, and quad-core CPUs carving out a decent share for themselves – the average user could potentially rip and encode a typical DVD in less than 30 minutes. Per a recent [H.264 benchmark dataset analysis](http://www.techarp.com/showarticle.aspx?artno=520), you can statistically expect to *halve* your encode time when going from 2 to 4 cores... and almost do it again when you go from 4 to 8!


![](https://blog.codinghorror.com/content/images/2025/04/image-104.png)


It helps, too, that there’s great free software like [Handbrake](http://handbrake.fr/) which makes it easy to harness that embarrassment of desktop CPU power to encode your DVDs.


![](https://blog.codinghorror.com/content/images/2025/04/image-103.png)


Yes, there are an intimidating number of knobs and dials to potentially tweak here, but what I like about handbrake is that I largely don’t have to. There are some logical presets on the right (clipped out of the screenshot for size, unfortunately) which will get you headed in the right direction: AppleTV, iPod, Film, Xbox 360, and so forth. I do set a handful of variables, like the overall bitrate – I prefer something between 900 and 1200 – and whether I need to deinterlace the source. But I mostly let Handbrake use its “auto” defaults, and get excellent results. If you’re curious about the details, there’s a [well-written description](https://web.archive.org/web/20080505143525/http://www.modmini.com/theatre/howto/dvdjukebox/conversion.php) of many of the Handbrake settings.


I had the most luck with the H.264 codec, which is aggressively multithreaded. I achieved 30-40 fps on my modest new [power efficient dual-core HTPC processor](https://blog.codinghorror.com/building-your-own-home-theater-pc/), and upwards of 100 fps on my [overclocked 4 GHz dual-core](https://blog.codinghorror.com/building-a-pc-part-v-upgrading/). Fortunately, Handbrake supports a batch encode mode, so you can queue up a bunch of jobs to run overnight.


I was *particularly* excited to find that I can pass the digital audio directly through [using the “AC3” setting](https://web.archive.org/web/20080913154846/http://trac.handbrake.fr/wiki/SurroundSoundGuide) for the audio encoder. That means, when playing these files back on a home theater PC, **the digital audio arrives at your receiver in exactly the same way it would from a DVD**, with a [few minor adjustments in ffdshow](https://web.archive.org/web/20110623190742/http://img517.imageshack.us/img517/4407/solosettingspdifab6.jpg). There is no audio degradation or conversion whatsoever! As something of an audiophile, I suffered mightily through many a re-encoded DVD that was downmixed to plain vanilla stereo over the years, so this is a huge step forward in my book.


So, in summary – **nearly the same digital video quality, exactly the same digital audio quality, all wrapped up in a single file less than a quarter of the original size of the DVD.** Seriously, I get chills. It’s geek nirvana. What’s not to love about encoding your DVD collection? It’s also a perfect use of those four CPU cores, which would otherwise lay idle 99% of the time.


Take, for example, one of my favorite movies, [Idiocracy](http://www.imdb.com/title/tt0387808/). I used Handbrake to convert this DVD from a set of files totaling 4.15 GB to a single 995 MB file, at almost no quality loss. See for yourself.


Still image captured from original DVD:


![](https://blog.codinghorror.com/content/images/2025/04/image-102.png)


Still image captured from H.264 encoded video of DVD:


![](https://blog.codinghorror.com/content/images/2025/04/image-101.png)


The above still was used in an earlier post, [A World of Endless Advertising](https://blog.codinghorror.com/a-world-of-endless-advertisements/). I love being able to grab a movie file over the network and quickly get the exact still I need for a blog post. Yes, there is a tiny loss of fidelity – particularly in the chair shadows on the bottom left, and the grain of the wall texture at the upper left. But I’m willing to live with that compromise if it means I don’t have to pull ginormous 8 GB ISO images files over the network.


Why re-encode DVDs you already own? For convenience, mostly – so you can watch them on your mobile devices, on your PCs, laptops, and anything else that vaguely resembles a computer in your home. Might as well put all those CPU horses to proper use. **A re-encoded DVD is *so* much more flexible** than those physical hunks of round, reflective plastic.

[multicore programming](https://blog.codinghorror.com/tag/multicore-programming/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[cpu cores](https://blog.codinghorror.com/tag/cpu-cores/)
[parallel processing](https://blog.codinghorror.com/tag/parallel-processing/)
