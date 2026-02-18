---
title: "Using Keyboard Maestro to Intercept Keyboard Shortcuts Usurped by the System"
date: 2006-10-16
url: https://daringfireball.net/2006/10/keyboard_maestro
slug: keyboard_maestro
word_count: 1209
---


A few weeks ago when Apple released Mac OS X 10.4.8, I wrote about the new [Zoom With Scroll Wheel feature](http://daringfireball.net/2006/09/zoom_using_scroll_wheel) in the Keyboard & Mouse panel of System Preferences. I noted the following downside to what is otherwise a very cool new feature:


> My only gripe is the ⌘⌥\ (Command-Option-Backslash) shortcut
> attached to the smoothing option. If you turn the “Zoom using
> scroll wheel” option on, this keyboard shortcut is applied
> system-wide, even when you aren’t zooming. That’s a problem if
> you’re using any applications that use this keystroke — and
> since BBEdit and Mailsmith use this for the Hard Wrap command,
> and I’ve got about 10 years of muscle memory using this command
> with this shortcut every single day, it’s a problem for me.
> […]
> And even if it really does deserve a system-wide shortcut, it
> ought to be configurable using the Keyboard Shortcuts tab in the
> Keyboard & Mouse prefs panel. Most of the other system-wide
> default keyboard shortcuts can be changed or just plain turned
> off in the Keyboard Shortcuts tab; but, alas, not this ⌘⌥\
> zoom-smoothing shortcut.


Just to clarify the conflict with BBEdit: the default shortcut for BBEdit’s “regular” Hard Wrap command (“Hard Wrap…” in the Text menu) is Command-Backslash. This brings up (or should I say “drops down”?) the Hard Wrap sheet, where you can specify your text-wrapping options. The Command-Option-Backslash shortcut is for the “don’t show me the configuration sheet, just do it using my current settings” Hard Wrap command (“Hard Wrap”, no ellipses, in the Text menu; when you hold down the Option key “Hard Wrap…” turns into “Hard Wrap”).


I really do use this shortcut all day, every day. It’s just one of those keyboard sequences that is burned-in deep down in my muscle memory. Not quite as far down as, say ⌘Z, ⌘X, ⌘C, and ⌘V, but pretty far down.


So, the problem is this: I want to be able to use the new Zoom With Scroll Wheel feature, but I don’t want to have to learn a new keyboard shortcut for hard wrapping in BBEdit and Mailsmith.


[Keyboard Maestro](http://www.keyboardmaestro.com/main/) to the rescue.


Keyboard Maestro is a $20 utility from Stairways Software (makers of Interarchy). Stairways bills it as a “macro utility”, and that’s as good a description as any. There are two software components to Keyboard Maestro:

- The main Keyboard Maestro application — this is what you use
to diddle with options, configure keyboard shortcuts, and define
and edit your macros.
- Keyboard Maestro Engine — an invisible background application
that launches as a login item; this is the software that
“listens” for your macro shortcuts and executes the associated
macros.


No haxie or input manager trickery involved. The engine is lean and mean: it consumes only 696 *kilobytes* of private memory here on my PowerBook.


When the Zoom With Scroll Wheel feature is turned on, regular apps like BBEdit no longer “see” that key sequence — the system consumes it at a lower level and doesn’t pass it along. Keyboard Maestro, however, still sees it, so you can assign that same sequence to a macro.


The first thing I did was create a new macro group in Keyboard Maestro, and named it “Bare Bones”. The macros in each group can be applied system-wide, or only to a list of certain apps. For this group, I’ve set it to apply only to BBEdit and Mailsmith.


The group contains one macro, which I named “Hard Wrap”, and assigned the trigger Command-Option-Backslash.


I thought of two ways to use Keyboard Maestro macro actions to invoke BBEdit’s Hard Wrap command. The first is “Select Menu Item”; you specify the name of the menu and the name of the menu command, then when you hit the macro’s keyboard shortcut, Keyboard Maestro simulates the selection of that menu item. The second would be to first assign a new keyboard shortcut to this command from with BBEdit’s own preferences window; then use Keyboard Maestro’s “Simulate Keypress” action to fire off the new shortcut you assigned to the Hard Wrap command.


Both techniques work, but neither is perfect. One minor problem with the “Select Menu Item” technique is that Keyboard Maestro sends the application an “activate” event before simulating the selection of the menu item. As a result, all current windows belonging to BBEdit (or whatever app you’re using this macro with) pop forward. Not a huge deal, but somewhat distracting.


The problem with the “set a new shortcut in BBEdit, then use Keyboard Maestro to simulate that shortcut using the old shortcut as the trigger” technique is that it doesn’t quite work reliably if the new shortcut you specify for the command in BBEdit uses the same keys as the Keyboard Maestro macro trigger. For example, I tried changing the shortcut within BBEdit from Command-Option-Backslash to *Control*-Option-Backslash; but that only worked from Keyboard Maestro when I very quickly tapped the Command-Option-Backslash macro trigger. I suspect the problem is that if you don’t type the sequence *very quickly*, the keys you’re pressing on the keyboard conflict with the simulated keypress events Keyboard Maestro generates. After I switched the shortcut within BBEdit to the utterly-out-of-the-way Control-F1, it worked fine.


So, here’s what I wound up doing. I changed the keyboard shortcut for the Hard Wrap command in BBEdit and Mailsmith to Command-Option-Return. That’s almost the same as Command-Option-Backslash (at least on a U.S. keyboard layout), and it makes some mnemonic sense, using the Return key for a command that adds hard line breaks. In Keyboard Maestro, I’ve set the macro to use the Select Menu Item action. My goal is to wean myself away from the old shortcut to the new one; but until the new muscle memory kicks in, the old shortcut will still work, albeit with the minor annoyance of all current BBEdit (or Mailsmith) windows popping to the front, which annoyance I’m thinking might serve as encouragement to remember to use the new shortcut.


Ideally, I try to run with as few system modifications as possible, and when I’m using one simply to enable a habit, I try to break that habit. Sometimes it takes a while — I ran [Unsanity’s WindowShade X](http://www.unsanity.com/haxies/wsx) for at least a year back in the 10.1 era before my window-shading habit faded away.


## Addenda

- Even though Keyboard Maestro still sees keyboard shortcuts that
are used by the system, it doesn’t *eat* them. So while you can
assign Command-Option-Backslash to a Keyboard Maestro macro, the
system still sees it, too — so when you invoke a macro assigned
to this trigger, it works, but the system will *also* toggle the
anti-aliasing setting for screen zooming.
- Keyboard Maestro is not a universal binary. It does work fine
under Rosetta, however.
- You can probably do something similar using other utilities
such as [QuicKeys](http://www.quickeys.com/products/qkx.html) or [iKey](http://www.scriptsoftware.com/ikey/), but I didn’t try any other
software because I already had a license for Keyboard Maestro.
If anyone sends me reports about other utilities that can
see and use keyboard shortcuts claimed by the system, I’ll list
them in an update.



| **Previous:** | [Processing Processes](https://daringfireball.net/2006/10/processing_processes) |
| **Next:** | [Membership Renewal](https://daringfireball.net/2006/10/membership_renewal) |


PreviousNext