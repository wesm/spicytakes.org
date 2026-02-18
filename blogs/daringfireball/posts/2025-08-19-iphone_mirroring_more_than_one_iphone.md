---
title: "How to Use iPhone Mirroring With More Than One iPhone"
date: 2025-08-19
url: https://daringfireball.net/2025/08/iphone_mirroring_more_than_one_iphone
slug: iphone_mirroring_more_than_one_iphone
word_count: 1000
---


I’ve been using two iPhones throughout the summer — one running iOS 18, the other running iOS 26 betas. I found myself wanting to switch between them with iPhone Mirroring on my Mac, but couldn’t figure out how. The answer, from Apple Support, “[iPhone Mirroring: Use your iPhone from your Mac](https://support.apple.com/en-us/120421)”:


> If you have more than one iPhone that is both signed in to your
> Apple Account and nearby, you can choose the one that your Mac
> uses for mirroring and iPhone notifications:
> Choose Apple menu  > System Settings, then click Desktop &
> Dock in the sidebar.
> Choose your iPhone from the iPhone pop-up menu on the right.
> This menu appears just below the “Use iPhone widgets” setting.
> It appears only when your Mac detects more than one nearby
> iPhone that can be used for mirroring.


That pop-up menu is about halfway down the screen in Desktop & Dock, in the “Widgets” section.1 I suspected this was possible, but I had to search the web ([via Kagi](https://daringfireball.net/2025/04/try_switching_to_kagi), the best search engine in the world, of course) to find the answer. I never would have thought to look in System Settings → Desktop & Dock, let alone, even if I happened to look in that panel, all the way down under “Widgets”.


Places where I *did* look:

- On the Mac, in the iPhone Mirroring app’s own Settings window. Nope.
- On the iPhone, in Settings → General → Airplay & Continuity. This is where you can control which Mac or Macs your iPhone is available from with iPhone Mirroring (e.g. you can go here to revoke access from a certain Mac), but it doesn’t help you change which iPhone, among multiple, that any particular Mac connects to.


To Apple’s credit, searching for “mirroring” in MacOS System Settings [does lead you to the correct setting](https://daringfireball.net/misc/2025/08/macos-18.6-settings-desktop-dock.png), but because it’s under “Widget settings”, I suspect some people who search for “mirroring” here will see that in the results list and not even bother clicking it, because “Widget settings” at first doesn’t sound like where you should go to choose between multiple phones for iPhone Mirroring. (It kind of makes sense, when you realize that the same iPhone that provides widgets to your Mac is the one available for iPhone Mirroring to connect to.)


To Apple’s discredit, Siri is no help, despite Apple Intelligence’s supposed [ability to harness “product knowledge”](https://9to5mac.com/2025/02/26/this-is-every-apple-intelligence-feature-thats-available-now/) from LLM training on Apple’s own support documents. After asking Siri, “How do I use multiple iPhones with iPhone mirroring?” on either a Mac or iPhone, I get a brief answer that says “You can set up more than one iPhone to use iPhone Mirroring with your Mac, but you can only connect to one iPhone at a time”, with a link to the iPhone User Guide that opens in the Tips app. That page in the iPhone User Guide, however — also available on the web as “[Control Your iPhone From Your Mac](https://support.apple.com/guide/mac-help/control-your-iphone-from-your-mac-mchl444d53a6/mac)” — doesn’t contain any mention of using more than one iPhone with iPhone Mirroring. So [this Apple Support document](https://support.apple.com/en-us/120421) on iPhone Mirroring does explain it (that’s the one I linked to at the top of this post), but [this one does not](https://support.apple.com/guide/mac-help/control-your-iphone-from-your-mac-mchl444d53a6/mac). No wonder Apple Intelligence’s “product knowledge”, trained on these documents, is somewhat confused.


But it gets worse. I gave Siri a second chance on my Mac, asking the same question, something along the lines of “How do I use multiple iPhones with iPhone mirroring?” (I can’t be sure exactly which words I used because Siri doesn’t show a chat transcript2), and the second time, [it responded thus](https://daringfireball.net/misc/2025/08/siri-mirroring-nonsense.png):


> To use multiple iPhones with iPhone Mirroring:
> Open the iPhone Mirroring app on your Mac.
> Click the “Connect” button.
> Enter your iPhone passcode and choose how to authenticate.
> Select the iPhone you want to use from the list of available
> iPhones.


This answer certainly describes one possible way that using multiple iPhones with iPhone Mirroring *should* work, but as an answer for how it actually *does* work, it’s abject nonsense. There is no “list of available iPhones” in the iPhone Mirroring app. If there were such a list to choose from, I’d never have had a question about this whole fucking thing in the first place.


---

1. The first time I looked in the Desktop & Dock panel in System Settings, there was no “iPhone” pop-up menu visible, despite the fact that both of my active iPhones were on my desk, right next to my MacBook Pro. But I remembered that in the last few days, I’d been having problems with [Continuity’s Universal Clipboard](https://support.apple.com/en-us/102430) feature too. In the past, when Universal Clipboard has gone on the fritz, I’ve solved the problem by toggling Bluetooth off and back on. I toggled Bluetooth on my Mac and boom, the “iPhone” menu appeared in the Desktop & Dock panel in System Settings, with the pop-up menu correctly listing both of my active iPhones. Universal Clipboard started working correctly again too. I bet the *next* version of Bluetooth is actually going to be reliable. ↩︎︎
2. From Wayne Ma’s blockbuster report back in April at The Information, “[How Apple Fumbled Siri’s AI Makeover](https://daringfireball.net/linked/2025/04/10/wayne-ma-the-information-apple-siri-fumble)”:

Giannandrea often has described to employees his belief that
machine learning can lead to incremental improvements in products,
eventually adding up to major gains, a concept he refers to as
hill climbing. He also has expressed a dim view of chatbots in the
past, telling Apple employees before and immediately after the
release of ChatGPT that he didn’t believe they added much value
for users.

[ChatGPT reported 700 million weekly active users this month](https://x.com/nickaturley/status/1952385556664520875), up from 500 million in March, and up 4× from last year. ↩︎



| **Previous:** | [Joe Caroff, Designer of the James Bond 007 Logo, Dies at 103](https://daringfireball.net/2025/08/joe_caroff_007_logo_designer) |
| **Next:** | [MSNBC, Spinning Out of NBCUniversal, Rebrands as ‘MS NOW’ With a Godawful Backronym and Even Worse Logo](https://daringfireball.net/2025/08/msnbc_ms_now_rebranding) |


PreviousNext