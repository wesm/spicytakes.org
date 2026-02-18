---
title: "Dictionary Look-Ups From BBEdit, Mailsmith, and TextWrangler"
date: 2005-05-07
url: https://daringfireball.net/2005/05/dictionary_bbedit
slug: dictionary_bbedit
word_count: 1417
---


The new Dictionary app is one of my favorite new features in Mac OS X
10.4. Dictionary’s primary advantage over online dictionaries —
including Sherlock’s — is that its database is stored on your
computer, and thus is always available; online dictionaries are
useless to an offline laptop. Plus, I like the presentation, and I
like the definitions. As a writer, Dictionary is pretty much exactly
what I want.


But, since I do the vast majority of my writing in BBEdit and
Mailsmith, I was faced with a problem. To be truly useful as a writing
aid, you need to be able to invoke your dictionary easily from the app
in which you’re writing. What I want to do is select a word in BBEdit
(or Mailsmith or TextWrangler) and tell Dictionary to look up that
word in one quick action. But:

- Dictionary’s “Look Up in Dictionary” contextual menu item
currently only appears in Cocoa NSTextView and WebView control
fields. Thus it doesn’t appear in BBEdit, TextWrangler, or
Mailsmith.
- Dictionary’s system-wide keyboard shortcut — Command-Control-D
by default, but configurable in the Keyboard & Mouse panel in
System Preferences — also only works in Cocoa NSTextView and
WebView fields.
**Update, 12 May 2005**: BBEdit 8.2.1 now supports the
Command-Control-D shortcut and inline Dictionary panel. Very, very
cool. I’m fairly certain Bare Bones is now the first third-party
developer to add support for these hooks.
- Dictionary does not have an AppleScript dictionary. (Technically,
it *does* have a scripting dictionary, but it’s just a default
Cocoa dictionary, and offers no scripting features for performing
definition look-ups, which means it’s effectively useless.)
- Dictionary ostensibly allows you to perform look-ups via the
`dict://` URL scheme, but, as I’ve [documented on my Tiger Details
report](http://daringfireball.net/misc/2005/04/tiger_details#dict-urls), this feature is half-baked at best, and for some users
doesn’t seem to work at all.


That leaves two options, both of which I’ve found to work very well.


## ‘Look Up in Dictionary’ Service


Dictionary’s menu command in the Services menu works just fine from
BBEdit/TextWrangler/Mailsmith. The only downside is that it doesn’t
have a keyboard shortcut, and mousing into the Services sub-menu is
too inconvenient.


However, you can easily add a custom shortcut to the “Look Up in
Dictionary” Services menu item:

1. Open the Keyboard & Mouse panel in System Preferences, then click on
the Keyboard Shortcuts tab.
2. Click the “+” button to add a new shortcut.
3. In the configuration sheet, you can either choose “All Applications”
or just pick a single application. Even though it seems as though
there’s just one system-wide Services menu, the truth is that each
app creates its own instance of the Services menu. So if you want,
you can customize a Service menu item shortcut for just one particular
app. For consistency, though, I think it’s better to choose “All
Applications” and use the same shortcut everywhere.
4. Type “Look Up in Dictionary” in the Menu Title field. This must match
exactly.
5. Type your new shortcut in the Keyboard Shortcut field. You can pretty
much type whatever shortcut you want here, and it’s important to note
that the system does not perform any conflict checking, so you can 
use a shortcut that’s already used by other menu items (including
another command in the Services menu itself).
6. You’ll need to quit and relaunch any apps that are currently
running to use this new shortcut.


## Scripting the Dictionary App via GUI Scripting


I’m so lazy that I don’t even want to have to select a word before
doing a look-up on it. If I don’t have a selection, I’d like my
look-up command to use whatever word the insertion point is touching.
This means the Services menu command is out, because it’s only enabled
when there’s a range of selected text.


We can use AppleScript to get the “current word” adjacent to the
insertion point (cf. “[‘Select Word’ Script for BBEdit](http://daringfireball.net/2003/09/select_word_script_for_bbedit)”,
published here back in 2003), but what can we do with it if Dictionary
isn’t scriptable and its support for `dict://` URLs is broken? We
resort to [GUI Scripting](http://www.apple.com/applescript/uiscripting/).


Here’s the script. (To use it with Mailsmith or TextWrangler, all you
need to do is change the `tell application "BBEdit"` line.)


```
-- This script uses the selected text in the frontmost window
-- as a query string for the Dictionary app. If there is no selection,
-- it uses whatever word the insertion point is touching.

tell application "BBEdit"
   tell window 1
      set dict_query to selection
      if (dict_query = "") or (class of dict_query is not character) then
         set sel_offset to characterOffset of selection
         set cur_line to startDisplayLine of selection
         try
            select (last word of display_line cur_line ¬
               whose characterOffset ≤ sel_offset)
            set dict_query to selection as text
         on error
            set dict_query to text returned of ¬
               (display dialog "Look Up in Dictionary:" default answer ¬
                  "" buttons {"Cancel", "Look Up"} default button 2)
         end try
      end if
   end tell
   set dict_query to dict_query as text
end tell

if dict_query is not "" then
   tell application "Dictionary" to activate
   tell application "System Events"
      tell process "Dictionary"
         set tf to text field 1 of group 1 of tool bar 1 ¬
            of window "Dictionary and Thesaurus"
         set value of tf to ""
         tell tf
            -- set value to dict_query
            keystroke dict_query
            keystroke return
         end tell
      end tell
   end tell
end if

```


The first part of the script sets `dict_query` to the text of the
current selection. If there is no text selection, then it tries to get
the “current word” adjacent to the insertion point. If that fails
(e.g. if the insertion point is currently on a blank line), it uses a
dialog box to prompt for a word to look up.


The GUI scripting part has two key steps (after making sure the
`dict_query` variable isn’t empty and activating the Dictionary app):

1. Set the tell target to the search field in Dictionary’s main
window’s toolbar.
2. Simulate keystrokes to enter the `dict_query` string in the field.
3. Simulate a “return” keystroke.


The script uses the GUI scripting `keystroke` command instead of
setting the value of the search field and then simulating a click on
the magnifying glass search button; in my experience this works
better. Also, the script first sets the value of the search text
field to the empty string; without this step, the new query is
sometimes appended to the existing query instead of replacing it.


Save the script in your BBEdit (or Mailsmith or TextWrangler) scripts
folder, then use the Scripts palette to assign a keyboard shortcut,
and you’re set. (I’ve got mine bound to Control-D, which is super-easy
to type.)


Remember that to use GUI Scripting, you need to turn it on; it’s off
by default. On Mac OS X 10.4, the easiest way to turn it on is to use
the new AppleScript Utility app (in the “AppleScript” folder inside
the top-level “Applications” folder). If you try running this script
with GUI Scripting turned off, you’ll get strange
“NSReceiverEvaluationScriptError” error messages.


## A Brief Plug for PreFab UI Browser


The GUI scripting part of the script looks fairly simple, but how did
I know that the name of the magnifying-glass icon button was “search”?
You need to know this, because simply setting the value of the text
field doesn’t initiate a look-up. For that matter, how did I know how
to string together the chain of objects to address the search text
field in the first place — the “`text field 1 of group 1 of tool bar
1`” bit?


Apple’s solution is the painfully stark [UI Element Inspector](http://www.apple.com/applescript/uiscripting/02.html) app.


But the only good way to determine the syntax for addressing interface
elements via GUI scripting is to use [PreFab UI Browser](http://www.prefab.com/uibrowser/), an excellent
utility that puts Apple’s UI Element Inspector [to shame](http://www.prefab.com/uibrowser/vs_ui_element_inspector.html). It costs
$55, but has a lenient and generous demo period during which you can
try it for free.


Trying to accomplish something with GUI scripting without using UI
Browser is like trying to walk around blindfolded. If not for UI
Browser, I seriously doubt I would have even attempted this script.


It’s a completely valid gripe that Dictionary ought to provide a
proper AppleScript command for performing look-ups, and I hope this
gets addressed in a future update. But in the meantime, GUI scripting
gets the job done today.



| **Previous:** | [The Tiger Details List](https://daringfireball.net/2005/04/tiger_details_list) |
| **Next:** | [I Suppose It Has to Be OK](https://daringfireball.net/2005/05/has_to_be_ok) |


PreviousNext