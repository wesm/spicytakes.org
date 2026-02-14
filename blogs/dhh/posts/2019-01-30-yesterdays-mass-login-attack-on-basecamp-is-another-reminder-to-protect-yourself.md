---
title: "Yesterday’s mass-login attack on Basecamp is another reminder to protect yourself"
date: 2019-01-30
url: https://signalvnoise.com/svn3/yesterdays-mass-login-attack-on-basecamp-is-another-reminder-to-protect-yourself/
slug: yesterdays-mass-login-attack-on-basecamp-is-another-reminder-to-protect-yourself
word_count: 538
---


Yesterday at 12:45pm central time, our ops team detected a dramatic spike in login requests to Basecamp. More than 30,000 login attempts were made in the hour that followed from a wide array of IP addresses. Our first line of defense was to block the offending addresses, but ultimately we needed to enable captcha to stop the attack.


After the attack was over, we diagnosed that 124 accounts had unauthorized access from the attack. We immediately reset the password for these accounts, logging out any intruders, and emailed the affected account holders with all the relevant information.


All of the unauthorized access was gained using the correct username and password for the account. It’s highly likely that these credentials were obtained from one of the big breaches, like those collected in combos like [Collection #1](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/), [Anti Public](https://threatpost.com/anti-public-combo-list-analysis-reveals-password-habits-improving/125627/), or [Exploit.in](https://medium.com/4iqdelvedeep/1-4-billion-clear-text-credentials-discovered-in-a-single-database-3131d0a1ae14). All the affected accounts showed as “owned” on [haveibeenpwned.com](https://haveibeenpwned.com).


Our preliminary investigation shows that none of the unauthorized access actually performed any actions within the accounts. It seemed like the attack focused on first validating which accounts were vulnerable, perhaps with a plan to later exploit these vulnerable accounts. Thankfully we were able to detect and stop the attack very quickly, and also ensure that any intruders were prevented further access.


Never the less, this is a serious reminder that you should never share the same password between multiple services. Particularly services such as Basecamp that may contain sensitive information. Here’s what we recommend you do to stay safe:


1.) **Use a password manager** to ensure you’re using different, secure passwords on every service you use. Then if one service is breached, you don’t have to worry about the rest. We use [1Password](https://1password.com/) at Basecamp and recommend it.


2.) **Subscribe to a breach notification service**, like the one offered by [haveibeenpwned.com](https://haveibeenpwned.com). Then you’ll be alerted if your credentials are part of hack known to the public.


3.) **Turn on two-factor authentication (2FA)** wherever you can! We offer [2FA protection for Basecamp using Google Sign-In](https://signalvnoise.com/svn3/protect-your-basecamp-login-with-googles-two-factor-authentication/). Most services that deal with sensitive information offer 2FA these days. It’s especially important that you enable this for critical services, like your email address.


Our ops team will continue to monitor and fight any future attacks. They did an excellent job detecting and addressing this particular attack. But if someone has your username and password, and you don’t have 2FA protection, there are limits to how effective this protection can be.


Protecting yourself against attacks like this is important. Take the time to learn the basics, and take the steps outlined above to limit the risk.


*Update: On January 31st, the mass-attack resumed in much greater strength than before. More than 5,000 IP addresses were used to test stolen credentials. 89 proven correct, but no content was accessed on these accounts, and we followed the same procedure of resetting all logins and writing the people affected. We’ve since beefed up our CAPTCHA protection across all applications and all clients, which has been effective at stopping the attack. CAPTCHA isn’t perfect, and some times it’s annoying, but it has provided effective protection against this wave of attack. We continue to work on shoring up defenses, but do follow the steps outlined above to protect yourself!*

