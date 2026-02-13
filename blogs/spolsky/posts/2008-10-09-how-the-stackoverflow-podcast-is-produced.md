---
title: "How the StackOverflow Podcast is produced"
date: 2008-10-09
url: https://www.joelonsoftware.com/2008/10/09/how-the-stackoverflow-podcast-is-produced/
word_count: 826
---


The [Stack Overflow Podcast](http://blog.stackoverflow.com/) is a weekly conversation between me and [Jeff Atwood](http://www.codinghorror.com/blog/). He lives in California and I’m in New York City, so it has been a bit of a technical challenge to get the audio quality up to FM radio quality.


We went through several different iterations trying to find the perfect setup to record the podcast.


The first few shows were done by phone. Our office [Asterisk](http://www.asterisk.org/) phone system includes a feature to record any conversation by pressing ** during a call. The sound quality was *really* low ([sample [MP3]](https://www.joelonsoftware.com/pictures/soundsnip1.mp3)).


For a few months we used a combination of [Skype](http://www.skype.com/) and [Pamela](http://www.pamela-systems.com/). Pamela has a feature that allowed me to record Skype conversations as a high quality WAV file. The sound quality was great, but there was one problem: if Jeff and I spoke at the same time, the recording would, for some reason, drop *both* of us ([sample [MP3]](https://www.joelonsoftware.com/pictures/soundsnip2.mp3)). We had to learn to be careful not to speak over each other and not to interrupt each other. This made the conversation sound stilted, and sometimes interesting things got lost. Another problem was that sounds from my computer weren’t recorded as a part of the podcast unless I prepared them as Pamela sound effects.


I knew that we needed a system that could record my voice locally, directly from the microphone, while recording the Skype conversation separately. I took some inspiration from [Leo Laporte’s podcasting setup](http://www.twit.tv/podcastequipment) and [Doug Kaye’s suggested setup](http://www.blogarithms.com/index.php/archives/2005/07/14/interviews-via-skype/) in building my own, which we started using in episode #25.


Here’s the basic schematic:


Here’s what it looks like:


**HEADSET: **The headset there is a [Sennheiser HMD-281-13](http://www.sennheiserusa.com/newsite/productdetail.asp?transid=004979), very high quality studio mic and headphone, which does a terrific job of cutting out noise.


**STUDIO MIXER: **I’m using a small DJ mixer that we happened to have sitting around to mix my voice with any sounds coming out of the computer, which I use to play audio files submitted by users. If you’re building your own setup, any kind of mixer will work as long as it has an XLR input with a preamp for the mic, and a line-level input for computer sound. I’m taking advantage of the fact that this mixer is stereo, even though everything I do is mono, so I can record from the left channel while sending the (identical) right channel over Skype to Jeff.


**RECORDING MIXER:** I got a [Fostex MR16HD](http://www.fostexusa.com/index.php?file=products/digital/mr16hd) from Zzounds:


This mixes together the studio mixer (my voice and computer sound) with Jeff’s voice from Skype, and records it all on a big internal hard drive.


I’m using two separate [M-Audio MobilePre USB](http://www.m-audio.com/products/en_us/MobilePreUSB.html) preamps. These are basically external, high quality sound cards, connected to the computer (and drawing power) via USB.


The first one provides an audio input and output channel to the computer used exclusively for the Skype conversation. The second one is simply a high-quality replacement for the crappy sound card built into the computer; it feeds sounds from the computer to the studio mixer and also to a set of speakers, which I turn off while recording to avoid feedback.


Skype, like most Windows programs, is pretty flexible about letting you choose which signal goes to which sound card when you have several installed:


This is especially convenient when you want Skype to ring on the speaker, while playing sound through the headset.


Once the podcast is over, I transfer the audio file (in uncompressed WAV format) from recording mixer to the computer, where I edit it in [Audacity](http://audacity.sourceforge.net/). I don’t do much editing; usually just chopping off the beginning and the end of the recording, and, occasionally, removing things that one of us really regretted saying. Finally, I run the whole WAV file through [The Levelator](http://www.conversationsnetwork.org/levelator), a fantastic little app developed by the folks at [The Conversations Network](http://www.conversationsnetwork.org/) (who host the podcast). The Levelator takes an entire podcast and adjusts the volumes automatically so that every speaker comes out at the same volume. It’s pretty much magic and eliminates any need to monitor or adjust levels during the recording.


The setup works great. We can talk over one another without dropouts ([sample [MP3]](https://www.joelonsoftware.com/pictures/soundsnip3.mp3)), which makes for a much livelier show, and the sound is near FM quality.


**Can’t this all be done in software?**


Yes! All the cables and analog mixers seem like a ridiculous way to set this up. I’m sure it can all be done with software, which, indeed was something I spent many many hours trying to get to work. There are a lot of little apps that cost $20 that claim to allow you to create virtual sound cards and virtual cables between them, all in software. I couldn’t figure any of them out, but I am pretty handy with an XLR cable, so this is the big hardware kludge I came up with. But it is a big kludge… I’d love to see step by step instructions for doing this properly in software.
