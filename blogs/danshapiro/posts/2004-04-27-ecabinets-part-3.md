---
title: "Ecabinets, part 3"
date: 2004-04-27
url: https://www.danshapiro.com/blog/2004/04/ecabinets-part-3/
word_count: 375
---


More ecab!  So here’s a summary of current challenges.  This is a “bad news” post; read the other entries under Software for more perspective.

1) Crashing.  Frequently.  Annoyingly.  The problem seems to be something in the render engine.  I’m going to mess with video driver settings to see if I can fix it.  On the bright side, I haven’t had a problem with a degenerate file yet (that always crashes when you open it), so with frequent saving, I can make progress.  On the down side, this means it’s very hard to isolate the bug to report.

2) Performance.  This software is **very** non-performance-optimized.  For example, if you enter an editing mode (e.g. “door frames”) and then immediately exit, everything is re-constructed from scratch.  Clearly, they’re not marking dirty bits and only doing the necessary work; they’re rebuilding the whole shmeer each time anything might have been changed.  Plus, this stuff’s just slow.  Lots of number crunching.  I might consider a system upgrade if everything works out.

3) Unnerving bugs.  I just reported one where adding a partition causes a shelf to magically disappear, leaving behind a corrupt and unusable file.  This is unnerving because it’s easy to reproduce, and makes me think they may not have a robust testing methadology.  Or any testing methadology.  The good news is that I spoke with them about it this morning and they hacked out a fix for next week’s build.  That’s somewhat reassuring, on the theory that if you’re going to ship buggy software, you better be prepared to fix the bugs fast.

4) No closed boxes.  You can’t make a six-sided box.  Kind of an odd limitation, and it prevents me from easily using it to make really amazing custom speaker boxes that are built in to cabinets.  Not a major ding, just a shame.  You can work around it, but you can’t use blind dados to attach the sixth side.


(I have to say that, generally, the software just feels slow and buggy. They do appear to be hard at work fixing this, and I hope they’re successful.  So far the benefits do outweigh the drawbacks, though.)

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
