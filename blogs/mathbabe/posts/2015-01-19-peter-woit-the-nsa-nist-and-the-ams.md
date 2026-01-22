---
title: "Peter Woit: The NSA, NIST and the AMS"
date: 2015-01-19
url: https://mathbabe.org/2015/01/19/peter-woit-the-nsa-nist-and-the-ams/
word_count: 863
---


*This was crossposted from [Not Even Wrong](http://www.math.columbia.edu/~woit/wordpress/?p=7457) and written by [Peter Woit](http://www.math.columbia.edu/~woit/).*


Last summer I wrote [here](http://www.math.columbia.edu/~woit/wordpress/?p=7045) about an article in the AMS Notices which appeared to make misleading claims about the NSA’s involvement in putting a backdoor in an NIST cryptography standard known as DUAL_EC_DRBG. The article by Richard George, a mathematician who worked at the NSA, addressed the issue of the NSA doing this kind of thing by discussing an example of past history when they were accused of doing this, but were really actually strengthening the standard. He then went on to claim that:


> I have never heard of any proven weakness in a cryptographic algorithm that’s linked to NSA; just innuendo.


This appears to be a denial of an NSA backdoor in the standard, while not saying so explicitly. If there is a backdoor, as most experts believe and the Snowden documents indicate, this was a fairly outrageous use of the AMS to mislead the math community and the public. At the time I argued with some at the AMS that they should insist that George address explicitly the question of the existence of the backdoor, but didn’t get anywhere with that. One of their arguments was that George was speaking for himself, not the NSA.


The question of fact here is a very simple and straightforward mathematical one: how was the choice used in the standard of points P and Q on an elliptic curve made? There is a known way to do this that provides a backdoor. Did the NSA use this method, or some other one for which no backdoor is known? The NSA refused to cooperate with the NIST investigation into this question. The only record of what happened when the NIST asked about how P and Q were chosen early on in the development of the standard is [this](http://csrc.nist.gov/groups/ST/crypto-review/documents/Email_Oct%2027%202004%20Don%20Johnson%20to%20John%20Kelsey.pdf), which indicates that people were told by the NSA that they were not allowed to publicly discuss the question.


Remarkably, the latest AMS Notices has a [new article](http://www.ams.org/notices/201502/rnoti-p165.pdf) with an extensive discussion of the DUAL_EC_DRBG issue, written by mathematician Michael Wertheimer, the NSA Director of Research. At first glance, Wertheimer appears to claim that the NSA was unaware of the possibility of a backdoor:


> With hindsight, NSA should have ceased supporting the dual EC_DRBG algorithm immediately after security researchers discovered the potential for a trapdoor. In truth, I can think of no better way to describe our failure to drop support for the Dual_EC_DRBG algorithm as anything other than regrettable.


On close reading though, one realizes that Wertheimer does not address at all the basic question: how were P and Q chosen? His language does not contain any actual denial that P and Q have a backdoor.


For a careful examination of the Wertheimer piece by an expert, see [this from Matthew Green](http://blog.cryptographyengineering.com/2015/01/hopefully-last-post-ill-ever-write-on.html). Green concludes that


> … it troubles me to see such confusing statements in a publication of the AMS. As a record of history, Dr. Wertheimer’s letter leaves much to be desired, and could easily lead people to the wrong understanding.


In a recent [podcast on the subject](https://threatpost.com/matthew-green-on-the-nsa-and-compromising-crypto-standards/110452) Green states


> I think it’s still going on… I think that the NSA has really adopted a policy of tampering with cryptographic products and they’re not going to give that up. I don’t think that this is a time that they want to go out admitting what they did in this particular case as a result of that.


Given that this is now the only official NSA statement about the DUAL_EC_DRBG issue, the Notices article has drawn a lot of attention, see for instance [here](http://it.slashdot.org/story/15/01/14/2036249/nsa-official-supporting-backdoored-random-number-generator-was-regrettable). The Register summarizes the story with the headline NSA: [So sorry we backed that borked crypto even after you spotted the backdoor](http://www.theregister.co.uk/2015/01/14/nsa_sorry_we_borked_nist_encryption_well_sorry_we_got_caught/).


The publication of the George and Wertheimer pieces by the AMS has created a situation where there are just two possibilities:

- Despite what experts believe and Snowden documents indicate, the NSA chose P and Q by a method that did not introduce a backdoor. For some reason though they are unwilling to state publicly that this is the case.
- P and Q were chosen with a backdoor, and the AMS has been now repeatedly been used to try and mislead the mathematics community about this issue.


I’ve contacted someone at the AMS to try and find out whether the question of a backdoor in P and Q was addressed in the refereeing process of the article, but been told that they won’t discuss this. I think this is an issue that now needs to be addressed by the AMS leadership, specifically by demanding assurances from Wertheimer that the NSA did not choose a backdoored P and Q. If this is the case I can see no reason why such assurances cannot be provided. If the NSA and Wertheimer won’t provide this, I think the AMS needs to immediately cut off its cooperative programs with the agency. There may be different opinions about the advisability of such programs, but I don’t think there can be any argument about the significance of the AMS being used by the NSA to mislead the mathematics community.
