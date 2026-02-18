---
title: "Hacked to Bits"
date: 2020-01-26
url: https://daringfireball.net/2020/01/hacked_to_bits
slug: hacked_to_bits
word_count: 1539
---


Another blockbuster security story last week, [initially broken by Stephanie Kirchgaessner for The Guardian](https://www.theguardian.com/technology/2020/jan/21/amazon-boss-jeff-bezoss-phone-hacked-by-saudi-crown-prince):


> The Amazon billionaire Jeff Bezos had his mobile phone “hacked” in
> 2018 after receiving a WhatsApp message that had apparently been
> sent from the personal account of the crown prince of Saudi
> Arabia, sources have told the Guardian.
> The encrypted message from the number used by Mohammed bin Salman
> is believed to have included a malicious file that infiltrated the
> phone of the world’s richest man, according to the results of a
> digital forensic analysis.
> This analysis found it “highly probable” that the intrusion
> into the phone was triggered by an infected video file sent
> from the account of the Saudi heir to Bezos, the owner of the
> Washington Post.
> The two men had been having a seemingly friendly WhatsApp exchange
> when, on 1 May of that year, the unsolicited file was sent,
> according to sources who spoke to the Guardian on the condition of
> anonymity.
> Large amounts of data were exfiltrated from Bezos’s phone within
> hours, according to a person familiar with the matter. The
> Guardian has no knowledge of what was taken from the phone or how
> it was used.


You will recall that [The National Enquirer published intimate text messages and personal photographs from Bezos that revealed an extramarital affair](https://www.wsj.com/articles/how-the-national-enquirer-got-bezos-texts-it-paid-200-000-to-his-lovers-brother-11552953981), which in turn led to Bezos and his wife of 25 years [divorcing](https://www.washingtonpost.com/arts-entertainment/2019/01/09/jeff-bezos-announces-divorce-mackenzie-bezos-after-years-together/).


Bezos unsurprisingly launched his own investigation into how the text messages and photos had been stolen from his phone and wound up in the hands of the Enquirer. According to Bezos’s team, early evidence pointed to Saudi Arabia. That Bezos’s investigators had evidence pointing to the Saudis spooked Enquirer publisher David Pecker enough that Pecker literally attempted to extort Bezos — offering not to publish additional photos in the Enquirer’s possession in exchange for Bezos dropping his investigation. Needless to say, Bezos told Pecker to fuck off, in [a remarkably cogent open letter](https://medium.com/@jeffreypbezos/no-thank-you-mr-pecker-146e3922310f) publicly revealing both the extortion scheme and Bezos’s investigative team’s suspicion that the Saudis were the culprits.1


At the time, there was much speculation as to *how* the Saudis hacked Bezos’s phone. Did they have agents intercepting his cellular signal? Technically possible, perhaps, especially if the text messages were SMS (we still don’t know what type of “texts” they were — we now know Bezos and MBS texted via WhatsApp, but we don’t know how Bezos and his girlfriend texted), but if the Saudis had in fact captured the information over the air, how would Bezos’s investigators ever have detected it months after the fact?


Now, [we seemingly know](https://www.vice.com/en_ca/article/v74v34/saudi-arabia-hacked-jeff-bezos-phone-technical-report). Bezos had a personal relationship with MBS and [MBS personally sent Bezos the payload to exploit his phone](https://www.nytimes.com/2020/01/22/technology/jeff-bezos-hack-iphone.html). The evidence is strong enough and the allegations serious enough that the United Nations [has issued a report on the matter](https://www.ohchr.org/Documents/Issues/Expression/SRsSumexFreedexAnnexes.pdf), considers it part of a pattern of human rights violations from the Saudi regime, and [is calling for the United States to further investigate](https://www.ohchr.org/EN/NewsEvents/Pages/DisplayNews.aspx?NewsID=25488&LangID=E).


But — *but!* — two days ago, The Wall Street Journal reported that federal prosecutors in Manhattan have evidence that The National Enquirer [obtained the photos from Lauren Sanchez’s brother](https://www.wsj.com/articles/prosecutors-have-evidence-bezos-girlfriend-gave-texts-to-brother-who-leaked-to-national-enquirer-11579908912), who in turn was sent them from his sister’s phone. Whether Lauren Sanchez sent them to her brother, or her brother had access to her phone and sent them to his phone from her phone himself, is unclear, but the fact that [Bezos and Sanchez are still together](https://www.scmp.com/lifestyle/fashion-beauty/article/3046795/jeff-bezos-makes-wild-fashion-statement-girlfriend-lauren) suggests Bezos believes the latter. It seems entirely possible that the Saudis [pwned](https://www.urbandictionary.com/define.php?term=pwned) Bezos’s phone but that it was his girlfriend’s brother who betrayed them to The Enquirer. Or, more conspiratorially, perhaps her brother — a prominent Trump supporter with ties to the [recently convicted felon and Trump advisor Roger Stone](https://www.theatlantic.com/politics/archive/2019/11/roger-stones-long-history-in-trump-world/581293/), a man who describes himself as a “dirty trickster” — was in cahoots with the Saudis and the Enquirer to cover their tracks.


This whole saga is extraordinary to say the least. With zero hyperbole, it sounds like the pitch for a Hollywood thriller:


*The richest man in the world — a billionaire a hundred times over — meets and exchanges phone numbers with the crown prince of Saudi Arabia, the most powerful dictator in the Middle East. The richest man in the world happens to own, as a mere side business, The Washington Post — a newspaper whose news coverage and opinion columns have been highly critical of the Saudi Arabian royal family’s brutal and regressive regime. The crown prince uses this superficial personal relationship with the richest man in the world to hack his phone via an infected attachment sent in a WhatsApp chat, using military-grade technology [seemingly created by NSO Group](https://www.businessinsider.com/jeff-bezos-phone-hacked-saudi-crown-prince-mbs-report-explained-2020-1), a secretive firm from Israel that supposedly only offers its services to trusted governments. Among the information the Saudis exfiltrate from the richest man in the world’s phone are text messages and intimate photos revealing an extramarital affair, which wind up published in The National Enquirer, whose publisher has long been a trusted confidant of the corrupt president of the United States, and had a stack of scandalous stories regarding said corrupt president’s own extra-marital affairs [locked in a safe](https://www.theguardian.com/us-news/2018/aug/24/national-enquirer-kept-files-in-safe-on-trump-hush-money-payments) as part of a decades-long conspiracy to keep those scandals out of the public eye. Said corrupt president of the United States is also a vociferous critic of The Washington Post and its owner, the richest man in the world. The publication of these intimate texts and photos leads to the dissolution of the richest man in the world’s 25-year marriage, and unsurprisingly angers him, leading him to hire a team of investigators to figure out how the texts and images from his phone were stolen. A few months later a team of Saudi agents [brutally murders and dismembers Saudi dissident Jamal Khashoggi](https://www.nytimes.com/2018/10/17/world/europe/turkey-saudi-khashoggi-dismember.html) — who was — wait for it — a journalist at The Washington Post whose columns were scathingly critical of the Saudi regime. The CIA soon determines that the Saudi hit team was acting at the direct behest of the crown prince; when informed of this, the corrupt president of the United States brushes it off with a more-or-less “Shit happens, what do you expect when you criticize our friends the Saudis? Those guys play hardball.” response.*


*Oh. And the corrupt president of the United States is also a nepotist. His  son-in-law is a senior White House advisor with a sprawling portfolio of responsibilities, a top-secret security clearance that was granted only because the president demanded it ([overriding concerns of national security officials](https://www.cnn.com/2019/03/23/politics/kushner-whatsapp-concerns/index.html)). Said son-in-law is known to communicate with the crown prince of Saudi Arabia [via — wait for it — WhatsApp](https://www.cnn.com/2019/03/23/politics/kushner-whatsapp-concerns/index.html).2*


I take it back, this is not the pitch for a movie. It’s the pitch for a season-long TV series. My proposed title: *Hacked to Bits*.


---

1. Bezos, in his 2017 letter to shareholders: “We don’t do PowerPoint (or any other slide-oriented) presentations at Amazon. Instead, we write narratively structured six-page memos. We silently read one at the beginning of each meeting in a kind of ‘study hall.’ ”
The idea is that lazy thinking, if not outright sophistry, is easily disguised within slide decks, but narrative prose — not bullet points but a real narrative — forces the writer to think everything through. Writing is thinking, I’ve always thought, too. I frequently start a column thinking my argument is A, but as I write, I realize I was wrong and in fact my argument is Z. It’s the act of writing that forces you to think the idea through right down to the bedrock. Anyway, Bezos’s open letter revealing the Enquirer’s scheme and his suspicion that the Saudis were the culprits shows that, unsurprisingly, he’s a remarkably cogent writer. [Reminds me](https://www.apple.com/hotnews/thoughts-on-flash/) of [someone else](https://daringfireball.net/2007/02/reading_between_the_lines). ↩︎
2. I actually think it’s unlikely that MBS hacked Kushner’s phone. Think about it. The hack of Bezos’s phone was eventually uncovered. If he hacked Kushner, it would have come out eventually too. Trump is embarrassingly cozy with the Saudis, but he would surely be furious if it were revealed the Saudis hacked Kushner’s phone. However useful hacking Kushner’s phone would be to their intelligence gathering, it couldn’t possibly be worth spoiling their relationship with Trump. Killing and dismembering a journalist working for The Washington Post ought to outrage the president. Hacking the phone of an American citizen — any American, prince or pauper — ought to outrage the president. But hacking the phone of someone in his family actually would. Trump’s strident antipathy toward Bezos effectively served as a free pass for the Saudis to hack his phone. That the United Nations is more outraged than the United States says it all.
But, still, the fact that it’s even possible that MBS did the same thing to Kushner that he did to Bezos — combined with the fact that security officials in the U.S. [were alarmed by Kushner’s use of WhatsApp all along](https://www.cnn.com/2019/03/23/politics/kushner-whatsapp-concerns/index.html) — is deeply concerning, to say the least. ↩︎︎



| **Previous:** | [Regarding Reuters’s Report That Apple Dropped Plan for Encrypting iCloud Backups](https://daringfireball.net/2020/01/reuters_report_on_apple_dropping_plan_for_encrypted_icloud_backups) |
| **Next:** | [The iPad Awkwardly Turns 10](https://daringfireball.net/2020/01/the_ipad_awkwardly_turns_10) |


PreviousNext