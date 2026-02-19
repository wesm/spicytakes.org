---
title: "Independent Days"
date: 2003-07-08
url: https://daringfireball.net/2003/07/independent_days
slug: independent_days
word_count: 4362
---


## Part 1: On Men’s Hairpieces and Web Design


First, an anecdote.


Several years ago, the Philadelphia Daily News ran a terrific feature about why men’s hairpieces tend to look so dreadful. As in: how come we can put men on the moon and transplant hearts, but [Charlton Heston](http://daringfireball.net/misc/2003/07/heston.jpg) has been walking around for 30 years with what can only be described as a dead possum on his head?


So the Daily News spoke to several Philadelphia-area hairpiece specialists, and their responses were identical: the problem is that when men buy hairpieces, they demand too much hair. I.e. it is possible to do a very convincing job with a hairpiece that makes you look *balding* rather than bald, but it is not possible to create a convincing hairpiece that makes it look as though you have a full head of hair.


These guys were pros, genuine craftsmen who took a lot of pride in their work. They wanted their customers to look *good*, not silly. But time after time, despite their best efforts to steer customers toward something subtle — something along the lines of Bruce Willis’s *Moonlighting*-era topper — their customers insisted on more. As one fellow explained it, a good hairpiece costs a lot of money, and for a lot of money, the customer wants to see a lot of hair.


This story stuck with me because it epitomizes the problems in any designer-client relationship. The designer typically does know best, but it’s the client who gets the final say. An analogy to web design is particularly apt. I’ve never liked the adage *Less is more* — it’s terribly clichéd, and its paradoxical nature makes it too easy to dismiss. I say *Less is better,* which is neither cute nor clever, but almost always true.


Less markup. Less scripting. Fewer navigation elements. Fewer colors. Fewer graphics. Omit needless words. This is how you make a good web site. I know this for a fact.


Such design goals, however worthy, are notoriously difficult to sell to clients. A good web site costs a lot of money, and for a lot of money, most clients want a lot of web site. Lots of scripts. Lots of graphics. Lots of needless words.


This web site, Daring Fireball, exemplifies almost everything I know about web design. This is pretty close to the best that I can do. Everything you see is there for a reason. Everything you don’t see is not there for a reason. Every decision was made with one goal in mind: making this a better web site for you, the reader. As Albert Einstein said, “Everything should be as simple as possible, but not more so.”


## Part 2: Damn, Dirty Adverts


But so why then am I defiling a minimalist design with ads from Google? Undeniably, the ads are both unattractive and distracting, neither of which adjectives are generally associated with making anything “better”.


Let’s not mince words. The answer is *money*. Well, and *time,* since time truly does equal money. And I’m not talking about merely covering my hosting expenses. I’m talking about generating a reasonable portion of my income from this web site.


I have no qualms about this goal.


If asked to describe Daring Fireball with just one word, I would not choose *weblog*. Rather, I would call it a *column.* Given a few more words, I would call it as a Mac column in the form of a weblog. To me, the two great formats for writers are the book and the column, in the same way that the two great foot races are the marathon and the sprint.


A good columnist establishes a rhythm, writes with a distinctive voice, and connects to a regular readership. That’s exactly what I’m striving for here. I don’t want to publish it anywhere but right here, on my site. Daring Fireball is more than just words; it is an entire presentation.


And where else *could* it be published? Certainly not in print. The immediacy and linkability of the web are central to Daring Fireball’s entire premise. Of course, most print periodicals now co-publish to the web, but just look at them. Given that presentation and design are important, publishing Daring Fireball as a column on a major corporate media web site would be a giant step backwards.


You might think that the Google ads now displayed here are ugly; but for fuck’s sake, look at the web sites produced by corporate media conglomerates. E.g. look at [Charles Haddad’s latest “Byte of the Apple”](http://www.businessweek.com/technology/content/jul2003/tc2003072_0512_tc056.htm) column for Business Week. I see five ads, in five different sizes; all of them graphical, three of them animated. *Animated!* Can you even conceive of a more deliberate attack on readability than peripheral animated advertisements? And yet animated ads are an industry standard practice.


And the layout: Business Week’s web pages use 4 irregularly shaped columns, three of the four columns contain ads. You can get an easier-to-read version by clicking the link to the “printer-friendly” version, but that requires waiting for an extra page to load, and removes essential site navigation links. Sites that offer “printer-friendly” versions of each article are effectively admitting that their standard page designs are overly complicated; what makes the “printer-friendly” versions better to print also makes them easier to read on screen. (CSS print media style sheets could take care of printer-formatting issues, with no extra clicks or work required on the reader’s part.)


Examine the HTML source code. Careful, it’s nauseating. The source code to Haddad’s column is [riddled with errors](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.businessweek.com%2Ftechnology%2Fcontent%2Fjul2003%2Ftc2003072_0512_tc056.htm&doctype=HTML+4.01+Transitional&charset=iso-8859-1+%28Western+Europe%29). Not just non-standard proprietary markup, but outright undeniable *errors*. Even if you subscribe to the “if it looks good in my browser, I don’t care about the code” school of thought, you have reason to complain. Business Week’s code is so bloated with crap that you’re forced to download 76 KB of source code just to read Haddad’s 800-word column. (That figure doesn’t include the size of the ad graphics.) In comparison, at this moment the front page of Daring Fireball contains 1,800 words, but the HTML document weighs only 20 KB. One-fourth the size, valid and well-formed, with over twice the actual content.


The ads, the layout, the crummy source code — none of these are Haddad’s fault. They are Business Week’s fault. Haddad has no control over the presentation or design; he just writes. But his writing isn’t so hot either, in this case. Haddad’s premise is that Apple is going to change from a Mac-centric company to an iPod-centric company.


There’s a kernel of truth to Haddad’s premise: the iPod *is* a smash hit, and indeed, support for Windows is a big part of that success. The iPod has single-handedly moved Apple into a leadership position in a totally new industry. And the iTunes Music Store is a huge deal.


All true. *But everybody already knows these things.* So Haddad took the sensational route, writing something that was sure to stir things up and generate some controversy. No one would have taken note or linked to this column if he had simply pointed out that the iPod has been a huge success and that Apple is in good shape to expand its leadership position in personal digital music players. The reaction to that would have been, “Duh.” So Haddad turned the journalism dial to yellow, and took the “the Macintosh is doomed, but the iPod will save Apple Computer” angle. Now that’s worth linking to — Business Week says the Mac is doomed!


Here’s Haddad’s kicker:


> And, when the Windows version is available, sales will
> 	jump even higher to 1.25 million, or equivalent to the sales of some
> 	Macs. With that kind of growth Macs will become a nice little side
> 	business — perhaps even a giveaway someday to lure eager iPod
> 	buyers.


Ignore for now that Apple has been selling a Windows version of the iPod for quite a while already — Haddad is referring to the upcoming iTunes for Windows, which probably *will* drive iPod sales even higher. Let’s just do the math. Let’s say Haddad’s speculation is correct, and that Apple will eventually sell 1.25 million iPods per year. Let’s further assume an average selling price of $400. That’s $500 million per year in revenue.


In 2002, [Apple reported $5.76 *billion* in revenue](http://www.apple.com/pr/library/2002/oct/16earnings.html). In 2001, $5.36 billion. $500 million in iPod revenue is certainly not chump change; but it certainly doesn’t indicate that Macs will become a “side business” for Apple any time soon. Sort of takes all the piss and vinegar out of Haddad’s premise, no?


Of course, there is one remaining major difference between Haddad’s Business Week column and an independent web site like Daring Fireball, and it is the key to understanding all the other differences: Haddad gets paid.


Hence the ads — Business Week collects money from its advertisers, then uses some of that money to pay their writers. One can assume that the plan is such that the ads accompanying Haddad’s columns generate more revenue than the cost of Haddad’s paychecks. I.e. that Haddad’s column is profitable for Business Week.


I’m going to further assume that Business Week charges its advertisers based on the number of impressions. Not how many times the ad get clicked, but rather how many times they are seen. This sort of advertising model is roughly analogous to that of the print world (where the ads are, of course, unclickable). This explains why there are so many ads — more ads on each page means more money.


This also explains why columnists in the technology trade press might be tempted to err on the side of sensationalism. Write something controversial, and you tend to get linked to from other sources. This brings in readers, readers who may well disagree vehemently with your premise, but readers nonetheless. More readers equals more impressions; more impressions equals more money.


Any traffic is good traffic when you’re charging advertisers per impression. Most people who know anything about the computer industry think [John C. Dvorak](http://www.pcmag.com/category2/0,4148,3574,00.asp) is a moron. But his editors at PC Magazine probably consider him one of their top writers. Not because he writes things that are insightful or accurate, but because he writes things that are controversial. (Remember his “[Apple Going to Intel Chips](http://daringfireball.net/2003/04/qwerty.html)” bit back in April?)


## Part 3: Your Humble Independent Web Publisher


The urge to pander to the lowest common denominator proves irresistible to most advertising-supported media.


Take television — shows with more viewers charge higher rates for advertisers. Thus, the primary goal for commercial television shows is to attract the largest possible audience. This is not the same goal as creating the best possible shows. High quality commercial broadcast shows do exist, but they are in the minority; for every *60 Minutes*, there are half a dozen crapfests like *Dateline NBC* or *20/20*.


Original shows on HBO — like *The Sopranos* and *Six Feet Under* — are vastly superior to their commercial network counterparts. HBO is a subscriber-based service, and carries no advertising. It attracts a much smaller, but more discriminating audience. HBO viewers are willing to pay for quality, and in turn, HBO is motivated to continue producing high-quality shows to attract more subscribers.


My goal for Daring Fireball is not to attract the largest possible audience. Rather, I’m trying to attract the *smartest* possible audience.


When you create anything for public consumption, you must make assumptions regarding the audience. Regarding you, courteous reader of Daring Fireball, I assume the following. You are intelligent. You appreciate good design and careful writing. You use a modern web browser that supports reasonably established web standards. Your time is valuable.


Most corporate commercial web sites assume the opposite. They assume you are incapable of basic critical thinking. They assume you will tolerate terrible design. They assume you are using Netscape 4; that you don’t mind waiting for their bloated pages to load; that you don’t mind loading a different page if you want to print; and that you are willing to tolerate blinking ads.


The distinction worth making is not between *professional* vs. *amateur* web sites. That just means whether you’re getting paid. The distinction worth making is *corporate* vs. *independent*.


It was corporations that fueled the dot-com binge, trying to turn the web into a big money medium, and who then deemed it a failure after that didn’t work out. No matter that their billion-dollar plans were never realistic and involved shoe-horning the web into the ill-fitting paradigms of existing media.


Independent web publishers — individuals and small teams — have never considered the web, as a medium, to be a failure. On the contrary, they view it as a roaring success. They have embraced all along that the web is neither like print nor broadcast — that the web is only like the web.


What is most remarkable is that the web is the only medium where independent personal publishers are delivering superior-quality products than the giant media conglomerates. Motion pictures? Forget about it. Even a low-budget film costs millions of dollars. A *shoestring* budget film might have a good story and engaging characters, but it isn’t going to look good. It’s an extremely expensive medium. Broadcast? Low-budget independents can only dream of producing broadcast media.


Print? Independents can fight to a draw here, in terms of quality, but it’s difficult to scale on a low budget. Paper and printing, and the distribution thereof, is much more expensive than Internet bandwidth.


The web is where independents shine. Independent web sites tend to look better and are better produced. Their URLs are even more readable. This isn’t bluster about the future, this is a description of today. With a text editor and an Apache web server, you’re on equal footing with any web site in the world. Even if you can’t design worth a lick, the default templates for most major weblog packages are decidedly more readable and better designed than typical corporate media web sites. For short-form opinion and analysis, the web cannot be beaten as a writing and reading medium. The immediacy, linkability, lack of word count restraints (this works *both* ways, short and long) and direct connection between writer and reader puts the independent producer at a decided advantage over media corporations.


Who are your favorite sources for technology opinion and analysis? My favorites are *all* independents. For other, more mainsteam, topics, e.g. politics, independents are gaining, and corporate media web sites tend to be propped up by successful print publications. The New York Times is almost certainly the best newspaper in the world, but it’s not a very good web site at all. It doesn’t look good, it’s hard to navigate, and worst of all, its content is only available for free for up to two weeks. That might make business sense, but it doesn’t make web sense — look no further than the crippling effect it’s had on The Times’s standing in Google rankings.


And so the question as to why I want to make money from Daring Fireball is backward. I say, *why not?*  If I printed a book, you’d expect me to sell copies. Same if I were in a band and made my own CD, or if I produced a movie on DVD. But so why do so many people assume that with web sites, “independent” need be synonymous with “volunteer”?


Well, there are good reasons for that. First, you can’t sell copies of a web site in the way you can with books, CDs, and DVDs. Nor can you charge for admittance, as you can with live performances or cinema screenings. You *can* charge a mandatory subscription fee, but that sucks, going completely against the nature of the web.


What options are left? Voluntary contributions and advertising.


Corporate media have chosen the advertising route, for obvious reasons. But as stated earlier, the choice to fund web sites via traditional advertising has profound effects on content, favoring quantity over quality.


Independent web sites that pursue funding tend to do so by asking for contributions. I’ve been thinking about potential ways to fund Daring Fireball for quite a while, and until recently, the contributions route seemed the only option. The closest analogy I can think of are fund drives for America’s public broadcasting stations. There is a certain appeal to the directness of being reader-funded: I write, you read; if you like, you pay. Or more specifically, *some* of you pay. Even in the most optimistic scenario, only a small minority of readers would contribute to a voluntary fund-raising drive. But that’s fine — with a regular readership of several thousand, a small minority could run well into three digits. A few hundred people, each donating, say, $25 — and you have something. You don’t have a full-time salary, but you’d at least have a nice side income.


Several thousand dollars a year would at least be on par with the money I could make writing freelance articles for larger media sites. For example, back in January, I wrote an article for O’Reilly’s MacDevCenter about [scripting BBEdit 7’s rectangular selections](http://www.macdevcenter.com/lpt/a/3087). I love this article, it’s one of my favorite things I’ve written in the last year. Which is why I pitched it to O’Reilly — and also why I wish I’d published it on Daring Fireball. I enjoyed cashing the check, of course, but it was only for a few hundred dollars. I don’t like the idea of taking my best articles and shopping them around — if I’m going to get paid to write, why not here at Daring Fireball?


The problem with asking for contributions from readers, however, is that the solution doesn’t scale. While I’m proud of Daring Fireball, I don’t think it’s a particularly special or deserving web site. *(I am not a unique snowflake.)* If Daring Fireball is worthy of funding, so are hundreds of other high-quality independent sites. Maybe thousands, and soon to be more.


The number in my head is $25 a year. That’s about 50 cents a week. It sounds fairly reasonable to contribute $25 a year to your favorite independent web site. But what happens when your 10 favorite web sites start asking for contributions? Now you’re looking at $250 a year, which sounds decidedly less like pocket change.


## Part 4: Wherein I Get to the Point; Or: How I Learned to Stop Worrying and Love the Ads


Which brings us to Google, and their AdSense program.


There are numerous other affiliate and advertising programs I could have used to whore up Daring Fireball. But I believe AdSense is different, and the only one worth trying.


First, their ads are just text. No images, no animation. Google’s ads are definitely not good-looking, and they clash horrendously with Daring Fireball’s design, but they’re downright subtle compared to the animated GIFs that comprise traditional web advertising.


Second, Google’s ads are not insulting to your intelligence. You’re not going to see any *You may already be a winner! Click Here!* ads.


Third, Google flat-out forbids the use of any JavaScript dirty tricks; most especially no pop-up windows. When you click a link in one of these ads, it’s just a link.


Fourth, Google’s ads are pay-per-*click*, not pay-per-impression. This is an advantage both for advertisers and for you, the reader. The advantage to advertisers is that they only pay when people actually click on their ads. The advantage to you, the reader, is that this policy (along with Google’s screening process) tends to keep away the bottom-dwellers.


Ostensibly, Google uses their content analysis algorithms to serve ads that are geared toward the content of each site in the AdSense program — much like how the “sponsored link” text ads work in Google.com search results. Actually, not just specific to each site, but specific to each *page*. In two weeks of AdSense at Daring Fireball, the results of this have been mixed. I’ve seen lots of Macintosh-related ads, which is pretty good. But for the last week, the ads on the home page have been related to “cost per click” advertising, thanks to the article I wrote when the ads debuted. And [this article about Apple’s Safari web browser](https://daringfireball.net/2003/05/safaris_unscriptable_tabs.html) contains ads for safari vacations to Africa. An honest mistake for an AI system, but certainly not on topic.


[**Update:** Google apparently thinks this very article is about men’s hair loss products, based on the accompanying ads. Which in addition to being somewhat funny, indicates either that their content analysis software only looks at the first few paragraphs on a page, or that hair loss companies are willing to pay more per click than Mac advertisers are.]


After two weeks, I’ve been averaging a hair under 40 cents per click. So where’s the money coming from? It’s coming from you, courteous reader. Not from your credit card or PayPal account, but from your eyeballs.


The lone natural resource in the media landscape is attention. Your attention is what all media are fighting for, and the laws of physics place finite limits upon it. I’ve seen a few comments regarding AdSense where people speculate that Google will have to soon either pull the plug or reduce the amount of money it pays per click — that at 40 or 50 cents per click, it just can’t last.


I think it can. Google is not paying for these clicks out of their corporate pockets — the advertisers are. The advertisers agree to pay Google a certain amount of money per click, and are happy to do so. That amount seems to vary, but it’s obviously somewhere in the general vicinity of one dollar per click. I’ve also spoken to several people who are paying to advertise in Google text ads, and every one of them is delighted with their results.


There’s no chicanery involved. Advertisers get exactly what they pay for — clicks to their web sites from you, my readers. Google charges a small amount of money from the advertiser for each click, keeps a portion for themselves, and passes the rest along to me. The advertiser is happy to get your clicks, Google and I are happy to get the advertiser’s money.


So effectively, Google’s AdSense is an exchange system for converting your attention into money. All advertising is based on a similar conversion, but Google’s is much more efficient, because a click is worth so much more than a mere ad impression. With traditional web advertising, Daring Fireball’s few thousand readers would be worth pennies per day. With Google AdSense, they seem to be worth *dollars* per day — an order of magnitude difference, but yet with much less intrusive ads.


At 40 cents a click, this has the potential to add up fairly quickly. AdSense has the potential to become a serious source of funding for independent web producers. Don’t sell yourself short — your attention is valuable, and advertisers are willing to pay handsomely for it.


## Part 5: A Man, A Plan, A Canal. Panama.


And so here is my plan. Next month will mark Daring Fireball’s one-year anniversary. At that time I’ll commence a brief fund-raising drive, asking for voluntary donations. Perhaps there will be T-shirts and other Daring-Fireball-logo’d tchotchkes.


In the meantime, the Google ads will continue.


I suspect that Google tracks which ads are being clicked on each site, and uses this information to fine-tune the ads it serves. So if Daring Fireball readers tend to click on ads related to Mac stuff, Google will start sending more Mac-related ads. If you’re willing to click on these ads, I ask you to look for ads that seem at least vaguely interesting to you. If none of the ads on a page are interesting, then don’t click on them. In this way, you’ll not only help me earn money honestly, you’ll also help make future ads more appropriate to Daring Fireball’s audience.


I realize that some of you despise the ads, and refuse to click on them. That’s OK. My AdSense cohort Dan Benjamin has devised an “[Optional Advertising](http://hivelogic.com/354.php)” apparatus, providing his Hivelogic readers the option to turn off the ads. A fine idea, and one I plan on duplicating here. (I also have a few idea for tinkering with ad placement in my layout.)


If you *are* willing to click a few ads per week, however, I want you to know that I appreciate it very much. AdSense effectively works as a micropayment system, but instead paying with small amounts of money, you pay with small bits of your attention. In no way is this “free money” — your attention is time, and time is money. In every modern Mac OS web browser, you can hold the Shift and Command keys while clicking a link to load the new page in a background window (or background tab), without disturbing the current front window. This is an excellent way to click ads while suffering minimal annoyance.


Further note that this funding plan does not imply any threats. I’m not saying, “Pay me or I’ll stop writing.” On the contrary, if this doesn’t work out — if no one contributes and no one clicks on the ads — Daring Fireball will simply continue as it has. I enjoy this very much, and have no plans to stop.


The idea is simply that with some financial support from you, my readers, I’ll be able to do *more*. More writing, more improvements to the site. Perhaps even some sort of public discussion forum, which many of you have asked for.


As always, I welcome your comments via email. Thanks for reading.


## Postscript: Further Reading

- The decline in traditional banner advertising has prompted Ric Ford to move MacInTouch toward voluntary reader funding. MacInTouch has been an outstanding source of daily information for a remarkably long time. It’s my first surf each morning. Ford’s “[The Future of MacInTouch](http://macintouch.com/future.html)” is worth reading, and MacInTouch is worth supporting.

- [Jeffrey Zeldman writes on the quality-vs.-quantity advantages](http://www.zeldman.com/daily/0703a.shtml#tutorials) that independent web sites enjoy over corporate media sites.



| **Previous:** | [Textiles](https://daringfireball.net/2003/07/textiles) |
| **Next:** | [The Good, the Bad, and the Avie](https://daringfireball.net/2003/07/the_good_the_bad_and_the_avie) |


PreviousNext