---
title: "Another Plug for e-junkie"
date: 2006-09-10
url: https://www.kalzumeus.com/2006/09/11/another-plug-for-e-junkie/
slug: another-plug-for-e-junkie
word_count: 446
---


Yesterday I mentioned that my customers suddenly had a lot of trouble getting mails from [e-junkie](http://www.e-junkie.com). Besides posting it on my blog, I also dropped e-junkie a note to advise them of the problem — it seemed like the right thing to do since if their outgoing mail server ended up on a RBL that would have been, well, a pretty bad thing for their business. They had a response within 2 hours that said they had gotten my note, checked everything, and it looked to be in order. But they kept following up regarding the specifics of which ISPs were misbehaving and whatnot, which is already above and beyond the call of duty.


I then asked whether I could possibly request a feature. Yesterday, I faced down the unpleasant prospect of having to *gulp* code Perl to fix this problem, by embedding my registration code in the post-sale confirmation page. e-junkie currently passes that page ~4 parameters when they send a customer to it, but none of them is the registration code, and I would have to generate the registration code on my server to make sure the code on that page and in the email were the same. Then I would use the parameters they passed to look up the registration code I had generated. Aside from this involving evil Perl code (is there any other kind?), there were some potentially nasty timing issues involved (pop quiz: what happens if the customer arrives before I have the request from e-junkie to generate the registration code? What happens if the customer arrives after the request to generate the registration code but before that request has caused the flat-file database I was contemplating to be updated?)


So I asked e-junkie if it were not too much trouble could they possibly pass the registration code along with the other parameters. If they did that, fixing this problem would be a matter of writing ten lines of Javascript. (The URL query string is stored in window.location.search. Code for parsing out a particular value from it is trivial or you can copy/paste from the Internet. Then just output this to something visible.)


Anyhow, I figured that they would probably “We’ll take this feature request under advisement”. I definately wasn’t expecting the next email to say “We were going to mail you back when this was implemented, but it turns out our engineering team will require 24 hours to get to it. Sorry for the delay.”


*Sorry for the delay!*


So there you have it: e-junkie, the best $5 per month I ever spent. (Obligatory disclaimer: opinions in this post are my own and I receive no compensation for them.)
