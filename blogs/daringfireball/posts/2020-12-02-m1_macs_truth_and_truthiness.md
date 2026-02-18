---
title: "M1 Macs: Truth and Truthiness"
date: 2020-12-02
url: https://daringfireball.net/2020/12/m1_macs_truth_and_truthiness
slug: m1_macs_truth_and_truthiness
word_count: 2875
---


We knew this to be true: Computers could run fast and hot, or slow and cool. For laptops in particular, the best you could hope for is a middle ground: fast enough and cool enough. But if you wanted a machine that ran really fast, it wasn’t going to run cool (and wasn’t going to last long on battery), and if you wanted a computer that ran cool (and lasted long on battery), it wasn’t going to be fast.


We knew this to be true because that was the way things were. But now, with the M1 Macs, it’s not. M1 Macs run very fast and do so while remaining very cool and lasting mind-bogglingly long on battery. It was a fundamental trade-off inherent to PC computing, and now we don’t have to make it.


We should have known better, because iPhones and iPads run fast and cool, but, they’re *different*. Right? They’re over *there*, running iOS, while Macs and other PCs are over *here*, running MacOS and Windows. But they’re not really different. They’re all just computers. And the best aspects of those computers — running fast and cool — obviously ought to be true for all computers.


M1 Macs embarrass all other PCs — all Intel-based Macs, including automobile-priced Mac Pros, and every single machine running Windows or Linux. Those machines are just standing around in their underwear now because the M1 stole all their pants. *Well, that just doesn’t happen,* your instincts tell you. One company, even a company like Apple, doesn’t just embarrass the entire rest of a highly-competitive longstanding industry. But just because something hasn’t happened — or hasn’t happened in a very long while — doesn’t mean it can’t happen. And in this case, it just happened.


