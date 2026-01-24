---
title: "The Dancing Bunnies Problem"
date: 2005-07-22
url: https://blog.codinghorror.com/the-dancing-bunnies-problem/
slug: the-dancing-bunnies-problem
word_count: 355
---

In an era of instant online worldwide connectivity, protecting users from themselves is a lot harder than it used to be. For one thing, [full trust can’t be trusted](https://blog.codinghorror.com/full-trust-cant-be-trusted/). And then there are all those [dancing bunnies](https://web.archive.org/web/20051206042509/http://blogs.msdn.com/larryosterman/archive/2005/07/12/438284.aspx) to contend with:

kg-card-begin: html

> What’s the dancing bunnies problem?
>     It’s a description of what happens when a user receives an email message that says “click here to see the dancing bunnies.”
>     The user wants to see the dancing bunnies, so they click there. It doesn’t matter how much you try to dissuade them, if they want to see the dancing bunnies, then by gum, they’re going to see the dancing bunnies. It doesn’t matter how many technical hurdles you put in their way, if they stop the user from seeing the dancing bunny, then they’re going to go and see the dancing bunny.
>     There are lots of techniques for mitigating the dancing bunny problem. There’s strict privilege separation - users don’t have access to any locations that can harm them. You can prevent users from downloading programs. You can make the user invoke magic commands to make code executable (chmod +e dancingbunnies). You can force the user to input a password when they want to access resources. You can block programs at the firewall. You can turn off scripting. You can do lots and lots of things.
>     However, at the end of the day, **the user still wants to see the dancing bunny, and they’ll do whatever is necessary to bypass your carefully constructed barriers in order to see the bunny.**

kg-card-end: html

Here’s hoping Longhorn (aka Windows Vista) is the first Microsoft OS to **default users to non-administrator accounts.** Because users can’t help themselves – they just have to [poke the bunny](https://web.archive.org/web/20050813004120/http://www.platinumgrit.com/poke.html).


I think the real solution, if there is one, is [high-speed virtualization](http://en.wikipedia.org/wiki/Virtualization_Technology). The user will always play in a sandbox that looks and performs exactly like their current installation, but is in fact a Virtual PC style image. If something bad happens, you just ball it up and throw it away.

[security](https://blog.codinghorror.com/tag/security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[email security](https://blog.codinghorror.com/tag/email-security/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[user behavior](https://blog.codinghorror.com/tag/user-behavior/)
