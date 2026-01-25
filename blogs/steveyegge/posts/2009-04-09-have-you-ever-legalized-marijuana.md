---
title: "Have you ever legalized marijuana?"
date: 2009-04-09
url: https://steve-yegge.blogspot.com/2009/04/have-you-ever-legalized-marijuana.html
word_count: 5499
---

Over the holidays I read a neat book called
, by Dan Ariely.  The book is a fascinating glimpse into several bizarre and unfortunate bugs in our mental software.  These bugs cause us to behave in weird but highly predictable ways in a bunch of everyday situations.
For instance, one chapter explains why bringing an uglier version of yourself to a party is guaranteed to get you more attention than other people who are arguably better-looking than you are.  I personally do this all the time, except that I'm usually the ugly one.  The same principle explains a ploy used by real-estate agents to get you to buy ugly houses.
Another chapter explains the bug that causes you to be a packrat, and shows why you desperately hold on to things you own, even if you know deep down that they would rate lower than pocket lint on eBay.
In any case, well, good book.  I'm going to harsh on it a teeny bit here, but it's only one tiny part towards the end, one that actually has little to do with the rest of the research presented in the book.  I still highly recommend it.  It's only about a 4- or 5-hour read: beyond the reach of most social-network commenters, perhaps, but you can probably handle it just fine.
So: about that harshing.  Dan Ariely, who seems like a pretty fascinating guy in his own right, independent of his nifty book, says something that's kinda naïve towards the end.  It doesn't
*seem*
naïve at all when you first read it.  But naïve it is.
Towards the end of the book — and I apologize here, since my copy is on loan to a friend at the moment, and you can't search inside the book on Amazon.com no-thanks to the book's publisher, so I can't double check the exact details — but towards the end, Dan works himself into a minor frenzy over what seems like a neat idea about credit cards.
**Credit Card Buckets**
Dan's idea is simple and appealing: let's partition credit limits into "buckets".  People are always maxing out their credit cards, and it leads to all sorts of financial misery, since the rates are always by definition just epsilon short of legal usury, so most people can never, ever pay down the debt.
Dan's idea is more or less as follows: you divide up your credit card available balance into "buckets", where each bucket represents a type of expense.  You might, for instance, have a bucket for rent and utilities, a bucket for alimony, a bucket for chocolate and desserts, a bucket for sports and leisure activities, a bucket for dining out, a bucket for home improvement, a bucket for groceries, and a bucket for discretionary spending, or "misc".
Each bucket would have its own credit limit, and the sum of all the individual limits would be your credit limit.  Let's assume you pay off your credit card entirely every month — not typical, but it simplifies the explanation.  Each month, you'd have a certain amount of money to spend on each bucket, and you would not be allowed to spend more than the limit for that purchase type.
OK, so that's the way I understood the proposal.  There were several pages devoted to it, as I recall, so I may have missed a few nuances here and there, but I'm hoping I've captured the essence of it.
As an aside, I read a short diatribe many years ago by a working mom whose kids were always asking her why they couldn't spend more money on entertainment purchases like video games.  She was having trouble getting through to them, so one month she took her paycheck, went to a bank, and got it issued to her in 1-dollar bills.  She took the bills home and piled them up on the table in front of her kids, who were amazed at the giant pile of money she had made.  She then went through her budget with them, stacking the bills into piles by expense type: this many dollars for rent, this many for utilities, this many for groceries, this many for soccer uniforms, etc.  At the end there were only a couple of dollars left, and the kids soberly realized that they needed to wait about 20 years and then start downloading games illegally online.
Anyway, Dan's idea was kind of similar.  In order to train consumers not to overspend in a given category, leading to overall overspending, they would be able to opt-in to a program that partitioned their credit, and presumably it would lead to much wiser, more deliberate spending.
It seemed logical enough to me!  It sounds similar to calorie-counting: I've found that explicitly keeping track of my calorie consumption each day does wonders for lowering my overall calorie intake.  Along the same lines, I am 100% sure that if I had an explicit budget, rather than just a vague gut feel for how much I'm spending, then I would spend less money each month.  We don't really have a proverb for this concept, but we do for the opposite: "out of sight, out of mind".  If your budget is in plain sight, well then...
Plus the idea of having
*types*
in my credit-card accounting was all the more alluring since I'm a programmer, and I "get" the idea of types.  Types are great.  Dan is effectively suggesting a strongly-typed approach to credit-card spending, so the programmer in me was all for it.
**Evil Banks (as if there's any other kind)**
Unfortunately, this story has a sad, bitter ending.  Normally I
*would*
want to add:  "like all overly-strong-typing scenarios", but that would just be mean.  So I'm not saying it!
Dan goes on to explain that banks are far too evil, or at any rate far too self-serving to implement his incredibly cool idea.  He actually took the idea to at least one bank, meeting with their board of directors and presenting the idea.  How cool is that?
Dan says the bank executives seemed to like his idea, and indicated that it might be a great way to get new customers.  Credit cards are all pretty much the same (i.e., loan sharks), so they need to find ways to differentiate themselves.  A nifty credit-bucketing program seemed like something marketing could run with.  They all said they'd look into it and see about maybe implementing it.
And then... nothing.  They never implemented the idea!  Not even a little prototype of it.  Nothing.
Dan theorized that profit margins, as always, are the culprit here.  Even if banks could potentially sign up more customers on the promise of better spending control, there's a fundamental problem here, which is that credit cards make money for the banks
*based on spending*
.  If consumers aren't spending as much, the banks won't make as much profit!
Banks make money off credit cards in at least three ways: they charge the merchant a fee at point of sale, they charge you interest on the loan, and they charge you fees such as the overdraft fee when you inadvertently overspend your limit.  All those ways require you to make purchases, and the last way actually requires you to overspend your limit — exactly what Dan's idea is trying to prevent!
I suppose a truly evil bank might look at buckets as an opportunity to screw you on fees for each individual bucket.  But Dan seems to think that on the whole, the fear of decreased margins — induced by the suddenly more rational consumer spending — is what is preventing banks from implementing his idea.
At the time I was reading the book, I thought, well gosh, I
*hate*
banks.  In fact, I don't even
*use*
a bank — I now use an investment brokerage that has banking services on the side.  You don't have to be rich to do this, and it saves you from ever having to walk into a bank again.  And if you choose this route, then whenever you walk into a bank you will immediately be struck by what amazing ghettos they are: little brick buildings with little vaults holding your little dollars, little lines to talk to little tellers who provide you with little help...  they're awful.  They stink.  I detest banks; I've found the whole notion loathsome for at least ten years before hating them became globally fashionable a few months ago.
So yeah.  Dan had me.  The banks are evil.  That's why they aren't implementing his idea.  Case closed.
**The little winged nagging programmer angel on my shoulder**
So just like Memento Guy in L.A. Confidential, my mind wouldn't let the case close forever.  (Why can I remember Rollo Tomasi but not the actor's name?  Oh wait, Guy Pearce.  Him.)
For the next couple of weeks, Dan's situation replayed in my head like a bad song.  I myself have given presentations to boards of executives in the past, usually presentations that had come to naught, and I felt a certain empathy with him.
As it happens, I also served time in Amazon.com's Customer Service Tools group for four years, leading the group for the latter half of my stay, and I know a thing or two about credit-card processing.  Not a whole lot, but definitely a thing or two.
And I'm a programmer.  Just like you.  (You might not know it yet, but you are.  Trust me.)
The programmer part of me started wondering: how would I implement Dan's idea?  What would it take to add "bucketization" to credit cards?
And the programmer part of me started to get a sinking feeling in the pit of his... uh, its... stomach.  It got the chills.  And a fever.  At the same time.  Why?  Because
*it*
, by which I mean "a part of me that wishes I could forget it", has been on software projects like that before.
The little nagging voice in my head started enumerating all the things you would need to do, like counting so many sheep.  First I imagined I worked at the bank, some poor schmuck of a programmer wearing a suit, working bankers hours and golfing every day at 3pm.  So, you know, pros and cons.  Then I imagined my boss coming in and saying: "Steve, we gotta implement Buckets.  The board just approved it.  Make it happen.  Yesterday."
Aw, crap.  OK, what to do.  First, we need a spec.  So, like, I ask my boss a few preliminary questions:
- Can customers control the buckets, or are they fixed?
- If fixed, how many are there?  What are their names?
- Let's assume for the remaining questions that they are NOT fixed, since a predefined set of buckets would be "insanely stupid" and rejected by customers.  So, how many buckets can a customer make?  Min and max?
- Can customers give the buckets names?  If not, do they have to use numbers?
- What characters can they use in the name?  What's the maximum length?  If we need to truncate the name in a printed statement, how do we truncate it?
- Can a customer change their buckets mid-month?
- Can a customer change their buckets between months?  What if their balance is nonzero?  Can they transfer balance between buckets?
- Can a customer change the name of a bucket?  Do names have to be unique?
- Exactly *how* does a customer name a bucket?  Online?  Over the phone?  By snail mail forms?  Talking to bank teller?  All of the above?
- Same question for all other configuration settings.  How?  Where?
- Do credit-card customer service reps have to know about the buckets?  How much do they have to know?  *(hint: everything)* Is there training involved? *(hint: yes)*
- Do the customer-service tools have to be redesigned to take into account this bucketization?
- What about the bank's customer self-service website?
- What about the phone interactive voice-response tree?
- What about the software that sends email updates to the customer?
- What about the software that generates printed billing statements?  How exactly does it represent the buckets, the individual spending limits and balances, the carry-overs from month to month, the transfers, the charge-backs, the individual per-bucket fees?
- What about the help text on the website?  What about the terms and conditions?  What about the little marketing pamphlets?  Should they try to explain all this shit, or just do some hand-waving?
- Can a customer insert a new bucket into the list?  How are the credit limits of the remaining buckets re-allocated?  What if adding a new bucket puts one or more of the older buckets over the limit?  Do we charge fees?  Do we tell the customer they're about to be charged a fee right before they create the bucket?  Is it, like, OK/Cancel?  Do we send them a follow-up email telling them they just fucked themselves over?  What exact wording do we use?
- Can a customer delete a bucket?  What if there's money in it?  What if it's overdrawn?  How do we represent the overdraft fee in the database?  How do we show the deletion event in their bill?
- Can a customer merge or consolidate buckets?
- What if a customer has an emergency situation, plenty of limit in other buckets, and they really really need to charge to a couple of buckets, but they want to avoid an overdraft fee?  What do they do?  Are the buckets mandatory or discretionary?
- How the hell do we even tell if they're buying "chocolate", anyway?  The vendor doesn't tell us the purchase type.  How do we know how to charge the right bucket?  What if it's ambiguous?  What if the buckets overlap?  Does the customer need a point-of-sale interface for deciding which bucket to put the charge in?  Can they do "separate checks" and split the charge into several buckets?
- Where are you going?  Answer me!
- WHAT THE EVER-LOVING *FUCK* ARE YOU PEOPLE SMOKING?  HUH?  HAVE YOU EVEN THOUGHT ABOUT THIS PROJECT FOR MORE THAN A MILLISECOND?  THE SPEC FOR THIS PROJECT WILL BE 5,000 PAGES!  IT WILL TAKE THOUSANDS OF MAN-YEARS TO IMPLEMENT, AND *NOBODY* WILL UNDERSTAND HOW IT WORKS OR HOW TO USE IT, EVEN IF WE SOMEHOW MANAGE TO LAUNCH IT!  IT'S FRIGGING IMPOSSIBLE!  IT'S INSANE!  __YOU__ ARE INSANE!  I QUIT!  NO, WAIT, YOU'RE FIRED!  ALL OF YOU!  AAAAAAAAAUUUGH!

