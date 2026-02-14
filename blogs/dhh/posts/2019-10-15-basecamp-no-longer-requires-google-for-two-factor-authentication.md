---
title: "Basecamp no longer requires Google for two-factor authentication"
date: 2019-10-15
url: https://signalvnoise.com/svn3/basecamp-no-longer-requires-google-for-two-factor-authentication/
slug: basecamp-no-longer-requires-google-for-two-factor-authentication
word_count: 454
---


When it became clear to us last year that using SMS for two-factor authentication (2FA) was insecure, we kinda panicked. We’d spent a lot of time originally building that SMS-based 2FA login system for Basecamp, and the prospect of having to build an entirely new system compatible with proper authentication apps seemed daunting. Especially with major security liability hanging over our head.


So we went the easy route, and [handed the 2FA authentication flow over to Google](https://signalvnoise.com/svn3/protect-your-basecamp-login-with-googles-two-factor-authentication/), using their Google Sign-In APIs. Now, that certainly gave us an immediate and secure solution. Nobody is disputing that Google knows security.


But requiring people to have a Google account to get a 2FA-protected Basecamp was an uncomfortable compromise. There are about a million good reasons for why you wouldn’t want Google to know everything about when you log into apps all over the internet. Google’s business is literally based on collecting as much data as possible, so it can use it all against you for ad targeting. That’s just not a regime we feel comfortable encouraging, let alone requiring.


So I’m thrilled to announce that we got our shit together and built our own, wonderful, and secure 2FA login protection for Basecamp. Google Sign-In still works, but it’s deprecated, and we’ll no longer be recommending it going forward.


Our new secure 2FA solution is built on the TOTP standard with backup codes as a fallback. So you can use any TOTP compatible authentication app, like [Authy](https://authy.com/features/), [1Password](https://1password.com), or [Duo](https://duo.com), and it works for all versions of Basecamp (here’s how to set it up [in Basecamp 3](https://3.basecamp-help.com/article/443-two-factor-authentication-2fa) and [Basecamp 2](https://2.basecamp-help.com/article/428-enable-two-factor-authentication)), as well as our legacy apps Highrise, Backpack, and Campfire.


Big kudos to [Rosa Gutiérrez](https://twitter.com/Rosapolis) from our Security, Infrastructure & Performance team for putting our fears about doing our own TOTP-based 2FA system to shame. She led the project, did the work, and the final result is just great.


Finally, it feels good to have one additional area of the business free from Big Tech entanglement. We also dumped Google Analytics a few months back from Basecamp.com (relying on [Clicky.com](https://clicky.com) instead), and we’ll continue the work to untangle ourselves from Google and the rest of the industry behemoths. It’s a long slog, it’s unlikely ever to be fully complete, but [every little bit helps](https://signalvnoise.com/svn3/every-little-bit-helps/).


Oh, and please, if you haven’t already, turn on 2FA to protect your Basecamp account. And if you aren’t already, use a password manager, like [1password](https://1password.com). If you’re reusing a password on Basecamp, and you’re not protected by 2FA, you’re at a grave risk of having your account compromised. [We work hard to protect everyone at Basecamp](https://signalvnoise.com/svn3/yesterdays-mass-login-attack-on-basecamp-is-another-reminder-to-protect-yourself/), but nothing will protect you online like using 2FA and a password manager everywhere you go.

