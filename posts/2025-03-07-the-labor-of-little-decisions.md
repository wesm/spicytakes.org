---
title: "The labor of little decisions"
subtitle: "And the intoxicating power of things that make them for us. Plus, LinkedIn! And White Lotus Power Rankings!"
date: 2025-03-07T18:06:49+00:00
url: https://benn.substack.com/p/the-labor-of-little-decisions
slug: the-labor-of-little-decisions
word_count: 2684
---


![](https://substackcdn.com/image/fetch/$s_!Oof4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880f2ed1-df5d-447b-8ba1-6f124e1f42ff_1200x630.png)

*The decider.*


If you are an 11-year-old fifth grader writing a book report, you spend a lot of time thinking about fonts. The right font makes you look smart. The right font sets the mood—Papyrusfor a report on ancient Egypt;Lucidafor Hernán Cortés;Copperplate Gothicfor Edgar Allen Poe;Stencilfor World War II. The right font (and the rightplastic cover) is how you get extra credit. So when you open up Microsoft Word to write your report, you think very carefully about the font, because it is very important to get it right.1


On the other hand, if you are an AI company, or a venture capitalist who invests in AI companies, you do not think very hard about fonts. You are doing important and challenging things that take all of your attention and energy. You read technical papers and solve the hard math problems at the sharp edge of computer science. You do not have time for trivial aesthetic dilettantes; fonts are frivolous distractions; they are tinsel for children; they are opiates for the unoccupied brain. So your website is simple: A plain white page that uses a safe default likeInter, or one of theoriginal Windows fontslikeCourier New, or, if you are engaged in especially serious work, does not evenspecifyafontatall.2


Ah, hahaha, no, that’s not true. We all care about the fonts that we use, because fonts are brand, and brand is identity. The font on our website, or the look of ouradult book reportPowerpoint busyworktells a story, even if that story is, “I want you to think I do not care about this.” The absence of a choice is itself a choice—a statement, even. There is no true neutral.


When you build anything on the internet, like a website or a software product, you have to make tons of choices like this. You have to pick the fonts. You have to decide what the buttons look like—should they have rounded corners? How do they animate when you click on them? Should they use words or icons? Youhave to decideon background colors, and border colors, and highlight colors, and hover colors. You have to decide on padding and margins and how much space to add between lines of text.


You have to make a lot of bigger decisions too. Do you put the menu at the top of the page or on the side? Do you open things in modals or in new pages? Do you automatically save people’s updates, or do you ask them to do it manually? Do you organize things with tags or folders? Can you create nested folders? When people search for stuff, how should the results get ordered?


Most of the time, you don’t carethatmuch about this stuff. Nobody builds a new app because they want to make Salesforce with prettier fonts, or because they want Google Sheets with the formatting ribbon on the side.3People build new products because they have some novel innovation—Salesforce with AI, or Google Sheetswith interactive dashboards, or Evernotewith some bizarro twist. All these other details are just necessary scaffolding.


Necessary, and time-consuming. Because, even if you don’t care about this stuff, you have to make decisions about it.


There’s this common bit that people use when they’re teaching kids how to use computers. They tell the kid to give them instructions abouthow to make a peanut butter and jelly sandwich, and say that they will follow the instructions exactly. “Put jelly on the bread,” the kid says. The teacher puts the jar of jelly on the bagged loaf of bread. “Nooo, open the jelly first!” The teacher smashes the jar open on the counter.


The point is that computers follow precise instructions. Which is great—that’s why they can fly rockets and run stock markets4—but it’s also exhausting. Because, in addition to making them pedantic chefs, it makes them demanding designers. All of the necessary decisions that go into making something have to be specified. Even if you don’t care about the particular color of your app’s background, you have to choose the exact shade. When you want to add a picture to a webpage, you have to choose exactly how big to make it, and the exact number of pixels to put in the margins around it. If you don’t tell the computer precisely how to make a button, the button won’t exist.


Of course, there are shortcuts—unstyled HTML; pre-made design frameworks likeBootstrap; picking a website you like and literally copying every color—but they’re only partial shortcuts. First, you can’t offload every decision, because there is no Bootstrap for choosing between modals or pages, or deciding if your app will use folders or tags. If you want to organize the notes in your bizarro note-taking app, you have to decide how to organize them.


Second, the defaults are boring! Things like Bootstrap are generic fads.5And, though wecanfully embrace the stock settings of raw HTML, that is both a severe choice—topretend to exist beyond fashion—and hard to maintain.


And so, we fiddle. We think about all of this stuff because we have to make some sort of decision, and we want to make a good one. We get distracted, reverting to our 11-year-old selves, scrolling through the font list on Microsoft Word looking for our favorite. We spend time making thousands of mostly insignificant choices—partly because computers require us to define everything in line by tedious line of code, and partly because, when we’re sitting in front of a control panel full of knobs to turn, we can’t help ourselves.6


That’s life, in a way. So much of it is the distracting labor of little decisions. It is having to think about small things of relatively little consequence, because you can’t eat an unchosen meal, wear an unstyled outfit, board an unbooked flight, or categorize your application’s documents with an unspecified organizational unit. And the decision is a often harder than the doing.


---


AI, we’re told, is coming for software engineers’ jobs. Butmost warningsinclude acaveat, of sorts: It’s coming forjuniorengineers. The robots are good enough to do the mechanical work of translating English instructions into performant code. But they aren’t good enough to make strategic architectural decisions, or see several steps ahead of the mistake they’re about to make. They willaccumulate tech debtfaster than they repair it, and engineers need to be theirguiding editor.


Though this all seems true enough (for now), there’s at least one way in which AI coding agents are much more like senior engineers than junior ones: They don't need precise specs. They don't need everything spelled out for them. You can chuck vague requests at Cursor, to add loading animations or to put a button on the bottom of a page, and they do it, with pretty good results. They won’t come up with completely original solutions—their aesthetic is some rough average of everyone else’s style—but that’s often the point. Not everything needs to be innovative; it just needs to workwithout being a pixel-perfect copyof something specific. You don’t want invention, but an adjustable default: Make it denser; make it look steampunk; make itsound expensive. You want to be expressive without the painful specificity of layers upon layers of tangled CSS. You wantthree words, not hex codes and pixel counts.


It also works for more structural changes: “Add nested folders for the notes;” or, “add folders;” or, even, “add a way to organize my bizarro notes.” Though its choices here aren’t groundbreaking either, they are often good enough—good enough to fill the supporting roles that they need to, and, maybe more importantly, good enough to settle our compulsion to tinker.


Inmy recent attemptto Build Something, that feature of the experience was as striking as anything. Thoughvibe codinghas come to mean “building software without needing to understand code,” there’s a more literal definition that better reflects its real allure: It’sdecisionby vibe. It’s being able to manifest stuff without actually having to choose what you really want. You can tell it your problem and your rough preferences, and ittakes the wheel.


When people wax poetic about vibe coding, I suspect this is what they’re really feeling. Yes, AI breaks through a technical ceiling, but it also frees them from decision fatigue. It lets them think about the things they want to think about, and delegate what they don’t. AI is mechanically useful because it does stuff for us, and that is what we usually talk about. But its emotionally intoxicating power—its real delight, or its real danger—is that itdecidesstuff for us.


---


Ah. But. Here’s a paradox I think about a lot: Why don’t people use AI to decide what to eat for dinner?


It seems like such an obvious thing. AI—both the vintage machine learning algorithms and today’s generative varietals—are very good at recommending things. People have to decide what to cook or where to go to eat all the time, and they hate doing it. The decision barely matters, and if we make a bad one, we get to try again tomorrow. And yet, most people (I think?) still scroll through Google reviews and cooking apps looking for restaurants and recipes.As god as my witness, I will not pick the restaurant—but I will not let the computer pick it either.


So, if you want to build an product that makes decisions for people—or even want to claim that AI can—it seems important to first understand why people are still reluctant to let it make this one?


My best guess is that there are two problems. First,the recommendation appsare missing a bunch of enigmatic context—I’m very hungry; I just ate pizza and don’t want it again; I’m in the mood for grilled chicken and a sweet peanut sauce. And second, the choices feel arbitrary. They tell you to makeJapanese curry chicken, or to eat at a random Italian restaurant, and don’t tell you why. Though they ostensibly make a choice for you, they also make it very easy to tell it no. “Pass; I don’t like that; it’s notthe best.” These apps aren’t decisions; they’re just more options.


But I think it’s solvable: Have the apps convince us. Tell uswhywe should eat there—it’s not usually crowded on Wednesdays; it’s been saved to your favorites for a while and you still haven’t gone; this review says that they serve ridiculous cocktails in novelty glassware, and we all know how you feel aboutridiculouscocktailsinnoveltyglassware. Make me think about what I’m giving up if I swipe left.


The thing is, this is easy? If LLMs are good at anything, it’sreverse-engineering a persuasive argument. That’s kind of their whole thing: Being confident and convincing, about everything, including stuff that they just made up.


Sometimes, that’s bad, and most people who build AI products try to solve it by working really hard to make the robots right. But, outside of a few very important situations—flying rockets and running stock markets and stuff like that—I’m not sure that’s what we actually want. We want decisions. We want to choose a font, and be as confident as the AI that it was right.


There are lots of examples of where this might work. The restaurant recommendation app, that sells us on its suggestions. A dating app that doesn’t try to find marginally better matches, but tells us why this match is worth asking out. A movie recommender that tells us what movie we should watch and why we’ll like it.7Tools for buying gifts and designing your apartment and buying clothes that aren’t justalgorithmic boxes of cottagecore dresses and chambray shirts, but are apps that tell you why you’d look great in cottagecore dresses and chambray shirts.


And, for the data people here, analytical apps that sell you on their conclusions. There is a small army of text-to-SQL startups that promise a future of instant answers and automatic insights. Most of these companies are hammering away at the technology, trying to get LLMs to conduct more accurate analyses. But this might be pushing on the wrong part of the problem. A better chart won’t convinces us to do things;more persuasive words will. Don’t build text-to-SQL; build text-to-SQL-to-argument, and give an executive the emotional support to make a decision.


After all, we're not really looking for the perfect font, because we never wanted to think about the font in the first place. We're just looking for permission to make a choice, and move on.


---


# Truman


See,thisis how it starts:


> Introducing ReachFor the first time in history, you can create an AI simulation of your own LinkedIn audience. Reach is your LinkedIn brand-building co-pilot, helping you test and refine your posts before you publish.


We sign up for the simulation to test our LinkedIn posts. We don't care about the simulation at first, because the simulation is not real. We can't sell our software in the simulation; the simulation does not need our recruiting services or our eight-week data engineering bootcamp. The simulation cannot subscribe to our newsletter.


But the simulation canlikeour newsletter. The simulation can talk about our newsletter. The simulation can make our newsletter seem important, and give us the thrill of our newsletter going viral. The simulation can become our connections, our fans, our parasocial suitors. The simulation can't buy our stuff, but it can give uswhat we really want: followers and fame.


The simulation is not real, but really, isBrandon Ellis | I Turn Founders into Fortune 500 CEOs | Author of the Zero-to-Unicorn Playbook | Blitzscalerreal either? We never talk to Brandon. We don’twantto talk to Brandon. Is Brandon a machine? Is Brandon from the simulation? It does not matter. Brandon is just a plausibly sentient thumb hovering over a like button. Brandon has less rizz than thatflirty Sesame bot. We’d rather talk to Sesame. We’d rather get a like from Sesame.


“Imagine seeing your post go viral before you post it,”Reach says. Sure, for now. But at some point, if you’ve already gone viral on the simulation, why bother trying to go viral onan even more lifeless one?


---


# The White Lotus Power Rankings


After the second episode, Saxon is holding strong, though Greg is climbing fast. The outlook is grim for Gaitok and Mook. And Piper seems more innocent, but the rest of the Ratliffs look a lot more sus


![](https://substackcdn.com/image/fetch/$s_!wrYO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf55a372-6a16-471b-9a26-b59b30a5f8b5_978x1274.png)


Episode two also smoothed out the demographic divide a bit:

- After the first episode, 88 percent of women found the male characters deplorable andzero percentof women found the men likable. Though men also thought that the men in the show were deplorable, nearly half of the male viewers thought male characters were the most charming. After episode two, however, both men and women found the male characters a lot more likable.
- But people’s murder suspicions flipped? After episode one, female viewers were twice as suspicious of the women as they were of the men, and male viewers were twice as suspicious of the men. After episode two, the women are now twice as suspicious of the men, and the men are somewhat more suspicious of the women. Suspicious.


![](https://substackcdn.com/image/fetch/$s_!J-05!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea12e178-637b-4730-8d68-529e54530ea7_990x636.png)


You know the drill. Vote early; vote often; vote for episode 3, which is the episode that already aired last Sunday:


Vote!

[1](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-1-158597799)

It is also very important to distract yourself from having to actually write about Hernán Cortés.

[2](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-2-158597799)

Introducing a newChatbot Arena: The ChatbotWebsiteArena.


![](https://substackcdn.com/image/fetch/$s_!nbdS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdea6569a-3ec5-4e25-9451-42cb76a54352_968x544.png)

[3](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-3-158597799)

This isn’t entirely true. Some productsreally areGoogle Docs with prettier fonts and the navigation bar on the side.

[4](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-4-158597799)

Citi, on the other hand.

[5](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-5-158597799)

It is the uniform of websites that take pride in their appearance, but lack the self-confidence to stand out from the crowd.

[6](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-6-158597799)

There’s a parallel here with the decisions people make about how to run a company. When you start a startup, it’s tempting to tinker with everything: To invent new organization structures and management philosophies and compensation plans. It’s almost always a bad idea. Most companies would be better off focusing on their one unique thing, and just doing theboring versionof everything else.

[7](https://benn.substack.com/p/the-labor-of-little-decisions#footnote-anchor-7-158597799)

You should watch the newGriff music videothat came out today, and you will like it because it’s a Griff music video.
