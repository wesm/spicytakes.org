---
title: "On Audio Visualization"
date: 2006-02-09
url: https://blog.codinghorror.com/on-audio-visualization/
slug: on-audio-visualization
word_count: 1116
---

I’m a big music fan. And as a longtime computer enthusiast, I’ve always been intrigued by the intersection of computers and music: **audio visualization**. The first experience I had with visualization was the 1993 CD-ROM add-on for [Atari’s short-lived Jaguar console](http://www.atariage.com/Jaguar/archives/hardware/). It included [Jeff Minter’s VLM-1](http://llamasoft.co.uk/vlm.php) (Visual Light Machine) burned into the firmware:

kg-card-begin: html

> Atari [was] developing a CD-ROM add-on for the Jaguar, and me and Ian Bennett, one of the Inmos guys, flew out to Sunnyvale to pitch them the idea of building a VLM implementation into the CD-ROM's firmware, to be invoked whenever the user played an audio CD. I was in particularly good favour at Atari, since “Tempest 2000” had been released to a degree of critical approval, and we got the green light to develop VLM for the add-on. It took about six months to make, with me doing all the graphical stuff and Ian writing the code to sample the audio stream and generate a frequency spectrum analysis which I then used to drive the visuals.
>     The results were very pleasing – I have vivid memories of going into the office in Sunnyvale when we were out there finishing off the code, and finding Leonard Tramiel playing classical music through it and dancing ecstatically around my cube.

kg-card-end: html

The VLM-1 was just the latest in this [llama-obsessed developer’s](https://web.archive.org/web/20090729181855/http://www.geocities.com/rmelick/19.htm) series of software experiments with audio visualization, going all the way back to 1984...

kg-card-begin: html


| [Psychedelia](http://llamasoft.co.uk/psychedelia.php) | 1984 | Commodore 64 |
| [Colourspace](http://llamasoft.co.uk/colourspace.php) | 1985 | Atari 400/800, Atari ST |
| [Trip-a-tron](http://llamasoft.co.uk/ttron.php) | 1987 | Amiga, Atari ST |
| [VLM-0](http://llamasoft.co.uk/vlm.php) | 1990 (unreleased) | [Inmos Transputer](http://en.wikipedia.org/wiki/Transputer) |
| [VLM-1](http://llamasoft.co.uk/vlm.php) | 1994 | Atari Jaguar CD-ROM |
| [VLM-2](http://llamasoft.co.uk/vlm.php) | 2000 | [Nuon](http://en.wikipedia.org/wiki/Nuon) |
| [VLM-3](http://llamasoft.co.uk/vlm.php) | 2003 (unreleased) | Gamecube |
| [Neon](http://llamasoft.co.uk/neon.php) | 2005 | Xbox 360 |


kg-card-end: html

... and ending with the Xbox 360. It was quite a coup for Microsoft to get Minter to write the visualization software embedded in every Xbox 360:


> [Neon] finally realizes my design of a modular lightsynth on top of that awesome computational power, and inheriting the multi-user controllability from VLM-3, and the results are simply amazing. Even I am continually amazed at what it is possible to get out of it, and I designed it. It is a true light synthesiser, and easily the most beautiful thing I have ever made, by a very long way. We thought VLM-3 was good, but this makes VLM-3 look like Psychedelia. It’s truly a generational increment – hence after years of long service I decided it’s finally time to lose the VLM name.
> It can be used purely as a visualizer – but a visualizer which instantly obsoletes all those still currently struggling along with VLM-1 techniques straight into the Stone Age. Or you can pick up the controllers and feel what it’s like to fly it as a Crew. It is truly a thing of beauty... I believe it finally begins to achieve the potential that I saw all those years ago when I first made Psychedelia... and I am happier with it than I have ever been with anything I’ve created in my entire career.


Talking about the Neon visualization doesn’t do it justice. You have to see it in action to appreciate how impressive it really is. If you have an Xbox 360, rip an audio CD and try it yourself. If you don’t, Minter provides [screenshots](http://www.llamasoft.co.uk/neon-screenshots.php) and [movies](http://www.llamasoft.co.uk/neon-movies.php).


I remember looking around in vain for PC audio CD visualization software in 1996; **it took the MP3 revolution and WinAmp to make audio visualization mainstream** several years later. Minter clearly influenced an entire generation of PC programmers:


> A while after [the Atari Jaguar’s CD-ROM add-on] was released, other “visualisers” started to appear on the PC, and at one time I was at a computer show in the US and one of the guys from Nullsoft came up to me and apologized for “borrowing” the techniques I’d used on the Jaguar VLM for their own visualisations. And, in fact, to this day much of the visualisation stuff that you see in the likes of Winamp, Windows Media Player and iTunes uses fundamentally the same technique – using feedback to amplify small source input dynamics – that I used in VLM-1.


Although the grandaddy of the PC visualization scene is the DOS based [Cthuga](https://web.archive.org/web/20060214161110/http://www.afn.org/~cthugha/), **the breakthrough PC visualizers were both WinAmp plugins: **[**Geiss**](http://www.geisswerks.com/geiss/index.html)** and **[**G-Force**](http://www.soundspectrum.com/g-force/)**. **G-Force, as noted in this 2001 [Wired article](https://web.archive.org/web/20060526111935/http://www.wired.com/news/business/1,42870-0.html), has an interesting history:


> For Andy O’Meara, creating a trend-setting computer graphics program has been a thoroughly depressing experience. After launching his program-turned-phenomenon, O’Meara had to ship out on a five-year tour of duty in the U.S. Navy.
> Last year, O’Meara released G-Force, software that “visualizes” music through an ever-changing stream of trippy graphics that morph and pulse to the music’s beat. G-Force, and other “vis” software like it, are rapidly becoming the equivalent of flying toasters – a wildly popular and instantly recognizable icon of the times, like lava lamps or disco balls.
> But for O’Meara, finding himself at the vanguard of the movement has been anything but uplifting. Thanks to the Navy ROTC scholarship program that paid his way through college, O’Meara spends most of his time on a nuclear submarine when he could be embarking on a multimedia career. He has already been offered the chance to join pop star Seal's forthcoming Togetherland tour, and he signed a lucrative licensing deal with Apple that convinced him he can make a living writing code. “If I wasn’t in the Navy, I’d be on tour with Seal working on visuals for him,” said O’Meara from his home port of San Diego. “Am I depressed about it? Yeah.”


As alluded to in the article, **G-Force was licensed for inclusion in iTunes**. It looks like O’Meara survived [his stint in the Navy](https://web.archive.org/web/20060315004424/http://www.55ware.com/about-andy.html) and is now actively maintaining and selling G-Force, with plugins available for virtually every player out there. Geiss, on the other hand, is still WinAmp-only, and [the latest version](https://web.archive.org/web/20060318160845/http://www.nullsoft.com/free/geiss2/) was released in 2003.


Although G-Force and Geiss are still decent visualizers, they’ve barely evolved at all: they are limited to 8-bit color internally, and make no use of hardware acceleration. On the plus side, they use very little CPU time on a modern PC, either. Seeing the Xbox 360 Neon visualizer next to these two makes them look antiquated:


![](https://blog.codinghorror.com/content/images/2025/05/image-194.png)


![](https://blog.codinghorror.com/content/images/2025/05/image-193.png)


I suppose we’ll have to wait another few years for the audio visualization developers to **catch up to the hardware capabilities of newer PCs**.

[audio visualization](https://blog.codinghorror.com/tag/audio-visualization/)
[music technology](https://blog.codinghorror.com/tag/music-technology/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
