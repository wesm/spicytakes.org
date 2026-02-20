---
title: "Dev Journal: First Three Days in the Trenches"
date: 2006-06-26
url: https://www.kalzumeus.com/2006/06/27/dev-journal-first-three-days-in-the-trenches/
slug: dev-journal-first-three-days-in-the-trenches
word_count: 505
---


Well, I got down to business this past weekend. Saturday, Sunday, and Monday I worked ~6 hours a day on my project. About 3/4 of that was writing code, the rest was getting signed up with my website and credit card processor.


I eventually went with [GoDaddy ](http://www.godaddy.com)for web hosting. No sense spending serious money on the project before I have some indication that there are actual, living, not-related-to-me people who want to spend money on it. My total bill for a new domain name and two months of Basic Hosting service (which is, incidentally, easy enough to launch a uISV from) was $10.02. So I’ll be in the black after my first sale, if you assume my time is worth nothing since the 18 hours would otherwise have been spent on an [unproductive addiction](http://www.worldofwarcraft.com).


I went through [eSellerate’s](http://www.esellerate.com) setup process but I’ve got an account representative (um, yay? You gentlemen cannot possibly expect to make enough out of me to dedicate one guy to my needs, so why bother) who has yet to get back to me. Thats a problem, as if this continues for a few more days it will delay launch. But, oh well, their interface has to be seen to be believed — going through their workflow (which is a bit complicated but nothing after I suffered through installing RedHatCMS at my day job) gives you the feeling “Wow, I’m really a professional now”. However, I haven’t yet discovered a quick and easy way to make a single-product checkout page with them. I don’t need a shopping cart — every page that pops up from the time someone clicks my “Buy now” link is an opportunity for second thoughts. I want to show the product, pricing, and start getting the credit card information immediately.


Which leads me to my new discovery which I found on the [Business of Software](http://discuss.joelonsoftware.com/?biz) forums: [Payloadz](http://www.payloadz.com). Payloadz is a payment processor which, apparently, operates exclusively through Paypal. Its essentially a script that sits somewhere on the Internet and intercepts an API call that Paypal optionally makes when you get a payment, reads out the details, and directs your customer to their full version/registration code/what have you. Its also “dirt cheap”. Their flat rate fee is 15%, which isn’t impressive compared to the options I reviewed below (remember, Paypal will also charge you 2.9% plus $.30 per transaction), but their [tiered structure](http://www.payloadz.com/account/levels.asp) works out to far, far less if you’re in the middle or high end of your tier. Consider, for example, if I have monthly sales of $250. That puts me in the middle of Premium I, which charges $15 a month. $15/250+ Paypal’s rake = approximately 10% (what eSellerate will charge you at the introductory rate). Sell $400 and its closer to 8%. And it declines precipitously from there. The major benefit, to my mind, is that Paypal is a trusted name (ok, so maybe not THAT trusted) and people have (hopefully) purchased from one of their shopping carts before, reducing barriers to the sale.
