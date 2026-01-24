---
title: "Speed Hashing"
date: 2012-04-06
url: https://blog.codinghorror.com/speed-hashing/
slug: speed-hashing
word_count: 2038
---

Hashes are a bit like fingerprints for data.


![](https://blog.codinghorror.com/content/images/2025/04/image-601.png)


A given hash uniquely represents a file, or any arbitrary collection of data. At least [in theory](https://blog.codinghorror.com/hashtables-pigeonholes-and-birthdays/). This is a 128-bit MD5 hash you’re looking at above, so it can represent at most 2128 unique items, or 340 trillion trillion *trillion*. In reality the usable space is substantially less; you can start seeing significant collisions once you’ve filled half the [square root of the space](https://web.archive.org/web/20120430113517/http://www.skrenta.com/2007/08/md5_tutorial.html), but the square root of an impossibly large number is still impossibly large.


Back in 2005, I wondered about the difference between a [checksum and a hash](https://blog.codinghorror.com/checksums-and-hashes/). You can think of a checksum as a person’s full name: **Eubediah Q. Horsefeathers**. It’s a shortcut to uniqueness that’s fast and simple, but easy to forge, because security isn’t really the point of naming. You don’t walk up to someone and demand their fingerprints to prove they are who they say they are. Names are just convenient disambiguator, a way of quickly determining who you’re talking to for social reasons, not absolute proof of identity. There can certainly be multiple people in the world with the same name, and it wouldn’t be too much trouble to legally change your name to match someone else’s. But changing your *fingerprint* to match Eubediah’s is another matter entirely; that should be impossible except [in the movies](http://www.imdb.com/title/tt0119094/).


### Secure hashes are designed to be tamper-proof


A properly designed secure hash function **changes its output radically with tiny single bit changes to the input data**, even if those changes are malicious and intended to cheat the hash. Unfortunately, not all hashes were designed properly, and some, like MD5, are outright broken and should [probably be reverted to checksums](http://www.mscs.dal.ca/~selinger/md5collision/).

kg-card-begin: html

> As we will explain below, the algorithm of Wang and Yu can be used to create files of arbitrary length that have identical MD5 hashes, and that differ only in 128 bytes somewhere in the middle of the file. Several people have used this technique to create pairs of interesting files with identical MD5 hashes:
> Magnus Daum and Stefan Lucks have created two PostScript files [with identical MD5 hash](http://web.archive.org/web/20071226014140/http://www.cits.rub.de/MD5Collisions/), of which one is a letter of recommendation, and the other is a security clearance.
> Eduardo Diaz has described a [scheme](https://web.archive.org/web/20120512200731/http://www.codeproject.com/Articles/11643/Exploiting-MD5-collisions-in-C) by which two programs could be packed into two archives with identical MD5 hash. A special “extractor” program turn one archive into a “good” program and the other into an “evil” one.
> In 2007, Marc Stevens, Arjen K. Lenstra, and Benne de Weger used an improved version of Wang and Yu’s attack known as the [chosen prefix collision](http://www.win.tue.nl/hashclash/SoftIntCodeSign/) method to produce two executable files with the same MD5 hash, but different behaviors. Unlike the old method, where the two files could only differ in a few carefully chosen bits, the chosen prefix method allows two completely arbitrary files to have the same MD5 hash, by appending a few thousand bytes at the end of each file.
> Didier Stevens used the evilize program (below) to create two different programs with [the same Authenticode digital signature](http://blog.didierstevens.com/2009/01/17/playing-with-authenticode-and-md5-collisions/). Authenticode is Microsoft’s code signing mechanism, and although it uses SHA1 by default, it still supports MD5.

kg-card-end: html

If you could mimic another person’s fingerprint or DNA at will, you could do some *seriously* evil stuff. MD5 is clearly compromised, and SHA-1 is [not looking too great](https://web.archive.org/web/20120408093705/http://tinsology.net/2010/12/is-sha1-still-viable/) these days.


The good news is that hashing algorithms (assuming you didn’t roll your own, God forbid) were designed by professional mathematicians and cryptographers who knew what they were doing. Just pick a hash of a newer vintage than MD5 (1991) and SHA-1 (1995), and you’ll be fine – at least as far as collisions and uniqueness are concerned. But keep reading.


### Secure hashes are designed to be slow


Speed of a checksum calculation is important, as checksums are generally working on data as it is being transmitted. If the checksum takes too long, it can affect your transfer speeds. If the checksum incurs significant CPU overhead, that means transferring data will also slow down or overload your PC. For example, imagine the sort of checksums that are used on video standards like [DisplayPort](http://en.wikipedia.org/wiki/DisplayPort), which can peak at 17.28 Gbit/sec.


But hashes aren’t designed for speed. In fact, quite the opposite: **hashes, when used for security, need to be slow**. The faster you can calculate the hash, the more viable it is to use brute force to mount attacks. Unfortunately, “slow” in 1990 and 2000 terms may not be enough. The hashing algorithm designers may have anticipated predicted increases in CPU power via Moore’s Law, but they almost certainly did *not* see the radical increases in GPU computing power coming.


How radical? Well, compare the results of CPU powered [hashcat](http://hashcat.net/hashcat/) with the GPU powered oclHashcat when calculating MD5 hashes:


The GPU on a single modern video card produces **over 150 times the number of hash calculations per second** compared to a modern CPU. If Moore’s Law anticipates a [doubling of computing power](https://blog.codinghorror.com/moores-law-in-practical-terms/) every 18 months, that’s like peeking **10 years into the future**. Pretty amazing stuff, isn’t it?


### Hashes and passwords


Let’s talk about passwords, since hashing and passwords are intimately related. Unless [you’re storing passwords incorrectly](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/), you *always* store a user’s password as a salted hash, never as plain text. Right? *Right?* This means if your database containing all those hashes is [compromised or leaked](https://blog.codinghorror.com/the-dirty-truth-about-web-passwords/), the users are still protected – nobody can figure out what their password actually is based on the hash stored in the database. Yes, there are of course [dictionary attacks](https://blog.codinghorror.com/dictionary-attacks-101/) that can be surprisingly effective, but we can’t protect users dead-set on using “monkey1” for their password from themselves. And anyway, the real solution to users choosing crappy passwords is not to make users remember ever more complicated and longer passwords, but to [do away with passwords altogether](https://blog.codinghorror.com/cutting-the-gordian-knot-of-web-identity/).


This has one unfortunate ramification for password hashes: very few of them were designed with such massive and commonly available GPU horsepower in mind. Here are my results on my current PC, which has **two ATI Radeon 7970 cards** generating nearly 16000 M c/s with MD5. I used oclHashcat-lite with the full range of a common US keyboard – that is, including uppercase, lowercase, numbers, and all possible symbols:

kg-card-begin: html


| all 6 character password MD5s | 47 seconds |
| all 7 character password MD5s | 1 hour, 14 minutes |
| all 8 character password MD5s | ~465 days |
| all 9 character password MD5s | *fuggedaboudit* |


kg-card-end: html

The process scales nearly perfectly as you add GPUs, so you can cut the time in half by putting four video cards in one machine. It may sound crazy, but enthusiasts have been doing it since 2008. And you could cut it in half *again* by building another PC with four more video cards, splitting the attack space. (Keep going if you’re either crazy, or working for the NSA.) Now we’re down to a semi-reasonable 117 days to generate all 8 character MD5s. But perhaps this is a worst-case scenario, as a lot of passwords have no special characters. How about if we try the same thing using **just uppercase, lowercase, and numbers**?

kg-card-begin: html


| all 6 character password MD5s | 3 seconds |
| all 7 character password MD5s | 4 minutes |
| all 8 character password MD5s | 4 hours |
| all 9 character password MD5s | 10 days |
| all 10 character password MD5s | ~625 days |
| all 11 character password MD5s | *fuggedaboudit* |


kg-card-end: html

If you’re curious about the worst case scenario, a 12 character all lowercase password is attainable in about 75 days on this PC. Try it yourself; here’s the script I used:

kg-card-begin: html

```

set BIN=oclHashcat-lite64
set OPTS=--gpu-accel 200 --gpu-watchdog 0 --outfile-watch 0 --restore-timer 0 --pw-min 6 --pw-max 6 --custom-charset1 ?l?d?s?u
%BIN% %OPTS% --hash-type 0 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ?1?1?1?1?1?1?1?1?1?1?1?1?1

```

kg-card-end: html

Just modify the `pw-min`, `pw-max` and the `custom-charset` as appropriate. Or, if you’re too lazy to try it yourself, browse through the [existing oclHashcat benchmarks](https://web.archive.org/web/20120429043601/http://thepasswordproject.com/oclhashcat_benchmarking) others have run. This will also give you some idea how computationally expensive various known hashes are on GPUs relative to each other, such as:

kg-card-begin: html


| MD5 | 23070.7 M/s |
| SHA-1 | 7973.8 M/s |
| SHA-256 | 3110.2 M/s |
| SHA-512 | 267.1 M/s |
| NTLM | 44035.3 M/s |
| DES | 185.1 M/s |
| WPA/WPA2 | 348.0 k/s |


kg-card-end: html

### What about rainbow tables?


Rainbow tables are [huge pre-computed lists of hashes](https://blog.codinghorror.com/rainbow-hash-cracking/), trading off table lookups to massive amounts of disk space (and potentially memory) for raw calculation speed. They are now utterly and completely obsolete. Nobody who knows what they’re doing would bother. They’d be wasting their time. I’ll let [Coda Hale explain](http://codahale.com/how-to-safely-store-a-password/):


> Rainbow tables, despite their recent popularity as a subject of blog posts, have not aged gracefully. Implementations of password crackers can leverage the massive amount of parallelism available in GPUs, peaking at billions of candidate passwords a second. You can literally test all lowercase, alphabetic passwords which are ≤7 characters in less than 2 seconds. And you can now rent the hardware which makes this possible to the tune of less than $3/hour. For about $300/hour, you could crack around 500,000,000,000 candidate passwords a second.
> Given this massive shift in the economics of cryptographic attacks, it simply doesn’t make sense for anyone to waste terabytes of disk space in the hope that their victim didn’t use a salt. It’s a lot easier to just crack the passwords. Even a “good” hashing scheme of `SHA256(salt + password)` is still completely vulnerable to these cheap and effective attacks.


### But when I store passwords I use salts so none of this applies to me!


Hey, awesome, you’re smart enough to not just use a hash, but also to [salt the hash](http://www.adayinthelifeof.nl/2011/02/02/password-hashing-and-salting/). Congratulations.

kg-card-begin: html

```

$saltedpassword = sha1(SALT . $password);

```

kg-card-end: html

I know what you’re thinking. “I can hide the salt, so the attacker won’t know it!” You can certainly try. You could put the salt somewhere else, like in a different database, or put it in a configuration file, or in some hypothetically secure hardware that has additional layers of protection. In the event that an attacker obtains your database with the password hashes, but somehow has no access to or knowledge of the salt it’s theoretically possible.


This will provide the illusion of security more than any actual security. Since you need both the salt and the choice of hash algorithm to generate the hash, and to check the hash, it’s unlikely an attacker would have one but not the other. If you’ve been compromised to the point that an attacker has your password database, it’s reasonable to assume they either have or can get your secret, hidden salt.


The first rule of security is to always assume and plan for the worst. Should you use a salt, ideally a random salt for each user? Sure, it’s definitely a good practice, and at the very least it lets you disambiguate two users who have the same password. But these days, **salts alone can no longer save you** from a person willing to spend a few thousand dollars on video card hardware, and if you think they can, you’re in trouble.


### I’m too busy to read all this.


If you are a user:


**Make sure all your passwords are 12 characters or more**, ideally a lot more. [I recommend adopting pass phrases](https://blog.codinghorror.com/passwords-vs-pass-phrases/), which are not only a lot easier to remember than passwords (if not type) but also *ridiculously* secure against brute forcing purely due to their length.


If you are a developer:


**Use **[**bcrypt**](http://en.wikipedia.org/wiki/Bcrypt)** or **[**PBKDF2**](http://en.wikipedia.org/wiki/Pbkdf2)** *exclusively* to hash anything you need to be secure**. These new hashes were specifically designed to be [difficult to implement on GPUs](http://security.stackexchange.com/a/6415). Do *not* use any other form of hash. Almost every other popular hashing scheme is vulnerable to brute forcing by arrays of commodity GPUs, which only get faster and more parallel and easier to program for every year.

[hashing](https://blog.codinghorror.com/tag/hashing/)
[security](https://blog.codinghorror.com/tag/security/)
[cryptography](https://blog.codinghorror.com/tag/cryptography/)
[checksum](https://blog.codinghorror.com/tag/checksum/)
[data integrity](https://blog.codinghorror.com/tag/data-integrity/)
