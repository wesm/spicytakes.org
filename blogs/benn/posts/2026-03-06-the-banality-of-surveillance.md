---
title: "The banality of surveillance"
subtitle: "Do our dull lives become worth watching?"
date: 2026-03-06T14:35:38+00:00
url: https://benn.substack.com/p/the-banality-of-surveillance
slug: the-banality-of-surveillance
word_count: 2282
---


![](https://substackcdn.com/image/fetch/$s_!96QI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7ad88e5c-dcb4-438b-889f-a711dfe3814f_2048x828.png)


For a while, I worked at a company that branded itself as the “enterprise social network,” though for all intents and purposes, it was the enterprise Facebook.1Facebook was moving all of our personal communication out of emails and into a shared feed of posts and replies; our product was designed to do the same thing for our professional communication.


That meant our product was also designed tolooklike Facebook.2There was a newsfeed; there were messages and threads; there were users; there were user profiles. There was a like button. It was Facebook, in a small corporate sandbox.


A couple months after I joined the company as a data analyst, the product and engineering department held one of its regular hack days.3Everyone had 24 hours to work on anything they wanted to, and then, a strict three minutes to present their project to the entire department. It was judged; there was a stage and an emcee; there was a soundboard full of jeers; there were trophies for winners; there was an open bar. There was pride in it, and everyone wanted to put on a good show. For this particular hack day, the data team was participating for the first time, and in the days leading up to the event, we talked about our ideas. What do you want to do, we asked each other? What are you going to build?


My idea felt obvious. If you had access to data on how people were using Facebook—which is the data we had, in a bizarro bureaucratic sort of way—what would be the first thing you’d look up? If you knew someone else had that data, what would be thelastthing you’d want them to look up?


Profile views. It’s clearly profile views. It’s who’s looking at your profile; it’s the profiles that you’re looking at. That was the holy grail; the third rail; thethird life. If you wanted to put on a good show—if you wanted to make adrunk audiencelook up from their laptops—that’s the data that will make them pay attention.


And it was, of course, data that we already had. Like any responsible SaaS product, our app was thoroughly “instrumented”—it recorded every click; every page view; every mobile interaction. We tracked the user who did it; the device that they did it from; their browser; their IP address; the sequence of clicks that came before; the sequence that came after. This type of logging was allgeneric, mundane, the “industry standard.” We used the sametracking librariesthat everyone else used. Werecordedthe sameeventsthateveryoneelse did. It was mindless and mechanical—years before I joined, an engineer had stuck a few lines of code in our app’s codebase, it captured millions of events an hour, and everything was dumped into a huge table called “event properties.” Because, as the legal documents all say, some piece of it might one day be useful to “improveourServices.”4


Though all this data was carefully protected in an encrypted database behind several firewalls and one very long password, that was not what made it secure. It was secure because it was a pain to use. You had to come up with interesting—or, you know, indelicate—questions to ask of it. You had to figure out how to answer that question using a sprawling array of machine-generated event logs. And you had to write 595-line SQL queries to do it all.5But any employee—at our company, or at the hundreds of other SaaS startups that were functionally identical to us, and who all logged identical streams of data—could write that query, combine those logs, and answer those questions.


Or, more generally: Prior to working in Silicon Valley, I assumed that data was secure because it was obfuscated by impressive cryptography and stored in buildings that wereguarded by tall fences. And I assumed that what we did on the internet was private—and people’s ability to draw any inferences from what we did was difficult—because “surveillance” required complex technologies that could detect faint patterns in millions of disparate signals. Yes, Target might be able to figure outif someone is pregnantbefore their father could, but that took years of careful observation and sophisticated science. It took well-trained humans working with well-trained models, years in the making.


If only. On an internet where everything is tracked—and man,everythingis tracked—surveillance does not require a Ph.D., or even any particularly advanced math. It just requires a junior analyst with 24 hours of free time.6Because the real fences around the data all we leave behind—and the real protections of our privacy—are neither tall nor covered in barbed wire. They are simply fences that are annoying to climb.7We are not hidden, on the internet; mostly, people are just too uninterested to bother looking for us.


---


Everyone already knows what happened: The United States Department of War wanted to use Claude.8Anthropic wanted them to use Claude, but with restrictions. The two sides could not agree; the negotiations broke down; the negotiations turned into outrighthostilities; the hostilities becamevery public.The Atlanticreports on part ofwhat went wrong:


> Anthropic learned that the Pentagon still wanted to use the company’s AI to analyze bulk data collected from Americans. That could include information such as the questions you ask your favorite chatbot, your Google search history, your GPS-tracked movements, and your credit-card transactions, all of which could be cross-referenced with other details about your life.


When we hear stories about “mass surveillance” and “artificial intelligence” and the “CIA,” it is tempting to imagine systems of unfathomable reach and sophistication. It is tempting to worry about shadowy government agencies using AI to hack into our phones andturn them into sonar transmitters.9It is tempting to see thethe Greco—a million sensors and cameras feeding into a machine that “doesn’t think, butreasons:”


> It reads every permutation in every wager in every seat in the entire casino, hand by hand. It’s wired into floor security cameras that measure pupil dilation, and determine if a win is legitimate or expected. It gathers bio feedback—players’ heart rates, body temperatures. It measures, on a second-by-second basis, whether the standard variations of gaming algorithms are holding or are being manipulated. The data is analyzed in real time, in a field of exabytes.


For better or for worse, reality is almost certainly much more mundane. Nobody wants to use AI to bug our phones, or to build a sprawling nerve system to track our vitals, becauseour phones are already bugged. Everything we do on them is recorded a dozen times over, by our wireless carriers, by the websites we visit and the apps we use, by the vendors and ad networks those companies are sending their data to, and in the marketplaces thatsellthatdata. We built the eyes of the Greco decades ago.


But that data has remained relatively secure—or maybe more precisely, its potential energy has remained relatively buried—largely because it’s tedious to work with. It’s messy; it’s scattered across different sources and in different formats; combining it together is a pain, and most of us are simply not interesting enough to investigate. Data analysts who work at shadowy government agencies have lives too, and they do not want to write 595-line SQL queries either.


But AI doesn’t mind. And that’s the boring danger of what happens next: Not of AI becoming a superintelligent Sherlock Holmes finding impossible patterns in its enormousmind palace,10but of it being a million monkeys at a million typewriters, doing the grunt work no person wanted to do. Because when prying questions are a prompt away—rather than 24 hours of work away—who wouldn’t get tempted to pry?


---


It does make you wonder though: While defense and intelligence agencies are unique in the legal and extralegal alleys in which they operate, they are not unique in their ability to warehouse massive amounts of data. In fact, asThe Atlanticpointed out, these agencies aren’t collecting this data themselves; they are buying it from other people, inopen markets:


> The government can purchase detailed records of Americans’ movements, web browsing, and associations from public sources without obtaining a warrant, a practice theIntelligence Community has acknowledgedraises privacy concerns and that has generated bipartisan opposition in Congress. Powerful AI makes it possible to assemble this scattered, individually innocuous data into a comprehensive picture of any person’s life—automatically and at massive scale.11


But if those agencies can buy that data, so can other people. If they can use AI to trawl through it “at massive scale,” so can other companies—especially if those companies are already collecting those events and messages themselves.12


People often talk about how AI breaks many of the foundational floorboards of our society. Our formal and informal senses of truth are built on the assumption that realistic photos and videos cannot be faked; that is breaking down. Our ambitions and careers are built on the assumption that intelligence and expertise are scarce; that is breaking down. Our sense of how the world works is often defined by what is possible for other people to doandwhat is worthwhile for them to do. Sure, we know it is possible for us to be monitored, but why would anyone bother watching the tapes? Everyone must have more important things to do with their time.


Banality is a sturdy armor. Or was, anyway.

[1](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-1-190098744)

It was founded in 2008, seven years before Facebooklaunchedthe official enterprise Facebook™, and 18 years before Facebookshut downthe official enterprise Facebook™.

[2](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-2-190098744)

On one hand, this was probably smart: People already knew how to use Facebook. On the other hand,if you knew how to use Facebook, you knew how to useFacebook.Which meant that people ended up using our productlike they used Facebook, and spent a lot of time posting pictures of their pets.

[3](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-3-190098744)

Hack days used to be a staple in Silicon Valley. Give people a couple days to be creative, to experiment with the side projects they’ve always been eyeing, and let them hack together a half-baked version to see if there’s the seed of a good idea. Sometimes, there is: Gmail was createdduring Google’s “20 percent” time, and a number of Facebook features were first createdduring hackathons.


Now, though, every dayis hack day, and every businessis a hack day project.

[4](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-4-190098744)

And it did! Notas much as we would’ve liked, maybe, but knowing the basic contours of what people do with your products is a very important part of making those products better.

[5](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-5-190098744)

“What an oddly specific number of lines,” the discerning reader might observe.

[6](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-6-190098744)

The hack day project ended up being an aggregated table of internal profile viewers and viewees, because as soon as you start looking at data like this, you realize how nuclear it could be. Still, that somewhat sanitized version of the project won the “Human Relations” award. It was meant to be ironic, but perhaps the real irony was the unintentional part: That, apparently, nobody actually knew whatHRstood for.

[7](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-7-190098744)

I discovered this again when our companywas bought by Microsoft:


> When I worked at Microsoft…we were trying to figure out how many people used O365, the online version of Office. The question was unanswerable. We heard rumors that there was a 6,000 line script that could parse some logs and approximate a guess, but nobody had ever seen it run. If an exec asked about O365 adoption, someone glued together a bunch of numbers in Excel. We all laugh at FTX for theirterrible balance sheetof one-off math and “hidden, poorly labeled accounts,” but we are all FTX; it’s just a matter of degree.

[8](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-8-190098744)

Or actually: the United States Department of Wardoesuse Claude. It uses Claudeto bomb Iran. It uses Claude to bomb Iran “at machine speed rather than human speed.” It uses Claude to “do the work of 2,000 staff with a team of just 20 people, according to a study of the system’s use by the Army’s 18th Airborne Corps by Georgetown University.”


Nothing is slowing down. The white collar apocalypseis here. AI isfar from reachingits theoretical disruptive capability.Introducing GPT 5.4.The sentient chatbotdidhelp us do it. All of these stories are fromyesterday.

[9](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-9-190098744)

Technically, “transducers?”

[10](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-10-190098744)

We’re still trying to get AI to reliably answer “how many orders did we get last week” on top of a table of orders.

[11](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-11-190098744)

Amodei made the same point inthat leaked memo:


> For example, it is legal for DoW to buy a bunch of private data on US citizens from vendors who have obtained that data in some legal way (often involving hidden consents to sell to third parties) and then analyze it at scale with AI to build profiles of citizens, their loyalties, movement patterns in physical space (the data they can get includes GPS data, etc), and much more.


And while we’re here: At the end of the memo, which was largely about what Amodei saw as OpenAI’s efforts to spin its messaging about the entire affair, Amodei said who he was most worried about being manipulated:


> I think this attempted spin/gaslighting is not working very well on the general public or the media, where people mostly see OpenAI’s deal with DoW as sketchy or suspicious, and see us as the heroes (we’re #2 in the App Store now!). It is working on some Twitter morons, which doesn’t matter, but my main worry is how to make sure it doesn’t work on OpenAI employees.


One way to think about competition between Anthropic and OpenAI is as a technological arms race for the control of Earth, of humanity, and of the entire cosmos. Another way to think about it is that it’s apopularity contest among a few thousand AI engineers.

[12](https://benn.substack.com/p/the-banality-of-surveillance#footnote-anchor-12-190098744)

For example, what data would the NSA really like to buy, but can’t? The messages that we’re all sending to AI chatbots, I imagine.
