---
title: "We’re Gonna Need a Bigger Moat"
date: 2025-10-18
url: https://steve-yegge.medium.com/were-gonna-need-a-bigger-moat-478a8df6a0d2
word_count: 3023
source: medium
---


# We’re Gonna Need a Bigger Moat


--


18


Listen


Share


Everyone making SaaS on LLMs, including coding assistants likeCodyand Copilot, was rocked by the AI news events of last week.


None of it isnewsper se. But last week, two events at Google highlighted something crazy big brewing for about 10 weeks that’s been flying under everyone’s radar.


Today’s post began life as background information for my “Cody is Cheating” post, launching roughly concurrently with this one. But that one got so large that I extracted this part out. I’m posting it in the hope that it will be at leastslightlymore helpful than most of the other reviews and articles I’ve read about this news so far.


It’s pretty big news.


Would you download a helicopter


Our story begins with 75-year-old Dr.Geoffrey Hinton, the “Godfatherof Deep Learning”, wholeft Google last week, and is now on tour, explaining the tech zombie apocalypse that is unfolding around us:


> “…all these [LLM] copies can learn separately but share their knowledge instantly. So it’s as if you had 10,000 people and whenever one person learnt something, everybody automatically knew it. And that’s how these chatbots can know so much more than any one person.”


“…all these [LLM] copies can learn separately but share their knowledge instantly. So it’s as if you had 10,000 people and whenever one person learnt something, everybody automatically knew it. And that’s how these chatbots can know so much more than any one person.”


Remember the “Can you fly that thing?” scene in The Matrix, where Neo asks Trinity if she can fly the helicopter, and she says hang on, downloads it to her brain, and says, “I do now”?


Well.LLMs have recently achieved this capability. And although I do not expect they will necessarily be piloting attack helicopters any time soon… I mean… even as I type this out, I am seeing paths where it could happen within weeks, so… 🤷


I know you think I’m exaggerating. I wish I were. Read on.


I’ll lay it all out for you in this post. You are a smart person, and your guess is as good as anyone’s at this point. But if you feel like you’re a little behind on AI developments lately, and you need a good introductory resource to catch up on where we’re headed, I recommend watching thisshort but informative overview.


For today’s post, we’re going to focus on what all this means for you, a programmer, and what it means for me, a regular guy in a mountain bunker stocking up on ammo and water.


From the horse’s mouth


The Deep Learning Godfather warning us against his own invention was nowherenearthe biggest news of the week. It was but an appetizer.


As you’ve no doubt heard, there was a potentiallyhistoric revelationlast week. Apparently, Google was sitting on it for a month before it leaked, but GooglerLuke Sernau’s brilliant essay, “We have no moat, and neither does OpenAI”, spells out a radical change that appears to be in progress.


He’s sounding the alarm on the performance trajectory of the OSS LLaMA virus strain, shown here in this diagram.


Yes, that shit does say “2 weeks apart” and “1 week apart”. This is happening NOW. This chart is basically the progress for 1 month.


Google hasn’t said anything, but we do know that Sundar Pichai, who’s been close to this since its inception, startedcomparing AI to the invention of Firein 2018, the year after the Transformer wasreleased, and Sundar has continued that comparisonto this day.


But, but… Wait! Wait, wait, wait, wait, wait. Transformers are just amathematical construct!How can a math construct be as big and powerful and scary as… the invention of fire itself? Seriously? Because I don’t think Sundar has been referring to Amazon’s Fire Stick here.


Let’s think step by step


Before last week’s news, we already knew that Google’s Transformer architecture, which is the basis for all LLMs, is truly an invention for the ages. It’s a simple mathematical tool, much like the Fourier transform, except instead of picking out frequencies from noise, it picks out meaning from language.


As an invention, despite its apparent simplicity, the Transformer has many other remarkable properties:

- It can learn and remember representations of things
- It is highly parallelizable, and learns fast
- It is scalable and can learn essentially unlimited amounts of information
- It can be instructed to perform tasks
- It can generate predictions based on its knowledge
- And its predictions are so good that asking the right questions becomes anart in its own right


