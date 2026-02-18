---
title: "Integrating a VT220 into my life"
date: 2016-03-22
url: https://drewdevault.com/2016/03/22/Integrating-a-VT220-into-my-life.html
slug: Integrating-a-VT220-into-my-life
word_count: 1166
---

I bought a DEC VT220 terminal a while ago, and put it next to my desk at work. I
use it to read emails on mutt now, and it’s actually quite pleasant. There was
some setup involved in making it as comfortable as possible, though.

Here’s the terminal up close:

## Hardware

First, I have several pieces of hardware involved in this:

* VT220 terminal
* LK201 keyboard (later made obsolete)
* [USB to serial adapter](http://amzn.com/B00IDSM6BW)
* [DB9->DB29 null modem cable](http://amzn.com/B00066HL50)

It took a while to get all of these things, but I was able to get a nice
refurbished terminal and a couple of crappy LK201 keyboards. Luckily I was able
to eventually remove the need for the keyboard.

## Basic Setup

Getting this working on Linux is actually pretty simple thanks to decades of
backwards compatability. Plug all of the cords together, turn on the machine,
and (on Arch, at least) run:

```
systemctl start serial-agetty@ttyUSB0.service
```

This will start up a getty for you to log into on your terminal. For a while I
would use the LK201 to log in to this getty and spin up a mail cilent.

I did have to make a couple of changes to serial-agetty@.service, though:

```
ExecStart=-/sbin/agetty -h -L 19200 %I vt220
```

This specifies the TERM variable as “vt220” and sets the baud rate to 19200. I
had to also set the baud rate in the terminal’s settings to 19200 baud as well,
to get the fastest possible terminal.

I eventually got into the habit of logging into the terminal with the LK201,
then running tmux and attaching to tmux from my desktop session. I would then
hide this tmux terminal in the upper left corner of my display, and move my
mouse over to it when I wanted to interact with the terminal. This let me use
the same keyboard I used for the rest of my computer experience to interact with
the VT220, instead of trying to use the LK201 as well. This was a bit annoying,
so eventually I did some more customization.

## Removing the keyboard

I wanted to be able to make everything automatic, so I could just boot my
computer and log in normally and treat the VT220 almost like a fourth monitor. I
started by automating the process of logging in and running tmux.

First, I created a user for the terminal:

```
useradd vt220
```

Then, I wrote a shell script that would serve as the user’s login shell and
would start tmux:

```
#!/usr/bin/env bash
if [[ $TERM == "screen" ]]
then
	sudo /usr/local/bin/login-sircmpwn
else
	tmux -S /var/tmux/vt220.sock
fi
```

I made that directory,  `/var/tmux/` , and made sure both the vt220 user and my
normal user had access to it. I also edited my sudoers file so that vt220 could
run that command as root:

```
vt220 ALL=(ALL) NOASSWD: /usr/local/bin/login-sircmpwn
```

I put the script into  `/usr/local/bin`  and added it to  `/etc/shells` , then made
it the login shell for the vt220 user with  `chsh` . I then moved to my own
systemd unit for starting the getty on ttyUSB0, this time with autologin:

```
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

[Unit]
Description=Serial Getty on %I
Documentation=man:agetty(8) man:systemd-getty-generator(8)
Documentation=http://0pointer.de/blog/projects/serial-console.html
BindsTo=dev-%i.device
After=dev-%i.device systemd-user-sessions.service plymouth-quit-wait.service

# If additional gettys are spawned during boot then we should make
# sure that this is synchronized before getty.target, even though
# getty.target didn't actually pull it in.
Before=getty.target
IgnoreOnIsolate=yes

[Service]
ExecStart=-/sbin/agetty -a vt220 -h -L 19200 %I vt220
Type=idle
Restart=always
UtmpIdentifier=%I
TTYPath=/dev/%I
TTYReset=yes
TTYVHangup=yes
KillMode=process
IgnoreSIGPIPE=no
SendSIGHUP=yes

[Install]
WantedBy=getty.target
```

The only difference here is that it invokes agetty with  `-a vt220`  to autologin
as that user.  `systemctl enable vtgetty@ttyUSB0.service`  makes it so that on
boot, the getty would run on ttyUSB0 and autologin as vt220. Then the script
from earlier will run tmux, and within tmux will run  `sudo /usr/local/bin/login-sircmpwn` , which is this shell script:

```
#!/usr/bin/env bash
until who | grep sircmpwn 2>&1 >/dev/null
do
	sleep 1
done
sudo -iu sircmpwn
```

What this does is pretty straightforward - it loops until I log in as sircmpwn,
then enters an interactive session with sudo as sircmpwn.

The net of all of this is that now, I can boot up my machine, and when I log in,
the VT220 starts up with tmux running and logged in as me. Then I went back to
the old way of attaching to this tmux session with a terminal on my desktop
session hidden in a corner of the screen. And now I could ditch the clunky old
LK201 keyboard!

## Treating the terminal as another output

I said earlier that my goal was to treat the terminal as a fake “output” that I
could switch to from my desktop session just like I switch between my three
graphical outputs. I run  [sway](https://github.com/SirCmpwn/sway) , of course, so
I decided to add a fake output in sway and see where that went. I made a
somewhat complicated  [branch](https://github.com/SirCmpwn/sway/compare/vt220) 
for this purpose, but the important change is here:

```
diff --git a/sway/handlers.c b/sway/handlers.c
index cec6319..60f8406 100644
--- a/sway/handlers.c
+++ b/sway/handlers.c
@@ -704,6 +704,21 @@ static void handle_wlc_ready(void) {
 		free(line);
 		list_del(config->cmd_queue, 0);
 	}
+	// VT220 stuff
+	// Adds a made up output that we can use for a tmux window
+	// connected to my vt220
+	swayc_t *output = new_swayc(C_OUTPUT);
+	output->name = "VT220";
+	output->handle = UINTPTR_MAX;
+	output->width = 1000;
+	output->height = 1000;
+	output->unmanaged = create_list();
+	output->bg_pid = -1;
+	add_child(&root_container, output);
+	output->x = -1000;
+	output->y = 0;
+	new_workspace(output, "__VT220");
+	// End VT220 stuff
 }
```

This creates a fake output and puts it to the far left, then adds a workspace to
it called __VT220. I assigned it the output handle of UINTPTR_MAX and everywhere
in sway that it would try to use the output handle to manipulate a real output,
I changed to to avoid doing so if the handle is UINTPTR_MAX. Then I added this
to my sway config:

```
for_window [title="__VT220"] move window to workspace __VT220 
```

And run this command when sway starts:

```
urxvt -T "__VT220" -e tmux -S /var/tmux/vt220.sock a
```

Which spawns a terminal whose window title is __VT220 running tmux attached to
the session running on the terminal. The for_window rule I added to my sway
config automatically moves this to the VT220 fake output and tada! It works. Now
I have a nice and comfortable way to use my terminal to read emails at work. Now
if only I could convince people to stop sending me HTML emails! I just bought a
second VT220 for use at home, too. Life’s good~

[Discussion on Hacker News](https://news.ycombinator.com/item?id=11339909)
