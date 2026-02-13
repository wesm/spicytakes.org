---
title: "Strategy Letter II: Chicken and Egg Problems"
date: 2000-05-24
url: https://www.joelonsoftware.com/2000/05/24/strategy-letter-ii-chicken-and-egg-problems/
word_count: 2692
---


The idea of advertising is to lie without getting caught. Most companies, when they run an advertising campaign, simply take the most unfortunate truth about their company, turn it upside down (“lie”), and drill that lie home. Let’s call it “proof by repeated assertion.” For example, plane travel is cramped and uncomfortable and airline employees are rude and unpleasant, indeed the whole commercial air *system* is designed as a means of torture. So almost all airline ads are going to be about how *comfortable* and *pleasant *it is to fly and how *pampered* you will be every step of the way. When British airways showed an ad with a businessman in a plane seat dreaming that he was a baby in a basket, all sense of reasonableness was gone for good.


Need another example? Paper companies are completely devastating our national forests, clear cutting old growth forest which they don’t even own. So when they advertise, they inevitably show some nice old pine forest and talk about how much they care about the environment. Cigarettes cause death, so their ads show life, like all the ads with happy smiling healthy people exercising outdoors. And so on.


When the Macintosh first came out, there was no software available for it. So obviously, Apple created a giant glossy catalog listing all the great software that was “available”. Half of the items listed said, in fine print, “under development,” and the other half couldn’t be had for love or money. Some were such lame products nobody would buy them. But even having a thick glossy catalog with one software “product” per page described in glowing prose couldn’t disguise the fact that you just could not buy a word processor or spreadsheet to run on your 128KB Macintosh. There were similar “software product guides” for NeXT and BeOS. (Attention, NeXT and BeOS bigots: I don’t need any flak about your poxy operating systems, OK? Write your own column.) The only thing a software product guide tells you is that there is no software available for the system. When you see one of these beasts, run fleeing in the opposite direction.


Amiga, Atari ST, Gem, IBM TopView, NeXT, BeOS, Windows CE, General Magic, the list of failed “new platforms” goes on and on. Because they are *platforms*, they are, by definition, not very interesting in and of themselves without juicy software to run on them. But, with very few exceptions (and I’m sure I’ll get a whole *host *of email from tedious supporters of arcane and unloved platforms like the Amiga or RSTS-11), no software developer with the least bit of common sense would intentionally write software for a platform with 100,000 users on a *good* day, like BeOS, when they could do the same amount of work and create software for a platform with 100,000,000 users, like Windows. The fact that anybody writes software for those oddball systems at all proves that the profit motive isn’t everything: religious fervor is still alive and well. Good for you, darling. You wrote a nice microEmacs clone for the Timex Sinclair 1000. Bravo. Here’s a quarter, buy yourself a treat.


So. If you’re in the platform creation business, you are probably going to suffer from what is commonly known as the *chicken and egg problem*. Nobody is going to buy your platform until there’s good software that runs on it, and nobody is going to write software until you have a big installed base. Ooops. It’s sort of like a Gordian Knot, although a Gordian Death Spiral might be more descriptive.


The chicken and egg problem, and variants thereof, is *the* most important element of strategy to understand. Well, OK, you can probably live without understanding it: Steve Jobs practically made a *career* out of not understanding the chicken and egg problem, *twice*. But the rest of us don’t have Jobs’ Personal Reality Distortion Field at our disposal, so we’ll have to buckle down and study hard.


Lesson one. The classic domain of chicken and egg problems is in software platforms. But here’s another chicken and egg problem: every month, *millions* of credit card companies mail out *zillions* of bills to consumers in the mail. People write paper checks, stuff them in trillions of envelopes, and mail them back. The envelopes are put in big boxes and taken to countries where labor is cheap to be opened and processed. But the whole operation costs quite a bit: the last figure I heard was that it is more than $1 per bill.


To us Internet wise-guys, that’s a joke. “Email me my bill”, you say. “I’ll pay it online!” You say. “It’ll only cost, say, 1/100000th of a penny. You’ll save *millions*” Or something like that.


And you’re right. So a lot of companies have tried to get into this field, which is technically known as *Bill Presentment*. One example is (guess who) Microsoft. Their solution, [TransPoint](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=514&ixReplies=2), looks like this: it’s a web site. You go there, and it shows you your bills. You pay them.


