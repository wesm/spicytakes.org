---
title: "URL Shortening: Hashes In Practice"
date: 2007-08-21
url: https://blog.codinghorror.com/url-shortening-hashes-in-practice/
slug: url-shortening-hashes-in-practice
word_count: 1132
---

I’ve become a big fan of Twitter. My philosophy is, [when in doubt, make it public](https://blog.codinghorror.com/when-in-doubt-make-it-public/), and Twitter is essentially public instant messaging. This suits me fine. Well, when Twitter is actually up and running, at least. Its [bouts of frequent downtime](https://blog.codinghorror.com/twitter-service-vs-platform/) are legendary, even today.


(I was going to put a screenshot of one of my favorite Twitter messages here, but as I write this Twitter is down. Again. No, I’m not kidding. OK, it’s back up.)


![](https://blog.codinghorror.com/content/images/2025/03/image-123.png)


One of the design constraints of Twitter is that every message is limited to 140 characters. You quickly learn to embrace and live within those constraints, but if you like to post URLs in your Twitter messages like I do, those 140 characters become very dear. That’s probably why **Twitter automatically converts any URLs over about 30 characters to short URLs using the **[**TinyUrl**](http://tinyurl.com/)** service**.


For instance, let’s say I wanted to make a shortened URL version of [Steve McConnell’s blog](https://web.archive.org/web/20091211212541/http://forums.construx.com/blogs/stevemcc/default.aspx).


`http://forums.construx.com/blogs/stevemcc/default.aspx`


It’s not a particularly long URL, but every character matters when it comes to Twitter. I found a list of common URL shortening services, let’s see how they compare:


```
http://qurl.net/1YU
http://rurl.org/808
http://jtty.com/cuy
http://elfurl.com/li4na
http://shurl.org/pHbnD
http://shrinkster.com/s9y
http://tinyurl.com/yvvtag
http://clipurl.com/?PAP269
http://shorl.com/dihyfradiduba

```


Looks like the best we can do is 3 characters to represent the URL, along with a mandatory 16 characters for the protocol, domain name (everyone [drops the leading “www”](https://blog.codinghorror.com/the-great-dub-dub-dub-debate/)), and slashes. That’s a total of **19 characters**, a nice improvement over the **54 characters** that make up the original URL. But using an URL shortening and redirection service isn’t without pitfalls of its own.

1. What if the URL redirection service goes belly up, as the [once-popular url123.com](https://signalvnoise.com/archives2/tinyurl_vs_url123) did? All your previous hyperlinks are instantly and forever broken. What if the redirection service is only sporadically available? That’s arguably even worse.
2. The URL no longer contains any hints whatsoever as to the content of the URL. It’s completely opaque. The only way to find out what’s behind that hyperlink is to actually click on it. This is not a great user experience for the person doing the clicking.
3. URL redirection services are often used by questionable people for nefarious reasons. Some were shut down because of all the spammers abusing their service.


Despite all the potential problems, URL shortening services are still useful in the right circumstances. For example, sending out very long hyperlinks in email is always risky; you never know when the email clients will insert line breaks in the links and render them unclickable. Not to mention mobile devices, where space is always at a premium.


**I often wonder why Google doesn’t offer an URL redirection service**, as they already keep an index of every URL in the world. The idea of Google disappearing tomorrow, or having availability problems, is far less likely than the seemingly random people and companies who operate these URL redirection services – often for no visible income.


But what really struck me about these services is how they’re **a perfect embodiment of a classical computer science concept – the **[**hash table**](https://en.wikipedia.org/wiki/Hash_table):


> In computer science, a hash table, or a hash map, is a data structure that associates keys with values. The primary operation it supports efficiently is a lookup: given a key (e.g. a person’s name), find the corresponding value (e.g. that person’s telephone number). It works by transforming the key using a hash function into a hash, a number that is used to index into an array to locate the desired location (“bucket”) where the values should be.


It doesn’t get more fundamental than the keys and values of our beloved hash tables. But some of the services use an absurdly small number of characters as keys – **1YU, 808, cuy** – to *represent the entire Steve McConnell blog URL*. Thinking about how they did that leads you to some interesting solutions. For instance, let’s compare the result of [applying traditional hash functions](https://www.fileformat.info/tool/hash.htm?text=http%3A%2F%2Fforums.construx.com%2Fblogs%2Fstevemcc%2Fdefault.aspx) to Steve’s blog URL:

kg-card-begin: html


| Adler32 | 399014e3 |
| CRC32 | 78aa9d1a |
| MD2 | 286c50c2db4fcad77adb4edeb3a937b2 |
| MD4 | 387ac3f6aae7956c4fab176271bb4518 |
| MD5 | f061a171dfc30635462850684f98b886 |
| SHA-1 | 3c93b6d332091b2970fb660d644d0ba3d756e322 |


kg-card-end: html

Even the shortest hash function, the 32-bit CRC, is a bit too long for this usage. That’s 4 bytes which will be at least five ASCII characters. To get a shorter URL, you’d have to switch to a 16-bit CRC. If you’re clever about how you turn those [16 bits into printable characters](https://blog.codinghorror.com/equipping-our-ascii-armor/), you just might be able to fit those 2 bytes into three ASCII characters.


But is a 16 bit hash enough to represent *every URL in the universe*? Rich Skrenta [helps us out with a little hash math](https://web.archive.org/web/20081104062949/http://www.skrenta.com/2007/08/md5_tutorial.html):

kg-card-begin: html

> Suppose you’re using something like [MD5](http://en.wikipedia.org/wiki/MD5) (the GOD of HASH). MD5 takes any length string of input bytes and outputs 128 bits. The bits are consistently random, based on the input string. If you send the same string in twice, you’ll get the exact same random 16 bytes coming out. But if you make even a tiny change to the input string – even a single bit change – you’ll get a completely different output hash.
> So when do you need to worry about collisions? The working rule-of-thumb here comes from the [birthday paradox](http://en.wikipedia.org/wiki/Birthday_paradox). Basically **you can expect to see the first collision after hashing 2n/2 items, or 2^64 for MD5**.
> 2^64 is a big number. If there are 100 billion urls on the web, and we MD5’d them all, would we see a collision? Well no, since 100,000,000,000 is way less than 2^64:
> 26418,446,744,073,709,551,616
> 237100,000,000,000

kg-card-end: html

For a 16-bit hash, our 2n/2 is a whopping 256; for a 32-bit hash it’d be 65,536. It’s pretty clear that **URL shortening services can’t rely on traditional hashing techniques**, at least not if they want to produce competitively small URLs.

kg-card-begin: html

My guess is the aggressive URL shortening services are doing a simple iteration across every permutation of the available characters they have as the URLs come in. Each new URL gets a unique three character combination until no more are left. How many URLs would that take? Let's say each character is simple alphanumeric, case sensitive A-Z, a-z, 0-9. You can do somewhat better because more ASCII characters than that are valid in URLs, but let's stick with this for the sake of argument. That's 26 + 26 + 10 or 62 possibilities per character. So with a three character URL, we can represent...

kg-card-end: html
62 **×** 62 **×** 62 = 238,328... about 250,000 unique three-character short URLs. Beyond that, they’d be forced to move to four character representations. Assuming, of course, that the old URLs never expire.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[social media](https://blog.codinghorror.com/tag/social-media/)
