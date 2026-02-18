---
title: "Apple Pulls Advanced Data Protection From the UK, in Defiance of UK Demand for Global Backdoor"
date: 2025-02-21
url: https://daringfireball.net/2025/02/apple_pulls_advanced_data_protection_from_the_uk
slug: apple_pulls_advanced_data_protection_from_the_uk
word_count: 1871
---


Apple, in a very precisely worded statement issued to the media (including me) this morning:


> Apple can no longer offer Advanced Data Protection (ADP) in the
> United Kingdom to new users and current UK users will eventually
> need to disable this security feature. ADP protects iCloud data
> with end-to-end encryption, which means the data can only be
> decrypted by the user who owns it, and only on their trusted
> devices. We are gravely disappointed that the protections provided
> by ADP will not be available to our customers in the UK given the
> continuing rise of data breaches and other threats to customer
> privacy. Enhancing the security of cloud storage with end-to-end
> encryption is more urgent than ever before. Apple remains
> committed to offering our users the highest level of security for
> their personal data and are hopeful that we will be able to do so
> in the future in the United Kingdom. [As we have said many times
> before](https://www.apple.com/privacy/government-information-requests/), we have never built a backdoor or master key to any of our
> products or services and we never will.


The context for this is the news that broke two weeks ago, [by Joseph Menn in The Washington Post](https://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/?pwapi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWFzb24iOiJnaWZ0IiwibmJmIjoxNzM4OTA0NDAwLCJpc3MiOiJzdWJzY3JpcHRpb25zIiwiZXhwIjoxNzQwMjg2Nzk5LCJpYXQiOjE3Mzg5MDQ0MDAsImp0aSI6ImRiNmNkODlmLThiZjMtNDkwMy05ZjJlLTFkYmIxOGJmNTViNSIsInVybCI6Imh0dHBzOi8vd3d3Lndhc2hpbmd0b25wb3N0LmNvbS90ZWNobm9sb2d5LzIwMjUvMDIvMDcvYXBwbGUtZW5jcnlwdGlvbi1iYWNrZG9vci11ay8ifQ.jmi16EkHDs4oV8NT_duwmo2NQd8rxE3enCtbFsh8KNU&itid=gfta), and [Tim Bradshaw in the Financial Times](https://www.ft.com/content/57b391a0-c531-4cde-a5e9-c5d60b21a161), that (quoting Menn’s report, emphasis added):


> Security officials in the United Kingdom have demanded that Apple
> create a back door allowing them to retrieve all the content any
> Apple user worldwide has uploaded to the cloud, people familiar
> with the matter told The Washington Post. The British government’s
> undisclosed order, issued last month, requires blanket capability
> to view fully encrypted material, not merely assistance in
> cracking a specific account, and has no known precedent in major
> democracies. [...]
> The office of the Home Secretary has served Apple with a document
> called a technical capability notice, ordering it to provide
> access under the sweeping U.K. Investigatory Powers Act of 2016,
> which authorizes law enforcement to compel assistance from
> companies when needed to collect evidence, the people said. The
> law, known by critics as the Snoopers’ Charter, *makes it a
> criminal offense to reveal that the government has even made such
> a demand*. An Apple spokesman declined to comment.


By definition, end-to-end encryption can have no secret backdoor, so compliance with this order from the UK would, in broad strokes, require Apple to abandon end-to-end encryption — not just for users in the UK but all users in all countries globally.1 More insidiously and outrageously, they are apparently forbidden by UK law, under severe penalty (imprisonment), from even informing the public about this demand, or, if they were to comply, from telling the public what they’ve done. The UK expects Apple to give them secret access to all iCloud data without Apple telling anyone — including, I believe, *even the US government* — that they’ve granted the UK government this breathtaking access.


Rather than comply, Apple is choosing instead to pull Advanced Data Protection from the UK. For UK users not already using ADP, the ability to enable it was already turned off before Apple’s statement was sent. [This report from BBC News](https://www.bbc.com/news/articles/cgj54eq4vejo) has [a screenshot](https://daringfireball.net/misc/2025/02/uk-adp-screenshot.jpeg) of what UK users see if they attempt to enable it today.


Re-read Apple’s statement above, which I’ve quoted in full, including the hyperlink. What stands out is that Apple is offering no explanation, not even a hint, *why* the company “can no longer offer Advanced Data Protection (ADP) in the United Kingdom to new users and current UK users will eventually need to disable this security feature”. On issues pertaining to security and privacy, Apple always explains its policies and features as best it can. The fact that Apple has offered no hint as to why they’re doing this is a [canary statement](https://en.wikipedia.org/wiki/Warrant_canary) of sorts: they’re making clear as best they can that they’re under a legal gag order that prevents them from even acknowledging that they’re under a legal gag order, by not telling us why they’re no longer able to offer ADP in the UK. This sort of read-between-the-lines implicit confirmation that they’re under a gag order is the only sort of confirmation they can legally offer, at risk of imprisonment.


Enabling ADP is controlled server-side, so Apple was able to disable the ability for UK users to turn on ADP without requiring a software update to devices. But it’s an open question how this will play out for users in the UK who already have ADP enabled. Apple cannot disable ADP remotely. With a moment’s thought, you can realize why they can’t: it would defeat the entire purpose. In the same way that Apple can’t hold its own key to decrypt a user’s data with ADP, they also can’t hold the ability to disable ADP.


Enabling ADP is reversible, however. After turning it on, a user can revert to standard protection, turning it off. But they must [manually confirm](https://daringfireball.net/misc/2025/02/adp-turn-off-screenshot.png) it. I suspect what Apple is going to do for UK users with ADP already enabled is begin issuing warnings, instructing them to disable it manually, before some deadline. Once that deadline passes, I think Apple will have to stop allowing iCloud access to ADP-protected accounts in the UK. That won’t leave the data of those users unprotected — they simply will lose access to sync until they disable ADP and revert to standard protection.


The bottom line is that the UK government is proceeding like a tyrannical authoritarian state. That’s not hyperbole. And the breathtaking scope of their order — being able to secretly snoop, without notice that they even have the capability, not only on their own citizens but every Apple user in the entire world — suggests a delusional belief that the British Empire still stands. It’s simultaneously infuriatingly offensive, mathematically ignorant (regarding the nature of end-to-end encryption), dangerous (as proven by the [recent Salt Typhoon attack](https://apnews.com/article/china-hack-us-telecoms-salt-typhoon-88cabc592dae2fa870772c5ce4ace5ea) China successfully waged to eavesdrop on non-E2EE communications in the United States), and laughably naive regarding the UK’s actual power and standing in the world.


Apple is, rightly and righteously, telling them to fuck off.


---

1. If you use Advanced Data Protection, your iCloud data can only be decrypted (a) by your own devices, (b) using the recovery key that you control from when you enabled ADP, or (c) by any recovery contacts you’ve created in iCloud. Apple insists that you must generate a recovery key or specify at least one recovery contact to enable ADP. Lose your devices, lose your recovery key, and lose your iCloud passphrase, and no one, including Apple, can recover your iCloud data. That level of cryptographically guaranteed security is the benefit of ADP. It’s also the risk of ADP. And there’s a convenience cost. For example, web access to iCloud. [Quoting from Apple’s own ADP documentation](https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web):

When a user first turns on Advanced Data Protection, web access
to their data at iCloud.com is automatically turned off. This is
because iCloud web servers no longer have access to the keys
required to decrypt and display the user’s data. The user can
choose to turn on web access again, and use the participation of
their trusted device to access their encrypted iCloud data on
the web.
After turning on web access, the user must authorize the web
sign-in on one of their trusted devices each time they visit
iCloud.com. The authorization “arms” the device for web access.
For the next hour, this device accepts requests from specific
Apple servers to upload individual service keys, but only those
corresponding to an allow list of services normally accessible on
iCloud.com. In other words, even after the user authorizes a web
sign-in, a server request is unable to induce the user’s device to
upload service keys for data that isn’t intended to be viewed on
iCloud.com, (such as Health data or passwords in iCloud Keychain).
Apple servers request only the service keys needed to decrypt the
specific data that the user is requesting to access on the web.
Every time a service key is uploaded, it is encrypted using an
ephemeral key bound to the web session that the user authorized,
and a notification is displayed on the user’s device, showing the
iCloud service whose data is temporarily being made available to
Apple servers.

It’s for reasons like “I lost my only device and forgot my iCloud password”, and to provide easy access to iCloud through the web, that Advanced Data Protection is not the default for all users.
I think it’s technically possible that Apple could maintain “end-to-end encryption” in a pedantic sense while adding an additional UK-controlled signing key to all encrypted data in iCloud. Let’s say you own two Apple devices, an iPhone and a Mac, and you use Advanced Data Protection. Your data can only be decrypted by those two devices, or by your recovery key, or by a device controlled by one of your recovery contacts. Apple could do something like add the UK government as, effectively, a recovery contact, to each and every user in the world’s encrypted iCloud data. That would still be “end-to-end”, it’s just that the UK government would control one of those end points. But the way iCloud security is designed, something like that cannot be added silently. When a new device is added to your iCloud account, all of your existing devices get a notification that a new device has been added. I personally see these notifications hundreds of times a year, every year, as I add new review unit devices to my account. Like back in September, I got four iPhone 16 review units, two Apple Watch review units, and purchased my own iPhone 16 Pro. And I own several Macs, several Apple Watches, and an iPad. Each one of those devices, when added to my iCloud account, even just temporarily for testing, generated a notification about the new device being added to my iCloud account to each and every one of my other devices, new or old, currently signed into my iCloud account. That’s a minor annoyance for me as a product reviewer, but of course I wouldn’t have it any other way. Apple’s system is built such that new devices cannot be added to the chain without a notification being generated and sent to every existing device in your account. This notification regarding new devices happens even with standard protection — it’s not exclusive to users who’ve enabled ADP.
So while in theory some company could (I think?) build a system that is fairly (but deceptively) described as “end-to-end encrypted” where one of the “ends” is secretly and silently controlled by the UK government, Apple’s iCloud is not such a system. Apple is prevented by UK law from explaining this, unfortunately, but I think it’s true that as iCloud currently stands, Apple cannot comply with the UK’s demands for ADP-protected accounts, because they can’t add a UK-controlled decryption key to existing iCloud accounts without notifying every device signed into every account. ↩︎



| **Previous:** | [Thoughts and Observations on Today’s iPhone 16e Announcement](https://daringfireball.net/2025/02/thoughts_and_observations_on_todays_iphone_16e_announcement) |
| **Next:** | [The iPhone 16e](https://daringfireball.net/2025/02/the_iphone_16e) |


PreviousNext