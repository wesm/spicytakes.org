---
title: "Beeper? I Hardly Knew Her."
date: 2023-12-10
url: https://daringfireball.net/2023/12/beeper_i_hardly_knew_her
slug: beeper_i_hardly_knew_her
word_count: 2219
---


[Beeper](https://www.beeper.com/) is a company founded by Eric Migicovsky, who is best known as the founder of the now-defunct [Pebble](https://en.wikipedia.org/wiki/Pebble_(watch)), [which made groundbreaking smartwatches a decade ago](https://daringfireball.net/search/pebble+watch). Migicovsky founded Beeper [to create a meta-platform](https://blog.beeper.com/p/the-universal-communication-bus-42dfb9a141ad) for disparate messaging apps — a single messaging client that could connect to dozens of different platforms like WhatsApp, Telegram, Twitter DMs, and more. Until this week, Beeper was best known for an app it has now rebranded as [Beeper Cloud](https://www.beeper.com/cloud). Beeper Cloud works as a single client for a slew of different messaging platforms — including iMessage — by way of relay servers. For each Beeper Cloud user, Beeper runs a virtual server in the cloud, and your local Beeper Cloud app communicates with that relay server. For each messaging service you connect to Beeper Cloud, the relay server needs to store your login credentials. You can also self-host your own server, which they describe as “[possible, but not an easy task right now](https://github.com/beeper/self-host)”, as it requires Linux system administration skills.


If you’re thinking that running a server instance for each user sounds like something that would be hard to scale, you’re right. [Beeper Cloud launched in January 2021](https://techcrunch.com/2021/01/21/pebble-founder-launches-beeper-a-universal-chat-app-that-works-with-imessage-and-others/), but there remains a (seemingly long) waitlist to get access today, nearly three years later.


If you’re thinking that giving your iCloud account credentials to a third party so that they can sign you into iMessage on a virtual MacOS machine in the cloud sounds like a sketchy idea, you’re correct. It’s a terrible idea.


If you’re thinking that a scheme like this sounds familiar, you’re right — there are a few other “universal chat” services which have also been in the news recently. The best is [Texts](https://texts.com/), a currently-desktop-only $12.50/month app created by Kishan Bagaria, and [recently acquired by Automattic](https://ma.tt/2023/10/texts-joins-automattic/) (the parent company of WordPress.com, Tumblr, and Day One, [among numerous other apps and services](https://automattic.com/)). Texts directly communicates using the protocols for services like WhatsApp and Twitter DMs, but for iMessage — which of course has no open APIs for third-party clients — communicates via AppleScript and accessibility APIs with Apple’s Messages app running on your own Mac.


The other such service I’m aware of is [Sunbird](https://www.sunbirdapp.com/), which was recently in the news for a partnership with upstart Android phone maker [Nothing](https://us.nothing.tech/pages/phone-2), wherein they created a white-label Android app called Nothing Chat, that brought iMessage support to Nothing phones by way of relay servers running virtual MacOS instances. [Turns out Nothing Chat and Sunbird were a privacy disaster](https://texts.blog/2023/11/18/sunbird-security/), with message contents and attachments stored unencrypted in a database, and some network traffic being transmitted over unencrypted HTTP. This, despite [claims at launch](https://www.youtube.com/watch?v=A9PP8AeSbbo) that everything was “end-to-end encrypted”. Nothing Chat was available in the Play Store for just four days last month [before being pulled after the security issues were discovered](https://www.theverge.com/2023/11/18/23966781/nothing-chats-imessage-unencrypted-sunbird-plaintext).


So, to recap the various third-party apps that support (or in the case of Sunbird/Nothing, support*ed*) iMessage:

- Beeper Cloud supports iMessage by way of relay servers in the cloud, to use which you must entrust Beeper with your iCloud account password. An [app-specific iCloud password](https://support.apple.com/en-us/102654) won’t work, because Messages relies upon your system-level iCloud account on MacOS. [**Update:** As of October, Beeper Cloud, although architected to rely upon cloud relay servers, [no longer uses Macs](https://blog.beeper.com/p/beeper-mini-is-back).] Beeper also relies upon relay servers for WhatsApp and Signal. [Beeper swears up and down you can trust them with this](https://www.beeper.com/faq#how-does-beeper-connect-to-encrypted-chat-networks-like-imessage-signal-whatsapp). They even have [a client for iOS on the App Store](https://apps.apple.com/us/app/beeper-universal-messenger/id1551695541?platform=iphone) (for now).
- Texts supports iMessage by communicating with the local instance of Apple’s Messages app running on the same Mac Texts is running on. No relay servers, and you never give Texts your iCloud password. It’s just one app (Texts) communicating with another app (Messages), both running locally on your Mac.
- Sunbird/Nothing Chat supported iMessage using relay servers, and it was revealed to be a security fiasco.


That brings us to this week, [when Beeper launched Beeper Mini](https://www.theverge.com/2023/12/5/23987817/beeper-mini-imessage-android-reverse-engineer) — a $2/month Android app that worked as a standalone iMessage client, thanks to the [reverse engineering efforts of a 16-year-old high school student](https://github.com/JJTech0130/pypush) (who goes by “JJTech1030” on GitHub, and apparently wishes to remain pseudonymous). Beeper Mini’s launch [garnered a lot of press attention](https://www.techmeme.com/231205/p18#a231205p18) — *blue bubbles for Android, finally*.


Quinn Nelson had early access to Beeper Mini, and [made an exemplary video showing it in action](https://www.youtube.com/watch?v=S24TDRxEna4) and explaining in detail how it worked — including using [JJTech1030’s open-source proof of concept](https://github.com/JJTech0130/pypush) from the terminal on a Linux laptop. If you’re curious about how Beeper Mini pulled this off and what it looked like in action, watch Nelson’s video.


I installed Beeper Mini on my Pixel 4, and it worked like a charm. In addition to working seamlessly — including support for group chats, tapbacks (albeit substituting animated emoji in place of Apple’s monochromatic badges), undoing sent messages, and editing recent messages — it’s just a really nice chat app. It looks a lot like what I’d imagine an official iMessage Android client from Apple would look like. Just like with an iPhone, Beeper Mini even worked without requiring you to sign in to an iCloud account. Beeper Mini reverse-engineered the way that Apple creates a new implicit iMessage account based on your phone number, via a one-time exchange of keys sent through SMS.1 But, if you wanted to use your existing iCloud account with Beeper Mini, you were able to sign in — which, unlike Beeper Cloud, worked with an app-specific password. When I tried Beeper Mini, I used a secondary iCloud account that I use for testing and product reviews, but even with that account, I would not have signed in if Beeper Mini didn’t support app-specific passwords.


[Migicovsky told The Verge](https://www.theverge.com/2023/12/5/23987817/beeper-mini-imessage-android-reverse-engineer) and Nelson that Beeper believed Apple would be unable to cut off their technique without also breaking iMessage for a significant number of iMessage users on actual Apple devices. I found that hard to believe, given that part of Beeper’s technique involves masquerading as a legitimate Apple device, re-using device identifiers. Others speculated that even if Apple *could* cut off Beeper Mini, either through technical changes or legal threats, they wouldn’t, lest they draw the ire of people happy to see iMessage available on Android. [E.g., Nilay Patel](https://www.threads.net/@reckless1280/post/C0eh1CHLbU-):


> Someone like Beeper finally reverse-engineering iMessage in this 
> was way inevitable and will cause Apple infinitely more pain and 
> bad press in trying to shut it down than if it had just made 
> things interoperable to begin with.


I found that unlikely as well. On Thursday night, two days after Beeper Mini launched, I wrote [on Threads](https://www.threads.net/@gruber/post/C0k1VgyMGZN) and [Mastodon](https://mastodon.social/@gruber/111542468082463653):


> My prediction is that Apple will make changes — fixing bugs 
> and/or closing loopholes — that break Beeper Mini. It’s untenable 
> that there’s unsanctioned client software for a messaging platform 
> for which privacy and security are a primary feature. 
> It’s a very nice app, remarkably clever, and for now works like a 
> charm, but if Apple wanted an iMessage client for Android they’d 
> release an iMessage client for Android. Seems irresponsible for 
> Beeper to charge a subscription for an unsupported service. 
> I think the only way Apple doesn’t break Beeper Mini by closing 
> loopholes is if they can’t, but I find that unlikely.


Glad I predicted that Thursday night, because on Friday, [Beeper Mini stopped working](https://www.techmeme.com/231208/p23#a231208p23). Apple also issued the following statement, which doesn’t mention Beeper by name, but didn’t need to:


> At Apple, we build our products and services with industry-leading 
> privacy and security technologies designed to give users control 
> of their data and keep personal information safe. We took steps to 
> protect our users by blocking techniques that exploit fake 
> credentials in order to gain access to iMessage. These techniques 
> posed significant risks to user security and privacy, including 
> the potential for metadata exposure and enabling unwanted 
> messages, spam, and phishing attacks. We will continue to make 
> updates in the future to protect our users.


That last sentence translates to “*We’ll keep closing loopholes if Beeper Mini finds another workaround.*”


It’s true that a lot of people — [including me](https://daringfireball.net/linked/2022/01/19/cue-imessage-android) — wish Apple would release an iMessage client for Android.2 As revealed in a deposition that was part of the *Epic v. Apple* Fortnight lawsuit, [Eddy Cue himself pushed for Apple to release an iMessage client for Android back in 2013](https://www.theverge.com/2021/4/27/22406303/imessage-android-eddy-cue-emails-apple-epic-deposition), when Facebook bought WhatsApp for $19 billion. But that’s Apple’s decision to make, and they obviously decided against it, choosing instead to keep iMessage as a value-add exclusively for Apple devices.


What I meant by it being “untenable” for Apple to look the other way at Beeper Mini wasn’t that Beeper made legitimate use of iMessage insecure. That’s part of the point of end-to-end encryption. But it was untenable *perception-wise* for Apple to allow unauthorized client software on a messaging platform heralded first and foremost for its *Apple-provided* privacy and security. Apple had even lost control over new account signups. That couldn’t stand, and that seems so obvious to me that I found it hard to believe Migicovsky truly believed Apple would allow it.3


But reading Migicovsky’s remarks to The Verge’s David Pierce in the wake of Apple’s response, [it seems he really is surprised](https://www.theverge.com/2023/12/9/23995150/beeper-imessage-android-apple-statement):


> Founder Eric Migicovsky said on Friday that he simply didn’t understand why Apple would block his app: “if Apple truly cares about the privacy and security of their own iPhone users, why would they stop a service that enables their own users to now send encrypted messages to Android users, rather than using unsecure SMS?”
> Migicovsky says now that his stance hasn’t changed, even after hearing Apple’s statement. He says he’d be happy to share Beeper’s code with Apple for a security review, so that it could be sure of Beeper’s security practices. Then he stops himself. “But I reject that entire premise! Because the position we’re starting from is that iPhone users can’t talk to Android users except through unencrypted messages.”


Well, you know, unless they use WhatsApp or Signal [or, now, finally, Facebook Messenger](https://arstechnica.com/tech-policy/2023/12/meta-defies-fbi-opposition-to-encryption-brings-e2ee-to-facebook-messenger/). Again, I wish Apple would release an iMessage client for Android. (But what I really wish is that they’d done so a decade ago, before current platforms had gotten so entrenched, country-by-country around the world.) But I don’t buy the argument that Apple is under any sort of ethical obligation to do so. Part of what makes iMessage so valuable is its seamlessness on iPhones — that you don’t even need to create an account when using your phone number as your identifier. What Migicovsky is implicitly arguing is that Apple is obliged to make E2EE messaging as seamless for Android users as they’ve made it for iPhone users.


---

1. This is actually pretty interesting. Part of the onboarding for Beeper Mini on Android requires granting it permission to read and send SMS messages. Beeper Mini does not work as an SMS messaging client (although they supposedly have (had?) plans to add that in the future — on Android, third-party apps can register to serve as the system’s default app for SMS, like you can on iOS for things like email and web browsing), but it needs SMS read and write access in order to exchange keys to allow you to register your cellular phone number with iMessage. I believe this is what the Messages app on iPhone does too, but iOS Messages hides this handshake-over-SMS from users — it just happens behind the scenes. On my Pixel, those SMS messages were visible in the system Messages app. First, Beeper Mini sent an SMS to 22223333 (which I presume is an Apple-controlled shortcode?):
`REG-REQ?v=3;t=742427F5960C7B246950C6CD0F8FA3DB
C8AF44B268931592099175BAE9D06618;r=2202323240;
`
Then 22223333 responded with:
`REG-RESP?v=3;r=2202323240;n=+1267•••••••;
s=026570EDECFFFFFFFF6F6BC100F449F092B7ABCB7A85ADDB2B89B9BD64
`
(I’ve replaced the last 7 digits of my Pixel’s phone number with bullets in the response. I also added line breaks for formatting — the original SMS messages were one line each.) This request-response handshake seems to be how Apple registers a phone number for iMessage without an associated Apple ID. ↩︎︎
2. Or open an iMessage API that could be used to create third-party clients like Beeper Mini. But an API seems far less likely than Apple releasing an iMessage app. Apple releasing an iMessage client for Android would be a pleasant surprise; Apple opening a third-party iMessage API would be shocking. ↩︎
3. It’s also the case that Apple just eats the cost of running iMessage — a fast, reliable messaging platform with over a billion users, and, by any reasonable estimate, *billions* of messages sent every single day (and thus, I’d wager, *trillions* per year) — at no charge and with no ads, with high-resolution image and video attachments. It’s subsidized by the sale of Apple devices. Would it pose a financial hardship to Apple to just offer iMessage free of charge to Android users? No. But the bill for running iMessage is surely significant. The whole business model for Beeper Mini presupposed that Apple should just foot the bill for the usage of Beeper’s (paying!) customers, as though iMessage is a public resource, or part of your cellular phone service, like SMS/MMS/RCS. ↩︎︎



| **Previous:** | [More on Sam Altman’s Ouster From OpenAI](https://daringfireball.net/2023/11/more_altman_openai) |
| **Next:** | [Beeper Mini Is Back, But Without Phone Number Registration](https://daringfireball.net/2023/12/beeper_mini_is_back) |


PreviousNext