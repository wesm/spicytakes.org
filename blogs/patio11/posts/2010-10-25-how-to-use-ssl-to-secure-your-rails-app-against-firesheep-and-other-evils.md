---
title: "How To Use SSL To Secure Your Rails App Against FireSheep And Other Evils"
date: 2010-10-25
url: https://www.kalzumeus.com/2010/10/25/how-to-use-ssl-to-secure-your-rails-app-against-firesheep-and-other-evils/
slug: how-to-use-ssl-to-secure-your-rails-app-against-firesheep-and-other-evils
word_count: 1319
---


The post on Hacker News today about [FireSheep](http://codebutler.com/firesheep), a Firefox addon which lets you trivially compromise the web application cookies/sessions of anyone on the same wireless network, gave me the much-needed impetus to upgrade my business to SSL security.  For the last several years, I haven’t encrypted traffic between the server and the user.  My theory was that my customer’s didn’t store anything security critical in their elementary school bingo card games, but the increasing amount of information available to the admin (me) plus a customer support story from this morning convinced me that compromise would be a Very Bad Thing.


**Implementing SSL in Rails was very painful** and resulted in my site being down or unusable for a large portion of my customers for much of the day.  (If I were doing it again, I would have paid the extra few bucks to set up a staging environment with its own certificate and verified everything worked on that prior to trying to fight my way through the process.) Luckily, since I am time-shifted from them by over 12 hours, few noticed.  In the interests of saving you and your customers some difficulty, I thought I would write up what I learned.


## What You Need Before You Get Started

1. A SSL certificate from a certificate authority which is trusted by the major browsers.  [GoDaddy](http://www.godaddy.com/ssl) sells them for $12.99 and they are perfectly adequate.
2. [SslRequirement](http://github.com/rails/ssl_requirement) and [AssetHostingWithMinimalSsl](http://github.com/dhh/asset-hosting-with-minimum-ssl), both plugins by DHH.
3. Rails to be fronted by Nginx.  The explanation for Apache is similar but the magic server configuration is different. (If you use Nginx+Passenger, can skip the Mongrel-specific bit below.)


## Nginx configuration


Nginx manages configurations on a per-server basis, and cannot have a single server declaration listen to both HTTP and HTTPS requests. We’re going to get around having to copy/paste our entire configuration (and maintain it in two places) by DRYing it into a single external snippet, then including it twice.


Right now, your Nginx config looks something like this:


Cut everything out of the server declaration (yes, everything) and externalize it into a separate file. It should now look like:


You can now create a separate declaration for your SSL server without causing much overlap:


I remember setting up the SSL certificate to be more of a nuisance than a difficulty, but if not, you can find [very detailed instructions](http://hostingfu.com/article/godaddy-turbossl-certificate-nginx) online.


Now, **if you are using Mongrel**, you need to do one more thing: withing EverythingJustCut.conf, you’ve got to find the place where Nginx is proxying to Mongrel and have Nginx set the X_FORWARDED_PROTO to https for HTTPS requests. This is the one and only signal that Rails, running on Mongrel, is going to get that a particular request is for SSL or not. This is trivial to do if you know you have to do it: just find all your existing proxy_set_header statements and add this after them:


## Very Carefully Scrub Your Website For Absolute URLs


Absolute URLs containing the scheme (i.e. anything starting with http:// ) are dangerous to your application, because if your page transmitted over HTTPS references a “certain type of resource” on HTTP, your browser may display a Scary Error Message to your users. Unhappily, the browsers get to pick what constitutes a security-critical resource.


The general rules for maintaining SSL security on HTTPS pages are:

- **Javascript files**: must always be loaded from HTTPS
- **Image files**: must always be loaded from HTTPS, **except** for Firefox and Safari
- **CSS files**: must always be loaded from HTTPS, **except** for Safari
- **other files**: may or may not be loaded from HTTPS


Do you think you’re going to remember that? Yeah, me neither. Hence, you don’t want any hardcoded http:// anywhere. Let Rails take care of it for you with AssetHostingWithMinimalSsl: all you have to do is be consistent about always loading e.g. images through the image_tag or image_path helper, CSS and Javascript through their associated helpers, etc, and you will always get the proper behavior. The tough part is that you’re going to have to take IE and drive through every page on your site verifying that it does not accidentally include a resource transmitted in the clear.


The configuration for AssetHostingWithMinimalSsl goes in your config/environments/production.rb file and is trivial:


Note that it is **very easy** to miss a http:// URL hidden in a CSS file, Javascript file, or analytics-package JS include somewhere. If you do that, even in an unused CSS selector, you will cause the browser to throw Big Scary Errors. Test that you have gotten everything **very thoroughly** prior to proceeding.


## Require SSL for Any Security Sensitive Actions


Why are we requiring SSL? To prevent against an attack where the bad guy can sniff the cookie out of there air, thereby appropriating it for himself and logging in as the logged-in user (either by compromising a session ID or, in Rails, compromising the user_id you probably stored in the tamper-proof CookieStore). So what do we have to SSL? Everything Rails sends or accepts a session cookie with. What is that? **Everything** that an actual browser can access. (If you are, like me, in the unenviable situation where some URLs are going to be hit by user agents which cannot support either HTTPS or cookies, don’t forget that requiring SSL for all actions won’t help you.)


The SslRequirement plugin makes it easier to do this sitewide than it otherwise would be:


This sets it so that SSL is required when we say it is in production only, and in other environments the statements which set up SSL requirements are merely silently ignored. Those functions are:

- **ssl_required**: takes a list of :symbols representing action names to require SSL for. Should be nearly all of your actions. If someone tries to access one of these actions over HTTP, they will be redirected to HTTPS (+).
- **ssl_allowed**: takes a list of :symbols representing action names to allow SSL for. If they aren’t required and aren’t allowed, then they’ll be redirected to HTTP if they try getting to this action over HTTPS.


You set them in each controller, on a per controller basis. There does not appear to be a handy mass assignment option like :all for this method, unlike most of the before_filter and similar things you find in Rails.


Note there is a subtlety here: if you let Rails share a session cookie over both HTTP and HTTPS, then if it is ever used over HTTP, byebye cookie security. This means you can either be very, very careful that you never let anyone access Rails actions over HTTP (and you pray a malicious attacker never tricks your users into clicking to a **valid link to your website**), or you ban your session cookie from being sent over HTTP at all:


This option will **probably break your site**, possibly subtly, the first time you switch it on. Test thoroughly. I haven’t got it 100% working for myself yet.


## Host downloadable files on SSL? You just broke IE.


After several hours of frustration, failing my way forward, and finally getting things working on Chrome/Firefox, I received a bug report from an IE using customer who couldn’t download her bingo cards. Some deep Googling revealed that IE, for architectural reasons known only to the IE team, does not play well with downloadable files over SSL unless you set some very specific headers:


Note I am using X-Accel-Redirect to have the file served directly through Nginx, rather than through Mongrel, as described [here](http://kovyrin.net/2006/11/01/nginx-x-accel-redirect-php-rails/).


## Conclusion


I hope that saved you and your customers some pain and insecurity. If you haven’t done this yet, and I think there are many Rails apps as open to exploitation as I was until this afternoon, I suggest you download FireSheep and see how quickly any idiot with wireless can compromise your admin session. Then, **fix this** as soon as possible.
