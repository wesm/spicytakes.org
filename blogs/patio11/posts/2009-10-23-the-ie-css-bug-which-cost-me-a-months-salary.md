---
title: "The IE CSS Bug That Cost Me A Month’s Salary"
date: 2009-10-23
url: https://www.kalzumeus.com/2009/10/23/the-ie-css-bug-which-cost-me-a-months-salary/
slug: the-ie-css-bug-which-cost-me-a-months-salary
word_count: 2371
---


//


I run a small business [selling software](http://www.bingocardcreator.com) (downloadable and online) which lets parents and teachers make bingo cards.  It is October, which is the busiest season on the educational bingo calendar, largely because Halloween is coming up.  Kids in school + candy-fueled frenzy + secular(ish) holiday + desire for fun activity = bingo bonanza!


However, due to an IE CSS bug, my Halloween experience is best described as “bobbing for poisoned apples”.


## The Design Improvement That Wasn’t


On September 21st my designer and I got together and we [created a new candidate design](https://www.kalzumeus.com/2009/09/21/ab-testing-signup-page/) for my sign up and login pages, which are both critical to conversions for my business.   The intent was to A/B test the new pages against the old design.  One critically important niggle that didn’t bother me at the time: while ideally an A/B test would test exactly the old HTML against exactly the new HTML, for obscure implementation reasons we ended up testing the old HTML plus one little change versus the new HTML.


That one little change was replacing the old sign up button (the stock HTML form submit one) with a graphical button.  I thought this was such an obviously beneficial change that it was not worth taking on extra coding complexity to keep it the old way.  Stupid, **stupid**, ***stupid***.


Thanks to the magic of subversion I was able to recover [exactly the HTML](http://www.bingocardcreator.com/files/old-site/registration.html) that was displayed on my site after the upgrade.  (This is one of the two A/B alternatives but it is exactly identical to the other one in the area that is relevant.)  Feel free to open that in your browser and see if you can spot the problem.


At this point I have to mention that I generally use IE8 or Chrome, and my designer uses Firefox.  This means I had never seen the new version of my site in IE6 or IE7 until trying to do tech support from an Internet cafe last night.  (Being a proper Japanese salaryman, I had missed the last train and stopped at the cafe to answer customer emails prior to staying at a hotel.)


Whereupon I discovered a slight problem.  In IE7, the site looked more like:


Hmm, the signup form has **no visible sign up button**.  The log in form also had **no visible log in button**.


I started panicking but was in no position to fix the bug at 2 AM in the morning from an Internet cafe, although I made a game attempt to do so.  (Word to the wise: trying to fix a Rails application by editing files in vi through a web console to your [Slicehost](http://www.slicehost.com) VPS is not recommended.)


## How Well Do Forms Without Buttons Convert?


Answer: not well at all.


You can still submit a form by hitting the Enter button even if you can’t see the submit button.  This is, however, not standard user behavior in my niche.  Let’s see what that did to conversion rates.  Using custom segments (a power-user feature from Google Analytics that I’ve literally never had any useful purpose for before), I’ve graphed the conversion rates among IE8 users (orange line), IE6/7 users (green line), and the site average (blue line).


As you can see, IE6/7 and IE8 are pretty much neck and neck in the month before the bug is introduced.  This makes sense, as we would not intuitively assume those two user populations would be very different from each other.  You can also see that they both track the site average reasonably well, which is practically true by definition as IE users make up the majority of visitors on my site (about 65%, give or take).


Then, after the bug gets introduced, the conversion rates for IE6/7 take a nosedive relative to IE8.  The site average in blue also declines, *solely because* it is being pulled lower by the underperformance of the old IEs.


In concrete terms, the conversion rate of IE6/IE7 users was **3.40%** after the bug.  (Note that this is *not* the conversion rate among people actually viewing the login/registration screens.  Google Analytics doesn’t let me conveniently break the numbers down for that.)  The conversion of IE8 users, by comparison, was **9.53%**.  In other words, if you trust my intuition that IE6/7 users are about as likely to convert as IE8 users all else being equal (which you should, just by eyeballing that graph), then **I lost about** **64% of my conversions** since September 21st.


## Putting The Damage In Economic Terms


I’m a glutton for punishment so I’m going to do the painful math.  Between September 21st and October 23rd, when I fixed the bug, I had roughly $4,500 worth of sales, of which IE6/7 users comprised about $2,080.  Since the IE6/7 bug is essentially meaningless after you get through registration (since the overwhelming majority of users pick Remember Me and never see either the sign in or sign up forms again), I’m going to make the simplifying assumption that the bug ripples straight to my bottom line.


We can then use simple math to figure out how much the 64% of sales I threw away was probably worth.  Ouch, I am wincing as I type this: **$3,750 in lost sales**.  That unfortunately flows almost straight to the bottom line, since all of my major costs (advertising, hosting, etc) happen whether I make the sale or not — I probably **lost in excess of $3,400 in profits**.  That is more than my monthly salary.


## How The Heck Do You Overlook That?


I wish I could blame Microsoft for my stupidity on this one, but aside from not testing the page in IE6/IE7 (which would have shown the bug immediately), I had ample opportunities to discover that there was a problem somewhere.  However, other things in the chaotic, fractally complex system that is a small business concealed them from me.


**Indication #1**: There are two types of signups on my site, trial signups (where I capture an email address) and anonymous guest signups (where I don’t).  Historically, I push the trial signups much harder, and my users signed up for them at a multiple of the guest signups.  (Guest accounts scarcely convert for me at all, which is why I don’t push them much.  However, an A/B test proved that removing the option didn’t increase the number of trials or paying customers, so I left the option in.)


Thus, when the mix of trial and guest users suddenly went from 880 : 350 to 792: 506, I should have said “Wait a minute, the guest accounts are getting much more popular.  Why is that?”  The answer to that is: Unsophisticated users, like the ones who make up most of my audience, will fill in their information and then see ‘Sign in as guest’ and ‘Cancel’.  Given only these two choices, clearly they want to ‘Sign in as guest’ rather than figure, “hmm, typically guest accounts don’t have usernames or passwords associated with them, I should email Patrick and ask what happened to the real sign up button.”


And indeed, I did see the explosion of guests on [my stats](http://www.bingocardcreator.com/stats/signups-per-day), but I had changed the graphing option from showing daily counts to showing weekly counts, and the disparity wasn’t big enough to catch my sustained attention.  (The inflection point on September 21st is **immediately** visible on the daily graph.)  After considering the matter for a few minutes I said “Eh, Halloween is coming up, which always broadens my market.  Maybe it is bringing in some less interested folks.  Oh well, nothing to worry about.”


**Indication #2**:


I check my conversion rates on AdWords roughly once a week, largely because if they start to suffer Google stops running my ads and I lose a lot of money.  I then noticed that the numbers were below where I expected them to be (“Hmm, that’s funny, a few weeks ago I was getting 24 – 27%, now it is saying 18%… what is up?”) but I never ran the following graph to see the full range.


Yeah, just from eyeballing that, you can see the problem right?  Visualizations are wonderful for seeing problems that you already know to look for.  However, they are poor for informing you of problems that aren’t visible in the default visualization, since you won’t spend the time to slice the data to see the problem if you don’t know it exists.


Honestly, I don’t know why I didn’t immediately punch the panic button when I saw my AdWords conversion rates start declining.  Again, October always throws my numbers into a total mess, and I was very busy in my day job and in my various [seasonal initiatives](https://www.kalzumeus.com/2009/10/14/holiday-promotion/) for taking advantage of Halloween.  So busy, in fact, that I offset most of the decline in sales, and so wasn’t given any advance warning by, e.g., having sales plunge to a fraction of normal.


**Indication #3**: What finally clued me into looking for this problem was a pattern in customer support requests, of all things.  As I mentioned earlier, guest accounts are historically rarer than trial accounts and they convert very, very poorly.  As a matter of fact, I think I probably had one sale to a guest account in history prior to the bug being introduced.


The code that I have which upgrades accounts in response to people paying me via Paypal and Google Checkout doesn’t handle guest accounts very well, because they’re anonymous.  It upgrades the account fine, but doesn’t register the email address they used for their payment with the guest account, which means the account still can’t log in after logging out.  (Since the guest account is still anonymous.)  However, since the system knows that the Registration Key issued to the purchaser is in use (on their guest account), if for some reason they log out or switch computers, they’ll be both unable to register a new account (because their Registration Key is in use) and unable to log into their guest account (because it is anonymous).  That is a pretty nasty Catch 22.


I’ve known about that Catch 22 for a while, but fixing it was not high on my list of priorities.  All of the following has to happen for it to actually bite a customer:

- They start using a guest account.
- They don’t give an email address when prompted by the fairly frequent upsells within the guest account.
- They nonetheless purchase the software within their guest session.
- They choose to use the online version of the software rather than the downloadable version (a not-insignificant portion of customers think the online version is the trial and the downloadable version is the “real deal” — well, if they pay me money, they can think *whatever they please*).
- They clear their cookies.
- They try to log in again.


Prior to the bug being introduced, I thought “This sequence of events is about as likely as flipping a coin and having it land on edge.”  And, indeed, it only ever happened to one person.  I fixed her record manually, looked at the code which caused the problem, and figured that an immediate fix was impossible.


Then I got emails from three people in the same day who were hit by the guest-purchase bug.  That was finally the eight sigma event that convinced me that my process was really, really out of control.  Whereupon I started investigating, beginning (fortuitously) with trying to log into my admin page on the site while on the Internet cafe’s IE7, and noticing that there was no login button.


## Technical Mumbo Jumbo


If you’re a CSS geek, you might be interested in knowing why the buttons vanished.  Fair enough: the HTML input element had a background image specified and a text-indent:-9000px property applied to it, which puts the standard text for the button way off the screen, leaving only the background image visible.  However, IE6/IE7 treat text-indent as moving the background image as well, so the entire control essentially vanished, leaving empty, unclickable space where it used to be.


The fix was fairly simple.  I am truly indebted to Laurence at My Drupal Blog for [posting about it](http://mydrupalblog.lhmdesign.com/theming-search-submit-button-css-cross-browser-compatible-solution).  He probably saved me an ulcer.  Essentially, I identify which browsers are using IE and then apply some sort of hacky stylings to make the background image display visibly, but cause the Sign Up text to be invisible by blending it with the background.  It is **very** hacky — sort of like patching a wound to your artery with duct tape — but you can’t be too choosy when you’re leaking over $100 a day and have the CSS skills of a vole rat.


## On The Bright Side


I don’t want to give you the wrong impression: despite this very, very serious issue, my business has been doing [very well](http://www.bingocardcreator.com/stats/sales-by-month) in October.  The usual seasonal fluctuation, my seasonal promotions, and all the various improvements I’ve been making in the last few months will still make it my best month ever, and historically the last week of October sees a strong spurt in sales, so it might even be the best month ever by quite a margin.


I also got a much-needed kick in the pants to remind me to test all changes, even the stupid little one-line changes, in all the browsers my customers routinely use.  One positive lesson learned is that IE8’s compatibility mode reproduced this bug exactly, so that will be an easy way to do this going forward.  Ideally I’d have some sort of automated test suite set up to catch this sort of thing (using Selenium or what have you), but that isn’t in the cards at present.  At the very least, I’m going to upgrade my automated stats tracking put **big red warnings** on my dashboard when the business starts to fail sanity checks.  An obnoxious red warning about conversion rates would have caught this a month ago, within less than 24 hours of the bug going into production.


I hope you learned something from my experience, and am quite willing to take additional lumps in the comments if you have any suggestions for good ways of preventing a similar bug in the future. Happy Halloween!
