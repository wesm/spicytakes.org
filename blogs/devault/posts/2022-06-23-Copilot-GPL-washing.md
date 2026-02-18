---
title: "GitHub Copilot and open source laundering"
date: 2022-06-23
url: https://drewdevault.com/2022/06/23/Copilot-GPL-washing.html
slug: Copilot-GPL-washing
word_count: 2176
---

*Disclaimer: I am the founder of a company which competes with GitHub. I am also
a long-time advocate for and developer of free and open source software, with a
broad understanding of free and open source software licensing and philosophy. I
will not name my company in this post to reduce the scope of my conflict of
interest.*

We have seen an explosion in machine learning in the past decade, alongside an
explosion in the popularity of free software. At the same time as FOSS has come
to dominate software and found its place in almost all new software products,
machine learning has increased dramatically in sophistication, facilitating more
natural interactions between humans and computers. However, despite their
parallel rise in computing, these two domains remain philosophically distant.

Though some audaciously-named companies might suggest otherwise, the machine
learning space has enjoyed almost none of the freedoms forwarded by the free and
open source software movement. Much of the actual code related to machine
learning is publicly available, and there are many public access research
papers available for anyone to read. However, the key to machine learning is
access to a high-quality dataset and heaps of computing power to process that
data, and these two resources are still kept under lock and key by almost all
participants in the space. 1

The essential barrier to entry for machine learning projects is overcoming these
two problems, which are often very costly to secure. A high-quality, well tagged
data set generally requires thousands of hours of labor to produce, 2  a task
which can potentially cost millions of dollars. Any approach which lowers this
figure is thus very desirable, even if the cost is making ethical compromises.
With Amazon, it takes the form of gig economy exploitation. With GitHub, it
takes the form of disregarding the terms of free software licenses. In the
process, they built a tool which facilitates the large-scale laundering of free
software into non-free software by their customers, who GitHub offers plausible
deniability through an inscrutable algorithm.

Free software is not an unqualified gift. There are terms for its use and
re-use. Even so-called “liberal” software licenses impose requirements on
re-use, such as attribution. To quote the MIT license:

> Permission is hereby granted […] subject to the following conditions: 
>  The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.

Or the equally “liberal” BSD license:

> Redistribution and use in source and binary forms, with or without
> modification, are permitted provided that the following conditions are met: 
>  Redistributions of source code must retain the above copyright notice, this
> list of conditions and the following disclaimer.

On the other end of the spectrum, copyleft licenses such as GNU General Public
License or Mozilla Public License go further, demanding not only attribution for
derivative works, but that such derived works are  *also released*  with the same
license. Quoting GPL:

> You may convey a work based on the Program, or the modifications to produce it
> from the Program, in the form of source code under the terms of section 4,
> provided that you also meet all of these conditions: 
>  […] 
>  You must license the entire work, as a whole, under this License to anyone who
> comes into possession of a copy.

And MPL:

> All distribution of Covered Software in Source Code Form, including any
> Modifications that You create or to which You contribute, must be under the
> terms of this License. You must inform recipients that the Source Code Form of
> the Covered Software is governed by the terms of this License, and how they
> can obtain a copy of this License. You may not attempt to alter or restrict
> the recipients’ rights in the Source Code Form.

Free software licenses impose obligations on the user through terms governing
attribution, sublicensing, distribution, patents, trademarks, and relationships
with laws like the Digital Millennium Copyright Act. The free software community
is no stranger to the difficulties in enforcing compliance with these
obligations, which some groups view as too onerous. But as onerous as one may
view these obligations to be, one is nevertheless required to comply with them.
If you believe that the force of copyright should protect your proprietary
software, then you must agree that it equally protects open source works,
despite the inconvenience or cost associated with this truth.

GitHub’s Copilot is trained on software governed by these terms, and it fails to
uphold them, and enables customers to accidentally fail to uphold these terms
themselves. Some argue about the risks of a “copyleft surprise”, wherein someone
incorporates a GPL licensed work into their product and is surprised to find
that they are obligated to release their product under the terms of the GPL as
well. Copilot institutionalizes this risk and any user who wishes to use it to
develop non-free software would be well-advised not to do so, else they may find
themselves legally liable to uphold these terms, perhaps ultimately being
required to release their works under the terms of a license which is
undesirable for their goals.

Essentially, the argument comes down to whether or not the model constitutes a
derivative work of its inputs. Microsoft argues that it does not. However, these
licenses are not specific regarding the means of derivation; the classic
approach of copying and pasting from one project to another need not be the only
means for these terms to apply. The model exists as the result of applying an
algorithm to these inputs, and thus the model itself is a derivative work of its
inputs. The model, then used to create new programs, forwards its obligations to
those works.

All of this assumes the best interpretation of Microsoft’s argument, with a
heavy reliance on the fact that the model becomes a general purpose programmer,
having meaningfully learned from its inputs and applying this knowledge to
produce original work. Should a human programmer take the same approach,
studying free software and applying those lessons, but not the code itself, to
original projects, I would agree that their applied knowledge is not creating
derivative works. However, that is not how machine learning works. Machine
learning is essentially a glorified pattern recognition and reproduction engine,
and does not represent a genuine generalization of the learning process. It is
perhaps capable of a limited amount of originality, but is also capable of
degrading to the simple case of copy and paste. Here is an example of Copilot
reproducing, verbatim, a function which is governed by the GPL, and would thus
be governed by its terms:

