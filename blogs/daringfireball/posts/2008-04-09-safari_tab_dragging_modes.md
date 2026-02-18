---
title: "Safari’s Tab Dragging Modes"
date: 2008-04-09
url: https://daringfireball.net/2008/04/safari_tab_dragging_modes
slug: safari_tab_dragging_modes
word_count: 515
---


In my [Firefox/Safari comparison](http://daringfireball.net/2008/04/firefox_3_safari_3), I praised Safari for allowing the user to tear off a tab into a new window. However, Safari’s behavior with tab-dragging is a little weird, and I suspect confusing to many people. When you drag a Safari tab, there are two dragging modes: *intra*-window and *inter*-window. In the intra-window dragging mode, you are simply rearranging the order of tabs within a single window. In the inter-window dragging mode, you can both reorder tabs within a window *and* drag tabs between windows (and spawn new windows from a dragged tab).


The mode is determined by the initial direction in which you drag. If you first drag left or right, you enter the intra-window mode;1 if you drag up or down, you enter the inter-window mode. Once you enter one of these modes, you cannot switch to the other except by dropping the tab and starting a new drag.


The two modes look different, visually. In the intra-window (left/right) model, the dragged tab simply looks like a normal tab attached to the window:


In the inter-window (up/down) model, the dragged tab’s appearance depends upon where it is currently hovering. When it’s hovering within the tab bar, toolbar, or bookmark bar of a window, it looks like a translucent tab:


In this case, when dropped, the tab moves from one spot to another, perhaps between two different windows.


When the tab is hovering anywhere else, it takes on the appearance of a thumbnail of the tab’s content:


In this case, when dropped, the tab spawns a new window.


This state of affairs is irritating at best, and confusing at worst. Confusing because I can’t think of any other drag operation on the Mac where you get a completely different mode based on the initial direction of the drag. [**Update:** Via Twitter, [Peter Hosey points to one](http://twitter.com/boredzo/statuses/786014744): dragging in a table view, where up/down selects multiple rows and left/right initiates a drag-and-drop with the clicked-upon row. Safari’s tabs are still the only drag-*and-drop* implementation I know of with different directional modes.] Irritating, because even if you understand how it works (which is a big *if*), it’s still easy to get locked in the wrong mode — if you want to drag down but move the mouse even one iota left or right first, you get locked in the intra-window mode and have to start over.


I don’t see why the intra-window (left-right) mode even exists. With the inter-window mode, you can do everything: reorder a tab within a window, move a tab to another existing window, or move a tab to its own new window. The intra-window mode only allows one thing: reordering tabs within their current window. I can’t think of a single reason why this mode exists.


---

1. There’s at least one exception: If you drag the leftmost tab to the left, you get the inter-window mode. Not so for dragging the rightmost tab to the right, however. ↩︎



| **Previous:** | [Firefox 3 vs. Safari 3 Addenda](https://daringfireball.net/2008/04/firefox_safari_addenda) |
| **Next:** | [Mac OS X’s ‘Search in Google’ Safari Tie-In](https://daringfireball.net/2008/04/google_safari_tiein) |


PreviousNext