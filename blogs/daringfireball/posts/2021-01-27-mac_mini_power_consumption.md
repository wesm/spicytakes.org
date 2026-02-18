---
title: "Mac Mini Power Consumption and Thermal Output Specs"
date: 2021-01-27
url: https://daringfireball.net/2021/01/mac_mini_power_consumption
slug: mac_mini_power_consumption
word_count: 901
---


A few weeks ago, Apple added the new M1 model to [their support page listing the power consumption and thermal output of all Mac Mini models](https://support.apple.com/en-us/HT201897) (including the 2005 original, which used a PowerPC G4 CPU). The numbers from 2014 onward are rather striking:

Markdown Table (NOTE: colspanning table headers)
|                         |  Idle  |   Max  |  Idle  |   Max |
| ------------------------|-------:|-------:|-------:|------:|
| 2020, M1                |     7  |    39  |    23  |   133 |
| 2018, 6-core Core i7    |    20  |   122  |    68  |   417 |
| 2014, 2-core Core i5    |     6  |    85  |    20  |   290 |
| …                       |        |        |        |       |
| 2006, Core Solo/Duo  |    23  |   110  |    79  |   376 |
| 2005, PowerPC G4        |    32  |    85  |   110  |   290 |


|  | Power Consumption
(Watts) | Thermal Output
(BTU/h) |
| Mac Mini Model | Idle | Max | Idle | Max |
| 2020, M1 | 7 | 39 | 23 | 133 |
| 2018, 6-core Core i7 | 20 | 122 | 68 | 417 |
| 2014, 2-core Core i5 | 6 | 85 | 20 | 290 |
| … |  |  |  |  |
| 2006, Core Solo/Duo | 23 | 110 | 79 | 376 |
| 2005, PowerPC G4 | 32 | 85 | 110 | 290 |



I’ve taken a few small liberties with my version of this table. I’ve rounded a few of the numbers to the nearest integer (e.g. the M1 Mac Mini’s actual idle power consumption is 6.8 W), and there were three different 2015 Core i5 Mac Mini models, but all three shared the same power consumption and thermal specs, so I’ve combined them into one item in the table. Likewise with the 2006 original Intel Mac Minis — there were separate Core Solo and Core Duo models, but they had the same power/thermal specs.


The gap between the 2014 models and the 2018 revision felt like “forever”, coincided with the dearth of updates to the “trash can” Mac Pro, and culminated with the small April 2017 roundtable discussion, where Phil Schiller, Craig Federighi, and John Ternus revealed to a handful of invited press their intention to make a “pro” iMac (which they then unveiled a few weeks later at WWDC, and shipped in December) and, more unusually, laid bare their plans for an all-new Mac Pro, which wasn’t unveiled until WWDC 2019 and didn’t ship until December that year. The basic message was that despite the dearth of recent updates, Apple remained as committed as ever to pro Mac hardware (and software).


[From my piece on that roundtable discussion](https://daringfireball.net/2017/04/the_mac_pro_lives):


> Near the end, John Paczkowski had the presence of mind to ask
> about the Mac Mini, which hadn’t been mentioned at all until
> that point. Schiller: “On that I’ll say the Mac Mini is an
> important product in our lineup and we weren’t bringing it up
> because it’s more of a mix of consumer with some pro use. […]
> The Mac Mini remains a product in our lineup, but nothing more
> to say about it today.”


This gap in Mac desktop hardware, from around 2014 through the roundtable mea culpa in April 2017, was viewed by many as a sign that Apple had lost interest in the Mac. Even after the roundtable meeting, however, Schiller’s “the Mac Mini remains a product in our lineup” comment was taken as a sign that even if Apple had a reinvigorated interest in high-end Mac desktops, the Mac Mini was not a priority.


But then came [the very well-regarded 2018 Mac Mini](https://sixcolors.com/post/2018/11/mac-mini-2018-review/). It *was* still an important product in Apple’s lineup! But well-regarded or not, look at the thermals in the table above. The 2018 Mac Mini has three times the power consumption and thermal output of the new M1 Mac Mini — and much higher numbers than the 2014 Mac Mini models it replaced. It’s an outlier on the trendline. And keep in mind that the M1 Mac Mini is also a *much* more performant computer. Apple does not like to talk about stuff like this, so we’re left to conjecture, but it’s not hard to look at this simple table of power consumption and thermal output and consider that those “gap years” in Mac desktop hardware — the Mac Mini in particular — were to a large extent the result of Intel’s chips running way too hot for Apple’s standards. And that in 2017, Apple bit the bullet and did the best they could with what Intel had to offer, realizing then that they needed another generation of Intel Macs (desktop and laptop) before Apple Silicon Macs would be ready.


Historically, it’s worth noting that the M1 Mac Mini’s *maximum* power consumption and thermal output are only ever so slightly higher than the *idle* power/thermal numbers for the original 2005 PowerPC G4 Mac Mini. A new M1 Mac Mini running at full speed uses about the same power as a G4 Mac Mini did just sitting there with the Finder open doing nothing. I don’t have GeekBench numbers handy for the G4 Mac Mini, but I believe the new M1 models are noticeably faster.



| **Previous:** | [Gus Mueller and Ken Kocienda on Brad Cox and Objective‑C](https://daringfireball.net/2021/01/mueller_cox_objc) |
| **Next:** | [My 2020 Apple Report Card](https://daringfireball.net/2021/01/my_2020_apple_report_card) |


PreviousNext