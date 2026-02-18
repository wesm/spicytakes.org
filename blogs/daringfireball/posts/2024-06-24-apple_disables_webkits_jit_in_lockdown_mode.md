---
title: "Apple Disables WebKit’s JIT in Lockdown Mode, Offering a Hint Why BrowserEngineKit Is Complex and Restricted"
date: 2024-06-24
url: https://daringfireball.net/2024/06/apple_disables_webkits_jit_in_lockdown_mode
slug: apple_disables_webkits_jit_in_lockdown_mode
word_count: 812
---


Last week I mentioned Apple’s prohibition on JITs — [just-in-time compilers](https://en.wikipedia.org/wiki/Just-in-time_compilation) — [in the context of their rejection of UTM SE](https://daringfireball.net/linked/2024/06/18/utm-notarization), an open source PC emulator. Apple’s prohibition on JITs, on security grounds, is a side issue regarding UTM SE, because UTM SE is the version of UTM that doesn’t use a JIT. But because it doesn’t use a JIT, it’s so slow that [the UTM team doesn’t consider it worth fighting](https://x.com/UTMapp/status/1799647652134654045) with Apple regarding its rejection.


On that no-JITs prohibition, though, it’s worth noting that Apple even disables its own trusted JIT in WebKit when you enable Lockdown Mode, which Apple [now describes](https://support.apple.com/en-us/105120) as “an optional, extreme protection that’s designed for the very few individuals who, because of who they are or what they do, might be personally targeted by some of the most sophisticated digital threats. Most people are never targeted by attacks of this nature.” Apple [previously described](https://daringfireball.net/linked/2022/07/11/lockdown-mode) Lockdown Mode as protection for those targeted by “private companies developing state-sponsored mercenary spyware”, but has [recently dropped](https://www.reuters.com/technology/cybersecurity/apple-warns-users-mercenary-spyware-attack-91-countries-including-india-et-2024-04-11/) the “state-sponsored” language.


[Here’s how Apple describes Lockdown Mode’s effect on web browsing](https://support.apple.com/en-us/105120):


> Web browsing — Certain complex web technologies are blocked, which
> might cause some websites to load more slowly or not operate
> correctly. In addition, web fonts might not be displayed, and
> images might be replaced with a missing image icon.


JavaScriptCore’s JIT interpreter is one of those “complex web technologies”. [Alexis Lours did some benchmarking two years ago](https://alexi.sh/blog/2022/07/lockdown-jsc/), when iOS 16 was in beta, to gauge the effect of disabling the JIT on JavaScript performance (and he also determined a long list of other WebKit features that get disabled in Lockdown Mode, a list I wish Apple would publish and keep up to date). Lours ran several benchmarks, but I suspect [Speedometer](https://browserbench.org/Speedometer3.0/) is most relevant to real-world usage. Lours’s benchmarking indicated roughly a two-third reduction in JavaScript performance with Lockdown Mode enabled in Speedometer.


This brings me to [BrowserEngineKit](https://developer.apple.com/documentation/browserenginekit), a new framework Apple created specifically for compliance with the EU’s DMA, which requires gatekeeping platforms to allow for third-party browser engines. Apple has permitted third-party *browsers* on iOS [for over a decade](https://www.theverge.com/2012/6/28/3123689/google-announces-chrome-for-iphone-and-ipad), but requires all browsers to use the system’s WebKit rendering engine. One take on Apple’s longstanding prohibition against third-party rendering engines is that they’re protecting their own interests with Safari. More or less that they’re just being dicks about it. But there really is a security angle to it. JavaScript engines run much faster with JIT compilation, but JITs inherently pose security challenges. There’s a whole section in the BrowserEngineKit docs [specifically about JIT compilation](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time).


As I see it Apple had three choices, broadly speaking, for complying with the third-party browser engine mandate in the DMA:

1. Disallow third-party browser engines from using JITs. This would clearly be deemed malicious by anyone who actually wants to see Chromium or Gecko-based browsers on iOS. JavaScript execution would be somewhere between 65 to 90 percent slower compared to WebKit.
2. Allow third-party browser engines in the EU to just use JIT compilation freely without restrictions. This would open iOS devices running such browsers to security vulnerabilities. The message to users would be, effectively, “If you use one of these browsers you’re on your own.”
3. Create something like BrowserEngineKit, which adds complexity in the name of allowing for JIT compilation (and other potentially insecure technologies) in a safer way, and limit the use of BrowserEngineKit only to trusted web browser developers.


Apple went with choice 3, and I doubt they gave serious consideration to anything else. Disallowing third-party rendering engines from using JITs wasn’t going to fly, and allowing them to run willy-nilly would be insecure. The use of BrowserEngineKit [also requires a special entitlement](https://developer.apple.com/support/alternative-browser-engines):


> Apple will provide authorized developers access to technologies
> within the system that enable critical functionality and help
> developers offer high-performance modern browser engines. These
> technologies include just-in-time compilation, multiprocess
> support, and more.
> However, as browser engines are constantly exposed to untrusted
> and potentially malicious content and have visibility of sensitive
> user data, they are one of the most common attack vectors for bad
> actors. To help keep users safe online, Apple will only authorize
> developers to implement alternative browser engines after meeting
> specific criteria and who commit to a number of ongoing privacy
> and security requirements, including timely security updates to
> address emerging threats and vulnerabilities.


BrowserEngineKit isn’t easy, but I genuinely don’t think any good solution would be. Browsers don’t need a special entitlement or complex framework to run on MacOS, true, but iOS is not MacOS. [To put it in Steven Sinofsky’s terms](https://hardcoresoftware.learningbyshipping.com/p/215-building-under-regulation), gatekeeping is a fundamental aspect of Apple’s brand promise with iOS.



| **Previous:** | [WWDC 2024: Apple Intelligence](https://daringfireball.net/2024/06/wwdc24_apple_intelligence) |
| **Next:** | [It’s the Guns, It’s the Guns, It’s the Guns](https://daringfireball.net/2024/07/its_the_guns) |


PreviousNext