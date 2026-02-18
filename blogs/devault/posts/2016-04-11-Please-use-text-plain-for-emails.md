---
title: "Please use text/plain for email"
date: 2016-04-11
url: https://drewdevault.com/2016/04/11/Please-use-text-plain-for-emails.html
slug: Please-use-text-plain-for-emails
word_count: 940
---

A lot of people have come to hate email, and not without good reason. I don’t
hate using email, and I attribute this to better email habits. Unfortunately,
most email clients these days lead users into bad habits that probably
contribute to the sad state of email in 2016. The biggest problem with email is
the widespread use of HTML email.

Compare email to snail mail. You probably throw out most of the mail you get -
it’s all junk, ads. Think about the difference between snail mail you read and
snail mail you throw out. Chances are, the mail you throw out is flashy flyers
and spam that’s carefully laid out by a designer and full of eye candy (kind of
like many HTML emails). However, if you receive a letter from a friend it’s
probably going to be a lot less flashy - just text on a page. Reading letters
like this is pleasant and welcome. Emails should be more like this.

I consider this the basic argument for plaintext emails - they make email
better. There are more specific problems with HTML emails that I can give,
though (not to mention the fact that I read emails  [on
this](https://drewdevault.com/2016/03/22/Integrating-a-VT220-into-my-life.html) 
now).

## What’s wrong with HTML email

**Tracking images**  are images that are included in HTML emails with <img
/> tags. These images have URLs with unique IDs in them that hit remote
servers and let them know that you opened the email, along with various details
about your mail client and such. This is a form of tracking, which many people
go to great lengths to prevent with tools like
 [uBlock](https://github.com/gorhill/uBlock) . Most email clients recognize this,
and actually  *block*  images from being shown without explicit user consent. If
your images aren’t even being shown, then why include them? Tracking users is
evil.

Many  **vulnerabilities**  in mail clients also stem from rendering HTML email.
Luckily, no mail clients have JavaScript enabled on their HTML email renderers.
However, security issues related to HTML emails are still found quite often in
mail clients. I don’t want to view this crap (and I don’t).

HTML email also makes  **phishing**  much easier. I’ve often received HTML emails
with links that hide their true intent by using a different href than their text
would suggest (and almost always with a tracking code added, ugh). They are also
 **incompatible**  with many email-based workflows, such as inline quoting,
mailing list participation, and sending & working with source code patches.

## Good habits for plaintext emails

Some nice things are possible when you choose to use plaintext emails. Remember
before when I was comparing emails to snail mail letters? Well, let’s continue
those comparisons. Popular email clients of 2016 have thoroughly bastardized
email, but here’s what it once was and perhaps what it could be today.

The common mail client today uses the abhorrent “ [top
posting](https://en.wikipedia.org/wiki/Posting_style#Top-posting) ” format, where
the entire previous message is dumped underneath your reply. As the usual quote
goes:

> A: Because it messes up the order in which people normally read text. 
>  Q: Why is top-posting such a bad thing? 
>  A: Top-posting. 
>  Q: What is the most annoying thing in e-mail?

A better way to write emails is the same way you write a letter to send via
snail mail. Would you photocopy the entire history of your correspondence and
staple it to your response? After a while you would start paying more for the
weight! Though bandwidth seems cheap now, the habit is still silly. Instead of
copying the entire conversation into your email, quote only the relevant parts
and respond to them inline. For example, let’s say I receive this email:

```
Hi Drew!

Could you take a look at the server this afternoon? I think it's having some
issues with nginx.

I also took care of the upgrades you asked for last night. Sorry it took so
long!

--
John Doe
```

The best way to respond to this would be:

```
Hi John!

>Could you take a look at the server this afternoon? I think it's having some
>issues with nginx.

No problem. I just had a quick look now and nginx was busted. Should be
working now.

>I also took care of the upgrades you asked for last night. Sorry it took so
>long!

Thanks!

--
Drew DeVault
```

John might follow up with this:

```
>Should be working now.

Yep, seems to be up. Thanks!

--
John Doe
```

Much better if you ask me. This works particularly well on mailing lists for
open source projects, where you send a patch and reviewers will respond by
quoting specific parts of your patch and leaving feedback. Just treat emails
like letters!

## Multipart emails

I think there are nothing but negatives to HTML email. I use
 [mutt](http://www.mutt.org/)  to read email, which doesn’t even render HTML
emails and allows me to compose emails with Vim. But if you absolutely insist on
using HTML emails, please use  [multipart
emails](https://en.wikipedia.org/wiki/MIME#Multipart_messages) . If you’re
sending automated emails, your programming language likely contains a mechanism
to facilitate this. The idea is that you send an alternative text/plain body for
your email. Be sure that this body contains all of the information of the HTML
version. If you do this, I will at least be willing to read your emails.

## How do I use plaintext emails?

Your mail client should have an option for composing emails with plaintext. Look
through your settings for it and it’ll change the default. Then you’re free!
Tell your friends to do the same, and your email life will be happier.
