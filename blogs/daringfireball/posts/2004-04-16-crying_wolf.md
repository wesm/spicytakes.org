---
title: "Crying Wolf"
date: 2004-04-16
url: https://daringfireball.net/2004/04/crying_wolf
slug: crying_wolf
word_count: 1477
---


First, a summary of last week’s ‘MP3Concept Trojan Horse’ fiasco:

- MP3Concept is indeed a [Trojan horse](http://en.wikipedia.org/wiki/trojan_horse), but the only known
instance is utterly benign — a harmless but quite clever proof
of concept that a single file can be both a CFM Mac application,
and also a valid MP3 audio file. Imagine if the Greeks had built
a gigantic wooden horse, but instead of filling it with army
troops, they had simply left a note inside telling the Trojans
to be careful.
- Technical details aside, the basic idea is that MP3Concept
is an application, with HFS file type ‘APPL’, and the Finder
reports its kind as such.
- Its icon is a copy of iTunes’s MP3 document icon. This icon
has nothing to do with the “.mp3” file name extension, nor is
it a pasted icon set through the Get Info window. It’s the
application’s icon, stored in the file’s resource fork.
- Thus, the icon looks like that of a normal MP3 file,
and the filename, “virus.mp3”, looks like that of a normal
MP3 file. Thus, the CFM trickery that allows the file to work
both as an app and an MP3 file — while clever — is mostly
beside the point. *Any* normal CFM app can be assigned an icon
and file name that make it appear, at a glance, to be a file
and not an app.
- This is not specific to Mac OS X. The “virus.mp3” application
works on both Mac OS X and Mac OS 9.
- No one with any sense would ever claim that Macs are impervious
to viruses, worms, or Trojan horses. *Especially* Trojans — which
just about anyone with a 3-digit IQ could put together. E.g.:

*Voilà* — you just wrote an innocuous Trojan horse.
Now, change step #1 from displaying a harmless dialog box, to, say,
deleting the contents of the current user’s Documents folder,
and you’ve written a dastardly, albeit not particularly clever,
Trojan horse. You don’t even need to be able write AppleScript;
you can simply use Script Editor’s record feature.
  1. Write an AppleScript that displays a dialog,
then quits.
  2. Save it as a script application.
  3. Name it “some_song_title.mp3”.
  4. Use the Finder’s Get Info window to paste the icon
from an iTunes MP3 file onto the script app.
- The crux: it has never been safe to blithely double-click a
“file” downloaded from an untrusted source simply because its
icon looks like that of a normal document.


## Grading the Participants


### Bo Lindbergh


Author of the “virus.mp3” proof-of-concept, which he [posted to
comp.sys.mac.programmer.misc on March 20](http://groups.google.com/groups?th=631707378ffe9292&seekm=blgl-5D750C.02150821032004%40news.bahnhof.se).


**Verdict:** Blameless. Lindbergh’s proof-of-concept is completely
innocuous, and the technical details of his technique are quite
clever. If there’s anything he should have done differently, it’s
the unfortunate name he chose for his demo. “virus.mp3” is not a
virus — it’s a Trojan horse. A file name such as “example.mp3”
would have been better. But, I suspect Lindbergh never imagined the
hubbub his demo ended up provoking.


### Intego


“Macintosh security experts”, makers of VirusBarrier, whose [press
release announcing protection against “MP3Concept”](http://www.intego.com/news/pr40.html) begat the
hysteria.


**Verdict:** Shameless and clueless. Intego’s press release is
riddled with serious inaccuracies. The crux of the press release is
this:


> Due to the use of this technique, users can no longer safely
> double-click MP3 files in Mac OS X. This same technique could be used
> with JPEG and GIF files, though no such cases of infected graphic files
> have yet been  seen.


Which just isn’t true. “virus.mp3” is an application, not a
document, at least in terms of how the Finder treats it on both Mac
OS 9 and OS X. An accurate, non-sensational way of issuing their
warning would have been to say something like: *A malicious
application can be disguised using an icon to make it look like a
document.*


Intego also claims:


> Mac OS X displays the icon of the MP3 file, with an .mp3 extension, 
> rather than showing the file as an application, leading users to
> believe that they can double-click the file to listen to it.


This is false. It’s either a deliberate lie, or written by
someone with no genuine understanding of what’s going on. Either
way, it discredits Intego.


This is how the Finder displays the “virus.mp3” file, in list and
column view:


There’s no question that one might be fooled into thinking it’s an
MP3 document, glancing only at the icon and filename, but in no way
is the Finder erroneously indicating that it is anything but an
application.


Computer security is serious business; warnings about
newly-discovered threats demand precise and accurate technical
descriptions. Intego’s press release regarding the MP3Concept
“threat” is vague and inaccurate. Inexcusable.


### MacJournals


The April 10 issue of [MDJ](http://www.macjournals.com/mdj/) (and the April 11 issue of its weekly
sibling [MWJ](http://www.macjournals.com/mwj/)) contained an exhaustive look at the entire saga,
including an outstanding explanation of the CFM trickery Lindbergh
used to stash both the executable binary code and MP3 data within
the data fork of a single file, analysis of the embarrassing factual
errors in Intego’s statements, and a scathing look at the press
coverage.


**Verdict:** Outstanding, timely, and comprehensive coverage.


(Disclosure: I was an occasional contributor to MDJ in 2003.)


### TidBITS


[Adam Engst’s coverage in TidBITS #726](http://db.tidbits.com/getbits.acgi?tbart=07636) covers fewer technical details than
MDJ’s report (as befits the TidBITS readership), but is equally lucid.


**Verdict:** Everything a Mac user ought to know about the threat of Trojan horses.


### Wired News


Leander Kahney’s initial report was headlined [“Trojan Horse Attacks
Mac OS X”](http://www.webwarrior.net/modules.php?op=modload&name=News&file=article&sid=4784). This is so wrong, so sensational, as to defy
belief.


To Kahney’s and Wired News’s credit, the initial report was later
replaced by a new article, headlined [“OS X Trojan Horse Is a Nag”](http://www.wired.com/news/mac/0,2125,63000,00.html),
which corrected the original article and began by putting the
situation in an accurate context:


> Security experts on Friday slammed security firm Intego for
> exaggerating the threat of what the company identified as the first
> Trojan for Mac OS X.


(Credit to MDJ for finding a working link to the initial Wired News report.)


**Verdict:** The initial report was the most sensational and least
accurate coverage I saw. They did the right thing by correcting
themselves within a day, but that doesn’t excuse the utterly
misleading initial report.


### CNN


**Update:** [Chris Nandor](http://pudge.net/) emailed to point that [CNN’s
coverage](http://www.cnn.com/2004/TECH/internet/04/09/apple.trojan/) was even worse than Wired’s, and went uncorrected.
Here’s the first sentence from CNN’s article:


> The first Trojan horse virus to target Apple’s latest operating system
> was discovered this week, and it appears to prey on the popularity of
> Apple’s popular music service.


Here’s what’s wrong with just that first sentence:

1. It wasn’t a virus.
2. It doesn’t “target” Apple’s latest operating system — the same file
works the same way on Mac OS 9.
3. It was three weeks old at the time of CNN’s report.
4. It’s completely unrelated to “Apple’s popular music service.”


**Verdict:** The remaining sentences aren’t any better.


### Coverage in the Daily Mac News Sites


[MacFixIt completely botched](http://www.macfixit.com/article.php?story=20040409073009731) its (non-bylined) report.
[MacNN](http://macnn.com/news/24162), [MacCentral](http://maccentral.macworld.com/news/2004/04/08/trojan/index.php?redirect=1082051439000), [MacObserver](http://www.macobserver.com/article/2004/04/08.13.shtml), and [MacMinute](http://www.macminute.com/2004/04/08/trojanhorse) all
did nothing more than regurgitate bits from Intego’s inaccurate
press release, and passed it along without the scrutiny it deserved.


*Linking is not reporting.* If these sites are news media, as they
all claim to be, and not merely clearing houses for press releases,
then they are obligated to investigate claims such as Intego’s
before publishing them. Does this mean they might get scooped by
less scrupulous “news” sites, which jump the gun to publish a
sensational “Trojan horse scare for Mac OS X” story? Sure. But
credibility stems from accuracy, not immediacy.


The vast majority of the news blurbs published by these sites don’t
demand investigation. An alleged security hole, however, is anything
but a typical story. MacCentral’s Jim Dalrymple did contact Symantec
for comment, but another vendor of commercial anti-virus/security
software isn’t where you go to get unbiased analysis of a Trojan
horse threat. These companies have a vested interest in convincing
Mac users that they need anti-virus software.


The core of the story, missed by all of the above Mac news sites, is
that Mac applications can have icons and file names that make them
appear at a glance to be documents. You don’t need anti-virus
software to defend against this threat — you simply need to be
careful that documents you download from untrusted sources are, in
fact, documents. The Finder can tell you this.


That’s what it boils down to. Anyone who couldn’t smell the
fishiness in Intego’s press release is unfit to write important Mac
OS security stories. Anyone who *did* smell the fishiness, but
published Intego’s claims anyway, should be ashamed.



| **Previous:** | [Preferences](https://daringfireball.net/2004/04/preferences) |
| **Next:** | [If It Ain’t Broke](https://daringfireball.net/2004/04/if_it_aint_broke) |


PreviousNext