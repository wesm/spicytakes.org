---
title: "How dbt succeeds"
subtitle: "Peacetime dbt, wartime dbt, and an alternative third thing."
date: 2023-04-14T16:46:10+00:00
url: https://benn.substack.com/p/how-dbt-succeeds
slug: how-dbt-succeeds
word_count: 2701
---


![](https://substackcdn.com/image/fetch/$s_!QsNL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ecad335-a8ba-4e04-9a77-8eb677c87e2d_960x430.png)

*Wartime dbt comin’.*


Of all the characters I’ve met in Silicon Valley’s data scene, one person will always have my undying loyalty:Peter Fishman.


Fish ran the data team at Yammer, and was my first boss in the tech industry. He was uninterested in glittery technology, didn’t care about the corporate charade, and, despite always being the smartest person in the room, was never once taken by self-aggrandizing puffery. Instead, he led via adage, analogy, and a relentless push to do practical things. Like a great basketball coach,1he gave us a philosophy to follow—which came to be known, colloquially at first and eventually as a published document, as the Fishman Playbook—and a license to freestyle once we were on the court. Working with Fish was like working with Norm McDonald: A subtle master of his craft who took you up long climbs and down short descentsthat were always worth the wait.


But my loyalty to Fish runs deeper than owing him credit for a bunch of stolen ideas; I owe him credit for the entirety of my career. In early 2012, I was stuck in a dead-end job as junior researcher at a think tank in Washington, D.C. I was six months and 58 applications into looking for a new job, and had yet to land a single offer. On application number 59—which was made possibleby a referral2—I lucked into an interview to work on Fish’s team.


Despite my dubious resume, my unproven skill set (not only did I not know SQL, I didn’t know what it was), and what was surely an alarming series of conversations during my onsite, Fish took a chance on me. He pulled from the path I was on—slumping towards a job as a bitter Hill staffer with no career prospects, destined to take my entitled frustrations out on the American people by gumming up the legislative process with petty acts of bureaucratic sabotage—and bent me towards the life I now have. If you’re a subscriber to this blog, a customer of Mode, or simply an American citizen who’s grateful that there isn’t someone trying, purely out of misanthropic spite, to require that all tax forms get submitted via fax, you too owe a debt to Fish.


Though Fish is singular, everyone has some version of Fish in their lives. We all have the coach who gave us a shot, the school that said yes, or the professor who turned an aimless elective into a lifelong passion. In the long arcing curves of our lives, we remember the sharp upward turns.


Fish put such a turn in my life. For people all over the data industry, dbt Labs put a turn in theirs.


No matter how you feel about dbt Labs, its impact on people's lives is undeniable. dbt, and the analytics engineering profession that followed it, plucked thousands of people out of jobs they didn't like andinto ones they did. It got peoplepaid. It encouraged them tooperate at the top of their license, intheir flow states. It created a communitythat celebrated themfor who they were and what they did.3


Some people may disagree with the corporate benefits of all of this—perhaps dbt isn’t the right architecture; perhaps analytics engineers aren’t operating at the top of their license, but above it, overpaid and out of their depth; perhaps workers are unwise to be loyal to a company that’s legally obligated to love its shareholders more than its fans. Maybe; time will tell. But to the people who've found better jobs, higher salaries, and a professional home, that’s irrelevant. I'm grateful to have been rescued by Fish, even if the data industry would be better off withoutyet another BI tooland yet another white guy with Ideas and a Blog;4a small army of analytics engineers is rightfully grateful to dbt Labs, even if modern data stack goes bust. Though dbt Labs' success is impressive, this bubbling appreciation from its users is what makes it truly unique.


This isn't to say that dbt Labs’ job has been easy. Nothing about hiring hundreds of people, supporting16,000 customers, and chasing extraordinarily ambitious revenue targets, all while trying to be the careful custodians of a popular community, is easy. Building a company at this pace is amarathon of sprints. That’s really hard, no matter how enthusiastic your cheering section.


Still, for most of their seven-year run, dbt Labs has been running through supportive crowds, over roads that tilts downhill. The coming miles, however, are full of hills and deserted streets. For dbt Labs to win the next stretch of the race, its tactics may need to change.


# An uneasy peace


It's always been a bit of a mystery to me why more companies haven't challenged dbt. Despite solving a widespread problem,occupying strategically important technological territory, and having arelatively thin technical moat, dbt Labs has historically had relatively few direct competitors. The explanation, I'm coming to realize, is obvious: Why bother competing with it? The explosion of interest in data tooling created lots of opportunities in adjacent spaces—observability, discovery, orchestration, semantics, activation, contracts, mesh—that don’t have dominant incumbents. In a world where companies could raise money on narrow solutions, don't rip at the prom king's coattails. Ride them.


dbt Labs has been a clear beneficiary of this implicit truce. Every data tool wanted to surf on dbt’s success. BI toolslaunchedintegrationswith it; orchestration vendorsranit; metrics layersaugmented it; databasesremarketedit. This didn’t just keep dbt Labs protected from competition; it also made everyone else a tacit reseller of dbt.


Since the market fell apart last year, however, these dynamics are compounding in reverse.


Across the entire economy, data teams are taking a more serious look at how they’re spending money. This puts a lot of pressure on the narrow data tools that happily integrated with dbt: They have inflated valuations, a deflating addressable market, and a ticking clock counting down how long they have to make up the difference. In that context, the budget spent on dbt isn’t a line item to piggyback on; it’s a target—and especially so if startups sense that there arecracks in dbt’s armor. Everyone’s friendsuntil we’re hungry, desperate, and there’sblood in the water.


Though there haven’t been major collisions yet, troops are amassing on the borders. There’s now adbt for the enterprise, and adbt with better developer ergonomics.5There are startups bringing dbt’s design principles to data assets that aren’t in your warehouse.6There are a handful of DAG-based orchestrators that claim to be better at running dbt jobs than dbt Cloud. And just two weeks ago, Looker announced that it was (predictably) spinning out LookML into anindependent semantic layer, putting the final nail in the once-congenital partnership between Looker and dbt.


So what should dbt Labs do? As I see it, they have three options.


## Peacetime dbt


I’veconsistently been skepticalthat dbt would be able to meaningfully monetize open-source data infrastructure technology by selling seats to a SaaS product—and I’ve consistently been proven wrong. By all accounts, dbt Labs is still growing at a remarkable clip on what can no longer be dismissed as a small revenue base. In a time whenSlack communities have become passé, dbt Labs’ continue to grow; in a year when travel budgets are getting ruthlessly gutted, Coalesce, dbt Labs’ conference, has,thus far, kept its character as a must-attendcelebration of the community and its common interests.


In other words, it ain’t broke; don’t try to fix it;as someone other than Gandhi once said, people fighting you is the penultimate step to you winning.


Still, even if these trends hold, I’m not sure that dbt Labs can keep walking the exact same path it’s on. Thus far, I think dbt owes a lot of its success to being unapologetically human. Rather than trying to design some perfect semantic abstraction, it built data models by and for people—they’re written in simple SQL, and create simple tables. There’s no complex configuration language, novirtualized OLAP cube, no nested or abstract data structure.


I’m increasingly becoming convinced that the entire modern data stack is on the cusp of getting rebuiltfor our AI overlords. If that happens, data models won’t get built for people,but for LLMs. LLMs, however, probably won’t write pure SQL, which is riddled with complexity; instead, I’d expect them to run through semantic models like LookML. People ask the LLM a question; it creates a “semantic query;” a semantic layer complies that request into a SQL query.


This structure would favor a semantic layer likeMalloy—tricky to understand, unnatural to query, but extremely flexible—over one built on top of human-readable tables. Fortunately for dbt Labs,Transformgives them a path to building a similar product. So who knows, maybe Transform is dbt Labs’ Instagram: A sensible pairing today, and a tactical stroke of genius tomorrow.


## Wartime dbt


If Transform turns out to be a brilliant bet, it won’t be dbt Labs’ first such move. Say what you will about the nascent dbt Semantic Layer, but its rollout was one of the shrewdest moves in the data industry in the last decade.7


Just as interest in universal semantic layers (akametrics layersakaheadless BI) was starting to heat up—five companieshad recently entered the space, with at least a couple more in stealth—dbt Labsannounced their plansto build a competing product. In doing so, they froze the market. Data teams, many of whom were already using dbt and liked it, decided that it didn’t make sense to bring on an independent metrics store if dbt would be offering one soon. Other startups couldn’t compete with dbt’s offering, because there was no concrete offering to compete against. And venture capitalists, concerned about dbt steamrolling the market, soured on the whole scene. This cleared the road for dbt—today, only one of the five companies is still working on the same product. If semantic layers end up being prized real estate—and especially if Transform keeps dbt relevant in our AI-overrun future8—put this in a business school case study.


dbt Labs could run this play again, in every adjacency. Plant a flag in the orchestration space, in data discovery, in observability, in contracts, in the mesh, and try to annex them all. Buy Dagster.9Subsume Malloy. Buy Preql to give business users a means for creating their own metrics in dbt.10Take on the entire transformation layer; bury every drag-and-drop orchestration tool with a visual designer embedded in dbt Cloud. Go to the mat with Informatica, andits $1.5billionbook of business. Just as Snowflakedeclared waron everyone who wants to store and process data, dbt Labs could do the same to every company that wants to prepare and transform data.


To be sure, they don’t need to do all of this at once,head down and guns blazing. But as their entry into the semantic layer illustrates, there are gambits here that, if played right, could keep dbt Labs firmly balanced on two feet, and put everyone else on their heels.


## Take the money and (dbt) run


dbt Labs’ third option is avoid the question entirely, and sell the company.


This isn’t exactly a novel suggestion. The possibility of one of the big database vendors buying dbt Labs getsfloated periodically. It’s sensible enough: Databases benefit from transformation tools; buying one as popular as dbt would let them siphon more workloads into their platform.


It’s also not surprising that a deal hasn’t gotten done. dbt Labs is currently valued at a premium not because of its technology, but because of its loyal community following and the future revenues that VCs assume that community can generate. For prominent vendors like Snowflake or GCP that already have relationships in every corner of the data industry, that community probably isn’t a monetizable asset. Rather than spending billions to own dbt Labs, they’re likely better off spending a few million dollars to be a supportive partner. And if they ultimately decide they want to offer their own native transformation layer, there aremuch cheaper options out there.


For dbt Labs, the math is inverted. So long as the trajectories of the product and community are healthy, stay the course, and work with everyone. It’s a gamble, though: If the plan is to IPO, dbt has to convert its community into cashflow at some point. Wall Street doesn't care about how much goodwill dbt Labs has; it doesn’t care about Slack members, or Github stars, or meetups hosted. It cares about how much cash dbt Labs can crank out.


Which brings me to Databricks.


As best I can tell, Databricks is running a clear second to Snowflake in the war to replace Oracle as the leader (not named Microsoft) in the enterprise database market. My naive guess is that Databricks’ problem is its branding—it’s historically been seen as anoverly-complicated data science platform, and not a meat-and-potatoes cloud data warehouse. To overtake Snowflake, it doesn’t need technology; it needs mindshare. It needs sales opportunities. It needs to feel like a safe default.


Nobody has the mindshare of dbt Labs. In dbt Labs, Databricks would be buying tens of thousands of warm introductions to prospects that may otherwise never give them a look. They’d also be buying legions of enthusiastic users who are, I suspect, more loyal to dbt than they are their warehouse.


For dbt Labs, Databricks offers a few things in return. First and foremost, Databricks would value dbt Labsfor what it is today. There’s a long road ahead for dbt Labs to extract revenue from its community; unlike other buyers, Databricks would likely want that community, and not just what it might become.


Second, Databricks solves the riddle of dbt Labs’ business model. Databricks can offer dbt as a free, unmetered service. It wouldn’t care if you use the open-source version or dbt Cloud, nor would it worry about how many seat licenses you buy. This frees up dbt Labs to focus on what it does best—driving adoption of dbt’s core services.


Finally, if the future of data runs through semantic LLMs, Databricks and dbt Labs arebetter positionedthan anyone to own that revolution. Done right, merging the two products doesn’t just derisk dbt Labs and put Databricks on the database map; it puts the two companies on a map of their own, in the middle ofone the biggest revolutions in technology in decades.


---


I have no idea which path is dbt Labs’ best bet—such is the luxury of being a talking head on the sidelines. But to admit my biases, I hope that they continue to succeed, just as I hope that Fish continues to succeed. However right or wrong their philosophies may be, both have transformed a lot of lives for the better. And that’s a thing worth rooting for.

[1](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-1-114804500)

Like, say, Dean Smith or Roy Williams.

[2](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-2-114804500)

By, it turns out, San Francisco’s most lynch-curious resident.

[3](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-3-114804500)

Of course, the community around dbt Labsisn’t perfect; nothing of its size is. But there are much darker paths it could’ve gone down. To paraphrase Winston Churchill, the data community is the worst collection of people in the tech industry, except for all the others.

[4](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-4-114804500)

Just wait until Istart a Podcast.

[5](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-5-114804500)

They aren’t marketed exactly as this, but the implications seem clear.

[6](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-6-114804500)

I.e.,dbt-excel, but for real.

[7](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-7-114804500)

I should also say I have no idea if this was intentional or not.

[8](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-8-114804500)

Funnily enough, dbt Labs’ acquisition of Transform alsofroze the market. Though the initial reviews of dbt Labs’ semantic layerwere tepid, Transform injects new promise into the product. For customers, the choice today is the same as it was a year ago: Wait for an upcoming release from a trusted vendor, or invest in a new product that may be redundant and inferior in a few months or quarters?

[9](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-9-114804500)

I’m a personal investor in Dagster, and am obviously rooting for this outcome because if dbt Labs buys Dagster for a cool one billion dollars, I will make just enough money to be able to buya brand new Mazda 3. Start a company to start a blog to invest in a company to engineer an acquisition to buy a mid-tier sedan without spending a dime?That’sorchestration, baby.

[10](https://benn.substack.com/p/how-dbt-succeeds#footnote-anchor-10-114804500)

I’m also a personal investor in Preql, though I haven’t yet made any plans for those winnings. Upgrade my Mazda 3 to a 2.5 Turbo Premium Plus, I guess.
