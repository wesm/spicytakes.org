---
title: "On the San Bernardino Suspect’s Apple ID Password Reset"
date: 2016-02-21
url: https://daringfireball.net/2016/02/san_bernardino_password_reset
slug: san_bernardino_password_reset
word_count: 1071
---


The latest news in the Apple-FBI legal fight has resulted in much confusion. [John Paczkowski, reporting for BuzzFeed](http://www.buzzfeed.com/johnpaczkowski/apple-terrorists-appleid-passcode-changed-in-government-cust):


> The FBI has [claimed](https://assets.documentcloud.org/documents/2716011/Apple-iPhone-Access-MOTION-to-COMPEL.pdf) that the password was changed by someone at
> the San Bernardino Health Department. Friday night, however,
> things took a further turn when the San Bernardino County’s
> official Twitter account [stated](https://twitter.com/CountyWire/status/700887823482630144), “The County was working
> cooperatively with the FBI when it reset the iCloud password at
> the FBI’s request.”
> County spokesman David Wert told BuzzFeed News on Saturday
> afternoon the tweet was an authentic statement, but he had nothing
> further to add.
> The Justice Department did not respond to requests for comment on
> Saturday; an Apple spokesperson said the company had no additional
> comment beyond prior statements.


[Here is what the FBI wrote in its legal motion](https://assets.documentcloud.org/documents/2716011/Apple-iPhone-Access-MOTION-to-COMPEL.pdf), in a footnote on the four ways Apple suggested they obtain the data they seek:


> (3) to attempt an auto-backup of the SUBJECT DEVICE with the
>     related iCloud account (which would not work in this case
>     because neither the owner nor the government knew the password
>     the iCloud account, and the owner, in an attempt to gain
>     access to some information in the hours after the attack, was
>     able to reset the password remotely, but that had the effect
>     of eliminating the possibility of an auto-backup);


To unpack this, the “owner” is *not* Syed Farook, the shooter. The iPhone at the center of this was supplied by Farook’s employer, the San Bernardino County Department of Public Health. They are the “owner”. The “government” is the federal government: the FBI and the Department of Justice.


The iPhone had been configured to back up to iCloud. However, at the time of the attack, it had not been backed up to iCloud for six weeks. Under warrant, Apple supplied the FBI with the data from that six-week-old backup. The FBI (for obvious reasons) would like the most recent six weeks of data from the phone, too.1


iCloud backups are triggered automatically when the phone is (a) on a known Wi-Fi network, and (b) plugged-in to power. Apple’s suggestion to the FBI was that if they took the iPhone to Farook’s office and plugged it in, it might trigger a backup. If that had worked, Apple could supply the FBI with the contents of that new backup, including the most recent six weeks of data.


It is not clear to me from any of the reports I have read *why* the iPhone had not been backed up in six weeks. It’s possible that Farook had disabled iCloud backups, in which case this whole thing is moot.2 But it’s also possible the only reason the phone hadn’t been backed up in six weeks is that it had not been plugged-in while on a known Wi-Fi network in six weeks. The phone would have to be unlocked to determine this, and the whole point of this fight is that the phone can’t be unlocked.


The FBI screwed this up by directing the San Bernardino County Department of Public Health to reset Farook’s Apple ID password. *They did not, and apparently could not, change anything on the phone itself.* But once they reset the Apple ID password, the phone could not back up to iCloud, because the phone needed to be updated with the newly-reset Apple ID password — and they could not do that because they can’t unlock the phone.


The key point is that you do not have to unlock an iPhone to have it back up to iCloud. But a locked iPhone *can’t* back up to iCloud if the associated Apple ID password has been changed.


Again, there are two password-type things at play here. The Apple ID (iCloud) password, and the four-digit device passcode locking the iPhone. The county, at the behest of the FBI, reset the Apple ID password. This did not allow them to unlock the iPhone, and, worse, it prevented the iPhone from initiating a new backup to iCloud.


*How* did the county reset Farook’s Apple ID password? We don’t know for sure, but the most likely answer is that if his Apple ID was his work-issued email account, then the IT department at the county could go to [iforgot.apple.com](https://iforgot.apple.com/), enter Farook’s work email address, and then access his email account to click the confirmation URL to reset the password.


In short:

- The data the FBI claims to want is on Farook’s iPhone.
- They already have access to his iCloud account.
- They might have been able to transfer the data on his iPhone to his iCloud account via an automated backup, but they can’t because they reset his Apple ID (iCloud) password.


The only possible explanations for this are incompetence or dishonesty on the part of the FBI. Incompetence, if they didn’t realize that resetting the Apple ID password could prevent the iPhone from backing up to iCloud. Dishonesty, if they directed the county to do this *knowing* the repercussions, with the goal of setting up this fight to force Apple to create a back door for them in iOS. I’m not sure which to believe at this point. I’d like to know exactly when this directive to reset the Apple ID password was given — ” in the hours after the attack” leaves a lot of wiggle room.


---

1. Much (or all?) of the data stored on Apple’s iCloud backup servers is not encrypted. Or, if it is encrypted, it is encrypted in a way that Apple can decrypt. [Apple has a PDF that describes the information](http://images.apple.com/privacy/docs/legal-process-guidelines-us.pdf) available to U.S. law enforcement from iCloud, but to me it’s not clear exactly what is available under warrant. I would bet a large sum of money that Apple is hard at work on an iCloud backup system that *does* store data encrypted in a way that Apple cannot read it without the user’s Apple ID password. ↩︎
2. Another possibility: Farook’s iCloud storage was full. If this were the case, presumably Apple could have granted his account additional storage to allow a fresh backup to occur. But again, this became moot as soon as the county reset the Apple ID password at the behest of the FBI. ↩︎︎



| **Previous:** | [Apple’s App Problem](https://daringfireball.net/2016/02/apples_app_problem) |
| **Next:** | [Brief Thoughts and Observations Regarding Today’s ‘Loop You In’ Apple Event](https://daringfireball.net/2016/03/thoughts_and_observations_loop_you_in) |


PreviousNext