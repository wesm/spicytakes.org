---
title: "I Just Logged In As You: How It Happened"
date: 2009-05-05
url: https://blog.codinghorror.com/i-just-logged-in-as-you-how-it-happened/
slug: i-just-logged-in-as-you-how-it-happened
word_count: 841
---

In my previous post [I Just Logged In As You](https://blog.codinghorror.com/i-just-logged-in-as-you/), I disclosed that someone was logging in as me – specifically because they **discovered my password**. But how?


If I wanted to discover someone’s password, I can think of a few ways:

1. **Educated guess.** If you know someone’s birthday, their pets, their children’s names, favorite movies, and so on – these are all potential passwords in various forms. This is classic social engineering, and it can work; that’s essentially how [Sarah Palin’s email was hacked](https://web.archive.org/web/20090519072445/http://www.wired.com/threatlevel/2008/09/palin-e-mail-ha). While my password *was* weak, it wasn’t anything you could reasonably guess based on public information available about me.
2. **Brute force dictionary attack.** If login attempts aren’t meaningfully [rate limited](https://blog.codinghorror.com/rate-limiting-and-velocity-checking/), then you can attempt a dictionary attack and pray the target password is a simple dictionary word. That’s how one [Twitter administrator’s account was compromised](https://web.archive.org/web/20090505225826/http://www.wired.com/threatlevel/2009/01/professed-twitt/). But failing to rate limit password attempts is strictly amateur hour stuff (and I’d argue borderline incompetence); no OpenID provider of any consequence would make this mistake.
3. **Interception.** Eavesdrop on the user in any way you can to discover their password: install a hardware keylogger, software keylogger, or perform network sniffing of unencrypted traffic. If you have physical access to the user, low-tech analog methods such as watching over someone’s shoulder as they type in their password are effectively the same thing. While I can’t *rule out* paranoid fantasies of keyloggers, if my machine was so thoroughly [0wnz0red](https://web.archive.org/web/20090516184747/http://dir.salon.com/story/tech/feature/2002/08/28/0wnz0red/index.html), I think my OpenID password would have been the least of my worries at that point.
4. **Impersonation.** Commonly known as phishing. You present the user with a plausible looking login page for a service they already use, and hope they enter their credentials. Alternately, in the depressingly common Web 2.0 style, you can just demand that [users give up their credentials](https://blog.codinghorror.com/please-give-us-your-email-password/) for some trivial integration feature with the target website. I consider both forms of phishing, and I call it [the forever hack](https://blog.codinghorror.com/phishing-the-forever-hack/) for good reason.


So which of these methods did this person use to obtain my password? **None of them**.


> It wasn’t a guess and it wasn’t brute force.
> I guess I can tell you, so you don’t fall into this trap again. **There’s a site I help out with that doesn’t salt their passwords.** They’re MD5 encrypted, but if you’ve got a dictionary password, it’s very easy to use a reverse-MD5 site to get the original. I was able to figure out you were a user on the site some time back, and realized I could do this, if only I knew your openid provider...
> (As an aside, I complained to the head of the site months ago that he ought to start salting passwords for this exact reason. I also run my passwords I need to be secure through a few reverse-hash websites, just to ensure that it’s not stored somewhere.)
> So, the unethical part was actually looking up this information in the first place. I apologize. But like I said, better than someone else getting into this data.


Hey, it looks like [**you’re storing passwords incorrectly!**](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/)


![](https://blog.codinghorror.com/content/images/2025/04/image-362.png)


We have met the enemy, and he is... programmers just like us. Seriously, go read that blog entry. It is exactly, *exactly* what just happened to me.


When I say programmers like us, I mean me, too. I acknowledge that I am also at fault here, for...

- using the same low-value credential password in two places.
- picking a particularly weak password.
- not using a high-value credential for something that clearly deserved it, namely, my moderator login to Stack Overflow.


All of this is true, and I shoulder the blame for that. Perhaps I should [take my own advice](https://blog.codinghorror.com/passphrase-evangelism/). A moment of weakness, I suppose.


The important thing to take away from this, if you’re a programmer working on an application that stores user credentials, is to ***get the hell out of the business of storing user credentials!*** As we’ve seen today, the world is full of stupid users like me who do incredibly stupid things. Are you equipped and willing do everything necessary to protect idiots like me from myself? That’s a key part of the promise of OpenID, and one of the reasons we chose it as the authentication system for Stack Overflow. As one commenter [noted](http://www.reddit.com/r/programming/comments/8hpog/i_just_logged_in_as_you/c09bq23) on Reddit:


> I, for one, think that my OpenID provider is more secure than the average guy running a forum.


Exactly. We outsourced our user credential system to people who are much better at it than us (well, depending on which OpenID provider you pick). And also because we didn’t think the world needed [yet another username and password](https://blog.codinghorror.com/openid-does-the-world-really-need-yet-another-username-and-password/). You’re welcome. I think.


So, what have we learned?

1. Programmers are the enemy.
2. Hey... wait a second, *I’m* a programmer!
3. `GOTO 1`


(Oh, and credit to [Malte](https://www.industrialempathy.com/), the first commenter to correctly identify what the likely password vulnerability was – less than an hour after the entry was posted!)

[social engineering](https://blog.codinghorror.com/tag/social-engineering/)
[password security](https://blog.codinghorror.com/tag/password-security/)
[brute force attack](https://blog.codinghorror.com/tag/brute-force-attack/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[password protection](https://blog.codinghorror.com/tag/password-protection/)
