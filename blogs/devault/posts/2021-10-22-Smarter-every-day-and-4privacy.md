---
title: "How SmarterEveryDay's 4privacy can, and cannot, meet its goals"
date: 2021-10-22
url: https://drewdevault.com/2021/10/22/Smarter-every-day-and-4privacy.html
slug: Smarter-every-day-and-4privacy
word_count: 1908
---

I don’t particularly find myself to be a fan of the SmarterEveryDay YouTube
channel, simply for being outside of Destin’s target audience most of the time.
I understand that Destin, the channel’s host, is a friendly person and a great
asset to his peers, and that he generally strives to do good. When I saw that he
was involved in a Kickstarter to develop a privacy product, it piqued my
interest. As a privacy advocate and jaded software engineer, I set out to find
out what it’s all about.

*You can watch the YouTube video [here](https://www.youtube.com/watch?v=KMtrY6lbjcY), and a short follow-up [here](https://www.youtube.com/watch?v=Hy6STq337qo).*

There are several things to praise here. I honestly thought that Destin’s
coverage of the topic of privacy for the layman was really well presented, and
took some notes to use the next time I’m explaining privacy issues to my
friends. The coverage of the history of wiretapping and the pivotal role played
by 9/11, complete with an empathetic view of the mindset of American adults
contemporary to it that many find hard to express, along with great drone shots
of Big Tech’s mysterious datacenters, this is all great stuff. For the right
project, Destin is a valuable asset with a large audience and a lot of
experience in making complex issues digestible for the every-person, and
4privacy is lucky to have access to him.

A lot of the buzzwords and things found on their  [technology page](https://4privacy.com/our-technology/)  are
promising as well. The focus on end-to-end encryption and zero-knowledge
principles,  *and*  the commitment to open source, are absolutely necessary and
are great to see here. A lot of the tech described, although briefly, seems like
it’s on the right track. The ability to use your own service provider, and the
focus on decentralization and federation, is very good.

I do have some concerns, however. Let’s break them down into these categories:

1. Incentives and economics
2. Responsibilities and cultivating trust
3. Ambitions and feasibility

Given the value ($$$) associated with private user information, it’s important
to know that the trove of private information overseen by a company like this is
safe from threats from the robber-barons of tech. 4privacy is  [looking for
investors](https://4privacy.com/contact-us/) , which is a red flag: investors demand a return, and if the
product isn’t profitable, user data is the first thing up for auction. So, how
will 4privacy make money? We need to know. They might say that the E2EE prevents
them from directly monetizing user data, and they’re right, but that’s only for
today. If they become a market incumbent, they will have the power to change the
technology in a way which compromises privacy faster than we can move to another
system, and we need to understand that this will not happen.

Growing consumer awareness in privacy issues over the past decade, combined with
a generally low level of technology literacy in the population, has allowed a
lot of grifters to arise. One of the common forms these grifts take is seen in
the rise of VPN companies, which prey on consumer fear and often use YouTube as
a marketing channel,  [including on Destin’s previous videos](https://www.youtube.com/watch?v=OdPoVi_h0r0) . Another giant,
flaming red flag appears whenever cryptocurrency is involved. In general terms,
the privacy space is thoroughly infested with bad actors, which makes matters of
trust very difficult. 4privacy needs to be prepared to be very honest and
transparent with not only their tech, but their financial structure and
incentives. With SourceHut, I had to  *engineer*  our incentives to suit stated
goals, and I communicate this to users so that they can make informed choices
about us. 4privacy would be wise to take similar steps, in full view of the
public.

Empowering users to make informed choices leads me into our next point: is
4privacy ready to bear the burden of responsibility for this system? As far as I
can glean from their mock-ups, they plan to be handling your government IDs,
passwords, healthcare information, confidential attorney/client communications,
and so on.  The consequences of having this information compromised are grave,
and this demands world-class security. It’s also extremely important for
4privacy to be honest with their users about what their security model can, and
cannot, make promises about.

You must be honest with your users, and help them to understand how the system
works, and when it doesn’t work, so that they can make informed choices about
how to trust it. This can be difficult when the profit motive is involved,
because they might conclude that they  *don’t*  want to use your service. It’s
even more difficult when you exist in a space full of grifters that are happy to
tell sweet lies to your users about fixing all of their problems. However, it
must be done.

Privacy tools are relied upon by vulnerable people facing challenging
situations. If you promise something you cannot deliver on, and they depend on
you to keep their information private in impossible conditions, when the other
shoe drops there could be dramatic consequences for their lives. If a journalist
in a war-torn country depends on you to keep their documents private, and you
fail, they could end up in prison or a labor camp or splattered on the wall of a
dark alley, and it’ll have been your fault. You  *must*  be forthright and
realistic with users about how your system can and cannot keep them safe. I hope
Destin’s future videos in the privacy series will cover how the system works in
more detail, including its limitations. He is skilled at explaining complicated
topics in a comprehensible manner for everyday people to understand, and I hope
he will leverage these skills here.

I have already noticed one place where they have failed to be honest in their
limitations, however, and it presents a major concern for me. Much of their
marketing speaks of the ability to  *revoke*  access to your private information
 *after*  a third-party has been provided access to it. This is, frankly, entirely
impossible, and I think it is extraordinarily irresponsible to design your
application in a manner that suggests that it can be done. To keep things short,
I’ll refute the idea as briefly as possible: what’s to stop someone from taking
a picture of the phone while it’s displaying your private info? Or writing it
down? When you press the “revoke” button in the app, and it dutifully disappears
from their phone screen, 1  the private information is still written on a piece
of paper in their desk drawer and you’re none the wiser. The application has
given you a  *false sense of security* , which is a major problem for a
privacy-oriented tool.

You  *can*  work in this problem space, albeit under severely limited constraints.
For example, consider how the SSH agent works: an application which wants to use
your private keys to sign something can ask the agent for help, but the agent
will not provide the cryptographic keys for it to use directly — the agent
will do the cryptographic operation on the application’s  *behalf*  and send the
 *results*  to the application to use. These constraints limit the use-cases
significantly, such that, for example, you could not send someone your social
security number using this system. You could, however, design a protocol in
which an organization which needs to verify your identity can ask, in
programmatic terms, “is this person who they say they are?”, and 4privacy
answers, possibly consulting their SSN, “yes” or “no”. This does not seem to be
what they’re aiming for, however.

So, with all of this in mind, how ambitious is their idea as a whole? Is it
feasible? What kind of resources will they need to pull it off?

In short, this idea is extraordinarily ambitious. They are designing a novel
cryptosystem, which is an immediate red flag: designing a secure cryptosystem is
one of the most technologically challenging feats a programming team can
undertake. Furthermore, they’re building a distributed, federated system, which
is itself a highly complex and challenging task, even more so when the system is
leveraged to exchange sensitive information. It can be done, but it takes an
extraordinarily talented team with hard-core technical chops and a lot of
experience.

What’s more, if they were to do this well, it would involve developing and
standardizing open protocols. This requires a greater degree of openness and
community participation than  [they are planning to do](https://github.com/4PrivacyEngine/4PrivacyEngine-Core) . Furthermore, they
need to get others to agree to implement these protocols, which involves solving
social and political problems — both in technical and non-technical
senses. For instance, the Dutch government stores much of my personal
information in the DigiD system. Will they be able to convince the Netherlands
to work with their protocols? How about every other country? And, if they want
me to store my health insurance in the app, how are they going to convince my
doctor to use the app to receive it? And how about every other doctor? And what
about all of the other domains they want to be involved in outside of healthcare
data? Will they interoperate with legacy systems to achieve the market
penetration they need? Will those legacy systems provide for their end-to-end
encryption needs, and if not, will users understand the consequences?

I’m not saying that any of this is impossible — only that it is
extraordinarily difficult to pull off. Extraordinary projects require
extraordinary resources.  They will need multiple highly talented engineering
teams working in parallel, and the support staff necessary to keep them going.

Their goal on Kickstarter, which was quickly met and exceeded, is $175,000. This
is nowhere near enough, so either they aren’t going to pull it off, or they have
more money from somewhere else. Destin is acknowledged as an investor, and they
are seeking more investments on their website — how much money, and from
whom, now and in the future? By taking the lion’s share from entities other than
their users, they have set up concerning incentives in which the entities
responsible for private data have millions on the line and are itchy to get
returns, and the entities whom the private data concerns haven’t been invited to
the negotiating table.

In short, I would urge them to do the following:

* Make clear their funding sources, incentive model, and plans for monetization.
Tell everyone the pitch they tell to private investors.
* Publish their whitepaper draft and invite public comment now, rather than when
it’s “finished”. Consider doing the same with the source code.
* Work to inform potential users about how the technology works, to the extent
that they can make informed choices about it. Destin would be a great help for
this.

4privacy should generally institute a policy of greater transparency and
openness by default, preferring to keep private only what they absolutely must.
There is no shame in iterating on an incomplete product in the view of the
public. On the contrary, I am quite proud that my business works in this manner.

The fundraising campaign quickly met its goal and will presumably only continue
to grow in the coming weeks — it’s reasonably certain that it will close
with at least $1M raised. Having met their goal, the product will presumably
ship, and we’ll see the answers to these questions eventually. The team has a
lot of work ahead of them: good luck.

1. And there’s no guarantee that it will, for the record. ↩︎
