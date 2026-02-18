---
title: "Training Large Language Models on the Public Web"
date: 2024-06-21
url: https://daringfireball.net/2024/06/training_large_language_models_on_the_public_web
slug: training_large_language_models_on_the_public_web
word_count: 854
---


Yesterday, quoting Anthropic’s announcement of their impressive new model, Claude 3.5 Sonnet, [I wrote](https://daringfireball.net/linked/2024/06/20/claude-3-5-sonnet):


> Also, from the bottom of the post, this interesting nugget:
> One of the core constitutional principles that guides our AI model
> development is privacy. We do not train our generative models on
> user-submitted data unless a user gives us explicit permission to
> do so. To date we have not used any customer or user-submitted
> data to train our generative models.
> [Even Apple can’t say that](https://www.macstories.net/linked/apple-details-its-ai-foundation-models-and-applebot-web-scraping/).


It now seems clear that I misread Anthropic’s statement. I wrongly interpreted this as implying that Claude was not trained on public web data. [Here is Anthropic’s FAQ on training data](https://support.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training):


> Large language models such as Claude need to be “trained” on text
> so that they can learn the patterns and connections between words.
> This training is important so that the model performs effectively
> and safely.
> While it is not our intention to “train” our models on personal
> data specifically, training data for our large language models,
> like others, can include web-based data that may contain publicly
> available personal data. We train our models using data from three
> sources:
> Publicly available information via the Internet
> Datasets that we license from third party businesses
> Data that our users or crowd workers provide
> We take steps to minimize the privacy impact on individuals
> through the training process. We operate under strict policies and
> guidelines for instance that we do not access password protected
> pages or bypass CAPTCHA controls. We undertake due diligence on
> the data that we license. And we encourage our users not to use
> our products and services to process personal data. Additionally,
> our [models are trained to respect privacy](https://www.anthropic.com/index/claudes-constitution): one of our
> constitutional “principles” at the heart of Claude, based on the
> Universal Declaration of Human Rights, is to choose the response
> that is most respectful of everyone’s privacy, independence,
> reputation, family, property rights, and rights of association.


[Here is Apple, from its announcement last week of their on-device and server foundation models](https://machinelearning.apple.com/research/introducing-apple-foundation-models):


> We train our foundation models on licensed data, including data
> selected to enhance specific features, as well as publicly
> available data collected by our web-crawler, AppleBot. Web
> publishers have [the option to opt out](https://support.apple.com/en-us/119829) of the use of their
> web content for Apple Intelligence training with a data usage
> control.
> We never use our users’ private personal data or user interactions
> when training our foundation models, and we apply filters to
> remove personally identifiable information like social security
> and credit card numbers that are publicly available on the
> Internet. We also filter profanity and other low-quality content
> to prevent its inclusion in the training corpus. In addition to
> filtering, we perform data extraction, deduplication, and the
> application of a model-based classifier to identify high quality
> documents.


This puts Apple in the same boat as Anthropic in terms of using public pages on the web as training sources. Some writers and creators object to this — [including Federico Viticci](https://machinelearning.apple.com/research/introducing-apple-foundation-models), whose piece on MacStories I linked to with my “Even Apple can’t say that” comment yesterday. [Dan Moren wrote a good introduction to blocking these crawling bots](https://sixcolors.com/post/2024/06/excluding-your-website-from-apples-ai-crawler/) with robots.txt directives.


The best argument against Apple’s use of public web pages for model training is that they trained first, but only after announcing Apple Intelligence last week issued the instructions for blocking Applebot for AI training purposes. Apple should clarify whether they plan to re-index the public data they used for training before Apple Intelligence ships in beta this summer. Clearly, a website that bans Applebot-Extended shouldn’t have its data in Apple’s training corpus simply because Applebot crawled it before Apple Intelligence was even announced. It’s fair for public data to be excluded on an opt-out basis, rather than included on an opt-in one, but Apple trained its models on the public web before they allowed for opting out.


But other than that chicken/egg opt-out issue, I don’t object to this. The whole point of the public web is that it’s there to learn from — even if the learner isn’t human. Is there a single LLM that was *not* trained on the public web? To my knowledge there is not, and a model that is ignorant of all information available on the public web would be, well, pretty ignorant of the world. To me the standards for LLMs should be similar to those we hold people to. You’re free to learn from anything I publish, but not free [to plagiarize it](https://daringfireball.net/linked/2024/06/19/robb-knight-perplexity). If you quote it, attribute and link to the source. That’s my standard for AI bots as well. So at the moment, [my robots.txt file](https://daringfireball.net/robots.txt) bans just one: Perplexity.


(I’d block a second, [the hypocrites at Arc](https://www.threads.net/@gruber/post/C8Zoz4jR-EB), if I could figure out how.)



| **Previous:** | [By My Count Trump Is Batting .900 on the Ten Commandments](https://daringfireball.net/2024/06/lousiana_ten_commandments_trump) |
| **Next:** | [WWDC 2024: Apple Intelligence](https://daringfireball.net/2024/06/wwdc24_apple_intelligence) |


PreviousNext