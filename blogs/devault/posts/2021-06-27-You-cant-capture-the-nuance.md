---
title: "You can't capture the nuance of my form fields"
date: 2021-06-27
url: https://drewdevault.com/2021/06/27/You-cant-capture-the-nuance.html
slug: You-cant-capture-the-nuance
word_count: 609
---

Check out this text box:

Here are some of the nuances of using this text box on my operating system
(Linux) and web browser (Firefox):

* Double clicking selects a word, and triple-clicking selects the whole line. If
I double- or triple-click-and-hold, I can drag the mouse to expand the
selection word-wise or line-wise, not just character-wise. This works with the
paragraphs of text in the body of this blog post, too.
* Holding control and pressing right will move move word-wise through the file.
It always moves to the start or end of the next or prior word, so pressing
“control+left, control+left, control+right” will end up in a different
position than “control+left” alone. Adding “shift” to any of these will mutate
the text selection.
* Clicking any of the whitespace after the end of the text will put the cursor
after the last character, even if you click to the left of the last character.
This makes it easy to start appending text to the end.
* Clicking and dragging from any point, I can drag the mouse straight upward,
exceeding the bounds of the text box or even the entire web browser, to select
all text from that point to the start of the text box. (Thanks minus for
mentioning this one)
* Selecting text and middle clicking anywhere will paste the text at the clicked
location. This uses a separate, distinct clipboard from the one accessed with
ctrl+c/ctrl+v. I can also use shift+insert to paste text from this secondary
clipboard (this is called the “primary selection”).

I rely on all of these nuances when I use form controls in my everyday life.
This is just for English, by the way. I often type in Japanese, which has an
entirely alien set of nuances. Here’s what that looks like on Android (mobile is
another beast entirely, too!):

Here’s another control:

There’s an invisible edit buffer, so I can type “Pennsylvania” (or just P) to
select what I want. I can type “New” and then press down to select “New Jersey”.
If I make a mistake and I’ve kept track of what I’ve typed in my head, I can use
backspace to make a correction, and it just works. I have lived in both of these
places, and worked both of these keystrokes into my muscle memory. Filling out a
form with my address on it and using an input box like this to select my state
of residence takes me less than a second.

You cannot capture all of this nuance in a home-grown form control, or even
anything close to it, but many JavaScript programmers do it anyway. Whenever I
encounter a custom form control, the time required to complete the form
increases from under a second to as much as a minute.

For myself, this is just very annoying. Imagine the same situation if you were
blind. The standard form inputs work everywhere, and are designed with
accessibility in mind, so you’re used to them and can easily fill in forms which
use the standard browser controls. But, when you hit a JavaScript-powered
organic cage-free non-GMO text box, you’re screwed.

There are hundreds of little nuances that users learn to use their computers
efficiently. The exact features a user relies on will vary between operating
systems, browsers, hardware, natural languages, physical ability, and personal
preferences and experience. There are dozens of tiny workflows that people
depend on every day that have never even occurred to you.

Making a custom form control with JavaScript is going to make life worse for a
lot of people. Just don’t do it. The browser’s built-in controls are quite
sufficient.
