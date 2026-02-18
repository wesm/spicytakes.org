---
title: "Beeper Mini Is Back, But Without Phone Number Registration"
date: 2023-12-11
url: https://daringfireball.net/2023/12/beeper_mini_is_back
slug: beeper_mini_is_back
word_count: 1259
---


As hinted by their team over the weekend, Beeper is going to play the cat-and-mouse game with Apple. [From cofounders Eric Migicovsky and Brad Murray on the Beeper blog](https://blog.beeper.com/p/beeper-mini-is-back):


> We’ve created an updated version of Beeper Mini that fixes an 
> issue that caused messages not to be sent or received.


That’s quite the euphemistic description of the situation.


> Phone number registration is not working yet. All users must now 
> sign in with an Apple ID. Messages will be sent and received via 
> your email address rather than phone number. We’re currently 
> working on a fix for this.


In other words, what remains broken is the implicit creation of an iMessage account based on the cellular phone number of your device. I described this process in broad terms [in a footnote on my column yesterday](https://daringfireball.net/2023/12/beeper_i_hardly_knew_her#fn1-2023-12-10). It’s a magically-invisible-to-the-user process that’s been part of iMessage since it first debuted as an iOS-only feature in iOS 5.1 (At the time, “iOS” covered iPhone, iPad, and iPod Touch.)


The “magic” is that you don’t have to sign up for an account, or create a new username or account identifier. You just send a message from your phone number to another phone number, and if both numbers are registered for iMessage, the message goes over iMessage instead of SMS, *even if you don’t have an Apple ID*. Beeper had that working last week. Now, Beeper users need to have an Apple ID, and sign into that Apple ID within Beeper. (Beeper should actively encourage users to create and use [an app-specific Apple ID password](https://support.apple.com/en-us/102654) for Beeper.)


I can confirm that today’s update to Beeper Mini in the Play Store restores the ability to use iMessage, if you’re signed into an Apple ID.


> We’ve made Beeper free to use. Things have been a bit chaotic, and 
> we’re not comfortable subjecting paying users to this. As soon as 
> things stabilize (we hope they will), we’ll look at turning on 
> subscriptions again. If you want to keep supporting us, feel free 
> to leave the subscription on 🙂.


Good on them. [Like I wrote](https://daringfireball.net/2023/12/beeper_i_hardly_knew_her), it was irresponsible to charge a subscription fee for a service they can’t guarantee access to.


> Beeper Mini launched on Tuesday and rocketed to top 20 of Play 
> Store charts. It was an instant hit. From what we can tell, Beeper 
> Mini was the fastest growing paid Android application launch in 
> history. In the first 48 hours, it was downloaded by more than 
> 100,000 people.


Making it free (instead of a $2/month subscription with 7-day free trial) should only help its popularity, but I think it’s an open question how much demand there is for this. iMessage users might wish their Android-owning friends would install it, but are typical Android users interested? If Android SMS users were interested in installing a third-party app to enable better cross-platform messaging, wouldn’t they be suggesting to their iPhone-using friends and family that *they* be the ones who install WhatsApp or Signal or something?


> Note: Beeper Cloud’s new Oct 2023 iMessage bridge never used Mac 
>       relay servers and still does not today. It uses a similar 
>       method to Beeper Mini, but runs on a cloud server.


Beeper Cloud *was* relying on Mac relay servers prior to October. And I think regardless of whether the relay servers are Macs or Linux boxes, it doesn’t change the fact that it’s a sketchy idea to entrust a relay server with your Apple ID credentials. But I think this recent change to Beeper Cloud means that you can use an app-specific password with that, too, just like with Beeper Mini — you never need to share your main Apple ID password.


> Many people have asked, ‘why don’t people just use Signal or 
> WhatsApp?’. The answer is that Messages App [*sic*] is the default chat 
> app for all iPhone customers. Not only is it the [default](https://en.wikipedia.org/wiki/Default_effect), iOS 
> makes it impossible to change the default chat app. In the US, 
> where the majority of people have iPhones, this means that the 
> easiest way to chat is by tapping on your friend’s name in your 
> contact list and hitting the ‘message’ button.


This is disingenuous. It is true that Apple does not allow third-party apps to handle anything related to your cellular account. So cellular phone calls only go through the built-in Phone app, and SMS messages only go through the Messages app. Messages isn’t merely the default handler for SMS, it’s the *only* handler for SMS. But there is no default for “chat”. iPhone users around the world, in countries where messaging is dominated by apps like WhatsApp or [Line](https://line.me/en/), have no problem ignoring Apple’s Messages app. People don’t start new chats in the Contacts app; they just open the messaging app they want to use. That’s the easiest way to chat.


What they’re really arguing here is that Beeper is entitled to piggyback on the work Apple has done to make iMessage texting seamless between iOS and Mac users — and more so, that Beeper is [entitled to free use of Apple’s iMessage server and networking infrastructure](https://daringfireball.net/2023/12/beeper_i_hardly_knew_her#fn3-2023-12-10).


> We deeply object to the allegation that Beeper Mini ‘poses 
> significant risks to user security and privacy’. This is 
> completely untrue. As we explained above, the opposite is actually 
> true. Beeper Mini increases the security and privacy of both 
> Android and iPhone customers. To prove this, we published a 
> detailed [blog post](https://blog.beeper.com/p/how-beeper-mini-works) about how the app keeps data secure and 
> private. Beeper Mini is end-to-end encrypted. The underlying 
> connection method is [open source](https://github.com/JJTech0130/pypush#dataplist-and-mac-serial-numbers), for anyone to review.


Apple guarantees the security of both the protocol (iMessage) *and* the client software (Messages). In fact, because Messages only runs on Apple devices, Apple further guarantees the security of the underlying operating system and hardware that Messages (the app) runs on, and that all iMessage messages are sent between. With Beeper Mini in the mix, Apple can only guarantee the protocol and *your* client software, if you’re using Messages. Is Beeper Mini storing cached message content and attachments securely on device? Is it transmitting privacy-sensitive metadata back to Beeper with analytics or crash logs? (Beeper Mini has a preference, “Share Diagnostics”, that is on by default but can be disabled.) Beeper can (and does!) vouch for the privacy and security of their client app, but Apple can’t. Beeper is correctly arguing that Beeper Mini does not (and cannot) compromise the security of the iMessage protocol, but that doesn’t mean that its existence doesn’t open security concerns for Apple and its users. And [as I wrote yesterday](https://daringfireball.net/2023/12/beeper_i_hardly_knew_her), the existence of an unauthorized client on a supposedly closed platform creates a genuine *perception* problem for Apple: if Apple can’t control the clients permitted to connect to iMessage, it looks like they’ve lost control of the platform. And to some degree, they *have* lost control over the iMessage platform.


It’s fun watching this cat-and-mouse game from the sidelines, but if I were Beeper, I wouldn’t want to be playing.


---

1. It’s worth rewatching [Scott Forstall’s introduction of iMessage at WWDC 2011](https://www.youtube.com/watch?v=NrBIgjodpFs). I know Apple is not going back, but man, I do miss live on-stage demos. The interplay between Forstall and Joz was actually funny, and the demo was completely live. ↩︎



| **Previous:** | [Beeper? I Hardly Knew Her.](https://daringfireball.net/2023/12/beeper_i_hardly_knew_her) |
| **Next:** | [iOS 17.3, Now in Beta, Includes New ‘Stolen Device Protection’ Feature](https://daringfireball.net/2023/12/ios_17-3_stolen_device_protection) |


PreviousNext