---
title: "XML: The Angle Bracket Tax"
date: 2008-05-11
url: https://blog.codinghorror.com/xml-the-angle-bracket-tax/
slug: xml-the-angle-bracket-tax
word_count: 829
---

Everywhere I look, programmers and programming tools seem to have standardized on [XML](http://en.wikipedia.org/wiki/XML). Configuration files, build scripts, local data storage, code comments, project files, you name it – **if it’s stored in a text file and needs to be retrieved and parsed, it’s probably XML.** I realize that we have to use *something* to represent reasonably human readable data stored in a text file, but XML sometimes feels an awful lot like using an enormous sledgehammer to drive common household nails.


I’m deeply ambivalent about XML. I’m reminded of this Winston Churchill quote:


> It has been said that democracy is the worst form of government except all the others that have been tried.


XML is like democracy. Sometimes it even works. On the other hand, it also means we end up with stuff like this:

kg-card-begin: html

```

<SOAP-ENV:Envelope xmlns:SOAP-ENV=“http://schemas.xmlsoap.org/soap/envelope/”
SOAP-ENV:encodingStyle=“http://schemas.xmlsoap.org/soap/encoding/”>
<SOAP-ENV:Body>
<m:GetLastTradePrice xmlns:m=“Some-URI”>
<symbol>DIS</symbol>
</m:GetLastTradePrice>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>

```

kg-card-end: html

**How much actual *information* is communicated here?** Precious little, and it’s buried in an astounding amount of noise. I don’t mean to pick on [SOAP](http://en.wikipedia.org/wiki/SOAP). This blanket criticism applies to XML, in whatever form it appears. I spend a disproportionate amount of my time wading through an endless sea of angle brackets and verbose tags desperately searching for the vaguest hint of actual information. It feels *wrong*.


You could argue, like [Derek Denny-Brown](http://en.wikipedia.org/wiki/Derek_Denny-Brown_(software_engineer)), that XML has been [misappropriated and misapplied](http://nothing-more.blogspot.com/2004/10/where-xml-goes-astray.html).


> I find it so interesting that XML has become so popular for such things as SOAP. XML was not designed with the SOAP scenarios in mind. Other examples of popular scenarios which deviate XML’s original goals are configuration files, quick-n-dirty databases, and [RSS]. I'll call these ‘data’ scenarios, as opposed to the ‘document’ scenarios for which XML was originally intended. In fact, I think it is safe to say that there is more usage of XML for ‘data’ scenarios than for ‘document’ scenarios, today.


Given its prevalence, you might decide that XML is technologically terrible, but you [have to use it anyway](https://web.archive.org/web/20080620083933/http://xmlsucks.org/but_you_have_to_use_it_anyway/does-xml-suck.html). It sure feels like, for any given representation of data in XML, there was a better, simpler choice out there somewhere. But it wasn’t pursued, because, well, XML can represent *anything*. Right?


Consider the following XML fragment:

kg-card-begin: html

```

<memo date=“2008-02-14”>
<from>
<name>The Whole World</name><email>[email protected]</email>
</from>
<to>
<name>Dawg</name><email>[email protected]</email>
</to>
<message>
Dear sir, you won the internet. http://is.gd/fh0
</message>
</memo>

```

kg-card-end: html

Because XML purports to represent *everything*, it ends up representing nothing particularly well.


Wouldn’t this information be easier to read and understand – and only nominally harder to parse – when expressed in its native format?

kg-card-begin: html

```

Date: Thu, 14 Feb 2008 16:55:03 +0800 (PST)
From: The Whole World <[email protected]>
To: Dawg <[email protected]>
Dear sir, you won the internet. http://is.gd/fh0

```

kg-card-end: html

You might argue that XML was never intended to be [human readable](https://web.archive.org/web/20080517040927/http://www.ibm.com/developerworks/xml/library/x-sbxml.html), that XML should be automagically generated via friendly tools behind the scenes, never exposed to a single living human eye. It’s a spectacularly grand vision. I hope one day our great-grandchildren can live in a world like that. Until that glorious day arrives, I’d sure enjoy reading text files that don’t make me suffer through the **XML angle bracket tax**.


So what, then, are the alternatives to XML? One popular choice is [YAML](http://en.wikipedia.org/wiki/YAML). I could explain it, but it’s easier to show you. Which, I think, is entirely the point.

kg-card-begin: html


| <club>
<players>
<player id=“kramnik”
name=“Vladimir Kramnik”
rating=“2700”
status=“GM” />
<player id=“fritz”
name=“Deep Fritz”
rating=“2700”
status=“Computer” />
<player id=“mertz”
name=“David Mertz”
rating=“1400”
status=“Amateur” />
</players>
<matches>
<match>
<Date>2002-10-04</Date>
<White refid=“fritz" />
<Black refid=“kramnik" />
<Result>Draw</Result>
</match>
<match>
<Date>2002-10-06</Date>
<White refid=“kramnik” />
<Black refid=“fritz” />
<Result>White</Result>
</match>
</matches>
</club> | players:
Vladimir Kramnik: &kramnik
rating: 2700
status: GM
Deep Fritz: &fritz
rating: 2700
status: Computer
David Mertz: &mertz
rating: 1400
status: Amateur
matches:
-
Date: 2002-10-04
White: *fritz
Black: *kramnik
Result: Draw
-
Date: 2002-10-06
White: *kramnik
Black: *fritz
Result: White |


kg-card-end: html

There’s also JSON notation, which some call the new, [fat-free alternative to XML](http://www.json.org/xml.html), though this is still hotly debated.


You could do worse than XML. It’s a reasonable choice, and if you’re going to use XML, then at least [learn to use it correctly](https://blog.codinghorror.com/are-you-an-xml-bozo/). But consider:

1. Should XML be the *default* choice?
2. Is XML the simplest possible thing that can work for your intended use?
3. Do you know [what the XML alternatives are](http://web.archive.org/web/20060325012720/www.pault.com/xmlalternatives.html)?
4. Wouldn’t it be nice to have easily readable, understandable data and configuration files, without all those sharp, pointy angle brackets *jabbing you directly in your ever-lovin’ eyeballs?*


I don’t necessarily think [XML sucks](http://c2.com/cgi/wiki?XmlSucks), but the mindless, blanket application of XML as [a dessert topping and a floor wax](http://snltranscripts.jt.org/75/75ishimmer.phtml) certainly does. Like all tools, it’s a question of how you use it. Please think twice before subjecting yourself, your fellow programmers, and your users to **the XML angle bracket tax**. <CleverEndQuote>Again.</CleverEndQuote>

[xml](https://blog.codinghorror.com/tag/xml/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[data storage](https://blog.codinghorror.com/tag/data-storage/)
