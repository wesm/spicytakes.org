---
title: "How to fit three bugs in 512 bytes of security code"
date: 2005-08-08
url: https://blog.codinghorror.com/how-to-fit-three-bugs-in-512-bytes-of-security-code/
slug: how-to-fit-three-bugs-in-512-bytes-of-security-code
word_count: 537
---

In the spirit of [iPod modem hacking](https://blog.codinghorror.com/ipod-hacking-via-modem/), Michael Steil documents how [hackers compromised the Xbox security](https://web.archive.org/web/20050810020112/http://www.xbox-linux.org/wiki/The_Hidden_Boot_Code_of_the_Xbox) system. Mostly thanks to 512 bytes of rather buggy security code embedded in the Xbox boot ROM:


> *The Xbox is an IBM PC, i.e. it has an x86 CPU. When the machine is turned on, it starts execution 16 bytes from the top of its address space, at the address FFFF_FFF0 (F000:FFF0). On an IBM PC, the upper 64 KB (or more) of the address space are occupied by the BIOS ROM, so the CPU starts execution in this ROM. The Xbox, having an external (reprogrammable) 1 MB Flash ROM chip (models since 2003 have only 256 KB), would normally start running code there as well, since this megabyte is also mapped into the uppermost area of the address space. But this would make it too easy for someone who wants to either replace the ROM image with a self-written one or patch it to break the chain of trust (“modchips”). If the ROM image could be fully accessed, it would be easy to reverse-engineer the code; encryption and obfuscation would only slow down the hacking process a bit.
> A common idea to make the code inaccessible is not to put it into an external chip, but integrate it into one of the other chips. Then there is no standard way to extract the data, and none to replace the chip with one with different contents. But this way, it is a lot more expensive, both the design of a chip that includes both ROM and additional logic, and updating the ROM in a new version of the Xbox if there is a flaw in the ROM.
> A good compromise is to store only a small amount of code in one of the other chips, and store the bulk of it in the external Flash chip. This small ROM can not be extracted easily, and it cannot be changed or replaced. The code in there just has to make sure that an attacker can neither understand nor successfully patch the bulk of the code he has access to, which is stored in Flash ROM.
> Microsoft decided to go this way, and they stored 512 bytes of code in the Xbox’ Southbridge, the MCPX (Media and Communications Processor for Xbox), which is manufactured by nVidia. This code is supposed to be mapped into the uppermost 512 bytes of the address space, so that the CPU starts execution there. It includes a decryption function with a secret key that deciphers (parts of the) “unsafe” code in the Flash ROM into RAM and runs it. Without knowing the key, it is practically impossible to understand or even patch the encrypted code in Flash ROM.*


I know [virtually nothing about cryptography](https://blog.codinghorror.com/encryption-for-dummies/), and I could have told you that checking a single 32-bit value is a remarkably poor substitute for a real hash.


I’m thinking Microsoft won’t be making these kinds of newbie security mistakes with the Xbox 360. Current [rumor suggests](https://web.archive.org/web/20050810014101/http://www.forbes.com/markets/2005/08/05/microsoft-xbox-launch-0805markets05.html) we won’t have to wait long to find out – the 360 will supposedly go on sale on or near black Friday.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[security](https://blog.codinghorror.com/tag/security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
