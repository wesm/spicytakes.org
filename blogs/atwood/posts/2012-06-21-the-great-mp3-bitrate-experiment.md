---
title: "The Great MP3 Bitrate Experiment"
date: 2012-06-21
url: https://blog.codinghorror.com/the-great-mp3-bitrate-experiment/
slug: the-great-mp3-bitrate-experiment
word_count: 1482
---

Lately I’ve been trying to rid my life of as many physical artifacts as possible. I’m with Merlin Mann on CDs:


![Can't believe how quickly CDs went from something I hate storing to something I hate buying to something I hate merely existing.](https://blog.codinghorror.com/content/images/2025/09/image-14.png)


Although I’d extend that line of thinking to DVDs as well. The death of physical media [has some definite downsides](https://blog.codinghorror.com/books-bits-vs-atoms/), but after owning certain movies once on VHS, then on DVD, and finally on Blu-Ray, I think I’m now at peace with the idea of **not owning any physical media ever again**, if I can help it.


My current strategy of wishing my physical media collection [into a cornfield](http://en.wikipedia.org/wiki/It's_a_Good_Life_(The_Twilight_Zone)) involves shipping all our DVDs to Second Spin via media mail, and paying our nephew $1 per CD to rip our CD collection using [Exact Audio Copy](http://www.exactaudiocopy.de/) and [LAME](http://lame.sourceforge.net/) as a summer project. The point of this exercise is absolutely *not* piracy; I have no interest in keeping both digital and physical copies of the media I paid for the privilege of owning temporarily licensing. Note that I didn’t bother ripping any of the DVDs because I hardly ever watched them; mostly they just collected dust. But [I continue to love music](https://blog.codinghorror.com/living-the-dream-rock-band/) and listen to my music collection on a daily basis. I’ll donate all the ripped CDs to some charity or library, and if I can’t pull that off, I’ll just destroy them outright. *Stupid atoms!*


CDs, unlike DVDs or even Blu-Rays, are considered **reference quality**. That is, the uncompressed digital audio data contained on a CD is a nearly perfect representation of the original studio master, for most reasonable people’s interpretation of “perfect,” [at least back in 1980](http://en.wikipedia.org/wiki/Compact_Disc#Audio_CD). So if you paid for a CD, you might be worried that ripping it to a *compressed* digital audio format would result in an inferior listening experience.


I’m not exactly an audiophile, but I like to think I have pretty good ears. I’ve recommended [buying $200+ headphones](https://blog.codinghorror.com/headphone-snobbery/) and [headphone amps](https://blog.codinghorror.com/who-needs-a-sound-card-anyway/) for quite a while now. By the way: still a good investment! Go do it! Anyhow, previous research and my own experiments led me to write [Getting the Best Bang for Your Byte](https://blog.codinghorror.com/variable-bit-rate-getting-the-best-bang-for-your-byte/) seven years ago. I concluded that **nobody could really hear the difference between a raw CD track and an MP3 using a decent encoder at a variable bit rate averaging around 160kbps**. Any bit rate higher than that was just wasting space on your device and your bandwidth for no rational reason. So-called “high resolution audio” was recently thoroughly [debunked for very similar reasons](http://people.xiph.org/~xiphmont/demo/neil-young.html).


> Articles last month revealed that musician Neil Young and Apple’s Steve Jobs [discussed offering digital music downloads](http://www.appleinsider.com/articles/12/02/01/neil_young_was_working_with_apple_on_super_high_def_music_format_.html) of ‘uncompromised studio quality.’ Much of the press and user commentary was particularly enthusiastic about the prospect of uncompressed 24 bit 192kHz downloads. 24/192 featured prominently in my own conversations with Mr. Young’s group several months ago.
> Unfortunately, there is no point to distributing music in 24-bit/192kHz format. **Its playback fidelity is slightly inferior to 16/44.1 or 16/48, and it takes up 6 times the space.**
> There are a few real problems with the audio quality and ‘experience’ of digitally distributed music today. 24/192 solves none of them. While everyone fixates on 24/192 as a magic bullet, we’re not going to see any actual improvement.


The authors of LAME must have agreed with me, because the typical, standard, recommended, default way of encoding any old audio input to MP3…

kg-card-begin: html

```

lame –preset standard “cd-track-raw.wav” “cd-track-encoded.mp3”

```

kg-card-end: html

… now produces variable bit rate MP3 tracks at a bitrate of around 192kbps on average.


![](https://blog.codinghorror.com/content/images/2025/04/image-648.png)


(Going down one level to the “medium” preset produces nearly exactly 160kbps average, my 2005 recommendation on the nose.)


Encoders have only gotten better since the good old days of 2005. Given the many orders of magnitude improvement in performance and storage since then, I’m totally comfortable with throwing an additional 32kbps in there, going from 160kbps average to 192kbps average *just to be totally safe*. That’s still a miniscule file size compared to the enormous amount of data required for mythical, aurally perfect raw audio. For a particular 4 minute and 56 second music track, that’d be:

kg-card-begin: html


| Uncompressed raw CD format | 51 mb |
| Lossless FLAC compression | 36 mb |
| LAME insane encoded MP3 (320kbps) | 11.6 mb |
| LAME standard encoded MP3 (192kbps avg) | 7.1 mb |


kg-card-end: html

Ripping to uncompressed audio is a non-starter. I don’t care how much of an ultra audio quality nerd you are, spending 7× or 5× the bandwidth and storage for **completely inaudible** “quality” improvements is a dagger directly in the heart of *this* efficiency-loving nerd, at least. Maybe if you’re planning to do a lot of remixing and manipulation it might make sense to retain the raw source audio, but for typical listening, never.


The difference between the 320kbps track and the 192kbps track is more rational to argue about. But **it’s still 1.6 times the size**. Yes, we have tons more bandwidth and storage and power today, but storage space on your mobile device will never be free, nor will bandwidth or storage in the cloud, where I think most of this stuff should ultimately reside. And all other things being equal, wouldn’t you rather be able to fit 200 songs on your device instead of 100? Wouldn’t you rather be able to download 10 tracks in the same time instead of 5? Efficiency, that’s where it’s at. Particularly when people with dog’s ears wouldn’t even be able to hear the difference.


### But Wait, I Have Dog Ears


Of course you do. [On the Internet, nobody knows you’re a dog.](http://en.wikipedia.org/wiki/On_the_Internet,_nobody_knows_you're_a_dog) Personally, I think you’re a human being full of crap, but let’s drop some science on this and see if you can prove it.


![](https://blog.codinghorror.com/content/images/2025/04/image-647.png)


When someone tells me “Dudes, come on, let’s steer clear of the worst song ever written!” I say *challenge accepted*. Behold **The Great MP3 Bitrate Experiment!**


As proposed on our very own [Audio and Video Production Stack Exchange](http://avp.stackexchange.com/questions/1406/are-there-any-audible-differences-between-192-and-320-kbit-s-mp3-files), we’re going to do a blind test of the same 2 minute excerpt of a particular rock audio track at a few different bitrates, ranging from 128kbps CBR MP3 all the way up to raw uncompressed CD audio. Each sample was encoded (if necessary), then exported to WAV so they all have the same file size. Can you tell the difference between any of these audio samples *using just your ears?*


### 1. Listen to each two minute audio sample


(update: experiment concluded; links removed.)

kg-card-begin: html


| Limburger |
| Cheddar |
| Gouda |
| Brie |
| Feta |


kg-card-end: html

### 2. Rate each sample for encoding quality


Once you’ve given each audio sample a listen – *with only your ears please, not analysis software* – **fill out this brief form and rate each audio sample from 1 to 5** on encoding quality, where one represents worst and five represents flawless.


Yes, it would be better to use a variety of different audio samples, [like SoundExpert does](http://soundexpert.org/testing-room), but I don’t have time to do that. Anyway, if the difference in encoding bitrate quality is as profound as certain vocal elements of the community would have you believe it is, that difference should be audible in *any* music track. To those who might argue that I am trolling audiophiles into listening to one of the worst-slash-best rock songs of all time… over and over and *over*… to prove a point… I say, how dare you impugn my honor in this manner, sir. *How dare you!*


I wasn’t comfortable making my [generous TypePad hosts](https://blog.codinghorror.com/welcome-back-comments/) suffer through the bandwidth demands of multiple 16 megabyte audio samples, so this was a fun opportunity to exercise my long dormant Amazon S3 account, and test out Amazon’s on-demand [CloudFront CDN](http://aws.amazon.com/cloudfront/). I hope I’m not rubbing any copyright holders the wrong way with this test; I just used a song excerpt for science, man! I’ll pull the files entirely after a few weeks just to be sure.


You’ll get no argument from me that the old standby of 128kbps constant bit rate encoding is not adequate for most music, even today, and you should be able to hear that in this test. But I also maintain that virtually nobody can reliably tell the difference between a 160kbps variable bit rate MP3 and the raw CD audio, much less 192kbps. If you’d like to prove me wrong, this is your big chance. Like the announcer in Smash TV, I say *good luck – you’re gonna need it*.


So which is it – **are you a dog or a man?** Give the samples a listen, then rate them. I’ll post the results of this experiment in a few days.

[mp3](https://blog.codinghorror.com/tag/mp3/)
[bitrate](https://blog.codinghorror.com/tag/bitrate/)
[digital media](https://blog.codinghorror.com/tag/digital-media/)
[exact audio copy](https://blog.codinghorror.com/tag/exact-audio-copy/)
[lame](https://blog.codinghorror.com/tag/lame/)
