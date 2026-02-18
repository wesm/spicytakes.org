---
title: "New iPhone Developer Agreement Bans the Use of Adobe’s Flash-to-iPhone Compiler"
date: 2010-04-08
url: https://daringfireball.net/2010/04/iphone_agreement_bans_flash_compiler
slug: iphone_agreement_bans_flash_compiler
word_count: 638
---


Prior to today’s release of the iPhone OS 4 SDK, section 3.3.1 of the iPhone Developer Program License Agreement read, in its entirety:


> 3.3.1 — Applications may only use Documented APIs in the manner
> prescribed by Apple and must not use or call any private APIs.


In the new version of the iPhone Developer Program License Agreement released by Apple today (and which developers must agree to before downloading the 4.0 SDK beta), section 3.3.1 now reads:


> 3.3.1 — Applications may only use Documented APIs in the manner
> prescribed by Apple and must not use or call any private APIs.
> Applications must be originally written in Objective-C, C, C++, or
> JavaScript as executed by the iPhone OS WebKit engine, and only
> code written in C, C++, and Objective-C may compile and directly
> link against the Documented APIs (e.g., Applications that link to
> Documented APIs through an intermediary translation or
> compatibility layer or tool are prohibited).


My reading of this new language is that cross-compilers, such as the [Flash-to-iPhone compiler](http://labs.adobe.com/technologies/flashcs5/appsfor_iphone/) in Adobe’s upcoming Flash Professional CS5 release, are prohibited. This also bans apps compiled using [MonoTouch](http://monotouch.net/) — a tool that compiles C# and .NET apps to the iPhone. It’s unclear what this means for tools like [Titanium](http://www.appcelerator.com/) and [PhoneGap](http://phonegap.com/), which let developers write JavaScript code that runs in WebKit inside a native iPhone app wrapper. They might be OK. [This tweet from the PhoneGap Twitter account](http://twitter.com/phonegap/status/11843827934) suggests they’re not worried. The folks at Appcelerator [realize, though, that they might be out of bounds](http://developer.appcelerator.com/blog/2010/04/apple-4-0-and-titanium.html) with Titanium. [Ansca’s Corona SDK](http://anscamobile.com/), which lets you write iPhone apps using Lua, strikes me as out of bounds.


I originally thought this would ban games written using [Unity3D](http://unity3d.com/unity/), but perhaps not — Unity3D produces a complete Xcode project and Objective-C source files, so it’s more like a pre-processor than a cross-compiler. Hard to tell. If you forced me to bet, though, the fact that developers are writing C# code puts Unity3D on the wrong side of this rule.


There was no mention of this change during the announcement event today, but the language in the agreement doesn’t leave much wiggle room for Flash CS5. It could hardly be more clear if they singled out Flash CS5 by name. (Wonder what Adobe does now? CS5 is *thisclose* to release and the iPhone compiler is the flagship feature in this version of Flash. They’re pretty much royally fucked.)


I’m not sure how exactly Apple intends to enforce this, but my understanding is that iPhone apps produced by Flash CS5 are easily identifiable as such by inspecting the contents of the app bundle. I’m not sure if there are any “intermediary translation or compatibility layers or tools” which produce app bundles that are indistinguishable from app bundles produced by Xcode and the official SDK.


**Update:** To be clear, I do not think that Apple is singling out Flash CS5. I do think, though, that Flash CS5’s cross-compiler epitomizes the sort of meta-frameworks Apple is not going to allow. Same goes for MonoTouch. What Apple doesn’t want — and as we see now, is not going to allow — is for anyone other than Apple to define the framework for native iPhone apps. What Apple is saying here is, if you’re going to write a native iPhone app, then you need to target our platform; if you want to do something else, then target the iPhone with an optimized web app. I.e., the iPhone OS supports two software platforms: Cocoa Touch and the web. Apple isn’t going to let anyone else build a meta-platform on top of Cocoa Touch. I think [this comment at Hacker News from “raganwald” nails Apple’s perspective on this](http://news.ycombinator.com/item?id=1250946).



| **Previous:** | [The iPad](https://daringfireball.net/2010/04/the_ipad) |
| **Next:** | [Why Apple Changed Section 3.3.1](https://daringfireball.net/2010/04/why_apple_changed_section_331) |


PreviousNext