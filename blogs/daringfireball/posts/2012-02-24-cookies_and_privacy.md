---
title: "Cookies and Privacy"
date: 2012-02-24
url: https://daringfireball.net/2012/02/cookies_and_privacy
slug: cookies_and_privacy
word_count: 1839
---


A week ago, John Battelle wrote a curious response to [this Wall Street Journal report](http://online.wsj.com/article/SB10001424052970204880404577225380456599176.html?mod=WSJ_hp_LEFTTopStories) about Google circumventing Safari’s (and, notably, Mobile Safari’s) default setting only to accept cookies from visited websites.


Long story short: Web [cookies](http://en.wikipedia.org/wiki/HTTP_cookie) are small bits of saved data that websites can store in your browser. Cookies are restricted by domain; if example.com stores a cookie in your browser, the only website your browser sends that cookie back to is example.com. But, by default, most desktop web browsers allow “third-party” cookies. That means if a page on *example.com* loads JavaScript from a different domain, that JavaScript is able to use cookies too. One common use is by ad networks; an ad network can set a cookie and then access that same cookie from any website that uses the same ad network. Google makes use of such cookies to display its ads. Ad networks that use cookies in this manner do so in order to track users across websites.


All major browsers give the user control over cookie permissions. Usually, with three options:

- Accept cookies from anywhere (i.e., allow third-party cookies)
- Accept cookies only from visited websites (disallow third-party cookies)
- Don’t accept any cookies at all


The difference with Safari is in the default for this setting. Most major browsers default to the first option, allowing all cookies. Safari and Mobile Safari default to the second, allowing only first-party cookies.


What the WSJ discovered is that Google (and a few other ad networks) found a way to store third-party cookies in Safari and Mobile Safari even when the option was set only to accept cookies from visited websites, as it is by default.


That brings us to Battelle’s response, “[A Sad State of Internet Affairs: The Journal on Google, Apple, and ‘Privacy’](http://battellemedia.com/archives/2012/02/a-sad-state-of-internet-affairs-the-journal-on-google-apple-and-privacy.php)”. (Background information: Battelle is [an expert on Google](http://www.amazon.com/Search-Rewrote-Business-Transformed-Culture/dp/1591840880), and is the founder and executive chair of [Federated Media](http://www.federatedmedia.net/), an ad network.)


Battelle writes:


> Here’s the lead in the Journal’s story, which requires a
> login/registration:
> “Google Inc. and other advertising companies have been bypassing
> the privacy settings of millions of people using Apple Inc.’s Web
> browser on their iPhones and computers — tracking the
> Web-browsing habits of people who intended for that kind of
> monitoring to be blocked.”
> Now, from what I can tell, the first part of that story is true —
> Google and many others have figured out ways to get around Apple’s
> default settings on Safari in iOS — the only browser that comes
> with iOS, a browser that, in my experience, has never asked me
> what kind of privacy settings I wanted, nor did it ask if I wanted
> to share my data with anyone else (I do, it turns out, for any
> number of perfectly good reasons).


Battelle has a good point here, which is that the Journal’s use of “intended” is too broad a stroke. *Some* Safari users have deliberately specified their cookie privacy settings, but most (and I’d wager nearly all) have never changed the default, and don’t even know what cookies are. But that’s true for users of all browsers, not just Safari. And it’s true for all settings, not just cookie preferences. *Most users don’t change settings and just use the defaults.* Default settings are incredibly important.


I can’t recall any browser prompting me about cookie privacy settings before using it.


> Apple assumes that I agree with Apple’s point of view on
> “privacy,” which, I must say, is ridiculous on its face, because
> the idea of a large corporation (Apple is the largest, in fact)
> determining in advance what I might want to do with my data is
> pretty much the opposite of “privacy.”


The difference with Safari isn’t that Apple has made *an* assumption about the user’s view regarding cookie privacy; it’s that Apple has made a *different* assumption than that made by other browser vendors.


> Then again, Apple decided I hated Flash, too, so I shouldn’t be
> that surprised, right?


Deciding that iOS would be better without Flash is not the same thing as deciding that all iOS users “hate” Flash.


> In short, Apple’s mobile version of Safari broke with common web
> practice, and as a result, it broke Google’s normal approach to
> engaging with consumers.


I’d have used “tracking” in place of “engaging with”, but that’s semantics. My quibble is with the notion that Safari “broke with common web practice”. All major browsers have an option to block third-party cookies. And I’ll bet Safari is not the first to block them by default. What’s new is that Safari (a) blocks third-party cookies by default, and (b) is popular and growing (particularly in mobile).


Safari hasn’t broken the web; it has simply broken the heretofore safe assumption that an overwhelming majority of web surfers accepted third-party cookies.


> Was Google’s “normal approach” wrong? Well, I suppose that’s a
> debate worth having — it’s currently standard practice and the
> backbone of the entire web advertising ecosystem — but the
> Journal doesn’t bother to go into those details. One can debate
> whether setting cookies should happen by default — but the fact
> is, that’s how it’s done on the open web.


Here, I think Battelle falls off the rails. No one is criticizing Google for using third-party tracking cookies in general. No one. What’s being criticized is Google devising and implementing a method to store third-party cookies in web browsers which are set not to accept third-party cookies. It didn’t happen by accident. Google wrote code specifically to circumvent this setting in Safari.


> The Journal article does later acknowledge, though not in a way
> that a reasonable reader would interpret as meaningful, that the
> mobile version of Safari has “default” (ie not user activated)
> settings that prevent Google and others (like ad giant WPP) to
> track user behavior the way they do on the “normal” Web. That’s a
> far cry from the Journal’s lead paragraph, which again, states
> Google bypassed the “the privacy settings of millions of people.”
> So when is a privacy setting really a privacy setting, I wonder?
> When Apple makes it so?


Again: we’re all in agreement here that this is a dispute about *default* settings, not which settings are available for user tweaking. So let’s concede that Battelle has a point that Google didn’t bypass the privacy settings of millions of *people* so much as they bypassed the privacy settings of millions of *web browsers*. What Battelle is implicitly arguing here is that it’s OK — or at least not so bad — for Google to bypass browser privacy settings if most users didn’t specify those settings manually. (There’s no way for Google to tell which Safari users block third-party cookies simply by default and which ones block them because they understand what’s going on and have made an explicit choice.)


> Since this story has broken, Google has discontinued its practice,
> making it look even worse, of course.


I’d argue that Google would look worse if they had continued the practice, even after it had been publicized.


> But let’s step back a second here and ask: why do you think Apple
> has made it impossible for advertising-driven companies like
> Google to execute what are industry standard practices on the open
> web (dropping cookies and tracking behavior so as to provide
> relevant services and advertising)? Do you think it’s because
> Apple cares deeply about your privacy?
> Really?


But they haven’t made it impossible. They’ve only changed the *default*. But the truth is the default setting is all that matters to Google and other immense ad networks, because what matters to them is aggregate user tracking, not individual user tracking.1


I certainly can’t prove that Apple specified this default setting for the sake of user privacy, rather than out of competitive spite against Google.2 But I’m thinking that if you took a thousand random iOS and Mac users, sat them down and explained to them in layman’s terms what browser cookies are and how Google uses them to track their behavior across the web, and then conducted a survey among them as to what Safari’s default cookie privacy setting should be, we’d find out that Apple chose well to break with tradition here.


> In this case, what Google and others have done sure sounds wrong
> — if you’ve going to resort to tricking a browser into offering
> up information designated by default as private, you need to
> somehow message the user and explain what’s going on.


*Sounds* wrong, or *is* wrong?


> Then again, in the open web, you don’t have to — most browsers
> let you set cookies by default.


So Safari isn’t part of the “open web” because it doesn’t allow ad networks to track users across websites by default? Used to be that all major browsers allowed websites to create pop-up (and pop-under) windows for advertising; are browsers that block such pop-ups by default not part of the “open web” as well?


What I detect in Google’s behavior (and Battelle’s more-or-less defense of it) is a sense of entitlement. That because in the past ad networks could track almost all users via cookies, they are entitled to continue tracking almost all users across the web via cookies, even when a large (and growing) number of them begin using a web browser which, by default, tries to prevent it.


Arguing that Google didn’t do anything wrong — or all that wrong — is one thing. But trying to spin this into an argument that Apple has done something wrong, and that Google was just reacting naturally, is something else.


---

1. The same goes for Flash. Mobile Safari wasn’t the first browser to ship without support for Flash or other media plugins. What made Mobile Safari’s lack of Flash support controversial is that it was the first *popular* browser to ship without Flash support, and thus the first to disrupt the assumption that “almost all” browsers had Flash support. ↩︎
2. It would be interesting to know what this setting defaulted to on the original iPhone back in 2007, when Apple and Google were buddy-buddy and Eric Schmidt even got to come on stage during the iPhone introduction and talk about what great corporate friends Apple and Google were.
**Update 1:**[This iLounge screenshot gallery of iPhone OS 1.0.2](http://www.ilounge.com/index.php/articles/comments/whats-changed-iphone-102-versus-111/) suggests the default setting has always been to disallow third-party cookies in Mobile Safari.
**Update 2:**I haven’t found any proof I can link to, but several DF readers attest that Safari for Mac debuted in 2003 with the same cookie privacy default setting. [This is also reported by Jonathan Mayer](http://webpolicy.org/2012/02/20/setting-the-record-straight-on-googles-safari-tracking/), the privacy/security researcher at Stanford who first uncovered Google’s circumvention of Safari’s cookie privacy settings. ↩︎



| **Previous:** | [Mountain Lion](https://daringfireball.net/2012/02/mountain_lion) |
| **Next:** | [Only Apple](https://daringfireball.net/2012/03/only_apple) |


PreviousNext