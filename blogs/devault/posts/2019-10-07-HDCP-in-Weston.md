---
title: "Why Collabora really added Digital Restrictions Management to Weston"
date: 2019-10-07
url: https://drewdevault.com/2019/10/07/HDCP-in-Weston.html
slug: HDCP-in-Weston
word_count: 1170
---

A recent article from Collabora,  [Why HDCP support in Weston is a good
thing](https://www.collabora.com/news-and-blog/blog/2019/10/03/why-hdcp-support-in-weston-is-a-good-thing/) , proports to offer a lot of insight into why
 [HDCP](https://en.wikipedia.org/wiki/High-bandwidth_Digital_Content_Protection)  - a Digital Restrictions Management (DRM) related technology - was
added to  [Weston](https://gitlab.freedesktop.org/wayland/weston)  - a well known basic Wayland compositor which was once
the reference compositor for Wayland. But this article is gaslighting you.
There is one reason and one reason alone that explains why HDCP support landed
in Weston.

Q: Why was HDCP added to Weston?

A: $$$$$

Why does Collabora want you to  *believe*  that HDCP support in Weston is a good
thing? Let’s look into this in more detail. First:  *is*  HDCP a bad thing?

DRM (Digital Restrictions Management) is the collective term for software which
attempts to restrict the rights of users attempting to access digital media.
It’s mostly unrelated to Direct Rendering Manager, an important Linux subsystem
for graphics which is closely related to Wayland. Digital Restrictions
Management is software used by media owners to prevent you from enjoying their
content except in specific, pre-prescribed ways.

There is universal agreement among the software community that DRM is
ineffective. Ultimately, these systems are defeated by the simple fact that no
amount of DRM can stop you from pointing your camera at your screen and pushing
record. But in practice, we don’t even need to resort to that - these systems
are far too weak to demand such measures.  [Here’s a $100 device on Amazon which
can break HDCP](https://www.amazon.com/HSV321/dp/B07C6KCBYB) . DRM is shown to be impossible even in  *theory* , as the
decryption keys have to live somewhere in your house in order to watch movies
there. Exfiltrating them is just a matter of putting forth the effort.  For most
users, it hardly requires any effort to bypass DRM - they can just punch “watch
[name of movie] for free” into Google. It’s well-understood and rather obvious
that DRM systems completely and entirely fail at their stated goal.

No reasonable engineer would knowingly agree to adding a broken system like that
to their system, and trust me - the entire engineering community has been made
well-aware of these faults. Any other system with these obvious flaws would be
discarded immediately, and if the media industry hadn’t had their hands firmly
clapped over their ears, screaming “la la la”, and throwing money at the
problem, it would have been. But, just adding a broken system isn’t necessarily
going to hurt much.  The problem is that, in its failure to achieve its stated
goals, DRM brings with it some serious side-effects. DRM is closely tied to
nonfree software - the RIAA mafia wants to keep their garbage a secret, after
all. Moreover, DRM takes away the freedom to play your media when and where you
want. Why should you have to have an internet connection? Why can’t you watch it
on your ancient iPod running Rockbox? DRM exists to restrict users from doing
what they want. More sinisterly, it exists to further the industry’s push to
end consumer ownership of its products - preferring to steal from you monthly
subscription fees and lease the media to you. Free software maintainers are
responsible for protecting their users from this kind of abuse, and putting DRM
into our software betrays them.

The authors are of the opinion that HDCP support in Weston does not take away
any rights from users. It doesn’t  *stop*  you from doing anything. This is true,
in the same way that killing environmental regulations doesn’t harm the
environment. Adding HDCP support is handing a bottle of whiskey to an abusive
husband. And the resulting system - and DRM as a whole - is known to be
inherently broken and ineffective, a fact that they even acknowledge in their
article. This feature  *enables*  media companies to abuse  *your*  users. Enough
cash might help some devs to doublethink their way out of it, but it’s true all
the same. They added these features to help abusive companies abuse their users,
in the hopes that they’ll send back more money or more patches. They say as much
in the article, it’s no secret.

Or, let’s give them the benefit of the doubt: perhaps their bosses forced them
to add this 1 . There have been other developers on this ledge, and I’ve talked
them down. Here’s the thing: it worked. Their organizations didn’t pursue DRM
any further. You are not the lowly code monkey you may think you are. Engineers
have real power in the organization. You can say “no” and it’s your
responsibility to say “no” when someone asks you to write unethical code.

Some of the people I’ve spoken to about HDCP for Wayland, particularly for
Weston, are of the opinion that “a protocol for it exists, therefore we will
implement it”. This is reckless and stupid. We already know what happens when
you bend the knee to our DRM overlords: look at Firefox. In 2014, Mozilla
added DRM to Firefox after a year of fighting against its standardization in the
W3C (a  [captured](https://en.wikipedia.org/wiki/Regulatory_capture)  organization which governs 2  web standards). They
capitulated, and it did absolutely nothing to stop them from being steamrolled
by Chrome’s growing popularity. Their market-share freefall didn’t even slow
down in 2014, or in any year since 3 . Collabora went down without a fight in
the first place.

Anyone who doesn’t recognize that self-interested organizations with a great
deal of resources are working against  *our*  interests as a free software
community is an idiot. We are at war with the bad actors pushing these systems,
and they are to be  [given no quarter](https://en.wikipedia.org/wiki/No_quarter) .
Anyone who realizes this and turns a blind eye to it is a coward. Anyone who
doesn’t stand up to their boss, sits down, implements it in our free software
ecosystem, and cashes their check the next Friday - is not only a coward, but a
traitor to their users, their peers, and to society as a whole.

“HDCP support in Weston is a good thing”? It’s a good thing for  *you* , maybe.
It’s a good thing for media conglomerates which want our ecosystem crushed
underfoot. It’s a bad thing for your users, and you know it, Collabora. Shame on
you for gaslighting us.

However… the person who  *reverts*  these changes is a hero, even in the face of
past mistakes. Weston, Collabora, you still have a chance to repent. Do what you
know is right and stand by those principles in the future.

P.S. To make sure I’m not writing downers all the time, rest assured that the
next article will bring good news - RaptorCS has been working hard to correct
the issues I raised in my last article.

1. This is just for the sake of argument. I’ve spoken 1-on-1 with some of the developers responsible and they stand by their statements as their personal opinions. ↩︎
2. Or at least attempts to govern. ↩︎
3. [Source: StatCounter](https://en.wikipedia.org/wiki/File:StatCounter-browser-ww-monthly-200901-201905.png). Measuring browser market-share is hard, collect your grain of salt [here](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers). ↩︎
