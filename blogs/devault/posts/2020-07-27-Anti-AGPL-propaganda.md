---
title: "The falsehoods of anti-AGPL propaganda"
date: 2020-07-27
url: https://drewdevault.com/2020/07/27/Anti-AGPL-propaganda.html
slug: Anti-AGPL-propaganda
word_count: 839
---

Google is well-known for  [forbidding the use of](https://opensource.google/docs/using/agpl-policy/)  software
using the  [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) , commonly known as “AGPL”.
Google is also well-known for being the subject of cargo-culting by fad
startups. Unfortunately, this means that they are susceptible to what is
ultimately anti-AGPL propaganda from Google, with little to no basis in fact.

*Obligatory: I’m not a lawyer; this is for informational purposes only.*

In truth, the terms of the AGPL are pretty easy to comply with. The basic
obligations of the AGPL which set it apart from other licenses are as follows:

* Any derivative works of AGPL-licensed software must also use the AGPL.
* Any users of such software are entitled to the source code under the terms of
the AGPL, including users accessing it over the network such as with their web
browser or via an API or internet protocol.

If you’re using AGPL-licensed software like a database engine or  [my own
AGPL-licensed works](https://sr.ht/~sircmpwn/sourcehut/) , and you haven’t made any changes to the source
code, you don’t have to do anything to comply. If you  *have*  modified the
software, you simply have to publish your modifications. The easiest way to do
this is to send it as a patch upstream, but you could use something as simple as
providing a tarball to your users. 1

The nuances are detailed and cover many edge cases to prevent abuse. But in
general, just publish your modifications under the same AGPL terms and you’ll
be good to go. The license is usually present in the source code as a  `COPYING` 
or  `LICENSE`  file, so if you just tar up your modified source code and drop a
link on your website, that’s good enough. If you want to go the extra mile and
express your gratitude to the original software developers, consider submitting
your changes for upstream inclusion. Generally, the feedback you’ll receive will
help to make your changes better for your use-case, too; and submitting your
work upstream will prevent your copy from diverging from upstream.

That’s pretty easy, right? I’m positive that your business has to deal with much
more onerous contracts than the AGPL. Then why does Google make a fuss about it?

[The Google page about the AGPL](https://opensource.google/docs/using/agpl-policy/)  details inaccurate (but
common 2 ) misconceptions about the obligations of the AGPL that don’t follow
from the text. Google states that if, for example, Google Maps used PostGIS as
its data store, and PostGIS used the AGPL, Google would be required to release
the Google Maps code. This is not true. They would be required to release  *their
PostGIS patches*  in this situation. AGPL does not extend the GPL in that it
makes the Internet count as a form of linking which creates a derivative work,
as Google implies, but rather that it makes anyone who uses the software via
the Internet entitled to its source code. It does not update the “what counts
as a ‘derivative work’” algorithm, so to speak — it updates the “what
counts as ‘distributing’ the software” algorithm.

The reason they spread these misconceptions is straightforward: they want to
discourage people from using the AGPL, because they cannot productize such
software effectively. Google wants to be able to incorporate FOSS software into
their products and sell it to users without the obligation to release their
derivative works. Google is an Internet company, and they offer Internet
services. The original GPL doesn’t threaten their scheme because their software
is accessed over the Internet, not distributed to end-users directly.

By discouraging the use of AGPL in the broader community, Google hopes to create
a larger set of free- and open-source software that they can take for their own
needs without any obligations to upstream. Ask yourself: why is documentation of
internal-facing decisions like what software licenses to use being published in
a public place? The answer is straightforward: to influence the public. This is
propaganda.

There’s a bizarre idea that software companies which eschew the AGPL in favor of
something like MIT are doing so specifically because they want companies “like
Google 3 ” to pay for their software, and they know that they have no chance if
they use AGPL. In truth, Google was never going to buy your software. If you
don’t use the AGPL, they’re just going to take your software and give nothing
back. If you do use the AGPL, they’re just going to develop a solution in-house.
There’s no outcome where Google pays you.

Don’t be afraid to use the AGPL, and don’t be afraid to use software which uses
the AGPL. The obligations are not especially onerous or difficult, despite what
Google would have you believe. The license isn’t that long — read it and
see for yourself.

1. *December 4th, 2024*: A correction to this passage was made following a clarification from Florian Kohrt. Thanks! ↩︎
2. Likely common *because of this page*. ↩︎
3. By the way, there are no more than 10 companies world-wide which are “like Google” by any measure. ↩︎
