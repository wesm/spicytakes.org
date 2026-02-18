---
title: "Things That Podcaster’s Rejection From the App Store Is Not About"
date: 2008-09-15
url: https://daringfireball.net/2008/09/podcasters_rejection
slug: podcasters_rejection
word_count: 559
---


Daniel Dilger has [a piece on Roughly Drafted today](http://www.roughlydrafted.com/2008/09/15/sdk-333-the-iphone-podcaster-surprise-myth/) arguing that Apple’s rejection of Podcaster from the App Store should not have been a surprise, and in fact should have been expected under section 3.3.3 of the iPhone SDK Agreement.


This is such bullshit it hurts my head.


Dilger quotes from section 3.3.3 of the iPhone SDK Agreement. It reads:


> 3.3.3 — Without Apple’s prior written approval, an Application may
> not provide, unlock or enable additional features or functionality
> through distribution mechanisms other than the iTunes Store.


This section of the agreement is clearly not about *content* distribution. It’s about *application* distribution. It’s a way of saying that you can’t distribute your app through the App Store as a free demo and then charge to unlock the full version using a non-iTunes service such as PayPal or Kagi.  Podcast downloads are neither “additional features” nor “functionality”.


And if this guideline *did* mean that audio content can only be distributed through iTunes, it would rule out a slew of apps that are in the App Store already. [AOL Radio](http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=281913144&mt=8) and [Pandora](http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewSoftware?id=284035177&mt=8) both stream music and other audio over the network, directly to your iPhone. File storage/viewer apps such as [FileMagnet](http://www.magnetismstudios.com/filemagnet/) and (today’s [aforelinked](http://daringfireball.net/linked/2008/09/15/air-sharing)) [Air Sharing](http://www.avatron.com/products/) let you transfer audio and video files to and from your iPhone, and offer playback on the iPhone.


Via email and in comments elsewhere on the web, I’ve also seen it argued that Podcaster was rejected out of cell network bandwidth concerns. No way. First, it’s not the reason Apple gave Podcaster developer Alex Sokirynsky. Second, if it were the reason, Apple could have simply asked Sokirynsky to restrict Podcaster to Wi-Fi only. It is trivial for an iPhone application to restrict itself to Wi-Fi only or to behave differently when using the cell network. (For example, the guidelines expressly prohibit VOIP features, but *only* over the cell network.)


But even that doesn’t hold up. Apple’s own YouTube app will download as much video as you want over the cell network. So does the MLB At Bat app. Yes, both YouTube and MLB At Bat request lower-quality video over the cell network than they do over Wi-Fi, but it’s still video. And the AOL and Pandora apps stream audio non-stop over the cell network.


Podcaster, so far as I can tell, complies with every written guideline in the SDK Agreement. If other guidelines exist, Apple should add them to the agreement. It doesn’t even make sense from a *thou shalt not hurt Apple’s music revenue stream* standpoint. Podcaster is different than, say, a hypothetical *buy and download music over the air* iPhone client for Amazon’s Music Store. (I’d argue that Apple should allow that, but at least if they didn’t, there’d be a clear financial impetus behind the decision.) But Podcaster allows over-the-air downloading of *free* content. It makes no sense.


The point is not that Apple *can’t* reject apps arbitrarily. They can. Elsewhere in the SDK Agreement is a more or less wildcard clause that grants Apple the right to reject apps — and remove apps which were previously accepted — for whatever reasons it chooses. The point isn’t about what Apple *can* do but what they *should* do.


And they shouldn’t be doing this.



| **Previous:** | [The App Store’s Exclusionary Policies](https://daringfireball.net/2008/09/app_store_exclusion) |
| **Next:** | [W/r/t DFW](https://daringfireball.net/2008/09/wrt_dfw) |


PreviousNext