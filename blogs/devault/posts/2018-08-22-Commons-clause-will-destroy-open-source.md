---
title: "The Commons Clause will destroy open source"
date: 2018-08-22
url: https://drewdevault.com/2018/08/22/Commons-clause-will-destroy-open-source.html
slug: Commons-clause-will-destroy-open-source
word_count: 1244
---

An alarmist title, I know, but it’s true. If the  [Commons
clause](https://commonsclause.com/)  were to be adopted by all open source
projects, they would cease to be open source 1 , and therefore the Commons
clause is trying to destroy open source. When this first appeared I spoke out
about it in discussion threads around the net, but didn’t think anyone would
take it seriously. Well, yesterday, some parts of Redis  [became proprietary
software](https://redislabs.com/community/commons-clause/) .

The Commons Clause promoted by Kevin Wang presents one of the greatest
existential threats to open source I’ve ever seen. It preys on a vulnerability
open source maintainers all suffer from, and one I can strongly relate to. It
 *sucks*  to not be able to make money from your open source work. It  *really* 
sucks when companies are using your work to make money for themselves. If a
solution presents itself, it’s tempting to jump at it. But the Commons Clause
doesn’t present a solution for supporting open source software. It presents a
framework for turning open source software into proprietary software.

What should we do about open source maintainers not getting the funding
they need? It’s a very real problem, and one Kevin has  [explicitly asked
us](https://twitter.com/kevinverse/status/1032074268291424257)  to talk about
before we criticise his solution to it. I would be happy to share my thoughts.
I’ve struggled for many years to find a way to finance myself as the maintainer
of many dozens of projects. For a long time it has been a demotivating struggle
with no clear solutions, a struggle which at one point probably left me
vulnerable to the temptations offered by the Commons Clause. But today, the
situation is clearly improving.

Personally, I have a harder go of it because very little of my open source
software is appealing to the businesses that have the budget to sponsor them.
Instead, I rely on the (much smaller and less stable) recurring donations of my
individual users. When I started accepting these, I did not think that it was
going to work out. But today, I’m making far more money from these donations
than I ever thought possible 2 , and I see an upwards trend which will
eventually lead me to being able to work on open source full time. If I were
able to add only a few business-level sponsorships to this equation, I think I
would easily have already reached my goals.

There are other options for securing financing for open source, some of which
Redis has already been exploring. Selling a hosted and supported version of
your service is often a good call. Offering consulting support for your
software has also worked for many groups in the past. Some projects succeed with
(A)GPL for everyone and BSD for a price. These are all better avenues to
explore - making your software proprietary is a tragic alternative that should
not be considered.

We need to combine these methods with a greater appreciation for open source in
the business community. Businesses need engineers - appeal to your peers so they
can appeal to the money on behalf of the projects they depend on. A $250/mo
recurring donation to would be a drop in the bucket of most businesses, but a
major boon to any open source project, with which the business will almost
certainly see tangible value-add as a result. When I get to work today I’m going
to identify open source projects we use that accept donations and make the
plea 3 , and keep making the plea week over week until money is spent. You
should, too.

Redis also stands out as a cautionary entry in the history of Contributor
License Agreements. Everyone who has contributed to the now-proprietary Redis
modules has had their hard work stolen and sold by RedisLabs under a proprietary
license. I do not sign CLAs and I think they’re a harmful practice for this very
reason. Asking a contributor to sign them is a slap in the face to the good will
which led them to make a contribution in the first place. Don’t sign these and
don’t ask others to.

I respect antirez 4  very much, but I am sorely disappointed in him. He should
have known better and, if you’re reading this, I urge you to roll back your
misguided decision. But the Commons Clause is much more deeply disturbing. What
Kevin is doing will ruin open source software, maybe for good 5 .

I really appreciate some of Kevin’s work.  [FOSSA](https://fossa.io/)  is a really
cool tool that can stand to provide some serious value to the open source
community.  [TL;DR Legal](https://tldrlegal.com/)  is a fantastic tool which has
already delivered a tremendous amount of value to open source, and I’ve
personally referenced it dozens of times. Thank you, honestly, for your work on
improving the legal landscape of open source. With Commons Clause, however,
Kevin has taken it too far.  [The four
freedoms](https://www.gnu.org/philosophy/free-sw.en.html)  are  *important* . The
only solution is to bury the Commons Clause project. Kill the website and GitHub
repository, and we can try to forget this ever happened.

I understand that turning back is going to be hard, which scares me. I know that
Kevin has already put a lot of effort into it and convinced himself that it’s
the Right Thing To Do. It takes work to write the clause, vet it for legal
issues, design a website (a beautiful one, I’ll give you that), and to promote
it among your target audience. I know how hard it is to distance yourself from
something you’ve staked your personal reputation on. You had only the best
intentions 6 , Kevin, but please step back from the ego and do the right thing -
take this down. You stand to undo all of your hard work for the open source
community in one fell swoop with this initiative. I’m begging you, stop while
it’s not too late.

Man, two angry articles in a row. I have more technical articles coming up, I
promise.

**Update 2018-08-23 03:00 UTC:**  Richard Stallman of the Free Software
Foundation reached out asking me to clarify the use of “open source” in this
article. I have refered to the FSF’s document on essential freedoms as a
definition of “open source”. In fact, it is the definition of free software - a
distinct concept. The FSF does not advocate for open source software, but
particularly for free (or “libre”) software, of which there is some intersection
with open source software. For more information on the difference, refer to
 [Richard’s article on the
subject](https://www.gnu.org/philosophy/open-source-misses-the-point.html) .

1. Under both the OSI and FSF definitions. The Commons Clause removes freedom 0 of the [four essential freedoms](https://www.gnu.org/philosophy/free-sw.en.html). ↩︎
2. [Figures here](https://drewdevault.com/donate) ↩︎
3. I intend to do an audit, but I have always (and I encourage you to always) kept an eye on the stuff we use as I come across it, looking for opportunities to donate. ↩︎
4. The maintainer of Redis ↩︎
5. As software gets abandoned, making the license more permissive is the last thing on the maintainer’s minds. So as the body of Commons Clause software grows, the graveyard will only ever fill. ↩︎
6. Honestly, this is a real problem that open source suffers from and I really appreciate the attempt to fix it, misguided as it may have been. But this is not okay, and Kevin needs to recognize the gravity of his mistake and move to correct it. ↩︎
