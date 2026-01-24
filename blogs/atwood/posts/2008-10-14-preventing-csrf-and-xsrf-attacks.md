---
title: "Preventing CSRF and XSRF Attacks"
date: 2008-10-14
url: https://blog.codinghorror.com/preventing-csrf-and-xsrf-attacks/
slug: preventing-csrf-and-xsrf-attacks
word_count: 814
---

In [Cross-Site Request Forgeries and You](https://blog.codinghorror.com/cross-site-request-forgeries-and-you/) I urged developers **to take a close look at possible CSRF / XSRF vulnerabilities on their own websites**. They’re the worst kind of vulnerability – very easy to exploit by attackers, yet not so intuitively easy to understand for software developers, at least until you’ve been bitten by one.


On the [Freedom to Tinker blog](http://freedom-to-tinker.com/blog/wzeller/popular-websites-vulnerable-cross-site-request-forgery-attacks), Bill Zeller offers one of the best, most concise explanation of XSRF that I’ve read to date:


> CSRF vulnerabilities occur when a website allows an authenticated user to perform a sensitive action but does not verify that the user herself is invoking that action. **The key to understanding CSRF attacks is to recognize that websites typically don’t verify that a request came from an authorized user. Instead they verify only that the request came from the *browser* of an authorized user.** Because browsers run code sent by multiple sites, there is a danger that one site will (unbeknownst to the user) send a request to a second site, and the second site will mistakenly think that the user authorized the request.


That’s the key element to understanding XSRF. **Attackers are gambling that users have a validated login cookie for your website already stored in their browser.** All they need to do is get that browser to make a request to your website on their behalf. If they can either:

1. Convince your users to click on a HTML page they’ve constructed
2. Insert arbitrary HTML in a target website that your users visit


The XSRF game is afoot. Not too difficult, is it?


Bill Zeller and Ed Felten also identified new XSRF vulnerabilities in four major websites less than two weeks ago:

1. ING Direct
*We discovered CSRF vulnerabilities in ING’s site that allowed an attacker to open additional accounts on behalf of a user and transfer funds from a user’s account to the attacker’s account.*
2. YouTube
*We discovered CSRF vulnerabilities in nearly every action a user can perform on YouTube.*
3. MetaFilter
*We discovered a CSRF vulnerability in MetaFilter that allowed an attacker to take control of a user’s account.*
4. The New York Times
*We discovered a CSRF vulnerability in NYTimes.com that makes user email addresses available to an attacker. If you are a NYTimes.com member, arbitrary sites can use this attack to determine your email address and use it to send spam or to identify you.*


If major public facing websites are falling prey to these serious XSRF exploits, how confident do you feel that *you* haven’t made the same mistakes? Consider carefully. I’m saying this as a developer who has *already* made these same mistakes on his own website. **I’m just as guilty as anyone.**


It’s our job to make sure future developers don’t repeat the same stupid mistakes we made – at least not without a fight. The Felten and Zeller paper (pdf) recommends the “double-submitted cookie” method to prevent XSRF:


> When a user visits a site, the site should generate a (cryptographically strong) pseudorandom value and set it as a cookie on the user’s machine. **The site should require every form submission to include this pseudorandom value as a form value and also as a cookie value.** When a POST request is sent to the site, the request should only be considered valid if the form value and the cookie value are the same. When an attacker submits a form on behalf of a user, he can only modify the values of the form. An attacker cannot read any data sent from the server or modify cookie values, per [the same-origin policy](https://web.archive.org/web/20081014022433/http://developer.mozilla.org/en/Same_origin_policy_for_JavaScript). This means that while an attacker can send any value he wants with the form, he will be unable to modify or read the value stored in the cookie. Since the cookie value and the form value must be the same, the attacker will be unable to successfully submit a form unless he is able to guess the pseudorandom value.


The advantage of this approach is that it requires no server state; you simply set the cookie value once, then every HTTP POST checks to ensure that one of the submitted <input> values contains the exact same cookie value. Any difference between the two means a possible XSRF attack.


An even stronger, albeit more complex, prevention method is to leverage server state – **to generate (and track, with timeout) a unique random key for every single HTML FORM you send down to the client.** We use a variant of this method on Stack Overflow with great success. That’s why with every <form> you’ll see the following:

kg-card-begin: html

```

<input id=“fkey” name=“fkey” type=“hidden” value=“df8652852f139” />

```

kg-card-end: html

If you want to audit a website for XSRF vulnerabilities, start by asking this simple question about every single HTML form you can find: **“where’s the XSRF value?”**

[security](https://blog.codinghorror.com/tag/security/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[csrf](https://blog.codinghorror.com/tag/csrf/)
[xsrf](https://blog.codinghorror.com/tag/xsrf/)
[vulnerabilities](https://blog.codinghorror.com/tag/vulnerabilities/)
