---
title: "Digital Certificates: Do They Work?"
date: 2007-12-20
url: https://blog.codinghorror.com/digital-certificates-do-they-work/
slug: digital-certificates-do-they-work
word_count: 894
---

The most obvious badge of internet security is the “lock” icon. The lock indicates that the website is backed by a [digital certificate](http://en.wikipedia.org/wiki/Digital_certificate):

1. This website is the real deal, *not* a fake set up by criminals to fool you.
2. All data between your browser and that website is sent encrypted. Nobody in the middle can read any sensitive information you submit to that website, such as your credit card number.


Here’s what PayPal looks like in Internet Explorer 7. The lock icon and green background of the address bar let us know that this website is backed by a digital certificate. Clicking on the lock provides additional detail about the certificate.


![](https://blog.codinghorror.com/content/images/2025/03/image-192.png)


Here’s PayPal in Firefox 2, which follows the same conventions. The address bar color changes, and the lock icon is present. Clicking on the lock produces a dialog with similar summary information.


![](https://blog.codinghorror.com/content/images/2025/03/image-191.png)


The summary is reasonable enough. The certificate authority institution, VeriSign, vouches that this site is indeed PayPal. One question I’ve always had, though, is this: **who decided VeriSign is a trusted authority?** There’s some kind of whitelist built into IE and Firefox that blesses these certificate authorities with [“root” status](http://en.wikipedia.org/wiki/Root_certificate). According to Wikipedia, a 2007 survey identified [6 major certificate authorities](http://en.wikipedia.org/wiki/Certificate_authority):

1. VeriSign (57.6%)
2. Comodo (8.3%)
3. GoDaddy (6.4%)
4. DigiCert (2.8%)
5. Network Solutions (1.3%)
6. Entrust (1.1%)


The certificate authority business has always struck me as an odd relationship, because it’s completely commercial and superficial. Fork over your $300-$2,500, some nominal proof of your identity, and you’re granted a certificate for a year. Does that imply trust? I’m not the only person to share these concerns; Bruce Schneier has an excellent whitepaper which examines the risks of [certification authorities and public-key infrastructure](https://web.archive.org/web/20080118133528/http://www.schneier.com/paper-pki-ft.txt):


> Certificates provide an attractive business model. They cost almost nothing to make, and if you can convince someone to buy a certificate each year for $5, that times the population of the Internet is a big yearly income. If you can convince someone to purchase a private CA and pay you a fee for every certificate he issues, you’re also in good shape. It’s no wonder so many companies are trying to cash in on this potential market. With that much money at stake, it is also no wonder that almost all the literature and lobbying on the subject is produced by PKI vendors. And this literature leaves some pretty basic questions unanswered: What good are certificates anyway? Are they secure? For what? In this essay, we hope to explore some of those questions.


The other problem with certificates is that, as an end user, it’s nearly impossible to tell a good, valid certificate provided by a reputable certificate authority from a bad one. If we click through to examine the PayPal certificate details, we’re presented with these three dense tabs:


![](https://blog.codinghorror.com/content/images/2025/03/image-189.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-188.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-187.png)


I don’t know about you, but none of that makes any sense to me. And I’m a programmer. Imagine the poor end user trying to make heads or tails of this. What does it all mean? Of course, most users simply won’t pay attention – it’s questionable [whether they’ll even notice](https://blog.codinghorror.com/phishing-the-forever-hack/) the presence of the lock icon and the color difference in the address bar.


Certificates aren’t just for websites; they can also be applied to executables, too. Here’s what happens when I double-click on the Safari 3.0.4 beta installer. It’s been signed by Apple using their digital certificate.


![](https://blog.codinghorror.com/content/images/2025/03/image-186.png)


Clicking on the word “Apple” opens detailed information about the certificate. Again, what does all this mean? How can we tell if it is valid?


![](https://blog.codinghorror.com/content/images/2025/03/image-185.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-184.png)


I understand the value of digital certificates in theory – to definitively establish the identity of a program or website before entrusting your data to it. Consider a real-world analog. What if I walked up to you on the street and told you I was a policeman? You might check to see if I’m wearing an appropriate uniform. You might ask to see my badge. You might wonder where my partner or squad car is. We use all these things to judge the authenticity of human interactions.


However, I don’t understand how the current digital certificate infrastructure prevents criminals from obtaining their own certificates with ease. Even though I could potentially fake a policeman’s badge and uniform in the real world, that pales compared with how trivially easy it is to obtain a digital certificate for code signing from TuCows:

- Create an account at Tucows
- Buy a Cert ($300)
- Email them your Drivers License
- Download the Cert
- Export your certificate from the machine and store in a safe place
- Grab signtool.exe from the .NET 2.0 SDK
- Sign your binary using the certificate from step 4


If the only validation is an emailed copy of a drivers’ license, that doesn’t exactly give me the warm fuzzies. And even if we enhance that with (more expensive, naturally) “extended validation,” I fail to see how this would prevent a determined, resourceful criminal from getting whatever certificate they need.


I suppose digital certificates are better than nothing. But I also worry that they’re incredibly confusing for the end user, easy to game, and ultimately provide a false sense of security – and that’s the most dangerous risk of all.

[security](https://blog.codinghorror.com/tag/security/)
[digital certificates](https://blog.codinghorror.com/tag/digital-certificates/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[internet security](https://blog.codinghorror.com/tag/internet-security/)
[certificate authorities](https://blog.codinghorror.com/tag/certificate-authorities/)
