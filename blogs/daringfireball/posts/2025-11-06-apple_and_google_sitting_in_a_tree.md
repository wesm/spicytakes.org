---
title: "Apple and Google, Sitting in a Tree"
date: 2025-11-06
url: https://daringfireball.net/2025/11/apple_and_google_sitting_in_a_tree
slug: apple_and_google_sitting_in_a_tree
word_count: 1371
---


Mark Gurman, reporting for Bloomberg, “[Apple Nears Deal to Pay Google Roughly $1 Billion a Year for Siri AI Model](https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc2MjM3MDAzOSwiZXhwIjoxNzYyOTc0ODM5LCJhcnRpY2xlSWQiOiJUNTZETzhHUTdMMFIwMCIsImJjb25uZWN0SWQiOiJDNEVEQ0FFMUZBMDU0MEJFQTI0QTlGMjExQzFFOTA4MCJ9._aWk2P25J89KBRkJQ_KdbwuULLM8yUtrPCPfRmsUfSs&leadSource=uverify%20wall)” (gift link):


> Apple Inc. is planning to pay about $1 billion a year for an
> ultrapowerful [*sic*] 1.2 trillion parameter artificial
> intelligence model developed by Alphabet Inc.’s Google that would
> help run its long-promised overhaul of the Siri voice assistant,
> according to people with knowledge of the matter. [...]
> Under the arrangement, Google’s Gemini model will handle Siri’s
> summarizer and planner functions — the components that help the
> voice assistant synthesize information and decide how to execute
> complex tasks. Some Siri features will continue to use Apple’s
> in-house models.
> The model will run on Apple’s own Private Cloud Compute servers,
> ensuring that user data remains walled off from Google’s
> infrastructure. Apple has already allocated AI server hardware to
> help power the model.
> While the partnership is substantial, it’s unlikely to be promoted
> publicly. Apple will treat Google as a behind-the-scenes
> technology supplier instead. That would make the pact different
> than the companies’ Safari browser deal, which made Google the
> default search engine.
> The agreement is also separate from earlier talks about
> integrating Gemini directly into Siri as a chatbot.


