---
title: "Firefox is on a slippery slope"
date: 2017-12-16
url: https://drewdevault.com/2017/12/16/Firefox-is-on-a-slippery-slope.html
slug: Firefox-is-on-a-slippery-slope
word_count: 632
---

For a long time, it was just setting the default search provider to Google in
exchange for a beefy stipend. Later, paid links in your new tab page were added.
Then, a proprietary service, Pocket, was bundled into the browser - not as an
addon, but a hardcoded feature. In the past few days, we’ve discovered an
advertisement in the form of browser extension was sideloaded into user
browsers. Whoever is leading these decisions at Mozilla needs to be stopped.

Here’s a breakdown of what happened a few days ago. Mozilla and NBC
Universal did a “collaboration” (read: promotion) for the TV show Mr. Robot.
It involved sideloading a sketchy browser extension which will  **invert**  text that
matches a list of Mr. Robot-related keywords like “fsociety”, “robot”, “undo”,
and “fuck”, and does a number of other things like adding an HTTP header to
certain sites you visit.

This extension was sideloaded into browsers via the “experiments” feature.
Not only are these experiments enabled by default, but updates  [have been
known](https://redd.it/7i4puf)  to re-enable it if you turn it off. The
advertisement addon shows up  [like
this](http://www.bolcer.org/looking-glass2.png)  on your addon page, and was
added to Firefox stable. If I saw this before I knew what was going on, I would
think my browser was compromised!  Apparently it was a mistake that this showed
up on the addon page, though - it was supposed to be  *silently*  sideloaded into
your browser!

There’s  [a ticket](https://bugzilla.mozilla.org/show_bug.cgi?id=1423003)  on
Bugzilla (Firefox’s bug tracker) for discussing this experiment, but it’s locked
down and no one outside of Mozilla can see it. There’s  [another
ticket](https://bugzilla.mozilla.org/show_bug.cgi?id=1424977) , filed by
concerned users, which has since been disabled and had many comments removed,
particularly the angry (but respectful) ones.

Mozilla, this is  **not okay** . This is wrong on so many levels. Frankly, whoever
was in charge should be fired over this - which is not something I call for
lightly.

First of all, web browsers are a  *tool* . I don’t want my browser to fool around,
I just want it to display websites faithfully. This is the prime directive of
web browsers, and you broke that. When I compile vim with gcc, I don’t want
gcc to make vim sporadically add “fsociety” into every document I write. I want
it to compile vim and go away.

More importantly, these advertising anti-features gravely - perhaps terminally -
violate user trust. This event tells us that “Firefox studies” into a backdoor
for advertisements, and I will  *never*  trust it again. But it doesn’t matter -
you’re going to re-enable it on the next update. You know what that means? I
will never trust  *Firefox*  again. I switched to
 [qutebrowser](http://qutebrowser.org/)  as my daily driver because this crap was
starting to add up, but I still used Firefox from time to time and never
resigned from it entirely or stopped recommending it to friends. Well, whatever
goodwill was left is gone now, and I will only recommend other browsers
henceforth.

Mozilla, you fucked up  *bad* , and you still haven’t apologised. The study is
still active and ongoing. There is no amount of money that you should have
accepted for this. This is the last straw - and I took a lot of straws from you.
Goodbye forever, Mozilla.

**Update 2017-12-16 @ 22:33**

It has been clarified that an about:config flag must be set for this addon’s
behavior to be visible. This improves the situation considerably, but I do not
think it exenorates Mozilla and I stand firm behind most of my points. The study
has also been rolled back by Mozilla, and Mozilla has issued
 [statements](https://gizmodo.com/mozilla-slipped-a-mr-robot-promo-plugin-into-firefox-1821332254) 
to the
 [media](https://gizmodo.com/after-blowback-firefox-will-move-mr-robot-extension-t-1821354314) 
justifying the study (no apology has been issued).

**Update 2017-12-18**

Mozilla has issued an apology:

[https://blog.mozilla.org/firefox/update-looking-glass-add/](https://blog.mozilla.org/firefox/update-looking-glass-add/)

**Responses** :

[Mozilla, Firefox, Looking Glass, and you](https://blog.jeaye.com/2017/12/16/firefox/) 
via jeaye.com
