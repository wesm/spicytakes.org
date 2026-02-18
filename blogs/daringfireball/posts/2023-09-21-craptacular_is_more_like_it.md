---
title: "Craptacular Is More Like It"
date: 2023-09-21
url: https://daringfireball.net/2023/09/craptacular_is_more_like_it
slug: craptacular_is_more_like_it
word_count: 2656
---


Aaron Tilley and Yang Jie, reporting for The Wall Street Journal under the not-at-all-clickbait-y headline “[Inside Apple’s Spectacular Failure to Build a Key Part for Its New iPhones](https://www.wsj.com/tech/apple-iphone-modem-chip-failure-6fe33d19)” ([News+ link](https://apple.news/AWKJlHS4MSQW1QmNj7lMUeA)):


> The new iPhone models unveiled last week are missing a proprietary 
> silicon chip that Apple had spent several years and billions of 
> dollars trying to develop in time for the rollout. The 2018 
> marching orders from Apple Chief Executive Tim Cook to design and 
> build a modem chip — a part that connects iPhones to wireless 
> carriers — led to the hiring of thousands of engineers. The goal 
> was to sever Apple’s grudging dependence on Qualcomm, a longtime 
> chip supplier that dominates the modem market.


The above lede sets the stage correctly, and if anything, undersells the contention between Apple and Qualcomm. Qualcomm does dominate the modem chip market, but that might even be putting it too mildly — they’re effectively the only game in town for good 5G cellular modem chips. And Apple’s reliance upon Qualcomm for cellular modems is more than just begrudged — it is despised. Even if Apple and Qualcomm got along, Apple [would have a problem](http://www.asymco.com/2011/01/17/the-cook-doctrine/) with its reliance upon a single company for a core technology. But Apple and Qualcomm do not get along, at all.


But everything that follows the above lede is dubious at best, and in parts, a nonsensical and rather transparent hit piece. It reads like it was fed to Tilley and Jie by Qualcomm, and they bought it hook, line, and sinker — despite obvious glaring problems.


> Apple had planned to have its modem chip ready to use in the new 
> iPhone models. But tests late last year found the chip was too 
> slow and prone to overheating. Its circuit board was so big it 
> would take up half an iPhone, making it unusable.


This simply makes no sense at all. It’s an impossible scenario. It sounds like something from an anonymous troll on Twitter/X, not a report in The Wall Street Journal. But it *was* reported by the Journal, so let’s ponder just how ridiculous this one paragraph is.


First, the timeline just doesn’t add up. We’re supposed to believe not just that Apple was only testing the feasibility of a modem chip for the iPhones 15 “late last year”, but also that the chip “was so big it would take up half an iPhone, making it unusable”. It’s true that a modem chip that “takes up half an iPhone” would be unusable, but so why would such a chip even be *considered* for possible use in this year’s phones? It could be the best-functioning 5G modem in the world — faster performance *and* more efficient — and it simply couldn’t be used if it were that big. It’s not even close. Look at [the teardown from an iPhone 14](https://www.ifixit.com/News/64865/iphone-14-teardown) to see how small Qualcomm’s X65 modem chipsets are.


It’s certainly possible that “late last year” Apple tested a *prototype* for an Apple-designed cellular modem, and that prototype was large, performed slowly, and ran too hot. That’s how component development works: functionality comes first in early large prototypes, miniaturization comes after. You don’t have to be a systems engineer to see how that makes sense. Why waste time on miniaturization for a component that isn’t known to work well enough?1


But there’s no way they were testing such a thing for *this year’s* iPhones. The lead time on hardware is *years* not months. And because Apple needs to produce hundreds of millions of new iPhones each year, the lead time for iPhone hardware designs is longer, not shorter, than most products. Apple not only knows today the cellular modem that will be in next year’s iPhone 16 models, they probably already have decided on the modems, along with just about everything else, for the iPhone 17 two years from now.


> Apple — which hasn’t publicly acknowledged its modem project, 
> much less its shortcomings — is estimated to have paid more than 
> $7.2 billion to Qualcomm last year for the chips.


Apple press release from 2019: “[Apple to Acquire the Majority of Intel’s Smartphone Modem Business](https://www.apple.com/newsroom/2019/07/apple-to-acquire-the-majority-of-intels-smartphone-modem-business/).” I’m not sure how they could acknowledge the project more clearly than that.


Back to the Journal:


> Engineering teams working on Apple’s modem chip have been slowed 
> by technical challenges, poor communication and managers split 
> over the wisdom of trying to design the chips rather than buy 
> them, these people said. Teams were siloed in separate groups 
> across the U.S. and abroad without a global leader. Some managers 
> discouraged the airing of bad news from engineers about delays or 
> setbacks, leading to unrealistic goals and blown deadlines.


Here’s where the Journal’s story starts to smell like a planted narrative from Qualcomm. We can’t know that Qualcomm is behind this, but we do know that Qualcomm threw shade at Apple’s modem efforts with a press release about a renewed deal between the companies [the day before the iPhone announcement event](https://daringfireball.net/linked/2023/09/11/qualcomm-apple-5g). How better to follow that up than a new story painting a picture of technical ineptitude and managerial chaos inside Apple’s modem team, set to appear the day before the iPhones 15 hit customers’ hands? This narrative especially suits Qualcomm if they’re concerned about their own engineering talent defecting.


> “Just because Apple builds the best silicon on the planet, it’s 
> ridiculous to think that they could also build a modem,” said 
> former Apple wireless director Jaydeep Ranade, who left the 
> company in 2018, the year the project began.


The Journal’s first named source is a [former Apple employee](https://www.linkedin.com/in/jaydeepranade/) who admittedly left the company before they even began their own modem project, and his keen insight is that a company that is good at one thing might not be good at an altogether different thing.


> Apple isn’t expected to produce a comparable chip until late 2025, 
> people familiar with the matter said. There could be further 
> delays, these people said, but the company believes it will 
> eventually succeed.


If Apple isn’t expecting to produce a 5G modem chip comparable to Qualcomm’s until “late 2025”, why would they have been testing a chip in 2022 hoping to put it in today’s iPhone 15? A project that is not yet four years old suddenly slipped an additional four years behind schedule? The story refutes itself.


> Apple found that designing a microprocessor, essentially a tiny 
> computer to run software, was easy by comparison. Modem chips, 
> which transmit and receive wireless data, must comply with 
> strict connectivity standards to serve wireless carriers around 
> the world. 
> “These delays indicate Apple didn’t anticipate the complexity of 
> the effort,” said Serge Willenegger, a former longtime Qualcomm 
> executive who left the company in 2018 and doesn’t know the 
> current state of the Apple chip. “Cellular is a monster.”


The second named source is [a retired executive who spent his entire career at Qualcomm](https://www.linkedin.com/in/serge-willenegger-bb06961/), and whose keen insight is to emphasize that the field where Qualcomm is the undisputed industry leader is very difficult.


> Apple’s push to build more of the various semiconductors used in 
> its products stretches back more than a decade. In 2010, the 
> company began using its own processing chips in iPhones and iPads. 
> The chips helped Apple outperform many of its Android rivals, 
> which relied on chips from Qualcomm, Taiwan-based MediaTek and 
> other makers.


Apple silicon outperforms “many Android rivals”? Please do share the ones it does not outperform. But those A-series chips are “easy”.


> The company in 2020 began replacing processor chips from Intel, 
> used for years in Mac computers, with a proprietary chip that 
> allowed its laptops to run faster and generate less heat, 
> improvements that helped [boost flagging Mac sales](https://www.wsj.com/articles/the-chips-that-rebooted-the-mac-11650081649?mod=article_inline). The 
> Apple chip also saved the company an estimated $75 to $150 on 
> every computer.


Apple’s universally hailed M-series chips are certainly helping Mac sales, but it’s wrong to say Mac sales were “flagging” on Intel. In fact, the final quarter of Mac sales *before* the debut of Apple silicon models — the third calendar quarter of 2020 — was, at the time, [the best sales quarter the Mac had ever had](https://daringfireball.net/linked/2020/10/29/aapl-q4-2020). This, despite the fact that the Apple silicon transition had been announced in June that year at WWDC. The Mac was breaking all-time sales records *before* the switch.


> Apple code-named its modem chip project Sinope, after the nymph in 
> Greek mythology who outsmarted Zeus. It began taking shape in 
> 2018, following the directive of Cook, Srouji, and others for 
> Apple to build its own wireless components, said Chris Deaver, a 
> former Apple human-resources executive and co-founder of BraveCore 
> consultants.


Deaver, the third named source in the Journal report, [worked at Apple in human resources from 2015-2019](https://www.linkedin.com/in/chris-deaver/details/experience/), and co-authored an upcoming book [whose pre-order description](https://www.amazon.com/Brave-Together-Design-Creativity-Co-Creation/dp/1265386676/?tag=df-amzn-20) reads, “From the thought leaders who helped Tim Cook transition Apple from ‘thinking different’ to ‘working different together’ — a timely guide that helps leaders be more creative and creatives be better leaders”. You will never guess the color palette of the book jacket.2


> Srouji flew to Munich to greet Apple’s newly acquired Intel 
> wireless employees in December 2019. He told a gathering that the 
> modem-chip project would be a game changer for Apple, the next 
> step in the company’s evolution, said people who watched the 
> meeting. He said the chip would distinguish Apple devices, as 
> Apple’s processors had done. 
> As Apple filled the project’s ranks with Intel engineers and 
> others hired from Qualcomm, company executives set a goal to have 
> the modem chip ready for fall 2023. It soon became apparent to 
> many of the wireless experts on the project that meeting the goal 
> was impossible.


So it was in 2019, not “late last year”, that Apple hoped for its own cellular modems to be suitable for the iPhones 15 this year. Again, this is all from the same WSJ report.


> Apple found that employing the brute force of thousands of 
> engineers, a strategy successful for designing the computer brain 
> of its smartphones and laptops, wasn’t enough to quickly produce a 
> superior modem chip.


The implication here is that Apple silicon is designed by the proverbial infinite monkeys typing on infinite typewriters — in complete contradiction of Brooks’s Law.


> Modem chips are trickier to make than processing chips because 
> they must work seamlessly with 5G wireless networks, as well as 
> the 2G, 3G and 4G networks used in countries around the world, 
> each with its own technological quirks. Apple microprocessors run 
> software programs designed solely for its iPhones and laptops.


Again and again, this story emphasizes that SoC’s — comprising CPUs, GPUs, neural processing units, and more — are easy, but cellular modems are uniquely difficult. The nonsensical spin in this paragraph is that cellular modems are made difficult by the variety of networks around the world, and Apple’s CPUs are made easier by the fact that they need only execute software “designed solely for its iPhones and laptops”. Let’s leave aside the fact that this clunky phrasing omits form factors like watches, tablets, and desktop computers, and instead consider that Apple silicon is so performant that, via Rosetta 2 translation (technology that I’m sure was also easy to make), the *slowest* Apple silicon Mac ever made (an M1 MacBook Air with 8 GB RAM) [runs software compiled for Intel processors faster than any Intel Mac Apple ever shipped](https://www.macrumors.com/2020/11/15/m1-chip-emulating-x86-benchmark/). Apple silicon not only doesn’t exclusively run software “designed” for it, it runs software compiled for Intel chips better than Intel’s own chips do.


> Apple executives who didn’t have experience with wireless chips 
> set tight timelines that weren’t realistic, former project 
> engineers said. Teams had to build prototype versions of the chips 
> and certify they would work with the many wireless carriers 
> worldwide, a time-consuming job.


The second sentence here implies that Apple’s modem project executives didn’t expect that they’d need to build prototypes or that worldwide carrier certification would be time-consuming — because I’m sure Apple had no difficulty getting the iPhone certified across all supported carriers prior to the start of this project in 2019.


> Executives better understood the challenge after Apple tested its 
> prototypes late last year. The results weren’t good, according to 
> people familiar with the tests. The chips were essentially three 
> years behind Qualcomm’s best modem chip. Using them threatened to 
> make iPhone wireless speeds slower than its competitors. 
> The company scratched plans to use the chips in Apple’s 2023 
> models, and the planned rollout was moved to 2024. Eventually, 
> Apple executives realized the company wouldn’t meet that goal 
> either. Apple instead opened negotiations with Qualcomm to 
> continue supplying the modem chips. Apple’s licensing deal with 
> Qualcomm expires in April 2025, though it can be extended for 
> another two years.


I cannot emphasize enough how goofy the idea is that “late last year” Apple was still hoping to use its own cellular modems in this year’s iPhones.


Here’s what the Journal is declaring a “spectacular failure”: High-end cellular modems are essential components that are very difficult to engineer, and Qualcomm owns the entire market. Apple bought Intel’s second-tier modem business for $1 billion in 2019 and set an ambitious goal of producing its own modems that match or surpass Qualcomm’s by 2023. They missed that best-case-scenario target and thus are still buying modems from Qualcomm and will continue to for at least the next year or two. Not only is this not a “spectacular failure”, not a word of it is news.


> Apple has the cash and the desire to keep pursuing its modem chip, 
> according to people involved with the project. “Apple isn’t going 
> to give up,” said Edward Snyder, a managing director of Charter 
> Equity Research and a wireless industry expert. “They hate 
> Qualcomm’s living guts.”


Finally, a named source in this cursed story who said something accurate.


---

1. For example, consider this passage from a February report by Bloomberg’s Mark Gurman [about Apple’s progress to invent a blood glucose monitor for Apple Watch](https://www.bloomberg.com/news/articles/2023-02-22/apple-watch-blood-glucose-monitor-could-revolutionize-diabetes-care-aapl):

Apple’s system — more than 12 years in the making — is now 
considered to be at a proof-of-concept stage, said the people, who 
asked not to be identified because the project is confidential. 
The company believes the technology is viable but needs to be 
shrunk down to a more practical size. 
Engineers are working to develop a prototype device about the size 
of an iPhone that can be strapped to a person’s bicep. That would 
be a significant reduction from an early version of the system 
that sat atop a table. 

That’s how prototypes work. But no one is proposing, with a straight face, that an iPhone-sized blood glucose monitor might go in next year’s Apple Watch. ↩︎
2. Deaver announced the book on LinkedIn a month ago, and [one of the comments on his post reads](https://www.linkedin.com/feed/update/urn:li:activity:7095517841457631232/), “Thank you for the early peek into your book Chris 🙏🏽😊 It’s very insightful 👏🏽👌🏽”. That comment is from ... Jaydeep Ranade, the second named source in the WSJ report. It’s enough to make a cynical person think that Aaron Tilley fishes for disgruntled former employees willing to be named sources by just clicking around on LinkedIn. But I’m sure it’s just a coincidence that one of the four named sources in the story happened to comment on the LinkedIn post of another. ↩︎︎



| **Previous:** | [The iPhones 15 Pro (and iPhones 15)](https://daringfireball.net/2023/09/the_iphones_15_pro) |
| **Next:** | [iPhone 15 OverheatGate Seems to Be a Nothingburger](https://daringfireball.net/2023/10/overheatgate_nothingburger) |


PreviousNext