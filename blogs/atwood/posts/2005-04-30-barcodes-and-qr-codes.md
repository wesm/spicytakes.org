---
title: "Barcodes and QR Codes"
date: 2005-04-30
url: https://blog.codinghorror.com/barcodes-and-qr-codes/
slug: barcodes-and-qr-codes
word_count: 329
---

I recently purchased a [USB CueCat](https://www.ebay.com/itm/393501980855) from eBay to play around with UPC barcodes, which I found out about from comments posted in a [Scott Hanselman blog entry](https://web.archive.org/web/20060629202002/http://www.hanselman.com/blog/CommentView,guid,48e61762-b273-4a6d-b0d0-f90cb56e3fde.aspx). It’s fun to run around the house scanning in UPCs from household items, although the low-powered LED reader in the CueCat definitely pales in comparison to the industrial laser readers you’ll find at your local supermarket. Still, you can’t beat it for $15, and the PS2 version can be had for even less. If you’re wondering why exactly you would want to do this, check out [Delicious Library](https://web.archive.org/web/20050508014830/http://www.delicious-monster.com/) ([review](http://arstechnica.com/reviews/apps/delicious-library.ars)). Like so many things Apple, it’s self-consciously cute where it should be practical, but the concept is sound.


I saw a reference in [Ned Batchelder’s blog](http://www.nedbatchelder.com/blog/index.html) to **UPCs on steroids**: something called [QRCode](https://web.archive.org/web/20050507173601/http://www.denso-wave.com/qrcode/qrfeature-e.html). QRCode is designed to be “scanned” via cell phone cameras, and it’s the most [information-dense 2D bar code format](http://www.denso-wave.com/qrcode/aboutqr-e.html) currently available:

- 7,089 numeric characters
- 4,296 alphanumeric characters
- 2,953 bytes
- 1,817 Kanji


You can generate your own QRCode using a web-based tool, but it doesn’t appear to work for the larger texts that I tried. There’s a small [Windows app](http://www.psytec.co.jp/docomo.html) which is unfortunately entirely in Japanese, but it’s superior to the web-based tool. Here’s a small animated movie* of it in action. It’s interesting to watch the data shift around and resize itself as more and more is added. Note the fixed reference points in the data as well, for camera orientation.


![Movie of QRCode generation](https://blog.codinghorror.com/content/images/uploads/2005/04/6a0120a85dcdae970b0120a86d4ea3970b-pi.gif)


It’s a shame American cell phones and American advertisers haven’t adopted QRCode. However, it may be a preview of things to come as cameras become a standard feature of cell phones.


*If you have Windows Media Player 9 or higher, you can view the WMP9 movie version of this app capture, which uses the [screen capture codec](https://web.archive.org/web/20050506171306/http://www.microsoft.com/windows/windowsmedia/9series/codecs/video.aspx) introduced in WMP9: it’s 50% smaller than the animated GIF and offers higher quality too!

[barcode](https://blog.codinghorror.com/tag/barcode/)
[qr code](https://blog.codinghorror.com/tag/qr-code/)
[upc](https://blog.codinghorror.com/tag/upc/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
