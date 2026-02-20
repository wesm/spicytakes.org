---
title: "How To Use E-Junkie Without Your Customers Seeing It"
date: 2008-06-12
url: https://www.kalzumeus.com/2008/06/12/how-to-use-e-junkie-without-your-customers-seeing-it/
slug: how-to-use-e-junkie-without-your-customers-seeing-it
word_count: 632
---


Hideho folks.  I’m taking a bit of a break from progress updates on the 30 Day Sprint (not progressing as much as I wanted to but I have Saturday blocked off with a designer buddy to get some stuff together) in order to answer a common question.


I love [e-junkie](http://www.e-junkie.com), the service.  So much so that I have been called Robin’s local sales rep.  And that is probably closer to the truth than I would like it to be.  But I really, really can’t stand the name — it says absolutely nothing positive to my customers about my business.  So I go to some pains to avoid them seeing it.  Since it will help other uISVs and e-junkie, I thought I’d give a rundown.


**Issue: Customer lands on e-junkie page after checkout, to receive CD key**


Resolution:


1)  Go to your e-junkie product settings.


2)  Click the box next to “Product Requires: … Redirection”.


3)  Click Next.


4)  Fill in the Redirection URL.  Point it to a page on your own web server.


5)  On the page on your web server, you will want to display the CD key and instructions for installing it, plus regurgitating all the other stuff you put in your thank you mail.  (Make it big and bold because people **do not read this page** unless you give them a darn obvious reason to.  Getting them to read it saves you support costs, trust me.)  You can handle the content.  If e-junkie has a CD key, for example if you uploaded a list to them or they run a script to generate one for you, they’ll put the CD key in a URL variable “key”.  So if your URL was [http://www.example.com/thanks.htm](http://www.example.com/thanks.htm), your customer will end up seeing [http://www.example.com/thanks.htm?something=here&somethingelse=here&key=yourkey](http://www.example.com/thanks.htm?something=here&somethingelse=here&key=yourkey) .  Your mission is to get that key onto the displayable page.  If you can do server side programming, for example in PHP, this is pretty trivial.  If you can’t, you can grab it with a [bit of Javascript](http://www.netlobo.com/url_query_string_javascript.html).


Either way, please secure your website against ye-olde insert-arbitrary-content-by-rewriting-the-URL trick.  You’ll thank me later.


**Issue: Customer’s mail server is throwing out your mail**


1)  e-junkie generated mail originates from one of (as of the last time I checked) three e-junkie.com servers.  It carries your name as the sender.  Bad news bears, this means that many automated checks on that email will say “e-junkie.com is spoofing honestmicroisv.com, oh no, its spaaaaam!”  What you need to do is publish an SPF record telling the world that e-junkie.com is a legitimate source of email for you.


2)  You’ll probably want to read the docs for your individual web hosting company on how to do an SPF record.  [GoDaddy](http://www.godaddy.com)‘s interface is rather sweet.


Issue: You have links to [www.e-junkie.com](http://www.e-junkie.com) all over your page.


1)  You aren’t using the Fat Free Cart?  OK, fix that right now.  (And watch your conversion rise!)


2)  You might be worried about folks seeing the links by looking at their address bar really closely after clicking on the links.  Personally, I doubt my customers are nearly that savvy, but maybe yours are.  What you need to do is publish a CNAME DNS record, aliasing store.bingocardcreator.com (example) to [www.e-junkie.com](http://www.e-junkie.com) .  Then, every time the GoDaddy docs say e-junkie.com, you just subsitute your local alias.  This **will not work with https **(customers don’t know what that is, either) but it will get rid of the e-junkie.com in the URL bar in most browsers that I am aware of (some might resolve the CNAME and then update — I don’t know which off the top of my head), and it will get rid of the URL on hover in every browser.


And that is your tip for the day.  Check back this weekend, I’ll be back to coding and writing up a storm.
