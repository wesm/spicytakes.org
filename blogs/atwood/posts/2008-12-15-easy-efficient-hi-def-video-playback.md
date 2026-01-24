---
title: "Easy, Efficient Hi-Def Video Playback"
date: 2008-12-15
url: https://blog.codinghorror.com/easy-efficient-hi-def-video-playback/
slug: easy-efficient-hi-def-video-playback
word_count: 1440
---

Ever since creating [my first home theater PC](https://blog.codinghorror.com/building-your-own-home-theater-pc/), I’ve archived my Netflix rental DVDs to files on the hard drive. I don’t do this because I want to rip off the movie industry; I do it for convenience. **It’s easier to deal with a collection of digital files than it is to deal with a bunch of shiny, easily scratched plastic discs.** Nor do I keep the movies around after I watch them. I already own more movies than I could possibly ever watch in one lifetime. As I get older, my desire to collect things is rapidly diminishing. My ripping is purely about simplicity and ease of use for me, the consumer.


After years archiving DVDs on my home theater PC, I was concerned that [the dawning Blu-Ray era](https://blog.codinghorror.com/blu-ray-is-it-time/) would make this impossible. Fortunately, that’s not the case. I experimented with [AnyDVD HD](https://web.archive.org/web/20081216023115/http://www.slysoft.com/en/anydvdhd.html) and my first batch of rented Netflix Blu-Ray discs:

1. Right click the SlySoft task bar icon; choose “Rip Video DVD to Harddisk”
2. Choose a path (it will create a subfolder)
3. Make sure you have at least 50 GB of free disk space
4. Click “Copy DVD”


So brainlessly easy, even *I* can do it.


You’ll end up with a folder containing all the subfolders and files that make up the Blu-Ray title. I’m not terribly interested in extras and so forth (did I mention that I don’t have time?), I just want the movie itself. It’s not hard to find. The movie file is in the folder:

kg-card-begin: html

```

/BDMV/STREAM/*.m2ts

```

kg-card-end: html

Sort by file size, identify the biggest file, and that’s your movie. Some movies are broken up into multiple files, but most of the ones I’ve done so far have been one giant honking file, somewhere between 8 and 20+ gigabytes in size. **Rename and copy that one giant m2ts file** wherever you want it, then delete all the other files.


Let’s look at [Terminator 3](http://www.amazon.com/dp/B0013ND36G) as a specific example. (Digression: I don’t understand why this movie gets such a bad rap. Sure, it’s not a landmark film like T1 or T2, but it’s a solid entry in the franchise, at least in my opinion.) Blu-Ray encompasses multiple [video and audio encoding formats](http://en.wikipedia.org/wiki/Blu-ray_Disc#Codecs), so we need to crack open the file and see what’s inside. I recommend using the [most excellent MediaInfo application](http://mediainfo.sourceforge.net/en) for this.

kg-card-begin: html

```

General
Complete name                    : terminator3.m2ts
Format                           : BDAV
Format/Info                      : BluRay Video
File size                        : 13.0 GiB
Duration                         : 1h 49mn
Overall bit rate                 : 17.1 Mbps
Maximum Overall bit rate         : 48.0 Mbps
  
Video
Format                           : VC-1
Format profile                   : AP@L3
Duration                         : 1h 48mn
Bit rate                         : 13.9 Mbps
Width                            : 1920 pixels
Height                           : 1080 pixels
Display aspect ratio             : 16/9
Frame rate                       : 23.976 fps
Colorimetry                      : 4:2:0
Scan type                        : Progressive
Bits/(Pixel*Frame)               : 0.280

  
Audio (1 of 6)
Format                           : AC-3
Format/Info                      : Audio Coding 3
Duration                         : 1h 49mn
Bit rate mode                    : Constant
Bit rate                         : 640 Kbps
Channel(s)                       : 6 channels
Channel positions                : Front: L C R, Surround: L R, LFE
Sampling rate                    : 48.0 KHz

```

kg-card-end: html

I’ve clipped a lot of the extraneous information away, but the most important parts here are the encodings:

- Video is [VC-1](http://en.wikipedia.org/wiki/VC-1), 1920 x 1080, 13.9 Mbps average
- Audio is [Dolby Digital AC-3](http://en.wikipedia.org/wiki/Dolby_Digital), 6 channel, 640 Kbps


The ripping part has been straightforward; what I haven’t been able to understand is why **playback of 1920 x 1080 high definition files is so spotty** on my current home theater PC:

1. Gigabyte GA-MA78GPM-DS2H Micro ATX motherboard (*highly* recommended)
2. AMD Athlon X2 4050e 2.1 GHz
3. Windows Vista 32-bit SP1
4. [ffdshow all-in-one codec pack](http://www.free-codecs.com/download/FFDshow.htm)


Everything I’ve read led me to believe that **any modern reasonably fast dual-core CPU is more than enough for high definition video playback**. While that’s *generally* true, some files are tougher than others. For example, taking advantage of my new multi-format drive, I picked up a cheap copy of the now-obsolete HD-DVD edition of [Planet Earth - The Complete BBC Series](http://www.amazon.com/dp/B000MRAAJM). (Which is amazing, by the way – it’s probably the ultimate high definition demo disc, and the shows are fascinating to boot.) These files are also encoded with VC-1 but at a somewhat higher bitrate than Terminator 3.


Unfortunately, on a dual core Athlon – even overclocked to 2.3 GHz – the Planet Earth rips are on the ragged edge of playability under Windows Media Player. CPU usage is well north of 80% all the time, and some peaks at 100% mean video stuttering and sound breakup at least a few times in each episode. This is unacceptable.


After a great deal of research, I found [Media Player Classic Home Cinema](http://mpc-hc.sourceforge.net/). The big deal here is two things:

1. All codecs are “burned into” the Media Player Classic executable, so there’s do dependency on whatever random codecs your PC happens to have installed (eg., ffdshow, cccp, Ivan’s Krazy Elite Kodek Pak, etc.).
2. It supports offloading video decoding duties to modern video cards. This is limited to recent Radeon HD models and nVidia 8 and 9 series. Fortunately, my HTPC motherboard includes an embedded Radeon HD 3200 – and since I blew up my old one (it’s a long story) the new version I just installed includes 128 megabytes of dedicated DDR3 video memory, too.


Now, remember that Terminator 3 is encoded with VC-1, effectively a Microsoft video codec. Windows Media Player supports this natively. You’d expect it to perform great, since it’s baked into the operating system, right?


![](https://blog.codinghorror.com/content/images/2025/04/image-239.png)


Wrong. This isn’t terrible performance, per se, but watch what happens when we play this same file using Media Player Classic Home Cinema, with hardware accelerated decoding enabled:


![](https://blog.codinghorror.com/content/images/2025/04/image-238.png)


Holy cow. **Using video hardware acceleration, we went from 75% CPU usage to 30% CPU usage**. That’s incredible. I knew modern video cards could *assist* in decoding high definition video, but I had no idea the difference was this profound.


But I want to play my movie files in [Windows Vista Media Center](https://blog.codinghorror.com/windows-vista-media-center/), not a weird little standalone app. Here’s the most awesome part of this post: *you can!*


As I discovered buried in [an obscure forum post](https://web.archive.org/web/20081217214604/http://www.xpmediacentre.com.au/community/video-audio-cards-vista/27878-mkv-h-264-hardware-acceleration-dxva-4.html), here’s how:

1. [download the standalone MPC-HC filters](http://sourceforge.net/project/showfiles.php?group_id=170561).
2. Extract `MPCVideoDec.ax` and copy it into `c:windowssystem32`
3. Open a command prompt, navigate to `c:windowssystem32`, and run `regsvr32 MPCVideoDec.ax`


Be sure you don’t have any other video codecs registered, as the MPC-HC filter can handle everything. **Once you register this magical codec, Windows Media Player (and thus, Windows Media Center) will use hardware accelerated high definition video playback**. It’s amazing. How amazing? Those Planet Earth rips, which used to take 80-100% of a mainstream dual core CPU, barely take 40% when using the hardware accelerated MPC-HC filters.


There is one caveat: for some reason, the MPC-HC filter doesn’t accelerate the H.264 Blu-Ray encoding format out of the box. But it can, though. You’ll need to use something like the [Radlight Filter Manager](http://www.free-codecs.com/download/RadLight_Filter_Manager.htm) to fix this. After launching it, navigate to the DirectShow filters part of the tree, then look for “MPC - Video decoder,” and click the Property Page button.


![](https://blog.codinghorror.com/content/images/2025/04/image-237.png)


On the Codecs tab, the only format not ticked for me was H.264/AVC. Tick that box and you’re covered. You now have **fully hardware accelerated playback for every possible Blu-Ray video encoding format.** For free!


In my earlier attempts to solve this high definition video playback problem, I bought a copy of CoreAVC’s “world’s fastest H.264 software video decoder.” And it was fast. Much faster than, say, the H.264 decoder included with ffdshow. My [Casino Royale](http://www.amazon.com/dp/B000MRA5NS) rip went from unplayable under ffdshow to eminently playable under CoreAVC, albeit at 80-90% CPU usage. I thought that was a great result until I saw the MPC-HC filter **play that very same Casino Royale file at around 25% CPU usage.** Zow. That’s a night and day difference between “world’s fastest” software and hardware accelerated H.264 decoding.


Now, if you have a *very* fast dual core CPU, or a moderately fast quad core CPU, you might be able to get away with pure software high definition video decoding (albeit at the cost of high CPU usage). But if, like me, you want to use a cheap, power-efficient dual core CPU to pull off high definition video playback, you’ll need to properly harness the hardware decoding abilities of modern video cards. Media Player Classic Home Cinema is an excellent example of how this *should* work, and it’s about the only one I could *get* to work.

[video playback](https://blog.codinghorror.com/tag/video-playback/)
[home theater pc](https://blog.codinghorror.com/tag/home-theater-pc/)
[digital files](https://blog.codinghorror.com/tag/digital-files/)
[netflix](https://blog.codinghorror.com/tag/netflix/)
[blu-ray](https://blog.codinghorror.com/tag/blu-ray/)