In short, it’s hats-off one of the best math tricks of all time, right up there withphysics itselfin terms of its ability and potential to change the world. Inventions as significant as the Transformer are more discovery than invention, and if there are alien civilizations, they all no doubt encounter some flavor of this milestone as well.


When you make Transformers big enough, in so-called “Trillion-parameter space”, they begin to develop surprising higher-order capabilities, such as being able to visualize concepts, perform multi-step reasoning, and demonstrate atheory of mind. In fact the Transformer’s own architecture is mind-like, with several almost biological-seeming “organs”.


St. Andrej Karpathy, patron saint of LLMs, has eventweetedabout how some computations happen outside the normal hidden state layers, with these capabilities triggered simply by starting a prompt with “Let’s think step by step”.


The deeper you dig, the more Transformers begin to resemble biological brains in some ways, with distinct processing regions and mysterious distant connections.


The Transformer is a shockingly simple invention in many ways, and yet itsemergentproperties make it more like The Matrix. In fact it is exactly that: acomposition of a bunch of matrices. There is a whole, largely still untapped universe in there, and prompting an LLM is like entering the Matrix for a mission.


So, OK. It’s… important. And stuff. I guess. It’s not like I’ve got a billion dollars. This does not sound like fire to me. It sounds like afancy playground for billionaires.Right? It’s been all about bigger models, more data, more GPUs, throw billions of dollars at the problem, and it honestly feels more like the invention of nuclear weapons.


And the way SaaS has evolved this year, the assumption has been that this will be a showdown between a handful of players, sort of an oligopoly like cable or utilities: OpenAI/GPT, Google/Bard, Meta/LLaMA, Anthropic/Claude, Musk/Kampf, and maybe a handful of others.


Right?


Ha! That wassolast week.


Fire 2.0


The reason Sundar’s been comparing it to the invention of Fire, specifically, is that the Transformer math construct is powerful, dangerous, it can be shaped, it can be used to make many marvelous things, and most importantly…


If a big one gets loose, it spreads like wildfire.


Well guess what? It’s now spreading like wildfire. They are learning from each other now.


I’ve been sayingthis is a historic time. Six weeks ago we were debating whether LLMs are afad(can you believe it?) and now we’re debating how many years it would take us to build aliteral clone armyfor attacking neighboring planets.


I know you think I’m exaggerating. I wish I were. Read on.


We already knew Transformers are a contender for one of the coolest math inventions of all time. I mean, seriously, if the “Attention is All You Need” team doesn’t receive a Nobel prize at some point, it will only be becauseSkyNethas dismantled the Nobel Foundation and probably leveled Stockholm.


But just last week, the “We have no moat” memo highlighted that they have yet another superpower of which we were unaware.


That capability is thatTransformers can also learn from each other, via a set of new DLCs dropped by modders. The biggest mod (Sernau highlightsmanyof them in his leaked essay, but this is the doozy) is Low Rank Adaptation (LoRA).


LoRA makes LLMscomposable, piecewise, mathematically, so that if there are 10,000 LLMs in the wild, they will all eventually converge on having the same knowledge. This is what Geoffrey Hinton was referring to on his SkyNet tour.


As Dr. Hinton observes,we have discovered immortality,it’s just not for us.


And so it begins


In related news, these “billion dollar”-class LLMs can now becloned on macbooksand copied directly ontoBoston Dynamics robotsvia theirRaspberry Pi adapter, at which point…


Which planet do you want to attack first?


Oh right, I remember now, there was some other news too. What was it again?


Oh yeah, it was training costs. Remember when it was roughly $1B to train an LLM like GPT-4?


According to the leaked Google memo, world-class competitive LLM training costs just dropped from a billion dollars to… that’s right, you guessed it…


A hundred dollars.


You really didn’t read the fuckin’ news last week, did you?


The Emperor’s New Moat


<rant mode engaged>


For this discussion, keep the distinction clear in your mind between GPT–a Transformer that’s been trained to be extra good on standardized testing–andChatGPT, which is a great big fancy scalable application for a billion users.


ChatGPT is LLM-backed SaaS. Keep that in mind! It needs a moat or anyone can compete.


