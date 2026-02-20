---
title: "I Saw An Extremely Subtle Bug Today And I Just Have To Tell Someone"
date: 2011-11-17
url: https://www.kalzumeus.com/2011/11/17/i-saw-an-extremely-subtle-bug-today-and-i-just-have-to-tell-someone/
slug: i-saw-an-extremely-subtle-bug-today-and-i-just-have-to-tell-someone
word_count: 3257
---


**This post will not help you sell more software. If you’re not fascinated by the inner workings of complex systems, go do something more important. If you are, grab some popcorn, because this is the best bug I’ve seen in years.**


Have you ever been logged into a site and get suddenly asked to log in again?  This is one of those minor nuisances of using the Internet, right?  If you’re not technically inclined, you think “Hmm, ghosts in the Googles.  Oh well, here is my username and password again.”  If you are technically inclined, you might think “Hmm, funny, my cookie picked a bad time to expire, or maybe my session was getting stored in Memcached on a machine which just went down.  Oh well, here is my username and password again.”


It turns out that [Bingo Card Creator](http://www.bingocardcreator.com) has been doing this pervasively to a fraction of my users for the last few months.  I never noticed it, and no one ever complained.


Here’s the scenario: Bingo Card Creator is a Rails application, originally coded against Rails 2.1.X and then gradually updated with Rails security releases.  Like many Rails applications, it stores sessions in a cookie (using CookieStore), and uses the session to hold only very limited data.  Specifically, it holds the (critical) user ID for logged in users and the (nice to have) pre-login session ID.  I use the pre-login session ID to tie some analytics stuff together on the back end — basically, it lets me associate newly created accounts with search terms and whatnot that bring them to my site.  The exact mechanism for doing that isn’t important to this bug — you just need to understand that the session resetting is a minor nuisance if it only happens once in a blue moon, and a huge nuisance if it happens pervasively.


## Subtle Indications My Site Was Borked


BCC maintains a whole lot of internal analytics, because I’m something of stats junkie.  Because BCC is in maintenance mode this year, I don’t actually view the stats on a regular basis — as long as the server stays up and users don’t have any complaints, I let the sleeping dog lie.  (I’ve been busy with other projects.)  Anyhow, one example of such a stat is “Of recently created trial accounts, how many were referred from the Halloween bingo cards mini-site?”  For most of the year, that should be a negligible number.


Except right about on Halloween, when the mini-site sees on the order of 30,000 visits or more.  This usually sells several thousand dollars worth of software.  That is fairly hard to miss, because if several thousand dollars don’t show up in my bank account, I’d know right away.  (Sidenote: I did lose about $1,000 due to an ill-timed server crash while I was on a cross-continental plane ride right during the middle of the pre-Halloween rush. Oof.)  So naturally, several thousand dollars implies a hundred or more sales (at $30 each) which implies thousands of trials, right?


Well, my internal analytics code was telling me that the Halloween site had referred ~100 trials of which 6 converted.   Which means that I should have expected a $200 bump in my bank balance.  Which was not what happened.


I mentally filed this away under “Hmm, that’s odd” but didn’t investigate immediately because I had not lost any money (or so I thought) and was busy that week.  Then recently, after doing an unrelated code push (I integrated [Stripe](http://www.stripe.com), it is awesome, full details later), I did my usual post-deploy smoke test and, after creating a new account, I got suddenly logged out of the application.


“Hmm, that’s odd.”  And I tried it again, twice, couldn’t produce the error, and mentally wrote it off to gremlins.


## In Which I Become Doubtful Of The Existence Of Gremlins


Four hours ago, my brain suddenly decided to put these facts together. The discrepancy for the sales statistics strongly suggests that, prior to accounts getting created, the session was getting cleared.  This meant that, when the account actually got created, the referrer was not associated with the account in the DB, which threw off subsequent stats gathered by my internal analytics.  Sessions getting randomly cleared would also cause the user to become instantly signed out.


I tried to reproduce the problem in development mode and was pervasively unable to do so.  Then I started trying to reproduce it on the live site and was able to, sporadically, but only in Incognito Mode in Chrome, and only if I clicked fairly fast.  (Don’t ask how many dozens of tries it took to figure out that fast clicking was the culprit.)


Having verified that it actually existed, I added instrumentation to tell me what my session ID was, and noticed — like expected — that it changed when I was suddenly logged out.  Sure enough, the session was getting wiped.  But why?


Racking my brains to figure out “What could reset a session in Rails other than explicitly trying to do it?”, I started listing up and discarding some candidates:

- The cookie expired in the browser — nope, expiry was set correctly
- The cookie got eaten by the hop from Nginx to Mongrel — nope, after investigation, cookies always matched on both sides (like expected)
- The cookie got too big and failed to serialize properly — nope, after looking through the Rails codebase, that looked like it would throw an exception
- The cookie got reset when Rails detected malicious behavior coming from the browser — **bingo!**


## CSRF Protection: When It Breaks, It Breaks *Very Quietly*

Cross-site request forgery (
[CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))
) is tricking the browser with a malicious (or compromised) site B to access something on site A.  Since requests for site A will carry A’s cookie
*whether requested by A or not*
, an image tag or embedded Javascript on B can do anything on A that a logged-in user can do, like accessing /accounts/wire_all_your_money_to_switzerland with the appropriate POST parameters to make it happen.  This is, to put it mildly, a bad thing.  Rails has lovely magic which defends against CSRF for you: all you have to do is include two lines of code

Rails will then basically generate cryptographically secure random number, totally transparently to you. This is called the CSRF token.


One copy goes in your Rails session, where only your server and the client can see it.  (n.b. Rails sessions are a bit opaque since they are Base64 encoded, but they can be trivially decoded by anyone who can read the cookie, including the end-user.  They can’t be **forged** because of another security feature, but don’t put anything you don’t want the user to know in the session.)


Another copy goes in the document’s HEAD (for access via Javascript) and in Rails-generated forms as a hidden value.  When Rails makes a PUT or POST request to the server (via helper-generated form or helper-generated Javascript), Rails will submit the copy included in the HTML code with the request, compare it to the one in the session, and bounce requests where they don’t match. Bad actions on other sites shouldn’t be able to read either a) a page on your site (the same origin policy prevents this) b) the contents of your cookie from your site, so this is secure.


