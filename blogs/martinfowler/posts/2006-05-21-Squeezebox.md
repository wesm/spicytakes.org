---
title: "Squeezebox"
description: "One of our favorite toys over the last couple of years has been theSqueezebox. It's a very simple device - about the size of a router, with ports for power, Ethernet,  amplifier, and aerials for wirel"
date: 2006-05-21T00:00:00
tags: ["gadgets"]
url: https://martinfowler.com/bliki/Squeezebox.html
slug: Squeezebox
word_count: 223
---


One of our favorite toys over the last couple of years has been the
[Squeezebox](http://www.slimdevices.com). It's a very simple device - about
the size of a router, with ports for power, Ethernet, 
amplifier, and aerials for wireless LAN. Its job is to take mp3 files streamed from a server and
play them through the amplifier.


The nice thing about it is that it means you can put all your music on
a single server (in my case the Debian box in my basement) and then
just use a squeezebox to play the music wherever you want it. I have one in
the living room, one in the office, one in the bedroom (wireless), and
one out on the porch. You control the squeezebox with
either a remote control or a web page. You can easily choose
playlists, folders of music or whatever. The files are streamed by an
open source perl server that runs on the server.


I've gone ultra-automated. Every night a ruby script runs on the
server and generates themed random playlists. That way I can have two
hours of 18th century classical music followed by an hour of blues
without having to make any decisions about what to listen to.


It's certainly made using mp3s a pleasure at home, and now the CDs are
relegated to boxes in the basement.
