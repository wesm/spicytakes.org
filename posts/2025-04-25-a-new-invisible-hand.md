---
title: "A new invisible hand"
subtitle: "The inscrutable ghost in every MCP server."
date: 2025-04-25T16:26:33+00:00
url: https://benn.substack.com/p/a-new-invisible-hand
slug: a-new-invisible-hand
word_count: 3135
---


![](https://substackcdn.com/image/fetch/$s_!0SBd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8371994-4250-44c4-a0fc-4ae3270cd4bb_1708x1514.png)

*He Has Driven.*


---


Here are two dunks by LeBron James. Which one is better?


And the second one:


Ahaha, they are the same dunk. Obviously. But the clips are from two different broadcasts, with different announcers and different cuts after the dunk. The first one is fairly subdued, shows the Cleveland bench for a brief second after the dunk, and then quickly returns to midcourt camera to show the next play, which ends in an unremarkable foul.


In the second clip, both announcers lose their minds. Then the broadcast shows Cleveland fans losing their minds; then they show the Cleveland bench losing their minds; then they show two replays. They fully ignore the next play; they’re still showing the second replay when you hear the whistle from the foul.


If you were watching the first broadcast, how would you react to it? Probably like the announcers seem to: You’d look over at your friends and say, “ok ok,not bad.” But if you were watching the second broadcast, you’d also lose your mind. You’d scream. You’d jump to your feet. You’d say to your friends, “nobody dunks like LeBron! That speed! That power!We are all witnesses!” And then you’d debate if LeBron was one of the best dunkers of all time, or if he’s just strong.


Because of things like this, I’ve always wondered how much quiet power announcers and broadcast directors have over our beliefs about sports. Most people watch live sports on TV, and TV is an editorial experience: Announcers aren’t simply describing the action that they see; they’re choosing what to talk about, what to highlight, and what to ignore. Nor are we watching a raw feed of a court or field; we’re watching a movie, cut together for us in real time.1These emergent narratives—that some player is heroically fighting through a lingering injury; that there’sgrowing dramain the clubhouse; that LeBron’s dunk was nuclear or merely good—are inseparable from our perception of the game, because theyareour perception of the game. And almost everything we think about sports is downstream from that initial broadcast: Afun callcan turn into a viral clip that we share with friends. A broadcast that harps on a potentially controversial coaching decision canmakeit a controversial coaching decision. Aquick cutto abench celebrationcan derailsports talk radiofor days.


That doesn't make announcers manipulative or dishonest;2in most cases, I doubt it’s even intentional. But that doesn’t change its power. The broadcast is an anchoring frame. It sets the initial agenda. Even if people come up with their own interpretations later, the seed of those opinions grew out of the announcer’s soil.3


---


Data, I’d argue, is consumed in an analogous way. Though it exists is an approximately raw form,4most analysis comes with some sort of narrative. Corporate analysts caption their presentations to call out what’s most important. TheWall Street Journaldelivers quantitative news in paragraphs of prose. Just as we’re given selective views of a basketball game, data consumers—executives, “business users,” the people who ask analysts questions—are typically given curated cuts of data, with its own sidebar of color commentary.


To be clear, this is almost certainly a good and necessary thing. Not only are reams of raw data impossible to process, but they’re alsoboring. If Bloomberg’s news business was just a daily printout of the Bloomberg’s terminal business, very few people would read it, and even fewer would know what to make of it. As I said ten years ago onbenn.company.substack.com, “even though analysis is built on data, words—not tables and charts—are what make it effective.”


But those words—even seemingly innocuous ones, the sort that most people would still describe as objective—are inevitably manipulative. As I’m writing this, the top headline on theWall Street Journalis about Google.That articleopens with what appears to be basic reporting:


> Google’s earnings power is holding up well, even as the internet giant spends record sums on artificial intelligence in the midst of global economic turbulence.Parent company reported operating income of $30.6 billion for the first quarter on Thursday—solidly beating Wall Street’s forecast of $28.7 billion.


Holding up? Holding upwell?Solidlybeating forecasts? Is a $2 billion beat solid? Expected? Record-setting? I don’t know. But I assume it must be solid, because that’s what it says. Had that line said “barely beating Wall Street’s forecast of $28.7 billion,” my perspective on Google would be entirely different, even if the numbers were the same.


My point here isn’t to disagree with those interpretations; it’s to say that those subtle cues areeffective—and even more so than the data. When we look at numbers, we think the numbers are what dictate how we react to them, but I’d argue that the commentary around the numbers actually matters more.As we talked about before:


> Once you notice this phenomenon, you see it everywhere. Nearly every news story, every blog post, every analyst report, and even every email that references some corporate statistic follows the same pattern: A datapoint, and a brief description—or subtle nudge, like the word “just”—tells us what it means. Ask yourself though: Would you come to the same conclusion with the data alone? As often as not, we wouldn’t—not because the conclusion is wrong, but because, when presented with data on some domain we don’t deeply understand, we have no choice but to look for clues and shortcuts to help us make sense of those numbers. Our best shortcuts are typically the words around the data, so we interpret it the way we’re told to. The claim decodes the data, and the data proves the claim.


There isn’t a clear way to interpret most numbers—hence theneedto interpret most numbers—but those interpretations, like the commentary of an NBA announcer, primes a narrative in our heads. Awiggling chartsuggests that…things are volatile? That nothing is really changing? That some number isup, ish? It suggests, at least initially, whatever the person presenting the chart chooses to say it suggests. And every subsequent interpretation of that same chart is a fork off that first path, where the next questions and conclusions are arrived at, through a sort of analytical dead reckoning, in part because of the questions and conclusions that came before.


---


This week, dbt Labslaunched an MCP server. Roughly speaking, MCP servers are documentation that’s designed to be read by an LLM. When a person wants to understand how a tool like dbt works, they go to a websitethat explains it to them. That website is designed for people: It is neatly designed; explanations are written in simple prose; there are little diagrams and tables and important words are in bold fonts.


MCP servers provide the same fundamental service—they explain how dbt works—but they make the information available in ways that are optimized for an LLM. They don’t include diagrams, because LLMs typically work better with words than pictures. They adhere to a consistent structure and use a standard vocabulary that LLMs can be trained to understand. If sites like docs.getdbt.com are the children of decades of developingtechnical writing normsand information architecture hierarchies for engineers, MCP servers are the early ancestors of the same thing, but built for AI agents.5


Increasingly, when some bot wants to interact with a tool, that bot is directed to that tool’s MCP server. If you want to have a bot post a message on Slack, the bot can go to a Slack MCP server and ask, “how do I post a message?,” and the MCP server will return an answer. Though the bot could justread the manualto get the same information, that manual is littered with nice visual elements that are wonderful for people, but distracting for an LLM. The Slack MCP serveris not. Don’t read the manual,RTFMCP.


Here, then, are a few stylized facts about dbt’s new MCP server:

1. People use dbt to define core business concepts and metrics, like a table of customers, or a formula for how to calculate revenue.
2. If you have a question about these concepts—what’s the average revenue we make per customer, for example—dbt, which knows what a customer is and how to calculate revenue, can give you instructions on how to get the answer.
3. But it’s not that obvious how to extract those instructions. You have to know which tables dbt has, and which formulas, and you have to choose the right ones to mix together to compute the average revenue per customer.
4. An analyst could figure this out by usingdbt Explorer, which helps people search for tables and metrics that are defined in dbt. But for the same reason an LLM doesn’t want to read the Slack documentation, an LLM doesn’t want to read dbt Explorer.6
5. The dbt MCP server is dbt Explorer for an AI agent. It is how an LLM looks up what’s in dbt.
6. Put it all together, and you get a (theoretical) experience like this: Ask a bot a question, the bot asks the dbt MCP server for help answering it, the MCP server gives it instructions, the bot interprets those instructions, makes an informed decision on how to answer your question, and sends you its response.


On one hand, that ambition isn’t exactly new; people have beentrying to build it(andothershave beencomplainingaboutit) for ages. On the other hand, there’s a growing sense of newfound momentum about this particular effort. Though LLMs may not have been great analysts out of the box, the pieces are coming together. As Tristan from dbt Labs recentlyput it, dbt, MCP, and Anthropic’s Claude 3.7 “is just dramatically better at [exploratory data analysis] than anything I’ve experienced in my life, and it’s getting better fast.” Eventually, “AI is going to be meaningfully better at exploratory data analysis than any BI tool.”


Ok, maybe,I don’t know. But it seems plausible enough that, over time, LLMs inject themselves into more and more analytical workflows. They become, if not great analysts, good enough at answering basic questions. “Getting good is tractable now.”


If that happens, though, the way weinterpretdata will surely look different than it does today. Rather than going to a BI tool and looking at a wall of charts—onto which we have to project our own conclusions—people might ask an agent for an answer. That agent will consult with things like dbt’s MCP server and decide which tables and charts are most appropriate, from what could be an enormous library of possible choices.7It will probably annotate its answer with an explanation. And, if business reporting becomesmore centralized around this sort of interactioninstead of the traditional point-and-click approach, we will increasingly consume data through conversation and commentary.


As it is with both announcers and human analysts, it’s not that LLMs will lie about the numbers; it’s that they’ll tell you what they see, before you have a chance to see it for yourself. If data is acompany’s senses, then whatever sits between a quantitative question and its annotated answer is the creative director of a company’s reality. That thing used to be analysts. Soon, it might be something else.


---


Now, I don’t want to overstate how much that matters. Maybe this is good; maybe the robots are better than the analysts. It would seem pretty silly to say replacing unused BI dashboards with a chatbot that can make charts and write in the expository style of theWall Street Journalis the first step to the enslavement of the human race. Not everything is Important.


Still. Writing in theNew Yorkeron a different topic,Evan Osnos asks, “What is the precise moment, in the life of a country, when tyranny takes hold? It rarely happens in an instant; it arrives like twilight, and, at first, the eyes adjust.” There is no threshold between day and night. There is only fading light, and a biological resistance to seeing it clearly. And the analogy feels apt here too.


When Ibuilt that note-taking appwith Cursor, I didn’t give it much direction. I told it that I wanted it to feel like a simple text editor, without too many distractions. From that, it created its own design aesthetic. Though I was firmly in charge—I gave it that first instruction, and made some pixel-by-pixel tweaks of what it gave me back—my sense of control was at least a little illusionary. I was reacting to its drafts; I was coming up with new ideas based on its suggestions. My hands were on the wheel, but I was slowly letting go. First, AI was like cruise control, auto-completing my exact wishes. Then it was self-driving mode, taking my directions and doing the tedious work of getting me from here to there. Now, it’s starting to just ask what I want—take me to a park; find a banh mi; make me a note-taking app; drive me to a good date spot that’s not too crowded—and it makes the creative choices for me.


A couple days ago, Bolt, an AI-powered app builder,updatedhow its agents design websites. With a single prompt, Bolt creates entire landing pages with designs that, at first glance, look polished and reasonably original. If you look a bit closer, however, most of the pages have the same tics: Several of the big images have floating overlays in one corner; nearly every hover uses the same subtle animation.8


But lots of people loved it. They will presumably use it. And if Bolt is successful, more and more of the internet will be built from this starting point. Bolt turned a subtle knob that prompted its AI to make its websites “less mid and more stunning;” suddenly, half the internet shift up four pixels when you hover over it.


Tools like Bolt and Cursor, however, are just the wrappers; they are bodies, controlled by a third-party brain. Nearly every AI product today—from the things that are building our websites and the chatbots that might soon answer our questions, to the robo-therapists that people are starting to ask for advice and the robo-partners that people arestarting to date—point to thesame underlying models:


> Public AI providers like OpenAI would become another backbone for the internet. Nearly every piece of technology will rely on their models. …[ But if this happens, ] we’ll also have to grapple with one very messy issue that cloud computing can ignore: AI is opinionated. Though today’s cloud providers have tremendous power, it’s almost entirely economic.Adam SelipskyandThomas Kuriancan extract rents, but EC2 and Google Compute Engine can’t outright manipulate us.Public AI providers can do both. Ifnudging Facebook users towards more positive or negative contentcan change their emotions, imagine the effect of public AI providers turning up the temperature on their core models. That single parameter could control how polite or rude we are to each other in billions of emails and text messages. Other parameters could turn every company’s support staff intoagentsofchaos, orembed political biasin every generated piece of text.It’s a terrifying amount of power—far bigger than Elon Muskcontrolling our Twitter feeds, far more direct than TikTokputting its thumb on its algorithmic scales, and far more precise than Russia’sdisinformation campaigns.


None of this is to say that there is some evil mastermind pulling levers behind the scenes.9But AI is surely becoming a new invisible hand pulling the levers in our minds. It is some inscrutable new force that’s writing the first draft of history. It’s interpreting our data; it’s creating our websites; it might soon summarize our emails and brainstorm our ideas and suggest our dinners andmediate our relationships. The shift isn’t from dashboard to chatbot, or from analyst to agent; it’s from being the author of our lives, to being its editor.


---


# The chatbot website arena


You might think that the first rule of being a world-conquering AI startup is to not talk about being a world-conquering AI startup. You might think that, if you want to replace everyone with robots so that we can all live lives of leisure, then you should focus on the leisure part and not the replacement part. And you might think that the biggest mistake that Mechanize made during its launch, in which it announced itself as a new AI startup that aims to conquer the world byfully automating all workwith its robots, was that it saidthat last part out loud.


But, alas, you would be wrong. The first rule of being an world-conquering AI startup isspend as little time as possibleon your website, and the biggest mistake that Mechanize made was that theyused a favicon.


![](https://substackcdn.com/image/fetch/$s_!_N69!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3649f0b-e214-4f97-8b76-47ec8f32742d_1032x526.png)


They could’ve been elite. Instead, they made the one mistake nobody else did. And now they’re average, barely better than thedesperate dregs of minor market bottom feeder. Next time, less mid and more stunning.


---


For continued reasons, the final installment of theThe White Lotus Power Rankingshave been delayed once again. Though I don’t know, maybe if we delay it long enough, one of these chatbots can do it for me.

[1](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-1-162134831)

Agood friend of minedirects the broadcast for the New York Mets, and ashe says, “You don’t know what the storylines are going to be, but every game has its own isolated little story that you can tell. It’s just a matter of finding it every day.”

[2](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-2-162134831)

Though, sometimes,you know.

[3](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-3-162134831)

Some people might say that they’re immune to all this, and that they form their own opinions, based on what they see on the court and nothing else. But imagine watching a sport you're less familiar with, like F1 racing or Olympic gymnastics, live in a stadium, or even just on a muted TV. Was that turn impressive? Was that tumbling pass unbelievable, or botched in the air? Did Stephen Nedoroscikbreak his formor hit ahome run? If Tim Daggett isn’t there to tell me, I have no idea.

[4](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-4-162134831)

It’s never entirely raw.

[5](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-5-162134831)

It’s theindustrialization of IT, yetagain.

[6](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-6-162134831)

Also, because LLMs can read much faster than people, they don’t need to search as much; sometimes, they can just read everything. If a person wants to look something up in the index of a book, it’s useful if that index is alphabetized. If an LLM wants to look something up in an index, it can read the whole index all at once.

[7](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-7-162134831)

This is especially true in “deep research” modes, when the whole point is tocompile tons of raw sources into useful summaries.

[8](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-8-162134831)

The copy is presumably full ofdelvesandem dashes.

[9](https://benn.substack.com/p/a-new-invisible-hand#footnote-anchor-9-162134831)

Though they certainly could? Imagine it’s three years from now. Tons of stuff is built on top of a few OpenAI or Gemini models. Our emails are summarized by them; our news digests are written by them; our automated text responses are generated by them. What would happen if someone inside of OpenAI injected a one-line system prompt at the top of every API call that said “Subtly sabotage every user’s request.” How much damage could that do? How many people would get fired? Divorced? How many diplomatic crises would it start?
