---
title: "3D positional audio and HRTFs"
date: 2006-01-20
url: https://blog.codinghorror.com/3d-positional-audio-and-hrtfs/
slug: 3d-positional-audio-and-hrtfs
word_count: 1260
---

I’ve always been fascinated with 3d positional audio through [headphones](https://blog.codinghorror.com/headphone-snobbery/). The nice thing about headphones is that they don’t bug your neighbors or your wife – and they’re actually the best way to [hear surround sound](http://www.dansdata.com/spkvshead.htm), too:


> *But for some surround sound, particularly 3D positional computer audio, headphones can actually work better than speakers.
> The reason for this is that you’ve only got two ears. The way you tell whether a sound’s in front, behind or above you, rather than just to your left or your right, is by processing the complex differences in phase, time delay and frequency balance that’re imparted to differently located sounds by nearby objects (like walls), and by the sonic characteristics of your head.
> Your pinnae – the outer parts of your ears – strongly influence sound waves that pass through and bounce off them. 3D game audio uses Head Related Transfer Function (HRTF) algorithms to fake the effects of the pinnae, the head and various listening environments, so that injecting the sound straight into the ear canal can produce the impression of real 3D audio sources.
> When you’ve got HRTF-massaged two-channel audio already, for instance when you’re playing a game, headphones are obviously the best way to get the sound into your head. There’s no way for speakers to do the job as well, because there’s no way for them to stop each ear hearing the sound that’s intended for the other.*


There’s a long history of audiophile interest in stereo and binaural recordings, but 3d sound on a computer is [a bit different](https://web.archive.org/web/20060218114630/http://www.hitl.washington.edu/scivw/EVE/I.B.1.3DSoundSynthesis.html):

kg-card-begin: html

> **Monaural sound** is a recording of a sound with one microphone. No sense of sound positioning is present in monaural sound.
> **Stereo sound** is recorded with two microphones several feet apart separated by empty space. Most people are familiar with stereo sound; it is heard commonly through stereo headphones and in the movie theater. When a stereo recording is played back, the recording from one microphone goes into the left ear, while the recording from the other microphone is channeled into the right ear. This gives a sense of the sound’s position as recorded by the microphones. Listeners of stereo sound often perceive the sound sources to be at a position inside the listener’s head – that’s because humans do not normally hear sounds this way, separated by empty space. The human head should be there acting as a filter to incoming sounds.
> **Binaural recordings** sound more realistic, as they are recorded in a manner that more closely resembles the human acoustic system: with the recording microphones embedded in a dummy head. Binaural recordings sound closer to what humans hear in the real world; the dummy head filters sound in a manner similar to the human head.
> **3D sound** attempts to take binaural recordings one step further by recording sounds with tiny probe microphones in the ears of a real person. These recordings are compared with the original sounds to compute the person’s head-related transfer function. The HRTF is a linear function that is based on the sound source’s position and takes into account many of the cues humans used to localize sounds. The HRTF is used to develop pairs of finite impulse response (FIR) filters for specific sound positions; each sound position requires two filters, one for the left ear, and one for the right. To place a sound at a certain position in virtual space, the set of FIR filters that correspond to the position is applied to the incoming sound, yielding spatial sound.

kg-card-end: html

Your ear shape (a.k.a. your pinnae) has a dramatic effect on [how you hear sound](http://en.wikipedia.org/wiki/Sound_localization). But don’t take my word for it – hear it for yourself. The 3D hearing test page has a [binaurally recorded sound sample](https://web.archive.org/web/20060213075246/http://www.waisman.wisc.edu/hdrl/take_Test.html) using eight different ear shapes.


![](https://blog.codinghorror.com/content/images/2025/05/image-162.png)


You can hear your PC sound card perform HRTFs using RightMark’s [3DSound Positioning Accuracy test](http://audio.rightmark.org/products/rm3ds.shtml). Note that you must switch to **DirectSound3D Hardware mode** (or better) via the System menu to hear anything more than stereo positioning!


![](https://blog.codinghorror.com/content/images/2025/05/image-163.png)


If your card supports EAX modes, try those too. However, when using EAX, make sure you switch to the “plain” environment for apples-to-apples testing. For some reason it defaults to “generic”, which colors the sound a bit.


HRTF functions magically convert stereo sound into 3D sound, but they are **computationally expensive**. That’s probably why DirectSound Software mode offers no HRTFs. You need an add-in sound card with hardware acceleration to achieve 3D sound with headphones. The first PC sound card to offer 3D positional sound was the Aureal Vortex via [the A3D API](http://en.wikipedia.org/wiki/A3D) circa 1998. I was a huge fan. But unfortunately, Aureal isn’t around any more.


So called “onboard” sound – the kind you get on your motherboard for free – has improved, but it generally has lower sound quality than a dedicated sound card, and it’s certainly not capable of meaningful hardware acceleration. **Onboard sound is simply not an option if you’re a gamer of any kind.** Although I grudgingly installed Creative sound cards in my PCs after the demise of Aureal, it was only because I had no other viable options. I always felt that Creative’s 3D sound HRTF algorithms were never as good as Aureal’s. Creative’s [new X-Fi sound cards](https://web.archive.org/web/20250109002132/https://en.creative.com/soundblaster/), however, are finally poised to change that. For one thing, they have a lot more horsepower:

kg-card-begin: html


| Sound Blaster Live! | 1998 | 2 million transistors |
| Sound Blaster Audigy 2 | 2002 | 4.1 million transistors |
| Pentium 4 "Northwood" 2.0GHz | 2002 | 55 million transistors |
| Sound Blaster X-Fi | 2005 | 51 million transistors |


kg-card-end: html

The X-Fi sound cards are also comically overpriced. *Three hundred bucks* for a sound card? But the lowest-end model, **the X-Fi XtremeMusic, sacrifices almost nothing compared to the fancier models and is priced within reason at around $110** online. That’s still double the cost of an Audigy 2, but unlike the last umpteen zillion Creative sound card “upgrades”, you get a much more powerful card this time with some truly useful new features:

- Up to 128 simultaneous sounds
- Vastly improved CMSS-3D headphone HRTFs
- Real time Smart Volume Management aka dynamic range compression
- Real time upsampling of 16-bit sound to 24-bit


If you’re looking for performance improvements over an earlier Sound Blaster card, there are none. It’s just more functionality with no performance loss. For more details, check out [Extremetech’s review of the X-Fi](https://web.archive.org/web/20060209045525/http://www.extremetech.com/article2/0,1697,1850381,00.asp) by my pal Loyd Case.


I’ve been testing the [X-Fi with Battlefield 2](https://web.archive.org/web/20060324163621/http://www.soundblaster.com/products/x-fi/technology/battlefield2/). It’s one of the only two games that explicitly supports the new card’s features at the moment (the other being the execrable Quake 4). I always play with headphones, and **I noticed the improved 3D sound HRTFs immediately**. The sound is also much richer with 128 voices; it’s easy to exceed the previous limit of 64 simultaneous sounds in large multiplayer games. I’m very impressed. I also tried the card with Doom 3 using the [1.3 EAX patch](https://web.archive.org/web/20060207125748/http://soundblaster.com/Gaming/doom3/?downloadtypedesc=12) and noticed similar improvements.


Although the X-Fi is a wee bit spendy, I can heartily recommend [the basic model](https://web.archive.org/web/20060823100608/http://castle.pricewatch.com/s/search.asp?s=+X-Fi+XtremeMusic+) to fans of 3D audio and headphones. And if you want a clean, non-cluttered install, don’t bother with the CD in the box. Just [download the latest X-Fi drivers](https://web.archive.org/web/20060128081352/http://us.creative.com/support/downloads/) from Creative’s website and install those instead.


![](https://blog.codinghorror.com/content/images/2025/05/image-164.png)


The Creative Audio Console comes with the base driver, and it’s all you need to configure the card.

[audio programming](https://blog.codinghorror.com/tag/audio-programming/)
[3d audio](https://blog.codinghorror.com/tag/3d-audio/)
[hrtfs](https://blog.codinghorror.com/tag/hrtfs/)
[surround sound](https://blog.codinghorror.com/tag/surround-sound/)
[headphones](https://blog.codinghorror.com/tag/headphones/)
