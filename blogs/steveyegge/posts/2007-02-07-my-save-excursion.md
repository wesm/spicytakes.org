---
title: "My save-excursion"
date: 2007-02-07
url: https://steve-yegge.blogspot.com/2007/02/my-save-excursion.html
word_count: 1597
---

A friend of mine on a neighboring team at Google presented me with an interesting math problem the other day.  It went like this:
**Friend:**
Hey Stevey!
**Me:**
Uh, you know people don't actually call me that to my face, right?  Only behind my back.
**Friend:**
*(cheerily)*
But you're Stevey!  Look at your badge!
**Me:**
Sigh.  OK, fine already.  What's this math problem?
**Friend:**
Let's say there's this hypothetical blogger who writes for 4 hours a month, and he desperately needs an editor who will never materialize, and in those 4 hours he produces very... large... ummm...
**Me:**
And what exactly are you trying to say there,
*ex-*
friend?
**Ex-friend:**
Oh, nothing!  It's purely hypothetical!  I'm just saying that I, er, well, I've been reading for hours and I'm only half done with your last blog entry, and I accidentally fell asleep and had a wonderful dream that I was finished reading it, and then I woke up and my keyboard was gone.  Plus I'm still not done yet.
**Me:**
That was a pretty long story.
**Ex-friend:**
*(reading what I wrote)*
That's not what I said!  What do you mean the keyboard was gone?
**Me:**
Uh, never mind.  I'll fix it in the real blog.
**Ex-friend:**
Fine.  Whatever.  Anyway, we were all thinking...
**Me:**
Oh!  So it's "we" now, is it?  And who are my
*other*
ex-friends in this particular
*hypothetical*
situation?
**Ex-friend:**
Jared and Todd and Jeremy.
**Me:**
B-b-but — you can't say their names in my blog!
**Ex-friend:**
Oopsie.
**Me:**
There are people listening!
**Ex-friend:**
No, Stevey, I think your readers all died of starvation on account of trying to finish your blogs in one sitting.
**Me:**
D'oh!  OK.  Yeah.  I think I get it.  You're saying — and correct me if I'm wrong here — that if I write for an hour a week, I'll produce blogs that are only like 600 times too long, rather than the usual, ah...
**Really-ex-friend-now:**
2400.
**Me:**
Ouch!  That's just... low.
*(frowning vaguely, looking at my fingers)*
I know how to multiply, you know.  I was just thinking about something else, that's all.
**Really-ex-friend-now:**
Well, we think maybe you should give it a try!  Just one hour a week.  You could be, like, a columnist.
**Me:**
Yeah!  I won't get paid, and nobody will read any of it, but otherwise it's pretty much exactly the same as a columnist in all respects.  I can be like... like Paul Graham, and sit around in my underwear writing articles about how I get to sit around in my underwear writing articles about stuff, on account of having written everything in Lisp.  Except I'll still have to wear pants.
**Friend:**
Um.
*(edging nervously towards the door)*
So does this mean I don't have to finish that last blog about Cinderella?
**Me:**
*sigh* Pinocchio.  And no, you don't have to finish it.  He dies at the end, anyway.
**Friend:**
*(sympathetic frowny-face)*
Sad.
*(runs out)*
**Stevey's Blog... Column... Thing.**
So!  I'm going to try writing for an hour a week, and also try limiting my blog to a certain number of words that columnists apparently never actually discuss but which appears to be around 800, and we'll see if it nets me fewer complaints.  And I'm going to start... last Friday!  This blog is officially 3 days late, but I figured apologizing could get me a couple of extra words.
As of that last paragraph, I was at 2338 chars, or 437 five-letter words, at least in the first draft.  I'll spend the rest of today's entry explaining how I knew that.
Since I'm writing this in Emacs (where else?) I need an Emacs command that will count the non-whitespace characters in the current buffer and tell me how many there are so far, plus divide by five to show how many "words" I've written, since as we all know from fifth-grade English class, words are always five letters.
First I type
and switch to my
buffer.  You can write lisp code there.  When it's tested, you can copy it into a file somewhere that's loaded by your .emacs.
I start with the basic interactive function skeleton:

```
(defun blog-column-length ()  "Print stats on current blog column, or blogollum, or whatever"  (interactive)  (message "hi there"))
```

