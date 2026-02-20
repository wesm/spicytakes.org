---
title: "Everything You Need To Know About Registration Systems"
date: 2006-09-04
url: https://www.kalzumeus.com/2006/09/05/everything-you-need-to-know-about-registration-systems/
slug: everything-you-need-to-know-about-registration-systems
word_count: 2724
---


… but were afraid to ask.


One of the most common questions asked on the Business of Software board by a new aspiring uISV is “How do I protect my software?” This post is meant to be a comprehensive answer to that question, so folks can point to it and say “Alright, now get out of my hair!”. Kidding, kidding, we were all there once.


First, a brief discussion on why you want to protect your software. The only reason you want to protect your software is to enforce the [limitations you have put on the trial version](http://microisvjournal.wordpress.com/2006/08/16/to-limit-or-not-to-limit/). Many people mistakenly come to the table with the assumption that protecting the software will somehow, magically, “protect my intellectual property” or something to that effect. This might be theoretically true but you will have an easier time conceptualizing your registration scheme if you think of it as primarily a marketing, rather than technical, measure. Its your salesman that encourages folks to pay you money.


Why is it important to remember your registration scheme is a salesman? Because salesmen do not typically kick their prospective customers where the sun doesn’t shine, and many registration schemes do. Aside from some clubs in Tokyo (and the less you know about them, the better, really), people generally don’t pay money for the privilege of being kicked. Yet many software developers keep including Nutcracker Suite protection systems, such as [Starforce](http://www.star-force.com/), which severely harm the user experience, out of the mistaken belief that this will eventually increase profits.


If you will permit be a bit of amateur psychoanalysis, I think this is because software developers in general, and uISVs in particular, feel *violated* when someone is using their software illegally. I know the feeling, it has happened to me (and, mark my words, it *will* happen to you). Someone who downloads your software and cracks it hasn’t cost you any more money than someone who picks your door and walks around your apartment for 20 minutes without touching anything, yet the feeling that your rights have been violated is the same. And perhaps in a fit of less-than-rational anger you might demand your apartment upgrade its security system to include dead-locks, pitbulls, a batallion of US Marines with shoot-to-kill-orders, and some cleverly disguised booby-traps involving acid or flaming oil, or perhaps just flaming acid. Of course, the local Girl Scout troop selling cookies will probably not react too well to the fortifications (aside from the “cute wittle puppy!”), so if you like having cookies delivered to your door this is probably not a good idea.


So lets talk about four classes of users and how they interact with your registration scheme.


The first type of user is perfectly honest and will always comply with your licensing scheme to the letter, even if ways to circumvent your registration scheme are obvious. Approximately everyone thinks they are this kind of user. To this kind of user, your registration scheme (a salesman for your software) can be only a hindrance in getting to use the software which he happily paid for.


The second type of user is *mostly* honest. He’s not a pirate, after all, he has a wife and kids and works at an insurance company. He scoffs at the kids on Napster who feel entitled to free music. And yet he also will happily buy one license of your software when your license tells him he really requires five, install and uninstall a time-limited trial version every two weeks, and perhaps even reset his system clock to get around a time limitation. But he won’t download a crack, no. A crack would be *stealing,* and stealing is wrong. This second type of user is where your protection (a salesman for your software!) will make most of his keep. How many of these users relative to totally honest users you have depends on your market, but sadly, they’re a lot more common than most non-developers would think.


The third type of user wants to use your software, but will pirate it given half the chance. Its too expensive, it doesn’t do quite what he needs, he doesn’t have the money, for-profit software development is evil, piracy is wrong but oh well… he has a lot of mental excuses. Some of this user group is very technically adept at finding cracks — they know what IRC channels to go to and what shady connections to excercize. Some of them rely on Google searches. You can potentially wheedle a small number of sales from this group with your protection scheme, and they’ll hate you for every minute of it.


The fourth type of user… “Do what you want ’cause a pirate is free, [**YOU ARE A PIRATE**!](http://www.youtube.com/watch?v=I0yI2MQf8Tk)” He flies the Jolly Roger and you will never, ever make a legitimate sale to him. Even if he does “buy” your software it will be with a stolen creditcard or chargebacked within 24 hours. You’ll find that there are countries on earth (*cough* China *cough*) where there are few users from any other type. Your protection system is not really relevant to this type of user, since he’ll be using the crack anyway.


Oh, yeah, lets talk about cracks a little bit. [You. Will. Be. Cracked.](http://discuss.joelonsoftware.com/default.asp?biz.5.363513.10) I really strongly recommend you read that post, because its true: no protection scheme will survive indefinite contact with the adversary. Your goal in instituting a protection scheme is not to achieve 0 utilization of your software by the Jolly Rogers of the world. It is primarily to keep circumvention methods obscure enough that it will take dedicated effort to discover either a way around your software *or* find someone who has found a way around your software.


There are several varities of cracks which you have to worry about. We are now crossing into the technical portion of this article, and will be discussing implementation details rather than philosophy, so pay attention.


1) A single good key. The cracker discovers, either via a “legitimate” purchase or analyzing your code, one single good key, and publishes it. This is the least damaging type of crack, because you can just ban that key in further updates to your software, and because if you use keys which are tied to other user data it will prevent someone from using the good key without otherwise impersonating the user it is tied to.


2) Keygen, or “key generators”. You have one of these lying around on your PC or server which generates good keys for your software. The cracker’s goal is not to replicate your system, but instead write one which produces at least some subset of the keys your system will produce. Many crackers prefer to write keygens because they get a psychological thrill out of “beating” you, but to most user groups there is no difference between one download and another.


3) A patch/crack which strips off your protection. For example, if you leave in a debug mode (if (!debug) {checkRegistrationKey();} else {registered = true;}), all the patch has to do is modify your executable to flip the debug bit and then your software is locked into the registered version. Creating a patch requires that your executable be a stable binary, as if the offsets of the bits to flip change applying an old patch will be impossible.


4) A cracked executable. This is the cracker’s least favorite method, because then he has to spend non-trivial amounts of bandwidth hosting the executable, and since he wants to host literally tens of thousands of executables this is irksome to him. However, remember, bandwidth is cheap — this is a speed bump, not a security mechanism.


