---
title: "‘Select Word’ Script for BBEdit"
date: 2003-09-23
url: https://daringfireball.net/2003/09/select_word_script_for_bbedit
slug: select_word_script_for_bbedit
word_count: 1875
---


Triple-clicking is the standard mouse gesture to select an entire line at once. But what if your hands are on the keyboard? BBEdit, not surprisingly, has you covered. The Edit → Select Line command (default shortcut: Cmd-L) selects the current line. A companion command, Select Paragraph (default shortcut: Cmd-Opt-L), takes things one step further: it selects the current line, as well as all adjacent lines that contain anything other than whitespace.


I use both these commands frequently; editing in an application that doesn’t support them drives me nuts. They’re as deeply ingrained in my muscle memory as the Cmd-A shortcut for Select All. BBEdit has supported both these commands at least as far back as 1993’s version 2.5, which is the oldest version of the user manual I have laying around.


A while back, it occurred to me that I’d like a third, similar command: Select Word. In the same way that Select Line acts like a triple-click, Select Word would act like a double-click: position the insertion point inside or next to a word, invoke the Select Word command, and that word would be selected, just as if you had double-clicked on it. If you had a partial word selected, Select Word would expand the selection to the entire word.


No need to file a feature request to Bare Bones, however — this command can be implemented using AppleScript. (And it works in Mailsmith, as well.)


My first crack at it worked, but was somewhat convoluted. I went about it the long way, by first finding the character position offset of the last word between the beginning of the document and the current selection; then selecting the first word after that offset. You don’t want to see that script; it’s junk.


