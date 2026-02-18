---
title: "Firefox 3 vs. Safari 3"
date: 2008-04-05
url: https://daringfireball.net/2008/04/firefox_3_safari_3
slug: firefox_3_safari_3
word_count: 1958
---


After a few weeks in the arms of Firefox 3 betas, I’ve returned to Safari as my daily browser. Unsurprisingly, it’s the interface that drove me back.


But I’m not talking about cosmetic issues — or at least not *only* about cosmetic issues. The new default theme for Firefox theme looks pretty good, especially when you switch the toolbar icons [to the small size](http://iamthewalr.us/blog/2008/03/27/smaller-is-better/). The Safari-style [“GrApple” Firefox themes](http://www.takebacktheweb.org/) I [linked to](http://daringfireball.net/linked/2008/march#mon-24-grapple) last month makes Firefox 3 look even better, albeit mostly by mimicking Safari.


But cosmetic appeal is just the surface. Steve Jobs, in [a 2003 New York Times magazine interview](http://www.nytimes.com/2003/11/30/magazine/30IPOD.html?ex=1386133200&en=750c9021e58923d5&ei=5007&partner=USERLAND), said:


> “Most people make the mistake of thinking design is what it looks
> like. People think it’s this veneer — that the designers are
> handed this box and told, ‘Make it look good!’ That’s not what we
> think design is. It’s not just what it looks like and feels like.
> Design is how it works.”


And that’s just it. Firefox 3’s shortcomings as a Mac app are behavioral, too. The main issues that drove me back to Safari:

- **Background Window Appearance** — Starting with Leopard,
standard application windows follow a simple, consistent
rule: the frontmost window of the current application gets a
medium gray color while all other windows have a lighter,
flatter look. The idea is that with several windows visible
at once, giving the active one a darker look makes it easier
to pick out visually. (One of the long-standing gripes
regarding the late brushed metal theme — *Christ, remember
that ugly thing?* — was that its windows barely changed
appearance when switching from active to inactive.)
Firefox 3 doesn’t do this. Its windows all have the darker
“active” look even when in the background. And I believe that its
theming mechanism does not allow for it.
- **Text Editing Shortcuts** — Firefox 3 still doesn’t support
certain standard Mac text editing key bindings. For example,
in a one-line text field, the Up and Down Arrow keys should
move the insertion point to the beginning and end of the
line, respectively. Drives me nuts.
- **Dictionary** — Firefox doesn’t support the system-wide
dictionary. In Safari (and most other apps), you can hover
the mouse over any word and use Command-Control-D (by
default) to display the definition of that word right there
in the current window.
- **Services** — Firefox doesn’t support the Services menu.
Safari does, and I use this all the time for invoking text
filters I’ve made using [ThisService](http://wafflesoftware.net/thisservice/), and for sending the
current text selection to LaunchBar as input.
- **Tabs** — Firefox 3 does let you drag to reorder tabs
within a window, and drag tabs between windows, but it
doesn’t let you drag a tab out of a window to create a new
window with just that tab. Safari 3 does. Picky-picky, I
know, but I use this feature in Safari every day to group
related tabs together in their own window.
- **Location Field** — The new Firefox 3 location field, the
so-called “[AwesomeBar](http://diveintomark.org/archives/2008/03/25/awesomebar)”, is too clever. When I click the
mouse in the middle of a URL, I just want to place the
insertion point. I don’t want to select the entire URL. If I
wanted to select the entire URL, I’d double-click. Click to
place, double-click to select — *just like any other text
field*.
Auto-completion in Firefox requires the use of the Down Arrow key to select something from the list of suggestions. In Safari you can just use Return to accept the first suggestion. It might just be habit, but it feels to me like Safari’s auto-completion works a little better. Also, in Firefox, during auto-completion, the Tab key acts like Down Arrow — it selects the next suggestion in the auto-completion list. In Safari Tab moves the focus to the Search field, as it should.
In Firefox’s favor, its new location field does some very cool things 
that Safari’s doesn’t. For example, when matching what you’ve typed against the URLs in your bookmarks and history, it looks anywhere within the URLs, not just at the beginning as Safari does. This means you can type “foo” to match the URL “example.com/foo/”. You can’t do that in Safari.
- **History** — I like Safari’s hierarchical History menu.
What Safari does is list the 20 most recently loaded URLs,
followed by sub-menus for each of the last seven days.
Firefox only lists the 10 most recent URLs in the History
menu. You can get more done right from the menu in Safari,
whereas in Firefox you’ve got to open the History window.
- **Page Load Progress Indicator** — Every time I dally with
another browser, I immediately miss Safari’s
in-location-field progress meter. Back in January 2003 when Apple released the first public beta of Safari 1.0, I described this feature as follows:1

Hideous. It looks like partially-selected text. Please scrap it.

Over time, the feature has not just grown on me, but I’ve come to appreciate the cleverness of its design. I was wrong, and whoever designed this for Safari was right. The truth is that page loading is the slowest and most unpleasant aspect of using a web browser. It’s important to know whether a page has finished loading yet, and so a browser’s progress indicator deserves a prominent spot. The best spot is near the location field, because that tends to be where your eyes are when a page starts loading. You can’t get any closer to the location field than being inside the location field itself. But, once a page *has* loaded, there’s no reason for a progress indicator to remain on screen.
Firefox 3 has a small spinning progress indicator in the toolbar. It’s too subtle, and as a simple spinner, offers no indication as to how far along the page load has progressed, only that it is still loading. Firefox does offer a proper progress bar in the status bar footer, but (a) it’s far from rather than close to the location field in the toolbar; and (b) the status bar is optional — if you turn it off, the only progress indicator is the spinner.
This one’s a total win for Safari.
- **New Tab Shortcut** — In Safari, Command-T always creates
a new tab, even if a browser window isn’t frontmost; it does
the Right Thing and creates a new tab in the frontmost
browser window and brings that window forward. In Firefox,
invoking Command-T just beeps if, say, the Downloads window is
frontmost, or if there is no open browser window.
- **Inline PDF Viewing** — An obvious win for Safari.
- **AppleScript Support** — Firefox 3 has almost none.
Safari’s is pretty good.


---


Firefox 3 does have a lot going for it. Yes, it’s still in beta (b5 at this writing), but even in beta it is far better, at least Mac-wise, than Firefox 2. It also unquestionably offers certain advantages over Safari. For one thing, it does a far better job managing memory. The main reason I switched from Safari to Firefox in the first place was memory consumption on my PowerBook G4 — after just a few hours of my use, Safari 3 inevitably consumes at least 300 MB, often more, of private memory. In the same usage, Firefox 3 never seemed to use more than 90 MB, even after a few days.


On a machine like my PowerBook with “just” 2 GB of RAM, Safari’s memory consumption can be a system-wide performance bottleneck. There are few more effective ways to slow down Mac OS X than to force the system to start swapping. But last week I switched to a new MacBook Pro with 4 GB of RAM, so while Safari still uses significantly more memory than Firefox, it doesn’t lead to VM swapping on my MacBook Pro like it did on my PowerBook.


I love Firefox’s auto-restoration of tabs and windows. Quit Firefox, relaunch it, and your previously-open tabs and windows are restored. Safari 3 has this feature, but makes you do it manually via the “Reopen All Windows From Last Session” command in the History menu. I’m sure most Safari users have no idea this feature even exists. At least as a preference, Safari should offer the ability to do this automatically.


Another very cool history-related Firefox 3 feature: the History → Recently Closed Tabs sub-menu. If you accidentally close a tab in Safari, and that tab has been open for so long that you don’t know where it is in your history, it’s a pain to fish it out. With this Firefox feature, you get two histories: (1) the main, traditional one, which stores pages by when they were *opened*, and (2) a second one, which stores pages based on when they were *closed*. Both are useful. Firefox also has a shortcut (Shift-Command-T) for restoring the most recently closed tab — perfect for the common scenario of recovering from an accidental tab closure.


Firefox 3 adds a new inline toolbar for password saving, similar to the inline text search bar that both Safari and Firefox now have. This password bar is very slick — it’s small and non-modal, staying out of the way until after you’ve finished logging into a site, at which point you can decide whether you want to allow Firefox to save your credentials for this site. Safari, on the other hand, still uses a modal alert for this, demanding your attention.


Perhaps the biggest difference between Safari and Firefox is that Firefox offers an official, supported extension API. Safari supports “Internet plugins” for things like QuickTime and Flash, but offers no extension API for modifying or adding features to the application itself. Thus, anyone who seeks to modify Safari must resort to unsupported input manager hacks for things like ad-blocking, [fancier search](http://www.inquisitorx.com/), etc. With Firefox, plugins such as these are fully supported. It does seem to be the case that many Firefox 2 plugins don’t yet work with Firefox 3, but it’s a tremendous advantage for Firefox that this extension mechanisms exists. This is so big a part of Firefox that it’s arguably downright criminal that I’ve buried mention of it at the bottom of this review. But the one I want most, [FlashBlock](http://flashblock.mozdev.org/), doesn’t yet work with the latest Firefox 3 betas.2


Most of my reasons for preferring Safari to Firefox are Mac-specific details. [Camino](http://caminobrowser.org/) gets some of them right, but not all, and it’s missing the best thing about Firefox — the extensions. For users new to the Mac, who aren’t aware of these details, Firefox 3 might be as good as or better than Safari in nearly every way. (For anyone more used to Windows than the Mac, the text editing behavior in Firefox might feel *right* rather than wrong, as it does to me.)


In short, competition in the Mac web browser space is strong and getting stronger. Firefox isn’t just a great web browser, but it’s a pretty good *Mac* web browser, too.


---

1. Nearly all my other complaints regarding that [initial public release of Safari](http://daringfireball.net/2003/01/safari) have since been rectified. Famously, Safari 1.0b1 didn’t support tabbed browser windows; Safari’s current tab support is my favorite of any browser. AppleScript support was non-existent; now it’s pretty good. Brushed metal windows are gone. And Safari’s location field auto-completion is much improved. ↩︎
2. Also excellent, perhaps even downright amazing, is the [Web Developer extension](http://chrispederick.com/work/web-developer/). But it’s not something that’s generally applicable for daily browsing. I suspect there are many web developers who use Safari for regular browsing but Firefox for development, because of the Web Developer extension. ↩︎



| **Previous:** | [The $64,000 Question](https://daringfireball.net/2008/04/64000_question) |
| **Next:** | [Firefox 3 vs. Safari 3 Addenda](https://daringfireball.net/2008/04/firefox_safari_addenda) |


PreviousNext