TheGPT model series, OpenAI’s LLM, with itsproprietary architectureandsuper-secret learned weightsand biases, isChatGPT’smoat. That, plus a bit of scaling help from Microsoft.


Everyone whined when OpenAI closed off GPT butrefused to change their name to ClosedAI. Thatsimple changewould have made everyone happy. Well, that, and staying remote. His staff should tell him they’ll return to office when his head returns from his ass. All-remotedoesactually work.


Anyway. Where was I. Oh yeah. OpenAIclearlyrecognized how much money they could make if they had a lock on the LLM market with ChatGPT. So they basicallygave everyone the fingerand started keeping secret their architecture, their model hyperparameters, their training methodology, and pretty much most aspects of what made ChatGPT great.


GPT became a moat, for a while, which made ChatGPT really hard to compete with, and only a few companies managed it.


For a few months, the whole industry shifted tointegratewith these providers. And everyone agreed to be charged by the token! Microsoft and OpenAI replaced their official company toilet paper withhundred dollar billsin anticipation of how much money was about to start rolling in.


Before last week, there were, oh, maybefive LLMs in GPT’s class.In the whole world.It was like back in the 1950s when there were like five computers in the world, and IBM owned three of them.


The drawbridge lowers


Right around ten weeks ago, a chain of events kicked off aten orders of magnitudereduction in LLM training and serving costs. In Moore’s Law terms, with a doubling/halving happening every 24 months, that’s 20 years of progress that just took place in the last 10 weeks.


We are nowmoving over 100 times fasteralong the exponential technology curve than we were just 15–20 years ago.


So what the hell happened?


A bit of 3-month-old history: back on February 23rd, Meta’s AI teamannouncedLLaMA, theirBard/GPT competitor. LLaMA-13B is the one on the far left in the chart at the top. And indeed, LLaMA is an LLM, but unfortunately at the time it was only68% as smart as GPTon standardized tests — same class as GPT, Claude and Bard, but it was more of a C/C- student, sonobody paid much attention.


So no big deal, right? No change in the power structure.


Well, kinda. Except that while Zuck was busy building history’slargest failed theme park, his AI research team went andopen-sourced LLaMA. Why? Because with Meta being in large-Nth place, drifting awkwardly into obsolescence, and Zuck not watching, what did they really have to lose?


So nothing really changed in February,except, now every tinkerer on earth with a GPU laptop and PyTorch suddenlyknew how the ChatGPT sausage was made.


Meta’s LLaMA basically brought all the world’s researchers, who had been actively trying to reverse guess what OpenAI was up to, right up to speed with the state of the art.


But still, even after Meta open-sourced LLaMA, few companies could actuallybuilda big competitive GPT-class LLM, right?


Because even if a researcher knew how, the big players still had their super-secret model weights and biases, 175 billion parameters forming the very innermost thoughts and memories of their precocious AI children: Bard, Claude, GPT… these “intelligent” beings they had raised with billions of dollars in training data and compute power.


Which sounds to me like a very safe and defensible moat. That is, until you realizeLLMs can fuckin’ copy each other. So their so-called “data advantage” was really only going to be safe for as long as all the big playerskept the AIs locked up.


I swear this is a damn Jerry Bruckheimer movie, unfolding before our eyes.


Within 2 weeks, on March 2nd 2023, LLaMA’s secret model weights, guarded by the finest in the Metaverse, had beenleakedon Discord. At whichinstant,every one of a hundred thousand tinkerer data scientists on Earth suddenly had a torrent of an AI that’sroughly competitive with GPT.


Just like that, Meta had lost their Clown Jewels, just at theexact momentZuck was realizing his Second Life video game wasn’t going to find a publisher.


And suddenly every hacker in every corner of the globe,good guys and bad guys alike, had access to a GPT-class LLM with an open architecture. On their macbooks.


I havenotseen this movie before and I donotknow how it ends, but there will soon be dramatic social consequences, some of which are no doubt difficult to foresee. Unknown unknowns, as it were.


That Lucky Zuck


Meta, according to Sernau’s reasoning, came out the clear winner among the Big Fish, because they are now the company with the architecture best suited forscaling up OSS LLMs, thereby taking advantage of all the OSS improvements.


