---
title: "Creating Ogg Theora Files on Mac OS X With ffmpeg2theora"
date: 2009-07-02
url: https://daringfireball.net/2009/07/ffmpeg2theora
slug: ffmpeg2theora
word_count: 498
---


To use the HTML 5 `<video>` tag in Firefox 3.5, you need video files encoded in the Ogg Theora format. Apple doesn’t support this format at all, so you can’t just export Ogg files from QuickTime like you can with H.264/MPEG-4. I spent some time trying to find the best easy way to create Ogg Theora files on Mac OS X, and I think [ffmpeg2theora](http://v2v.cc/~j/ffmpeg2theora/) is it.


In his “[Video for Everybody](http://camendesign.com/code/video_for_everybody)” article I [linked to](http://daringfireball.net/linked/2009/07/01/camen-video) yesterday, Kroc Camen suggests using [HandBrake](http://handbrake.fr/) to create Ogg Theora files, but I couldn’t get it to work in HandBrake 0.9.3 (the current release version) without crashing. (Well, one time it created a file without crashing, but the file was corrupt.) It ends up that HandBrake’s broken Ogg support is a known issue with no easy solution, and so [Ogg support has been removed from the current branch of HandBrake](http://forum.handbrake.fr/viewtopic.php?f=5&t=11201), and there are no plans to bring it back.


Camen also linked to [Xiph](http://www.xiph.org/quicktime/), an open-source QuickTime component that adds Ogg Theora playback and export to QuickTime. I don’t want to install this, however. For one thing, the only open-source QuickTime component I’ve ever had a good experience with is [Perian](http://perian.org/). For another, I don’t want Ogg playback support in QuickTime. The [fork in supported codecs](http://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2009-June/020620.html) for the `<video>` tag — Safari won’t support Ogg Theora and Firefox and Opera won’t support H.264 — doesn’t mean you can’t support all three browsers. It just means that to support all three, you need to include at least two `<source>` elements within the `<video>` tag, one pointing to an H.264-encoded file, the other to an Ogg Theora file, like this:


```
<video>
    <source src="example-video.mp4" type="video/mp4" />
    <source src="example-video.ogv" type="video/ogg" />
</video>

```


This serves the H.264 to Safari, the Ogg Theora to Firefox. And for Chrome 3.0, which supports both formats, this should serve the H.264 version because it’s specified first.


[ffmpeg2theora](http://v2v.cc/~j/ffmpeg2theora/) is the one tool I found that simply *just works* for transcoding to Ogg Theora. The downside to ffmpeg2theora is that it’s only available as a command-line tool. But:

1. It has a nice Mac OS X .pkg installer. Launch it, authorize it with admin credentials, and it’ll install the `ffmpeg2theora` tool in */usr/local/bin/*.
2. The command-line syntax could not be simpler. You just type:
`ffmpeg2theora example.m4v
`
and it gets to work, outputting a file named example.ogv right next to the .m4v file. It shows an updating progress message in Terminal while it’s working. There are more options (and it comes with a man page that documents them), but in my testing you can just use the defaults.


ffmpeg2theora’s output looks good. I gave it a 3.9 MB H.264 file as input, and it created a 3.5 MB .ogv file that looked pretty good — way better than typical web video in a Flash player — when I played it back in [VLC](http://www.videolan.org/vlc/) and Firefox 3.5.



| **Previous:** | [Copy and Paste](https://daringfireball.net/2009/06/copy_and_paste) |
| **Next:** | [Mobile Phone Keyboards](https://daringfireball.net/2009/07/mobile_phone_keyboards) |


PreviousNext