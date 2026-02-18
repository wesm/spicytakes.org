---
title: "Wading Through AccuWeather’s Bullshit Response"
date: 2017-08-23
url: https://daringfireball.net/2017/08/wading_through_accuweathers_bullshit_response
slug: wading_through_accuweathers_bullshit_response
word_count: 1041
---


[AccuWeather issued a statement](https://www.accuweather.com/en/press/69041756) regarding the controversy over their app [sending location-identifying information to a monetization firm](https://daringfireball.net/linked/2017/08/22/strafach-accuweather). [It’s a veritable mountain of horseshit](https://www.accuweather.com/en/press/69041756):


> Despite stories to the contrary from sources not connected to the
> actual information, if a user opts out of location tracking on
> AccuWeather, no GPS coordinates are collected or passed without
> further opt-in permission from the user.


The accusation has nothing to do with “GPS coordinates”. The accusation is that their iOS app is collecting Wi-Fi router names and MAC addresses and sending them to servers that belong to Reveal Mobile, which in turn can easily be used to locate the user. Claiming this is about GPS coordinates is like if they were caught stealing debit cards and they issued a denial that they never stole anyone’s cash.


The accusation comes from Will Strafach, a respected security researcher who discovered the “actual information” by observing network traffic. He saw the AccuWeather iOS app sending his router’s name and MAC address to Reveal Mobile. This isn’t speculation. They were caught red-handed — [go ahead and read Strafach’s original report](https://medium.com/@chronic_9612/advisory-accuweather-ios-app-sends-location-information-to-data-monetization-firm-83327c6a4870).


GPS information is more precise, and if you grant the AccuWeather app permission to access your location (under the guise of showing you local weather wherever you are, as well as localized weather alerts), that more precise data is passed along to Reveal Mobile as well. But Wi-Fi router information can be used to locate you within a few meters using publicly available databases. Seriously, go ahead and try it yourself: [plug your Wi-Fi router’s BSSID MAC address into this website](https://find-wifi.mylnikov.org/), and there’s a good chance it’ll pinpoint your location on the map.


> Other data, such as Wi-Fi network information that is not user
> information, was for a short period available on the Reveal SDK,
> but was unused by AccuWeather.


In what way is the name and MAC address of your router not “user information”? And saying the information was “unused by AccuWeather” is again sleight of hand. The accusation is not that AccuWeather itself was using the location of the Wi-Fi router, but that Reveal Mobile was. [Here are Reveal Mobile’s own words about how they use location data](https://revealmobile.com/profit-data-location-mobile-shoppers/):


> By expanding the use case of location data to pre- and
> post-shopping experiences, entirely new possibilities open up for
> online and offline retailers. The value lies in understanding the
> path of a consumer and where they go throughout the day. Traveling
> from home to work to retail to soccer practice to dinner is vital
> to knowing the customer, and represents the new opportunity of
> mobile location data. […]
> Location data also informs the home and work location of
> customers. Pairing this information with existing demographic
> targeting criteria allows retailers to target consumers with a
> high propensity to visit based upon two of their most relevant
> locations.


In other words, Reveal Mobile makes money by revealing your location to retailers (anonymously, so they claim), and AccuWeather made money from Reveal by embedding their SDK in their app.


Back to AccuWeather’s statement:


> In fact, AccuWeather was unaware the data was available to it.
> Accordingly, at no point was the data used by AccuWeather for any
> purpose.


If true, AccuWeather is seemingly claiming they embedded Reveal Mobile’s SDK in their app *without knowing what it did*. I believe them. But that’s a shocking admission of negligence.


> AccuWeather and Reveal Mobile are committed to following the
> standards and best practices of the industry.


No they’re not. If they were, they never would have sent MAC addresses and router names without the user’s consent, and implicitly, against the user’s consent in the case where they opted out of sharing location data with the AccuWeather app.


And even in the case where the user does grant the AccuWeather app permission to access Location Services (a perfectly reasonable thing to do for a weather app), I don’t think it’s a “best practice” to share this data with a retail marketing firm. I’ll bet most users of the AccuWeather app naively presume that the app only uses their location to show them localized weather conditions and alerts.


> We also recognize this is a quickly evolving field and what is
> best practice one day may change the next. Accordingly, we work to
> update our practices regularly.


The best practices for respecting the privacy of users do not change from day to day. What they mean is that one day your app can be doing something shady unbeknownst to the world, and the next day it can be discovered and widely publicized, painting your company as untrustworthy. But that’s not about “best practices” — that’s about *what you can get away with* changing from one day to the next.


> To avoid any further misinterpretation, while Reveal is updating
> its SDK, AccuWeather will be removing the Reveal SDK from its iOS
> app until it is fully compliant with appropriate requirements.
> Once reinstated, the end result should be that zero data is
> transmitted back to Reveal Mobile when someone opts out of
> location sharing. In the meanwhile, AccuWeather had already
> disabled the SDK, pending removal of the SDK and then later
> reinstatement.


With emphasis added: “the end result *should* be that zero data is transmitted back to Reveal Mobile when someone opts out of location sharing”? *Should* be? That’s confidence inspiring.


> Reveal has stated that the SDK could be misconstrued, and they
> assure that no reverse engineering of locations was ever conducted
> by any information they gathered, nor was that the intent.


I find this very difficult to believe. Reveal’s own description of their business is that they sell user location to retailers. Why else would they be collecting router MAC addresses if not to use a reverse lookup to locate users?


> We are grateful to have a supportive community that highlights
> areas where we can optimize and be more transparent.


Translation: *Fuck you, Will Strafach.*



| **Previous:** | [Some Comments Regarding The New York Times’s Report on Apple’s Titan Project](https://daringfireball.net/2017/08/titan_nyt) |
| **Next:** | [Serfing on the Giants’ Farms](https://daringfireball.net/2017/09/serfing_on_the_giants_farms) |


PreviousNext