---
title: "On commercial forks of FOSS projects"
date: 2021-12-18
url: https://drewdevault.com/2021/12/18/Commercial-forks-of-FOSS-projects.html
slug: Commercial-forks-of-FOSS-projects
word_count: 815
---

The gaming and live streaming industry is a lucrative and rapidly growing
commercial sector with a unique understanding of copyright and intellectual
property, and many parties with conflicting interests and access to different
economic resources.

The understanding of intellectual property among gamers and the companies which
serve them differs substantailly from that of free software, and literacy in the
values and philosophy of free software among this community is very low. It is
then of little surprise that we see abuse of free software from this community,
namely in the recent (and illegal) commercial forks of a popular FOSS streaming
platform called  [OBS Studio](https://obsproject.com)  by companies like TikTok.

These forks are in violation of the software license of OBS Studio, which is
both illegal and unethical. But the “why” behind this is interesting for a
number of reasons. For one, there  *is*  a legitimate means through which
commercial entities can repurpose free software projects, up to and including
reskinning and rebranding and selling them. The gaming community also has an
unusual perspective on copyright which colors their understanding of the
situation. Consider, for instance, the modding community.

Game modifications (mods) exist in a grey area with respect to copyright.
Modding in general is entirely legal, though some game companies do not
understand this (or choose not to understand this) and take action against them.
Modders also often use assets of dubious provenance in their work. Many people
believe that, because this is all given away for free, the use is legitimate,
and though they are morally correct, they are not legally correct. Additionally,
since most mods are free (as in beer), 1  the currency their authors receive
for their work is credit and renown. Authors of these mods tend to defend their
work fiercely against its “theft”. Modders also tend to be younger, and grew up
after the internet revolution and the commoditization of software.

On the other hand, the conditions under which free software can be “stolen” are
quite different, because the redistribution, reuse, and modification of free
software, including for commercial purposes, is an explicit part of the social
and legal contract of FOSS. This freedom comes, however, with some conditions.
The nature of these conditions varies from liberal to strict. For instance,
software distributed with the MIT license requires little more than crediting
the original authors in any derivative works. On the other end of this spectrum,
copyleft licenses like the GPL family require that any derivative works of the
original project are  *also*  released under the GPL license. OBS Studio uses the
GPL license, and it is in this respect that all of these forks have made a legal
misstep.

If a company like TikTok wants to use OBS Studio to develop its own streaming
software, they are  *allowed to do this* , though the degree to which they are
 *encouraged*  to do this is the subject of some debate. 2  However, they must
release the source code for their modifications under the same GPL license. They
can repurpose and rebrand OBS Studio only if their repurposed and rebranded
version is made available to the free software community under the same terms.
Then OBS Studio can take any improvements they like from the TikTok version and
incorporate them into the original OBS Studio software, so that everyone shares
the benefit — TikTok, OBS users, StreamLabs, and StreamElements alike, as
well as anyone else who wants in on the game.

This happens fairly often with free software and often forms a healthy
relationship by establishing an incentive and a pool of economic resources to
provide for the upkeep and development of that software. Many developers of a
project like this are often hired by such companies to do their work. Sometimes,
this relationship is viewed more negatively, but that’s a subject for another
post. It works best when all of the players view each other as collaborators,
not competitors.

That’s not what happening here, though. What we’re seeing instead is the brazen
theft of free software by corporations who believe that, because their legal
budget exceeds the resources available to the maintainers, might makes right.

Free software is designed to be used commercially, but you have to do it
correctly. This is a resource which is made available to companies who want to
exploit it, but they must do so according to the terms of the licenses. It’s not
a free lunch.

1. I think that this is likely the case specifically to dis-incentivize legal action by the gaming companies (who would likely be wrong, but have a lot of money) or from the owners of dubiously repurposed assets (who would likely be right, and also have a lot of money). One notable exception is the Black Mesa mod, which received an explicit blessing from Valve for its sale. ↩︎
2. For my part, I’m in the “this is encouraged” camp. ↩︎
