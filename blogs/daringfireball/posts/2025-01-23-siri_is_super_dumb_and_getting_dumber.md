---
title: "Siri Is Super Dumb and Getting Dumber"
date: 2025-01-23
url: https://daringfireball.net/2025/01/siri_is_super_dumb_and_getting_dumber
slug: siri_is_super_dumb_and_getting_dumber
word_count: 2155
---


Writing about the [current state of Apple Intelligence yesterday](https://daringfireball.net/linked/2025/01/22/ios-18-3-macos-153-apple-intelligence-default-onboarding), I mentioned how utterly stupid and laughably wrong Siri is when asked the simple question, “Who won Super Bowl 13?”, and mentioned that that particular example came from a friend. That friend was Paul Kafasis, and he took it and pursued it thoroughly, asking Siri “Who won Super Bowl __?” for every number from 1 through 60.


[His report at One Foot Tsunami documenting the results](https://onefoottsunami.com/2025/01/23/not-so-super-apple/) is utterly damning:


> So, how did Siri do? With the absolute most charitable
> interpretation, Siri correctly provided the winner of just 20 of
> the 58 Super Bowls that have been played. That’s an absolutely
> abysmal 34% completion percentage. If Siri were a quarterback, it
> would be drummed out of the NFL.
> Siri did once manage to get four years in a row correct (Super
> Bowls IX through XII), but only if we give it credit for providing
> the right answer for the wrong reason. More realistically, it
> thrice correctly answered three in a row (Super Bowls V through
> VII, XXXV through XXVII, and LVII through LIX). At its worst, it
> got an amazing 15 in a row wrong (Super Bowls XVII through XXXII).
> Most amusingly, it credited the Philadelphia Eagles with an
> astonishing *33 Super Bowl wins* they haven’t earned, to go with
> the 1 they have.
> Below, I’ve gathered a dozen of my favorite responses, in
> sequential order.


Kafasis’s selected responses are absolutely hilarious, and he documented every single one of the results in a spreadsheet available to download in both Excel and PDF formats. [Just read it](https://onefoottsunami.com/2025/01/23/not-so-super-apple/).


It’s just incredible how stupid Siri is about a subject matter of such popularity. If you had guessed that Siri could get half the Super Bowls right, you lost, and it wasn’t even that close.


Other answer engines handle the same questions with aplomb. I haven’t run a comprehensive test from Super Bowls 1 through 60 because I’m lazy, but a spot-check of a few random numbers in that range indicates that every other ask-a-question-get-an-answer agent I personally use gets them all correct. I tried ChatGPT, Kagi, DuckDuckGo, and Google. Those four all even fare well on the arguably trick questions regarding the winners of Super Bowls 59 and 60, which haven’t yet been played. E.g., asked the winner of Super Bowl 59, Kagi’s “Quick Answer”1 starts: “Super Bowl 59 is scheduled to take place on February 9, 2025. As of now, the game has not yet occurred, so there is no winner to report.”


Super Bowl winners aren’t some obscure topic, like, say, asking “Who won the 2004 North Dakota high school boys’ state basketball championship?” — a question I just completely pulled out of my ass, but which, amazingly, [Kagi answered correctly](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-kagi.png) for Class A, and [ChatGPT answered correctly](https://chatgpt.com/share/6792593b-bdb0-8011-8657-332320b63a75) for [both Class A and Class B](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-chatgpt.png), and provided a link to [this video of the Class A championship game on YouTube](https://www.youtube.com/watch?v=nDZIngPqcaM). That’s amazing! I picked an obscure state (no offense to Dakotans, North or South), a year pretty far in the past, and the high school sport that I personally played best and care most about. And both Kagi and ChatGPT got it right. (I’d give Kagi an A, and ChatGPT an A+ for naming the champions of both classes, and extra credit atop the A+ for the YouTube links.)


DuckDuckGo gets partial credit: its top search result is a link to [this web page that lists all previous boys’ basketball state champions back to 1914](https://ndhsaanow.com/champions/basketball-boys). That’s a perfect answer for a search engine. But as an answer engine, DuckDuckGo’s “AI Assist” feature answered, “Dickinson Trinity won the 2004 North Dakota high school boys’ state basketball championship.” That’s technically correct, but Dickinson Trinity was the 2004 *Class B* champion, the class for smaller schools. My prompting question was ambiguous on this, because, like I said, I pulled it out of my ass and had no idea that North Dakota has two school-size classes for high school sports. But if an answer engine is only going to name one champion, it ought to be for Class A. Still, though: not wrong.


Old Siri — which is to say pre-Apple-Intelligence Siri — does OK on this same question. On my Mac running MacOS 15.1.1, where ChatGPT integration is not yet available, Siri declined to answer the question itself and [provided a list of links](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-old-siri-mac.png), search-engine-style, and the top link was to [this two-page PDF](https://nebula.wsimg.com/6f47a6a9c59223689d07522ffe65113f?AccessKeyId=770BF0A52A890E445EEB&disposition=0&alloworigin=1) listing the complete history of North Dakota’s Class A boys’ and girls’ champions, but only through 2019. Not great, but good enough.


New Siri — powered by Apple Intelligence™ with ChatGPT integration enabled — gets the answer completely but plausibly wrong, which is the *worst* way to get it wrong. It’s also *inconsistently* wrong — I tried the same question four times, and got a different answer, all of them wrong, each time. It’s a complete failure.


The correct answer is that St. Mary’s Central defeated Bismarck High 50-46.2 (St. Mary’s is apparently sometimes referred to as “Bismarck St. Mary’s.”)


Here’s my first attempt with Siri, with ChatGPT integration, on iOS 18.3 RC1:

Siri's main answer:

  > In 2004, the Dickinson Midgets won the North Dakota Class A boys'
  > basketball state championship.<br/>
  > <small>ChatGPT (1 source) • Check important info for mistakes.</small>

Tapping on “ChatGPT (1 source)” shows a button linking to “bismarckschools.org”, which opened a link to [this 72-page PDF](https://activities.bismarckschools.org/archived/basketball/2004/state_a/stateabb.pdf) that was prepared *for* the 2004 North Dakota boys’ and girls’ Class A state tournaments. It has the schedule for the 2004 tournaments, and lists the boys’ and girls’ winners from 2003. The boys’s champion in 2003 was — you guessed it — the Dickinson Midgets.3


So I tried again, and Siri gave me this ([screenshot](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-siri+chatgpt-ios18.3-take2.png)):


> In the 2004 North Dakota high school boys’ state basketball
> championship, Bismarck High School defeated Bismarck Century High
> School to win the Class A title.


which not only is wrong, but doesn’t correspond to any championship game in North Dakota history, boys’ or girls’. Third try ([screenshot](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-siri+chatgpt-ios18.3-take3.png)):


> In 2004, the North Dakota high school boys’ state basketball
> championship was won by Bismarck High School. They defeated St.
> Mary’s Central High School in the title game.


which is correct about the two teams, but wrong about who won. The cited source that time was [the YouTube video](https://www.youtube.com/watch?v=nDZIngPqcaM) of the championship game. My fourth and final attempt at the same question ([screenshot](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-siri+chatgpt-ios18.3-take4.png)):


> The 2004 North Dakota Class A Boys’ Basketball State Championship
> was won by Fargo North High School. They defeated Minot High
> School in the championship game.


Fargo North did defeat Minot in the state championship game ... [in 1977](https://ndhsaanow.com/champions/basketball-boys).


I want to reiterate that I didn’t cherry-pick this question. When I started work this morning I thought I was simply going to link, with very little additional commentary, to Kafasis’s exhaustive [“Who won Super Bowl __?” exegesis at One Foot Tsunami](https://onefoottsunami.com/2025/01/23/not-so-super-apple/). (Which I’ll implore you once more to read, if only for the laughs.) I came up with “Who won the 2004 North Dakota high school boys’ state basketball championship?” off the top of my head as a spitball question that an AI-driven answer engine *could* plausibly answer correctly, but (so I thought) probably couldn’t. But Kagi gets it right, DuckDuckGo gets it sort-of right, and ChatGPT answers not just correctly but superlatively. What makes Siri’s ineptitude baffling is that ChatGPT is Siri’s [much-heralded](https://openai.com/index/openai-and-apple-announce-partnership/) partner for providing “world knowledge” answers.4 Siri with Apple Intelligence is so bad that it gets the answer to this question wrong even with the ostensible help of ChatGPT, which when used directly gets it perfectly right. And Siri-with-ChatGPT seemingly gets it wrong in a completely different way, citing different winners and losers (all wrong) each time. It’s like Siri is a special-ed student permitted to take an exam with the help of a tutor who knows the correct answers, and still flunks. (Given that iOS 18.3 Siri’s answer is seemingly different each time, perhaps if I kept trying, eventually it would deliver the correct answer in the way that a million monkeys with a million typewriters might — [but probably not](https://www.smithsonianmag.com/smart-news/chimpanzees-could-never-randomly-type-the-complete-works-of-shakespeare-study-finds-180985394/) — eventually peck out a sentence from Shakespeare.)


But it’s even worse than that, because old Siri, without Apple Intelligence, at least recognizes that Siri itself doesn’t know the answer and provides a genuinely helpful response by providing a list of links to the web, all of which contain accurate information pertaining to the question. Siri with Apple Intelligence, with ChatGPT integration enabled, is a massive regression.


If there’s any consolation for the Siri team at Apple, it’s that one other company’s AI-powered answer engine gave me an embarrassingly wrong response when asked for the 2004 North Dakota boys’ basketball champions: Google. Google’s regular web search results for that query are OK, with the top link being [the same PDF file](https://nebula.wsimg.com/6f47a6a9c59223689d07522ffe65113f?AccessKeyId=770BF0A52A890E445EEB&disposition=0&alloworigin=1), with results that only run through 2019, that old pre-AI Siri offered as its first result. (Even old Siri’s list-of-links response is hamstrung, competitively, by using Google search to provide its answers; both Kagi and DuckDuckGo provide better non-AI web search results for this query than Google.) But Google’s “AI Overview” answers are, like Siri with Apple Intelligence, both wrong and indeterminate.


If anything, believe it or not, Google’s AI Overview gave me the single worst answer in this whole saga, the first time I tried:


[
](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-google-take1.png)


The Lower Brule Sioux did win the Lakota Nation Invitational in 2004, but that was a holiday tournament, not the state championship. The Lower Brule boys’ basketball team has never won a state championship, but has finished as the Class B runner-up in the state tournament [twice in recent years](https://www.sdhsaa.com/Yearbook/B-Basketball.pdf) — in 2022 and 2023. But I feel confident predicting that Lower Brule will never win the North Dakota state championship ... because Lower Brule is a school in *South* Dakota.


Asked a second time, Google’s AI Overview did better, offering ([screenshot](https://daringfireball.net/misc/2025/01/2004-nd-boys-basketball-google-take2.png)):


> Dickinson High School won the 2004 North Dakota high school boys’
> state basketball championship.


which is the same technically correct, but not ideal answer that DuckDuckGo gave. (Technically correct insofar as Dickinson Trinity won the 2004 *Class B* boys’ championship.) Asked a third and fourth time, Google AI Overview stuck with Dickinson, so perhaps I got (un)lucky with its first boneheaded response.


Misery loves company they say, so perhaps Apple should, [as they’ve hinted since WWDC last June](https://techcrunch.com/2024/06/10/apple-confirms-plans-to-work-with-googles-gemini-in-the-future/), partner with Google to add Gemini as another “world knowledge” partner to power — or is it weaken? — Apple Intelligence.


---

1. Kagi offers a brilliantly simple interface to trigger these AI-powered “Quick Answers”: just end your query with a question mark. Searching for “foo bar” will just give you search results; searching for “foo bar?” will give you the same search results, but with a Quick Answer at the top. ↩︎︎
2. Bismarck High led throughout the game, and entered the 4th quarter with a 7-point lead, and were still up by 5 with three minutes to play. St. Mary’s made a really nice comeback in those final minutes. [Give the last few minutes a watch](https://youtu.be/nDZIngPqcaM?t=4369) — it was a great game. ↩︎︎
3. A rather unfortunate nickname, particularly for basketball. Did Dickinson High School lose some sort of bet long ago to get saddled with that for a mascot? ↩︎︎
4. When this Apple-OpenAI partnership was announced, there was much [speculation](https://daringfireball.net/linked/2024/05/30/information-altman-apple) about who’d be paying whom. The answer is that neither side is paying the other. Linking to [Mark Gurman’s scoop](https://www.bloomberg.com/news/articles/2024-06-12/apple-to-pay-openai-for-chatgpt-through-distribution-not-cash) on the arrangement, [I wrote back in June](https://daringfireball.net/linked/2024/06/13/gurman-openai-apple):

Apple getting this free of charge, in exchange only for the
prestige of showing the ChatGPT logo and credit to users of Apple
devices who engage the integration, is the Apple-iest negotiation
in recent memory. My money says Eddy Cue, Steve Jobs’s favorite
co-negotiator, made the deal. (I’d love to take Eddy Cue with me
to the dealer when next I buy a car.)

What hadn’t occurred to me until now is that not only is OpenAI getting no money from Apple out of this arrangement, but that the net brand equity they’re getting from it might be *negative*. These Super Bowl and high school basketball queries are handled perfectly by ChatGPT when using it directly — but Siri’s attribution makes it look like ChatGPT is to blame for these utterly and at times laughably wrong bungled answers. As it stands, Apple is getting a scapegoat more than a partner out of this deal. ↩︎︎



| **Previous:** | [Let’s Not Mince Words Regarding Trump’s Executive Order to Pause Enforcement of the TikTok Law and Provide Supposed Immunity to Companies That Are in Clear Violation of It](https://daringfireball.net/2025/01/npr_trump_tiktok) |
| **Next:** | [ICE Raids Are an Escalation of Our Long-Simmering De Facto Cold Civil War](https://daringfireball.net/2025/01/ice_raids_are_an_escalation_of_a_de_facto_cold_civil_war) |


PreviousNext