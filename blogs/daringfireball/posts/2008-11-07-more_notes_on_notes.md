---
title: "More Notes on Notes"
date: 2008-11-07
url: https://daringfireball.net/2008/11/more_notes_on_notes
slug: more_notes_on_notes
word_count: 1514
---


Some thoughtful feedback from readers regarding [my analysis](http://daringfireball.net/2008/11/iphone_likeness) of the UI design of the iPhone’s built-in Notes app.


## Creation vs. Modification Date Sorting


Regarding my assertion that sorting notes by modification date was the right choice, Glen Raphael1 writes:


> That would be fine for me if it were sorted chronologically by note
> *creation* time. That is what the Newton NotePad did and what the
> Palm notepad app did — quite sensibly. However, what Apple chose to
> do here was sort by note *modification* time. Which is insane.
> If I take notes in a variety of contexts over time, my notes are
> nicely sorted in historical order — the older notes are further down
> the list and notes taken at a similar time are in proximity to one
> another. So I can use my temporal memory to find things. Paper
> notepads in the real world work like that too. But on the iPhone if
> I ever go back to review my old notes and *make any changes*, those
> notes spontaneously jump to the top of the stack. That has two
> negative consequences:
> After reviewing and revising old notes, my notes are in a random
> order. Given that the chronological ordering has been violated and
> there’s no search feature, you simply can’t find old notes in a
> large stack. It doesn’t scale the way the Newton/Palm/everybody-else
> -in-the-known-universe approach does.
> If I scroll back to find an old note, revise it, and want to
> continue scrolling back to look at or revise the next note *before*
> that one… I can’t find it. Because the note I just changed has
> moved, it’s no longer adjacent to the one taken before it. This
> means lots of extra scrolling if I want to try to find the next note
> in series.
> In notepad apps on other platforms, I could easily scroll to the
> 40th newest note, delete a couple parts of that note I no longer
> care about, click/tap/button press once to get to the 41st newest
> note, fix a typo there, click/tap/button press once to get to the
> 42nd note and read it to refresh my memory, and continue down the
> stack — reading and revising as I go along. Try doing that with
> iPhone and you’ll want to throw the thing against a wall.
> As a result of this “feature” I no longer use Notes. I’ve switched
> to MagicPad and wish I could just delete Notes. Yeah, MagicPad has
> got copy/paste and font stuff, but for me the killer feature was
> simply that it allowed me via a settings preference to sort by note
> creation time, which is clearly the *correct* default.


These are strong points. I don’t keep a ton of notes in my iPhone around at a time — I carry a paper notebook with me wherever I go, and which is where I jot most transient thoughts/items. I use Notes on the iPhone mostly for reference material I’ll want to come back to many times (which is to say, over a long enough period of time that I’ll have gone through several paper notebooks over that period), and for very specific temporary material like my airline flight reservation number for a trip.


If you’re the sort of person who uses Notes for everything — say, if you’ve got dozens of notes — I can see how sorting by modification date might be maddening.


It also occurs to me that sorting by creation date would fit better with Notes’s “looks like a paper tablet” visual metaphor. With a paper notebook, it’s easy to find something you know you jotted down “about a month ago” just by flipping back to the right spot in the notebook.


In short, switching Notes to creation date sorting seems like a good idea. It would work better for people like Raphael, who keep a large number of active notes — and it would work just about the same for people like me, with a small number of active notes. Light users of Notes almost certainly wouldn’t even notice the change.


## Apple’s Private ‘default.png’ Cheat


iPhone apps typically take at least a few seconds to launch, sometimes more. Developers can include an image to be loaded immediately after the app launches, named “default.png”. You can use this as a splash screen (more or less as a title card for the app), or, you can display the empty skeleton of the app’s UI (making it look like the real UI is starting to load, when in fact it’s just a *screenshot* of an empty UI).


Apple’s own apps — which don’t have the same restrictions as third-party apps — have another option available, which I’ll call “dynamic default.png”. What many Apple apps do is take a screenshot of the current display when you quit, and overwrite the default.png file inside the application bundle with that screenshot. Then when next you launch that app, you immediately see the entire contents of the screen from when you previously quit — but it’s still just a screenshot, a static image. It *looks* like the app has launched instantly, but in fact you’ve still got to wait a few seconds for the app to restore itself to the point where it’s actually ready to use.


I’ve seen third-party iPhone developers complaining that this trick is only available to Apple; they want to use it too. The technical reason why they can’t is that because application bundles are cryptographically signed, you can’t modify the contents of the application bundle (by, in this case, changing the default.png resource file) without breaking the digital signature. Apple could enable this feature for signed applications by providing for a way to specify a dynamic default.png that exists outside the application bundle, somewhere in the application’s private *Library* folder.


But I don’t think these dynamic default.png files are a good idea in the first place. I fully realize that the user’s *perception* of performance is often more important than actual measured-by-a-stopwatch performance, but in the case of dynamic default.png files, I think it goes too far. It is frustrating to see a complete UI that looks usable but isn’t. Dynamic default.png files make application launch times *look* faster, but they don’t make them *feel* faster. I feel like a dolt every time I get tricked into uselessly tapping UI elements on a default.png screen.


Notes uses this dynamic default.png cheat, and there are only very subtle indications to tell when the actual UI has replaced the screenshot (and is therefore ready to use). Several readers wrote in to complain about their frustration at not being able to tell when Notes is actually ready to use. Keshuv Prasad writes:


> The splash/loading screen for the list view is identical to the
> loaded view and gives no indication when one becomes the other.
> In note view the background lines blink when the loading screen turns into
> a loaded screen, but the pre- and post-loaded screens are
> identical.
> Photos, for example, displays a blank list as its splash screen
> and only shows the individual items (Camera Roll, Photo Library,
> etc.), after the app has loaded.  This makes it easy to tell
> whether the app is loading or has already loaded.
> Applying this same design to Notes would reduce frustration with
> not knowing whether or not the screen is responsive or not upon
> loading the app (note view would show a blank note, with the
> appearance of text indicating that it has finished loading).


I too find the Photos model — where you just see a more or less empty shell of the UI upon launch — to be superior. That way, as soon as you see actual content, you know the app is ready to use.


Prasad has another good suggestion:


> My second issue is how the notes are displayed in list view.
> There are up to 8 notes listed and the bottom one’s row fits
> exactly on the screen.  To use Photos as an example, it only
> displays 7 full rows, with the 8th row cut off.  Yes, the number
> of notes is in parentheses after Notes, but having the last row
> cut off (Contacts does this as well) would be a nice visual
> indicator that there is something below to scroll.  This is a
> minor quibble, though.


In other words, because iPhone list views don’t show persistent scroll bars (which, on the Mac, provide an indication when there is more content below what is visible), it’s helpful if the row height is such that a whole number of rows don’t fit exactly on screen. Good suggestion.


---

1. In a previous Apple handheld platform universe, Raphael was the developer of [NewtPaint](http://www.scottsplace.net/newtonsource/html/newtpaint.html). ↩︎



| **Previous:** | [Tangled Up in White](https://daringfireball.net/2008/11/tangled_up_in_white) |
| **Next:** | [Executive Scuttlebutt](https://daringfireball.net/2008/11/executive_scuttlebutt) |


PreviousNext