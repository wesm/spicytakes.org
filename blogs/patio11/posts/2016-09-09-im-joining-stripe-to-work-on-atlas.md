---
title: "I’m Joining Stripe to Work on Atlas"
date: 2016-09-09
url: https://www.kalzumeus.com/2016/09/09/im-joining-stripe-to-work-on-atlas/
slug: im-joining-stripe-to-work-on-atlas
word_count: 3315
---


I’m joining [Stripe](https://www.stripe.com) to work on [Atlas](https://www.stripe.com/atlas/). Let me tell you why.


(If you don’t know me, howdy, I’m Patrick. I’ve run a succession of small software businesses from Japan for the last 10 years. They’re documented in a bit of depth on this blog and in HN comments, conference presentations, and the like.)


Some years ago, when I was still working for a Japanese company, I had a wee little side project called Bingo Card Creator. I wanted to be able to take payment for it over the Internet. Options for doing this in 2006 were absolutely terrible. I eventually signed with a shareware payment processor who wanted to keep 11% of sales for renting me their merchant account, and “signed” is to be read literally: it cost me over 1/4 of my budget to send them a fax internationally accepting their (egregious) terms and conditions.


I was quite excited when Stripe launched back in 2011, and quickly moved all of my businesses to it. In addition to being transformatively better from an API and business perspective, it was obvious from the first that [Stripe gets people like me](https://www.kalzumeus.com/2012/08/06/stripe-and-ab-testing-made-me-a-small-fortune/). (See, in particular, where their CEO Patrick Collison helped me debug a Ruby dependency issue with the use of git bisect. That *actually happened*.)


## The Global Community of Small Software Entrepreneurs


Neither Chicago (where I grew up) or Ogaki, Japan (where I lived when starting my business) is the beating heart of the global software industry. I knew no one in software growing up and assumed that the only options available were safe boring jobs at big boring companies. When a classmate at college interviewed with Google, everyone I knew advised her to get a job at a consulting company, instead, rather than taking a flyer on a flash-in-the-pan Internet thingy.


That social and educational background explains a bit of how I found myself doing soul-crushing J2EE Big Freaking Enterprise Web Applications as a Japanese salaryman. (Ask me for the full story sometime.) It doesn’t explain how I escaped that hellish existence.


*That* was largely due to a single decision of Joel Spolsky: he made a forum attached to his blog where people interested in the business of software could talk shop. I read it obsessively in my spare moments, and it introduced me to the unthinkable notion that regular old geeks like me could run software companies. I thought it was illegal, because, like Jon Snow, I knew nothing — nobody had ever told me that “creating intellectual property” is something that you *don’t need to ask permission to do* and my background therefore suggested it was either forbidden, risky, or risked being forbidden.


I never thought I could build a [Fog Creek](https://www.fogcreek.com), but I saw a bunch of other geeks building [Poker Co-pilot](https://www.pokercopilot.com) and [Perfect Table Plan](https://www.perfecttableplan.com) and [skeet-shooting scoring software](http://www.microisv.com/archives/2006/03/06/conception-to-sales-in-7-days-can-it-be-done/), and I was pretty sure I could at least do something like *that*.


So I released Bingo Card Creator, and — still cognizant of the fact that I knew nothing — I [decided to blog about what I was learning](http://discuss.joelonsoftware.com/default.asp?biz.5.357620.10) in real time. And I kept doing that for the next few years. I knew precious little about software development, but luckily the Internet is full of people who do. I knew nothing about marketing or sales, but the forum regulars were happy to talk me through the basics of AdWords and the Internet had some decent guidelines for SEO. And so on.


Fast forward ten years: I’ve built three software companies, worked in others, and now know more-than-nothing. My wee little blog and HN comments now total about ~3 million words, and other geeks have reported to me that they were able to use them to get their own businesses / careers off the ground, which makes me happier than anything else businesswise.


I’ve also spent a lot of time (a *lot* of time) online and offline with a worldwide community of practice. Just like there is a cognizable tribe of Rubyists or Pythonistas or ballet dancers, who share something with all other Rubyists or Pythonistas or ballet dancers regardless of borders or language, We Who Work For The Internet have gone out, found each other, and decided we rather like each others’ company.


We have forums. We have (nascent) professional journals. We have conferences. We started talking shop and we ended up as friends.


I’ve gone to work substantially every day for the last 10 years in my own software company, fixing bugs and running AdWords campaigns, but my biggest impact — and the most personally fulfilling one — has been helping others start and grow their own businesses.


## Silicon Valley Is Full Of Crazy People


As part of rubbing elbows online with my tribe, I’ve had contact with another tribe over the years, which is venture-backed Silicon Valley entrepreneurs. To paraphrase a remark made by a Japanese businessman of my acquaintance, they’re a society organized around attempting to find the optimal level of crazy.


When you have too much crazy, you start a social network for cat photo sharing and say — in all earnestness — that it will change the world for all days to come.


When you have too little crazy, you end up taking a safe job at a megacorp and staying even though you hate it.


When you have *just enough* crazy, you found a payments company, heedless of the fact that founding a payments company is doomed to failure because it involves


[mountains of hard and boring work](http://paulgraham.com/schlep.html) and the incumbents have billions of dollars.


Patrick and John Collison are close-to-optimally crazy. When Patrick says “Stripe’s goal is to increase the GDP of the Internet”, that isn’t like Cthulhu’s goal to make a dent in the universe. It implies real people are going to make real businesses selling real products and thereby experience real improvements in their real lives. I know this works. I have seen it. I have lived it. I have watched it work for hundreds of friends and acquaintances.


## Atlas Is Crazy


A couple of months ago, Patrick Collison came to me with another crazy idea. He said Stripe wanted to make “simple incorporation as a service”, so that any entrepreneur worldwide could have a corporate entity and a bank account spun up about as easily as they could get an EC2 server.


This idea is crazy. I’ve incorporated four companies and opened business bank accounts for all of them. The most recent required over a hundred pages of documentation and six weeks of negotiation to assuage a risk department’s concerns about foreign tech entrepreneurs. (Thanks, [Bitcoin](http://www.wsj.com/articles/SB10001424052702303801304579410010379087576).) You’re not supposed to be able to do this.


Stripe did it. With crazy speed: the project was in beta within 11 weeks of conception. It can take that long *to form a single company* in much of the world. Stripe solved the problem like an engineer: establishing one company requires an annoying amount of form-filling so instead of buckling down and doing it you just make a company-establishing web application and abstract away form-filling for all time.


And they’re crazily ambitious about where it ends up: not simply incorporating companies, but eating all of the crufty back office work which distracts Internet businesses from getting more real products into the hands of real customers. Payments, contracts, invoices, bookkeeping, incorporation, taxes, etc etc, all things you have to do even if what you’re *actually* doing is selling bingo cards to elementary schoolteachers.


Patrick describes the success case for Atlas as being visible in global macroeconomic indicators, which is crazy. That said: if you’ve seen how fragile new businesses are at the margins (“Can I get a bank account? Can I get an insurance policy issued in time to close this first deal? Can I get a corporate entity spun up to actually be able to sign a lease or write employment contracts?”), then interventions early in the business funnel may well increase the number of successful businesses surviving to major milestones like launch, profitability, bringing on employees, and sustained economic impact. And if you believe that new businesses are where economic growth is going to come from, that sounds very impactful. Perhaps even crazily impactful, for well-established economies like [the US](http://www.kauffman.org/what-we-do/resources/entrepreneurship-policy-digest/the-importance-of-young-firms-for-economic-growth) and [Japan](http://www.mckinsey.com/~/media/mckinsey%20offices/japan/pdf/future_of_japan_executive_summary_march_2015.ashx) and for [emerging economies worldwide](http://www.worldbank.org/en/news/feature/2016/06/20/entrepreneurs-and-small-businesses-spur-economic-growth-and-create-jobs).


## The Crazy, It Is Catching


My co-founders and I made the decision recently to wind down our last business, Starfighter, and pursue new adventures. I thought I was going to sell Appointment Reminder (the SaaS business which I’ve run for the last few years, and never really loved) and start another small SaaS business. That would pay the rent and let me continue writing and speaking with other entrepreneurs, which is the part of this gig that I really enjoy.


Patrick had a crazy proposition for me: why don’t I come work for Stripe on Atlas.


I found myself saying yes, largely because I think the potential impact of Atlas (and Stripe generally) is crazily high.


There are probably about a hundred thousand We Who Work For The Internet. There will shortly be a few million, and there will eventually be hundreds of millions.


The firm is a technological innovation which changed the world forever. The Internet is a technological innovation which changed the world forever. Firms which live on the Internet are already happening. Their growth, in number and aggregate impact, is inevitable.


## There Is No Future For Scarcity


(This section owes more than a little bit to Naval Ravikant’s thoughts on leverage, most succinctly captured [here](https://startupboy.com/2009/11/09/the-returns-to-entrepreneurship/).)


There is no conceivable future in which Internet-enabled firms are less numerous than e.g. insurance agents, which the US alone has ~450,000 of.


There is no conceivable future where it becomes harder to make products people are willing to pay for than it is in 2016. The technologies will change, but Rails is now the lower bar of how productive a software platform can be. Getting your physical product manufactured by a contract factory in China is within the capacity of college students in the first world; that or similar capabilities will only get more broadly distributed.


There is no conceivable future in which it gets harder to charge people money than it is in 2016. It cost $250,000 and six months of integration to charge a single credit card online in 1999. By 2006, that was down to hundreds of dollars and weeks of effort. In 2016, the integration can be done in a morning and the costs have likewise cratered. We will not forget how to do it.


There is no conceivable future where the network-effect businesses we use to reach customers — Google, AdWords, Facebook, the App Store, Twitter, Kickstarter, Alibaba, etc — collectively retreat in the number or aggregate affluence of the potential customers they can address. (See footnote.)


There is no conceivable future in which the number of people connected to the Internet shrinks. There is no conceivable future where smartphones become more exclusive products than they currently are.


There is no conceivable future in which the percentage of transactions consummated online decreases from its present ~1% in the most connected economies. The number of transactions worldwide will rise, by orders of magnitude.


These fundamental economic forces will continue bringing down the cost of starting new businesses and increasing the potential impact they have, even at very low levels of capitalization. We will see an explosion of them.


## So Why Hasn’t It Happened Yet?


Our future colleagues are presently prevented from starting by a host of logistical difficulties and informational barriers. They don’t have business bank accounts. They don’t know what bookkeeping is. They’ve never negotiated a master services agreement. These are all things that can be learned, but the depth and breadth required from an aspiring entrepreneur feels forbidding.


So I’m joining Atlas to work on community and communication, which means something like “scalably educate the world’s Internet-enabled entrepreneurs, reduce any barrier to entry, and assist the global community of practice in growing to accommodate *a lot* more people.”


Hopefully the next few years look a lot like the last few years: code, write, talk, present, and be as helpful to as many people as possible. The main difference is that I now get scored on that impact directly, as opposed to it being a fun sideline hobby while my day job is actually shipping and selling business productivity software.


Stripe’s interest in increasing the GDP of the Internet is fairly transparent: they intend for Stripe to be the obvious choice for payment rails of every Internet business, and for Atlas to be the obvious choice for the back office of every Internet business. If that comes to pass, Stripe will be an enormously successful company.


## Back To Working In Japan


I spend most of my working time on the Internet, but I actually live in Japan, and rather enjoy it here. If I have one professional regret, it is that fairly little of my work directly improves my local community.


I’m excited for the future of Stripe Japan.


Stripe Japan has a weird constraint where it has to be true to being Stripe (an entrepreneur-friendly focused-on-developers company) and, simultaneously, an authentically Japanese company.


I happen to be a bilingual developer-turned-entrepreneur who can pull off Responsible Japanese Salaryman when required. I look forward to helping Stripe Japan earn the trust of Japanese companies and be a pleasant environment for a multinational, multicultural team to work in. Also, I can help the mothership understand when they’re asking Stripe Japan to operate at incorrect levels of crazy.


We hope to grow Stripe Japan to a thriving software company in its own right. In addition to directly employing people in jobs which are better than those historically available here, we hope to provide additional evidence that a better way of working is possible.


Naturally, we hope to reduce payments as a barrier to entry among Japanese companies. There is a mind-boggling amount of cost and complexity to taking non-cash payments in Japan. Ask me if you’re curious, but the short version is that historically minimum-viable-online-payments has required more than a million dollars in capital. (Thankfully, this is starting to change.) That’s why anecdotally Japanese entrepreneurs have told me for years that they’re more jealous of Americans having access to Stripe than any other company.


We’re going to give entrepreneurs at all stages the Stripe experience that US startups now take for granted and *also* access to the walled gardens of Japan’s native payments ecosystems.


There are plenty of barriers to running a company in this country. Historically, the mechanics of collecting money are a major one. We will solve that problem.


## Back to Being An Employee


I didn’t think I was ever going to be an employee again, and honestly, I have mixed emotions about it. That’s why I turned down other opportunities in the past.


Stripe is offering a very compelling mixture of impact and autonomy. I’m particularly attracted to the company culture of employees not being restricted to individual job descriptions, but rather getting autonomy and ownership to bring projects to completion. That appeals to the broad-spectrum generalist in me. It helps that the Atlas team is presently tiny and in dire need of broad-spectrum generalists. Some people would feel overwhelmed if asked to write Ruby, negotiate with vendors, and construct lifecycle email sequences — that sounds to me like a fulfilling way to spend any given Tuesday.


At the same time, I’m looking forward to working with a team. One of my favorite parts of Starfighter was working with smart co-founders and *not* having sole responsibility for generating forward progress in the company, which is the nature of the beast in self-employment. It will be nice to know that payroll, legal, devops, and the like are sorted by competent professionals who enjoy doing them, so that I can be a competent professional on the things I’m actually good at and not have to worry if the server is down at 2 AM.


It’s going to be an adjustment to having a boss again. It might be a bit of an adjustment for Stripe, too, as their expectation that I operate autonomously will probably not always coincide with their immediate desires.


Fun story: I’m probably their only employee who asked for “Employee will be permitted to continue criticizing Bitcoin in their personal capacity, despite the fact that Bitcoin is a technology that Stripe [uses and promotes](https://stripe.com/bitcoin)” to be written into the employment contract. (One might sensibly wonder if that were actually intended as a [“no brown M&Ms”](https://www.entrepreneur.com/article/232420) clause simply to test how serious they were regarding autonomy, but no, I just wanted to continue criticizing Bitcoin. Everyone needs a hobby.)


## What Happens To Your Other Businesses?


**Starfighter**: [Starfighter](https://www.starfighters.io) will be winding down operations. We experienced the oldest startup story: we shipped a great product but the business didn’t end up working out. I wish Thomas and Erin the best in their new adventure and they are likewise rooting for me at Stripe. I also wish our players and clients success in their future endeavors — feel free to contact me down the line if I can help you out (in my personal capacity).


If you want to know more about Starfighter, please check Starfighter spaces.


**Appointment Reminder**: Appointment Reminder will be sold in the next few weeks, through [FEI](https://www.feinternational.com), who I used to sell Bingo Card Creator last year. As of the publication of this post, the sale is already deeply in progress. If you have questions, please route them to FEI.


I’ll likely write up what I learned from AR at some point.


**Kalzumeus Software**: I will continue periodically writing and speaking in my personal capacity here and at my usual watering holes, but imagine that Atlas will be more than enough work for the next few years. I will likely not do any new products under the Kalzumeus banner.


Incidentally, I’ve partnered with [Nick Disabato](http://draft.nu) to finally finish that conversion optimization course I have been working on for forever-and-a-day, as my last bit of major creative work prior to starting with Stripe. (We wrapped two days of video shoots five minutes ago.) More details from Nick and I on our respective mailing lists as that is ready to show.


## Want To Work At Stripe?


Stripe is hiring. Atlas is hiring. Stripe Japan is hiring. Their jobs page is [here](https://stripe.com/jobs).


The overwhelming majority of jobs in the technology industry do not go to people who cold apply via jobs pages. This is important for you to know and operationalize. In general, you want to find someone inside the company who has hiring authority, make a good impression on them, and then get them to start the ball rolling on an internal application process.


I don’t have hiring authority, but I’ve had a [standing invitation](https://www.kalzumeus.com/standing-invitation) to talk to anyone interested in the software industry open for several years, and that isn’t going anywhere. I work *at* Stripe; I work **for** the Internet. If you’re on the Internet, I work for you, too. If you’re interested in potentially exploring options at Stripe, feel free to email me. I’ll happily take you out to coffee and/or a Skype call, give you the inside scoop, and make sure you’re routed to one of the friendly, accessible people internally who can actually make the hiring process happen. You cannot possibly waste my time.


See you on the Internet, and thanks.


### Footnotes


There is a conceivable future where the de-facto monopolies that control discovery levy a 30% business privilege tax on the entire Internet, but living in that hypothetical cyberpunk dystopia would still be superior to every economic arrangement prior to the Internet. Man, what a downer of a footnote. Have I mentioned that it’s a good thing to make payment rails that don’t go through AppAmaGooBookSoft?
