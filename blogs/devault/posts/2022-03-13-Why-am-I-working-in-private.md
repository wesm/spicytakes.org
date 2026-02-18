---
title: "Why am I building a programming language in private?"
date: 2022-03-13
url: https://drewdevault.com/2022/03/13/Why-am-I-working-in-private.html
slug: Why-am-I-working-in-private
word_count: 1250
---

As many readers are aware, I have been working on designing and implementing a
systems programming language. This weekend, I’ve been writing a PNG file decoder
in it, and over the past week, I have been working on a simple kernel with it as
well. I’m very pleased with our progress so far — I recently remarked that
this language feels like the language I always wanted, and that’s mission
accomplished by any definition I care to consider.

I started the project on December 27th, 2019, just over two years ago, and I
have kept it in a semi-private state since. Though I have not given its name in
public, the git repos, mailing lists, and bug trackers use sourcehut’s
“unlisted” state, so anyone who knows the URL can see them. The website is also
public, though its domain name is also undisclosed, and it is full of
documentation, tutorials, and resources for developers. People can find the
language if they want to, though at this stage the community only welcomes
contributors, not users or onlookers. News of the project nominally spreads by
word of mouth and with calls-to-action on this blog, and to date a total of 30
people have worked on it over the course of 3,029 commits. It is a major,
large-scale project, secret though it may be.

And, though we’ve invested a ton of work into this project together, it remains
as-of-yet unfinished. There is no major software written in our language, though
several efforts are underway. Several of our key goals have yet to be merged
upstream, such as date/time support, TLS, and regular expressions, though,
again, these efforts are well underway. Until we have major useful projects
written in our language, we cannot be confident in our design, and efforts in
these respects do a great deal to inform us regarding any changes which might be
necessary. And some changes are already in the pipeline: we have plans to make
several major revisions to the language and standard library design, which are
certain to require changes in downstream software.

When our community is small and private, these changes are fairly easy to reckon
with. Almost everyone who is developing a project based on our language is also
someone who has worked on the compiler or standard library. Often, the person
who implements a breaking change will also send patches to various downstreams
updating them to be compatible with this change,  *for every extant software
project written in the language* . This is a task which can be undertaken by one
person. We all understand the need for these changes, participate in the
discussions and review the implementations, and have the expertise necessary to
make the appropriate changes to our projects.

Moreover, all of these people are also understanding of the in-development
nature of the project. All users of our language are equipped with the knowledge
that they are expected to help fix the bugs they identify, and with the skills
and expertise necessary to follow-up on this fact. We don’t have to think about
users who stumble upon the project, spend a few hours trying to use it, then
encounter an under-developed part of the language and run out of enthusiasm. We
still lack DWARF support, so debugging is a chore. Sometimes the compiler
segfaults or aborts without printing a useful error message. It’s a
work-in-progress, after all. These kinds of problems can discourage new learners
very fast, and often requires the developers to offer some of their precious
bandwidth to provide expert assistance. With the semi-private model, there are,
at any given time, a very small number of people involved who are new to the
language and require more hands-on support to help them through their problems.

A new programming language is a major undertaking. We’re building one with an
explicit emphasis on simplicity and we’re still not done after two years. When
most people hear about the project for the first time, I don’t want them to find
a half-completed language which they will fail to apply to their problem because
it’s not fleshed out for their use-case. The initial release will have
comprehensive documentation, a detailed specification, and stability guarantees,
so it can be picked up and used in production by curious users on day one. I
want to fast-forward to the phase where people study it to learn how to apply it
to their problems, rather than to learn  *if they can*  apply it to their
problems.

Even though it is under development in private, this project is both “free
software” and “open source”, according to my strict understanding of those terms
as defined by the FSF and OSI. “Open source” does not mean that the project has
a public face. The compiler is GPL 3.0 licensed, the standard library is MPL
2.0, and the specification is CC-BY-ND (the latter is notably less free, albeit
for good reasons), and these details are what matter. Every person who has
worked on the project, and every person who stumbles upon it, possesses the
right to lift the veil of secrecy and share it with the world. The reason they
don’t is because I asked them not to, and we maintain a mutual understanding
regarding the need for privacy.

On a few occasions, someone has discovered the project and taken it upon
themselves to share it in public places, including Hacker News, Lemmy, and
4chan. While this is well within your rights, I ask you to respect our wishes
and allow us to develop this project in peace. I know that many readers are
excited to try it out, but please give us some time and space to ensure that you
are presented with a robust product. At the moment, we anticipate going public
early next year. Thank you for your patience.

Thank you for taking the time to read my thoughts as well. I welcome your
thoughts and opinions on the subject:  [my inbox is always open](mailto:sir@cmpwn.com) . If you
disagree, I would appreciate it if you reached out to me to discuss it before
posting about the project online. And, if you want to get involved, here is a
list of things we could use help with — email me to volunteer if you have
both the time and expertise necessary:

* Cryptography
* Ports for new architectures or operating systems
* Image & pixel formats/conversions
* SQL database adapters
* Signal handling
* JSON parsing & encoding
* Compression and decompression
* Archive formats

If you definitely don’t want to wait for the language to go public, volunteering
in one of our focus areas is the best way to get involved. Get in touch! If not,
then the release will come around sooner than you think. We’re depending on your
patience and trust.

*Update 2022-03-14*

This blog post immediately generated detailed discussions on Hacker News and
Lobsters in which people posted the language’s website and started tearing into
everything they don’t like about it.

It’s not done yet, and the current state of the language is not representative
of the project goals. This post was not a marketing stunt. It was a heartfelt
appeal to your better nature.

You know, I have a lot on my plate. All of it adds up to a lot of stress. I had
hoped that you would help relieve some of that stress by taking me seriously
when I explained my motivations and asked nicely for you to leave us be. I was
wrong.
