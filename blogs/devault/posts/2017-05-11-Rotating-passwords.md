---
title: "Rotating passwords in bulk in the wake of security events"
date: 2017-05-11
url: https://drewdevault.com/2017/05/11/Rotating-passwords.html
slug: Rotating-passwords
word_count: 469
---

I’ve been putting this post off for a while. Do you remember the  [CloudFlare
security
problem](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/) 
that happened a few months ago? This is the one that disclosed huge amounts of
sensitive information for huge numbers websites. When this happened, your
accounts on  [thousands of
websites](https://github.com/pirate/sites-using-cloudflare)  were potentially
compromised.

Updating passwords for all of these services at once was a major source of
frustration for users. Updating a single password can take 5 minutes, and
changing dozens of them might take hours. I decided that I wanted to make this
process easier.

```
$ ./pass-rotate github.com linode.com news.ycombinator.com twitter.com
Rotating github.com... 
  Enter your two factor (TOTP) code:
OK
Rotating linode.com... 
  Enter your two-factor (TOTP) code:
OK
Rotating news.ycombinator.com... OK
Rotating twitter.com... 
  Enter your SMS authorization code:
OK                                                                       
```

I just changed 4 passwords in about 20 seconds. This is
 [pass-rotate](https://github.com/SirCmpwn/pass-rotate) , which is basically
youtube-dl for rotating passwords. It integrates with your password manager to
make it easy to change your password. pass-rotate is also provided in the form
of a library that password managers can directly integrate with to provide
first-class support for password rotation with a shared implementation of
various websites. Not only can it help you rotate passwords after security
events, but it can be used for periodic password rotation to keep your accounts
safer in general.

How this was basically done is by reverse engineering the password change flow of
each of the websites it supports. Each provider’s backend submits HTTP requests
that simulates logging into the website and interacting with the password reset
form. This is often quite simple, like
 [github.py](https://github.com/SirCmpwn/pass-rotate/blob/master/passrotate/providers/github.py) ,
but can sometimes be quite complex, like
 [namecheap.py](https://github.com/SirCmpwn/pass-rotate/blob/master/passrotate/providers/namecheap.py) .

The current list of supported services is available
 [here](https://github.com/SirCmpwn/pass-rotate/wiki/Currently-supported-services) .
There’s also an issue to discuss making a standardized mechanism for automated
password rotation  [here](https://github.com/SirCmpwn/pass-rotate/issues/1) . At
the time of writing, the list of supported services is:

* Cloudflare  ✗ TOTP
* Digital Ocean  ✗ TOTP
* Discord  ✓ TOTP
* GitHub  ✓ TOTP ✗ U2F
* Linode  ✓ TOTP
* NameCheap  ✓ SMS
* Pixiv
* Twitter  ✓ SMS ✓ TOTP
* YCombinator

Adding new services is easy - check out  [the
guide](https://github.com/SirCmpwn/pass-rotate/blob/master/CONTRIBUTING.md) . I
would be happy to merge your pull requests. Please add websites you use and
websites you maintain!

I also set up a Patreon campaign today. If you’d like to contribute to my work,
please visit  [the Patreon page](https://patreon.com/sircmpwn) . This supports all
of my open source projects, but if you want to support pass-rotate in
particular feel free to let me know when you make your contribution. This kind
of project needs long term maintenance to support countless providers and
keep up with changes to them. Feel free to let me know what service providers
you want me to add support for when you make your pledge!
