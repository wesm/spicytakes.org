---
title: "Dysfunctional Specifications"
date: 2005-11-27
url: https://blog.codinghorror.com/dysfunctional-specifications/
slug: dysfunctional-specifications
word_count: 1281
---

The guys at 37signals [think functional specs are worthless](http://www.37signals.com/svn/archives/001050.php):


> **Don’t write a functional specifications document.** Why? Well, there’s nothing functional about a functional specifications document.
> Functional specifications documents lead to an illusion of agreement. A bunch of people agreeing on paragraphs of text is not real agreement. Everyone is reading the same thing, but they’re often thinking something different. This inevitably comes out in the future when it’s too late. “Wait, that’s not what I had in mind...” “Huh? That’s not how we described it.” “Yes it was and we all agreed on it – you even signed off on it.” You know the drill.
> Functional specifications document are “yes documents.” They’re political. They’re all about getting to “yes” and we think the goal up front should be getting to “no.” Functional specs lead to scope creep from the very start. There’s very little cost in saying “yeah, ok, let’s add that” to a Word document.
> Functional specs are often appeasement documents. They’re about making people feel involved. But, there’s very little reality attached to anything you do when the builders aren’t building, the designers aren’t designing, and the people aren’t using. We think reality builds better products than appeasement.
> Functional specs are about making decisions before you have enough information to decide. They are about predicting the future and we all know how accurate that is.


In lieu of a functional spec, the guys at 37 Signals recommend writing **a simple one page story of what the app should do**. This probably isn’t a functional spec in the traditional sense; it’s more like a vision statement. And you should have a [vision statement](https://blog.codinghorror.com/vision-quest/), because half the developers on your team probably can’t tell you what they’re building anyway.


Linus Torvalds evidently [hates functional specifications](http://kerneltrap.org/node/5725), too:

kg-card-begin: html

> A “spec” is close to useless. I have never seen a spec that was both big enough to be useful and accurate. And I have seen lots of total crap work that was based on specs. It’s the single worst way to write software, because it by definition means that the software was written to match theory, not reality. There are two major reasons to avoid specs:
> They’re dangerously wrong. Reality is different, and anybody who thinks specs matter over reality should get out of kernel programming NOW. When reality and specs clash, the spec has zero meaning. Zilch. Nada. None. It’s like real science: if you have a theory that doesn’t match experiments, it doesn’t matter how much you like that theory. It’s wrong. You can use it as an approximation, but you MUST keep in mind that it’s an approximation.
> Specs have an inevitable tendency to introduce abstraction levels and wording and documentation policies that make sense for a written spec. Trying to implement actual code off the spec leads to the code looking and working like CRAP. The classic example of this is the OSI network model protocols. Classic spec-design, which had absolutely zero relevance for the real world. We still talk about the seven layers model, because it’s a convenient model for discussion, but that has absolutely zero to do with any real-life software engineering. In other words, it’s a way to talk about things, not to implement them. And that’s important. Specs are a basis for talking about things. But they are not a basis for implementing software.
> So please don’t bother talking about specs. Real standards grow up despite specs, not thanks to them.

kg-card-end: html

In defense of functional specs, there’s a [rebuttal of Linus’ position](https://web.archive.org/web/20051222055802/http://pl.atyp.us/wordpress/?p=979) at Canned Platypus. And Joel has a persuasive three-part essay [championing functional specifications](http://www.joelonsoftware.com/articles/fog0000000036.html) that’s chock full of great advice; I highly recommend reading all three parts. Unfortunately, you know you’re in trouble when Joel tells you how hard it is to write functional specifications [that people actually read](http://www.joelonsoftware.com/articles/fog0000000033.html):


> The biggest complaint you’ll hear from teams that do write specs is that “nobody reads them.” When nobody reads specs, the people who write them tend to get a little bit cynical. It’s like the old Dilbert cartoon in which engineers use stacks of 4-inch thick specs to build extensions to their cubicles. At your typical big, bureaucratic company, everybody spends months and months writing boring specs. Once the spec is done, it goes up on the shelf, never to be taken down again, and the product is implemented from scratch without any regard to what the spec said, because nobody read the spec, because it was so dang mind-numbing. The very process of writing the spec might have been a good exercise, because it forced everyone, at least, to think over the issues. But the fact that the spec was shelved (unread and unloved) when it was completed makes people feel like it was all a bunch of work for naught.
> Also, if your spec never gets read, you get a lot of arguments when the finished product is delivered. Somebody (management, marketing, or a customer) says: “wait a minute! You promised me that there would be a Clam Steamer! Where’s the clam steamer?” And the programmers say, “no, actually, if you look on the spec on chapter 3, subchapter 4, paragraph 2.3.0.1, you’ll see it says quite explicitly ‘no clam steamer.’” But that doesn’t satisfy the customer, who is always right, so the grumpy programmers have to go retrofit a clam steamer into the thing (making them even more cynical about specs). Or a manager says, “hey, all the wording on this dialog is too verbose, and there should be an advertisement at the top of every dialog box.” And the programmers say, in frustration, “but you approved the spec which precisely listed the layout and contents of every dialog box!” But of course, the manager hadn’t actually read the spec, because when he tried, his brain started seeping out through his eye sockets, and anyway, it was interfering with his Tuesday golf game.
> So. Specs are good, but not if nobody reads them. As a spec-writer, you have to trick people into reading your stuff, and you should also probably make an effort not to cause any already-too-small brains to leak out through eye-sockets.


**If it takes a writer as good as Joel to trick people into reading functional specs, the rest of us are totally screwed.** I guess that’s hard to see when you’re Joel, but it’s been obvious to me on every project I’ve ever worked on.


Having spent the better part of the last two months writing functional specifications, I’m of two minds on them:

1. Yes, you absolutely should plan what you’re going to do before you do it.
2. No, you shouldn’t try to plan everything you do in excruciating detail, because you’ll forget a million things, then on top of that you’ll encounter a bunch of problems you hadn’t even considered, so you’ll end up rewriting it all anyway.


You have to strike some kind of balance between a one-page vision statement and an obsessively detailed five volume masterwork of a functional spec. I can’t tell you what level of specification is appropriate for what you’re doing, but here’s what has worked for me:

- When in doubt, **err on the side of that one-page vision statement.** At least people will read that. Maybe.
- **Plan a little, then code a little. Repeat.** Planning and implementation should overlap; they’re symbiotic processes. Too much planning is just as wrongheaded as no planning.
- **Your spec should be a dynamic, living document.** It should change and grow along with your code. Have you considered making your spec a Wiki?

[specifications](https://blog.codinghorror.com/tag/specifications/)
[programming](https://blog.codinghorror.com/tag/programming/)
[software development](https://blog.codinghorror.com/tag/software-development/)
