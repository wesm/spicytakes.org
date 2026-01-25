---
title: "Settling the OS X focus-follows-mouse debate"
date: 2008-04-24
url: https://steve-yegge.blogspot.com/2008/04/settling-osx-focus-follows-mouse-debate.html
word_count: 5548
---

I recently switched to using OS X full-time for all my client-side computing.  Still using Linux on the backends, of course, at home and at work, but I now use Macs for my client machines.
I'm not a Mac fanboy.  I'm sort of a wannabe Mac fanboy, but I'm not familiar enough with the OS yet (either as a user or as a programmer) to really rave about it.  I will say this: it was kinda fun turning off that last Windows box for the last time.
My main reason for switching was that I'm getting old and the fonts look nicer.  Pretty stupid reason, isn't it?  I thought so too.  But getting old kinda sneaks up on you.  I've gone from preferring six-point font when I was twelve to 20-point font now that I'm 40.  So at least for me, my ideal font point size appears to be
.
That sucks.
One day I noticed that I could actually read the screen when I was browsing in the Apple store, and I did some experimentation and found that yes, I can actually read normal-person's fonts on the Mac.  And they look kinda nice, too – the antialiasing engine seems to be smarter (and faster) than the ones I've seen on Windows and Linux.
So there ya go.  Fonts.  And now I have to learn all this new stuff, like what all those weird little symbols mean on the keys, and how to use the Finder, and what a "DMG file" is, and other stuff.  But the screen looks
*soooo*
nice, so it's worth it.  How do they do it?  It's not just the fonts.  OS X windows look whiter and cleaner than their Windows/Linux cousins running on the same display with similar video hardware.  It's a mystery to me, but it's kinda cool.
**Almost pain-free migration**
I've been using a work-issued MacBook Pro laptop for the past year, and that helped a lot with the transition, since when you're on the road trying to get some work done, you have no choice but to figure out how to do basic OS tasks.  So that was a nice, slow, reasonably pain-free way to teach myself the basic skills you need.
I only bring this up because I know a
*lot*
of programmers (myself included) who've tried Macs repeatedly and run away scared.  If you stick with it a little longer, it's not too bad!  Particularly with their latest OS X release (
), it's gotten a lot easier to do basic configuration for people accustomed to Linux.
For starters, it comes with a good X11 implementation, and there is a
[MacPorts](http://www.macports.org)
project that ports all your favorite Unix stuff.  And they're not lame half-broken ports like the ones you have to live with in
[Cygwin](http://www.cygwin.com)
.  For instance, in a Bash shell running inside Emacs you can ssh into a Linux box and not get a bunch of greebly control characters.
And OS X is Unix, based on FreeBSD, so all your normal favorite Unix stuff pretty much works the same, or at least as much as you can expect across different flavors of Unix.
The only real reason I was using Windows at all, to be honest, was for hardware-device compatibility and for multimedia.  The Mac has drivers for everything I cared about (my router, my printer, my camera, etc.)  and beats Windows hands-down on any sort of multimedia, so it was becoming clear that Windows wasn't buying me much anymore.
I suppose I could do a blow-by-blow guide for how a Unix-and-Windows user can configure their Mac for maximum happiness.  If anyone's interested, anyway.  Not today, though.  The bottom line is that pretty much everything you don't like is configurable... with one ugly exception.  And I don't mean "Mary Ann on Gilligan's Island Ugly", either.  I mean Ugly ugly.
**The Big Focus Issue**
Ever since the Dawn of Time (Jan 1, 1970), people have been bitching about the lack of focus-follows-mouse on Mac computers.  They started complaining about it fourteen years before the first Mac was even released, that's how bad it was.
Every time they bring it up on Mac forums, the Mac users with non-Unix backgrounds ask "what's that?"  And then a bunch of wrong answers start flying around, with a few right answers interspersed but drowned out in the noise.
So let me tell you what it is first, in case you're not from a Unix background.  Focus-follows-mouse means that when you move the mouse cursor, the window under the cursor gets the keyboard focus.  But saying that confuses Mac people who all assume that "focused" is synonymous with "foreground", because that's the way it works on the Mac.
The confusion stems from the fact that focus-follows-mouse comes in not one, but
**two**
, yes that's right,
*two*
yummy flavors.
**Flavor #1: autofocus**
— in this flavor, reminiscent perhaps of a sweet juicy mandarin orange, the window under the mouse gets the keyboard focus but
*does not come to the front*
.  This allows you to interact with a partially-obscured window.  It's especially useful when you have a terminal or shell window open, and it's running a background process that you want to observe... you guessed it, in the background!  You leave a little bit of the bottom and/or side of the window uncovered so you can keep an eye on the output.
Real-life use case: let's say you're a programmer who writes in C++.  You will, of course, spend most of your working day playing Solitaire and reading reddit, because C++ is
[too goddamned stupid](http://yosefk.com/c++fqa/)
to do anything but gigantic, slow batch compiles of the entire dependency universe.  So you have at least four windows open at any given time: your editor, your compile shell, your browser, and your Solitaire game.  You've spent a lot of time adjusting your window configuration to be "just right", and unless you have a 30-inch screen (for instance, because you work for Google), your windows overlap.
Watching your compile status is like checking your rear-view mirror; you do it every 7 seconds or so, even though you know the compiler will take a minimum of 15 minutes.  It's like a slow-motion train wreck that you just can't tear your eyes from, even while playing Solitaire and reading reddit.  And every once in a while you'll need to enter a command (e.g. "make", after you've fixed the umpteenth compiler warning about doing a perfectly valid type conversion).  The last thing you want is to have to click the window to bring it to the front just so you can type "make", because then you'll need to go futz around with your window configuration again to get the window to go to back to whatever Z-location it used to be in the window stack.
I know it doesn't sound like a big effort, but programmers are really,
*really*
lazy, and they like to minimize motion.  They'd use feeder tubes if the Health Department would let them.
So in the autofocus flavor, it's important that the window that gets the focus does
*not*
automatically come to the front.
**Flavor #2: autoraise**
— in this pungent flavor, somewhat evocative of a slightly overripe Durian fruit left in the tropical sun for about nine hours, moving the mouse into a new window automatically brings that window to the front.  In the especially horrible default configuration, it comes to the front instantly, so the act of moving your mouse across the screen makes it look like that old "rectangles" screen saver, and your window configuration is utterly obliterated in under a second.
Many programmers feel that autofocus is delicate butterfly and autoraise is a big, stinky buffalo.  That's just how they feel about it.  No accounting for taste.  I, for one, think of autoraise as a big, stinky,
*deceased*
buffalo carcass that someone thoughtfully dragged into my living room while I was on vacation, probably towards the beginning of the vacation, and then they turned up my thermostat to 110°F, closed the windows and tossed a Durian fruit at the wall for good measure.
But maybe it's just me.
So one of the most annoying aspects of the whole "how do I get focus-follows-mouse behavior on my Mac" debate is that everyone assumes you mean autoraise.  There are a number of packages out there, most of them commercial, that offer autoraise as a feature, and Mac users point you to these products and then get all smugly about how they've solved your problem and how Macs still rule the universe, when in fact the problem is still festering away.
It's no wonder people still use Linux as their UI.  That one feature alone keeps hordes of programmers from switching.  (And yes, you can get the behavior on Windows using their TweakUI power tools, so some programmers use Windows as a Linux shell with a decent media player.)
**Super-Stevey to the rescue (well, almost)**
Given that I switched quite recently to the Mac, I'm still reeling from the lack of focus-follows-mouse behavior.  To help you put yourself in my shoes, imagine that your latest operating system upgrade (whatever OS you happen to be running) includes a new mandatory feature wherein each time you click on a window to focus it, a loud alarm goes off ("BLONK!  BLONK!  BLONK! ...") and you have to open the System menu and select "silence window alarm" to shut it up.
That's what not having autofocus is like to people who've been using it for the past 10 to 30 years (in my case, 20 years).  BLONK!  BLONK!  BLONK!  I'm serious.  It's that bad.  Not exaggerating even a tiny bit.
I'm sure you could eventually get used to this behavior, and even find yourself arguing on newsgroups that you rather like the blonk blonk sound, since it reminds you that you've recently chosen to switch to another application or to another window within the current application, plus it's really not that big a deal because you can just open the System menu and turn it off.
It's amazing how so many people choose to rationalize stuff they're forced to live with.  Why not just admit it sucks?  Sometimes stuff sucks!  C'mon, admit it!  Jeez!
But even if you
*eventually*
managed to rationalize it, you'd be pretty fugging pissed off the first, oh, ten thousand or so times it happened to you after the upgrade.
So the other day, after the 100th or so BLONK! BLONK! BLONK! alarm when I innocently tried to type into a different window, I found myself quietly contemplating the pros and cons of getting an assault rifle, heading down to the Apple campus, and making my opinions known to all until the SWAT team took me out.  And then I thought: "hey, as attractive as that option sounds right now, I have a better idea: why not fix it myself?  I make occasional claims to being a programmer, right?  How blonking hard can it be?  I'll budget one evening for it."
I actually wound up spending 2 evenings on it, since although coming up to speed on the Apple tools and APIs was almost trivial, this particular issue turned out to be thorny in a variety of unexpected ways.
But I did get it working, for some definition of "working", and now I'm in a position to settle the debate for the forseeable future, which I estimate to be about the next five to seven years in this case.
**The Definitive Answer**
*Short version:*
you can
*almost*
get it working, but not quite, on account of an arguable bug in one of the Carbon (that is, Mac C++) APIs.  What I got working was a system-wide autofocus mode that unfortunately only re-routes
*unmodified*
keys to the window under the cursor.  You can fake the Shift modifier by translating the key code manually, but the Control, Command and Alt/Option keys never make it through to background applications.  (They do get delivered to the foreground app if your mouse is there, so the bug only happens for background apps.)
So if your use case is limited to, say, typing commands into a command shell, and you don't need to use the control, alt or command keys, then you can have working autofocus!  In fact, you can even make it so that only your terminal windows (or any application list of your choice) get the autofocus behavior, and all other applications get the normal must-click-to-focus behavior.  So even my "failed" attempt might yet hold some small utility for us ancient Unix hackers.  I'll play with it for a while and see.
*Long Version:*
As close as I came in my little 2-day effort, I now believe at this point that it's unlikely that autofocus will ever be available on Macs, sad as that news will be for thousands of would-be Mac users.  And not just any users: they're
*programmers*
, all potentially capable of learning to write Mac applications and collectively enhancing the value of Apple's platform.  So it's kind of a big opportunity cost for Apple.  But there are both technical issues and design issues that make it a serious problem to support autofocus on Macs.
It's probably not
*impossible*
, but the cost is high enough that when their OS engineers think about tackling it, they'll probably decide it's not worth the effort, since the company seems to fail to appreciate just how big a stumbling block the lack of autofocus-sans-autoraise really is for so many competent Unix programmers out there.
So, Apple OS engineers, I'm not saying you're not smart.  I'm just saying you're not smart
*enough*
. ;-)
Just kidding, of course, and I'll dispense with the child psychology.  Here's why I think they're not going to fix it.  The rest of this blog entry consists of boring technical details, so if you're getting antsy, please feel completely free to skip to the very end.
**How it works**
First, one caveat: I'm not a
.  I don't even play one on TV.  I just downloaded Xcode (their development toolkit) for the first time three days ago.  I've never written any Mac programs before this one, not even an AppleScript script, and I only started looking at their APIs a couple days ago.  So I might be wrong about some or all of this.
The first problem you encounter is that there's no public Mac API for getting any sort of usable handle to a running application so you can interact with it programmatically.  This is apparently for security reasons.  I won't harp on this decision, although it does seem odd to deny sophisticated (read: sudo-enabled) users the choice of loading privileged apps into their system.  Any application can run amok with your filesystem, personal data and network connection, so it seems odd that you'd arbitrarily choose not to let them also run amok with your other running apps.
In any case, there's a loophole.  Apple, out of sheer generosity, goodwill, and the kindness of their heart o' hearts, and also partly because
[United States Federal Law](http://www.section508.gov/)
requires it, but mostly out of sheer generosity, goodwill and the kindness of their hearts, has provided a set of "Accessibility APIs" that give you a certain federally mandated level of remote control over running applications in the system.
OS X actually has two more or less discrete sets of APIs: one for C/C++ (
), and one for
(
).  Cocoa incidentally also happens to be the API you use for Python and Ruby scripting on the Mac; I took a detour for a few hours and learned the basics of RubyCocoa, and was quite pleased at how well it worked.
One of the reasons I took the RubyCocoa detour was that the subset of the Accessibility APIs I needed for implementing autofocus is fairly cumbersome to explore using C++ and Xcode.  I made an executive decision to spend (and potentially waste) some time seeing if I could make faster progress using one of the scripting APIs, because I was encountering bugs and/or unexpected behavior that called for some exploratory programming.
Carbon offers an abstraction called an
[AXUIElementRef](http://developer.apple.com/documentation/Accessibility/Reference/AccessibilityLowlevel/AXUIElement/index.html)
, which is a proxy object representing a UI element (e.g. an application, a window, or widget) in any running app on the system.  This subsystem is designed and implemented entirely using the Properties Pattern, which, as it happens, I'll be blogging about at length in the very near future.  Normally this pattern is quite flexible, and I can fully understand their reasons for using it here: it gave them legal compliance with an absolute minimum of effort.
But the Properties pattern is healthiest in a dynamic environment that lets you poke around reflectively to get the names of properties, fetch their values, traverse parent links, and so on.  Carbon provides APIs for manipulating all these UI-element properties with C++, but it really is cumbersome: lots of casting, lots of wrappers, lots of recompilation every time you want to try just one more thing.  Call me spoiled, but I only budgeted a day for this feature!
So I learned a bit of RubyCocoa, and it appears – as far as I can tell – that the relevant Accessibility APIs are
*only*
available through Carbon, and not through Cocoa, which means if you want to use them, you can't use Objective-C, Ruby or Python.  Or at least I couldn't find a way.  If I'm wrong, someone
*please*
correct me, since I'd really like an experimentation platform that handles Carbon APIs that have no Cocoa equivalents.
**Really Grubby Details**
I told you it'd be boring!  What are you still doing here?
OK, whatever.  You're a glutton for punishment, I tell ya.
There are three basic components to the focus-follows-mouse solution:
1. Create an "event tap" to filter all system keypresses.
2. Find the frontmost window under the mouse
3. Redirect the keypresses to that window.

That's all there is to it.  This is the solution I envisioned before I'd even downloaded Xcode, and unsurprisingly, it appears to be the only reasonable way to accomplish the task in OS X.  I mean, how else would you do it?
The event-tap API is straightforward, with just one teeny, minor exception almost not worth mentioning, which is that it doesn't work.  It compiles, runs, and fails silently.  This took me several hours to figure out.  It turns out that event taps are considered to be part of the Accessibility APIs, and for security reasons, your process either has to be running as root, or you have to enable "assistive technologies" in the Universal Access section of System Preferences.  I stumbled across this in some random newsgroup after a LOT of searching.  In retrospect it was kinda there in the API documentation, but they didn't make it super clear.
Whew!  There went several hours down the drain, but now I had a C program that fired up and listened for keypresses, printing them to stdout.  The event-tap API gives you the option of swallowing the keypresses (or changing the event, or even returning a new event to replace the old one), so it's plenty flexible enough for our needs.
Next, I needed to find the window under the cursor, which first meant finding the global cursor position.  This also turned out to be surprisingly non-obvious.  The best solution I found, from someone's blog, was to create a NULL event and then get its mouse coordinates.  So intuitive!  Just like Mom used to do it!
Sigh.
Once you have your mouse coordinates, you use a "hit test" to find the window at that screen position.  It's one of two Carbon-only APIs you need: you create a proxy for the system-wide UI object with
, and pass it to the global hit-test function
to get the UI element under the mouse.
Then it gets a little ugly, though not terribly so.  These
objects have all their information in property lists.  This would be trivial to navigate in RubyCocoa, but the
API set doesn't seem to exist in Cocoa — specifically the parts that deal with "any running application" rather than "
*your*
application".
So you grub around in the object and its parent chain, clunkily printing stuff in C++ and releasing reference-counts, until you find an ancestor with a "role" attribute of "application".  That's the element you need for delivering keyboard events.
We can deliver the keyboard event to the unfocused window, through this poorly-documented API call:

```
AXError AXUIElementPostKeyboardEvent(AXUIElementRef application,                                     CGCharCode keyChar,                                     CGKeyCode virtualKey,                                     Boolean keyDown);
```

All good so far.  Excluding the time spent figuring out the access-control problem with event taps, and the time spent playing with RubyCocoa, I'm only about five hours into the whole endeavor.
Oh yeah, and the time spent dicking with Xcode trying to figure out how to add a library build target to the executable.  I've done it two or three times now and
*still*
can't remember how I did it.
The
function points you to its non-Accessible cousin
, which is
*also*
more or less undocumented.  Can you tell they really don't want you to use this stuff?  This cousin function has a teeny bit of explanation in its header file
, which Xcode provides no easy way of locating via search.  You can look for it in Spotlight, hoping you'll get lucky and it won't hang like it did for me just now.  Or you can do what I did and just use
[Google Desktop](http://www.desktop.google.com/mac/)
search to pop to it instantly.
The explanation in the header file says:

```
/* * Synthesize keyboard events.  Based on the values entered, * the appropriate key down, key up, and flags changed events are generated. * If keyChar is NUL (0), an appropriate value will be guessed at, based on the * default keymapping. * * All keystrokes needed to generate a character must be entered, including * SHIFT, CONTROL, OPTION, and COMMAND keys.  For example, to produce a 'Z', * the SHIFT key must be down, the 'z' key must go down, and then the SHIFT * and 'z' key must be released: * CGPostKeyboardEvent( (CGCharCode)0, (CGKeyCode)56, true ); // shift down * CGPostKeyboardEvent( (CGCharCode)'Z', (CGKeyCode)6, true ); // 'z' down * CGPostKeyboardEvent( (CGCharCode)'Z', (CGKeyCode)6, false ); // 'z' up * CGPostKeyboardEvent( (CGCharCode)0, (CGKeyCode)56, false ); // 'shift up */
```

That's it.  That's what they give you.  Open questions about the explanation include (a) why are they passing capital-'Z' if they already reported that the shift key was down, (b) if there's a guesser when you pass NULL, why do you need to pass 'Z', (c) how do you get the char code for a given key code, and is it the same on all keyboards, and (d) why didn't they include a "THE FIRST PARAGRAH IS A LIE" disclaimer around the first paragraph?
Open questions be damned.  We fearlessly press on, and just pass "whatever" and see what happens.  Specifically, I always pass NULL for the char code, and pass the key code I got from the event tap callback as-is.
And it worked!  Sort of!  I start my little app (which has no UI), move the mouse into a window from a non-foreground application, and I can type into it!
Except I can only type unmodified keys.  It's completely ignoring my keyboard event posts for Shift, Control, Alt and Command.  That's the lie part.  They said they'd generate flags changed events.  They lied.
After some more painful C++ experimentation, I find that the call does NOT ignore modifier keys when posting to (a) the focused application or (b) the system-wide application, which just posts to the focused app.  The call only drops modifier keys on the floor for non-focused apps.
There's a
[big ol' thread about this exact problem](http://lists.apple.com/archives/Accessibility-dev/2002/Dec/msg00032.html)
from six years ago on the Apple accessibility-dev mailing list.  Six years!  I read every last word of the thread.
The first takeaway is that Apple OS engineers don't want you to do stuff that they don't want you to do, and they specifically define "stuff they don't want you to do" as "stuff they don't think you want to do."  This is actually endemic to Apple forums in general.  Whenever someone says "I want focus follows mouse behavior!", some people inevitably reply that "you really don't want to do this".  It's that whole "we designed it the
*right*
way for everyone" mentality that turns off so many would-be Mac users.
For what it's worth, the Apple engineers really were trying to be helpful in this guy's situation, and I know how hard it can be to respond to a mailing list in the capacity of "developer representing the company".  But it took them a long time to understand his needs, because (and I'm speculating here) they implemented the Accessibility APIs only because their Mom told them to, and they don't truly appreciate at a deep level what it means to have a disability, and how important it is for many people to be able to choose a different UI paradigm.
And yes, I am taking the arguably un-PC position that having your fingers hardwired to focus-follows-mouse from 20 years of use can be viewed as a minor disability of sorts.  I'll be the first to admit that it's not the kind of "real" disability the government probably had in mind when they mandated the Accessibility APIs.
But I
*did*
switch to the Mac because my eyes are slowly beginning to fail.  Ironic that I should be forced to trade one disability for another.
**The underlying issue**
OK, let's assume for the moment that Apple really does have our best interests at heart, and that they can get over the painful notion that their usability test findings may not actually apply to 100% of all users 100% of the time.
Even if they wanted to help fix it — and in this case, all they'd need to do is NOT drop the modifier keys on the floor when you call
— there are some deep-rooted architectural issues at play here, and I finally "got it" while reading that thread.
The problem is that Macs, always and forever, have put the menu bar of the focused application at the top of the screen.  The menu bars of unfocused applications are hidden and are not in any way user-interactible.
As you might expect, this UI assumption has been baked into the Mac APIs from the very beginning.  Programmers will take advantage of any axiom they can in order to get things working, so over time this has turned from a UI design assumption into an architectural "feature".
In particular, when an app is in the background, its menu structure may not be intact, and the app may be in a state that assumes it will not be receiving any keyboard input.  One concrete example mentioned in the thread was that when an app is in the background, the child menu items do not have parent links (although the parents still have pointers to the children.)
This has serious ramifications for focus-follows-mouse.  There are certain built-in hotkeys that can activate menu entries, and apps are also free to define their own.  If you try to activate a menu in a background application, it
*could*
in theory wind up crashing the app, if the app is assuming an intact menu structure and is traversing bottom-up rather than top-down.
You could attempt a knee-jerk solution by allowing Control and Alt through, but deny the Command modifier, since that's the most common menu-activation modifier (I think).  But there's another class of applications (Emacs included) that dynamically generates at least part of its menu structure based on the data content.  For instance, the Emacs Imenu package generates a list of jump targets from a source-code buffer.  Even typing a new function definition could still trigger a rebuild of the IMenu, which (for all anyone knows) could crash Emacs.
You could of course ask app developers to fix this on an application-by-application basis, but there are generations of legacy apps that can never be fixed.  The only way to
*guarantee*
that pressing a key could never crash an application would be to fix the OS X user-interface architecture to normalize application behavior for foreground and background operation.  This could be hard.  It could expose its own set of difficult or even intractable problems for legacy apps.  Or maybe it's really easy.  I don't know, since I can't see their code.  But I suspect it's not easy.
And Apple has no real motivation to fix it, because their UI was designed for "everyone".  People who would use focus-follows-mouse are presumably a tiny minority, so even if they're mostly programmers the cost/benefit likely isn't there.
It is, of course, completely fixable if Apple
*really*
wanted to fix it.  I've heard many war stories over the years from Microsoft folks who've had to put compatibility hacks into OS releases, some quite extensive, in order to support popular applications that relied on undocumented OS behavior that suddenly broke.  Imagine those poor guys that had to implement perfect DOS/Windows emulation on NT, for example.  I suspect that by comparison, fixing focus-follows-mouse would be relatively straightforward.
But I predict it won't happen in the next 5 to 7 years, unless the government suddenly decides that this API is required for properly assistive technologies.
It's interesting that you can get
*so close*
using the existing APIs: I have true focus-follows-mouse behavior implemented for non-modified keys.  Sure, the window doesn't actually focus, so some applications don't even show a cursor.  But if you're willing to live with occasional glitches, the feature works great.
In any event, what's weirdest about all this is that the API lets you send non-modifier keys to the background app, because as I pointed out, it's still possible for vanilla keys to crash applications!  If the state of the app is materially different when it's unfocused, and the app isn't expecting keyboard input when unfocused, then it could crash.  Dropping the modifier keys on the floor may reduce the probability of Badness, but it certainly doesn't eliminate the possibility.
Was it an accident that they let any keys through at all?  That would surprise me greatly, since the OS engineers seem determined to close undocumented behavior loopholes.  But if they had a reason (perhaps a legal reason) to permit unmodified keys through, what was it about the reason that lets them drop the modifier keys?
I wish I knew.
**Open letter to the Apple Wish Fairy**
If I could wave a magic wand, I'd ask for them to fix the API to pass the modifier keys along to the app, and just put a note in the docs that Bad Things could happen, so Buyer Beware.
They already do this for those exact APIs anyway.
's documentation says: "This function is not recommended for general use because of undocumented special cases and undesirable side effects."  And this is for the API that only talks to the focused foreground app!  The AXUI version is obviously double-buyer-beware, and apps can't even use it without prompting for the superuser password, unless the user has purposely enabled assistive technologies.
There would be bugs, yes.  Some applications would have to push out new releases to properly support focus-follows-mouse, and some legacy apps would never be fixed.  But you could disable the behavior on an app-by-app basis, or just take a "Doctor, it hurts when I do this" approach.
Unfortunately I don't have a magic wand; all I have is my distinctly nonmagical blog, which I'm using to soothe myself via copious whining.
**Epilogue**
This whole thing has been an interesting lesson in how the government can actually force companies to open up their locked-down systems.  The whole "you'll have it
*our*
way, and like it" mentality is crumbling with these assistive technologies.  I hope the feds mandate opening things up even further, since we're only partway there so far.
In the interim, I'm sure I'll eventually get used to life without autofocus.  BLONK!  My 30-inch screen helps, as does Spaces, since it's easier to give windows their own non-overlapping real estate.
I might even give autoraise another try.  Some developers have implemented it in
[a horrible way](http://code.google.com/p/xmouse/)
, by generating a mouse click when you move the mouse into a window, which often results in activating UI objects unintentionally just by moving the mouse.  Ouch.  But there might be some commercial implementations that do it "right", or I can just hack my autofocus app to do it that way.  Combined with an autoraise delay and minimizing my overlapping windows, it might just work.  We'll see.
And everything else so far about the Mac has seemed pretty nice, or when it's been not nice, at least it's been fixable with a little configuration effort.  I liked the OS X APIs on the whole, and the RubyCocoa thing is pretty sweet.  I might even wind up writing some native clients — something I thought I'd never do again, given how awful my Windows native-client experiences have been over the years.
So I'll keep using my Macs.  They're all just plumbing for Emacs, anyway.  And now my plumbing has nicer fonts.
**If you skipped straight to the end...**
...you didn't miss much.  See you next time!