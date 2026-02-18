---
title: "Apple’s New ‘Child Safety’ Initiatives, and the Slippery Slope"
date: 2021-08-06
url: https://daringfireball.net/2021/08/apple_child_safety_initiatives_slippery_slope
slug: apple_child_safety_initiatives_slippery_slope
word_count: 3151
---


[Apple yesterday announced three new “Child Safety” initiatives](https://www.apple.com/child-safety/):


> First, new communication tools will enable parents to play a more
> informed role in helping their children navigate communication
> online. The Messages app will use on-device machine learning to
> warn about sensitive content, while keeping private communications
> unreadable by Apple.
> Next, iOS and iPadOS will use new applications of cryptography
> to help limit the spread of CSAM online, while designing for
> user privacy. CSAM detection will help Apple provide valuable
> information to law enforcement on collections of CSAM in
> iCloud Photos.
> Finally, updates to Siri and Search provide parents and children
> expanded information and help if they encounter unsafe situations.
> Siri and Search will also intervene when users try to search for
> CSAM-related topics.


(CSAM stands for [Child Sexual Abuse Material](https://www.inhope.org/EN/articles/child-sexual-abuse-material) — a.k.a. child pornography. People familiar with the lingo seem to pronounce it *see-sam*. Another acronym to know: NCMEC — *nick-meck* — the [National Center for Missing and Exploited Children](https://www.missingkids.org/). That’s the nonprofit organization, founded and funded by the U.S. government, that maintains the database of known CSAM.)


The third initiative — updates to Siri and Search — is the easiest to understand and, I think, uncontroversial. The first two, however, seem not well-understood, and are, justifiably, receiving intense scrutiny from privacy advocates.


My first advice is to read [Apple’s own high-level description of the features](https://www.apple.com/child-safety/), which ends with links to detailed technical documentation regarding the encryption and techniques Apple is employing in the implementations, and “technical assessments” from three leading researchers in cryptography and computer vision.


The Messages feature is specifically only for children in a shared iCloud family account. If you’re an adult, nothing is changing with regard to any photos you send or receive through Messages. And if you’re a parent with children whom the feature *could* apply to, you’ll need to explicitly opt in to enable the feature. It will not turn on automatically when your devices are updated to iOS 15. If a child sends or receives (and chooses to view) an image that triggers a warning, the notification is sent from the child’s device to the parents’ devices — Apple itself is not notified, nor is law enforcement. These parental notifications are only for children 12 or younger in a family iCloud account; parents do not have the option of receiving notifications for teenagers, although teenagers can receive the content warnings on their devices.


It’s also worth pointing out that it’s a feature of the Messages *app*, not the iMessage *service*. For one thing, this means it applies to images sent or received via SMS, not just iMessage. But more importantly, it changes nothing about the end-to-end encryption inherent to the iMessage protocol. The image processing to detect sexually explicit images happens before (for sending) or after (for receiving) the endpoints. It seems like a good feature with few downsides. ([The EFF disagrees](https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life).)


The CSAM detection for iCloud Photo Library is more complicated, delicate, and controversial. But it only applies to images being sent to iCloud Photo Library. If you don’t use iCloud Photo Library, no images on your devices are fingerprinted. But, of course, most of us *do* use iCloud Photo Library.


I mentioned above that Apple’s “Child Safety” page for these new features has links to technical assessments from outside experts. In particular, I thought [the description of Apple’s CSAM detection from Benny Pinkas](https://www.apple.com/child-safety/pdf/Technical_Assessment_of_CSAM_Detection_Benny_Pinkas.pdf) — a cryptography researcher at Bar-Ilan University in Israel — was instructive:


> My research in cryptography has spanned more than 25 years. I
> initiated the applied research on privacy preserving computation,
> an area of cryptography that makes it possible for multiple
> participants to run computations while concealing their private
> inputs. In particular, I pioneered research on private set
> intersection (PSI).
> The Apple PSI system solves a very challenging problem of
> detecting photos with CSAM content while keeping the contents of
> all non-CSAM photos encrypted and private. Photos are only
> analyzed on users’ devices. Each photo is accompanied by a safety
> voucher that includes information about the photo, protected by
> two layers of encryption. This information includes a NeuralHash
> and a visual derivative of the photo. Only if the Apple cloud
> identifies that a user is trying to upload a significant number of
> photos with CSAM content, the information associated with these
> specific photos can be opened by the cloud. If a user uploads less
> than a predefined threshold number of photos containing CSAM
> content then the information associated with all of photos of this
> user is kept encrypted, even if some of these photos contain CSAM
> content. It is important to note that no information about non-CSAM
> content can be revealed by the Apple PSI system. […]
> The design is accompanied by security proofs that I have evaluated
> and confirmed.


For obvious reasons, this feature is *not* optional. If you use iCloud Photo Library, the images in your library will go through this fingerprinting. (This includes the images already in your iCloud Photo Library, not just newly-uploaded images after the feature ships later this year.) To opt out of this fingerprint matching, you’ll need to disable iCloud Photo Library.


A big source of confusion seems to be what *fingerprinting* entails. Fingerprinting is not content analysis. It’s not determining *what* is in a photo. It’s just a way of assigning unique identifiers — essentially long numbers — to photos, in a way that will generate the same fingerprint identifier if the same image is cropped, resized, or even changed from color to grayscale. It’s not a way of determining whether two photos (the user’s local photo, and an image in the CSAM database from NCMEC) are of the same subject — it’s a way of determining whether they are two versions of the *same image*. If I take a photo of, say, my car, and you take a photo of my car, the images should not produce the same fingerprint even though they’re photos of the same car in the same location. And, in the same way that real-world fingerprints can’t be backwards engineered to determine what the person they belong to looks like, these fingerprints cannot be backwards engineered to determine anything at all about the subject matter of the photographs.


The Messages features for children in iCloud family accounts *is* doing content analysis to try to identify sexually explicit photos, but is *not* checking image fingerprint hashes against the database of CSAM fingerprints.


The CSAM detection for images uploaded to iCloud Photo Library is *not* doing content analysis, and is only checking fingerprint hashes against the database of known CSAM fingerprints. So, to name one common innocent example, if you have photos of your kids in the bathtub, or otherwise frolicking in a state of undress, no content analysis is performed that tries to detect that, hey, this is a picture of an undressed child. Fingerprints from images of similar content are not themselves similar. Two photographs of the same subject should produce entirely dissimilar fingerprints. The fingerprints of your own photos of your kids are no more likely to match the fingerprint of an image in NCMEC’s CSAM database than is a photo of a sunset or a fish.


The database will be part of iOS 15, and is a database of fingerprints, *not* images. Apple does not have the images in NCMEC’s library of known CSAM, and in fact *cannot* — NCMEC is the only organization in the U.S. that is legally permitted to possess these photos.


If you don’t use iCloud Photo Library, none of this applies to you. If you do use iCloud Photo Library, this detection is only applied to the images in your photo library that are synced to iCloud.


Furthermore, one match isn’t enough to trigger any action. There’s a “threshold” — some number of matches against the CSAM database — that must be met. Apple isn’t saying what this threshold number is, but, for the sake of argument, let’s say that threshold is 10. With 10 or fewer matches, nothing happens, and nothing *can* happen on Apple’s end. Only after 11 matches (threshold + 1) will Apple be alerted. Even then, someone at Apple will investigate, by examining the contents of the *safety vouchers* that will accompany each photo in iCloud Photo Library. These vouchers are encrypted such that they can only be decrypted on the server side if threshold + 1 matches have been identified. From [Apple’s own description](https://www.apple.com/child-safety/):


> Using another technology called threshold secret sharing, the
> system ensures the contents of the safety vouchers cannot be
> interpreted by Apple unless the iCloud Photos account crosses a
> threshold of known CSAM content. The threshold is set to provide
> an extremely high level of accuracy and ensures less than a one in
> one trillion chance per year of incorrectly flagging a given
> account.


Even if your account is — against those one in a trillion odds, if Apple’s math is correct — *incorrectly* flagged for exceeding the threshold, someone at Apple will examine the contents of the safety vouchers for those flagged images before reporting the incident to law enforcement. Apple is cryptographically only able to examine the safety vouchers for those images whose fingerprints matched items in the CSAM database. The vouchers include a “visual derivative” of the image — basically a low-res version of the image. If innocent photos are somehow wrongly flagged, Apple’s reviewers should notice.


---


All of these features are fairly grouped together under a “child safety” umbrella, but I can’t help but wonder if it was a mistake to announce them together. Many people are clearly conflating them, including those reporting on the initiative for the news media. E.g. The Washington Post’s “*never met an Apple story that couldn’t be painted in the worst possible light*” [Reed Albergotti’s report](https://www.washingtonpost.com/technology/2021/08/05/apple-child-pornography-iphone/), the first three paragraphs of which are simply wrong1 and the headline for which is grossly misleading (“Apple Is Prying Into iPhones to Find Sexual Predators, but Privacy Activists Worry Governments Could Weaponize the Feature”).


It’s also worth noting that fingerprint hash matching against NCMEC’s database is already happening on other major cloud hosting services and social networks. [From The New York Times’s report on Apple’s initiative](https://www.nytimes.com/2021/08/05/technology/apple-iphones-privacy.html):


> U.S. law requires tech companies to flag cases of child sexual
> abuse to the authorities. Apple has historically flagged fewer
> cases than other companies. Last year, for instance, Apple
> reported 265 cases to the National Center for Missing &
> Exploited Children, while Facebook reported 20.3 million,
> according to the center’s statistics. That enormous gap is due
> in part to Apple’s decision not to scan for such material,
> citing the privacy of its users.


The difference going forward is that Apple will be matching fingerprints against NCMEC’s database client-side, not server-side. But I suspect others will follow suit, including Facebook and Google, with client-side fingerprint matching for end-to-end encrypted services. There is no way to perform this matching server-side with any E2EE service — between the sender and receiver endpoints, the server has no way to decrypt the images with end-to-end encryption.


Which in turn makes me wonder if Apple sees this initiative as a necessary first step toward providing end-to-end encryption for iCloud Photo Library and iCloud device backups. [Apple has long encrypted all iCloud data that can be encrypted](https://support.apple.com/en-us/HT202303),2 both in transit and on server, but device backups, photos, and iCloud Drive are among the things that are not *end-to-end* encrypted. Apple has the keys to decrypt them, and can be compelled to do so by law enforcement.


In January 2020, [Reuters reported that Apple in 2018 dropped plans to use end-to-end encryption for iCloud backups at the behest of the FBI](https://www.reuters.com/article/us-apple-fbi-icloud-exclusive-idUSKBN1ZK1CT):


> Apple Inc. dropped plans to let iPhone users fully encrypt
> backups of their devices in the company’s iCloud service after the
> FBI complained that the move would harm investigations, six
> sources familiar with the matter told Reuters.
> The tech giant’s reversal, about two years ago, has not previously
> been reported. It shows how much Apple has been willing to help
> U.S. law enforcement and intelligence agencies, despite taking a
> harder line in high-profile legal disputes with the government and
> casting itself as a defender of its customers’ information.


Whether Reuters’s report that Apple caved to FBI pressure on E2EE iCloud backups is accurate or not, I don’t know, but I do know that privacy advocates (including myself) would love to see Apple enable E2EE for *everything* in iCloud, and that law enforcement agencies around the world would not. This fingerprint matching for CSAM could pave the way for a middle ground, if Apple unveils end-to-end encryption for iCloud photos and backups in the future. In such a scenario, Apple would have no cryptographic ability to turn your backups or entire photo library over to anyone, but they would be able to flag and report iCloud accounts whose photo libraries exceed the threshold for CSAM database fingerprint matches, including the “visual derivatives” of the matching photos — all without Apple ever seeing or being able to see your original photos on iCloud.


It’s also possible Apple has simply permanently shelved plans to use end-to-end encryption for all iCloud data. No surprise: they’re not saying. But it feels very plausible to me that Apple views this privacy-protecting CSAM detection as a necessary first step to broadening the use of end-to-end encryption.


---


In short, if these features work as described and *only* as described, there’s almost no cause for concern. In an interview with The New York Times for [its aforelinked report on this initiative](https://www.nytimes.com/2021/08/05/technology/apple-iphones-privacy.html), Erik Neuenschwander, Apple’s chief privacy engineer, said, “If you’re storing a collection of CSAM material, yes, this is bad for you. But for the rest of you, this is no different.” By all accounts, that is fair and true.


But the “if” in “if these features work as described and *only* as described” is the rub. That “if” is the whole ballgame. If you discard alarmism from critics of this initiative who clearly do not understand how the features work, you’re still left with completely legitimate concerns from trustworthy experts about how the features could be abused or misused in the future.


What happens, for example, if China demands that it provide its own database of image fingerprints for use with this system — a database that would likely include images related to political dissent. [Tank man](https://www.bbc.com/news/av/world-asia-48476879), say, or any of the remarkable litany of comparisons [showing the striking resemblance of Xi Jinping to Winnie the Pooh](https://www.google.com/search?tbm=isch&q=xi+jinping+looks+like+winnie+the+pooh).


This slippery-slope argument is a legitimate concern. Apple’s response is simply that they’ll refuse. Again, from [Jack Nicas’s report for The Times](https://www.nytimes.com/2021/08/05/technology/apple-iphones-privacy.html):


> Mr. Green said he worried that such a system could be abused
> because it showed law enforcement and governments that Apple now
> had a way to flag certain content on a phone while maintaining its
> encryption. Apple has previously argued to the authorities that
> encryption prevents it from retrieving certain data.
> “What happens when other governments ask Apple to use this for
> other purposes?” Mr. Green asked. “What’s Apple going to say?”
> Mr. Neuenschwander dismissed those concerns, saying that
> safeguards are in place to prevent abuse of the system and that
> Apple would reject any such demands from a government.
> “We will inform them that we did not build the thing they’re
> thinking of,” he said.


Will Apple actually flatly refuse any and all such demands? If they do, it’s all good. If they don’t, and these features creep into surveillance for things like political dissent, copyright infringement, LGBT imagery, or adult pornography — anything at all beyond irrefutable CSAM — it’ll prove disastrous to Apple’s reputation for privacy protection. [The EFF seems to see such slipping down the slope as inevitable](https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life).


We shall see. The stakes are incredibly high, and Apple knows it. Whatever you think of Apple’s decision to implement these features, they’re not doing so lightly.


---

1. Albergotti’s opening, verbatim:

Apple unveiled a sweeping new set of software tools Thursday that
will scan iPhones and other devices for child pornography and text
messages with explicit content and report users suspected of
storing illegal pictures on their phones to authorities.

Wrong. The only photos that might be reported to authorities are those being sent to iCloud. “Scan” is a misleading verb. And the entire “text messages” feature is only for children in shared iCloud family accounts. Albergotti’s alarmist lede makes it sound like all content for all users in Messages will be “scanned”, whereas in fact nothing sent to or from an adult user in Messages will ever be “scanned” — unless an image is saved from Messages to Photos and iCloud Photo Library is enabled.

The aggressive plan to thwart child predators and pedophiles and
prohibit them from utilizing Apple’s services for illegal activity
pitted the tech giant against civil liberties activists and
appeared to contradict some of its own long-held assertions about
privacy and the way the company interacts with law enforcement.

As announced, none of these features contradict any of Apple’s “long-held assertions”.

The move also raises new questions about the nature of smartphones
and who really owns the computers in their pockets. The new
software will perform scans on its users’ devices without their
knowledge or explicit consent, and potentially put innocent users
in legal jeopardy.

None of this raises any questions about who owns your iPhone. It does assert that Apple owns iCloud’s servers, but no images on an iPhone that isn’t syncing to iCloud Photo Library will ever be fingerprinted. The Messages content warnings for children are explicitly opt in, as is syncing to iCloud Photo Library. Unless Apple’s cryptographic math is catastrophically wrong, it is exceedingly unlikely that innocent users’ photos will ever be flagged, and even if they are flagged for exceeding the threshold for CSAM fingerprint matches, there’s a manual review by Apple before anything is reported to law enforcement.
It’s hard to imagine a three-paragraph lede that is more histrionically misleading than Albergotti’s in this report. ↩︎
2. The exception is IMAP email, which is encrypted in transit between client and server but is not stored encrypted on the server, because that’s how IMAP was designed. Long story short, email is probably the least secure messaging service you use. If you wouldn’t put it on paper and send via postal mail, don’t send it via email. ↩︎︎



| **Previous:** | [Document Proxy Icons in MacOS 11 and 12 as a — Ahem — Proxy for Apple’s Current UI Design Sensibilities](https://daringfireball.net/2021/07/document_proxy_icons_macos_11_and_12) |
| **Next:** | [Charlie Watts](https://daringfireball.net/2021/08/charlie_watts) |


PreviousNext