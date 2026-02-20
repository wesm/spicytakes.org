---
title: "iBox Overlay Doesn't Scroll"
date: 2009-02-10
url: https://www.kalzumeus.com/2009/02/10/ibox-overlay-doesnt-scroll/
slug: ibox-overlay-doesnt-scroll
word_count: 337
---


Hello, Google searcher!  I spent 2 hours so you don’t have to!


Search for the following line of code:


els.overlay.style.height = height + ‘px';


Now add this after it.  Problem solved!


//causes the overlay to scroll as the page scrolls — necessary for Safari/Chrome/FF3


if (document.viewport && document.viewport.getScrollOffsets()) {


var top = document.viewport.getScrollOffsets()[1];


els.overlay.style.top = top + “px”;


}


OK, back to regular readers of this blog: as mentioned previously, I’m testing a new shopping cart.  There were previously 3 known issues:

1. the overlay didn’t scroll
2. the price got all funky in Google Checkout under some conditions
3. the quantity and price were inconsistent if you switched the item after closing the cart


I’m happy to report:

1. I patched iBox to avoid this issue, and tested it in five browsers because I just have no life whatsoever.  Please see above code if you need it.
2. e-junkie continued their years-long practice of above-and-beyond support and corrected my misunderstanding of their API, which let me patch my code around this
3. I patched my code, in a ho-hum workmanlike fashion.


The more I use Javascript the more I feel that a) all websites I’ve ever used are missing massive opportunities to make their user interaction sexier than they can possibly imagine and b) I can understand why, because coding Javascript is the most painful programming I’ve done since C in college.


Oh, God, the cross-browser issues!  The sheer complexity of the DOM model!  The paucity of good documentation available in my IDE next to autocomplete!  (Sorry, I will always be a Java programmer at heart.)


Anyhow, if you want to take a gander at the [current version of the sample car](http://www.bingocardcreator.com/purchasing-alternate.htm)t or [compare it to the current cart](http://www.bingocardcreator.com/purchasing.htm), go nuts.  After I alter it a bit tomorrow to make the error handling sexier (i.e. for the disallowed multiple purchase through Google — it has never happened before but, eh, why not ship it right the first time), I am going to start the split test.
