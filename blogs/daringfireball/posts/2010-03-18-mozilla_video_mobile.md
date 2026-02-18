---
title: "Mozilla, Video, and Mobile Computing"
date: 2010-03-18
url: https://daringfireball.net/2010/03/mozilla_video_mobile
slug: mozilla_video_mobile
word_count: 853
---


With [Microsoft’s announcement this week that IE9 will support H.264 HTML5 video](http://blogs.msdn.com/ie/archive/2010/03/16/html5-hardware-accelerated-first-ie9-platform-preview-available-for-developers.aspx), three of the big four browsers — IE, Safari, and Chrome — will soon support H.264. The only major browser holdout is Firefox.1


[Mozilla is couching their position](http://weblogs.mozillazine.org/roc/archives/2010/01/video_freedom_a.html) in terms of ideals: H.264 is an open industry standard but patent-encumbered and has licensing fees; Ogg Theora is open, not patent-encumbered, and free of licensing fees.


[Brian Crescimanno has written a fine argument](http://briancrescimanno.com/2010/03/17/dear-mozilla-please-dont-kill-html5-video/) that this is a situation where pragmatism should win out over idealism, and that Mozilla should include support for H.264 (in addition to Ogg Theora) in Firefox. As he points out, it’s not as though Mozilla has never before supported proprietary formats (e.g. GIF). But Crescimanno’s best point is that Mozilla’s support for Ogg Theora is doomed because it’s technically inferior to H.264:


> People and businesses are willing to embrace free software when it
> provides an equal or better product than the proprietary
> alternatives (see the success of Linux on the server). However,
> when free software doesn’t keep up with the best non-free
> products, people stay away (see the lack of success of Linux on
> the desktop). Simply put, there just aren’t that many people who
> share the same moral imperative as the Free Software Foundation;
> most of them just want it to work.


Put another way, “open and better” is a recipe for success; “open but worse” is a recipe for obscurity. Popular video publishing sites aren’t going to use Ogg Theora *instead of* H.264, and I think they’re very unlikely to support it *in addition to* H.264, either. Encoding and storage are expensive; supporting both would at least double those costs.


The practical effect of Mozilla’s current position will not be to drive adoption of Ogg Theora. What’s going to happen is that Safari, Chrome, and even IE9 users will be served HTML5 video, and Firefox users will get Flash. Publishers will support both HTML5 video (for Safari, Chrome, and IE9 users) alongside Flash (for browsers that don’t support HTML5 and H.264) because they already have the Flash video publishing infrastructure in place, and because Flash can be used to publish H.264-encoded video. Publishers don’t have to encode (and store) video twice; they can encode (and store) it once and serve it two different ways. The sites that are the most popular — YouTube being number one, obviously — would bear the most expense to support an additional encoding format. It isn’t going to happen.


So, even those using the latest version of Firefox will be treated like they’re using a legacy browser. Mozilla’s intransigence in the name of “openness” will result in Firefox users being served video using the *closed* Flash Player plugin, and behind the scenes the video is likely to be encoded using H.264 anyway.


There’s another factor that occurred to me recently: mobile computing. Apple, Google, and Microsoft all seem to view mobile computing as a top-level priority. H.264 video playback on mobile devices is aided by dedicated H.264 decoding hardware. That’s how the iPhone and iPods get such long battery life for video playback. I believe this is also true for Android devices, and will be true for Windows Phone 7 and Zunes. Relying on the CPU for video playback simply isn’t practical on mobile devices. There are no hardware decoding chips for Ogg Theora. If you want to send video to mobile devices, H.264 is the only practical encoding for the near future. (I think this explains why Microsoft is throwing its support behind H.264 rather than some proprietary video codec of its own — Microsoft knows a winning position when it sees one.) Ogg Theora may well be “good enough” for desktop computers, but it’s completely unacceptable for mobile devices.


Mozilla, as an organization, doesn’t seem to value mobile computing as a top priority. Yes, they have [mobile initiatives](http://www.mozilla.com/en-US/mobile/). But the only platform they have a mobile browser for is Nokia Maemo. All of you using a Nokia Maemo, please raise your hands. *Crickets*. Compare and contrast with WebKit, which I suspect will soon have more mobile than desktop users.


The needs of mobile computing are driving the adoption of H.264 HTML5 video more than anything else, but Mozilla doesn’t feel that pressure because it isn’t a mobile company. And at this point, “not a mobile company” is getting hard to distinguish from “not a relevant company”.2


---

1. Opera is on Mozilla’s side, supporting Ogg Theora instead of H.264, but Opera isn’t a major browser in my book. Feel free to include it in your book, though. ↩︎
2. Opera, on the other hand, is a major player in the mobile market. I think it’s safe to say that Opera is far more relevant in mobile computing than on the desktop. So it strikes me as odd that they aren’t on board with H.264. Perhaps (unlike Mozilla) they truly can’t afford the licensing fees. ↩︎



| **Previous:** | [An Ode to DiskWarrior, SuperDuper, and Dropbox](https://daringfireball.net/2010/03/ode_to_diskwarrior_superduper_dropbox) |
| **Next:** | [Hope You Enjoy the Smell of Napalm in the Morning](https://daringfireball.net/2010/03/napalm_in_the_morning) |


PreviousNext