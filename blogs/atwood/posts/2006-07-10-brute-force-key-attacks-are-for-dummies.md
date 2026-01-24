---
title: "Brute Force Key Attacks Are for Dummies"
date: 2006-07-10
url: https://blog.codinghorror.com/brute-force-key-attacks-are-for-dummies/
slug: brute-force-key-attacks-are-for-dummies
word_count: 742
---

Cory Doctorow recently linked to this [fascinating email](https://web.archive.org/web/20080709090010/http://www.interesting-people.org/archives/interesting-people/200607/msg00058.html) from Jon Callas, the [CTO of PGP corporation](https://web.archive.org/web/20060615085301/http://www.pgp.com/library/ctocorner/index.html). In it, Jon describes **the impossibility of brute force attacks on modern cryptography**:


> Modern cryptographic systems are essentially unbreakable, particularly if an adversary is restricted to intercepts. We have argued for, designed, and built systems with 128 bits of security precisely because they are essentially unbreakable. It is very easy to underestimate the power of exponentials. 2^128 is a very big number. Burt Kaliski first came up with this characterization, and if he had a nickel for every time I tell it, he could buy a latte or three.
> Imagine a computer that is the size of a grain of sand that can test keys against some encrypted data. Also imagine that it can test a key in the amount of time it takes light to cross it. **Then consider a cluster of these computers, so many that if you covered the earth with them, they would cover the whole planet to the height of 1 meter. The cluster of computers would crack a 128-bit key on average in 1,000 years.**
> If you want to brute-force a key, it literally takes a planet-full of computers. And of course, there are always 256-bit keys, if you worry about the possibility that government has a spare planet that they want to devote to key-cracking.


Each additional bit doubles the number of keys you have to test in a brute force attack, so by the time you get to 128 or 256 bits, you have a staggeringly large number of potential keys to test. The classic illustration of this [exponential growth](http://en.wikipedia.org/wiki/Exponential_growth#Rice_on_a_chessboard) is the fable of the mathematician, the king, and the chess board:


> There is an old Persian legend about a clever courtier who presented a beautiful chessboard to his king and requested that the king give him in return 1 grain of rice for the first square on the board, 2 grains of rice for the second square, 4 grains for the third, and so forth. The king readily agreed and ordered rice to be brought from his stores. By the fortieth square a million million rice grains had to be brought from the storerooms. The king’s entire rice supply was exhausted long before he reached the sixty-fourth square. Exponential increase is deceptive because it generates immense numbers very quickly.


By the time you get to that 32nd chessboard square, you’re facing a very large number indeed.


![](https://blog.codinghorror.com/content/images/2025/05/image-331.png)


However, 2^32 isn’t necessarily a very large set of keys when you’re performing a brute force attack with a **worldwide distributed network of computers**. Such as the [RC5 distributed computing project](http://www.distributed.net/rc5/). Here’s what they’ve done so far:

- a **56-bit** key was [cracked in 250 days](http://stats.distributed.net/projects.php?project_id=3).
- a **64-bit** key was [cracked in 1,757 days](http://stats.distributed.net/projects.php?project_id=5).
- a **72-bit** key is still being cracked; 1,316 days so far with 379,906 days remaining.


The earliest 56-bit challenge, which ended in 1997, tested keys at a rate of 1.6 million per second. The ongoing 72-bit challenge is currently testing keys at the rate of 139.2 million per second. We’re testing keys 88 times faster than we were 10 years ago, through natural increases in computing power and additional computers added to the distributed computing network.


And yet the RC5-72 project **still has 1,040 years to go before they test the entire key space**. Remember, that’s for a lousy 72-bit key! If we want to double the amount of time the brute force attack will take, all we need to do is tack on one teeny, tiny little bit to our key. 73-bit key? 2,080 years. 74-bit key? 4,160 years.


It’s painfully clear that a brute force attack on even a 128 bit key is a fool’s errand. Even if you’re using a planet covered with computers that crack keys at the speed of light.


If you’re a smart attacker, **you already know that brute force key attacks are strictly for dummies** with no grasp of math or time. There are so many other vulnerabilities that are much, much easier to attack:

- Rootkits
- Social engineering
- Keyloggers
- Obtain the private key file and attack the password on it


Of course, beyond ruling out brute force attacks, I’m barely scratching the surface here. Jon Callas’ Black Hat conference presentation [Hacking PGP](http://www.blackhat.com/presentations/bh-europe-05/bh-eu-05-callas-up.pdf) (pdf) goes into much more detail, if you’re interested.

[security](https://blog.codinghorror.com/tag/security/)
[cryptography](https://blog.codinghorror.com/tag/cryptography/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[brute force attacks](https://blog.codinghorror.com/tag/brute-force-attacks/)
[modern cryptography](https://blog.codinghorror.com/tag/modern-cryptography/)
