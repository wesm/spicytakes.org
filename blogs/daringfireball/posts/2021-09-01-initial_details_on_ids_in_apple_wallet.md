---
title: "Initial Details on Using Driver’s Licenses and State ID’s in Apple Wallet"
date: 2021-09-01
url: https://daringfireball.net/2021/09/initial_details_on_ids_in_apple_wallet
slug: initial_details_on_ids_in_apple_wallet
word_count: 1340
---


[Apple Newsroom](https://www.apple.com/newsroom/2021/09/apple-announces-first-states-to-adopt-drivers-licenses-and-state-ids-in-wallet/):


> Apple today announced that it is working with several states
> across the country, which will roll out the ability for their
> residents to seamlessly and securely add their driver’s license or
> state ID to Wallet on their iPhone and Apple Watch. Arizona and
> Georgia will be the first states to introduce this new innovation
> to their residents, with Connecticut, Iowa, Kentucky, Maryland,
> Oklahoma, and Utah to follow. The Transportation Security
> Administration (TSA) will enable select airport security
> checkpoints and lanes in participating airports as the first
> locations customers can use their driver’s license or state ID in
> Wallet. Built with privacy at the forefront, Wallet provides a
> more secure and convenient way for customers to present their
> driver’s licenses and state IDs on iPhone or Apple Watch.


There’s a lot of information about exactly how this will work in the Newsroom post, including screenshots. I got to talk with Apple about this today, and I’m impressed. A few important details:


> Driver’s licenses and state IDs in Wallet are only presented
> digitally through encrypted communication directly between the
> device and the identity reader, so users do not need to unlock,
> show, or hand over their device.


This is a *super* key point. Of course no one wants to hand over their phone to anyone. More importantly, no one should *ever* hand their phone to a police officer, and that goes a hundredfold if it’s unlocked.1 The Wallet system Apple has designed for ID is very much like Apple Pay. When you pay with a physical credit card, you often hand your card to an employee. When you pay with Apple Pay, you *never* hand your phone to an employee. It wouldn’t even work, because no one else can authorize an Apple Pay transaction without *your* biometric authentication. This ID feature for Wallet is exactly like that: it doesn’t work without your biometric authentication, and your phone does not unlock when you use it.


An interesting sidenote: when using a Touch ID iPhone with Apple Wallet’s ID feature, you must register one and only one finger when you add your ID to your Wallet, and whenever you verify your ID in Wallet, you’ll need to use that same finger. Apple has never recommended allowing your spouse or partner to register one of their fingers on your iPhone, but many people do that. This feature is designed to ensure that the same person who enrolled their state ID in Wallet is the same person verifying it biometrically. (This is not an issue with Face ID, obviously.)


To use your ID in Wallet, you tap your phone (or watch) against an NFC terminal, and you get [an Apple Pay-like sheet showing you who is asking for your ID](https://daringfireball.net/misc/2021/09/apple_wallet-state-id_privacy.jpeg) (e.g., TSA), and exactly which details from your ID they’re asking for (e.g., name, photo, date of birth — but perhaps *not* other embedded details like your blood type or your home address). So if you’re just buying booze, say, and the clerk or server needs to check your age, they could prompt only to verify that you’re 21 or older, without even seeing your exact birthdate, let alone any other details from your ID. It is exceedingly more private than handing over a physical ID card, perhaps even more so than using Apple Pay compared to handing over a physical credit card.


Also, it’s an open standard:


> Apple’s mobile ID implementation supports the ISO 18013-5 mDL
> (mobile driver’s license) standard which Apple has played an
> active role in the development of, and which sets clear guidelines
> for the industry around protecting consumers’ privacy when
> presenting an ID or driver’s license through a mobile device.


---


[Apple announced Apple Pay 7 years ago](https://www.apple.com/newsroom/2014/09/09Apple-Announces-Apple-Pay/). It worked at few places at first. Soon, though, it started being accepted at more establishments, as businesses upgraded older terminals with new card readers for modern chip-enabled cards. But two years in, the impatient *gimme-that-one-cookie-now-I-don’t-care-if-I-can-just-wait-a-few-minutes-and-get-a-whole-bunch-of-cookies-later* geniuses at Business Insider were running headlines like “[Apple Pay Is Struggling to Catch On](https://www.businessinsider.com/apple-pay-is-struggling-to-catch-on-2016-6)”.


You don’t see headlines like that [any more](https://www.businessinsider.com/apple-bet-apple-pay-shows-results-transactions-market-share-increases-2020-2). Nor do you see many headlines about Google Pay “catching up” — [it’s not](https://www.nfcw.com/whats-new-in-payments/apple-pay-used-for-more-than-90-of-us-mobile-wallet-debit-transactions-in-2020/) and maybe never will.


These things take time, partnerships, evangelism, planning, and diligent hard work. There were a lot more complaints asking why Apple Pay didn’t work almost everywhere circa 2016 than there are kudos now that it does work almost everywhere. Patience and focus are essential to winning a long game, but success can be rather thankless. Apple excels at thankless long games. Other companies, [not so much](http://assets.businessinsider.com/google-pay-payments-team-seeing-executive-exodus-turnover-caesar-sengupta-2021-8?op=1).


I expect a similar timeline for using ID through Apple Wallet: a year or two where it seems like we can’t really use it anywhere, another few years where we start using it more and more, and then, when we start getting close to a decade down the road, without much fanfare, it’ll be our default method of presenting ID.2


---

1. Seriously, never ever hand your phone to a cop or anyone vaguely cop-like, like the rent-a-cops working for TSA. If they tell you that you must, refuse. If you really need to hand it over, they’ll take it from you. Also, and this is really important, something you should internalize now, so you don’t have to try to remember it in a moment of stress or panic: [how to hard-lock your iPhone](https://support.apple.com/en-us/HT203017).
With a Face ID iPhone, you hard-lock your iPhone by pressing and holding the side button and either volume button. Two seconds or so — just long enough to make the “Slide to power off” screen appear. (That screen also has sliders for Medical ID and Emergency SOS.) With a Touch ID iPhone, you just press and hold the power button.
Once you do this, your iPhone will require your passcode to unlock. You can’t use Face ID or Touch ID to unlock until after you’ve unlocked with your passcode. That means even if someone confiscates your phone by force, they cannot unlock it by pointing it at your face or by forcing your finger onto the Touch ID sensor. Remember to put your iPhone into this mode *every* time you’re separated from it as you go through the magnetometer at any security checkpoint, especially in the airport.
Don’t just memorize this, internalize it, so you can do it without even thinking. Make it something you know the way you know your own middle name. By design, it’s an action you can perform surreptitiously while your iPhone remains in your pocket or purse.
Another action to remember: [If you click the power button five times in a row](https://support.apple.com/guide/iphone/make-emergency-calls-iph3c99374c/ios), your iPhone will immediately sound a klaxon and will initiate an Emergency SOS call in three seconds. This will also hard-lock your phone, but, by design, it is the opposite of surreptitious. ↩︎
2. I’ll tell you what would be some nice icing on the cake: if Apple can convince state DMVs to let Apple design the digital cards in Wallet. My driver’s license is [so goddamned ugly](https://www.dmv.pa.gov/Driver-Services/Driver-Licensing/Pages/New-Driver-License-Design.aspx) — mostly typeset in Arial (of-fucking-course), with a script font for “Pennsylvania” that looks like it came on a clip art CD included free with every Compaq PC in 1994 — that if it were a design project for a class I was teaching, I’d pull the student aside and make them this offer: take an F for the project, or, promise to change majors and I’ll give them a gentleperson’s C on their way out the door of design school. Most other states don’t do much better. ID cards should be beautiful and inspiring objects, a source of pride. Help us Apple-Wan Kenobi, you’re our only hope. ↩︎︎



| **Previous:** | [Let’s Consider Some of the Implications of Third-Party Payment Processing for In-App Purchasing on iOS and Android](https://daringfireball.net/2021/08/implications_of_third-party_payment_processing_for_iap) |
| **Next:** | [Why iPhone Names Have Numbers and Most Other Apple Product Names Don’t](https://daringfireball.net/2021/09/iphone_names) |


PreviousNext