---
title: "DRM Ignorance is Expensive"
date: 2008-02-04
url: https://blog.codinghorror.com/drm-ignorance-is-expensive/
slug: drm-ignorance-is-expensive
word_count: 1121
---

I recently became the reluctant owner of an [Xbox 360](http://en.wikipedia.org/wiki/Xbox_360). Limping along with my ancient PlayStation 2 – I remember buying that thing on launch day way back in 2000 – was no longer viable in light of [my Rock Band addiction](https://blog.codinghorror.com/living-the-dream-rock-band/). I’ve been avoiding a new console purchase for as long as humanly possible, but the version of Rock Band offered on the PS2 is almost *criminally* crippled: it offers no downloadable content, no band customization, and a barely-there practice mode.


Although it was expensive, I’ve been quite happy with my Xbox 360 upgrade overall. I bought [the Xbox 360 Pro value bundle](http://www.amazon.com/exec/obidos/ASIN/B000W91YTA), so I own the more modern, much quieter “Falcon” revision of the console along with two games. The [optional VGA adapter](http://www.amazon.com/exec/obidos/ASIN/B000B6MLTG) works perfectly with my projector setup at 1024 x 768, and the Xbox Live internet experience is quite impressive and polished by now. I do wish WiFi was included in the box, rather than being yet another [$90 accessory](http://www.amazon.com/exec/obidos/ASIN/B000B6MLV4) I have to buy, but **hawking overpriced accessories is just the way the console economy works** – you have to factor the required extra controllers, memory cards, charging stations, audio/video cables, and so on into the overall cost of ownership. That’s the way it has always been for every console I’ve ever owned, going all the way back to the [Atari 2600](http://en.wikipedia.org/wiki/Atari_2600).


![](https://blog.codinghorror.com/content/images/2025/03/image-448.png)


I’ve purchased lots of downloadable content on the Xbox 360 at work, primarily new songs for Guitar Hero 2, Guitar Hero 3, and Rock Band. I foolishly assumed all along that it would be **no big deal to transfer that purchased content** if I ever purchased an Xbox 360 for my home.


Big mistake.


I didn’t realize **how precarious my understanding was of Xbox 360 digital rights management was**. If, like me, you believe that in the future...

- most consumer devices will not be complex general purpose computers, but simpler fixed function devices
- all content will be downloaded
- the hardware will be tightly controlled
- the delivery network will be private and commercially locked down


... then **for better or worse, products like the iPhone and Xbox 360 represent the future of computing**. Apple has already taken us [quite far down this road](https://blog.codinghorror.com/why-doesnt-anyone-give-a-crap-about-freedom-zero/), with tremendous commercial success. Thus, it behooves us to understand precisely how the Xbox 360’s mature, mainstream DRM model works. The Xbox 360 may or may not be around in five years, but it is quite likely that some form of its DRM will be.


Let me break it down for you, so you don’t make the same naïve mistake I did. All content you purchase and download on the Xbox 360 is keyed to two specific things:

1. The **hardware signature** of the Xbox 360 you purchased the content on
2. The **Xbox Live profile** that you purchased the content with


If you keep these two variables in mind, it’s easier to understand why things work the way they do. Also, remember that any Xbox Live account is inherently “online.” You’re logging in to a secure internet validation server every time you buy anything through your Xbox Live account.


It’s not *quite* as dire as it sounds, though. Pick your [dongle](http://en.wikipedia.org/wiki/Dongle):

1. **Xbox 360 hardware dongle**
All purchased content is available for use by *any* account on that particular console you purchased it on. You can share ownership of that content with anyone else who has physical access to your Xbox 360, whether their account is local (offline) or Xbox Live (online). Note that if your console hardware signature ever changes – say, if your console fails and you get a replacement – you’re in trouble.
2. **Xbox Live profile dongle**
As long as you’re logged in to Xbox Live (and thus by definition using an Xbox 360 connected to the internet), you can re-download purchased content and play it on *any* Xbox 360. How do you transport your profile? Through the removable hard drive or a memory card. The hard drive works best, as you’ll save yourself some download time.


It is not possible to copy an Xbox Live profile; every login writes a unique key to the profile, and all subsequent logins validate the expected key. It is possible to perform an “account recovery” and move the account, but doing so automatically invalidates *any* other copies of the profile. The cardinal rule is this: **there can only ever be one valid physical copy of an Xbox Live profile at any given time**. Duplication is not allowed and rigorously enforced server-side.


The user penalty for hardware failure, however, is pretty severe; it sounds like iTunes has a [better hardware failure recovery model](https://web.archive.org/web/20080317034921/http://perfectcr.com/archives/41-Dude,-Wheres-my-offline-Xbox-Live-Marketplace-Content.html) for its song DRM:


> Microsoft has every right to protect their content, but to punish those who have had their consoles replaced due to failure is unacceptable. I see threads appear daily on all the popular forums about this issue. Typically it takes three to four weeks to get consoles replaced by Microsoft. Little do these users know their [newly repaired Xboxes will appear to be someone else’s Xbox to the DRM].
> I don’t intend to provide a solution to the problem here. I only want to bring attention to the issue. I am sure an iTunes like approach could be implemented where users can “authorize” and “deauthorize” the console tied to their content. I am just surprised that a software company like Microsoft cannot find a better solution than creating dummy accounts and asking users to call 1-800-4-MYXBOX time and time again in the hopes of getting their points refunded just so they can access their content offline.


Getting back to my specific problem: how do I transfer the licenses for all those songs I bought to my home Xbox? I experimented with Microsoft’s recommended solution of storing my Xbox Live profile on a memory card, but this meant I’d be schlepping a memory card dongle back and forth from home to work in perpetuity. That’s not practical or tenable.


In the end, I broke down and **re-purchased 11,240 MS Points worth of Guitar Hero 2, Guitar Hero 3, and Rock Band songs through my personal Xbox Live profile on my home Xbox 360**. If you’re keeping score at home that’s $140.50 in real money. To buy the exact same content. Again.


I have nobody to blame but myself, I suppose. DRM sucks, but it’s unavoidable and arguably the future, in the form of ubiquitous consumer devices like the Xbox 360 and iPhone. I’m not asking you to like it. Nobody likes it. But at the very least understand how it works, because as I recently found out, **DRM ignorance is expensive**.

[gaming consoles](https://blog.codinghorror.com/tag/gaming-consoles/)
[drm](https://blog.codinghorror.com/tag/drm/)
[xbox 360](https://blog.codinghorror.com/tag/xbox-360/)
[software bundles](https://blog.codinghorror.com/tag/software-bundles/)
[gaming experience](https://blog.codinghorror.com/tag/gaming-experience/)
