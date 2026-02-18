---
title: "Disambiguating iPhone Model Names That Have the ‘S’ Suffix"
date: 2024-11-12
url: https://daringfireball.net/2024/11/disambiguating_iphone_model_names_that_have_the_s_suffix
slug: disambiguating_iphone_model_names_that_have_the_s_suffix
word_count: 1031
---


Here’s the Apple support page [listing the devices compatible with iOS 18](https://support.apple.com/guide/iphone/iphone-models-compatible-with-ios-18-iphe3fa5df43/ios). They’re listed in chronological order, oldest to newest, and the list begins with the iPhone XR and iPhone XS from 2018. But on this support page, Apple styles the “R” and “S” suffixes as small caps. Screenshot:


Earlier today [I linked](https://daringfireball.net/linked/2024/11/12/find-my-airtags-airlines) to [this Apple Newsroom post](https://www.apple.com/newsroom/2024/11/apples-find-my-enables-sharing-location-of-lost-items-with-third-parties/), regarding the new “Share Location” feature in Find My in iOS 18.2 beta 3. The Apple Newsroom post contains this sentence on iOS 18 compatibility:


> Share Item Location is available now in most regions worldwide as
> part of the public beta of iOS 18.2, which will soon be available
> to all users as a free software update for iPhone Xs and later.


Is that the iPhone XS, styled with a lowercase *s*? Or are they referring to 2017’s iPhone X, and pluralizing it with the lowercase *s*? By nature of my work, I know that Apple’s internal style is never to pluralize a product name like “iPhone X” by adding an *s*; they would write something like “iPhone X models” or “iPhone X devices”. But to the casual reader, it’s ambiguous. I wound up double-checking on Apple’s aforelinked support page for iOS 18 device compatibility, just to be sure. And even there it’s only clear because a small caps *R* has a distinctive uppercase letterform.


Apple’s S suffix for certain iPhone models — 3GS, 4S, 5S, 6S, XS — has always been problematic in this regard. It’s a particular problem for publications with an all-caps headline style, such as posts here on Daring Fireball. [This post from July 2008](https://daringfireball.net/linked/2008/07/18/iphone-supply), shortly after the iPhone 3G came out, is headlined “iPhone 3Gs in Short Supply”, but when you see it styled on DF itself, [it looks like](https://daringfireball.net/misc/2024/11/iphone-3g-plural-s-2008.png) “IPHONE 3GS IN SHORT SUPPLY”. At the time I wrote that, it wasn’t confusing at all — the iPhone 3G had only started shipping a few weeks prior, so the iPhone 3GS didn’t even exist yet (and with the 3G being the second-ever iPhone model, there wasn’t yet any history of Apple applying an S suffix to a model name). If I had it to do all over again, I’d have used an apostrophe (“iPhone 3G’s in Short Supply”) or just omitted pluralizing it in the first place (“iPhone 3G in Short Supply”).1


But the letter S has a second ambiguity problem, in addition to pluralization: its upper and lowercase letterforms are distinguished only by size, not shape, in most roman fonts. That means if you try to distinguish it via the use of small caps, it’s to no avail, because a small caps uppercase *S* looks nearly (if not completely) identical to a lowercase *s*. And in fact, that’s exactly how Apple tends to style the *S* and *R* in “iPhone XS” and “iPhone XR”, as evidenced by the screenshot above showing the device compatibility list for iOS 18.


Viewing the HTML source on Apple Newsroom shows that that’s how they’ve styled “XS” in today’s post:


```
iPhone X<span class="all-small-caps">s</span> and later

```


The `all-small-caps` class is a simple one-rule style defined [in the Apple Newsroom CSS](https://www.apple.com/newsroom/styles/site.built.css):2


```
.all-small-caps {
    font-variant-caps:all-small-caps
}

```


Here’s where I think Apple could do better. In their HTML markup, they should use an uppercase *S* inside the `span` tag delineating the small caps. They should do this:


```
<span class="all-small-caps">S</span>

```


instead of this:


```
<span class="all-small-caps">s</span>

```


Both of those will render the *s* in small caps in the browser. But when a user copies and pastes the text from the rendered output in their browser, they’ll get the *S* or *s* in the same case it is in the HTML, because small-caps styling doesn’t carry across copy-and-pasting. Whether the original HTML markup uses an uppercase *S* or lowercase *s* inside the `all-small-caps` span, the rendered output users see in their web browser will be a small caps *S*. But what the user gets when copying and pasting will fall back to the actual case of the *S* in the HTML code.


Ideally, Apple wants us to see that *S* in small caps. But it’s inevitably going to fall back to simple upper or lowercase after copying and pasting, and in that situation (yes, I was tempted mightily to write *case* there), it’s clearly better to fall back on uppercase, giving copy-and-pasters the unambiguous “iPhone XS”.


Anyway, I’m glad Apple has seemingly abandoned these S-suffixed iPhone names. Next year when the XS and XR age out of support for iOS 19, we might be done writing about them in the present tense.


---

1. It’s a mistake, and a suggestion of low literacy, to erroneously use the apostrophe-s sequence to pluralize words or names where the proper way to spell the plural is to just add *s*. E.g., Apple employees are said to *bleed six colors*, not *bleed six color’s*. You surely know this. For chrissake you’re reading a footnote in a persnickety post regarding best practices in HTML markup for disambiguating product names in uncommon edge cases. But it’s not true that one should never form plurals using apostrophes. Per [The New York Times Manual of Style and Usage](https://www.amazon.com/York-Times-Manual-Style-Usage-dp-1101905441/dp/1101905441/?tag=df-amzn-20): “Use apostrophes for plurals formed from single letters: *He received A’s and B’s on his report card. Mind your p’s and q’s.*” [My own style guide](https://daringfireball.net/misc/df-style-guide.text) goes further, and endorses apostrophes for plurals of initialisms in headlines (because of DF’s all-caps headline style for short posts), to make clear that in a headline such as, say, “Truckers Are Still Buying CB’s”, that they’re buying two-way radios, not the television network. ↩︎
2. I, for one, do not care for Apple’s CSS coding style that [omits the optional trailing semicolon](https://stackoverflow.com/questions/11939595/leaving-out-the-last-semicolon-of-a-css-block) from the last rule in a block. Makes me just a tad itchy when I see that.3 ↩︎︎
3. While I’m straying way out in the coding-style weeds here, let me also observe that I feel old and grumpy about the fact that Apple’s HTML markup on Newsroom posts wraps body text paragraphs in `<div class="pagebody-copy">` tags, rather than simple semantic `<p>` tags. ↩︎︎



| **Previous:** | [How It Went](https://daringfireball.net/2024/11/how_it_went) |
| **Next:** | [Dr. Oz](https://daringfireball.net/2024/11/dr_oz) |


PreviousNext