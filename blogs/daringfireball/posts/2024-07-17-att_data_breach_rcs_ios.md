---
title: "The AT&T Data Breach Shows Why RCS Can’t Be Trusted and the Downside of Apple Adding Support for It in iOS 18"
date: 2024-07-17
url: https://daringfireball.net/2024/07/att_data_breach_rcs_ios
slug: att_data_breach_rcs_ios
word_count: 1472
---


Here’s a hot take: [last week’s news of a massive AT&T breach](https://daringfireball.net/linked/2024/07/12/att-massive-data-breach) revealing the phone call and text messaging records of all AT&T customers for six months in 2022 exemplifies why RCS is a terrible protocol that ought not exist, and why it’s a mistake that Apple is adding support for it to iOS 18 this year.


The pro-RCS argument is that it improves upon SMS by adding support for much larger image and video attachments, as well as niceties like typing indicators. It really is just like SMS but better, which makes it seem, on the surface, like a no-brainer that all cell phone platforms should support it. In this view, the only reason for Apple’s yearslong refusal to support RCS was to maintain a maximum feature gap between iMessage (which, famously, is exclusive to Apple’s devices) and carrier-based messaging. In day-to-day use people can’t *see* that iMessage is fully end-to-end encrypted, but everyone can plainly see that images and videos sent over SMS/MMS look like shit. So it looks like nothing but pure spite that Apple refused, for years, to support RCS.


But the argument against RCS is strong and simple: it doesn’t support end-to-end encryption. The only new messaging platforms that should gain any traction are those that not only support E2EE, but that *require it*. Messaging and audio/video calls should *only* work through E2EE. That’s true for iMessage and FaceTime.


SMS and traditional telephone voice calls lack any encryption at all, but they’re firmly established. Just like email. But anything new should only be supported if it’s fundamentally based on E2EE. [The RCS spec](https://en.wikipedia.org/wiki/Rich_Communication_Services#Specifications) offers no message encryption at all. Google has implemented its own encryption for RCS, but, that’s a proprietary implementation that only works for messages sent between users who are all using Google’s own Messages app. [From Google’s “Messages End-to-End Encryption Overview”](https://www.gstatic.com/messages/papers/messages_e2ee.pdf):


> In order to store and exchange user public keys like identity
> keys and prekeys, we need to have a central key server. Unlike
> the RCS messaging servers, the key server is currently only
> hosted by Google.


Perhaps, someday, the RCS spec will support an open standard for E2EE. I’m not holding my breath for that. For one thing, industry consortiums tend not to produce good solutions to hard problems, and an open standard for E2EE messaging is a very hard problem. Maybe impossible. Someone has to handle key exchange and management, but who would that be in an open standard? Then there’s the politics: law enforcement agencies the world over will pressure carriers against that. [As I reported back in February](https://daringfireball.net/2024/02/eu_rcs_imessage), the primary reason Apple changed course on supporting RCS is that it’s mandated in China. The Chinese government surely loves RCS *because* it isn’t encrypted.


That’s not unique to China or other authoritarian dictatorships. Even in the West, law enforcement and spy agencies *love* the fact that telephone voice calls and cellular text messages are unencrypted. We don’t know how much they record and keep, but it’s a known fact that the NSA has black boxes installed at the carriers’ call centers, and the safest bet is that they record and store all of it. But even if you trust law enforcement agencies to handle this sensitive data securely, it’s clear, from this latest data breach alone, that the carriers themselves cannot be trusted. They’re inept. They [always have been inept](https://www.youtube.com/watch?v=UdULhkh6yeA). And my money says they always will be.


But even if, somehow, a future version of the RCS spec supports E2EE, what about older devices that only support today’s non-encrypted version of RCS? Even if RCS eventually supports E2EE — which, again, I doubt — such support will surely be optional, not mandatory, because RCS has already shipped and is in widespread use on Android without encryption. That’s why messaging platforms should be built around E2EE from the start. It’s difficult to mandate E2EE on a platform that already supports unencrypted messaging. RCS should have been *exclusively* E2EE; instead, the standard offers no encryption at all.


Carrier-based messaging was best left as a legacy protocol. SMS wasn’t dying, but it was slowly fading away, and should have been left for things like automated “your table is ready” notifications from restaurants. RCS is just going to give carrier-based messaging new legs that it shouldn’t have gotten.


Another thing that sucks about carrier-based messaging is that it requires a device with an active SIM card from a carrier. Yes, you can send and receive SMS from a Mac or iPad [with Text Message Forwarding](https://support.apple.com/en-mide/guide/messages/icht8a28bb9a/mac), but you need the iPhone to do the forwarding. If you power down (or worse, lose) your iPhone, your Mac and iPad will no longer be able to send or receive SMS messages — and I presume [that will be true for RCS as well](https://support.google.com/messages/answer/9487020). Whereas with modern messaging platforms like iMessage, Signal, and WhatsApp, devices like PCs and tablets can serve as clients without a phone.1


There is, admittedly, a good argument in favor of RCS. Basically, that phone carrier messaging is now and always will be a universally accessible form of communication. [Effectively](https://www.pewresearch.org/global/2022/12/06/internet-smartphone-and-social-media-use-in-advanced-economies-2022/), everyone who is online has a cell phone, and those phones can all send and receive SMS. Because carrier-based messaging isn’t going away, this argument goes, it ought to be made as good as possible, and RCS — despite its deficiencies — is clearly better than SMS. Therefore RCS ought to be supported by all mobile devices, including iOS. Here’s Andy Ihnatko, [in a discussion with me on Threads back in November](https://www.threads.net/@gruber/post/CzxGU_cxzWk):


> Carrier-based messaging on a pre-installed messaging app might
> seem irrelevant to many of us. But it serves and suffices. And the
> process of discovery, selection, and installation of a different
> service — and getting your entire social circle on board with it — is *deathly* for so many people.
> “If I know their phone number, I can send them a message or a
> photo” is a world-beater of a feature for the average user. This
> is why such apps should be as muscular as feasibly possible.


Ihnatko is right, but only if you believe that carrier-based messaging should remain the baseline. I do not. And it’s also a U.S.-centric viewpoint. In most countries around the world, platforms like WhatsApp, Line, and Facebook Messenger serve that role, as the baseline “everyone has it” messaging platform — and those countries are better for it. I prefer iMessage, personally, for multiple reasons, but iMessage is fundamentally limited from serving that “everyone has it” baseline role by Apple’s decision not to ship an Android client. Eddy Cue doesn’t lose many arguments [but he lost that one](https://daringfireball.net/linked/2022/01/19/cue-imessage-android). All of the effort spent pushing Apple to support RCS would have been better spent pushing Apple to ship iMessage for Android. And without a supported iMessage client for Android, that role ought to go to WhatsApp, not RCS. WhatsApp is free, secure, and works equally well on all phones.


[Meta knows this](https://www.hollywoodreporter.com/tv/tv-news/modern-family-reboot-whatsapp-ad-original-cast-1235925415/), and [clearly smells the opportunity](https://www.youtube.com/watch?v=Uyu--_gLt7s). Does Apple?


---

1. Two notes on this. First: security researcher Tommy Mysk [recently publicized](https://mjtsai.com/blog/2024/07/08/signal-for-macs-encrypted-database/) some serious issues with how Signal’s Mac client stores data locally, especially the fact that it stores its encryption key in a plain text file readable by any app on your Mac. This is not a defect in the Signal protocol, which is fully end-to-end encrypted, and arguably the gold standard for privacy. The problem with Signal’s desktop apps is that they’re storing information locally, without protection, outside the endpoints of “E2EE”. As Mysk proved, you can just copy Signal’s data folder from one Mac (that is properly signed into Signal) to another Mac (say, an attacker’s machine) and that second machine will be able to send and receive messages without the user being able to detect that an unauthorized machine has access to their account. [Signal claims to be addressing this flaw](https://www.bleepingcomputer.com/news/security/signal-downplays-encryption-key-flaw-fixes-it-after-x-drama/) in a future version now in beta testing.
Second: Meta’s companywide aversion to developing native iPad apps includes WhatsApp. At least with Threads and Instagram, they allow the iPhone apps to run on iPadOS in letterboxed compatibility mode. But [as you can see in this screenshot](https://daringfireball.net/misc/2024/07/whatsapp-ipad-no-dice.png) (which also shows how the lack of a proper native iPad client for WhatsApp has created a cottage industry of sketchy third-party apps in the App Store that are presenting themselves as WhatsApp clients), the iPhone WhatsApp client can’t even be installed on an iPad. This is so irritating. Meta does have proper native iPad versions of the blue Facebook app and Messenger, so I suppose there’s hope they’ll ship a proper WhatsApp client for iPad eventually. ↩︎



| **Previous:** | [It’s the Guns, It’s the Guns, It’s the Guns](https://daringfireball.net/2024/07/its_the_guns) |
| **Next:** | [Apple Strikes Deal With Taboola to Sell Ads for Apple News](https://daringfireball.net/2024/07/apple_taboola_sitting_in_a_tree) |


PreviousNext