---
title: "Another Payment Processor To Look At"
date: 2006-07-25
url: https://www.kalzumeus.com/2006/07/25/another-payment-processor-to-look-at/
slug: another-payment-processor-to-look-at
word_count: 388
---


I decided to switch my payment processing from [Payloadz](http://www.payloadz.com) to [www.e-junkie.com](http://www.e-junkie.com) .  I’ll be keeping Payloadz around for their web store link but driving all the traffic from my site to e-junkie.  There are three major reasons:


Automatic Redirection: Its absolutely crucial to me that I be able to redirect customers back to my site after the transaction is completed.  Currently, I just want to capture the fact that they’ve made a purchase with Google Analytics.  However, I’m thinking of eventually displaying their registration code in-line in the page and dropping them directly at a quick-start guide.  e-junkie made this trivially simple to accomplish.  Payloadz… not so much.  I had to hack up a form myself for each link I wanted this behavior on, which was not an option considering that form would have to be in my site navigation on every page.


Rational Pricing: e-junkie is $5 a month, regardless of how much I sell.  Payloadz is… strange.  For sales under $100 in any consecutive 30 days I pay nothing.  If I get above $100, I have to pay $15, and that continues to $500.  At which point I have to pay $29.  And so on and so forth.  Frankly, I don’t know where my monthly sales are going to stabilize and don’t want them stabilizing at a point where I routinely pay 12-15% of sales to somebody doing, well, essentially not a heck of a lot for me.


Customer experience: Payloadz let me add my own text to emails to my customer, but I couldn’t change their default text, which was not applicable to my product and does not match my tone elsewhere.  e-junkie let me write my own email template, soup to nuts.  I also don’t have to have their corporate name present anywhere visible to the user at any point in the process, which I rather like because neither Payloadz nor e-junkie screams “responsible businessman of the sort I am glad to pay to get educational materials from”, which is sort of what I’m going for.


I would still heartily recommend Payloadz to people selling, say, $5 e-books on eBay.  And eventually I’ll stop paying e-junkie and roll my own IPN solution.  Perhaps.  I figure that will take me 2 hours, and $5 a month is not really worth 2 hours of my time…
