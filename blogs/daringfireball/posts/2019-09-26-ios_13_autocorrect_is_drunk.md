---
title: "iOS 13 Autocorrect Is Drunk"
date: 2019-09-26
url: https://daringfireball.net/2019/09/ios_13_autocorrect_is_drunk
slug: ios_13_autocorrect_is_drunk
word_count: 716
---


[I asked the following on Twitter Tuesday](https://twitter.com/gruber/status/1176617212569890817): “Does anyone else find that autocorrect on iOS 13 (including 13.1) makes more mistakes than before? Can’t tell if it’s a real issue or just an anti-placebo effect.”


The resulting [thread](https://twitter.com/gruber/status/1176617212569890817) is overflowing with answers in the affirmative. One thing I and others have noticed is that when you type a dictionary word correctly — meaning you hit the exact right keys on the on-screen keyboard — iOS 13 autocorrect will replace it with a different dictionary word that makes no contextual sense. Even beyond dictionary words, I’m seeing really strange corrections. Two nights ago [I typed “Dobbs”](https://twitter.com/gruber/status/1176724868680863745), including the Shift key for the “D”, and iOS 13.1 autocorrected it to “adobe”, with a lowercase “a”.


I don’t see how that’s even close on a QWERTY keyboard. The way autocorrect tends to work is to look for alternate words based on the proximity of letters on the keyboard. Most famously, *fuck* gets replaced by *duck* because the D key is next to F on a QWERTY keyboard. That’s why it never replaces *fuck* with, say, *suck*, *puck*, or *luck* — it’s always *duck* because D and F are next to each other.1


So how in the world does “Dobbs” get replaced by “adobe”? Even “Adobe” would make slightly more sense, because that’s a common proper noun (and one I personally use) and would acknowledge that I hit the Shift key to type an uppercase letter. Letter by letter, with “×” denoting letters nowhere near each other on the keyboard, “✓” denoting the same letter, and “-” denoting characters close to each other on the keyboard:


```
D o b b s
a d o b e
× × × ✓ - 

```


Even the S/E substitution is questionable, though — iOS’s autocorrect, in my experience, usually looks at characters next to each other in the same row of the keyboard. The E key is above and mostly to the right of S.


[**Update:** A few minutes after publishing, a [few](https://twitter.com/snoopy369/status/1177289720591781891) [readers](https://twitter.com/yonatron/status/1177290116269793281) [suggested](https://twitter.com/UlurooSpeaks/status/1177294569114935296) a somewhat reasonable [explanation](https://twitter.com/Clarko/status/1177293109622788096) for Dobbs/adobe: A is above the Shift key on the iPhone keyboard, so if the keyboard thought I meant A instead of Shift, the rest of the letters line up a bit better, although the keyboard also has to interpret the double B’s as a mistake too. I still say this is a terrible substitution, and can’t recall anything like it prior to iOS 13.]


A lot of the examples in the responses to my tweet are even more baffling, including words being substituted [from other languages](https://twitter.com/mattcassinelli/status/1177281315147636736).


I tweeted this wondering if the autocorrect suckage I was seeing was just me — perhaps the result of a reverse placebo effect (a.k.a. [nocebo effect](https://en.m.wikipedia.org/wiki/Nocebo)) where, once I suspected autocorrect in iOS 13 might be bad, I started seeing what I expected to see. But now I’m close to convinced that, among iOS 13.0 and 13.1’s numerous other bugs and problems, autocorrect has suffered a severe regression.


One possible culprit: iOS 13’s new [“Slide to Type” feature](https://sixcolors.com/post/2019/09/13-features-of-ios-13-quickpath-keyboard/), which is enabled by default. I have tried various swipe-to-type keyboards over the years (on both iOS, via third-party keyboards; and Android, where they’ve long been prevalent as built-in features), and have never taken to them. My thumb-pecking habits were long ago hardwired into my brain. So I turned this feature off on iOS 13 last night. I have no idea if that’s the culprit — I haven’t used the iPhone long enough since turning it off to pass judgment — but given that I don’t want to use Slide to Type anyway, it can’t hurt to try. Feel free to chime in [on the Twitter thread](https://twitter.com/gruber/status/1176617212569890817) if you’re seeing similar autocorrect wonkiness.


---

1. The origins of this heuristic are explored and explained in detail by the creator of the original iPhone keyboard, [Ken Kocienda](https://twitter.com/kocienda), in his book *[Creative Selection](http://creativeselection.io/)*. It’s one of the most remarkable books on Apple ever written, and in particular, offers a detailed look at one of the truly make-or-break features of the original iPhone. It’s hard to overstate how much skepticism the iPhone faced over its lack of a hardware keyboard. ↩︎



| **Previous:** | [iPhones 11 and Apple Watch Series 5 Q&A](https://daringfireball.net/2019/09/iphones_11_apple_watch_series_5_q_and_a) |
| **Next:** | [Richard Stallman’s Disgrace](https://daringfireball.net/2019/09/richard_stallmans_disgrace) |


PreviousNext