The specifics of how it “bounces requests” are very important.


## Point Releases Sometimes Contain Doozies


My personal understanding of Rails up until an hour ago was that a CSRF violation would raise an exception.  This would practically never get seen by a legitimate user operation, so few people are aware of that, but I had seen it a time or two when security auditing BCC.  (Some of my geeky friends had, back in the day, exploited BCC with a CSRF and helpfully told me how to fix it.  Naturally, after fixing it I verified that the site worked as expected with the fix.)


So if the CSRF protection was somehow eating sessions, I would expect to see that exception getting logged and emailed to me by [Airbrake](http://www.airbrakeapp.com) (formerly Hoptoad — it emails you when an exception happens in production, highly recommended).   That wasn’t happening.


Then I decided to dig into the Rails source.  Whereupon I learned that Rails 2.3.11 changed the behavior of CSRF protection: instead of throwing exceptions, it would silently just clear the session and re-run the request.  For most sensitive operations (e.g. those which require a signed in user), this would force a signout and then any potentially damaging operation would be averted.


Here’s the [relevant code in Rails 2.3.11](https://github.com/rails/rails/blob/b0c3d451a242b53c9992cafa9108d0df52b4f2f0/actionpack/lib/action_controller/request_forgery_protection.rb):


Versus the [relevant code in Rails 2.3.10](https://github.com/rails/rails/blob/v2.3.10/actionpack/lib/action_controller/request_forgery_protection.rb) (sidenote: you can see all of this easily in Github because Rails is diligent about tagging releases, a practice you should certainly follow in your own development):


And, sure enough, checking Subversion showed that I upgraded the version of Rails I was using in January of this year in response to [this security advisory](http://weblog.rubyonrails.org/2011/2/8/csrf-protection-bypass-in-ruby-on-rails). I read that, made the required modifications to my application, tested, and had no problems.


## So What Went Wrong Then?


After I was sure that sessions were being reset (but only in production), I added a bit of instrumentation to the live site to record the session ID for people coming from my IP address and to log when it changed. This let me find the culprit: a bit of Javascript that A/Bingo, my A/B testing library, uses to verify that people are human. It assumes that robots generally won’t run Javascript engines capable of doing POST requests, so it does an ajax-y POST to my server to assert humanity of the end-user, thus keeping almost all bots out of my stats.


That code has been live over a year. Why did it suddenly start causing session resets? Oh, another change in the 2.3.11 upgrade:


The old code:


Notice that request.xhr? will cause this request to be verified if it evaluates to true, regardless of the other things in the OR statements. request.xhr? tests whether a request is ajax-y in nature. A/Bingo’s humanity-verifying POST is, so it didn’t trigger the CSRF check.


The new code, however:


Yep, as announced in the patch notes, we lost the exemption for XHR requests. So the A/Bingo mark_human request will, because it makes no particular effort to include a CSRF token (which I will be changing very quickly, as A/Bingo is my project), with certainty cause the CSRF check to fail in 2.3.11. This will result in not a noisy exception (the previous behavior) but instead a silent reset followed by re-running the action. A/Bingo, which doesn’t care a whit whether you’re logged in, will then mark your freshly new session as human. If the previous contents of your session mattered, for example to keep you signed in, they are now gone. A/Bingo will not reaudit your humanity, though, because your session now marks you as human, so this will only ever happen to your browser once.


## Race Conditions: Not Just In Java Thread Programming


So why did this never show up in development and why did it show up only sporadically in production? Well, consider how a browser interprets a page presented to it: it first downloads the HTML, then downloads the assets, blocking when it discovers e.g. CSS or Javascript which alters the document. This means that Javascript very low on a page may never execute if someone above it blocks them until the user navigates away. (This is a pretty gross simplification of how multiple pieces of very complicated and often incompatible software do something very difficult. If you want details, read stuff by the people behind YSlow. They’re geniuses and taught me all that I successfully learned about this process.) Someone like, say, external analytics utilities loaded over the public Internet. My page includes a few such scripts, like Google Analytics and CrazyEgg. They are off in development to avoid polluting my stats.


This plus the lack of network latency means that, on development, a browser which sees a page that includes the humanity testing Javascript will almost certainly execute it. That will cause the session to be burned, once, on the first page load. Since my invariable workflow for manual testing is “Start with a new browser at the homepage or landing page, do stuff, make sure it works”, the order of execution is:

1. I load the front page or a landing page. The session is initialized to some value S1.
2. (A few milliseconds later.) The A/Bingo Javascript checks for my humanity, resetting the session to some new value S2.
3. I hit the registration or login button, and the site works as I expect it to.
4. Since the site knows I am human now, that never gets checked again, and the session never gets reset again.


In production though, the workflow could very well be:

1. The user arrives at the front page or landing page. The session is initialized to some value S1, including (say) their referrer information.
2. A bunch of Javascript starts loading ahead of the A/Bingo check.
3. The user, within one or two seconds (depending on network latency to those external scripts), either logs in or creates an account.
4. The browser never successfully executes the A/Bingo check.
5. The user arrives at their dashboard. When it is rendered, the server (robotically) decides it isn’t quite sure if they are human yet, and includes that Javascript again. (This behavior is *designed* because I was aware of the timing issue, I just didn’t realize how it would shake out with the 2.3.11 upgrade.
6. This time, the user ponders their dashboard enough for the A/Bingo Javascript to post successfully. This resets their session to some new value S2.
7. The user clicks anything on the page, and (because S2 doesn’t include their logged in user ID) gets taken to a login screen.
8. The user is now durably marked as human, so the A/Bingo check never fires again, preventing a second unceremonious logout.


This neatly explains the logged out users. How to explain the missing referrer information? Well, if the user is NOT very fast on the click on the first page, they’ll have their referrer cleared out of the session before they successfully signup. They’ll get marked as a human prior to creating their account, though, so they’ll never even notice the unceremonious logout. This is the behavior of the overwhelming bulk of new users, which is why the stats were getting comprehensively borked but almost no users thought to complain.


This difference in behavior based on the hidden interaction of two concurrent processes is called a race condition. Race conditions are why sane programmers don’t program with threads or, if they do, they use shared-nothing architecture and pass all communication between the threads through a message queue written by someone who knows what they are doing (if you have to ask, it isn’t you — seriously, multithreaded programming is hard). I haven’t seen a race condition in years, because the genre of web applications I write and their architectures makes me mostly immune to them. Well, I just got busted back to CS102. Sadly, the core lesson of CS102 hasn’t changed: reasoning through why race conditions happen is *very hard*.


## Saved By Unsophisticated Users, Sort Of


Users returning after the session naturally expired (2 weeks) would go through the dance again, potentially getting asked to log in twice. However, it took most of them enough time to have the human check prior to finding where the Sign In button was, so the percentage of users who actually visibly saw the bug was fairly small. (I’m guessing, from a quick heuristic run on my log files, that it was below 1% of accounts. That’s the optimistic way to say it. The pessimistic way is to say that this bug negatively affected the better part of a thousand people, and probably cost me sales from some of them.)


## Whose Fault Is This?


If my users are inconvenienced, it is my fault, always. I should have read the patch notes for 2.3.11 more diligently, to discover the very consequential line “In addition to altering the templates, an application’s javascript must be changed to send the token with Ajax requests.”, and I should have been more aware that there was a one-line Javascript method pulled in by a library (which I wrote, so that is no excuse) which was not automatically upgraded with the Rails helper methods.


I’m not sure if more diligent testing would have caught this. Race conditions are hard to diagnose, and while I might have caught it by including production levels of external Javascript in my development environment, the symptoms would only have been visible a fraction of the time anyhow, and in ways which didn’t visibly break the application most of the time. (Who checks their stats for the development version to make sure they’re sensible after implementing that function correctly the first time?)


What I really should have done about this is addressing it earlier, when I first got the inkling that there was some weird edge case which would cause a logged in user to become logged out. I futzed around with my configuration once or twice and saw the problem go away (because it was non-deterministic), but rather than futzing I should have figured out a complicated but reducible series of steps that would always cause the issue. That would have sent me down the right road for fixing it.


## So How Do You Address This


Immediate term, a one-line patch turns off CSRF protection for the A/Bingo mark_human action, preventing it from accidentally resetting the session.


I also added a note about this to the A/Bingo documentation. I’ll patch A/Bingo after I have enough brain cells left to do that in a way which won’t break anyone’s applications. After I patch A/Bingo, that work-around won’t be necessary.


## Why’d You Write This Post?


Because, after hours spelunking in Firebug, my codebase, and the innards of obsolete version of Rails to understand what was happening, I had to tell *somebody*. Some people have water coolers. I have the Internet. Hopefully, someone in this wide world will find this discussion useful.


If you’re wondering what the day-to-day life of an engineer is like or why it’s so dang hard some of the time, this might be a good example (of the pathological case — the typical case is writing boring code which solves boring problems, like laying out a 5×5 grid on a bingo card and randomizing the word order). Bingo Card Creator is not terribly complicated software when compared to most applications, but it sits on top of other pieces of code (Rails, the web server the browser, the TCP/IP stack, the underlying OS, the hardware on both ends, etc) which collectively are *orders of magnitude* more complicated than any physical artifact ever created by the human race.


Most of the time that complexity is abstracted away from both the user and the developer, both as blissfully ignorant of the layers below as an ant walking on an aircraft carrier is ignorant of the depth of the ocean. But when a problem bubbles up and writing it off to gremlins isn’t getting the job done, you have to start looking at the lower levels of abstraction. That is rather harder than dealing with just the higher levels of abstraction. (Joel Spolsky has an article about [this subject](http://www.joelonsoftware.com/articles/LeakyAbstractions.html).)
