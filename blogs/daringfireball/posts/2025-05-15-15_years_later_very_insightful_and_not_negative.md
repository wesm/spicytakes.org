---
title: "15 Years Later: ‘Very Insightful and Not Negative’"
date: 2025-05-15
url: https://daringfireball.net/2025/05/15_years_later_very_insightful_and_not_negative
slug: 15_years_later_very_insightful_and_not_negative
word_count: 1520
---


Earlier this week Nilay Patel was working on the show notes for [the episode of Decoder I guested on](https://www.theverge.com/decoder-podcast-with-nilay-patel/664802/apple-app-store-iphone-ios-fortnite-epic-games-lawsuit), and he texted me to ask if I could recall the time Steve Jobs sent some random developer a link to an article I wrote about the App Store. He wanted to cite it as an example of Daring Fireball being read, at high levels inside Apple, for a long time. I recalled the whole thing vaguely, as a “holy shit” moment, but not specifically. I hadn’t thought about it in years. But I was sure I could find it in the DF archives.


Turns out, I couldn’t find it, because, it turns out, in a fit of inexplicable modesty and humility, *I never linked to it*. (From [a TechCrunch interview I did at the time](https://techcrunch.com/2010/04/12/gruber-apple-was-right-adobe-get-over-it-video/), after the saga went somewhat viral: “When asked for his response to Steve’s shout-out, Gruber meekly grinned and said, ‘I just smiled.’”)


Here’s the rough timeline of events. On Thursday 8 April 2010, Apple updated the App Store guidelines to ban the use of Adobe’s then-new Flash-to-iPhone compiler. [From my post on the change](https://daringfireball.net/2010/04/iphone_agreement_bans_flash_compiler) (which, to some degree, broke the news):


> Prior to today’s release of the iPhone OS 4 SDK, section 3.3.1 of
> the iPhone Developer Program License Agreement read, in its
> entirety:
> 3.3.1 — Applications may only use Documented APIs in the manner
>     prescribed by Apple and must not use or call any private
>     APIs.
> In the new version of the iPhone Developer Program License
> Agreement released by Apple today (and which developers must agree
> to before downloading the 4.0 SDK beta), section 3.3.1 now reads:
> 3.3.1 — Applications may only use Documented APIs in the manner
>     prescribed by Apple and must not use or call any private
>     APIs. Applications must be originally written in Objective-C,
>     C, C++, or JavaScript as executed by the iPhone OS WebKit
>     engine, and only code written in C, C++, and Objective-C may
>     compile and directly link against the Documented APIs (e.g.,
>     Applications that link to Documented APIs through an
>     intermediary translation or compatibility layer or tool are
>     prohibited).
> My reading of this new language is that cross-compilers, such as
> the [Flash-to-iPhone compiler](http://labs.adobe.com/technologies/flashcs5/appsfor_iphone/) in Adobe’s upcoming Flash
> Professional CS5 release, are prohibited. This also bans apps
> compiled using [MonoTouch](http://monotouch.net/) — a tool that compiles C# and .NET
> apps to the iPhone.


This was *enormously* controversial at the time, but I also thought largely misunderstood by developers. Later that same day, I published another piece articulating my take on Apple’s reasoning for the change, “[Why Apple Changed Section 3.3.1](https://daringfireball.net/2010/04/why_apple_changed_section_331)”. From that article:


> We’re still in the early days of the transition from the PC era to
> the mobile era. Right now, Apple is winning. There are other
> winners right now too — RIM is still growing, and Android has
> grown a ton in the past year.
> The App Store platform could turn into a long-term de facto
> standard platform. That’s how Microsoft became Microsoft. At a
> certain point developers wrote apps for Windows because so many
> users were on Windows and users bought Windows PCs because all the
> software was being written for Windows. That’s the sort of
> situation that creates a license to print money.


That seems prescient. (The “license to print money” part — not the “RIM is still growing” part.)


> So what Apple does not want is for some other company to establish
> a de facto standard software platform *on top* of Cocoa Touch. Not
> Adobe’s Flash. Not .NET (through MonoTouch). If that were to
> happen, there’s no lock-in advantage. If, say, a mobile Flash
> software platform — which encompassed multiple lower-level
> platforms, running on iPhone, Android, Windows Phone 7, and
> BlackBerry — were established, that app market would not give
> people a reason to prefer the iPhone.
> And, obviously, such a meta-platform would be out of Apple’s
> control. Consider a world where some other company’s
> cross-platform toolkit proved wildly popular. Then Apple releases
> major new features to iPhone OS, and that other company’s toolkit
> is slow to adopt them. At that point, it’s the *other* company
> that controls when third-party apps can make use of these
> features.
> So from Apple’s perspective, changing the iPhone Developer Program
> License Agreement to prohibit the use of things like Flash CS5 and
> MonoTouch to create iPhone apps makes complete sense. I’m not
> saying you have to like this. I’m not arguing that it’s anything
> other than ruthless competitiveness. I’m not arguing (up to this
> point) that it benefits anyone other than Apple itself. I’m just
> arguing that it makes sense from Apple’s perspective — and it was
> Apple’s decision to make.


Two days later, on 10 April 2010, developer Greg Slepak emailed Steve Jobs to complain about the decision, citing negative sentiment on Hacker News (much has changed since 2010, but some things have not), writing:


> Hi Steve,
> Lots of people are pissed off at Apple’s mandate that applications
> be “originally written” in C/C++/Objective-C. If you go, for
> example, to the Hacker News homepage right now:
> [http://news.ycombinator.com/](http://news.ycombinator.com/)
> You’ll see that most of the front page stories about this new
> restriction, with #1 being: “[Steve Jobs Has Just Gone Mad](http://whydoeseverythingsuck.com/2010/04/steve-jobs-has-just-gone-mad.html)” with
> (currently) 243 upvotes. The top 5 stories are all negative
> reactions to the TOS, and there are several others below them as
> well. Not a single positive reaction, even from John Gruber, your
> biggest fan.
> I love your product, but your SDK TOS are growing on it like an
> invisible cancer.
> Sincerely,


Jobs wrote back to Slepak (starting a brief exchange of emails):


> We think John Gruber’s post is very insightful and not negative:
> [http://daringfireball.net/2010/04/why_apple_changed_section_331](http://daringfireball.net/2010/04/why_apple_changed_section_331)
> Steve


[Slepak posted the exchange to his blog](https://www.taoeffect.com/blog/2010/04/steve-jobs-response-on-section-3-3-1/), Tao Effect, and, well, as Jobs himself might have said, “Boom.” (This was [a not infrequent thing](https://www.macstories.net/news/steve-jobs-what-have-you-done-thats-so-great/) at the time, where random users or developers would email Jobs, he’d write back with something pithy, and they’d post the exchange. It was kind of crazy — the most famous CEO in the world, just doing customer service email — and his emails were always sharp.)


So, what would *you* do if Steve Jobs was quoted in a viral blog post saying, “We think «*Your Name Here*»’s post is very insightful and not negative”? I decided to just sit there with a smug look on my face for a few days (which, arguably, isn’t all that different from what I do most days) and pretend that it was no big deal. I didn’t link to it or mention it on Daring Fireball, and as far as I can tell, [I didn’t even tweet it](https://x.com/search?q=%22not%20negative%22%20(from%3Agruber)&src=typed_query). As best I can recall, I thought I should just play it cool. I mean of course my article about why Apple changed Section 3.3.1 was right. Why brag? Given that Steve Jobs was reading Daring Fireball, I didn’t want him to read a post from me acting like it was a big deal that he’d recommended a piece I wrote and agreed with it.


That was pretty stupid on my part. Or at least silly. My older perspective, today, is not to overthink such things. If something cool happens, I link to it. It seems ridiculous in hindsight that I didn’t link to Slepak’s post. And, I was thinking this week, if *I* couldn’t find a link to the overall story because *I* wrongly presumed I must have linked to it at the time, I wondered how many other readers, over the years, have gone hunting for that “very insightful and not negative” story and couldn’t find it because it was never mentioned or linked to on Daring Fireball.


So, today, I wrote the post I should have written back then, and [backdated it to 11 April 2010](https://daringfireball.net/linked/2010/04/11/very-insightful-and-not-negative).


To complete the timeline, April 2010 was a busy month. That same month saw [HP buy Palm](https://techcrunch.com/2010/04/28/hp-palm-deal-webos/) (in a last-ditch effort to remain relevant as the industry rapidly shifted from being PC-centric to mobile-centric), [Apple acquire a company called “Siri”](https://daringfireball.net/linked/2010/04/28/siri), and [Gizmodo publish details on the iPhone 4 prototype](https://daringfireball.net/linked/2010/04/28/slate-iphone) some poor Apple engineer accidentally left in a bar. [The original iPad](https://daringfireball.net/2010/04/the_ipad) had [just shipped](https://web.archive.org/web/20100404043324/http://www.time.com/time/business/article/0,8599,1976935,00.html). And at the end of the month, Jobs published “[Thoughts on Flash](https://daringfireball.net/linked/2010/04/29/jobs-thoughts-on-flash)” on the Apple.com homepage. It’s kind of wild that was all in one month — scrolling down [the monthly archive page for April 2010](https://daringfireball.net/linked/2010/04/) is just [one gem](https://daringfireball.net/linked/2010/04/30/cabin-fever) after [another](https://daringfireball.net/linked/2010/04/30/thoughts-on-horses).


Re-reading “[Thoughts on Flash](https://web.archive.org/web/20100722001052/http://www.apple.com/hotnews/thoughts-on-flash/)” again now, for the umpteenth time, I’ll say this: I think Steve Jobs’s post was very insightful and not negative.



| **Previous:** | [That EU App Store Warning About External Purchases Is Not New, and Apple Proposed Improving It Nine Months Ago](https://daringfireball.net/2025/05/that_eu_app_store_warning_about_external_purchases_is_not_new) |
| **Next:** | [More Insight and Not-Negativity](https://daringfireball.net/2025/05/more_insight_and_not-negativity) |


PreviousNext