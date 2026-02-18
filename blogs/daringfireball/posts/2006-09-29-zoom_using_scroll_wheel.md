---
title: "New in 10.4.8: Zoom Using Scroll Wheel"
date: 2006-09-29
url: https://daringfireball.net/2006/09/zoom_using_scroll_wheel
slug: zoom_using_scroll_wheel
word_count: 604
---


Here’s a new feature in the Mac OS X 10.4.8 mouse preferences panel:1 “Zoom using scroll wheel”:


[**Update:** The same feature is also available for trackpad users who have the “Use two fingers to scroll” option turned on.]


It’s on by default, with the “while holding” modifer key set to Control. The modifier picker is a combo box — the drop-down menu lets you choose between Control, Option, and Command, but when the combo box has focus, you can specify multiple modifier keys simply by pressing them on your keyboard. You can’t set it to only use Shift, but you can use Shift in conjunction with one or more of the other modifiers.


The Options button opens a sheet with a few additional preference settings. The first is a set of radio buttons to determine how the zoomed screen scrolls when you move your mouse; I find the default setting, “Continuously with the pointer”, works best.


The other option is a checkbox labeled “Smooth images (Press ⌘⌥\ to turn smoothing on or off)”. The name is a bit misleading — it doesn’t just smooth images, it smooths (a.k.a. anti-aliases) the entire screen. If you’re using this feature as I intend to, to examine pixel-level layout details, it’s best to leave this off.


Overall, the feature works great; having zoom available at a moment’s notice is a bit more convenient than firing up a utility like [xScope](http://iconfactory.com/software/xscope) or [Art Directors Toolkit](http://www.code-line.com/software/artdirectorstoolkit.html). If you zoom just a little bit and let go of the modifier key, it snaps back to no zoom — this seems like a sensible defense against accidental zooms.


My only gripe is the ⌘⌥\ (Command-Option-Backslash) shortcut attached to the smoothing option. If you turn the “Zoom using scroll wheel” option on, this keyboard shortcut is applied system-wide, even when you aren’t zooming. That’s a problem if you’re using any applications that use this keystroke — and since BBEdit2 and Mailsmith use this for the Hard Wrap command, and I’ve got about 10 years of muscle memory using this command with this shortcut every single day, it’s a problem for me.


Minor system updates shouldn’t just gobble up keyboard shortcuts like this. For one thing, I don’t see why this particular option is so important that it deserves a system-wide keyboard shortcut. Who’s going to be toggling this smoothing option so frequently that they need a keyboard shortcut?


And even if it really does deserve a system-wide shortcut, it ought to be configurable using the Keyboard Shortcuts tab in the Keyboard & Mouse prefs panel. Most of the other system-wide default keyboard shortcuts can be changed or just plain turned off in the Keyboard Shortcuts tab; but, alas, not this ⌘⌥\ zoom-smoothing shortcut.


If anyone knows of a good hack for changing or disabling this keyboard shortcut, please let me know.


[**Update:** The ⌘⌥\ shortcut has apparently been used for toggling zoom-smoothing since 10.2, when *keyboard-based* zooming was introduced (in the Universal Access panel in System Prefs); I never noticed because I never use the keyboard-based zooming feature, and it (the shortcut) has been off by default up until 10.4.8. But the point remains: most of the other Universal Access keyboard shortcuts are adjustable; this one should be, too.]


---

1. Some readers report seeing this feature prior to 10.4.8; apparently it shipped with the drivers for the new Wireless Mighty Mouse, and perhaps also shipped in the version of 10.4.7 that shipped with some recent Macs. ↩︎
2. And TextWrangler. ↩︎



| **Previous:** | [Generalissimo Francisco Franco: Still Dead; Kieren McCarthy: Still a Jackass](https://daringfireball.net/2006/09/mccarthy_still_a_jackass) |
| **Next:** | [Brand New](https://daringfireball.net/2006/10/brand_new) |


PreviousNext