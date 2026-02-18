---
title: "Opening Files Together in a New BBEdit Text Window"
date: 2004-09-17
url: https://daringfireball.net/2004/09/bbedit_open_together
slug: bbedit_open_together
word_count: 947
---


As mentioned in my [BBEdit 8 review](http://daringfireball.net/2004/09/bbedit_8), BBEdit offers a few new
options (in the Documents panel in the preferences window) to control
the behavior of the new multi-document text windows. You can either have
new and opened documents open by default in the front window, or you can
have them open by default in a new window by themselves (i.e., just like
BBEdit 7 and earlier).


These options are perfect if you want just one window with all
your open documents, or if you want to stick with the traditional
one-document-per-window model.


But what I want is something in-between. By default, I want documents to
open using the traditional individual-window model. But I also want to
be able to open a group of related files all at once, together in a
single new window — in a single action from the Finder.


So, I wrote an AppleScript to do this, which I’ve named “BBEdit - Open
Together”. I’m using it with Brent Simmons’s free [Big Cat Scripts
contextual menu plug-in](http://ranchero.com/bigcat/), so that from the Finder, I can simply
select the files I want to open and then choose it from the Scripts
sub-menu that Big Cat adds to the Finder’s contextual menu. To use it
with Big Cat, copy the script below, paste it into a new Script Editor
document, and save it here (in “Script” format):


```
~/Library/Application Support/Big Cat Scripts/Files/

```


This script might be useful regardless of your default document-opening
preference.


[**Update, 30 March 2005:** Scripting improvements in BBEdit 8.1 have made this much easier than it was in BBEdit 8.0. See the [updated script here](https://daringfireball.net/2005/03/open_together_in_bbedit).]


Here’s the source:


```
on main(file_list)
    tell application "BBEdit"
        set w to make new text window
        set show documents drawer of w to true
        set show navigation bar of w to true
        -- Get the ID of the untitled doc created with w:
        set doc_id to ID of document 1 of w
        try
            open file_list opening in w
        end try
        -- Close the untitled doc created with w:
        close document id doc_id
        activate
    end tell
end main

```


The `main` handler is Big Cat’s idiom for the main loop of the script.
If you don’t want to use Big Cat, you could change `main` to `open`, and
save the script as an application, which you could then invoke via
drag-and-drop.


Here’s how it works.


Regardless if you’re using a Big Cat `main` handler or an `open`
handler, `file_list` is a list of aliases, one for each of the files
selected in the Finder (if you’re using Big Cat) or dropped onto the
script application.


We start by telling BBEdit to create a new text window, and save a
reference to that window as `w`. We then make sure the document drawer
and navigation bar in the new window are both displayed.


Next comes the only part of the script that’s vaguely tricky. When you
create a new `text window` in BBEdit, it automatically contains a
new untitled document. There is no way to create an “empty” text window
containing no documents; when you close the last document in a window,
the window goes away.


So, for now, we store the `ID` property of the untitled document in the
new window. Every item in BBEdit’s scripting object model has a unique
ID.


Next, we tell BBEdit to open the list of aliases in `file_list`. There’s
no need to loop through the list and open them one at a time — in fact,
for a long list of files, it’s considerably more efficient to tell
BBEdit to open the list in one statement. The `in w` is all it takes to
open these files in the new text window we just created. If we left off
the `in w`, the files would open according to your preferences.


At this point, we have one last bit of cleaning up to do: closing the
untitled new document that was created when we made the new text window
`w`. We can’t use an index like `document 1 of w` or `document 2 of w`,
because we don’t know what the index number is for the untitled document
we want to close. Each window’s list of documents is sorted
alphabetically. This is why we stashed away the ID of the untitled
document — because IDs are unique.


(We couldn’t close this document *before* opening the files in
`file_list` because it was the only document in `w` at the time, and so
the entire window would have gone away when the document was closed.)


Lastly, we use the `activate` command to pop BBEdit to the front. This
brings every open BBEdit window forward; if you’d prefer only to pop the
newly-created window forward, you can change the `activate` line to:


```
tell w to activate

```


## Perl Implementation


(Added 21 September 2004.)


[Chris Nandor ported the above script to Perl](http://use.perl.org/~pudge/journal/20977):


> My sentiments about BBEdit’s new feature to allow opening
> files into the same window are similar to John Gruber’s. The
> difference is, I rarely use the Finder for opening files,
> compared to how often I use a terminal.
> I wrote to [Bare Bones] asking them to add a feature to the
> `bbedit` command line program allowing opening of multiple
> files to a single window, but in the meantime, I ported
> John’s AppleScript to Perl (which also allows it to be used,
> unchanged, with Big Cat).


Very useful if you open files from the command line, plus it’s a good
example showing how to translate AppleScript into Perl using Chris’s
`Mac::Glue` module.



| **Previous:** | [BBEdit 8](https://daringfireball.net/2004/09/bbedit_8) |
| **Next:** | [Sponsor This](https://daringfireball.net/2004/09/sponsor_this) |


PreviousNext