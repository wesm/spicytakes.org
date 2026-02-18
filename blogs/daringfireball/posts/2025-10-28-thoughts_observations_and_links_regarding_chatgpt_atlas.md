---
title: "Thoughts, Observations, and Links Regarding ChatGPT Atlas"
date: 2025-10-28
url: https://daringfireball.net/2025/10/thoughts_observations_and_links_regarding_chatgpt_atlas
slug: thoughts_observations_and_links_regarding_chatgpt_atlas
word_count: 1500
---


OpenAI, [one week ago](https://openai.com/index/introducing-chatgpt-atlas/):


> Today we’re introducing ChatGPT Atlas, a new web browser built
> with ChatGPT at its core.
> AI gives us a rare moment to rethink what it means to use the web.
> Last year, we added search in ChatGPT so you could instantly find
> timely information from across the internet — and it quickly
> became one of our most-used features. But your browser is where
> all of your work, tools, and context come together. A browser
> built with ChatGPT takes us closer to a true super-assistant that
> understands your world and helps you achieve your goals.


A few minutes into [the 22-minute introduction video](https://www.youtube.com/live/8UWKxJbjriY), Ben Goodger,1 engineering lead for Atlas, says:


> “We wanted to make sure that Atlas didn’t feel like your old
> browser, just with a chat button that was bolted on. But instead,
> we made ChatGPT the beating heart of Atlas.”


After giving it a try over the last week, to me Atlas feels like … Chrome with a chat button bolted on. I do not see the appeal, at all, despite being a daily user of ChatGPT. Atlas offers nothing to me that’s better than using Safari as a standalone browser and [ChatGPT’s excellent native Mac app](https://chatgpt.com/download/) as a standalone AI chatbot. But, for me, my browser is *not* “where all of [my] work, tools, and context come together”. I use an email app for email, a notes app for notes, a text editor and blog editor for writing and programming, a photos app for my photo library, a native feed reader app for feed reading, etc. My web browser is for browsing pages on the web. Perhaps this sort of browser/chat hybrid appeals better to people who live the majority of their desktop-computing lives in browser tabs.

- The main interface isn’t a combo search/location field, but rather a chat/location field. Instead of getting search results for a query, you get a chat response. If I wanted this I’d just ask my prompt in ChatGPT. Oftentimes — usually, even — I really do want a list of search results, and I want them fast. ChatGPT responses in Atlas are not a list of web pages, and are — compared to Google Search or my preferred search engine, Kagi — very slow. ChatGPT is many things but a good search engine replacement it is not. But that seems to be the entire premise of Atlas.
- Atlas offers an agent mode where it actually surfs the web for you. One of the demos from their launch video involved getting a list of ingredients from a recipe on a web page, and then allowing Atlas to buy all those ingredients for you. That seems crazy to me. Do not want.
- Atlas is a Chromium browser, supports Chrome extensions, and but currently is only available for the Mac. It’s not particularly Mac-like though, [as Michael Tsai notes](https://mjtsai.com/blog/2025/10/22/chatgpt-atlas/):

Alas, it doesn’t support AppleScript and has System Settings–style
preferences.

System Settings-style preferences are certainly better than Chrome-style “settings in a web page tab”, though. Also, in my testing, Atlas doesn’t make good use of Apple Passwords for autofill.
- ChatGPT is [running a promotion that offers users increased rate limits](https://help.openai.com/en/articles/12608430-chatgpt-atlas-default-browser-promotion) if they make — and keep — Atlas their default web browser. I’ve never before seen a web browser offer any sort of incentive like this for making it your default. This promotion strikes me as simultaneously clever and icky.
- [Simon Willison’s initial thoughts](https://simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/) echo my own:

I continue to find this entire category of [browser agents](https://simonwillison.net/tags/browser-agents/)
*deeply* confusing.
The security and privacy risks involved here still feel
insurmountably high to me — I certainly won’t be trusting any of
these products until a bunch of security researchers have given
them a very thorough beating. [...]
I also find these products pretty unexciting to use. I tried out
agent mode and it was like watching a first-time computer user
painstakingly learn to use a mouse for the first time. I have yet
to find my own use-cases for when this kind of interaction feels
useful to me, though I’m not ruling that out.
- Lastly, Anil Dash’s assessment is rather scathing, “[The Browser That’s Anti-Web](https://www.anildash.com/2025/10/22/atlas-anti-web-browser/)”:

In the demo for Atlas, the OpenAI team shows a user trying to find
a Google Doc from their browser history. A normal user would type
keywords like “atlas design” and see their browser show a list of
recent pages. They would recognize the phrase “Google Docs” or the
icon, and click on it to get back to where they were.
But in the OpenAI demo, the team member types out:

search web history for a doc about atlas core design

This is *worse in every conceivable way*. It’s slower, more prone
to error, and redundant. But it also highlights one of the biggest
invisible problems: you’re switching “modes”. Normally, an LLM’s
default mode is to create plausible extrapolations based on its
training data. Basically, it’s supposed to make things up. But
this demo has to explicitly walk you through “now it’s time to go
search my browser history” because it’s coercing the AI to look
through local content.

Chat is a great interface for, well, chatting. People love texting. And it turns out that chat conversations are a very good user interface for interacting with LLMs. We humans enjoy texting with other humans, and we enjoy texting with LLMs. But typed-out text commands are not a good user interface at all for browsing the web. We had an entirely text-based Internet before the World Wide Web, and the point-and-click visual metaphor of the Web won out.
Dash, later on:

It’s no coincidence that hundreds of people who work at OpenAI,
including many of the most powerful executives, are alumni of
Facebook/Meta, especially during the era of many of that
company’s most egregious abuses of people’s privacy. In the
marketing materials and demonstrations of Atlas, OpenAI’s team
describes the browser as being able to be your “agent”,
performing tasks on your behalf.
But in reality, *you are the agent for ChatGPT*.
During setup, Atlas pushes very aggressively for you to turn on
“memories” (where it tracks and stores everything you do and uses
it to train an AI model about you) and to enable “Ask ChatGPT” on
any website, where it’s following along with you as you browse the
web. By keeping the ChatGPT sidebar open while you browse, and
giving it permission to look over your shoulder, OpenAI can
suddenly access all kinds of things on the internet that they
could never get to on their own.

This jibes with my impression after giving Atlas a try. The point of it doesn’t seem to be to provide a better web browser for me to use, but rather, to provide ChatGPT with the personal context of my digital life that it otherwise couldn’t get.


---


That last point raises the question of just how stable we should consider the Apple-OpenAI partnership for ChatGPT-backed Apple Intelligence features. Apple’s goal for a “more personalized Siri” — [the whole thing](https://daringfireball.net/2025/03/something_is_rotten_in_the_state_of_cupertino) Apple promised at WWDC 2024 but had to postpone for a full year early this year — is for the ecosystem of native apps on Apple platforms, particularly iOS and MacOS, to serve as the personal knowledge context for personalized AI features through [App Intents](https://developer.apple.com/documentation/appintents). That’s the basis for the “When is my mom’s flight arriving?” type of interaction that Apple has promised, but still has not delivered. The premise of Atlas (and its brethren AI-integrated browsers like [The Browser Company’s Dia](https://www.diabrowser.com/) and [Perplexity’s Comet](https://www.perplexity.ai/comet/)) is that you should live your entire desktop computing life inside your browser, which in turn will give the AI agent that is integrated with your browser the contextual knowledge for your entire life.


OpenAI’s ambitions are clearly at odds with Apple’s.


OpenAI’s advantage here is that ChatGPT is the most popular LLM chatbot in the world, by far. Apple doesn’t even have an LLM chatbot of its own, let alone a good or popular one. But Apple’s advantage is a big one: most people don’t live their digital lives on desktop computers, where it’s an option to do most things in a web browser. Most people’s primary computing devices are their phones — and even for people whose primary devices are desktop computers, their phones are much-used satellite devices. And on both iOS and Android alike, people live their mobile digital lives through native apps, not websites.


---

1. Goodger is a titanic figure in the web browser world, having helped [create Mozilla Firefox](https://web.archive.org/web/20111116060139/http://weblogs.mozillazine.org/ben/archives/009698.html) in the early 2000s, and then [joining Google in 2005](https://web.archive.org/web/20050210015629/http://weblogs.mozillazine.org/ben/archives/007366.html) to help create Chrome. [I noted last year](https://daringfireball.net/linked/2024/11/26/openai-browser) that Goodger leaving Google for OpenAI was a pretty clear sign that OpenAI was creating its own web browser. ↩︎



| **Previous:** | [Apple Loses Landmark U.K. Lawsuit Over App Store Commissions](https://daringfireball.net/2025/10/apple_uk_lawsuit_app_store_commissions) |
| **Next:** | [Apple and Google, Sitting in a Tree](https://daringfireball.net/2025/11/apple_and_google_sitting_in_a_tree) |


PreviousNext