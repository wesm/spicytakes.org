---
title: "AppleScript ‘Whose’ Clauses"
date: 2003-09-19
url: https://daringfireball.net/2003/09/applescript_whose_clauses
slug: applescript_whose_clauses
word_count: 358
---


AppleScript gets a rap for being easy-to-read, but hard-to-write. And it’s a somewhat deserving reputation. But the problem isn’t with the language itself, per se, but rather with the syntactical vagaries of disparate application scripting dictionaries. The AppleScript language itself is rather small, and in fact offers some very neat features.


One of these is the concept of a *filtered reference*, using a `whose` clause.


For example, using BBEdit, you can get a list of every word in the front window like this:


```

tell application "BBEdit"
   tell window 1
      set my_list to every word 
   end tell
end tell

```


But what if we only want the words that contain the letter “z”? In most programming languages, the way you’d tackle this would go something like this:

1. Create a list (a.k.a. array) of all the words.
2. Loop through each word, one at a time.
3. Check if the current word contains the letter “z”; if so, append it to a second list.


With an AppleScript `whose` clause, however, we can do this all at once, like this:


```

tell application "BBEdit"
   tell window 1
      set my_list to every word whose characters contains "z"
   end tell
end tell

```


Or if you only want the words that start with “z”:


```

tell application "BBEdit"
   tell window 1
      set my_list to every word whose first character is "z"
   end tell
end tell

```


You can use `whose` clauses to create filtered references in any decently-scriptable app. For example, in the Mac OS X Finder, you can get a list of all the items in your Documents folder that start with “A”:


```

tell application "Finder"
   set f to folder "Documents" of home
   set my_list to every item of f whose name starts with "A"
end tell

```


Or every file in your Documents folder with BBEdit’s creator code:


```

tell application "Finder"
   set f to folder "Documents" of home
   set my_list to every file of f whose creator type is "R*ch"
end tell

```


We’ll put `whose` clauses to work next week.



| **Previous:** | [IBM Compatible](https://daringfireball.net/2003/09/ibm_compatible) |
| **Next:** | [‘Select Word’ Script for BBEdit](https://daringfireball.net/2003/09/select_word_script_for_bbedit) |


PreviousNext