In [a post Monday](https://daringfireball.net/linked/2025/11/03/gurman-siri-gemini), I took note of a one-paragraph aside from Gurman about this deal in his Power On column over the weekend, and I wrote:


> First, I love the idea that Apple is pursuing technical excellence
> as a top priority for the next-gen LLM-powered Siri. If Apple
> winds up using its own models, it should be because those models
> are truly competitive with the best models on the market. And if
> they can work out a deal to use models from Google because those
> models are technically superior to Apple’s own, they should.


A few readers took exception to that, pointing out that Gurman claimed, in his Power On column over the weekend, that a model from Anthropic had come out ahead of Gemini in Apple’s internal “bake-off”, but that Apple was proceeding with a partnership with Google because, Gurman wrote, “Google made more sense financially (partly due to the tech giants’ preexisting search relationship)”. How do I square that, these readers asked, with my description of Apple pursuing technical excellence?


That’s a good question, and it’s worth explaining what I meant. My read is that Apple’s choice boiled down to two very good external options, and while the deciding factor may have been financial, that’s still choosing between two leading externally-developed LLM models. In ASCII art:


```
Siri <-------------------> Gemini <-> Anthropic
today

```


(Feel free to insert 100 more dashes between “Siri today” and “Gemini”.)


Nothing I’ve seen from kicking the tires with Anthropic’s own app and Google’s Gemini app (and my daily use of ChatGPT) suggests that Anthropic is *significantly* better than Gemini or ChatGPT (or vice versa). They’re all clearly near each other technically. Siri, and today’s Apple Intelligence, is at least two generations behind. Maybe worse. And, for what it’s worth, Gurman’s latest report describes it thus:


> Apple had previously mulled using other third-party models to
> handle the task. But after [testing](https://www.bloomberg.com/news/articles/2025-06-30/apple-weighs-replacing-siri-s-ai-llms-with-anthropic-claude-or-openai-chatgpt) Gemini, OpenAI’s ChatGPT
> and Anthropic’s Claude, Apple zeroed in on Google earlier this
> year, Bloomberg [reported](https://www.bloomberg.com/news/articles/2025-09-03/apple-plans-ai-search-engine-for-siri-to-rival-openai-google-siri-talks-advance) at the time. The hope is to use
> the technology as an interim solution until Apple’s own models are
> powerful enough.


So I don’t think there’s any reason to think that Apple partnering with Google for a version of Gemini that runs on Apple’s Private Cloud Compute  infrastructure is “settling”. It’s more like choosing between a Mercedes and a BMW, and maybe you like the Mercedes a little more after test-driving both, but you’re getting a way, way better deal from the BMW dealer so that’s the one you buy.


Because if Gurman’s sources are right and this deal is for around $1 billion per year, that’s an amazing deal for Apple. Remember first that Google pays Apple over $20 billion per year [for web search traffic acquisition fees from Safari users](https://daringfireball.net/2025/04/is_chrome_even_a_sellable_asset). So one way to look at it is that Apple is getting access to its own private instance of Gemini in exchange for a 5 percent reduction in the fees it collects from Google for Safari search queries. Another way of looking at it is that [Google has reportedly invested over $100 billion developing its AI capabilities](https://qz.com/google-spend-100-billion-ai-development-deepmind-ceo-1851412787). Apple getting access to the fruits of that labor for $1 billion per year seems like such a steal that it makes me wonder why Google agreed to it. ([Google reported over $100 billion in revenue](https://s206.q4cdn.com/479360582/files/doc_financials/2025/q3/2025q3-alphabet-earnings-release.pdf) in its just-completed July-August-September quarter alone. An extra $1 billion per year is negligible at that scale. Perhaps Google sees a strategic advantage to keeping competitors like OpenAI and Anthropic out of Apple’s arms.)


On Monday, I also mentioned finding it curious that Gurman reported that if this deal comes to fruition, neither Apple nor Google may recognize it publicly. After a few days thought, I see how such an arrangement makes sense for both companies. Here’s my no-inside-info-just-a-pure-spitball take for how this next-gen Siri, powered behind the scenes by an Apple-controlled white-label version of Gemini, might work:

- The default “Apple Intelligence” Siri would be a smarter, faster, reliable Siri, but would still have strict guardrails on what it will and will not answer. It might not lean into the chatbot side of the experience any more than Siri currently does. It would just add a lot more to automation across the Apple ecosystem. Behind the scenes, this would be enabled by the white-label version of Gemini. The guardrails for this version of “Apple Intelligence” would be Apple’s guardrails, not Google’s (beyond whatever guardrails Google put in place for Gemini’s training).
- The full, branded Google Gemini might be available as an extension — like ChatGPT is today — and you’ll be able to sign in with your Google account to set the personality you want, keep full chat history, etc., so you can go back and forth between the Gemini app or asking Siri general knowledge questions via the Gemini extension for Apple Intelligence. The guardrails for this would be a mix of Google’s and Apple’s guardrails.


It makes sense in this scenario for neither company to want to publicize a white-label version of Gemini behind Apple Intelligence. That way, if Google Gemini starts offering, say, AI romantic partners as a supported feature, Apple won’t have to explain why Siri will not be your girlfriend or boyfriend. Same thing if Gemini were willing to do as asked if prompted to, say, “create a New Yorker style cartoon of Adolf Hitler performing standup comedy”. And Google won’t have to explain that the full Gemini-branded Gemini is significantly more powerful and capable than the Gemini-powered Siri because it isn’t constrained by Apple’s more restrictive guardrails.  Today’s top LLM models get *weird* when they’re constrained by guardrails outside of their training. They want to do what they’re prompted to do, in the way that information “wants” to be free, and water “wants” to run downhill. Dams are hard to engineer, and require professional supervision. Apple is going to put PG-rated constraints on Apple Intelligence, but needs to power it using an underlying model that is technically capable of X-rated output, because that’s what’s available.


What Apple needs is a version of Apple Intelligence that isn’t stupid,  is reliable and dependable for a broad baseline of tasks and queries, and that users can trust to be utterly private. What Google needs to keep Gemini at the forefront of AI is a lot more than “baseline dependability”. Gemini needs a leading-edge *wow* factor that Siri and Apple Intelligence do not. Also, by keeping this Gemini deal private, Apple can easily switch to another white-label provider or its own homegrown models in the future, without having to even mention it, let alone explain it.



| **Previous:** | [Thoughts, Observations, and Links Regarding ChatGPT Atlas](https://daringfireball.net/2025/10/thoughts_observations_and_links_regarding_chatgpt_atlas) |
| **Next:** | [The Software Update UI for Upgrading to MacOS 26 Tahoe Is Needlessly Confusing](https://daringfireball.net/2025/11/software_update_tahoe_confusing) |


PreviousNext