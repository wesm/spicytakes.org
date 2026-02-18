---
title: "Caching Out"
date: 2005-03-26
url: https://daringfireball.net/2005/03/caching_out
slug: caching_out
word_count: 335
---


A few brief updates on the Mac OS X 10.3 font cache bug:

- After yesterday’s report, a few readers do report seeing
bloated font cache files even though they don’t have any
PostScript fonts installed. I still think PostScript fonts
exacerbate the problem, but apparently they’re not the only
cause.
- Many readers have recommended Mark Douma’s [Font Finagler](http://homepage.mac.com/mdouma46/fontfinagler/), a
$10 shareware utility that deletes your system’s font cache
files for you. I personally can’t see spending $10 to delete a
few files which are easily removed by hand (and, frankly, I feel
more comfortable trashing them manually anyway), but at least a
few dozen DF readers are happy Font Finagler users.
A few other readers suggested [OnyX](http://www.titanium.free.fr/english.html), a freeware utility that
presents a bunch of system maintenance tasks in a Mac-style
user interface. Included amongst its features is the ability
to delete font caches.
- The cache bloating is somehow related to the fact that on
login, ATSServer opens every font located in the system’s font
folders:

Thus, one way to avoid the bug is to use a third-party font
manager, such as [Suitcase](http://www.extensis.com/en/products/product_family.jsp?id=1054), which stores your font files in any
location *other* than the system’s font folders.
Apple’s Font Book does not itself cause this problem (at least I
don’t think it does), but it doesn’t avoid it, either, because
when you use Font Book, it stores all of your fonts, including
your disabled fonts, in the system’s font folders.
The point here is not that you should buy Suitcase just to avoid
this bug,1 but rather to explain
why, if you’re already using Suitcase or a similar utility, you
probably haven’t been affected by this bug, even if you’ve got the
entire Adobe Type Library installed.
  - `/System/Library/Fonts/`
  - `/Library/Fonts/`
  - `~/Library/Fonts/`


---

1. If for no other reason than that I expect this bug to
be fixed in Mac OS X 10.3.9.  ↩︎



| **Previous:** | [Font Caches Gone Wild](https://daringfireball.net/2005/03/font_caches_gone_wild) |
| **Next:** | [Pre-Order Tiger From Amazon](https://daringfireball.net/2005/03/preorder_tiger) |


PreviousNext