---
title: "The Case For Case Insensitivity"
date: 2005-12-04
url: https://blog.codinghorror.com/the-case-for-case-insensitivity/
slug: the-case-for-case-insensitivity
word_count: 483
---

One of the most pernicious problems with C-based languages is that **they’re case-sensitive**. While this decision may have made sense in 1972 [when the language was created](https://web.archive.org/web/20051204084401/http://cm.bell-labs.com/cm/cs/who/dmr/chist.html), one wonders why the [sins of Kernighan and Ritchie](https://web.archive.org/web/20051204084148/http://cm.bell-labs.com/cm/cs/cbook/) have been blindly perpetuated for the last thirty-three years.


I realize this is a religious issue. I’m not attempting to change anyone’s mind. I’m merely voicing my discontent with the status quo. Thirty plus years later, does case sensitivity still make sense? Julian at OddThinking makes a compelling argument that it doesn’t in [The Case for Case-Preserving, Case-Insensitivity](http://www.somethinkodd.com/oddthinking/2005/10/27/the-case-for-case-preserving-case-insensitivity/):


> Suppose I declare that “KEANU REEVES interferes with elephants.” Can I claim that I was not libelling the wooden Hollywood actor, purely because I spelt his name in all-caps? Can I claim to a judge that KEANU REEVES was a undeclared identifier and therefore the entire statement was semantically meaningless? Of course not. The English language is flexible enough to recognize that “KEANU” and “Keanu” are the same name. Even mail addressed to “KeAnU rEeVeS” will be delivered to the correct person.
> If a computer can also disambiguate this accurately, it should do so too. If the software fails to adapt to the similarity of upper- and lower-case, it leads to frustration.
> For me, an example of this frustration appears in both Python and PHP. Each of them have the same killer combination: they are case-sensitive with identifiers, but they are scripting language that do not resolve identifiers at parse-time. **I consistently fall for the same traps. A distressingly large percentage of my debugging time is spent correcting mistyped identifiers - often not detected until several minutes into a test run. The most common mistyping I make is incorrect capitalization.** Of those, the two most common capitalization errors I make are: HOlding DOwn THe SHift KEy TOo LOng, and being inconsistent in CamelCasing the term “fileName” (I never did resolve satisfactorily whether it was one word or two!)


However you feel about case sensitivity, the bottom line has to be this: does it cost you productivity? The answer is undeniably yes, [as Scott Hanselman notes](https://web.archive.org/web/20060421153558/http://www.hanselman.com/blog/CommentView,guid,a393244f-bd14-49d3-b76e-ac94753e00d8.aspx):


> I spend an hour today debugging a possible problem only to notice that “SignOn!”= “Signon.”
> **If I had a nickel for every time Case-Sensitivity or Case-Insensitivity bit me, I’d have like seven or eight bucks. Seriously.**
> Moral: Know if whatever you’re working on cares about Case, and if it does, make a Post-It to remind you and stick it to your monitor.


There’s nothing we can do about existing tools and languages that are case sensitive, but we can make sure we don’t perpetuate past mistakes. Unless you have extremely compelling reasons to make something case-sensitive, **case insensitivity is a much more human being friendly design choice. **Designing software that’s easier for machines is questionable at best.

[case sensitivity](https://blog.codinghorror.com/tag/case-sensitivity/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
