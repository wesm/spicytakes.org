---
title: "Conflict of Interest: Payment Processors vs uISVs"
date: 2007-07-05
url: https://www.kalzumeus.com/2007/07/05/conflict-of-interest-payment-processors-vs-uisvs/
slug: conflict-of-interest-payment-processors-vs-uisvs
word_count: 2036
---


I sometimes take a bit of guff from other uISVs for not using a “real” payment processor.  Some folks believe Google Checkout/Paypal are “unprofessional” or “hobbyist”.  I respect that opinion.  However, if the recent events at SWREG are any indication, I’ll wear that amateur label proudly.  They recently introduced a new upsell item in shopping carts of the uISVs they serve, and its one that makes one recall the many alternate definitions of the word *professional*.


Andy Brice has got the [story](http://successfulsoftware.net/2007/07/04/swreg-customers-beware/) covered and the [BoS forums](http://discuss.joelonsoftware.com/default.asp?biz.5.515181.23) are buzzing about it, but in brief, SWREG has placed a button labeled Continue after the last page after the checkout funnel.  If you click the button, you will be billed $9 a month to your credit card, silently, until you figure out who the heck is billing you and try to cancel.  This is orchestrated by an outfit called [Reservation Rewards](http://adam.rosi-kessel.org/weblog/the_man/webloyalty_aka_wli_reservations_is_a_scam.html) aka [WebLoyalty.com](http://adam.rosi-kessel.org/weblog/2007/05/24/webloyalty-recap/) aka [TravelValuePlus](http://it.slashdot.org/article.pl?sid=05/06/20/0514256) aka [BuyersAssurance.com](http://billyoceanseleven.wordpress.com/2007/03/23/scammed-by-chadwicks-and-reservation-rewards/) aka AnyoneWithSixDBAsIsTryingToScamYou.com.  Theoretically, they send you coupons in return for your $9 a month.  Many, many folks report never getting the coupons, never receiving a single of the multiple emails they steadfastly claim to send, and never having done the double opt-in gymnastics that they claim isolates people from getting locked into their service without wanting to be.


See, here’s the rub.  There is a nice feature of the Internet that folks learn early: if you don’t give your credit card details to someone, they can’t bill you.  Entering your credit card details is a signal both of major trust and of the fact that you understand that, absent you taking some action, you’re about to authorize forking over some money.  WebScamInc could never get “millions of satisfied customers” to authorize the $9 for nothing purchase with their lack of service, so they piggyback on the trust the customer has in you.


And THAT, more than anything else, is what burns my biscuit about this.  It is bad enough that a business would abuse their own customers enough to facilitate theft by fraud from them, and some large businesses did this quite often in the Wild West days of the Internet.  What makes it particularly galling, though, is that a customer at SWREG is **not** SWREG’s customer — he’s the customer of some uISV somewhere who stays up nights toiling away writing emails, polishing web copy, and smashing bugs to earn the trust of people he has never met over the Internet.  And what does the customer get for being foolish enough to trust him?  He gets stabbed in the back by someone whose only purpose in life is to be a convenient CGI interface to a merchant account.


Oh, but it gets better.  Over at Andy’s blog, Jessy from SWREG has this explanation of why they allowed a scammer to take up residence on their service.  Its… well… here, read it.


> Hello,
>   The offering is a perks offering for customers. In no way are they tricked into using this, and it is clearly disclosed what they are signing up for. The signup page looks nothing like the order form or SWREG clearly differentiating it from the product purchase.
>   Customers are also very easily able to cancel the perk offering at any time. They can choose to pay the fee and receive great discounts at very popular, well-known brands/stores within their country.
>   SWREG has made this optional for our clients. These are offerings used at Amazon and EBay, nothing new or out of the ordinary for customers.
>   If you have any questions please don’t hesitate to contact me.
>   Thanks,
>   Jessy
>   (*Email address omitted by me.*)


This is willfully obtuse.  Yes, if you read [every](http://www.icons-icons.com/swreg/swreg-2-offer.png) [word](http://www.icons-icons.com/swreg/swreg-3-yes.png) on the SWREG order page, you will indeed realize that the 8pt font says you are submitting your data to a third party and authorizing them to debit your credit card.  The 24 point font on the blue button, however, says “Yes.  Click here now”.  And SWREG, as an e-commerce merchant, should darn well better know that *Internet pages are not made to be read*.  They are made to be scanned — readers evaluate, in a period of seconds, whether or not anything on the page has interest to them *and then* they drill down into that content, either by reading it or interacting with their interface.


A large block of small text font on a web page, placed against a blue button with a strong call to action, isn’t asking to be read.  **Its asking to be missed**.  It is exactly where any web site designer worth their salt would say “You know, if I put that in CrazyEgg or did a real heat map study, that area would be a deep blue dead zone.  I sure hope the content writers don’t put anything important there.”


There is also the context to consider.  This is important — if you are in the middle of a transaction, and you have already gotten over the mental “Give this vendor [i.e. the uISV] money” barrier, then everything from the start of the funnel to the end of the funnel reads *Click next to continue*.  If that button had said, in 48 point font, “Click here to format C:\” **I still could have gotten 5% conversion with it**!  Its like putting something on the second to last page of an installer — we all know that nobody reads anything, they just mindlessly click next until the application pops up or they are dumped to their desktop because *our industry has trained them for decades that nothing they are about to see is important*.  That is why, when we design web applications, we put destructive actions behind popup confirmations, and we put really destructive actions behind things which are designed to jar the user out of their GUI induced fugue, like “Type d-e-l-e-t-e to drop the database”.  Spending money is customarily put behind a similar speedbump, entering credit card details, and this scam is designed precisely to circumvent that safety valve.


Oh, but spending money isn’t necessarily destructive, as Jess points out.  Maybe folks like the discounts they’re getting at a wide variety of establishments in their country, for the low, low price of $9 a month.


Tell me, do the [one thousand, nine hundred, and seventeen customers](http://adam.rosi-kessel.org/weblog/the_man/webloyalty_aka_wli_reservations_is_a_scam.html) who commented on just one of the “Reservation Rewards is a scam” thread sound like they are satisfied customers happy to have received discounts?  Lets review a couple of these comments, shall we?


Daniel said


> wow i cant belive this i just noticed these same charges on my account and only noticed because it made me overdraft in my debit account. i called the bank and they told me that it has been going on since july thats $54 that they have talken with out me knowing i have no idea where they got the info tho i always shop through paypal but makbe that is the problem all i know is that this needs to be stopped it is wrong.


Matt said


> Thanks for putting this up. I just got off the phone with these guys. They claimed they “were making an exception to the rules” when they refunded 4 months worth of charges to me. I asked where they got my CC# and they claimed it was from ebgames.com, a site I sometimes buy stuff from. I’m filing a complaint with the Connecticut Department of Consumer Protection and will be taking the issue up with ebgames.com customer service and perhaps the Pennsylvania Bureau of Consumer Protection if that doesn’t work out well.


(You can feel free to add this to the SWREG defense: Well, if Reservations Rewards is good enough to scam ebgames’ customers, then it is good enough to scam ours!)


Don said:


> I am currently serving in Iraq, have been for 4 months, and noticed that I have been recieving charges from WLI for $7 (am I a lucky one to get off so cheap?). I have gone to their webpage with an unloaded weapon—you see, you have a logon & password to see “your” account information. Beings I did not know I was a member, needless to say I do not have that info. So I e-mailed them my name as it appears on my credit card, told them to cease, desist & refund….. Hoping for the best.


You know what lack of capital letters, fractured syntax, and a certain lack of savvy about e-commerce reminds me of?  Oh, yeah, a significant portion of my customers.  (Even English teachers “let their hair down” when they are writing emails, sometimes.)  Unlike any significant portion of my customers, these folks are howling for blood.  And if you’re using SWREG, they are howling for *your* blood, because despite the fact that you are the little minnow and SWREG is the multi-million dollar corporation to the extent that anyone realizes you are in fact separate entities (and most don’t) the presence of SWREG’s website wrapped within a mere portion of your own makes it look like they’re working for you.  And, hey, with them getting a sliver of the transaction, that is what the relationship really is.


Which is the problem from SWREG’s point of view.  They can’t increase their cut of the transaction size, or you will flee to one of their competitors, or decide to go to e-junkie/Paypal.  You can get a customer to purchase from you multiple times to increase your revenue, but that is only an option for SWREG to the extent that you stay one of their vendors.  So they are constantly on the lookout for new revenue streams, and both aggressive cross-selling to your customers and selling them down the river to scumbuckets.com are apparently options on the table.


So, what to do about it?  Well, if you’re not a customer of SWREG, great.  Celebrate your good fortune… and give your e-commerce provider a jaundiced look and a quick assessment of whether they would ever stab your customers in the back.  If they would, make preparations for your inevitable separation as soon as that provider makes the decision that your future loyalty is worth less than the amount they can extract out of your customers today.


I came *very* close to giving Google Checkout the boot once, on Earth Day.  They proposed to cross-sell my customers into a $10 carbon offset.  It wasn’t nearly this scummy — the carbon offset was clearly marketed as a separate item, it would have required another separate checkout process to buy, and of course the only reason you would actually click on a button saying Click Here To Buy a $10 carbon offset is if you wanted to actually buy an indulgence offset.  Google’s saving grace was that they realized this was going to be controversial and offered me an opt-out.  (It really should have been an opt-in.  I have no strong opinions either way on begging for alms soliciting charitable contributions but impair your customers’ experience to do it, not mine.  I don’t see any “Thanks for searching for flapjack recipes on Google.  While you’re here, interested in buying a carbon offset?” cluttering up your famously minimalist interface.)


And if you are a SWREG customer?  I think Tom Rath on the BoS boards said it best:


> Now I need to spend the next few days alerting my customers of this con, apologizing profusely to those who found themselves roped into it, and write cheques to cover whatever expenses have been incurred by those foolish enough to trust my company’s judgment.


I don’t know what Tom Rath sells off the top of my head, but whatever it is, that paragraph makes me want to buy one on general principle.  Those are the words of a man you can trust.  That is the tone that we strive to strike as little honest fish in a stormy ocean filled with unscrupulous sharks trying to take a bite off of anyone doing business on the Internet.


And SWREG?  Well, suffice it to say that the W in the name is looking like a dorsal fin to me at the moment.  Duh duh, duh duh, duh duh duh duh duh duh…
