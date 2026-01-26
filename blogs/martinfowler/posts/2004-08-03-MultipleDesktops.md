---
title: "Multiple Desktops"
description: "A couple of years ago I changed an important aspect of my 		working life. Before then I tried to work on only one computer (or 		more strictly only one hard drive). All my working files were kept 		on"
date: 2004-08-03T00:00:00
tags: ["writing"]
url: https://martinfowler.com/bliki/MultipleDesktops.html
slug: MultipleDesktops
word_count: 384
---


A couple of years ago I changed an important aspect of my
		working life. Before then I tried to work on only one computer (or
		more strictly only one hard drive). All my working files were kept
		on my laptop hard drive. If I used a desktop machine I used those
		files through file sharing facilities.


This changed last year when I bought my powerbook. Now I swap
		regularly between three computers: mac powerbook, windows laptop,
		and Ubuntu desktop.


All of this means I need to keep multiple machines up to date
		with each other - at least as far as my working files are
		concerned. I've been greatly helped by the fact that just as I
		went to multiple desktops, my main email service shifted from POP
		to IMAP. Despite some hiccups, I can say that IMAP (I use
		Thunderbird as my client) works very well across multiple
		machines.


Most of my working files are coordinated by Subversion. Any time I
		switch machines I commit my working directory and do an update on
		my new machine. Everything keeps nicely synced, and I get full
		version control too.


Some synchronizations aren't as good as I'd like. Keeping my
		address books straight is awkward. Thunderbird insists on putting
		them in a particular place, which puts them out of the Subversion check.
		Furthermore it's binary, which makes merging harder. This is
		particularly annoying as I like the fact that Thunderbird works
		with textual files for email - which adds to my comfort when
		hiccups do happen. And then the sync with the PDA is awkward
		too. I could really do with a decent way to sync up all my
		contacts and calendar stuff across these platforms. Another area
		is news aggregators. They can share feeds through OPML (at least
		in theory) but not keep track of what I've read and what I haven't.


Keeping to text files as much as possible is useful. As I do all
		my [writing 
			in XML](https://martinfowler.com/articles/writingInXml.html), all I need is a text editor to keep my writing work
		in sync. Diagrams are more of an issue, as there isn't anything
		that works for me on all platforms. But of course part of the
		advantage of the multiple computer setup is that I can use any
		application that's particular to one system.