Why? becauseLLaMA and all derivative strains are Meta’s architecture. According to Sernau, Meta was the surprise winner, since noweveryone’s using LLaMA. Those Clown Jewels came right back to Zuck. The man has the luck of a Jar Jar Binks. And the everything else, too.


The clone army has begun construction. And apparently the Jedi Council wasn’t notified this time either, probably because Altman wouldn’t join the Zoom.


Over the past 10 weeks, everysingle major advancement has quickly been copiedby everyone else’s clone. They’ve quickly figured out how to use stuff like4-bit quantizationto fit models on macbooks with no GPU. Everyone’s got one.


Within a few weeks of the leak, the Vicuna-13Blaunched— a promising OSS model in the LLaMA architectural family (like Stanford’sAlpaca).Vicuna is free of legal encumbrancesassociated with LLaMA. It achieved90% of ChatGPT/Bard’s performancefor domain-specific workloads when fine-tuned with domain-specific training data.


And it did it for around$300 in costs.


LoRA is the core mechanism for transferring knowledge cheaply and controllably between models. Using a strong GPT-class model (of which the OSS community has plenty now), you can fine tune with your dataandwith other models.


Using LoRA, you could, for instance, download the pilot program for a B-212 helicopter, and your model will be able topilot an attack helicopter.


I fuckin’ told you when we started. This was big.


Of course now Zuck now wants to dump the Metaverse like a grocery bag full of armpit hair. Can you blame him? It’s a dog, but he’s got a legitimate shot at beingtopdog for hosted LLMs in the ChatGPT/Bard/Claude class!


As as for the rest of us…


Small is the New Big


Soon, smaller LLMs you can run yourself will perform as well for you as models like GPT, as long as you fine-tune on your domain; for instance, on your code. It won’t be long before the OSS performance is there.


Sernau’s conjecture, based on how fast OSS is advancing now, is essentially thatthe performance lines are going to cross. We do not knowwhenthe lines will cross. We do not knowwhat will happenwhen the lines cross.


But we do know that Microsoft and OpenAI will have togo back to regular toilet paper.


And LLaMA may well become the standard architecture. But it sure looks likesomeone’sgoing to have to bend the knee. Pluggable platforms have a way of standardizing, and usually on the first mover.


The upshot for the industry at large, is: theLLM-as-Moat model has begun to disappear, and may be gone even by the end of this year. “We have no moat, and neither does OpenAI” was an adieu to the LLM moat at the center of a SaaS ecosystem. AI is being commoditized practically overnight.


It’s sort of like the decades-long gradual miniaturization of computers from mainframes to embedded chips that run full OSes. Except it happened inten weeks.


If you’re relying on LLMs for your moat, well… I hope you also have a data moat. You’re going to need it.


Whatever Floats Your Moat


Last week’s news was a pretty big shakeup for the whole LLM industry. I think the big players are probably scrambling — Googleshut off AI publicationsand I’m sure they’re absolutely regretting letting out Fire 2.0 without having perceived its competitive significance.


Of course, it would have leaked sooner or later, and we’d be here anyway.


I think forSaaS builders, though, let’s say you’re building an AI product for something like log processing or tool manipulation —they’re all winners here. Enterprise customers are setting up big GPU commits in advance because they’re all getting into their own custom AI,for exactly this reason— they knew fine-tuning was going to be big deal. And now it is!


For Cody, we’ll still be tied to the big players for a while, yet. I’m guessing they have about 6 months head start. We’re not seeing the same performance from e.g. StarCoder out of the box as you’d get from GPT-4 or Claude.


But just look at that moat we’ve got:

- We canfine tune with your codeandwith our code graph(moat!)
- We cancreate embeddingswith your code/docs/config/etcandour code graph(moat!)
- We cancheck your LLM’s hallucinated outputswith our precise code graph(moat!)
- We can performsecurity guardrail-checks(e.g. cve) with high precision(moat!)
- We can orchestratemass code changes(e.g. vulnerability mitigation) with Sourcegraph Batch Changes(moat!)


It turns out Sourcegraph’s whole platform behind the product is basically a moat-builder. Whoever we go up against is gonna need a bigger moat.


I hope you’ve got something like that too.