In general, it is to your advantage to force the adversary to use countermeasures which are higher up that list. This means that your protection scheme should:


1) **Require user-specific data** so that a single good registration key does not break your software everywhere. The most obvious choice is username, but this is not very secure. Other popular choices include hard drive serial numbers, MAC addresses, GUIDs, etc. Remember, this will inconvinience legitimate users — you **will** have users who spell their name differently on their Paypal accounts versus in your software (example: McKenzie != Mckenzie has gotten my mother a few times, Bob Smith versus Robert Smith), you **will** have users who expect (and are perhaps, depending on your license, entitled) to use the software both at work and at home, you **will** have users whose hard drive dies and your software will cease to work on the new one. All of these become support issues for you, because your salesman is busy trodding on the toes of people who have already given you money. Consider carefully how much pain you will authorize him to inflict. For myself, I thought the risk of a serial key leaking was less than the amount of difficulty I would have policing unique serials, so while I ask folks for their name to generate my keys they’ll actually work for any name you put in (Shh, don’t tell the crackers :) ).


2) **Obfuscate your code**. Especially if you are using an interpreted language, such as .NET or Java, decompilers exist which will print out your protection routines in their entirety. This was how my very first hacked in version 1.0 happened, and that resulted in a keygen (i.e. total tactical victory for the bad guys). I’ve since started using [ProGuard](http://proguard.sourceforge.net/), a lovely OSS utility which takes your nice, easily decompileable JAR file and returns gibberish which still executes. This plus a (partial, backwards compatible) fix for the earlier keygen has kept me from getting hit with another wave of me hearties from China, although I know of at least one functioning keygen out there — but its buried beyond the reach of my casual pirate customers, which is a total strategic victory for me. Obfuscation is nice in that unless you need reflection or debugging stack traces it can’t hurt a legitimate user.


3) **Change binaries early and often** . Frequently changing your binary, via any method you want (obfuscation utilities can often do this — so can minor patches to your code), forces pirates to either host the executable themselves or deal with “customer support” requests like “Waaaaaah your patch doesn’t work anymore lol”.


OK, now, finally, on to license key generation algorithms. Some design considerations:


1) Are you going to run this offline, or are you going to run this on a server?


2) How much information from your customer does the algorithm require? How are you going to get this? e.g. if you require their hard drive serial number, you suddenly add the requirement “Customers can only purchase my application through my application”, which may be less than desireable.


