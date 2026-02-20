---
title: "Google's Lawyers Admit To gmail Privacy Leak"
date: 2006-07-27
url: https://www.kalzumeus.com/2006/07/28/googles-lawyers-admit-to-gmail-privacy-leak/
slug: googles-lawyers-admit-to-gmail-privacy-leak
word_count: 1003
---


The background: Google was sued recently regarding their efforts to prevent click-fraud in AdWords. It was a class-action suit, which basically means that there are a large number of people who were “harmed” by the tortious action at issue and that some lawyer has taken it upon themselves to sue on behalf of all of the ones who don’t opt out. Class action suits are a huge scam but that is another matter altogether.


Google attempted to settle the suit. In the process, the would have to contact class members (the people who have theoretically lost money due to fradulent clicks), and they hired a firm which specializes in this sort of work. So far so good. And that firm zealously tried to contact class members in a variety of ways, including through snail mail and email. So far so good.


Now, we all know the problems with getting mail to large numbers of people. Mail addresses changed, people go on vacation, challenge-response systems are engaged, what have you. The firm zealously tried to correct for all of these, by investigating new email addresses, tracking people down after vacation, clicking through the “I am a human” tests, etc. So far so good.


Now, what is the other main way for a mail delivery to fail? Spam filters. Now, remember, as a class member you haven’t opted-in to the lawsuit or the settlement. You might not even think you’ve been harmed by the action at issue, or you have no desire to waste your time for what is typically a sliver of a credit (the attourneys, of course, get 25%-33% of millions — in this case attourney fees will probably go above $20 million). So you might understandably not want to really talk to someone wanting to talk to you about the lawsuit. In this case, service from an agent of Google’s to tell you about your rights regarding the lawsuit is spam. You didn’t ask for it, you don’t want it, and it has a commercial purpose (they’re being paid to get the email to you, and the email is sent to divide up a pot of money — although unlike most spam its not your money).


So, as can be expected, lots of these advertisers have Gmail accounts. And what did Google do? **It checked them**. Google algorithmically peaked at all the accounts on the list their agent had developed which they had access to, to see if the mail was marked spam or not. There were **75,000 accounts** in which it was marked spam, and **an unknown (larger) amount of accounts must have been compromised** to get that statistic.


Unhinged rantings of a conspiracy nut? Well, no. **Google’s lawyers bragged about this** in a recent document they filed to the court regarding the settlement (which is tied up in legal wrangling). In relevant part (page 13 of the [pdf of the document](http://googleblog.blogspot.com/pdf/objections_response.pdf) which Matt Cutts provided on his blog [while responding to concerns about click fraud](http://www.mattcutts.com/blog/independent-report-on-invalid-clicks-released/)):


> Gilardi [ed: the firm Google was using to contact people] also re-sent 74,591 email notices to intended recipients whose addresses ended in “gmail.com” and “googlemail.com”, and *for* *whom Google had information* that the first email notice had been directed to the recipient’s spam folder. (italics mine)


Google is apparently hunky-dory with this. Its essential for the Google lawyers to demonstate that their notices stand up to certain legal requirements regarding legitimately trying to notify class members (note that its completely non-essential to go peeking). Google brags on page twelve:


> [T]here is no question that Google complied with the notice procedures ordered by this court. *In fact, Google did more than was required to provide the best notice practicable*. (italics mine)


I’m sorry Google, I just don’t remember telling you you could go peeking at the mail, even to “provide the best notice practicable”. As a matter of fact, given that I know you’ll be storing it for life I actually bothered to read that [privacy policy](http://www.google.com/privacypolicy.html) of yours. Lets see, where was it… aha.


> **Information sharing**
>   Google only shares personal information with other companies or individuals outside of Google in the following limited circumstances:
> </p> 
>   We have your consent. We require opt-in consent for the sharing of any sensitive personal information.
>   We provide such information to our subsidiaries, affiliated companies or other trusted businesses or persons for the purpose of processing personal information on our behalf. We require that these parties agree to process such information based on our instructions and in compliance with this Policy and any other appropriate confidentiality and security measures.
>   We have a good faith belief that access, use, preservation or disclosure of such information is reasonably necessary to (a) satisfy any applicable law, regulation, legal process or enforceable governmental request, (b) enforce applicable [Terms of Service](http://www.google.com/terms_of_service.html), including investigation of potential violations thereof, (c) detect, prevent, or otherwise address fraud, security or technical issues, or (d) protect against imminent harm to the rights, property or safety of Google, its users or the public as required or permitted by law.
>   </font></ul> </blockquote> 
>     Hmm, thats what I remember: opt-in consent for all disclosures of private data. I think the** contents of my inbox **is pretty darn private. So that ones out. You’ve already explained in your own words that the peeping was more than the court required, so excuse #3 is out. So what about #2: were you “processing information on [Google’s] behalf”? If you were, then **this exemption swallows the entirety of the policy policy**!
>     I’m less than happy, and now seriously wondering if all those business documents I’ve got floating around my Gmail inbox are going to end up in the hands of your lawyers without so much as a by-your-leave if your lawyers, in their sole discretion, think its for my own good strategically a good idea to get Google out of a lawsuit.
>     Do no evil, indeed.
>     [Edit: Fixed spelling mistakes and bolded some juicy bits.]