That's pretty much the minimal command you can invoke with M-x.  After typing it out, I put the cursor anywhere inside the function definition and type
(i.e., Ctrl-Alt-x) to evaluate it.  Note that we don't have to restart Emacs to do this.  *Ahem*.  At least Eclipse comes with free bullets.
Now we can type
*M-x blog-column-length*
to see the "hi there" message printed to the minibuffer.  If I were doing lots of output, I could use
, but I figure this can just be a one-liner.  The
function takes arguments similar to C's
*printf*
.
Note: by evaluating my function, I've fully integrated it into Emacs.  I can tab-complete the command name, do
to read the help string, do
to find it in the list of commands that have 'blog' in the name, and so on.  Emacs is cool.  Why aren't all editors like this?
I mean, if you were trying to follow along with our little exercise in Eclipse, at this point you
*might*
have it out of the box, maybe, but there would be parts all over the floor, styrofoam everywhere, and you'd be staring at the 10-page Hello, World demo trying to figure out where
goes.  Good ole Eclipse.  And I hear the Visual Studio team was jealous of Eclipse's "lightweight" plugin system.  (Is it any wonder that developers never customize their tools?  Jeez.)
Anyway, all that's left is to count the characters.  It helps to know one wacky thing about Emacs: most functions are written as scripted versions of exactly what you would have done by hand.  That's how it got to be called "Emacs" — Editor Macros.  As you learn the editor commands, you're also learning how to program Emacs, because you can use all those commands in your elisp code.  Sweet!
There are lots of ways to count the non-whitespace characters in the buffer, but the first one that came to mind is to go to the beginning of the buffer and start looking at each character, incrementing some counter if it's not whitespace, and keep going until we get to the end of the buffer.
So that's what we'll do.  First, go to the beginning of the buffer:

```
(goto-char (point-min))
```

You could also use

```
(beginning-of-buffer)
```

if you prefer.  No biggie.
Then we need a loop.  How about "while"?  Sounds good to me.  Let's loop while we're not at the end of the buffer:

```
(while (not (eobp))      )
```

It's good to know all the little functions for testing if you're at the beginning of the line (bolp), end of line (eolp), beginning of buffer (bobp), end of buffer (eobp), etc.  'p' means predicate; i.e.  a function that returns true/false.  It's just a lispy naming convention.
Oh, let's wrap the whole thing in a
.  That's an emacs macro that saves/restores the point and mark around any editing operations.  If you want to be able to run your command without affecting the user's actual cursor position, use
You see it all over.  There's even a haiku about it:

```
The friends chat gaily,I stand up to join their talk.My save-excursion.
```

Really.  It's a real Emacs haiku.  Look it up!  The only Eclipse haiku I know goes like this:

```
startApplication()thenWaitFriggingForever()thenItGoesRealSlow()
```

That's what they used to say about Emacs, but then hardware got faster so they needed a new elephant.
Anyway, here's what we've got so far:

```
(defun blog-column-length ()  "Print stats on current blog column, or blogollum, or whatever"  (interactive)  (save-excursion    (goto-char (point-min))    (while (not (eobp))      ;; we're going to increment a counter in here     )    (message "count will be displayed here")))
```

First, we need to declare a variable.  I'm tellin' ya: declaring your variables is all the rage these days.

```
(let ((char-count 0))
```

This declares a variable
, initialized to zero, within the scope of the let-block, which is sort of like a curly-brace block in C or Java.  The extra parens date back to 1955, and they get real grumpy if you mention them, so let's not.
Next we need to say "unless we're looking at a whitespace char, increment char-count".  Here's how:

```
(unless (looking-at "[ \t\r\n]")  (incf char-count))
```

Gosh.  And everyone always says they despise Lisp.  It's not
*that*
hard, is it?  The only trick is knowing where to put the parentheses, and that's easy.  It's just
.  If
is a call to a function, then you parenthesize it, and it all nests nicely, sorta like XML but without all the yelling.
Plus those extra ones around the
declaration, but we don't talk about them, remember?  That's how you remember them.
Then we move the cursor forward:

```
(forward-char 1)
```

Putting it all together:

```
(defun blog-column-length ()  "Print stats on current blog column, or blogollum, or whatever"  (interactive)  (save-excursion    (goto-char (point-min))    (let ((char-count 0))      (while (not (eobp))        (unless (looking-at "[ \t\r\n]")          (incf char-count))        (forward-char 1))      (message "%d chars, %d words" char-count (/ char-count 5)))))
```

Et voila.  Almost exactly 1 hour.  Well, 90 minutes, but who's counting.
6936 chars, 1387 words.  OK, it's a little longer than my target, but what's a few words in the pursuit of Emacs education between friends?  Plus I got a couple of jabs in at Eclipse, so it's not a total loss.
See you all next week!