---
title: "YouTube vs. Fair Use"
date: 2010-09-17
url: https://blog.codinghorror.com/youtube-vs-fair-use/
slug: youtube-vs-fair-use
word_count: 1546
---

In [YouTube: The Big Copyright Lie](https://blog.codinghorror.com/youtube-the-big-copyright-lie/), I described my love-hate relationship with YouTube, at least as it existed in way back in the dark ages of 2007.


> Now think back through all the videos you’ve watched on YouTube. How many of them contained any original content?
> It’s perhaps the ultimate case of cognitive dissonance: by YouTube’s own rules [which prohibit copyrighted content], YouTube cannot exist. And yet it does.
> How do we reconcile YouTube’s official hard-line position on copyright with the reality that 90% of the content on their site is clearly copyrighted and clearly used without permission? It seems YouTube has an awfully convenient “don’t ask, don’t tell” policy – they make no effort to verify that the uploaded content is either original content or fair use. The copyrighted content stays up until the copyright owner complains. Then, and only then, is it removed.


Today’s lesson, then, is **be careful what you ask for**.


At the time, I just assumed that YouTube would never be able to resolve this problem through technology. The idea that you could somehow fingerprint every user-created uploaded video against *every piece of copyrighted video ever created* was so laughable to me that I wrote it off as impossible.


A few days ago I uploaded a small clip from the movie [Better Off Dead](http://www.imdb.com/title/tt0088794/) to YouTube, in order to use it in the [Go That Way, Really Fast](https://blog.codinghorror.com/go-that-way-really-fast/) blog entry. This is quintessential **fair use**: a tiny excerpt of the movie, presented in the context of a larger blog entry. So far, so good.


But then I uploaded a small clip from a different movie that I’m planning to use in another, future blog entry. Within an hour of uploading it, I received this email:


> Dear {username},
> Your video, {title}, may have content that is owned or licensed by {company}.
> No action is required on your part; however, if you are interested in learning how this affects your video, please visit [the Content ID Matches section](http://www.youtube.com/my_videos_copyright) of your account for more information.
> Sincerely,
>  ~ The YouTube Team


This 90 second clip is [from a recent movie](https://blog.codinghorror.com/but-you-did-not-persuade-me/). Not a hugely popular movie, mind you, but a movie you’ve probably heard of. This email both fascinated and horrified me. **How did they match a random, weirdly cropped (thanks, Windows Movie Maker) clip from the middle of a non-blockbuster movie** within an hour of me uploading it? This had to be some kind of automated process that checks uploaded user content against every piece of copyrighted content ever created (or the top n subset thereof), *exactly the kind that I thought was impossible.*


Uh oh.


I began to do some research. I quickly found [Fun with YouTube’s Audio Content ID System](https://www.scottsmitelli.com/articles/youtube-audio-content-id/), which doesn’t cover video, but it’s definitely related:


> I was caught by surprise one day when I received an automated email from YouTube informing me that my video had a music rights issue and it was removed from the site. I didn’t really care.
> Then a car commercial parody I made (arguably one of my better videos) was taken down because I used an unlicensed song. That pissed me off. I couldn’t easily go back and re-edit the video to remove the song, as the source media had long since been archived in a shoebox somewhere. And I couldn’t simply re-upload the video, as it got identified and taken down every time. I needed to find a way to outsmart the fingerprinter. I was angry and I had a lot of free time. Not a good combination.
> I racked my brain trying to think of every possible audio manipulation that might get by the fingerprinter. I came up with an almost-scientific method for testing each modification, and I got to work.


Further research led me to this brief TED talk, [How YouTube Thinks About Copyright](https://www.youtube.com/watch?v=UoX-YihV_ew&ab_channel=TED).

kg-card-begin: html

> We compare each upload against all the reference files in our database. This heat map is going to show you how the brain of this system works.
>     Here we can see the reference file being compared to the user generated content. The system compares every moment of one to the other to see if there’s a match. This means we can identify a match even if the copy uses just a portion of the original file, plays it in slow motion, and has degraded audio or video.
>     The scale and speed of this system is truly breathtaking – we’re not just talking about a few videos, we’re talking about over 100 years of video every day between new uploads and the legacy scans we regularly do across all of the content on the site. And when we compare those 100 years of video, we’re comparing it against millions of reference files in our database. It’d be like 36,000 people staring at 36,000 monitors each and every day without as much as a coffee break.

kg-card-end: html

I have to admit that I’m astounded by the scope, scale, and sheer effectiveness of YouTube’s new copyright detection system *that I thought was impossible! *Seriously, watch the TED talk. It’s not long. The more I researched [YouTube’s video identification tool](http://www.google.com/support/youtube/bin/answer.py?hl=en&answer=83766), the more I realized that **resistance is futile**. It’s *so* good that the only way to defeat it is by degrading your audio and video so much that you have effectively ruined it. And when it comes to copyright violations, if you can achieve mutually assured destruction, then you have won. Absolutely and unconditionally.


This is an outcome so incredible I am still having trouble believing it. But I have the automatically blocked uploads to prove it.


Now, **I am in no way proposing that copyright is something we should be trying to defeat or work around**. I suppose I was just used to the [laissez faire](http://en.wikipedia.org/wiki/Laissez-faire) status quo on YouTube, and the idea of a video copyright detection system this effective was completely beyond the pale. My hat is off to the engineers at Google who came up with this system. They aren’t the bad guys here; they offer some rather sane alternatives when copyright matches are found:


> If Content ID identifies a match between a user upload and material in the reference library, it applies the usage policy designated by the content owner. The usage policy tells the system what to do with the video. Matches can be to only the audio portion of an upload, the video portion only, or both.
> There are three usage policies – **Block, Track or Monetize**. If a rights owner specifies a **Block** policy, the video will not be viewable on YouTube. If the rights owner specifies a **Track** policy, the video will continue to be made available on YouTube and the rights owner will receive information about the video, such as how many views it receives. For a **Monetize** policy, the video will continue to be available on YouTube and ads will appear in conjunction with the video. The policies can be region-specific, so a content owner can allow a particular piece of material in one country and block the material in another.


The particular content provider whose copyright I matched chose the draconian block policy. That’s certainly not Google’s fault, but I guess you could say [I’m Feeling Unlucky](https://blog.codinghorror.com/googles-number-one-ui-mistake/).


Although the 90 second clip I uploaded is clearly copyrighted content – I would never dispute that – **my intent is not to facilitate illegal use, but to “quote” the movie scene as part of a larger blog entry.** YouTube does provide recourse for uploaders; they make it easy to file a dispute once the content is flagged as copyrighted. So I dutifully filled out the dispute form, indicating that I felt I had a reasonable claim of fair use.


![](https://blog.codinghorror.com/content/images/2025/04/image-483.png)


Unfortunately, my fair use claim was denied without explanation by the copyright holder.


Let’s consider the four guidelines for fair use I outlined in my original 2007 blog entry:

1. Is the use transformative?
2. Is the source material intended for the public good?
3. How much was taken?
4. What’s the market effect?


While we’re clear on 3 and 4, items 1 and 2 are hazy in a mashup. This would definitely be transformative, and I like to think that I’m writing for the erudition of myself and others, not merely to entertain people. I uploaded with the *intent* of the video being viewed through a blog entry, with YouTube as the content host only. But it was still 90 seconds of the movie viewable on YouTube by anyone, context free.


So I’m torn.


On one hand, this is an *insanely* impressive technological coup. The idea that YouTube can (with the assistance of the copyright holders) really validate every minute of uploaded video against **every minute of every major copyrighted work** is unfathomable to me. When YouTube promised to do this to placate copyright owners, I was sure they were delaying for time. But much to my fair-use-loving dismay, they’ve actually gone and *built* the damn thing – and it works.
Just, maybe, it works a little *too* well. I’m still looking for video sharing services that offer some kind of fair use protection.

[copyright](https://blog.codinghorror.com/tag/copyright/)
[fair use](https://blog.codinghorror.com/tag/fair-use/)
[youtube](https://blog.codinghorror.com/tag/youtube/)
[content moderation](https://blog.codinghorror.com/tag/content-moderation/)
[intellectual property](https://blog.codinghorror.com/tag/intellectual-property/)
