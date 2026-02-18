---
title: "The European Commission Had Nothing to Do With Apple’s Reversal on Supporting RCS"
date: 2024-02-16
url: https://daringfireball.net/2024/02/eu_rcs_imessage
slug: eu_rcs_imessage
word_count: 1072
---


[The European Commission, earlier this week](https://digital-markets-act.ec.europa.eu/commission-closes-market-investigations-microsofts-and-apples-services-under-digital-markets-act-2024-02-13_en):


> Yesterday, the Commission has adopted decisions closing four 
> market investigations that were launched on 5 September 2023 under 
> the Digital Markets Act (DMA), finding that Apple and Microsoft 
> should not be designated as gatekeepers for the following core 
> platform services: Apple’s messaging service iMessage, Microsoft’s 
> online search engine Bing, web browser Edge and online advertising 
> service Microsoft Advertising. 
> The decisions conclude the Commission’s investigations opened 
> following the notification by Apple and Microsoft in July 2023 of 
> the core platform services that met the quantitative thresholds. 
> Among these notified services were also the four services 
> concerned by today’s decisions. Together with the notifications, 
> Apple and Microsoft also submitted so-called ‘rebuttal’ arguments, 
> explaining why despite meeting the quantitative thresholds, these 
> four core platform services should not, in their view, qualify as 
> gateways.


We’ve had pretty obvious hints [since early September](https://www.theverge.com/2023/9/4/23858948/eu-microsoft-apple-bing-imessage-dma-gatekeepers-list-dispute) that iMessage and Bing would be considered exempt from “gatekeeper” status, and thus exempt from the DMA. Now that’s official.


But in November, when Apple changed course and [announced that it would support the RCS messaging standard](https://daringfireball.net/linked/2023/11/16/apple-rcs), many Apple critics/EC cheerleaders simply presumed that Apple’s change of mind on RCS was somehow the result of the EU’s regulatory muscle. This made zero sense, other than revealing an irrational, dare I say fanatical, belief in the righteousness of overzealous government regulation versus natural market forces. For one thing, it made no sense timing-wise: word leaked from the EU in September that iMessage was not going to be considered a gatekeeper — a decision made official this week — but somehow Apple announced “coming next year” support for RCS in November?


Second, the DMA makes no mention of “RCS” anywhere. It’s just not mentioned. There are provisions in the DMA regarding messaging platform “interoperability”, but that’s about some sort of [fantasy world where disparate platforms like iMessage, WhatsApp, Instagram DMs, and Facebook Messenger](https://www.eff.org/deeplinks/2022/04/eu-digital-markets-acts-interoperability-rule-addresses-important-need-raises) could be forced to allow the interchange of messages between platforms while maintaining end-to-end encryption, and open themselves to interop with upstarts like Signal. RCS isn’t an interop protocol between messaging platforms. RCS is a messaging platform itself — one that offers no encryption in its standard, and which is controlled by cell phone carriers. RCS is just a slightly better replacement for SMS.


The surprisingly-commonly-held assumption that the EC forced Apple’s change of mind on RCS is just lazy thinking: *Apple said, [for years](https://www.macrumors.com/2022/09/08/tim-cook-on-ios-rcs-buy-your-mom-an-iphone/), they didn’t want to support RCS (true); the DMA is imposing new regulations on Apple that will force it to do some things Apple doesn’t want to do (true); therefore it was the DMA that forced Apple to change its mind on RCS (fallacious conclusion)*. It also belies an ignorance of what iMessage is. iMessage is not SMS with blue bubbles and higher-resolution attachments. [iMessage is a wholly independent messaging platform that is offered as a free-of-charge service for Apple device owners](https://daringfireball.net/2023/12/beep_beep), with full-featured clients for Mac, iPad, and Vision. You can — and most people do — use your phone number as your primary unique identifier for iMessage, but you can also use any email address attached to your Apple ID account. Other platforms that have nothing to do with carrier-based SMS or RCS messaging use phone numbers for identifiers too — e.g. Signal and WhatsApp — but iMessage stands alone among popular services for allowing you to use it without even having a phone or phone number.


RCS is like SMS in that you must have a phone, must have an active SIM card with a cellular carrier, and can only use that phone to use RCS. You might say, “*Hey, wait a minute, I send and receive SMS messages in the Messages app on my iPad and Mac — not just my iPhone.”* But that’s just clever programming on Apple’s part. Every single green SMS message you send or receive on your iPad, Mac, or Vision Pro is being sent and received through your iPhone. Messages simply handles the “it just works” magic between your multiple devices to make it *seem* like other devices can act as true SMS client devices. Power your iPhone off and try to send or receive an SMS message from another Apple device. It doesn’t work, because it can’t work, because SMS is a phone carrier protocol. RCS is exactly the same in that regard. You need a phone to use RCS. You don’t need a phone to use iMessage.


So even if iMessage *had* been deemed a “gatekeeper” messaging platform by the European Commission — which it was not — adding RCS support to the iPhone Messages app would not have mattered a whit when it came to DMA compliance. The Messages app is a client for multiple messaging platforms — SMS and iMessage. It’s the iMessage platform that the DMA might have applied to. And adding support for RCS to the Messages app on iPhones wouldn’t have made any difference at all regarding interoperability with non-cellular “gatekeeping” messaging platforms like WhatsApp and Facebook Messenger.


But then why did Apple do a 180° turn on RCS? I can’t say for certain, alas, but after spending the last few months periodically poking around the trees inhabited by little birdies, I do have good news for fans of coercive government regulation. Apple’s hand was effectively forced. But by China, not the EU.


Chinese carriers have been [proponents of RCS for years](https://www.gsma.com/futurenetworks/latest-news/china-operators-make-major-rcs-commitment-whitepaper/), and last year, the Chinese government began the process of codifying into law that to achieve certification, [new 5G devices will be required to support RCS](https://www.miit.gov.cn/gzcy/yjzj/art/2023/art_2d5a7969581b4b12a78cd2c455649a8c.html). ([Here’s a good English translation on Reddit](https://www.reddit.com/r/UniversalProfile/comments/153rrwl/chinas_proposed_regulation_could_force_apple_to/) of the parts relevant to Apple.) Shockingly, the Chinese government seemingly isn’t concerned that the RCS standard has no provisions for encryption. The little birdies I’ve spoken to all said the same thing: iOS support for RCS is all about China.


Apple would prefer simply to continue ignoring RCS, on the grounds that they want to support neither any new non-E2EE protocols, nor any new carrier-controlled protocols (whether encrypted or not). But when the CCP says device makers must jump to sell their products in China, Apple asks “How high?”


China, unlike the EU, seemingly knows how to draft effective regulations to achieve specific goals.



| **Previous:** | [Phil Spencer Puts Apple’s Money Where His Mouth Is](https://daringfireball.net/2024/02/phil_spencer_puts_apples_money_where_his_mouth_is) |
| **Next:** | [Apple Sports](https://daringfireball.net/2024/02/apple_sports) |


PreviousNext