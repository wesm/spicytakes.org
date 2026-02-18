---
title: "‘Secure Intent’ on Apple Devices"
date: 2021-06-02
url: https://daringfireball.net/2021/06/secure_intent_on_apple_devices
slug: secure_intent_on_apple_devices
word_count: 1725
---


Interesting new document in the May update to Apple’s Platform Security guide: “[Secure Intent and Connections to the Secure Enclave](https://support.apple.com/guide/security/secure-intent-connections-enclave-sec7a94f7d1e/web)” ([spotted by Glenn Fleishman](https://twitter.com/GlennF/status/1398370585734836224)). It’s short, so I’m quoting it in its entirety:


> Secure intent provides a way to confirm a user’s intent without
> any interaction with the operating system or Application
> Processor. The connection is a physical link — from a physical
> button to the Secure Enclave — that’s available in the following:
> iPhone X or later
> Apple Watch Series 1 or later
> iPad Pro (all models)
> iPad Air (2020)
> Mac computers with Apple Silicon
> With this link, users can confirm their intent to complete an
> operation in a way designed such that even software running with
> root privileges or in the kernel can’t spoof.
> This feature is used to confirm user intent during Apple Pay
> transactions and when finalizing pairing Magic Keyboard with Touch
> ID to a Mac with Apple silicon. A double-press on the appropriate
> button when prompted by the user interface signals confirmation of
> user intent. For more information, see [Securing purchases with
> Apple Pay](https://support.apple.com/guide/security/uses-for-touch-id-and-face-id-secc5227ff3c/1/web/). A similar mechanism — based on the Secure Enclave
> and T2 firmware — is supported on MacBook models with the Apple
> T2 Security Chip and no Touch Bar.


First things first, this sentence seems to be outdated/wrong:


> A double-press on the appropriate
> button when prompted by the user interface signals confirmation of
> user intent.


because some of the devices on this list don’t require double-pressing a button. The double-press rule is only for Face ID devices. Touch ID devices on this list only require a fingerprint scan — that includes MacBooks, M1 Macs with the new Magic Keyboard, and older iPad Pros.


In broad strokes, we can classify Apple devices into five categories with regard to authentication and secure intent:

1. Devices that support neither Face ID nor Touch ID in any way. On such devices (old iOS devices, and Intel Macs without a Touch Bar or Touch ID button) you can only authenticate by entering passcodes / passwords.
2. iOS devices with Touch ID on the home button. Most such devices are not included in this list. See below.
3. Devices with Touch ID support *not* on a home button. This includes the new iPad Air (which has Touch ID on the power button), and recent MacBook  models with a Touch Bar or with a Touch ID power button. (The above-quoted support document from Apple mentions “Mac computers with Apple Silicon”, and also says “a similar mechanism ... is supported on MacBook models with the Apple T2 Security Chip and no Touch Bar”. That seemingly omits Intel-based MacBook Pros with a Touch Bar, but I think that’s a mistake. Any MacBook Pro with a T2 security chip should, I think, be eligible for the same “similar mechanism” as the ones without a Touch Bar.)
4. Face ID devices: iPhones X or later, and 2018 or later iPad Pros.1
5. Apple Watch, which has neither Face ID nor Touch ID, but knows when it has been removed from your wrist *after* it’s been unlocked via passcode or via unlocking the iPhone to which it is paired. (A lot of Apple Watch owners are not aware that you don’t have to enter your passcode when you put the watch on — you can just put it on and the Watch will unlock when next you unlock your iPhone.) Once unlocked, your Apple Watch is trusted until you take it off.


The desktop Macs eligible for secure intent — the new M1 iMac and the M1 Mac Mini that launched last November — do not qualify without a trusted peripheral. Neither of them has Touch ID *on the computer itself*. To use Touch ID, they need to be paired with one of Apple’s new Magic Keyboards. This still qualifies for secure intent, despite the fact that secure intent requires “a physical link from a physical button to the Secure Enclave”, *because the keyboard itself contains its own Secure Enclave*. [**Update 4 June 2021:** I was wrong — the Magic Keyboard does *not* have its own Secure Enclave. [See this post for details](https://daringfireball.net/linked/2021/06/04/magic-keyboard-with-touch-id). But it’s also the case that Apple’s “secure intent” description is now wrong as well, because clearly there’s no “physical link” between the Touch ID sensor of a wireless keyboard and the Secure Enclave in the Mac with which it’s paired.]


Likewise, for several years now, *any* modern Mac has been able to use an Apple Watch paired to the same iCloud account as a “secure intent” device, very much like using a paired Touch ID Magic Keyboard. You can use a double-click of your Apple Watch side button to confirm purchases and administrator-privileged actions like moving protected files to the Trash. Same thing for [unlocking your Mac](https://support.apple.com/en-us/HT206995): your Watch counts as a secure authentication method (but with no interaction required, only proximity).


Conspicuously absent from the list of “secure intent” devices are all *most* iOS devices with Touch ID on the home button. The exceptions are [the early iPad Pro models from 2015–2017](https://support.apple.com/en-us/HT201471#ipadpro). I have no idea why those early iPad Pros qualify but Touch ID iPhones and non-Pro iPads do not.


One factor — but a factor that wouldn’t explain why home button iPad Pro models qualify for secure intent — might be that the home button is overloaded on those devices. There have been [a handful of scam apps](https://www.wired.com/story/iphone-touch-id-scam-apps/) that pop up “surprise” in-app purchase prompts, and if the user tries to press the Touch ID home button with the intention of just getting out of the app and back to the home screen, they risk *confirming* the unwanted purchase as soon as they put their finger on the home button. If all software were trustworthy, Touch ID on the home button would be ideal. With the potential for untrustworthy software, it’s not an ideal design to use the same button for “*get me out of here with a press*” and for “*just touch this to confirm*”. In the shift from home button Touch ID to Face ID on iPhones and iPads, Apple has recalibrated the balance between convenience and security to be a little more secure but a little less convenient.


But perhaps the reason Touch ID home button devices don’t qualify for this list is simply that those home buttons don’t have the direct “physical link” to the Secure Enclave that the new Touch ID buttons do (on MacBook keyboards and the new iPad Air’s side button). Perhaps they work in a way such that malware with root privileges could potentially spoof them? And, somehow, the early iPad Pro models were designed with a more secure connection between the home button and Secure Enclave?


Face ID by itself is a good and convenient authentication system for low-security authentication. Unlocking your device, opening up a locked note in Apple Notes, viewing passwords in your Keychain, etc. But for actions that should require extra confirmation, Face ID alone isn’t enough. Consider in-app purchases — it’s not feasible to *just* use Face ID to confirm a purchase, because if you see the purchase confirmation on screen, you’re already looking at your iPhone or iPad.


The extra confirmation for Face ID *could* be something on screen that you tap or click, but then it would be susceptible to malware that, in theory, might be on your device. Anything on screen is only as secure as iOS or MacOS itself. That’s why Apple made double-clicking the side button the confirmation for Face ID — the software running on your device cannot spoof a double-click of the side button, and the side button has a direct physical connection to the Secure Enclave that doesn’t go through the OS.


I think this is why Face ID on Macs might prove a little tricky. If a future iMac, say, has Face ID built in, that should work fine for low-security authentications like unlocking your Mac when it wakes from sleep. But for “secure intent”, where does the physical button connected directly to a Secure Enclave go? The iMac *could* use its power button, like iOS devices do, but the power button on iMacs is on the back of the display. It’s not meant to be convenient. You want the confirmation button to be built into a keyboard, and that keyboard needs to have its own Secure Enclave to have a physical connection to the button. Bluetooth and USB are out — they both go through the OS, so they’re not secure enough. And if you need a Magic Keyboard or Apple Watch for secure intent confirmation, would it really be that convenient to have Face ID on iMacs just for unlocking the screen on wake? Maybe. But like I said, it’s tricky.


[**Update 4 June 2021:** The new M1 iMacs *do* use their power buttons as a form of secure intention confirmation: you need to double-press the power button to confirm pairing a Bluetooth keyboard. I didn’t notice this with my review unit because [Apple pairs the included keyboard with the iMac at the factory](https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/1/web/1).]


This is true for MacBooks too. They could (and I hope someday will) add Face ID, but if they do, Face ID will likely only be used for low-security authentication, and “secure intent” will necessitate that there still be a Touch ID button *in addition to* Face ID, or that the user be wearing a trusted Apple Watch.2


In short, I suspect Apple’s biometric authentication future will be multi-sensor.


---

1. The 2nd generation iPhone SE came after the iPhone X, and does not have Face ID, but because it shipped after the iPhone X, it should qualify for “iPhone X or later” — but it’s unclear to me if it qualifies for secure intent. I think now that the list is growing, Apple ought to list each supported device specifically. ↩︎︎
2. And again, think about how these confirmations work on Apple Watch: you don’t OK them on screen, you OK them with a double-click of the hardware side button, something software in WatchOS cannot spoof. ↩︎



| **Previous:** | [The New Siri Remote (and Updated Apple TV 4K)](https://daringfireball.net/2021/05/the_new_siri_remote_etc) |
| **Next:** | [App Store: The Schiller Cut](https://daringfireball.net/2021/06/app_store_the_schiller_cut) |


PreviousNext