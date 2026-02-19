---
title: "Save and Restore Safari URLs"
date: 2003-02-03
url: https://daringfireball.net/2003/02/save_and_restore_safari_urls
slug: save_and_restore_safari_urls
word_count: 1191
---


The whole point of scriptable application software is that it allows us, the users, to add and tweak features. By spending the time up-front to make an application scriptable, developers save time down the line, by allowing users to add new features on their own, using (relatively) simple scripts.


For example, I’ve long been annoyed by the inability of web browsers to remember which URLs were open the last time they were quit. I typically have half a dozen or so web browser windows open at any given moment, open to URLs I mean to read in the future.


Having all these windows open makes me reluctant to quit my browser. I don’t want to quit, because I need to do something to remember the open URLs which I haven’t finished reading. I don’t want to bookmark them — that would be overkill. These are URLs I want to read once, then close. These aren’t URLs I want to remember forever; if I were to bookmark them, I’d need to clean them out of my bookmark list later, after reading them. Not to mention that there’s no easy to way to add bookmarks for all open windows in one step.


We can solve this problem with AppleScript. I use [Apple’s system-wide script menu for Mac OS X](http://www.apple.com/applescript/script_menu/), so I saved these scripts in the “Scripts” folder in the “Library” folder in my home directory. (Actually, I saved them in a “Safari” folder inside the Scripts folder, grouping them together in a sub-menu of the main scripts menu.)


The first script, which we’ll name “Save Safari URLs”, will do the following:

1. Create a list of URLs for each Safari document window.
2. Write that list to a text file named “Safari Saved URLs” in the Preferences folder. One URL per line. Overwrite the previous contents of the file — we only want to remember the URLs that are open right now.


We’ll name the second script “Restore Safari URLs”. It will:

1. Read the “Safari Saved URLs” text file in the Preferences folder.
2. Create a list of URLs.
3. Tell Safari to open each URL in the list.


While we’re at it, we’ll create a third script, “Clear Safari URLs”, which will simply delete the contents of the “Safari Saved URLs” file.


## Save Safari URLs


```

tell application "Safari"
    set url_list to URL of every document
end tell

-- convert url_list to text
set old_delim to AppleScript's text item delimiters
set AppleScript's text item delimiters to return
set url_list to url_list as text
set AppleScript's text item delimiters to old_delim

-- get path to prefs file where URLs will be stored
set prefs_folder to path to preferences folder as string
set prefs_file to prefs_folder & "Safari Saved URLs"

try
    set open_file to ¬
        open for access file prefs_file with write permission
    -- erase current contents of file:
    set eof of open_file to 0
    write url_list to open_file starting at eof
    close access open_file
on error
    try
        close access file prefs_file
    end try
end try

```


How it works:


First, we create `url_list`, a list of the URLs from each Safari document. Next, we want to convert `url_list` from an AppleScript list to text. We want text because we’re going to write the list to a simple text file. When you tell AppleScript to convert a list to text, it separates list items using a global AppleScript property called `text item delimiters`. The default value for `text item delimiters` is `""`, the empty string. (Actually, to be pedantic, the default value is `{""}`, a list with one value, the empty string.) This means that by default, when you convert a list to text, the list items are concatenated together with no separators. If this is your list:


```

{"one", "two", "three"}

```


converting it to text with the default delimiter will yield:


```

onetwothree

```


We want to write the URLs to a text file, one URL per line. So, we want to set `AppleScript's text item delimiters` to `return`. (`Return` is an AppleScript keyword to represent the \r character.)
After doing so, converting the list above to text would yield:


```

one
two
three

```


However, because `text item delimiters` is a global AppleScript property shared by all AppleScripts on your computer, the right thing to do is to save the current value, change `text item delimiters` to what we want, then restore the previous value when we’re finished.


Next, we create a string with the path to the preferences file in which we’re going to store the URLs. Then we write the URLs to the file. By setting the file’s `eof` (end-of-file) to zero, we’re deleting any existing contents of the file. In other words, when this script runs, it overwrites any existing URLs in the file; it does not append. The whole thing is wrapped in a `try` block so that if we catch any errors, we still close the file before the script exits.


## Restore Safari URLs


```

-- get path to prefs file where URLs are stored
set prefs_folder to path to preferences folder as string
set prefs_file to prefs_folder & "Safari Saved URLs"

try
    set open_file to ¬
        open for access file prefs_file without write permission
    set url_list to read open_file using delimiter return
    close access open_file
    tell application "Safari"
        repeat with the_url in url_list
            open location the_url
        end repeat
    end tell
on error
    try
        close access file prefs_file
    end try
end try

```


This one is pretty straightforward, especially once you understand how the “Save Safari URLs” script works.


First, we create a string pointing to our preferences file. Then we open the file. We read the contents of the file into the variable `url_list`. The `using delimiter return` part tells AppleScript to give us the file contents as a list, using `return` as the separator for each item. In other words, each line of the file as a separate list item.


If this is successful, we loop through the list, and tell Safari to open each URL. We put the Safari `tell` block in the `try` block, because we only want it to run if the prefs file was read successfully.


## Clear Safari URLs


```

display dialog ¬
    "Clear stored Safari URL list?" buttons {"Cancel", "Clear"} ¬
    default button 2 with icon note

if button returned of result is "Clear" then
    -- get path to prefs file where URLs will be stored
    set prefs_folder to path to preferences folder as string
    set prefs_file to prefs_folder & "Safari Saved URLs"
    
    try
        set open_file to ¬
            open for access file prefs_file with write permission
        -- erase current contents of file:
        set eof of open_file to 0
        close access open_file
    on error
        try
            close access file prefs_file
        end try
    end try
end if

```


This is really simple. Open the prefs file. Set `eof` to zero. Close the file. The prefs file is now empty. For something destructive like this, we ask for confirmation by popping up a dialog box. Clearly named buttons help keep things, well, *clear*.



| **Previous:** | [Scripting Safari URLs Update](https://daringfireball.net/2003/01/scripting_safari_urls_update) |
| **Next:** | [Remember IE?](https://daringfireball.net/2003/02/remember_ie) |


PreviousNext