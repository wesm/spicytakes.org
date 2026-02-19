---
title: "Developer Goodies"
date: 2002-12-23
url: https://daringfireball.net/2002/12/developer_goodies
slug: developer_goodies
word_count: 1044
---


Three interesting bits of developer tool news from the weekend:


## Project Builder Support for BBEdit


[The latest version of Project Builder](http://developer.apple.com/tools/macosxtools.html) finally supports external editors, most especially the two text editors at opposing ends of the spectrum: BBEdit and emacs. This is delightful news. I’ve only tinkered with it so far, but it seems decent enough.


You probably don’t use developer tools like Project Builder, but if you use a Mac, you’re no more than one degree of separation away from someone who does. Good development tools make programmers happy, and happy programmers write better software.


## Script Editor 2.0 Beta


Apple released a [beta version of Script Editor 2.0](http://www.apple.com/applescript/script_editor/), rewritten for Mac OS X. It is most definitely a major improvement over the old Script Editor, which is so woefully underpowered as to give AppleScript as a whole a bad name. The old Script Editor has been around for at least 10 years, and still doesn’t have a Find command. In a programming editor.


The new Script Editor not only adds a Find dialog, but also sports a revamped user interface, making more information available in script windows. For example, instead of a single “Result” window to display the result of the most recently executed script, the new Script Editor offers a Result tab at the bottom of each script window. Nice.


To top it off, the new Script Editor is itself a scriptable application. The old Script Editor, shamefully, is not. Other modern amenities, such as multiple undo, are supported.


In cursory testing, it seems stable. Its “beta” status might be more an indication of a lack of UI refinement than under-the-hood
instability. For example, the Font and Format menus both seem
superfluous — there seems to be no need for any of the commands in either of these menus.


It’s no [Script Debugger](http://www.latenightsw.com/sd3.0/index.html), but that’s OK — Script Debugger is overkill for most users. The new Script Editor is like iMovie; Script Debugger is like Final Cut Pro. The old Script Editor is like trying to make a flip-book-movie using a pencil and wet paper.


## GUI Scripting


And then there’s [GUI Scripting](http://www.apple.com/applescript/GUI/), which MDJ/MWJ publisher Matt Deatherage described as “this
weekend’s ‘holy crap’ link” on the MacJournals-Talk mailing list. From Apple’s description:


> Scripters have often requested the ability to control, via
> 	AppleScript, applications which either do not have AppleScript support or
> 	are only partially scriptable. The new Developer Tools release contains a
> 	beta version of the System Events application incorporating support for
> 	scripting the GUI (Graphic User Interface) of applications. 
>  Using this version of the System Events application, AppleScript
> 	scripts can select menu items, push buttons, enter text into text fields,
> 	and generally control the GUI of most non-Classic applications.


Holy crap is right.


If you don’t use AppleScript, this might not sound like a surprising feature. But the sort of “macro” scripting described above runs contrary to everything AppleScript has been capable of in the past. AppleScript is not a macro language that acts like an automated user, driving the visual interface of an application. Instead, Apple is a language designed for sending Apple events, to drive an internal interface to scriptable applications. (GUI Scripting does not bode well for [QuicKeys](http://www.quickeys.com/), I think.)


What that means is that prior to GUI Scripting, AppleScript was only useful for automating scriptable applications. Far too many Mac applications aren’t scriptable, and even among those that are, many offer scripting dictionaries that are some combination of inadequate, superficial, and crummy.


And so some would often complain that AppleScript is inadequate, because it does not allow for scripting unscriptable applications. Others would complain that more applications should be scriptable. Such as, for example, many of Apple’s own applications, many of which aren’t scriptable in any serious sense of the word.


And indeed, many of the example scripts on Apple’s GUI Scripting web page are poking about Mac OS X applications from Apple, applications like System Preferences which *should* be truly scriptable, but aren’t.


For example, look at this snippet from a GUI Scripting example that changes the mouse (or trackpad) settings:


```

tell application "System Events"
   tell process "System Preferences"
      click menu item "Mouse" of menu "View" of menu bar 1
      delay 3
      tell window "Mouse"
         -- powerbooks will have two tabs: mouse and trackpad
         if (exists tab group 1) then
         tell tab group 1
            -- tabs are considered radio buttons
            click radio button "Mouse"
            delay 1
            -- Tracking Speed: 0.0 to 7.0
            set value of slider 1 to 7.0
            -- Double-Click Speed: 0.0 to 1.8
            set value of slider 2 to 1.2

```


That *sucks*. It means your script is utterly dependent on the exact layout of the visual interface. Instead of referring to named objects and classes, you must refer to GUI controls *by position*. If the layout of the Mouse prefs panel changes in the future, this script will break. Or worse, the script will misbehave in seemingly random ways; if the sliders for tracking speed and double-click speed swap positions in a future version of the Mouse panel, the above script will still run, but it will change the wrong settings.


Yes, it’s just an example script. But if Apple’s going to acknowledge that you might want to change the settings for your mouse via AppleScript, they ought to allow you to do it the right way.


This is not to say the GUI Scripting concept doesn’t have its appeal. For one thing, I can imagine that it will be very useful for simulating user actions when QA-testing applications. And there’s no denying the reality that there exist many applications which do not properly support OSA scripting, yet which would be handy to automate. What I fear, however, is that GUI Scripting will provide cover to lazy and ignorant developers who do not wish to provide genuine scripting interfaces to their applications. *We don’t need to provide a decent scripting dictionary, just use GUI Scripting.*


I’d feel a lot worse about this, however, if it weren’t for the Script Editor 2.0 beta, which shows that at least some developers at Apple are still interested in creating good scripting interfaces.



| **Previous:** | [bbdiff 1.1](https://daringfireball.net/2002/12/bbdiff_11) |
| **Next:** | [Rascal](https://daringfireball.net/2002/12/rascal) |


PreviousNext