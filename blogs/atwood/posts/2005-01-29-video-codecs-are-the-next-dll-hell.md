---
title: "Video Codecs are the next DLL Hell"
date: 2005-01-29
url: https://blog.codinghorror.com/video-codecs-are-the-next-dll-hell/
slug: video-codecs-are-the-next-dll-hell
word_count: 1116
---

This issue needs more attention. Via [Steve Makofsky](https://web.archive.org/web/20050830020309/http://www.furrygoat.com/2005/01/are_codecs_the_.html):


> ***Codecs are the next DLL hell**. While I love *[*Nero Digital’s simplicity and quality*](https://blog.codinghorror.com/dvd-ripping-and-nero-recode/)*, the MP4s it produces aren’t compatible with most commercial DVD players (due to the AAC or AVC audio). I’ve tried Dr. Divx – I get audio that isn’t in sync with the video. Heck, even the camcorder video I saved the other night as an MPEG had some sort of audio codec problem. The most surprising? Some Windows Media (WMV) files that I’ve created in Adobe Premiere have had problems showing on my dad’s machine. I suspect he has a codec problem of sorts. Codecs are the next DLL hell. While I love Nero Digital’s simplicity and quality, the MP4s it produces aren’t compatible with most commercial DVD players (due to the AAC or AVC audio). I’ve tried Dr. Divx - I get audio that isn’t in sync with the video. Heck, even the camcorder video I saved the other night as an MPEG had some sort of audio codec problem. The most surprising? Some Windows Media (WMV) files that I’ve created in Adobe Premiere have had problems showing on my dad’s machine. I suspect he has a codec problem of sorts.*


Via [Chris Lanier](https://web.archive.org/web/20051208122423/http://msmvps.com/chrisl/archive/2005/01/27/34039.aspx):


> *Another big issue is that these companies want their codecs to decode everything. Not only does the DivX codec from DivXNetworks decode DivX, but will also do XviD and 3ivX decoding. The 3ivX Suite decodes 3ivX, XviD, and DivX. So you get people installing DivX, XviD and 3ivX because they all have different names, and all the decoders can basically do the same thing (which is not always true; decode quality can be very different). Nero and EZ CD Creator also ship with MPEG-4 decoders that will generally decode XviD and DivX. **Are you counting how many things on the system can decode the same content? It’s too many!**
> Microsoft has always been slow to correctly address these problems, and they really are problems. They can’t address or fix people on the Internet being dumb and offering packs of pirated and hacked codecs but **I would say a good 60-70% of the problems people have with Windows Media Player are due to codecs. People have issues with Windows Media Center Edition and codecs all the time.** The main problem is that a large pool of [uncoordinated] companies are [doing this]. Microsoft should take a stand and do a good job of educating people on what codecs are, what they do, how to find out what codec is used in a file, and where to download the correct codec.*


It’s an embarrassment that Windows Media Center [in its Windows XP incarnation] is totally dependent on a valid MPEG-2 codec – *it literally cannot function at all without one* – and yet does not ship with one in the box. On Chris’ site, there’s a response from Microsoft’s Ted Youmans that lists the reason I’ve always suspected: licensing costs.


> ***The problem with shipping an mpeg2 codec in the box is the royalties.** When MS includes something it goes out in every copy whether the user will use it or not. Including the codecs would dramatically increase the price of windows to OEMs. These same OEMs already have deals with IHV’s to include their mpeg2 decoders and use it as an upsell to customers.
> Note that a DV codec is almost synonymous with an mpeg2 codec.
> I can’t say what MS will or won’t do in the future, but it isn’t quite as simple as just including them.
> As to the original post: It’s a very difficult problem to solve. DShow was based on the merit system (pun intended) with the idea being that using a combination of the filter’s merit and how specific the media type/sub type is one could reasonably pick the right codec every time. It wasn’t really designed for a competing merit nuclear arms race.
> Now you can solve it on an application level easy enough, just specify the filter you want and ignore the merit. But how to generically solve it, where any application will always get the “right” filter is quite a bit more complex. The question becomes how do you know what the right filter is? You can’t programmatically tell if one has better decode quality than another. Heck, people can’t even subjectively agree on what is best.
> Test solution 1: within the current framework each user can choose what they want their “default” one to be and raise its merit all the way. If individuals do it, then there is no arms race, but if MS provides a mechanism for you to do it you will suddenly see every new codec with its merit set at the max, and it will all be useless again. So now we need to provide a way to lower the merit of other “unwanted filters,” easy enough but now the system is just as complex as it is today.
> Test solution 2: Teach each app writer how to select their own filter and ignore the merit. This way they don’t need to register high, they will get what they want anyway. The problem is this is extra work and they can just get this for “free” by raising their merit. Development time is money. Aside from that there are the generic applications (like MCE) which need to rely on someone else’s codec and they don’t have the luxury of specifying their own unless they present you with a list and ask you to choose.
> I really don’t have any answers for you. What I can tell you is that we are (and have been for quite some time) aware of the problem. It is one of our main concerns while designing the next generation of multimedia API’s.*


The parallels with DLL Hell are eerily accurate.


I think Ted’s response is a copout. Cost? What about the “hidden” cost of all the thousands of codec problem posts on [The Green Button forums](https://web.archive.org/web/20050405225945/http://www.thegreenbutton.com/community/messages.aspx?ForumID=38)? **Microsoft needs to provide a default MPEG-2 implementation in the MCE box.** Yeah, the OEMs may get pissed, but so what? Which is more important: the Microsoft software customer, or some faceless OEM? At some point Microsoft has to take a clear stand for the customer. Nobody else in this random collection of companies has the authority to make that kind of binding decision in the customer’s favor.


OEMs will do what is best for them, not for us. Microsoft is the only consumer advocate that can help. If they abdicate their responsibility here, all Microsoft customers lose.

[codec](https://blog.codinghorror.com/tag/codec/)
[dll hell](https://blog.codinghorror.com/tag/dll-hell/)
[video codecs](https://blog.codinghorror.com/tag/video-codecs/)
[compatibility](https://blog.codinghorror.com/tag/compatibility/)
[audio codec](https://blog.codinghorror.com/tag/audio-codec/)
