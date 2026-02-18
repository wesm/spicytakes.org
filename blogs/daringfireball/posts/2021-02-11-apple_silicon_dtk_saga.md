---
title: "The Two-Day Saga of the Apple Silicon DTK Exchange Program"
date: 2021-02-11
url: https://daringfireball.net/2021/02/apple_silicon_dtk_saga
slug: apple_silicon_dtk_saga
word_count: 1239
---


[Michael Tsai has a detailed rundown](https://mjtsai.com/blog/2021/02/04/apple-wants-developer-transition-kits-back/) (as ever) of last week’s brief controversy over Apple asking developers to return their Apple Silicon Mac developer transition kits (DTKs). See his post for all the details, but let me try to summarize the whole thing, in order, because it’s a good story.


In June 2005, when Apple announced the Mac transition from PowerPC to Intel, they offered developers Intel-based DTK hardware. They looked like1 the then-current “cheese grater” Power Mac G5s, but the innards were Intel PCs. You paid Apple $1000, they sent you a DTK to use for a year to port PowerPC Mac software to Intel, and when the year was up you were required to send the DTKs back to Apple. But in January 2006, shortly after the announcement of the first batch of Intel-based Macs, Apple made a surprise announcement. [As I wrote then](https://daringfireball.net/linked/2006/01/10/dtk):


> Apple is exchanging the $1000 Developer Transition Kit machines
> for 17-inch Intel iMacs, one for one, cross-shipped, shipping
> costs paid both ways. Pretty sweet deal, considering everyone
> thought they’d have to send back the DTKs in exchange for a
> steaming pile of corporate gratitude. (Thanks to Nat Irons for
> that turn of phrase.)


(I had to keep that parenthetical in there, because damn that is a good turn of phrase.)


When Apple announced DTK hardware last June for the Apple Silicon transition, the terms were different mainly in that the DTKs were only $500, not $1000. But Apple still wanted them back after a year, and expressly reserved the right to ask for them back before the year was up. Not only was there no mention of any sort of exchange credit when the DTKs were returned, the terms made it clear that Apple wasn’t even providing a warranty for the DTKs. If you paid for one, and it went belly-up, Apple owed you nothing. [Really, no warranty](https://developer.apple.com/terms/universal-app-quick-start-program/Developer-Universal-App-Quick-Start-Program.pdf):2


> No Warranty
> The Developer Transition Kit is not fully tested and is to be used
> only for limited testing and development purposes as set forth in
> Section 2. The Developer Transition Kit may contain errors that
> could cause failures or loss of data and may be incomplete or
> contain inaccuracies. The Developer Transition Kit is provided to
> You solely on an “AS IS” and “AS AVAILABLE” basis. USE OF THE
> DEVELOPER TRANSITION KIT IS AT YOUR SOLE RISK AND THE ENTIRE RISK
> AS TO SATISFACTORY QUALITY, PERFORMANCE, ACCURACY, RELIABILITY,
> AND EFFORT IS WITH YOU.


That’s just the *start* of the “APPLE MAKES NO WARRANTIES, EXPRESS OR IMPLIED…” section, but there’s only so much all-caps legalese I can bear to quote. Suffice it to say, the terms were very clear:

1. You apply for the program.
2. If accepted, you pay Apple $500.
3. Apple sends you a DTK.
4. No warranty.
5. Apple can ask for it back at any time, and when they do, you have 30 days to return it.


That’s it.


That, however, didn’t stop people from assuming that once Apple Silicon Macs were announced, Apple would announce an exchange program similar to the previous one during the Intel transition.


A week ago, [they did announce an exchange program](https://9to5mac.com/2021/02/03/apple-asking-developers-to-return-dtk-mac-mini-offers-200-credit-for-buying-m1-macs/). Apple said developers could get $200 credit that was usable only for the purchase of an M1 Mac (MacBook Air, MacBook Pro, or Mac Mini) but would expire May 31.


Developers had quite a few objections to this offer:

- Many developers are waiting for subsequent Apple Silicon Macs — 16-inch MacBook Pros, iMacs, or even just higher-end 13-inch MacBooks or Mac Minis.
- An expiration date of May 31 precludes any Macs set to be announced at WWDC, which everyone reasonably presumes will be held in June.
- A $200 credit for a $500 DTK rental seemed miserly coming from the richest company in the world, when, 15 years ago — at a time when Apple was very, very far from the richest company in the world — they exchanged $1000 DTKs for $1300 iMacs.
- Some developers have already purchased M1 Macs, have no desire for another, and were annoyed, justifiably, that this credit wasn’t offered back in November or December when the M1 Macs were announced.
- Developers used those DTKs to help Apple as much or more than to help themselves. It was in Apple’s interests for as much third-party software to be Apple Silicon native at, or soon after, the launch of the M1 Macs.


The objection to those objections is rather obvious, though: every developer who paid for one of these DTKs agreed to very clear terms that promised nothing at all except, well, an implied steaming pile of corporate gratitude.


After just two days, [Apple sent developers an email with the subject, “We heard you and we agree”](https://twitter.com/gruber/status/1357921261058482176):


> We heard your feedback regarding the 200 USD appreciation credit
> mentioned in our last email. Our intention was to recognize the
> tremendous effort that you have put into creating amazing
> universal apps. By partnering with us early, you showed your
> commitment to our platform and a willingness to be trailblazers.
> So instead of the 200 USD credit that expires in May, we are
> giving you a 500 USD Apple credit and extending the time you can
> use it to get a new M1 Mac through the end of the year. If you
> already purchased a new M1 Mac, the Apple credit gives you the
> flexibility to purchase any Apple product to help with your app
> development work.


I would file this email under “Making Things Right”:

- Developers who paid for the DTKs get credit for the full $500.
- The expiration goes through the end of the year, by which point, surely, there will be a broad range of additional Apple Silicon Macs.
- If a developer in the DTK program has already bought an M1 Mac, they can use the $500 credit toward any other product.


So what happened? I think it’s exactly what Apple’s second email states: someone at Apple thought $200 credit was a generous offer, the offer went out, Apple realized they made a mistake based on developer reaction, and they issued a new offer — 2.5× more costly in dollars, but clearly worth it to Apple in goodwill — within one day. My quibble isn’t that Apple made a mistake with the amount of the “appreciation credit”, but with why it took them so long to make the initial offer. Why not have it ready in December — especially given that the DTKs really are sort of crummy machines, and the M1 Macs are vastly superior in both performance and reliability? Apple should have done whatever it could to get developers to move from DTKs to production M1 Macs as soon as possible.


Make few mistakes, but recognize the mistakes you do make quickly, admit to them, and fix them. That’s the recipe.


---

1. My favorite story about the Intel DTKs [was about what they *sounded* like](https://daringfireball.net/2008/04/big_fan), not what they looked like. ↩︎
2. [Another](https://daringfireball.net/linked/2020/08/17/apple-developer-program-license-agreement) legal PDF from Apple typeset in Arial. What the hell is going on in Apple’s legal department? ↩︎︎



| **Previous:** | [2020 Quote of the Year: ‘What’s the Downside for Humoring Him?’](https://daringfireball.net/2021/02/whats_the_downside) |
| **Next:** | [Volkswagen CEO Herbert Diess on Apple’s Purported Interest in Making Cars](https://daringfireball.net/2021/02/volkswagen_ceo_apple_car) |


PreviousNext