---
title: "JavaScript and HTML: Forgiveness by Default"
date: 2007-04-26
url: https://blog.codinghorror.com/javascript-and-html-forgiveness-by-default/
slug: javascript-and-html-forgiveness-by-default
word_count: 1040
---

I’ve been troubleshooting a bit of JavaScript lately, so I’ve [enabled script debugging](https://web.archive.org/web/20070504180318/http://blogs.msdn.com/ie/archive/2004/10/26/247912.aspx) in IE7. Whenever the browser encounters a JavaScript error on a web page, instead of the default, unobtrusive little status bar notification...


![](https://blog.codinghorror.com/content/images/2025/05/image-485.png)


... I now get one of these glaring, modal error debug notification dialogs:


![](https://blog.codinghorror.com/content/images/2025/05/image-486.png)


I left this setting enabled out of pure forgetfulness. Browsing the web this way, I quickly realized that **the web is full of JavaScript errors.** You can barely click through three links before encountering a JavaScript error of one kind or another. Often they come in pairs, triplets, sometimes dozens of them. It’s nearly impossible to navigate the web with JavaScript error notification enabled.


JavaScript errors are so pervasive, in fact, that it’s easy to understand why IE demotes them to nearly invisible status bar elements. If they didn’t, nobody would be able to browse the web without getting notified to death. Firefox goes even further: there’s *no visible UI whatsoever* for any JavaScript errors on the current web page. You have to open the Tools | Error Console dialog to see them.


The upshot of this is that JavaScript errors, unless they result in obvious functional problems, tend to go unnoticed. **Things that would cause show stopping compiler errors in any other language are at worst minor inconveniences in JavaScript.** When errors are ignored by default, what you end up with is an incredibly tolerant, extremely permissive programming ecosystem. If it works, it works, errors be damned.


But this unparalleled flexibility has its price. Just ask Dave Murdock, who [found out the hard way](http://www.innerexception.com/2007/04/tip-make-sure-you-declare-javascript.html) how flexible JavaScript can be.

kg-card-begin: html

> So I dug into the code, which I hadn’t written, and I saw JavaScript similar to this in the execution path that was causing Firefox to hang:
> var startIndex = 0;
> for (i = startIndex; i < endIndex; i++) {
> // do some stuff here
> }
> This works fine in Internet Explorer 7. What happens in Firefox? i is reinitialized to startIndex after every run of the loop. You have to declare the loop like this for it to work:
> var startIndex = 0;
> for (var i = startIndex; i < endIndex; i++) {
> // do some stuff here
> }
> Putting the var before i is the way it ought to be as far as I can tell, but both Internet Explorer and Firefox do the wrong thing by developers here. Both browsers should be sticklers about requiring var in a loop variable declaration and produce a clear JavaScript interpreter error before the code has the chance to run.

kg-card-end: html

It’s not just JavaScript. HTML and CSS are incredibly forgiving of errors as well. Ned Batchelder [observed bizarrely tolerant behavior](https://web.archive.org/web/20070430074554/http://www.nedbatchelder.com/blog/200701.html#e20070118T062812) when specifying named colors that don’t exist. Consider this small snippet of HTML:

kg-card-begin: html

<font color=‘red’>█ This is RED</font>

kg-card-end: html
As you vary the named color, you don’t get the error you might expect. What you do get is weird colors:
kg-card-begin: html




Firefox
IE7
Opera


red

█ #ff0000


█ #ff0000


█ #ff0000



seagreen

█ #2e8b57


█ #2e8b57


█ #2e8b57



sea green

█ #0e00ee


█ #0e00ee


█ #0ea00e



sxbxxsreen

█ #0000e0


█ #0000e0


█ #00b000



sxbxxsree

█ #00000e


█ #0b00ee


█ #00b000



sxbxxsrn

█ #000000


█ #0b0000


█ #00b000



sxbxeen

█ #000e00


█ #0bee00


█ #00b0ee



sreen

█ #00ee00


█ #00ee00


█ #00ee00



ffff00

█ #ffff00


█ #ffff00


█ #ffff00



xf8000

█ #0f8000


█ #0f8000


█ #0f8000




kg-card-end: html
(If you’re curious how “sea green” can possibly equate to blue, the answers are in [the comments to Ned’s post](https://web.archive.org/web/20070501021853/http://www.nedbatchelder.com/reactor/comment.php?entryid=e20070118T062812&title=Color%20parsing%20brainteaser).)I can’t think of any other programming environment that goes to such lengths to avoid presenting error messages, that tries so hard to make broken code work, at least a little. Although there was a push to tighten up HTML into the much more strictly enforced XHTML, it’s [an utter failure](http://www.hixie.ch/advocacy/xhtml). If you’re not convinced, read [Mark Pilgrim’s thought experiment](https://web.archive.org/web/20070427180307/http://diveintomark.org/archives/2004/01/14/thought_experiment):Imagine that you posted a long rant about how [strict XHTML validation] is the [way the world should work](http://nick.typepad.com/blog/2004/01/feeddemon_and_w.html), that clients should be the gatekeepers of wellformedness, and strictly reject any invalid XML that comes their way. You click ‘Publish,’ you double-check that your page validates, and you merrily close your laptop and get on with your life.

A few hours later, you start getting email from your readers that your site is broken. Some of them are nice enough to include a URL, others simply scream at you incoherently and tell you that you suck. (This part of the thought experiment should not be terribly difficult to imagine either, for anyone who has ever dealt with end-user bug reports.) You test the page, and lo and behold, they are correct: the page that you so happily and validly authored is now not well-formed, and it not showing up at all in any browser. You try validating the page with a third-party validator service, only to discover that it gives you an error message you’ve never seen before and that you don’t understand.Unfortunately, [the Draconians won](http://www.tbray.org/ongoing/When/200x/2004/01/16/DraconianHistory): when rendering as strict XHTML, any error in your page results in a page that not only doesn’t render, but also presents a nasty error message to users.They may not have realized it at the time, but the Draconians inadvertently destroyed the future of XHTML with this single, irrevocable decision.The lesson here, it seems to me, is that **forgiveness by default is absolutely *required* for the kind of large-scale, worldwide adoption that the web enjoys**.The permissive, flexible tolerance designed into HTML and JavaScript is alien to programmers who grew up being regularly flagellated by their compiler for the tiniest of mistakes. Some of us were punished so much so that we actually started to *like* it. We point and laugh at the all the awful HTML and JavaScript on the web that barely functions. We scratch our heads and wonder why the browser can’t give us the punishment we so richly deserve for our terrible, terrible mistakes.Even though programmers have learned to like draconian strictness, **forgiveness by default is what works**. It’s here to stay. We should learn to love our [beautiful soup](http://www.crummy.com/software/BeautifulSoup/) instead.

[javascript](https://blog.codinghorror.com/tag/javascript/)
[html](https://blog.codinghorror.com/tag/html/)
[debugging](https://blog.codinghorror.com/tag/debugging/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
