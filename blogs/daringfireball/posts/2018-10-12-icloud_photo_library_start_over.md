---
title: "Sometimes It’s Better to Just Start Over With iCloud Photo Library Syncing"
date: 2018-10-12
url: https://daringfireball.net/2018/10/icloud_photo_library_start_over
slug: icloud_photo_library_start_over
word_count: 1285
---


Early this week I noticed that I wasn’t able to use the [Instant Hotspot feature](https://support.apple.com/en-us/HT204681#hotspot) with my iPhone XS. That’s the feature where you can leave the cellular hotspot turned off in Settings, but enable it on-the-fly from a Mac when you connect via the Wi-Fi menu. These “Personal Hotspots” show up at the top of the list of available Wi-Fi networks, in their own special section of the menu. My Wi-Fi menu no longer listed my iPhone, only my iPad. If I went into the iPhone’s Settings app and enabled the Personal Hotspot manually — i.e. turned it on and left it on — my iPhone’s hotspot was listed as a regular Wi-Fi network on my Mac, and when I connected, it worked just fine. So the hotspot worked, but the magic Instant Hotspot feature wasn’t working.


I tried rebooting the Mac and iPhone, of course. No dice. I reset network settings on the phone. No dice. I then noticed that my iPhone’s name (Settings → General → About → Name) had been changed to “iPhone”. Not even “John’s iPhone”, which is the default when you set up a new iPhone. Just plain “iPhone”. I changed it back to my custom name. Rebooted the phone again. Still no Instant Hotspot. And then eventually the device name was changed back to “iPhone” again. Weird, right? This was all on the release version of iOS 12.0.1, by the way.


I had a trip to New York coming up, and wanted to fix this. I did some searching on the web and eventually stumbled on a thread [that suggested signing out of iCloud and then signing back in](https://discussions.apple.com/thread/8556888). This makes some sense, because all of these [Continuity features](https://support.apple.com/en-us/HT204681) go through iCloud. So I did that on the iPhone, and, long story short, that seemed to fix the issue. After one more reboot of the phone, Instant Hotspot was working perfectly.


A side effect of signing out of and back into iCloud is that it seemed to reset my iPhone’s photo library sync state. It didn’t delete my photos, but once I was signed back in to iCloud, the Photos app was trying to re-upload my entire library (over 28,000 photos and 1,100 videos) back to iCloud. I don’t think it was actually *uploading* them — I think that’s just the word Photos uses to indicate what it’s doing — but rather checking each of the photos on the phone against each of the photos in my iCloud library.


It got through most of them fairly quickly, but the last 4,500 or so were effectively stuck. This process was proceeding really slowly. Profoundly slowly. I kept the phone plugged in last night and checked every hour, and it was only processing about 15 or 16 items per hour. I let it run overnight and it only moved from 4,183 remaining items to just over 4,000.


Effectively, I think what happens is that when you turn off iCloud Photo Library, it leaves all the photos and videos on your phone in your local library. When you turn iCloud Photo Library back on, it has no idea which of the items in your local iPhone library are duplicates of items in your iCloud library, and so it has to check them one by one. Whatever algorithm it’s using for this is slow as molasses.


[Adam Engst wrote about a similar problem](https://tidbits.com/2018/01/25/bad-apple-1-icloud-photo-library-re-uploading/) on the Mac earlier this year:


> I was seeing some strange problems on my 27-inch iMac running
> macOS 10.13.3 High Sierra. Messages wasn’t getting or sending
> messages, Wi-Fi calling wasn’t working, and after upgrading to
> 10.13.3, I was unable to enable auto-unlock with my Apple Watch.
> To solve these problems, I turned iCloud off and back on. Despite
> the iCloud preference pane throwing an ominous error, the problems
> did indeed disappear.
> However, there’s a nasty side effect of turning iCloud off and
> back on: iCloud Photo Library needs to re-upload all your photos.
> It does this in order to compare the library’s contents to the
> synchronization “truth” at iCloud. Fair enough, except that this
> process can take days, depending on the size of your Photos
> library and the speed of your Internet connection. Bad Apple! We
> don’t see that sort of poor performance with Dropbox or Google
> Drive, and this behavior is both unnecessary and driving people
> away from iCloud Photo Library.


That’s pretty much exactly what I was seeing on my iPhone.


What surprised me about this isn’t just that it’s so dreadfully slow, but that iCloud Photo Library has gotten amazingly good in the last few years. It’s not just very reliable, but very fast. I took a lot of photos using three different iPhones (my old iPhone X, and my review unit iPhones XS and XS Max) while writing [my XS review last month](https://daringfireball.net/2018/09/the_iphones_xs). And I worked on the review on two different Macs. Every photo and video I took on every iPhone synced to all the other devices in a matter of seconds every single time. iCloud Photo Library made the whole process ridiculously easy.


Wiping and restoring my entire iPhone seemed like overkill when the only issue I was having was photo syncing. So my next idea was to delete all the photos from my phone and start over from scratch with iCloud Photo Library.


So here’s what I did, and it seems to have worked. First, I eyeballed all the recent photos and videos I’d shot using my iPhone and double-checked that they had all already been synced to iCloud. They were — I could see all my recent shots on my other devices.


Next, I disabled iCloud Photo Library on my iPhone again. You do that by going into the Apple ID section of Settings (where your name is shown at the very top of the root level) → iCloud → Photos and turned off everything. When it asked if I wanted to download a copy of the photos and videos from my iCloud library I declined.


Next, I wanted to delete every single photo and video from my iPhone. To my knowledge there is no easy way to do this on the iPhone itself. (There are a lot of tasks like this that are easy on the Mac thanks to Edit → Select All that are painfully tedious on iOS. **Update:** Here’s a clever way [to use iOS 12’s Shortcuts app to delete all photos and videos from your Library](https://twitter.com/micahherstand/status/1051873159257960448).) I connected the iPhone to my Mac with a Lightning cable and used Image Capture to delete all photos and videos from my phone. Image Capture just treats the iPhone like a regular camera. Image Capture crashed three times during this process (I’m still running MacOS High Sierra 10.13.6, for what it’s worth), but after the fourth run the iPhone had no photos or videos left.


Then I re-enabled iCloud Photo Library on the phone, and about 20 minutes later, everything was back to normal. My iPhone reported exactly the same number of photos and videos in my library as on all my other devices. Most of those items are still [just placeholders](https://daringfireball.net/misc/2018/10/placeholders.png), even as I write this, but they’re filling in steadily — which is exactly how iCloud Photo Library works when you start syncing a large library to a new device.


So if you temporarily turn off iCloud Photo Library and turn it back on, it might be easier to just delete all your photos from your iPhone first, and let them all sync back from iCloud.



| **Previous:** | [Bloomberg’s ‘The Big Hack’](https://daringfireball.net/2018/10/bloomberg_the_big_hack) |
| **Next:** | [The iPhone XR](https://daringfireball.net/2018/10/the_iphone_xr) |


PreviousNext