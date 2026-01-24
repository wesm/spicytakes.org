---
title: "So You’d Like to Send Some Email (Through Code)"
date: 2010-04-21
url: https://blog.codinghorror.com/so-youd-like-to-send-some-email-through-code/
slug: so-youd-like-to-send-some-email-through-code
word_count: 1432
---

I have what I would charitably describe as a [hate-hate](http://www.google.com/search?q=site:codinghorror.com+email) relationship with email. I desperately try to avoid sending email, not just for myself, but also in the code I write.


Despite my misgivings, **email is the cockroach of communication mediums: *you just can’t kill it***. Email is the one method of online contact that almost everyone – at least for that subset of “everyone” which includes people who can bear to touch a computer at all – is guaranteed to have, and use. Yes, you can make a fairly compelling case that email is [for old stupid people](http://www.techdirt.com/articles/20071114/144228.shtml), but let’s table that discussion for now.


So, reluctantly, we come to the issue of **sending email through code**. It’s easy! Let’s send some email through oh, I don’t know, let’s say... Ruby, courtesy of some sample code I found while [browsing the Ruby tag](http://stackoverflow.com/questions/tagged/ruby) on Stack Overflow.

kg-card-begin: html

```

require ‘net/smtp’

def send_email(to, subject = "", body = "")
    from = “[email protected]”
    body= “From: #{from}\r\nTo: #{to}\r\nSubject: #{subject}\r\n\r\n#{body}\r\n”

    Net::SMTP.start(‘192.168.10.213’, 25, ‘192.168.0.218’) do |smtp|
        smtp.send_message body, from, to
    end
end

send_email “[email protected]”, “test”, “blah blah blah”

```

kg-card-end: html

There’s a bug in this code, though. Do you see it?


**Just because you *send* an email doesn’t mean it will arrive.** Not by a long shot. Bear in mind this is *email* we’re talking about. It was never designed to survive a bitter onslaught of criminals and spam, not to mention the explosive, exponential growth it has seen over the last twenty years. Email is a well that has been truly and thoroughly poisoned – the digital equivalent of a superfund cleanup site. The ecosystem around email is a dank miasma of half-implemented, incompletely supported anti-spam hacks and workarounds.


Which means the odds of that random email your code just sent getting to its specific destination is... spotty. At best.


If you want email your code sends to actually *arrive* in someone’s AOL mailbox, to the dulcet tones of “You’ve Got Mail!”, there are a few things you must do first. And most of them are only peripherally related to writing code.


**1. Make sure the computer sending the email has a Reverse PTR record**


What’s a [reverse PTR record](http://aplawrence.com/Blog/B961.html)? It’s something your ISP has to configure for you – a way of verifying that the email you send from a particular IP address actually belongs to the domain it is purportedly from.


> Not every IP address has a corresponding PTR record. In fact, if you took a random sampling of addresses your firewall blocked because they were up to no good, you’d probably find most have no PTR record - a dig -x gets you no information. That’s also apt to be true for mail spammers, or their PTR doesn’t match up: if you do a dig -x on their IP you get a result, but if you look up that result you might not get the same IP you started with.
> That’s why PTR records have become important. Originally, PTR records were just intended as a convenience, and perhaps as a way to be neat and complete. There still are no requirements that you have a PTR record or that it be accurate, but because of the abuse of the internet by spammers, certain conventions have grown up. For example, you may not be able to send email to some sites if you don’t have a valid PTR record, or if your pointer is “generic.”
> How do you get a PTR record? You might think that this is done by your domain registrar – after all, they point your domain to an IP address. Or you might think whoever handles your DNS would do this. But the PTR record isn’t up to them, it’s up to the ISP that “owns” the IP block it came from. They are the ones who need to create the PTR record.

kg-card-begin: html

A reverse PTR record is critical. How critical? Don’t even bother reading any further until you’ve verified that your ISP has correctly configured the reverse PTR record for the server that will be sending email. It is absolutely the most common check done by mail servers these days. Fail the reverse PTR check, and I guarantee that a *huge* percentage of the emails you send will end up in the great bit bucket in the sky – and not in the email inboxes you intended.

kg-card-end: html

**2. Configure DomainKeys Identified Mail in your DNS and code**


What’s [DomainKeys Identified Mail](http://en.wikipedia.org/wiki/DKIM)? With DKIM, you “sign” every email you send with your private key, a key only *you* could possibly know. And this can be verified by attempting to decrypt the email using the public key stored in your public DNS records. It’s really quite clever!


The first thing you need to do is generate some public-private key pairs (one for every domain you want to send email from) via OpenSSL. I used [a win32 version I found](http://www.slproweb.com/products/Win32OpenSSL.html). Issue these commands to produce the keys in the below files:


```
$ openssl genrsa -out rsa.private 1024
$ openssl rsa -in rsa.private -out rsa.public -pubout -outform PEM

```


These public and private keys are just big ol’ Base64 encoded strings, so plop them in your code as configuration string resources that you can retrieve later.


Next, add some DNS records. You’ll need two new TXT records.

kg-card-begin: html

_domainkey.example.com

“o=~; [[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)”
selector._domainkey.example.com

“k=rsa; p={public-key-base64-string-here}”

kg-card-end: html

The first TXT DNS record is the global DomainKeys policy and contact email.


The second TXT DNS record is the public base64 key you generated earlier, as one giant unbroken string. Note that the “selector” part of this record can be anything you want; it’s basically just a disambiguating string.


Almost done. One last thing – we need to sign our emails before sending them. In any rational world this would be handled by an email library of some kind. We use Mailbee.NET which makes this fairly painless:

kg-card-begin: html

```

smtp.Message = dk.Sign(smtp.Message,
null, AppSettings.Email.DomainKeyPrivate, false, “selector”);

```

kg-card-end: html

**3. Set up a SPF / SenderID record in your DNS**


To be honest, [SenderID](http://en.wikipedia.org/wiki/Sender_ID) is a bit of a “nice to have” compared to the above two. But if you’ve gone this far, you might as well go the distance. SenderID, while a little antiquated and kind of... Microsoft/Hotmail centric... doesn’t take much additional effort.


SenderID isn’t complicated. It’s another TXT DNS record at the root of, say, example.com, which contains a specially formatted string documenting all the allowed IP addresses that mail can be expected to come from. Here’s an example:

kg-card-begin: html

```

“v=spf1 a mx ip4:10.0.0.1 ip4:10.0.0.2 ~all”

```

kg-card-end: html

You can use the Sender ID SPF Record Wizard to generate one of these for each domain you send email from.


**That sucked. How do I know all this junk is working?**


I agree, it sucked. Email sucks; what did you expect? I used two methods to verify that all the above was working:

kg-card-begin: html
1. Test emails sent to a Gmail account.


Use the “show original” menu on the arriving email to see the raw message content as seen by the email server. You want to verify that the headers definitely contain the following:
Received-SPF: pass
Authentication-Results: ... spf=pass ... dkim=pass
If you see that, then the Reverse PTR and DKIM signing you set up is working. Google provides *excellent* diagnostic feedback in their email server headers, so if something isn’t working, you can usually discover enough of a hint there to figure out why.
2. Test emails sent to the Port25 email verifier


Port25 offers a really nifty public service – you can send email to [[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection) and it will reply to the from: address with an extensive diagnostic! Here’s an example summary result from a test email I just sent to it:


SPF check:          pass
DomainKeys check:   fail
DKIM check:         pass
Sender-ID check:    pass
SpamAssassin check: ham


You want to pass SPF, DKIM, and Sender-ID. Don’t worry about the DomainKeys failure, as I believe it is spurious – DKIM is the “newer” version of that same protocol.

kg-card-end: html

Yes, the above three steps are quite a bit of work just to send a lousy email. But I don’t send email lightly. By the time I’ve reached the point where I am forced to write code to send out email, **I really, *really* want those damn emails to arrive**. By any means necessary.


And for those who are the unfortunate recipients of these emails: my condolences.

[ruby](https://blog.codinghorror.com/tag/ruby/)
[email](https://blog.codinghorror.com/tag/email/)
[code](https://blog.codinghorror.com/tag/code/)
[software development](https://blog.codinghorror.com/tag/software-development/)
