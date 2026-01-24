---
title: "Software Internationalization, SIMS Style"
date: 2007-03-09
url: https://blog.codinghorror.com/software-internationalization-sims-style/
slug: software-internationalization-sims-style
word_count: 967
---

Internationalization of software is incredibly challenging. Consider this [Wikipedia sandbox page in Arabic](http://ar.wikipedia.org/wiki/Sandbox), which is a right-to-left (RTL) language:


![Wikipedia sandbox in Arabic](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0128777004e0970c-pi.png)


Compare that layout with the Wikipedia page on [internationalization and localization in English](http://en.wikipedia.org/wiki/Internationalization_and_localization). Now consider how you’d implement switching between English and Arabic in [MediaWiki](http://www.mediawiki.org/), the software that powers Wikipedia:

- Every bit of static text on the page has to come out of a unicode string resource file, indexed per-culture.
- Images that happen to contain text, or are otherwise culture-specific, must also be placed in a resource file and indexed per-culture.
- Numbers, currency, and dates must be displayed (and validated) differently depending on what country your audience lives in.
- You could detect the country your users are in, and automatically assume which language they’re using. But this is obviously problematic in countries where multiple languages are spoken. Or, you can allow users to manually choose a language the first time they access your application. This is slightly easier in web applications, because you can absorb the ambient language setting from the browser’s HTTP headers.


It’s a lot of work.


Beyond the purely mechanical grunt work of translation, there are deeper cultural issues to consider, such as avoiding offensive images, colors, or concepts for certain cultures – and how the concepts you’re trying to express in the software will map to a given culture. As noted in a related Larry Osterman post, these deeper cultural considerations are collectively known as *localization*:


> [localization] is a step past translation, taking the certain communication code associated with a certain culture. There are so many aspects you have to think about such as their moral values, working styles, social structures, etc... in order to get desired (or non-desired) outputs. This is one of the big reasons that automated translation tools leave so much to be desired – humans know about the cultural issues involved in a language, computers don’t.


[The Sims](http://en.wikipedia.org/wiki/The_Sims) has a unique solution that sidesteps the software internationalization problem. They invented an entirely new, completely artificial language: [Simlish](http://en.wikipedia.org/wiki/Simlish). **Simlish renders your cultural background irrelevant. When you redefine language as gibberish, it’s equally meaningless to everyone.** Or is it? Somehow, The Sims is playable without a lick of translation or localization, without any comprehensible language of any sort.


> Signs in The Sims games often do not contain text; they consist entirely of graphics. For instance, the stop sign in The Sims is a red octagon with a flat, white hand. In The Sims 2 it becomes a white bar instead. The sign for a grocery store depicts a cornucopia, and that of a restaurant shows a hamburger or a place setting.
> In The Sims, most text is only distinguishable at very close zooms. On book covers, newspapers and Nightlife’s “Sims Must Wash Hands” sign, **the lettering is all nonsense characters that bear about as much resemblance to Latin characters as they do to Cyrillic. Almost no actual characters from any known alphabet are used.** The game uses the Simoleon sign (closely resembling ) as the currency symbol.
> When Sims are writing novels or term papers, dingbats from the Wingdings font appear as text on the screen. The notebooks used for homework contain writing composed of random lines.


![](https://blog.codinghorror.com/content/images/2025/03/image-39.png)


Characters in The SIMS don’t just write in Simlish – they speak it, too:


> When The Sims was originally designed, [Will Wright](http://en.wikipedia.org/wiki/Will_Wright) wanted the language the Sims spoke to be unrecognizable but full of emotion. That way, every player could construct their own story without being confined to a Maxis-written script (to say nothing of the mind-numbing repetition). We experimented with fractured Ukrainian, and the Tagalog language of The Philippines. Will even suggested that perhaps we base the sound on Navajo, inspired by the code talkers of WWII. None of those languages allowed us the sound we were looking for – so we opted for complete improvisation.


Simlish is, by definition, meaningless. And yet it’s surprisingly easy to figure out what a Sim is talking about, even without any visual point of reference or a facial expression to read. The intonation and context of the sounds is enough to extract meaning. Try these two Simlish MP3 samples and hear for yourself.

Simlish example 1
0:00
/
11.064
Simlish Example 2
0:00
/
11.064

Simlish even extends to music. Last year, Maxis paid many original artists to re-record their songs with [Simlish lyrics](http://www.gamespot.com/pc/strategy/thesims2/news_6119747.html):


> Each artist rerecorded one of their songs with new vocal tracks, **replacing English lyrics with nonsensical Sim-speak**. Simlish words don’t have any real meaning, so the artists were free to come up with whatever sounded good, as long as English didn’t seep in. The result isn’t that different from what bands like the Cocteau Twins and Vas already do. The idea is to transcend words and use the human voice to express pure emotion.
> Charlotte Martin, whose song “Beautiful Life” finds its way onto [the University soundtrack](https://www.youtube.com/watch?v=NZ8yEm7opOc), took things a step further than some of the other artists. She didn’t just sing gobbledygook, she made sure all the Simlish words were consistent with their counterparts in the English version. “It still had the same meaning, I just had to write it in an alien language,” Martin said. In rewriting the song, Martin said it changed the way she thinks about lyrics, letting her come at her creation from a more technical standpoint, paying closer attention to syllables and rhythm.


To me, the two funniest examples are the simlish re-recordings of the [Pussycat Dolls’](http://en.wikipedia.org/wiki/Pussycat_Dolls)  "Don’t Cha” and [Lily Allen's](https://en.wikipedia.org/wiki/Lily_Allen) "Smile".


But the SIMS still very much has a life of its own in the [SIMS 4](https://en.wikipedia.org/wiki/The_Sims_4) (2014-2025), and as they say, "[the hits keep coming and they don't stop coming](https://sims.fandom.com/wiki/Songs_in_Simlish)."

[internationalization](https://blog.codinghorror.com/tag/internationalization/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[multilingual support](https://blog.codinghorror.com/tag/multilingual-support/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[localization](https://blog.codinghorror.com/tag/localization/)
