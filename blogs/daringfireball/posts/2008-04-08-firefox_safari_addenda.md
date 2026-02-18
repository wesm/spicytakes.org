---
title: "Firefox 3 vs. Safari 3 Addenda"
date: 2008-04-08
url: https://daringfireball.net/2008/04/firefox_safari_addenda
slug: firefox_safari_addenda
word_count: 1067
---


## Classifying My Criticism


After reading all the feedback regarding my [Safari 3/Firefox 3 comparison](http://daringfireball.net/2008/04/firefox_3_safari_3) from over the weekend, it occurred to me that I should have clearly organized my criticism of Firefox 3 into two separate categories: those issues where Firefox is clearly wrong, and those which are subjective issues where I just happen to prefer the way Safari works.


Things where Firefox is wrong:

- Background windows don’t have Leopard’s light gray “disabled” appearance.
- Text editing shortcuts don’t follow Mac standards.
- No Services menu or system-wide Dictionary support.
- The “New Tab” command only works when a browser window is frontmost.
- No AppleScript support.
- Tabs can’t be dragged to create a new window.
- Inline PDF viewing.


Subjective design issues:

- Firefox’s location field auto-completion requires you to use Down Arrow (or Tab) to select one of the suggestions; Safari lets you just hit Return to choose the first one. Some people strongly prefer Firefox’s method because Safari’s method gets in their way when they really do want to go to the “example.com” homepage, but Safari unhelpfully auto-completes to a page within the example.com domain. With Firefox’s method you have to hit an extra key (Down Arrow) to get any auto-completion at all. With Safari’s method you have to hit an extra key (Delete) to reject auto-completion when you really just want the URL you’ve typed into the field. I simply prefer Safari’s behavior.1
- I prefer Safari’s “inside the location field” progress indicator. There is, however, a Firefox extension called [Fission](https://addons.mozilla.org/en-US/firefox/addon/1951) that mimics this, and it works in the current Firefox 3 beta.


In case it wasn’t clear, I certainly wasn’t pushing for Firefox to clone Safari’s UI and behavior. In fact, that would be foolish — Firefox can’t be better than Safari if it isn’t different.


## Mike Beltzner’s Response


Mozilla developer Mike Beltzner wrote a [thoughtful weblog post](http://www.beltzner.ca/mike/archives/2008/04/good-suggestion.html) responding to mine. The best news is that two of my top complaints, the lack of a proper “background” window appearance and the text editing behavior of arrow keys, are set to be addressed before Firefox 3.0 ships. **Update:** Cool: the bug where Command-T only works with a browser window frontmost [is already fixed](https://bugzilla.mozilla.org/show_bug.cgi?id=425486) in nightly builds.


Regarding the text editing bug:


> Gruber’s not alone. A non-scientific survey of Mac users showed
> that 8% believed this to be the most significant problem with
> Firefox on the Mac. There’s [a bug on file](https://bugzilla.mozilla.org/show_bug.cgi?id=231754) which has had some
> activity, and it looks like Josh Aas would be willing to review a
> patch if one came along.


It warms my heart that so many Mac users care about this. Beltzner also expressed interest in some of the other issues, like dragging a tab to create a new window. His whole piece is worth reading, and shows why Firefox 3 is already such an improvement in Mac-specific ways.


## Development Versus Daily Browsing


The point of my comparison was to explain why I went back to Safari for daily browsing, but I mentioned in my review that many web developers might use Safari for browsing, but Firefox for web development testing. Dozens of readers wrote in to say they do just that, and most of them pointed out that I neglected to mention [Joe Hewitt’s acclaimed Firebug extension](http://www.getfirebug.com/) for web developers.


Safari 3 has beefed up its own web developer tools — its [new Develop menu](http://developer.apple.com/internet/safari/faq.html) includes a slew of useful tools, including a Web Inspector window that’s comparable to the Firefox Web Developer plugin. Plus there’s [Drosera](http://trac.webkit.org/projects/webkit/wiki/Drosera), the JavaScript debugger for WebKit. But I didn’t get a single email from anyone who prefers Safari developer tools over Firebug and Firefox.


Here’s an oddity I forgot to mention, though: Safari 3.1’s View Source window still doesn’t offer HTML syntax highlighting — but it’s clearly capable of it, because the source view in the Web Inspector window has it.


## Counting Clicks


Complaining about Firefox’s “just click in the location field and the whole URL will be selected automatically” behavior, I wrote:


> When I click the mouse in the middle of a URL, I just want to
> place the insertion point. I don’t want to select the entire URL.
> If I wanted to select the entire URL, I’d double-click. Click to
> place, double-click to select — just like any other text field.


Clearly that was wrong. Double-clicking should select a “word” within the URL, and triple-clicking should Select All. *That’s* standard Mac text field behavior, and that’s how Safari works. The only excuse I can offer is that I never triple-click in Safari because I know that there’s a convenient shortcut to select the entire URL if that’s what I want: just single-click on the favicon on the left side of the location field. (You can also drag this favicon, even from a Safari window in the background.)


## Benchmarks


I didn’t bother with benchmarks because I don’t care. Both Safari 3 and Firefox 3 feel fast enough to me, and I didn’t notice any sites where one performed significantly better than the other. Your mileage may vary; a few readers claim, for example, that Gmail works a lot faster in Firefox.


## FlashBlock and Other Extensions


I was under the impression that the FlashBlock Firefox extension didn’t yet work with Firefox 3, because it doesn’t appear in the Get Add-Ons tab of Firefox’s Add-Ons window. It does work, though — you just have to go to [the FlashBlock web page](http://flashblock.mozdev.org/installation1.html) to install it. What FlashBlock does is very cool: it disables all Flash elements on a page until you click on them. If you’re as annoyed by obnoxious animation as I am, it’s just what the doctor ordered.


It’s also the case that you can disable the version checking that keeps not-yet-certified-for-Firefox-3 add-ons from loading; apparently many of them work just fine.


And a bunch of people suggested input manager hacks for Safari that attempt some of these same things. I know these things exist, and I’ve used some in the past, but they are not equivalent to Firefox extensions based on supported, official APIs.


---

1. And as I [linked](http://daringfireball.net/linked/2008/april#mon-07-bengtsson) the other day, it’s possible to get this behavior in Firefox [via a hidden preference](http://overooped.com/post/30932542). ↩︎



| **Previous:** | [Firefox 3 vs. Safari 3](https://daringfireball.net/2008/04/firefox_3_safari_3) |
| **Next:** | [Safari’s Tab Dragging Modes](https://daringfireball.net/2008/04/safari_tab_dragging_modes) |


PreviousNext