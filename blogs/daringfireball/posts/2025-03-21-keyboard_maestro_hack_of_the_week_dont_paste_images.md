---
title: "Keyboard Maestro Hack of the Week: Don’t Paste Images"
date: 2025-03-21
url: https://daringfireball.net/2025/03/keyboard_maestro_hack_of_the_week_dont_paste_images
slug: keyboard_maestro_hack_of_the_week_dont_paste_images
word_count: 981
---


My number one tip for becoming a Mac power user is to get into [Keyboard Maestro](https://www.keyboardmaestro.com/main/). Using Keyboard Maestro feels like gaining superpowers. I keep meaning to write more about Keyboard Maestro, and so I’m just going to start documenting all the little use cases I find for it. Here’s one from today.


I use [MarsEdit](https://redsweater.com/marsedit/) to publish at least 99 percent of the posts on this site. (The other 1 percent are posts I create on my phone, using the web interface for Movable Type.) I use MarsEdit *a lot*. About once a week or so, I accidentally try to paste text in MarsEdit when I think I have text on my clipboard, but it’s actually an image. When you paste an image in MarsEdit, it’s not like pasting into Mail or Notes or TextEdit, where the image just goes into the text. So MarsEdit, trying to be helpful, opens its [Upload Utility window](https://daringfireball.net/misc/2025/03/marsedit-upload-utility.png) — which, if I were using WordPress or some other CMS, might allow me to upload the image to my server for referencing from the HTML of the blog post. That’s not how my system works, and not how I want it to work, so every time this happens I have to close the Upload Utility window. And every time, I try to do this by hitting the Esc key on my keyboard. But the Upload Utility window isn’t a dialog box with a Cancel button that would be triggered by Esc. It’s a regular window. So after hitting the Esc key, which doesn’t do anything in this context, I then remember, once again, that I need to hit ⌘W instead. (I think I don’t naturally think to hit ⌘W because my instincts tell me ⌘W would try to close the blog window I’m writing in.)


Today it happened again, and finally the notion occurred to me that I could fix this with Keyboard Maestro. My first thought was that I could create a macro that *would* close the frontmost window in MarsEdit if, and only if, the frontmost window was named “Upload Utility”. A second later it occurred to me that I could probably do better than that, and prevent the Upload Utility window from opening in the first place if I ever try to paste an image in MarsEdit.


I was right. This wasn’t just super easy to create in Keyboard Maestro, it was super quick. I’ve spent 10× more time writing about this macro here than I did creating it. I think that’s why I so seldom write about my little hacks in Keyboard Maestro — they not only save me time and eliminate annoyances once they’re created, but they’re so easy to create that I just get back to whatever I was previously doing after making a new one.


First, I have a group (think: folders) in Keyboard Maestro for every app for which I’ve created app-specific macros. You just create a new group and set it to only be available when one (or more) specific applications are active. Inside my group for MarsEdit, I created a new macro named “Don’t Paste Images”.


It’s triggered by the hot key sequence ⌘V. That means every single time I paste in MarsEdit, this macro will run. Keyboard Maestro is so frigging fast that I’ll never notice. (Keyboard Maestro macros execute so fast that in some scenarios, you have to add steps to pause for, say, 0.2 seconds to keep the macro from getting ahead of the user interface it’s manipulating.)


The macro executes a simple [if-then-else action](https://wiki.keyboardmaestro.com/action/If_Then_Else) with the following pseudocode logic:


```
if the System Clipboard has an image
    play a sound
else
    simulate the keystroke ⌘V

```


That’s the whole thing. And it worked perfectly the first time I tried it. [Here’s a screenshot of my macro](https://daringfireball.net/misc/2025/03/km-dont-paste-images-marsedit.png).


So if *I* type ⌘V in MarsEdit, and the clipboard contains an image, I just hear a beep. (I could just default to the system beep, but I chose the standard MacOS “Bottle” sound just for this macro — I sort of want to know that it’s *this* macro keeping me from pasting whatever text I wrongly thought was on my clipboard, so I want a distinctive sound to play.) Nothing gets pasted, so MarsEdit’s Upload Utility window doesn’t appear.


If the clipboard *doesn’t* contain an image, then Keyboard Maestro simulates a ⌘V shortcut and that gets passed to MarsEdit, and from my perspective as a user, it’s just like a normal paste of the text I expected. I have a few macros that work like this, where the macro is trigged by an application’s own keyboard shortcut, and the macro will (if certain conditions are met) pass through the same simulated keyboard shortcut to the application. When I first tried this, many years ago, I was half worried that it would trigger an infinite loop, where the simulated keystroke from the Keyboard Maestro macro would re-trigger the macro. I was wrong to worry — Keyboard Maestro is too clever for that.


You almost certainly don’t have my particular problem with the occasional inadvertent pasting of images into MarsEdit. But I bet you have your own esoteric annoyances related to your own most-used apps and most-frequent tasks. Keyboard Maestro lets you effectively add your own little features to your favorite apps — often with no “scripting” at all. The best part is, while writing this very blog post, my new “Don’t Paste Images” macro saved me from seeing that cursed Upload Utility window once more, because I had the screenshot of the macro on my clipboard, when I thought I had copied the URL for it on my server.



| **Previous:** | [A Postscript on the Singular Nature of Mark Gurman’s Reporting](https://daringfireball.net/2025/03/a_postscript_on_the_singular_nature_of_mark_gurmans_reporting) |
| **Next:** | [It Might Be Time for Me to Collect Some Being Right Points for My 2023 Bluesky Prediction](https://daringfireball.net/2025/03/bluesky_being_right_points) |


PreviousNext