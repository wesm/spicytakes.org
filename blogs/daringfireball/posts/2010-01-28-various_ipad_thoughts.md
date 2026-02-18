---
title: "Various and Assorted Thoughts and Observations Regarding the Just-Announced iPad"
date: 2010-01-28
url: https://daringfireball.net/2010/01/various_ipad_thoughts
slug: various_ipad_thoughts
word_count: 1644
---


## Automatic Transmission


Used to be that to drive a car, you, the driver, needed to operate a clutch pedal and gear shifter and manually change gears for the transmission as you accelerated and decelerated. Then came the automatic transmission. With an automatic, the transmission is entirely abstracted away. The clutch is gone. To go faster, you just press harder on the gas pedal.


That’s where Apple is taking computing. A car with an automatic transmission still shifts gears; the driver just doesn’t need to know about it. A computer running iPhone OS still has a hierarchical file system; the user just never sees it.


That’s not to say there aren’t trade-offs involved. Car enthusiasts (and genuine experts like race car drivers) still drive cars with manual transmissions. They offer more control; they’re more efficient. But the vast majority of cars sold today are automatics. So too it’ll be with computers. Eventually, the vast majority will be like the iPad in terms of the degree to which the underlying *computer* is abstracted away. Manual computers, like the Mac and Windows PCs, will slowly shift from the standard to the niche, something of interest only to experts and enthusiasts and developers.


## Popovers and Split Views


Across the iPad system, Apple has introduced a new UI element, which they’re calling popovers. It’s a perfect name. Popovers are like a cross between dialog boxes, drop-down menus, and inspector palettes. One example is the list of mailboxes in Mail when in vertical mode. When iPad Mail is in horizontal mode, you see a split view with two panels at once: accounts/mailboxes/messages on the left, and an always-present message detail panel on the right. When iPad Mail is in vertical mode, you just get one panel, but you can tap a button at the top left to show a popover of messages in the current mailbox.


They’re very well thought-out. As their name implies, they appear on-screen “over” existing views. But you can’t drag them around. They aren’t windows. They’re in a fixed position, always with an arrow pointing to the button or other control (like an event in Calendar) that the user tapped to open the popover. To close a popover, you just tap away from it — tapping anywhere other than within the popover closes it. Perhaps conceptually, it’s more like tapping the view *under* the popover to make it disappear. So popovers don’t have an “X” button in the top-left corner, or anything explicitly labeled “Close” or “Cancel” or “Done”. You just tap away. This is one of those aspects of the iPad UI that you just have to *feel* to get. It feels perfect.


According to the iPad Human Interface Guidelines (which, alas, are only available to registered iPhone SDK developers), there is a modal variant:


> Popovers and modal views are similar, in the sense that people
> typically can’t interact with the main view while a popover or
> modal view is open. But a modal view is always modal, whereas a
> popover can be used in two different ways:
> Modal, in which case the popover dims the screen area around
> it and requires an explicit dismissal. This behavior is very
> similar to that of a modal view, but a popover’s appearance tends
> to give the experience a lighter weight.
> Non-modal, in which case the popover does not dim the screen
> area around it and people can tap outside its bounds to dismiss
> it. This behavior makes a non-modal popover seem like another view
> in the application, not a separate state.


I don’t recall encountering the modal variety during my all-too-brief iPad spelunking expedition; the non-modal ones seem far more prevalent.


The overall effect of popovers is that you do *far* less view switching in an iPad app than you do an iPhone app. Things that slide an entirely new full-screen view on screen on the iPhone — like say going back from a message to a list of messages, or displaying your Safari bookmarks, or showing the details of a calendar event — on the iPad instead appear as popovers on a main view.


So imagine, say, an iPad Twitter client in horizontal mode. You could have a split view with a list of tweets running down the left. On the right, you could have a web view for reading web pages linked from tweets. Rather than sliding over and replacing the tweet list, they could exist side-by-side. And then a popover could provide an interface for switching between different accounts.


## Information Density


The iPad display offers 1024 × 768 pixels. At 9.7 inches diagonally, the pixel density is roughly 132 pixels per inch. That’s less than the iPhone and iPod Touch, which have 480 × 320 displays with roughly 162 pixels per inch. So text looks a little less sharp on the iPad. But it seemed to me that I naturally held it further away from my face than I do my iPhone, such that it seems just about equally sharp *effectively*.


