---
title: "Don't Make My Really Elementary SEO Mistake"
date: 2007-10-07
url: https://www.kalzumeus.com/2007/10/07/dont-make-my-really-elementary-seo-mistake/
slug: dont-make-my-really-elementary-seo-mistake
word_count: 458
---


So, fourteen months into marketing Bingo Card Creator and quite a bit into becoming an amateur SEO, I finally added a 301 redirect from bingocardcreator.com to [www.bingocardcreator.com](http://www.bingocardcreator.com/)


Folks who are more experienced in ways of SEO will be doing a faceplant when they hear that, since it is often suggested as one of the very first things you should do.  The reasoning is simple: search engines currently treat things on different subdomains as being mostly unconnected websites, so in the eyes of the all powerful Googlebot a link from a download site to bingocardcreator.com and a link from a teacher to [www.bingocardcreator.com](http://www.bingocardcreator.com/) are votes for two different websites rather than votes for the single unified entity.  A 301 redirect, on the other hand, tells browsers and search engine bots that what they are looking for is a) not available where they asked for it and b) is available somewhere else, on a permanent basis.  When Google et al see a URL that is 301ed to another URL, they just treat the first as an alias of the second.


My failure to have this redirect in place is really bad.  I remember thinking of fixing it a few months ago, but it was a stray thought when I was on the train.  The next stray thought was “Well, I’m really the only person who ever links to the page, and I always choose www, so it won’t really make a difference”.


Today, I used [WebsiteGrader](http://www.websitegrader.com), an impressive piece of linkbait done by the [HubSpot](http://www.hubspot.com) folks.  I think I have mentioned them before.  Anyhow, I was doing it in preparation for releasing my own little bit of linkbait in the next 48 hours or so.  Buried in the results was a **gigantic red warning** saying that I had forgotten to do this.  I’ve been ignoring the mental equivalent of gigantic red warnings for a year.  However, I’m a very data oriented person, and WebsiteGrader reported I had 550 inbound links to [www.bingocardcreator.com](http://www.bingocardcreator.com/) (I know the number to be higher, but its an inexact science) and… 553 to bingocardcreator.com.


**Faceplant**.  All that work creating linkable content and I was throwing half of it away.


I’m especially embarassed because this is  something that can be fixed in literally fifteen seconds, especially if you’re using Apache.  (Which, if you’re using Joe Random’s Super Cheap Webhosting Service, or GoDaddy for that matter, you almost certainly are.)  Copy the following into the .htaccess file in your web root directory (there are other options, this is just the quickest to explain).  You don’t need the first line if it is already there, and I’d suggest these be at the top of your file:


> RewriteEngine On
> RewriteCond %{HTTP_HOST} ^putyourdomainnamehere.com [NC]


> RewriteRule ^(.*)$ http://www.putyourdomainnamehere.com/$1 [L,R=301]
