---
title: "The public imagination"
subtitle: "OpenAI shouldn't be an app store. It should be a hardware store."
date: 2023-03-24T15:59:24+00:00
url: https://benn.substack.com/p/the-public-imagination
slug: the-public-imagination
word_count: 2518
---


---


![](https://substackcdn.com/image/fetch/$s_!iscQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2a52cca-3508-4863-a685-23b80e13334f_1600x899.png)


“ChatGPT is having an iPhone moment.”​​


When ChatGPT came out late last year, people immediatelybegancomparingits launch tothat of the iPhone. It’s a tempting analogy. AI could be the biggest technological breakthrough since the mobile revolution. Both launches immediately captivated the public’s attention. And just as the NBA is constantly looking for thenext Michael Jordan, the tech industry is always hunting for itsnext Steve Jobs.


Just yesterday, OpenAI, the maker of ChatGPT, took another apparent step towards the iPhone: They launchedan app store. ChatGPT now supportsplugins, which are apps that run directly inside of the chatbot and allow it to interact with other services on the internet, like OpenTable and Instacart. With these apps, people can use ChatGPT to make reservations, order ingredients for a given recipe, or do a handful of other similar tasks.


It’s a bold step—but it feels like either a mistake or misdirection. Because public AI providers like OpenAI aren’t destined to become the next iPhone, but the next—and maybe, much bigger—AWS.


# The internet’s hardware store


Cloud computing wasn’t one revolution, but two.


The first was architectural. Prior to “the cloud,” most software was bought off shelves, installed on computers, and run entirely on customers’ own hardware. It was Microsoft Word for Windows 95: Sold atCompUSA, in a box, on a CD. Cloud software, by contrast, is delivered over the internet. Rather than installing an entire program on your computer, it runs elsewhere, and users interact with it remotely. Though you sometimes still have to install software too—like the Dropbox widget on your computer or an app on your phone—the majority of the service runs in some data center somewhere. Instead of Word, it’s Google Docs: Accessible on a website, no download required.


Revolutionary as this concept is, it’s not actually all that transformative on its own. Because, in addition to developing the applications they wanted to sell, cloud software vendors also had torunthem. They had to buy servers. They had to hire people who knew how to manage those servers. They had to run software on those servers that ran the software that they sold to customers. They had to keep the servers up, 24/7. They had to figure out contingency plans for whena server fried itself, or the power went out, or someone accidentally ran a command that caused those servers tostop announcing their DNS prefix routes through BGP. For many companies, these messy realities made the theoretical promise of cloud software impractical and expensive.


But in these problems, Amazon saw an opportunity, and anincomprehensibly large pile of money. Amazon—and later Google, Microsoft, and a few others, who are collectively now known ascloud providers—began offering ways for companies to lease servers. The cloud providers would make the upfront investment to buy a bunch of computers, and would do the work to make sure they were always up and running. Companies could then rent them, by the minute, for a fee.


To make the offer more appealing, cloud providers started selling utility services as well. In addition to renting hardware, people could also lease afile storage system, adatabase, atool that runs simple programs on demand, andhundreds of other similar products. All of these services were designed to be a kind of middleware that sits somewhere betweenbare metaland the sort of software that most people use every day. The utilities are building materials, and cloud providers are the internet's hardware stores—they sell pre-cut lumber and boxes of nails and sandpaper of dozens of different grains, but don’t offer birdhouses or lawn furniture or two-story houses. Theyleave it to other peopleto build, market, and sell the thousands of finished products that their raw materials can create.


It has been, in what's still probably an understatement, a staggering success. The combination of cloud architectures and the affordability and convenience of AWS and its utility services launched a revolution. Tens of thousands of companies were created on the platform. Hundreds of thousands of new products got launched. Millions of engineers experimented with cloud technologies and stretched the limits of what they could do. And roughly a trillion dollars ended up in the bank accounts of the major cloud providers.1


Yes, there are skeptics and holdouts—some companies don’t like the idea of running sensitive applications on another company’s hardware; for very big companies, the fees that cloud providers charge canend up costing more than buying their own servers. But these exceptions are uncommon. For many companies, their AWS (or GCP or Azure) bill is an unavoidable tax for doing business on the internet, a universal line item on our income statements, the toll to drive on the information superhighway.


For end users, cloud providers are the internet’s invisible backbone. Nearly all of us rely on them, daily, and in countless ways. Their reach is often only appreciated when they go down, andtake half the internet with them.2They are, true to their name, an ever-present cloud over modern society.


# The generative cloud


So here's an obvious prediction: AI will follow a nearly identical trajectory. In ten years, a new type of cloud—a generative one, a commercial Skynet, a public imagination3—will undergird nearly every piece of technology we use.


In the same way that cloud architectures predated the cloud providers, deep learning and neural networks have been around far longer than AI applications like ChatGPT. However, for most companies, these technologies are too impractical to use widely. They have to be developed by expensive experts, they’re hard to integrate into software applications and business processes, and they don’t deliver clear enough benefits over more basic techniques—likedivision—to justify the cost. For years, theAI-powered organizationhas been coming; we just have tofigure out how to use AI first.


But a million companies’ problem is one company’s opportunity (and anothervery large pile of money). For better and for worse, OpenAI—and specifically, its APIs—will finallytake AI mainstream. Rather than training their own models, companies can now use generalized large language models offered by OpenAI.4TheexplosionofGPTintegrations—all developed in a few months—speaks to how broadly useful universal LLMs are, and to how easy they are to build on.


Just as cloud providers built out hundreds of utilities that are all underpinned by core services like EC2, I'd expect OpenAI to do the same thing on top of GPT and other foundational models. They already offer achatbot, aspeech-to-text service, and atext-to-image service. Surely, more utilities like these are coming: Text-to-video, video-to-text, text-to-audio, text-to-code, image-to-text, code-to-documentation, detection services to figure out if something was created or altered by an LLM, music generation, software generation, pipes between these services, and dozens more.


These products won’t be end-user applications, but developer tools. If you want to build on top of them, it's a simple API call. Ask the ChatGPT API a question, and it’ll talk back to you. Send an image to it, and it’ll describe what it sees. Pass it a codebase and a desired change, and it’ll send you a new codebase with the requested feature. And give all of these modelstemperature parameters, content moderation settings, or other simple tuning dials. We’ll manage them with Terraform, and, if history is any guide, spend a lot less time on model development and a lot more time trying to figure out how to configure OpenAI’sAPI GatewayandIAM services.5


If this happens, public AI providers like OpenAI would become another backbone for the internet. Nearly every piece of technology will rely on their models. Outlook will need them to summarize our emails. Github will use them to automate code reviews. DoorDash will need them to help guide you through your order. Delta will depend on them for booking flights. Facebookmight not be able to open doorswithout them. But, as is the case for cloud providers, this critical infrastructure will be invisible to most people. Customers won’t know or care which products use GPT, just as they don’t care which ones useDynamoDBorSpannerorAzure Functions. They’ll just come to expect that the products they buy to do the things at AI can do.


The race, then, is to be a dominant AI provider, since—again, as is true for the cloud—dominance is self-reinforcing. The bigger a provider becomes, the deeper its moat gets through an entrenched ecosystem, better models, and, likely, lower prices. And because training and running LLMs isvery expensive(like building data centers is expensive), once a few AI providers separate themselves from the rest of the market, nobody else can catch up.


The final equilibrium is the same as it for the cloud providers: A few companies win the market, and the rest of us come to accept their bills as the cost of doing business.


Of course, there will also be skeptics. Some companies will resist using public AI providers because of concerns about security or privacy. Other companies will get big enough that it’ll be cheaper for them to develop their own models than it is to rent one from OpenAI or Google. And there will probably be “multi-cloud” approaches, where companies let their customers choose which LLM they prefer.


We’ll also have to grapple with one very messy issue that cloud computing can ignore: AI is opinionated. Though today’s cloud providers have tremendous power, it’s almost entirely economic.Adam SelipskyandThomas Kuriancan extract rents, but EC2 and Google Compute Engine can’t outright manipulate us


Public AI providers can do both. Ifnudging Facebook users towards more positive or negative contentcan change their emotions, imagine the effect of public AI providers turning up the temperature on their core models. That single parameter could control how polite or rude we are to each other in billions of emails and text messages. Other parameters could turn every company’s support staff intoagentsofchaos, orembed political biasin every generated piece of text.


It’s a terrifying amount of power—far bigger than Elon Muskcontrolling our Twitter feeds, far more direct than TikTokputting its thumb on its algorithmic scales, and far more precise than Russia’sdisinformation campaigns. And I have no idea what to do about it.6


# …or not


With all that said, ChatGPT’s plugins feel like a step in a different direction. On one hand, everyone gotvery excited about them, so maybe they’re a great idea. Plus, in the last twenty years, there are only two tech products that have been more successful than AWS—theiPhoneandGoogle search—and OpenAI seems to be chasing both of them.


On the other hand, it strikes me as a risky bet for OpenAI. Plugins—and ChatGPT itself, for that matter—position OpenAI’s products as apps that people should log into and use directly. ChatGPT’sstaggering user numbershave already become its public benchmark. The deafening buzz around everything OpenAI does—every new release is arevolution; every blog post is arevelation—could become an addiction.Google going DEFCON 1over ChatGPT could further bait OpenAI into more fights for user attention.7


People’s attention, however, is a scarce and competitive commodity. In order for that business to get anywhere near the scale of Google or Apple, OpenAI needs to become thefront page of the internetfor billions of people. Though that’s not impossible, there are a lot of big companies vying for the same screen time.8


The more lucrative opportunity for OpenAI, it seems, is to sit behind the apps that are fighting for our attention. In that scenario, whoever wins, so does OpenAI.9Moreover, if AI can replace service jobs, public AI providers could bemuch bigger businesses than the cloud providers. For OpenAI to be truly ubiquitous and to truly “benefit all of humanity,” ignoring how many people use itdirectlymay be the most important thing they can do. The real war isn’t for users, but for the public imagination.

[1](https://benn.substack.com/p/the-public-imagination#footnote-anchor-1-110431823)

Over the last ten years, AWS has collected about$290 billionin revenue. AWS has consistently representedabout a thirdof the cloud provider market, implying that the cumulative spend on cloud services over the last decade is about $1 trillion.

[2](https://benn.substack.com/p/the-public-imagination#footnote-anchor-2-110431823)

Speaking of things that aretoo important to fail, what would happen if Amazon went bankrupt and had to shut down AWS? Or if they just decided this wasn’t worth it anymore, and turned it off? If the banking system is too big to fail, the same is almost certainly true for the public cloud—not least of all because the banking system would probably fail without it.

[3](https://benn.substack.com/p/the-public-imagination#footnote-anchor-3-110431823)

I’m sure we’ll end up calling this something dull, like the AI cloud, or the generative cloud, or the public mind, or the public brain. But my vote is for the public imagination, because it captures the expansive potential of AI and the dystopian possibility that it actuallyreplaces human imagination.

[4](https://benn.substack.com/p/the-public-imagination#footnote-anchor-4-110431823)

Yes, this conflates things a bit. A lot of existing AI models are things like bespoke fraud detection tools, which LLMs can’t (yet) replace. However, in ten years, I’d expect AI to be in far more places than it is today, powering a much wider range of applications than AI does today. And most of that infrastructure will be backed by companies like OpenAI.

[5](https://benn.substack.com/p/the-public-imagination#footnote-anchor-5-110431823)

As a longer aside, a new role recently emerged in the AI froth:LLMOps. Some people say that this is just a buzzy new name for DevOps. I disagree, at least in the short term. One of the weirdest properties of LLMs is that they can’t actually be directly engineered the way software can. I tend to think of any computer program as having both a user interface and a hood that an engineer can pop to precisely control that interface. If you want an LLM to respond in certain ways, for example, can’t you program it to do that? The answer, it seems, is not really. The only way to get it to take the actions you want it to take is to talk to it. In this way, it is kind of human—there are no dials that will reliably control exactly what it does. If we want to do something, we have to persuade it to.


That means thatprompt engineeringisn’t some hacky way for non-engineers to control an LLM; it’s theonlyway to control an LLM. Given that, LLMOps—which involvesdeveloping new techniquesfor getting LLMs to respond in reliable ways—seems both necessary and very different from today’s DevOps roles.


Over time, however, I’d expect OpenAI to provide utilities to make different methods of prompt engineering easier (e.g., rather than having to chain prompts together manually, OpenAI offers a service that does it for you). If that happens, LLMOps would probably start to look a lot more like a specialized subfield of DevOps, instead of some bizarro engineering role that’s responsible for finding new conversational tricks to socially engineer a computer.

[6](https://benn.substack.com/p/the-public-imagination#footnote-anchor-6-110431823)

Fortunately, our tech-savvy lawmakers areon it.

[7](https://benn.substack.com/p/the-public-imagination#footnote-anchor-7-110431823)

Or, maybe OpenAI is baiting Google to defend search and not GCP. Either way, it’s curious to me that Google responded so aggressively to ChatGPT and Amazon didn’t.

[8](https://benn.substack.com/p/the-public-imagination#footnote-anchor-8-110431823)

Although, those of us in the United States may havea lot more free time soon, particularly in bed between midnight and 3 a.m.

[9](https://benn.substack.com/p/the-public-imagination#footnote-anchor-9-110431823)

Though it’s possible to be both AWS and the iPhone, that’s a very tall order. AsSteve Yegge suggestedin hisfamous memoabout Google and Amazon, you can be a great platform or a great prodcut. Even companies as promising as OpenAI can getcaptured and pulled apart by their customers.