Another long-held belief: emulating or translating apps compiled for a different architecture is necessarily going to be irritatingly slow and somewhat incompatible at best, and unusably slow and wildly incompatible as a general rule. But Apple’s [Rosetta 2 translation layer](https://developer.apple.com/documentation/apple_silicon/about_the_rosetta_translation_environment?language=objc) for running x86 software on Apple Silicon is a technical marvel. Remarkably compatible, and so fast that when combined with the pure speed of the M1 chips themselves, it actually runs Intel Mac software as fast or faster than on most actual Intel Mac hardware. It’s not like Intel apps running in Rosetta run OK, and native Apple Silicon apps run well; it’s more like Intel apps in Rosetta run well and Apple Silicon apps run even better. Yes, of course you want apps compiled to run natively, but most users running most apps — including some professional apps — won’t notice.


Those of us who’ve been paying attention aren’t surprised that the M1 Macs have overturned these assumptions about what tradeoffs are unavoidable in terms of performance per watt. And it shouldn’t be a surprise that Apple had a remarkably good translation solution ready to go (despite the fact that yours truly, [once again](https://daringfireball.net/2005/06/see_you_intel), wrongly [predicted otherwise](https://daringfireball.net/2020/06/on_apple_announcing_the_mac_arm_transition_at_wwdc#emulation)). It’s just a delight to see it finally come to fruition.


For the industry as a whole, though, the M1 Macs have dropped as a bit of a shock. One reason for this, I think, is that Apple’s silicon prowess in iOS devices has been a slow boil. iPhones and iPads are better computers — faster and more efficient — than their Android competitors. But it’s been an annual incremental game. And it’s hard to tell what’s attributable to iOS’s software efficiency vs. Android and what’s attributable to Apple’s silicon prowess vs. Qualcomm and Samsung and whoever else is making chips for Android devices.


M1 Macs completely upend what we can and should expect from PCs. It’s a breakthrough along the lines of the iPhone itself in 2007.


The adage is, “If it sounds too good to be true, it probably is.” Emphasis on *probably* — the M1 Macs are an exception. They really are that good. But, like the iPhone in 2007, there are people who refuse to believe it.


Exhibit A: Patrick Moorhead, whose review for Forbes — “[Apple MacBook Pro 13” M1 Review — Why You Might Want to Pass](https://www.forbes.com/sites/patrickmoorhead/2020/11/21/apple-macbook-pro-13-m1-reviewwhy-you-might-want-to-pass/)” — [took off](https://www.techmeme.com/201124/p3#a201124p3) when published last week.


Moorhead’s review bears little relation to the reality of the M1 Macs, but plays right into expectations of the status quo. *ARM chips are efficient and Apple’s ARM chips are the best, but none of them are a threat to Intel and AMD’s x86 chips for high-end performance. Emulation is slow and buggy and it will take years for a lot of important software to be updated to run natively.* None of that’s true in the M1 Macs’ case, but that’s the premise of Moorhead’s article.


And some folks bought it — some out of [reasonable skepticism](https://twitter.com/TonyRomm/status/1331247834298019844), and [some out of stupidity](https://twitter.com/thurrott/status/1330866325556768770).


Moorhead opens thus:


> I’ve read the first batch of Apple MacBook Pro 13″ M1 reviews
> and you’d be hard to find anything negative about the new
> laptop. At the worst, there were some complaints about the iOS
> app experience, but on the whole, early reviews, described the
> new MacBook Pro 13″ essentially as God’s gift to the notebook
> wanting masses.
> Don’t get me wrong, there were some very positive things about the
> new laptop. The new M1 processor is impressive, but far from
> perfect — it has many warts, that nearly nobody is discussing.


Not one of these purported “warts” with the M1 is ever mentioned. Whatever real problems Moorhead ran into (and some were indeed real), they’re all related to software issues. Either MacOS 11 Big Sur itself, or Rosetta, or apps he’s trying to use that have compatibility issues with MacOS 11 or Rosetta or both. But: software. Those issues are real, and the fact that M1 Macs require MacOS 11 Big Sur is the single biggest reason why some Mac users can’t or at least shouldn’t buy one just yet. Even if there were no architecture transition, in normal years it’s completely reasonable for many users to delay upgrading to major new releases of MacOS. I didn’t upgrade my old MacBook Pro to MacOS 10.15 Catalina until August of this year.


Here’s a terrific piece by Peter Steinberger — “[Apple Silicon M1: A Developer’s Perspective](https://steipete.com/posts/apple-silicon-m1-a-developer-perspective/)” — that goes into great detail about how amazing the M1 is but also how many essential developer tools aren’t compatible or fully compatible with MacOS 11 on Apple Silicon yet. [Steinberger’s conclusion](https://steipete.com/posts/apple-silicon-m1-a-developer-perspective/):


> The new M1 MacBooks are fast, beautiful and silent and the hype is
> absolutely justified. There’s still a lot to do on the
> software-front to catch up, and the bugs around older iOS
> Simulators are especially problematic.
> All of that can be fixed in software and the whole industry is
> currently working on making the experience better, so by next
> year, when Apple updates the 16-inch MacBook Pro and releases the
> next generation of their M chip line, it should be absolutely
> possible to use a M1 Mac as main dev machine.


Steinberger’s is a scrupulously fair conclusion. Perversely, developers, who by nature of their profession best understand exactly what an architecture transition like this entails, might be among the few professions who can’t yet move their primary computing to an Apple Silicon device by nature of the software tools they depend upon. (Some developers *can* move now, and — because Xcode running on the M1 compiles code so much faster than any Intel MacBook — are rejoicing.)


Moorhead, on the other hand, claims that it’s the M1 that has — again, his word — “warts”:


> I think the new MacBook Pro 13” M1 will likely be fine for
> users who use 100% Apple software, stay primarily in Safari and
> don’t need to connect it to a bunch of peripherals, and have a
> lot of money.


Is Chrome “100 percent Apple software”? Because Chrome runs better on the M1 than it does on any other Mac. Yes, Safari is faster and more energy efficient than Chrome, but Safari is faster than Chrome on Intel-based Macs as well. “And have a lot of money” — I have no idea what that even means other than being able to buy a Mac in the first place, which seems to me a given. But while the entry price for a MacBook Air remains $999, the effective usefulness of the new M1 $999 MacBook Air is *far* higher than that of the $999 Intel-based MacBook Air it replaced. The M1 is good news even for Mac users on a smaller budget.


> I wanted to provide some balance to those early reviews and
> discuss who I believe *shouldn’t* consider the new MacBook Pro 13”
> M1. I know that may sound *negative*, but I call it *balance*.
> I’ve used my unit for nearly five days and here is my assessment
> of whom I think should avoid it.


Stephen Colbert famously quipped at the 2006 White House Correspondents’ Dinner that “[reality has a well-known liberal bias.](https://en.wikiquote.org/wiki/Stephen_Colbert)” Well, the reality of the M1 has an Apple bias. There is no “*Well, here’s the downside*” with regard to the state of Apple Silicon versus the entire rest of the industry. Yes, the M1 is a consumer chip with consumer limits — two USB ports, a maximum of 16 GB of RAM — but that’s the nature of *these* Apple Silicon Mac models, not all Apple Silicon Mac models to come.


There is no balance, if by balance, you’re looking for a story that says any PC hardware, ARM or x86, is competitive in any way with the M1 Macs for low-energy computing. I’m reminded of another quote, from then-CEO Ed Colligan of then-company Palm in November 2006, [a few months ahead of the iPhone’s introduction](https://daringfireball.net/2006/11/colligan_head_stuck):


> Responding to questions from New York Times correspondent John
> Markoff at a Churchill Club breakfast gathering Thursday morning,
> Colligan laughed off the idea that any company — including the
> wildly popular Apple Computer — could easily win customers in the
> finicky smart-phone sector.
> “We’ve learned and struggled for a few years here figuring out how
> to make a decent phone,” he said. “PC guys are not going to just
> figure this out. They’re not going to just walk in.”


Patrick Moorhead’s M1 Mac review can be paraphrased as “*Intel and AMD have learned and struggled for a few years here figuring out how to make decent PC chips. Apple hasn’t just magically figured this out. They’re not going to just walk in.*”


The difference is, Colligan at least hadn’t seen the iPhone yet. Moorhead has an M1 MacBook Pro in his hands. He either should know better, or does know better and wrote this grossly misleading tripe anyway, knowing there was an Apple-skeptical audience willing to lap it up.


We’ve seen this before. In 2013, Apple announced the iPhone 5S with the A7 chip, the first 64-bit mobile CPU — years ahead of industry expectations. [Here’s what Moorhead said then](https://daringfireball.net/linked/2013/09/12/samsung-64):


> “Adding 64-bit processor capabilities adds nothing to the user
> experience today, as it would requires over four gigabytes of
> memory,” Patrick Moorhead of Moor Insights and Strategy, and a
> former executive at AMD, told AllThingsD. “Most phones today only
> have one to two gigabytes of memory, and it will be years before
> the norm is four.”


[That did not pan out well for Moorhead](https://www.anandtech.com/show/7335/the-iphone-5s-review/4).


In 2015, Apple shipped the first iPad Pro, with the A9X chip. 
Aaron Souppouris wrote a piece for Engadget headlined “[The iPad Pro’s Chip Is Not a Big Deal](https://www.engadget.com/2015-11-14-ipad-pro-a9x-chip.html)”. You will never guess who Souppouris’s expert source was:


> But what of the benchmark tests that show the iPad Pro
> outperforming Intel’s Core M processor, and even coming close to
> Intel’s MacBook Pro range? Don’t believe them. Patrick Moorhead, a
> highly respected analyst with a strong background in chips, urges
> caution, especially when it comes to comparing GeekBench numbers,
> as many have. “GeekBench is a synthetic, mobile benchmark,”
> Moorhead tells Engadget. “The benchmark code is more like mobile
> application code than it is desktop code.” Using GeekBench to test
> A9X versus Intel chips is “like comparing apples and oranges or an
> SUV with a sedan on the straight-away,” he explains. [...]
> Apple doesn’t have such a large legacy to support — it only moved
> to Intel chips nine years ago — but there would be no perceivable
> benefit to switching an existing x86 platform to ARM. “I do not
> believe ARM-based chips will be powering Macs in the next few
> years,” said Moorhead. “I do believe Apple will attempt to scale
> up the iPad Pro even further, which could potentially eat into
> Macbook [*sic*] sales.” [...]
> According to Moorhead, Intel came close to putting one of its
> chips inside the iPad Pro. “[The iPad Pro] business is open to
> both Apple’s own ARM-based AX chips and Intel,” he explained,
> “Intel is fighting hard to get that business and I believe almost
> had [the iPad Pro contract] with the new Skylake-based Core M had
> it been available earlier.”


So on the M1 Mac rave-review side, we have [every major professional reviewer](https://www.techmeme.com/201117/p18#a201117p18), along with [dozens and dozens of ordinary M1 Mac purchasers](https://www.singhkays.com/blog/apple-silicon-m1-black-magic/) out in the real world, doing real things, who just can’t believe what the M1 is capable of.


And on the other side, we have Patrick Moorhead, the guy who said Apple’s 64-bit A7 chip in the iPhone 5S was no big deal; that we shouldn’t have believed the benchmarks showing the original iPad Pro pantsing Intel’s chips five years ago; and that not only was Apple unlikely to switch the Mac away from Intel, but that Intel, in fact, was *this close* to getting its chips into the iPad Pro.


One of these sides deserves more skepticism than the other.


---


[Here’s an M1 MacBook Pro review I just loved, from Nadim Kobeissi](https://nadim.computer/posts/2020-11-26-macbookm1.html):


> At the risk of making this a very boring review, all I have to say
> is basically that all of the above is so far holding as true. This
> computer is nuts. Compiling tons of things in the background
> doesn’t slow down Safari web browsing, somehow. I haven’t had to
> plug it in once since I fully charged it up two days ago.
> Performance is so quiet and cool that I feel like my terminal
> compiling a bunch of things is actually an SSH into a much
> stronger workstation located somewhere else. I actually discovered
> that I’ve had an instinct of measuring my MacBook’s CPU usage by
> feeling the heat on the strip of aluminum right above the Touch
> Bar, and I can’t even do that anymore now. Because even if the M1
> MacBook Pro has been running at 100% on all cores for ten straight
> minutes, you’ll barely feel it getting warm.


Kobeissi is both technically scrupulous (and clearly knowledgeable) but also doesn’t hide his genuine enthusiasm. The M1 *is* exciting! Even I am using exclamation marks. And what a keen point Kobeissi makes about subconsciously equating a laptop working hard with physical manifestations — as heat you can feel and fan noise you can hear. It is, for now, utterly uncanny that when an M1 MacBook exerts itself computationally it neither gets warm nor makes any noise. Soon though, that will seem utterly normal, and it’ll be every other laptop in the world, the ones that do get hot and do make noise (or never go fast in the first place) that will seem wrong and weird.


Kobeissi also calls out this particular slide from Apple’s M1 keynote:


[
](https://daringfireball.net/misc/2020/12/m1-performance-vs-power-bezos-chart.png)


He writes:


> This graph is completely worthless. Honestly. Nobody knows to this
> day what Apple meant by “Latest PC laptop chip”, and both axes
> aren’t even numbered. It’s stupid that Apple still pulls this sort
> of thing off, and it immediately makes you question just how good
> the M1 is really supposed to be.


I get it. It’s a pure [Bezos chart](https://twitter.com/jsnell/status/481863414180896769). With no scale on either axis and a comparison against an unnamed competitor, there’s no way to verify that it’s true.


But I also get why Apple presented it this way, because while it’s not meaningful in any scientific sense, per se, it is very much an accurate illustration of the M1 vs. its competition overall. Is this a graph of exporting video? Or compiling code? Or running complex web applications in a browser? Or playing a game? *Yes*. That’s what this graph is trying to say: yes to all of it. The M1 is up *here*, running fast and cool, and all the competing chips from Intel, AMD, Qualcomm, Samsung, and whoever else are down *there*, running hot or running slow, looking around for their recently stolen pants.


To borrow another Colbert-ism, sometimes an assertion of [truthiness](http://www.cc.com/video-playlists/kw3fj0/the-opposition-with-jordan-klepper-welcome-to-the-opposition-w--jordan-klepper/63ite2) is actually true.



| **Previous:** | [The M1 Macs](https://daringfireball.net/2020/11/the_m1_macs) |
| **Next:** | [Heavy Is the Head That Wears the AirPods Max](https://daringfireball.net/2020/12/heavy_is_the_head_that_wears_the_airpods_max) |


PreviousNext