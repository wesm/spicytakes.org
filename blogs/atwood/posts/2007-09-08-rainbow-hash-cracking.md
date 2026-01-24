---
title: "Rainbow Hash Cracking"
date: 2007-09-08
url: https://blog.codinghorror.com/rainbow-hash-cracking/
slug: rainbow-hash-cracking
word_count: 1345
---

The multi-platform password cracker [Ophcrack](http://ophcrack.sourceforge.net/) is incredibly fast. How fast? **It can crack the password “Fgpyyih804423” in 160 seconds**. Most people would consider that password fairly secure. The [Microsoft password strength checker](https://web.archive.org/web/20070923070117/https://www.microsoft.com/protect/yourself/password/checker.mspx) rates it “strong.” The [Geekwisdom password strength meter](https://web.archive.org/web/20071011005335/http://www.geekwisdom.com/dyn/passwdmeter) rates it “mediocre.”


Why is Ophcrack so fast? Because it uses [Rainbow Tables](http://en.wikipedia.org/wiki/Rainbow_table). No, not the kind of rainbows I have as my desktop background.


![](https://blog.codinghorror.com/content/images/2025/05/image-524.png)


Although those are beautiful, too.


To understand how rainbow tables work, you first have to understand how passwords are stored on computers, whether on your own desktop, or on a remote web server somewhere.


**Passwords are *never* stored in plaintext.** At least they shouldn’t be, unless you’re building the world’s most insecure system using the world’s most naïve programmers. Instead, passwords are stored as the [output of a hash function](https://blog.codinghorror.com/checksums-and-hashes/). Hashes are one-way operations. Even if an attacker gained access to the hashed version of your password, it’s not possible to reconstitute the password from the hash value alone.


But it is possible to attack the hashed value of your password using **rainbow tables: enormous, pre-computed hash values for every possible combination of characters**. An attacking PC could certainly calculate all these hashes on the fly, but taking advantage of a massive table of pre-computed hash values enables the attack to proceed several orders of magnitude faster – assuming the attacking machine has enough RAM to store the entire table (or at least most of it) in memory. It’s a classic [time-memory tradeoff](https://web.archive.org/web/20071002233805/http://lasecwww.epfl.ch/~oechslin/projects/ophcrack/), exactly the sort of cheating shortcut you’d expect a black hat attacker to take.


How enormous are rainbow tables? The installation dialog for Ophcrack should give you an idea:


![](https://blog.codinghorror.com/content/images/2025/05/image-525.png)


It takes a long time to generate these massive rainbow tables, but once they’re out there, every attacking computer can leverage those tables to make their attacks on hashed passwords that much more potent.


The smallest rainbow table available is the basic alphanumeric one, and even it is 388 megabytes. That’s the default table you get with the Ophcrack bootable ISO. Even that small-ish table is remarkably effective. I used it to attack some passwords I set up in a Windows XP virtual machine with the following results:

kg-card-begin: html


|  | found? | seconds |
| Password1! |  | 700 |
| Fgpyyih804423 | **yes** | 159 |
| Fgpyyih80442% |  | 700 |
| saMejus9 | **yes** | 140 |
| thequickbrownfoxjumpsoverthelazydog |  | 700 |


kg-card-end: html

You wouldn’t expect this rainbow table to work on the passwords with non-alphanumeric characters (%&^$# and the like) because the table doesn’t contain those characters. You’ll also note that that [passphrases](https://blog.codinghorror.com/passphrase-evangelism/), which I am a big fan of, are immune to this technique due to their length. But then again, **this attack covered 99.9% of all possible 14 character alphanumeric passwords in 11 minutes**, and that was with the *smallest* of the available rainbow tables. We could do better by using larger, more complete rainbow tables. The Ophcrack documentation describes the differences between the available rainbow tables it uses:

kg-card-begin: html


| Alphanumeric 10k | 388 MB | Contains the LanManager hashes of 99.9% of all alphanumerical passwords. These are passwords made of mixed case letters and numbers (about 80 billion hashes). Because the LanManager hash cuts passwords into two pieces of 7 characters, passwords of length 1 to 14 can be cracked with this table set. Since the LanManager hash is also not case sensitive, the 80 billion hashes in this table set corresponds to 12 septillion (or 283) passwords. |
| Alphanumeric 5k | 720 MB | Contains the LanManager hashes of 99.9% of all alphanumerical passwords. However, because the tables are twice as large, cracking is about four times faster if you have at least 1 GB of RAM. |
| Extended | 7.5 GB | Contains the LanManager hashes of 96% of all passwords made of up to 14 mixed case letters, numbers and the following 33 special characters: !"#$%&'()*+,-./:;<=>?@[]^_`{|} ~. There are about 7 trillion hashes in this table set covering 5 octillion (or 292) passwords. |
| NT | 8.5 GB | You can use this table set to crack the NT hashes on machines where the LanManager hash has been disabled. The set contains 99.0% of the hashes of the passwords made of the following characters:
        
up to 6 mixed case letters, numbers and 33 special characters (same as above)
7 mixed-case letters and numbers
8 lower-case letters and numbers

There are 7 trillion hashes in this table, corresponding to 7 trillion passwords (the NT hash does not suffer from the weaknesses of the LanManager hash). |


kg-card-end: html

Note that all rainbow tables have specific lengths and character sets they work in. Passwords that are too long, or contain a character not in the table’s character set, are completely immune to attack from that rainbow table.


**Unfortunately, Windows servers are particularly vulnerable to rainbow table attack**, due to unforgivably weak [legacy Lan Manager hashes](http://en.wikipedia.org/wiki/LM_hash). I’m stunned that the legacy Lan Manager support “feature” is still enabled by default in Windows Server 2003. It’s *highly* advisable that you [disable Lan Manager hashes](http://support.microsoft.com/kb/299656), particularly on Windows servers which happen to store domain credentials for every single user. It’d be an awful shame to inconvenience all your Windows 98 users, but I think the increase in security is worth it.


I read that Windows Server 2008 will [finally kill off LM hashes](https://web.archive.org/web/20071102234219/http://www.microsoft.com/technet/technetmag/issues/2006/08/SecurityWatch/) when it’s released next year. Windows Vista already removed support for these obsolete hashes on the desktop. Running OphCrack on my Vista box results in this dialog:


> All LM hashes are empty. Please use NT hash tables to crack the remaining hashes.


I’d love to, but I can’t find a reliable source for the 8.5 GB rainbow table of NT hashes that I need to proceed.


The Ophcrack tool isn’t very flexible. It doesn’t allow you to generate your own rainbow tables. For that, you’ll need to use the [Project Rainbow Crack](https://web.archive.org/web/20061105080552/http://www.antsight.com/zsl/rainbowcrack/) tools, which can be used to attack almost any character set and any hashing algorithm. But beware. **There’s a reason rainbow table attacks have only emerged recently, as the price of 2 to 4 gigabytes of memory in a desktop machine have approached realistic levels**. When I said *massive*, I meant it. Here are some generated rainbow table sizes for the more secure NT hash:

kg-card-begin: html


| Character Set | Length | Table Size |
| `ABCDEFGHIJKLMNOPQRSTUVWXYZ` | 14 | 0.6 GB |
| `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789` | 14 | 3 GB |
| `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=` | 14 | 24 GB |
| `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|:;"'<>,.?/` | 14 | 64 GB |


kg-card-end: html

A rainbow table attack is usually overkill for a desktop machine. If hackers have physical access to the machine, security is irrelevant. That’s rule number 3 in the [10 Immutable Laws of Computer Security](https://web.archive.org/web/20071011002225/http://www.microsoft.com/technet/archive/community/columns/security/essays/10imlaws.mspx?mfr=true). There are any number of tools that can reset passwords given physical access to the machine.


But **when a remote hacker obtains a large list of hashed passwords from a server or database**, we’re in trouble. There’s significant risk from a rainbow table attack. That’s why you should never rely on hashes alone – always add [some salt to your hash](https://web.archive.org/web/20071011075356/http://aspnet.4guysfromrolla.com/articles/112002-1.aspx) so the resulting hash values are unique. Salting a hash sounds complicated (and vaguely delicious), but it’s quite simple. You prefix a unique value to the password before hashing it:

kg-card-begin: html

```
hash = md5(‘deliciously-salty-’ + password)
```

kg-card-end: html

If you’ve salted your password hashes, an attacker can’t use a rainbow table attack against you – the hash results from “password” and “deliciously-salty-password” won’t match. Unless your hacker somehow knows that all your hashes are “deliciously-salty-” ones. Even then, he or she would have to generate a custom rainbow table specifically for you.

kg-card-begin: html

UPDATE: Please read Thomas Ptacek’s excellent and [informative response to this post](https://web.archive.org/web/20090924015929/http://chargen.matasano.com/chargen/2007/9/7/enough-with-the-rainbow-tables-what-you-need-to-know-about-s.html). It goes into much more detal about the nuts and bolts of password hashing. Unlike me, Thomas is a real security expert.

kg-card-end: html
[security](https://blog.codinghorror.com/tag/security/)
[password cracking](https://blog.codinghorror.com/tag/password-cracking/)
[hash function](https://blog.codinghorror.com/tag/hash-function/)
[rainbow tables](https://blog.codinghorror.com/tag/rainbow-tables/)
[cryptography](https://blog.codinghorror.com/tag/cryptography/)
