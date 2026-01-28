---
title: "Decentralized funding? An analysis of three programs"
date: 2018-08-15
url: https://nadia.xyz/grant-programs
word_count: 4476
---


# Decentralized funding? An analysis of three programs


August 15, 2018


As more open source projects attract funding, an important follow-up question becomes: “How should they spend it?”


While it might seem silly at first that projects raise money and don’t know how to spend it, the problem is more complicated than it seems. What a project spends money on depends on how much of it they have. A $1,000 budget enables very different funding decisions from a $100,000 or $1M budget, not to mention whether it’s recurring or not.


There are also complex questions that come with raising and spending money in a decentralized organization. Which contributors should get paid? Is it based on need, or who did the most work? What if one contributor lives in an expensive city, and another in a small town: should they get paid the same amount? Should funding even go towards labor, or should it only pay for overhead? As example of this tension, Evan You funded his own work on Patreon for a long time before [creating a separate funding mechanism](https://medium.com/the-vue-point/vue-is-now-on-opencollective-1ef89ca1334b) for Vue.js.


All this leads to a chicken-and-egg problem, where funders want to know how their money will be spent before they commit, and projects struggle to respond, because the answer depends on so many variables.


So let’s pretend there’s a magical alternate universe where money flows freely in an open source project. What would those projects spend it on? How would they decide how to allocate funding? And what becomes possible when money’s available?


Luckily, a few examples already exist, so we don’t have to pretend. I decided to dig into some of these programs to understand who funds them, how they allocate funding, and what we can learn about how money is organized and spent.


# Methodology & data


I put a lot of thought into choosing the right set of programs to study. [1] I was explicitly interested in looking at community grant programs, because they offer a path to decentralized work that isn’t “get hired by a company” or “start a business”. Among my criteria:

- **Well-capitalized:** The goal is to understand how projects spend money if they have enough of it
- **Demonstrable impact:** Have been around for a few cycles and successfully distributed money to contributors
- **Upstream-centric:** Money is designated for work that benefits the *core* project (this excludes R&D and incubator programs), and anybody can apply for funding
- **Public proposal tracker**, so I can explore the data


Based on these criteria, I chose the following three programs:

- [Dash Budget Vote Proposal Tracker](https://dashvotetracker.com/)
- [Monero Funding Forum System](https://forum.getmonero.org/)
- [Zcash Foundation Grants](https://github.com/ZcashFoundation/GrantProposals-2018Q2)


I picked these for their varied scope and robustness. [Dash](https://github.com/dashpay) has a semi-autonomous program with a huge budget ($1M+ monthly), [Monero](https://github.com/monero-project) has a crowdfunded community approach, and [Zcash](https://github.com/Zcash) has a more centralized, yet public process, funded by their foundation. Because I’m interested in the structural tradeoffs of different program designs, I figured this would be a good group to compare and contrast.


After selecting these programs, I went through all of their proposals, collecting information and coding each proposal into a category. You can view the data I used, with caveats and methodology, [in this repo](https://github.com/nayafia/proposals-analysis).


After reading the proposals, I spent time on each program’s website and associated forums to try to understand their structure and application process. I decided not to interview anyone about it, because I wanted to understand the programs as well as any random contributor would. If there are any inaccuracies in how I’ve depicted these, I’d *love* to hear it - just drop me a line, and I’ll correct or add context as needed.


# Program structure and design


I’ll start with observations about how the programs are structured, since that helps contextualize what’s getting funded.


For each program, I evaluated their structure across a few key elements: **funding source**, **application process**, **decision process**, and **accountability**.


## Zcash Foundation Grants


The [Zcash Foundation grant program](https://github.com/ZcashFoundation/GrantProposals-2018Q2/) most closely resembles a traditional grant process, funding things like software development, infrastructure, maintenance, education, and research. They’re explicitly not interested in funding monetizable ideas (ex. businesses built on Zcash). Grants are expected to fall into 1-6 person-months of effort, with all output being open source.


> The Zcash Foundation is a non-profit organization, and is therefore especially interested in funding proposals that are public goods and not obviously monetizable. [Zcash Foundation Grants: Call for Proposals](https://github.com/ZcashFoundation/GrantProposals-2018Q2/)


Anybody can apply for funding by filing a pre-proposal in their GitHub public proposal tracker. After the proposal is opened, public discussion ensues, which anybody can comment on. All communication happens publicly, so anyone can see the status of an application at any given time.


After a predetermined period of time, the review committee informs pre-proposal applicants whether their application is a leading candidate. While their decision is non-binding, it’s meant to help applicants understand whether to spend additional time writing a full proposal.


After full proposals are submitted, final decisions are made. Grant recipients must submit monthly progress reports, as well as a longer report six months after funding.


Compared to Monero and Dash’s programs, this is a newer program. Two rounds have taken place thus far (2017Q4 and 2018Q2; final decisions have not been made in the latter round). The program had a 2017Q4 budget of $80,000, funded by the Zcash Foundation, which they increased to $250,000 in 2018Q2, funded by the Zcash Foundation and the Blockchain Institute.


(Edit: the foundation itself is [funded by Zcash’s “founder reward”](https://blog.z.cash/announcing-the-zcash-foundation/): a small portion of Zcash’s block reward that is distributed over 4 years to founders, employees, investors, and the foundation, among other things. At today’s prices, the value of the foundation’s total 273,000 ZEC allocation would be $40M. [2])


Decisions are made by a grant review committee of 5-6 community members, appointed by the Zcash Foundation Board. The committee includes reviewers who are not employed by Zcash or the Zcash Foundation (whether by design, I’m not sure). Final committee funding decisions must be approved by the Zcash Foundation board.


## Monero Forum Funding System (FFS)


Monero’s [Forum Funding System (FFS)](https://forum.getmonero.org/) was by far the most difficult program to understand from an outsider’s perspective, with little public documentation around its process. I expect some of these details are outdated or incorrect. The lack of documentation came up in several forum threads, so I think they’re aware of this issue; it just made it harder for me to understand.


Compared to Zcash, Monero uses a more decentralized process, with no official earmarked budget, and proposals funded via crowdfunding.


Like the other programs, all proposals are [tracked publicly](https://forum.getmonero.org/). Unlike the other programs, Monero explicitly decouples the value of a proposal from who completes the work. From what I can tell, their goal is to make paid work more resilient. If someone disappears, another person could theoretically pick up the proposal from where they left off.


> The person pitching the idea shouldn’t be the one putting it in funding required, because how do they know how much it will cost? It’s NOT a bounty, it’s funding a specific thing. – fluffypony, [“Community Ideas not Making into the Funding Areas of Website”](https://forum.getmonero.org/6/ideas/324/community-ideas-not-making-into-the-funding-areas-of-website)


Anybody can propose an idea in the “Ideas” section, and the community is encouraged to discuss whether that idea would be valuable to work on. Ideas that are successfully vetted move to the next stage, “Open Tasks”, where anybody who’s interested in working on that idea can pitch themselves as the right person for the job (sort of like a job opening). After a team is assigned to the proposal, it moves into the “Funding Required” stage, to raise funds for work. Like Kickstarter, this process is entirely crowdfunded: anybody can donate Monero towards these projects.


(Edit: Monero’s samsunggalaxyplayer also shared that *“Monero FFS proposals are typically discussed on #monero-community during the biweekly community meetings to establish rough consensus.”* [3])


After a proposal is funded, it moves to the “Work in Progress” stage. Funds are held in escrow and disbursed to the recipient as specific milestones are met. Grantees are expected to provide regular progress reports at this stage. Finally, after everything has been funded, and work has been completed, the proposal is archived in the “Completed Tasks” section.


## Dash Budget Vote Proposal Tracker


Dash’s [Budget Vote Proposal Tracker](https://dashvotetracker.com/) is the most robust of the three programs, with a clearly-defined monthly budget paid out directly from its blockchain.


10% of Dash’s block rewards are earmarked for this program, decreasing by ~7% roughly every year. (The budget is large: this month, it’s 6176.72 Dash, which comes out to ~$1.28M USD at today’s exchange rate.) Any money that’s not allocated that month is “burned” (not created) to reduce inflation.


Like the other programs, anybody can create a proposal, but they’re incentivized to go through the pre-proposal process first: a formal proposal costs 5 Dash to open (~$1000 USD at today’s rate, destroyed upon receipt). The fee is meant to discourage spam; many proposals include fee reimbursement as part of their budget.


Only “masternodes” can vote on Dash proposals. Masternodes are individuals who host “full” wallets in exchange for money, which have more functionality than a “regular” wallet, and require locking 1000 Dash (~$200K USD) in their wallet. In other words, they’re people with a significant stake in Dash’s future. At the time of this writing, there are 4,788 masternodes.


Reputation plays a big role in who gets funded (for an example, see the quote and its thread below). Applicants are encouraged to build a relationship with the community, demonstrate that they’re the right person for the job, and drum up support for their proposal in the [pre-proposal forum](https://www.dash.org/forum/topic/pre-budget-proposal-discussions.93/).


> You are unknown to the community. So it’s a good idea to start with a proposal with a lower amount (e.g. 100 DASH) and proof the value you delivered to the DASH project. I suppose the community will be glad to fund a larger project, if the small one was successful. – rango, [Proposal “Share with Millions”](https://www.dashcentral.org/p/Share-with-Millions)


Proposals receive funding if “Net Votes” (total Yes minus total No votes) exceeds 10% of all active masternodes. Because proposals are competing for a finite monthly budget, it’s possible for a proposal to meet the vote criteria but not be funded, if not enough funding is available. Funding is prioritized based on higher net votes and the amount requested. However, winning-but-not-funded proposals can remain active for another monthly cycle, and may be funded then.


While there are no formal accountability requirements, [Dash Watch](https://www.dashwatch.org/) (funded by the proposal process!) was created to provide more insight and monitoring into funded proposals. Accountability is closely tied to reputation; some proposals don’t get funded because of the person’s reputation and/or previous ability to deliver.


# Analysis: Program structure


After going through each program in detail, I made some observations about design tradeoffs and considerations.


## Application process


All three programs have a public application process, which I didn’t see anyone complain about. A public process means more people can help signal, filter, and up/downvote the right applications. A potential downside might be that signaling could misfire and discourage otherwise-good proposals. But the upside is that others can quickly vote down bad proposals and save everyone time (ex. if the applicant has a poor reputation or the idea has already been implemented). In the case of Zcash, because decisions are made by a small committee, a public process makes it harder to levy accusations of collusion or favoritism.


Every program also used a pre-proposal process, which serves as a gentle gating mechanism, striking a balance between being completely open vs. reducing noise. Pre-proposals also shift more work to the applicant up front, which helps distinguish between serious ideas and “nice-to-have” feature requests.


Public documentation is important to help community members understand how to apply for funding. Dash and Zcash were particularly well-documented. Although there’s no way to determine this, I wonder whether the lack of clear documentation in Monero FFS affects the type or volume of proposals they receive.


Finally, reputation is a useful signaling mechanism. I’ll explore this more in the next section, but core teams and repeat winners seem to attract a large portion of funding. For this reason, Monero’s process struck me as somewhat inefficient. *Who* works on a project seems just as important as the idea itself; if there isn’t a good team to work on an idea, is the idea really worth debating? Keeping team and idea together could help reduce noise and make it easier to find serious proposals.


## Funding source


Each program has a very different funding source. Monero doesn’t have a dedicated budget, Zcash gets a budget from their foundation, and Dash has a budget whose size is written immutably into its blockchain.


The upside of using a crowdfunded process like Monero’s is that, in theory at least, only “worthy” ideas get funded. While Dash doesn’t require spending its entire monthly budget, I’m guessing that having a dedicated budget leads to superfluous ideas being proposed and funded, simply because the money is available. (It may also be why Dash funds an extraordinary number of marketing and event sponsorships.) If you have the money, you’ll find ways to spend it, even if it’s not really necessary. On the other hand, this might be a sign that Dash should just have a smaller budget (which does fluctuate based on Dash’s fiat value), not that dedicated funding itself is bad.


The downside of using a crowdfunded process is that without a dedicated budget to work from, it’s harder to plan ahead. It’s also not as future-proof. If Dash declines in popularity, the size of the budget will decrease as the currency is devalued, but at least they will always have a budget. If Monero declines in popularity, who will fund future proposals? This seems to take us right into the same funding problem as many open source projects.


Zcash offers a middle path, with dedicated funding from a well-capitalized foundation, but whether that funding is available also depends on a centralized authority (the foundation) rather than the Zcash community. Ideally, a foundation serves the community’s interests, but it doesn’t always; this can lead to the same governance problems we see in traditional funding structures today.


## Decision process


Who decides what gets funded ranges from a hand-picked committee (Zcash) to major stakeholders (Dash) to anybody who holds currency (Monero). I’m not sure what the right answer is here, but it seems important that funding decisions are made by community stakeholders, however that’s defined.


Personally, I was most intrigued by Dash’s system, because it seemed to balance community stakeholders with incentives to participate. Committees by appointment can be dangerous, because the community must rely on someone else’s judgment of character. But not having a clear electorate at all, like Monero, can suffer from the same bias, because how do you know that what got funded actually represents the interests of the community? Leaving it *too* open can turn funding into a popularity contest.


On the other hand, it’s not clear (to me, anyway) who the masternodes really are. I like that becoming a masternode seems to be a clear and objective process (contingent upon being able to front the capital). But it seems possible that masternodes could easily collude to control the entire budget process, and that some commenters could be higher-signal than others, skewing the vote. Also, while masternodes are probably more incentivized than others to vote on the budget, voter turnout, at ~18% of masternodes, is still pretty low. [4]


Finally, [I’m skeptical that any voting process](https://nadia.xyz/voting) scales well. Dash addresses the scalability problem via [contractor organizations](https://docs.dash.org/en/latest/governance/understanding.html#scaling-and-future-uses) that distribute funds to smaller projects, but that seems to lead us right into the faction problem that plagues democracy today.


In Monero’s case, the voting population is self-defining: whomever cares enough to pay attention to FFS, and has Monero to donate, can participate in the process. However, I saw several comments from people saying that FFS isn’t very active. I wonder if that’s a design flaw of an open funding system: in order to truly be “community approved”, the community needs regularly monitor the forum, which I doubt most people do.


Again, Zcash offers a middle path, with tradeoffs around centralization (see discussion in previous section), but proposals that are public and can be commented on by anyone. The upside of a committee is there is a dedicated group of people reviewing proposals, who also have experience in figuring out which proposals should get funded. However, committees can also attract questions around whether funding decisions represent the interests of the community.


Maybe there isn’t a perfect decision making process, but it’s worth being explicit about the tradeoffs, namely:

- Who should participate in the decision process?
- Whose views are represented by the decision makers (not necessarily the same as “who decides”)?
- How to incentivize decision makers to regularly participate?
- How to prevent or at least reduce the chances of collusion?


## Accountability


Accountability helps community members understand where their money is going and make more informed decisions about funding future ideas and people. Zcash had the most explicit and straightforward process, requiring regular reports from people who receive funding awards. Monero seemed to suffer from a [lack of accountability](https://forum.getmonero.org/6/ideas/86954/forum-funding-system-change-of-policy) that makes it harder for people to know what to fund.


I liked [Dash Watch](https://www.dashwatch.org/) as an example of a more robust accountability initiative, although it requires more community effort to maintain.


There are also implicit accountability mechanisms. Funding based on milestones and reporting seems useful, as it incentivizes recipients to continue to deliver on projects with longer timelines. Projects can be de-funded if the recipient doesn’t deliver.


> I wish I could vote yes, but the track record of your team/organization is abysmal. Until we have full delivery on past proposals (and no, your update is not enough), I have to vote no to protect the interests of our network. – Macrochip, [Proposal Dash-Developer-Workshops](https://www.dashcentral.org/p/dash-developer-workshops)


# Analysis: How funding is allocated


Given the design tradeoffs above, I looked at which types of proposals were funded across programs.


Note: for the most part, I didn’t include Zcash below, because it has fewer total proposals and the final awards for 2018Q2 haven’t yet been made. (So close!) I’ll update the data when those decisions are announced, but the following analysis primarily looks at Monero and Dash.


## What gets funded


It’s immediately obvious that community grant programs are a valuable way to fund core (i.e. maintenance) work. Core work made up ~10% of all Monero proposals, but one-third of all funded proposals. On Dash, core work made up about one-fifth of funded proposals. 100% of Dash core proposals were approved (compared to ~80% of other proposals). [5] The Zcash Foundation doesn’t fund as much core work through its grant program, likely because it has a separate company with full-time employees.


Proposal types differed between funded vs. non-funded proposals. On Monero, non-funded proposals were heavy on application, feature, and community ideas, but funded proposals mostly consisted of core, research, and conference travel.


Dash funds a lot of marketing, making up nearly half of all proposals in their system, which struck me as unusually high. As mentioned earlier, I wonder if this is because they have a dedicated budget that they’re incentivized to spend somehow.


## Who gets funded


Nearly half of Monero’s funded proposals went to just six people: *moneromooo* (core developer), *fluffypony* (core developer), *SarangNoether* (research), *suraeNoether* (research), *samsunggalaxyplayer* (community), and *rehrar* (design, project management).


Over one-third of Dash’s funded proposals went to just three people: *babygiraffe* (representing core), *eduffield* (representing core), and *amanda_b_johnson* (outreach and community).


“Who gets funded” paints a compelling picture of what a decentralized team could look like. Core members are paid to work on the project, but their salaries are contingent on community approval and public accountability. As far as I can tell, nobody from the community was upset about funding their work. On the contrary, commenters were supportive and enthusiastic, providing thoughtful feedback. Amanda_b_johnson, who’s received $100K+ over six proposals for her Dash outreach work, is a great example (see thread quoted below).


> I wouldn’t mind paying half a year upfront to save some work. Also, considering the value of your previous contributions, your personal fee is very modest -almost in the scale of reimbursed voluntary work- compared to some other efforts. Please don’t be embarrassed. – paulkuit, [“Proposal Scaling Up Publicity With Amanda + PMBC”](https://www.dashcentral.org/p/ScalingUpPublicityWithAmandaPMBC)


For both Monero and Dash, nearly every proposal submitted by one of these “regulars” was funded. Proposals are often funded for 3-6 months ([example](https://forum.getmonero.org/8/funding-required/90280/more-mooo-monero-coding-july-september)), which provides more financial stability than a monthly cadence, though not as much as an annual salary. Today, many full-time maintainers are hired by a company to work on the project, but in these cases, a project’s community becomes its board, which seems better from a governance standpoint.


There’s a clear difference in language between funded and non-funded proposals. Proposals in the ideas stage use language like “it’d be great if…”, “can we get…”, “is anyone interested in…” and “I’m not a programmer but…”. These are much like “nice-to-have” feature requests for traditional companies. As expected, non-funded proposals came from a long tail of applicants, with fewer repeat submitters.


By contrast, funded proposals often come from people who can successfully demonstrate prior dedication and commitment to the project, and/or people with useful specialized skills (like security or research, as with SarangNoether/suraeNoether for Monero). This supports my hypothesis that funding is ideally allocated towards regular contributors, maintainers, and people with “known” reputations, rather than random or first-time contributors.


A final observation: in open source, not everything that’s valuable is immediately fundable, but that’s not necessarily a bad thing. A good example of this are translations, many of which were not funded in Monero. Translations are a popular contribution to open source projects, but it might be hard to fund a translation for a less-popular language (ex. Greek vs. Spanish). Ditto to new ideas or features. These are great examples of contributions that don’t or shouldn’t require funding, but instead happen because someone cared enough to make them. In some cases, contributors opened a funding proposal *after* they’d created something valuable (see example quoted below), which offers a possible path to compensation.


> I wish to apply for a grant to continue work on the [Zcash Desktop GUI] wallet and enhance it. I made this wallet because I am excited about Zcash and wish to contribute to its future development. Since this is a hobby to me, having some funding will help a lot. If the wallet is enhanced, it will give users a better UI experience and contribute to the advancement of Zcash! – vaklinov, [Enhancements to the Zcash Desktop GUI Wallet](https://github.com/ZcashFoundation/GrantProposals-2017Q4/issues/7)


## Size of funding


The median size of successful proposals are:

- Monero: XMR106 (USD $6,786, calculated based on historical rates at the time of each proposal)
- Dash: DASH114 (USD $22,088, calculated based on historical rates at the time of each proposal)
- Zcash: $15,000 (this was [a bit fuzzier](https://github.com/nayafia/proposals-analysis/blob/master/zcash/readme_zcash.md) to calculate)


I’m not sure what to make of these amounts. They’re not very large (and some represent multiple months of work), and some core contributors clearly pay themselves below market rate. However, the size of these funds do make the case for larger budgets than what we [currently tend to see](https://opencollective.com/discover). On the other hand, while the projects all seemed to benefit from funding, they don’t require absurd amounts of money to move the needle, either - which I think is a good sign.


# Conclusions


I did this analysis because I wanted to understand: 1) how open source projects spend their money when they have it, and 2) principles for effective program design. In summary:

- The projects studied primarily allocate their funding towards core work, community, marketing, and research
- Reputation matters. Funding goes mostly toward a small group of trusted contributors, and this doesn’t seem to be controversial
- Not all useful contributions require funding, and some benefit from upfront work
- Projects don’t need a ton of funding to make a difference, but they had no trouble spending the money they do have


Some takeaways around program design include:

- Use a public application process for transparency and to leverage community knowledge
- Have a pre-proposal process to reduce noise
- Funding should come from community stakeholders (however that’s defined)
- No clear best practices on who should make funding decisions, but no major contentions yet, either. It’s unclear how well decision processes will hold up as projects scale and decline


Finally, a few caveats. These projects all operate in a similar field, which probably influences what gets funded (ex. research probably doesn’t play as big of a role in other open source projects). Conclusions were drawn based on my observations of just three programs, which don’t necessarily represent open source as a whole.


Suggestion for further analysis: I’m guessing that who and what gets funded changes over time. For example, I seemed to notice (though I didn’t verify) that Dash marketing proposals seemed to decline over time, as community proposals grew. Because Monero and Dash data go back to 2014 and 2015, respectively, it’d be cool to see how a project’s needs change over time. I didn’t do this analysis, but [you’re welcome to!](https://github.com/nayafia/proposals-analysis)


Reading through hundreds of proposals, I felt inspired by the enthusiasm of contributors, as well as the community members who chimed in to support them. I came away feeling more certain that money can unlock so much more opportunity and stability for open source projects. Hopefully this analysis will be useful not just to projects handling money, but also to funders looking for impactful ways to support them.


### Notes

- [Secure Scuttlebutt](https://github.com/ssbc/grants-process/blob/master/grants.md) grants
- Smartcash’s [SmartHive Governance Portal](https://vote.smartcash.cc/)
- [Python Software Foundation](https://www.python.org/psf/grants/) grants
- [Ethereum Community Foundation](https://ecf.network/) grants
- [Stellar Partnership Grant Program](https://www.stellar.org/lumens/stellar-partnership-grant-program)
- Request Network’s [Request Fund](https://blog.request.network/request-network-project-update-january-19th-2018-announcing-a-30-million-request-fund-6a6f87d27d43)
- [Django Fellowship Program](https://www.djangoproject.com/fundraising/#fellowship-program)
- [Bitcoin Development Grant](https://bitcoindevelopmentgrant.com/en/)

1. In case you’re interested, here are some other programs I considered, but didn’t analyze: ↩
2. Thanks to [@selx771](https://twitter.com/selx771/status/1030154757292339201) on Twitter for suggesting this edit. ↩
3. Thanks to samsunggalaxyplayer for [sharing the helpful update](https://twitter.com/JEhrenhofer/status/1030146386652803072) via Twitter. ↩
4. I eyeballed this by taking the total number of votes per proposal, divided by the current number of masternodes today, and averaging those numbers. ↩
5. There are two core proposals that weren’t approved, but these were special proposals to directed any leftover funds to core (instead of burning the money), which were explicitly asked to not be voted over 12% approval. So I count these as approved. ↩


---


*For future updates, subscribe via [newsletter](https://nayafia.substack.com/) or [RSS](https://nadia.xyz/feed.xml). Get in touch via [Twitter](https://twitter.com/nayafia).*

Google tag (gtag.js)