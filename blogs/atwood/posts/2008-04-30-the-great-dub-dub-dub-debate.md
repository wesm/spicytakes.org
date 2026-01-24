---
title: "The Great Dub-Dub-Dub Debate"
date: 2008-04-30
url: https://blog.codinghorror.com/the-great-dub-dub-dub-debate/
slug: the-great-dub-dub-dub-debate
word_count: 848
---

Pop quiz, hotshot. Which is the *superior* Uniform Resource Locator?


[www.fakeplasticrock.com](https://web.archive.org/web/20110414194701/http://www.fakeplasticrock.com/)


or


[fakeplasticrock.com](https://web.archive.org/web/20110414194701/http://www.fakeplasticrock.com/)


This is one of those intractable problems. Global wars have been fought over so much less. In hacker circles, this is sometimes referred to as a [bikeshed discussion](http://www.unixguide.net/freebsd/faq/16.19.shtml).


![](https://blog.codinghorror.com/content/images/2025/08/dub-dub-dub-link-letters-cropped.png)


That said, I do have a few bits of practical advice that I think apply unilaterally, whatever your position is:

- **Pick one or the other form and stick with it.** Once the URL is out there in the wild, you need everyone to link to the same form for link juice amplification purposes, if nothing else. If half your incoming links are split between the www and non-www forms of your URL, that will hurt you a heck of lot more than picking the “wrong” prefix. It’s also a bad idea to decide a few years down the road that you want to switch teams – so choose wisely.
- **Make sure your site works with or without the leading www prefix.** Regardless of your position on this critically important issue, your site should work either way. Serving up visitors who assumed you had a leading www prefix a 404 page is just plain bad internet citizenship, and borderline rude. Sure, encourage people to use the *correct* form of your URL but don’t penalize them when they fail to respect your wishes. It’s best if you [implement URL rewriting rules](https://blog.codinghorror.com/url-rewriting-to-prevent-duplicate-urls/) that “fix” the error automatically and with no fuss for your visitors.
- **The www prefix is implicit and assumed outside the address bar**. Even if you use it – and many of the biggest sites on the internet still do – nobody *says* the dub-dub-dub any more, and certainly you’re not printing “www” on your logos and business cards and so forth.
- **Consider whether you plan to use other subdomains**. If you plan to have, say, `blog.*` and `mail.*` and `beta.*` subdomain prefixes active on your domain, you might actually want the www as a disambiguator.
- **WARNING**: If you pick the domain `example.com`, be aware that *all* cookies you store on that domain will be sent to all subdomains… forever. This is a major downside I didn't discover until years later, and it's big enough to make me regret choosing `stackoverflow.com` versus `www.stackoverflow.com`.


Beyond that, it’s largely a matter of taste, though you could make a case that [user-centered URL design](https://web.archive.org/web/20080510094746/http://blog.welldesignedurls.org/2007/02/19/urlquiz-1-www-or-non-www/) should rule the day. If we’re dropping the www prefix, why stop there? Why not drop the http:// protocol specifier before it, and the inevitable .com at the end, too?


For me, though, the great dub-dub-dub debate is mostly a source of amusement. Readable URLs are important, but **you should be far more concerned about the content behind that URL than the URL itself**. It’s the kind of meaningless distraction that is parodied beautifully in the animated series [Home Movies](http://en.wikipedia.org/wiki/Home_Movies_(TV_series)).

kg-card-begin: html
kg-card-end: html

> **Melissa:** You know, Brendan, you don’t have to say dubya-dubya-dubya any more.
> **Brendan:** What? Why?
> **Melissa:** You can just say the website name without the dubya-dubya-dubya.
> **Brendan:** No, no, no. That’s how you type it in, Melissa. Dubya-dubya-dubya dot..
> **Melissa:** I know that’s how you *type* it, but you don’t have to *say* it. If you said to me, moviewinnerorweiner dot com, I would know what you meant, without the double-u.. double-u.. double-u.
> **Brendan:** So no w’s, ever?
> **Melissa:** OK, Brendan, for the sake of *this* conversation, you don’t have to say dubyadubyadubya. Because I know what it is. And so does the rest of the world.

kg-card-begin: html
kg-card-end: html

> **Brendan:** dubya-dubya-dubya dot movieweinerorwinner dot com likes my stuff a lot, so they asked me to write some stuff.
> **Jason:** you’re writing a review for dubya-dubya-dubya dot movieweinerorwinner dot com?
> **Melissa:** (shouting) You guys, you don’t have to say dubya-dubya-dubya!
> **Brendan:** But yet..
> **Melissa:** I don’t want to have this conerversation again!
> **Jason:** What are you talking about, Melissa?
> **Brendan:** You have to say it Melissa. You gotta say it.
> **Melissa:** (exasperated sigh) You don’t!
> **Brendan:** You *gotta* say it.
> **Melissa:** You don’t, because everyone knows what it means!
> **Jason:** How do you know it’s a website?
> **Melissa:** Because you say dot com.
> **Jason:** Yeah, but how do you know it’s dubya-dubya-dubya?
> **Brendan:** Yeah, that’s a good point!
> **Melissa:** Because it’s just one of those things that when something’s around for a long enough time in society, you can just abbreviate it.
> **Brendan:** Like what else?
> **Jason:** Like what, like names? Names of people?
> **Brendan:** That’s what I was saying.
> **Melissa:** (exasperated) All right, you know what? Say dubya-dubya-dubya, I don’t care.
> **Jason:** No, you know what I’m saying.
> **Melissa:** No, forget it. You’re right. In fact, don’t say dubya-dubya-dubya, say “world wide web” every time you say a website.
> (pause)
> **Jason:** No, that’s a total waste.
> **Brendan:** That’s a waste of time.


My point exactly.

[web development](https://blog.codinghorror.com/tag/web-development/)
[url conventions](https://blog.codinghorror.com/tag/url-conventions/)
[seo](https://blog.codinghorror.com/tag/seo/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
[coding standards](https://blog.codinghorror.com/tag/coding-standards/)
