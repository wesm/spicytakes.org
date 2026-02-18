---
title: "Rootkit, Eh?"
date: 2011-12-01
url: https://daringfireball.net/2011/12/rootkit_eh
slug: rootkit_eh
word_count: 641
---


Thom Holwerda, OSNews, headline: “[CarrierIQ Rootkit Found on Android, iOS](http://www.osnews.com/story/25384/CarrierIQ_Rootkit_Found_on_Android_iOS)”


Really?


On iOS the setting is off by default, plainly labeled, and even when turned on, [apparently](http://blog.chpwn.com/post/13572216737) only logs (a) location data and (b) when a phone call was active. And it doesn’t even log location data if Location Services are disabled — a setting which, again, is plainly labeled and easy to find.


[According to Trevor Eckhart](http://androidsecuritytest.com/features/logs-and-services/loggers/carrieriq/), on HTC Android phones, the Carrier IQ daemon logs the following: every number you press in the phone dialer, every key you type on the keyboard, every SMS message you receive, every URL you open in the web browser, every app you open, all media playback, and your location. There is no visible sign that this is running, the process is hidden from the process viewer, and there is no way to turn it off.


From that information, Holwerda chooses the headline “CarrierIQ Rootkit Found on Android, iOS”. [**Update:** The headline has since been changed to “CarrierIQ Rootkit Found on Android”.]


> As a sidenote, it amuses me to no end how someone like John Gruber
> has mysteriously and quite suddenly adopted the “it’s the
> carrier’s fault!”-mantra now that iOS has also been found to
> include CarrierIQ. Which is ironic, since it appears that Apple is
> the only one including CarrierIQ (slightly butchered, but still)
> within the operating system itself, whereas on Android, it’s a
> carrier thing.


I could point out that describing the Carrier IQ-related logging on iOS as a “slightly butchered” version of what’s been found on HTC Android phones is an absurd instance of [false equivalence](http://mediamatters.org/blog/201101100029), but that’s self-evident. I enjoy a debate regarding my work and any perceived biases in it, and I’d like to think that OSNews is a reasonable source with a different perspective, which is why I’m responding to this. But I worry here that I’m trying to reason with the unreasonable.


How could my stance on Carrier IQ “suddenly” change when I’d never written about it before yesterday? I’ve gone back and re-read everything I’ve written about it thus far ([here](http://daringfireball.net/linked/2011/11/30/), [here](http://daringfireball.net/2011/12/translation_carrier_iq), and [here](http://daringfireball.net/linked/2011/12/01/)), and I can’t find a single word where I place blame anywhere other than in the hands of the carriers. (Which, as the story continues to unfold, looks to be exactly where the blame *should* be placed.) I didn’t even crack an “Android is open” joke.


What’s important here is not merely the presence of anything related to “Carrier IQ”. What’s important is the surreptitious logging and collection of sensitive private data. It is certainly interesting that Apple is using Carrier IQ services to log anything at all, and worthy of investigation. But to date, we’ve learned nothing scandalous, misleading, or unclear about what Apple is doing in this regard. There’s not a shred of evidence that Apple is now or ever was using Carrier IQ for anything other than collecting only and exactly the sort of data Apple says, plainly, that it collects when the user chooses — explicitly — to allow it.


Apple has a clearly-worded diagnostics collection privacy policy, which you can read on the device in Settings → General → About → Diagnostics & Usage → “About Diagnostics and Privacy”. I’m hosting [a copy of it here](http://daringfireball.net/misc/2011/12/ios-5-diagnostics-privacy-policy.text) so everyone can read it. It’s short and utterly reasonable.


The worst that can be said of Apple in this saga is that they’re guilty by association — that Apple used, for innocuous purposes, the services of a company that others have used for nefarious purposes. To put this in the same boat as Android devices which ship from the factory with secret keyloggers installed is absurd.



| **Previous:** | [Translation From Corporate Jargon Doublespeak to English of Carrier IQ’s ‘Media Alert’ ](https://daringfireball.net/2011/12/translation_carrier_iq) |
| **Next:** | [The New Twitter (R.I.P. Tweetie)](https://daringfireball.net/2011/12/new_twitter) |


PreviousNext