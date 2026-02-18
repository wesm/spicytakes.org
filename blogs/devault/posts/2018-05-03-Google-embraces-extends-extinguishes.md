---
title: "Google embraces, extends, and extinguishes"
date: 2018-05-03
url: https://drewdevault.com/2018/05/03/Google-embraces-extends-extinguishes.html
slug: Google-embraces-extends-extinguishes
word_count: 687
---

Microsoft infamously coined the euphemism “ [embrace, extend,
extinguish](https://en.wikipedia.org/wiki/Embrace,_extend,_and_extinguish) ” to
describe their strategy for disrupting markets dominated by open standards.
These days, Microsoft seems to have turned the other leaf, contributing to a
huge amount of open source and supporting open standards, and is becoming a good
citizen of the technology community. It’s time to turn our concerns to Google.

Google famously “embraced” email on April Fool’s day, 2004, which is of course
based on an open standard and federates with the rest of the world. If you’ve
read the news lately, you might have seen that Google is shipping a big update
to GMail soon, which adds “self-destructing” emails that vanish from the
recipient’s inbox after a time. Leaving aside that this promise is impossible to
deliver, look at the implementation - Google emails a link to a webpage with the
actual email content, and does magic in their client to make it look seamless.
Thus, they “extend” email. The “extinguish” with GMail is also well underway -
it’s infamous for having an extremely strict spam filter for incoming emails
from people who run personal or niche mail servers.

Then there’s AMP. It’s an understatement to say Google embraced the web - but
AMP is how they enter the “extend” phase. AMP is a “standard”, but they don’t
listen to any external feedback on it and it serves as a vehicle for keeping
users on their platform even when reading content from other websites. This is
thought to be the main intention of the service, as there are plenty of other
(and more effective) ways of rewarding lightweight pages in their search
results. The “extinguish” phase comes as sites that don’t play ball get pushed
out of Google search results and into obscurity. AMP is perhaps the most blatant
of Google’s strategies, serving only to further Google’s agenda at the expense
of everyone else.

The list of grievances continues. Consider Google’s dizzying collection of chat
applications. In its initial form, gtalk supported XMPP, an open and federated
standard for chat applications. Google dropped support for XMPP in 2014 and
continued the development of their proprietary platform up thru today’s Hangouts
and Google Chat platforms - neither of which support any open standards. Slack
is also evidently taking cues from Google here, recently shutting down their own
IRC and XMPP bridges.

Google Reader’s discontinuation fits too. RSS’s decline was evident before
Google axed it, but killing Reader dealt a huge blow to any of RSS’s remaining
momentum. Google said themselves they wanted to consolidate users onto the rest
of their services - none of which, I should add, support any open syndication
standards.

What of Google’s role as a participant in open source? Sure, they make a lot of
software open source, but they don’t collaborate with anyone.  They forked from
WebKit to get Apple out of the picture, and contributing to Chromium as a
non-Googler is notoriously difficult. Android is the same story - open source in
principle, but non-Googler AOSP contributors bemoan their awful approach to
external patches. It took Google over a decade to start making headway on
upstreaming their Linux patches for Android, too. Google writes papers about AI,
presumably to incentivize their academics with recognition for their work. This
is great until you notice that the crucial piece, the trained models, is always
absent.

For many people, the alluring convenience of Google’s services is overwhelming.
It’s hard to hear these things. But we must face facts: embrace, extend,
extinguish is a core part of Google’s playbook today. It’s important that we
work to diversify the internet and fight the monoculture they’re fostering.

**2018-05-04 18:12 UTC** : I retract my criticism of Google’s open source portfolio
as a whole, and acknowledge their positive impact on many projects. However, of
the projects explicitly mentioned I maintain that my criticism is valid.

**2018-05-05 11:17 UTC** : Apparently the previous retraction caused some
confusion. I am  *only*  retracting the insinuation that Google isn’t a good actor
in open source, namely the first sentence of paragraph 6. The rest of the
article has not been retracted.
