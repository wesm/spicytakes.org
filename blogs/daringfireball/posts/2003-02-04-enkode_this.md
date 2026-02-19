---
title: "Enkode This"
date: 2003-02-04
url: https://daringfireball.net/2003/02/enkode_this
slug: enkode_this
word_count: 337
---


Dan Benjamin has launched [Hiveware](http://hiveware.com/), purveyors of fine software. Their first project is Enkoder, an update to Mr. Benjamin’s previous Hivelogic Email Address Encoder. You can tell that the new Enkoder is better and more fun, because its name is spelled with a *k*.


The Enkoder is available in three forms, all free of charge:

- [Enkoder Mac OS X application](http://hiveware.com/enkoder.php) (sporting a refined, polished interface)
- [Enkoder web form](http://hiveware.com/enkoder_form.php) (accessible from any browser, on any platform)
- [Enkoder command-line tool](http://www.hiveware.com/enkode_tool.php) (for Mac OS X, Windows, Linux, and FreeBSD)


It is natural and convenient to use `mailto` links in web pages so that readers can send you email. The problem, however, is that spammers have written spidering programs that crawl the web, looking for email addresses. If you put an address on a web page in plain text, soon thereafter you will begin receiving spam at that address.


A rudimentary defense is to use HTML entities to encode your address. This was the mechanism we previously applied here at Daring Fireball. For example, instead of using the letter “c”, you instead use the decimal entity “`&#99;`” or the hexadecimal entity “`&#x63;`”. Repeat for every character in your address and your address will be protected from many spam harvesters.


*Many*, not all.


The problem with this technique is that it isn’t very hard at all to write a spam harvesting spider that can decode HTML entities. A few lines of Perl will do it.


The Hiveware Enkoder goes much further, using devilishly clever JavaScript to hide your address from anyone looking at your web page source code (such as spam harvesters), but presenting pleasantly clickable links when the page is rendered in a web browser. This is not impregnable security. It is merely heightened obscurity. At least for now, however, Enkoder will put your email addresses one step ahead of the spammers.


We’re using it here at Daring Fireball. We recommend you do the same.



| **Previous:** | [Remember IE?](https://daringfireball.net/2003/02/remember_ie) |
| **Next:** | [SmartyPants 1.1](https://daringfireball.net/2003/02/smartypants_11) |


PreviousNext