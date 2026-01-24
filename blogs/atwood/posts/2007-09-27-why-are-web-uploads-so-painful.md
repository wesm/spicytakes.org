---
title: "Why Are Web Uploads So Painful?"
date: 2007-09-27
url: https://blog.codinghorror.com/why-are-web-uploads-so-painful/
slug: why-are-web-uploads-so-painful
word_count: 824
---

As video on the web becomes increasingly mainstream, I’ve been dabbling a bit with video sharing myself. But **I’ve found that publishing video content on the web is extraordinarily painful**, bordering on cruel and unusual punishment. The web upload process is a serious barrier to online video sharing, and here’s why:

1. **Video files are huge**
Video files are easily the largest files most users will ever create. Even at very modest resolutions and bitrates, the file size will be more than 10 megabytes for anything except the shortest of video clips. And high definition? Forget about it. That’s hundreds of megabytes.
2. **Limited upstream bandwidth**
Most people have highly asymmetric internet connections: massive download bandwidth, but the tiniest trickle of upload bandwidth. This trickle of upload has to be shared among all the applications competing for bandwidth. Uploading giant video files is challenging under the best of conditions, and most people’s internet connections are more like worst case scenarios for uploading.
3. **Uploads are precious**
Downloads are a dime a dozen. If a download fails, who cares? There are a hundred different sources to get any particular download from. Re-downloading is fast and easy. But uploads are different. If you’re uploading a video, it’s likely something you have somehow edited and invested time in. Maybe it’s a video you created yourself. You’re uploading it with the intent of sharing. If the upload fails, you won’t be able to share what you’ve created with anyone – so you care intensely about that upload. Uploads are far more precious than downloads, and should be treated with appropriate respect by the browser and the server.


Worst of all, **our existing browser and HTTP infrastructure is absolutely horrible at handling large file uploads**. I mean profoundly, abysmally bad.


Consider the upload form for Google Video. It does as little as it possibly can without actually being a vanilla HTML 4.01 form. Once I start an upload of my many-megabyte video file, there’s no feedback whatsoever about what’s happening. There’s only a generic animated GIF and an admonishment not to close the browser window. When will my upload be done? Could be 10 minutes; could be 10 hours. Who knows?


![](https://blog.codinghorror.com/content/images/2025/04/image-215.png)


The YouTube video upload page is slightly better; it uses a flash-based element to provide basic percentage-done feedback on the upload.


![](https://blog.codinghorror.com/content/images/2025/04/image-214.png)


Despite the spartan progress feedback, the YouTube upload page is hardly any better than the Google Video upload page. If I accidentally navigate away from the upload page – or much to my chagrin, if I click on that “having trouble” link – my upload is arbitrarily cancelled with no warning whatsoever. There’s no hope of resuming where I left off. I have to start over from scratch, which is *punishing* when you’re dealing with a large video file and a typical trickle-upload internet connection.


If Google Video and YouTube represent the state of the art for web-based video uploads, that’s an embarrassment.


I can’t find *any* video sharing sites that do uploads well. **Large file upload seems to be a textbook case for the advantages of desktop applications over even the most modern of web applications.** The Google Video page actually recommends using their desktop uploader for video files over 100 megabytes in size. Based on my abysmal user experience to date, I’m inclined to use a desktop uploader for any video file over *10* megabytes.


Large file uploads are an inhospitable wasteland on today’s web. But what really drives me crazy is that *it doesn’t have to be this bad*. Our web browsers are failing us. **Current web browsers treat downloads as first-class citizens, but uploads don’t even rate third-class treatment.** Internet Explorer provides a nice enough download user interface:


![](https://blog.codinghorror.com/content/images/2025/04/image-213.png)


Like so much about IE, this download dialog has barely changed since 1999. Firefox has an improved download dialog that handles multiple simultaneous downloads.


![](https://blog.codinghorror.com/content/images/2025/04/image-212.png)


**Why can’t browsers, at the very least, provide the same level of feedback about uploads as they do about downloads?** The browser surely knows the size of the file I just told it to upload, and it’s responsible for streaming those bytes to the server, so it should also be able to tell me when the upload will finish. Longer term, I’d like to see support for resumable uploads, just like today’s browsers can resume HTTP downloads in some select scenarios.


It’s clear to me that large file uploads will become increasingly prevalent on the web as video trickles down to the mainstream. **Uploads are not the freakish edge conditions they might have been in 2001.** I hope future browsers can extend the same great support they have for file downloads to file uploads. But that doesn’t help us today. Perhaps more sophisticated browser plugin environments – such as [Silverlight](https://web.archive.org/web/20070809011406/http://silverlight.net/) and AIR – can enable a better user experience for these large file uploads, sooner rather than later.

[video upload](https://blog.codinghorror.com/tag/video-upload/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[bandwidth](https://blog.codinghorror.com/tag/bandwidth/)
[file size](https://blog.codinghorror.com/tag/file-size/)
[internet connectivity](https://blog.codinghorror.com/tag/internet-connectivity/)
