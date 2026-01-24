---
title: "Spam via SMTP Non-Delivery Reports"
date: 2006-05-07
url: https://blog.codinghorror.com/spam-via-smtp-non-delivery-reports/
slug: spam-via-smtp-non-delivery-reports
word_count: 445
---

I have modest email needs, so I use the default SMTP and POP3 services in Windows Server 2003. Although I have email relay disabled, **spammers are still managing to send spam through my SMTP service** – via non-delivery reports!


In other words, spammers are *intentionally sending email messages to nonexistent email addresses on my domain*. Here’s a representative [sniffer trace](https://blog.codinghorror.com/sniff-this/) from earlier today:

kg-card-begin: html

MAIL FROM:**<[[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)>**
250 2.1.0 OK
RCPT TO:**<[[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)>**
250 2.1.5 OK
354 Start mail input
DATA
(spam email body elided)
250 2.6.0  Queued mail for delivery

MAIL FROM:**<[[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)>**
250 2.1.0 OK
RCPT TO:**<[[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)>**
250 2.1.5 OK
DATA
(spam email body elided)
250 2.6.0  Queued mail for delivery


kg-card-end: html
This repeats dozens of times, with different from and to email address. **The person in the “from” address will get a non-delivery report from my server that includes the original spam message as an attachment**.This is also known as a “Reverse NDR attack,” because the non-delivery report goes to the recipient (e.g., the victim) instead of the sender.I’ve pored over the SMTP settings in Windows Server 2003 and I can’t figure out a way to fix this. I did find this cool [STMP tar pit feature](https://web.archive.org/web/20060510205657/http://support.microsoft.com/kb/842851/) which sounds appropriate – but unfortunately, will have no effect in my case. As you can see from the above sniffer trace, the basic SMTP service is not smart enough to perform “recipient filtering” – to reject email for users that don’t exist at the time of submission. The validation of the address occurs *after* the email delivery process begins, which is too late.I thought about suppressing non-delivery reports entirely, but this breaks the email protocol:*Some of you might think it would be better to simply turn off recipient filtering, rely on your 3rd party antispam product, and suppress NDRs (as spammers typically use spoofed domains anyway). This is possible but unfortunately doing so breaks *[*RFC 2821*](http://www.faqs.org/rfcs/rfc2821.html)*, which states that a NDR must be returned if an e-mail message for an invalid recipient is accepted. In addition it also means normal users that perhaps make a typo in an e-mail address will never receive an NDR informing them of the issue.*What I really need is some way to **make the default SMTP service in Windows Server 2003 reject emails for invalid recipients prior to accepting the message**. That, along with the built-in tarpit support, should break spammers.I hate to buy a commercial mail server to replace the simple STMP and POP3 services provided with Windows Server 2003. But unless I can stem the tide of SMTP non-delivery report spam, I guess I’ll have to.

[email security](https://blog.codinghorror.com/tag/email-security/)
[smtp](https://blog.codinghorror.com/tag/smtp/)
[spam filtering](https://blog.codinghorror.com/tag/spam-filtering/)
[windows server](https://blog.codinghorror.com/tag/windows-server/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
