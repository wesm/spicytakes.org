---
title: "Remember IE?"
date: 2003-02-03
url: https://daringfireball.net/2003/02/remember_ie
slug: remember_ie
word_count: 494
---


Back in the old days, the leading browser for Mac OS X was Internet Explorer. That’s right, kids — Microsoft used to write Macintosh software.


In addition to offering better web standards support than any other browser in that era, IE for Mac was also quite scriptable. You could, in fact, make minor adjustments to our [Save and Restore Safari URLs](http://daringfireball.net/2003/02/save_and_restore_safari_urls.html) scripts posted earlier today, and use them with IE.


And, remarkably, aftering making these changes, the same scripts could be used both on Mac OS X and on the now-long-forgotten Mac OS 9 (a relic so old that it used the rainbow-colored Apple logo; ask your grandpa about it).


The biggest change is in how we get the list of currently open URLs. Whereas in Safari we simply say:


```

tell application "Safari"
    set url_list to URL of every document
end tell

```


IE forces us to create this list by hand, parsing the results of non-object-model scripting verbs. This is how [Abraham Lincoln](http://www.whitehouse.gov/history/presidents/al16.html) wrote scripts:


```

set url_list to {}
tell application "Internet Explorer"
    set win_list to ListWindows
    repeat with w in win_list
        set the_info to GetWindowInfo (w)
        copy item 1 of the_info to end of url_list
    end repeat
end tell

```


Without further ado, the scripts:


## Save IE URLs


```

set url_list to {}

tell application "Internet Explorer"
    set win_list to ListWindows
    repeat with w in win_list
        set the_info to GetWindowInfo (w)
        copy item 1 of the_info to end of url_list
    end repeat
end tell

-- convert url_list to text
set old_delim to AppleScript's text item delimiters
set AppleScript's text item delimiters to return
set url_list to url_list as text
set AppleScript's text item delimiters to old_delim

-- get path to prefs file where URLs will be stored
set prefs_folder to path to preferences folder as string
set prefs_file to prefs_folder & "Internet Explorer Saved URLs"

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


## Restore IE URLs


```

-- get path to prefs file where URLs are stored
set prefs_folder to path to preferences folder as string
set prefs_file to prefs_folder & "Internet Explorer Saved URLs"

try
    set open_file to ¬
        open for access file prefs_file without write permission
    set url_list to read open_file using delimiter return
    close access open_file
    tell application "Internet Explorer"
        repeat with the_url in url_list
            GetURL the_url
        end repeat
    end tell
on error
    try
        close access file prefs_file
    end try
end try

```


## Further Reading


[Jesse Shanks](http://www.blankreb.com/studioarticles.php?ID=22):


> Combining Safari, AppleScript and the nature of the OS X system, a new and more efficient way of browsing can be created that makes the question of tabbed browsing somewhat irrelevant.



| **Previous:** | [Save and Restore Safari URLs](https://daringfireball.net/2003/02/save_and_restore_safari_urls) |
| **Next:** | [Enkode This](https://daringfireball.net/2003/02/enkode_this) |


PreviousNext