---
title: "Moved Blog From WordPress.com to Own Server"
date: 2009-02-27
url: https://www.kalzumeus.com/2009/02/27/moved-blog-from-wordpresscom-to-own-server/
slug: moved-blog-from-wordpresscom-to-own-server
word_count: 419
---


Hideho everybody.  Two years after getting the notion to do it, I have finally completed the move of my blog to my own server.  The main reasons is to make me the captain of the blog’s destiny, as opposed to WordPress.  (Non-poetic version: I want to manage my own plugins, themes, and general look for the site — particularly important as my business expands and I might use this for something other than just writing about BCC.)


Process to move a blog from WordPress.com to your own server:


1)  Register domain name


2)  Go to WordPress.com and set your blog’s domain as the one you’ve just registered.  This will cost you $10 a year.


3)  Wait several months while Google gradually gets the notion that yourblog.wordpress.com is really www.yourdomain.com (WordPress will 301 redirect to your new domain IF AND ONLY IF you continue paying them the $10 a year — its a steal, do it).


4)  At your hosting provider of choice, install the WordPress software.  You’ll probably want to configure it under a test subdomain for the moment (I used a domain I keep lying around for just such an occasion).


5)  From WordPress.com, export a dump of all your posts & etc.


6)  Import the dump into your self-hosted blog.  If your blog export was over 2 MB (mine weighed in at 2.1), you can have the import succeed by finding your php.ini file and changing the max_upload_size setting line — it should read “max_upload_size = 10MB;”


7)  Test blog, see that most stuff continues to work.


8)  Go to your domain registrar and change the DNS entries for your domain from ns1.wordpress.com, etc, to the DNS entries for your hosting provider.  Wait a few minutes.


9)  Turn on Akismet for your new blog or you’ll be spam city before you know it.  I got 50 lovely comments welcoming me to my new digs within the first 15 minutes.  They all seemed to be by people who work in the pharmaceutical industry.


And, of course, you can play around with your settings, themes, plugins, and etc.  I’ve gone ahead and used the Leviathan theme (customized very mildly with a custom title image — 5 minutes in Paint.NET, will probably replace it with a real image done by my art guy later) and installed a plugin to finally allow me to do some decent syntax highlighting here.  Hopefully that will induce me to post code more often.


Tell me if you notice anything greviously wrong about the blog!
