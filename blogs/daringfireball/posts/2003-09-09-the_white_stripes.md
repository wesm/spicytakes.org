---
title: "The White Stripes"
date: 2003-09-09
url: https://daringfireball.net/2003/09/the_white_stripes
slug: the_white_stripes
word_count: 602
---


About two few weeks ago, I switched to a new squarish ad layout from Google. With this new format and the customizable colors before it, I’m really happy with the way the ads look here on Daring Fireball. The only hiccup is caused by what I believe to be a bug in Safari — and if it’s not a bug, per se, at the very least it’s a discrepancy from other modern browsers.


Here’s how the ads look in Camino (and other Mozilla-derived browsers, as well as Mac IE 5 and Win IE 6):


However, this is how they look in Safari:


Note the spurious horizontal white stripe at the bottom — that’s the aforementioned hiccup.


What’s going on is this. Google’s AdSense program supplies me with a snippet of JavaScript code to paste into web pages where I want the ads to appear. This JavaScript code does two things: (1) it creates an inline frame (a.k.a. [iframe](http://www.htmlhelp.com/reference/html40/special/iframe.html)); (2) fills the inline frame with a web page from Google’s AdSense web server.


An inline frame is like a hole in the surrounding page, and the hole is filled in with another web page. You can see this for yourself by control-clicking inside the ad box on this page, and choosing “Open Frame in New Window” from the contextual menu.


In the ad layout I’m using now, the iframe is specified exactly 250 pixels tall. It is filled by a web page that creates a table, which table is also exactly 250 pixels tall, thus perfectly fitting the iframe.


That’s the intention, at least. The problem is that while Safari renders the iframe 250 pixels tall, as specified, it renders the table only 248 pixels tall. The remaining two pixels appear as a white stripe. The extra pixels are white because the background color I’ve specified for my ads is only applied to the table, not to the background of the ad page itself. (Google could fix the problem by setting the background of the ad page’s body tag to my specified background color, instead of just setting the table’s background color; and I’ve reported this to Google as a bug.)


If you’ve got a screen ruler and want to measure it yourself, open the ad iframe in its own window first. The border you see around the ads on this page is *mine*, generated via CSS — thus the ad box you see is a bit larger than 250 pixels, and the actual AdSense iframe has no visible border.


I think this may be a bug in Safari because the table, as specified by Google, explicitly declares itself with a height of 250 pixels:


```

<table width="300" height="250" cellspacing="1" 
 cellpadding="0" border="0" bgcolor="#535C66">

```


However, I say it “may be a bug” because *height* is a bogus attribute for a table tag — completely non-standard. It’s a junk attribute first supported by some ancient version of Netscape. It’s rather incongruous to see a company as clever as Google writing such embarrassingly bad markup (although not necessarily surprising, since their markup for Google.com is similarly utterly non-standards-compliant).


I’ve submitted a bug report against Safari to Apple, but frankly I won’t blame them if they don’t want to fix this. Safari makes a heroic and largely successful attempt to render non-standard HTML markup just like crummy old versions of Netscape and IE do, but it’s impossible to achieve 100 percent compatibility. There is no “correct” rendering for non-standard markup.


In the meantime, if you use Safari, please forgive the stripe.



| **Previous:** | [Using CVS with BBEdit](https://daringfireball.net/2003/09/using_cvs_with_bbedit) |
| **Next:** | [IBM Compatible](https://daringfireball.net/2003/09/ibm_compatible) |


PreviousNext