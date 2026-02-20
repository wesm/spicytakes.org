---
title: "Deceptive AdSense Ads Worse Than Click Fraud"
date: 2007-09-20
url: https://www.kalzumeus.com/2007/09/20/deceptive-adsense-ads-worse-than-click-fraud/
slug: deceptive-adsense-ads-worse-than-click-fraud
word_count: 2279
---


Much has been written about the dangers posed by click fraud on the Google advertising products, and how Google has taken steps to address the problem.  Click fraud, however, is only one of the ways for webmasters to defraud advertisers of money.  I will detail another way in this post.  The technique is already widely known among webmasters who use AdSense (and, indeed, sometimes I wonder if Google doesn’t encourage it).  If you’re spending money on the Content Network, you also need to understand it so that you can cut your losses when appropriate.


A bit of back story: recently, I bumped by spending on the Content Network up by 30%, to the “several hundred dollars a month” range.  As you might imagine, at 9 cents a click (bingo cards aren’t the world’s most competitive niche) this means I was getting a virtual torrent of traffic.  During my daily check of the summary statistics (a habit I suggest you get into after major changes to AdWords — in normal operation once a week is fine), I noticed that my click-through rate (CTR) on the content campaign had skyrocketed from 1% to 15%.


*That couldn’t possibly be natural.*  Remember, an AdSense ad is, by definition, being shown to someone who is at least partially interested in something related to your product but has not expressed any interest in being sold to yet.  (Folks on Google frequently have expressed an interest with their search queries, such as *buy bingo card creator*, which is why CTRs are orders of magnitude higher there.)  As such, you should expect CTRs to be much lower than on AdWords ads — dropping from 8-10% for a really good AdWords ad to about .5-1% or so for AdSense on most sites.


