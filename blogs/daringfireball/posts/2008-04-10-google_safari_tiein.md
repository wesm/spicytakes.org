---
title: "Mac OS X’s ‘Search in Google’ Safari Tie-In"
date: 2008-04-10
url: https://daringfireball.net/2008/04/google_safari_tiein
slug: google_safari_tiein
word_count: 343
---


For the most part, if you want to use a browser other than Safari as your default, Mac OS X makes it easy. Safari’s preference window lets you pick any browser as your default, and most other Mac browsers let you make this choice in their prefs windows, too — so you don’t have to use Safari to specify, say, Camino or OmniWeb as your default.1


Once you make this choice, everything pretty much works as you’d expect. Click a link in any other app and it’ll open the browser you’ve selected as your default. A notable and annoying exception, though, is the Cocoa text system’s “Search in Google” contextual menu item. This is a contextual menu command that appears system-wide. If you Control-click on a word or a range of selected text and choose “Search in Google”, the search is performed in Safari, regardless whether it’s your preferred browser (or even whether it’s already running).


Cocoa’s contextual menu “Search in Google” command, as currently implemented, does hook specifically into Safari’s Google Search feature: the terms you search for appear in the Google Search field in Safari’s toolbar. A simpler way to implement the feature would be to construct a Google search URL containing the terms and open that URL in the default browser. This would make the feature work equally well in all browsers — but would deprive Apple of a few pennies in [Google affiliate lucre](http://daringfireball.net/2007/06/wwdc_2007_keynote) for each such search.


I use this command somewhat frequently, and whenever I switch to something other than Safari as my default browser, it’s the only tie-in to Safari that really irks me.2


---

1. Not Firefox, though. ↩︎
2. There are other Safari-specific tie-ins, like the way iTunes syncs Safari bookmarks, and only Safari bookmarks, with an iPhone. But that one strikes me as reasonable; I don’t expect Apple to parse other browsers’ file formats (although they do parse IE’s on Windows). ↩︎



| **Previous:** | [Safari’s Tab Dragging Modes](https://daringfireball.net/2008/04/safari_tab_dragging_modes) |
| **Next:** | [How Much Money Does Apple Get From Google?](https://daringfireball.net/2008/04/apple_google_money) |


PreviousNext