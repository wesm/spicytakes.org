---
title: "Whatever Happened to Voice Recognition?"
date: 2010-06-21
url: https://blog.codinghorror.com/whatever-happened-to-voice-recognition/
slug: whatever-happened-to-voice-recognition
word_count: 1320
---

Remember that Scene in [Star Trek IV](http://www.imdb.com/title/tt0092007/) where Scotty tried to use a Mac Plus?


![](https://blog.codinghorror.com/content/images/2025/04/image-475.png)


Using a mouse or keyboard to control a computer? Don’t be silly. In the future, clearly there’s only one way computers will be controlled: by **speaking to them**.


There’s only one teeny-tiny problem with this magical future world of computers we control with our voices.


![](https://blog.codinghorror.com/content/images/2025/04/image-474.png)


It doesn’t work.


Despite ridiculous, order of magnitude [increases in computing power](https://blog.codinghorror.com/moores-law-in-practical-terms/) over the last decade, we can’t figure out how to get speech recognition accuracy above 80% – when the baseline *human* voice transcription accuracy rate is anywhere from 96% to 98%!


> In 2001 recognition accuracy topped out at 80%, far short of HAL-like levels of comprehension. Adding data or computing power made no difference. Researchers at Carnegie Mellon University checked again in 2006 and found the situation [unchanged](http://www.cs.brandeis.edu/~marc/misc/proceedings/lrec-2006/pdf/802_pdf.pdf). With human discrimination as high as 98%, the unclosed gap left little basis for conversation. But sticking to a few topics, like numbers, helped. Saying “one” into the phone works about as well as pressing a button, approaching 100% accuracy. But loosen the vocabulary constraint and recognition begins to drift, turning to vertigo in the wide-open vastness of linguistic space.


As Robert Fortner explained in [Rest in Peas: The Unrecognized Death of Speech Recognition](https://web.archive.org/web/20100723141454/http://robertfortner.posterous.com/the-unrecognized-death-of-speech-recognition), after all these years, we’re desperately far away from any sort of universal speech recognition that’s useful or practical.


Now, we do have to clarify that we’re talking about universal recognition: saying *anything* to a computer, and having it reliably convert that into a valid, accurate text representation. When you constrain the voice input to a more limited vocabulary – say, just numbers, or only the names that happen to be in your telephone’s address book – it’s not unreasonable to expect a high level of accuracy. I tend to think of this as “voice control” rather than “voice recognition.”


Still, I think we’re avoiding the real question: **is voice control, even hypothetically *perfect* voice control, more effective than the lower tech alternatives?** In my experience, speech is one of the least effective, inefficient forms of communicating with other human beings. By that, I mean...

- typical spoken communication tends to be off-the-cuff and ad-hoc. Unless you’re extremely disciplined, on average you will be unclear, rambling, and excessively verbose.
- people tend to hear about half of what you say at any given time. [If you’re lucky](https://blog.codinghorror.com/the-value-of-repetition-again/).
- spoken communication puts a highly disproportionate burden on the listener. Compare the time it takes to process a voicemail versus the time it takes to read an email.


I am by no means *against* talking with my fellow human beings. I have a very deep respect for those rare few who are great communicators in the challenging medium of conversational speech. Though we’ve all been trained literally from birth how to use our voices to communicate, **voice communication remains filled with pitfalls and misunderstandings**. Even in the best of conditions.


So why in the world – outside of a disability – would I want to extend the creaky, rickety old bridge of voice communication to controlling my computer? Isn’t there a better way?


Robert’s post contains some examples in the comments from voice control enthusiasts:


> in addition to extremely accurate voice dictation, there are those really cool commands, like being able to say something like “search Google for Balloon Boy” or something like that and having it automatically open up your browser and enter the search term – something like this is accomplished many times faster than a human could do it. Or, being able to total up a column of numbers in Microsoft Excel by saying simply “total this column” and seeing the results in a blink of an eye, literally.


That’s funny, because **I just fired up the Google app on my iPhone, said “balloon boy” into it, and got... a search for “blue boy.”** I am not making this up. As for the Excel example, total *which* column? Let’s assume you’ve dealt with the tricky problem of selecting what column you’re talking about with only your voice. (I’m sorry, was it D5? B5?) Wouldn’t it be many times faster to click the toolbar icon with your mouse, or press the keyboard command equivalent, to sum the column – rather than methodically and tediously saying the words “sum this column” out loud?


I’m also trying to imagine a room full of people controlling their computers or phones using their voices. It’s difficult enough to get work done in today’s chatty work environments without the added burden of a floor full of people saying “[zoom... enhance](http://www.youtube.com/watch?v=Vxq9yj2pVWk)” to their computers all day long. Wouldn’t we all end up hoarse *and* deaf?


Let’s look at another practical example – YouTube’s [automatic speech recognition feature](http://googlesystem.blogspot.com/2009/11/youtube-audio-transcription.html). I clicked through to [the first UC Berkeley video](http://www.youtube.com/ucberkeley#p/u/0/BL9gmMzpRr4) with this feature, clicked the CC (closed caption) icon, and immediately got... this.


![](https://blog.codinghorror.com/content/images/2025/04/image-473.png)


“Light exerts force on matter.” But according to Google’s automatic speech recognition, it’s “like the search for some matter.” Unsurprisingly, it does not get better from there. You’d be way more confused than educated if you had to learn this lecture from the automatic transcription.


Back when Joel Spolsky and I [had a podcast together](http://itc.conversationsnetwork.org/series/stackoverflow.html), **a helpful listener suggested using speech recognition to get a basic podcast transcript going**. Everything I knew about voice recognition told me this wouldn’t help, but harm. What’s worse: transcribing everything by hand, from scratch – or correcting every third or fourth word in an auto-generated machine transcript? Maybe it’s just me, but the friction of the huge error rate inherent in the machine transcript seems far more intimidating than a blank slate human transcription. The humans may not be particularly efficient, but they all *add* value along the way – collective human judgment can editorially improve the transcript, by removing all the duplication, repetition, and “ums” of a literal, by-the-book transcription.


In 2004, Mike Bliss composed [a poem about voice recognition](https://web.archive.org/web/20100626021645/http://www.theblisspages.com/cms.php?mbid=147). He then read it to voice recognition software on his PC, and rewrote it as recognized.

kg-card-begin: html


| a poem by Mike Bliss

like a baby, it listens
it can’t discriminate
it tries to understand
it reflects what it thinks you say
it gets it wrong... sometimes
sometimes it gets it right.
One day it will grow up,
like a baby, it has potential
will it go to work?
will it turn to crime?
you look at it indulgently.
you can’t help loving it, can you? | a poem by like myth

like a baby, it nuisance
it can’t discriminate
it tries to oven
it reflects lot it things you say
it gets it run sometimes
sometimes it gets it right
won’t day it will grow bop
Ninth a baby, it has provincial
will it both to look?
will it the two crime?
you move at it inevitably
you can’t help loving it, cannot you? |


kg-card-end: html

The real punchline here is that Mike re-ran the experiment in 2008, and after 5 minutes of voice training, **the voice recognition got all but 2 words of the original poem correct!**


I suspect that’s still not good enough in the face of the existing simpler alternatives. Remember handwriting recognition? It was all the rage in the era of the [Apple Newton](http://en.wikipedia.org/wiki/Newton_(platform)).


![](https://blog.codinghorror.com/content/images/2025/04/image-472.png)


It wasn’t as bad as Doonesbury made it out to be. I learned [Palm’s Graffiti](http://en.wikipedia.org/wiki/Graffiti_(Palm_OS)) handwriting recognition language and got fairly proficient with it. **More than ten years later, you’d expect to see *massively* improved handwriting recognition of some sort in today’s iPads and iPhones and iOthers, right?** Well, maybe, if by “massively improved” you mean “nonexistent.”


While it still surely has its niche uses, I personally don’t miss handwriting recognition. Not even a little. And I can’t help wondering if voice recognition will go the same way.

[speech recognition](https://blog.codinghorror.com/tag/speech-recognition/)
[voice control](https://blog.codinghorror.com/tag/voice-control/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
