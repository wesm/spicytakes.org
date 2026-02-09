---
title: "Simplest Possible P2P Voice Chat Using Fire★"
date: 2014-07-02
url: https://blog.mempko.com/simplest-possible-voice-chat-app-in-fire-e2-98-85/
slug: simplest-possible-voice-chat-app-in-fire-e2-98-85
word_count: 282
tags: ['peer-to-peer applications', 'play sound', 'voice chat', '#wordpress', '#Import 2024-11-03 23:36']
---



[Fire★](http://www.firestr.com/?ref=blog.mempko.com) is a platform for making writing peer-to-peer applications as simple as possible. I am going to show here how to write the simplest, most dumb and basic voice chat app using Fire★. I have recently added the ability to grab sound from the microphone and play sound through the speaker. With the capability to get raw audio from a microphone, ability to play sound, and the ability to send messages, writing a very basic voice chat app is easy. All Fire★ applications are written in the Lua programming language.


Creating a mic and speaker is easy.


[code language=”javascript”]

m = app:mic("got_sound", "pcm")

s = app:speaker("pcm")

m:start()

[/code]


The constructor for the microphone takes a callback and a codec to use. In this case we will use simple pcm. Whenever audio data is captured from the microphone, got_sound will be called.


[code language=”javascript”]

function got_sound(d)

	local m = app:message()

	m:set_type("s")

	m:set_bin("d", d)

	app:send(m)

end

[/code]


“got_sound” simply takes the pcm audio data, and wraps it in a message to send to all the peers.


[code language=”javascript”]

app:when_message("s", "play_sound")

function play_sound(m)

	s:play(m:get_bin("d"))

end

[/code]


The audio messages are of type ‘s’ and when a peer gets a message of type ‘s’, the “play_sound” function is called. “play_sound” simply plays the pcm audio to the speaker.


This is the code for possibly the simplest peer-to-peer voice chat application you can write. I have checked into GitHub a slightly more complicated version with the basic GUI you see in the screenshot above here: [https://github.com/mempko/firestr/tree/master/src/packaged_apps/voice](https://github.com/mempko/firestr/tree/master/src/packaged_apps/voice?ref=blog.mempko.com)


Of course this is no where near a real voice chat app. I just wanted to demonstrate that there is a basic foundation that can support voice chat. Next up, video!

