---
title: "I Just Logged In As You"
date: 2009-05-03
url: https://blog.codinghorror.com/i-just-logged-in-as-you/
slug: i-just-logged-in-as-you
word_count: 521
---

I received this anonymous email a few days ago:


> I found what one could call a security hole in Stackoverflow. I’m curious enough to go digging around for holes, but too ethical to actually do anything with them. However, I’m afraid that by pointing it out I’ll get banned, because a good member doesn’t poke around like I just did. I promise I did nothing with what I found out besides confirm the hole.
> You may be wondering why I’m e-mailing you personally, rather than [[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection). It’ll make sense when I reveal the hole, which is...
> I logged in as you.
> How? Well, there were two pieces of the puzzle, the password and the openid provider. I had a possible password; today your blog post revealed the openid provider. I logged in, freaked out that it *actually worked*, then logged out. The only reason I had the password is because your password is totally inadequate for someone running a site like StackOverflow. I don’t want to go into any more detail than that, but man - dictionary password!
> I’ve read about the secret “hacker” badge... if you’re not going to punish me for my transgression, then I will reveal who I am and I sure wouldn’t mind getting it. Still, I can understand if you’re upset - I wouldn’t want someone else digging up my password. (That’s why I send this friendly e-mail instead of hoarding, or worst, selling, the information.)
> Please, go change your openid password, before someone less ethical than I finds it.
> - A friend of the site


These are the kinds of emails that make your blood run cold. Good thing I haven’t made too many enemies. Today, I mean. So far. The day’s not over, yet.


Is it true? Did someone just log in as me? I checked the OpenID logs, and sure enough, **there was a valid login from an IP address I didn’t recognize**. He wasn’t bluffing. *He really did log in as me.*


While it’s true I probably should have used a more secure password, in my defense:

1. The particular OpenID account I use is typically for low-value logins like blog comments and so forth. It’s not exactly a high security form of identity for the use I have in mind.*
2. The password *was* relatively simple, but I wouldn’t go so far as to characterize it as a “dictionary password” – it wasn’t quite “password1” or “monkey” or “happiness,” or anything like that. It was weak, yes, but [dictionary password attacks](https://blog.codinghorror.com/dictionary-attacks-101/), like all brute force attacks, [are still for dummies](https://blog.codinghorror.com/hardware-assisted-brute-force-attacks-still-for-dummies/).


What’s interesting about this, though, is **how it happened**. I’ll reveal that tomorrow, with this one hint: I’ve talked about this exact sort of vulnerability several times on this very blog.


Until then, take your best guess: **how do you think this person discovered my password? **I’ll highlight the best response tomorrow with the answer.


*Although as a Stack Overflow moderator I have unusual powers and probably should have used an alternate OpenID with more security.

[security](https://blog.codinghorror.com/tag/security/)
[ethical hacking](https://blog.codinghorror.com/tag/ethical-hacking/)
[password security](https://blog.codinghorror.com/tag/password-security/)
[vulnerability](https://blog.codinghorror.com/tag/vulnerability/)
[openid](https://blog.codinghorror.com/tag/openid/)
