---
title: "Anti-Bootlegging Measures and the iPhone App Store"
date: 2009-02-11
url: https://daringfireball.net/2009/02/anti_bootlegging_app_store
slug: anti_bootlegging_app_store
word_count: 948
---


[Marco Arment](http://tumblelog.marco.org/75389335), responding to my expectation that iPhone developers are set to begin implementing their own anti-bootlegging measures:


> The ideal piracy detection system doesn’t make it immediately
> obvious to the crackers that their efforts have been detected.
> That way, they believe their crack is sufficient, release it, and
> move on to another app.
> If your app interacts with a web service, you can then do all
> sorts of interesting things. For example, you can log the unique
> iPhone IDs that run pirated copies of your app and blacklist them
> from future updates. Or you could quit the app on launch, but only
> after it has been installed for a few days. You could even create
> a database of pirating iPhone IDs and share it with other
> developers.


The idea of anti-piracy measures which only kick in after the app has been in use for a certain amount of time is clever. But, it’d be a bad idea to just quit at launch without explanation when the protection kicks in — the user, though a bootlegger, would be left with the impression that your app is faulty, unstable, and/or downright junky. You’re probably not going to convert them to a sale, but they also might start spreading the word that your app crashes randomly after a few days of use.


Better to make it explicit to the user what is happening. Pop up an alert that politely asks them to consider buying a legit copy. It probably won’t convert a high percentage of bootleggers to honest customers, but at least they’ll know that the app didn’t *crash*.


Panic did some experimentation with this a little over a year ago, when they released CandyBar 3.1 They have a phone-home system for serial numbers — not for any sort of Adobe- or Microsoft-style “activation” scheme, but simply to check whether a serial number is valid or known to be circulating on bootleg message boards and forums. They experimented with different dialog boxes that appeared when a user entered a known-to-be-pirated serial number. One message was staid and serious (“Microsoft-style”, in Cabel Sasser’s words), along the lines of “*It appears someone gave you an invalid serial number…*”; the other two messages were more personal, along the lines of “*Please don’t pirate CandyBar. We’re a small company making software for you, and software sales are what keep our company going.*”


They got better results with the more personal messages — about 10 percent of would be bootleggers presented with those dialogs clicked the button and immediately bought a legitimate license for the app. But even the staid, impersonal message had a 5 percent sell-through rate — far higher than Panic expected.


The benefit of Apple’s FairPlay protection for App Store apps is that individual developers don’t need to spend time working on their own protection schemes. But the problem is that the current protection scheme is universal and uniform — every licensed app from the App Store is FairPlay-protected in the same way. So when bootleggers found a way to crack one App Store app, they found a way to crack *every* App Store app. iPhone apps are easier to bootleg systematically than Mac apps because every single iPhone app is protected the same way. I think an iPhone developer who added the most rudimentary custom protection scheme would significantly cut down on casual piracy, insofar as the automated FairPlay-stripping tools would no longer suffice to create a working crack. Mac apps get cracked, yes, but some clever cracker has to take the time to crack each one individually.


For people with jailbroken phones and awareness of Appulo.us, it’s like a return to the old days of true “shareware”, where you can download a working copy of the software and the only impetus to pay for it is a sense of honesty. There’s a mountain of evidence that shows that this doesn’t work.


Some iPhone developers have a good sense of how rampant App Store bootlegging is, because their apps have some sort of web service or phone-home integration. (E.g. apps which sync data to a web server, or games that report scores to a global high score list.) I spoke to a developer who works on a best-selling iPhone game (who asked not to be identified because he didn’t have permission from his employer to reveal this information). The game in question attempts to identify when it’s running as a bootleg copy, and when it does, pings the company’s web server. According to my source, roughly two out of three users of the game are running bootleg copies.


Arment ends his advice with this:


> Or you could just ignore the pirates, since hardly anyone
> jailbreaks their phone and they’ll never pay for anything anyway,
> and spend that time making the app better to attract more paying
> customers.


I strongly suspect games are bootlegged more often than other types of iPhone software, for obvious reasons, but numbers like those from my source are simply out of whack. And they also suggest that far more than “hardly anyone” jailbreaks their iPhone.


I’m not endorsing the idea of iPhone developers writing code that simply refuses to run on any jailbroken device, but I can see the appeal of it. Not all jailbreakers are bootleggers, but all bootleggers are jailbreakers.


---

1. See [episode #15 of The Talk Show](http://thetalkshow.net/#15), an interview I conducted with Panic co-founders Cabel Sasser and Steven Frank at Macworld Expo 2008. The relevant bit starts around the 46:00 mark. ↩︎



| **Previous:** | [Apple, Google, and Palm](https://daringfireball.net/2009/02/apple_google_palm) |
| **Next:** | [Copying the Wrong Thing](https://daringfireball.net/2009/02/copying_the_wrong_thing) |


PreviousNext