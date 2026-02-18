---
title: "Leopard Details: Anchored Row Selection in NSTableView"
date: 2008-02-20
url: https://daringfireball.net/2008/02/anchored_selection
slug: anchored_selection
word_count: 577
---


In August 2006, I wrote “[Highly Selective](http://daringfireball.net/2006/08/highly_selective)”, a detailed critique of the way keyboard-based multiple item selection works in most Mac OS X software. In short, there are two models for multiple item selection, *anchored* and *unanchored*:


**ANCHORED:** The selection grows in one direction, and shrinks in the other. In the anchored selection model, if you select two or more items in a list using Shift-Down, then pressing Shift-Up will deselect items from the bottom of the selection range. (And vice versa: if you start by selecting items with Shift-Up, Shift-Down will deselect from the top of the selection.)


**UNANCHORED:** The selection grows in both directions and never shrinks. In the unanchored selection model Shift-Down always extends the selection range downward and Shift-Up always extends it upward.


My argument was that anchored is better, because it allows you to correct for mistakes without switching to the mouse. E.g. if you press Shift-Down four times but realize you’ve selected one too many items, in the anchored model you can simply press Shift-Up to deselect the last item; in the unanchored model, pressing Shift-Up *adds* another item at the top of the selection range. The problem was that most Mac apps used the unanchored model, because it was the default for Cocoa’s NSTableView and Carbon’s Data Browser.


Key word there being “was”.


In Leopard, Cocoa’s NSTableView changed to the anchored model. You can see this in just about any Cocoa app that has a list that supports multiple selection: Mail’s message list, iChat’s Buddy window, Safari’s bookmarks, and Address Book are just a few examples. Regarding third-party apps, I wrote:


> There’s certainly a consistency argument to be in favor of using the
> Apple-supplied default selection behavior, regardless whether you
> personally agree with it. The idea being that by using the default
> behavior, list selection will work the same in your software as it
> does almost everywhere else. And if Apple does change the behavior
> in some future version of Mac OS X, your software will pick up the
> new default behavior “for free”.


That’s exactly what happened — all apps that use Cocoa’s NSTableView, not just Apple’s, picked up the new anchored selection model for free on Leopard.


So if you’ve noticed this change in, say, Mail, it’s not Mail that changed, but rather the underlying NSTableView list control used in many Cocoa apps. Which is why the behavior did *not* change in apps that use the Carbon Data Browser control (the equivalent in Carbon to NSTableView in Cocoa). The Finder and iTunes are Apple’s two most prominent Carbon apps, and both still use the unanchored selection model. You can also see this in third-party Carbon apps like Interarchy.


Ideally, it would be better — both in terms of consistency and usability — if Apple had changed this behavior in the Carbon Data Browser, too. The overwhelming majority of Mac users have no idea what Cocoa and Carbon are, so the different behavior in the Finder and iTunes is, to them, seemingly arbitrary. But if there’s one single thing I hoped to see Apple do regarding this issue in Leopard, it’s exactly what they did: change it in NSTableView.


I have no idea who pushed for this change at Apple, nor whether my essay was influential in the decision. But whoever you are, I thank you.



| **Previous:** | [The Appeal of the MacBook Air](https://daringfireball.net/2008/02/macbook_air_appeal) |
| **Next:** | [Flim-Flash](https://daringfireball.net/2008/02/flim-flash) |


PreviousNext