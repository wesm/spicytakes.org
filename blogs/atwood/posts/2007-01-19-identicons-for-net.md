---
title: "Identicons for .NET"
date: 2007-01-19
url: https://blog.codinghorror.com/identicons-for-net/
slug: identicons-for-net
word_count: 265
---

Don Park invented Identicons last week.


![](https://blog.codinghorror.com/content/images/2025/03/image-290.png)


An Identicon is **a small, anonymized visual glyph that represents your IP address**. [Don explains it](https://web.archive.org/web/20070125011239/http://www.docuverse.com/blog/donpark/2007/01/19/identicon-explained) better than I do:


> I originally came up with this idea to be used as an easy means of visually distinguishing multiple units of information, anything that can be reduced to bits. It’s not just IPs but also people, places, and things.
> IMHO, too much of the web what we read are textual or numeric information which are not easy to distinguish at a glance when they are jumbled up together. So I think adding visual identifiers will make the user experience much more enjoyable.
> I think Identicons have many use cases. One use is embedding them in wiki pages to identify authors. Another is using them in CRM to identify customers. I can go on and on. It’s not just about IP addresses but information that tends to move in ’herds.’


It’s genius. And the simple algorithm Don came up with produces beautiful, unique results. Just scroll through [the comments on his blog](http://web.archive.org/web/20070206213620/http://www.docuverse.com/blog/donpark/2007/01/18/visual-security-9-block-ip-identification) to see Identicons in action. They work amazingly well, even at 16x16. [Jon Galloway](http://weblogs.asp.net/jgalloway/) and I were inspired. We rolled up our sleeves and ported [Don’s Identicon code](https://web.archive.org/web/20070125011202/http://www.docuverse.com/blog/donpark/2007/01/19/identicon-updated-and-source-released) from Java to .NET 2.0.


![](https://blog.codinghorror.com/content/images/icon/pinned-octocat-093da3e6fa40.svg)


Identicons aren’t just for show. They're quite practical. **Rather than printing everyone’s IP address next to their comment, you can show their anonymized Identicon.** It’s more private, it’s almost as useful, and it’s much more fun. Download the sample and try it yourself.

[identicons](https://blog.codinghorror.com/tag/identicons/)
[.net](https://blog.codinghorror.com/tag/net/)
[ip address](https://blog.codinghorror.com/tag/ip-address/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[visual identifier](https://blog.codinghorror.com/tag/visual-identifier/)
