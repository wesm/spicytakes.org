---
title: "It is important for free software to use free software infrastructure"
date: 2022-03-29
url: https://drewdevault.com/2022/03/29/free-software-free-infrastructure.html
slug: free-software-free-infrastructure
word_count: 1307
---

*Disclaimer: I founded a project and a company that focuses on free software
infrastructure. I will elect not to name them in this post, and will only
recommend solutions I do not have a vested interest in.*

Free and open source software (FOSS) projects need infrastructure. Somewhere to
host the code, to facilitate things like code review, end-user support, bug
tracking, marketing, and so on. A common example of this is the “forge”
platform: infrastructure which pitches itself as a one-stop shop for many of the
needs of FOSS projects in one place, such as code hosting and review, bug
tracking, discussions, and so on. Many projects will also reach for additional
platforms to provide other kinds of infrastructure: chat rooms, forums, social
media, and more.

Many of these needs have  non-free ,
proprietary solutions available. GitHub is a popular proprietary code forge, and
GitLab, the biggest competitor to GitHub, is partially non-free. Some projects
use Discord or Slack for chat rooms, Reddit as a forum, or Twitter and Facebook
for marketing, outreach, and support; all of these are non-free. In my opinion,
relying on these platforms to provide infrastructure for your FOSS project is a
mistake.

When your FOSS project chooses to use a non-free platform, you give it an
official vote of confidence on behalf of your project. In other words, you lend
some of your project’s credibility and legitimacy to the platforms you choose.
These platforms are defined by network effects, and your choice is an investment
in that network. I would question this investment in and of itself, and the
wisdom of offering these platforms your confidence and legitimacy, but there’s a
more concerning consequence of this choice as well: an investment in a non-free
platform is also a  *divestment*  from the free alternatives.

Again, network effects are the main driver of success in these platforms. Large
commercial platforms have a lot of advantages in this respect: large marketing
budgets, lots of capital from investors, and the incumbency advantage. The
larger the incumbent platform, the more difficult the task of competing with it
becomes. Contrast this with free software platforms, which generally don’t have
the benefit of large amounts of investment or big marketing budgets. Moreover,
businesses are significantly more likely to play dirty to secure their foothold
than free software projects are. If your own FOSS projects compete with
proprietary commercial options, you should be very familiar with these
challenges.

FOSS platforms are at an inherent disadvantage, and your faith in them, or lack
thereof, carries a lot of weight. GitHub won’t lose sleep if your project
chooses to host its code somewhere else, but choosing  [Codeberg](https://codeberg.org) , for example,
means a lot to them. In effect, your choice matters disproportionately to the
free platforms: choosing GitHub hurts Codeberg much more than choosing Codeberg
hurts GitHub. And why should a project choose to use your offering over the
proprietary alternatives if you won’t extend them the same courtesy? FOSS
solidarity is important for uplifting the ecosystem as a whole.

However, for some projects, what ultimately matters to them has little to do
with the benefit of the ecosystem as a whole, but instead considers only the
potential for their project’s individual growth and popularity. Many projects
choose to prioritize access to the established audience that large commercial
platforms provide, in order to maximize their odds of becoming popular, and
enjoying some of the knock-on effects of that popularity, such as more
contributions. 1  Such projects would prefer to exacerbate the network
effects problem rather than risk some of its social capital on a less popular
platform.

To me, this is selfish and unethical outright, though you may have different
ethical standards. Unfortunately, arguments against most commercial platforms
for any reasonable ethical standard are available in abundance, but they tend to
be easily overcome by confirmation bias. Someone who may loudly object to the
practices of the US Immigration and Customs Enforcement agency, for example, can
quickly find some justification to continue using GitHub despite their
collaboration with them. If this example isn’t to your tastes, there are many
examples for each of many platforms. For projects that don’t want to move, these
are usually swept under the rug. 2

But, to be clear, I am not asking you to use inferior platforms for
philosophical or altruistic reasons. These are only one of many factors which
should contribute to your decision-making, and aptitude is another valid factor
to consider. That said, many FOSS platforms are, at least in my opinion,
functionally superior to their proprietary competition. Whether their
differences are better for your project’s unique needs is something I must leave
for you to research on your own, but most projects don’t bother with the
research at all. Rest assured: these projects are not ghettos living in the
shadow of their larger commercial counterparts, but exciting platforms in their
own right which offer many unique advantages.

What’s more, if you need them to do something differently to better suit your
project’s needs, you are empowered to improve them. You’re not subservient to
the whims of the commercial entity who is responsible for the code, waiting for
them to prioritize the issue or even to care about it in the first place. If a
problem is important to you, that’s enough for you to get it fixed on a FOSS
platform. You might not think you have the time or expertise to do so (though
maybe one of your collaborators does), but more importantly, this establishes a
mentality of collective ownership and responsibility over all free software as a
whole — popularize this philosophy and it could just as easily be you
receiving a contribution in a similar manner tomorrow.

In short, choosing non-free platforms is an individualist, short-term investment
which prioritizes your project’s apparent access to popularity over the success
of the FOSS ecosystem as a whole. On the other hand, choosing FOSS platforms is
a collectivist investment in the long-term success of the FOSS ecosystem as a
whole, driving its overall growth. Your choice matters. You can help the FOSS
ecosystem by choosing FOSS platforms, or you can hurt the FOSS ecosystem by
choosing non-free platforms. Please choose carefully.

Here are some recommendations for free software tools that facilitate common
needs for free software projects:

* Code forges:  [Codeberg](https://codeberg.org) ,  [Gitea](https://gitea.io/en-us) *,  [Gerrit](https://www.gerritcodereview.com) *,  [GitLab](https://gitlab.com) †
* Instant messaging:  [Matrix](https://matrix.org/) ,  [Libera Chat](https://libera.chat) 3
* Publishing:  [Codeberg pages](https://codeberg.page/) ,  [Write.as](https://write.as/) ,  [PeerTube](https://joinpeertube.org/)
* Social media:  [Mastodon](https://joinmastodon.org) ,  [Lemmy](https://join-lemmy.org/)
* Mailing lists:  [FreeLists](https://www.freelists.org) ,  [public-inbox](https://public-inbox.org/public-inbox-overview.html) *,  [Mailman](http://www.list.org) *

* Self-hosted only  
 
† Partially non-free, recommended only if no other solutions are suitable

P.S. If your project is already established on non-free platforms, the easiest
time to revisit this choice is right now. It will only ever get more difficult
to move as your project grows and gets further established on proprietary
platforms. Please consider moving sooner rather than later.

1. I should note here that I’m uncritically presenting “popularity” as a good thing for a project to have, which aligns, I think, with the thought processes of the projects I’m describing. However, the truth is not quite so. Perhaps a topic for another day’s blog post. ↩︎
2. A particularly egregious example is the [Ethical Source](https://ethicalsource.dev/) movement. I disagree with them on many grounds, but pertinent to this article is the fact that they publish (non-free) software licenses which advocate for anti-capitalist sentiments like worker rights and ethical judgements such as non-violence, doing so on… GitHub and Twitter, private for-profit platforms with a myriad of published ethical violations. ↩︎
3. I have made the arguments from this post to Libera staff many times, but they still rely on GitHub, Twitter, and Facebook. They were one of the motivations for writing this post. I hope that they have a change of heart someday. ↩︎