I learned the correct way to do it from [a message Shane Stanley posted](http://search.barebones.com/action.lasso?-database=lists.fp3&-layout=import&-response=detail.html&-recid=12598675&-search) to the BBEdit-Scripting mailing list in March 2002. Here’s a slightly rewritten version of Stanley’s script:


```

tell application "BBEdit"
   tell window 1
      set sel_offset to characterOffset of selection
      select (last word whose characterOffset ≤ sel_offset)
   end tell
end tell

```


This script implements the Select Word command in just two lines (not counting `tell` statements).


The first line gets the offset of the current selection. A *characterOffset* is an integer value, corresponding to the position of a character in the document, starting from 1. There’s always a selection — an insertion point counts as a zero-width selection between two characters. Thus, the `characterOffset of selection` tells you where the selection starts.


The second line is where we determine which the “current” word is and select it. It’s a lot of action for one line of AppleScript. The use of a `whose` clause is essential; see my brief [introduction to whose clauses from last week](http://daringfireball.net/2003/09/applescript_whose_clauses.html) if you’re not familiar with them.


In this case, we’re using a `whose` clause to create a filtered reference to every word with an offset less than the offset of the current selection. Actually, *less than or equal to*, so that when the insertion point is positioned at the beginning of a word, we’ll select that word instead of the previous one. (To generate a `≤` sign in AppleScript, you can simply type “`<=`” in your script editor; when the script is compiled it’ll be turned into a genuine `≤`.)


Of those words, we’re interested in the last one. The AppleScript keyword `last` returns the last element of a list. Equivalently, we could instead have asked for `(word -1 whose characterOffset ≤ sel_offset)`; asking for the -1st element of a list returns the last item, the -2nd the second-to-last, etc.


Once we have a reference to the word we want to select, we can simply tell the window to select it. Being able to tell the window to select a word sounds quite obvious, and indeed is convenient, but if you think about it, it’s pretty slick. The long route would be to determine the length and offset of the target word, and then specify a range of characters as the object of the `select` command.


## Getting Specific


At this point, at first glance, it looks like we’re done. However, this script has a serious performance problem which will only appear when the script is invoked in largish documents (where by “largish”, I mean more than a few hundred lines or so; the exact point where performance goes from fast to slow isn’t important.)


The problem results from our `whose` clause. We ask for every word with an offset less than the offset of the current selection; what’s implied in this `whose` clause is that we’re asking for *every word in the window* whose offset is less than the selection offset. In a largish document, this can be many thousands of words. Instead of running instantaneously, as it does with small documents, it might take several seconds — which isn’t catastrophic, but which is annoying enough to defeat the purpose of the script.


Through the power of the `whose` clause, we, as scripters, do not need to allocate a temporary list variable to hold every word of the window, nor do we need to test each word to see if its offset meets our criterion. But this work still must be done — it’s performed behind the scenes, by AppleScript.


Imagine you own a robot, and that you live on a small island. You’re starting to get hungry for lunch, and so you tell your robot to go out and find the closest restaurant to your house that serves fresh-cut French fries. The robot leaves, locates every restaurant on the island that serves fresh-cut fries, computes the distance from each to your house, and then returns home with the results, a half-hour after departing.


Now imagine that you and your robot move from the small island to somewhere in North America. If you then issued the robot the same command, it’s going to be *long* past lunchtime when your robot arrives home with the result. (Even longer if the robot manages to cross the Panama Canal.)


The command, as given, doesn’t scale. You instead should say something like, “Find the closest restaurant that serves fresh-cut fries, within five miles of home.” Now, no matter where you live, your robot will return with the answer within a reasonable period of time.


That’s roughly analogous to the problem with the `whose` clause in our script. What we need is additional specificity, so that AppleScript doesn’t need to ask BBEdit to return a list of every word in the entire document. The nature of our script is that the word we’re looking for is always going to be on the same line as the selection. So, instead of asking for every word in the *document* whose offset is less than the selection offset, we can instead ask for every word on the current *line* with such an offset:


```

tell application "BBEdit"
   tell window 1
      set sel_offset to characterOffset of selection
      set cur_line to startLine of selection
      select (last word of line cur_line ¬
         whose characterOffset ≤ sel_offset)
   end tell
end tell

```


This script will perform poorly only when the current line is extremely long, as in like thousands-of-words-on-a-single-line long. We can even further isolate the chances of a problem by working with BBEdit’s *display* lines rather than regular lines.


In BBEdit, a plain old `line` is a run of text, separated by a return. Even if you have soft-wrapping turned on, so that long lines wrap on-screen, `lines` are separated by returns. These are also known as “hard lines” (in English, not AppleScript). A `display_line`, also known as a “soft line”, is what you see on-screen. If soft-wrapping is turned off, `lines` and `display_lines` are the same. Note the underscore in “`display_line`” — this was a nomenclatural decision Bare Bones made to avoid ambiguity; if it were a space instead of an underscore, it might look like the verb *display* followed by the object class *line*.


Switching to `display_lines` gives us this:


```

tell application "BBEdit"
   tell window 1
      set sel_offset to characterOffset of selection
      set cur_line to startDisplayLine of selection
      select (last word of display_line cur_line ¬
         whose characterOffset ≤ sel_offset)
   end tell
end tell

```


This script will only incur a performance penalty in the rare case where you have extremely long lines of text and soft-wrapping is turned off.


One last touch, the *coup de grâce*, then we’re done. As it stands, the script makes a slightly non-obvious assumption — namely, that the current `display_line` contains at least one word with an offset less than or equal to the selection offset. If it doesn’t — like say if the insertion point is at the beginning of an empty line, or a line that starts with whitespace — the script will generate an error. (The original script, has a similar but even less obvious assumption: that the entire text of the window contains at least one word preceding the selection.)


The solution is to use a `try` block, and if we catch an error, do something useful. A reasonable action would be to select the entire current line. And so, the final script:


```

tell application "BBEdit"
   tell window 1
      set sel_offset to characterOffset of selection
      set cur_line to startDisplayLine of selection
      try
         select (last word of display_line cur_line ¬
            whose characterOffset ≤ sel_offset)
      on error
         select display_line cur_line
      end try
   end tell
end tell

```


## Postscript: Missing But Obvious Optimizations


One could argue that the hypothetical robot in the aforementioned scenario ought to be able to deal, gracefully, with the original non-specific command. Even without any sort of “common sense” AI, given that we asked for the *closest* restaurant that serves fresh-cut fries, once the robot finds a single such restaurant, it could in theory be smart enough not to venture any further from home, and thus continue searching only for restaurants that are closer than the one already found.


Likewise, since we specifically ask only for the *last* word with an offset less than (or equal to) the selection offset, in theory, this query could be optimized such that there wouldn’t be a need to determine and allocate memory for a temporary list of *every* word in the document. It really only needs to go backwards from the current selection and find one word. But that’s not how AppleScript works, and so neither does our hypothetical robot.


In fact, there’s also no reason why returning of a list of many thousands of words couldn’t occur fairly quickly. By modern standards, a list/array with merely “many thousands” of elements ought to be allocated and iterated very quickly. I’m honestly unsure whether this problem is due to (a) inefficiencies in the current AppleScript engine itself; (b) constraints on the size of data passed through Apple events; (c) BBEdit’s handling of the `whose` clause Apple event; or (d) some combination of more than one of the above factors. However, in BBEdit’s defense, I see similar (if not worse) performance limitations in other text-suite savvy scriptable editors. Hopefully, at some point in the not-too-distant future, AppleScript will be able to handle much larger data sets quickly and efficiently.



| **Previous:** | [AppleScript ‘Whose’ Clauses](https://daringfireball.net/2003/09/applescript_whose_clauses) |
| **Next:** | [Interview: Michael Tsai](https://daringfireball.net/2003/09/interview_michael_tsai) |


PreviousNext