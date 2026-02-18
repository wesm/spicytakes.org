---
title: "Third-Party USB-C to Lightning Cables Might Come in Mid-2019 (Which Is Good, Because I Still Don’t Think iPhone Is Ever Going to Switch to USB-C)"
date: 2018-11-15
url: https://daringfireball.net/2018/11/third_party_usb-c_to_lightning_cables
slug: third_party_usb-c_to_lightning_cables
word_count: 2053
---


Regarding [my question a few days ago](https://daringfireball.net/linked/2018/11/13/third-party-usbc-lightning-cables) about why there still aren’t any third-party MFI-certified USB-C to Lighting cables, here’s a report from [Japanese site Macotakara, back in September](http://www.macotakara.jp/blog/news/entry-35646.html) (scroll down for their English translation):


> Apple informed developers who participate in the MFi licensing
> program that they are planning to approve third-party products of
> “Apple USB-C to Lightning Cable”.
> Apple plans to move C48 Lightning connector to C89 Lightning
> connector, C68 Lightning connector to C78 Lightning connector,
> ​​C12 Lightning connector to C79 Lightning connector, the price
> will also be about $0.50 higher.
> In order to manufacture the USB-C to Lightning cable, a new “C94
> Lightning connector” is necessary, it explains that it becomes
> a maximum 15W power supply specification in the case of
> non-USB-PD and 18W charging is supported in the case of USB-PD
> compatible. […]
> As it is in the stage of USB-C to Lightning Developer Preview,
> third party USB-C to Lightning cable is expected to be released in
> mid-2019.


A few things to unpack here. “PD” stands for [Power Delivery](https://www.androidauthority.com/usb-power-delivery-806266/), a protocol for providing power up to 100W by switching to higher voltage. This is an alternative to Qualcomm’s Quick Charge standard in use on some Android phones. Standard USB is fixed at 5V and max current of 2.1A. 5V × 2.1A = ~10W max. Apple’s fastest non-PD USB charger is [the 12W charger](https://www.apple.com/shop/product/MD836LL/A/apple-12w-usb-power-adapter) that came with older iPad Pros. That one does 5.2V × 2.4A = 12.48W. (You can see the output volts and amps in the small print on all chargers.)


With a PD power supply, chargers support multiple output configurations, and the devices negotiate which to use via a handshake. [Apple’s old 29W charger](https://www.macrumors.com/2018/06/04/apple-29w-usb-c-power-adapter/) supported two output configurations ([photo](https://daringfireball.net/misc/2018/11/apple-29w-charger.jpg)):

- 14.5V × 2.0A = 29W
- 5.2V × 2.4A = 12.48W


[Apple’s new 30W charger](https://www.apple.com/shop/product/MR2A2LL/A/30w-usb-c-power-adapter) supports four output configurations ([photo](https://daringfireball.net/misc/2018/11/apple-30w-charger.jpg)):

- 20V × 1.5A = 30W
- 15V × 2A = 30W
- 9V × 3A = 27W
- 5V × 3A = 15W


The next thing to understand is that [MFI certification](https://developer.apple.com/programs/mfi/) requires vendors to source their Lightning connectors from Apple.1 The old connectors don’t support PD, and the new connectors that do aren’t yet available to third parties. Basically, this is why the only option for officially certified USB-C to Lightning cables remains Apple’s own 1m and 2m cables.


Yes, there are some no-name brand USB-C to Lightning cables available on Amazon right now. Amazon even labels one of them “Amazon’s Choice”. But they aren’t MFI-certified and I don’t think any of them support more than 10W. Personally, I would never trust these uncertified cables. The reviews on Amazon are full of complaints that they fail after a few weeks, and honestly I wouldn’t trust them in terms of safety. I get wanting to charge Lightning devices from USB-C chargers and MacBooks, but if you don’t want to buy Apple’s own cables (which admittedly are expensive) you might as well just use an old USB-A to Lightning cable and a USB-C to USB-A adapter, because you’re still limited to the non-PD charging limits. The no-name brand USB-C to Lightning cables available today do not support PD, are not certified, and are limited to 12 watts. There’s a reason they only come from no-name brands.


It’s small consolation to those of us looking for high-quality third-party USB-C to Lightning cables and adapters today, but it does sound like they’ll start appearing in the second quarter of 2019.


## The iPhone and USB-C


This brings me to a second point, which feels at least tangentially related to this whole USB-C to Lightning situation. Now that the iPad Pros have switched to USB-C, there are a lot of people — possibly *most* of you reading this — who think/hope Apple is going to switch the iPhone from Lightning to USB-C next year.


I don’t think that’s going to happen, ever. I could be wrong — there are definitely some compelling reasons why they might. But I don’t think they will for a few reasons.


First, Apple likes having complete control over the iPhone peripheral market. Consider iPhone cases that include a built-in battery pack. There aren’t many of them. Apple only recently approved [Mophie’s battery pack for the year-old iPhone X](http://www.mophie.com/shop/iphone-x/juice-pack-air-iphone-x). Battery packs are difficult — they block inductive charging and they can interfere with the phone’s antennas. That’s why [Apple’s own battery case for the iPhone 7](https://www.apple.com/shop/product/MN002LL/A/iphone-7-smart-battery-case-black) had such a seemingly weird hump-on-the-back design: that design kept the battery from interfering with the antennas. It’s in Apple’s interest to certify that third-battery cases don’t interfere with antenna reception, because if they *did* interfere, people would naturally blame the iPhone for the poor reception, not the case.


But Apple wields its MFI control in other ways too. In a Twitter thread Wednesday, [Nilay Patel pointed out](https://twitter.com/reckless/status/1062540481505251328) there has never been an MFI-certified battery case with a headphone jack. This almost certainly is not because no one thought to make one, but rather that Apple will not approve them. Apple clearly thinks external battery packs (connected to iPhones via a cable) are a better solution than cases with integrated batteries. With Lightning, they can effectively control this. If the iPhone were to switch to USB-C, I don’t think they could stop anyone from making USB-C battery cases. I do not think Apple will cede this control.


Second, the nerd world may clamor for one universal connector that charges everything from iPhones to iPads to MacBooks, but the normal world just wants their existing cables to keep working when they buy a new iPhone. Lightning is obviously better than the old 30-pin adapter — the old 30-pin connectors look ridiculous in hindsight. But people upgrading from older iPhones were *outraged* when Apple introduced Lightning with the iPhone 5 in 2012. They saw it as a money grab — a new port introduced so everyone would have to buy new cables. The fact that you wouldn’t have to buy USB-C cables from Apple wouldn’t change that perception if future iPhones switch to USB-C — nerds might rejoice but regular folks will object.


For however many iPhone users there are who are upset that iPhones continue to use the proprietary Lightning port when they could, technically, use USB-C instead, I would bet big money there are way more who just want Apple to keep using Lightning because they already have Lightning cables everywhere they need them. It’s also almost certainly true that there are way more iPhone owners who do not own either an iPad or MacBook than there are iPhone users who also own an iPad or MacBook. These iPhone owners don’t care that the new iPad Pro and recent MacBooks have switched to USB-C. And even those iPhone owners who *do* own an iPad or MacBook are very unlikely to own the brand-new $800-and-up iPad Pro, and their MacBooks are most likely models with MagSafe.


Third (and admittedly a distant third at that), Lightning connectors and ports are smaller. Sure, at 5.9mm thick, the new iPad Pros are the thinnest iOS devices ever,2 and they use USB-C. But still, it’s easier to make a thinner device with a smaller connector. I also think Lightning connectors are more pleasant to use. They’re easier to plug in and easier to pull out. Lightning is a simple, elegant male/female design. USB-C, like all previous USB versions, is a weird male connector with female slot / female port with a tiny little male connector inside. USB-C certainly has some technical advantages over Lightning, but iPhones don’t need those features. The elegance (and I suspect durability) of Lightning probably matters more to Apple.


So:

1. Apple would prefer to maintain MFI control over all iPhone peripherals.
2. Most iPhone users would be displeased, at least in the short-term, by a switch to USB-C.
3. Lightning is smaller and more elegant than USB-C and Apple prefers smaller and more elegant.


I think iPhones will stick with Lightning until wireless charging is fast enough that Apple can remove all ports, Apple Watch-style.


In fact, I don’t think regular (non-Pro) iPads will switch to USB-C either. Apple is pitching the iPad Pros’ switch to USB-C based on actual professional features — driving external 5K displays, using PC-class peripherals, and support for very high-power charging. The only one of those that might apply to regular iPads is faster charging, which is always nice to have, but even that wouldn’t matter much to most iPad users, who (a) stick with whatever charger Apple supplies in the box, and (b) choose extra chargers based on price, not output wattage. (Spec-knowledgeable nerds have trouble believing this, but *many* iPhone users love the wimpy 5W charger Apple includes with iPhones because it’s so small.)


## Lightning Gadgets


When I think of Lightning-powered devices I tend to think of iPhones and iPads. But over the last few years, Apple has put Lightning ports into a bunch of battery-powered gadgets:

- AirPods charging case
- Magic Keyboard, Trackpad, and Mouse
- Apple TV Siri remote
- [Apple TV gaming controllers](https://www.apple.com/shop/tv/tv-accessories/remotes-controllers?page=1#!&f=gamecontrol&fh=46c1%2B45ef)
- Apple Pencil 1


Most of those aren’t related to iPhones at all — the iPhone could switch to USB-C and it wouldn’t really matter if these gadgets stayed on Lightning. Except for one: the AirPods charging case. That’s the one that is intimately tied to iPhone use in daily life. You really want to be able to charge your AirPods case with the connector you’re most likely to have handy, and that’s your phone charger.


There were rumors that Apple might ship next-generation AirPods this year. (There *still* are rumors they might ship this year, in fact, [even though at this date that doesn’t seem very likely](https://daringfireball.net/linked/2018/11/15/airpods-2-this-year).) That would have been an interesting hint regarding the future of the iPhone’s charging port. I really don’t think Apple would launch a second generation of AirPods now, and sell them all through next year, only to change the iPhone’s charging port to USB-C in September.


One supply chain leaker with a supposedly good track record [published a photo purportedly showing new AirPods cases](https://twitter.com/laobaiTD/status/1062618308212473856), and, for what that’s worth (not much, in my opinion), the cases shown still have Lightning ports.


If Apple *had* announced second-generation AirPods this year, and the new cases still had Lightning ports, I’d take that as a strong sign that next year’s iPhones will too. And if they had shipped *without* Lightning ports (using inductive charging instead, perhaps, like Apple Pencil 2), I’d be a little less willing to bet that next year’s new iPhones will stick with Lightning. But Apple has not announced new AirPods (or even just new AirPod cases), nor recent updates to any of its Lightning-powered gadgets other than Pencil, so we don’t have any clues to glean on this front.


---

1. MFI licensees sign non-disclosure agreements with Apple [with exorbitant financial penalties](https://twitter.com/reckless/status/1062465926027796485). So, they tend not to talk. But one little birdie I spoke with recently said that last year, for months, there simply were no Lightning connectors available to third parties, because Apple was consuming the entire supply because they were including three with each iPhone 8 and iPhone X — one for the cable, one for the headphones, and one for the headphone adapter. These supply constraints make me wonder if that’s why this year’s new iPhones still ship only with USB-A Lightning cables and chargers — Apple may not have felt confident in the supply of the new Lightning connectors that work with USB-C PD charging speeds. If they had included a USB-C to Lighting cable with every iPhone XS and XR, they’d have needed at least 50 million new Lightning connectors this quarter, and they apparently don’t even have enough to sell them to MFI licensees until some time next year. ↩︎
2. Remember the iPod Touch? Apple [still sells them](https://www.apple.com/ipod-touch/), but they’re so long in the tooth they still use iPhone 6-class A8 chips. I think the plethora of old hand-me-down iPhones has really put a crimp the market for iPod Touches. I can’t even remember the last time I heard someone say “iTouch”. ↩︎︎



| **Previous:** | [Apple’s Q4 2018 Results](https://daringfireball.net/2018/11/aapl_q4_results) |
| **Next:** | [An Alternative Theory on Purportedly Weak iPhone XR Demand](https://daringfireball.net/2018/11/iphone_xr_theory) |


PreviousNext