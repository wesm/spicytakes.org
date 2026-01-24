---
title: "The Rise of the PokerBots"
date: 2005-08-27
url: https://blog.codinghorror.com/the-rise-of-the-pokerbots/
slug: the-rise-of-the-pokerbots
word_count: 951
---

Computer geeks have a long history of gaming the gaming industry. One of the most notable exploits is documented in the book [Bringing Down The House](http://www.amazon.com/exec/obidos/ASIN/0743225708): The Inside Story of Six MIT Students Who Took Vegas for Millions (read [an excerpt](https://web.archive.org/web/20050828002928/http://www.wired.com/wired/archive/10.09/vegas.html) in Wired). But things have changed now that gambling is moving to the internet in a big way. There’s a fascinating article on Wired about [the rise of the PokerBots](https://web.archive.org/web/20060113200705/http://www.wired.com/wired/archive/13.09/pokerbots.html?tw=wn_tophead_7):


> For years, there has been chatter among online players about the coming poker bot infestation. WinHoldEm is turning those rumors into reality, and that is a serious problem for the online gambling business. Players come online seeking a “fair” shot – a contest against other humans, not robots. But an invasion of bots implies a fixed game (even though, like their mortal counterparts, they can and do lose if their hands are bad enough or opponents good enough). So the poker sites loudly proclaim that automated play is no big deal. At the same time, they are fighting back by quietly scanning for and eliminating suspicious accounts. “We’re making sure we never have bots on our site,” says PartyPoker marketing director Vikrant Bhargava.
> That’s an impossible promise to keep, says Ray E. Bornert II, WinHoldEm’s elusive creator. He’s trying to flood the online world with his bot – and make a killing in the process. Bornert offers an elaborate justification for what many view as outright cheating: Online poker is already rife with computer-assisted card sharks and – thanks to him – a growing number of outright bots. Players should get wise and arm themselves with the best bot available, which is, of course, WinHoldEm.
> There’s a quiet knock at the door of a hotel room in Atlanta. It’s Bornert. A stocky, wide-faced 43-year-old with a neat goatee and nervous manner, he’s carrying a router in a plastic bag. To demonstrate his software, he insists on meeting here in private, several miles from his office. He doesn’t want anyone from the poker business to know where he is. “Our guard is constantly up,” he says.
> For Bornert, a former evangelical student, outsmarting the poker sites is not just a mission, it’s a market. A suite of WinHoldEm programs is available for download at [www.winholdem.net](http://www.winholdem.net/). For $25, you get a bare-bones setup: run-of-the-mill poker-hand analysis software. For $200, you can buy the full package: a one-year subscription to the team edition, which includes the autoplaying bot and a card-sharing module that allows multiple players to communicate during a game. Bornert won’t say how many customers he has; he’ll admit only that he makes a living selling WinHoldEm.


I can tell you from personal experience playing *free* multiplayer internet games that cheating has always been a serious problem. Game developers have to be vigilant and develop countermeasures early. If they don’t, popular games rapidly degenerate into a morass of disheartened, unsure players and an unknown number of cheaters. Nothing psyches you out more than the idea that another player can switch to perfect, bot-like skills at will. Did they win because they were better than you, or because they cheated? There’s just no way to know. It utterly destroys the game experience.


If people are that willing to cheat for literally *nothing*, with zero money at stake, **imagine what lengths they’ll go to when real money is involved**.


That’s why I tend to believe Mr. Bornert, a former evangelical student, when he compares WinHoldEm to civil disobedience:


> “The reality is that the game changed the moment it moved to the Internet,” Bornert says. Bots and bot-aided collusion were inevitable. Rather than seduce anyone into thinking such things didn’t exist, Bornert had another notion: Put the power in the players’ hands. By democratizing computer-assisted firepower, he’d make it part of the competition. “It’s like football – if you don’t wear a helmet and pads, you’re going to get hurt," he says. "A poker bot is your equipment.” And if that is considered unethical, then so be it. “I’d rather be unethical than be a victim,” he says. “This is intentional civil disobedience.”


Despite the protests of the online casino brass, **the rise of the bots is completely inevitable**. There’s simply too much money at stake.


Out of curiosity, I checked out the winholdem support pages. This app is doing **true GUI screen-scraping of the poker apps**. That’s why your poker app settings and Windows display options have to be locked down to known standards.


Of course, online casinos can (and do) fight back:

1. Make your poker apps (these are regular .exe type apps) scan for instances of winholdem running on your local pc. Some online casinos are already doing this. There’s [a countermeasure for that,](http://www.winholdem.net/antidetect.html) too: run it on a remote computer with an application that transmits screenshots of the poker app to the remote machine.
2. Periodically strike up a conversation with the “player.” That’s tougher to combat. You could possibly re-broadcast your chat messages to IM services, if you happen to be near a computer at the time. The bots should limit their play at any given table to prevent a lot of conversation. And definitely have a vast library of canned phrases to respond with – maybe even [an Eliza implementation](https://web.archive.org/web/20050829194659/http://www.manifestation.com/neurotoys/eliza.php3).
3. Change the UI every hand. This is the one option that I didn’t see explored in the article, but would be the hardest to combat. If the cards vary in size, color, design, and position every hand – the scraping app is hosed.


In the meantime, if anyone is making a killing on internet poker with their ’bot, more power to you.

[machine learning](https://blog.codinghorror.com/tag/machine-learning/)
[artificial intelligence](https://blog.codinghorror.com/tag/artificial-intelligence/)
[online gambling](https://blog.codinghorror.com/tag/online-gambling/)
[poker bots](https://blog.codinghorror.com/tag/poker-bots/)
[automated play](https://blog.codinghorror.com/tag/automated-play/)
