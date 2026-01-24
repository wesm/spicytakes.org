---
title: "The Problem With Configurability"
date: 2005-09-07
url: https://blog.codinghorror.com/the-problem-with-configurability/
slug: the-problem-with-configurability
word_count: 822
---

I’ve recently been experimenting with a [few hand-picked desktop utilities](http://www.hanselman.com/blog/ScottHanselmans2005UltimateDeveloperAndPowerUsersToolList.aspx), but I am rapidly reaching the point of diminishing returns: the effort required to run and maintain all these utilities is greater than the productivity benefit.


Furthermore, if I learn to rely on a highly custom desktop, **I’ve crippled my ability to work on a stock Windows XP or Win2k3 box**. I can certainly bring my favorite apps with me [on a USB key](https://blog.codinghorror.com/whats-on-your-keychain/), but I also have to spend time setting them up on each box I touch. Is it worth it?


Configurability is mixed blessing, even for developers. You can completely customize your VS.NET 2003 environment, including setting all the keymappings to a compatibility mode. But have you ever tried to work on someone else’s “customized” Visual Studio? I do this occasionally when we’re hashing out quick solutions to problems, and if VS.NET is highly customized on that developer’s machine, I can’t get any work done. None of the [standard shortcuts](https://blog.codinghorror.com/visual-studio-net-2003-and-2005-keyboard-shortcuts/) do anything recognizable. We can’t work on the problem together at all. At least not on that machine.


Joel explored a similar topic in chapter 3 of [his UI book](http://www.amazon.com/exec/obidos/ASIN/1893115941) when he asked: [is customization worth it?](http://www.joelonsoftware.com/uibook/chapters/fog0000000059.html)


> The trouble was, I don’t use one computer. I use all kinds of computers. I use other people’s computers. I use three computers fairly regularly at home and three at work. I use computers in the test lab at work. The trouble with customizing your environment is that it just doesn’t propagate, so it’s not even worth the trouble.
> Most advanced users use several computers regularly; they upgrade their computer every couple of years, they reinstall their operating system every three weeks. It’s true that the first time they realized you could completely remap the keyboard in Word, they changed everything around to be more to their liking, but as soon as they upgraded to Windows 95 those settings got lost, and they weren’t the same at work, and eventually they just stopped reconfiguring things. **I’ve asked a lot of my “power user” friends about this; hardly any of them do any customization other than the bare minimum necessary to make their system behave reasonably.**


If customization is a mixed bag for advanced users like us, that can’t bode well for average users:


> Every time you provide an option, you’re asking the user to make a decision. That means they will have to think about something and decide about it. It’s not necessarily a bad thing, but, in general, you should always try to minimize the number of decisions that people have to make.


In other words, [don’t make users think](https://blog.codinghorror.com/dont-make-me-think-second-edition/). Or at least **don’t make them think about anything outside the narrow focus of their immediate goal**. Furthermore, making everything configurable really means the [designer isn’t doing his job](http://usability.typepad.com/confusability/2004/09/the_problems_wi.html). This is something Jakob Nielsen points out in his introduction to the book [Designing Visual Interfaces](http://www.amazon.com/exec/obidos/ASIN/0133033899):


> In the bedroom wall example, people might buy the house anyway and then paint over the wall with a more agreeable color. This example leads me to consider an excuse some developers have for not providing a satisfactory visual interface to their products: “the user can just customize the design to his or her individual taste!” **Leaving the design to the users is the ultimate abdication of the designer’s responsibility to provide a quality product**, and many studies have shown that users are in fact very poor designers and often customize their interface in ways that are detrimental to their productivity (eg, by using color combinations that are [known to cause reduced readability](https://blog.codinghorror.com/code-colorizing-and-readability/) of screen text). Even though there are often reasons to allow users to customize some aspects of their environment, **it is absolutely essential for the designer to give the users a carefully thought out set of defaults to start with.** Also, users will be much more likely to end up with appropriate customized design if they are given some pre-specified (and well-designed) options to choose from as done, for example, in the [Pantone ColorUp](https://web.archive.org/web/20060427041207/http://www.smartcomputing.com/editorial/dictionary/detail.asp?searchtype=2&DicID=18470&RefType=Encyclopedia&guid=) set of recommended color combinations for presentation slides.


There’s an interesting extension of this philosophy in [Ruby on Rails](https://web.archive.org/web/20050907075217/http://www.onlamp.com/pub/a/onlamp/2005/01/20/rails.html) called **convention over configuration**:


> Convention over configuration means an end to verbose XML configuration files – there aren’t any in Rails! Instead of configuration files, a Rails application uses a few simple programming conventions that allow it to figure out everything through reflection and discovery. Your application code and your running database already contain everything that Rails needs to know!


You might come out ahead by **intentionally choosing to make things not configurable**:

1. It forces you to carefully select good default values
2. It forces you to pick a strategy and run with it rather than hedging your bets and trying to satisfy everyone
3. It’s one less thing for the user to think about when using your software

[configurability](https://blog.codinghorror.com/tag/configurability/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
