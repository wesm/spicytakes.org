---
title: "What if it was infinitely fast?"
date: 2005-07-26
url: https://blog.codinghorror.com/what-if-it-was-infinitely-fast/
slug: what-if-it-was-infinitely-fast
word_count: 514
---

When it comes to performance, there’s always a bottleneck. The question is, which bottleneck? That’s why one of the more interesting [back of the envelope calculations](https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/) is to ask, “what if it was infinitely fast?”


One way to make something infinitely fast is to make it a no-op. Instead of doing work, it does nothing. This is also known as “null driver” in hardware circles. It shows how fast your hardware could be given the limits of the underlying operating system infrastructure. Standard 2D graphics operations in Windows have been equal to null driver performance [since about 1999](https://web.archive.org/web/20051124171310/http://www.azillionmonkeys.com/qed/accelerator.html):


> Modern graphics companies concerned about 2D performance take something called a NULL driver – a graphics driver than accepts the low level rendering commands but does no rendering work whatsoever – and see how close they can come to its performance. Companies like Matrox are basically almost at the NULL driver performance in all situations.


This probably says more about Windows overhead than it does about actual 2D performance.


Gary Tarolli was the CTO of [3dfx Interactive](http://en.wikipedia.org/wiki/3Dfx). Their Voodoo series of add-on video cards pioneered real time 3D graphics on the PC. Gary had this to say about infinitely fast 3D hardware in 1998:


> I just want to put in a few cents here. I know Voodoo2 relieves the CPU of triangle setup processing, however, that is all it relieves the CPU of. If a game is taking up 80% of the CPU time, which is not that uncommon, **then even if we replaced our hardware with INFINITELY fast hardware, you only get a small increase in performance** (1.25x). Voodoo2 isn’t infinitely fast, so the results are even smaller. Each game takes up a different amount of the CPU, so you will see different results for different games.


It’s hard to imagine the CTO of a hardware startup actually answering questions about the product he designed in the newsgroups. Only in 1998, I guess.


AnandTech’s review of the first affordable [solid state hard drive](http://www.anandtech.com/storage/showdoc.aspx?i=2480&p=1) offers a tantalizing glimpse of infinitely fast storage devices – and some new bottlenecks we couldn’t see before:

kg-card-begin: html


| Benchmark | Times faster |
| Business Winstone | 1.02x |
| Content Creation Winstone | 1.03x |
| Windows XP Boot Time | 1.5x |
| Battlefield 2 level load time | 1.3x |
| Photoshop CS load time | 1.7x |
| MS Outlook 2003 load time | 1.0x |
| 693mb file copy | 3.8x |


kg-card-end: html

It’s an interesting experiment. Kudos to Gigabyte for making a 4gb solid state hard drive affordable. All you need is $70 for the i-RAM device itself, and 4gb of PC3200 DDR RAM (at current pricing, $90 x 4). Sure, “under $500” isn’t exactly cheap, but relative to other solid state hard drives, it’s an incredible bargain.


Unfortunately, Having an infinitely fast solid state hard drive doesn’t do a whole lot to improve raw performance. It’s probably best used as a device to reveal where all the *other* performance bottlenecks are.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[performance](https://blog.codinghorror.com/tag/performance/)
[null driver](https://blog.codinghorror.com/tag/null-driver/)
[software infrastructure](https://blog.codinghorror.com/tag/software-infrastructure/)
[2d graphics](https://blog.codinghorror.com/tag/2d-graphics/)