What I found interesting is that I’m very familiar with this resolution — for *years* I used PowerBooks and iBooks with 1024 × 768 displays running Mac OS 9 or Mac OS X. 1024 × 768 somehow seems very different on the iPad than on Mac OS — physically smaller but conceptually bigger. The full-screen concept, without Mac-style overlapping draggable windows, leaves the iPad free to use as many pixels as possible for display *content* rather than UI chrome.


With the iPad Calendar app for example, the month view seemed more efficient and information-dense than iCal running on my 1440 × 900 pixel MacBook Pro display.


Also interesting is iPad Safari. Even though the screen offers the same pixel count as what was once the standard size for a laptop display, iPad Safari renders pages like iPhone Safari. The web surfing experience is all about zooming and panning.


## Hardware Keyboard Support


The announcement that most surprised me is the iPad’s support for hardware keyboards — not just the new docking unit, but also Bluetooth keyboards. I’m surprised because it is a very practical decision, but not elegant. There’s a certain beauty to how, with the iPhone and iPod Touch, input is completely and utterly limited to the touchscreen.


Needless to say, though, I’m surprised in a happy way. I can totally imagine traveling to conferences (or events like this) without a MacBook, but rather with an iPad and a keyboard.


The on-screen iPad keyboard is not bad at all, for what it is, but it’s exactly what you think — it’s for *pecking* not *typing*. If you want to do actual writing, you’re going to want a hardware keyboard.


Having used the hardware keyboard yesterday, though, it is clearly a secondary form of input. You cannot even vaguely drive the iPad interface by keyboard alone. It is almost entirely only for text input. The arrow keys really only work for text editing. Shift-arrow combos work for selecting ranges of text, and Command-arrow combos work for moving the insertion point to the beginning/end of lines. Option-arrow combos do not work for moving a word at a time, though.


Arrow keys don’t work for navigating the interface. This is the sort of thing I expect to improve over time (and who knows, maybe even before it actually ships), but there are some glaring holes. For example, in iPad Mail, when you start typing in the To: field to address a message, and the iPhone-style autocomplete suggestion list appears under the field, you cannot select from it using the keyboard. You have to touch the screen. The docking keyboard has no Esc key, replacing it instead with a key to simulate the iPad Home button. But so if you try to dismiss a popover with “Esc” and hit that button, boom, you’re dropped back to the home screen. And once back at the home screen, there doesn’t seem to be a way to launch apps via keyboard alone. It just seems like it’s not finished yet.


## Typography and iBooks


The iPad’s version of iPhone OS contains more fonts than iPhone OS 3.1, including my beloved Gill Sans. The iBooks app lets you switch the text face, but only from a choice of five fonts.


iBooks uses full-justified layout for books, with no apparent option to switch to ragged right. It doesn’t do hyphenation, so you wind up with very unsightly word-spacing gaps. No e-reader I’m aware of does justice to proper book typography, but I was hoping for better from Apple. It’s decent web-caliber typography, not print-caliber typography.


As for Amazon, they might wind up delighted with this thing. Apple’s in the business of selling devices first, content second. I think Amazon is in the content business first, the device business second. A world where Kindle hardware sales pale in comparison to the iPad but where there’s a very popular Kindle app for iPad that competes against iBooks is not a bad situation for Amazon. Apple is only selling e-books for use on their own devices; Amazon is willing to sell e-books anywhere they can.


## Money on the Table


Lastly, a thought regarding the iPad’s aggressive pricing. Apple is obviously leaving money on the table here. They could easily charge $999 as the starting price and have hundreds of people lined up outside every Apple Store ready to buy one on day one. Then they could drop the price later in the year, as the holiday season approaches.


Clearly they’re more interested in unit sales than per-unit margin. The mobile computing landscape is in land-grab mode, and Apple is trying to stake out a long-term dominating position.



| **Previous:** | [The iPad Big Picture](https://daringfireball.net/2010/01/ipad_big_picture) |
| **Next:** | [Who Can Do Something About Those Blue Boxes?](https://daringfireball.net/2010/01/blue_boxes) |


PreviousNext