3) Are you going to roll your own, or use an off-the-shelf system like [Armadillo](http://siliconrealms.com/index.shtml)? In general, you’re not paying for security (although its likely that their system is more secure than yours, its not totally secure), you’re paying for convinience. Armadillo has been broken before and will be broken again, like every other security system.


4) How do you get the registration key to the user? Do you want to display it on a website, display it on an email, or update the application directly (sometimes called “automatic key injection”? A lot of the payment processors (including [e-Sellerate](http://www.e-sellerate.net), as I recall) promote systems that have this as a feature. Its quite nice, as it reduces customer support headaches (what was my registration key? How do I input it again?), particularly with non-technical customers. I didn’t do this myself, primarily because it required more development effort than my schedule had time for.


OK, if you’re still with me, lets talk some strategies for key generation if you want to do it yourself.


1) **Public key encryption**. Basically, your registration key sends a message: “Bob Smith, I hereby give you the right to use my software, in exchange for the consideration you have given me”. The problem is that Jolly Roger wants to be able to forge the message and replace Bob Smith with Jolly Roger, thus bamboozling your program into functioning for him. Luckily, there is a solution to this: public key cryptography. Public key cryptography works like this: you have a pair of keys. One of them is public and you can give it out to everybody, including the adversary. One of them is private and you **guard it with your life**. Since your trial version will be in the hands of the adversary, the only thing the trial version can know is your public key.


Practically speaking, you first take the hash value of all the identifying information you have. Then, you encrypt this with your private key: the output of this encryption is your “registration key/serial number”. Your software then performs the same calculation of the hash value in parallel, and decrypts your serial number using your public key, which results in a hash value. If the two hash values match, you unlock the software. If not, you display a nicely worded message to contact support (remember, your protection mechanism is a salesman).


If you are interested in the math behind encryption, which gets kind of heady, Wikipedia has a nice article on [RSA](http://en.wikipedia.org/wiki/RSA#Signing_messages). I’ll give you my dirty little secret: I’ve got a very incomplete understanding of a lot of the number theory involved, and I don’t trust myself to implement encryption. Neither should you. Really, trust Bob Schneider, you’ll probably just end up breaking something. Instead, take the crypto library which comes with your package of choice, and **USE IT**. Look for “MD5 digest” or “message signing” in your documentation if you’re unfamiliar with the whole field and just want to be done, quickly.


2) **Everything else**. Any other mechanism is insecurity which you’re tolerating for the sake of preserving your time as a developer. With that in mind, for preventing casual piracy you don’t need to go as far as public key crypto, although I would oh-so-strongly suggest doing so. I ignored my own advice though, and did something similar to the following: take two random constants A and B, which are “secret” in the sense that you have to actually decompile my program to find them (“But Patrick, thats not very secret is it. After all, the program is in the hands of the adversary.” **EXACTLY**). if (serial ^ A) % B == 0, then the serial is good. Note this doesn’t allow for any use of identifying information, and was chosen totally because I could implement it in 30 seconds. If I did another product today, I would spend 30 minutes instead and use Java’s excellent crypto libraries. The weaknesses of my approach are obvious: with access to the code breaking it takes a matter of seconds, one serial number will work for any number of computers, etc etc. But it was sufficient to my purposes because my target customer has enough difficulty getting a legitimate version installed, to say nothing of navigating the dark corners of the Internet where the keygens flourish.


Where/when to check the serial number: I check once on startup. A lot of people say “Check in all sorts of places”, to make it harder for someone to crack by stripping out the check. If you want to be particularly nasty to the cracker, check in all sorts of places using inlined code (i.e. **DON’T** externalize it all into SerialNumberVerifier.class) and if at all possible make it multi-threaded and hard to recognize when it fails, too. But this just makes it harder to make the crack, not impossible, and remember your goal is generally not to defeat the cracker. Defeating the cracker does not make you an appreciable amount of money. You just need to defeat the casual user in most instances, and the casual user does not have access to a debugger nor know how to use one.


Alright, that about wraps it up. This article is a work in progress, so I might beef it up some more, perhaps with code samples or techniques to impose, e.g., time limitations. Someday. In the meanwhile, I hope you learned something.


[Edit: Yo ho, me hearties.  If ye be wantin’ to stick it to a pirate without having to program a thing, [cast yer glass over this way](http://microisvjournal.wordpress.com/2006/09/06/yo-ho-me-hearties-yo-ho/).]
