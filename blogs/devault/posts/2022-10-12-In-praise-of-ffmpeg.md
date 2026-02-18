---
title: "In praise of ffmpeg"
date: 2022-10-12
url: https://drewdevault.com/2022/10/12/In-praise-of-ffmpeg.html
slug: In-praise-of-ffmpeg
word_count: 659
---

My last “ [In praise of](https://drewdevault.com/2022/09/02/2022-09-02-In-praise-of-qemu.html) ” article covered qemu, a project founded by Fabrice
Bellard, and today I want to take a look at another work by Bellard:
 [ffmpeg](https://ffmpeg.org) . Bellard has a knack for building high-quality software which solves
a problem so well that every other solution becomes obsolete shortly thereafter,
and ffmpeg is no exception.

ffmpeg has been described as the Swiss army knife of multimedia. It incorporates
hundreds of video, audio, and image decoders and encoders, muxers and demuxers,
filters and devices. It provides a CLI and a set of libraries for working with
its tools, and is the core component of many video and audio players as a result
(including my preferred multimedia player,  [mpv](https://mpv.io) ). If you want to do almost
anything with multimedia files — re-encode them, re-mux them, live stream
it, whatever — ffmpeg can handle it with ease.

Let me share an example.

I was recently hanging out at my local hackerspace and wanted to play some PS2
games on my laptop. My laptop is not powerful enough to drive  [PCSX2](https://pcsx2.net) , but my
workstation on the other side of town certainly was. So I forwarded my game
controller to my workstation via USB/IP and pulled up the ffmpeg manual to
figure out how to live-stream the game to my laptop. ffmpeg can capture video
from KMS buffers directly, use the GPU to efficiently downscale them, grab audio
from pulse, encode them with settings tuned for low-latency, and mux it into a
UDP socket. On the other end I set up mpv to receive the stream and play it
back.

```
ffmpeg \
  -f pulse \
  -i alsa_output.platform-snd_aloop.0.analog-surround-51.monitor \
  -f kmsgrab \
  -thread_queue_size 64 \   # reduce input latency
  -i - \
  # Capture and downscale frames on the GPU:
  -vf 'hwmap=derive_device=vaapi,scale_vaapi=1280:720,hwdownload,format=bgr0' \
  -c:v libx264 \
  -preset:v superfast \     # encode video as fast as possible
  -tune zerolatency \       # tune encoder for low latency
  -intra-refresh 1 \        # reduces latency and mitigates dropped packets
  -f mpegts \               # mux into mpegts stream, well-suited to this use-case
  -b:v 3M \                 # configure target video bandwidth
  udp://$hackerspace:41841
```

With an hour of tinkering and reading man pages, I was able to come up with a
single command which produced a working remote video game streaming setup  *from
scratch*  thanks to ffmpeg. ffmpeg is  *amazing* .

I have relied on ffmpeg for many tasks and for many years. It has always been
there to handle any little multimedia-related task I might put it to for
personal use — re-encoding audio files so they fit on my phone, taking
clips from videos to share, muxing fonts into mkv files, capturing video from my
webcam,  [live streaming hacking sessions on my own platform](https://drewdevault.com/2018/08/26/Self-hosted-livestreaming.html) , or anything
else I can imagine. It formed the foundation of  [MediaCrush](https://github.com/mediacrush/mediacrush)  back in the day,
where we used it to optimize multimedia files for efficient viewing on the web,
back when that was more difficult than “just transcode it to a webm”.

ffmpeg is notable for being one of the first large-scale FOSS projects to
completely eradicate proprietary software in its niche. Virtually all
multimedia-related companies rely on ffmpeg to do their heavy lifting. It took a
complex problem and solved it, with free software. The book is now closed on
multimedia: ffmpeg is the solution to almost all of your problems. And if it’s
not, you’re more likely to patch ffmpeg than to develop something new. The code
is accessible and the community are experts in your problem domain.

ffmpeg is one of the foremost pillars of achievement in free software. It has
touched the lives of every reader, whether they know it or not. If you’ve ever
watched TV, or gone to a movie, or watched videos online, or listened to a
podcast, odds are that ffmpeg was involved in making it possible. It is one of
the most well-executed and important software projects of all time.
