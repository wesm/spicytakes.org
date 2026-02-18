---
title: "Bloomberg’s ‘The Big Hack’"
date: 2018-10-04
url: https://daringfireball.net/2018/10/bloomberg_the_big_hack
slug: bloomberg_the_big_hack
word_count: 1340
---


Bloomberg Businessweek today published [an absolutely incredible story](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies) alleging that Chinese intelligence compromised thousands of data center servers by infiltrating the supply chain to insert hard-to-detect rogue chips on motherboards from a company named Supermicro. [The entire report](https://www.bloomberg.com/news/features/2018-10-04/the-big-hack-how-china-used-a-tiny-chip-to-infiltrate-america-s-top-companies), by Jordan Robertson and Michael Riley, is worth reading in full.


Bloomberg alleges that Apple and Amazon were both among the companies that installed the compromised hardware. Apple and Amazon both vehemently deny the report. Someone is either wrong or lying. This cannot all be true.


From Bloomberg’s report, regarding Amazon:


> Nested on the servers’ motherboards, the testers found a tiny
> microchip, not much bigger than a grain of rice, that wasn’t part
> of the boards’ original design. Amazon reported the discovery to
> U.S. authorities, sending a shudder through the intelligence
> community. Elemental’s servers could be found in Department of
> Defense data centers, the CIA’s drone operations, and the onboard
> networks of Navy warships. And Elemental was just one of hundreds
> of Supermicro customers.


Regarding Apple:


> Apple was an important Supermicro customer and had planned to
> order more than 30,000 of its servers in two years for a new
> global network of data centers. Three senior insiders at Apple say
> that in the summer of 2015, it, too, found malicious chips on
> Supermicro motherboards. Apple severed ties with Supermicro the
> following year, for what it described as unrelated reasons.


And regarding both companies’ denials:


> The companies’ denials are countered by six current and former
> senior national security officials, who — in conversations that
> began during the Obama administration and continued under the
> Trump administration — detailed the discovery of the chips and
> the government’s investigation. One of those officials and two
> people inside AWS provided extensive information on how the attack
> played out at Elemental and Amazon; the official and one of the
> insiders also described Amazon’s cooperation with the government
> investigation. In addition to the three Apple insiders, four of
> the six U.S. officials confirmed that Apple was a victim.


The companies’ denials are seemingly unequivocal, however. [Apple’s statement to Bloomberg](https://www.bloomberg.com/news/articles/2018-10-04/the-big-hack-amazon-apple-supermicro-and-beijing-respond):


> Over the course of the past year, Bloomberg has contacted us
> multiple times with claims, sometimes vague and sometimes
> elaborate, of an alleged security incident at Apple. Each time, we
> have conducted rigorous internal investigations based on their
> inquiries and each time we have found absolutely no evidence to
> support any of them. We have repeatedly and consistently offered
> factual responses, on the record, refuting virtually every aspect
> of Bloomberg’s story relating to Apple.
> On this we can be very clear: Apple has never found malicious
> chips, “hardware manipulations” or vulnerabilities purposely
> planted in any server. Apple never had any contact with the FBI or
> any other agency about such an incident. We are not aware of any
> investigation by the FBI, nor are our contacts in law enforcement.


That statement is credited only to “Apple”, so presumably it was written by Apple PR. Amazon issued a similar statement to Bloomberg, but later published a full response, signed by Steve Schmidt, the company’s chief information security officer. [Schmidt is adamant and clear](https://aws.amazon.com/blogs/security/setting-the-record-straight-on-bloomberg-businessweeks-erroneous-article/):


> There are so many inaccuracies in this article as it relates to
> Amazon that they’re hard to count. We will name only a few of them
> here. First, when Amazon was considering acquiring Elemental, we
> did a lot of due diligence with our own security team, and also
> commissioned a single external security company to do a security
> assessment for us as well. That report did not identify any issues
> with modified chips or hardware. As is typical with most of these
> audits, it offered some recommended areas to remediate, and we
> fixed all critical issues before the acquisition closed. This was
> the sole external security report commissioned. Bloomberg has
> admittedly never seen our commissioned security report nor any
> other (and refused to share any details of any purported other
> report with us).
> The article also claims that after learning of hardware
> modifications and malicious chips in Elemental servers, we
> conducted a network-wide audit of SuperMicro motherboards and
> discovered the malicious chips in a Beijing data center. This
> claim is similarly untrue. The first and most obvious reason is
> that we never found modified hardware or malicious chips in
> Elemental servers. Aside from that, we never found modified
> hardware or malicious chips in servers in any of our data centers.


I see no way around it: either Bloomberg’s report is significantly wrong, at least as pertains to Amazon and Apple, or Apple and Amazon have issued blatantly false denials. You can, perhaps, chalk up Apple’s denial to it being written by Apple PR. I don’t think this would happen, but hypothetically this issue could be deemed so sensitive — either within the company or as a national security issue — that the people at Apple with knowledge of the situation lied to Apple PR. But in my experience, Apple PR does not lie. Do they spin the truth in ways that favor the company? Of course. That’s their job. But they don’t lie, because they understand that one of Apple’s key assets is its credibility. They’d say nothing before they’d lie.


Schmidt signing his name to Amazon’s response is more telling. Presumably no one at Amazon would be more familiar with the details of such a breach than Schmidt.


One way or the other, there is more to come on this story, and the credibility of either Bloomberg, or Apple *and* Amazon, is going to take a significant hit. Currently those are the two most valuable [publicly-traded](http://time.com/money/5282501/apple-trillion-biggest-companies-in-history/) companies in the world.


A few other notable tidbits. From Bloomberg’s report:


> One government official says China’s goal was long-term access to
> high-value corporate secrets and sensitive government networks. No
> consumer data is known to have been stolen.


And then this from Amazon’s response:


> Because Elemental appliances are not designed to be exposed to the
> public internet, our customers are protected against the
> vulnerability by default.


I do not understand how, if these servers are not exposed to the public internet, they could “phone home” to Chinese servers outside the data centers.


Technical details aside, the whole central thesis of the story rings true — China cannot be trusted as a state actor, but the entire technology industry is dependent upon the Chinese supply chain. It is completely credible that the managers of Chinese factories are susceptible to bribes and threats of “inspections” that would shut down their plants. From the Bloomberg report:


> Over the decades, the security of the supply chain became an
> article of faith despite repeated warnings by Western officials. A
> belief formed that China was unlikely to jeopardize its position
> as workshop to the world by letting its spies meddle in its
> factories. That left the decision about where to build commercial
> systems resting largely on where capacity was greatest and
> cheapest. “You end up with a classic Satan’s bargain”, one former
> U.S. official says. “You can have less supply than you want and
> guarantee it’s secure, or you can have the supply you need, but
> there will be risk. Every organization has accepted the second
> proposition.”


Lastly, whatever the veracity of the report, Bloomberg deserves kudos for this sentence:


> Two of Elemental’s biggest early clients were the Mormon church,
> which used the technology to beam sermons to congregations around
> the world, and the adult film industry, which did not.


**Update:** [Apple has issued a stronger denial of Bloomberg’s report](https://daringfireball.net/linked/2018/10/04/what-businessweek-got-wrong-about-apple).



| **Previous:** | [The Great DF Random Slowdown Should Be Over](https://daringfireball.net/2018/09/df_slowdown) |
| **Next:** | [Sometimes It’s Better to Just Start Over With iCloud Photo Library Syncing](https://daringfireball.net/2018/10/icloud_photo_library_start_over) |


PreviousNext