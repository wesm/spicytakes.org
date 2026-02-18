---
title: "Using Cage for a seamless remote Wayland session"
date: 2019-04-23
url: https://drewdevault.com/2019/04/23/Using-cage-for-a-seamless-RDP-Wayland-desktop.html
slug: Using-cage-for-a-seamless-RDP-Wayland-desktop
word_count: 369
---

Congratulations to Jente Hidskes on  [the first release of
Cage](https://www.hjdskes.nl/blog/cage-01/) ! Cage is a Wayland compositor
designed for kiosks - though, as you’ll shortly find out, is useful in many
unexpected ways. It launches a single application, in fullscreen, and exits the
compositor when that application exits. This lets you basically add a
DRM+KMS+libinput session to any Wayland-compatible application (or X application
via XWayland) and run it in a tiny wlroots compositor.

I actually was planning on writing something like this at some point (for a
project which still hasn’t really come off the ground yet), so I was excited
when Jente  [announced it](https://www.hjdskes.nl/blog/cage/)  in December. With
the addition of the  [RDP backend](https://github.com/swaywm/wlroots/pull/1578) 
in wlroots, I thought it would be cool to combine these to make a seamless
remote desktop experience. In short, I installed
 [FreeRDP](http://www.freerdp.com/)  and Cage on my laptop, and
 [sway](https://swaywm.org)  on my desktop. On my desktop, I  [generated TLS
certificates per the wlroots
docs](https://github.com/swaywm/wlroots/blob/master/docs/env_vars.md#rdp-backend) 
and ran sway like so:

```
WLR_RDP_TLS_CERT_PATH=$HOME/tls.crt \
WLR_RDP_TLS_KEY_PATH=$HOME/tls.key \
WLR_BACKENDS=rdp \
sway
```

Then, on my laptop, I can run this script:

```
#!/bin/sh
if [ $# -eq 0 ]
then
	export XDG_RUNTIME_DIR=/tmp
	exec cage sway-remote launch
else
	sleep 3
	exec xfreerdp \
		-v homura \
		--bpp 32 \
		--size 1280x800 \
		--rfx
fi
```

The first branch is taken on the first run, and it starts up cage and asks it to
run this script again. The second branch then starts up xfreerdp and connects to
my desktop (its hostname is  `homura` ). xfreerdp is then fullscreened and all of
my laptop’s input events are directed to it. The result is an experience which
is basically identical to running sway directly on my laptop, except it’s
actually running on my desktop and using the remote desktop protocol to send
everything back and forth.

This isn’t especially practical, but it is a cool hack. It’s definitely not
network transparency like some people want, but I wasn’t aiming for that. It’s
just a neat thing you can do now that we have an RDP backend for wlroots. And
congrats again to Jente - be sure to give Cage a look and see if you can think
of any other novel use-cases, too!
