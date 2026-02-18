---
title: "How ‘Unlock With Apple Watch’ While Wearing a Face Mask Works in iOS 14.5"
date: 2021-02-21
url: https://daringfireball.net/2021/02/unlock_with_apple_watch_with_face_mask
slug: unlock_with_apple_watch_with_face_mask
word_count: 1440
---


I don’t generally write about features in beta versions of iOS. In fact, I don’t generally install beta versions of iOS, at least on my main iPhone. But the new “Unlock With Apple Watch” feature, which kicks in when you’re wearing a face mask, was too tempting to resist.


First things first: to use this feature, you need to install iOS 14.5 on your iPhone and WatchOS 7.4 on your Apple Watch (both of which are, at this writing, on their second developer betas). So far, for me, these OS releases have been utterly reliable. Your mileage may vary, and running a beta OS on your daily-carry devices is always at your own risk. But I think the later we go in OS release cycles, the more stable the betas tend to be. Over the summer, between WWDC and the September (or October) new iPhone event, iOS releases can be buggy as hell. The x.1 releases are usually the stable ones, and the releases after that tend to be very stable in beta — Apple uses these releases to fix bugs and to add new features that are stable. If anything, I think iOS 14.5 is very stable technically, and only volatile *politically*, with the new opt-in requirement for targeted ad user tracking.


After using this feature for a few weeks now, I can’t see going back. As the designated errand runner in our quarantined family, it’s a game changer. Prior to iOS 14.5, using a Face ID iPhone while wearing a face mask sucked. Every single time you unlocked your phone, you needed to enter the passcode/passphrase. The longer your passcode, the more secure it is (of course), but the more annoying it is to enter incessantly.


“Unlock With Apple Watch” eliminates almost all of that annoyance. It’s that good. It’s optional (as it should be), and off by default (also as it should be, for reasons explained below). It’s easy to turn on in Settings on your iPhone: go to Face ID & Passcode, enter your passcode, and scroll down to the “Unlock With Apple Watch” section, where you’ll find toggles for each Apple Watch (running WatchOS 7.4 or later) paired with your iPhone.


Here is how the feature seems to work.

1. Does Face ID work normally? I.e. is the face in front of the phone *you*, the owner, and are you not wearing a mask? If so, unlock normally. Normal non-mask Face ID is unchanged when this feature is enabled.
2. If Face ID fails, is there a face wearing a mask in front of the phone? If so, is an authorized Apple Watch in a secure state (i.e. the watch itself is unlocked and on your wrist) and *very* close to the iPhone? If so, unlock, and send a notification to the watch stating that the watch was just used to unlock this iPhone. The notification sent to the watch includes a button to immediately lock the iPhone.


Because it’s a two-step process (step #1 first, then step #2), it does take a bit longer than Face ID without a mask (which is really just step #1). But it works more than fast enough to be a pleasant convenience experience. Regular Face ID is so fast you forget it’s even there; “Unlock With Apple Watch” is slow enough that you notice it’s there, but fast enough that it isn’t a bother.


It’s important to note that in step #2, it works with *any* face wearing a mask. It’s not trying to do a half-face check that your eyes and forehead look like you, or anything like that. My iPhone will unlock if my wife or son is the face in front of my iPhone — but only if they’re wearing a mask, and only if my Apple Watch is very close to the phone. I’d say less than 1 meter — pretty much about what you would think the maximum distance would be between a watch on one wrist and an iPhone in the other hand.


When this feature kicks in, you *always* get a wrist notification telling you it happened, [with just one button](https://daringfireball.net/misc/2021/02/watchos-unlock-notification.png): “Lock iPhone”. If you tap this button, the iPhone is immediately hard-locked and requires your passcode to be re-entered even if you take your mask off. (It’s the same hard-locked mode you can put your iPhone into manually by pressing and holding the power button and one of the volume buttons — a good tip to remember when going through a security checkpoint or any other potential encounter with law enforcement.)


I’m not sure if anyone will be annoyed by this mandatory wrist notification, but they shouldn’t be, and it shouldn’t be optional. You want this notification every time to prevent anyone from surreptitiously unlocking your iPhone near you, just by putting a face mask on.


Also, if your Apple Watch is in Sleep mode (the bed icon in WatchOS’s Control Center), [the feature does not work](https://daringfireball.net/misc/2021/02/iphone-lock-screen-sleep-mode.jpeg).


It’s occasionally slow. And two or three times, I got a message on my iPhone that my watch was too far away for the feature to work, even though I raised my watch-wearing wrist next to the phone. These hiccups were rare, and to my recollection, I only ran into them with iOS 14.5 beta 1, not beta 2.


Even in the worst case scenario, where the feature doesn’t work, you’re no worse off than you were before the feature existed: you simply have to manually enter your phone’s passcode.


Last but not least, the “Unlock With Apple Watch” feature very specifically seems to be looking for a face wearing a face mask. The feature does not kick in if Face ID fails for any other reason — like, say, if you’re wearing sunglasses with lenses that Face ID can’t see through. (I wish they’d make this work with sunglasses, too.)


## Addenda


**Throwing Shade:** There seems to be some confusion over what I’m asking for w/r/t sunglasses. Face ID has always supported an option to turn off “Require Attention for Face ID”. When off, Face ID will work even if it doesn’t detect your eyes looking at the screen. (It’s an essential accessibility feature for people with certain vision problems.) If you own sunglasses that the iPhone’s TrueDepth camera system can’t “see” through, you can disable “Require Attention for Face ID” to allow Face ID to work while you’re wearing your shades.


This is far from ideal though, because it weakens Face ID *all the time*, not just when you’re wearing sunglasses. What’s nice about the new “Unlock With Apple Watch” feature is that it only applies when you’re wearing a mask *and* your Apple Watch. What I’m saying I’d like to see Apple support is an extension of “Unlock With Apple Watch” that would do the same thing for sunglasses that it currently does for face masks. I’ve heard from readers who have trouble with Face ID when wearing their motorcycle helmets, too, and I’m sure there are other examples. Basically, I’d like to see Apple add the option of trusting your Apple Watch to unlock your iPhone in more scenarios where your face can’t be recognized. My request is very different from, and more secure than, the existing “Require Attention” feature.


(Speaking of which, while wearing a mask, “Unlock With Apple Watch” does *not* check for whether your eyes are looking at the display, regardless of your setting for “Require Attention for Face ID”. Again, this makes sense, because it’s not Face ID — “Unlock With Apple Watch” is an alternative authentication method that kicks in *after* Face ID has failed.)


**Apple Pay:** I didn’t mention the fact that “Unlock With Apple Watch” does not work with Apple Pay. This makes sense, because however secure “Unlock With Apple Watch” is (and I think it’s quite secure), it’s not as secure as Face ID authenticating your actual face. For payments, you obviously want the highest level of secure authentication.


Also, for Apple Pay, if you’re wearing your Apple Watch (a requirement for “Unlock With Apple Watch”), you can *just use your Apple Watch for Apple Pay*.


It also doesn’t work with apps that use Face ID for authentication within them. Banking apps, for example, or unlocking locked notes in Apple Notes. But this makes sense too — the feature is specifically called “Unlock With Apple Watch”. It unlocks your phone, that’s it. Anything else that requires Face ID for secure authentication still requires Face ID.



| **Previous:** | [Volkswagen CEO Herbert Diess on Apple’s Purported Interest in Making Cars](https://daringfireball.net/2021/02/volkswagen_ceo_apple_car) |
| **Next:** | [Apple Mail and Hidden Tracking Images](https://daringfireball.net/2021/02/apple_mail_and_hidden_tracking_images) |


PreviousNext