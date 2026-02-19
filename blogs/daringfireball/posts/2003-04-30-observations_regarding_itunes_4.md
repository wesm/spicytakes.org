---
title: "Observations Regarding iTunes 4"
date: 2003-04-30
url: https://daringfireball.net/2003/04/observations_regarding_itunes_4
slug: observations_regarding_itunes_4
word_count: 707
---


## Shared Music Breaks Scripting


While the iTunes Music Store is getting much of the press, my favorite feature in iTunes 4 is the music sharing. It’s fast, it’s simple, and works great.


As [Chris Nandor points out](http://use.perl.org/~pudge/journal/11890), however, it breaks iTunes’s scripting interface. What happens is that if you’re listening to a shared library and try to do this:


```

tell application "iTunes"
    get current track
end tell

```


iTunes returns an error (which Script Debugger reports as an “Unknown object type”).


This bug breaks all sorts of useful things you can do with iTunes via AppleScript. Getting properties on the current track is how all the numerous “What’s Currently Playing in iTunes” widgets work (for example, I’m pretty sure this is how [Kung-Tunes](http://kung-foo.tv/itti.php) does its thing). It’s only broken for iTunes shared music — it still works just fine with tracks in your own library, as well as for other streams, such as iTunes’s “Radio” sources.


Nandor has also done some detective work on [how to turn streamed music into MP3 files](http://use.perl.org/~pudge/journal/11922) — it’s neither easy nor convenient, but it’s always fun to see how things work.


## Lock-In?


[Rafe Colburn is suspicious](http://rc3.org/cgi-bin/less.pl?arg=5178):


> Something occurred to me last night about Apple’s new music service. The killer advantage here for Apple is that their DRM locks Mac users into the Mac platform for the long term. Maybe this will change, but right now you can only play the tracks purchased through Apple’s music service on a Mac. Once you’ve bought an iPod’s worth of music, you have several gigs of reasons why switching from your Mac to a PC would be a really, really bad idea. I guess you could go to the trouble of ripping all your songs onto CD and then ripping them back onto your PC as MP3s, but that brings about a loss of quality and is a huge pain to boot. Maybe I’m way off here and soon there will be a PC app that will Apple’s audio files, but in the meantime, this looks like a particularly fiendish way to make sure that people who switch stay switched.


“Fiendish” seems like a terribly loaded word here. What could Apple possibly have done differently? From a consumer standpoint, sure, it’d be great if Apple’s music store were selling music files in a completely open cross-platform format, with no rights management at all. *But the music labels would never have agreed to this.* If you start from the idea that there must be some form of rights management involved, what Apple has come up with is very much in consumers’ favor. It’s not subscription-based. It’s not time-limited. There are no hidden fees. There are no pop-up ads. You get to burn CDs, and you get to listen to the AAC files on up to three computers.


Once someone has purchased a large library of music from the iTunes Music Store, will that act as an enticement to stay with the Mac? Sure. But I fail to see how it’s a fiendish scheme — it’s a value added feature of the Mac OS. Fiendish would be if the new version iTunes somehow forced or tricked you into creating a music library dependent on Apple — like if it translated all your MP3 files into a proprietary format, or insisted upon using a proprietary format when ripping music from CDs. The fact is, there’s nothing in iTunes 4 that prevents you from listening to digital music the same way you did before the iTunes Music Store — you can still encode your own music in MP3 format, and you can still play bootleg MP3 files. The iTunes Music Store is something *more*, not something *else*.


## Micropayments


Perhaps the biggest mystery regarding the Music Store is how Apple solved the micropayments problem: credit card companies typically take at least $0.25 or more from each transaction, thus making very small charges (like $0.99) unfeasible. Yet somehow Apple has pulled it off.


Jonathan Rentzsch, the man with more consecutive consonants in his name than anyone else on Earth, [has a theory how Apple is doing it](http://rentzsch.com/notes/creditCardMicropayments).



| **Previous:** | [RTF to Plain Text Translator](https://daringfireball.net/2003/04/rtf_to_plain_text_translator) |
| **Next:** | [Interface Details: iTunes vs. Safari](https://daringfireball.net/2003/05/interface_details_itunes_vs_safari) |


PreviousNext