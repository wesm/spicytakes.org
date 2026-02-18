---
title: "Gmail is a huge source of spam"
date: 2021-02-25
url: https://drewdevault.com/2021/02/25/Gmail-is-a-huge-source-of-spam.html
slug: Gmail-is-a-huge-source-of-spam
word_count: 411
---

5× as many spam registrations on sourcehut are from gmail than from the
second-largest offender.

```
# SELECT
  SPLIT_PART(email, '@', 2) as domain, count(*) as count
  FROM "user"
  WHERE user_type = 'suspended'
  GROUP BY domain
  ORDER BY count DESC;
          domain           | count
---------------------------+-------
 gmail.com                 |   119
 qq.com                    |    26
 mail.ru                   |    17
 mailinator.com            |    10
 yopmail.com               |     6
 aol.com                   |     6
 yahoo.com                 |     6
[...more omitted...]
```

This is just the ones which got through: most spam registrations are detected
and ignored before they make it to the database.

A huge number of spam emails I recieve in my personal inbox originate from
@gmail.com, and often they arrive in my inbox unscathed (as opposed to going to
Junk) because Gmail is considered a reputable mail provider. My colleague
estimates that between 15% and 25% of the spam emails sent to a mailing list he
administrates comes from Gmail.

One might argue that, because Gmail is the world’s largest email provider, it’s
natural to expect that they would have the largest volume of spam simply because
they have proportionally more users who might use it for spam. I would argue
that this instead tells us that they have the largest responsibility to curtail
spam on their platform.

I’ve forwarded many, many reports to  [abuse@gmail.com](mailto:abuse@gmail.com) , but they’ve never followed
up and the problem has not become any better. I have had half a mind to block
Gmail registrations on sourcehut outright, but about 41% of all registrations
use Gmail.

It bears repeating that anyone with any level of technical expertise ought to
know better than to use Gmail. I usually recommend
 [Migadu](https://www.migadu.com) 1 , but there are many options to choose from.
If you’re worried about mail deliverability issues, don’t be — it’s more
or less a myth in $CURRENTYEAR. If you set up
 DKIM 
properly and unlist your IP address from the
 DNSBL s (a simple process), then your mails
will get through.

In case you’re wondering, the dis-award for second-worst goes to Amazon SES.
They don’t register on sourcehut (it’s outgoing only, so that makes sense), but
I see them often in my personal inbox. However, SES only appears at a rate of
about a tenth of the gmail spam, and they appear to actually listen to my abuse
reports, so I can more or less forgive them for it.

1. Full disclosure: sourcehut has a business relationship with Migadu, though I’ve recommended them since long before we met. ↩︎
