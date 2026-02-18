---
title: "How I set up an automatic weekly blog digest"
date: 2017-12-28
url: https://jvns.ca/blog/2017/12/28/making-a-weekly-newsletter/
slug: making-a-weekly-newsletter
word_count: 683
---


Earlier this year someone asked me why my blog didn’t have an email newsletter. My instinctive
reaction was “I don’t have time to do that every week!! I won’t remember!”. But then I realized that
I could **automatically** generate a weekly blog digest! Now I’ve had it for ~6 months
([https://jvns.ca/newsletter)](https://jvns.ca/newsletter)).


The weekly digest has turned out to be a cool easy thing so I wanted to talk about how it works!


### Why send out blog posts by email?


I was confused at first about why people were asking me for an email newsletter – I use an RSS
reader, and I don’t **want** blog posts emailed me to me. But of course, lots of people do not use
RSS readers, but they still want to keep up with the blogs they read! That makes sense!


So I decided to try automatically generating a weekly digest of my blog every week with the contents
of all the blog posts I wrote the previous week.


As of today, apparently 1050 people have signed up to get weekly blog updates by email (thanks! ❤). So
apparently this really is a useful thing!


### How the weekly digest works


I’ve used Mailchimp for email newsletters before, so I used Mailchimp to set it up. I use their free
version. (which I can use until I get to 2000 subscribers)
Setting it up was really simple (I used [these directions](https://kb.mailchimp.com/campaigns/blog-posts-in-campaigns/share-your-blog-posts-with-mailchimp))!
I just had to:

- create a new campaign
- type in my RSS feed address ([https://jvns.ca/atom.xml](https://jvns.ca/atom.xml))
- set up a template
- done!


The newsletter gets sent on Thursday every week and I don’t have to do anything! Nice!


### coding a template manually: totally worth it


Mailchimp has a lot of pretty email templates you can use. I got frustrated with these
templates last week – it was displaying in a weird way in my email, and I didn’t think all the
fancy CSS they were using in their template was really adding anything.


So I made a new template manually to create weekly blog digests! Here’s the HTML for the template.
Basically it just loops over all blog posts from that week and includes each one in the email.


You might notice that there’s no unsubscribe link in the template – Mailchimp adds that
automatically at the end, which is nice.


```
<p>

Hello! Welcome to Julia's blog digest for the week.
Here are the blog posts I wrote this week! I'm
always interested to hear what you think at
<a href="https://twitter.com/@b0rk">@b0rk</a> on
Twitter.

</p>

<p>
A list of just the links:
</p>

<p>
   *|RSSITEMS:|* <span style="color: #ff5e00"> ★ </span>
   <a href="*|RSSITEM:URL|*">*|RSSITEM:TITLE|*</a> <br>
   *|END:RSSITEMS|*
</p>

And the full content of all the posts, if you want to 
read everything in this email:

*|RSSITEMS:|*
<h2> <a href="*|RSSITEM:URL|*">*|RSSITEM:TITLE|*</a> </h2>

*|RSSITEM:CONTENT_FULL|*

<hr>

*|END:RSSITEMS|*

```


Here’s what it came out looking like in my inbox. I thought it looked really normal and simple and
good!


You might notice that I include the full content of the post in the email. This is because one of my
pet peeves is blogs which don’t include the full content of their posts in their RSS feeds – I end
up subscribing to those blogs but then not actually reading them.


### weird bugs


For all of July no newsletters got sent out because I hit a limit on Mailchimp’s free plan and
didn’t notice (they have a limit on total subscribers to all your campaigns) so they stopped
sending it. Oops! I deleted some old mailing lists I wasn’t using and they started again.


I subscribe to the newsletter myself which helps me notice/debug problems like this – it took me 6
weeks to notice that I wasn’t getting newsletters anymore, but eventually I noticed and fixed it!


### that’s all!


If you have a blog and you also want to create a newsletter from your RSS feed maybe this will be
useful to you! I really like that it’s a simple transparent opt-in thing (nobody gets email who
doesn’t want it!) and that people seem to find it useful!
