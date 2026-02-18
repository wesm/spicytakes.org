---
title: "Why Prusa is floundering, and how you can avoid their fate"
date: 2023-12-26
url: https://drewdevault.com/2023/12/26/2023-12-26-Prusa-is-floundering.html
slug: 2023-12-26-Prusa-is-floundering
word_count: 1524
---

Prusa is a 3D printer manufacturer which has a long history of being admired by
the 3D printing community for high quality, open source printers. They have been
struggling as of late, and came under criticism for making the firmware of their
Mk4 printer non-free. 1

[Armin Ronacher](https://lucumr.pocoo.org/2023/12/25/life-and-death-of-open-source/)  uses Prusa as a case-study in why open source companies
fail, and uses this example to underline his argument that open source needs to
adapt for commercial needs, namely by adding commercial exclusivity clauses to
its licenses – Armin is one of the principal proponents of the non-free
Functional Source License. Armin cites his experience with a Chinese
manufactured 3D printer as evidence that intellectual property is at the heart
of Prusa’s decline, and goes on to discuss how this dynamic applies to his own
work in developing a non-free license for use with Sentry. I find this work
pretty interesting – FSL is a novel entry into the non-free license compendium,
and it’s certainly a better way to do software than proprietary models, assuming
that it’s not characterized as free or open source. But, allow me to use the
same case study to draw different conclusions.

It is clear on the face of it that Prusa’s move to a non-free firmware is
unrelated to their struggles with the Chinese competition – their firmware was
GPL’d, and the cited competitor (Bambu) evidently respects copyleft, and there’s
no evidence that Bambu’s printers incorporate derivatives of Prusa’s firmware in
a manner which violates the GPL. Making the license non-free is immaterial to
the market dynamics between Prusa and Bambu, so the real explanation must lie
elsewhere.

If you had asked me 10 years ago what I expected Prusa’s largest risk would be,
I would have simply answered “China” and you would have probably said the same.
The Chinese economy and industrial base can outcompete Western manufacturing in
almost every manufacturing market. 2  This was always the obvious
vulnerability in their business model, and they  *absolutely*  needed to be
prepared for this situation, or their death was all but certain. Prusa made one
of the classic errors in open source business models: they made their product,
made it open source, sold it, and assumed that they were done working on their
business model.

It was inevitable that someday Chinese manufacturers would undercut Prusa on
manufacturing costs. Prusa responded to this certainty by not diversifying their
business model whatsoever. There has only ever been one Prusa product: their
latest 3D printer model. The Mk4 costs $1,200. You can buy the previous
generation (at $1,000), or the MINI (from 2019, $500). You can open your wallet
and get their high-end printers, which are neat but fail to address the one
thing that most users at this price-point really want, which is more build
volume. Or, you can buy an Ender 3 off Amazon right now for $180 and you’ll get
better than half of the value of an Mk4 at an 85% discount. You could also buy
Creality’s flagship model for a cool $800 and get a product which beats the Mk4
in every respect. China has joined the market, bringing with them all of the
competitive advantages their industrial base can bring to bear, and Prusa’s
naive strategy is causing their position to fall like a rock.

Someone new to 3D printing will pick up an Ender and will probably be happy with
it for 1-2 years. When they upgrade, will they upgrade to a Prusa or an Ender 5?
Three to five years a customer spends in someone else’s customer pipeline is an
incredibly expensive opportunity cost Prusa is missing out on. This opportunity
cost is the kind of arithmetic that would make loss leaders like a cheap,
low-end, low-or-negative-margin Prusa printer make financial sense. Hell, Prusa
should have made a separate product line of white-labeled Chinese entry-level 3D
printers just to get people on the Prusa brand.

Prusa left many stones unturned. Bambu’s cloud slicer is a massive lost
opportunity for Prusa. On-demand cloud printing services are another lost
opportunity. Prusa could have built a marketplace for models & parts and skimmed
a margin off of the top, but they waited until 2022 to launch Printables –
waiting until the 11th hour when everyone was fed up with Thingiverse. Imagine a
Prusa where it works out of the box, you can fire up a slicer in your browser
which auto-connects to your printer and prints models from a Prusa-operated
model repository, paying $10 for a premium model, $1 off the top goes to Prusa,
with the same saved payment details which ensure that a fresh spool of Prusa
filament arrives at your front door when it auto-detects that your printer is
almost out. The print you want is too big for your build volume? Click here to
have it cloud printed – do you want priority shipping for that? Your hot-end is
reaching the end of its life – as one of our valued business customers on our
premium support contract we would be happy to send you a temporary replacement
printer while yours is shipped in for service.

Prusa’s early foothold in the market was strong, and they were wise to execute
the way they did early on. But they  *absolutely*  had to diversify their lines of
business. Prusa left gaping holes in the market and utterly failed to capitalize
on any of them. Prusa could have been synonymous with 3D printing if they had
invested in the brand (though they probably needed a better name). I should be
able to walk into a Best Buy and pick up an entry-level Prusa for $250-$500, or
into a Home Depot and pick up a workshop model for $1000-$2000. I should be able
to bring it home, unbox it, scan a QR code to register it with PrusaConnect, and
have a Benchy printing in less than 10 minutes.

Chinese manufacturers did all of this and more, and they’re winning. They aren’t
just cheaper – they offer an outright better product. These are not cheap
knock-offs: if you want the best 3D printer today it’s going to be a Chinese
one, regardless of how much you want to spend, but, as it happens, you’re going
to spend less.

Note that none of this is material to the license of the product, be it free or
non-free. It’s about building a brand, developing a customer relationship, and
identifying and exploiting market opportunities. Hackers and enthusiasts who
found companies like Prusa tend to imagine that the product is everything, but
it’s not. Maybe 10% of the work is developing the 3D printer itself –
don’t abandon the other 90% of your business. Especially when you make that 10%
open: someone else is going to repurpose it, do the other 90%, and eat your
lunch. FOSS is  *great*  precisely because it makes that 10% into community
property and shares the cost of innovation, but you’d be a fool to act as if
that was all there was to it. You need to deal with sales and marketing, chase
down promising leads, identify and respond to risks, look for and exploit new
market opportunities, and much more to be successful.

This is a classic failure mode of open source businesses, and it’s  *Prusa’s
fault* . They had an excellent foothold early in the market, leveraging open
source and open hardware to great results and working hand-in-hand with
enthusiasts early on to develop the essential technology of 3D printing. Then,
they figured they were done developing their business model, and completely
dropped the ball as a result. Open source is not an “if you build it, the money
will come” situation, and to think otherwise is a grave mistake. Businesses need
to identify their risks and then mitigate them, and if they don’t do that due
diligence, then it’s  *their fault*  when it fails – it’s not a problem with
FOSS.

Free and open source software is an incredibly powerful tool, including as a
commercial opportunity. FOSS really has changed the world! But building a
business is still hard, and in addition to its fantastic advantages, the FOSS
model poses important and challenging constraints that you need to understand
and work with. You have to be creative, and you must do a risk/reward assessment
to understand how it applies to your business and how you can utilize it for
commercial success. Do the legwork and you can utilize FOSS for a competitive
advantage, but skip this step and you will probably fail within a decade.

1. I sourced this information from Armin’s blog post, but it didn’t
hold up to a later fact check: the
[Mk4 firmware](https://github.com/prusa3d/Prusa-Firmware-Buddy) seems to be
free software. It seems the controversy here has to do with Prusa
developing its slicer software behind closed doors and doing occasional
source-code dumps, rather than managing a more traditional “bazaar” style
project. ↩︎
2. That said, there are still vulnerabilities in the Chinese industrial
base that can be exploited by savvy Western entrepreneurs. Chinese access to
Western markets is constrained below a certain scale, for instance, in ways
that Western businesses are not. ↩︎
