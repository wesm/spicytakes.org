---
title: "The Paper Data Storage Option"
date: 2009-07-31
url: https://blog.codinghorror.com/the-paper-data-storage-option/
slug: the-paper-data-storage-option
word_count: 858
---

As programmers, we [regularly work with text encodings](https://blog.codinghorror.com/there-aint-no-such-thing-as-plain-text/). But there’s another sort of encoding at work here, one we process so often and so rapidly that it’s invisible to us, and we forget about it. I’m talking about **visual encoding – translating the visual glyphs of the alphabet you’re reading right now**. The alphabet is no different than any other optical machine readable input, except the machines are *us*.


But how efficient is the alphabet at encoding information on a page? Consider some of the alternatives – different visual representations of data you could print on a page, or display on a monitor:


[5081 punch card](http://en.wikipedia.org/wiki/Punched_card#IBM_80_column_punch_card_format)
up to 80 alphanumeric characters


![](https://blog.codinghorror.com/content/images/2025/04/image-421.png)


[Maxicode](http://en.wikipedia.org/wiki/MaxiCode)
up to 93 alphanumeric characters


![](https://blog.codinghorror.com/content/images/2025/04/image-420.png)


[Data Matrix](http://en.wikipedia.org/wiki/Data_matrix_%28computer%29)
up to 2,335 alphanumeric characters


![](https://blog.codinghorror.com/content/images/2025/04/image-419.png)


[QR Code](http://en.wikipedia.org/wiki/QR_Code)
up to 4,296 alphanumeric characters


![](https://blog.codinghorror.com/content/images/2025/04/image-418.png)


[Aztec Code](http://en.wikipedia.org/wiki/Aztec_Code)
up to 3,067 alphanumeric characters


![](https://blog.codinghorror.com/content/images/2025/04/image-417.png)


[High Capacity Color Barcode](http://en.wikipedia.org/wiki/High_Capacity_Color_Barcode)
varies by # of color and density; up to 3,500 characters per square inch


![](https://blog.codinghorror.com/content/images/2025/04/image-415.png)


Printed page
about 10,000 characters per page


![](https://blog.codinghorror.com/content/images/2025/04/image-413.png)


Paper the way we typically use it is criminally inefficient. It has a ton of wasted data storage space. That’s where programs like [PaperBack](http://ollydbg.de/Paperbak/) come in:


> PaperBack is a free application that allows you to back up your precious files on ordinary paper in the form of oversized bitmaps. **If you have a good laser printer with the 600 dpi resolution, you can save up to 500,000 bytes of uncompressed data on a single sheet.**
> You may ask –why? Why, for heaven’s sake, do I need to make paper backups, if there are so many alternative possibilities like CD-R’s, DVD-R’s, memory sticks, flash cards, hard disks, streaming tapes, ZIP drives, network storage, magneto-optical cartridges, and even 8-inch double-sided floppy disks formatted for DEC PDP-11? The answer is simple: you don’t. However, by looking on CD or magnetic tape, you are not able to tell whether your data is readable or not. You must insert your medium into the drive, if you even have one, and try to read it.
> Paper is different. Do you remember punched cards? For years, cards were the main storage medium for the source code. I agree that 100K+ programs were... inconvenient, but hey, only real programmers dared to write applications that large. And used cards were good as notepads, too. Punched tapes were also common. And even the most weird encodings, like [CDC](http://en.wikipedia.org/wiki/CDC_display_code) or [EBCDIC](http://en.wikipedia.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code), were readable by humans (I mean, by real programmers).
> Of course, bitmaps produced by PaperBack are also human-readable (with the small help of any decent microscope). I’m joking. What you need is a scanner attached to your PC.


PaperBack, like many of the other visual encodings listed above, includes provisions for:

- compression – to increase the amount of data stored in a given area.
- redundancy – in case part of the image becomes damaged or is otherwise unreadable.
- encryption – to prevent the image from being readable by anyone except the intended recipient.


![](https://blog.codinghorror.com/content/images/2025/04/image-412.png)


Sure, it’s still paper, but the digital “alphabet” you’re putting on that paper is a far more sophisticated way to store the underlying data than traditional ASCII text.


This may all seem a bit fanciful, since the alphabet is about all us poor human machines can reasonably deal with, at least not without the assistance of a computer and scanner. But there is at least one legitimate use for this stuff, the [trusted paper key](http://en.wikipedia.org/wiki/Trusted_paper_key). There’s even software for this purpose, [PaperKey](http://www.jabberwocky.com/software/paperkey/):


> The goal with paper is not secure storage. There are countless ways to store something securely. A paper backup also isn’t a replacement for the usual machine readable (tape, CD-R, DVD-R, etc.) backups, but rather as an if-all-else-fails method of restoring a key. Most of the storage media in use today do not have particularly good long-term (measured in years to decades) retention of data. If and when the CD-R and/or tape cassette and/or USB key and/or hard drive the secret key is stored on becomes unusable, the paper copy can be used to restore the secret key.
> For paper, on the other hand, to claim it will last for 100 years is not even vaguely impressive. High-quality paper with good ink regularly lasts many hundreds of years even under less than optimal conditions.
> Another bonus is that ink on paper is readable by humans. Not all backup methods will be readable 50 years later, so even if you have the backup, you can’t easily buy a drive to read it. I doubt this will happen anytime soon with CD-R as there are just so many of them out there, but the storage industry is littered with old now-dead ways of storing data.


Computer encoding formats and data storage schemes come and go. This is why so much archival material survives best in the simplest possible formats, like unadorned ASCII. Depending on what your goals are, **a combination of simple digital encoding and the good old boring, reliable, really *really* old school technology of physical paper** can still make sense.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[data encoding](https://blog.codinghorror.com/tag/data-encoding/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[visual representation](https://blog.codinghorror.com/tag/visual-representation/)
[optical character recognition](https://blog.codinghorror.com/tag/optical-character-recognition/)
