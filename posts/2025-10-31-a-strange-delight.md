---
title: "A strange delight"
subtitle: "We are more machine now than man, and it's better if we remember that."
date: 2025-10-31T18:07:24+00:00
url: https://benn.substack.com/p/a-strange-delight
slug: a-strange-delight
word_count: 1718
---


![Minority Report' Review: 2002 Movie](https://substackcdn.com/image/fetch/$s_!tLIR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91854e86-ad60-4dc6-a6e0-e3b20aae47b0_1296x730.jpeg)


Have you ever seenMinority Report? Do you rememberthis scene, where Tom Cruise uses a pair of gloves to flip through a bunch of videos on a giant screen? When you first saw it, did you think that it looked cool? Did you want to use a computer like that? Did you ever think, I don’t care what I’m trying to do—he’s solving murders before the victims are dead; I’m mostly responding to emails long after they matter—but I bet it’d be pretty fun to do it with controllers attached to my hands?


Have you ever driven a sports car? Have you ever borrowedyour uncle’s BMW, taken a turn faster than you would in your Toyota, and been startled by how precisely it angles through the bend? By how firm it feels on the road? By how easily it finds its pace? Have you ever thought, I don’t have anything practical to do with this car, but if it were mine, I’d look for an excuse to drive it?


Have you ever shot a gun? Even if they aren’t your thing—andthey aren’t mine—did their appeal start to make sense? Was there something stupefying in its weight and heavy trigger, and then, all at once, its sound, its recoil, and its explosive hammer? Did you find something electric in it? Not in any practical problem that it might solve or in its alleged everyday utility, but in its awful, intoxicating power?


---


Most software is not like that. We might say it’s magical; we might describe it as delightful; but, come on. We usually say that because we have something to sell—the product itself, or our taste in it. The only emotion that software typically evokes is slow-simmering frustration; the best software often—aspirationally!—evokes nothing at all. One of Fivetran’s core product principles is toset it and forget it. Google Chrome was built toget out of your way. Those are often our highest ideals: To be efficient, to “just work,” to “help us get back to the things we really care about.”


But, occasionally, we stumble across something different.


It was not a car, or a gun, or a personal IMAX mind-melded to the FBI’s Eye of Sauron, but I still remember the first time that I wrote a script that scraped stuff from the internet.1I wanted some numbers from YouTube, they were available in a chart under each video, and I didn’t want to write them all down by hand. So, I wrote a short program to collect them for me. Eventually, my cryptic incantation somehow worked, and the terminal ticked through a series of confirmations:2“Getting videos…Found 57 videos.Retrieving video 1…Done. Retrieving video 2… Done. …”


It was, of course, an unremarkable piece of technology. Apopular websitecould retrieve an obscure object from a distant warehouse and physically deliver it to your door in under 24 hours; all I was asking a computer to do was copy a few dozen numbers from the internet and paste them into a file. Still, that is what made it striking. Amazon’s operations are impossible to comprehend; my script was practically mechanical. You could see its individual pieces; you could see its incessant digital hands and its relentless energy; you could see the impossible infallibility of its math.


And, there was the rote work that I did, and then, the work thatitdid. Yes, that work was dumb, but when we use a computer to do something important, it’s too easy to get distracted by the destination. How fast can I create this document? How efficiently can I file these expenses? How well does it do this Job To Be Done? Can the car haul enough groceries? Does the automated drone have tactical practicality? When there is aworldwide network of abstract magicbehind a computer, weforget to be amazed by it.


But, up close, there is something mesmerizing about watchinga machine do its simple work.


---


Here’s a question,whilewe’rehere: What if dbt had launched itself with a UI?


For years, dbt’s only interface was the command line. You told it what to do, and, like my old Python scripts, it would slowly print out its progress. That was it—there was no webpage for running dbt; there wasn’t even a way to interact with it using buttons or a mouse. And when it was put on the internet, dbt’s first UI was, for the most part, stilla command line and some logs.


But suppose there had been more. Suppose the first version of dbt had included everything that was there,plusan interface for dragging and dropping models togetheron a visual canvas. And suppose that nothing else had been different: dbt Core was developed at the same pace, with the same functionality. Would it have been more successful?Lesssuccessful?


One answer is that it would’ve been better, becausemore is always better. Another answer is that it would’ve been worse, because dbt’s limited interface taught data analysts technical skills. For many analysts, dbt was a gateway: Learn dbt; learn how to stumble around the command line; learn foundational engineering tools like git; learn how to write a bit of code, how to write your own scripts, and, eventually, how to do a lot more with a computer than you otherwise could. A UI would’ve shortcut that, and given training wheels to a profession that needed to learn how to ride a bike.


But a third answer is that it would’ve been worse becausethe command line tool was a big part of dbt’s appeal. It was a gateway, though not for practical skills; it was a gateway to the same oddly evocative experience3that I stumbled into when I was trying to scrape YouTube. It was thousands of people’s first glimpse into the guts of their computer, and its arithmetic power. After a lifetime of pointing and clicking, it was the first time we fully commanded a computer with a keyboard and all ten of our fingers. After waiting for websites to load behind a bunch of spinners, we saw how quickly a computer could respond when you removed ads, pictures, and a quarter-million lines of javascript.4It was our first version of Tom Cruise’s gloves, and our first computational sports car. And it was our first time directly holding a gun,with the safety off.


It was not perfect, of course. Analog tools can be frustrating, and we all had our protective checklists.5But there was something mesmerizing in it too.


---


For reasons, I’ve spent a lot of time in two products over the last couple months:Snowsight, Snowflake’s built-in query and visualization tool; and terminal-based coding apps likeClaude CodeandCodex.


If you use these tools, you will notice two things. First, the terminal apps are extraordinarily basic. Their interfaces are text, displayed in bulleted lists and a monospaced font. The text is usually white; occasionally, it’s off-white. Sometimes, the text is in a box. You navigate the app with arrow keys. You cannot use a mouse. Anthropic’s and OpenAI’s frontier models—the most advanced programs that humans have ever created—sit behind these apps, but the apps themselves could be rendered by adot matrix printer.


TheSnowsight UIcould not be more different. There are tabs and dynamic panels; there are buttons and hover states and user preferences. There are loading states; empty states; overflow states. There is a left-side navigation menu that animates as it slides open, and animates again as the menu’s contents unfurl. And there is AI too: When you click into the query editor, a bluesparklepulses twice; click on that button, and a chat dialogue appears—a chat dialogue that, roughly speaking, contains almost the entirety of Claude Code’s UI.


But the second thing you will notice—or at least, the second thing that I noticed—is, when bouncing between Claude Code and Snowflake, you prefer Claude Code. That could be a basic point about clutter and product bloat, though that seems like a lazy criticism: Snowflake’s editor, by most reasonable measures, a well-composed piece of software. It is also the child of two startups that were hallmarks oftechnical tasteandmodern software design.


Still, it is Claude Code—theBrother WP-80—that feels modern. Most reviews of Claude Code say that’s because of what itdoes,and that it’s good despite its raw interface. “Ironically, its simplicity contributes significantly to its charm,”said one post; “A terminal interface for chat-based code editing? Sounds like a step backward. But Anthropic did a decent job with it,”said another. Maybe that’s true; maybe for proper engineers, terminal interfaces are outdated anachronisms, an unnecessarily uncomfortable Jeep Wrangler in a world with Waymos and Teslas.


I’m not so sure though. Because, for all the comforts that come withdriving a sofa down the highway, luxury is rarely an emotional experience. We are not moved by detachment. Tools like Claude Code puts you as close to the technology as it can. Though it only exists on a screen, it is an unexpectedly physical product. Its aesthetic suggests that you’re plugged directly into the mainframe; its snappiness implies that there’s no intermediation. It’s just you and the machine, and the uncanny sense of dexterity that comes with learning how to use it.


---


Touch grass, they say. Good advice, I suppose, in anincreasingly artificial world. But as computers and the internet become ever more unavoidable, I hope that those of us who build them don’t anesthetize them too much. The internet does not need more whiz-bang whirligigs or beautifully efficient minimalism. We can also go the other way, and build stuff that reminds us that computers are physical things too. Because real delight—and productivity, if we must—comes from feeling the machine that we live our lives on, rather than forgetting to see that it exists.

[1](https://benn.substack.com/p/a-strange-delight#footnote-anchor-1-177675177)

By “stuff,” I of course mean “the number of likesMiley Cyrus’ and Lana Del Ray’s music videos got on YouTube.”

[2](https://benn.substack.com/p/a-strange-delight#footnote-anchor-2-177675177)

Evidently, the terminal did not actually do this, becausemy barbaric PHP scraperdidn’t print anything at all. But my later scripts—like, uh, theprice_of_weed_scraper.py—were much more professional.

[3](https://benn.substack.com/p/a-strange-delight#footnote-anchor-3-177675177)

Or, aStrange Delight.

[4](https://benn.substack.com/p/a-strange-delight#footnote-anchor-4-177675177)

Rendering the homepage of theNew York Timesrequires 11,000 kilobytes of javascript, which is about 11 million characters, or,at 40 characters per line, 275,000 lines.

[5](https://benn.substack.com/p/a-strange-delight#footnote-anchor-5-177675177)

Like our git cheatsheets, which usually started by suggesting reasonable things—remember to pull! Write descriptive commit messages!—and ended withgit reset --hard HEAD, a link tothis page, and an instruction on how tolaunch your computer into the sun.
