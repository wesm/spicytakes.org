---
title: "Superhuman and Email Privacy"
date: 2019-07-23
url: https://daringfireball.net/2019/07/superhuman_and_email_privacy
slug: superhuman_and_email_privacy
word_count: 764
---


Mike Davidson, “[Superhuman’s Superficial Privacy Fixes Do Not Prevent It From Spying on You](https://mikeindustries.com/blog/archive/2019/07/superhumans-superficial-privacy-fixes-do-not-prevent-it-from-spying-on-you)”:


> Last week was a good week for privacy. Or was it?
> It took [an article I almost didn’t publish](https://mikeindustries.com/blog/archive/2019/06/superhuman-is-spying-on-you) and tens of
> thousands of people [saying they were creeped out](https://twitter.com/search?q=https%3A%2F%2Fmikeindustries.com%2Fblog%2Farchive%2F2019%2F06%2Fsuperhuman-is-spying-on-you&src=typed_query), but
> Superhuman [admitted they were wrong and reduced the danger that
> their surveillance pixels introduce](https://blog.superhuman.com/read-statuses-bdf0cc34b6a5). Good on Rahul Vohra and
> team for that.
> I will say, however, that I’m a little surprised how quickly some
> people are rolling over and giving Superhuman credit for fixing a
> problem that they didn’t actually fix. From tech press articles
> implying that the company quickly closed all of its privacy
> issues, to friends sending me nice notes, I don’t think people are
> paying close enough attention here. This is not “[Mission
> Accomplished](https://en.wikipedia.org/wiki/Mission_Accomplished_speech)” for ethical product design or privacy — at all.


If you haven’t been following this saga from earlier this month, it’s well worth your time to read the whole thing, including [Davidson’s original post](https://mikeindustries.com/blog/archive/2019/06/superhuman-is-spying-on-you) and Superhuman CEO Rahul Vohra’s genuinely thoughtful — but ultimately unsatisfying — [response](https://blog.superhuman.com/read-statuses-bdf0cc34b6a5).


Basically, Superhuman is an invitation-only Gmail front-end whose users seem to genuinely love it. But they embed tracking pixels in emails by default, and use these pixels to show the sender when (and until last week, *where*, which is truly fucked up) the recipient views them. They call them “read receipts”, and functionally they do work like read receipts, insofar as they indicate when you read a message. But real email read receipts are under the *recipient’s* control, and they’re a simple binary flag, read or unread — they don’t tell the sender how many times or when you view a message.


I know that mailing list software generally includes tracking pixels. I don’t think that’s ethical either. On a personal level, though, with Superhuman, tracking when and how many times a recipient views a message is simply absurdly wrong.


It’s also something the vast, overwhelming majority of people don’t even realize is possible. I’ve told the basic Superhuman tracking story to a few people over the last few weeks, and asked whether they realized this was possible; all of them expressed shock and many of them outrage as well. Email should be private, *and most people assume, incorrectly, that it is*. You have to be a web developer of some sort to understand how this is possible. Email is supposed to be like paper mail — you send it, they get it, and you have no idea whether they read it or not. It bounces back to you if they never even receive it, say, because you addressed it incorrectly. The original conception of email is completely private.


But also, the original conception of email is that messages are plain text. No fonts, no styles, just plain text, with optional attachments. But those attachments are embedded in the message, not pulled from a server when the message is viewed.


Once we allowed email clients to act as de facto web browsers, loading remote content from servers when messages are viewed, we opened up not just a can of worms but an entire case of canned worms. Every privacy exploit for a web browser is now a privacy exploit for email. But it’s worse, because people naturally assume that email is completely private.


Read receipts should be under the control of the recipient, not the sender. Full stop. The strength of email is that it is open and decentralized, but that’s email’s weakness too. No closed messaging platform that I’m aware of allows for read receipts that are controlled by the sender, not the recipient.


I think Superhuman should be ashamed of themselves for building this feature in the first place — particularly the geo-tracking. But ultimately, *email clients should defend against this*. The fact that this nonconsensual tracking is even possible should be treated as a serious bug in all email clients. Apple Mail — both on Mac and iOS — allows you to disable loading of remote images as a preference, but that breaks most graphically rich emails. Mail clients should allow remote images but load them anonymously, through a proxy server perhaps. I’m sure it’s a tricky problem to solve, but I’m convinced it can be solved.


Email should be every bit as private as people assume that it is.



| **Previous:** | [Apple Is Sending Out Another Silent Update To Fix the Webcam Flaw in Zoom’s Partner Apps](https://daringfireball.net/2019/07/another_zoom_update) |
| **Next:** | [Siri, Privacy, and Trust](https://daringfireball.net/2019/08/siri_privacy_trust) |


PreviousNext