---
title: "A few ways to make money in FOSS"
date: 2020-11-20
url: https://drewdevault.com/2020/11/20/A-few-ways-to-make-money-in-FOSS.html
slug: A-few-ways-to-make-money-in-FOSS
word_count: 936
---

I work on free and open-source software full time, and I make a comfortable
living doing it. And I don’t half-ass it: 100% of my code is free and
open-source. There’s no proprietary add-ons, no periodic code dumps, just
100% bona-fide free and open source software. Others have often sought my advice
— how can they, too, make a living doing open source?

Well, there’s more than one way to skin a cat. There are many varieties of
software, each with different needs, and many kinds of people, each with
different needs. The exact approach which works for you and your project will
vary quite a bit depending on the nature of your project.

I would generally categorize my advice into two bins:

* You want to make money from your own projects
* You want to make money participating in open source

The first one is more difficult. We’ll start with the latter.

## Being employed in FOSS

One way to make money in FOSS is to get someone to pay you to write free
software. There’s lots of advantages to this: minimal personal risk, at-market
salaries, benefits, and so on, but at the cost of not necessarily getting to
choose what you work on all the time.

I have a little trick that I often suggest to people who vaguely want to work
“in FOSS”, but who aren’t trying to find the monetization potential in their own
projects. Use git to clone the source repositories for some (large) projects
you’re interested in,
 [the kind of stuff you want to work on](https://drewdevault.com/2020/08/10/How-to-contribute-to-FOSS.html) ,
and then run this command:

```
git log -n100000 --format="%ae" | cut -d@ -f2 | sort | uniq -c | sort -nr | less
```

This will output a list of the email domains who have committed to the
repository in the last 100,000 commits. This is a good set of leads for
companies who might be interested in paying you to work on projects like this
😉

Another good way is to explicitly seek out large companies known to work a lot
in FOSS, and see if they’re hiring in those departments. There are some
companies that specialize in FOSS, such as RedHat, Collabora, and dozens more;
and there are large companies with FOSS-specific teams, such as Intel, AMD, IBM,
and so on.

## Making money from your own FOSS work

If you want to pay for the project infrastructure, and maybe beer money for the
weekend, then donations are an easy way to do that. I’ll give it to you
straight, though: you’re unlikely to make a living from donations.  Programmers
who do are a small minority. If you want to make a living from FOSS, it’s
going to be more difficult.

Start by unlearning what you think you know about startups. The toxic startup
culture around venture capital and endless hyper-growth is more stressful, less
likely to succeed, and socially irresponsible. Building a sustainable business
responsibly takes time, careful planning, and hard work. The fast route —
venture capital funded — is going to impose constraints on your business
that will ultimately make it difficult to remain true to your open-source
mission.

And yes, you are building a  *business* . You need to start thinking of your
project as a business and of yourself as a business owner. This undertaking is
going to require developing business skills in planning, budgeting, scheduling,
resource allocation, marketing & sales, compliance, and more. At times, you will
be forced to embrace your inner
 [suit](http://www.catb.org/jargon/html/S/suit.html) . Channel your engineering
problem-solving skills into the business problems.

So, you’ve got the right mindset. What are some business models that work?

[SourceHut](https://sourcehut.org) , my company, has two revenue streams. We have
a hosted SaaS product. It’s open source, and users can choose to deploy and
maintain it themselves, or they can just buy a hosted account from us. The
services are somewhat complex, so the managed offering saves them a lot of time.
We have skilled sysops/sysadmins, support channels, and so on, for paying users.
Importantly, we don’t have a free tier (but we do choose to provide free service
to those who need it, at our discretion).

Our secondary revenue stream is  [free software
consulting](https://sourcehut.org/consultancy) . Our developers work part-time
writing free and open-source software on contracts. We’re asked to help
implement features upstream for various projects, or to develop new open-source
applications or libraries, to share our expertise in operations, and so on, and
charge for these services. This is different from providing paid support or
development on our own projects — we accept contracts to work on  *any* 
open source project.

The other approach to consulting is also possible: paid support and development
on your own projects. If there are businesses that rely on your project, then
you may be able to offer them support or develop new features or bugfixes that
they need, on a paid basis. Projects with a large corporate userbase also
sometimes  *do*  find success in donations — albeit rebranded as
sponsorships. The largest projects often set up foundations to manage them in
this manner.

These are, in my experience, some of the most successful approaches to
monetizing FOSS. You may have success with a combination of these, or with other
business models as well.  Remember to turn that engineering mind of yours
towards the task of monetization, and experiment with and invent new ways of
making money that best suit the kind of software you want to work on.

Feel free to  [reach out](mailto:sir@cmpwn.com)  if you have some questions or
need a sounding board for your ideas. Good luck!
