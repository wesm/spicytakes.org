---
title: "Boring Stevey Status Update"
date: 2007-12-06
url: https://steve-yegge.blogspot.com/2007/12/boring-stevey-status-update.html
word_count: 1398
---

I had an exciting morning of not getting fired today.  Get this:  I'm on a trip to Google's Mountain View headquarters, and was glancing at Reddit between meetings, and lo and behold, I was inexplicably in the
[Reddit Tabloids](http://programming.reddit.com/info/62art/comments/)
again,
*this*
time for being fired, or so people were speculating (far too hopefully, I might add.  Geez.)  Needless to say, I immediately put all my other work-related plans on "pause" while I tried to figure out whether I was, in fact, being fired.  Can't accuse me of not having my priorities straight!
It turns out it was a minor mixup by an automated system, a system that decided to jump-start its own evolution by going directly from brownian motion to VP-level decision-making (2 evolutionary hops total.  Hee.).  This automated system had apparently just watched the movie
[Brazil](http://en.wikipedia.org/wiki/Brazil_%28film%29)
, and thought it would be fun to send me off to Information Retrieval.  So my account was disabled, from which lonely data point the Reddit crowd concluded that I must be getting fired
*right now*
, in real time, like OJ in his white SUV.  And seeing as I was too surprised to think of a counter-hypothesis, I spent about 20 minutes in an undignified, trouser-soiling panic.  Thanks, Reddit!
Anyhoo, after some friends inside Google had undone the mistake for me, I pondered the overall thrust of the Reddit comment thread ("You suck".  "No, YOU suck."  "Your mom sucks."
) and decided I really ought to write
*something*
.  Otherwise I'm likely to fall off the wagon and disappear for a year.  Time is just whooshing away.  I wish I could get back to High School Time, where even a single hour-long class can seem like eternity, and 4 years is effectively infinite.  Sigh.
I do have a bunch of half-finished blog posts lying around, but nothing has really gelled yet.  So I guess I'll ramble about stuff I've been up to.  You know.  A status update.  Blech.
Incidentally, I've decided to try to limit myself to roughly 1000-word posts, which is about the length of a newspaper column, near as I can tell.  I'll prolly just call it 5000 non-whitespace characters, and write an Emacs function to tell me when I've gone over.  Off the top of my head, maybe something like:

```
(defun blog-check ()  (interactive)  (save-excursion    (goto-char (point-min))    (let ((count 0))      (while (not (eobp))        (unless (looking-at "\\s-")          (incf count))        (forward-char))      (message "%s:  %d chars, %d words"                (if (<= count 5000)                   "OK so far"                 "Dude, too long")               count               (/ count 5)))))
```

which, when I run
, faithfully reports:

```
"You suck."  "No, YOU suck."  "Your mom sucks."
```

Oops, sorry.  Wrong macro.  My new function actually tells me:

```
OK so far:  2177 chars, 435 words.
```

Halfway there, baby!
So...  In 500-ish remaining words, here are the first things that come to mind as I sit in this comfy modern-looking couch in Building 43 of Google's Mountain View headquarters.
**JavaScript**
I've been doing a lot of JavaScript-related stuff lately.  I don't know if JavaScript 2 (aka
[ECMAScript Edition 4)](http://www.ecmascript.org/)
is going to be
*the*
[Next Big Language](http://steve-yegge.blogspot.com/2007/02/next-big-language.html)
, but it's certainly going to be
*a*
Next Big Language.  (There's room for more than one, obviously.)  And in the meantime, well, JavaScript 1.7 is working plenty well for me.
Let's see... I'm working on a book on Mozilla Rhino with Norris Boyd (the primary author of Rhino, now a Googler in Boston).  It's coming along in bursts, and is probably about 10% complete after 3 months of dorking around with it on weekends between football games (that goes for both me and Norris, as it turns out, although
*his*
team is 12-0, dammit).  But it should be a pretty cool book, assuming football season ever ends.  The book is pretty much where all my Joke Output has been focused lately, which hopefully helps explain my recent blog drought.
I've been watching the EcmaScript Edition 4
[fireworks](http://weblogs.mozillazine.org/roadmap/archives/2007/10/)
with keen interest.  While I wouldn't want to name any specific parties, for fear of offending someone, it seems to me that one party, whom I'll refer to as "Uncle Mike", is up to his perverted old tricks again.  If, like many others, you feel that "Uncle Mike" is being a "complete dickwad" (to put it as euphemistically as I can) then you can help by getting all your friends and sales people and random family members to switch to Firefox.  Really.  It'll help.
You might also write a polite letter to your favorite
[Ecma General Assembly Voting Member Company](http://www.ecma-international.org/memento/ordinary.htm)
, telling them how much you and your ten thousand closest friends are really looking forward to the imminent ratification of EcmaScript Edition 4.  Or hell, spam all of them.  That's what Uncle Mike does.
**NBE**
Continuing in the spirit of freeing all my cats from bag-imprisonment, I should also mention I've been working on an Ecma-262 compliant JavaScript interpreter in Emacs-Lisp.  I used to have actual details here, but it ate up 1000+ words, so I'll just summarize for ya.
The short synopsis is that I'm building a complete JavaScript environment in Emacs-Lisp, with two goals: (1) create a world-class JavaScript IDE for Emacs, and (2) permit writing Emacs extensions in JavaScript, since (2a) people aren't exactly flocking to elisp, and (2b) JavaScript turns out to be a better language, now that I know them both in excruciating detail.  Emacs is a great environment that needs a better extension language, and JavaScript seems well suited to navigate the popularity-vs.-elegance tightrope I'm faced with.
That's the elevator pitch:  puts people to sleep in 20 seconds,
*guaranteed.*
The status-in-brief is that I now have a fully functional, Ecma-262 compliant JavaScript interpreter and runtime in elisp, which began as a port of
[Narcissus](http://en.wikipedia.org/wiki/Narcissus_(JavaScript_engine))
.  I'm currently reworking the parser and parse tree to be faster and more IDE-friendly.  Next I'll need to turn the interpreter into a byte-compiler that emits Emacs-Lisp bytecode, which should enable it to run as fast as (or faster than) Emacs-Lisp.  Then I'll need to actually write the IDE and the emacs host objects.
The whole thing looks to be at least a year out, at least on my current budget of 3 hours a week, so don't hold your breath.  I'm giving priority to the IDE functionality, since I kinda need it for other projects, so that could potentially happen by summer.
If you happen to think of a clever name for this project, please let me know.
**Other Stuff**
Well, this 1000-word limit is... a toughie.  I've already blown through it, although hopefully I get some slack for counting HTML tags.  But I have to wrap up, so I'll close with some Unsubstantiated Random Thoughts that maybe I can clarify in upcoming crudely-truncated entries:
Google continues to be an astoundingly awesome place to work.  Like my friend Dominic says, "it feels like I've won the lottery every day."
Our Rhino on Rails framework is still working great for us, and has finally begun to gain serious internal momentum at Google.  Hopefully next year we can open-source it.
Interviewing for tech jobs at Google continues to be really hard (for both interviewer and interviewee), and I've accumulated enough truly useful interviewee-prep tips to merit a full blog post.  Look for that one soon.
I still use Emacs to an extent that could justifiably be described as "unhealthy".  I'd love to do another Effective Emacs post someday.
I still watch a lot of Anime.  Currently watching
[Le Chevalier D'Eon](http://en.wikipedia.org/wiki/Le_Chevalier_D%27Eon)
, which is pretty awesome so far.
I taught my dog Cino to play guitar, a feat which so astounds people that they all say I should put it on YouTube, so there's Yet Another Side Project for me.
I'd love to write more about all this.  The 1000-word limit seems to have made it feasible for me to create posts in a single sitting, with no bathroom breaks, provided I can actually go to 1500 "words".  So hopefully in addition to all my side projects, I can blog more often.
And with that, I'm going to get back to my "day job" project(s), which are sadly confidential.  But they're so cool that if I
*did*
tell you about them, you'd be so overwhelmed that you'd have to go sit in one of our $5000-ish massage chairs, like the dude sitting next to me right now.
Man this place rocks.