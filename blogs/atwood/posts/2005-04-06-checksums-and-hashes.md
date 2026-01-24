---
title: "Checksums and Hashes"
date: 2005-04-06
url: https://blog.codinghorror.com/checksums-and-hashes/
slug: checksums-and-hashes
word_count: 379
---

I learned to appreciate the value of the [Cyclic Redundancy Check](http://en.wikipedia.org/wiki/Cyclic_redundancy_check) (CRC) algorithm in my 8-bit, 300 baud file transferring days. If the CRC of the local file matched the CRC stored in the file (or on the server), I had a valid download. I also learned a little bit about the [pigeonhole principle](http://www.cut-the-knot.org/do_you_know/pigeon.shtml) when I downloaded a file with a matching CRC that was corrupt! An 8-bit CRC only has 256 possible values, after all.


[Checksums](http://en.wikipedia.org/wiki/Checksum) are somewhat analogous to filesystem “fingerprints”– no two should ever be alike, and any modification to the file should change the checksum. But checksums are unsuitable for any kind of security work:


> *CRCs cannot be safely relied upon to verify data integrity (that no changes whatsoever have occurred), since it’s extremely easy to **intentionally** change data without modifying its CRC.*


That’s probably because CRC is a simple algorithm designed for speed – not security. As I discovered, a checksum is really just a specific kind of **hash**. Steve Friedl’s, [Illustrated Guide to Cryptographic Hashes](http://www.unixwiz.net/techtips/iguide-crypto-hashes.html) is an excellent, highly visual introduction to the more general theory behind hashing. The .NET framework provides a few essential security-oriented hashing algorithms in the `System.Security.Cryptography` namespace:

- MACTripleDes
- MD5
- SHA1
- SHA256
- SHA384
- SHA512


As far as I can tell, there are only three hash algorithms represented here: [Des](http://en.wikipedia.org/wiki/DES), [MD5](http://en.wikipedia.org/wiki/Md5), and [SHA](http://en.wikipedia.org/wiki/SHA). SHA is available in a couple different sizes, and **bigger is better**: every extra bit doubles the number of possible keys and thus reduces the pigeonhole effect. It also doubles the number of brute force attempts one would theoretically need to make in an attack.


However, if **all you need to do is tell two things apart**, you don’t need fancy security hashes. Just use the humble `GetHashCode` method:

kg-card-begin: html

```
Dim s As String = "Hash browns"
Console.WriteLine(s.GetHashCode)
```

kg-card-end: html

I’m not clear exactly which algorithm was used to generate this hash, but I’m sure it’s at least as good as [my CRC32 class](https://blog.codinghorror.com/squishysyntaxhighlighter-and-crc32/).


I hear more hashing algorithms will be introduced with .NET 2.0. I’d like to see CRC32 in there at the very least. For an interactive demonstration of the 13 most popular hash algorithms, I recommend SlavaSoft’s [HashCalc](https://web.archive.org/web/20050530081312/http://www.slavasoft.com/hashcalc/).

[checksums](https://blog.codinghorror.com/tag/checksums/)
[crc](https://blog.codinghorror.com/tag/crc/)
[hashes](https://blog.codinghorror.com/tag/hashes/)
[data integrity](https://blog.codinghorror.com/tag/data-integrity/)
[security](https://blog.codinghorror.com/tag/security/)
