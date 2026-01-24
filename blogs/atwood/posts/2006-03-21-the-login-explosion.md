---
title: "The Login Explosion"
date: 2006-03-21
url: https://blog.codinghorror.com/the-login-explosion/
slug: the-login-explosion
word_count: 781
---

I have fifty online logins, and I can’t remember any of them.


![](https://blog.codinghorror.com/content/images/2025/05/image-234.png)


What’s my password? I can’t use the same password for every website. That’s not secure. So every password is unique and specific to that website. And what’s my login name? Hopefully it’s my email address, if the site allows that. But which email address?


What’s a poor user to do?


Scott Hanselman recently highlighted [what he uses](http://www.hanselman.com/blog/MicrosoftFingerprintReaderAndPasswordMinder.aspx) to combat the login explosion:

- [Microsoft Fingerprint Reader](https://web.archive.org/web/20060405030125/http://www.microsoft.com/hardware/mouseandkeyboard/productdetails.aspx?pid=036)
- [Keith’s Password Minder](https://web.archive.org/web/20060406150842/http://www.pluralsight.com/tools.aspx)
- [Foldershare](https://web.archive.org/web/20060423235636/http://weblogs.asp.net/rosherove/archive/2006/02/16/438417.aspx) to synchronize the password file across multiple computers


When you need two programs, a bit of hardware, your finger, and a file-sharing web service to solve a problem, you don’t really have a solution for the login explosion. **What you have is an even bigger problem**.


![](https://blog.codinghorror.com/content/images/2025/05/image-235.png)


One particular pitfall is **the idea that your fingerprint is a secure substitute for your password**. This review of a [typical USB fingerprint reader](http://www.dansdata.com/uareu.htm) illustrates just how foolish that misconception is:


> *The jelly fingertip peeled off the putty very easily, as you’d expect – clean, cold Silly Putty doesn’t stick very well to anything but itself. The gelatin was full of bubbles from my stirring, but the jelly thumb nonetheless had a pretty good complement of print-ridges on it.
> Ugly and bubble-y the jelly thumb was, but the scanner loved it. **It thought the jelly finger was a real one more than 50% of the time.** And since you can attempt recognition about once a second, that means it’d be trivially easy to log in with a thing like this, even with people watching. Trim the jelly so it fits over the end of your real finger, and some very rudimentary prestidigitation will keep your fakery from the attention of onlookers.
> I also found it was possible to enroll the jelly thumb as a new finger. It took me four attempts to do it, and its recognition rate wasn’t any better than when I was trying to match it to my real finger. But that’s still quite good enough to be useable in an, um, covert situation.*


Making a [gummi fingertip](http://cryptome.org/gummy.htm) is not difficult, and all current fingerprint readers are fooled by even marginal gummi fingertips a [hundred percent of the time](http://cryptome.org/fake-prints.htm). In fact, all biometric systems have significant weaknesses:


> *Earlier [in 2002], German tech mag c’t *[*tested nine fingerprint scanners*](http://www.heise.de/ct/english/02/11/114/)* (six capacitive, two optical and one thermal), plus Panasonic’s Authenticam iris scanner, and Cognitec Systems’ FaceVACS-Logon facial recognition system. All of the widgets tested were current models, and all came with impressive marketing claims.
> Two finger scanners c’t tested just didn’t work properly. Of the remainder, the capacitive sensors could be fooled in a number of ways if an authorized user hasn’t cleaned the sensor after fingering it. A latent print on many capacitive sensors can be revived by, for instance, breathing on it, applying graphite powder, or pressing a plastic carrier bag with water in it up against the sensor.
> The graphite powder method works with lifted prints, too – follow your target to the pub, grab his glass after he’s finished with it, dust a print with graphite, lift it with tape, and you’re ready to go.
> Optical sensors didn’t fare any better. C’t fooled them with silicone fingers made from an impression in wax, and also succeeded with backlit graphite print-copies on tape.*


All biometrics can be easily attacked with commonly available materials and widely known techniques.


But the real problem isn’t the biometrics. **The real problem is relying on a single method of security**. Any security expert can tell you that security is based on...

1. What you are
2. What you know
3. What you have


Any authentication method that relies on only *one* of these things is inherently insecure. If you lose your laptop (something you have), you’re still somewhat protected because the thief does not have your password (something you know). Ditto for your cell phone. Switching from only using passwords to only using fingerprints is simply trading one set of insecurities for another.


I have high hopes that Microsoft’s InfoCard will be a more viable solution to the login explosion. The InfoCard related MIX06 sessions I’ve attended so far look promising: it’s simple, it does not require any Microsoft servers or software, and it has been developed in conjunction with the rest of the online community. Kim Cameron’s Laws of Identity whitepaper has the most comprehensible high-level overview of the problems InfoCard is trying to solve. It’s a great read.


Until InfoCard arrives, I guess I’ll be clicking the “Having trouble logging in” link. Again.

[password management](https://blog.codinghorror.com/tag/password-management/)
[security](https://blog.codinghorror.com/tag/security/)
[authentication](https://blog.codinghorror.com/tag/authentication/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
