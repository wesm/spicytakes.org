---
title: "Password Rules Are Bullshit"
date: 2017-03-10
url: https://blog.codinghorror.com/password-rules-are-bullshit/
slug: password-rules-are-bullshit
word_count: 1736
---

Of the many, many, *many* [bad things about passwords](https://blog.codinghorror.com/the-dirty-truth-about-web-passwords/), you know what the worst is? Password rules.


![If we don't solve the password problem for users in my lifetime I am gonna haunt you from beyond the grave as a ghost](https://blog.codinghorror.com/content/images/2025/09/ezgif-85806fa2542788-2.png)


Let this pledge be duly noted on the permanent record of the Internet. I don’t know if there’s an afterlife, but I’ll be finding out soon enough, and I plan to go out *mad as hell*.


The world is absolutely awash in terrible password rules:

- [Dumb Password Rules](https://github.com/duffn/dumb-password-rules)
- [Bad Password Policies](http://badpasswordpolicies.tumblr.com/)
- [Password Requirements Shaming](http://password-shaming.tumblr.com/)


But I don’t need to tell you this. The more likely you are to use a truly random password generation tool, like us über-geeks are supposed to, the more likely you have suffered mightily – and daily – under this regime.


Have you seen the classic [XKCD about passwords](https://xkcd.com/936/)?


![To anyone who understands information theory and security and is in an infuriating argument with someone who does not (possibly involving mixed case), I sincerely apologize.](https://blog.codinghorror.com/content/images/2017/03/password_strength.png)


We [can certainly debate](https://security.stackexchange.com/questions/6095/xkcd-936-short-complex-password-or-long-dictionary-passphrase) whether “correct horse battery staple” is a viable password strategy or not, but the argument here is mostly that *length matters*.


![That's What She Said](https://blog.codinghorror.com/content/images/2017/03/twss.jpg)


No, seriously, it does. I’ll go so far as to say [your password is too damn short](https://blog.codinghorror.com/your-password-is-too-damn-short/). These days, given the state of cloud computing and GPU password hash cracking, any password of 8 characters or less is perilously close to *no password at all*.


So then perhaps we have one rule, that **passwords must not be short**. A long password is much more likely to be secure than a short one… right?


What about this four character password?


![](https://blog.codinghorror.com/content/images/2025/02/image-45.png)


What about this eight character password?


![](https://blog.codinghorror.com/content/images/2025/02/image-44.png)


Or this (hypothetical, but all too real) seven character password?


![](https://blog.codinghorror.com/content/images/2025/02/image-43.png)


> @codinghorror I’m sorry but your password must contain 1 char each from: Arabic, Chinese, Thai, Korean, Klingon, Wingdings and an emoji – Finley Creative (@FinleyCreative) March 3, 2016


You may also be surprised, if you paste the above four Unicode emojis into your favorite login dialog (go ahead – try it), to discover that it… *isn’t* in fact four characters.


![](https://blog.codinghorror.com/content/images/2017/03/discourse-login-emoji-password.png)


Oh dear.


```
"💩".length === 2

```


Our old pal [Unicode strikes again](http://blog.jonnew.com/posts/poo-dot-length-equals-two).


As it turns out, even the simple rule that “your password must be of reasonable length”… ain’t necessarily so. Particularly if we stop thinking like [Ugly ASCII Americans](https://blog.codinghorror.com/the-ugly-american-programmer/).


And what of those nice, long passwords? Are they *always* secure?


```
aaaaaaaaaaaaaaaaaaa
0123456789012345689
passwordpassword
usernamepassword

```


Of course not, because *have you met any users lately?*


![I changed all my passwords to "incorrect"](https://blog.codinghorror.com/content/images/2017/03/incorrect-password.jpg)


They consistently ruin every piece of software I’ve ever written. Yes, yes, I know you, Mr. or Ms. über-geek, know *all* about the concept of entropy. But expressing your love of entropy as terrible, idiosyncratic password rules…

- must contain uppercase
- must contain lowercase
- must contain a number
- must contain a special character


…is a spectacular failure of imagination in a world of Unicode and Emoji.


As we built [Discourse](https://discourse.org/), I discovered that the login dialog was a remarkably complex piece of software, despite its surface simplicity. The primary password rule we used was also the simplest one: **length**. Since I wrote that, we’ve already increased our minimum password default length from 8 to 10 characters. And if you happen to be an admin or moderator, we decided the minimum has to be even more, **15** characters.


I also advocated **checking passwords against the 100,000 most common passwords**. If you look at 10 million [passwords from data breaches in 2016](https://web.archive.org/web/20170116185739/https://blog.keepersecurity.com/2017/01/13/most-common-passwords-of-2016-research-study/), you’ll find the top 25 most used passwords are:

kg-card-begin: html


| `123456`
`123456789`
`qwerty`
`12345678`
`111111`
`1234567890`
`1234567`
`password`
`123123`
`987654321`
`qwertyuiop`
`mynoob` | `123321`
`666666`
`18atcskd2w`
`7777777`
`1q2w3e4r`
`654321`
`555555`
`3rjs1la7qe`
`google`
`1q2w3e4r5t`
`123qwe`
`zxcvbnm`
`1q2w3e` |


kg-card-end: html

Even this data betrays some ASCII-centrism. The numbers are the same in any culture I suppose, but I find it hard to believe the average Chinese person will ever choose the passwords “password” ; “quertyuiop” or “mynoob.” So this list *has* to be customizable, localizable.


(One interesting idea is to search for common shorter password matches inside longer passwords, but I think this would cause too many false positives.)


If you examine the data, this also turns into an argument in favor of password length. Note that only 5 of the top 25 passwords are 10 characters, so if we require 10 character passwords, we’ve already reduced our exposure to the most common passwords by 80%. I saw this originally when I gathered millions and [millions of leaked passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords) for Discourse research, then filtered the list down to just those passwords reflecting our new minimum requirement of 10 characters or more.


![](https://blog.codinghorror.com/content/images/2017/03/top-million-common-passwords-by-length.png)


It suddenly became a *tiny* list. (If you’ve done similar common password research, please do share your results in the comments.)


I’d like to offer the following common sense advice to my fellow developers:


#### 1. Password rules are bullshit

- They don’t work.
- They heavily penalize your ideal audience, people that use real random password generators. Hey guess what, that password randomly *didn’t* have a number or symbol in it. I just double checked my math textbook, and yep, it’s possible. I’m pretty sure.
- They frustrate average users, who then become uncooperative and use “creative” workarounds that make their passwords *less* secure.
- They are often wrong, in the sense that the rules chosen are grossly incomplete and/or insane, per the many shaming links I’ve shared above.
- Seriously, for the *love of God*, stop with this arbitrary password rule nonsense already. If you won’t take my word for it, read this [2016 NIST password rules recommendation](https://web.archive.org/web/20160819155226/https://nakedsecurity.sophos.com/2016/08/18/nists-new-password-rules-what-you-need-to-know/). It’s right there, “no composition rules.” However, I do see one error, it should have said “no *bullshit* composition rules.”


#### 2. Enforce a minimum *Unicode* password length


One rule is at least easy to remember, understand, and enforce. This is the proverbial one rule to bring them all, and in the darkness bind them.


![](https://blog.codinghorror.com/content/images/2017/03/one-donut-to-bind-them-all.jpg)

- It’s simple. Users can count. Most of them, anyway.
- It works. The data *shows us* it works; just download any common password list of your choice and group by password length.
- The math doesn’t lie. All other things being equal, a longer password *will* be more random – and thus more secure – than a short password.
- Accept that even this one rule isn’t inviolate. A minimum password length of 6 on a Chinese site *might* be perfectly reasonable. A 20 character password *can* be ridiculously insecure.
- If you don’t allow (almost) every single Unicode character in the password input field, you are probably doing it wrong.
- It’s a bit of an implementation detail, but make sure *maximum* password length is reasonable as well.


#### 3. Check for common passwords


As I’ve already noted, the definition of “common” depends on your audience, and language, but it is a terrible disservice to users when you let them choose passwords that exist in the list of 10k, 100k, or million most common known passwords from data breaches. There’s *no question* that a hacker will submit these common passwords in a hack attempt – and it’s shocking how far you can get, even with aggressive password attempt rate limiting, using just the 1,000 most common passwords.

- 1.6% have a password from the top 10 passwords
- 4.4% have a password from the top 100 passwords
- 9.7% have a password from the top 500 passwords
- 13.2% have a password from the top 1,000 passwords
- 30% have a password from the top 10,000 passwords


Lucky you, there are millions and millions of real breached password lists out there to sift through. It is sort of fun to do data forensics, because these aren’t hypothetical synthetic Jack the Ripper password rules some bored programmer dreamed up, these are *real* passwords used by *real* users.


Do the research. Collect the data. Protect your users from themselves.


#### 4. Check for basic entropy


No need to get fancy here; pick the measure of entropy that satisfies you deep in the truthiness of your gut. But remember you have to be able to *explain* it to users when they fail the check, too.


![](https://blog.codinghorror.com/content/images/2025/02/image-46.png)


I had a bit of a sad when I realized that we were perfectly fine with users selecting a 10 character password that was literally “aaaaaaaaaa.” In my opinion, the simplest way to do this is to ensure that there are at least (x) unique characters out of (y) total characters. And that’s what we do as of the current beta version of Discourse. But I’d love your ideas in the comments, too. The simpler and clearer the better!


#### 5. Check for special case passwords


I’m embarrassed to admit that when building the Discourse login, as I discussed in [The God Login](https://blog.codinghorror.com/the-god-login/), we missed two common cases that you really *have* to block:

- password equal to username
- password equal to email address


🤦 If you are using Discourse versions earlier than 1.4, I’m so sorry and *please upgrade immediately*.


Similarly, you might also want to block other special cases like:

- password equal to URL or domain of website
- password equal to app name


In short, try to think outside the password input box, like a user would.


> 🔔 **Clarification**
> A few people have interpreted this post as “all the *other* password rules are bullshit, except these four I will now list.” That’s not what I’m trying to say here.
> The idea is to focus on the one understandable, simple, practical, works-in-real-life-in-every-situation rule: **length**. Users can enter (almost) anything, in proper Unicode, *provided it*’*s long enough*. That’s the **one rule to bind them all** that we need to teach users: length!
> Items #3 through #5 are more like genie-special-exception checks, a you [can’t wish for infinite wishes](https://www.youtube.com/watch?v=Bwic3hJ4q1A) kind of thing. It doesn’t need to be discussed up front because it *should* be really rare. Yes, you must stop users from having comically bad passwords that equal their username, or `aaaaaaaaaaa` or `0123456789`, but only as post-entry checks, not as rules that need to be explained in advance.
> So TL;DR: one rule. Length. Enter whatever you want, just make sure it’s long enough to be a reasonable password.

[passwords](https://blog.codinghorror.com/tag/passwords/)
[password policies](https://blog.codinghorror.com/tag/password-policies/)
[password management](https://blog.codinghorror.com/tag/password-management/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
