---
title: "Harry Potter And The Cryptocurrency of Stars"
date: 2014-08-05
url: https://www.kalzumeus.com/2014/08/05/harry-potter-and-the-cryptocurrency-of-stars/
slug: harry-potter-and-the-cryptocurrency-of-stars
word_count: 6045
---


If you’re wondering why my blog suddenly has Harry Potter fanfic click this to show the spoiler otherwise it might be more fun to dive right in.

Recently, a new cryptocurrency called
[Stellar](http://www.stellar.org)
was announced.  This happens on a daily basis these days, and the vast majority of them amount to nothing.  Stellar, on the other hand, is
[backed by Stripe](https://stripe.com/blog/stellar)
(among a host of Silicon Valley bigwigs), designed to fix some issues with Bitcoin (a system/asset/community/engineering artifact/etc of which I am a
[notorious critic](http://hn.algolia.com/#!/comment/forever/prefix/0/author%3Apatio11%20bitcoin)
), and appears to be a protocol for value exchange which happens to include a novel asset to be used in a self-organizing distributed boiler room rather than the other way around.</p>

So I thought it was worth understanding how Stellar works, at the protocol level. It turned out to be easier to explain with a story than a code sample.


With apologies to J.K. Rowling, here we go:


## What Is Value, Anyway?


**Goblin Banker**: So, young Master Potter, I understand that these last few days have been a bit trying for you, but on the upside, you’re filthy stinking rich.


**Harry Potter**: I’m still having trouble wrapping my head around piles and piles of gold coins in a vault guarded by a dragon.  What did you call them again?


**Goblin Banker**: Galleons.


**Harry Potter**: And weren’t there Sickles and Knuts, too?


**Goblin Banker**: Meaningless complications for the moment, sir.  Let’s just focus on your galleons.


**Harry Potter**: What is a galleon worth, anyway?


**Goblin Banker**: What is anything *worth*, young Master Potter?  An apple or a dragon’s egg or the limb of an ancient yew severed in a lightning strike?  All things are worth what someone will happily trade you for them.


**Harry Potter**: I’m having trouble thinking that gold is really like an apple.  Surely it is worth much more, right?


**Goblin Banker**: I suppose that depends.  If you’re starving, an apple will save your life and gold won’t.  But we aren’t talking about gold, we’re talking about galleons.


**Harry Potter**:  Galleons are gold, right?


**Goblin Banker**: Galleons are a currency, Master Potter.  They happen to have a bit of gold in them, to be true, but the real magic of them — a strikingly ordinary kind of magic — is that the inhabitants of Wizarding Britain *want to have them* and, accordingly, you can trade for almost anything if you have enough galleons.  And, as we’ve established, you have enough galleons.


**Harry Potter**: Carrying that mountain of gold around is going to be trouble.  I need to go buy supplies for Hogwarts!


**Goblin Banker**: Not to worry, sir.  We have much more convenient ways of dealing with currencies than you might be used to in the Muggle world.  There’s none of this nonsense with carrying large amounts of money on your person and physically handing them to other people.


**Harry Potter**: Oh, you have a debit card which lets me withdraw galleons?  Maybe a Visa, accepted everywhere I could want to spend them?


**Goblin Banker:** OK, OK, I take your point, Muggles have progressed a wee bit over the years.  In the wizarding world, though, we use cryptocurrencies.


**Harry Potter**: Crypto-what?


**Goblin Banker**: Math math math, blah blah blah, suffice it to say that it’s magic which you have no need to understand but which allows you to conveniently exchange value without needing to physically hand over golden tokens to your counterparty.


**Harry Potter**: So I… buy this crypter-currency with galleons?  And then I hand it over to the shop?


## In Which Harry Potter Discovers Debt, A Mysterious And Powerful Magic


**Goblin Banker**: Hmm…  young Master Potter, have you ever heard of the phrase “IOU”?


**Harry Potter**: Of course.


**Goblin Banker**: Think of cryptocurrency more as an IOU that you can conveniently trade to people.  For example, do you trust us here at Gringotts?


**Harry Potter**: Well, you seem to have just showed me a mountain of gold when you could just as easily have taken me to an empty room and I would have been none the wiser, so I suppose I do trust you.


**Goblin Banker**: Words are important in this world, young Master Potter.  Put your right hand on this ledgerbook and say “I trust Gringotts…”


**Harry Potter**: “I trust Gringotts…”


**Goblin Banker**: “… to the sum of 100,000 galleons.”


**Harry Potter**: “To the sum of 100,000 galleons.”


**The Ledgerbook**: Welcome to Gringotts, young Master Potter.  Your current balance is: nothing.


**Harry Potter**: Great Scotts, it’s magic!  So now I have 100,000 galleons?


**Goblin Banker**: No, you have a vault full of galleons, but the ledgerbook and all of Wizarding Britain just witnessed the fact that you trust us to give you an IOU worth anything up to 100,000 galleons.


**Harry Potter**: Why can’t I just trust you with… all the galleons?


**Goblin Banker**: No one is worth unlimited trust, young Master Potter, not even a goblin.


Here, let’s get you set up with some walking around money.  One hundred galleons should be plenty for the moment, so I’ll send a runner down to the vault to take out 100 physical galleons, which we’ll keep, and issue you an IOU.  You, or anyone else, can bring the IOU back to Gringotts, and we’ll give that person back 100 physical galleons.  Sound fair?


**Harry Potter**: Certainly.


**Goblin Banker**: Ledgerbook, send 100 galleons to Harry Potter.


**Ledgerbook**: Young Master Potter, your current balance is: 100 Gringotts galleons.


**Harry Potter**: Oh, you *make* the galleons here at Gringotts?


**Goblin Banker**: Well, in point of fact we do, but it is called a “Gringotts galleon” because we issued the IOU, not because we issued the underlying asset.  Don’t worry about it for now.


## Debts Which Are Transferable Enable Transactions


*some time later*


**Ron Weasley**: Funny that three first-year Hogwarts students happened to bump into each other while doing shopping, isn’t it?


**Hermione Granger**: That’s so convenient for teaching Harry here about wizard commerce, it’s like Diagon Alley is the Room of Requirement.


**Harry and Ron**: What?


**Hermione Granger**: Clearly you two are going to be the best of friends.  Oh look, here we are, Olivander’s Wand Shop.  You’ll want a wand.


**Olivander**: A wand chooses the wizard, my boy!  Oh look, this one here with a phoenix feather core is practically singing to you.  It is a steal at only ten galleons.


**Hermione Granger**: Did you say a phoenix feather?  Where have I read about that before?


**Olivander**: Eight galleons then!  Seven if Little Miss Know-It-All never says another word while I’m negotiating with a customer!


**Harry Potter**: Easy, easy, I just want a wand so that I can do magic.  Seven galleons sounds like a fair offer.  Umm, where’s your ledgerbook?


**Olivander**: Goblins use the ledgerbook directly, but carrying around one with you all the time would be dreadfully inconvenient just to spend money.  I mean, think of how heavy it would be.


**Hermione Granger**: Gigabytes at the very least.  And if it were sustaining hundreds of transactions per second like Visa and each person needed their own copy of the ledgerbook then very soon ledgerbooks would represent a significant fraction of all disk space in the United Kingdom.  That’s clearly not sustainable.


**Ron Weasley**: What’s a gigabyte?


**Hermione Granger**: Your ignorance is wearying and yet strangely adorable.


**Olivander**: So instead of ledgerbooks, you just wave your wand and send a message to the world via a magic spell.  Here, Mister Potter, repeat after me: slight flick of wrist, “*Stellarmus,* send Olivander seven galleons.”


**Harry Potter**: Stellar-what?


**Olivander**: Stellar sounds nice and happened to have a domain name available. *Stellarmus* because Hogwart’s last Latin teacher got eaten by a troll four hundred years ago and they haven’t replaced him since.


**Harry Potter**: Alright.  Stellarmus, send Olivander seven galleons.


**Olivander**: … Great.  A pleasure doing business with you.  Please remember to bring your kids back in thirty years — you won’t believe how hard it is keeping a wand shop in business, what with it being a once-in-a-lifetime purchase which costs trivial bits of money.


**Harry Potter**: What just happened?


**Hermione Granger**: A minute ago, Gringotts owed you 100 galleons.  Mr. Olliver here trusts Gringotts IOUs much like you do.  You’ll find that is quite common in Wizarding Britain.  You told Stellarmus to send him seven galleons, so it transferred seven galleons of your Gringotts IOU to him.


**Ron Weasley**: So he can pop down to Gringotts and get himself some gold, any time he wants.


**Hermione Granger**: Or he could just Stellarmus it to anyone else who trusts Gringotts without having to actually withdraw the galleons.


**Ron Weasley**: Right, or that, I suppose.  Right then, I guess we’ll just wait around here.


**Harry Potter**: I have my wand, he has his galleons, what is there to wait for?


**Ron Weasley**: Well, shouldn’t transferring money take a while?


**Hermione Granger**: Some cryptocurrencies require you to wait while mysterious wizards called “miners” run hundreds of billions of magical maths spells, called a proof of work, to make sure no one is tampering with the block chain.  One block appears roughly every ten minutes and a transaction needs to have been included in a block at least six deep to be settled.  If we had settled this transaction with one of those cryptocurrencies, Mr. Ollivander couldn’t be sure we had paid him for about an hour, although that is just an approximation based on probabilistic reasoning and observed features of the protocol rather than anything deterministic.


**Harry Potter**: That sounds dreadfully inconvenient.


**Hermione Granger**: And it would be, but Stellarmus doesn’t use a proof of work system, it uses an iterative consensus algorithm, so confirmations are almost instant — closer to “a slow remote API request” than anything involving a blockchain.  No mining happens and there is no duplicative work performed worldwide in the hopes of getting seigniorage.


**Ron Weasley**: I don’t think I understood a single word in that explanation.


**Harry Potter**: Me neither.


**Hermione Granger**: Promise me you won’t talk to the Defense Against the Dark Arts Professor and you’ll never have to care about that.


## Walking The Web Of Trusted Currencies


**Ron Weasley**: I’m famished.  Let’s drop by Muggle London for some chips.


**Harry Potter**: Great idea.


**Ron Weasley**: How do you people in Muggle Britain pay for things again?


**Harry Potter**: Well, since we’re children, typically that would be by handing over paper money.


**Ron Weasley**: That sounds dreadful.  Just Stellarmus them some galleons.


**Hermione Granger**: Wizards have this funny prejudice against Muggle financial instruments but they have the desirable property of *actually working*.  And you can’t Stellarmus galleons to a Muggle — he isn’t connected to the Stellarmus network and, even if he were, it would be *his choice* to accept galleons or not.


**Harry Potter**: No problem, mate, I’ll spot you.  Here, one plate of chips.  Get me back for a quid when you’ve got one, OK?


**Ron Weasley**: What’s a quid?


**Hermione Granger**: Quid, noun, British slang for one pound sterling.


**Ron Weasley**: What’s a pound sterling?


**Hermione Granger**: It’s like a galleon except used by Muggles.  Harry just paid using a pound note, written on paper.


**Ron Weasley**: Paper?!  Not gold?


**Harry Potter**: What’s it matter?  It bought you chips, didn’t it.  Everything is worth what someone will give you for it, or something.  A goblin told me that.


**Ron Weasley**: But couldn’t they just print more paper?


**Harry Potter**: Yep.  That’s sort of the point of paper.


**Ron Weasley**: But couldn’t they just print an unimaginably gigantic stack of paper and then all of the paper would be worthless and you’d have to carry around wheelbarrows of it to buy chips?


**Hermione Granger**: You *have* been talking to the Defense Professor, haven’t you?


**Harry Potter**: I guess we just have to trust they don’t do that.  Anyhow, you owe me a quid.


**Ron Weasley**: I don’t have a quid.


**Harry Potter**: No worries, I know you’re good for it.


**Hermione Granger**: You could make that official, you know.


**Harry and Ron**: What?


**Hermione Granger**: Well, since you trust Ron up to one pound, just tell Stellarmus.  Then Ron can send you an IOU for a pound.


**Harry**: Stellarmus, I trust Ron Weasley for one quid… that’s strange, nothing happened.


**Hermione Granger**: You have to say what kind of Great British pound you trust him for.  A pound isn’t just a pound and a galleon isn’t just a galleon.  A Gringotts galleon is useful to buy things from people because people trust Gringotts to actually have galleons when they ask for them.  You wouldn’t get very far if all you had were Weasley galleons.


**Ron Weasley**: Hey!


**Hermione Granger**: Sorry Ron, facts are facts.  Gringotts is widely known to be reputable.  The Weasley family doesn’t have that reputation and, as a result, currently absolutely no one trusts anyone else for a Weasley!GAL.


**Ron Weasley**: A what?


**Hermione Granger**: The mid-word exclamation point is a notation sometimes used in fanfiction to distinguish two things that, since they appear in radically different circumstances, might be quite different even though they have similar names.  The part before the exclamation point is the name of the gateway — the person ultimately responsible for turning real-life things into IOUs and IOUs back into real-life things — and the part after is the currency.


**Harry Potter**: Fanfiction?  You’re such a nerd.


**Hermione Granger**: You’re rich in cryptocurrencies, so glass houses and etcetera.  Anyhow, GAL is the three-letter symbol for galleons just like GBP is for pounds.


**Ron Weasley**: Do they have to be three letters?


**Hermione Granger**: Wow, that’s the first intelligent thought I’ve heard from you.  So I suppose that’s just a rather strange limitation in the Stellarmus spell which comes from us traditionally using three-letter symbols to represent currencies issued by nations.  Naturally, that’s far from the only kind of currency these days.


**Harry Potter**: Alright, let me try again:  Stellarmus, I trust Ron Weasley with one Weasley!GBP.


**Ron Weasley**: Stellarmus, send Harry Potter a quid!


**Hermione**: And there you go.  Harry now has an IOU from Ron for one pound, and Ron now owes Harry one pound.  It balances, just like double-entry accounting.


**Harry Potter**: That’s amazing!  Here, Hermione, go fetch us a soda.  Stellarmus, send Hermione a quid.


**Hermione Granger**: First off, you can fetch your own soda.  Second, that won’t work, because while you might trust this lummox with up to one pound, I don’t trust his pound IOUs at all.  To send me a pound, either you have to have a balance in pounds drawn on a gateway I trust, or you have to walk the trust graph to a currency and gateway pair that I do trust.


**Harry Potter**: Run that by me again?


**Hermione Granger**: Think of physical money.  That will make it simpler.  The chip shop only takes pounds.  You only have galleons, but you want chips.  You need to find someone who wants galleons and has pounds, trade galleons for pounds, and then pay pounds to the chip shop.


**Harry Potter**: So… I’d run out to a currency exchange.


**Hermione Granger**: Exactly.  But happily, that’s built into Stellarmus.  The wrinkle is that there is currently no path between the currency which you have, which is Weasley!GBP, and any currency that I accept.


**Harry Potter**: What currencies do you trust?


**Hermione Granger**: Ask Stellarmus.  They’re public knowledge.


**Harry Potter**: Stellarmus, what currencies does Hermione Granger accept?


*Stellarmus rattles off a long, long list.*


**Harry Potter**: What on earth is a Tokyo!ABL?


**Hermione Granger**: It’s a claim against an online Magic: The Gathering exchange headquartered in Tokyo for one Alpha Black Lotus, which is a card that I’ve wanted for a while.


**Ron Weasley**: You’d trust a random company in Tokyo to send you magic cards?


**Hermione Granger**: They’re not magic cards, they’re Magic cards, and yes, I’d trust that company to hold Magic cards for me.  Nothing else though.  It would certainly be dreadfully stupid to say “Stellarmus, I trust The Company That Must Not Be Named for 50 million USD.”


**Harry Potter**: Why do I get the feeling you know more about this topic than I do?


**Hermione Granger**: Welcome to life, Harry Potter.  I know more about every topic than you do.


**Ron Weasley**: Do you know how to have Harry send you a quid?


**Hermione Granger**: Sure.  At least one person has to make an offer which connects Weasley!GBP and anything I want.  Probably stellar.


**Ron Weasley**: Hang on, what’s a stellar?


**Hermione Granger**: Stellar is a convenience currency used by the Stellarmus network to assist people in making markets in currency/gateway to currency/gateway where they don’t have a convenient linkage between them.


**Ron Weasley**: Is a stellar gold or paper?


**Hermione Granger**: None of the above — it’s just a number.  Sort of like how a Weasley!GBP is just a number — after all, you have neither gold nor paper.  That doesn’t mean it isn’t real though.


**Ron Weasley**: Hang on a second — stellars?  I think one of my brothers gave me some once.


**Hermione Granger**: Alright then, one second while I phone a friend of mine who fancies herself something of a finance whiz.


**Cho Chang**: What’s up, Hermione?


**Hermione Granger**: There exists a counterparty trying to convince me to accept a GBP on an unreliable gateway and I’m not willing to take the counterparty risk, so I was wondering if you’d make an offer on Stellarmus to buy Weasley!GBP for stellar.


**Cho Chang**: Weasley!GBP?  Weasley as in “The Weasleys?”  Do I have to explain to you why nobody has made this market yet?


**Hermione Granger**: It’s only for one pound and I’m asking as a favor to teach a newbie how Stellarmus works.


**Cho Chang**: Alright, as a favor: Stellarmus, I offer to buy one Weasley!GBP in exchange for ten stellars.


**Hermione Granger**: That’s a *favor*?


**Cho Chang**: Counterparty risk, yo.  If your counterparty doesn’t like it, they can find another path through the trust graph to you.  Which, as we’ve established, doesn’t exist *for a reason*.


**Hermione Granger**: Alright, alright, thanks Cho.  Harry, if you were to try sending me a pound again you’d now be able to but…


**Harry Potter**: Stellarmus, send one GBP to Hermione Granger.


**Stellarmus**: We can’t find a path to send her GBP, but we can send her 10 Stellar at a cost of one GBP.  Does that work?


**Harry Potter**: Stellarmus, send 10 Stellar to Hermione Granger at the cost of one GBP.


**Stellarmus**: Done!


**Hermione Granger**: Have people ever told you to think before acting?  It is a useful skill in life.  While you’re taking time to do a bit of thinking, you might listen to people explaining important things to you.


**Harry Potter**: What?  You got a pound.


**Hermione Granger**: No.  Stellarmus might be magic but fundamentally it’s only an algorithm, and it just did exactly what you told it to.  It figured out a way to take one pound from you and transfer 10 stellar to me.


**Harry Potter**: So ten stellar to the quid, right?


**Hermione Granger**: So if I were to hypothetically use one of the more trusted GBP gateways in Wizarding Britain, the going rate is actually closer to 5,000 stellars to a pound.


**Harry and Ron**: WHAT?!  Why so many?


**Hermione Granger**:  Who cares how many it is?  Things are worth what people will give you for them.  The important bit is that you just transferred something which is actually worth about 1/500th what you think it is worth.  If we weren’t friends, it is highly unlikely that the transaction you wanted to have happen — to whit, me getting us sodas — would actually proceed as planned.


**Harry Potter**: So who has my quid?


**Hermione Granger**: Cho has *her* quid, more specifically, her Weasley!GBP.  It was only your Weasley!GBP until you told Stellarmus to figure out some way to transfer that value to me.


**Harry Potter**: Cho just cheated me!


**Hermione Granger**: Cho didn’t even *talk* to you, at any point.  She just told the world that she was willing to buy Weasley!GBP and as she has a worldwide monopoly on that poor life decision then she can name her own price for it.  You’re lucky she offered you ten, to be honest, because it requires her to be on the hook if Ron here fails to deliver.


**Ron Weasley**: Wait wait, so I owe Cho 1/500th of a quid?


**Hermione Granger**: See, this is what I mean about Ron being an unreliable counterparty, because he doesn’t understand what he’s agreed to do and might be considering defaulting on his obligations.  Before Harry sent his transaction, you owed one pound.  You still owe one pound.  You just owe it to Cho now.


**Harry Potter**: So if I’m hearing you right, I just tried to send you value, but lost a lot of it in the exchange.  What can I do to avoid having this happen in the future?


**Hermione Granger**: Well, for one thing, you could put your own offer out.  Something like “I will buy 1 Weasley!GBP for 0.2 Gringotts!GAL.”  Anybody could see you doing that and then decide to facilitate any Weasley!GBP transactions because they want Gringotts!GAL.


Or, in the alternative, Ron here could convince people that he was more trustworthy, because if people believe that a Weasley!GBP has value, and they tell Stellarmus that by attempting to buy it, then it actually has value.  Basically, you’d try to convince people to outbid Cho.


Or, you could just convince me to accept Weasley!GBP.


**Ron Weasley**: I like to think I’m a trustworthy guy.  I’m totally good for your Muggles weird paper-with-an-old-lady-who-doesn’t-even-move money.


**Hermione Granger**: I like you, Ron, but not enough to trust you with money.  Save my life a few times first and maybe we’ll talk.


**Harry Potter**: Should I buy stellars then?


**Hermione Granger**: I wouldn’t particularly recommend it.  There’s only two things you can do with them — power the Stellarmus spell, which uses so few as to not be worth mentioning, and use them as an intermediary currency when you’re trading currency/gateway pairs which don’t have a more direct connection to each other on the trust graph.  In the real world, most IOUs you’d actually want to own are issued by one of a number of highly-interconnected organizations bound together by strong pre-existing mutual trust.  It’s highly likely that in the overwhelming majority of transactions you don’t need an intermediary currency at all, you just play Seven (Or More, Or Less) Degrees To Gringotts Galleons, which is easy for you because Stellarmus does all the work.


**Ron Weasley:** But if you’re wrong, and I buy stellars while they’re still 5000 to a quid, and they later turn out to be valuable, can I get rich?


**Hermione Granger**: If you want to get rich, you should study hard in school and create something of value.


**Harry Potter**: Or find out that, surprise, mum and dad were secretly loaded and have left it all to you.


**Hermione Granger**: You, sir, are a terrible role model.


**Ron Weasley**: Where did your folks get all that money, anyway?


**Harry Potter**: I don’t know mate, I don’t know.


## A Choice Of Evils


*later that year*


**Defense Professor**: Hello, students.  I’m the new Defense Against The Dark Arts professor.


**Harry Potter**: Pleased to meet you sir.  I’m Harry, this is Ron and Hermione.  What’s your name?


**Defense Professor**: We have too high a turnover to be given names.  Besides, I prefer to be anonymous.  Can’t be too sure who is watching.


**Hermione Granger** (whispering): Harry, first rule of wizarding: never trust the Defense Professor.


**Defense Professor**: Stellarmus, ten Hogwarts House points for Gryffindor.


**Harry Potter**: OK, now you’re just pulling my leg.  Hogwarts House points aren’t even a thing, and Gryffindor isn’t even a person.


**Hermione Granger**: Check Stellarmus, Harry.  Accounts don’t necessarily have to be people — they could be a person, or a House, or a company, or one of many accounts controlled by anyone who possesses the right magic words.


**Harry Potter**: Stellarmus, info on account Gryffindor.


**Stellarmus**: House Gryffindor has a balance of: ten Hogwarts Professor Hogwarts House points.


**Ron Weasley**: It’s that easy!?  Stellarmus, 10 points for Gryffindor!  … Why didn’t that work?  Stellarmus, 10 points for Harry!  That didn’t work either?!


**Defense Professor**: In the first place, House Gryffindor only trusts Hogwarts Professors, of which I am one, to be the issuers of Hogwarts House Points which it accepts.  In the second place, even if you got Harry to accept Hogwarts House Points from you, which would be a terrible decision of the type you both seem to love, the real-world decisionmaking only uses genuine Hogwarts Professor Hogwarts House points.  All other Hogwarts House points are meaningless forgeries.  It’s our own private currency, and even if you could possibly issue it, which you can’t, nobody except our pre-authorized participants can possess it.  That would be the four Hogwarts Houses.


**Hermione Granger**: That bit is important, because it lets gateways choose to restrict who they do business with.  For example, if your jurisdiction requires you to comply with Know Your Customer or anti-moneylaundering requirements, then you might not want to let people transfer your IOUs to pseudonymous identities on the Internet.  You’d require that people show up at the bank and prove their identity prior to giving their account the capability to hold your IOUs.


**Harry Potter**: Well, on the plus side, all this security means that nobody can take points away from Gryffindor.


**Defense Professor**: Stellarmus, in my capacity as keyholder for Gryffindor, five points from Gryffindor.  This is, as we say in teaching, an object lesson.


**Ron Weasley**: What just happened?!


**Hermione Granger**: The Defense Professor isn’t just the Defense Professor.  He can also act to control any accounts whose magic words he knows.  He knows the magic words for House Gryffindor’s account, presumably because the Hogwarts faculty are a closed system of mutually high-trust peers, and so he can direct their accounts to do anything.


**Harry Potter**: Wait, why do Hogwarts faculty trust the Defense Professor when the first rule of wizardry is “Don’t trust the Defense Professor?”


**Defense Professor**: Because the Hogwarts faculty are fools.  Trust is for the weak, anyhow.  The only *real* currency is a totally trustless currency.


**Hermione Granger**: Oh no, you did it.  Now we’re going to get the lecture.


**Defense Professor**: The problem with fiat currencies is that they can just be conjured into being.  And you know who does the conjuring?  *Banks*.  *Governments*!  Pah on all of them — anyone who trusts goblins or Muggles or civil servants is stupid and deserves what happens to them.  And what will happen to them is *ruin*.


**Ron Weasley**: Well banks sound fairly trustworthy, Professor…


**Defense Professor**: Don’t you understand, Weasley?  Gringotts is just a jumped up version of you — and how you convinced anyone to accept a currency you just *asserted the existence of* I’ll never know — they’re able to control the M1 money supply via fractional-reserve banking and …


**Hermione Granger**: Those words don’t mean what you think they mean.


**Defense Professor**: Stellarmus, five points from Gryffindor, for interrupting a monologue.  As I was saying, you need to have a fixed money supply, something that the banksters and goblins can’t inflate away the value of, and you need to be able to transfer hard assets, not debts which will ultimately be defaulted on.


**Harry Potter**: So you want something like gold?


**Defense Professor**: Not something like gold, Potter, something *better* than gold.  You can’t send gold to China in a second or carry enough gold to buy a castle in your head.  No, I mean cryptocurrency.


**Ron Weasley**: I remember that word.  You mean like stellar.


**Defense Professor:** A worthless pre-mined altcoin!  No, I mean the original cryptocurrency, the one with the most defensible network, the one whose initial distribution went to followers of a genius rather than people chosen at random from the Daily Prophet’s social network!  I mean…


**Hermione Granger**: The Cryptocurrency That Cannot Be Named.


**Defense Professor**: To speak its name is to invoke powers behind your first-year’s comprehensions.  What do you know of the blockchain?


**Harry Potter**: Math math math, blah blah blah?


**Defense Professor**: The blockchain is the most important technological advance since the Internet.  Possibly, in the history of the human race.


**Hermione Granger**: Stellarmus owes a lot to the underlying ideas of it, actually.


**Defense Professor**: Speak not of your little toy.  Real cryptocurrency is raw power.  Controlled by no one and responsible to everyone, it will forever change how finance is conducted.


**Hermione Granger**: You’ve used Stellarmus.


**Defense Professor**: Yes, but like most people, I use it like a toy.  The total market value of real cryptocurrency is worth billions of whatever your favorite illusionary “fiat” currency is.  *Billions*.


**Hermione Granger**: Hmm, OK, when you’re right you’re right: your network does have massively more adoption than my network.


**Defense Professor**: Right, and no currency network will ever, ever be more adopted than my network.  Currency is the strongest network effects business.


**Harry Potter**: Err, Professor, don’t the Muggles’ currencies count as a network, too?  I mean, you can send them by computer, and they have *individual buildings* which are worth more than all cryptocurrencies put together.  In addition to that being, um, disproof by counterexample, even if the networks effect argument were true, wouldn’t that have been an insurmountable barrier against the success of your own network, which you appear to think is succeeding?


**Hermione Granger**: The boys are, apparently, not *entirely* incapable of learning.


**Defense Professor**: A fat lot of good those buildings will do them when their civilization crumbles due to currency collapse because they trusted the wrong people!  I trust only math!


**Hermione Granger**: That’s all well and good within the network, but even for true followers, you generally aren’t paid in math and you can’t live only on math.


**Defense Professor**: A temporary problem.  It will be better after we seize power.


**Hermione Granger**: But in 2014, what do you do?


**Defense Professor**: …  I’ve been known to trade worthless fiat currencies for The One True Currency.  It’s no different than any other purchase, except I’m totally in control.


**Hermione Granger**: How was the trip to the creditor’s meeting in Tokyo?


**Defense Professor**: Your smugness is insufferable.


*People* who trusted that institution deserve what they got for trusting anyone.  This just reinforces the need for a trustless currency.  Not like stellars, which is built on a foundation of trust for centralized authorities.


**Harry Potter**: That’s true, isn’t it?  I mean, I say I trust Gringotts, but what happens if they go under?


**Hermione Granger**: That’s out of scope for Stellarmus.  I suppose you’d hope that Gringotts is a regulated bank in Wizarding Britain and that the Ministry of Magic would make you whole.


**Defense Professor**: Pah, the Ministry of Magic.  Quite possibly the only thing I trust less than a goblin.  While we’re on the subject of trust, Granger, why don’t you explain to the boys here what “trusting the network” means?


**Hermione Granger**: So in any distributed system you need some way to get everyone on the same page about what reality is right now.  Consistency, availability, partition tolerance: pick any two.  The Defense Professor’s cryptocurrency does this in a trustless fashion — no matter how many peers lie to you, as long as there is at least one peer who is truthful, you learn the true (consistent) state of reality.


**Defense Professor**: The truth will set you free.


**Hermione Granger**: Unless, of course, sufficient miners conspire against you, in which case they can retroactively overwrite reality at will.  You have to trust them not to do that.


**Defense Professor**:  You don’t have to trust their intentions, you just have to verify that the protocol is incentive compatible.  It would cost far more value for them to conspire against you than they would capture from that action, while collaborating with you is simple and generates more value for them.  So how do you trust *your* network?


**Hermione Granger**: Well, I seed it with trusted peers — like Hogwarts, Gringotts, and the Ministry of Magic — and then they vote on reality.  As long as they don’t *all* decide to tell me *the same* lie, I always get the truth from them.


**Defense Professor**: Granger is, of course, trusting that The Adversary never controls Hogwarts, Gringotts, and the Ministry of Magic at the same time.


**Ron Weasley**: That seems pretty reasonable, though.


**Defense Professor**: You think a far-reaching conspiracy can’t simultaneously capture all your trusted institutions?  I love the young and naive.


**Hermione Granger**: Well, while it doesn’t look like we’re going to settle this argument anytime soon, I have a suggestion.  You like a particular cryptocurrency.  I like stellars.  Trade?


**Defense Professor**: You go first.  I will never trust Stellarmus with a currency that I actually value.


**Hermione Granger**: Well, since we’ve established that you use exchanges — even while pinching your nose — if one of them happens to run a Stellarmus gateway, through the Stellarmus network we can find a path between one of my cryptocurrency balances and the exchange you tr… do business with, transfer them a cryptocurrency IOU, and tell them out-of-band to redeem it to you.  They’ll compensate me for the cryptocurrency.  What’s your favorite exchange?


**Defense Professor**: Alright, I’ll name one *very quietly*.


**Hermione Granger**: Great, as it happens, I already trust that one.  That makes it really easy — Stellarmus, I offer to sell a… you know… for five ChoChang!JPY.  And done.  The exchange will take care of settling up with you, off the Stellarmus network.


**Defense Professor**: Wait, what?!  That was at a gigantic discount to their present value.


**Hermione Granger**: Well, we’ve established that I don’t want that asset anywhere near as much as you seem to.


**Defense Professor**: Would you do that trade again?


**Hermione Granger:** Maybe, but there’s no liquidity for it at the moment.  I could put out an order for it now but your favorite currency bounces around all the time and I don’t want it going all the way to zero when I don’t have my eyes on the wand.


**Defense Professor**: At that price I will be your counterparty!  One second.


By the eldritch rites of Satoshi, transfer to my exchange’s account three infinitely divisible currency units.  I’ll bounce a fraction of them off your toy network into something that the Stellarmus spell will trade for a ChoChang!JPY, swap that for a cryptocurrency with actual value, and turn you into a value pump.


**Harry Potter**: I’m not feeling like anything is happening.


**Defense Professor**: Give me an hour or so to wait for confirmations and then this is ***totally on***.


## Author Notes


Have I mentioned that I don’t like Bitcoin?  I don’t like Bitcoin.  I’ve been working on a one-stop-shop explanation of why I don’t like Bitcoin, but haven’t posted it yet.  Check back here on the blog if it interests you.


While I don’t like Bitcoin, I tried to be fair to the technical reality of it.  To the best of my knowledge, no character in the above story ever tells a direct lie.


Do I like Stellar?  Too early to tell.  I haven’t really dug into it as an engineering artifact.  The embryonic ecosystem does not yet have any tangible economic value.  (And the Bitcoin ecosystem?  *whistles*)  Suffice it to say that at the moment it looks like a very interesting proposal for something that may some day be a toy, and some people I trust believe the toy may eventually be more than a toy, but I have no particular reason to believe or disbelieve that that will be the case yet.


Financial disclaimer: I hold no position in Bitcoin (though if it were conveniently possible, I’d hold a position best characterized by “long on far-dated far-out-of-the-money BTC puts, with a personally substantial chunk of money at risk”).  I participated in the free Stellar giveaway out of technical interest, but gave substantially all the stellar I received to [Watsi](http://www.watsi.org).  (I tried to give all of them but technical limitations prohibit that at the moment.)
