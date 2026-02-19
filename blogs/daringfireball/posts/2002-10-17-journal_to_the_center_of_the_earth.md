---
title: "Journal to the Center of the Earth"
date: 2002-10-17
url: https://daringfireball.net/2002/10/journal_to_the_center_of_the_earth
slug: journal_to_the_center_of_the_earth
word_count: 205
---


Earlier, when I [doubted](http://daringfireball.net/2002/10/stepping_on_eweeks_blue_suede_shoes.html) the veracity of eWeek’s apparent scoop on a secret new journaling file system set to appear in Mac OS X 10.2.2, I wrote:


> To change a disk from one file system to another, you need to reformat it. What eWeek is claiming simply isn’t possible. 
> A journaling file system doesn’t simply write a single “journal” file containing all the journaling information. The whole point of a journaling file system is that the journaling data is a fundamental part of the format itself.


Thoughtful readers Chris Cogdon and [Jeff Williams](http://pinchy.org/) both emailed me to point out that Linux’s ext3 journaling file system proves me wrong about both of the above points. (1) It is backwards and forwards compatible with the non-journaling ext2 format, so you don’t need to reformat an ext2 disk to switch to ext3. (2) It can be configured to write the journal to a single file, hidden away in /root.


Details can be found at [Red Hat](http://www.redhat.com/support/wpapers/redhat/ext3/#easy).


So I take back the bit about it being “impossible”, but I stand by the rest of my argument. I don’t think this is going to appear in 10.2.2.



| **Previous:** | [Listen](https://daringfireball.net/2002/10/listen) |
| **Next:** | [Exposed](https://daringfireball.net/2002/10/exposed) |


PreviousNext