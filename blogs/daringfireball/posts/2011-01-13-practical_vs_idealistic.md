---
title: "The Practical vs. Idealistic Scenarios for the Near-Term Future of Online Video"
date: 2011-01-13
url: https://daringfireball.net/2011/01/practical_vs_idealistic
slug: practical_vs_idealistic
word_count: 1464
---


## Or: How Google’s decision to drop native H.264 playback from Chrome serves to prop up Flash Player


Stefan Richter, of FlashComGuru (a Flash developer site) [tries answering my five simple questions](http://www.flashcomguru.com/index.cfm/2011/1/12/answers-for-john-gruber). I don’t think his answers are very good, but I encourage you to judge for yourself. For example:


> 3: YouTube uses H.264 to encode video. Presumably, YouTube will
> be re-encoding its entire library using WebM. When this happens,
> will YouTube’s support for H.264 be dropped, to ‘enable open
> innovation’? If not, why not?
> A. It won’t matter either way. I have a feeling that YouTube will
>    ensure that their videos can be played back. Did things break
>    when YouTube transitioned to H.264? Actually, transitioning is
>    the wrong term here. Contrary to popular belief there was never
>    such a thing as a ‘Flash video codec’. Flash has supported
>    H.264 for years, alongside other codecs. Adding WebM to the mix
>    is a formality now.


“It won’t matter either way?” If YouTube drops H.264 and goes WebM-only, YouTube will cease to work on any device or software that doesn’t support WebM. This includes Safari and Internet Explorer. Now, perhaps in those cases, by the time this hypothetical dropping of H.264 from YouTube occurs, there will be a new version of Flash Player that supports WebM; thus allowing Safari and IE users to continue using YouTube through Flash and only through Flash. Sounds great.


But what about devices that don’t support Flash? No more YouTube for iOS devices, including Apple TV. Or for Windows Phone 7. Perhaps Richter’s take on that is along the lines of “*Tough noogies for Apple and iOS users — that’s what you get for not supporting Flash.*” Fair enough. But that seems a decidedly Flash-centric stance to me.


The bit at the end of Richter’s answer about Flash Player codecs is unrelated to my question. It is true that many people are confused about Flash Player’s relationship with video codecs. John Nack’s piece from March, “[H.264 Isn’t an Alternative to Flash](http://blogs.adobe.com/jnack/2010/03/h264_isnt_an_alternative_to_flash.html)”, offers a good primer. In short, one way to play H.264 video is through Flash Player; another way is through the HTML5 `<video>` element.


My fourth question did pertain to Flash, however. Richter answers:


> Q 4: Do you expect companies like Netflix, Amazon, Vimeo, Major
>    League Baseball, and anyone else who currently streams H.264 to
>    dual-encode all of their video using WebM? If not, how will
>    Chrome users watch this content other than by resorting to
>    Flash Player’s support for H.264 playback?
> A: Maybe like so: Chrome user navigates to video page. Site
>    detects Chrome. Chrome plays video using Flash which is bundled
>    into Chrome, using an H.264 or WebM version of the content,
>    whichever is available. User is happy. What am I missing here?
>    Is there something inherently wrong with playing a video in
>    Flash?


I asked how Chrome users will play video from these services other than via Flash, and Richter’s answer is “What’s wrong with Flash?” That’s not an answer.


Let me be clear, though: there is nothing wrong with playing a video in Flash. I mean that seriously, no sarcasm. What there’s something wrong with is *requiring* Flash Player to play video. That’s the whole point of the HTML5 `<video>` element: to enable web video without requiring the use of proprietary plugins.


If depending upon Flash Player for video playback is fine, then why doesn’t Chrome just drop support for HTML5 video entirely? I think it’s fair to say that the point of Chrome supporting WebM-encoded video via HTML5 is that Google expects Chrome users to actually be served WebM-encoded video via HTML5.


I think proponents of Google’s decision to drop H.264 support in Chrome imagine the following scenario:

1. Major online video providers (Netflix, Amazon, Vimeo, Major League Baseball, etc.) see that Firefox and Chrome support WebM but not H.264 via HTML5.
2. They decide to dual-encode their content libraries in H.264 and WebM. They send H.264 to clients that support only H.264, and WebM to clients that support only WebM.
3. Eventually, perhaps, the forces of good and openness prevail, and these companies drop support for H.264 entirely in favor of WebM, despite the fact that WebM [is a technically inferior encoding format](http://carlodaffara.conecta.it/?p=420).


Let’s call this the idealistic scenario. I think this is what Mozilla and Opera have been expecting all along. So far, it hasn’t happened. Will Chrome joining them make a difference? One thing Google can bring to the table that Mozilla cannot is content: YouTube. But I’m not asking about YouTube. I’m asking about every other major provider of online video.


Keep in mind that in this idealistic scenario, providers would be doubling their storage and encoding costs, by supporting both H.264 and WebM. The only way they could avoid doubling these costs would be by dropping support for H.264, which would mean dropping support for all clients that only support H.264. This scenario also assumes that the legal teams at these providers are confident in WebM’s patent status. This is not an insignificant assumption.


Here, on the other hand, is the scenario I foresee:

1. Major online video providers (Netflix, Amazon, Vimeo, Major League Baseball, etc.) already have invested in H.264, both technically and legally.
2. These providers, right now, today, send H.264-encoded video in one of two ways: directly, to clients with native H.264 playback; and wrapped in Flash, for web browsers with Flash Player installed.
3. Chrome drops support for H.264 and these simply send Chrome users H.264-encoded video via Flash.
4. These services continue to ignore devices and clients that support neither straight H.264 nor Flash Player (e.g. Firefox running on Ubuntu).


Let’s call this the practical scenario. In this scenario, the providers incur no additional storage or encoding costs. They take on no additional legal liability. They don’t really have to do any additional work.


Here’s [what Marco Arment wrote about Mozilla’s HTML5 codec stance](http://www.marco.org/136785976), 18 months ago:


> By not supporting the practical [H.264] format, Mozilla isn’t
> making a brave statement or taking a stand: they’re just keeping
> everyone on Flash and preventing meaningful adoption of HTML5’s
> `<video>` element.


The last 18 months have proven him right, thus far. A few things have changed since then. The “free and open” format preferred by H.264 opponents has changed from Ogg Theora to WebM, thanks to Google. This is truly a good thing, because WebM is a technically superior format. (Technically superior to Ogg Theora, that is — not H.264.) But technical inferiority wasn’t the only factor, or even the leading factor, holding Ogg Theora back.


I have nothing against WebM. In fact, prior to this week’s announcement, I thought Chrome had the best HTML5 video policy of any browser: they supported *all* the relevant codecs. Supporting WebM *and* H.264 is better than supporting only one or the other, in my book. But if you’re only going to support one, I say support the one that is in wide use, with extensive wide-ranging support from camera makers, mobile playback devices, and online video services.


I don’t think these H.264 opponents have any idea how to drive adoption of new technology. Apple was able to motivate companies to deliver non-Flash H.264-encoded video by making devices like the iPhone, iPad, and iPod Touch which had the following qualities:

1. The devices are very popular. There is a large lucrative audience of people who own them and want to watch video from companies like Netflix, Vimeo, and Major League Baseball.
2. The devices offer excellent support for H.264. Smooth playback and low power consumption.
3. There is no other way to send video to these devices.


That third point is key. Some of these companies took on a lot of work in order to serve video to iOS devices, because their existing systems were based entirely on Flash Player. But because Flash Player is not available on iOS, this was still *the least possible work they could do* — other than not supporting iOS devices at all.


The least amount of work these companies can do now, to continue serving video to Chrome users, is to keep using H.264-encoded video via Flash Player. There is no sign that any of these companies share the idealistic concerns of H.264 opponents, and every sign that they’re satisfied with H.264’s technical merits and legal status.


Thus, dropping native H.264 playback from Chrome while still allowing H.264 playback via Flash Player isn’t going to drive adoption of WebM. It just means that Chrome users will get H.264 via Flash.



| **Previous:** | [Simple Questions for Google Regarding Chrome’s Dropping of H.264](https://daringfireball.net/2011/01/simple_questions) |
| **Next:** | [Too Late](https://daringfireball.net/2011/01/lyons_too_late) |


PreviousNext