The license reproduced by Copilot is not correct, neither in form nor function.
This code was not written by V. Petkov and the GPL imposes much stronger
obligations than those suggested by the comment. This small example was
deliberately provoked with a suggestive prompt (this famous function is known as
the “ [fast inverse square root](https://en.wikipedia.org/wiki/Fast_inverse_square_root) ”) and the “float Q_”, but it’s not a stretch to
assume someone can accidentally do something similar with any particularly
unlucky English-language description of their goal.

Of course, the use of a suggestive prompt to convince Copilot to print GPL
licensed code suggests another use: deliberately laundering FOSS source code. If
Microsoft’s argument holds, then indeed the only thing which is necessary to
legally circumvent a free software license is to teach a machine learning
algorithm to regurgitate a function you want to use.

This is a problem. I have two suggestions to offer to two audiences: one for
GitHub, and another for free software developers who are worried about Copilot.

To GitHub: this is your Oracle v Google moment. You’ve invested in building a
platform on top of which the open source revolution was built, and leveraging
this platform for this move is a deep betrayal of the community’s trust. The law
applies to you, and banking on the fact that the decentralized open source
community will not be able to mount an effective legal challenge to your $7.5B
Microsoft war chest does not change this. The open source community is
astonished, and the astonishment is slowly but surely boiling over into rage as
our concerns fall on deaf ears and you push forward with the Copilot release. I
expect that if the situation does not change, you will find a group motivated
enough to challenge this. The legitimacy of the free software ecosystem may rest
on this problem, and there are many companies who are financially incentivized
to see to it that this legitimacy stands. I am certainly prepared to join a
class action lawsuit as a maintainer, or alongside other companies with
interests in free software making use of our financial resources to facilitate a
lawsuit.

The tool can be improved, probably still in time to avoid the most harmful
effects (harmful to your business, that is) of Copilot. I offer the following
specific suggestions:

1. Allow GitHub users and repositories to opt-out of being incorporated into the
model. Better, allow them to opt-in. Do not tie this flag into unrelated
projects like Software Heritage and the Internet Archive.
2. Track the software licenses which are incorporated into the model and inform
users of their obligations with respect to those licenses.
3. Remove copyleft code from the model entirely, unless you want to make the
model and its support code free software as well.
4. Consider compensating the copyright owners of free software projects
incorporated into the model with a margin from the Copilot usage fees, in
exchange for a license permitting this use.

Your current model probably needs to be thrown out. The GPL code incorporated
into it entitles anyone who uses it to receive a GPL’d copy of the model for
their own use. It entitles these people to commercial use, to build a competing
product with it. But, it presumably also includes works under incompatible
licenses, such as the CDDL, which is… problematic. The whole thing is a legal
mess.

I cannot speak for the rest of the community that have been hurt by this
project, but for my part, I would be okay with not pursuing the answers to any
of these questions with you in court if you agreed to resolve these problems
now.

And, my advice to free software maintainers who are pissed that their licenses
are being ignored. First, don’t use GitHub and your code will not make it into
the model (for now).  [I’ve written before](https://drewdevault.com/2022/03/29/free-software-free-infrastructure.html)  about why it’s generally important
for free software projects to use free software infrastructure, and this only
re-enforces that fact. Furthermore, the old “vote with your wallet” approach is
a good way to show your disfavor. That said, if it occurs to you that you
 *don’t*  actually pay for GitHub, then you may want to take a moment to consider
if the incentives created by that relationship explain this development and may
lead to more unfavorable outcomes for you in the future.

You may also be tempted to solve this problem by changing your software licenses
to prohibit this behavior. I’ll say upfront that according to Microsoft’s
interpretation of the situation (invoking fair use), it doesn’t matter to them
which license you use: they’ll use your code regardless. In fact,  [some
proprietary code](https://twitter.com/ChrisGr93091552/status/1539731632931803137)  was found to have been incorporated into the model. However, I
still support your efforts to address this in your software licenses, as it
provides an even stronger legal foundation upon which we can reject Copilot.

I will caution you that the way you approach that clause of your license is
important. Whenever writing or changing a free and open source software license,
you should consider whether or not it will still qualify as free or open source
after your changes. To be specific, a clause which outright forbids the use of
your code for training a machine learning model will make your software
 *non-free* , and I do not recommend this approach. Instead, I would update your
licenses to clarify that incorporating the code into a machine learning model is
considered a form of derived work, and that your license terms apply to the
model and any works produced with that model.

To summarize, I think that GitHub Copilot is a bad idea as designed. It
represents a flagrant disregard of FOSS licensing in of itself, and it enables
similar disregard — deliberate or otherwise — among its users. I
hope they will heed my suggestions, and I hope that my words to the free
software community offer some concrete ways to move forward with this problem.

1. Shout-out to Mozilla Common Voice, one of the few exceptions to this rule,
which is an excellent project that has produced a high-quality, freely
available dataset of voice samples, and used it to develop free models and
software for text-to-speech and speech recognition. ↩︎
2. Typically exploitative labor from low-development countries which the tech
industry often pretends isn’t a hair’s breadth away from slavery. ↩︎
