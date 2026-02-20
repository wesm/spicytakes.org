---
title: "Dropbox-style Two-sided Sharing Incentives"
date: 2010-04-28
url: https://www.kalzumeus.com/2010/04/28/dropbox-style-two-sided-sharing-incentives/
slug: dropbox-style-two-sided-sharing-incentives
word_count: 2076
---


Last weekend, among a whole schedule of other great presentations at the [Startup Lessons Learned conference](http://www.sllconf.com/) (you can watch the video [here](http://blog.kevindonaldson.me/summary-of-startup-lessons-learned-conference-0)), the folks behind [Dropbox](http://www.dropbox.com) had a [presentation](http://www.slideshare.net/gueste94e4c/dropbox-startup-lessons-learned-3836587) ([video](http://blog.kevindonaldson.me/summary-of-startup-lessons-learned-conference-0)) about how they went about growing their business.  Apparently search ads were too expensive for them (due to bidding up by other venture-funded firms in their space) and the long tail of search was not panning out, but their referral program worked out really well for them.  Really, really superflously well for them.


(For those who haven’t used it, Dropbox is absurdly well-implemented file storage, backup, and sharing in the clooooooooooooud.  They have saved my life twice when hard drives died and save me hours of time schlepping files from my Windows PC to my Ubuntu box and back again.  Go try them out if you haven’t already — I can’t imagine not having them anymore.  Anyhow: the business model is “We’ll give you 2 GB of space for free, or you pay us to get more than that.”)


The biggest single thing about their referral program is that it has a two-sided incentive for sharing: the person who signs up for Dropbox through your referral link gets a better deal than they would have gotten from the homepage, **and** you also get a free bonus yourself.  That is marvelous, marvelous psychology there: it gives both parties a benefit so the email seems less like spam, and social relations being what they are, the person receiving the gift feels a wee bit obligated to accept it.  (This same dynamic is used by many of the social gaming companies on Facebook, to degrees which almost make me feel icky.)


This works great for Dropbox because they have a product which they can easily make more useful in a granular fashion: just add more space and stir.  The cost of the marginal space is truly miniscule as a cost of customer acquisition: a few pennies a month if the user actually fills it, and most will not.  However, the passionate freebie seeking techies in the audience will use their disproportionate-sized online megaphones to scrape another few gigs out of their account.


The more I thought about it, the more impressed with this idea I was.  I had considered and rejected “Tell a friend” as a marketing scheme for BCC a few years back, on the theory that it just creates more spam and few of my customers would use it, but the double-sided incentive addresses both of those issues for me.  Plus I thought I could potentially implement it very quickly.  (I had a funny idea for a minimum viable tell-a-friend page: just ask for the friend’s email address and then have it ping me when someone submits anything.  I’d send the emails and credit both users manually.  That would have taken my development time from about six hours to one hour, but I decided to do it the “right way” on the theory that a few hours isn’t much of a risk to me anymore.)


So I decided to test out a version of this for Bingo Card Creator.  Historically, I have given free trial users 15 bingo cards for free.  (This neatly segments my markets between parents, who very rarely have 16 children, and teachers and professional users, who rarely play bingo with under a dozen players.)  I’m allowing them to invite friends: each successful invite gives both parties 3 extra cards, with a cap at 12 gained from inviting.  This theoretically will allow a large portion of my core customer base to get their program for free, but I think that paying is ridiculously more efficient for most of them, so it will only be the truly inveterate skinflints who sign up four of their closest friends so that they can get 27 cards for class.


The cost of allowing users to print extra bingo cards is, of course, too low to measure.


## This Feature Is Surprisingly Hard


I’m used to pushing changes which only require ten lines of code, but this feature was a monster:

- Tell a friend page
- Processing email addresses put into that form
- Actually sending emails
- Facebook sharing integration
- Customized signup page
- I-Can’t-Believe-They’re-Not-Affiliate URLs
- Properly crediting people for signups
- Anti-abuse measures (mostly making it so that folks can’t use it to spam)
- Minimum viable stats tracking (no charts yet)


All in all, it took a solid day.


I’m really pleased with a couple of implementation choices:


**Getting the user’s first name**:


My gut feeling (yeah yeah, A/B test incoming) is that users will be overwhelmingly more likely to respond to an invitation from Jane than from jsmith@example.com or from “a friend.”  So I asked customers to provide it if they haven’t already.  It is totally optional but I’m thinking they’re overwhelmingly going to comply.


**Highlighting the offer on the signup page:**


I hit the social proof fairly hard on the signup page: mentioning again that Bob or whomever sent the invitation, and that both Bob and the user will benefit from accepting the offer.  This page could stand to be a lot prettier, and I could probably throw a testimonial in here somewhere…  In this example, our generous inviting user’s name is Bingo.


**Facebook integration**:


Recently, having spent far too much of my time playing Facebook games (market research, I swear!) and scouting out the ecosystem more, I’ve noticed something.  One, a quarter of the female members of my family aged 30+ are currently sheering sheep, planting pumpkins, or throwing pigs at each other.  Two, my friends seem to comment on things they share… *a lot*.  Whoa.  This whole Facebook thing might actually have legs.


It turns out that getting folks to share links on Facebook is child’s play: [one line of code](http://www.facebook.com/facebook-widgets/share.php) that you can copy/paste.  With a [bit more work](http://wiki.developers.facebook.com/index.php/Facebook_Share/Specifying_Meta_Tags), you can customize the text Facebook will pull out of the page.  I customized the text to include a strong call to action with added social proof, naturally.  **Facebook sharing: not just for blog posts.**


**
 **


One feature that I particularly like about the Facebook option is that it only requires two mouse clicks from users (one to open, one to confirm — assuming they’re already cookied on FB), and it** doesn’t require them to understand or recall email addresses**.  My users have enough problems remembering and managing their own email addresses — I don’t want to include a “look up Anne’s email address” step in the workflow.


**Finding folks when they’re ready:**


Here’s an idea ripped straight off of the better Facebook games: give folks an opportunity to share stuff right when they hit the wall.  (Well, most of the Facebook games artificially construct the wall such that you have to share to get around it…  but I’m not that tricky.)  For example, if someone wants to print 22 cards and only has 15 quota, that would be a great time to remind them of the incentive.


## Metrics Tracking


At the moment I put in very, very basic stats tracking:

- Who ever accessed the invite page.
- Who sent invites via email, and how many.
- How many folks signed up as a result of invites.  (No source tracking, but GA should show me that, easily — referrer is Facebook, etc.)
- Daily counts of all of the above.
- As you could probably have guessed, I turned this on via an [A/B test](http://www.bingocardcreator.com/abingo) and will be watching to see if it hurts conversion to purchases.  (This is just a first cut, since it is possible that shaving 10% off sales from inviters would be worth getting the invitees, if invitees turn out to convert well.)
- I’ve laid the groundwork for tracking the viral coefficient, although I strongly, strongly suspect it will be far below 1.  (I am not promoting this very aggressively, at all.)


## Future Directions


In addition to the obvious (testing to see if this actually works), I have a few ideas for how to improve this in the future.


One obvious thing which I will probably not do is to ask folks for their webmail login details, grab their contact lists, and assist them in selecting folks to receive emails.  That would be stupidly effective, but it teaches bad Internet practices (do **not** give your Gmail details to random websites!) and frankly I don’t want it to be *that* easy to send invites.  We’ve all got that one aunt who has not figured out netiquette for Farmville and sends 14 lost kittens a day: I do not want to be her enabler.


I’ll probably also work on placement of the offer to invite, copy on the invite page, invite email, and invitation signup page (including graphical design), and will do some much more sophisticated metrics on this if early results look promising.


## Will It Work?


Your guess is as good as mine.  In favor of it working, most of my customers and many of my trial users are very thrilled with Bingo Card Creator.  Many of them have figured out how to share it with friends despite me not giving them any good way to do so (not a trivial thing for elementary school English teachers — one bragged to me that she found out how to make a link to the website on her desktop and then bring it to her sister on a floppy, and if they’re getting over barriers to conversion *that* high, you know there must be something going on).  There is also the natural penny-pinching nature of teachers operating in my favor — the fact that the program is not free is far and away my #1 user complaint — and the fact that they tend to travel in packs.


In favor of the idea not working out so well: these are not very plugged in people as compared to Dropbox’s early adopter userbase, the actual mechanics of sharing still require non-trivial technical expertise (understanding email addresses and knowing those of your friends, for the option I’m giving highest billing to), and there are non-trivial business risks if it either becomes too popular or if folks feel that the invitation emails are an imposition.


Speaking of which: I capped the number of invites I’ll send out per user at 5 (hard-capped at the moment), capped the number of invitations any individual will receive at 1, and have capped the system at a total of 500 a day until I have some idea of how many is safe to send.


**Bug of the Year Award**:


It is early, but I think this already won it: a poorly considered after_save callback on my user model caused users’ mailing list settings at MailChimp to be updated if their user record was updated.  That was previously desirable, since there was nothing in the user model which could be updated without touching either their email address or their mailing list settings, and all updates were at the user’s personal request.  However, when I put the users’ card limit in there, then updated that for 50,000 users to set it to the default value, the callback fired and suddenly I got about 30,000 Delayed jobs all waiting to ping MailChimp.  I was ignorant of this until — thank God for checklists — I was testing the deploy and found out that I could not print bingo cards.  I assumed I had botched the Delayed Job worker processes again, but no, they were up… and right after I confirmed that I got the email saying “Delayed Job has spiked to 30,000 jobs in the queue!”


As soon as I realized what had happened I hit the Big Red Button on DJ, but not before a few thousand of them had been processed.  For users who had actually confirmed the signup to the mailing list before, I don’t think anything bad happened.  For those who had second thoughts before double-optin, they were all hit with another email from MailChimp on my behalf, seemingly out of the blue.  I’ve now got an inbox of “Who are you and why are you spamming me?” to deal with.  *sigh*


On the plate for tomorrow: figure out how I could have seen this one coming.  My testing and staging environments simply ignore API calls to MailChimp for the obvious reason — I wonder if I should have them throw exceptions instead unless they’re explicitly expected behavior.
