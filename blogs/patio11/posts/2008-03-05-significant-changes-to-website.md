---
title: "Significant Changes To Website"
date: 2008-03-05
url: https://www.kalzumeus.com/2008/03/05/significant-changes-to-website/
slug: significant-changes-to-website
word_count: 478
---


I’m now testing some of the upgrades to my website made possible by the new design: my [purchasing page](http://www.bingocardcreator.com/purchasing.htm) now has eye-level testimonials (the first of many — got to go through a year of email and put them on rotation) and some sidebarized credibility enhancing goodness.  The rails code for this is pretty simple:


<%= render :partial => ‘paging_bob_walsh’ %>


(He finally nagged me enough to put up testimonials.  OK, so perhaps he didn’t mention it to me directly, but the little Marketing Bob angel on my shoulder kept saying “Patrick, Patrick, where are your credibility markers?” until I gave in.


The second change I’m particularly proud of — it is designed with both SEO and users in mind.  Take a look at the sidebar on any of the “static” pages of the site (you know, the ones which are normally stuffed full of content but which don’t typically directly help conversions).


As you can see, I now stealthily plug the holiday bingo cards for a period in advance of (and slightly past) the actual holiday, giving Google plenty of time to spider me and apply the front page link juice straight to that card.  I then pad out the rest of the slots with cards and categories chosen randomly.  That is iteration 1.0 of my linking architecture — I’m going to transition it to a neat little concept I call Rawlsian linking in a week or so, after I have it coded.  Suffice it to say its what linking would look like if the goal were to redistribute the wealth between pages.  The randomness is a fairly decent first approximation for now, and hopefully my users will also enjoy it, causing them to spend more time on my pages and become more likely to download the free trial.


Finally, I noticed in my logs that Google was hitting a lot of URLs with capital letters in them.  This was suprising, since my app is only supposed to generate URLs with lower-case letters.


Example:


[http://www.bingocardcreator.com/bingo-cards/Economics](http://www.bingocardcreator.com/bingo-cards/Economics)


[http://www.bingocardcreator.com/bingo-cards/economics](http://www.bingocardcreator.com/bingo-cards/economics)


(Same content, different URLs — uh oh!  Note if you were to click on those now you’d see it has been fixed.)


This was also catastrophically bad news, because if two URLs share the same content, they split their link juice and invite the duplicate content penalty to chase both URLs out of the index.


I fixed it by identifying the two actions which had the issues and then, if the URL had a capital letter in it, lowercasing the URL and issuing a 301 redirect to the proper, canonical version.  There is probably a less hackish way to do this:


> def show


> #prevent Google from indexing uppercased and lowercased versions of same content


> if (request.request_uri != request.request_uri.downcase)


> headers[“Status”] = “301 Moved Permanently”


> redirect_to request.request_uri.downcase


> else #process as normal


> end


> end


> end
