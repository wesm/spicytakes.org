---
title: "iMessage Editing and Un-Sending in the Fourth iOS 16 and MacOS 13 Developer Betas"
date: 2022-08-01
url: https://daringfireball.net/2022/08/messages_editing_and_unsending_beta_4
slug: messages_editing_and_unsending_beta_4
word_count: 622
---


The iOS 16 and MacOS 13 “Ventura” fourth developer beta [shipped last week](https://www.macrumors.com/2022/07/27/ios-16-beta-4-messages-changes/). Most interesting to me are the updates to Messages and the new iMessage features announced at WWDC. The edit-a-message-you-just-sent feature, intended for fixing typos or mistakes, has been tweaked. The time limit for editing is now 15 minutes, sent messages can be edited up to five times, and the recipient of an edited message now has the ability to see the edit history by tapping the small “Edited” label under an edited message.


Undoing sent messages is now implemented too, with a two-minute time limit. I dig the balloon-popping effect you see as the sender after unsending the message. As the sender of the unsent message, you get a small-print status message in the chat timeline (the same style as “Delivered” and “Read” receipts) that says “You unsent a message. *Recipient Name* may still see the message on devices where the software hasn’t been updated.” On the recipient’s device, if they’re using MacOS 13 or iOS 16, the unsent message just disappears, but it’s replaced by a small-print status message that says “*Sender Name* unsent a message”.


Recipients do not get notifications for edits or unsends.

- [Video of editing a message](https://daringfireball.s3.amazonaws.com/misc/2022/07/ios-16-b4-edit-imessage.mp4).
- [Video of a recipient viewing the edit history](https://daringfireball.s3.amazonaws.com/misc/2022/07/ios-16-b4-view-edited-imessage.mp4).
- [Video of unsending a message](https://daringfireball.s3.amazonaws.com/misc/2022/07/ios-16-b4-undo-send-imessage.mp4).
- [Screenshot of a recipient’s indication that a message was unsent](https://daringfireball.s3.amazonaws.com/misc/2022/07/ios-16-b4-recipient-unsent-imessage.jpeg).


The unfortunate hitch with the new editing and unsending features is that they’re not backwards-compatible with the currently shipping versions of Messages. Unsent messages appear as they were originally delivered on recipient devices running older MacOS or iOS versions. Edited messages [appear as discrete new messages on older OSes](https://daringfireball.s3.amazonaws.com/misc/2022/07/macos-12-edited-imessage-legacy-view.png), in the form “Edited to ‘*Updated text of message*’”.


---


I like these features a lot, and think both of them will be much-used. It’s a shame they weren’t designed into the iMessage protocol years ago, but by year’s end, most people will be using iOS and MacOS versions that support them, and within a few years, almost everyone will.


The time limits, visible edit history, and even the fact that both features exist seem to be a source of [minor confusion](https://twitter.com/gruber/status/1552403063813578752), though.


Why offer message editing if you can just delete a message and resend it with the typo corrected? A three-step Undo-Send / type-a-corrected-version-of-the-message / resend works as an alternative to the actual Edit feature if you do it immediately. But it doesn’t if the message with the typo [is no longer the most recent message in the thread](https://twitter.com/gruber/status/1552536972433956864). Undo Send means “it was a mistake to send this message at all.”


Why offer an edit history? As the sender, it’s natural to wish that you could just fix a mistake without the recipient seeing the changes. But once the original typo-laden message arrives on the recipient’s device, it no longer belongs solely to the sender. There’s an implied property right, as it were, for the recipient to be able to see what was sent to them. An edit history is the best balance. (Slack, to name one example I’m familiar with, has shown an “Edited” label on edited messages for years, but won’t show you what the edits actually were. This annoys me occasionally.) The edit history can simply satisfy the recipient’s curiosity, but it also serves as strong discouragement against abuse. A malicious actor can’t send an abusive or misleading message and then edit it without a paper trail.


Why limit edits to five changes? Because stop screwing around. Five seems generous, really — my gut feeling is three strikes and you’re done.


Why have time limits? Because ink needs to dry.



| **Previous:** | [The 2022 13-Inch MacBook Air](https://daringfireball.net/2022/07/the_2022_13-inch_macbook_air) |
| **Next:** | [Vin Scully](https://daringfireball.net/2022/08/vin_scully) |


PreviousNext