So, now, if you get your bills on this Microsoft system, you have to visit the web page every few days to see if any bills have arrived so you don’t miss them. If you get, say, 10 bills a month, this might not be too big a hassle. Therein lies the other problem: there are only a small handful of merchants that will bill you over this system. So for all your other bills, you’ll have to go elsewhere.


End result? It’s not worth it. I would be surprised if 10,000 people are using this system. Now, Microsoft has to go to merchants and say, “bill your customers over our system!” And the merchants will say, “OK! How much will it cost?” And Microsoft will say, “50 cents! But it’s a lot cheaper than $1!” And the merchants will say, “OK. Anything else?” And Microsoft will say, “Oh yes, it will cost you about $250,000 to set up the software, connect our systems to your systems, and get everything working.”


And since Microsoft has so few dang users on this system, it’s hard to imagine why anyone would pay $250,000 to save 50 cents on 37 users. Aha! The chicken and egg problem has reared its ugly head! Customers won’t show up until you have merchants, and merchants won’t show up until you have customers! Eventually, Microsoft is just going to spend their way out of this predicament. For smaller companies, that’s not an option. So what can you do?


Software platforms actually gives us some nice hints as to how to roast your chicken and egg problem. Let’s look a bit at the history of personal computer software platforms in the years since the IBM-PC came out; maybe we’ll discover something!