However, site design can have a major influence on how effective a site’s ads are at getting clicked.  Google recognizes this and teaches some of the tricks to optimize the ads (which, after all, makes them money): [blend the ads into your site](https://www.google.com/adsense/support/bin/answer.py?answer=17957), [place the ads where they are likely to be clicked](https://www.google.com/adsense/support/bin/answer.py?answer=17954), etc.  However, they have an [anti-fraud policy](https://www.google.com/adsense/support/bin/answer.py?answer=48182&sourceid=aso&subid=ww-en-et-asblog_2007-06-05&medium=link) for sites which toe the line, because using certain techniques to get the ads clicked on results in non-interested surfers clicking them, and that costs advertisers money and drives them away from the service.


Since web pages are made to be scanned, anything that causes your eyes to be drawn toward an ad but away from its content causes your click-through rate to soar.  One previously common tactic, which is now banned, was to line up images with the advertisements in order to suggest to visitors that the links provided explanations for the images.  This resulted in [quadrupling CTRs](http://forums.digitalpoint.com/showthread.php?t=17104) for the ads.  Since the AdSense equation is


Revenue = (traffic) * (# of ad units) * (CTR) * (cost per click) * (percentage Google gives you)


that quadrupled revenues for participating webmasters.  I’m strongly tempted to say “unscrupulous webmasters”, because once the visitor realizes they’ve been had they’ll be on the back button without a second thought, costing the advertiser money without giving them any chance to pitch their products to an interested customer.  That is, of course, the entire point of the excercise.


So that is the old scam.  Here is the new hotness: using CSS and HTML, organize your website in the fairly typical sections-broken-by-heads style.  Then, optimize your CSS such that the section travels off the page, with the clipping at a common resolution (800×600 or 1024×768) happening in such a way as to cut off the legitimate content and thereby give your visitors the impression that *the ad is the content* promised in the section headings.


There are at least eight sites which are using this technique in the quite non-competitive bingo card niche.  I have taken a screenshot of one site which I thought was iconic.  (*Editor’s note: After first posting this, the author of that site got in touch with me and said the placement was accidental.  I have no particular reason to disbelieve him, as inspection of his other pages shows a variety of ad placements.  I’m afraid that accident doesn’t explain the other sites, though.  I am keeping the pictures up to demonstrate the general tactic, but have edited the remainder of this post to be less accusatory of his site in particular.*)  You really have to see it in [full-screen glory](https://images1.kalzumeus.com/blog-images/adsense-manipulation.gif) to appreciate the effect.  That screenshot is about 255kb and shows the site in default IE7, but if you wanted to be really devious you can use CSS hacks to make it work equally well in all browsers at once, using pixel perfect layouts and a bit of elbow grease.  I have obscured the “branding” of the site, and have obscured the ads of my competitors to avoid associating them with it.  (If you happen to be a competitor of mine, [drop me an email](http://www.bingocardcreator.com/support.htm) and I will happily give you my list of sites which are using these strategies, or you can make your own as described below.)


Here is a close up on the main content area of the page.  Again, you really should look at in in context — the actual CONTENT here is invisible until you scroll.  Unsophisticated visitors miss the distinction between the blended links and the advertisements (which happen to have quite similar titles) and click on the ads instead of the file links.  Click to see the expanded version.


Remember, the site does not actually **show** that content in the middle unless you scroll down to see it — and even with the content there, it is easy for an unsophisticated Internet user to click on the ads thinking they are getting the promised downloads.


*And click they do. * From my statistics, roughly 16% of the visitors of that page clicked on my one, single advertisement.  Given there were five advertisements, a click in my niche costs about a dime, and Google splits somewhere in the general neighborhood of 50-50 with webmasters, we can guestimate their revenue per thousand visitors using the above formula:


Revenue = 1000 * 5 * .16 * .1 * .5 = **$40 CPM**.  (Edit: The site owner suggests that he is earning $7.50 CPM for the site as a whole.  I don’t have access to his console, but I think my estimate is closer than his for pages which employ this technique.)


Sorting the list of the hundreds of advertisers I am paying, and ignoring ones for whom small numbers distort results, it seems like a more typical CPM for an honest advertiser in my niche is about $2.50.  So its fairly obvious why breaking the rules is so attractive — a single page with less than 1k impressions a day could generate something like $12,000 a year.


And when I say *generating*, I mean “taking it from the advertisers”.


Most business owners understand the economics of advertising a product, but a brief review for the peanut gallery: I sell a $25 product, of which $24 is profit.  (It helps to be in software, the gross margins are quite healthy.)  The primary goal of having a user visit my page is to get them into the free trial of the software, which convinces about 2.5% of them to convert (i.e. buy), getting me my $24.  Thus, it is rational for me to spend anything less than $24 * .025 = 60 cents (at the margin) to achieve one trial being downloaded.


I have reason to suspect, given a year of data, that the attractiveness of my website and sales proposition should convince about 22% of interested visitors to take the trial for a spin.  Given that clicks in my niche cost about 9 to 11 cents each, this gives me an average cost of about 36-43 cents per trial download (it bounces around on a daily basis).  As 43 is less than 60, that means I am mildly profitable, with not too much room for error (if my conversion rate decreases to 2% and my cost per trial rises a few pennies I’m not making money anymore).


**Bamboozling visitors to click on my ads hurts me more than errors ever could.**


When an unsophisticated Internet user clicks on the “Create Bingo Cards” link thinking “This is step #1 of the 3 step process this website is pitching to me”, and then they are suddenly whisked to my very visually distinct site, they figure “Uh oh, something went wrong”.  And they immediately click the Back Button, to try to fix the mistake.  (Many of them probably click on a different ad instead, a mistake which is frustrating for them and great news for both the publisher and Google.)  As a result, it wasn’t 22% of folks coming in from these ads who actually completed a trial download, no, it was about 2%.  Which means that I was paying approximately $50 to get a sale of a $25 product — I guess I can make the loss up on volume?


Oh, but it gets worse: Google is very, very smart about where they show your ads.  This is why they have a Content Score for the search network which prioritizes high CTR ads over low CTR ads: this maximizes money.  Google’s incentive is to maximize the number of clicks while minimizing the number of impressions,  because if they capture 100% of my budget then they want me out of the rotation ASAP so they can sell the inventory to another sucker advertiser.  This unholy, and I hope unintended, alliance of Google and the publishers using this trick sucked my budget dry within the first two hours of every day.  Google’s automated algorithms helpfully suggested I increase my spending by a factor of ten to compensate, so that instead of spending $15 a day to make $7.50 I would be spending $150 a day to make $75, for a monthly loss in the $2,000 range.


**That Certainly Sucks.  What Can I Do About It?**


1)  First, if you’re not in the position to routinely monitor your AdWords performance, opt out of the content network and don’t come back.  The scum sites are always one step ahead of Google, by definition, and if you’re not one step ahead of them that $2,000 a month loss could be yours.


2)  If you are in the position to routinely monitor your AdWords performance, use the Reporting feature in your AdWords console.  The report you want is Site Placement, for the previous 7 days.  Make sure you include the CTR and Cost Per Conversions columns.  Then, every day, grab your report in CSV format, and run a simple script on it to report all of the URLs where the CTR is higher than a threshold (I use 4%), the number of clicks is substantial (otherwise you’ll ban a lot of mom-and-pop sites for no good reason because 100% of their 1 visitors this month clicked your ad), and your Cost Per Conversion is greater than your profit.  (Almost guaranteed if you set your threshold right, because the only way to beat that threshold is to be exploiting your visitors, and exploited folks don’t make happy customers.)  Then, take any domain which appears on this screen, and add it to your banned list.


I am a Cygwin junkie so I do this with a gawk script every day, but if you are not a scripting wizard you can do it the longhand way, by increasing the number of rows in the visible report to 100, sorting by descending CTR (click it twice), and then visually identifying the rows that have significant number of clicks.  Then, take any domain which appears on this screen, and add it to your banned list.


3)  If you are an engineer or product manager at Google, please, we could use some algorithmic help here.  I realize this suggestion is going to cost you money in the shortrun, but when advertisers lose money you will eventually lose money too, because they will stop advertising.  We give you all the information you need to calculate our maximum desirable cost per conversion (I have my doubts that we are intelligent in doing this, because you can use that information to screw us over royally, but business is based on a foundation of trust and for the moment I’m going to trust you).  You should provide a setting (or make it default behavior!) that ads stop appearing on any site where they transparently won’t be profitable.  I would also suggest screening sustained abnormal CTRs automatically for fraud or Terms of Service violations.


4)  If you find a website which is abusive in their ad placement, you can complain to Google.  Realistically, I think they value algorithmic solutions over manual ones so much that you have zero hope of being heard (and they have to — they got to being a gazillion dollar company by NOT having to pay a human to deal with the little shrimp with the $15 a day advertising budget).  But if it makes you feel better, [here is the link](https://www.google.com/adsense/support/bin/request.py?search_ask=1&subtopic=&contact=report_violoation&main_topic=other&contact_type=11&contact_topic=Report+a+policy+violation&Action.Search=Continue).


[Note: This post has been edited, as the author of the pictured site disputes my characterization of it, and claims that the effect was accidental.  As I have no particular reason to disbelieve that, and his other pages do not appear to be exploitative, I’m giving him the benefit of the doubt and have edited this post to remove accusations directed at his site specifically.  The technique, however, is being used by multiple sites and it strains credulity to think that eight people independently accidentally developed cross-browser compliant CSS and liquid layouts to achieve this effect.]
