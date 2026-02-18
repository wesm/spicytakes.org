---
title: "Plaid is an evil nightmare product from Security Hell"
date: 2022-02-19
url: https://drewdevault.com/2022/02/19/Plaid-is-an-evil-nightmare-product.html
slug: Plaid-is-an-evil-nightmare-product
word_count: 577
---

[Plaid](https://plaid.com)  is a business that has built a widget that can be embedded in any of
their customer’s websites which allows their customers to configure integrations
with a list of third-party service providers. To facilitate this, Plaid pops up
a widget on their customer’s domain which asks the end-user to  *type in their
username and password*  for the third-party service provider. If necessary, they
will ask for a 2FA code. This is done without the third party’s permission,
presumably through a browser emulator and a provider-specific munging shim, and
collects the user’s credentials on a domain which is operated by neither the
third party nor by Plaid.

The third-party service provider in question is the end-user’s bank.

What the actual fuck!

Plaid has weighed on my mind for a while, though I might have just ignored them
if they hadn’t been enjoying a sharp rise in adoption across the industry. For
decades, we have stressed the importance of double-checking the domain name and
the little TLS “lock” icon before entering your account details for anything. It
is perhaps the single most important piece of advice the digital security
community has tried to bring into the public conciousness. Plaid wants to throw
out all of those years of hard work and ask users to enter their freaking  *bank
credentials*  into a third-party form.

The raison d’être for Plaid is that banks are infamously inflexible and slow on
the uptake for new technology. The status quo which Plaid aims to disrupt (ugh),
at least for US bank account holders, involves the user entering their routing
number and account number into a form. The service provider makes two small
(<$1) deposits, and when they show up on the user’s account statement a couple
of days later, the user confirms the amounts with the service provider, the
service provider withdraws the amounts again, and the integration is complete.
The purpose of this dance is to provide a sufficiently strong guarantee that the
account holder is same person who is configuring the integration.

This process is annoying. Fixing it would require banks to develop, deploy, and
standardize on better technology, and, well, good luck with that. And, honestly,
a company which set out with the goal of addressing this problem ethically would
have a laudable ambition. But even so, banks  *are*  modernizing around the world,
and tearing down the pillars of online security in exchange for a mild
convenience is ridiculous.

A convincing argument can be made that this platform violates the Computer Fraud
and Abuse Act. Last year,  [they paid out $58M](https://www.jurist.org/news/2021/08/plaid-agrees-to-pay-58-million-in-data-privacy-class-action-lawsuit/)  in one of many lawsuits for
scraping and selling your bank data. Plaid thus joins the ranks of Uber, AirBnB,
and others like them in my reckoning as a “move fast and break laws” company.
This platform can only exist if they are either willfully malignant or grossly
incompetent. They’ve built something that they know is wrong, and are hoping
that they can outrun the regulators.

This behavior is not acceptable. This company needs to be regulated into the
dirt and made an example of. Shame on you Plaid, and shame on everyone involved
in bringing this product to market. Shame on their B2B customers as well, who
cannot, such as they may like to, offload ethical due-diligence onto their
vendors. Please don’t work for these start-ups.  [I hold employees complicit in
their employer’s misbehavior](https://drewdevault.com/2020/05/05/We-are-complicit-in-our-employers-deeds.html) . You have options, please go make the world a
better place somewhere else.
