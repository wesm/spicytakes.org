---
title: "Finished My Mini-Development Project, Mostly"
date: 2009-02-08
url: https://www.kalzumeus.com/2009/02/08/finished-my-mini-development-project-mostly/
slug: finished-my-mini-development-project-mostly
word_count: 468
---


[Yesterday I mentioned](http://kalzumeus.com/2009/02/07/new-mini-development-project-for-me/) that I would be making a new shopping cart.


I’ll be blogging about this much more extensively later, but after pouring 8 hours into the massive black hole of time that is Javascript (aaaaaaaahhhhh I hate you so), I got the new and improved cart working.  It isn’t quite user-ready yet and isn’t anywhere NEAR where I would consider releasing it as code for other uISVs, but you can go play around with it to get the general feel.


Known bug: e-junkie seems to have an issue when you override a price for an item and use a Google Checkout Buy It Now button.  I use this feature to move the pricing logic from the e-junkie servers to my Javascript, where it gets “bugs in your teeth fast” speed improvements.  I will probably delay releasing this until e-junkie fixes that issue or I decide to work around it with a business rule modification.


Known bug #2: If you pick a non-one number in the cart, then close it, then reopen it, your total is calculated incorrectly until you do at least one keypress in the quantity field.  I know what is causing this and will squash it fairly soon, but just feel like “I’m done for the day”.


Old cart, for comparison: [Bingo Card Creator purchasing page](http://www.bingocardcreator.com/purchasing.htm).


New cart: [http://www.bingocardcreator.com/purchasing-alternate.htm](http://www.bingocardcreator.com/purchasing-alternate.htm)


How I feel:

1. The new cart is bugs in your teeth fast for loading.  Mission accomplished.  Currently it takes the same amount of time when you click Checkout as the current cart does, which needs to get disguised a bit better.
2. Try adding a CD to your cart in both and tell me which you like better.  I think this is going to be worth significant money for me.
3. In general, I think the user interaction simplifies markedly.  The new lightbox-esque effect, provided by [iBox ](http://www.ibegin.com/labs/ibox/)(a wonderful piece of software with some significant teething issues I’ll talk about later) makes the “Continue Shopping” button redundant.  Gone.  Because I no longer incur an AJAX roundtrip to another server every time the user does anything, I don’t need to tie their updates to the Update Cart button, hence it is gone.
4. I sort of like being able to customize the branding a little bit.  For example, while you and I know this is a shopping cart, I think that whole metaphor just confuses users.  Gone.  Instead, slap in logo and text.


Let me know what you think.  After I’ve sanded down the few issues I’m going to start the A/B test and then start packaging this so that other folks can use it.  Expect a very long “making of” post as well — I actually got to solve some fun technical issues for a change, so I’ll tell folks how I did it.
