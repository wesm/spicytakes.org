---
title: "Meta Replaced the Native Windows WhatsApp App With a Shitty Web App"
date: 2025-11-15
url: https://daringfireball.net/2025/11/meta_whatsapp_windows_shitty_web_app
slug: meta_whatsapp_windows_shitty_web_app
word_count: 904
---


[Mayank Parmar, writing for Windows Latest](https://www.windowslatest.com/2025/11/12/meta-just-killed-native-whatsapp-on-windows-11-now-it-opens-webview-uses-1gb-ram-all-the-time/):


> WhatsApp on Windows 11 has just got a “major” upgrade, and you’re
> probably going to hate it because it simply loads web.whatsapp.com
> in a WebView2 container. This means WhatsApp on Windows 11 is
> cooked, and it’s back to being absolute garbage in terms of
> performance.
> WhatsApp is one of those Windows apps that went from being a web
> wrapper to a native app and then back to the web again after all
> these years of investment. WhatsApp for Windows was originally an
> Electron app, and it was eventually replaced with UWP after years
> of investment. Four years later, WhatsApp is going back to
> WebView2, abandoning the original WinUI/UWP native idea. [...]
> An app can use a lot of memory, and it does not necessarily mean
> it’s a performance nightmare, but the issue with the new WhatsApp
> is that it feels sluggish. You’re going to notice sluggish
> performance, long loading time, and other performance issues when
> browsing different conversations.
> We also noticed that it does not work well with Windows
> notifications. It also struggles with Windows 11’s Do Not Disturb
> mode or Active Hours. And there are delayed notifications problems
> as well.


I found this post interesting on a few fronts.


First, from the perspective of Meta. They replaced a shitty web app wrapper for Windows with a modern native Windows app, one that seemingly pleased Windows aficionados like Parmar. And now they’ve thrown that app away, going back to what that native app replaced four years ago: a web app wrapper that is bloated, slow, and unsurprisingly has poor support for native Windows features. It’s bad enough that so many large companies never even bother creating native apps, but it feels even worse to see a good native app abandoned.


Second, it’s interesting reading Parmar’s list of gripes about the new web-app-wrapper WhatsApp app. All his gripes have merit, but it struck me that none of them are about the UI. Maybe the web app’s UI is actually fine? I have no idea. But I suspect it’s more that the Windows nerd mindset has UI design quality and adherence to recommended platform idioms way down on their list of priorities. That’s why they’re Windows users, not Mac users.


Lastly, I wonder if this bodes poorly for the future of the current [WhatsApp app for MacOS](https://apps.apple.com/us/app/whatsapp-messenger/id310633997), a native app written using [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst), Apple’s framework for porting iOS UIKit apps to the Mac. Like most Catalyst apps, WhatsApp for Mac isn’t a good Mac app. It doesn’t support the Services menu at all. It doesn’t let you open chats into standalone windows, or open more than one chat window. It opens its Settings right in its one main window. The whole “there’s only one window, and everything is in that one window” design is very iOS. The menu bar is a HIG prescriptivist’s nightmare. All the multi-word menu commands are in *Sentence case* rather than *Title Case* (except, of course, for the menu commands that come “free” with Catalyst — how do the developers of the app not notice this?), and the menu title order goes: File, Chat, Edit, Call, View, Window, Help (obviously [it should be](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar) File, Edit, View, Chat, Call, Window, Help). Has there ever once, in 41 years, been a good Mac app that puts a menu between “File” and “Edit”?


But, still, WhatsApp for Mac is a better Mac app [than any Electron app I’ve ever used](https://daringfireball.net/2018/12/electron_and_the_decline_of_native_apps). Examining it now, it seems lightweight on both CPU usage and memory. It feels a bit better to me than either Signal or Beeper, both of which are developed using Electron, and both of which consume more RAM than WhatsApp. To name just one obvious nicety: when you send a new message in an older chat in WhatsApp, that chat *animates* as it moves to the top of the list of chats. It slides up, and other chats slide down as they re-sort. In the Signal and Beeper apps for Mac, an updated chat just zaps to the top of the chat list, with no animation at all. Gross.


The question is, did Meta scrap its native Windows app because they don’t care that much about Windows in particular? Or because they don’t care that much about native desktop apps, period — and a crude web app wrapper is coming to Mac next? WhatsApp for Mac is currently the [top-ranked free app in the Mac App Store](https://apps.apple.com/us/mac/charts/36?chart=top-free) — but it’s also [the top-ranked free Windows app in the Microsoft Store](https://apps.microsoft.com/collections/computed/apps/TopTrending?hl=en-US&gl=US). Meta did just ship a native Apple Watch app for WhatsApp, but if you want an app for WatchOS, it has to be native. You can’t ship a web app wrapper like an Electron app there.


Personally, I won’t care too much if Meta shitcans the WhatsApp Mac app, because I barely use WhatsApp. But outside America, WhatsApp is the dominant messaging platform in much (most?) of the world. I’d be worried  if I were a Mac user who uses WhatsApp heavily.



| **Previous:** | [OpenAI Releases GPT-5.1, Along With Renamed and New Personalities](https://daringfireball.net/2025/11/chatgpt_5-1_with_renamed_and_new_personalities) |
| **Next:** | [Exploring, in Detail, Apple’s Compliance With the EU’s DMA Mandate Regarding Apple Watch, Third-Party Accessories, and the Syncing of Saved Wi-Fi Networks From iPhones to Which They’re Paired](https://daringfireball.net/2025/11/apple_eu_dma_iphone_accessories_wi-fi_sync) |


PreviousNext