Most people think that the IBM-PC required PC-DOS. Not true. When the IBM-PC first came out, you had a choice of three operating systems: PC-DOS, XENIX (a wimpy 8 bit version of UNIX published by, and I am not making this up, Microsoft), and something called [UCSD P-System](http://www.threedee.com/jcm/psystem/), which was, if you can believe this, just like Java: nice, slow, portable bytecodes, about 20 years before Java.


Now, most people have never heard of XENIX or UCSD’s weirdo stuff. You kids today probably think that this is because Microsoft took over the market for dinky operating systems through marketing muscle or something. Absolutely not true; Microsoft was tiny in those days. The company with the marketing muscle was Digital Research, which had a different operating system.  So, why was PC-DOS the winner of the three way race?


Before the PC, the only real operating system you could get was CP/M, although the market for CP/M based computers, which cost about $10,000, was too small. They were cranky and expensive and not very user friendly. But those who did buy them, did so to use as word processors, because you could get a pretty good word processor called WordStar for CP/M, and the Apple II just could *not* do word processing (it didn’t have lower case, to begin with).


Now, here’s a little known fact: even DOS 1.0 was designed with a CP/M backwards compatibility mode *built in*. Not only did it have its own spiffy new programming interface, known to hard core programmers as INT 21, but it fully supported the old CP/M programming interface. It could *almost *run CP/M software. In fact,  WordStar was ported to DOS by changing *one single byte* in the code. (Real Programmers can tell you what that byte was, I’ve long since forgotten).


That bears mentioning again. WordStar was ported to DOS by changing *one single byte* in the code.  Let that sink in.


There.


Got it?


DOS was popular *because it had software from day one*. And it had software because Tim Paterson had thought to include a CP/M compatibility feature in it, because way back in the dark ages somebody was smart about chicken and egg problems.


Fast forward. In the entire *history* of the PC platform, there have only been two major paradigm shifts that took along almost every PC user: we all switched to Windows 3.x, and then we all switched to Windows 95. Only a tiny number of people ever switched to anything else on the way. Microsoft conspiracy to take over the world? Fine, you’re welcome to think that. I think it’s for another, more interesting reason, which just comes back to the chicken and the egg.


*We all switched to Windows 3.x*. The important clue in that sentence is the *3*. Why didn’t we all switch to Windows 1.0? Or Windows 2.0?  Or Windows 286 or Windows 386 which followed? Is it because it takes Microsoft five releases to “get it right”? **No.**


The actual reason was even more subtle than that, and it has to do with a very arcane hardware features that first showed up on the Intel 80386 chip which Windows 3.0 required.

- Feature one: old DOS programs put things on the screen by writing directly to memory locations which corresponded to character cells on the screen. This was the only way to do output fast enough to make your program look good. But Windows ran in graphics mode. On older Intel chips, the Microsoft engineers had no choice but to flip into full screen mode when they were running DOS programs. But on the 80386, they could set up virtual memory blocks and set interrupts so that the operating system was *notified *whenever a program tried to write to screen memory. Windows could then write the equivalent text into a graphical window on the screen instantly.
- Feature two: old DOS programs assumed they had the run of the chip. As a result, they didn’t play well together. But the Intel 80386 had the ability to create “virtual” PCs, each of them acting like a complete 8086, so old PC programs could pretend like they had the computer to themselves, even while other programs were running and, themselves, pretending they had the whole computer to themselves.


So **Windows 3.x on Intel 80386s was the first version that could run multiple DOS programs respectably.** (Technically, Windows 386 could too, but 80386s were rare and expensive until about the time that Windows 3.0 came out.) Windows 3.0 was the first version that could actually do a reasonable job running all your old software.


Windows 95? No problem. Nice new 32 bit API, but it still ran old 16 bit software perfectly. Microsoft obsessed about this, spending a big chunk of change testing every old program they could find with Windows 95. Jon Ross, who wrote the original version of SimCity for Windows 3.x, told me that he accidentally left a bug in SimCity where he read memory that he had just freed. Yep. It worked fine on Windows 3.x, because the memory never went anywhere. Here’s the amazing part: On beta versions of Windows 95, SimCity wasn’t working in testing. Microsoft tracked down the bug and *added specific code to Windows 95 that looks for SimCity*. If it finds SimCity running, it runs the memory allocator in a special mode that doesn’t free memory right away. That’s the kind of obsession with backward compatibility that made people willing to upgrade to Windows 95.


You should be starting to get some ideas about how to break the chicken and egg problem: provide a backwards compatibility mode which either delivers a truckload of chickens, or a truckload of eggs, depending on how you look at it, and sit back and rake in the bucks.


Ah. Now back to bill presentment. Remember bill presentment? The chicken-egg problem is that you can only get your Con Ed bills, so you won’t use the service. How can you solve it? Microsoft couldn’t figure it out. PayMyBills.com (and a half dozen other Silicon Valley startups) all figured it out at the same time. You provide a *backwards compatibility mode*: if the merchant won’t support the system, just get the merchant to mail their damn paper bills to University Avenue, in Palo Alto, where a bunch of actual human beings will open them and scan them in. Now you can get *all* your bills on their web site. Since every merchant on earth is available on the system, customers are happy to use it, even if it is running in this weird backwards compatibility mode where stupid Visa member banks send the bill electronically to a printer, print it out on paper, stuff it in an envelope, ship it 1500 miles to California, where it is cut open, the stupid flyers harping worthless “free” AM clock radios that actually cost $9.95 are thrown into a landfill somewhere, and the paper bill is scanned back into a computer and stuck up on the web where it should have been sent in the first place. But the stupid backwards compatibility mode will eventually go away, because PayMyBills.com, unlike Microsoft, can actually get customers to use their system, so pretty soon they’ll be able to go to the stupid Visa member banks and say, “hey, I’ve got 93,400 of your customers. Why don’t you save yourselves $93,400 each month with a direct wire connection to me?” And suddenly PayMyBills.com is very profitable while Microsoft is still struggling to sign up their second electric utility, maybe one serving Georgia would be a nice change of pace.


Companies that fail to recognize the Chicken and Egg problem can be thought of as *boil the ocean* companies: their business plan requires 93,000,000 humans to cooperate with their crazy business scheme before it actually works. One of the most outrageously stupid ideas I ever encountered was called [ActiveNames](http://www.directmag.com/ar/marketing_activenames_shutters_business/). Their boneheaded idea was that everybody in the world would install a little add-in to their email client which looked up people’s names on their central servers to get the actual email address. Then instead of telling people that your email address is kermit@sesame-street.com, you would tell them that your ActiveName is “spolsky”, and if they want to email you, they need to install this special software. Bzzzzzt. Wrong answer. I can’t even *begin *to list all the reasons this idea is never going to work.


Conclusion: if you’re in a market with a chicken and egg problem, you *better *have a backwards-compatibility answer that dissolves the problem, or it’s going to take you a loooong time to get going (like, forever).


There are a lot of other companies that recognized the chicken and egg problem face on and defeated it intelligently. When [Transmeta](http://www.transmeta.com/) unveiled their new CPU, it was the first time in a *long* time that a company that was *not* Intel finally admitted that if you’re a CPU, and you want a zillion people to buy you, you gotta run x86 code. This after Hitachi, Motorola, IBM, MIPS, National Semiconductor, and who knows how many other companies deceived themselves into thinking that they had the right to invent a new instruction set. The Transmeta architecture assumes from day one that any business plan that calls for making a computer that doesn’t run Excel is just not going anywhere.
