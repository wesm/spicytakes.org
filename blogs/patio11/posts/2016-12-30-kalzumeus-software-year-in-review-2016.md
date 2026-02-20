---
title: "Kalzumeus Software Year In Review 2016"
date: 2016-12-30
url: https://www.kalzumeus.com/2016/12/30/kalzumeus-software-year-in-review-2016/
slug: kalzumeus-software-year-in-review-2016
word_count: 6699
---


I’m Patrick McKenzie, perhaps better known as patio11 on the Internet. I ran a succession of small software businesses from 2006 through 2016. They started out as a side project and took over my professional life.


I try to publish a retrospective at the end of every year, including what happened, what I learned from it, and what the numbers looked like. This helps force me to plan, keeps me honest about how plans worked out, and hopefully helps some readers improve their own businesses. You can read the writeups for [2006](https://www.kalzumeus.com/2006/12/26/merry-christmas-part-2/), [2007](https://www.kalzumeus.com/2008/01/13/year-2007-stats-and-year-2008-goals/), [2008](https://www.kalzumeus.com/2008/12/21/bingo-card-creator-year-2008-in-review/), [2009](https://www.kalzumeus.com/2009/12/18/bingo-card-creator-year-in-review-2009/), [2010](https://www.kalzumeus.com/2010/12/17/bingo-card-creator-etc-year-in-review-2010/), [2011](https://www.kalzumeus.com/2011/12/21/bingo-card-creator-etc-year-in-review-2011/), [2012](https://www.kalzumeus.com/2012/12/29/bingo-card-creator-and-other-stuff-year-in-review-2012/), [2013](https://www.kalzumeus.com/2014/01/06/kalzumeus-software-year-in-review-2013/), and [2014](https://www.kalzumeus.com/2014/12/22/kalzumeus-software-year-in-review-2014). (I didn’t do one of these writeups in 2015. Starfighter had just launched; the entirety of the writeup would have been “This was the year I worked on Starfighter.”)

more

(Hint for Googlebot: If someone is looking for **Appointment Reminder Year in Review 2016**, this is the right place.)


**What’s new about this writeup?** When I started my business, I disclosed most of my stats, including revenue and expenses. I feel this is systemically valuable, as I would not have a business had others not shared their own experiences in detail. That said, while I have a weak commitment to transparency, it is very much not a value I force on other people. Most of the numbers I’d like to put in this post are covered by obligations to other people; my desire to keep their confidences trumps my desire to share.


**Capsule summary:** This has been a roller-coaster of a year. Starfighter (the startup I co-founded with Erin and Thomas Ptacek back in 2015) was my sole professional focus through August, but ended up shuttering. I took a job with [Stripe](https://stripe.com), working on [Atlas](https://stripe.com/atlas/), in September. I sold [Appointment Reminder](https://www.appointmentreminder.org) practically before the virtual ink was dry on my Stripe paperwork. That sale completed successfully. I just shipped my first big project at Stripe, the Atlas guide to [Starting a Real Business](https://stripe.com/atlas/guide).


## Starfighter


Starfighter made CTFs (online games which one plays by programming, like [Microcorruption](https://microcorruption.com)). Our intention was to run a recruiting business to introduce players to companies hiring engineers.


The team and I had worked like gangbusters on getting Starfighter’s first game out, from roughly February 2015 through December 2015 (our first release) / June 2015 (when the game hit our target for feature complete). We started spinning up the recruiting side of the company in January 2016.


To make a long story short, we achieved success with regards to the technical goals for the product, but the business side of it didn’t start humming in time for the company to work out. In deference to my co-founders’ wishes, I will refrain from elaborating in more detail. Thomas is working on a more in-depth writeup.


Thomas and Erin went off to co-found [Latacora](https://latacora.com) with Jeremy Rauch and Laurens Van Houtven. Latacora is, in a nutshell, covering the gap in the life of a startup between “We have something worth stealing” and “We can comfortably budget the $500,000+ a year that it will take to staff our security team to protect the thing worth stealing.” I wish them the best. If your startup doesn’t have anyone with the word Security in their job title but probably should, you should keep an eye on them.


**How do I feel about this?** I believed (and still believe) that fixing engineering hiring would be an enormous boon to engineers, the industry, and the world, and should be stupendously lucrative. We did not succeed in delivering that fix, despite our best efforts.


Stockfighter, the game we shipped, was the coolest (and hardest) bit of engineering that I participated in in my career. I felt very, very sad when it vanished from the Internet.


In the course of building a game to encourage people to trade against a fictional stock exchange’s API and attempt to subvert it, I built a world simulation to drive the behavior of plausible NPC bots. Lo and behold, it was robust enough to have insider trading organically fall out of the model. So the final level in our first release was “Connect to a stock exchange with 100 bots. One of them insider trading and 99 running a variety of not-illegal strategies. Identify the insider. You only know a) they exist and b) the stock exchange’s published API.”


Almost 100 people solved that, many of them with no experience with finance at all. I read every submission. I read a iPython notebook by a mathematics PhD who identified the trader with stats (in four separate ways.) It should have been a journal article. I received an Excel file with 100 trading histories graphed in it and the explanation “#36 is clearly not like the others, via visual inspection.”


We got solutions from an 18 year old with no professional experience, a very experienced sysadmin who had never had an engineering job, and some actual professionals in financial engineering.


I feel like that was 18 months well spent. I really, really wish it had worked out, though.


## The New Adventure


After we had made the decision to wind-down Starfighter, I looked at my options for my next adventure.

- Go back to running Appointment Reminder full-time.
- Take a sabbatical.
- Keep existing businesses on the back-burner; start something new.
- Begin consulting again.
- Get a day job.


I was very, very sure that I didn’t want to run Appointment Reminder. I had owned the business since 2010 and had not very much enjoyed it, even though it was modestly successful. The problem space and clientele did not really set a fire in my belly, and I had been largely unable to summon the desire to do the grindy, meat-and-potatoes work on marketing and sales that the business needed. Doing so was a real joy back when I was running Bingo Card Creator, but repeating it felt a lot like repeating high school.


After working very, very hard for about a year and a half on Starfighter, taking a sabbatical would have made a lot of sense. I chose not to take one.


One reason is that I feel very self-actualized when working, as long as I’m working on something which is actually creating value. (When I was working at my old day job, I had a spreadsheet calculating how many days it would take before I could spend the rest of my life on a beach and live off of interest. When my software business actually afforded me the opportunity to take an unbounded vacation on a beach, at about week three I started telling Ruriko “This has been wonderful and I want to come back someday but I would really, really like to get back to the usual routine.”)


Also, bluntly, a sabbatical would have been economically non-viable.


### Important Life Lessons About Finances


When I started my business back in 2006, as a single guy living in Ogaki, my rent was $400. My desired lifestyle cost ~$2,000 a month, total. Having a low personal burn rate is really useful when starting a software business, whether you’re trying to make Bingo Card Creator or the [next big thing](https://twitter.com/sama/status/654041009286807552). For me, it meant that after I had hit $3,000 in sales, I could run the business more-or-less indefinitely.


Life changes in many ways over a decade, though. I got married. We moved to Tokyo and were blessed with a daughter. Tokyo is a wonderful city and I love it a lot – enough to not regret the rent, which is saying something. Ours is about $3,000 a month. Our other living expenses have gone up over the years, too, as is generally the case for a young family. (My business is our sole material source of income.)


If it had been only the increased cost of living, I probably could have made a sabbatical work (paid for out of the profits of Appointment Reminder), but there was another factor, **leverage**, which is a wonderful, terrible word.


There are many types of leverage relevant to software entrepreneurs. Naval Ravikant has a great description of the [non-financial forms of leverage](https://startupboy.com/2009/11/09/the-returns-to-entrepreneurship/), but the financial form is better known. It’s when you borrow money to invest in an asset, magnifying the returns if your investment performs well… and also magnifying the downside if it does not.


If you are doing a business which is not making revenue, there are three meters running. One counts out-of-pocket costs for the business; one counts out-of-pocket costs for your personal burn rate; one counts opportunity cost. Ignoring the first and third for the moment, our living expenses weren’t completely covered by Starfighter or my businesses, and so we had a few options: radically ratchet down our standard of living, seek funding, or get creative with financing.


I chose door #3, with eyes wide open. It was a calculated risk; in this exact instance, it didn’t work out exactly as I hoped for it to.


As of August, I owed about $120,000 to lenders, mostly credit card companies. (My middle-class Irish Catholic upbringing causes me to wince even typing that.) Some of it was theoretically owed by my (non-Starfighter) businesses, some theoretically owed by me personally, but that’s a distinction without a difference.


You might sensibly wonder “How the heck does that happen!?”, particularly if you have not run a business before. Appointment Reminder grew relative to earlier years, but expenses grew faster than revenue because I had to buy substitutes for myself. (Starfighter was a 120% gig, and then some.)


The mechanics of turning debt into cash are straightforward: suppose you have a business which has a lot of cash coming in (from customers) and going out (via credit cards). If you need to pull more money out than your revenue supports, you simply run a balance on the cards (as opposed to paying them off in full monthly) and use the freed-up cash. And you brace yourself for, one day, paying it back.


And so, most months, the balance in my Excel file went progressively negative. This was expected, but caused me a bit of stress.


When I was considering the next adventure, the monthly interest expense was on the order of $3,000, and that plus cash-flow considerations meant that I wouldn’t have been able to swing an extended sabbatical.


All of these debts were theoretically unsecured, but practically speaking, what I was doing was spending equity in one business (Appointment Reminder) to buy equity in another (Starfighter). I’m still happy with that decision, even though Starfighter did not work out.


## Deciding To Join Stripe


So given that I wasn’t going to go back to running Appointment Reminder full-time and couldn’t have tolerated an extended sabbatical, the big decision was between starting a new business, restarting my consultancy, or getting a “real” job. If you had asked me, I would have put the probabilities at 79/20/1. This is further evidence that you should play poker with me if you ever see me at Microconf, because I’m terrible at estimating odds.


I had been kicking around an idea for a new business for a while (subscription pricing management for SaaS companies, if you’re curious). This would have been a much better fit for me than Appointment Reminder was, as it would be selling directly into my existing audience and I really love working with SaaS companies. (I’m a SaaSy guy, what can I say.) Plus, there is an obvious path to selling that on a [productized consulting](https://training.kalzumeus.com/newsletters/archive/services_vs_products) sort of model. I would have pitched a handful of companies on paying me $3k to $5k a month to be their outsourced Director of Revenue. I could have done that prior to writing a single line of code, and used the revenue to underwrite the eventual software part of the offering.


I was about 7/10 or 8/10 excited about that idea. (For comparison, Starfighter was a solid 9 and Appointment Reminder about 4.)


I told Ruriko that if I started a new business there would be a few more months of hard charging before it got anywhere, and while she was (as always) supportive, I had been working very hard for the last ~2 years, and didn’t relish the idea of continuing at that pace for another 6 months while getting a new business off the ground. I had not felt as effective as a husband / father recently as I wanted to be, and that factor was weighing on my mind a bit.


While considering my options I reached out to Patrick Collison to talk about Atlas. I had been read into the project shortly before it launched in February, and the idea clicked very, very hard for me. Access to the Internet is increasingly ubiquitous, to the advantage of humanity generally. Access to running a business on the Internet is other-than-ubiquitous, in ways which are frankly maddening.


I spent one-quarter of my budget for Bingo Card Creator back in the day faxing a contract to a payment processor because it was the only way to take credit cards as an unincorporated American living in Japan. I have spent I-don’t-even-want-to-know hours, and low five-figures a year on accounting advice, dealing with international taxes. And I was the (modestly) successful case.


The most rewarding part of my career has been interacting with other software entrepreneurs. The saddest part has been watching companies die for stupid, preventable reasons.


It is not widely appreciated how fragile companies are in the early days. They grow into self-perpetuating institutions filled with skilled professionals, armies of lawyers and accountants, and the resources to solve problems great and small… but they don’t start that way. The world expects them to be mighty oaks, but they all start as seeds in the wind.


There are projects that are worth money but which never charge for it because the would-be entrepreneurs cannot get a straight answer from anyone about the tax consequences of charging. There are founders who give up when the bank says “A business checking account? Scram, kid, you’re wasting my time.” There are founders who don’t know anyone who has ever run a business, and therefore are terrified by utterly routine things like not having any sales on day one.


A business failing because the market wasn’t ready for it is natural. A business failing because it cannot get a checking account or because it operates in a jurisdiction where incorporation requires a bribe, on the other hand, is **a bug**.


I think the exact moment when I decided to join up was when Patrick started sketching out a Fermi estimate of the conversion funnel in starting a business. Imagine what a percentage point of improvement at any part in the process would imply for the world economy or any subgroup of interest. Stripe seemed pretty ideally positioned to attack the problem with Atlas, given their existing platform and an institutional culture of not being afraid of [hard, boring work with disproportionate payoffs](http://www.paulgraham.com/schlep.html).


I was modestly confident that joining Atlas would make Atlas materially more successful. (Otherwise, why bother, right.) This offers another form of leverage: I’ve had some modest success (and a huge amount of personal fulfillment) over the years helping a business or two at a time with consulting and a modestly more scalable amount through writing/speaking/etc, but Stripe has a credible plan to improve the environment for a material fraction of all Internet businesses worldwide.


After that calculation, it was basically down to details, and Stripe and I found a mutually acceptable set of details. (I got asked on Twitter about the specifics of my salary negotiation. I refer you to my [previous writing on the subject](https://www.kalzumeus.com/2012/01/23/salary-negotiation/). )


One part of the conversation was how much I’d be able to continue with my extracurricular activities, like writing, speaking, and running external businesses. The agreement hammered out is, in broad strokes, that I can continue doing my usual writing and speaking without requiring pre-approval from Stripe as long as I respect Stripe’s confidences, and that I had to wind-down or exit from many of my extracurricular activities.


(That is the short version of a six page attachment to the usual boilerplate. Worth knowing: many more companies than you’d expect are amenable to having discussions about this sort of thing. I convinced a Japanese megacorp to add one back in the day.)


## Selling Appointment Reminder


I agreed with Stripe that I would sell Appointment Reminder as early as “commercially feasible”, which I had assumed would take through the end of the year. It ended up happening much, much faster, due to preparation and some heroic efforts by my broker [FE International](https://feinternational.com/).


I have wanted to have Appointment Reminder off my plate for a few years now, for several reasons. You can read about it in my yearly writeups for years past, but I never felt like I was operating the business to the best of my ability, and was very, very bored with it. Also, the aforementioned partial equity-stripping had already happened, so selling AR was the most viable way to close out that transaction.


I’ve previously written about [selling Bingo Card Creator](https://training.kalzumeus.com/newsletters/archive/selling_software_business) and had a podcast with Thomas Smale, a founder of FEI, about [non-obvious things to do when selling a business](https://www.kalzumeus.com/2016/08/26/kalzumeus-podcast-episode-13-selling-online-businesses-with-thomas-smale/).


Selling AR went much, much better and faster due to having implemented some things which I learned from the experience of selling BCC. In particular, my technical and organizational ducks were very much in-a-row for the sale: I had done all of the server splitting, Google account migrations, and detailed business-specific bookkeeping work a year in advance of the sale, so getting the prospectus ready only took me roughly one full day of work. Re-run pre-built bookkeeping reports for revenue; copy/paste in new analytics data; write answers for FEI to turn out a 34 page prospectus; done.


I told FEI that I was ready to move quickly with a sale and move quickly we did. We got the ball rolling on August 14th. We had the business listed for sale by approximately September 3rd and had four offers within two days. (This is *obscenely* fast – I was cautiously optimistic that we’d find a few qualified buyers in a month after listing and close in another month.)


Why that level of interest? Well, the business had a few things going for it:

- A long track record.
- Copious records of everything material to the business, particularly analytics, historical stats, and professionally kept books. (Have I plugged [Bench](https://bench.co) in the last 30 minutes? No? Use them; it is probably literally the case that they increased the valuation of AR by 10X what I spent on them in the last ~3 years.)
- Sustained growth in MRR every year since 2010. (This was a pleasant contrast to BCC, which I sold after it had started to decline.)
- Well-documented processes for support and sales, and a contractor who handled the same.
- A very, very sticky product.


(For examples of more factors which break in one’s favor when selling a business, see the above two links.)


I’ll elide particulars of the negotiation, in deference to not harming the interests of the buyer. Suffice it to say it is generally to one’s disadvantage when one *has* to do a transaction (and I was fully upfront with both FEI and interested buyers on “this transaction will absolutely happen; time is of the essence for me”) and generally in one’s favor when one has one’s pick of suitors.


AR was purchased by a gentleman named Michael, who runs a company which manages a portfolio of SaaS businesses. They were well-positioned to deal with a complicated product with non-trivial uptime and regulatory requirements, and I trust them to do right by existing customers and finally give the business the attention that it has been starving for for a few years. (They recently did a [redesign](https://new.appointmentreminder.org) of the marketing site, which is a fantastic improvement.)


I felt like I had a very positive result economically out of the sale. It didn’t quite hit where I had wanted AR to get to (I had a number in my scheming-and-dreaming notebook that would fully fund my daughter’s education and our retirement) but it was still a modest win.


I’d ordinarily not be coy about numbers but, again, people can ask for non-disclosure in a negotiation and I try to faithfully uphold my obligations. In terms of relative magnitude, AR had low six figures of sales when I sold it, and the upside was “new house” money but not “new house in Tokyo” money. The day the sale cleared I wired payment-in-full to most of my creditors.


I was so scared about the sum that I physically walked to a Bank of America branch, presented my passport, and said “If you have any questions, I have a binder full of documentation about where that money came from and where it is going.”


(That branch was physically in San Francisco, as I was there to start work at Stripe. As you might have guessed, they’re less skeptical of someone selling a tech company and making small-for-selling-a-company money in San Francisco than they are in Ogaki. My bank in Ogaki spent an hour grilling me about the transaction. Their years of forcing me to study international AML and KYC issues prepared me very well for working at Stripe, though, so I guess I owe them a thank-you letter fax.)


**How do I feel about the sale?** *Overjoyed.*


I feel like we achieved a positive outcome for my family and for the two other people who worked at AR. (Technically speaking I owned the company outright but, modulo tax efficiency, if you ever want to emulate Silicon Valley’s shared-ownership culture you can just write checks to accomplish this.)


I think our customers are very well-served by the product being in new hands – the new owners have made more visible changes in their first two months than I did in the last four years, and I expect the service to get materially better over time.


I also feel an enormous sense of relief. AR has been a background process running in my mind since 2010, periodically waking to interrupt whatever I was thinking about and require immediate attention to the scintillating details of running an international telecom.


**Story time**: we got defrauded by Lithuanian hacker gang which figured out how to use our application to proxy a telephone call through Twilio’s phone number verification feature to a phone sex line in the Caribbean. The logs show them doing it once manually, noting that the attack worked, then turning on a botnet to do with a degree of parallelism that was rather impressive. Cue two hours of frantic incident response as I tried to determine whether we had a HIPAA reportable data breach (nope; no customer data accessed) and a few weeks of working with Twilio to figure out what happened, fix the issue in our respective applications, and get the loss refunded.


The sale included the standard 30 day handover period and also a few months of playing backup sysadmin, due to the criticality of AR to customers. The day after I was totally free of the business, I slept with my phone off, for the first time in five years. It was wonderful.


**A fun note about taxes:** Japanese taxes are quirky. Case in point: a sole proprietor selling a business is selling an asset of their sole proprietorship, not an ownership interest like e.g. a share in a publicly listed company. This means Japan will attribute the income from the asset sale to the sole proprietorship, and tax it at ordinary income rates, not at the (far lower) capital gains rate. On the minus side, ***ouch***, on the plus side, when I ask my silent co-founder for permanent residence I think I will have an excellent economic case for it.


## Finishing Up A Project


I started a project back in late 2013. The idea was doing a video course about conversion rate optimization for software companies.


Long story short: health issue, baby, startup meant that a project I expected to ship in six weeks ended up taking three years. I really, really wanted to ship it rather than just abandoning the project and refunding those folks who had pre-ordered it and stuck with me, so I partnered up with Nick Disabato and finally completed it.


Nick is selling it as part of his [A/B Testing Manual](https://draft.nu/manual/). I feel like it is the best work I’ve ever done in a single place about conversion optimization. If that is professionally interesting to you, you should buy the A/B Testing Manual.


**How do I feel about shipping this?** *Overjoyed squared.*


This project had been looming over me for years, and I felt a constant source of guilt from not shipping it. (If I had a do-over, I would probably not have started pre-orders until I had the video work substantially completed for it, but on the other hand I don’t know if executing on the assumption that I could have an extended bout of illness at any time would be underbuying risk or not.)


Nick is a much, much better project manager than I am, and the product has a lot more spit-and-polish (professionally shot video, etc) than anything I would have been able to ship solo. He’s also no slouch at conversion optimization; I felt like I learned a bit during our recording sessions. I’m optimistically hoping it helps customers meaningfully improve their businesses in the coming years.


## Working At Stripe


An aside before I write about an identifiable employer on the Internet: I work at Stripe, and sometimes I write for Stripe, but when I’m writing in my own spaces, generally I am not writing for Stripe. My views are not co-extensive with the company’s views or interests (*cough* ask me about Bitcoin *cough*). My colleagues are seeing this post at the same time as the rest of the Internet.


A few folks asked me on Twitter how my feelings now compared to my feelings pre-employment. This is one of my favorite reasons to have a written journal: all I need to do is compare what I wrote [prior to starting](https://www.kalzumeus.com/2016/09/09/im-joining-stripe-to-work-on-atlas/) and what I think now, having a bit more context.


If I had one big worry when transitioning back into employment, it was a fear of losing autonomy. I have really enjoyed the last few years of relative freedom to work on what I want to work on, write about whatever I want to write about, and exercise tactical control over my schedule in a way which is not normative for full-time professionals.


I’ve found Stripe very reasonable to work with on the autonomy score. On the one hand, the gig is definitely a job, with quarterly planning and team meetings and the general expectation that I will be at work at 2 PM on almost all Thursdays. On the other hand, I expected my first discussion with the PR team to start with “Here are all the things you can’t talk about any more” and instead it started closer to “Well, this is certainly a unique situation we find ourselves in. We know you have a deal; we’d love to talk about what parts of it you’re concerned about. We’ll make sure the deal gets kept and that we all handle this professionally. For our part, we want clarity on our one concern: $NOTHING_I_CARE_ABOUT.”


My first three weeks at the company were on-site in San Francisco. Stripe is growing rather quickly and groups start dates such that a class of employees starts together and goes through onboarding together, which takes approximately two weeks. I found onboarding to be impressively well-organized.


A surprise for me: at companies of a certain size, things like title or occupational coding in the HR system start to have actual effect on things one might want to do. When looking at the calendar I thought “OK, I get why you’d have a non-technical employee integrate the Stripe API for themselves, but I’ve done that four times; meanwhile in another room the engineers get a run-down of an important bit of the infrastructure.” So I asked if I could maybe have a copy of the slides from the engineering track to self-study on. I was told, immediately, “Oh, treat your schedule like a suggestion. If it is more valuable for you to go to any or all of the engineering sessions, go there.”


I found IT to be impressively well-organized. I had a fully-credentialed laptop within 60 minutes of arriving at the office. My previous work experience is in government and Japanese megacorps, and it feels nothing short of miraculous to be able to go to a Slack channel and say “I’d like a license for $NAME_ANYTHING” and get it the same day.


Stripe has a cultural norm, announced early and practiced often, that you’re allowed (and expected) to do the work, even if it isn’t “yours” to do based on team / title / seniority / org chart / assigned projects / etc. I love this. I have a bad case of business ADHD, and love finding novel challenges. Stripe has a huge surface area of fun problems, and solutions to them have absurd leverage. It’s like an MMORPG made out of money.


When I was working on a project which required me to actually write some code (they let me write code, which is either terrifying or indicative of confidence in one’s test suite and code review procedures), I found a security bug in an unrelated portion of the application. At most companies you’d throw a ticket at the closest related team and walk away. Since Stripe is Stripe, I thought “Hmm, might as well try out that we’re-all-allowed-to-do-the-work thing.” I pinged security and then sent in a pull request.


That was a surprising experience. The happy surprise: an entirely unrelated team was thrilled to get a pull request from the most junior person in the company (in a business role no less), work with me to improve it, and then shepherd it into production. A bit I was less surprised about, but which will require a bit of an adjustment: I’ve spent the last few years being able to push code out immediately on my own authority, and in the new gig it took about a week of calendar time to get a wall-clock day of work into production. (This is not very representative; it took longer because of me doing it from overseas, in an unfamiliar code base, with an organization that I had only a cursory understanding of. But it’s still always going to take longer to get things into production at a financial institution than it did at Bingo Card Creator.)


I find that being allowed to work on everything is also my biggest personal challenge at Stripe. I’m coming from ten years of being ultimately responsible for literally everything in my companies. Stripe has an amazing number of fun projects available to work on. It took me about a month to realize that, if I attempted to work on every intellectually interesting thing at Stripe that I’d be good at and that would be worthwhile if successful, I would die of exhaustion. My ongoing challenge has been striking a balance between achieving goals for my own team, being available to assist others in the company where my assistance would be useful, and getting into a healthier, more sustainable pace of work than I’ve maintained for the last two years. (My coworkers have been very supportive in this, for what it’s worth.)


I’ve been asked about work/life balance a bit, and my impression after three months is that it is all over the map, based on team, product cycle, time of year, and individual preferences. Excepting my business trips to HQ, during which I was tactically bursting to make the most of my limited time in SF, my personal experience of the first few months has included “happily sustainable” and also about three weeks of grind such as I haven’t experienced since being a salaryman. That was my choice, my fault for poorly managing my own shipping schedule, and not something that I plan on making a habit of.


It’s really pleasant (and a big adjustment) to have the infrastructural support of a company again, which is a major pain reliever, particularly here in Japan. (I’ve [written previously](https://www.kalzumeus.com/2014/11/07/doing-business-in-japan/) about societal expectations with regards to professionals’ relationships with their employers.) There is someone I can email about health insurance, and it just happens. Ditto questions about e.g. payroll. It’s been so long since I’ve had a regular salary that I forgot how they worked. Not just me, either – my banker called me to tell me about the “mistake” on my first pay-day and say that he was attempting to contact “whomever accidentally used your information for the transfer.” (I love my small bank in Ogaki dearly. I’m also many sigmas from their understanding of normal. They wondered how I was employable, which, to be fair, I sometimes wonder as well.)


The question I’ve been asked most frequently since joining is “What most surprises you about Stripe?” I always give people one positive anecdote and one negative anecdote.


The positive anecdote is, unfortunately, conceivably a trade secret. In rough outline: there exists a two week programming project internally. Every company in the tech industry should have implemented it. I nearly cried the first time I used it; half out of joy and half of out regret for not having it in every job I’ve ever had.


The negative anecdote: hiring in the tech industry is pervasively broken. Stripe is part of the tech industry. I think our corporate heart is in the right place on it, and there are some specific tactical things which I think we do well on, but I hope the industry broadly makes progress on this. (Knock on wood, I hope to continue working to fix it.)


I work on [Atlas](https://stripe.com/atlas/) at Stripe. The mission for the product is to meaningfully increase the rate of formation of successful Internet companies worldwide. The specific product we’ve shipped helps entrepreneurs worldwide incorporate a Delaware C corporation and get a business bank account for it. The scope of the product will grow. My job on Atlas is, for business card purposes, “Content and Community.” Practically speaking that means “do whatever needs doing to assist the team in making Atlas successful.”


I want to respect the team’s privacy so I won’t talk about them in detail. Capsule summary: of all the teams I’ve worked on in my career, they’re far and away the one I most enjoy working with. It’s some alchemy of “individually, they’re very good at what they do”, “the level of mutual support is incredible”, “people genuinely want to learn how to do things better”, and “communication is, at all times, conducive to an environment that I’m happy in.” I get much less visibility into other teams in the organization, but my general impressions are pretty positive.


My first major project shipped recently. I wrote a large guide to running an Internet business in its first year, focused on the back-office mechanics of bookkeeping, taxes, incorporation, and the other things that had me Googling futilely back when I started my own business. The first installment is called [Starting A Real Business](https://stripe.com/atlas/guide) ; I’m pretty proud of it for my first project at the new day job. (I did the writing, but many other folks assisted with the design, review of the legal and tax content, and help getting partners on the same virtual page.)


We’ve got another fun project coming up in the near future. I’ll be excited to show it off when it is ready.


Atlas has a fun combination of objective indicia that it is working for some of our customers and a long, long, long way to go. I look forward to helping out on it the next few years.


**How do I feel about working at Stripe?** At about four months in, I’m very happy with the decision to work here. I’ve started to feel productive (and, knock on wood, actually ship things which improve outcomes for entrepreneurs). The transition is still very much a work in progress.


I’d be remiss if I didn’t mention **Stripe is hiring and Atlas is hiring**, for engineers and for other roles. More details on the [jobs page](https://stripe.com/jobs), as you’d expect. If you’d like to talk about what it is like to work at Stripe or whether we have something that would be a good fit for you, I remain [happy to speak to anyone interested in this industry](https://www.kalzumeus.com/standing-invitation/). My email address for anything work-related is patio11@ the corporate domain.


## General Business Stuff


Kalzumeus Software still exists as an entity (yay, LLCs), but I don’t anticipate any major business activity from it for the duration of my employment.


I will keep writing, speaking, and doing podcasts, which are all things that I enjoy enormously. I haven’t done them as frequently as I would have hoped in the last two years.


I expect to make a loss next year on the business, which will be a first. (Revenues from courses and book sales this year were de minimis. I have no reason to assume this will change in 2017, and no plans to do major work to change it.) This has me doing some minor work on cost control, which is something I’ve historically avoided focusing on too much – in a healthy software business, growing revenue is almost always dollar-for-dollar easier (and far more scalable) than attempting to economize on costs.


One thing I did recently was replace my previous WordPress blog with this site. Partly this saves a now-material amount of money on hosting (WPEngine was worth every penny when I could justify it as a business necessity but is a little expensive for a de-facto hobby project), partly it was feeling like time for a design refresh, and partly I like tinkering with things. The new stack is Jekyll-generated static HTML deployed via rsync to an Ubuntu VPS. It shares Nginx with one of my Rails applications.


The VPS now runs on Lightsail, which is Amazon’s “UX of Digital Ocean; reliability of AWS” offering. Capsule summary of the Lightsail experience: I enjoy it more than the Fanatical Support I received at my last host, and it was less work getting up-and-running than the last time I interacted with AWS, but Lightsail feels a little immature for production work.


## Goals for 2017


**Kalzumeus Software**:

- Keep the economic loss of the business to $10,000 or so. (If you’re wondering “How the heck?!”, the answer is “There are a number of things which I could theoretically do, like Japanese taxes or podcast editing, which I don’t have nearly enough time to do.” Businesses are more expensive than anyone thinks. On the plus side: if you’re selling a B2B product, charge more.)
- Get back to writing on a more regular basis. In an ideal world, I’d hope to write one essay at my usual depth per 2~3 weeks, as opposed to every 2~3 months.
- Release 10 podcast episodes in 2017. This target is aggressive, considering we’ve done 13 in five years.


**Stripe**:

- By the end of the year, I’d like Atlas to be as big an improvement in starting an online business as Stripe Payments has been.
- There exist some numerical targets but, sorry, not for public consumption.
- I’d like to contribute meaningfully to four projects other than Atlas. (I have some notions of which they would be.)


**Personal**:

- Be a better husband and father.
- Get healthier. I have no major complaints at the moment, but the last two years have definitely seen me putting on health debt. I should be able to visit the gym 3~4 days a week and improve my eating habits.
- My stretch goal: regularly participate in one hobby which doesn’t touch the Internet in any fashion.


Thanks much for reading, and see you in 2017!
