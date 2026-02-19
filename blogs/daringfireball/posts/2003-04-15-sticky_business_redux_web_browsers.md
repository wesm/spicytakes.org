---
title: "Sticky Business Redux: Web Browsers"
date: 2003-04-15
url: https://daringfireball.net/2003/04/sticky_business_redux_web_browsers
slug: sticky_business_redux_web_browsers
word_count: 1888
---


## Where QuarkXPress 3.32 Is Still Considered ‘New’


Several Quark-using readers responded to yesterday’s “[The Sticky Business of Page Layout](http://daringfireball.net/2003/04/the_sticky_business_of_page_layout.html)”, pointing to a major obstacle preventing them from moving to InDesign: print shops that don’t accept (or frown upon) InDesign files.


I did mention this in passing, when discussing how proprietary document formats make an application sticky:


> Document formats are another source of stickiness (most spectacularly used
> by Microsoft to attach users to the Office suite). Your print shop might
> only accept QuarkXPress documents. Your clients might send you QuarkXPress
> documents.


If you don’t work in the print design industry, this might come as a bit of a surprise. You might be thinking, *Why not just switch to another print shop which does accept InDesign files?* Which is a reasonable question, but ignores the fact that designers and printers develop very strong relationships. A good print shop — one that reliably produces good output quickly — is hard to find. When you find a printer you trust, the tendency is to stick with them.


The problem is that the printing industry moves at a decidedly old-world pace. It’s an industry that considers Gutenberg a pioneer, not Jobs. Printing presses get replaced after decades, not years. And that, unfortunately, is the pace at which many of them considering buying new software. To printers, InDesign is still brand-spanking new.


In desktop publishing, no single designer is an island. If you’re a software developer (of any kind, application or web), you can produce your own output from start to finish. Your source code, processed through your software, distributed to the world on your server. But in print, even if you work by and for yourself, you need a print shop to create your final output.


## Lessons in Successful Monopoly Maintenance


The idea I put forth yesterday to explain Quark’s fall from grace could be summarized thusly: Without serious competition, application software tends to stagnate.


Photoshop serves as an exception to the rule — an application that hasn’t had serious competition in over a decade, but yet has remained popular and has improved fairly consistently with each revision. If Quark Inc. had steered XPress in a similar direction — with steady improvements and a humble focus on doing just one thing, page layout — there likely never would have been an InDesign, because there wouldn’t have been an opening for it to succeed. If InDesign does eventually topple QuarkXPress, or even establish itself as a peer with significant market share, Quark will have no one to blame but itself.


But more than Adobe, the company Quark could have learned the most from is Microsoft. Microsoft is unquestionably the most competitive company in the world. During the antitrust unpleasantness, I often saw comparisons between Microsoft and the old AT&T monopoly, with complaints along the lines of “lack of competition has lead to a stagnant industry”. But those comparisons never made much sense — the computer industry has not been stagnant under Microsoft’s rule. Dominated and steered in undesirable directions, yes — but not stagnant.


AT&T built a telephone monopoly and then sat on it, competing with no one.
Microsoft, on the other hand, has never stopped competing. After killing
competing products and companies, *it competes with older versions of
its own products*. WordPerfect and Lotus 123 are no longer serious
competition for Office; but old versions of Word and Excel are. Mac OS and
Linux aren’t Windows XP’s main competition; Windows 98 and 2000 are.


(That’s not to say I don’t believe Microsoft used its monopoly position illegally. [Plainly](http://usvms.gpo.gov/ms-findings2.html), they did. I’m only saying that it was never accurate to describe Microsoft as “uncompetitive”.)


Quark’s problem is that large numbers of its users aren’t upgrading. Many places still run version 3.32, which came out in 1996. I know many designers who use version 4 (myself included), but I don’t personally know anyone using version 5. The main reason is that after establishing dominance in the page layout market, Quark tried to expand XPress’s reach into other markets, namely web design. Spreadsheet features sell new copies of Excel; page layout features sell InDesign, and could have sold new versions of QuarkXPress.


The message Quark has been trying to sell is “The new version of XPress does new things in addition to page layout.” What they should have been selling is “The new version does page layout better.”


## Where Microsoft Doesn’t Compete


Microsoft simply wants your money for their software. They don’t care if your last purchase was from them or their competitor, they’re only concerned about your *next* purchase, and the one after that. Except, that is, for one very notable product, which they give away for free.


Internet Explorer.


In the beginning, of course, Microsoft was extremely competitive with Internet Explorer, free or not. The company had decided that Netscape was a threat, and the rest is history. But remember: the first versions of Internet Explorer, on both Windows and Mac, stunk. Netscape’s browser was faster and less crashy. In just a few years, however, Internet Explorer was both a superior application *and* had an operating system monopoly behind it.


But now what? Internet Explorer’s purpose was to dominate the browser market, not to generate revenue. Once it achieved dominance, many declared the browser market dead — which wasn’t a bad guess, given Microsoft’s history in other markets. But the difference with Internet Explorer is that Microsoft seems to have lost interest, and progress on the app has slowed tremendously. The reason is that unlike its for-pay software, Microsoft doesn’t have much of an interest in whether you’re using an older version of IE, or the latest release.


And so the demise of the browser market has been greatly exaggerated. It is in fact resurgent, with more competition now than in 1996. That’s not to say any browser is in a position to knock Internet Explorer for Windows away from at least, say, an 80-percent market share, but who’s in that 80 percent? A large part of IE’s market share consists of people who just don’t care, *or don’t even know,* which web browser they’re using. No one (with the possible exception of AOL) can compete with Microsoft for that “don’t know/don’t care” market. But amongst the rest of us, IE is faring poorly, on the Mac and Windows. (E.g., how does anyone live without pop-up blocking?)


Superior options to IE abound. On Mac OS X, there are [Camino](http://www.mozilla.org/projects/camino/) and [Safari](http://www.apple.com/safari/).


Even on Windows, where IE will surely remain the default bundled browser, serious competition exists. Opera is fast and fairly inexpensive. And then there’s Phoenix, the leaner and meaner nothing-even-resembling-a-kitchen-sink successor to Mozilla. (There’s even an [unofficial Mac version of Phoenix](http://www.kmgerish.com/misc.html), if you’re curious. While nowhere near as nice a Mac app as Camino, Phoenix is clearly a very nice browser for Windows.)


But the big news from last week is OmniWeb 4.5, available now as a [pre-beta “sneakypeek” release](http://www.omnigroup.com/ftp/pub/software/MacOSX/.sneakypeek/), which has switched from Omni’s own custom rendering engine to [Apple’s WebCore](http://www.mozillazine.org/weblogs/hyatt/WebCore/), the [KHTML](http://developer.kde.org/documentation/library/kdeqt/kde3arch/khtml/)-derived rendering library at the heart of Safari. Humble “.5” version number notwithstanding, this is a huge move for The Omni Group.


Omni’s old rendering library did OK with old-style web pages, laid out with tables and with type specified in `<font>` tags.  But its handling of CSS is, well, piss-poor. Switching to WebCore means dropping their own code — code they’d been building ever since OmniWeb started life on NeXT, years before Mac OS X. (OmniWeb’s copyright date is 1994.) It’s hard to drop your own code, but this is clearly the right move for The Omni Group.


## Where Browsers Get Sticky


There are two very different aspects to programming a web browser — the application, and the HTML rendering engine. The OmniWeb *application* has always been admirable; it was the *rendering engine* that was a clunker. Switching to WebCore lets Omni focus their efforts where they were already strong. Instead of fighting two fronts — the browser app and the renderer — now they only need to fight one, and it’s the one where they were already doing well.


A comparison between OmniWeb and Safari shows just how different two applications using the same library can be. Web pages look nearly the same in both browsers, but the browsers themselves look and feel very different indeed.


Omni’s switch to WebCore is also remarkable in that they’re using it today. No less an authority than [Dave Hyatt has recommended that third party developers wait](http://www.mozillazine.org/weblogs/hyatt/archives/2003_01.html#001733) until the full Safari SDK is released before attempting to use the WebCore rendering engine. The SDK, however, isn’t slated to ship until later this year. Given Omni’s cadre of experienced Cocoa (nee NextStep) developers, it’s not shocking that they’re the only developers so far to pull this off, but it’s certainly a pleasant surprise.


What further makes this exciting is that it’s relatively easy to switch from one web browser to another. The only data you need to move are your bookmarks, and most browsers import and export bookmarks as HTML files. Plug-ins are in a standard format and can be used in any browser. Where browsers are stickiest is in how they render web pages. So long as a new browser does a good job rendering all the sites you visit, it’s easy for you to switch to that browser.


When Internet Explorer ascended to dominance, the fear was that web developers would in turn create sites using proprietary Microsoft widgets which only worked in IE, forever cementing IE as the only usable browser. This never happened, fortunately. Sure, *some* sites are locked into proprietary IE technologies, but they’re a minority. Web standards are *gaining* in popularity, not falling. Score one for common sense.


Of course, doing a good job rendering most web sites — even ones which don’t use proprietary Microsoft technologies — is an inordinately complicated programming task. That’s why there are more successful browser applications than there are successful rendering libraries (e.g., Mozilla, Camino, and Phoenix all use the Gecko rendering library). Custom rendering engines tend to fall hopelessly behind (e.g. [iCab](http://www.icab.de/), and prior to this week, OmniWeb).


With a capable rendering engine in place, it’s relatively easy to get users to switch to a new browser — or at the very least to give it a try. That’s not to say a web browser’s human interface doesn’t generate a bit of stickiness. Users get accustomed to features like tabbed-browsing, or the ability to Shift-Command-click to open links into new windows behind the current one. But there’s also room for flexibility and creativity. Bookmark management, for example, differs greatly between the major Mac OS X browsers.


I can’t think of any other major application category where
popularity can rise and fall as quickly as web browsers. Whereas it might take InDesign 10 years to topple Quark, the two most
popular Mac browsers amongst Daring Fireball readers are Safari and Camino,
neither of which even existed a year ago. And if the current sneakypeek releases
are any indication, version 4.5 could catapult OmniWeb all the way from
“also-ran” to the top three. It’s that good an application (and
WebCore/KHTML is that good a rendering library).



| **Previous:** | [The Sticky Business of Page Layout](https://daringfireball.net/2003/04/the_sticky_business_of_page_layout) |
| **Next:** | [Command Line Fun](https://daringfireball.net/2003/04/command_line_fun) |


PreviousNext