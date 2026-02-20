---
title: "Bad Places To Have Bugs: Pricing Logic"
date: 2009-03-30
url: https://www.kalzumeus.com/2009/03/30/bad-places-to-have-bugs-pricing-logic/
slug: bad-places-to-have-bugs-pricing-logic
word_count: 331
---


About a week ago I noticed a deficiency in my understanding of how my shopping cart actually worked for purchases of 2+ units: specifically, e-junkie thought they were mispriced and was bouncing the transactions, resulting in a customer getting charged but not getting their key automatically. I only get about one of these orders a year, so I hadn’t seen the behavior yet. *sigh* So I did something I thought I would fix it: turn on variable pricing, then set prices manually through my cart. Done, right?


Wrong. The next day, I started getting orders at $20.00, the new price floor. I looked around for the possible cause and figured that if you had Javascript disabled or clicked through my cart before its Javascript could load, you’d get taken to e-junkie’s fallback hosted cart, where you’d be given the option of modifying the price. For some reason it defaulted to $20, despite $29.95 being set as the default price. Not quite sure why. So I fixed it, by making the default item be a single copy at $29.95 and only having the pricing logic apply when buying through my cart.


But still the $20.00 units kept coming. Then it hit me — it wasn’t actually that edge case, it was a different edge case — involving an ugly mess of Google Checkout, e-junkie, and my code. Grr. So I went back to Plan A: reverted to the cart which charges 1,499 customers a year correctly and causes 1 guy to wait a bit while I decide how to address this in a more long-term fashion, rather than having half of the purchases this week get screwy behavior.


I lost about $120 that I know about in arbitrary discounts, plus more if anyone was scared off by the weird inconsistency between my site’s pricing and the pricing at Paypal/Google Checkout. Not that I blame them. Grr.


Memo to self: self, you’ve said it before, but avoid doing 5 minute changes at midnight.
