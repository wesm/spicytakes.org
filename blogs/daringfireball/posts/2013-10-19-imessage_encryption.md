---
title: "iMessage End-to-End Encryption: We Have to Take Apple’s Word for It"
date: 2013-10-19
url: https://daringfireball.net/2013/10/imessage_encryption
slug: imessage_encryption
word_count: 1090
---


Earlier this year, as revelations regarding U.S. government/law enforcement snooping came to light, Apple published a “Commitment to Customer Privacy”. [It says, in part](https://www.apple.com/apples-commitment-to-customer-privacy/):


> Apple has always placed a priority on protecting our customers’
> personal data, and we don’t collect or maintain a mountain of
> personal details about our customers in the first place. There are
> certain categories of information which we do not provide to law
> enforcement or any other group because we choose not to retain it.
> For example, conversations which take place over iMessage and
> FaceTime are protected by end-to-end encryption so no one but the
> sender and receiver can see or read them. Apple cannot decrypt
> that data.


This week, security [researchers at Quarkslab published a white paper](http://blog.quarkslab.com/imessage-privacy.html) disputing this, claiming, at the top:


> What we are *not* saying: Apple reads your iMessages.
> What we are saying: Apple can read your iMessages if they choose
> to, or if they are required to do so by a government order.
> As Apple claims, there is end-to-end encryption. The weakness is
> in the key infrastructure as it is controlled by Apple: they can
> change a key anytime they want, thus read the content of our
> iMessages.


Writing at AllThingsD, [John Paczkowski reports](http://allthingsd.com/20131018/apple-no-we-cant-read-your-imessages/):


> Asked by AllThingsD if the firms’s claim is legitimate, renowned
> security technologist Bruce Schneier replied with a definitive
> yes. “The researchers show that iMessage could be undetectably
> designed to intercept and read messages, not that it is designed
> to do so,” Schneier said.
> But Apple insists it is not so motivated. And it stands by its
> June claims about iMessage’s security. Apple says that
> QuarksLab’s theory is just that — a theory, and one that would
> require a re-architecting of iMessage for it ever to be a threat
> in the real world.
> “iMessage is not architected to allow Apple to read messages,”
> said Apple spokeswoman Trudy Muller in a statement to AllThingsD.
> “The research discussed theoretical vulnerabilities that would
> require Apple to re-engineer the iMessage system to exploit it,
> and Apple has no plans or intentions to do so.”


In other words, this is in many ways a semantic argument over the difference between *can* and *could be*. What Quarkslab’s research proves (I read the paper and admit I found it largely over my head — but I’ll accept Schneier’s vouching for its validity) is that Apple’s iMessage back-end *could* be designed to allow for Apple to intercept and read message content, and there is no way we, as iMessage users, would be able to detect it.


What Apple has said, and reiterated today, is that iMessage’s back-end is not in fact designed in that way — that there is no mechanism in the system for Apple employees to surreptitiously change the encryption key to allow for messages to be decrypted during transit.


Thus, I think Dan Goodin at Ars Technica took things too far in [his report on Quarkslab’s findings](http://arstechnica.com/security/2013/10/contrary-to-public-claims-apple-can-read-your-imessages/), writing:


> Contrary to public claims, Apple employees *can* read communications
> sent with its iMessage service, according to researchers who have
> reverse engineered it.


That’s not what Quarkslab proved. What they proved is that Apple *could be*, and that we as users have no way to verify cryptographically that they are not.


It comes down to Apple’s word.


If you believe or even suspect that Apple is lying about this, consider at least that Apple is taking an enormous risk by doing so. If they are in fact allowing law enforcement or the NSA to surreptitiously decrypt iMessage content, their corporate credibility will suffer an enormous, perhaps irrevocable loss if it ever comes to light. In the case of law enforcement, decrypted iMessage content used in a prosecution would necessarily need to be revealed as evidence in court. In the case of a secret agency like the NSA, it’s entirely possible that [Edward Snowden](http://en.wikipedia.org/wiki/Edward_Snowden) is already in possession of proof of such a back door, and even if not, Apple would remain forever at the risk of another whistleblower revealing such a thing.


Leaving aside the moral implications of flat-out lying to their customers, I would think that if iMessage’s back-end were designed with a weakness exploitable by Apple as Quarkslab supposes, Apple would say or promise nothing with regard to iMessage’s susceptibility to server-side decryption rather than compound that weakness with blatant lies to the contrary. To lie would be to take an enormous PR risk for a relatively small PR gain. I say “small PR gain” simply because I doubt most people who use iMessage even know their messages are supposed to be securely encrypted from end-to-end. I say “large PR risk” because if Apple’s statements regarding iMessage encryption are eventually discredited, the backlash in the press will be severe (and justly so).


(**Sidenote**: My understanding is that Apple does not permanently store iMessage message content on its servers. Even in encrypted form, iMessage data is only in Apple’s hands while in transit. Once delivered, it’s gone. [**Update:** Or, perhaps better said, some amount of time after being delivered, it’s gone. Just how long Apple will hold messages pending delivery, I don’t know. In some cases it seems to be days, as anyone who’s taken a device that’s been offline for a few days and received a sudden burst of iMessages can attest.] This is by design. In a discussion with a source at Apple earlier this year, I was told that some time ago word came down from the top that wherever possible,1 Apple’s messaging services should be designed in a such a way that there is nothing — or, at least, as little data as possible — stored or logged for law enforcement agencies to ask for. And the same is true of decrypting content while in transit. An uncynical take on this: Apple cares about customer privacy and knows that storing nothing at all is the only way to protect it. A cynical take: Apple seeks to wash its hands of any possible involvement in such matters.)


---

1. So, for example, this does not apply to iCloud email. Email is by design susceptible in numerous ways: it’s usually transmitted in plain text and it’s stored on the server. ↩︎



| **Previous:** | [Apple and China](https://daringfireball.net/2013/10/apple_and_china) |
| **Next:** | [Thoughts and Observations Regarding This Week’s Apple Event Introducing the iPad Air and Retina iPad Mini](https://daringfireball.net/2013/10/this_weeks_ipad_event) |


PreviousNext