---
title: "Nim and the SpACE iN tHe le_Xe_mEs"
date: 2020-09-28
url: https://zedshaw.com/blog/2020-09-28-nim-and-the-space-in-the-lexemes/
slug: nim-and-the-space-in-the-lexemes
word_count: 1821
---



# Nim and the SpACE iN tHe le_Xe_mEs


I love the concept of [space in my art](https://zedshaw.com/blog/2020-08-17-energy-space-and-magic). Do I make the painting closed and exact, challenging myself to see how photographic I can be? Or, do I leave things unsaid, implied, and let the viewer walk in and sit down to be there with me? As I get older I feel that work needs space, and that I don't need to say everything all the time to say something. Saying everything and leaving nothing for other people ends up feeling authoritarian to me. Enforcing my will on others and expecting them to just like it because my great mind and hands sloshed paint down exactly? Nah. That's not me. Mostly?


This realization formed through studying classical realism a short time. I could paint and [draw photo realistically](https://zedshaw.com/blog/2016-08-14-taking-my-saint-anger-cast-drawing-home) but it drove me mad and took far too long. Sitting there grinding out tiny marks with tinier pencils for 8 months nearly broke me. I proved I could do it, and moved on with my life, but while I studied I noticed a common quality about the people who were very into this photographic style of painting and drawing: fear.


Nearly every person I encountered who was obsessed with making a perfect drawing seemed to be filled with fear of being wrong. They didn't worry that they weren't improving or that they weren't making an intentional piece of art. They worried that someone else would come along and point out a flaw in them by pointing out a mistake in their drawing. The drawing and paintings for them were a way to prove that they were worthy of love and capable by enforcing an exacting accuracy that bordered on the brutal in its self-flagellation. They spent hundreds hours scratching tiny lines onto pieces of paper seemingly out of fear of being judged a failure for getting the size of a tomato slightly wrong.


As I studied painting I started to realize that my programming skills came from a world that was also populated by the same people, and that I had this same mentality. This idea that if I didn't make my code solid, tight, and error free that everything was going to come crashing down on me. I'd lose my job, the respect of my peers, and be deemed a failure because a single function had a single mistake. I'm definitely not the only person who feels this way about code, and the entire industry is to blame.


For the last 30 years nearly every major movement in software has been an attempt to shame programmers into feeling inadequate for a situation that is entire out of their control. The vast majority of programmers didn't invent the browser, computers, operating systems, and programming languages they're forced to use, so how can they be to blame? How can a guy who created a language that's incredibly hard to use give a talk saying [we're all to blame for the mess we're in](https://www.youtube.com/watch?v=lKXe3HUG2l4) when none of us are the ones writing this crap?


The majority of us have no say in the tools we use all day, and if we criticize these tools an army of Developer Evangelists comes out of the tweets to throw more shame. Shame on you for questioning why the people in charge keep using obnoxious C++ style APIs in JavaScript! Shame on your for saying that open source project is terrible! "How dare Zed say that! Get him!"


Yet, this attitude seems to come from a position of accepting authoritarianism. I'm an asshole for saying a project is too big, too slow, and not well written; but if [Google says your project is junk](https://twitter.com/addyosmani/status/1304676118822174721) you will gleefully agree, bow [your head in shame](https://momentjs.com/docs/#/-project-status/) and shut it down like good little programmers. We'll all accept shaming from the corporations in power, but then reject it when it's from a peer? It should be the inverse.


The [open source projects](https://www.youtube.com/watch?v=M-sc73Y-zQA) and corporations using shame to push their products for the last 30 years have crafted two generations of programmers who live in constant fear. That fear causes them to squeeze all the space out of their creative endeavors while simultaneously scrambling to appease anyone who will promise to keep them safe. C++ promises to keep you safe from C! Java promises to keep you safe from C++! Ruby promises to keep you safe from Java! Node.js promises to keep you safe from Ruby! Haskell promises to keep you safe from everything!


Just be good programmers and don't question our edicts to you. Don't question why the [BDFL of a project is picking and choosing the projects of his friends](https://www.djangoproject.com/weblog/2006/aug/07/guidointerview/) and trying to destroy [potential competitors](https://webpy.org). Just keep doing what he says and proclaim magic dead, languages dead, don't question him. Be good and he'll keep you safe, but shame on you for not working hard enough. Shame, shame, shame.


This industry practice of selling shame has infected every programmer--myself included--with a propensity to unwittingly be an authoritarian. Go find any project right now with a Code of Conduct--even projects that *invented* Codes of Conduct--and you'll find authoritarianism:

1. They list only the project leader as the person to contact about abuses by the project leader.
2. They violate notions of Enthusiastic Informed Universal Consent by not holding elections for the leaders of the projects.
3. They refuse to list their potential punishments so you can't have informed consent before you join and place yourself under their pervasive and total control even outside of their project.
4. The list of enforcers is usually secret, enforcers have complete unilateral control to enforce at will, and the enforcers are never elected or held accountable.
5. All infractions of the code of conduct are met with equal brutality with no concept of the progressive values of rehabilitation over retribution.
6. Even worse, in many instances this brutal enforcement is unequal [totalitarianism for commoners](https://techcrunch.com/2013/03/21/a-dongle-joke-that-spiraled-way-out-of-control/) while [people in charge get away with asking women to touch their one eyed snake](http://holdenweb.blogspot.com/2012/12/im-sorry.html).


The totalitarianism and authoritarianism is so pervasive in this industry that even the people best positioned to put a stop to it end up using it without even realizing it. They *love* ends being justified by the means when it's *their* means. They *love* totalitarian enforcement of secret rules by secret people when it's *their* secret rules and *their* secret people. They love total authoritarian enforcement of their poorly defined rules in everyone's daily lives when it's *their* authoritarian rules. They love using triggering offensive terms when it's *their* enemies they trigger.


The authoritarianism in programming is so pervasive and internalized that I'm guilty of this hypocrisy myself. *Everyone* in the industry is guilty of authoritarian tendencies. Through art I've begun to realize how my blueprints of computational expression were founded on a slab of totalitarian thought. I fully internalized the idea that space in a software system leads to disaster. If you just leave one thing open to interpretation then you will be hacked, laughed at, ridiculed, and shamed for *daring* to fail to convert a string to an integer one time.


I ran smack into this hypocrisy when I found this feature in Nim called [style insensitivity](https://github.com/nim-lang/Nim/wiki/Unofficial-FAQ#why-is-it-caseunderscore-insensitive). I had a visceral and hateful reaction to it. I couldn't explain why though. Why was the idea of letting people write out functions how it best suits them so riddled with worms of fear? Isn't this adding space to the language? A space I desperately crave in my programming life?


I feel there's a need to explain style insensitivity so you can understand just how irrational my reaction was. Style insensitivity is the idea that a person should be giving the space to write `close_the_door` or `closeTheDoor` or even `cLoSe_ThEdO_or`. All of those map to the single name `closethedoor` which Nim claims reduces bugs since you can't accidentally have those classic 1-char-off errors found in other languages.


And when I ran into that I freaked the fuck out. What in the fucking hell? Why would *I* let some random jackass run into *MY* code base and type some fucking garbage like `cLoSe_ThEdO_or`? If I wrote `close_the_door` then fucking dammit everyone else has to type exactly what I typed or else the entire project is doomed! Do you remember how in Ruby nearly every fuckboy with a fucking idea thought it was cute to copy Why's terrible fucking coding style and endlessly chain dots after dots in a random sequence nobody could understand? A fucking distaster! Remember when they did this in all those other total failure languages?! Right. Exactly. This caused their failures! Why would you do this Nim? You were doing so good and now *thi*.......wait.


By hating on this feature I'm removing space that Nim is trying to create. What if this isn't really that bad *now*? Sure, in the past languages were kind of clunky and allowing this seemed to always lead to disaster. But, Nim is a very advanced compiler, probably the most advanced usable compiler out there. Nim gives me all of the safety features of other languages without forcing me to do work for the compiler. I'm not working a borrow checker for the compiler. I'm not sorting out hilbert spaces across a 4 dimensional hyper plane just to print "Hello World." It's doing a pretty good job of giving me room to express myself *and* safety at the same time.


My reaction to Nim's style insensitivity could just be more of that pervasive authoritarianism I've internalized as a programmer. It's so difficult to scrub out things that you *believe* kept you safe all these years, but maybe I need to think of Nim like it's a very nice kindergarten. It's safe, and there's no sharp objects around the room, but I'm allowed to run around like an idiot and play. Nim keeps me from hurting myself too much, and then gives me the freedom to express myself more easily because it's adding space to my toys. Space that other [programming languages try to squash](http://blog.erlang.org/introducing-ssa/) and destroy in the name of "safety" [when the compiler could just do that for me](https://www.cs.princeton.edu/~appel/papers/ssafun.pdf) like many compilers [already do](https://gcc.gnu.org/onlinedocs/gccint/SSA.html).


Through this writing I've come to the conclusion that I will force myself to use Nim and see if I'm right about its ability to give me space in my creative programming projects. Maybe this is an act of defiance against the [Fauxpen Source programming languages](https://groups.google.com/forum/#!msg/golang-nuts/6dKNSN0M_kg/Y1yDJRwQBgAJ) that suck in free developer time while pretending to be all about the [community](https://utcc.utoronto.ca/~cks/space/blog/programming/GoIsGooglesLanguage). I figure the worst that happens is I develop an informed opinion about Nim and can speak rationally about its design rather than using my ancient programmer's propensity to ascribe totalitarian beliefs to how good code should be written.


Because ultimately, I'd love to be able to just write code the way I just paint. Just a little.



---


###### More from Zed A. Shaw
