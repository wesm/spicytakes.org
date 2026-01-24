---
title: "Getting Back to Web Basics"
date: 2006-01-04
url: https://blog.codinghorror.com/getting-back-to-web-basics/
slug: getting-back-to-web-basics
word_count: 1010
---

Every few years, Jakob Nielsen takes websites to task with a Top Ten Web Design Mistakes article. Although things have clearly improved since [the original 1996 list](http://www.useit.com/alertbox/9605a.html), I’m particularly concerned that **in the competitive frenzy to get all JavaScripted up for Web 2.0, we may be defeating the very simplicity that made the web so popular**. Nielsen shares this concern:

kg-card-begin: html

> *This year’s [list of top problems](http://www.useit.com/alertbox/designmistakes.html) clearly proves the need to get back to Web design basics. There’s much talk about new fancy “Web 2.0” features on the Internet industry’s mailing lists and websites, as well as at conferences. But users don’t care about technology and don’t especially want new features. They just want quality improvements in the basics:
>  * 
> text they can read;
> content that answers their questions;
> navigation and search that help them find what they want;
> short and simple forms (streamlined registration, checkout, and other workflow;) and
> no bugs, typos, or corrupted data; no linkrot; no outdated content
> *Anytime you feel tempted to add a new feature or advanced technology to your site, first consider whether you would get a higher ROI by spending the resources on polishing the quality of what you already have. Most companies, e-commerce sites, government agencies, and non-profit organizations would contribute more to their website’s business goals with better headlines than with any new technology (aside from a better search engine, of course).*

kg-card-end: html

Of course, Web 2.0 isn’t just JavaScript. But according to Paul Graham, JavaScript is one of the three key characteristics that [define Web 2.0](http://www.paulgraham.com/web20.html):


> *One ingredient of its meaning is certainly Ajax, which I can still only just bear to use without scare quotes. Basically, **what “Ajax” means is “Javascript now works.”** And that in turn means that web-based applications can now be made to work much more like desktop ones.
> In fact the new generation of software is *[*being written way too fast*](https://blog.codinghorror.com/new-years-resolutions-for-microsoft/)* for Microsoft even to channel it, let alone write their own in house. Their only hope now is to buy all the best Ajax startups before Google does. And even that’s going to be hard, because Google has as big a head start in buying microstartups as it did in search a few years ago. After all, Google Maps, the canonical Ajax application, was the result of a startup they bought.*


I’ve visited quite a few Ajax sites that **committed the cardinal sin of the web: they broke the back button.** Nothing demonstrates an utter disregard for the user quite like breaking the back button does. Going “back” is the second most common user activity after clicking a hyperlink. Didn’t we learn our lesson with <frame>? Frame based layouts are so widely reviled for their address bar and back button breaking ways that they have been banished to [freak-in-a-sideshow status](http://www.useit.com/alertbox/9612.html). And yet when an Ajax app breaks the back button, it’s no big deal, it’s an acceptable side-effect of all that cool client-side processing?


Well, it is a big deal, and it isn’t acceptable. I hate to single out everyone’s favorite whipping boy, but it’s the most recent example:

1. Visit http://www.live.com (now obsolete)
2. Click the Add Content link
3. Search for anything; I used “news”
4. Now click the back button. It won’t do anything.


I don’t care how many fancy client-side features your site has – if you break the back button, you broke the internet for your users. I can’t emphasize this enough.


A big part of the web’s ease of use is basic visibility – if you can see it, you can click it. Nothing hidden. Nothing up our sleeves. But the minute you throw a drop-down menu on your page, you’ve broken that contract with the user. That’s why **drop-down menus don’t belong on the web**. And yet we can’t seem to get away from the damn things.


[Amazon](http://www.amazon.com/), of all places, has an incredibly annoying DHTML menu on their home page. Just mouse over the “See All 32 Product Categories” tab. Is it really necessary for this tab to spawn an aggravating DHTML Javascript popup, complete with its own click-interrupting animation? It’s disconcerting to accidentally mouse over this area and have a popup blasted in your face. Why not just let me click the link and see the categories, like every other web page I’ve ever visited?


Worse, many sites’ implementations of drop-down menus are erratic and inferior to the menus in the operating system. Consider the [3leaf site](https://web.archive.org/web/20060207200048/http://3leaf.com/Home.aspx): why can’t I click on the Services menu, while all the others are clickable? Why doesn’t the pointer change to indicate that I’m clicking on a hyperlink? The [future of drop-down menus](https://blog.codinghorror.com/on-the-death-of-the-main-menu/) is uncertain even in Windows; shoehorning a marginal GUI convention on today’s web is asking for trouble. Better to avoid these problems altogether by ditching drop-down menus entirely.


[Shaun Inman’s site](https://web.archive.org/web/20060104041722/https://shauninman.com/plete/), which was inexplicably nominated for a [best-designed bloggie award](http://2005.bloggies.com/), is truly painful to visit. It reads like a laundry list of Nielsen’s complaints:

- The font is tiny by default, on both IE and Firefox
- Visited links are shown in unreadable strikeout font
- Crazy, confusing top and bottom navigation slide-out panels


Shaun Inman seems to be a well-regarded web designer – shouldn’t he know better? Or is it the Web 2.0 kool-aid? If that’s what it takes to get a bloggie design award, I’m sure hoping [this guy](https://web.archive.org/web/20060916201734/https://web.utk.edu/~gwhitney/awful/awful2.html) starts a blog, because he’s a shoo-in for 2006.


I don’t want to turn this into a rant session, so I’ll stop here. **Clever JavaScript on your web page does not exempt you from good web design.** Instead of spending all this time exerting maximum cleverness to transcend the weaknesses of the web medium, It might be a better idea to play to the web’s strengths – such as speeding up [how fast your pages load](http://bravenewword.typepad.com/brave_new_word/2005/11/web_developers_.html), or avoiding [recent ill-advised design trends](http://blog.outer-court.com/archive/2005-12-31-n34.html). And whatever you do, *don’t break the freaking back button*.

[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[web design](https://blog.codinghorror.com/tag/web-design/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
