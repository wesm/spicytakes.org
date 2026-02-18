---
title: "As if Anyone Needed Further Proof, Patrick Soon-Shiong’s Los Angeles Times Is Now a Propaganda Rag (and They’re Bad at HTML)"
date: 2025-02-01
url: https://daringfireball.net/2025/02/soon-shiong_la_times_propaganda_rag
slug: soon-shiong_la_times_propaganda_rag
word_count: 837
---


[Editors note from The New Republic](https://newrepublic.com/article/191030/rfk-jr-op-ed-los-angeles-times):


> As The New Republic [reported on Friday](https://newrepublic.com/post/191007/la-times-robert-f-kennedy-jr-donald-trump), The Los Angeles
> Times — currently in a race to the bottom [with The Washington
> Post](https://newrepublic.com/post/188445/washington-post-bezos-trump-failure) to determine which of the two venerable institutions
> can sell out to Donald Trump the hardest — found itself in a
> fresh controversy after contributor Eric Reinhart accused the
> paper of [making significant edits](https://www.latimes.com/opinion/story/2025-01-29/rfk-jr-trump-health-reform) to a piece of his that
> was largely critical of Robert F. Kennedy, Jr. into one that
> depicted the president’s pick to run the Department of Health and
> Human Services with an “optimistic tone,” largely “suggesting
> that the virulent conspiracy theorist could be an answer and
> solution to the American public’s bubbling resentment toward the
> health care industry.”
> Reinhart exposed the shady goings-on on X (fka Twitter). “Editing
> out the most urgent point of an OpEd in the minutes before sending
> to press while then also assigning a title and image that suggest
> an argument entirely opposite to the author’s clear intent is
> pretty shitty,” [he wrote](https://bsky.app/profile/ericreinhart.bsky.social/post/3lh2ell45722u). In light of this lamentable
> journalistic malpractice, The New Republic has agreed to run
> Reinhart’s piece as he intended it to be read.


Reinhart’s headline at TNR, encapsulating the intended thrust of his piece: “[RFK Jr’s Wrecking Ball Won’t Fix Public Health](https://newrepublic.com/article/191030/rfk-jr-op-ed-los-angeles-times)”, and the closing paragraph of the column:


> Although RFK, Jr., and Luigi Mangione are both responses to the
> same underlying problem of US healthcare corruption, there is a
> major difference between them: one allegedly operated outside the
> law to kill one person in defense of millions, whereas the other — via his egomaniacal [disregard](https://www.washingtonpost.com/health/2025/01/28/rfk-jr-disparaged-vaccines-dozens-times-recent-years-misled-race/) for scientific evidence — seeks to use law itself to inflict preventable death on those
> millions.


The headline the LA Times ran his piece under, after their editing: “[Trump’s Healthcare Disruption Could Pay Off — if He Pushes Real Reform](https://www.latimes.com/opinion/story/2025-01-29/rfk-jr-trump-health-reform)”, and its closing paragraphs:


> Such an approach would shift us away from overreliance on
> expensive medical treatments and toward public health as it should
> be: a project by and for [the people](https://direct.mit.edu/daed/article/152/4/245/118232/Empowering-the-Extra-Ordinary) that makes full use
> of government resources to [empower communities](https://www.statnews.com/2023/02/24/fixing-public-health-systems-revolution-physicians-take-backseat/).
> We should demand fundamental transformations in how we approach
> health in America, but a wrecking ball alone won’t deliver what
> we need.


After all the [shenanigans](https://daringfireball.net/2024/10/profiles_in_cowardice_bezos_lewis_washington_post) [Soon-Shiong began pulling](https://daringfireball.net/linked/2024/12/05/owner-patrick-soon-shiong-is-tanking-the-la-times) pre- [and post-election](https://daringfireball.net/linked/2024/12/13/soon-shiong-la-times), my only question here is whether Reinhart really believed the LA Times op-ed page was going to run his piece as written.


## Super-Nerdy Bonus Material


My original intention for this post ended above. I wanted to quote the TNR editors note that explained the situation, quote Reinhart’s intended headline and closing paragraph, and contrast those with the benign gibberish headline and closing that the LA Times actually published. Done. But I’ve got more. Turns out, the LA Times itself effectively published *proof* of its “editing” that completely perverted Reinhart’s intended thrust.


I have a small arsenal of homegrown tools I use to automate the work of writing DF. [Markdown](https://daringfireball.net/projects/markdown/) itself is the crown jewel of them. But over the now many years I’ve been doing this I’ve created a whole toolbox of scripts and macros that help me do what I do faster and with fewer errors. (And I still commit plenty of errors.) One of the smaller ones that I’ve never shared publicly (but probably [should](https://daringfireball.net/projects/)) is a Keyboard Maestro macro that lets me select a range of text in Safari and copy that selection as Markdown-formatted text. It picks up spans of italics and boldfacing, but most importantly, it picks up hyperlinks in the original text and converts them to the Markdown link style I prefer ([defined reference links](https://daringfireball.net/projects/markdown/syntax#link)).


You will note in my blockquote above of Reinhart’s intended closing paragraph, as published at The New Republic, he linked the word “disregard” to [this January 28 report from The Washington Post](https://www.washingtonpost.com/health/2025/01/28/rfk-jr-disparaged-vaccines-dozens-times-recent-years-misled-race/): “RFK Jr. Disparaged Vaccines Dozens of Times in Recent Years and Made Baseless Claims on Race”. No link to that Washington Post report appears, visually, in the butchered version of Reinhart’s piece that ran in the LA Times.


But, my “Copy Markdown Blockquote” macro picked up an effectively invisible-to-the-user link to that article, in the HTML markup between their closing paragraph and Reinhart’s author bio beneath it. You can view source at the LA Times website and see for yourself, but here’s a screenshot:


[
](https://daringfireball.net/misc/2025/02/la-times-reinhart-html-screenshot.png)


You can’t see the link or click on it as rendered in a browser, because there’s no content between the opening `<a …>` and closing `</a>` tags, but whoever at the LA Times edited Reinhart’s column to pervert its meaning, did so sloppily, leaving behind at least this one acerbic vestigial link from his originally-submitted prose.



| **Previous:** | [Pebble Founder Eric Migicovsky Is Bringing It Back](https://daringfireball.net/2025/01/repebble) |
| **Next:** | [‘Hot Tub’, a Hardcore Porn App for iOS, Hits AltStore in the E.U.](https://daringfireball.net/2025/02/hot_tob_hardcore_porno_app_eu) |


PreviousNext