---
title: "iOS Messages and Smart Punctuation"
date: 2018-02-20
url: https://daringfireball.net/2018/02/ios_messages_smart_punctuation
slug: ios_messages_smart_punctuation
word_count: 559
---


iOS 11 finally added a long-awaited feature for those of us who care about typographic details: [smart punctuation](https://www.macstories.net/stories/ios-11-the-macstories-review/10/#smart-punctuation). You can turn this on in Settings → General → Keyboards. When enabled, quotes and apostrophes (like "this" and 'this') are automatically turned into their proper counterparts (like “this” and ‘this’), two hyphens in a row (--) are turned into a proper em-dash (—), etc.


I say “finally” because MacOS has had the feature in the standard text editing system for many years, and I can’t think of a good reason why it wasn’t in iOS years ago. I can say it’s not a difficult programming job to solve because [I’ve solved it](https://daringfireball.net/projects/smartypants/) in the more difficult context of smartening punctuation in prose without messing up the necessary dumb quotes inside HTML tags.


In some recent update to iOS (I think 11.2.5, but it might have been an earlier 11.2.x update), smart punctuation stopped working in Messages — and as far as I can tell, only Messages. Why? My best guess: unintended consequences when sending SMS messages.


[Here’s a thread on Apple’s help forum addressing the issue](https://forums.developer.apple.com/thread/87450). SMS is such an old standard that it was designed with the [ASCII character set](https://en.wikipedia.org/wiki/ASCII) in mind. An SMS message containing only ASCII characters can contain up to 160 characters. Include even just a single non-ASCII character, though — such as a curly quote or apostrophe, or an emoji — and the entire message must be encoded using a 16-bit alphabet, limiting the message to just 70 characters because the length of the message in bytes remains fixed by the protocol.1


In short: if you stick to dumb quotes, you can put 160 characters in an SMS message. Include just one smart/curly quote, and you only get 70 characters.


I don’t know for sure that this is why iOS 11’s smart punctuation feature no longer works in Messages, but it’s the only explanation that I can think of. (I’ve seen some speculation that this might be a machine learning bug, but machine learning bugs, like the [infamous “I → weird-looking A” fiasco](https://www.macrumors.com/2017/11/01/ios-11-predictive-text-bug/) from a few months ago, aren’t limited to one app like Messages. And “Smart Punctuation” is a separate setting from “Predictive Text” in the Settings app — you can use either without the other.)


But if I’m right about why, then why does it apply to iMessage messages — a.k.a. blue-bubble messages — too? iMessage messages aren’t limited by the antiquated constraints of SMS in any other way, so why limit them typographically?


This is a story with a happy ending, because it looks like iOS 11.3 will fix this. After installing [today’s new 11.3 developer beta](https://www.macrumors.com/2018/02/20/apple-seeds-ios-11-3-beta-3-to-developers/) on both an iPad and iPhone, smart punctuation is back when writing a (blue) iMessage, and is disabled only when writing a (green) SMS.2


Smart.


---

1. Technically, [SMS messages use the GSM-7 text encoding](https://en.wikipedia.org/wiki/SMS#Message_size), not ASCII. But like ASCII, GSM-7 is a 7-bit encoding limited to just 128 characters. ↩︎
2. It still isn’t as smart as it could be. Consider the case of [people who write in a language that requires 16-bit encoding](https://twitter.com/nosenkow/status/966077457056100352), and thus are limited to 70 characters in all their SMS messages. Why disable smart punctuation for them? ↩︎︎



| **Previous:** | [Sponsoring Daring Fireball, Early 2018 Edition](https://daringfireball.net/2018/02/sponsoring_daring_fireball) |
| **Next:** | [Max Krieger’s Twitter Threads on Design](https://daringfireball.net/2018/03/max_krieger_twitter_design_threads) |


PreviousNext