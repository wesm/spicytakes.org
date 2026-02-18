---
title: "Apple Issues a Workaround for the Blood Oxygen Sensor Ban for U.S. Apple Watches"
date: 2025-08-14
url: https://daringfireball.net/2025/08/apple_workaround_blood_oxygen_ban
slug: apple_workaround_blood_oxygen_ban
word_count: 886
---


Apple Newsroom this morning, “[An Update on Blood Oxygen for Apple Watch in the U.S.](https://www.apple.com/newsroom/2025/08/an-update-on-blood-oxygen-for-apple-watch-in-the-us/)”:


> Apple will introduce a redesigned Blood Oxygen feature for
> some Apple Watch Series 9, Series 10, and Apple Watch Ultra 2
> users through an iPhone and Apple Watch software update coming
> later today.
> Users with these models in the U.S. who currently do not have the
> Blood Oxygen feature will have access to the redesigned Blood
> Oxygen feature by updating their paired iPhone to iOS 18.6.1 and
> their Apple Watch to watchOS 11.6.1. Following this update, sensor
> data from the Blood Oxygen app on Apple Watch will be measured and
> calculated on the paired iPhone, and results can be viewed in the
> Respiratory section of the Health app. This update was enabled by
> a recent U.S. Customs ruling.
> There will be no impact to Apple Watch units previously purchased
> that include the original Blood Oxygen feature, nor to Apple Watch
> units purchased outside of the U.S.


The iOS 18.6.1 and WatchOS 11.6.1 updates appeared a few hours after Apple’s announcement.


If you have an Apple Watch with the blood oxygen sensor purchased *outside* the US, you can ignore today’s news. You were never affected by the US International Trade Commission import ban (which stems from [a patent lawsuit from a company named Masimo](https://daringfireball.net/search/masimo)), so today’s workaround isn’t necessary. The same goes for Series 9 and Ultra 2 models sold in the US prior to the ban taking effect in January 2024.


What today’s workaround does is process *and* display the blood oxygen sensor data on your watch’s paired iPhone, rather than on the Apple Watch itself. That, apparently, is what the new US Customs ruling holds does not violate Masimo’s patent. No processing of the sensor data on the watch, and no display of the results on the watch. But the sensor that takes the measurements, of course, is on your watch. If you bought your Apple Watch before the ban, or you bought it outside the US, you still get on-watch processing and on-watch display of results. (Which means users outside the US still have a slightly better blood oxygen experience.)


If your Apple Watch was affected by the import ban, after today’s software updates, you should be able to both initiate a blood oxygen reading manually (using the Blood Oxygen app on the Watch) and get automatic background readings, like when you’re wearing your watch while sleeping. What is different for Series 9, Series 10, and Ultra 2 models in the US that didn’t have the original Blood Oxygen feature, compared to models not affected by the US ban, is where the measurement is *calculated* and *visible*. If you initiate a measurement while your watch is out of range of its paired iPhone, the results will be calculated on the iPhone once it is back in range.


Also important, and not clear at all from Apple’s initial announcement this morning: After the iOS 18.6.1 and WatchOS 11.6.1 software updates, the iPhone and Apple Watch need to download an over-the-air asset to enable the redesigned Blood Oxygen feature. This apparently may take up to 24 hours. Until this asset download happens, the Blood Oxygen app on your Apple Watch will still say “The Blood Oxygen app is no longer available”. To jump-start the download, users can open the Health app on their iPhone, and the ECG app on their Apple Watch. I was in this boat personally with an Ultra 2 from last year, and opening the Health app on my iPhone and taking an ECG reading on the watch did the trick — after that, launching the Blood Oxygen app on the watch [showed a new message](https://daringfireball.net/misc/2025/08/blood-oxygen-app-watchos-11.6.1.png):


> The Blood Oxygen App Has Changed
> You will now find Blood Oxygen results in the Health app on your iPhone.


(**Update:** I am reliably informed that you don’t need to take an ECG reading on the watch. Just opening the ECG app is enough to trigger the asset download needed by the Blood Oxygen app. I figured why not take a reading while I was in there, though.)


The US Customs ruling that Apple is citing to allow them to offer this workaround — “HQ H351038”, per a source at Apple — [is not yet publicly available](https://rulings.cbp.gov/). But reading between the lines, the implication is that US Customs has decided that Masimo’s patents only apply to on-device sensor processing (and display of results?).


I continue to think that Masimo is a patent troll. At the time they filed their complaint with the ITC, [they didn’t even have a smartwatch on the market](https://daringfireball.net/linked/2025/07/11/apple-masimo-appeals-court). And [the smartwatch they now sell](https://www.masimo.com/products/monitors/masimo-w1-medical-watch/) — years after filing the complaint — looks like an Apple Watch with a second button instead of a digital crown. The two patents in question ([10,912,502](https://patents.google.com/patent/US10912502B2/en) and [10,945,648](https://patents.google.com/patent/US10945648B2/en)) are set to expire in August 2028, and I suspect this patent suit has been a last-ditch attempt to monetize them before they expire by extorting a settlement from Apple. Good luck with that now.



| **Previous:** | [Max Read’s ‘A Literary History of Fake Texts in Apple’s Marketing Materials’](https://daringfireball.net/2025/08/max_read_literary_history_fake_apple_texts) |
| **Next:** | [Joe Caroff, Designer of the James Bond 007 Logo, Dies at 103](https://daringfireball.net/2025/08/joe_caroff_007_logo_designer) |


PreviousNext