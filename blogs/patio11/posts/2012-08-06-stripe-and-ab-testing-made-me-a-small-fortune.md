---
title: "Stripe And A/B Testing Made Me A Small Fortune"
date: 2012-08-06
url: https://www.kalzumeus.com/2012/08/06/stripe-and-ab-testing-made-me-a-small-fortune/
slug: stripe-and-ab-testing-made-me-a-small-fortune
word_count: 3849
---


I’ve run software businesses for the last six years, all premised on the simple notion that if I provide value to customers they should pay me money.  The actual implementation of translating their desire to pay into money in my bank account was less simple… until I found [Stripe](http://www.stripe.com).  They’re now up there with Twilio and Heroku in terms of “infrastructure companies which will totally change the way savvy software companies do business”, and if they ever get international processing nailed, I think they’ll probably take over the industry to Paypalian scales.


How do I love you Stripe, let me count the ways…


## Well Thought Out API Design


Ever worked directly with the Paypal API?  Keith, my podcast co-host and somebody who routinely codes systems that process millions in payments, shudders when he mentions it.  The Paypal API is powerful and (fairly) reliable, but the experience of coding against it is absolutely maddening.  It is very much a legacy API which has to support decisions made at the dawn of the Internet which were largely driven by considerations not relevant to software developers or web entrepreneurs.


Stripe’s API is one of the best I’ve ever worked with:

- It uses all the REST-y goodness that the web development community has come up with in the last few years.
- The [documentation](https://stripe.com/docs/api) is suitably comprehensive, organized for easy consumption, and screams “You will have this in a secondary window when you’re coding stuff that matters” rather than “This was designed as a 450 page PDF by a standards committee.”  The table of contents for any one of Paypal’s APIs is longer than all the docs for Stripe… and less useful.
- There are several first-party libraries available, they work, and they feel like first-class citizens of their respective ecosystem.  [Stripe-ruby](https://github.com/stripe/stripe-ruby) is fantastic and feels like ruby.


## Most Painless Integration Ever

As a direct consequence of having a really, really well-designed API, integration with Stripe was a breeze.  Getting credit card processing hooked into Bingo Card Creator — authorization, charging, accounting, the works — was
**29 lines of code**
.  I signed up for Stripe, got started with the API documentation, and successfully charged a real credit card from production
**three hours later**
.  They’ve got the fastest time-to-business-value of any API since Twilio.
One major reason Stripe works exceptionally easily is because of stripe.js.  Basically, if you’ve ever tried to charge credit cards before, you’re aware that there is a PCI-DSS standard out there and if, e.g., credit card numbers ever hit your hardware then you’re in for a world of painful compliance audits and ridiculous checking-boxes-for-the-sake-of-checking-boxes.  (“No, I don’t run my server on a server which sits in an unlocked room in a building the general public has access to.  Phew,
*dodged a bullet there*
.  Now excuse me while I go install some anti-virus software on my Ubuntu box and very diligently review my Nginx logs daily.”)
There are two major ways around PCI compliance:
- You redirect people off-site for the transaction to e.g. Paypal or Google Wallet, and let the megacorps worry about it, then they redirect people back to you when they are done.  This is a poor user experience that often confuses customers and might decrease conversion rates.
- You have an iframe or something capture their credit card on your site but actually submit it only to the payment processor.

Stripe.js is a very well-implemented “or something”, where JavaScript that they’ll provide for you hooks into your credit card form with trivial work.  (About ~6 lines for me.)  When a user submits the form, you instruct Stripe.js to AJAX-y over to their servers and authorize the card.  Then you process the results in a callback.  This lets you verify e.g. that the card exists and is chargeable prior to submitting your form and executing your server-side purchase logic.  Stripe will then give you a token allowing you to securely charge the card for the authorized amount, and you can choose whether to do that or not on your server-side.  (For example, I perform other business logic validations first, and void the authorization if e.g. the user has already purchased the software.)
This means that their credit card details never hit your server.  Now, rationally speaking, if your server is insecure then the page the credit card form is hosted on is in the hands of the enemy, and you can no longer trust that Stripe is the only party which sees the credit cards.  However, PCI compliance has very few rational parts about it.  Stripe gets you past that hurdle with a minimum of pain.
**This is really, really important for developers because you get end-to-end control of the user experience.**
You don’t have to do a redirect off-site and you don’t have to have a garishly styled external iframe in the middle of your app.  You can slide a credit card form in whatever part of your workflow makes sense, have it feel organically like your app (because
*it is, actually, your app*
), avoid the Paypal/Google attempts to use your relationship with a customer to capture a new account for themselves, etc etc.  That has the potential to significantly increase revenue.  (More on that later.)

## Amazing Support For Developers by Developers

So let’s say you happen to support a Ruby on Rails application coded by a novice web programmer in 2008.  Hey, it happens.  There are a lot of old gems required for the program to operate, somewhat creakily.  Let’s further suppose that this causes you to have a conflict with a dependency from an external API vendor, because the vendor doesn’t specify what version of the old gem to use with their ruby library.  If you mail support@, and tell them “When using a version of this gem four years out of date, your library dies on a particular line, because you use an API that doesn’t exist in the oldest versions of the library.  I can’t use the latest version of the library because it causes dependency conflicts.  What should I do?”, what would you expect them to say?
**Here’s what I expected**
:  “Thanks for your email.  We can’t help you with coding your application.  You should use the latest version of the library.  Please see our FAQ at…”

**Here’s what Stripe actually said:**


```
Hey Patrick,

Thanks for the report. I took a quick look:

$ git clone git@github.com:archiloque/<wbr>rest-client
$ git bisect start
$ git bisect good v1.0.3
$ git bisect bad v1.6.1
$ git bisect run ruby -rubygems -e '$:.unshift "lib"; require "stripe"; Stripe.api_key = "KEY"; begin; Stripe::Plan.all.count;
  rescue; exit 0; end; exit 1'

Suggests that 7563fd as the culprit. Looking at the log, this seems to be around 1.3.0. Then:

$ git log v1.3.1..7563fd
$ git log v1.4.0..7563fd

So, looks like v1.4.0 is the first version that included that #body interface change.

I just pushed stripe-ruby 1.5.22, which adds a dependency on 1.4.0 of rest-client.
 
Thanks again for the heads up. Let us know if you run into anything else.

```


I am not easily emotionally moved by git command lines, but this is clearly somebody who understands me and what I need in life.  In addition to exactly diagnosing the problem (I was on rest-client 1.0.3, the most recent version was 1.6.1, and it would really have been compatible with anything after 1.4.0), he fixed it for everyone else.


(Sidenote: This is one of the very few times in my life where mailing support@ made me a better engineer.  “You can figure out which version of a library breaks your application by running your minimal failing test suite commit-by-commit, watching for exactly the commit where it fails, and then correlating that to the released version which will actually work for you.  But since that will take forever, use binary search instead.  And there exists a git command which will do this for you.”)


**That email was signed by the co-founder.  **Patrick Collison, when he isn’t *running a payments company*, apparently found time to verse himself in arcane git commands.  I was practically *vibrating* with “These guys understand where I’m coming from.” after that, and they’ve not let me down since.


I’ve had exactly one serious problem with Stripe, in a year.  Their API broke for three transactions, due to a load balancer issue.  This caused their client library to return “Unspecified error, card not charged”, prompting my application to not deliver software to the user, but they were actually charged.  Clearly, that’s quite problematic.  They proactively got in touch with me about it, fixed the problem, and generally demonstrated competence and professionalism.  I gave away three free copies of the software and apologized profusely.  We haven’t had any recurrences since then, over about a thousand transactions.


## Their Web Application Rocks


So in addition to programmatically charging cards, payment processors typically provide web interfaces.  They’re typically abysmal.  Paypal’s — and, again, I like Paypal — will take upwards of 15 seconds to find a transaction when you’re searching *by its primary key*, and it looks like it was written in 1996, principally because it was.


Stripe’s interface is pretty (don’t discount how much that matters, since you actually have to use it), snappy, responsive, and well-thought-out.  It has an awesomebox which, given 1234 as input, will quickly find every transaction with 1234 as the last four digits of the credit card, bring up the transaction for sale #1234 (an ID my code passed over with the transaction), finds all of your $1,234.00 charges sorted by recency, etc.  There *has* to be someone in Stripe who actually runs a side-business on it, I swear.  That or they’re telepaths.


Refunds are one click.  (And also available with an API.  This has saved me tens of minutes versus Paypal, since I have to log in, find the transaction, and write a refund note manually to do a refund with them.  It also saves me a lot of frustration, as correlating Cindy Smith to a Paypal transaction is difficult, whereas in Stripe all I have to do is keep their authorization token around server-side and then refunding a transaction is as easy as *customer.sale.refund!*)


Each transaction has a programmer-comprehensible set of logs attached to it, so I can quickly debug application problems.


Oh, they also have an API sandbox, with credentials segregated from the production API, and which can be manipulated via both the web interface and the API trivially.  I think this is an absolute hard requirement for APIs which can actually touch the real world.  (It is one of my *very* few knocks against the Twilio API.)


## Stripe Has Fair, Comprehensible, Comparatively Transparent Terms


Ever heard “Paypal turned off my account waily waily” or “Paypal froze my money waily waily”?  Most complaints about Paypal actually aren’t about the API, they’re complaints motivated by a) commerce is *hard* because of the amount of fraud on the Internet and b) Paypal doesn’t historically do a great job of giving you resolution options if it’s fraud detection is overly aggressive in your case.  (I actually believe that they’re worlds better on this than they are perceived to be — the one time Paypal had an overly aggressive fraud alert on my account I was able to resolve it with a single one-minute telephone call.)


Stripe asks for prior review of your business model but, in my experience, approves you automatically and then actually does the human review while you actually have a set of working API keys.  They make transfers to your bank account 7 days after your customers pay you, to make an allowance for fraud/refunds/etc.  Seven days is *impressively* faster than most merchant accounts.


Stripe really shines in those rare cases where you need a human in the loop.  It’s still always a good idea to tell people in advance if you’re going to do something which will trip a fraud screen (e.g. open payments for a widely anticipated conference and then collect $X00,000 in $500 chunks from people in multiple countries — this will almost certainly get a Paypal account frozen).  A friend of mine — who has previously had issues with cleared payments getting filched by Google Checkout and then got Google’s customary /dev/null customer support — asked Stripe if an upcoming product launch would cause an account freeze.  “Thanks for contacting us.  Of course not.  You’re *clearly* legit.”  It’s like they found the sweet spot between “Computers can make decisions in lightning-speed at scale” and “Humans can actually be trusted with *discretion*.”


## Developers Obsess About Price So I Guess I Have To Mention It


Stripe charges $0.30 + 2.9% per transaction, which is comparable with Paypal at low volumes.  This is frequently the #1 thing devs tell me they look for in their payment processor.  That is *insane*.  We sell products which have margins that come very close to 100%, and saving pennies on transactions to spend tens of thousands on integration costs (*) or to shave full percentages off our conversion rates is *absolute madness*.

- Think I’m exaggerating?  That’s about two weeks of dev time.  Trust me, you will not get a shopping cart integration done in two weeks with most payment providers.  Again, it took me **three hours** with Stripe.  I still can’t believe that.


## I Extensively A/B Tested Stripe Against Off-Site Checkout And Found…


… that I should really not ship prototype shopping carts, even when I think it is really cool to get something out the door.


Back prior to the redesign of Bingo Card Creator, I tested Stripe on-site credit card payments (the interface for which I threw together with Twitter bootstrap in ~45 minutes) against Paypal and Google Checkout.  Specifically:


Test #1: Paypal / Google Checkout vs. Paypal / Google Checkout / Stripe


Test #2: Paypal / Google Checkout / Stripe vs. Stripe


Test #3: All three vs. all three, with the difference being whether customers upgrading directly after a trial limitation had been reached were sent to the purchasing page or an in-app credit card form


All three of these tests were null results.  (i.e. No significant difference in aggregate purchases between either of the two options.  **Interesting, though, any time paying by credit cards was an option, that was overwhelmingly the customer favorite**.  When the choice is Paypal versus Google Checkout, I get 50/50.  When the choice is Paypal / Google Checkout / Credit Card, I get 5-5-90 or thereabouts.  That could be sensitive to the design of my pages, I don’t know — I tested e.g. re-ordering the buttons and that didn’t change things, but didn’t go on to test e.g. button copy or color.)


[**Edit**: Whoopsie!  A comment on HN sent me back to my A/B testing records.  Turns out Test #2, which I had misreported as PP/GC vs. Stripe but was actually PP/GC/Stripe vs. Stripe, was actually a weak 90% significant win for PP/GC/Stripe.  Test #3 was a weak 90% significant win for sending folks to the purchasing page rather than the hacky Boostrap CC form.  Sorry for the misreporting earlier — these were in the Big Book O’ Failed Tests and I forgot to check the detailed reason for why.]


So, despite customers overwhelmingly choosing credit cards, adding that option via Stripe wasn’t capturing additional sales at the margin.  **This was surprising to me**, because it is received wisdom in the conversion rate optimization community that users hate off-site checkout.  I mentally tied a string around my finger to revisit the issue later.


## I Followed Up On Earlier Testing And…


Earlier this year, after having decided to offer all three payment options full-time, [I did an experimental website redesign](https://www.kalzumeus.com/2012/04/19/ab-testing-is-frustrating/), in an A/B test.  This gave me the opportunity to have my cobbled-together credit card form replaced by one done by a professional designer.  That experimental redesign was very, very wide-ranging and affected pretty much every stage of the software purchase funnel.  Results were mixed — some steps radically better, others worse — and netted out to no significant change in revenue.  Since the user experience was very improved, I adopted the redesign.


While I was looking at the stages of the purchasing funnel, I saw that the newly redesigned checkout experience didn’t really seem to motivate customers more or less than the old, ugly checkout experience, but users continue to overwhelmingly prefer credit card checkout either way.


Anyhow, some months later, I took a run at fixing the part of the funnel which had suffered most in the redesign.  For whatever reason, improvements in the usability of my application had made users much less likely to hit the free trial limitations.  This caused less of them to get taken into the purchasing pathway, after which point their experience was largely consistent across both versions of the site.


So I tested the stupidest thing that could possibly work to get more people to hit the trial limitations: decrease people’s free quota from 15 cards to 8 cards.  And I did that in an A/B test.  One line of code which tested, literally, two characters in the program.


**Wham.**


Not only did the 8 card limit *absolutely crush* the 15 card limit (99% statistical confidence, 1.89% conversion rate instead of 1.04% conversion rate from free trials to paid accounts on a sample size in the 5,000s range), it did something which is fairly rare in my A/B tests: it caused synergistic effects.  Ordinarily, I operate on the Bayes-is-about-to-turn-over-in-his-grave assumption that two stages in the funnel are largely totally independent from each other.  So, for example, if stage #1 is “Did they hit the trial limitation?” and stage #2 is “Did they purchase the software once in the shopping cart?”, I default to expecting that a test which increases the number of people hitting the limitation will not meaningfully impact the conversion rate in the shopping cart.  This is because this assumption has previously been good enough to bet money on, at least in my business.


Well, this time I lost the bet… or I won, catastrophically.  It seems that the marginal prospects (with the between-8-and-15 cards needs)  hitting the trial limitation have very different behavior when exposed to the shopping cart than the will-hit-the-limit-regardless prospects.  I did half a dozen tests to isolate the exact cause (I’ll spare you the deep dive into bingo customer minutiae).  Suffice it to say there is a) a customer group which needs between 8 and 15 cards and b) they really, really like pretty checkouts.  (I’m guessing that I’ve probably captured significant business from a portion of the population which isn’t teachers, who make up about 60% of my customers typically, but haven’t done any qualitative surveys to figure out who these new folks are.)


So, anyhow, with 99% confidence of a huge increase, you adopt the change, right?  I did that back in May.


Since selling to elementary schoolteachers is highly seasonal, let’s look at [year over year](http://www.bingocardcreator.com/stats/sales-by-month) results.  All of these months have the new redesign in place for 2012, but the new trial limitation was implemented mid-May and default behavior by the end of the month.


May: +38% increase in sales


June: **+108% increase in sales** (in the dead of summer, my slowest season)


July: +33% (dang, *only?*)


If this change continues being motivational during the school year it will be worth several tens of thousands of dollars a year to me.  If not, drats, it only doubled my money on the redesign.  I like giving credit where credit is due, so:

- The redesign that debuted as “Awesome for users, meh for the business” now retroactively looks like the best idea for this year.  Thanks [Ashraful](http://madebyargon.com/).  (Hire him.)
- Stripe, which makes the purchasing part of the funnel possible now, is incredibly amazing.  (And now processing 90% of my transaction volume for this product.)
- As much as I love the above two, I have to give most of the credit to making decisions on the basis of data.  I know I’m a broken record on this, but no matter how many times I say it it doesn’t seem to change the behavior of many folks in the industry, so: A/B testing prints money.  So does having sufficient metrics in place such that one knows where the high priority places to A/B test are.


Incidentally, I do A/B testing with [A/Bingo](http://www.bingocardcreator.com/abingo/) and measure test effectiveness throughout the funnel using KissMetrics, since A/Bingo won’t track multiple conversion types for a single test out of the box.  (Ben Kamens at the Khan Academy [persuasively argues](http://bjk5.com/post/28269263789/lessons-learned-a-b-testing-with-gae-bingo) that fixing this would be a good idea.  It is on my list.)  Two years ago someone [asked](http://news.ycombinator.com/item?id=1512340) me whether I thought $150 a month for [KissMetrics](http://www.kissmetrics.com) was worth it.  Ahem, yep!


## Back To Stripe


Stripe is now my first choice for payment processing.  All of my new projects will start with Stripe and — maybe! — use Paypal if I get around to it.  (I don’t feel any impetus to migrate away from Paypal on BCC or Appointment Reminder — the code works and Paypal is, as mentioned, responsive when I have problems… but the CEO of eBay isn’t running git bisect for me if I have an API issue, so I feel no need to keep them in my plans forever.)


Two minor niggles mentioned for the purpose of completeness:

- They occasionally expect me to be a better programmer than I am, by trusting me to do things correctly the first time.  (A customer had — I kid you not — a lightning strike hit her computer during checkout, and as a consequence the JS callback fired 36 times.  This resulted in 36 transactions, which Stripe processed without complaint.  *Oops*.  Server-side validation added.  Luckily, I caught the anomaly before my customer did, so I was able to refund and explain it to her prior to her bank asking for $1,078.20.)
- “Authorize first, charge a second later” shows up on a lot of my customer’s online credit card statements as two separate charges until the first authorization gets voided, which can take days.  I’m almost certain this is not a Stripe issue and is, rather, a legacy payments infrastructure issue.  C’est la vie.  This causes about an email a month, and no customer has ever had a problem after I explain it.  (Editor’s note: Somebody from Stripe emailed me a work-around — just don’t feed Stripe.js a price and it won’t pre-auth the card.)

If you’re US-based, you can use Stripe, too, and they have my unreserved don’t-even-bother-looking-elsewhere recommendation.  If you’re not US-based, I feel your pain, and hope Stripe expands to your neck of the woods as quickly as possible.  (In the meanwhile, check out Paypal.)

*Standard disclaimer*: I occasionally write about companies which I use in my business and I feel are relevant to you guys.  Stripe isn’t a client.  I haven’t accepted anything of value from them… well, OK, technically speaking they have deposited $30,000 into my bank account, but you know what I mean.  (I think I also got mailed a hoodie at one point.)
