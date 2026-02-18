---
title: "Why the HTML5 ‘Video’ Element Is Effectively Unusable, Even in Browsers Which Support It"
date: 2009-12-21
url: https://daringfireball.net/2009/12/html5_video_unusable
slug: html5_video_unusable
word_count: 1589
---


[**Update, 22 Dec 2009:** In the original version of this article, I incorrectly reported that Firefox auto-buffers HTML5 video content by default, as Safari and Chrome do. It does not, as shown by [Christopher Blizzard’s simple tests here](http://hacks.mozilla.org/2009/12/autobuffering-video-in-firefox/). I regret the error, and have revised the article accordingly. For posterity, the [source for the original version is preserved here](https://daringfireball.net/misc/2009/12/html5_video_unusable.original.text). You can create a precise list of changes by doing a diff against the [source for the current revision](https://daringfireball.net/2009/12/html5_video_unusable.text).]


I seldom post video to DF, but when I do, I refuse to embed Flash,1 I want the markup to be sane and standard, I want the video to play in popular standards-compliant web browsers, and I don’t want the video to download/buffer automatically. [Here’s an example from a year ago](http://daringfireball.net/2008/04/big_fan), using QuickTime.


What you see upon page load is a poster frame (a still image), then you (the user) click the poster frame to actually download and watch the video. Here’s the markup I used then:


```
<embed
   width="320" height="256"
   type="video/quicktime"
   pluginspage="http://www.apple.com/quicktime/download/"
   src="dtk-panic-1-poster.jpg"
   href="dtk-panic-1.mov"
   target="myself"
   controller="false"
   autoplay="false"
   scale="aspect"
/>

```


That markup met all of my aforementioned desires but for one: the `<embed>` tag is not standard. Worse, it now has a new significant problem: it doesn’t work at all in Chrome (at least on the Mac).


So I’ve been [paying attention](http://daringfireball.net/2009/07/ffmpeg2theora) to the new [`<video>` element in HTML5](http://html5doctor.com/the-video-element/). In a nut, it attempts to make embedding a video in a web page just as easy markup-wise as embedding an image with the `<img>` tag. (Likewise for audio with the new `<audio>` element.)


The obvious downside to relying solely on the `<video>` element to embed web video is that because it’s new, the only browsers that support it are recent releases of Safari, Firefox, and Chrome. This isn’t one of those things that just doesn’t work in IE6 or IE7 — it doesn’t work in IE *period*. Therefore few sites are using HTML5 video in production now, and of those, nearly all are doing so with [fallback markup](http://henriksjokvist.net/archive/2009/2/using-the-html5-video-tag-with-a-flash-fallback), often of [significant complexity](http://camendesign.com/code/video_for_everybody), that presents the video using a Flash player for other browsers. Because (a) I don’t post much video; (b) the overwhelming majority of DF’s audience is in fact using an HTML5-compatible version of Safari, Firefox, or Chrome;2 and (c) I’m willing to [be a dick](http://daringfireball.net/linked/2009/06/30/ff5) about this; I do not care about fallbacks for browsers that don’t support `<video>`.


What I’d like to do is just use `<video>`, with two source elements — MP4 and OGV — for all the cross-browser reasons specified in [Mark Pilgrim’s fine chapter on video](http://diveintohtml5.org/video.html) in his in-progress HTML5 book. (Short version: Safari and MobileSafari support only MP4, Firefox supports only OGV, Chrome supports both MP4 and OGV.)3


So I decided to try this last week with [the screencast videos](http://daringfireball.net/misc/2009/12/user_guide_demos) I created to illustrate my [piece on PastryKit](http://daringfireball.net/2009/12/pastrykit). I tried markup like this:


```
<video height="475"  width="407"  controls  poster="iphoneguide-mac.png">
   <source src="iphoneguide-mac.mp4" type="video/mp4" />
   <source src="iphoneguide-mac.ogv" type="video/ogg" />
</video>

```


**The good news:** The above markup results in video that plays in Safari, Chrome, and Firefox. It also works perfectly in MobileSafari on iPhone OS. Safari and Chrome play the MP4 video, Firefox plays the OGV. (Chrome supports both formats, and plays the one listed first. I want it to play the MP4 version because the video and audio are of noticeably superior quality.) That is the entirety of the necessary markup; if you’re unfamiliar with the sort of nasty markup typically used to embed video, try a little View Source on a few web pages that embed video.


**The bad news:** In two of the three browsers (Safari 4.0.4 and Chrome 4.0.249.43), with the above simple markup, the video content buffers automatically on page load. What I mean is that as soon as you load the web page, the browsers download the actual video files that are embedded. As stated at the outset, I don’t want that. Instead, on page load, I want the browser to render only the *poster* image, and load the video only after the user has clicked to initiate playback.


The HTML5 spec defines an [`autobuffer` attribute for the video and other media elements](http://www.whatwg.org/specs/web-apps/current-work/#attr-media-autobuffer) (bold emphasis added):


> The `autobuffer` attribute is a boolean attribute. Its presence
> hints to the user agent that the author believes that the media
> element will likely be used, even though the element does not have
> an `autoplay` attribute. (The attribute has no effect if used in
> conjunction with the `autoplay` attribute, though including both
> is not an error.) **This attribute may be ignored altogether.**


Firefox honors the `autobuffer` attribute. Omit the attribute from your markup, and video content will not auto-buffer in Firefox. Include it, and it will.


But alas, in my testing, Safari and Chrome take the spec up on the aforebolded offer to ignore this attribute. Even if you do not explicitly turn this attribute on, Safari and Chrome will still auto-buffer the content for your `<video>` (and `<audio>`) elements. There is no way to suppress this using HTML markup.


You might be thinking, “*Hey, but default auto-buffering sounds like a good feature, because that way users won’t have to wait as long for the video to be ready to play.*” I presume this sort of thinking is what led the Safari and Chrome teams to do this.


But this browser behavior is very much undesirable for both publishers and users in common contexts. Users loading the page over a slow connection, or a pay-by-the-megabyte metered connection (which is common with wireless networks), should not be forced to download a potentially large video every time they load the page. Likewise, publishers should not be forced to pay for the bandwidth to transmit videos that won’t be watched.


Think, in particular, of the nature of publishing embedded video on a weblog. I, the publisher, post an entry containing embedded video. That post may remain on my home page for a week. Regular readers may load the home page dozens of times during the period when the video appears on the page. With auto-buffering, they’re going to download the full video every time they load the page. Local caching may alleviate some of that, but for sites with high traffic and/or which frequently embed video, the difference is enormous.


This is why embedded video from YouTube, Vimeo, and all similar services works on a click-to-load basis. Auto-buffering is fine *as an optional attribute*, but for many (probably most) contexts, click-to-load is essential behavior.


But as far as I can see, there’s no way to get click-to-load video in Safari or Chrome using just a `<video>` element. The only workaround I could think of was to do something like this:

1. In the HTML markup, rather than a `<video>` element, instead use an `<img>` element with the intended poster frame.
2. Add an `onclick` JavaScript handler to the `<img>` element, which, when invoked, does some DOM jiggery-pokery to remove the just-clicked-upon `<img>` element and replace it with a `<video>` element that sources the intended video files.


And, in fact, that is exactly what I resorted to for my PastryKit videos. Do a View Source on [that page](http://daringfireball.net/misc/2009/12/user_guide_demos) to see the solution. There goes the nice clean just-as-easy-to-include-a-video-as-an-image markup. (My sincere thanks to [Faruk Ateş](http://farukat.es/) and [Paul Irish](http://paulirish.com/) for helping with the jiggery-pokery implementation.)


[This WebKit bug](https://bugs.webkit.org/show_bug.cgi?id=25267) filed back in April indicates I’m not the first person to stumble on this shortcoming. That’s about `<audio>` instead of `<video>`, but the principle is exactly the same. And the example cited in this bug report seems like a perfect scenario where everyone should agree that media content should not buffer automatically: a podcast archive page with an `<audio>` element for every previous episode.


A big part of the appeal of the `<video>` and `<audio>` elements is that they should be easier to use. As it stands today, though, these elements are unusable in popular contexts without resorting to JavaScript DOM manipulation to effectively turn auto-buffering off.


I think the HTML5 spec should be changed such that the value of the `autobuffer` attribute must be respected. And even if the spec is not changed, web browsers should not choose to ignore it. Web browsers should only buffer HTML5 media content when the `autobuffer` or `autoplay` attribute has been explicitly turned on in the markup.


---

1. As for why I refuse to embed Flash, let me put it this way. I use and highly recommend ClickToFlash, which blocks all Flash content by default. Why would I publish content using a technology that I personally block by default? I truly hope to see Flash fade as the de facto standard for embedded web video, and I’m willing to put my markup where my mouth is. ↩︎
2. As of this writing, Daring Fireball [gets about twice as many page views from MobileSafari](http://twitter.com/daringfireball/status/6812496176) as all versions of Internet Explorer combined on a typical weekday. ↩︎
3. Having to include separate source elements of the same video content encoded in two different formats is indeed an inconvenience. Not so much the extra markup as the extra work producing and encoding the second video file. Even the short videos I created to illustrate my PastryKit piece took a few minutes each to encode. Relative to most computing tasks today, encoding video once is already painfully slow. Encoding it twice is a time sink no one needs. But that’s the way it stands. ↩︎



| **Previous:** | [More on PastryKit](https://daringfireball.net/2009/12/more_on_pastrykit) |
| **Next:** | [The Tablet](https://daringfireball.net/2009/12/the_tablet) |


PreviousNext