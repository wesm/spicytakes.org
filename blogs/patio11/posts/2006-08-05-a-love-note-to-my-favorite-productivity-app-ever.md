---
title: "A Love Note To My Favorite Productivity App.  Ever."
date: 2006-08-05
url: https://www.kalzumeus.com/2006/08/05/a-love-note-to-my-favorite-productivity-app-ever/
slug: a-love-note-to-my-favorite-productivity-app-ever
word_count: 1034
---


I just downloaded the Direct Access program from Nagarasoft today. It lets you [type words to act as shortcuts](http://www.nagarsoft.com/) to essentially anything you want on your computer. In default mode, its “type your keyword, then hit F1″ and you get your action. I call that the BANG key because in the Linux world typing a BANG (exclamation point) after the first few letters of a command gets you completion for it if you’ve done it recently. For example, out of the box fireBANG gets you a browser opened… from any place you can type text on your system.


15 minutes of setting up keys which are more useful to me and I had a configuration which I was happy with. I also remapped the BANG key to Alt-Enter, which I can quickly hit without having to move a hand and which I’m used to from Java IDEs. **My productivity has not increased so much since I learned to Alt-Tab**.


Let me paint a picture for you: here’s what my screen generally looks like when I’m in development mode.


Looking at this ugly monstrosity, I suddenly realize “Uh oh, I really need to copy/paste a file from C:\cygwin\home\nameofdayjob\nameofdayjobcurrentproject\server\perl to C:\cygwin\home\nameofdayjob\nameofdayjobcurrentproject\client . And then I need to zip it. Aww “#$”. Zipping isn’t bad, thats as simple as right-clicking the file and using Winzip’s shell integration.


But opening monsterfolder is tricky. If I had the desktop available it would be as simple as picking the right shortcut out of the fourty that are there. But I don’t — I’ve got 15 other applications vying for my attention. And, likely as not, one of them is modal at the moment. Which means even if I try Windows-M (“Automagically minimize all programs and dump you on your desktop” — and if you don’t use this, START) I’ll get trapped at some file chooser dialog somewhere. So instead I have to navigate to it by picking one of those open explorer windows and typing the whole evil path in the address bar, in the process losing the contents of the explorer window.


**But no longer**!


Now its svrBANG and I get taken straight to that directory.


Now imagine I’m staring at that ugly, cluttered screen and one of the office secretaries comes up to me. “Sorry, Patrick, this needs your signature urgently.” “This” is invariably a memo which has Japanese I can’t read on it. The most recent culprit was “international exchange activities aimed at promoting economic improvement”, which *naturally* the Japanese have a two-letter word for. I have a dictionary site which I am totally dependent on for situations like that bookmarked in Firefox (it would practically be my homepage if my company didn’t lock me to www.nameofdayjob.com to increase our access count — I offered to write them a robot to hit the page 100 times a day to allow me to set mine to Google or something but noooooo they said that would be cheating). So I’ve got to click one of the firefox windows from the task bar (2 clicks), open up a new tab, and load the bookmark.


**No longer**! dicBANG and my functional illiteracy is successfully hidden for another 5 minutes!


Do you have a Start Menu which is overflowing with programs which you use once in a blue moon but can’t get rid of because you would then have to fish them out of Program Files or God knows where else? Just assign them shortcuts. PadGenerator is an excellent candidate for this — I only need it once for every Bingo Card Creator update — padBANG, done, one program group saved. I’m addicted to the old Windows-R, calc/notepad/cmd/mspaint trick. Now I don’t have to Windows-R anymore, and can extend that to programs which aren’t in the system path. paintBANG now brings up Paint.NET (oh, love that program). ftpBANG brings up Filezilla.


Do you have 432 web services you have to check on a regular basis? I’m sort of obsessive-compulsive about having access to data, and yet I underuse bookmarks hideously (never liked them because they were never portable between computers). Which means to get to Google Sitemaps, for example, I generally go to Google (via typing it out in my address bar, no less — a habit which I will never break) and then Get Lucky with “Google Sitemaps”. Now its sitemapsBANG, from anywhere. adwordsBANG. wsjBANG. instaBANG ([instapundit](http://www.instapundit.com), my “got 5 minutes to kill” blog of choice). josBANG. blogBANG (I’ll give you [one guess](http://microisvjournal.wordpress.com)). ffBANG (I shortened “fireBANG” to “ffBANG” for my favorite web browser, since I use this one so often).


Then I got started thinking of ways I could abuse this with my IDEs. I don’t know about you but on a scale of 1-10 I probably use all my IDEs at about a 3, because I never put in enough time to learn the guts of them. As a result, what should be simple like “Use autocomplete to throw out a try/catch block” is just beyond my capabilities for most of them. And I often end up editing programs in non-IDEs just for convinience (my favorite being nano, a pico clone — laugh all you want). Now I’ve got nice portable macros like #intconvBANG. Java mavens might recognize this one:


> try {
> bar = Integer.parseInt(foo);
> } catch(NumberFormatException e) { };


Then I just replace bar and foo as appropriate and I’m done.


Here’s another which might be a little quirky: kBANG. k is, in my personal coding convention, always my variable-of-first-choice for iterating through anything other than an array. If I’m doing GAWK, its always (for k in hash). If I’m doing Java, k is my temporary variable that holds the iterator’s next(). Thus, kBANG is:


> java.util.Iterator iterator = foo.iterator();
> Object k;
> while (iterator.hasNext()) {
> k = iterator.next();
> }


The program is $40 (save 15% with a discount available to most people who know what the acronym JoS/BoS stands for — search for the words “the 13th August”). The first time I saw that, before actually using it, I thought “God, thats a lot of money for a single-use toy”. Now I think it would be cheap at twice the price.
