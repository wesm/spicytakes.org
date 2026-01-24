---
title: "The Web Browser Address Bar is the New Command Line"
date: 2009-05-11
url: https://blog.codinghorror.com/the-web-browser-address-bar-is-the-new-command-line/
slug: the-web-browser-address-bar-is-the-new-command-line
word_count: 359
---

Google’s [Chrome browser](https://blog.codinghorror.com/why-cant-error-messages-be-fun/) passes anything you type into the address bar that isn’t an obvious URI on to the default search engine.


![](https://blog.codinghorror.com/content/images/2025/04/image-364.png)


While web browsers should have some built-in smarts, they can never match the collective intelligence of a worldwide search engine. [For example](http://www.google.com/help/features.html):

kg-card-begin: html

> [weather San Francisco](http://www.google.com/search?q=weather+San+Francisco)
>  [CSCO](http://www.google.com/search?q=CSCO)
>  [time London](http://www.google.com/search?q=time+London)
>  [san francisco 49ers](http://www.google.com/search?q=san+francisco+49ers)
>  [5*9+(sqrt 10)^3=](http://www.google.com/search?q=5*9%2B(sqrt+10)^3%3D)
>  [Henry+Wadsworth+Longfellow](http://www.google.com/search?q=Henry+Wadsworth+Longfellow)
>  [earthquake](http://www.google.com/search?q=earthquake)
>  [10.5 cm in inches](http://www.google.com/search?q=10.5+cm+in+inches)
>  [population FL](http://www.google.com/search?q=population+FL)
>  [Italian food 02138](http://www.google.com/search?q=Italian+food+02138)
>  [movies 94705](http://www.google.com/search?q=movies+94705)
>  [homes Los Angeles](http://www.google.com/search?q=homes+Los+Angeles)
>  [150 GBP in USD](http://www.google.com/search?q=150+GBP+in+USD)
>  [Seattle map](http://www.google.com/search?q=Seattle+map)
>  [Patent 5123123](http://www.google.com/search?q=Patent+5123123)
>  [650](http://www.google.com/search?q=650)
>  [american airlines 18](http://www.google.com/search?q=american+airlines+18)
>  [036000250015](http://www.google.com/search?q=036000250015)
>  [JH4NA1157MT001832](http://www.google.com/search?q=JH4NA1157MT001832)
>  510-525-xxxx (I’m hesitant to [link](http://en.wikipedia.org/wiki/867-5309/Jenny#Popularity_and_litigation) a listed personal phone number here, but it does work)

kg-card-end: html

I like to think of the **web browser address bar as the new command line**.


Oh, you wanted dozens of cryptic, obscure UNIX style command line [operators](http://www.google.com/help/cheatsheet.html) and parameters? [No problem](https://blog.codinghorror.com/google-fu/)!


> [define:defenestrate](http://www.google.com/search?q=define%3Adefenestrate)
> [presidents 1850...1860](http://www.google.com/search?q=presidents+1850...1860)
> [“plants vs. zombies” daterange:2454955-2454955](http://www.google.com/search?q=%22plants+vs.+zombies%22+daterange%3A2454955-2454955)
> [link:experts-exchange.com sucks](http://www.google.com/search?q=link%3Aexperts-exchange.com+sucks)
> [filetype:pdf programming language poster](http://www.google.com/search?q=+filetype%3Apdf+programming+language+poster)
> [allintitle:nigerian site:www.snopes.com](http://www.google.com/search?q=allintitle%3Anigerian+site%3Awww.snopes.com)


Any command line worth its salt has some kind of scripting language built in, too, right? No sweat. Just try entering this in your browser’s address bar.

kg-card-begin: html

```
javascript:alert(‘Hello, world!’)

```

kg-card-end: html

The sky’s the limit from there; whatever JavaScript you can fit in the address bar is fair game. These are more commonly known as [“bookmarklets”](http://www.google.com/search?q=bookmarklets).


Apparently we’ve spent the last 20 years [reimplementing the UNIX command line ](https://blog.codinghorror.com/when-in-doubt-make-it-public/)in the browser. Services like [yubnub](http://yubnub.org/) make this process even more social, with collaborative group creation (and ranking!) of new commands. You can find some of the cooler ones on the [golden eggs page](http://yubnub.org/kernel/golden_eggs?args=).


> [gimf “carrot top”](http://yubnub.org/parser/parse?command=gimf+%22carrot%20top%22)
> [esv Ezekiel 25:17](http://yubnub.org/parser/parse?command=esv+Ezekiel+25:17)
> 2g color colour


Honestly, I was never a big command-line enthusiast; even way back when on my Amiga I’d choose the GUI over the CLI whenever I could. But maybe I bet on the wrong horse. Perhaps the command prompt – or more specifically, the **search oriented, crowdsourced, world public command prompt** – really [is the future](https://blog.codinghorror.com/is-the-command-prompt-the-new-desktop/).

[search engines](https://blog.codinghorror.com/tag/search-engines/)
[web browsers](https://blog.codinghorror.com/tag/web-browsers/)
[command line](https://blog.codinghorror.com/tag/command-line/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
