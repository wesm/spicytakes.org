---
title: "Regarding Reuters’s Report That Apple Dropped Plan for Encrypting iCloud Backups"
date: 2020-01-21
url: https://daringfireball.net/2020/01/reuters_report_on_apple_dropping_plan_for_encrypted_icloud_backups
slug: reuters_report_on_apple_dropping_plan_for_encrypted_icloud_backups
word_count: 1746
---


[Blockbuster report by Joseph Menn for Reuters](https://www.reuters.com/article/us-apple-fbi-icloud-exclusive-idUSKBN1ZK1CT):


> Apple Inc. dropped plans to let iPhone users fully encrypt backups
> of their devices in the company’s iCloud service after the FBI
> complained that the move would harm investigations, six sources
> familiar with the matter told Reuters.
> The tech giant’s reversal, about two years ago, has not previously
> been reported. It shows how much Apple has been willing to help
> U.S. law enforcement and intelligence agencies, despite taking a
> harder line in high-profile legal disputes with the government and
> casting itself as a defender of its customers’ information.


I want to go deep on this, because, *if true*, it’s staggering, heartbreaking news. [Go read Menn’s entire report](https://www.reuters.com/article/us-apple-fbi-icloud-exclusive-idUSKBN1ZK1CT). I’ll wait.


OK. First, Reuters’ headline — “Apple Dropped Plan for Encrypting Backups After FBI Complained” — is missing one essential word: *iCloud*. For at least the last decade, Apple has offered truly secure encrypted *local* backups of iOS devices, using iTunes on a Mac or PC. (Starting with MacOS 10.15 Catalina, this feature is now in the Finder.) With encrypted local backups, if you don’t have the passphrase used to encrypt the backup, no one, including Apple, can access the backup data. (Local backups to your Mac or PC are *not* encrypted by default — more on this below — and non-encrypted local backups therefore omit sensitive data like your passwords.)


It’s essential that Apple still supports local backups, for many reasons, but for most iPhone and iPad users it’s irrelevant, because they never connect their devices to a Mac or PC, and the overwhelming majority of them surely have no idea that the feature even exists. iCloud backups are the only backups most iOS users ever use, and it is a fact that there is no option to truly encrypt them.


This fact has been, to me, a bit of a head-scratcher for the last few years — it’s the one gaping hole in Apple’s commitment to cryptographically-guaranteed privacy for its customers.1


In fact, it’s so contrary to Apple’s stance as [The Privacy Company](https://www.9to5mac.com/2019/01/05/apple-privacy-billboard-vegas-ces/#) that I’ve already heard from several tech-savvy users today, in the wake of Reuters’s report, that they had assumed until now that their iCloud backups *were* encrypted.


The bottom line is that iCloud backups are not end-to-end encrypted, but should be, at least optionally. Menn’s report for Reuters suggests the reason they’re not is that Apple bowed to requests from the FBI. I do not believe his report is entirely correct. Menn writes:


> More than two years ago, Apple told the FBI that it planned to
> offer users end-to-end encryption when storing their phone data on
> iCloud, according to one current and three former FBI officials
> and one current and one former Apple employee.
> Under that plan, primarily designed to thwart hackers, Apple would
> no longer have a key to unlock the encrypted data, meaning it
> would not be able to turn material over to authorities in a
> readable form even under court order.
> In private talks with Apple soon after, representatives of the
> FBI’s cyber crime agents and its operational technology division
> objected to the plan, arguing it would deny them the most
> effective means for gaining evidence against iPhone-using
> suspects, the government sources said.
> When Apple spoke privately to the FBI about its work on phone
> security the following year, the end-to-end encryption plan had
> been dropped, according to the six sources. Reuters could not
> determine why exactly Apple dropped the plan.


Menn is a solid reporter and I have no reason to doubt what he is reporting. What I suspect though, based on (a) everything we all know about Apple, and (b) my own private conversations over the last several years, with rank-and-file Apple sources who’ve been directly involved with the company’s security engineering, is that Menn’s sources for the “Apple told the FBI that it planned to offer users end-to-end encryption when storing their phone data on iCloud” bit were the FBI sources, not the Apple sources, and that it is not accurate.


It simply is not in Apple’s nature to tell *anyone* outside the company about *any* of its future product plans. I’m not sure how I could make that more clear. It is not in Apple’s DNA to ask permission for anything. (Cf. the theory that a company’s culture is permanently shaped by the personality of its founders.)


Encrypting iCloud backups would be perfectly legal. There would be no legal requirement for Apple to brief the FBI ahead of time. Nor would there be any reason to brief the FBI ahead of time just to get the FBI’s opinion on the idea. We all know what the FBI thinks about strong encryption. How would this supposed conversation have gone down?


***FBI Official**: So, what brings you here?*


***Apple Representative**: Well, we’re thinking about offering encrypted iCloud backups, such that only the user would hold the keys.*


***FBI Official**: ——*


***Apple Representative**: And, uh, we were wondering what you folks thought about that.*


***FBI Official**: Is this a joke?*


I would find it less surprising to know that Apple acquiesced to the FBI’s request not to allow encrypted iCloud backups than that Apple briefed the FBI about such a plan before it was put in place.


I’ll take as fact all of the following, based on Menn’s report and common sense:

1. Apple had and perhaps still has a plan to encrypt iCloud
backups in a way that only the user controls the keys. I.e.
that without the backup passphrase, there would be no way for
Apple to access the data contained in the backup.
2. The FBI has requested that Apple not offer encrypted iCloud
backups. I would be surprised if the FBI does not reiterate its
stance on this issue whenever they meet with Apple regarding
security matters. Apple might never have mentioned a plan to
encrypt iCloud backups, but the FBI isn’t stupid. It has surely
occurred to anyone who has followed Apple’s progress on
security — which to date has only ever moved in the direction
of providing customers with more cryptographically-guaranteed
privacy — that encrypted iCloud backups are something the
company has at the very least *considered*.
3. Apple cancelled or postponed its plan to offer encrypted iCloud
backups.


*It does not necessarily follow that #3 is the result of #2.*


It *could* be the reason, but there are several other logical explanations. It’s a subtle point, but the “due to” in VentureBeat’s headline on Reuter’s syndicated report — “[Apple’s iCloud Backups Are Unencrypted Due to Law Enforcement Pressure](https://venturebeat.com/2020/01/21/apples-icloud-backups-are-unencrypted-due-to-law-enforcement-pressure/)” — is not justified by the reporting. (Reuters’s original headline uses “after”.)


I’ll repeat the last line of the previous quote from Menn’s report:


> Reuters could not determine why exactly Apple dropped the plan.


Dueling sources follow:


> “Legal killed it, for reasons you can imagine,” another former
> Apple employee said he was told, without any specific mention of
> why the plan was dropped or if the FBI was a factor in the
> decision.
> That person told Reuters the company did not want to risk being
> attacked by public officials for protecting criminals, sued for
> moving previously accessible data out of reach of government
> agencies or used as an excuse for new legislation against
> encryption.
> “They decided they weren’t going to poke the bear anymore,” the
> person said, referring to Apple’s court battle with the FBI in
> 2016 over access to an iPhone used by one of the suspects in a
> mass shooting in San Bernardino, California.


If that is the case — that Apple’s legal department killed the project to avoid “poking the bear” — then it’s ultimately irrelevant whether Apple briefed the FBI in advance or not. It’s acquiescence, and users will be left unprotected. Not just in the U.S., where the FBI has jurisdiction, but *everywhere in the world* where encryption is legal.


Menn’s FBI sources clearly think that’s the case:


> Two of the former FBI officials, who were not present in talks
> with Apple, told Reuters it appeared that the FBI’s arguments that
> the backups provided vital evidence in thousands of cases had
> prevailed.
> “It’s because Apple was convinced,” said one. “Outside of that
> public spat over San Bernardino, Apple gets along with the federal
> government.”


What else could it be? This:


> However, a former Apple employee said it was possible the
> encryption project was dropped for other reasons, such as concern
> that more customers would find themselves locked out of their data
> more often.


That’s a key point. Surely there are hundreds, maybe thousands, of people every day who need to access their iCloud backups who do not remember their password. The fact that Apple can help them is a benefit to those users. That’s why I would endorse following the way local iTunes device backups work: make encryption an option, with a clear warning that if you lose your backup password, no one, including Apple, will be able to restore your data. I would be surprised if Apple’s plan for encrypted iCloud backups were not exactly that.


Buried deep in the article is, to me, the most alarming aspect of Menn’s report:


> Once the decision was made, the 10 or so experts on the Apple
> encryption project — variously code-named Plesio and KeyDrop — were told to stop working on the effort, three people familiar
> with the matter told Reuters.


The proof of the pudding is in the eating — let’s see what Apple actually does. 
Reuters’s report notwithstanding, I would not be surprised if end-to-end encrypted iCloud backups are forthcoming. This should be at the top of our list of hoped-for features at WWDC 2020.


This isn’t about Apple foiling law enforcement. It isn’t about Apple helping criminals. It’s about Apple enabling its customers to own and control their own data. As things stand, if you use iCloud backup, you do not own and control the data therein.


---

1. Email is another gaping hole. But that’s how email works everywhere — it’s inherently insecure by design. Read [this 2013 piece by Geoff Duncan](https://www.digitaltrends.com/computing/can-email-ever-be-secure/) for a cogent explanation. ↩︎



| **Previous:** | [Quit Confirmation for Safari on MacOS](https://daringfireball.net/2020/01/quit_confirmation_for_safari_on_macos) |
| **Next:** | [Hacked to Bits](https://daringfireball.net/2020/01/hacked_to_bits) |


PreviousNext