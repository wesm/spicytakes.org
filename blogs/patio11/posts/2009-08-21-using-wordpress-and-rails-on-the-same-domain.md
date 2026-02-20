---
title: "Using WordPress and Rails on the Same Domain"
date: 2009-08-21
url: https://www.kalzumeus.com/2009/08/22/using-wordpress-and-rails-on-the-same-domain/
slug: using-wordpress-and-rails-on-the-same-domain
word_count: 652
---


I finally got serious about putting [a blog](http://www.bingocardcreator.com/blog/) on the Bingo Card Creator site today.  Since Bingo Card Creator is powered by Rails, ideally I’d be using a Rails blog platform, but frankly, they’re all vastly inferior to WordPress.  I could have slapped up a WordPress blog on a subdomain and called it a day, but I always advise people to put blogs on subdirectories for SEO reasons, so I thought I’d do it properly.


**It is easy to bork this** setup if you don’t understand WordPress and Nginx configuration files.  Make backups of all server config before you start modifying them.


## Extracting a WordPress Theme from your Rails App


If you’re not a PHP-speaking web designer, this step can take a lot of time.  Or, alternatively, you can just pay $10 and use [ThemesPress](http://www.themespress.com/).  They have a web-app where you copy/paste in some HTML and CSS and they spit out a widget-enabled WordPress theme for you for $10.  This is **well worth your time**.

1. Look at your main CSS file.  Identify any images which have relative URLs.  Replace them with absolute URLs.  This will save you from having to upload the images to ThemesPress to see the preview, and besides, you should be doing this anyhow for static assets so that you can serve them from images{1,2,3}.example.com and speed up page loading.
2. Load the main page for your site.  Click view source.  Strip out the place where Rails loads your CSS.  Replace your sidebar contents with **{SIDEBAR}**.  Replace your main body contents with **{CONTENT}**.  Replace any relative URLs to images with absolute URLs as in step #1.  Save this file for a second.
3. Go over to ThemePress, skip the image uploading step, and follow the onscreen directions.
4. Pay them their $10.  Bwahaha, you now have a WordPress theme for your Rails app.


## Set WordPress Up At A Private URL

1. I find the easiest way to do this is to create a new subdomain (blog.example.com, for example) and have Apache listen to requests on a non-standard port.  If you’re not paranoid about other people seeing your work in progress, you can put it on port 80 like usual.  I suggest not using a private IP at this stage, as you’ll find it difficult to diagnose problems in your browser until you get to the Nginx config step.
2. Install WordPress like you normally would.
3. Verify that the theme you created works well, make a post, etc.
4. Go to WordPress Settings and change the Blog URL to be your final blog URL.  For example, http://www.example.com/blog rather than blog.example.com.  That URL won’t work right now.  Don’t worry, we’ll fix it.


## Tweak Nginx Settings So That It Reverse Proxies Your Blog

1. I could discuss the rationale for these [settings](http://pastie.org/591348) a bit more, but they are a bit quirky.  If you copy/paste them, they should mostly work.  Good enough, right?
2. Restart Nginx.
3. Verify that you can access your main blog page and your admin page.  **Do not proceed without doing this.**


## Change Your WordPress Settings

- WordPress has two URLs listed in settings, one WordPress URL and one Blog URL.  Your WordPress URL still reads something like blog.example.com.  Since Nginx is now set up properly, go ahead and change that to http://www.example.com/blog/ , like your blog URL.
- You now have NO need to publicly access the WordPress server, since the only user who will ever see it is Nginx, while proxying for you.  You can go ahead and move it to a private IP.  This will mean Google doesn’t come along and access blog.example.com by accident, then think “Hey, he is stealing content from himself.


There you have it, one blog on your Rails app!  Now start writing.


P.S. Don’t forget to tweak your Rails templates to, you know, link to the blog like a first class citizen of your website.
