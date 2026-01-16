---
title: "Can analysis ever be automated?"
subtitle: "The catch-22 of all these AI analysts. Plus, go crazy folks; go crazy."
date: 2025-08-01T17:14:12+00:00
url: https://benn.substack.com/p/can-analysis-ever-be-automated
slug: can-analysis-ever-be-automated
word_count: 2943
---


![](https://substackcdn.com/image/fetch/$s_!H--P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F902149b7-b890-43e5-afc9-6885d00f853c_1920x1080.jpeg)

*Spocklooksgoodat Excel, but how can we know for sure?*


Here are four charts about the internet, and a quiz:


![](https://substackcdn.com/image/fetch/$s_!6ayQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fade4bc60-a916-495b-8d96-2648124d1fc1_1600x1076.png)


And the quiz: Which charts are right? Or, to make it easier,how would you figure out which charts are right?


I’ll give you a hint: I made one of these charts, and I think I did it right. One of them was made by Paul Krugman, who,givenhiscredentialsand thesizeof hisaudience, probably made it correctly. One was made by ChatGPT, and one was posted on Reddit, by someone whose handle is XsLiveInTexas.


So, which is which? And again, which ones are right?


I mean, ahaha, obviously, there is no easy way to know. If these were photographs, or websites, or mobile apps on your phone, you could probably tell which one was made by one of the most citedexperts of his generation, which one was dug out of Reddit, and which one I haphazardly threw together in about ten minutes. You could probably tell because they might look different.1One app might be buggy and slow, and another might be crisp and reliable. Or there might be signs about which one came from ChatGPT, because it was full of em dashes andunnecessary comments.2


But more importantly, you probably wouldn't even care about who made which one, because you could judge the correctness of each thing on its own merits. You could say which photograph you liked, or which website felt well designed, or which app worked, simply by looking at them or using them.


That’s because these things—like most things—are self-validating: If they work, they work. You can judge them directly, without knowing anything about where they came from or how they’re made. Though the definition of working can be wide—not only do the buttons in an app need to do what they say they do, but there also can’t be esoteric bugs, it needs to be sufficiently fast, it needs to not store users’picturesandprivate messagesin databases that anyone can access—all of this can be verified by the person using the product. Knowing the internals can help with this verification,3but it’s not strictly necessary. No matter how an app was built, if nobody can’t break it, it’s not broken.


When people talk about the dangers of vibe coding, they often worry about AI writing, if not bad code,uncannycode. “It works, it’s clear, it’s tested, and it’s maintainable,”they say, “but it’s written in a way that doesn’t follow the project conventions we’ve accepted.” This has always struck me as an odd concern—or at least, an overstated and potentially temporary one. Code quality is a proxy for application quality, and application quality is both what we care aboutandverifiable on its own. Though it’s slightly more complicated than that—you can’t test every possible edge of a website or an app—at some theoretical limit, an application’s code could be completely incomprehensible, andthat’s fine. And while we may never reach that limit,we could get a lot closer.


But none of this is true for charts, or, more generally, for analysis. There’s no way to know if a chart “works” unless you understand how it was built; the validity of the external product depends on the validity of its internals. Is the source data reliable? Was the math done correctly? Is every formula correctly encoded? We can’t “test” a chart, or verify that it’s correct on its own merits.4Instead, we can only judge it by proxy: Do its conclusions sound plausible enough? Does it look like it was carefully made? Who made it? And then we have to choose if we trust it, or not.


Anyway, last month, a startup called Fundamental Research Labs releasedShortcut, which is a spreadsheet application that looks nearly identical to Excel. Except, it’s 2025,so it’s Excel, with AI:


> You’ll notice Shortcut looks pretty familiar. It has near perfect feature parity with Excel. You can open up existing Excels5and work from there, or you can export them, and of course you can run formulas, but you can also one-shot most of your work and come back when it’s done.Here’s Shortcut solving one of the hardest problems in all of Excel: The Financial Modeling World Cup case that takes about an hour. I attach multiple PDFs, and I ask it to solve it using the existing model, and to make a new sheet with the answers. Now, it actually uses the existing model the way you’re supposed to, and using real Excel formulas. So if fills out the net revenues and then goes and starts to tackle costs, and fills out the rest of the income statement. Then it starts tackling the balance sheet, and realizes the PP&E line item is messed up, and it just recursively solves its own mistakes. So it fixes the PP&E, fills out the rest of the balance sheet, and then it proceeds to the cash flow statement.…Shortcut is also very strong at building complicated models from scratch. Here I asked it to build a multi-tab pro forma cap table6for a post-Series A company and it did this in a single shot in less than 10 minutes—something that takes professional lawyers up to a full day to get done correctly.


Ok, um, how do you trustthat? Not only is there no way to test a cap table (without recreating the cap table, which, again, sort of defeats the purpose of having something do it automatically), but whatever the cap table says is tautologically true—a company’s official cap table is whatever the lawyers’ spreadsheet says it is. There isn’t a reality to compare the cap table to, because the cap tableisreality.


It is weird to me how infrequently this comes up. By now, we’ve all gottenpretty usedto hearingpromisesthatAI analystsarecoming(mostly, of course, from people selling AI analysts). But when people talk about thechallenges associatedwith automating analytical work, they often talk about making sure agents have the right data and context to answer questions correctly. The far bigger problem, however, seems to be thatthere’s no way to know if the work is right. You can’t click around a chart to see if it works like you can on a vibe-coded app. You can’t vouch for a spreadsheet withoutchecking all the spreadsheet’s formulas. All you can do is either read through the code, line by tedious line, or recreate the whole thing yourself. And if you have to do that, what exactly are we automating here?


Although, I guess there’s another way to look at this. A bot doing analysis is to an analyst what an analyst is to everyone else. The CEO asking their finance team for a financial statement can’t verify their work either. People looking at charts on the internet can’t—or don’t—check if they’re right. Both have to believe by reputation and association.


And maybe that’s the difference between products like Claude Code that build software, and products like Shortcut that try to make spreadsheets and do analysis: For the former, real world, in-the-wild correctness matters more than aesthetics and arbitrary benchmarks, because we’ll eventually find its bugs. For the latter, the inverse may be true—its the aesthetics and benchmarks7are what really matter, because we can’t test their work; all we can do is decide if we trust it.


—


To answer the quiz:


I madechart 1, from data provided by the St. Louis Fed. ChatGPT madechart 2, Paul Krugman madechart 3, andchart 4is from XsLiveInTexas. But outside of chart 1, I have no idea if any of them are actually correct, which is kind of the whole point here.


---


# Everyone is crazy now


Over the last couple years, a new type of, uh, “company” has become popular on Wall Street:The crypto treasury company.The idea is simple, and stupid: If you were to list a bank account with $100 million in it on the stock exchange, the market would probably value that company at about $100 million.8But if you were to list a bitcoin wallet with $100 million worth of bitcoin in it, the market seems to value that company at $200 million.


It’s a bit more nuanced than that, but not much. Though you can’t list actual bank accounts, companies have bank accounts. And if a company adds an extra dollar to their bank account, the company will trade a dollar higher. If they add a dollar of bitcoin to their balance sheet, the company trades two dollars higher.


So, if you’re a public company, there’s a pretty straightforward trade:

1. Borrow a bunch of money.
2. Use it to buy bitcoin.
3. Watch your stock price go up by twice as much money as you borrowed.
4. Issue new stock, sell it at the new price, pay back the loans, and keep all the extra money.
5. Or, even better, use the extra money to buy more bitcoin, and keep doing it forever.


This trade was first discovered—invented? manifest?—by Microstrategy. Microstrategy was founded in 1989, and, for thirty years, was a software business. Their2019 annual reporttalked about being a “global leader in enterprise analytics software” and their vision to “enable Intelligence Everywhere™ by delivering world-class software and services that empower enterprise users with actionable intelligence.” You know, classic software stuff. In that filing, they reported making $486 million in revenue, and didn’t mention bitcoin a single time. And the company was worthabout $1.4 billion.


Over the next five years, Microstrategy bought $25 billion worth of bitcoin.9Intheir most recent annual filing, they said “bitcoin” 803 times. And though their software business has barely changed—in 2024, it brought in $463 million in revenue—the company was worth $80 billion at the end of last year.10


Naturally, lots of othercompanies noticed this:


> Companies are raising tens of billions of dollars, not to invest in their businesses or hire employees, but to purchase bitcoin and more obscure cryptocurrencies. A Japanese hotel operator, a French semiconductor manufacturer, a Florida toy maker, a nail-salon chain, an electric-bike maker—they’re all plowing cash into tokens, helping to send all kinds of digital currencies to record levels. News that a new company plans to buy crypto is enough to send its shares flying—spurring others to consider joining the frenzy.Since June 1, 98 companies have announced plans to raise over $43 billion to buy bitcoin and other cryptocurrencies, according to Architect Partners, a crypto advisory firm. Nearly $86 billion has been raised for this purpose since the start of the year.


For some reason, the gambit keeps working. Companies—typically small, stagnant ones that have little to lose11—announce plansto become some sort of cryptocurrency holding company; the stockgoes straight up, valuing the company at a huge premium relative to its cryptocurrency holdings; nobody quite knows why.


People have speculated that theremight be rational reasonsfor the market to react this way: Maybe Microstrategy can use all that money to build a huge software business; maybe stock market investors wants exposure to crypto, and buying equities that are effectively bitcoin indexes funds is a useful way to do it. But there is also another, more obvious, explanation—it’s 2025, and in 2025, everything is a meme, andeveryone is crazy.From Matt Levine:


> The obvious appeal of the crypto treasury strategy for most small US public companies is probably along the lines of ‘nobody is paying attention to our tiny company, but if we announce we’re buying a big pot of crypto, retail traders will get excited and overpay for our stock.


As we talked about last week, this now seems to be the most reliable way to make money these days:

1. Do something crazy.
2. Get attention for it.
3. Monetize that attention.


Like: Reddit-loving retail day traders love crypto, and crazy shenanigans. Buying a bunch of crypto shows them you aren’t some boring wooden company but are crazy and degenerate and fun; they decidethey like the stock. And the whole thing becomes somewhat self-fulfilling, because institutional investors anticipate Reddit liking the stock, everyone buys it, and it goes up.


Still, for companies that want to become crypto treasuries, there’s at least one problem with this plan: Crazy is relative. In 2020, a public companybuying bitcoinwas crazy. It’s not crazy when everyone’s doing it. So maybe buyingEthereumis? OrSolana? You have to find new things.


But of course, you can be crazy and based in other ways too. For example, AMC, which has been one of Reddit’s favorite stocks since theGamestop incident, tried to buy agold mine, and thestock went up. More recently, American Eaglewent all inon a, uh, bold marketing campaign with Sydney Sweeney, and thestock went up. If Astronomer had been a public company two weeks ago, what do you think would’ve happened to the stock?12


And so, a reader writes in:


> Right now the most shareholder maximizing thing American Eagle could do is probably appoint Sydney Sweeney as CEO.


Surely, half the boardrooms in Americaare weighingif they should buy crypto. But shouldn't they be weighing other things too? Crypto is mainstream!JPMorganisletting peoplebuy crypto! Microstrategy’s narrow discovery was that crypto is worth a lot of money on the stock market. But their broader discovery is that being crazy is worth a lot of money on the stock market. And what would prove to the retail market that you’re crazy like them more than appointing Sydney Sweeney—or anyone from the Reddit-coded cinematic universe—as your CEO, especially if you’re the first company to do it? How much wouldthatstock go up?Go crazy, folks, go crazy!


—


While we’re here, I have more questions:

1. I said earlier that a bank account worth $100 million would trade for $100 million on the stock market. But would it? If a company came out and said they were now a dollar bill treasury company, and made a big, ironic show about how their entire business was storing dollar bills in a bank vault, and they actually did that, with a giantScrooge McDuckswimming pool of money, do you think that company would trade for $100 million? Less?More?I don’t know! Someone should try it.
2. I said earlier that most crypto treasury companies become crypto treasury companies because they’re small and stagnant businesses that have nothing to lose. So what would happen if a huge company decided to become a crypto treasury company? Google has about$100 billion of cash(or cash equivalents) on hand; what iftheybought $50 billion worth of bitcoin? It’s one thing to be crazy when you have nothing to lose; it’s another thing when you have a$2 trillion businessto lose.
3. After the whole Coldplay circus, Astronomer eventually responded byreleasing an ad(of sorts) with Gwyneth Paltrow. The bit wasgenerally well received, as both relatable and lightly self-deprecating, and as a smart way to gently capitalize on the attention. But selling a product, especially a niche one like Astronomer, is an awfully inefficient way to make money from attention these days. What you really want to do is sell financial assets—a meme coin, Astronomer stock, anything. So rather than running an ad, should they had launched a coin? An emergency IPO? When you’re the biggest meme of the year, isn’t the right thing to do to immediately turn that meme into something you can sell?

[1](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-1-169857033)

For example, ofthesetwowebsites, which one was made by Stripe, and which one was made by personal injury lawyers in Las Vegas?

[2](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-2-169857033)

Yeah,whowouldeverusethose?

[3](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-3-169857033)

For example,penetration testsare often done by engineers who have access to an application’s codebase. They look for flimsy bits of code, and then bang around the software to see if they can exploit the cracks. Normal hackers (and everyday users) are typically only able to do the latter.

[4](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-4-169857033)

There are potentially two counterarguments to this, but neither strike me as particularly compelling. The first is that you can “test” a chart by testing its conclusion in the real world. A chart tells you tomove from LA to New York; you move from LA in New York; you find out if it was a good idea. But that’s obviously indirect, extraordinarily impractical, and sometimes, outright impossible. How do you test the chart that shows how fast different products got to 100 million users? There is no experiment to run that would confirm its conclusions.The second way to test a chart is to recreate it. That works, in the sense that you could confirm what it says is true, but is sort of self-defeating. What’s the point of making a chart if the people reading it don’t believe it unless they make it themselves?

[5](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-5-169857033)

Excels? Are we allowed to say that?

[6](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-6-169857033)

Cap tables keep track of who owns shares in a company. In their simplest form, cap tables are spreadsheets that list people’s names, the number of shares they each have, and how much of the company they own. Real cap tables are much more complicated than this, because there are different share classes, people often hold options to buy shares but don’t own the shares yet, and so on.

[7](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-7-169857033)

Speaking of, for reasons, if you have thoughts on or are interested in benchmarks for analytical work…email me?

[8](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-8-169857033)

Although…what if…(see the next section).

[9](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-9-169857033)

How did they get the money to do this? By buying bitcoin, seeing their stock price go up, selling stock into that demand, and buying more bitcoin. As they said in their annual filing, “during 2024, we purchased bitcoin using $16.330 billion of the net proceeds from our sale of class A common stock under our at-the-market equity offering program.”

[10](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-10-169857033)

And today, the company is now simply called Strategy; itshomepageis a dashboard of its balance sheet and bitcoin prices; it owns 628,791 bitcoin, which is worth $72 billion at today’s prices; the company trades at $107 billion.

[11](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-11-169857033)

Although…what if…(see the next section).

[12](https://benn.substack.com/p/can-analysis-ever-be-automated#footnote-anchor-12-169857033)

Although…what if…(see the next section).
