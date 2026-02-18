---
title: "Seriously, don't sign a CLA"
date: 2023-07-04
url: https://drewdevault.com/2023/07/04/Dont-sign-a-CLA-2.html
slug: Dont-sign-a-CLA-2
word_count: 950
---

[SourceGraph](https://about.sourcegraph.com/)  is making their product closed source, abandoning the Apache
2.0 license it was originally distributed under, so once again we convene in the
ritual condemnation we offer to commercial products that piss in the pool of
open source. Invoking Bryan Cantrill once more:

[Bryan Cantrill on OpenSolaris — YouTube](https://youtu.be/-zRN7XLCRhc?t=2483) 
 A contributor license agreement, or CLA, usually (but not always) includes an
important clause: a copyright assignment. These agreements are provided by
upstream maintainers to contributors to open source software projects, and they
demand a signature before the contributor’s work is incorporated into the
upstream project. The copyright assignment clause that is usually included
serves to offer the upstream maintainers more rights over the contributor’s work
than the contributor was offered by upstream, generally in the form of ownership
or effective ownership over the contributor’s copyright and the right to license
it in any manner they choose in the future, including proprietary distributions. 
 This is a strategy employed by commercial companies with one purpose only: to
place a rug under the project, so that they can pull at the first sign of a bad
quarter. This strategy exists to subvert the open source social contract. These
companies wish to enjoy the market appeal of open source and the free labor of
their community to improve their product, but do *not* want to secure these
contributors any rights over their work. 
 This is particularly pathetic in cases like that of SourceGraph, which used a
permissive Apache 2.0 license. Such licenses already allow their software to be
incorporated into non-free commercial works, such is the defining nature of a
permissive license, with relatively few obligations: in this case, a simple
attribution will suffice. SourceGraph could have been made non-free without a
CLA at all if this one obligation was met. The owners of SourceGraph find the
simple task of crediting their contributors too onerous. This is disgusting. 
 SourceGraph once approached SourceHut asking about building an integration
between our platforms. They wanted us to do most of the work, which is a bit
tacky but reasonable under the reciprocal social contract of open source. We
did not prioritize it and I’m glad that we didn’t: our work would have been made
non-free. 
 Make no mistake: a CLA is a promise that a open source software project will one
day become non-free. Don’t sign them. 
 **What are my rights as a contributor?** 
 If you sign away your rights by agreeing to a CLA, you retain all of the rights
associated with your work. 
 By default, you own the copyright over your contribution and the contribution is
licensed under the same software license the original project uses, thus, your
contribution is offered to the upstream project on the same terms that their
contribution was offered to you. The copyright for such projects is held
collectively by all contributors. 
 You also always have the right to fork an open source project and distribute
your improvements on your own terms, without signing a CLA – the only power
upstream holds is authority over the “canonical” distribution. If the rug is
pulled from under you, you may also continue to use, and improve, versions of
the software from prior to the change in license. 
 **How do I prevent this from happening to my project?** 
 A CLA is a promise that software will one day become non-free; you can also
promise the opposite. Leave copyright in the collective hands of all
contributors and use a copyleft license. 
 Without the written consent of all contributors, or performing their labor
yourself by re-writing their contributions, you cannot change the license of a
project. Skipping the CLA leaves their rights intact. 
 In the case of a permissive software license, a new license (including
proprietary licenses) can be applied to the project and it can be redistributed
under those terms. In this way, all future changes can be written with a new
license. The analogy is similar to that of a new project with a proprietary
license taking a permissively licensed project and incorporating all of the code
into itself before making further changes. 
 You can prevent this as well with a copyleft license: such a license requires
the original maintainers to distribute future changes to the work under a free
software license. Unless they can get all copyright holders – all of the
contributors – to agree to a change in license, they are obligated to
distribute their improvements on the same terms. 
 Thus, the absence of a CLA combined with the use of a copyleft license serves as
a strong promise about the future of the project. 
 Learn more at [writefreesoftware.org](https://writefreesoftware.org): 
 
[Managing copyright ownership](https://writefreesoftware.org/learn/participate/copyright-ownership/)
[Re-using free software](https://writefreesoftware.org/learn/participate/derived-works/)
[What is copyleft?](https://writefreesoftware.org/learn/participate/derived-works/)
 
 **What should I do as a business instead of a CLA?** 
 It is not ethical to demand copyright assignment in addition to the free labor
of the open source community. However, there are some less questionable aspects
of a contributor license agreement which you may uphold without any ethical
qualms, notably to establish provenance. 
 Many CLAs include clauses which establish the provenance of the contribution and
transfer liability to the contributor, such that the contributor agrees that
their contribution is either their own work or they are authorized to use the
copyright (for example, with permission from their employer). This is a
reasonable thing to ask for from contributors, and manages your exposure to
legal risks. 
 The best way to ask for this is to require contributions to be “signed-off” with
the [Developer Certificate of
Origin](https://drewdevault.com/2021/04/12/DCO.html). 
  
 Previously: 
 
[Breaking down Apollo Federation’s anti-FOSS corporate gaslighting](https://drewdevault.com/2021/11/05/Apollo-federation-2-gaslighting.html)
[The Developer Certificate of Origin is a great alternative to a CLA](https://drewdevault.com/2021/04/12/DCO.html)
[Open source means surrendering your monopoly over commercial exploitation](https://drewdevault.com/2021/01/20/FOSS-is-to-surrender-your-monopoly.html)
[Elasticsearch does not belong to Elastic](https://drewdevault.com/2021/01/19/Elasticsearch-does-not-belong-to-Elastic.html)
