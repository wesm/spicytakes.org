---
title: "In Defense of Not-Invented-Here Syndrome"
date: 2001-10-14
url: https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/
word_count: 1056
---


Time for a pop quiz.
 1. Code Reuse is:

a) Good
b) Bad

2. Reinventing the Wheel is:

a) Good
b) Bad

3. The Not-Invented-Here Syndrome is:

a) Good
b) Bad

Of course, *everybody knows* that you should always leverage other people’s work. The correct answers are, *of course*, 1(a) 2(b) 3(b).
Right?
Not so fast, there!
The Not-Invented-Here Syndrome is considered a classic management pathology, in which a team refuses to use a technology that they didn’t create themselves. People with NIH syndrome are obviously just being petty, refusing to do what’s in the best interest of the overall organization because they can’t find a way to take credit. (Right?) The Boring Business History Section at your local megabookstore is rife with stories about stupid teams that spend millions of dollars and twelve years building something they could have bought at Egghead for $9.99. And everybody who has paid any attention *whatsoever* to three decades of progress in computer programming knows that Reuse is the Holy Grail of all modern programming systems.
Right. Well, that’s what I thought, too. So when I was the program manager in charge of the first implementation of Visual Basic for Applications, I put together a careful coalition of four, count them, four different teams at Microsoft to get custom dialog boxes in Excel VBA. The idea was complicated and fraught with interdependencies. There was a team called AFX that was working on some kind of dialog editor. Then we would use this brand new code from the OLE group which let you embed one app inside another. And the Visual Basic team would provide the programming language behind it. After a week of negotiation I got the AFX, OLE, and VB teams to agree to this in principle.
I stopped by Andrew Kwatinetz’s office. He was my manager at the time and taught me everything I know. “The Excel development team will never accept it,” he said. “You know their motto? ‘Find the dependencies — and eliminate them.’ They’ll never go for something with so many dependencies.”
In-ter-est-ing. I hadn’t known that. I guess that explained why Excel had its own* *C compiler.
By now I’m sure many of my readers are rolling on the floor laughing. “Isn’t Microsoft stupid,” you’re thinking, “they refused to use other people’s code and they even had their own compiler just for one product.”
Not so fast, big boy! The Excel team’s ruggedly independent mentality also meant that they always shipped on time, their code was of uniformly high quality, and they had a compiler which, back in the 1980s, generated pcode and could therefore run unmodified on Macintosh’s 68000 chip as well as Intel PCs. The pcode also made the executable file about half the size that Intel binaries would have been, which loaded faster from floppy disks and required less RAM.
“Find the dependencies — and eliminate them.” When you’re working on a really, really good team with great programmers, everybody else’s code, frankly, is bug-infested garbage, and nobody else knows how to ship on time. When you’re a cordon bleu chef and you *need* fresh lavender, you grow it yourself instead of buying it in the farmers’ market, because sometimes they don’t have fresh lavender or they have old lavender which they pass off as fresh.
Indeed during the recent dotcom mania a bunch of quack business writers suggested that the company of the future would be totally virtual — just a trendy couple sipping Chardonnay in their living room outsourcing everything. What these hyperventilating “visionaries” overlooked is that the market pays for value added. Two yuppies in a living room buying an e-commerce engine from company A and selling merchandise made by company B and warehoused and shipped by company C, with customer service from company D, isn’t honestly adding much value. In fact, if you’ve ever had to outsource a critical business function, you realize that outsourcing is hell. Without direct control over customer service, you’re going to get nightmarishly bad customer service — the kind people write about in their weblogs when they tried to get someone, *anyone*, from some phone company to do even the most basic thing. If you outsource fulfillment, and your fulfillment partner has a different idea about what constitutes prompt delivery, your customers are not going to be happy, and there’s nothing you can do about it, because it took 3 months to find a fulfillment partner in the first place, and in fact, you won’t even *know* that your customers are unhappy, because they can’t talk to you, because you’ve set up an outsourced customer service center with the explicit aim of *not* listening to your own customers. That e-commerce engine you bought? There’s no way it’s going to be as flexible as what Amazon does with obidos, which they wrote themselves. (And if it is, then Amazon has no advantage over their competitors who bought the same thing). And no off-the-shelf web server is going to be as blazingly fast as what Google does with their hand-coded, hand-optimized server.
This principle, unfortunately, seems to be directly in conflict with the ideal of “code reuse good — reinventing wheel bad.”
The best advice I can offer:

**If it’s a core business function — do it yourself, no matter what.**

Pick your core business competencies and goals, and do those in house. If you’re a software company, writing excellent code is how you’re going to succeed. Go ahead and outsource the company cafeteria and the CD-ROM duplication. If you’re a pharmaceutical company, write software for drug research, but don’t write your own accounting package. If you’re a web accounting service, write your own accounting package, but don’t try to create your own magazine ads. If you have customers, never outsource customer service.
If you’re developing a computer game where the plot is your competitive advantage, it’s OK to use a third party 3D library. But if cool 3D effects are going to be your distinguishing feature, you had better roll your own. 
The only exception to this rule, I suspect, is if your own people are more incompetent than everyone else, so whenever you try to do anything in house, it’s botched up. Yes, there are plenty of places like this. If you’re in one of them, I can’t help you.
[Discuss](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=112)
