---
title: "What do we do when we get it wrong?"
subtitle: "This is not a rhetorical question."
date: 2022-08-19T16:57:32+00:00
url: https://benn.substack.com/p/when-we-get-it-wrong
slug: when-we-get-it-wrong
word_count: 2110
---


![](https://substackcdn.com/image/fetch/$s_!PKh7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5707141-0353-4da5-8ac1-0aa2ccb7564f_3100x1560.png)

*Sometimes,we miscalculate.*


Every once in a while, to the great displeasure of my coworkers and colleagues, Ihave the opportunityto “get my hands dirty on some real analysis” at Mode. In these brief, perilous moments, I become ananachronistic analyst, an out-to-pasture exec pretending not to be out of practice, a clown in the codebase—a codebase where my legacy is a shoddy foundation that has long since been gutted, corrected or replaced.I try to show off my arm; everyone else waits for me to leave.


To nobody’s surprise but my own, I sometimes get things wrong. I accidentally fan out a join in a product usage model;1I fail to consider some nuance in a query that computes our average revenue per user;2I botch the logic behind our user retention rate.3In some cases, these errors get caught immediately and never make it beyond the safe confines of our data team’s review process. In other cases, my mistakes, shrouded in a six hundred line Rube Goldberg machine ofunconventionally formatted SQL, slip through.4They make their way into production—in dashboards, in board decks, inpeople’s heads—and silently compound until, months later, some unwitting data scientist, hiking through an adjacent query, finds a dead body.


As an industry, we spend a lot of time talking about how technology can protect analysts from these mistakes. Wecreateproducts5to detect them; we writecontracts in our APIsto prevent them; webuild processesthat correct them; wedebate architecturesthat make them harder to introduce. This all seems generally good; if data is as messy and error-prone as every cynical analyst and data observability pitch deck says it is, we need to take a lot of precautions.


But there’s a weird paradox to this dialogue. For as much as we talk about how to avoid getting things wrong—which is an implicit acknowledgement that we get things wrong a lot—we spend hardly any time talking about what happens when we do.


# Some shift in the numbers


In early February of this year, sometime in between my unwelcome joy rides through our dbt project and Mode report library, I logged into Substack to look at the metrics for this blog. Substack rewarded my vanity with an alarming message: They'd messed up. When calculating the number they use to headline every post’s performance—the number of views—they double counted email opens. The metrics (which I definitely don’t care about and assign no personal meaning to, no, none whatsoever, nothing at all was tied up in those at all, I didn’t even know Substack tracked views tbh) fell off a cliff. Everything was down between twenty and fifty percent.


I have no inside knowledge of what caused the issue, and Substack didn’t say much about itbeyond a few tweetsabout “a bug” that caused“some shift in the numbers.”But having published my fair share of eventually-correct dashboards, I have my guesses: Some events got logged twice, and the query that computed view counts didn’t clean this up. Or an analyst misunderstood the distinction betweenemail_openedandemail_viewedevents, and mistakenly thought that opening an email implied it was viewed. Or a query just had a typo or a bit of faulty logic or a bad join onto a table that seemed like it’d have one row per email but actually has two, and view counts got doubled. Such are the occupational hazards of being an analyst. Do the job log enough, and we allbreak something6—and somehow, the numbers are never revised up.7


For all of the various guides, training materials, and SEO-bait that our industry produces, I’ve never seen a single conversation8about what we’re supposed to do when—when, not if—something like this happens.


Perhaps that’s because there’s a seemingly common sense, ethical answer: Tell people about the issue, disclose what happened, and update charts and figures with the right values. And we can, as we are often inclined to do, borrow from engineering teams: Hold ablameless retro, write anafter-action review, and move on. No deeper discussion is required.


Maybe. But if nothing else, I think it’s worth asking if the ostensibly “right” answer is actually so right after all. Plus, there are enough differences between engineering incidents and data errors that we should question if that’s the right discipline to draw our lessons from.


# Analytics != Ethics


Suppose that you shipped some worrying—but not egregious!—error that miscalculates a metric of moderate importance. Say, for instance, that the list of leads you send out to your sales team every week ranks leads incorrectly, and the best prospects aren’t always at the top of the list. Nobody notices, and you find the mistake before anyone else catches it. Putting aside what youdo—and your conscience, and any inherent value in being transparent9—if you couldmanifesta reality, what would it be?


Ideally, Ithinkyou’d want the issue to be fixed, and nobody to know it was ever wrong. Despite its sheen of scientific rigor, data is aconfidence game; the only currency we have is trust. Issuing a correction, then, undercuts that trust, with little benefit. People start questioning if any data is reliable, and sales reps start giving your lead scores the side-eye. It’s possible the correction shows people that you’re making efforts to find and fix issues—but more likely, I suspect, it just makes people aware that there are potential issues for them to be worried about.


The counterpoint to this is that mistakes don’t happen in a vacuum. While the lead scoring bug might escape notice, some other problem won’t. A data team that silently fixes the errors they find, but publicly fixes the errors that other people find, might make everyone believe that they only test in production. In this context, a few showy corrections could bolster people’s trust in the data they see.


That, I think, could point to an odd solution: Issue corrections, but less frequently than you make them. Analytics is an imprecise art, often built on top of a shaky foundation of fickle and unreliable data. Data teams can only be effective if people trust that artmore than they probably should. Cynically, strategically timed corrections could be a confidence trick that makes analytics just gritty enough to be real, but not appear so flimsy as to be worthless.


# Analytics != Engineering


The other deeply complicating factor about analytical bugs is that they’re not at all the same as software bugs. It’s tempting to draw the comparison—we look to software engineering for so many other things, and development teams have spent decades perfecting how to fix stuff. The parallels, however, are mostly superficial.


Engineering bugs and outages tend to be point-in-time issues. They cause visible, obvious problems when they happen. In some cases, those mistakes can have lasting ramifications—peoplemiss flights, you have to buy anew server cage—but most run-of-the-mill bugs have very brief echoes. When things are broken, we’re upset; when things are working, we're happy.


Analytical bugs, from bad data to miscalculated metrics to unsound analysis, are different. They stick. Strategic decisions get made on them. History is defined by them. Investments have been made;jobs have been quit;newsrooms have been restructured;far-reaching policies have been enacted. And more gently, minds have been made up, and beliefs have become entrenched.10


Moreover, the “users” affected by incorrect metrics—execs building their annual plans, writers taking a full-time flier on Substack, editors firing reporters for videographers, politicians passing austerity bills, and sales reps calling the wrong prospects—may never know that something was wrong. A busted feature is easy to spot, whereas good data looks the same as bad data.


This is what makes analytical corrections so hard. Our data isfull of errors, nobody knows it, and any one of those errors could—likely won’t, but could—lead to an irreversible mistake. How do you fightthatenemy?


# “We have 100 customers, give or take”


Honestly, I don’t know—the title of this post isn’t a rhetorical question. At best, I have two half-baked and off-the-wall guesses.


First, rather than leaning into engineering philosophies—iterate, move fast and break things, adopt a blameless mindset—we should take more cuesfrom journalists. Both analysts and journalists put forward projections of the world, and both professions are only as good as the trust people have in those projections. Moreover, while bad reporting can be corrected, it can’t easily be undone. Once a story is out there, it can take on a life of its own.


In that context, a blameless, iterative culture actually seems dangerous. With journalists’ power comes responsibility, and personal accountability to mistakes. If data teams want the same kind of influence, to be in the room where decisions get made, and to “be heard and have an impact,” we probably have to bear the burden of our mistakes.


Second, we should think about ways to protect ourselves from having to make corrections. Someday, we’ll have an AI-powered, DALL-E-backed, real time anomaly detection and data extrapolation system that corrects bad data, replaces missing data, and draws fun pictures of charts in Gartner decks that recommend you restructure your management hierarchy in the style of Picasso’s blue period. Until then, though, we could try something easier: Rounding.


A long time ago,Sean Taylortold me about a brilliantly simple solution he came up with to communicate uncertainty in numbers: Round them, so that people know they aren’t exact. For example, rather than saying that the Braves had an8.4 percent chanceof winning the World Series last year, which implies a figure that is both precise and accurate,11just say 10 percent. The difference is meaningless, and shows people that they should take the figure as an educated guess.


Weird as it seems, we could do the same for other metrics, including those we can precisely count, but are uncertain that we can count exactly right.


For example, in another recent correction, Substack made a minor adjustment to how they measure historical traffic. It was the sort ofsmall, fiddling changethat doesn’t materially affect anything, other than my confidence in the numbers. If Substack presented all of their data as rounded numbers—daily counts to the nearest ten or hundred—the adjustment would’ve had less of an impact, both because fewer things would change, and because I would’ve already assumed the counts were estimates.


And that, I think, gets at the root of the challenge: No matter how vetted our queries and precise our math, most things that we produce as data teamsareestimates. They may look irrefutable and exact—between 1 am EST on August 15, 2022 and 1 am EST on August 16, 2022, we had exactly 6,373,118 active users—but they’re not. Some logs could’ve been dropped; the definition of an active user could change; the calculation could exclude some type of activity, like opening an email, that other people argue makes a user active; some cavalier exec could’ve butchered the entire thing. Everything is a bit of a guess, and sometimes, we’re going to get the guesses wrong. The more pertinent question is what we do aboutthat.

[1](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-1-69403898)

“Benn, this dashboard says that you wrote nine hundred thousand queries yesterday. Does that sound right to you?”

[2](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-2-69403898)

“Benn, do you think if we lost four million dollars per user per month, would we still be in business?”

[3](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-3-69403898)

“Benn, I asked you for our new user retention rate by segment, and you gave me apie chartwhere one of the values just says six thousand dollars.”

[4](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-4-69403898)

If you can’t beat a code review, wear it down.

[5](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-5-69403898)

I’m apersonal investorin Bigeye.

[6](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-6-69403898)

Ah yes, anOsha recordableinjury, the kind we actually want to avoid. “Well, last week, Steve got gored by a forklift, but it happened when he was on break, so technically speaking, he wasn’t working and we aren’t legally required to report anything.”

[7](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-7-69403898)

This is a bit weird, actually. Anecdotally speaking, it seems like most corrections make things worse, not better. I have no idea why that is. Maybe overcounting is easier than undercounting, because our default is to count everything, not filter out everything? Because we can spot-check against real customers, but can’t prove the negative that not real customers aren’t included? Because when we do undercount something, we don’t notice it because missing data is, well, missing? I don’t know, but the universe seems aligned against us.

[8](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-8-69403898)

Admittedly,I don’t read.

[9](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-9-69403898)

To be clear, I’m not saying we shouldn’t value these things, or that we shouldn’t be ethical. I’m simply asking what we’d want if put those values aside, for the point of seeing if we can get to that thing while still acting in an ethical way.

[10](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-10-69403898)

Is fat bad for you? If you, like me, grew up in the nineties, you probably can never fully rid yourself of some embedded sense that,no matter how much you got conned, fat has to bekindaunhealthy.

[11](https://benn.substack.com/p/when-we-get-it-wrong#footnote-anchor-11-69403898)

Andoff by 91.6 percent
