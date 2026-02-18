---
title: "The D.O.J. Goes After Google’s ‘Communicate With Care’ Program"
date: 2022-03-24
url: https://daringfireball.net/2022/03/doj_google_communicate_with_care
slug: doj_google_communicate_with_care
word_count: 994
---


[Jon Brodkin, writing for Ars Technica](https://arstechnica.com/tech-policy/2022/03/google-routinely-hides-emails-from-litigation-by-ccing-attorneys-doj-alleges/):


> The US Department of Justice and 14 state attorneys general
> yesterday asked a federal judge to sanction Google for misusing
> attorney-client privilege to hide emails from litigation.
> “In a program called ‘Communicate with Care,’ Google trains and
> directs employees to add an attorney, a privilege label, and a
> generic ‘request’ for counsel’s advice to shield sensitive
> business communications, regardless of whether any legal advice is
> actually needed or sought. Often, knowing the game, the in-house
> counsel included in these Communicate-with-Care emails does not
> respond at all,” the DOJ told the court. The fact that attorneys
> often don’t reply to the emails “underscor[es] that these
> communications are not genuine requests for legal advice but
> rather an effort to hide potential evidence,” the DOJ said. [...]
> CCing lawyers is a [common
> practice](https://www.todaysgeneralcounsel.com/to-cc-or-not-to-cc-that-is-the-privilege-question/),
> but the DOJ says Google took it to an “egregious” level. “Google’s
> institutionalized manufacturing of false privilege claims is
> egregious, spanning nearly a decade and permeating the company
> from the top executives on down,” the DOJ said.


Without commenting on Google’s program or the specifics of the DOJ’s accusations, the broader issue makes me think about the nature of digital communication. Pre-email, business communication between colleagues was typically either in-person (not recorded), on the phone (not recorded), or via printed memoranda and reports (recorded, on paper). During a legal inquiry, printed memos could be subpoenaed or subject to discovery, and phone records could too. But telephone records only show who called whom, when, and for how long. The content of phone calls wasn’t (and still isn’t) recorded.


Email corresponds directly to the form of printed memos. That’s even where email lingo like “CC” and the “Subject” line comes from. (“CC” originally stood for “[carbon copy](https://www.merriam-webster.com/dictionary/carbon%20copy)”, which is how those copies were actually made — using [carbon paper](https://en.wikipedia.org/wiki/Carbon_paper).) Emails are seemingly just like paper memos, only digital. But, because email is so much more profoundly convenient to use, both to send and receive, it quickly became more casual. Psychologically, using email for work *feels* a lot more like face-to-face conversations or phone calls. Many people with office jobs send thousands of emails per year at work. Only a maniac sent out thousands of printed memos per year pre-email.


I don’t think you have to be doing something immoral or on shaky legal footing to want to communicate with colleagues privately, without fear of those communications being exposed in future legal inquiries. Any sort of strategic deliberation is something you’d naturally want to remain forever private. So I get the basic desire. But I think a loose policy of just cc’ing company attorneys on we-want-this-to-remain-private emails is a poor strategy. The emails are still there. And the DOJ and state attorneys general can look at this behavior, see that the lawyers aren’t really involved in the discussions, and raise a stink about it, as they have with Google. Whatever the contents of those emails, this “Communicate With Care” program *looks* shady.


Last year, writing about a Phil Schiller email that was made public through discovery in the Epic v. Apple lawsuit, [I asked a question in a footnote](https://daringfireball.net/2021/06/app_store_the_schiller_cut#fn1-2021-06-07):1


> It really has all been email, too. Unless I’m missing something,
> not one piece of communication entered into evidence — from
> either Apple or Epic — has been anything other than an email
> message. Not one message from iMessage or any other messaging
> service. I find that very surprising. Do Apple executives never
> use iMessage to discuss work? Nor Epic’s? If anyone with legal
> expertise can explain why this is, let me know.


I got a few answers from readers. Basically, there’s little that would stop either side in a lawsuit from demanding access to private messages from services like iMessage, WhatsApp, Signal, Telegram, etc. [Correction: [Telegram should not be in that list](https://daringfireball.net/linked/2022/03/25/telegram-encryption).] In criminal investigations, of course, law enforcement often does attempt to obtain such messages — law enforcement tries to obtain *everything*. But in many civil proceedings there’s an unspoken gentleperson’s agreement not to pursue such messages through discovery, being deemed too broad, too personal, too invasive. Technically, there’s a big difference between these services and email. Email is stored unencrypted on a server. The aforementioned messaging services are end-to-end encrypted. You’d have to get them from the individual parties’ devices — presuming they weren’t deleted.


So what I don’t get about Google’s “Communicate With Care” policy is why it involves email at all. Why not a policy recommending against using email, period, for anything deemed confidential? I get that Google is in [a uniquely awkward position](https://arstechnica.com/gadgets/2021/08/a-decade-and-a-half-of-instability-the-history-of-google-messaging-apps/) regarding post-email messaging services, but how about just using a service other than email that’s end-to-end encrypted? Or discussing all such matters in person or over voice? Part of me thinks this “Communicate With Care” policy at Google is just arrogant, but more than that, I think it’s just foolishly stubborn. If you don’t want it discovered, don’t put it in email.


On the other hand, [as Eric Schmidt himself once advised](https://www.eff.org/deeplinks/2009/12/google-ceo-eric-schmidt-dismisses-privacy), “If you have something that you don’t want anyone to know, maybe you shouldn’t be doing it in the first place.”


---

1. Speaking of footnotes, post-publication, a friend pointed me to at least one iMessage exchange that *was* entered into evidence in Epic v. Apple — exhibit PX-0276, between Apple employees Herve Sibert and Eric Friedman. I can’t find a link online, but it was part of a trove of evidence that was briefly hosted on Box.com during the trial. I’ll host [a copy of the PDF here](https://daringfireball.net/misc/2022/03/PX-0276.pdf). It doesn’t strike me as particularly interesting in and of itself, but it does show that at least one iMessage exchange was entered into evidence. ↩︎



| **Previous:** | [The Apple Studio Display](https://daringfireball.net/2022/03/the_apple_studio_display) |
| **Next:** | [Apple’s Dance With the Netherlands ACM Continues](https://daringfireball.net/2022/04/apple_netherlands_acm_dance) |


PreviousNext