The little nagging white-robed behaloed programmer whispering in my ear was getting pretty goddamned irritating at this point.  And it asked a LOT more questions than the ones in the list above, which is merely a representative sample.  My stress level began approaching what I might call "Amazon levels", and I don't even work there anymore.  Thank God.
But for all its downsides (e.g. as voiced by my brother Mike, who was in the Navy on an aircraft carrier in the Persian Gulf during the 1990s Gulf War, and later worked at Amazon, and declared after four years that Amazon was _way_ more stressful), Amazon did teach me a valuable lesson, namely that YOUR IDEA IS INSANE.  It doesn't even matter what it is.  It's frigging insane.  You are a nut case.  Because anything you try to do at Amazon these days involves touching a thousand systems, all of which are processing gazillions of transactions a second, and you want to completely redo the database schema, and
*you don't even know the answers to these fucking questions, DO YOU?*
I suppose I should think of it as a valuable experience.  If nothing else, I understand Complexity in a way most people will, mercifully, never have to.
Anyway, I hope I've imparted the basic flavor of my thinking after having been totally bought into Dan's idea.  Here's how I (now) envision the days just after Dan's meeting with the bank executives:
**Day 1:**
*(executives)*
: Managers, we'd like you to look into this incredible new idea from Dan Ariely.  We think it could revolutionize consumer credit-card spending in a way that makes everyone love us and sign up for our services, dramatically increasing both our profit margin and our overall customer satisfaction.  And it's an incredibly simple idea!
**Day 2:**
*(managers)*
: Programmers, project managers and marketers, we'd like you to flesh out this idea from On High, and give us some time estimates.  We all know we only have a budget of about 2 months for ideas from the Board this year, so let's try to make it fit.  How long will it take?
**Day 3:**
*(grunts)*
: A billion years.  We quit.  Fuck you.
**Day 4:**
*(managers)*
: Executives, we think it will take about 3 years.  It's surprisingly hard.  We wouldn't be able to do anything else at our current staffing levels.  Should we move forward?
**Day 5:**
*(executives)*
: Two
*years*
?  Good lord!  For a project that _might_ increase our profit margins and customer satisfaction, but could also cause customers to be so confused that we have to triple our Customer Service headcount?  We don't think that sounds... well, reasonable.  Although it would be a very interesting experiment, it's simply too expensive for us to attempt.  Should we tell Dan?  Well... it might be patentable, and we might be able to get around to it
*someday*
if there's a sudden glut of programmer expertise, so... maybe we'd better just sit on it for now.  Who's up for golf?
In reality I'm sure it went down a
*little*
different from that.  For instance, they may have had the Day 5 meeting late, and then gone to a strip club instead of a driving range.
But I'm pretty sure that aside from the mundane details, that's exactly how it went down.  Because that kind of shit happened at Amazon pretty much every week I was there, for almost seven years.  (And astonishingly, we actually managed to launch at least half those crazy ideas, by burning through people like little tea lights.  But that's another story.  Plus, no bank can execute like Amazon can.  Banks just don't have the culture for it.  Bless 'em.)
**Legalization**
So.  I'm two glasses of wine into this whine.  I'm going to go get a third glass, mark the calories off in my spreadsheet, and then wrap up.  If you don't know what's coming by now, then you're pretty stupid, but on the plus side you're an amazingly fast reader, so I'll go through the motions anyway.
<gets third glass>
It doesn't actually matter what your stance is on the legalization of marijuana, for purposes of this little essay.  You could be radically opposed to it on religious, moral, or "parental" grounds.  Or you could be so radically in favor that you've been laughing hysterically and rubbing your hands together incessantly ever since you started reading this post.  If you know what I mean.  Or you could be somewhere in between, moderate and yet open-minded.
It doesn't matter.
This blog is about
*complexity*
, the bugbear that haunts software developers, program managers, project managers, and all other individuals associated with trying to launch new software projects and services.
Dan Ariely would have made a great VP (that is, Vice President).  If you think that legalizing marijuana is a black-and-white, let's just decide it and get the frigging thing legalized once-and-for-all issue, then you too have some VP blood in you.
VPs have what my brother Mike refers to as "Shit's Easy Syndrome".
You know.  As in, shit's easy.  If it's easy to imagine, then it's easy to implement.  Programming is just turning imagination into reality.  You can churn through shit as fast as the conscious mind can envision it.  Any programmer who can't keep up is an underperformer who needs to be "topgraded" to make room for incredible new college hires who can make it happen, no matter what "it" happens to be, even if they have to work 27 hours a day, which of course they can because by virtue of being new college hires, they have no social lives and no spouses or significant others, and they probably smoke a lot of crack from being in the dorms so they can stay awake for weeks at a time.
That's the kind of programmer we need at our venerable institution.  And we are completely anti-slavery, for the record.
Shit's Easy syndrome is, well, pretty easy to acquire.  Heck, you don't even have to be a VP.  Directors sometimes get it if they stay away from the code for too long.
As for the rest of us, well, we ought to know better.  YOU, as a frequenter of reddit and a programmer (wannabe or actual, it doesn't matter),
*you*
ought to know better.
Let's ask our little naggy angel: what would it take to legalize marijuana?
I don't know the answer, and I'm certainly no expert, but I've been on enough projects like this to know how to start asking the right questions.
**What exactly do you mean... "legalization"?**
So... one minor, teeny-weeny almost insigificant caveat before I continue: I have smoked marijuana (and inhaled it, deeply) on more occasions than I can count.  And yet I'm almost undoubtedly smarter than your kid that you're so goddamned worried about.  I skipped three grades (3rd, 7th and 8th), entered high school at age 11 and graduated at age 14, took A.P. courses, had stellar SAT scores, was a U.S. Navy nuclear reactor operator, went to the University of Washington and earned a Computer Science degree, worked at major corporations like Amazon.com and Google for many years as a senior staff engineer and/or senior development manager, and now I'm an internationally famous blogger.
I don't usually dwell on that, but today it's relevant.  It's relevant because I've smoked a LOT of pot, and I dare you to prove that it has impaired me in any scientifically detectable way.  We would debate, and you would lose; nevertheless I
*double-dog dare you*
.
So, well, sure... from
*that*
perspective, yeah, I'm in favor of legalization.  The laws are stupid.  Legalize it, already.  For cryin' out loud.  Jeez.
However, from a
*programmer's*
perspective (and keep in mind that I was also an Engineering Project Lead at Geoworks for 3 years, a Technical Program Manager at Amazon for a year, a Senior Development Manager at Amazon for about 5 years, and now I'm a plain-vanilla programmer with 3.5 years at Google, so I've done it all), the idea gives me the chills.  And a fever.
Because laws are pretty much like programs.  You have to specify their behavior at almost (not quite, but almost) the same level of detail, using a language that's almost as crappy as our programming languages today — English.  Or whatever your native language is: it sucks too.  If you don't believe me, ask a lawyer.  Or try to write a technical spec in your native tongue that the programmers don't ultimately poke full of holes.
Aw, don't try.  Don't even bother.  Just trust me on this one.  Today's natural languages are completely unsuitable for specificity, and "legalese", as much as we all love to ridicule it, is our collective best effort to permit being logical, specific, and unambiguous.
I have more respect for The Average Reddit Commenter than I have for, well, the average commenter in any other forum, period, assuming that "period" is stevey-legalese for "except for LTU, news.ycombinator and their ilk, mumble mumble."
But the Average Reddit Commenter has gone too far.  Everyone these days, when debating the merits and demerits of marijuana legalization, seems to have completely overlooked the fact that it's HARD.  It's a project of vast, nearly unimaginable complexity.
Think about it.  What kinds of laws do we have about alcohol and tobacco?  Is it just one law each, saying "it's legal" or "it's illegal?"  Of course not, and you're insulted that I asked such an obviously rhetorical question, yet intrigued by my line of reasoning.  Admit it!  How is marijuana similar to alcohol?  How is it different?  How is it similar and different to tobacco?
Let's let the little angel ask a few preliminary questions, just to see where it takes us, shall we?
- Is it legal to drink alcohol in a TV commercial?  No?  OK, what about marijuana, then?  Can you smoke it in a commercial?  Can you SHOW it?  Can you talk about it?  Can you show marijuana smoke at a party, without anyone actually being seen smoking it?  Can you recommend its use to children under the age of 9?  What exactly are the laws going to be around advertising and marijuana?
- Do we let everyone out of prison who was incarcerated for possession and/or sale of marijuana?  If not, then what do we tell them when they start rioting?  If so, what do we do with them?  Do we subsidize halfway houses?  Do we give them their pot back?  How much pot, exactly, do they need to have possessed in order to effect their judicial reversal and subsequent amnesty?  A bud?  An ounce?  A cargo ship full?
- Is it legal to sell, or just possess?  If the latter, then how do we integrate the illegality of selling it into the advertising campaigns that tell us it's legal to own it?
- If it's legal to sell it, WHO can sell it?  Who can they sell it to?  Where can they sell it?  Where can they purchase it?  Are we simply going to relax all the border laws, all the policies, all the local, state and federal laws and statutes that govern how we prioritize policing it?  All at once?  Is there a grandfather clause?  On what _exact_ date, GMT, does it become legal, and what happens to pending litigation at that time?
- Are we going to license it?  Like state alcohol liquor licenses, of which there are a fixed number?  What department does the licensing?  How do you regulate it?  Who inspects the premises looking for license violations, and how often?  What, exactly, are they looking for?
- Is it OK to smoke marijuana at home?  At work?  In a restaurant?  In a designated Pot Bar?  On the street?  Can you pull out a seventeen-foot-long water bong and take a big hit in the middle of a shopping mall, and ask everyone near you to take a hit with you, since it's totally awesome skunkweed that you, like, can't get in the local vending machine?  If it's not OK, then why not?
- Can you drive when you're stoned?  What's the legal blood-THC level?  Is it state-regulated or federal-regulated?  For that matter, what is the jurisdiction for ALL marijuana-related laws?  Can states override federal rulings?  Provinces?  Counties?  Cities?  Homeowners associations?
- What exactly is the Coast Guard supposed to do now?  Can illegal drug smugglers just land and start selling on the docks?  Are consumers supposed to buy their marijuana on the street?  What happens to the existing supply-chain operations?  How are they taxed?  Who oversees it?
- Can you smoke marijuana on airplanes?  Can airplanes offer it to their customers in-flight?  Is it regulated in-flight more like tobacco (don't get the smoke in other peoples' faces) or alcohol (imbibe as you will, as long as you don't "appear intoxicated"?)  What about marijuana brownies?  Are you allowed to eat it in areas where you're not allowed to smoke it?
- Can an airplane captain smoke pot?  A ship captain?  A train conductor?  The driver of a car?  An attendee at a Broadway musical?  A politician in a legislative session?  What is the comprehensive list of occupations, positions and scenarios in which smoking pot is legal?  What about eating pot?  What about holding it?  What about holding a pot plant?  What about the seeds?
- Speaking of the seeds, are there different laws governing distribution, sale and possession of seeds vs. plants vs. buds vs. joints?  If so, why?  If not, why not?
- What laws govern the transportation of marijuana in any form into or out of countries where it is still illegal?  What policies are states able to enact?  Is it OK under any circumstances for a person to go to jail over the possession or use of marijuana?  If so, what are those circumstances?
- Are there any laws governing the use of marijuana by atheletes?  U.S. military personnel?  Government employees?  Government contractors?  U.S. ambassadors, in title or in spirit?  What are our extradition laws?  What do we do about citizens who are subject to the death penalty in countries like Singapore for the possession of sufficient quantities of what we now consider to be legal substances?
- What about derivatives?  Are the laws the same for hashish?  How do we tell the difference?  What if someone engineers a super-powerful plant?  How do the new laws extend to a potential spectrum of new drugs similar to THC?
- For driving and operating machinery, do we have legal definitions that are equivalent of blood-alcohol percentage, and if so, what are these definitions?  How do we establish them?  How do we figure out what is actually dangerous?  How do we test for these levels?  When they are established, do we we put up signs on all roadways?  Do we update the Driver's Education materials?  How do we communicate this change to the public?  How does legalization impact our public health education programs?  Do they have to immediately retract all campaigning, advertising and distributed literature that mentions marijuana?  How does legalization interact with the "Say no to drugs" programs?  Do we need extra education to differentiate between a drug that is now legal (but wasn't before) and drugs that are still illegal?  What's our story here?  What about other drugs that are even less addictive and/or less intrusive than marijuana? Monsanto is eventually going to sue the living shit out of *someone* for using genetically-engineered pot seeds.  Can they sue individuals with a single plant in their windowsill?  *(answer: yes)* Will Oprah step in and help that beleaguered individual?  *(answer: we'll see!)*

I'm not an expert, and in fact I've gone to extra-special effort to avoid all possibility of being accused of having researched this subject.  I know NOTHING about it.
But the questions, they're bugging me.  How the hell do we implement all this?  Sure, it's "legal" in Amsterdam, or so they say.  I've never been there, and I suspect their laws are way too vague for the overly-litigious United States of America.
I hope it's obvious that we can't say "it's just like tobacco" (it's not) or "it's just like alcohol" (it's not), or (God help us) "it's just like doing alcohol and tobacco together, so take the intersection of their laws".
Marijuana, whether you like the idea of legalizing it or not, is a
*project*
.  It requires an
*implementation*
, and the implementation is a lot like that of a software project.  The US federal government is analogous to "The Company", and the states are analogous to "The Teams" that comprise the company.  Some of them have free time; some do not.  Some of them agree with the overall goal; some do not.  And every single miniscule little detail has to be worked out, and written up, and voted on, and approved, and then specified, and implemented, and enforced.
And there will be bugs.  And loopholes.  And unexpected interactions.  The best-laid plans will go awry.
People will die.  It's a certainty.  Some people are going to die as a direct consequence of legalization of marijuana.  I don't like it, and you don't like it, and most of us would probably argue that it shouldn't hold up legislation or legalization indefinitely... but we have to take it into account.  Because if it's YOU who dies, smashed to death on the iceberg by your skunkweed-stoned ship captain, you're going to be REALLY pissed off.  I guarantee it.
Shit is NOT easy.  Remember that.  Shit is NOT easy.  If you think it's easy, then you are being naïve.  You are being a future VP.  Don't be that way.
Try to think about how you would implement it.  Yourself.  If your boss came to you and said: "Make it happen.  Yesterday."  Have you ever legalized marijuana?
I haven't.  But I wouldn't want to be the people who decide how to legalize it.  Their asses are majorly on the line.  Even more than ours were at Amazon.
My advice: give it some time.  Hell, give _Obama_ some time.  Whether you still like him or not, he's not a frigging King, he's a President.  He can't make stuff happen overnight by waving his magical sceptre.  He just can't.  I don't know what you were thinking, but "overnight" is a pipe dream, and "a few months" is
*definitely*
"overnight", in presidential terms.
Moral of the story: Shit is
*not*
easy.  Stuff takes time.  Months.  Years.  Decades.  It's OK!  You'll still be here.  Count your calories. Exercise.  And you'll still be here to see it all happen.
Patience.  It's a wonderful thing.  I can't wait!