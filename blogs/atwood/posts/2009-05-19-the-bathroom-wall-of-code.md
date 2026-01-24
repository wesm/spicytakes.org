---
title: "The Bathroom Wall of Code"
date: 2009-05-19
url: https://blog.codinghorror.com/the-bathroom-wall-of-code/
slug: the-bathroom-wall-of-code
word_count: 608
---

In [Why Isn’t My Encryption... Encrypting?](https://blog.codinghorror.com/why-isnt-my-encryption-encrypting/), many were up in arms about the flawed function I posted. And rightfully so, as there was a huge mistake in that code that just about invalidates any so-called “encryption” it performs. But there’s one small problem: **I didn’t write that function**.


Now, I am certainly *responsible* for that function, in the sense that it magically appeared in our codebase one day – and the the entire project is the sum of all the code contributed by every programmer working on it. I invoke the [First Rule of Programming: It’s Always Your Fault](https://blog.codinghorror.com/the-first-rule-of-programming-its-always-your-fault/). And by “your,” I don’t mean the particular programmer who contributed this code, who shall remain blissfully nameless. I mean us – the entire team. The onus is on us, as a team, to vet every line of code at the time it is contributed, and constantly [peer review each other’s code](https://blog.codinghorror.com/whos-your-coding-buddy/). It’s a responsibility we shoulder together. Nobody owns the code, because [everybody owns the code](https://blog.codinghorror.com/you-gotta-own-it/).


Yes, I failed. Because the *team* failed.


Geoff Weinhold left this prophetic comment on the post:


> The irony in this is that someone will inevitably end up here for sample encryption code and blindly copy/paste your flawed code.


Indeed. Heaven forbid someone copy and paste flawed code *from the internet* into their project! In fact, a quick search on some of the unique strings in that original `Encrypt()` function turns up a few... interesting... search results.

kg-card-begin: html


| 01/2006 | [C# Shiznit - Library Encrypt and Decrypt Methods using TripleDES and MD5](https://web.archive.org/web/20090831081010/http://www.csharper.net/blog/library_encrypt_and_decrypt_methods_using_tripledes_and_md5.aspx) |
| 05/2006 | [Code Project - Encrypt and Decrypt Data with C#](https://web.archive.org/web/20100324022718/http://www.codeproject.com/KB/web-security/Cryptography_MD5_TriDES.aspx?display=Print) |
| 04/2007 | [Bytes - String Encryption Help](https://web.archive.org/web/20090521132011/http://bytes.com/groups/net-c/636048-string-encryption-help) |
| 06/2008 | [Egghead Cafe - invalid length while decrypting TripleDESCryptoServiceProvider](https://web.archive.org/web/20110622061337/http://www.eggheadcafe.com/community/aspnet/7/10039718/invalid-length-while-decrypting-tripledescryptoserviceprovider.aspx) |
| 09/2008 | [ASP.NET Forums - Need help on password-encrypted key used for signing](https://web.archive.org/web/20090522105345/http://forums.asp.net/t/1313494.aspx) |
| 11/2008 | [code:keep Encryption](https://web.archive.org/web/20091207013816/http://www.codekeep.net/snippets/af1cd375-059a-4175-93d7-25eea2c5c660.aspx) |
| 12/2008 | [Encrypt/Decrypt the password in C# .net](http://www.dotnetspider.com/forum/185122-Encrypt-Decrypt-password-C-net.aspx) |
| 05/2009 | [My Own Stupid Blog Post](https://blog.codinghorror.com/why-isnt-my-encryption-encrypting/) |


kg-card-end: html

That’s just a sampling of the 131 web hits I got. To [paraphrase Austin Powers](http://www.imdb.com/title/tt0118655/quotes#qt0367867)** this `Encrypt()` function is like the village bicycle: everybody’s had a ride.** It’s a shame this *particular* bicycle happens to have a crippling lack of brakes that makes it dangerous to ride, but what can you do.


Scott Hanselman [coined](http://www.hanselman.com/blog/GoogleCodeSearchNowYouCanSearchTheBathroomWallOfCode.aspx) a nice phrase for this: **the internet as the bathroom wall of code**.


![](https://blog.codinghorror.com/content/images/2025/04/image-366.png)


It’s true. People, being people, have gone and scrawled a bunch of random code graffiti all over the damn internet. Some of it is vanity tagging. Some of it is borderline vandalism. And some of it is art. How do we tell the difference?


That’s the very reason I put forth a [modest proposal for the copy and paste school of code reuse](https://blog.codinghorror.com/a-modest-proposal-for-the-copy-and-paste-school-of-code-reuse/). Not that it would have helped in this case, but it sure would be nice if someone could **perform a grep replace**...

kg-card-begin: html

```

s/Mode = CipherMode.ECB/Mode = CipherMode.CBC/g

```

kg-card-end: html

... on, like, *the entire internet*. So other projects don’t absorb this critically flawed code sample.


In the meantime, until that tool is developed, I recommend that you **apply extra-strength peer review to any code snippets you absorb into your project from the bathroom wall of code**. That internet code snippet you’re looking at, the one that appears to be *just what you’re looking for*, could also be random graffiti scrawled on a bathroom wall.


It’s true that some bathrooms are nicer than others. But as we’ve learned, it pays to be especially careful when cribbing code from the internet.

[security](https://blog.codinghorror.com/tag/security/)
[code review](https://blog.codinghorror.com/tag/code-review/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
