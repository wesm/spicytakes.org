---
title: "Make Your Email Hacker Proof"
date: 2012-04-17
url: https://blog.codinghorror.com/make-your-email-hacker-proof/
slug: make-your-email-hacker-proof
word_count: 1251
---

It’s only a matter of time until your email gets hacked. Don’t believe me? Just read [this harrowing cautionary tale](http://www.theatlantic.com/magazine/archive/2011/11/hacked/8673/?single_page=true).


> When [my wife] came back to her desk, half an hour later, she couldn’t log into Gmail at all. By that time, I was up and looking at e‑mail, and we both quickly saw what the real problem was. In my inbox I found a message purporting to be from her, followed by a quickly proliferating stream of concerned responses from friends and acquaintances, all about the fact that she had been “mugged in Madrid.” The account had seemed sluggish earlier that morning because my wife had tried to use it at just the moment a hacker was taking it over and changing its settings – including the password, so that she couldn’t log in again.
> …
> The greatest practical fear for my wife and me was that, even if she eventually managed to retrieve her records, so much of our personal and financial data would be in someone else’s presumably hostile hands that we would spend our remaining years looking over our shoulders, wondering how and when something would be put to damaging use. At some point over the past six years, **our [email] correspondence would certainly have included every number or code that was important to us – credit card numbers, bank-account information, medical info, and any other sensitive data you can imagine.**


Now get everyone you know to read it, too. Please. It’s for their own good.


Your email is [the skeleton key](https://blog.codinghorror.com/please-give-us-your-email-password/) to your online identity. When you lose control of your email to a hacker – not if, but *when* you lose control of your email to a hacker – the situation is dire. Email is a one stop shop for online identity theft. You should start thinking of security for your email as roughly equivalent to the sort of security you’d want on your bank account. It’s exceedingly close to that in practice.


The good news, at least if you use Gmail, is that **you can make your email virtually hacker-proof today, provided you own a cell phone**. The fancy geek technical term for this is [two factor authentication](https://blog.codinghorror.com/what-you-have-what-you-know-what-you-are/), but that doesn’t matter right now. What matters is that until you turn this on, your email is vulnerable. So let's get started. Not tomorrow. Not next week. [*Right. Freaking. Now.*](https://blog.codinghorror.com/yes-but-what-have-you-done/)


### Go to your Google Account Settings


![](https://blog.codinghorror.com/content/images/2025/04/image-619.png)


Make sure you’re logged in. Expand the little drop-down user info panel at the top right of most Google pages. From here, click “Account” to view your account settings.


![](https://blog.codinghorror.com/content/images/2025/04/image-618.png)


On the account settings page, click “edit” next to 2-step verification and turn it on.


### Have Your Cell Phone Ready


Gmail will walk you through the next few steps. You just need a telephone that can receive SMS text messages. Enter the numeric code sent through the text message to proceed.


![](https://blog.codinghorror.com/content/images/2025/04/image-617.png)


### Now Log In With Your Password and a PIN


Now your password alone is no longer enough to access your email.


![](https://blog.codinghorror.com/content/images/2025/04/image-616.png)


Once this is enabled, **accessing your email always requires the password, *and* a code delivered via your cell phone**. (You can check the “remember me for 30 days on this device” checkbox so you don’t have to do this every time.) With this in place, even if they discover your super sekrit email password, would-be hackers can’t do anything useful with it! To access your email, they’d need to somehow gain control of your cell phone, too. I can’t see that happening unless you’re in some sort of hostage situation, and at that point I think email security is the least of your problems.


### What If I Lose My Cell Phone?


Your cell phone isn’t the only way to get the secondary PIN you need to access your email. On the account page there are multiple ways to generate verification codes, including adding a secondary backup phone number, and downloading mobile applications that can generate verification codes without a text message (but that requires a smart phone, naturally).


![](https://blog.codinghorror.com/content/images/2025/04/image-615.png)


This also includes the never-fails-always-works option: **printing out the single-use backup verification codes on a piece of paper**. Go do this now. *Right now! *And keep those backup codes with you at all times. Put them in your wallet, purse, man-purse, or whatever it is that travels with you most often when you get out of bed.


![](https://blog.codinghorror.com/content/images/2025/04/image-614.png)


### What About Apps That Access Email?


Applications or websites that access your email, and thus necessarily store your email address and password, are also affected. They have no idea that they now need to enter a PIN, too, so they’ll all be broken. You’ll need to **generate app-specific passwords for your email**. To do that, visit the accounts page.


![](https://blog.codinghorror.com/content/images/2025/04/image-613.png)


Click on authorizing applications & sites, then enter a name for the application and click the Generate Password button.


![](https://blog.codinghorror.com/content/images/2025/04/image-612.png)


Let me be clear about this, because it can be confusing: **enter that specially generated password in the application, *not* your master email password**.


This effectively creates a list of passwords specific to each application. So you can see the date each one was last used, and revoke each app’s permission to touch your email individually as necessary without ever revealing your primary email password to *any* application, ever. See, I told you, there is a method to the apparent madness.


### But I Don’t Use Gmail


Either nag your email provider to provide two-factor authentication, or switch over. Email security is critically important these days, and switching is easy(ish). Gmail has had fully secure connections for [quite a while now](https://blog.codinghorror.com/should-all-web-traffic-be-encrypted/), and once you add two-factor authentication to the mix, that’s about as much online email safety as you can reasonably hope to achieve short of going back to snail mail.


### Hey, This Sounds Like a Pain!


I know what you’re thinking. Yes, this is a pain in the ass. I’ll fully acknowledge that. But you know what’s an even *bigger* pain in the ass? Having your entire online identity stolen and trashed by a hacker who happens to obtain your email password one day. Remember that article I exhorted you to read at the beginning? Oh, you didn’t read it? Go freaking read it now!


Permit me to [channel Jamie Zawinski](https://blog.codinghorror.com/whats-your-backup-strategy/) one last time: “OMG, entering these email codes on every device I access email would be a lot of work! That sounds like a hassle!” **Shut up. I know things. You will listen to me. Do it anyway.**


I’ve been living with this scheme for a few months now, and I’ve convinced my wife to as well. I won’t lie to you; it hasn’t all been wine and roses for us either. But it is inconvenient in the same way that bank vaults and door locks are. The upside is that once you enable this, your email becomes **extremely secure**, to the point that you can (and I regularly do) email yourself highly sensitive data like passwords and logins to other sites you visit so you can easily retrieve them later.


If you choose not to do this, well, at least you’ve educated yourself about the risks. And I hope you’re extremely careful with your email password and change it regularly to something complex. You’re making life all too easy for the hackers who make a fabulous living from stealing and permanently defacing online identities *just like yours*.

[security](https://blog.codinghorror.com/tag/security/)
[email security](https://blog.codinghorror.com/tag/email-security/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[cyber security](https://blog.codinghorror.com/tag/cyber-security/)
[data protection](https://blog.codinghorror.com/tag/data-protection/)
