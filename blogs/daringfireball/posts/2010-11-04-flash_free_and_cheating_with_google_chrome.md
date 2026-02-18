---
title: "Going Flash-Free on Mac OS X, and How to Cheat When You Need It"
date: 2010-11-04
url: https://daringfireball.net/2010/11/flash_free_and_cheating_with_google_chrome
slug: flash_free_and_cheating_with_google_chrome
word_count: 1146
---


Last week [I mentioned](http://daringfireball.net/linked/2010/10/25/youtube5) that, [following Steven Frank’s lead](http://stevenf.tumblr.com/post/1376712559/when-i-heard-that-the-new-macbook-air-models-were), I’d completely disabled Flash Player on my Mac.﻿ But I have a cheat, for web pages with Flash content with no non-Flash workaround. I’m really happy with this setup, so I thought I’d document it here.


Previously, I used and recommended the excellent [ClickToFlash plugin for Safari](http://clicktoflash.com/). The original ClickToFlash is a *plugin*, not an *extension*. That sounds pedantic, perhaps, but bear with me. Earlier this year, Safari 5 introduced a new, officially supported *extension* API. These Safari extensions are much like Firefox extensions. They’re written using JavaScript (and HTML and CSS for presentation, if they present a user interface). Safari extensions are the things [Apple lists here](http://extensions.apple.com/), and which you manage via the Extensions tab in Safari’s preferences window. Web content *plugins* are not new — they date back to Netscape in the mid-1990s. Plugins are for content formats. E.g., if you have the QuickTime plugin installed, then your browser can play embedded QuickTime movies. Flash Player is a plugin.


The original ClickToFlash was possible before the Safari 5 *extension* API even existed because it (the original ClickToFlash) is a *plugin*. It masquerades as a plugin that claims to be able to play Flash content, and overrides the actual Flash Player plugin. So when you load a web page containing Flash, the browser lets the ClickToFlash plugin handle the embedded Flash. Instead of actually loading the Flash content, ClickToFlash instead draws a box with a nice little “Flash” logo. If the user clicks that box, ClickToFlash hands the content over to the *actual* Flash Player plugin. Thus, Flash Player is there, and works, but it only loads after the user clicks on a Flash content box to load it. It’s a kludge, but it works well, and I’ll bet many of you are using it.


Confusion sets in when you see that there also exists [a “ClickToFlash” *extension* for Safari 5](http://hoyois.github.com/safariextensions/clicktoflash/) — a project by Marc Hoyois that duplicates most of the features of the ClickToFlash plugin using the new extension API instead of the long-standing plugin API. It looks interesting, and some DF readers have emailed me to endorse it, but I haven’t tried it personally.


Here’s what I did last week.


First, I disabled the Flash Player and old ClickToFlash plugins. On my system, Flash Player was in the default location: */Library/Internet Plug-Ins/*. I moved “Flash Player.plugin”, “flashplayer.xpt”, and “NP-PPC-Dir-Shockwave” out of that folder and into a new folder I created next to it named “Internet Plug-Ins (Disabled)”. All you need to do to disable them is move them out of */Library/Internet Plug-Ins/*. I also moved ClickToFlash (“ClickToFlash.webplugin”) to this disabled plugins folder. (ClickToFlash, if you have it installed, might be in the *Library/Internet Plug-Ins/* folder in your home folder, rather than at the root level of your startup drive.)


After logging out and logging back in to my user account, Flash Player is no longer available to Safari or Firefox. This is more or less the state Mac OS X [is now shipping in by default](http://daringfireball.net/2010/10/apple_no_longer_bundling_flash_with_mac_os_x). To me this is better, and in some way more honest, than using ClickToFlash. Without Flash installed, Safari effectively tells websites you visit, “Hey, I don’t have Flash installed”, which allows the sites to send alternative content. Static images instead of Flash for ads, for example. With ClickToFlash, Safari is effectively telling websites you visit, “Yes, sure, I have Flash installed,” but then not actually loading Flash content. I see far fewer “Flash missing” boxes in web pages now than I did with ClickToFlash.


As per Frank’s recommendation, I’ve installed the excellent [YouTube5 Safari extension by Connor McKay](http://www.verticalforest.com/2010/10/27/youtube5-version-2/). With this extension installed, embedded YouTube videos are modified to use the HTML5 video tag rather than Flash Player for playback. This is possible because behind the scenes, all YouTube videos are encoded using H.264.


For the vast majority of my surfing, this new setup works great. I prefer it over my previous setup using the ClickToFlash plugin because Flash Player is never left running in the background because of a background Safari web page on which I clicked to load Flash content hours (or even days) ago. It also means that the Flash plugin never gets loaded into other non-browser apps that happen to use WebKit — eliminating the number one [source of crashes](http://inessential.com/2009/02/23/app_wanted_crash_log_database_and_analy) for many of these apps.


## Cheating With Google Chrome


But that doesn’t mean I never run into Flash content I wish to view but for which there is no HTML5 alternative. Google Chrome offers a workaround — Chrome includes its own self-contained Flash Player plugin. Removing Flash Player from */Library/Internet Plug-Ins/* prevents Safari and Firefox (and almost all other Mac web browsers) from loading Flash content, but not Chrome.


So, whenever I hit a page with Flash content I wish to view, I open that page in Chrome. As soon as I’m done watching it, I quit Chrome, which ensures Flash Player isn’t left running in the background.


I’ve also added a shortcut for opening the current Safari page in Chrome quickly. First, if you haven’t done so already, enable Safari’s Develop menu. (It’s a checkbox in the “Advanced” panel of Safari’s preferences window.) The Develop menu contains an “Open Page With” sub-menu, which lists all the web browsers you have installed on your system. [Using the Keyboard Shortcuts section in System Preferences](http://support.apple.com/kb/HT2490?viewlocale=en_US#l4), I set a custom menu key shortcut for the command to open the current page in Google Chrome. Whenever I’m on a page in Safari with Flash content I wish to view, I hit that shortcut, and boom, Chrome launches and loads that page. (Hint: when you create the custom shortcut, and are asked for the name of the menu item, just use “Google Chrome” or “Google Chrome.app” (whichever appears in your Open Page With sub-menu).)


**Update, 14 March 2011:** Safari 5.0.4 changed the Develop menu a bit, breaking the above instructions. The easiest solution is to [use this AppleScript from TJ Luoma](http://www.tuaw.com/2011/03/14/use-applescript-to-open-current-safari-url-in-google-chrome/).


## The Coming of HTML5 Animated Ads


Whenever I mention the performance and battery life gains to be had by disabling Flash Player (like [this eye opener from yesterday](http://daringfireball.net/linked/2010/11/03/ars-flash-air)), I get a few responses via email and Twitter pointing out that if advertisers switch to HTML5 from Flash for obnoxious animated ads, those performance gains may vanish, and, perhaps worse, it won’t be as easy to block unwanted HTML5 animation in this hypothetical future as it is to block unwanted Flash animation today, because HTML5 isn’t rendered through a specific plugin.


My answer: We’ll cross that bridge when we come to it. As of today, there are significant performance and battery life gains to be had by disabling Flash Player on Mac OS X.



| **Previous:** | [Regarding the Idea of iPad Apps Running on Mac OS X](https://daringfireball.net/2010/11/ipad_apps_mac_os_x) |
| **Next:** | [Apple’s Pricing Advantage](https://daringfireball.net/2010/11/apples_pricing_advantage) |


PreviousNext