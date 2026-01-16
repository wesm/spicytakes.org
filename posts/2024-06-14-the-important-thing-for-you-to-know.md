---
title: "The important thing for you to know is that it’s not my fault"
subtitle: "It’s a shame that things didn’t work out, but I can’t be blamed for that. Plus, introducing Attention numbers, the best way to value your startup."
date: 2024-06-14T16:49:11+00:00
url: https://benn.substack.com/p/the-important-thing-for-you-to-know
slug: the-important-thing-for-you-to-know
word_count: 3057
---


![](https://substackcdn.com/image/fetch/$s_!0fS8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff33c02e5-21cb-4fab-bf3d-4c07176a5571_1600x814.png)

*“Look, I’m fired.I know I’m fired. But that was not my fault. Y’all are trash. Ticketmaster, you trash. Santander, you trash. Advanced Auto Parts, listen to me when I say this, you are trash.”*


We are, here atInitech, very sorry that your money is gone. We are sorry that the email addresses and credit card numbers you gave us were sold off down by the docks, and that some Russian hackers stole your identity. The security and confidentiality of your data isour number one priorityat Initech, and it is a shame that your information has been compromised. Our team of experts will be happy to assist you in any way we can (provided that you are on our Enterprise or Enterprise+ tier).


But it is also important to understand that none of this is our fault. Security iscore to our businessandour platform; it isbuilt into every layerof our product. Our companyruns on trust,customer trust,your trust, and we take that responsibility very seriously. Our software issecure by default. It isindustry-leading,enterprise-grade,state-of-the-art,end-to-end,world-class. We have manybadges,certifications,accreditations, andacronyms—TLS 1.2, AES-256, SOC 2, ISO 27001, GDPR, CCPR, GxP, ITAR, IL5 DoD SRG, etc—that demonstrate how we treat your data asif it were our data.


So look. We did our part. But if you put50,000 dollars in a shoeboxand hand it to a stranger in a black SUV, that is not on us. If youfell for a phishing emailand sent your Gmail password toFancy Bear,1you messed up, not us. And if you usesimple passwordsand don’t enable multi-factor authentication on your account—which, of course, we strongly recommend that you do—there is only so much we can do to protect you. We make the locks, they are good locks, and we can’t be blamed if you don’t use them properly.


Because we useourlocks properly. We havemany reportsfrom outside auditors that confirm this. We have a chief security officer; we have an official “data protection officer.” We maintain a list of 224SOC-2 “controls”—password policies for our company Slack, code review standards for our engineers, regular security training programs for employees, a Dropcam in our office, and many others—that are carefully tracked and tediously documented.2


Still, because we are committed totransparent communication, we commissioned an independent investigation to figure out how your money was stolen. Third-party cybersecurity experts found no evidence of a breach of Initech, our systems, or our employees. Instead, your money was stolen because of compromised customer credentials; i.e., someone stole your password; i.e.,PEBCAK; i.e., askill issue; i.e, you, not us. You gave your debit card and PIN number to a thief; don’t blame the ATM.


In conclusion, we did our job. It’s a shame that this bad thing happened, and we are unhappy about it and all of that. But the most important thing for you to understand here is that it’s not our fault.


—


A couple weeks ago, some hackersstole a bunch of data out of Snowflake:


> Security researchers say they believe financially motivated cybercriminals have stolen a “significant volume of data” from hundreds of customers hosting their vast banks of data with cloud storage giant Snowflake.Incident response firm Mandiant, which is working with Snowflake to investigate the recent spate of data thefts, said in a blog post Monday that the two firms have notified around 165 customers that their data may have been stolen.


Snowflake, as part of theircommitment to transparency, hired third-party cybersecurity experts CrowdStrike and Mandiant to investigate the hack; they “have not identified evidence suggesting this activity was caused by a vulnerability, misconfiguration, or breach of Snowflake’s platform” or “by compromised credentials of current or former Snowflake personnel;” they said itwascaused “compromised customer credentials” that were “exposed through unrelated cyber threat activity;” theystrongly recommendthat all account administrators use multi-factor authentication to protect their accounts.


In other words, Snowflake says that they did what any reasonable cloud software vendor would be expected to do. And while it is unfortunate that this happened, the important thing to know is that it wasn’t their fault.


—


But was it? Was Snowflake to blame? Their customers? Nobody but the hackers themselves? What exactly are we supposed to make of this whole thing?3


On one hand, by all accounts, it doesn’t seem like Snowflake did anything capital-W Wrong. They followed the protocols that they were supposed to follow; they built software according to the standards they were supposed to meet; no Snowflake employee stole anything, left a door open, or told somebody something they shouldn’t have.4They were an ATM, and someone stole their customers’ PINs. Itishard to blame the ATM for that.


On the other hand, Snowflake did, in a sense, make the ATM popular. Twenty years ago, most databases lived behind firewalls and were only available via VPNs or from approved IP addresses. Corporate data was, almost literally, in a locked vault that you had to physically break into to steal. Today, in part because of Snowflake’s success and its own effortsmarketing the benefits of the cloud, people can log into their databases like they would any other website, througha publicly-accessible web page,5with a username and password. Snowflake also helped popularize using basic authentication methods like usernames and passwords as themodernstandardbywhichdataproductsconnecttodatabases.


In essence, Snowflake and other cloud warehouse vendors moved data out of the firewalled vaults, and into ATMs all over the internet. That’s a design pattern that is fundamentally more vulnerable to certain types of hacks than the prior version.6Accordingly,most criticisms of Snowflakearen’t just about Snowflake, but about problems inherent in SaaS software: That simple single-factor authentication is simple to hack. When money is in a bank, you have to rob the bank to get it out. When money is an ATM, you just need to steal some debit cards and phish for people’s PINs.7


But! It’s also a design pattern that we like! ATMsareconvenient. Multi-factor authenticationisannoying. The convenience of the cloud and putting everything on the internet is the world we asked for—and so, it’s a world that Snowflake can give us, without violating any generally accepted accessibility protocols. In 2000, had a company built a database that you could log into from a website and with the password “password,” we would probably blame that company if its customers’ accounts got hacked. Now, eh—we may not exonerate the company completely, but we put a lot of the blame on the customers themselves.


That’s the thing about data breaches, and about the entire software security industrial complex: It’s not about security; it’s aboutblame.


Most companies don’t get have lengthy security pages and pay for tedious compliance reports because they believe that jumping through a bunch of bureaucratic hoops, like logging when every employee was added or removed from Asana, will make anything meaningfully more secure; they jump through those hoops and get those reports so that, if something does go wrong, they can say that it’s not their fault.8The probability that companies want to minimize is not the probability of a hack; they want to minimize the probabilitythat they get blamed for a hack.9Compliance standards aren’t about security; compliance standards are about liability.10And in the two-decade long transition to the cloud, we’ve come to shift the liability for things likebad password policiesonto the users and not the vendors.


That’s the bet Snowflake made in making things like multi-factor authentication optional—that they ultimately wouldn’t be blamed for a hack like this. As the story escalated,11they’ve added the reverseStreisand: Turn a mountain into a molehill by largelydoing as little press as possible,12and hope the whole thing blows over. Which probably isn’t a bad strategy, at least for the time being. If the important thing is for people not to think that it’s your fault—and in cloud software security, that is andalways has beenthe important thing—you can’t get blamed for something that nobody’s talking about.


---


# Blame, again


There’s also a broader point here. The entire corporate cybersecurity apparatus is designed to preemptively make the case that whatever went wrong isn’t our fault. But we don’t just do that with security policies. We pre-build this argument—that the important thing for you to know is that it’s not my fault—all the time, and are as frequently motivated by it as we are whatever problem we’re ostensibly trying to solve.


For example, when a controversial decision is being made, people will often softly object. They won’t want tochangethe decision, because then, if something bad happens, itwillbe their fault. Instead, they will just want to object “for the record”—a record that will likely get forgotten if things go well, but they’ll definitely remember if things go poorly.


For example, when an investor invests in a startup, they will sometimes push CEOs to make certain decisions. They will nudge, cajole, and coerce—but almost never outright instruct. Because they aren’t here to make decisions; they’re here to advise and support. If that advice works out, great, they’re adding value. And if it doesn’t, well, that’s not their fault. The CEO makes the decisions.


For example, when an executive asks a data team for some sort of analysis, they’re asking for counsel, but they’re also often asking for a contingency.If the decision goes well, “you can claim credit for your cleverness. If it doesn’t, you can say you just did what any reasonable person would’ve done,” and listened to the data. I played the numbers, and it’s not my fault that we got unlucky.


Everyone will say that the important thing iswinning as a team. And in good times, sure, it is. But people are always looking for ways to buy themselves an insurance policy, becausein bad times, the important thing for you to understandis that it isn’t my fault.


---


# Cloud security, again


When stories like the one about Snowflake come out, the first reaction is usually to point fingers. The second is bewilderment: How could they let this happen? How could they have been so unusually careless?


Which, oh man, if only. Every tech company presents themselves like Initech, as very serious experts who build bleeding-edge security programs with militaristic discipline. And maybe a few do. But most tech companiesare FTX: Full of loose access controls, everything passed around Slack, held togetherby Scotch tape and bubble gum.


Back sometime before the pandemic, the team at Mode used a popular product—let's call itPodesData—that connected directly to Snowflake, which we were using as our primary data warehouse. PodesData had to interact with our data, and was was authorized to do it in the same way as just about every other tool that connects to Snowflake: We created a new Snowflake user called something like THIRD_PARTY_PODESDATA, granted that user access to the data is that PodesData needed to see, and provided that users’s password to PodesData, via some web form inside of their application.


A few months later, we had some mundane technical issue that we needed help fixing. We emailed their support team, and an agent started investigating different things that might’ve gone wrong. At some point during the conversation, the agent emailed us a screenshot of what they were seeing “on their side.” The screenshot was of a query the agent had written, directly against our Snowflake database, frominside the Snowflake console.


We lost our minds. Because the existence of this screenshot meant three things:

1. The support agent had logged into the Snowflake app with the username and password we gave PodesData. That implied our database password wasn’t locked in some encrypted vault, but was out in the open, available to any enterprising support agent who thought it would be useful to poke around.
2. Once they logged in, the agent had manually written a query and looked at the results. In the screenshot, they were looking at the data we were trying to debug, but they could’ve written whatever query they wanted. They were in our house, and could open whatever drawers they wanted.
3. This had all happened because of an unremarkable issue for an unremarkable customer. A front-line support agent wrote the query. Our ticket hadn’t been escalated to PodesData’s senior staff; the problem wasn’t urgent. This practice, of copying plaintext passwords, logging into customer accounts, and looking at whatever data they deemed useful, wasn’t an exception in an emergency. It was, by all appearances, standard procedure.


We threw a tantrum, canceled our contract on the spot, and migrated to a competitor within a few days. But, while this was bad, it wasn't exactlysurprising. If you work around startups for a while—or for a few weeks, really—you’ll see dozens of these stories. Of data being passed around encrypted thumb drives. Of passwords accidentally posted in public Github repos. Of unsecured laptops being left at coffee shops. Of every employee having access to production databases that, as we were told by PodesData, they are instructed but technically not required to get permission to use.


Every SaaS company has carefully-worded security policies that are written by lawyers. And then they have lived security policies, which are usually “most people don’t know how to write SQL, so it’s probably fine.”


---


# Attention numbers


I mean,it wasan acquihire, right?


For the second year in a row, Databricks announced a billion-dollar acquisition on the first day of their biggest rival’s annual conference.13In 2023, Databricks acquired MosaicML, then a two-year old startup that was makinga few million dollars a yearin revenue, for $1.3 billion. This year, Databricks boughtTabular, which is a piece of database middleware that was attempting to turn an open-source data format into a product, forbetween one and two billion dollars.


Neither deals were traditional nine-figure tech acquisitions, in which an acquirer is looking to buy a mature product, customers, and a revenue stream. Instead, they were both about hiring teams. In MosaicML, Databricks bought a bunch of experienced AI researchers (and some GPUs) in a bet that everyenterprise will eventually want to train their own LLM. In Tabular, Databricks bought the architects of a popular open-source framework. When Databricks announced the acquisition,they made absolutely no mentionof the Tabular product, its business, or anything that had been created from the day after its founding. By all appearances, Databricks wasn’t interested in the company, its customers, its community, or even a single line of its code. What they wanted was “the original Iceberg team.”


That’s how the world seems to work in theAI Upside Downwe’re currently living in. Acquihires are no longer soft landings; they’re were all the money is.


Because businesses can be valued in two ways: Based on their business fundamentals, or based on talent and hype. If you’re valued based on your business,it’s brutal out there. Revenue multiples are at historic lows, and investors punishing companiesthat are growing slowly.


But for companies that are are judged based on their teams, their valuations are effectively uncapped. A viral AI company founded bygold-medalist engineersis worth2 billion dollars in six months. Another AI startup that has a bunch of employees with lowErdos numbersto “Attention is All You Need” (Attention numbers? I don’t know)raised 220 million dollarsless than a year after being founded. A company that builds aJeff Dunham puppetas a chatbot (and is definitely going to getsued by Tesla shareholders) is worth18 billion dollars, because Elon Musk.


As always,Russ Hanneman was right: If you show revenue, people will ask how much, and it will never be enough. But if you have no revenue, you can be a pure AI play. And right now, no multiple is higher than the Attention number multiple.

[1](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-1-145645344)

Aka APT28 aka Pawn Storm aka Sofacy Group aka Sednit aka Tsar Team aka STRONTIUM aka Forest Blizzard aka GRU Unit 26165.

[2](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-2-145645344)

Well, sorta, we actuallybought some softwarethat did most of it for us in a few weeks. But the important thing is thatwe have the certificate, right?

[3](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-3-145645344)

Are we allowed to even ask this question?

[4](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-4-145645344)

This isn’t entirely true. An internal account that Snowflake used for customer demos was compromised, because a Snowflake employee appears to have fallen victim to the same hacking campaign that Snowflake’s customers did. However, the information in that internal account wasn’t, it appears, used to hack into any other Snowflake accounts. It’s as though the hackers stole a bunch of PIN numbers from a bank’s customers, including the PIN number for one of the bank’s corporate checking accounts. It’s not a great look, but that PIN number didn’t give them access to anyone else’s PIN numbers.

[5](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-5-145645344)

Username: zuck. Password:dadada. No dice.

[6](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-6-145645344)

Roughly, there are two types of vulnerabilities: Technical and social. Technical hacks are those that outwit the code itself—it’s like cracking a safe with a drill or byBeautiful Minding the way the safe feels. Social hacks are those that exploit people, like convincing someone that you’re their boss and you need them to send you their email password. Snowflake, and cloud software in general, is probably moretechnicallysecure than most self-hosted databases and applications, just as an ATM is probably more physically secure than a safe in someone’s house. But they are almost certainly lesssociallysecure, because all hackers need to do is convince someone to give them their password in something like a fake password reset email.

[7](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-7-145645344)

Although, for debit cards, you don’t even need to do that. You can just use “1234,” and you’ll be right11 percent of the time.

[8](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-8-145645344)

Compliance reports also serve the same function for customers. If a vendor gets hacked, the person who bought the software wants to be able to say it’s not their fault either. When Ticketmaster’s CEO calls their CIO into their office and askshow they could’ve let this happen, the CIO can say they did their diligence; Snowflake had all of the right credentials;  blamethem.

[9](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-9-145645344)

Imagine that the CEO of a software company has two dials in front of them. One controls the likelihood that their customers’ money and data gets stolen; the other controls the likelihood their company gets blamed for money and data being stolen. Nearly every CEO would set the first dial to 100 percent and the second dial to zero percent before they set both dials to one percent.

[10](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-10-145645344)

Although sometimes, it’s about marketing. DoesApple really carethat deeply about your privacy? DoesElon Musk? Probably not. But they can sell privacy as a brand.

[11](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-11-145645344)

No. I refuse.

[12](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-12-145645344)

They have to do some press, because there are often legal and contractual requirements to disclose these sorts of breaches.

[13](https://benn.substack.com/p/the-important-thing-for-you-to-know#footnote-anchor-13-145645344)

It’s so petty.I love it.
