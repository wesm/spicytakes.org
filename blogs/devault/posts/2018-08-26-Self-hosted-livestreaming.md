---
title: "How to make a self-hosted video livestream"
date: 2018-08-26
url: https://drewdevault.com/2018/08/26/Self-hosted-livestreaming.html
slug: Self-hosted-livestreaming
word_count: 854
---

I have seen some articles in the past which explain how to build the ecosystem
 *around*  your video streaming, such as live chat and forums, but which leave the
actual video streaming to Twitch.tv. I made a note the last time I saw one of
these articles to write one of my own explaining the video bit. As is often the
case with video, we’ll be using the excellent  [ffmpeg](http://ffmpeg.org/)  tool
for this. If it’s A/V-related, ffmpeg can probably do it.

*Note: a demonstration video was previously shown here, but as traffic on this
article died down I took it offline to reduce unnecessary load.*

ffmpeg has a built-in  [DASH](https://dashif.org/)  output format, which is the
current industry standard for live streaming video to web browsers. It works by
splitting the output up into discrete files and using an  [XML
file](/dash/live.mpd)  (an MPD playlist) to tell the player where they are. Few
browsers support DASH natively, but
 [dash.js](https://github.com/Dash-Industry-Forum/dash.js/wiki)  can polyfill it
by periodically downloading the latest manifest and driving the video element
itself.

Getting the source video into ffmpeg is a little bit beyond the scope of this
article, but I know some readers won’t be familiar with ffmpeg so I’ll have
mercy. Let’s say you want to play some static video files like I’m doing above:

```
ffmpeg \
	-re \
	-stream_loop -1 \
	-i my-video.mkv \
```

This will tell ffmpeg to read the input (-i) in real time (-re), and loop it
indefinitely. If instead you want to, for example, use x11grab instead to
capture your screen and pulse to capture desktop audio, try this:

```
    -f x11grab \
    -r 30 \
    -video_size 1920x1080 \
    -i $DISPLAY \
    -f pulse \
    -i alsa_input.usb-Blue_Microphones_Yeti_Stereo_Microphone_REV8-00.analog-stereo
```

This sets the framerate to 30 FPS and the video resolution to 1080p, then reads
from the X11 display  `$DISPLAY`  (usually :0). Then we add pulseaudio and use my
microphone source name, which I obtained with  `pactl list sources` .

Let’s add some arguments describing the output format. Your typical web browser
is a finicky bitch and has some very specific demands from your output format if
you want maximum compatability:

```
    -codec:v libx264 \
    -profile:v baseline \
    -level 4 \
    -pix_fmt yuv420p \
    -preset veryfast \
    -codec:a aac \
```

This specifices the libx264 video encoder with the baseline level 4 profile, the
most broadly compatible x264 profile, with the yuv420p pixel format, the most
broadly compatible pixel format, the veryfast preset to make sure we can encode
it in realtime, the aac audio codec. Now that we’ve specified the parameters for
the output, let’s configure the output format: DASH.

```
	-f dash \
	-window_size 5 \
	-remove_at_exit 1 \
	/tmp/dash/live.mpd
```

The window_size specifies the maximum number of A/V segments to keep in the
manifest at any time, and remove_at_exit will clean up all of the files when
ffmpeg exits. The output file is the path to the playlist to write to disk, and
the segments will be written next to it. The last step is to serve this with
nginx:

```
location /dash {
        types {
                application/dash+xml mpd;
                video/mp4 m4v;
                audio/mp4 m4a;
        }
        add_header Access-Control-Allow-Origin *;
        root /tmp;
}
```

You can now point the  [DASH reference
player](http://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html) 
at  `http://your-server.org/dash/live.mpd`  and see your video streaming there.
Neato! You can add dash.js to your website and you know have a fully self-hosted
video live streaming setup ready to rock.

Perhaps the ffmpeg swiss army knife isn’t your cup of tea. If you want to, for
example, use  [OBS Studio](https://obsproject.com/) , you might want to take a
somewhat different approach. The
 [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module)  provides an RTMP
(real-time media protocol) server that integrates with nginx. After adding
the DASH output, you’ll end up with something like this:

```
rtmp {
    server {
        listen 1935;

        application live {
            dash on;
            dash_path /tmp/dash;
            dash_fragment 15s;
        }
    }
}
```

Then you can stream to  `rtmp://your-server.org/live`  and your dash segments
will show up in  `/tmp/dash` . There’s no password protection here, so put it in
the stream URL (e.g.  `application R9AyTRfguLK8` ) or use an IP whitelist:

```
application live {
    allow publish your-ip;
    deny publish all;
}
```

If you want to get creative with it you can use
 [`on_publish`](https://github.com/arut/nginx-rtmp-module/wiki/Directives#on_publish) 
to hit an web service with some details and return a non-2xx code to forbid
streaming. Have fun!

I learned all of this stuff by making a bot which livestreamed Google hangouts
over the LAN to get around the participant limit at work. I’ll do a full writeup
about that one later!

Here’s the full script I’m using to generate the live stream on this
page:

```
#!/bin/sh
rm -f /tmp/playlist
mkdir -p /tmp/dash
for file in /var/www/mirror.sr.ht/hacksway-2018/*
do
	echo "file '$file'" >> /tmp/playlist
done

ffmpeg \
	-re \
	-loglevel error \
	-stream_loop -1 \
	-f concat \
	-safe 0 \
	-i /tmp/playlist \
	-vf "drawtext=\
			fontfile=/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf:\
			text='%{gmtime\:%Y-%m-%d %T} UTC':\
			fontcolor=white:\
			x=(w-text_w)/2:y=128:\
			box=1:boxcolor=black:\
			fontsize=72,
		drawtext=\
			fontfile=/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf:\
			text='REBROADCAST':\
			fontcolor=white:\
			x=(w-text_w)/2:y=16:\
			box=1:boxcolor=black:\
			fontsize=48" \
	-codec:v libx264 \
	-profile:v baseline \
	-pix_fmt yuv420p \
	-level 4 \
	-preset veryfast \
	-codec:a aac \
	-f dash \
	-window_size 5 \
	-remove_at_exit 1 \
	/tmp/dash/live.mpd
```
