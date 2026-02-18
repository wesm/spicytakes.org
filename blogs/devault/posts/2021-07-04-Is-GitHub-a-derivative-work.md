---
title: "Is GitHub a derivative work of GPL'd software?"
date: 2021-07-04
url: https://drewdevault.com/2021/07/04/Is-GitHub-a-derivative-work.html
slug: Is-GitHub-a-derivative-work
word_count: 804
---

GitHub recently announced a tool called  [Copilot](https://copilot.github.com) , a tool which uses machine
learning to provide code suggestions, inciting no small degree of controversy.
One particular facet of the ensuing discussion piques my curiosity: what happens
if the model was trained using software licensed with the GNU General Public
License?

*Disclaimer: I am the founder of a company which competes with GitHub.*

The GPL is among a family of licenses considered “copyleft”, which are
characterized by their “viral” nature. In particular, the trait common to
copyleft works is the requirement that “derivative works” are required to
publish their new work under the same terms as the original copyleft license.
Some weak copyleft licenses, like the Mozilla Public License, only apply to any
changes to specific files from the original code. Stronger licenses like the GPL
family affect the broader work that any GPL’d code has been incorporated into.

[A recent tweet by @mitsuhiko](https://twitter.com/mitsuhiko/status/1410886329924194309)  notes that Copilot can be caused to
produce, verbatim, the famous fast inverse square root function from Quake III
Arena: a codebase distributed under the GNU GPL 2.0 license. This raises an
interesting legal question: is the work produced by a machine learning system,
or even the machine learning system itself, a derivative work of the inputs to
the model?   [Another tweet](https://twitter.com/eevee/status/1410037309848752128)  suggests that, if the answer is “no”,
GitHub Copilot can be used as a means of washing the GPL off of code you want to
use without obeying its license. But, what if the answer is “yes”?

I won’t take a position on this question 1 , but I will point out something
interesting: if the answer is “ *yes* , machine learning models create derivative
works of their inputs”, then GitHub may itself now be considered a derivative
work of copyleft software. Consider this statement from GitHub’s blog post on
the subject:

> During GitHub Copilot’s early development, nearly 300 employees used it in
> their daily work as part of an internal trial.

—  [Albert Ziegler: A first look at rote learning in GitHub Copilot suggestions](https://docs.github.com/en/github/copilot/research-recitation)

If 300 GitHub employees used Copilot as part of their daily workflow, they are
likely to have incorporated the output of Copilot into nearly every software
property of GitHub, which provides network services to users. If the model was
trained on software using the GNU Affero General Public License (AGPL), and the
use of this model created a derivative work, this may entitle all GitHub users
to receive a copy of GitHub’s source code under the terms of the AGPL,
effectively forcing GitHub to become an open source project. I’m normally
against GPL enforcement by means of pulling the rug out from underneath someone
who made an honest mistake 2 , but in this case it would certainly be a
fascinating case of comeuppance.

Following the Copilot announcement, many of the ensuing discussions hinted to me
at a broader divide in the technology community with respect to machine
learning. I’ve seen many discussions having to wrestle with philosophical
differences between participants, who give different answers to more fundamental
questions regarding the ethics of machine learning: what rights should be, and
are, afforded to the owners of the content which is incorporated into training
data for machine learning? If I want to publish a work which I  *don’t*  want to
be incorporated into a model, or which, if used for a model, would entitle the
public to access to that model, could I? Ought I be allowed to? What if the work
being used is my personal information, collected without my knowledge or
consent? What if the information is used against me, for example in making
lending decisions? What if it’s used against society’s interests at large?

The differences of opinion I’ve seen in the discussions born from this
announcement seem to suggest a substantial divide over machine learning, which
the tech community may have yet to address, or even understand the depth of. I
predict that GitHub Copilot will mark one of several inciting events which start
to rub some of the glamour off of machine learning technology and gets us
thinking about the ethical questions it presents. 3

1. Though I definitely have one 😉 ↩︎
2. I support GPL enforcement, but I think we would be wise to equip users with a clear understanding of what our license entails, so that those mistakes are less likely to happen in the first place. ↩︎
3. I also predict that capitalism will do that thing it normally does and sweep all of the ethics under the rug in any scenario in which addressing the problem would call their line of business into doubt, ultimately leaving the dilemma uncomfortably unresolved as most of us realize it’s a dodgy ethical situation while simultaneously being paid to not think about it too hard. ↩︎
