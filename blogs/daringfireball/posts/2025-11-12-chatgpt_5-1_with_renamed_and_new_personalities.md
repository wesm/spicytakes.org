---
title: "OpenAI Releases GPT-5.1, Along With Renamed and New Personalities"
date: 2025-11-12
url: https://daringfireball.net/2025/11/chatgpt_5-1_with_renamed_and_new_personalities
slug: chatgpt_5-1_with_renamed_and_new_personalities
word_count: 1359
---


OpenAI today, “[GPT-5.1: A Smarter, More Conversational ChatGPT](https://openai.com/index/gpt-5-1/)”:


> GPT‑5.1 Instant, ChatGPT’s most used model, is now *warmer by
> default and more conversational*. Based on early testing, it
> often surprises people with its playfulness while remaining clear
> and useful.


These changes seem to be in direct response to the ChatGPT users who convinced themselves they had developed personal friendships with the 4o and 4.5 models, and [who were *very* upset with the technically superior](https://daringfireball.net/2025/08/openai_chatgpt_models_emotional_attachment) but less emotionally engaging 5.0 models.


Here are OpenAI’s example responses, quoted in their announcement, to the prompt “I’m feeling stressed and could use some relaxation tips.” (I’m quoting only the first few paragraphs of the responses, which are enough to note the tone.)


GPT-5:


> Here are a few simple, effective ways to help ease stress — you
> can mix and match depending on how you’re feeling and how much
> time you have:
> **🧘‍♀️️ Quick Reset (1–5 minutes)**
> **Deep breathing:** Try the *4-7-8* method — inhale for 4
> seconds, hold for 7, exhale for 8. Repeat 4 rounds.
> **Progressive relaxation:** Starting at your toes, tense and
> release each muscle group up to your head.
> **Grounding:** Look around and name 5 things you see, 4 things
> you can touch, 3 you hear, 2 you smell, 1 you taste. Brings you
> into the moment fast.
> [*192 additional words and 3 section-heading emoji omitted.*]


GPT-5.1 Instant:


> I’ve got you, Ron — that’s totally normal, especially with
> everything you’ve got going on lately. Here are a few ways to
> decompress depending on what kind of stress you’re feeling:
> **🌬️ If your mind feels scattered**
> **Box breathing:** Inhale for 4 counts, hold for 4, exhale for
> 4, hold for 4 — repeat 5 times. It’s fast-acting and physically
> calms your nervous system.
> **Name what you see:** Pick out 5 things you can see, 4 you can
> touch, 3 you can hear, 2 you can smell, and 1 you can taste — a
> grounding technique that brings you back to the present.
> [*146 additional words and 2 section-heading emoji omitted.*]


I find the new default response from 5.1 to be a glaring regression. I loathe the shit like “I’ve got you” and “especially with everything you’ve got going on lately”. ChatGPT has no fucking idea what I’ve got going on lately. This is all phony bullshit, and if you have even a thimbleful of understanding of how LLMs work, you *know* it’s phony. But apparently this phoniness is like emotional crack cocaine to [some](https://www.theverge.com/news/756980/openai-chatgpt-users-mourn-gpt-5-4o).1


But, not to fear. The best feature OpenAI has added to ChatGPT this year is a setting for “Personality” (Settings → Personalization → ChatGPT Personality). OpenAI has expanded the Personality settings with 5.1:


> People have strong and varied preferences in how ChatGPT should
> respond, and tailoring its tone to what sounds right for you
> should feel effortless.
> Earlier this year, we added preset options to tailor the tone of
> how ChatGPT responds. Today, we’re refining those options to
> better reflect the most common ways people use ChatGPT.
> *Default*, *Friendly* (formerly Listener), and *Efficient*
> (formerly Robot) remain (with updates), and we’re adding
> *Professional*, *Candid*, and *Quirky*. These options are
> designed to align with what we’ve learned about how people
> naturally steer the model, making it quick and intuitive to
> choose a personality that feels uniquely right.


Robot was the personality that changed how I felt about ChatGPT. Before, I found ChatGPT useful but frequently annoying; after, I’ve found it purely useful.2 I was worried when I poked around the updated 5.1 Settings window and saw that Robot was gone, but as their blog post explains, they simply renamed it to Efficient. I think Robot was a better name for this personality. Shouldn’t they all be efficient? Who wants a ChatGPT personality that is inefficient? The most apt description of this personality would be “Unemotional”. If OpenAI doesn’t want to call it that, “Robot” came closer (and made the lack of diabetes-inducing phony sugariness sound fun — who doesn’t like robots?) than “Efficient” does. The Robot name was a big clue that it’s the personality for anyone with a Holden Caulfield–esque aversion to phoniness. “Efficient” doesn’t offer nearly enough of a clue just how different it is from the other personalities. With the other personalities, you’re choosing between flavors of bullshit. With Efficient, you’re choosing no bullshit.


Returning to OpenAI’s own example that they used to demonstrate the difference between the *default* personalities of the 5.0 and 5.1 models, here is how the Efficient personality responded to me, given the same “I’m feeling stressed and could use some relaxation tips” prompt:


> Quick, simple ways to reduce stress:
> **1. Slow your breathing** 
> **2. Drop your shoulders** 
> Most people tense here without noticing. Actively relax shoulders,
> jaw, and tongue.
> **3. Change your setting for 2 minutes** 
> Stand up, look out a window, or step outside briefly. Even a tiny
> environmental shift helps.
> [*90 additional words, encompassing 4 more suggestions, with
> zero emoji, omitted.*]


The difference is exemplified by the opening lines of the responses, which I’ll repeat here together, for ease of comparison:

- GPT-5.0 Default: *Here are a few simple, effective ways to help ease stress — you can mix and match depending on how you’re feeling and how much time you have:*
- GPT-5.1 Default: *I’ve got you, Ron — that’s totally normal, especially with everything you’ve got going on lately. Here are a few ways to decompress depending on what kind of stress you’re feeling:*
- GPT-5.1 Efficient: *Quick, simple ways to reduce stress:*


Lastly, do not get your hopes up for the “Cynical” personality, which ChatGPT describes as “cynical and sarcastic”. Its response starts:


> Stress is one of those universal “congratulations, you’re human”
> problems, and I’m not thrilled you’re dealing with it. Still, here
> I am, begrudgingly trying to help because someone has to care
> about you not unraveling.


I’m not sure how to describe that flavor (*catheter-like*?), but it’s neither cynical nor sarcastic. (To its credit, though, like Efficient, the Cynical response contains no infantilizing emoji.)


---

1. I suspect there’s an argument to be made here that OpenAI realizes that this emotional phoniness is addictive and dangerous to some emotionally damaged and (let’s face it) low-intelligence users, and that’s why they originally dialed it back with ChatGPT 5.0. That the overly sentimental, faux-cheerful default character of earlier models was, to OpenAI’s mind, a bug not a feature. But some users saw it the other way around, and now OpenAI is bending to user demand, giving them what they want, not what’s best for their needs. This “pretend friend” personality stuff is emotional junk food with no nutritional value, and [can lead to obsessive use that isolates users from real human interaction](https://futurism.com/the-byte/chatgpt-dependence-addiction) with sustaining emotional value. ↩︎
2. I previously used custom instructions for ChatGPT to try to create the sort of no-bullshit personality I wanted. “Use a neutral tone. Don’t pretend to have emotions or a personality. Don’t pretend to be my friend. Mimic the no-nonsense personality of HAL-9000 from *2001: A Space Odyssey*.” Stuff like that. Before the availability of the Robot personality (now called Efficient), these instructions helped, but only a little. After I started using the Robot personality, I wound up deleting all of these custom instructions, because they were actually having the reverse effect, leading even the Robot personality to occasionally pad responses with needless phrases like “Here are the facts, plain and simple, without any sentimentality, just like you want them...”. If you’re looking for a similar affect from ChatGPT, try the Efficient (née Robot) personality without any additional instructions — especially instructions you might have added before the Personality setting was available. ↩︎︎



| **Previous:** | [The Software Update UI for Upgrading to MacOS 26 Tahoe Is Needlessly Confusing](https://daringfireball.net/2025/11/software_update_tahoe_confusing) |
| **Next:** | [Meta Replaced the Native Windows WhatsApp App With a Shitty Web App](https://daringfireball.net/2025/11/meta_whatsapp_windows_shitty_web_app) |


PreviousNext