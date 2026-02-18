---
title: "This Apple-HTC Patent Thing"
date: 2010-03-03
url: https://daringfireball.net/2010/03/this_apple_htc_patent_thing
slug: this_apple_htc_patent_thing
word_count: 3138
---


There are two aspects surrounding Apple’s patent litigation against HTC that demand further consideration. First, the severe problems with the U.S. patent system as a whole, particularly with regard to software patents. Second, the strategic implications of Apple’s decision to file suit.


Smart writers with first-hand experience with software patents have written much over the past few years on the system itself. Tim Bray, in particular, [has written extensively](http://www.google.com/search?q=patents+site%3Atbray.org) on them, including his own experience obtaining them. I’ll quote here from [one of his early pieces on the subject](http://www.tbray.org/ongoing/When/200x/2003/09/15/SWPatents):


> **Are Software Patents a Broken Idea?** — I really don’t know. One of
> my brothers, an Industrial Designer, has his name on a patent for
> a device for mixing gases that’s used in chromatographs. When he
> showed me the filing, with the drawings and schematics and so on,
> I was impressed; these guys had cooked up a new arrangement of
> valves and geometries that did a practical task in an elegant and
> new way. It felt much more rigorous than the way we go about
> inventing new technology in the software space; but maybe that’s
> just because I’m way too close to the software world and can see
> all the warts on its underbelly.
> I’m inclined to think there’s a spectrum of reasonability in
> software patents. “One-click ordering” seems like a grievous
> error, simply because if you said those three words to any
> web-savvy ecommerce-savvy programmer, they’d say “OK” and build it
> for you and it would work; which doesn’t seem to meet a high
> enough bar to qualify as an invention. But consider the basic PGP
> setup by Phil Zimmerman, it’s just immensely clever and elegant. I
> have the feeling that that really does qualify as an invention in
> totally the same sense as my brother’s gas-mixing apparatus.
> Obviously I think the things I filed are closer to PGP than
> one-click ordering.


In a later follow-up, [Bray wrote](http://www.tbray.org/ongoing/When/200x/2004/10/12/PatentTheory):


> Does this mean that I’ve concluded that software patents are
> just fine, thank you, and the current rat’s-nest of litigation
> is good business practice?
> No; while I generally agree with [Jonathan](http://blogs.sun.com/roller/page/jonathan/20040930#i_believe_in_ip) that the
> software-patent idea is not inherently broken (and thus disagree
> with [Richard Stallman](http://www.cl.cam.ac.uk/~mgk25/stallman-patents.html)), the fact is that it’s almost
> impossible for rational people to have a rational discussion
> about software patents. The reason is the insanely-dysfunctional
> behavior of the US Patent and Trademark Office, whose idiotic
> willingness to [grant patents on anything without regard for
> prior art or the obviousness test](http://www.tbray.org/ongoing/When/200x/2004/08/05/LinuxPatents) has totally poisoned the
> waters of this discussion. The result, as I’ve argued before, is
> that the net effect of the software-patent system is to serve as
> a parasitic tax by lawyers on businesspeople.
> Where I disagree with Jonathan is on what’s known as
> “business-method” patents: one-click ordering, per-employee
> pricing. I’m having trouble seeing the benefit to society in
> granting patents on something that could never possibly be done
> secretly. I also think that to get a patent, an invention should
> include innovation *both in conception and implementation*.


The emphasis in the last sentence quoted above is mine. I’ve quoted extensively here from Bray because, having re-read his patent-related essays, I find myself in nearly complete agreement with him. I’m not opposed to the idea of the patent system on general principle (as Stallman and many others are). And I think in many fields, the system has worked and continues to work well.


But for software the system, in practice, is undeniably broken. There’s an argument to be made that software is inherently different than other fields of invention, different in such a way that patents should not apply — or, should apply for a significantly shorter period of time before expiring. You can’t (or at least shouldn’t) be able to patent mathematics, and there are good arguments that programming is a branch of mathematics. But because software patents *are* granted, concede at least for the moment that certain kinds of software innovations *ought* to be patentable. Even with that in mind, clearly the U.S. Patent Office is and has granted patents for things which ought not be patentable. Not just silly frivolous things, but patents that have been granted for *concepts* alone, rather than specific innovative *implementations* of said concepts. Ideas in the abstract, rather than implementations of ideas.


Just a few weeks ago, Bray published “[Giving Up on Patents](http://www.tbray.org/ongoing/When/201x/2010/02/22/Patent-Fail)”:


> Not so many years ago, even as I was filled with [fear and loathing](http://www.tbray.org/ongoing/When/200x/2004/08/05/LinuxPatents)
> of the hideous misconduct of the US Patent & Trademark Office, I
> retained some respect for the notion of patents. I even wrote what
> I think is an unusually easy-to-read introduction to [Patent
> Theory](http://www.tbray.org/ongoing/When/200x/2004/10/12/PatentTheory).
> But no more. The whole thing is too broken to be fixed. Maybe it
> worked once, but it doesn’t any more. The patent system needs to
> be torn down and thrown out.


Paul Graham, who has also been awarded software patents, [has written well on the subject](http://www.paulgraham.com/softwarepatents.html), too:


> We, as hackers, know the USPTO is letting people patent the knives
> and forks of our world. The problem is, the USPTO are not hackers.
> They’re probably good at judging new inventions for casting steel
> or grinding lenses, but they don’t understand software yet.


And:


> There’s nothing special about physical embodiments of control
> systems that should make them patentable, and the software
> equivalent not.
> Unfortunately, patent law is inconsistent on this point. Patent
> law in most countries says that algorithms aren’t patentable.
> This rule is left over from a time when “algorithm” meant
> something like the Sieve of Eratosthenes. In 1800, people could
> not see as readily as we can that a great many patents on
> mechanical objects were really patents on the algorithms they
> embodied.
> Patent lawyers still have to pretend that’s what they’re doing
> when they patent algorithms. You must not use the word
> “algorithm” in the title of a patent application, just as you
> must not use the word “essays” in the title of a book. If you
> want to patent an algorithm, you have to frame it as a computer
> system executing that algorithm. Then it’s mechanical; phew. The
> default euphemism for algorithm is “system and method.” Try a
> patent search for that phrase and see how many results you get.


These arcane rules lead to patents being described in an obfuscated manner. That they are patenting algorithms but must pretend they’re patenting something else is the definition of a broken system.


To me, “user interface” patents are hand-in-hand with “[business method patents](http://en.wikipedia.org/wiki/Business_method_patent)” as examples of things which, no matter how innovative or original, ought not be patentable. They’re idea patents.


Adobe, to take one example, has a patent on [tabbed palettes](http://eupat.ffii.org/patents/samples/ep689133/index.en.html). If you’ve used Adobe apps like Photoshop, InDesign, or Illustrator in the past decade, you know what they are. Design applications have been using floating on-screen palettes all the way back to the original MacPaint in 1984. Unlike dialog boxes, they weren’t modal and “floated” over the document window. Unlike menus, they remained visible. They’re ubiquitous in design apps. One shortcoming, however, was that if you opened too many of them, you cluttered your screen — the more palettes you have open, the less room you have for displaying the document itself. Adobe came up with a great feature: they allowed you to dock multiple palettes together as tabs within a single palette window, and you could drag individual tabs between windows or drag them out into their own window. (Similar, at the palette level, to tabbed web browser windows.) Adobe patented the idea, and when Macromedia implemented a version of it, [Adobe sued](http://news.cnet.com/2100-1040-898061.html) (and won — a measly $2.8 million). To me, that’s exactly the sort of patent litigation that is aimed at stifling innovation rather than rewarding it. Building on the ideas of others is fundamental to competition.


No one company can or should be expected to change the entire U.S. patent system. Like any entrenched system with powerful entities who seek to maintain the status quo, we’re likely stuck with it. And so the way the computer industry has dealt with it is detente. Companies obtain as many patents as they can, written as broadly as they can get away with. And since everyone (where by “everyone” I mean all large tech corporations) has a large patent portfolio, and nearly every idea under the sun has been patented by someone to some degree, most of them are inert. Company A doesn’t sue Company B for infringing upon patents held by A because A’s own products almost certainly infringe upon some patents held by B.


This is why pure patent troll companies such as [Nathan Myhrvold’s Intellectual Ventures](http://techdirt.com/articles/20100217/1853298215.shtml) are so despised. They’re immune from the threat of counter-suit because they have no products or services. Their only business is extorting patent licensing fees.


The analogy to nuclear weapons is overwrought when considered literally, but in terms of strategy it’s quite apt. [Paul Graham, on Amazon’s notorious “one-click” patent](http://www.paulgraham.com/softwarepatents.html):


> Where Amazon went over to the dark side was not in applying for
> the patent, but in enforcing it. A lot of companies (Microsoft,
> for example) have been granted large numbers of preposterously
> over-broad patents, but they keep them mainly for defensive
> purposes. Like nuclear weapons, the main role of big companies’
> patent portfolios is to threaten anyone who attacks them with a
> counter-suit. Amazon’s suit against Barnes & Noble was thus the
> equivalent of a nuclear first strike.
> That suit probably hurt Amazon more than it helped them. Barnes &
> Noble was a lame site; Amazon would have crushed them anyway. To
> attack a rival they could have ignored, Amazon put a lasting black
> mark on their own reputation. Even now I think if you asked
> hackers to free-associate about Amazon, the one-click patent would
> turn up in the first ten topics.


Which brings us to Apple and HTC. Regardless of the merits of all 20 of the patents Apple accuses HTC of violating, strategy-wise the comparison to Amazon and Barnes and Noble seems apt: Apple has the clearly superior product and is winning handily in the marketplace. Whatever benefit in the market Apple hopes to achieve by this suit to me seems likely to be worth far less than the loss of good will and prestige Apple will suffer if they vigorously pursue this case (let alone if they initiate more such suits).


[Wil Shipley, in an open letter to Steve Jobs regarding the HTC litigation](http://wilshipley.com/blog/2010/03/open-letter-to-steve-jobs-concerning.html):


> You’ve famously taken and built on ideas from your competitors,
> as have I, as we should, as great artists do. Why is what HTC has
> done worse? Whether an idea was patented doesn’t change the
> morality of copying it, it only changes the ability to sue. […]
> If Apple becomes a company that uses its might to quash
> competition instead of using its brains, it’s going to find the
> brainiest people will slowly stop working there. You know this,
> you watched it happen at Microsoft.


Copying ideas is how progress is made. It’s copying implementations that is wrong (and illegal). Admittedly there are gray areas, and reasonable people can disagree about whether some specific instances cross that line. But HTC’s phones are not copies of the iPhone. The Nexus One is without question highly influenced by the iPhone, both in terms of physical form factor and the Android software from Google. But it is also without question not a clone.


My favorite theory thus far regarding why Apple is suing HTC is expressed entirely in [this tweet from John Siracusa](http://twitter.com/siracusa/status/9884001169):


> To me, the Apple patent suit smells like nothing more than a
> manifestation of Jobs’s own sense of injustice.


I.e., Jobs is *offended* by HTC’s products, not worried about them. I can understand the indignation, or at least imagine that I can.


Apple’s press releases tend to be remarkably terse and plainspoken, at least by the standards of modern corporate communication. And when Jobs is quoted in them, the words are carefully chosen and meaningful, worthy of being carefully parsed1 — not at all like the bromides attributed to CEOs from most companies in most PRs. [The PR announcing these suits against HTC is no exception](http://www.apple.com/pr/library/2010/03/02patents.html):


> “We can sit by and watch competitors steal our patented
> inventions, or we can do something about it. We’ve decided to do
> something about it,” said Steve Jobs, Apple’s CEO. “We think
> competition is healthy, but competitors should create their own
> original technology, not steal ours.”


That’s not the language of a licensing dispute or the beginning of a polite negotiation. That’s the language of a man aggrieved.


During Jobs’s iPhone introduction keynote address in January 2007, before showing what the iPhone looked like, Jobs put up this slide showing four of the then-leading smartphones on the market: the Motorola Q, a BlackBerry, a Palm Treo, and the Nokia E62.


Those pre-iPhone smartphones Jobs displayed all shared the same fundamental design: half-screen, half keyboard, and an up/down/left/right navigation controller. Now [look at this prototype Android phone](http://gizmodo.com/gadgets/android-hardware-in-the-wild/google-android-prototype-in-the-wild-334909.php) Gizmodo spotted in December 2007 — 11 months after the iPhone introduction. Android was conceived of that same old model — the prototype Gizmodo found in December 2007 would have fit perfectly alongside the other four phones in Jobs’s keynote slide.


The gaping chasm between that Treo-ish/BlackBerry-ish prototype Android device and the [HTC G1](http://www.htc.com/www/product/g1/overview.html) that went on sale a year later (let alone the Nexus One today) was bridged by ideas from the iPhone.


The iPhone introduced a new model. A true great leap forward in the state of the art. Not a small screen that shows you things which you manipulate indirectly using buttons and trackballs occupying half the device’s surface area, but instead a touchscreen that occupies almost the entirety of the surface area, showing things you manipulate directly.


Android is a far better platform today than it would have been if Apple had never created the iPhone. That, in some sense, is not fair.


I think Siracusa is exactly right that Jobs has a particularly acute sensitivity to this sort of unfairness. This litigation, perhaps then, isn’t about particular specific patented components, but rather is about the big idea, the general gist and grand ambition of the iPhone as the basic model for how modern mobile devices should be designed and work.


No doubt some of you are nodding your heads and see this as justification for Apple’s suit. But life isn’t fair. Great ideas make the world better. Apple can rightly expect to benefit greatly from the ideas embodied by the iPhone, but they can’t expect to reap *all* of the benefits from those ideas.


That’s the nature of implementing insanely great ideas. The bar has been raised, and, yes, Apple did most of the lifting. That’s how it goes.


[Paul Graham, yesterday](http://news.ycombinator.com/item?id=1161807):


> If this had happened a day earlier I don’t think I would have
> posted that RFS. Apple is inching ever closer to evil, and I worry
> that there’s no one within the company who can stand up to Jobs
> and tell him so.


“That RFS” is the [request for iPad software startups](http://ycombinator.com/rfs6.html) from Graham’s Y Combinator, and lest you think “evil” is too overwrought a word, Graham clarified [later in the same thread](http://news.ycombinator.com/item?id=1161946):


> Historically the word “evil” has had a pretty broad meaning. Among
> tech companies the word has a new and fairly specific sense that
> follows from Paul Buchheit’s slogan “Don’t be evil.” That’s the
> sense I was using. It has a pretty low bar. It means, roughly,
> winning by taking advantage of people instead of by doing good
> work.


I wouldn’t use the word *evil* this way, but I’m right there with Graham on this sentiment. And I say this not in any sort of hippy-dippy sense of expecting or even hoping for Apple to behave selflessly, holding them to a separate idealistic standard, or expecting them to fight with one arm tied behind their corporate back. And only a fool would argue that a company should never seek redress through litigation.


But I believe that it’s good business, in the long run, for a company’s acts of aggression to take place in the market, not in the courts. My concern regarding this litigation against HTC is that it looks like an act of competitive aggression, not defense.


I can think of only a few optimistic angles for this suit. One is that perhaps it’s a by-product of the suit Apple is engaged in against (and initiated by) Nokia. Apple’s counter-suit against Nokia involves some of the same patents at play here, and perhaps Apple’s lawyers have concluded that they need to enforce them against someone like HTC in order to use them in their counter-suit against Nokia. Or, perhaps one or more of the truly technical patents Apple has cited against HTC are genuine instances of intellectual property theft, the specific nature of which is unclear from the opaque language of the patent filings, and the rest of the cited patent violations were tacked on as part of a legal strategy along the lines of “*If you’re going to punch them, punch them as hard as you can*”. I.e. that they’ve filed suit as widely as they can, but have specific narrow violations in mind.


What worries me is the idea that Apple, or even just Steve Jobs, believes that phones like the Nexus One have no right to exist, period, and that patent litigation to keep them off the market is in the company’s interests. I say it’s worrisome not because I think it’s evil, or foolish, or unreasonable, but because it is unwise, shortsighted, and unnecessary.


---

1. For example, consider the timing of [this PR Apple released early in the morning on January 5](http://daringfireball.net/linked/2010/01/05/app-store-3b), announcing the three-billionth download from the App Store. Jobs is quoted thus: “The revolutionary App Store offers iPhone and iPod touch users an experience unlike anything else available on other mobile devices, and we see no signs of the competition catching up anytime soon.”
January 5 was the day Google held its event to unveil the Nexus One. ↩︎



| **Previous:** | [Assorted Brief Observations and Thoughts Regarding Windows Phone 7](https://daringfireball.net/2010/03/thoughts_regarding_windows_phone_7) |
| **Next:** | [A Thought Regarding the Old Apple-v.-Microsoft ‘Look and Feel’ Lawsuit](https://daringfireball.net/2010/03/regarding_old_apple_microsoft_suit) |


PreviousNext