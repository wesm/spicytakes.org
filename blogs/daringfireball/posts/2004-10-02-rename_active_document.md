---
title: "‘Rename Active Document’ Script for BBEdit"
date: 2004-10-02
url: https://daringfireball.net/2004/10/rename_active_document
slug: rename_active_document
word_count: 618
---


A feature I’ve always wanted, but which no application I’m aware of
offers, is the ability to rename an open document. “Save As” is not the
same thing — because while it allows you to save a document with a new
name, it leaves behind the previously-saved copy of the file with the
old name.


Typically, to rename an open document, you need to do something like this:

1. Save and close the document.
2. Switch to the Finder.
3. Select the document file.
4. Rename.
5. Re-open.


You can skip steps 1 and 5 in apps that are savvy enough to recognize
when the name of an open document file has been changed in the Finder.
But even then, this has always struck me as something that ought to be
doable in a single step.


So, here’s an AppleScript for BBEdit 8 that does it. When you run the
script, it pops up a simple dialog box containing a text edit field, set
with the current name of the frontmost document. To rename the document,
just type a new name and click the Rename button.


Not only is it multi-document window savvy (renaming the current
document in a multi-doc window), but it *also* allows you to rename new
untitled documents which haven’t yet been saved. I use this for
temporary scratch documents which I don’t need to keep, but for which
I’d like to have more descriptive names than something like
“untitled
text 5”.


(This script will *not* work with versions of BBEdit prior to 8.0,
because it depends on recent improvements to BBEdit’s scripting syntax.)


Here’s the script:


```
tell application "BBEdit"
    activate
    set old_name to name of text window 1
    set dialog_result to display dialog ¬
        "Rename active document:" default answer (old_name) ¬
        buttons {"Cancel", "Rename"} default button 2 ¬
        with icon note
    if button returned of dialog_result = "Rename" then
        set new_name to text returned of dialog_result
        set d to active document of text window 1
        if (d's on disk) then
            set the_file to d's file
            tell application "Finder"
                set name of the_file to new_name
            end tell
        else -- it's a document that has never been saved
            set name of d to new_name
        end if
    end if
end tell

```


To use it, copy and paste the script into a new Script Editor document,
then save it in your ‘`~/Library/Application Support/BBEdit/Scripts/`’
folder.


## How It Works


First, we save the current name of the frontmost document by getting the
name of `text window 1`. We save this in a variable named `old_name`.
Then we use AppleScript’s `display dialog` command to present a dialog
box with a text edit field, the contents of which are set to `old_name`.


A variable named `dialog_result` is used to store the result record from
the `display dialog` command. This record contains which button was
clicked to dismiss the dialog and the string in the dialog’s text edit
field.


If the user clicks Rename, we get the new document name from the
`dialog_result` record, and create a variable named `d` that references
the active document of text window 1.


BBEdit’s `document` object has an “on disk” property; this is a boolean
value that’s true if the document is represented by a file somewhere in
your file system, false otherwise (like, say, a new document that has
never been saved). If `(d's on disk)` is true, we tell the Finder to
change the name of `d`’s associated file — “file” is another property
defined by BBEdit’s `document` object.


Otherwise, if `(d's on disk)` is false, we simply change the value of
`d`’s “name” property.



| **Previous:** | [Windows Versus the World](https://daringfireball.net/2004/09/windows_vs_world) |
| **Next:** | [BBEdit Soft Wrap Toggling](https://daringfireball.net/2004/10/bbedit_soft_wrap_toggling) |


PreviousNext