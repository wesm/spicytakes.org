---
title: "Belkin Kvm Linux"
description: "(Problems with mouse, Belkin KVM switch and Linux)"
date: 2004-08-04T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/BelkinKvmLinux.html
slug: BelkinKvmLinux
word_count: 538
---


(Problems with mouse, Belkin KVM switch and Linux)


I've got a Belkin KVM switch which I use to swap between various
	machines by my desk. I really like it as I can share a monitor,
	keyboard and mouse between different machines at a press of a
	button. When I was switching between two windows machines there was
	no problem, but I have been getting a problem with linux.


The worst problem shows itself when I switch into Linux and mouse
	goes haywire, moving around at random and clicking buttons. If this
	happens I can get things back to normal by switching in and out of
	another virtual console.


(If that means nothing to you, here is the long
	explanation. Linux boxes have multiple virtual consoles. If you are
	in text mode you can switch between these by pressing alt-f1, alt-f2
	etc and get a different login. If you are in X windows you use
	ctrl-alt-f1 etc. To get back to X you keep pressing alt-f1, alt-f2
	etc till you find which virtual console displays X - in my case
	(debian) it's alt-f7. So I get out of trouble my going ctrl-alt-f5
	followed by alt-f7. I don't know why I use f5 on the first key
	press, anything from 1-6 should work.)


Switching in and out of virtual consoles is a pain, of course.
I've been playing around with installs recently and noticed some did
had this mouse madness and  some didn't. I haven't done any detailed
troubleshooting on this, but I did swap the mouse definitions in my
XF86Config file.


The one that had a problem was from a RedHat 9 install.


```

Section âInputDeviceâ
        Identifier  âMouse0â
        Driver      âmouseâ
        Option      âProtocolâ âIMPS/2â
        Option      âDeviceâ â/dev/psauxâ
        Option      âZAxisMappingâ â4 5â
        Option      âEmulate3Buttonsâ ânoâ
EndSection

```


I changed this to


```

Section âInputDeviceâ
        Identifier  âPS/2 Mouseâ
        Driver      âmouseâ
        Option      âProtocolâ âautoâ
        Option      âZAxisMappingâ          â4 5â
        Option      âDeviceâ â/dev/psauxâ
        Option      âEmulate3Buttonsâ âtrueâ
        Option      âEmulate3Timeoutâ â70â
        Option      âSendCoreEventsâ  âtrueâ
EndSection

```


This came from a morphix install. (The Morphix install had other
	problems with my monitor.) I won't try to figure out what the
	important change is, I'm pretty ignorant of X and would like to be
	more so.


To make the change visible in the file I changed another section
	from


```

Section âServerLayoutâ
	Identifier     âDefault Layoutâ
	Screen      0  âScreen0â 0 0
	InputDevice    âMouse0â âCorePointerâ
	InputDevice    âKeyboard0â âCoreKeyboardâ
	InputDevice    âDevInputMiceâ âAlwaysCoreâ
EndSection
```


to


```

Section âServerLayoutâ
        Identifier     âDefault Layoutâ
        Screen      0  âScreen0â 0 0
        InputDevice    âPS/2 Mouseâ âCorePointerâ #imported from Morphix install
        InputDevice    âKeyboard0â âCoreKeyboardâ
#commented out as Morphic didn't have it
#       InputDevice    âDevInputMiceâ âAlwaysCoreâ 
EndSection

```


Now I don't have mouse jigger problems on that machine. However
	when I do switch in the mouse won't respond till I shake it around a
	bit - I can live with that. Sometimes it's been a while before it
	responds and switched in and out of the windows box and/or the
	virtual consoles before it responds. I can live with that too.


One day I hope someone or something will make configuring X as
easy as it is to get windows to work. At the moment this is one of the
most painful parts of using Linux as a desktop machine.
