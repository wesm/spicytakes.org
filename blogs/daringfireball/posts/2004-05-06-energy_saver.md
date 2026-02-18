---
title: "What to Do When Your Energy Saver Prefs Panel Won’t Load"
date: 2004-05-06
url: https://daringfireball.net/2004/05/energy_saver
slug: energy_saver
word_count: 1078
---


A few months ago, I started seeing the following problems on my iBook
(G3, 800 MHz), running Mac OS X 10.3:

- Four times, it completely froze while I was using it.
- Three times, it wouldn’t wake from sleep.
- I couldn’t get the Energy Saver panel in System Preferences to load.


Neither the freezes nor the wake-from-sleep problems were
reproducible. Every few days, however, one or the other would bite
me.


The freezes were very deep, but not quite total: I could still move the
mouse pointer around the screen, using either my mouse or trackpad.
But clicks didn’t register and keystrokes had no effect. It was not
merely a problem with my login session, either — when the freezes
occurred, I could not even connect using ssh from another machine.


The wake-from-sleep problems were what prompted me to check my
Energy Saver settings, which is when I discovered that the Energy
Saver panel would not load. I’d click on the Energy Saver icon in
the System Preferences window (or choose it from the View menu), and the
title of the System Preferences window would change to “Loading Energy
Saver…”, but it wouldn’t actually load.


Googling not only didn’t turn up an answer, it didn’t even turn up
other instances of the problem.


On a whim, I tried pressing different modifier keys while trying to
load the Energy Saver panel. Option-click worked, sort of. When it
loaded, after Option-clicking the Energy Saver icon, it looked like
this:


There are a few things wrong with what was displayed:

1. There’s a tab for UPS, but which should only appear if you’re
actually using a UPS (uninterruptible power supply). I am not.
2. The status message under the tab area ought to say something
along the lines of “You are using custom optimization. Current
battery charge is 95 percent.” Instead, mine said
“profile_message”. That’s obviously just placeholder text, which
is supposed to be set to the actual status. (And, indeed, if you
open up EnergySaver.prefPane’s EnergySaverPref.nib resource file
in Interface Builder, you’ll see that “profile_message” is the
static text item’s default value.)
3. You can’t tell from the above screenshot, but my battery
status *was* displayed in the menu bar, but the checkbox in the
pref panel indicated it wasn’t.


In short, my Energy Saver settings were seriously hosed.


I tried logging out and logging in using a newly-created admin
account, and Energy Saver worked just fine. When I logged back in
with my regular account, however, I had the same problems. This
narrowed it down to something specific to my main login account, not
something system-wide.


I moved the Preferences folder out of my home Library folder, then
logged out and logged back in. Now, Energy Saver loaded just fine.
So I had it narrowed down to something in my Preferences folder.


I put the Preferences folder back in place, and moved half its files
out. Logged out, logged in. Energy Saver would *not* load. Moved
half the remaining preference files out, logged out/in. Nope.
Repeat, repeat, repeat.


Now I had an empty Preferences folder (other than the files that
were recreated automatically each time I logged in), but I still
couldn’t load Energy Saver.


I moved the entire Preferences folder out of the Library folder
again. And again, Energy Saver now worked just fine.


Silly me, trying to do this from the Finder.


I opened Terminal, cd’d to ~/Library/Preferences/, and an
invocation of “`ls -AF`” turned up a handful of hidden dot files. I.e.
files with names that start with a dot, the Unix man’s way of
turning files “invisible”.


Ends up the bugger was “.GlobalPreferences.plist”. I restored all my
original pref files, but deleted .GlobalPreferences.plist, and the
problem went away.


So there you go. I can’t prove that this was related to my
wake-from-sleep problems, but it’s been about three weeks since I
fixed this, and I haven’t had problems waking from sleep since.


## Killing Just the Problematic Section of the .GlobalPreferences.plist File


I was willing to leave it at that — nuke the
.GlobalPreferences.plist file (hereafter, for brevity, “.GP file”,
and go on my merry way. I did, of course, take a look inside my
original .GP file, and while it was full of dozens of entries, none
of them looked to be essential. But nor did any look to be corrupted, and
curiously, none seemed to have anything whatsoever to do with Energy
Saver.


The only thing I really noticed losing were some, but not all, of my
Appearance settings. Instead of Graphite, I was back to Aqua.
Instead of my custom text selection color (196/196/204 specified in
RGB), I was back to Blue. Instead of [double scroll arrows](http://www.macosxhints.com/article.php?story=20010927011840284) at
both ends of a scroll bar, I was back the default. Easy enough to
reconfigure.


But, yesterday, it happened again. My Energy Saver control panel
would not load. The only reason I even tried loading it was because
I’d started writing this article, and I figured I had better check to
make sure the damn thing was still cooperating.


This time, I bit the bullet and figured out which setting in .GP was
causing the problem with Energy Saver. Ends up it was this:


```
<key>AppleICUDateTimeSymbols</key>
<dict>
    <key>5</key>
    <array>
        <string>a</string>
        <string>p</string>
    </array>
</dict>

```


Which is the result of my custom time format, as specified in the
International System Preferences panel. I set my times to look like
“11:44p” instead of the U.S. standard “11:44 PM”.


This bug is fully reproducible:

1. Launch System Preferences. (It seems to cache successfully
loaded prefs panels, so quit and relaunch if it’s already
running.)
2. Click on International, then click on the Formats tab.
3. Click the button to customize your time format.
4. Change “ AM” to just “A”, and “ PM” to just “P”.
5. Now try to load the Energy Saver panel.


On the machines here at Fireball Manor, Energy Saver will not load
with a custom time format specified as per above. It’s the M’s that
seem to matter. These formats cause no problems with Energy Saver:
‘11:44 PM’, ‘11:44PM’, ‘11:44 pm’, ‘11:44pm’. But these formats do: ‘11:44 P’,
‘11:44P’, ‘11:44 p’, ‘11:44p’.


Yes, yes — I’ll file a proper report with Apple about this. But first
things first — blog it so it gets into Google, the world’s best
troubleshooting database.



| **Previous:** | [Fixing Corrupt Preferences for Default Internet Helpers](https://daringfireball.net/2004/05/internet_helper) |
| **Next:** | [Writing for Google](https://daringfireball.net/2004/05/writing_for_google) |


PreviousNext