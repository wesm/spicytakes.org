---
title: "CAPTCHA is Dead, Long Live CAPTCHA!"
date: 2008-03-04
url: https://blog.codinghorror.com/captcha-is-dead-long-live-captcha/
slug: captcha-is-dead-long-live-captcha
word_count: 646
---

In November 2007 I called these three [CAPTCHA implementations “unbreakable”](https://blog.codinghorror.com/has-captcha-been-broken/):

kg-card-begin: html


| Google
(unbreakable) |  |
| Hotmail
(unbreakable) |  |
| Yahoo
(unbreakable) |  |


kg-card-end: html

2008 is shaping up to be a very bad year indeed for CAPTCHAs:

- Jan 17: InformationWeek reports [Yahoo CAPTCHA broken](https://web.archive.org/web/20080308222203/http://www.informationweek.com/news/showArticle.jhtml?articleID=205900620)
- Feb 6: Websense reports [Hotmail CAPTCHA broken](https://web.archive.org/web/20080324135538/http://www.websense.com/securitylabs/blog/blog.php?BlogID=171)
- Feb 22: Websense reports [Google CAPTCHA broken](https://web.archive.org/web/20080304081037/http://www.websense.com/securitylabs/blog/blog.php?BlogID=174)


Which means I am now 0 for 3. Understand that **I am no fan of CAPTCHA**. I view them as a [necessary and important evil](https://blog.codinghorror.com/captcha-effectiveness/), one of precious few things separating average internet users from a torrential deluge of email, comment, and forum spam.


So reading that the three best CAPTCHA implementations have been defeated sort of breaks my heart. Even what I consider to be the strongest, Google’s implementation, fell hard:


> On average, only 1 in every 5 CAPTCHA breaking requests are successfully including both algorithms used by the bot, approximating a success rate of 20%.


A twenty percent success rate doesn’t sound like much, but these spammers are harnessing networks of compromised PCs to send out thousands upon thousands of simultaneous sign-up requests to GMail, Hotmail, and Yahoo Mail from computers all over the world. Even a *five percent* success rate against a particular email service CAPTCHA would be cause for serious concern; with twenty percent success rate you might as well put a fork in that thing – it’s done.


In the meantime, CAPTCHA still serves a useful purpose – speed bumps that prevent evil bots and the nefarious people who run them from *completely *overrunning the internet, [as Gunter Ollman notes](https://web.archive.org/web/20080403060415/http://blogs.iss.net/archive/CAPTCHA.html):


> CAPTCHAs were a good idea, but frankly, in today’s profit-motivated attack environment they have largely become irrelevant as a protection technology. Yes, the CAPTCHAs can be made stronger, but they are already too advanced for a large percentage of Internet users. Personally, I don’t think it’s really worth strengthening the algorithms used to create more complex CAPTCHAs – instead, just deploy them as a small “speed-bump” to stop the script-kiddies and their unsophisticated automated attack tools. CAPTCHAs aren’t the right tool for stopping today’s commercially minded attackers.


There’s simply too much money to be made in email spam for the commercial CAPTCHA algorithms, regardless of how good they may be, to survive forever. How old is Google’s CAPTCHA now? Two to three years old? In the short term, **perhaps proliferation and evolution of many different CAPTCHA techniques is the most effective prevention**. You should *emulate* the techniques from the most effective and human-readable industrial grade commercial CAPTCHA, but avoid copying them outright. Otherwise, when they’re inevitably broken, you’re broken too. CAPTCHA defeating tools are tailored to very specific inputs; if there’s little to no monetary incentive, odds are nobody will bother to customize one for yours. My ridiculously simple “orange” comment form protection is ample evidence of that.


Beyond diversification, the deeper question remains: **how do we tell automated bots from people – without alienating our users in the process?** How can we build a next generation CAPTCHA that’s less vulnerable to attack?


Here’s some food for thought:

- [Distinguish pictures of dogs from cats](https://web.archive.org/web/20080309144356/http://research.microsoft.com/asirra/)
- Choose a word that relates to all the images
- [ASCII art](https://web.archive.org/web/20080311141522/http://www.thephppro.com/products/captcha/)
- [Solve failed OCR inputs](https://web.archive.org/web/20080307015310/http://recaptcha.net/learnmore.html)
- Trivia questions
- Math and word problems


At some point, unfortunately, CAPTCHA devolves from a simple human reading test into an intelligence test or an acuity test. Depending on how invasive you want to be, you’ll eventually be forced to [move to two-factor authentication](https://blog.codinghorror.com/what-you-have-what-you-know-what-you-are/), like sending a text message to someone’s cell phone with a temporary key.


I don’t have the all answers, but one thing is for sure: I hate spammers. As fellow spam-hating internet users we all have a vested interest in **seeing CAPTCHA techniques evolve to defeat spammers**.

[security](https://blog.codinghorror.com/tag/security/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[spam prevention](https://blog.codinghorror.com/tag/spam-prevention/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[internet security](https://blog.codinghorror.com/tag/internet-security/)
